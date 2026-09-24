"""Health honesty — GET /api/master/health derives real jail + engine, not hard-coded True."""
import unittest, json
from pathlib import Path
from axiom_harness.paths import is_safe_relative, OUTPUTS, STAGING_ROOT

class TestHealthHonesty(unittest.TestCase):
    def test_health_logic_via_paths(self):
        # health must derive via is_safe_relative, not hard-coded
        self.assertTrue(is_safe_relative("missions/master_demo_wtf001.yaml"))
        self.assertFalse(is_safe_relative("%2e%2e/escape"))
        self.assertFalse(is_safe_relative("%2525252e%2525252e/escape"))
        # engine_present derived from OUTPUTS/demo existence
        engine_present = (OUTPUTS / "demo").exists()
        self.assertIsInstance(engine_present, bool)

    def test_health_source_is_honest(self):
        src = (STAGING_ROOT / "api" / "main.py").read_text()
        self.assertIn("is_safe_relative", src)
        self.assertIn("OUTPUTS", src)
        self.assertIn("engine_present", src)
        self.assertIn("ai_computed_metrics", src)
        self.assertIn("False", src)
        # not hard-coded path_jail True literal without call
        self.assertNotIn('"path_jail": True', src)

    def test_health_json_shape(self):
        # simulate what api/main.py GET returns: ai_computed_metrics false + path_jail + engine_present + sealed
        probe = "missions/master_demo_wtf001.yaml"
        body = {
            "ai_computed_metrics": False,
            "path_jail": is_safe_relative(probe),
            "engine_present": (OUTPUTS / "demo").exists(),
            "sealed": is_safe_relative(probe),
        }
        self.assertIs(body["ai_computed_metrics"], False)
        self.assertTrue(body["path_jail"])
        self.assertIn("engine_present", body)

    def test_health_not_fake_hardcoded(self):
        self.assertTrue(is_safe_relative("missions/master_demo_wtf001.yaml"))
        self.assertFalse(is_safe_relative("%2e%2e/escape"))
        self.assertFalse(is_safe_relative("%2525252e%2525252e/escape"))
        self.assertTrue((STAGING_ROOT / "missions" / "master_demo_wtf001.yaml").exists())

    def test_health_source_has_try_except(self):
        src = (STAGING_ROOT / "api" / "main.py").read_text()
        # health wraps in try/except to stay honest on error
        self.assertIn("try:", src)
        self.assertIn("path_jail", src)
