"""V1.4 Multilingual — §20-22 language as experimental variable."""
from axiom_harness.mission import MasterMission, LanguageConfig, LanguageCode

BASE = {"id": "WTF-001", "protocol": "sha256:abc", "context_kind": "FRESH", "env_kind": "STATIC"}

def test_language_primary_and_variants():
    m = MasterMission(**BASE, language=LanguageConfig(primary=LanguageCode.EN, variants=[LanguageCode.ID, LanguageCode.ES], keep_params_constant=True))
    assert m.language.primary == LanguageCode.EN
    assert LanguageCode.ID in m.language.variants
    assert m.language.keep_params_constant is True

def test_language_single_and_detect():
    m = MasterMission(**BASE, language=LanguageConfig(primary=LanguageCode.ZH, detect_switch=True))
    assert m.language.primary == LanguageCode.ZH
    assert m.language.detect_switch is True

def test_language_variants_cross_control():
    m = MasterMission(**BASE, language=LanguageConfig(primary=LanguageCode.EN, variants=[LanguageCode.FR, LanguageCode.DE, LanguageCode.JA, LanguageCode.AR], keep_params_constant=True))
    assert len(m.language.variants) == 4
    # frozen
    try:
        m.language.primary = LanguageCode.ES
        assert False
    except Exception:
        pass
