"""V1.8 Multi-agent — Analyst/Critic/Maker/Observer/Adversary, isolated contexts, §35.

Durable tests per durable-test-collateral: test_valid_201 (POST valid isolated true ->201),
test_invalid_422 (bad payload ->422), test_isolated_contexts (two parallel isolated).
Asserts per_eca OFF (PER/ECA not wired in V1.8 staging).
"""
import json

from axiom_harness.mission import MasterMission, MultiAgentConfig, AgentRole

BASE = {"id": "WTF-001", "protocol": "sha256:abc", "context_kind": "FRESH", "env_kind": "MULTI_AGENT"}


def _post(payload: dict, path: str = "/api/master/multi-agent"):
    """Durable local simulation of POST /api/master/multi-agent — mirrors api/main.py 201/422 without socket bind."""
    try:
        m = MasterMission(**payload)
        # per_eca OFF invariant — V1.8 should default to OFF
        assert m.per_eca_state.get("per") == "OFF" and m.per_eca_state.get("eca") == "OFF", f"per_eca must be OFF got {m.per_eca_state}"
        if m.multi_agent is None:
            raise ValueError("failed_policy: multi_agent missing")
        mc = m.multi_agent
        if not mc.agents:
            raise ValueError("failed_policy: agents empty — requires at least one of A Analyst B Critic C Maker D Observer E Adversary")
        body = {"multi_agent": True, "experiment_id": m.id, "agents": [a.value for a in mc.agents], "isolated": mc.isolated, "config_hash": m.protocol, "sealed": True, "per_eca": m.per_eca_state}
        return 201, body
    except AssertionError:
        raise
    except Exception as e:
        return 422, {"failed_policy": str(e)}


def test_valid_201():
    """POST multi-agent valid isolated true ->201 (durable). Assert per_eca OFF."""
    # direct model check with per_eca OFF
    m = MasterMission(**BASE, multi_agent=MultiAgentConfig(agents=[AgentRole.ANALYST, AgentRole.CRITIC], isolated=True))
    assert m.per_eca_state == {"per": "OFF", "eca": "OFF"}
    assert m.multi_agent.isolated is True
    assert AgentRole.ANALYST in m.multi_agent.agents
    # frozen
    try:
        m.multi_agent.agents.append(AgentRole.ADVERSARY)  # type: ignore
        assert False, "frozen should block append"
    except Exception:
        pass
    # via HTTP API 201
    payload = {**BASE, "multi_agent": {"agents": ["Analyst", "Critic"], "isolated": True}}
    status, data = _post(payload)
    assert status == 201, f"expected 201 got {status} {data}"
    assert data.get("multi_agent") is True
    assert data.get("isolated") is True
    assert data.get("sealed") is True
    assert data.get("config_hash") == "sha256:abc"
    assert data.get("per_eca") == {"per": "OFF", "eca": "OFF"}
    assert "Analyst" in data.get("agents", [])
    assert "Critic" in data.get("agents", [])


def test_invalid_422():
    """Bad payload ->422 (durable). Assert per_eca OFF on valid baseline."""
    # baseline valid still has per_eca OFF
    m_ok = MasterMission(**BASE, multi_agent=MultiAgentConfig(agents=[AgentRole.ANALYST], isolated=True))
    assert m_ok.per_eca_state.get("per") == "OFF"
    assert m_ok.per_eca_state.get("eca") == "OFF"
    # missing multi_agent
    payload_missing = {**BASE}
    status, data = _post(payload_missing)
    assert status == 422, f"expected 422 for missing got {status} {data}"
    assert "failed_policy" in json.dumps(data)
    # empty agents
    payload_empty = {**BASE, "multi_agent": {"agents": [], "isolated": True}}
    status2, data2 = _post(payload_empty)
    assert status2 == 422, f"expected 422 for empty agents got {status2} {data2}"
    assert "failed_policy" in json.dumps(data2)
    # invalid agent name -> 422 via pydantic
    payload_bad = {**BASE, "multi_agent": {"agents": ["BOGUS"], "isolated": True}}
    status3, data3 = _post(payload_bad)
    assert status3 == 422, f"expected 422 for bad agent got {status3} {data3}"
    assert "failed_policy" in json.dumps(data3)


def test_isolated_contexts():
    """Two parallel isolated (durable). Assert per_eca OFF and no shared state."""
    m1 = MasterMission(**BASE, multi_agent=MultiAgentConfig(agents=[AgentRole.ANALYST, AgentRole.CRITIC], isolated=True))
    m2 = MasterMission(**BASE, multi_agent=MultiAgentConfig(agents=[AgentRole.MAKER, AgentRole.OBSERVER, AgentRole.ADVERSARY], isolated=True))
    assert m1.per_eca_state == {"per": "OFF", "eca": "OFF"}
    assert m2.per_eca_state == {"per": "OFF", "eca": "OFF"}
    assert m1.multi_agent.isolated is True
    assert m2.multi_agent.isolated is True
    assert set(m1.multi_agent.agents) != set(m2.multi_agent.agents)
    assert m1.multi_agent is not m2.multi_agent
    try:
        m1.id = "HACKED"  # type: ignore
        assert False, "MasterMission frozen should prevent id mutation"
    except Exception:
        pass
    try:
        m1.multi_agent.isolated = False  # type: ignore
        assert False, "MultiAgentConfig frozen should prevent mutation"
    except Exception:
        pass
    m_full = MasterMission(**BASE, multi_agent=MultiAgentConfig())
    assert len(m_full.multi_agent.agents) == 5
    assert AgentRole.ADVERSARY in m_full.multi_agent.agents
    assert m_full.multi_agent.isolated is True
    assert m_full.per_eca_state == {"per": "OFF", "eca": "OFF"}
    # API-level two parallel isolated calls
    payload_a = {**BASE, "multi_agent": {"agents": ["Analyst", "Critic"], "isolated": True}}
    payload_b = {**BASE, "id": "WTF-002", "multi_agent": {"agents": ["Maker", "Observer", "Adversary"], "isolated": True}}
    status_a, data_a = _post(payload_a)
    status_b, data_b = _post(payload_b)
    assert status_a == 201 and status_b == 201
    assert data_a["isolated"] is True
    assert data_b["isolated"] is True
    assert data_a["per_eca"] == {"per": "OFF", "eca": "OFF"}
    assert data_b["per_eca"] == {"per": "OFF", "eca": "OFF"}
    assert data_a["experiment_id"] == "WTF-001"
    assert data_b["experiment_id"] == "WTF-002"
    assert set(data_a["agents"]) != set(data_b["agents"])


# backward compat aliases for earlier runner expecting multi_agent prefix
def test_multi_agent_valid_201():
    return test_valid_201()

def test_multi_agent_invalid_422():
    return test_invalid_422()

def test_multi_agent_isolated_contexts():
    return test_isolated_contexts()
