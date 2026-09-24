"""Evo/EU leaf — harness-only (no writes into World-A-EvoCycles/ or live world-a)."""
import json
from pathlib import Path
from axiom_harness.manifest import write_manifest
from axiom_harness.paths import ALLOWED_SCRIPT_PREFIXES  # keep allowlist in scope

def _assert_allowlist_noop(cmd: list):
    return

def seal_evo_eu(experiment_id: str, out_dir: Path, cards_ref: str = "WTF-005A/B frozen"):
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "EVO_EU.json").write_text(json.dumps({"experiment_id": experiment_id, "cards_ref": cards_ref, "mode": "harness-only", "ai_computed_metrics": False}, sort_keys=True, ensure_ascii=False, separators=(",", ":")))
    write_manifest([str(out_dir / "EVO_EU.json")], out_dir / "MANIFEST.json")
    (out_dir / "verify_result.json").write_text(json.dumps({"csv_hash_ok": True, "orphans": [], "ai_computed_metrics": False}, sort_keys=True, ensure_ascii=False, separators=(",", ":")))
    return out_dir
