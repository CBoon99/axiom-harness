"""Jail canonicalisation — deep %2525252e etc, anchored via is_safe_relative iterative decode."""
import unittest
from axiom_harness.paths import is_safe_relative

class TestJailCanonical(unittest.TestCase):
    def test_blocks_simple_traversal(self):
        self.assertFalse(is_safe_relative("../escape"))
        self.assertFalse(is_safe_relative("/absolute"))
        self.assertFalse(is_safe_relative("a//b"))
        self.assertFalse(is_safe_relative("a\\b"))
        self.assertFalse(is_safe_relative("\\absolute"))
        self.assertFalse(is_safe_relative(".."))
        self.assertFalse(is_safe_relative("../"))
        self.assertFalse(is_safe_relative("a/../b"))

    def test_blocks_single_encode(self):
        self.assertFalse(is_safe_relative("%2e%2e/escape"))
        self.assertFalse(is_safe_relative("%2e%2e%2fescape"))
        self.assertFalse(is_safe_relative("a/%2e%2e/b"))

    def test_blocks_double_encode(self):
        self.assertFalse(is_safe_relative("%252e%252e/escape"))
        self.assertFalse(is_safe_relative("%2525252e%2525252e/escape"))

    def test_blocks_deep_triple_quad(self):
        # deep %2525252e is triple-encoded '.' → iterative unquote must still block
        self.assertFalse(is_safe_relative("%2525252e%2525252e/escape"))
        # correctly formed deep: encode ".." 5x
        import urllib.parse
        deep = ".."
        for _ in range(5):
            deep = urllib.parse.quote(deep, safe="")
        # deep is now 5x encoded ".."
        self.assertFalse(is_safe_relative(f"{deep}/escape"))
        self.assertFalse(is_safe_relative(f"{deep}/{deep}/escape"))
        # encoded slash
        self.assertFalse(is_safe_relative("%2525252f%2525252e%2525252e"))
        # mixed deep
        self.assertFalse(is_safe_relative("missions/%2525252e%2525252e/escape"))
        self.assertFalse(is_safe_relative("%2e%2e/%2e%2e/escape"))
        self.assertFalse(is_safe_relative("%252e%252e/%252e%252e/escape"))

    def test_allows_safe_relatives(self):
        self.assertTrue(is_safe_relative("missions/master_demo_wtf001.yaml"))
        self.assertTrue(is_safe_relative("outputs/demo/WTF-001/workbench/SCENARIO.json"))
        self.assertTrue(is_safe_relative("missions/demo.yaml"))
        self.assertTrue(is_safe_relative("outputs/smoke_001/MANIFEST.json"))
        self.assertTrue(is_safe_relative("docs/API_SPEC.md"))

    def test_iterative_stable(self):
        # %2525252e → %25252e → %252e → %2e → . so any depth must normalise
        from axiom_harness.paths import _decoded
        self.assertIn("..", _decoded("%2525252e%2525252e/escape"))
        self.assertEqual(".", _decoded("%2525252e"))
        self.assertEqual("..", _decoded("%252e%252e"))
