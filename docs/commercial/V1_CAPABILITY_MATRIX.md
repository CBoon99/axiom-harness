# V1 CAPABILITY MATRIX — AXIOM HARNESS
**V1 scope:** `PLAN_V1.md` + `PROJECT_PROFILE V1` — only these 8 are V1 commercial deliverables.

| # | Capability | What V1 does | Evidence |
|---|------------|--------------|----------|
| 1 | **CONTROL** | Define experiment, model, context, environment, information sources, permissions, schedule, parallel via frozen `MasterMission` (`WTF-001` hash) | `axiom_harness/mission.py` `frozen=True`, `missions/master_demo_wtf001.yaml` |
| 2 | **SANDBOX** | Keep runs isolated and governed (terminal substrate, jail `is_safe_relative`, `ALLOWLIST` anchored on `cmd[2]`) | `axiom_harness/paths.py`, `tests/test_jail_canonical.py` |
| 3 | **RUN / SEQUENCE / PARALLEL** | Run controlled experiments and repeated/parallel conditions (One/Sequence/All/Parallel) | `tests/test_parallel_v12.py` `test_lvm_pause_live_scalable.py` |
| 4 | **LIVE ROOM** | Compare multiple actors/models/humans under controlled context | `tests/test_live_v17.py` |
| 5 | **TIMELINE** | Preserve event order and execution history (scrubbable, synchronised replay) | `axiom_harness/watcher.py`, `tests/test_lvm_pause_live_scalable.py` |
| 6 | **SEALED EVIDENCE** | Produce canonical evidence seal and provenance record (5-file `SCENARIO.json/scenario.csv/DECISION_SUMMARY.json/MANIFEST.json/verify_result.json`, chain `B.prev=A`, `ai_computed_metrics:false`) | `axiom_harness/manifest.py`, `tests/test_manifest_canonical.py`, `test_seal_gate.py` |
| 7 | **EXPORT** | Produce documented evidence/export pack | `tests/test_matrix_seals.py` (now generating `outputs/18cell`) |
| 8 | **GOVERNED UPSTREAM ACTORS** | Harness can execute upstream modules such as `ECA/PER` without taking ownership of their internal mathematics (`per:OFF/eca:OFF` transport, `MOCK` explicitly `MOCK`, `per_eca_state` hash) | `axiom_harness/adapters/per_eca.py` `ensure_off`, `tests/test_harness_boundary.py` 12 tests |

**Not V1 (future, not in V1 promise):** `V1.8 Multi-agent (Analyst/Critic/Maker)`, `V1.9 Patch Illusion Visual (224→14→768→576 tokens receipt)`, `V2/V3 Human Axiom` — all modular rooms after V1.

Each capability maps to existing Harness machinery; no new duplicated upstream mathematics.
