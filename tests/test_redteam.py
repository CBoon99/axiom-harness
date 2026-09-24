import unittest
from pathlib import Path
import tempfile, json
from axiom_harness.paths import is_safe_relative
from axiom_harness.adapters.workbench import _assert_allowlist

class TestRedTeam(unittest.TestCase):
    def test_path_escape_blocked(self):
        for p in ["../escape", "%2e%2e/escape", "%2525252e%2525252e/escape", "a//b", "a\\b", "/absolute"]:
            self.assertFalse(is_safe_relative(p), f"should block {p}")

    def test_allowlist_blocks_smuggle(self):
        with self.assertRaises(ValueError):
            _assert_allowlist(["python3","-m","evil","--","scripts/factory_evil"])
        _assert_allowlist(["python3","-m","axiom_wb","evaluate","x"])

    def test_per_eca_on_blocked(self):
        from axiom_harness.adapters.per_eca import ensure_off
        with self.assertRaises(RuntimeError):
            ensure_off({"per":"ON","eca":"OFF"})

    def test_manifest_tamper_detected(self):
        from axiom_harness.manifest import write_manifest, sha256_file
        with tempfile.TemporaryDirectory() as td:
            a = Path(td)/"a.txt"; a.write_text("hello")
            out = Path(td)/"MANIFEST.json"
            write_manifest([a], out)
            # tamper file after manifest
            a.write_text("tampered")
            # recompute should mismatch
            self.assertNotEqual(sha256_file(a), json.loads(out.read_text())["files"][0]["sha256"])

    def test_health_not_fake(self):
        from axiom_harness.paths import is_safe_relative
        self.assertTrue(is_safe_relative("missions/master_demo_wtf001.yaml"))
        self.assertFalse(is_safe_relative("%2e%2e/escape"))
