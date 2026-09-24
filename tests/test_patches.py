import unittest, tempfile, json
from pathlib import Path
from axiom_harness.manifest import write_manifest, write_run_pointer
from axiom_harness.paths import ALLOWED_SCRIPT_PREFIXES, is_safe_relative
from axiom_harness.watcher import Watcher, Lifecycle
from axiom_harness.mission import MasterMission

class TestPatches(unittest.TestCase):
    def test_manifest_canonical_no_indent(self):
        with tempfile.TemporaryDirectory() as td:
            a = Path(td)/"a.txt"; a.write_text("a")
            out = Path(td)/"MANIFEST.json"
            write_manifest([a], out)
            raw = out.read_text()
            self.assertNotIn("\n  ", raw)  # no pretty indent
            self.assertIn('","', raw)  # separators (",",":")
            # round-trip hash recompute
            self.assertEqual(raw, json.dumps(json.loads(raw), sort_keys=True, ensure_ascii=False, separators=(",", ":")))

    def test_run_pointer_canonical(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td)/"ptr.json"
            write_run_pointer("WTF-001", "abc", out)
            self.assertNotIn("\n  ", out.read_text())

    def test_allowed_prefixes_include_axiom(self):
        self.assertIn("scripts/factory_", ALLOWED_SCRIPT_PREFIXES)
        self.assertIn("AXIOM_", ALLOWED_SCRIPT_PREFIXES)

    def test_is_safe_blocks_traversal(self):
        self.assertFalse(is_safe_relative("../escape"))
        self.assertFalse(is_safe_relative("/absolute"))
        self.assertFalse(is_safe_relative("%2e%2e/escape"))
        self.assertFalse(is_safe_relative("%252e%252e/escape"))
        self.assertFalse(is_safe_relative("a//b"))
        self.assertFalse(is_safe_relative("a\\b"))
        self.assertTrue(is_safe_relative("missions/demo.yaml"))

    def test_watcher_guards_lifecycle(self):
        w = Watcher("WTF-001")
        w.transition(Lifecycle.STARTED)
        w.transition(Lifecycle.RUNNING)
        with self.assertRaises(ValueError):
            w.transition(Lifecycle.COMPLETE)  # illegal jump
        w.transition(Lifecycle.STOPPING)
        w.transition(Lifecycle.SEALED)
        w.transition(Lifecycle.COMPLETE)
        self.assertEqual(w.lifecycle, Lifecycle.COMPLETE)

    def test_master_mission_requires_new_fields(self):
        m = MasterMission(id="WTF-001", protocol="p", participant="MODEL", model="analyst", model_version="llama-3.2-11b", per_eca_state={"per":"OFF","eca":"OFF"}, cost={"tokens_input":0}, context_kind="FRESH", env_kind="STATIC", params={}, permissions={})
        self.assertEqual(m.model_version, "llama-3.2-11b")
