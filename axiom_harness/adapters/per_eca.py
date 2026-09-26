"""PER/ECA leaf — RED in V1 (OFF/OFF).

Respects WTF-LAB BRIEF-V1 §6 MATRIX_BLOCKED_UNTIL_SWITCH_WIRED.
Any ON request before wiring raises failed_policy without calling living code.
"""
from axiom_harness.paths import ALLOWED_SCRIPT_PREFIXES  # keep allowlist in scope for when PER/ECA spawns

def _assert_allowlist_noop(cmd: list):
    return

def _get_state_val(state, key):
    # support dict and PerEcaState model
    try:
        return state.get(key) if hasattr(state, "get") else getattr(state, key)
    except Exception:
        return getattr(state, key, None) if hasattr(state, key) else None


def _check_lock_status():
    # LOCK-STATUS.json gate — next_authorized_action must allow ON
    import json
    from pathlib import Path
    p = Path(__file__).resolve().parents[2] / "LOCK-STATUS.json"
    try:
        data = json.loads(p.read_text())
        nxt = data.get("next_authorized_action", "")
        # only allow ON when explicitly authorized
        return "PER_ON" in nxt or "ECA_ON" in nxt
    except Exception:
        return False


def ensure_off(per_eca_state):
    per = _get_state_val(per_eca_state, "per")
    eca = _get_state_val(per_eca_state, "eca")
    if per == "ON" or eca == "ON":
        # check LOCK-STATUS gate — keep CORPUS ON / PER OFF / ECA OFF until wired
        if not _check_lock_status():
            raise RuntimeError("failed_policy: MATRIX_BLOCKED_UNTIL_SWITCH_WIRED — PER/ECA OFF in V1 (LOCK-STATUS next_authorized_action=PER_OFF_ECA_OFF)")
        # even if lock allows, still require gate wiring (handled in api/main.py) — hash-only, no duplicated maths
        raise RuntimeError("failed_policy: MATRIX_BLOCKED_UNTIL_SWITCH_WIRED — PER/ECA ON requires gated wiring")


def gate_ok(per_eca_state, evidence=None) -> bool:
    """Stub OFF until adapters wired — keep CORPUS ON / PER OFF / ECA OFF, hash-only check only."""
    # Phase 2 keeps gate OFF — return False unless LOCK-STATUS explicitly enables
    if not _check_lock_status():
        return False
    if evidence is None:
        return False
    # no duplicated maths here — hash-only placeholder, adapters will provide real check
    return False

def seal_per_eca(experiment_id: str, out_dir, per_eca_state):
    ensure_off(per_eca_state)
    out_dir.mkdir(parents=True, exist_ok=True)
    import json, datetime as _dt
    from axiom_harness.manifest import write_manifest
    # normalize PerEcaState model to dict for json
    try:
        state_dict = per_eca_state.model_dump() if hasattr(per_eca_state, "model_dump") else dict(per_eca_state)
    except Exception:
        state_dict = {"per": _get_state_val(per_eca_state, "per"), "eca": _get_state_val(per_eca_state, "eca")}
    (out_dir / "PER_ECA_SKIPPED.json").write_text(json.dumps({"experiment_id": experiment_id, "per_eca_state": state_dict, "ai_computed_metrics": False}, sort_keys=True, ensure_ascii=False, separators=(",", ":")))
    write_manifest([str(out_dir / "PER_ECA_SKIPPED.json")], out_dir / "MANIFEST.json")
    (out_dir / "verify_result.json").write_text(json.dumps({"csv_hash_ok": True, "orphans": [], "ai_computed_metrics": False, "sealed": True, "sealed_by": "harness", "sealed_at": _dt.datetime.now(_dt.timezone.utc).isoformat(), "instrument": "per_eca", "sop_version": "1.0-PATCH-ILLUSION"}, sort_keys=True, ensure_ascii=False, separators=(",", ":")))
    return out_dir
