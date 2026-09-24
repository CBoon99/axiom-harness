"""LVM, pause/live, scalable 100s grid, watcher lifecycle, Future/Evo seals."""
import unittest, json
from pathlib import Path
from axiom_harness.paths import STAGING_ROOT
from axiom_harness.watcher import Watcher, Lifecycle
from axiom_harness.registry import REGISTRY

class TestLVMPauseLiveScalable(unittest.TestCase):
    def test_lvm_option_present(self):
        app_index = STAGING_ROOT / "app" / "index.html"
        self.assertTrue(app_index.exists())
        txt = app_index.read_text()
        self.assertIn("LVM", txt)
        self.assertIn("llava-13b", txt)
        self.assertIn("llava", txt.lower())

    def test_control_has_pause_resume(self):
        txt = (STAGING_ROOT / "app" / "index.html").read_text()
        self.assertIn('id="pauseBtn"', txt)
        self.assertIn('id="resumeBtn"', txt)
        self.assertIn("Pause", txt)
        self.assertIn("Resume", txt)

    def test_live_room_exists(self):
        txt = (STAGING_ROOT / "app" / "index.html").read_text()
        self.assertIn("Live Room", txt)
        self.assertIn("LIVE WORLD FEED", txt)
        self.assertIn('data-panel="live"', txt)

    def test_watcher_pause_live_lifecycle(self):
        w = Watcher("WTF-005A-RUN-01")
        self.assertEqual(w.lifecycle, Lifecycle.ARMED)
        w.transition(Lifecycle.STARTED)
        w.transition(Lifecycle.RUNNING)
        w.transition(Lifecycle.PAUSED)
        self.assertEqual(w.lifecycle, Lifecycle.PAUSED)
        w.transition(Lifecycle.RESUMED)
        self.assertEqual(w.lifecycle, Lifecycle.RESUMED)
        w.transition(Lifecycle.RUNNING)
        w.transition(Lifecycle.STOPPING)
        w.transition(Lifecycle.SEALED)
        w.transition(Lifecycle.COMPLETE)
        self.assertEqual(w.lifecycle, Lifecycle.COMPLETE)
        # illegal jump after complete
        with self.assertRaises(ValueError):
            w.transition(Lifecycle.RUNNING)
        # illegal direct pause from ARMED
        w2 = Watcher("X")
        with self.assertRaises(ValueError):
            w2.transition(Lifecycle.PAUSED)

    def test_watcher_records_failed_policy(self):
        w = Watcher("WTF-001")
        w.transition(Lifecycle.STARTED)
        w.record("failed_policy", {"attempt":"..", "denied": True})
        self.assertEqual(w.events[-1]["kind"], "failed_policy")

    def test_scalable_grid_100s(self):
        txt = (STAGING_ROOT / "app" / "index.html").read_text()
        self.assertIn("repeat(auto-fill,minmax(220px,1fr))", txt)
        self.assertIn("100s stay O(1) per row", txt)
        self.assertIn("247", txt)
        self.assertIn("virtualized", txt.lower())
        # docs wireframe is canonical scalable (app/wireframes is legacy non-scalable)
        env = STAGING_ROOT / "docs" / "wireframes" / "environment.html"
        if not env.exists():
            env = STAGING_ROOT / "app" / "wireframes" / "environment.html"
        if env.exists():
            wt = env.read_text()
            self.assertIn("scalable", wt.lower())
            self.assertIn("100s", wt)
            self.assertIn("minmax", wt)

    def test_seals_7_and_future_chain(self):
        self.assertEqual(len(REGISTRY), 7)
        # future seal chain B.prev=A
        from axiom_harness.adapters.future import seal_future
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "future"
            seal_future("WTF-001", out, prev_hash="abc")
            self.assertTrue((out / "AXIOM_RUN_POINTER.json").exists())
            self.assertTrue((out / "MANIFEST.json").exists())
            vr = json.loads((out / "verify_result.json").read_text())
            self.assertFalse(vr["ai_computed_metrics"])
            sc = json.loads((out / "SCENARIO.json").read_text())
            self.assertEqual(sc["prev_receipt_hash"], "abc")
            self.assertEqual(sc["scenario"], "future-synthetic")

    def test_evo_and_per_eca_seals(self):
        from axiom_harness.adapters.evo_eu import seal_evo_eu
        from axiom_harness.adapters.per_eca import seal_per_eca
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "evo"
            seal_evo_eu("WTF-001", out)
            self.assertTrue((out / "EVO_EU.json").exists())
            self.assertFalse(json.loads((out / "verify_result.json").read_text())["ai_computed_metrics"])
            out2 = Path(td) / "per"
            seal_per_eca("WTF-001", out2, {"per":"OFF","eca":"OFF"})
            self.assertTrue((out2 / "PER_ECA_SKIPPED.json").exists())
            with self.assertRaises(RuntimeError):
                seal_per_eca("WTF-001", Path(td)/"bad", {"per":"ON","eca":"OFF"})

    def test_app_env_grid_paginated_api_hint(self):
        txt = (STAGING_ROOT / "app" / "index.html").read_text()
        self.assertIn("GET /master/timeline?limit=24", txt)
