# MATH MODULAR MAP — REGISTRY ONLY (not source of truth)
**Gate 2 — 2026-09-24 — Staging only, Master frozen**
**Single hash contract:** `sort_keys True, ensure_ascii False, separators (",",":")` no indent — `WTF-005A-HASH-v3` via `axiom_harness/manifest.py:15`

This map does **not** duplicate upstream mathematics. It records **what Harness knows** about each upstream: identity, version, hash, interface, status. Formulas/thresholds remain owned by upstreams — Harness only records hashes.

## Upstream Registry — actual committed state + hashes + interfaces

| PROJECT | OWNER | CANONICAL_FILE | IMPLEMENTATION_HASH (sha256:16) | CONFIG_HASH | VERSION | INTERFACE | STATUS |
|---------|-------|----------------|----------------------------------|-------------|---------|-----------|--------|
| **Evidence Axiom** | Axiom Evidence Layer | `docs/gap-review/harness/living_gap_review_score.py` | `60c94d95173a34ab` | scorer `0.1.0` `evidence_layer_freeze_retrieval_v1` | 0.1.0 | `FreezeEvidenceIndex, scorer_version` | **UPSTREAM-BLOCKED** — not Harness-certified (see `WORKING.md` BML Quad Frozen Evaluator) |
| **PER** | `Axiom PER (Progressive Evidence Retrieval)` | `PER-Core/sim/telescope.py` | `7ae692a5cfbe5fcf` | UNKNOWN — no separate committed config audited (weights in code `HYPOTHESIS_WEIGHTS`) | UNKNOWN | `Telescope(index).score_probes()` | **UPSTREAM-BLOCKED** — do not certify clean based on Harness readings |
| **ECA** | `Axiom Evidence Layer/ECA` | `ECA/sim/telescope.py` | `bf7329c836d8b820` | UNKNOWN — prior `ECA/plugin/eca_config.json` was Harness-created competing config (deleted `rm` 2026-09-24); ECA owns canonical, not Harness | UNKNOWN (ECA/spec `1.2`) | `Telescope + GateOk + FALSIFY P2 + evidence_gate` | **UPSTREAM-BLOCKED** — unresolved reproducibility/dependency per ECA V1 §12 (do NOT certify clean; Harness records boundary only) |
| **Future Workbench** | `Axiom-Workbench` | `axiom_wb/pipeline.py` | `e8fbd398675f7112` | `seal_pair B.prev=A` via `manifest.py:20` | UNKNOWN | `python3 -m axiom_wb evaluate` | **UPSTREAM-BLOCKED** — read-only, not Harness-certified |
| **EvoCycles** | `World-A-EvoCycles` | `WORLD-A/*` | UNKNOWN — NOT AUDITED (no hash computed this gate) | UNKNOWN | UNKNOWN | `harness_ ids, B-0 physics` | UNKNOWN — NOT AUDITED |
| **Testing Harness** | `Axiom Harness` | `WTF-005A/B/LAB` | UNKNOWN | UNKNOWN | UNKNOWN | `EU-01…06 6A loop` | UNKNOWN — NOT AUDITED |
| **Epistemic-UX** | `Epistemic-UX-Stress-Harness` | `EU-01…06` | UNKNOWN | UNKNOWN | UNKNOWN | `6A loop` | UNKNOWN — NOT AUDITED |

**For formulas/thresholds/weights/gates:** REFERENCE upstream owner — see `ECA/sim/telescope.py:101-162` for `GateOk`, `PER-Core/sim/telescope.py:18` for `IG`, `Axiom-Workbench/baselines.py` for `EMA span20` etc. — **no threshold in this map becomes Harness-authoritative**. No `ECA maths`, `PER maths`, `Evidence Axiom maths`, `Future maths` reproduced as Harness logic.

## Harness Orchestration Registry — Harness-owned (LOAD/CONFIGURE/FREEZE/RUN/RECORD/SEAL)

| HARNESS CONFIG | CODE LOCATION | HASHED VIA | STATUS |
|----------------|---------------|------------|--------|
| `ScheduleConfig` `ONCE/INTERVAL/REPEATING/CONTINUOUS/UNTIL/CRON` | `axiom_harness/mission.py:ScheduleConfig` | `MasterMission protocol` `WTF-005A-HASH-v3` | HARNESS-OWNED `frozen=True` |
| `ParallelConfig` `ONE/SEQUENCE/ALL/PARALLEL 1..64` | `mission.py:ParallelConfig` | `protocol` | HARNESS-OWNED |
| `DataConfig` `CSV/JSON/.../VIDEO` jail | `mission.py:DataConfig` | `protocol` | HARNESS-OWNED |
| `LanguageConfig` 10 codes | `mission.py:LanguageConfig` | `protocol` | HARNESS-OWNED |
| `AudioConfig` 6 kinds | `mission.py:AudioConfig` | `protocol` | HARNESS-OWNED |
| `SensorConfig` 6 kinds | `mission.py:SensorConfig` | `protocol` | HARNESS-OWNED |
| `LiveConfig` 6 feeds | `mission.py:LiveConfig` | `protocol` | HARNESS-OWNED |

Harness **does not** own upstream thresholds — it only records `IMPLEMENTATION_HASH` + `CONFIG_HASH` received from upstream via `adapters/per_eca.py` transport. No duplicated ECA/PER maths remains in `axiom_harness/` (verified `rg GateOk → 0 hits` in Harness `axiom_harness/*.py`).
