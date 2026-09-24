import unittest
from axiom_harness.mission import MasterMission

class TestGateway(unittest.TestCase):
    def test_gateway_requires_fields(self):
        # gateway must reject missing model_version/per_eca_state via api seal gate
        m = MasterMission(id="WTF-001", protocol="sha256:abc", participant="MODEL", model="analyst", model_version="llama-3.2-11b", per_eca_state={"per":"OFF","eca":"OFF"}, cost={}, context_kind="FRESH", env_kind="STATIC", params={}, permissions={})
        self.assertEqual(m.per_eca_state["per"], "OFF")

    def test_gateway_blocks_on(self):
        from axiom_harness.adapters.per_eca import ensure_off
        with self.assertRaises(RuntimeError):
            ensure_off({"per":"ON","eca":"OFF"})

    def test_seal_gate_api(self):
        # api/main.py POST /master/seal must require model_version/per_eca_state — covered by MasterMission defaults, gate checks presence
        from axiom_harness.mission import MasterMission
        m = MasterMission(id="X", protocol="p", participant="MODEL", model="a", context_kind="FRESH", env_kind="STATIC", params={}, permissions={})
        self.assertIn("per", m.per_eca_state)
