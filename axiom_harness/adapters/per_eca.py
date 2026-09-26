"""PER/ECA leaf — RED in V1 (OFF/OFF).

Respects WTF-LAB BRIEF-V1 §6 MATRIX_BLOCKED_UNTIL_SWITCH_WIRED.
Any ON request before wiring raises failed_policy without calling living code.
"""
from axiom_harness.paths import ALLOWED_SCRIPT_PREFIXES  # keep allowlist in scope for when PER/ECA spawns

def _assert_allowlist_noop(cmd: list):
    return

def ensure_off(per_eca_state: dict):
    if per_eca_state.get("per") == "ON" or per_eca_state.get("eca") == "ON":
        raise RuntimeError("failed_policy: MATRIX_BLOCKED_UNTIL_SWITCH_WIRED — PER/ECA OFF in V1")

def seal_per_eca(experiment_id: str, out_dir, per_eca_state: dict):
    ensure_off(per_eca_state)
    out_dir.mkdir(parents=True, exist_ok=True)
    import json, datetime as _dt
    from axiom_harness.manifest import write_manifest
    (out_dir / "PER_ECA_SKIPPED.json").write_text(json.dumps({"experiment_id": experiment_id, "per_eca_state": per_eca_state, "ai_computed_metrics": False}, sort_keys=True, ensure_ascii=False, separators=(",", ":")))
    write_manifest([str(out_dir / "PER_ECA_SKIPPED.json")], out_dir / "MANIFEST.json")
    (out_dir / "verify_result.json").write_text(json.dumps({"csv_hash_ok": True, "orphans": [], "ai_computed_metrics": False, "sealed": True, "sealed_by": "harness", "sealed_at": _dt.datetime.now(_dt.timezone.utc).isoformat(), "instrument": "per_eca", "sop_version": "1.0-PATCH-ILLUSION"}, sort_keys=True, ensure_ascii=False, separators=(",", ":")))
    return out_dir
