"""Receipt hallmark — every seal carries who+when (Step 1.2).

Verifies Phase 1.2: sealed_by/at/instrument/sop_version present on every verify_result.json.
"""
import json
import tempfile
from pathlib import Path


def _assert_hallmark(data: dict):
    for k in ("sealed_by", "sealed_at", "instrument", "sop_version"):
        assert k in data, f"missing hallmark {k}"
        assert data[k], f"empty hallmark {k}"
    assert data.get("ai_computed_metrics") is False
    # sealed_at should be ISO8601
    assert "T" in data["sealed_at"]


def test_workbench_hallmark():
    from axiom_harness.adapters.workbench import seal_workbench
    from axiom_harness.paths import STAGING_ROOT
    import tempfile as _tf
    from pathlib import Path as _P
    with _tf.TemporaryDirectory() as td:
        out = _P(td) / "WTF-001"
        mf = STAGING_ROOT / "missions" / "master_demo_wtf001.yaml"
        seal_workbench(mf, out)
        vr = json.loads((out / "verify_result.json").read_text())
        _assert_hallmark(vr)
        assert vr["instrument"] == "axiom_wb"


def test_per_eca_hallmark():
    from axiom_harness.adapters.per_eca import seal_per_eca
    with tempfile.TemporaryDirectory() as td:
        out = Path(td) / "WTF-002"
        seal_per_eca("WTF-002", out, {"per": "OFF", "eca": "OFF"})
        vr = json.loads((out / "verify_result.json").read_text())
        _assert_hallmark(vr)
        assert vr["instrument"] == "per_eca"


def test_evo_eu_hallmark():
    from axiom_harness.adapters.evo_eu import seal_evo_eu
    with tempfile.TemporaryDirectory() as td:
        out = Path(td) / "WTF-003"
        seal_evo_eu("WTF-003", out)
        vr = json.loads((out / "verify_result.json").read_text())
        _assert_hallmark(vr)
        assert vr["instrument"] == "evo_eu"


def test_future_hallmark():
    from axiom_harness.adapters.future import seal_future
    with tempfile.TemporaryDirectory() as td:
        out = Path(td) / "WTF-004"
        seal_future("WTF-004", out, prev_hash="abc")
        vr = json.loads((out / "verify_result.json").read_text())
        _assert_hallmark(vr)
        assert vr["instrument"] == "future"
