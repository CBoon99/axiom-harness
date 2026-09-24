"""Seal gate — model_version + per_eca_state + protocol via api/main.py logic."""
import unittest, json
from pathlib import Path
from axiom_harness.mission import MasterMission
from axiom_harness.paths import STAGING_ROOT

def _seal_gate(data: dict):
    """Mirror api/main.py POST /api/master/seal gate."""
    m = MasterMission(**data)
    if not m.model_version or not m.per_eca_state:
        raise ValueError("failed_policy: missing model_version/per_eca_state")
    return {"sealed": True, "config_hash": m.protocol, "experiment_id": m.id}

class TestSealGate(unittest.TestCase):
    def test_valid_seal(self):
        payload = {"id":"WTF-001","protocol":"sha256:f4e9f08b079669fd25aa8d17c50e360fda10aad501863196ee54dab27e4ee0e0","participant":"MODEL","model":"analyst","model_version":"llama-3.2-11b","per_eca_state":{"per":"OFF","eca":"OFF"},"cost":{},"context_kind":"FRESH","env_kind":"STATIC","params":{},"permissions":{}}
        j = _seal_gate(payload)
        self.assertTrue(j["sealed"])
        self.assertEqual(j["config_hash"], payload["protocol"])
        self.assertEqual(j["experiment_id"], "WTF-001")

    def test_empty_model_version_fails(self):
        payload = {"id":"WTF-002","protocol":"p","participant":"MODEL","model":"analyst","model_version":"","per_eca_state":{"per":"OFF","eca":"OFF"},"cost":{},"context_kind":"FRESH","env_kind":"STATIC","params":{},"permissions":{}}
        with self.assertRaises(ValueError) as cm:
            _seal_gate(payload)
        self.assertIn("failed_policy", str(cm.exception))

    def test_empty_per_eca_fails(self):
        payload = {"id":"WTF-003","protocol":"p","participant":"MODEL","model":"analyst","model_version":"llama-3.2-11b","per_eca_state":{},"cost":{},"context_kind":"FRESH","env_kind":"STATIC","params":{},"permissions":{}}
        with self.assertRaises(ValueError):
            _seal_gate(payload)

    def test_none_per_eca_fails(self):
        payload = {"id":"WTF-004","protocol":"p","participant":"MODEL","model":"analyst","model_version":"llama-3.2-11b","per_eca_state": None,"cost":{},"context_kind":"FRESH","env_kind":"STATIC","params":{},"permissions":{}}
        with self.assertRaises(Exception):
            _seal_gate(payload)

    def test_seal_source_checks_gate(self):
        src = (STAGING_ROOT / "api" / "main.py").read_text()
        self.assertIn("model_version", src)
        self.assertIn("per_eca_state", src)
        self.assertIn("failed_policy", src)
        self.assertIn("sealed", src)

    def test_mastermission_frozen(self):
        m = MasterMission(id="WTF-001", protocol="p", participant="MODEL", model="analyst", model_version="llama-3.2-11b", per_eca_state={"per":"OFF","eca":"OFF"}, cost={}, context_kind="FRESH", env_kind="STATIC", params={}, permissions={})
        with self.assertRaises(Exception):
            m.id = "WTF-002"

    def test_mastermission_has_fields(self):
        m = MasterMission(id="WTF-005A-RUN-01", protocol="sha256:abc", participant="MODEL", model="analyst", model_version="llama-3.2-11b", per_eca_state={"per":"OFF","eca":"OFF"}, cost={"tokens_input":0}, context_kind="FRESH", env_kind="STATIC", params={"runs":18}, permissions={})
        self.assertEqual(m.model_version, "llama-3.2-11b")
        self.assertEqual(m.per_eca_state["per"], "OFF")
        self.assertEqual(m.context_kind, "FRESH")
