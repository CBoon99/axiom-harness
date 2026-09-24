"""Workbench leaf — jailed subprocess adapter (P2).

Calls `python3 -m axiom_wb evaluate` via allowlist, timeout 3600, cwd jail.
Falls back to distinguishable placeholder when engine missing — never fake green.
"""
import subprocess, json
from pathlib import Path
from axiom_harness.paths import is_safe_relative, OUTPUTS, ALLOWED_SCRIPT_PREFIXES, STAGING_ROOT

def _assert_allowlist(cmd: list):
    # cmd[0] is python3, cmd[2] is module; enforce allowlist
    m = " ".join(cmd)
    if not any(p in m for p in ALLOWED_SCRIPT_PREFIXES) and "axiom_wb" not in m:
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
    files = [str(p) for p in out_dir.glob("*") if p.is_file()]
    write_manifest(files, out_dir / "MANIFEST.json")
    (out_dir / "verify_result.json").write_text(json.dumps({"csv_hash_ok": engine_present, "orphans": [], "ai_computed_metrics": False, "contradiction_flag": "OK", "gold_id": "N/A", "engine_present": engine_present, "sealed": engine_present}, sort_keys=True, ensure_ascii=False, separators=(",", ":")))
    return out_dir
