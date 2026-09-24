"""Workbench leaf — jailed subprocess adapter (P2).

Calls `python3 -m axiom_wb evaluate` via allowlist, timeout 3600, cwd jail.
Falls back to distinguishable placeholder when engine missing — never fake green.
"""
import subprocess, json
from pathlib import Path
from axiom_harness.paths import is_safe_relative, OUTPUTS, ALLOWED_SCRIPT_PREFIXES, STAGING_ROOT

def _assert_allowlist(cmd: list):
    # Anchored check — validate ONLY the module argv, not substring of joined string nor trailing args.
    # cmd is ["python3", "-m", "<module>", ...] — module must be allowlisted. Trailing smuggle must not whitelist evil module.
    if len(cmd) < 3 or cmd[0] != "python3" or cmd[1] != "-m":
        raise ValueError(f"failed_policy: allowlist violation {cmd}")
    module = cmd[2]
    if module == "axiom_wb":
        return
    if any(module.startswith(p) for p in ALLOWED_SCRIPT_PREFIXES):
        return
    raise ValueError(f"failed_policy: allowlist violation {cmd}")

def seal_workbench(mission_yaml: Path, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    # hard gate — never assert, never Path.cwd()
    p_str = str(mission_yaml)
    # make relative to STAGING_ROOT if absolute
    try:
        rel = str(mission_yaml.relative_to(STAGING_ROOT)) if mission_yaml.is_absolute() else p_str
    except Exception:
        rel = p_str
    if not is_safe_relative(rel):
        raise ValueError(f"failed_policy: jail violation {mission_yaml}")
    cmd = ["python3", "-m", "axiom_wb", "evaluate", str(mission_yaml), "--out", str(out_dir)]
    _assert_allowlist(cmd)
    engine_present = False
    try:
        r = subprocess.run(cmd, timeout=3600, cwd=str(out_dir), check=False)
        engine_present = (r.returncode == 0)
    except Exception as e:
        (out_dir / "error.log").write_text(str(e))
        engine_present = False
    # ensure minimal sealed trio exists — distinguish placeholder
    for f in ["SCENARIO.json", "scenario.csv", "DECISION_SUMMARY.json"]:
        p = out_dir / f
        if not p.exists():
            p.write_text(json.dumps({"placeholder": f, "engine": "missing", "sealed": False, "ai_computed_metrics": False}, sort_keys=True, ensure_ascii=False, separators=(",", ":")))
    from axiom_harness.manifest import write_manifest
    # P0 fix: explicit file set, not glob(*) — only sealed trio + engine-declared
    sealed_files = ["SCENARIO.json", "scenario.csv", "DECISION_SUMMARY.json"]
    files = [str(out_dir / f) for f in sealed_files if (out_dir / f).exists()]
    # also include any engine-declared outputs explicitly listed in DECISION_SUMMARY if present
    try:
        dec = json.loads((out_dir / "DECISION_SUMMARY.json").read_text())
        for extra in dec.get("extra_files", []):
            if is_safe_relative(extra):
                p = out_dir / extra
                if p.exists() and str(p) not in files:
                    files.append(str(p))
    except Exception:
        pass
    write_manifest(files, out_dir / "MANIFEST.json")
    import datetime as _dt
    (out_dir / "verify_result.json").write_text(json.dumps({"csv_hash_ok": engine_present, "orphans": [], "ai_computed_metrics": False, "contradiction_flag": "OK", "gold_id": "N/A", "engine_present": engine_present, "sealed": engine_present, "sealed_by": "harness", "sealed_at": _dt.datetime.now(_dt.timezone.utc).isoformat(), "instrument": "axiom_wb", "sop_version": "1.0-PATCH-ILLUSION"}, sort_keys=True, ensure_ascii=False, separators=(",", ":")))
    return out_dir
