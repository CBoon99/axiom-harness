"""Phase 2 — PER/ECA gated bolt-on (FrozenDict + GateOk)."""
import unittest
import json
from pathlib import Path


class TestPerEcaGated(unittest.TestCase):
    def test_off_gate(self):
        from axiom_harness.adapters.per_eca import ensure_off
        # OFF passes
        ensure_off({"per": "OFF", "eca": "OFF"})
        from axiom_harness.mission import PerEcaState
        ensure_off(PerEcaState(per="OFF", eca="OFF"))
        # ON fails with failed_policy
        with self.assertRaises(RuntimeError) as cm:
            ensure_off({"per": "ON", "eca": "OFF"})
        self.assertIn("failed_policy", str(cm.exception))
        with self.assertRaises(RuntimeError):
            ensure_off({"per": "OFF", "eca": "ON"})
        with self.assertRaises(RuntimeError):
            ensure_off(PerEcaState(per="ON", eca="OFF"))

    def test_frozen_inner_immutable(self):
        from axiom_harness.mission import MasterMission
        from pydantic import ValidationError
        m = MasterMission(id="WTF-001", protocol="p", context_kind="FRESH", env_kind="STATIC", params={}, permissions={})
        # outer frozen
        with self.assertRaises(Exception):
            m.id = "WTF-002"
        # inner dict mutation must fail — PerEcaState is frozen
        with self.assertRaises(Exception):
            m.per_eca_state.per = "ON"
        with self.assertRaises(Exception):
            m.per_eca_state.eca = "ON"
        # legacy dict-style mutation via __setitem__ not supported — must raise
        with self.assertRaises(Exception):
            m.per_eca_state["per"] = "ON"

    def test_gate_ok_only_when_wired(self):
        from axiom_harness.adapters.per_eca import gate_ok
        # Without LOCK-STATUS ON and without evidence, gate is OFF (Phase 2 keeps OFF)
        self.assertFalse(gate_ok({"per": "OFF", "eca": "OFF"}, None))
        self.assertFalse(gate_ok({"per": "OFF", "eca": "OFF"}, {"R": [1, 2, 3, 4], "delta_H": 0.6, "sealed": True, "hash_ok": True, "falsify": True, "repeat": False, "N": 10, "T": 5}))
        # |R|>3 fails
        self.assertFalse(gate_ok({"per": "OFF", "eca": "OFF"}, {"R": [1, 2, 3, 4], "delta_H": 0.6, "sealed": True, "hash_ok": True, "falsify": True, "repeat": False, "N": 10, "T": 5}))
        # correct shape but still OFF because LOCK-STATUS is PER_OFF_ECA_OFF
        evidence = {"R": [1, 2], "delta_H": 0.6, "sealed": True, "hash_ok": True, "falsify": True, "repeat": False, "N": 10, "T": 5}
        # gate_ok should be False while LOCK-STATUS next_authorized_action=PER_OFF_ECA_OFF
        self.assertFalse(gate_ok({"per": "OFF", "eca": "OFF"}, evidence))
        # also check per/eca config gate stays OFF
        from axiom_harness.mission import MasterMission, PerConfig
        m = MasterMission(id="WTF-001", protocol="p", context_kind="FRESH", env_kind="STATIC", params={}, permissions={}, per=PerConfig(enabled=False, mode="OFF"))
        self.assertEqual(m.per.mode, "OFF")
        self.assertIsNone(m.eca)

    def test_per_eca_bprev_a_untouched(self):
        # B.prev=A chain must remain green via existing harness_boundary tests
        from axiom_harness.mission import MasterMission
        m1 = MasterMission(id="WTF-001", protocol="p1", context_kind="FRESH", env_kind="STATIC", params={}, permissions={})
        m2 = MasterMission(id="WTF-002", protocol="p2", context_kind="FRESH", env_kind="STATIC", params={}, permissions={})
        self.assertEqual(m1.per_eca_state, {"per": "OFF", "eca": "OFF"})
        self.assertEqual(m2.per_eca_state, {"per": "OFF", "eca": "OFF"})
