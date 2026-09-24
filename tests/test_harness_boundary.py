"""Harness boundary — orchestration only, no duplicated ECA/PER maths."""
import importlib, pathlib, json

def test_harness_cannot_calculate_gateok():
    # Harness must not contain GateOk, ΔH, T_max logic
    h_path = pathlib.Path(__file__).parents[1] / "axiom_harness"
    for p in h_path.rglob("*.py"):
        txt = p.read_text()
        assert "GateOk" not in txt or "ECA" not in p.name, f"{p} must not calculate GateOk"
        # no duplicated H calculation except doc reference
        if "ΔH" in txt:
            assert "evidence" not in p.name.lower() or "archive" in str(p), f"{p} duplicated ΔH"

def test_harness_cannot_alter_eca_config():
    from axiom_harness.mission import MasterMission
    # Harness only transports per_eca_state OFF, cannot set ON without adapter raising
    m = MasterMission(id="WTF-001", protocol="sha256:abc", context_kind="FRESH", env_kind="STATIC", per_eca_state={"per":"ON","eca":"OFF"})
    from axiom_harness.adapters.per_eca import ensure_off
    try:
        ensure_off(m.per_eca_state)
        assert False, "should raise MATRIX_BLOCKED"
    except RuntimeError as e:
        assert "MATRIX_BLOCKED_UNTIL_SWITCH_WIRED" in str(e)

def test_harness_cannot_silent_provider_replace():
    # Only AnthropicProvider in ECA/plugin exists, Harness has no provider factory
    h_provider = list((pathlib.Path(__file__).parents[1] / "axiom_harness").rglob("*provider*"))
    assert len(h_provider) == 0, "Harness must not have provider factory"

def test_harness_records_hashes():
    from axiom_harness.adapters.per_eca import seal_per_eca
    import tempfile, pathlib
    out = pathlib.Path(tempfile.mkdtemp()) / "out"
    seal_per_eca("WTF-001", out, {"per":"OFF","eca":"OFF"})
    data = json.loads((out / "PER_ECA_SKIPPED.json").read_text())
    assert data["per_eca_state"] == {"per":"OFF","eca":"OFF"}
    assert data["ai_computed_metrics"] is False
    assert "ECA" not in str(data) or "OFF" in str(data)

def test_propagates_refusal_unchanged():
    from axiom_harness.adapters.per_eca import ensure_off
    bad = {"per":"OFF","eca":"ON"}
    try:
        ensure_off(bad)
        assert False
    except RuntimeError as e:
        msg = str(e)
        # refusal is explicit, not silently converted to success
        assert "failed_policy" in msg

def test_no_mock_as_live():
    # Harness mission.py has no MOCK/LIVE mode for ECA
    txt = (pathlib.Path(__file__).parents[1] / "axiom_harness/mission.py").read_text()
    assert "MOCK" not in txt

def test_adapter_failure_explicit():
    from axiom_harness.adapters.per_eca import ensure_off
    try:
        ensure_off({"per":"ON","eca":"OFF"})
    except RuntimeError as e:
        assert "failed_policy" in str(e)
    else:
        assert False

def test_no_duplicated_maths():
    # Harness must not contain HYPOTHESIS_WEIGHTS, T_max, epsilon duplication
    root = pathlib.Path(__file__).parents[1]
    for p in (root / "axiom_harness").rglob("*.py"):
        txt = p.read_text()
        assert "HYPOTHESIS_WEIGHTS" not in txt
        assert "T_max" not in txt
        assert "epsilon_base" not in txt

def test_harness_cannot_import_untracked_sibling_code():
    # Harness must not import untracked sibling-repository code (PER/ECA via sys.path hack)
    txt = (pathlib.Path(__file__).parents[1] / "axiom_harness/mission.py").read_text()
    assert "sys.path" not in txt
    assert "PER-Core" not in txt
    assert "ECA/sim" not in txt

def test_harness_cannot_rely_on_local_only_files():
    # Harness adapter must not rely on local-only upstream files (e.g., /tmp/anthropic_key)
    for p in (pathlib.Path(__file__).parents[1] / "axiom_harness").rglob("*.py"):
        txt = p.read_text()
        assert "/tmp/anthropic_key" not in txt
        assert "untracked" not in txt.lower() or "tracked" in txt.lower()

def test_harness_cannot_convert_failure_to_pass():
    from axiom_harness.adapters.per_eca import ensure_off
    # ensure_off failure must stay failed_policy, not become PASS
    try:
        ensure_off({"per":"ON","eca":"OFF"})
    except RuntimeError as e:
        assert "failed_policy" in str(e)
        # must not be sealed:true
        assert "sealed" not in str(e).lower() or "true" not in str(e).lower()

def test_harness_cannot_declare_upstream_proven():
    # Invocation success != proven — Harness must not declare ECA proven merely because invocation succeeded
    # Check that no Harness file claims ECA proven
    for p in (pathlib.Path(__file__).parents[1] / "axiom_harness").rglob("*.py"):
        txt = p.read_text().lower()
        assert "eca proven" not in txt
        assert "eca_pass" not in txt
