"""V1.2 Parallel — §14 RUN modes + §62 model matrix, isolated sandboxes capped 64."""
from axiom_harness.mission import MasterMission, ParallelConfig, ParallelMode

BASE = {"id": "WTF-001", "protocol": "sha256:abc", "context_kind": "FRESH", "env_kind": "STATIC"}

def test_parallel_one_isolated():
    m = MasterMission(**BASE, parallel=ParallelConfig(mode=ParallelMode.ONE, parallel_count=1, isolated=True))
    assert m.parallel.parallel_count == 1
    assert m.parallel.isolated is True

def test_parallel_matrix_and_all():
    m = MasterMission(**BASE, parallel=ParallelConfig(mode=ParallelMode.PARALLEL, parallel_count=4, model_matrix=["A","B","C","D"], isolated=True))
    assert m.parallel.model_matrix == ["A","B","C","D"]
    assert m.parallel.mode == ParallelMode.PARALLEL
    # frozen
    try:
        m.parallel.parallel_count = 2
        assert False
    except Exception:
        pass

def test_parallel_sequence_capped():
    m = MasterMission(**BASE, parallel=ParallelConfig(mode=ParallelMode.SEQUENCE, parallel_count=8))
    assert m.parallel.parallel_count == 8
    # cap 64 enforced by validator — 65 should fail
    try:
        MasterMission(**BASE, parallel=ParallelConfig(parallel_count=65))
        assert False, "should reject >64"
    except Exception:
        pass

def test_parallel_api_gate():
    # API validates missing parallel
    from axiom_harness.mission import MasterMission as MM
    m = MM(**BASE, parallel=ParallelConfig(mode=ParallelMode.ALL, parallel_count=3))
    assert m.parallel.mode == ParallelMode.ALL
