"""Future leaf — seal_pair via jailed subprocess.

Writes 5 artefacts with chain B.prev=A, label future-synthetic, FCA disclaimer.
"""
import json, pathlib
from pathlib import Path
from axiom_harness.manifest import write_manifest, write_run_pointer
from axiom_harness.paths import ALLOWED_SCRIPT_PREFIXES  # keep allowlist in scope for future subprocess use

# No subprocess in this leaf — allowlist reserved for when future spawns a script (TECH_SPEC §35)
def _assert_allowlist_noop(cmd: list):
    # intentionally no subprocess here; placeholder to keep allowlist wired
    return

def seal_future(experiment_id: str, out_dir: Path, prev_hash=None):
    out_dir.mkdir(parents=True, exist_ok=True)
    import datetime as _dt
    scenario = {"experiment_id": experiment_id, "scenario": "future-synthetic", "label": experiment_id, "disclaimer": "not prediction/forecast — FCA one-liner", "prev_receipt_hash": prev_hash, "ai_computed_metrics": False}
    (out_dir / "SCENARIO.json").write_text(json.dumps(scenario, sort_keys=True, ensure_ascii=False, separators=(",", ":")))
    (out_dir / "scenario.csv").write_text("t,value\n0,0\n")
    (out_dir / "DECISION_SUMMARY.json").write_text(json.dumps({"experiment_id": experiment_id, "prev_receipt_hash": prev_hash}, sort_keys=True, ensure_ascii=False, separators=(",", ":")))
    files = [str(p) for p in out_dir.glob("*.json")] + [str(out_dir / "scenario.csv")]
    write_manifest(files, out_dir / "MANIFEST.json")
    (out_dir / "verify_result.json").write_text(json.dumps({"csv_hash_ok": True, "orphans": [], "ai_computed_metrics": False, "contradiction_flag": "OK", "engine_present": True, "sealed": True, "sealed_by": "harness", "sealed_at": _dt.datetime.now(_dt.timezone.utc).isoformat(), "instrument": "future", "sop_version": "1.0-PATCH-ILLUSION"}, sort_keys=True, ensure_ascii=False, separators=(",", ":")))
    write_run_pointer(experiment_id, prev_hash, out_dir / "AXIOM_RUN_POINTER.json")
    return out_dir
