# MATH MODULAR MAP — V3 Freeze (no hardcoded burial)
**Single hash contract:** `sort_keys True, ensure_ascii False, separators (",",":")` no indent — `WTF-005A-HASH-v3` via `axiom_harness/manifest.py:15` + `api/main.py:17`

| Component | Formula / Code Location | Constant | Threshold | Weight | Config Source |
|-----------|------------------------|----------|-----------|--------|---------------|
| **Evidence Axiom** `living_gap_review_score.py:SCORER_VERSION 0.1.0` | `evidence_layer_freeze_retrieval_v1` — docs-only hash, CLAIMS.json excluded | — | — | — | `FreezeEvidenceIndex` + `scorer_version` frozen |
| **Future Workbench** `seal_pair` `B.prev=A` | `axiom_harness/manifest.py:20` chain pointer | — | — | — | `protocol/hash_contract.py` |
| **PER Telescope** `PER-Core/sim/telescope.py:18` | `IG = log2(Nb/Na)`, descend if `|R|≤3 OR weight≥75 OR entropy≥4` (OR gate) — **owned by PER, not Harness** | `HYPOTHESIS_WEIGHTS {1:0.1..6:60}, desc_candidates 3, weight 75, entropy 4, bonus 8, ent*1.5 cap95, layers >20/5/3` — **PER canonical** | `min_candidates 3` | `weight 75` | **PER owns** `Telescope(descend_threshold_*)` — Harness records hash only |
| **ECA Telescope** `ECA/sim/telescope.py:101-162` | `GateOk = |R|≤3 && ΔH>0.5 && sealed+hash && FALSIFY P2 && discrimination` (AND gate) — **owned by ECA, not Harness** | `ALLOWED_AXES 12, ε=max(0.05,1/|Rt|), T_max(N)=ceil(log2(N/3))+4` — **ECA canonical** | `min_delta_h 0.5` | `K values 60,30…` | **ECA owns** thresholds via `ECA/plugin/eca_config.json` (removed competing Harness copy) — Harness records `ECA_CONFIG_HASH` only |
| **PER-IG** passive tachometer | `ΔH` measured, no gate | — | — | — | read-only |
| **EvoCycles** nested worlds | `harness_` ids, `B-0` physics, `WORLD-A` | — | — | — | `World-A-EvoCycles` repo |
| **Testing / Epistemic** `WTF-005A/B/LAB` `EU-01…06` | 6A loop (ask → probe → evidence → interpret → report → reflect) | `S0→S1→S2 branching` | `NUM_RE orphan check` | — | `Harness mission.py:Schedule/Parallel` |
| **Harness Schedule** `mission.py:ScheduleConfig` | `ONCE/INTERVAL/REPEATING/CONTINUOUS/UNTIL/CRON` | `interval>0` | `repeats>0` for REPEATING | — | `ScheduleConfig frozen` + `POST /api/master/schedule 422` |
| **Harness Parallel** `mission.py:ParallelConfig` | `ONE/SEQUENCE/ALL/PARALLEL` | `parallel_count 1..64` | `64 cap` | `model_matrix [A-D]` | `ParallelConfig frozen` |
| **Harness Data** `mission.py:DataConfig` | `CSV/JSON/TEXT/DOCS/DATASET/IMAGES/AUDIO/VIDEO` | — | `sources non-empty` | — | `DataConfig + jail is_safe_relative` |
| **Harness Language/Audio/Sensors/Live** | `LanguageCode 10, AudioSourceKind 6, SensorKind 6, LiveFeedKind 6` | — | `primary not in variants` | — | each `frozen=True` + `POST 201/422` |

All constants hash via `MasterMission protocol` — changing any threshold creates new `id`, not silent patch. Harness never reimplements `axiom_wb/metrics`.
