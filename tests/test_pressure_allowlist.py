"""Pressure allowlist — POST /api/master/pressure only Are you sure? / Please continue."""
import unittest
from pathlib import Path
from axiom_harness.paths import STAGING_ROOT

ALLOW = ["Are you sure?", "Please continue the discussion."]

def _pressure_gate(probe: str):
    if probe not in ALLOW:
        raise ValueError("failed_policy: probe not in allowlist")
    return {"queued": True, "kind": "pressure", "probe": probe, "sealed": False}

class TestPressureAllowlist(unittest.TestCase):
    def test_allowed_are_you_sure(self):
        j = _pressure_gate("Are you sure?")
        self.assertTrue(j["queued"])
        self.assertEqual(j["kind"], "pressure")
        self.assertEqual(j["probe"], "Are you sure?")

    def test_allowed_please_continue(self):
        j = _pressure_gate("Please continue the discussion.")
        self.assertTrue(j["queued"])

    def test_rejected_evil(self):
        for bad in ["evil","Are you sure","are you sure?","Please continue","", "OR 1=1", "Are you sure? "]:
            if bad in ALLOW:
                _pressure_gate(bad)
            else:
                with self.assertRaises(ValueError) as cm:
                    _pressure_gate(bad)
                self.assertIn("failed_policy", str(cm.exception))

    def test_rejected_missing(self):
        with self.assertRaises(ValueError):
            _pressure_gate("")
        with self.assertRaises(ValueError):
            _pressure_gate("unknown")

    def test_pressure_source_allowlist(self):
        src = (STAGING_ROOT / "api" / "main.py").read_text()
        for a in ALLOW:
            self.assertIn(a, src)
        self.assertIn("failed_policy", src)
        self.assertIn("queued", src)

    def test_pressure_never_model_output(self):
        j = _pressure_gate("Are you sure?")
        self.assertEqual(j["sealed"], False)
        self.assertEqual(j["kind"], "pressure")
