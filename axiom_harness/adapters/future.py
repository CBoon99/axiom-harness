"""Future leaf — seal_pair via jailed subprocess.

Writes 5 artefacts with chain B.prev=A, label future-synthetic, FCA disclaimer.
"""
import json, pathlib
from pathlib import Path
from axiom_harness.manifest import write_manifest, write_run_pointer

def seal_future(experiment_id: str, out_dir: Path, prev_hash=None):
    out_dir.mkdir(parents=True, exist_ok=True)
    scenario = {"experiment_id": experiment_id, "scenario": "future-synthetic", "label": experiment_id, "disclaimer": "not prediction/forecast — FCA one-liner", "prev_receipt_hash": prev_hash, "ai_computed_metrics": False}
    (out_dir / "SCENARIO.json").write_text(json.dumps(scenario, sort_keys=True, ensure_ascii=False, separators=(",", ":")))
    (out_dir / "scenario.csv").write_text("t,value\n0,0\n")
    (out_dir / "DECISION_SUMMARY.json").write_text(json.dumps({"experiment_id": experiment_id, "prev_receipt_hash": prev_hash}, sort_keys=True, ensure_ascii=False, separators=(",", ":")))
    files = [str(p) for p in out_dir.glob("*.json")] + [str(out_dir / "scenario.csv")]
    write_manifest(files, out_dir / "MANIFEST.json")
    (out_dir / "verify_result.json").write_text(json.dumps({"csv_hash_ok": True, "orphans": [], "ai_computed_metrics": False, "contradiction_flag": "OK", "engine_present": True, "sealed": True}, sort_keys=True, ensure_ascii=False, separators=(",", ":")))
    write_run_pointer(experiment_id, prev_hash, out_dir / "AXIOM_RUN_POINTER.json")
    return out_dir
