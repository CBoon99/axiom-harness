"""Allowlist anchored — validate ONLY module argv, smuggle must fail."""
import unittest
from axiom_harness.adapters.workbench import _assert_allowlist
from axiom_harness.paths import ALLOWED_SCRIPT_PREFIXES

class TestAllowlistAnchored(unittest.TestCase):
    def test_prefixes(self):
        self.assertIn("scripts/factory_", ALLOWED_SCRIPT_PREFIXES)
        self.assertIn("AXIOM_", ALLOWED_SCRIPT_PREFIXES)

    def test_allows_axiom_wb(self):
        _assert_allowlist(["python3","-m","axiom_wb","evaluate","x"])
        _assert_allowlist(["python3","-m","axiom_wb","evaluate","--out","/tmp"])

    def test_allows_factory_prefix(self):
        _assert_allowlist(["python3","-m","scripts/factory_foo"])
        _assert_allowlist(["python3","-m","scripts/factory_bar","--arg","1"])
        _assert_allowlist(["python3","-m","AXIOM_test"])
        _assert_allowlist(["python3","-m","AXIOM_EVO"])

    def test_blocks_evil_smuggle(self):
        with self.assertRaises(ValueError) as cm:
            _assert_allowlist(["python3","-m","evil","--","scripts/factory_evil"])
        self.assertIn("failed_policy", str(cm.exception))
        # joined string contains allowlist but module is evil — must still block
        with self.assertRaises(ValueError):
            _assert_allowlist(["python3","-m","evil","scripts/factory_foo"])
        with self.assertRaises(ValueError):
            _assert_allowlist(["python3","-m","bad","--out","scripts/factory_x"])

    def test_blocks_wrong_binary_and_missing(self):
        with self.assertRaises(ValueError):
            _assert_allowlist(["python","-m","axiom_wb"])
        with self.assertRaises(ValueError):
            _assert_allowlist(["python3","axiom_wb"])
        with self.assertRaises(ValueError):
            _assert_allowlist(["python3","-m"])
        with self.assertRaises(ValueError):
            _assert_allowlist(["python3"])
        with self.assertRaises(ValueError):
            _assert_allowlist(["python3","-m","not_allowed_module"])

    def test_blocks_trailing_args_dont_whitelist(self):
        # trailing factory string must not make evil module pass
        with self.assertRaises(ValueError):
            _assert_allowlist(["python3","-m","evil","scripts/factory_evil","--","axiom_wb"])
        with self.assertRaises(ValueError):
            _assert_allowlist(["python3","-m","evil_module"])

    def test_future_per_eca_noop_stays_off(self):
        from axiom_harness.adapters.per_eca import ensure_off
        ensure_off({"per":"OFF","eca":"OFF"})
        with self.assertRaises(RuntimeError):
            ensure_off({"per":"ON","eca":"OFF"})
        with self.assertRaises(RuntimeError):
            ensure_off({"per":"OFF","eca":"ON"})
        with self.assertRaises(RuntimeError):
            ensure_off({"per":"ON","eca":"ON"})
