"""V1.6 Sensors — §28 identity/source/timestamp/permission/status/policy/schema."""
from axiom_harness.mission import MasterMission, SensorConfig, SensorKind

BASE = {"id": "WTF-001", "protocol": "sha256:abc", "context_kind": "FRESH", "env_kind": "STATIC"}

def test_sensors_kinds_and_policy():
    m = MasterMission(**BASE, sensors=SensorConfig(kinds=[SensorKind.DIGITAL, SensorKind.AI], recording_policy="ALWAYS"))
    assert SensorKind.DIGITAL in m.sensors.kinds
    assert m.sensors.recording_policy == "ALWAYS"

def test_sensors_physical_iot_human():
    m = MasterMission(**BASE, sensors=SensorConfig(kinds=[SensorKind.PHYSICAL, SensorKind.IOT, SensorKind.HUMAN], identities=["mic-01","cam-02"], recording_policy="ON_EVENT", data_schema="sensor:v1"))
    assert "mic-01" in m.sensors.identities
    assert m.sensors.data_schema == "sensor:v1"

def test_sensors_frozen():
    m = MasterMission(**BASE, sensors=SensorConfig(kinds=[SensorKind.ENVIRONMENTAL]))
    try:
        m.sensors.kinds.append(SensorKind.AI)
        assert False
    except Exception:
        pass
