# HARNESS AUDIT — 2026-09-26 — §35 A→Z Read-Only Trace

**Lab:** Axiom Lab Harness (Harness-Master - Dont Touch / Staging) — House Order §35
**Heads:** `c6a880a` (plan seal c55a0ed4) → `7df9aae` (Phase 1) → `3719d88` (Phase 2) → `e6754e1` (Phase 3) — final `e6754e1`
**Status:** READ-ONLY — no maths/thresholds/tests/receipts changed in this file, only trace
**Determinism:** `WTF-005A-HASH-v3` `sort_keys True ensure_ascii False separators (",",":")` SHA-256

## A→Z Trace (REQUIREMENT → EXPERIMENT → METHOD → RUN → RECEIPT → FINDING) — both directions

| # | Requirement (MASTER §) | Experiment | Method (frozen) | Run (outputs/<RUN>/) | Receipt (5-file seal) | Finding / Verdict |
|---|---|---|---|---|---|---|
| 1 | §6 MATRIX_BLOCKED_UNTIL_SWITCH_WIRED — CORPUS ON / PER OFF / ECA OFF | `missions/master_demo_wtf001.yaml` + `LOCK-STATUS.json` next_authorized_action=PER_OFF_ECA_OFF | `axiom_harness/mission.py` `PerEcaState FrozenDict Literal OFF|ON` + `PerConfig/EcaConfig frozen Optional` + `adapters/per_eca.py ensure_off + gate_ok` | `outputs/18cell/WTF-005A-RUN-01..18` + `outputs/TEST-EXPORT-22` | `verify_result.json` `sealed_by:harness sealed_at:ISO instrument:per_eca sop_version:1.0-PATCH-ILLUSION ai_computed_metrics:false orphans:[]` | `PASS` — `per_eca_state inner mutability` closed (FrozenDict), `ensure_off` raises `failed_policy: MATRIX_BLOCKED` on ON, `per/eca` bolt-on stays OFF until GateOk wired (hash-only, no T_max duplication) |
| 2 | §19, §35 G10 AXIOM_ broad → narrow | `tests/test_allowlist_anchored + test_patches` | `axiom_harness/paths.py ALLOWED_SCRIPT_PREFIXES=["scripts/factory_","AXIOM_WB_"]` + `adapters/workbench.py _assert_allowlist anchored on cmd[2]` | `proof/phase1-browser/*.png` (12-page) | `test_allowlist_anchored 5 tests + test_patches 7 tests` | `PASS` — `AXIOM_WB_` narrow, `AXIOM_test`/`AXIOM_EVO` now correctly `failed_policy`, `axiom_wb` + `scripts/factory_*` still pass, G8 `owner:axiom-harness` narrow held |
| 3 | §10, §21 sealed_by/at/instrument/sop_version hallmark — verifiable who+when | `tests/test_receipt_signature.py` | `adapters/workbench|per_eca|evo_eu|future → verify_result.json` adds `sealed_by:harness sealed_at:UTC ISO instrument:axiom_wb/per_eca/evo_eu/future sop_version:1.0-PATCH-ILLUSION` | `outputs/18cell/*/workbench/verify_result.json` + `outputs/TEST-EXPORT-22/*` | `verify_result.json` contains `sealed_by + sealed_at + instrument + sop_version + ai_computed_metrics:false` | `PASS` — 4 hallmark tests `test_workbench/per_eca/evo_eu/future_hallmark` all 4 passed, `sealed_at` ISO8601 `T` present |
| 4 | §15, §19 ENV — CLT python + pydantic pin | `docs/SETUP.md` One-liner + `.python-version` | `.python-version 3.9.6` + `docs/SETUP.md` `PYTHONPATH="$PWD" PATH="/Library/Developer/CommandLineTools/usr/bin:$PATH" /Library/.../python3 -m pytest -q` | `fresh clone /tmp/stranger-cold-evidence-1790432499` | `pytest -q 143→147→149 passed 0 warnings` + `smoke.sh 5/5` (health jail OK, seal validates, pressure allowlist OK, manifest canonical OK, orphans 0) | `PASS` — stranger cold-run `git clone file:// → 143 passed` (Phase 1), `147` (Phase 2), `149` (Phase 3) via exact one-liner, no manual fix, `file:// app/index.html 200` |
| 5 | §24 V1.9 Video + §25/27 V2 Films + §66-67 Observatory — already proven | `app/video.html + films.html + observatory.html` | `VideoConfig + FilmsConfig + ObservatoryConfig frozen` | `outputs/18cell` + `proof/phase1-browser/app-video|films|observatory-1280.png` | `test_video_v19 5 + test_films_v2 5 + test_observatory_external 7` | `PASS` — `127K + 63K + 57K` screenshots, `POST /master/video|films|observatory 201/422` |
| 6 | §51 V2+ External API + V3 Human — already proven | `app/external_api.html + human.html` | `ExternalAPIConfig + HumanConfig frozen` | `proof/phase1-browser/app-external_api|human-1280.png` | `test_human_v3 5 + test_export 3→5` | `PASS` |
| 7 | §22 V2 Visual Layer 4 — 393,216:1 one room, not World-A | `docs/BRIEF_REVOLUTIONARY_V2_PATCH_IS_ONE_ROOM.md` | `axiom_harness/mission.py` `VisualConfig layer:4 compression_ratio:393216 frozen Optional` — verified `app/` vs `world-a/` isolated | `outputs/TEST-EXPORT-22` + `missions/master_demo_wtf001.yaml` | `VisualConfig enabled True layer 4` test via `MasterMission(visual=VisualConfig)` | `PASS` — Layer 4 isolated, no World-A contamination, `test 149` green |
| 8 | §22, §29 Export 22-file pack — `sha256sum -c manifest-sha256.txt` | `api/main.py POST /master/export` | `api/main.py` generates 22 canonical files `SCENARIO.json … plot_gallery/plot1..3.svg` + `delivery-sheet.csv` + `MANIFEST.json` + `deliverable.zip` + `manifest-sha256.txt` | `outputs/EXPORT-001/deliverable.zip (22 files) + manifest-sha256.txt` | `test_export_v1 5 tests` — `test_22_file_pack 22 + test_sha256sum_c OK` | `PASS` — `deliverable.zip: OK` via `shasum -a 256 -c`, `B.prev=A` preserved |
| 9 | §14, §62 Parallel + §24 branch — already proven | `app/wireframes/*.html` | `ParallelConfig 1..64` | `proof/phase1-browser/parallel-1..5-1280.png` (N=5 isolated) | `test_parallel_v12 + test_multi_agent_v18 6` | `PASS` — 5× isolated sessions, no shared state |

## Reverse Trace (FINDING → RECEIPT → RUN → METHOD → EXPERIMENT → REQUIREMENT)

* `147→149 passed` → `tests/test_per_eca_gated.py + test_export_v1 22-file` → `axiom_harness/mission.py PerEcaState + VisualConfig` → `missions/master_demo_wtf001.yaml` + `LOCK-STATUS.json` → `§6, §19, §22`
* `proof/phase1-browser/*.png 17 files` → `agent-browser` `file:// app/index.html 200` → `app/*.html 7 + wireframes 5` → `§24-27, §66-67`
* `outputs/EXPORT-001/manifest-sha256.txt: OK` → `api/main.py POST /master/export 22 files` → `§22 Export`
* `LOCK-STATUS.json next_authorized_action=PER_OFF_ECA_OFF` → `adapters/per_eca.py ensure_off + gate_ok` → `§6`
* `B.prev=A chain` verified via `tests/test_matrix_seals.py 18cell` + `smoke.sh [5] orphans[]==0` → `§12, §19`

## Sealed By/At (who+when) — hallmarked receipts

* Every `verify_result.json` now carries `sealed_by:harness` + `sealed_at:ISO8601 UTC` + `instrument:axiom_wb|per_eca|evo_eu|future` + `sop_version:1.0-PATCH-ILLUSION` — verified by `test_receipt_signature.py 4 tests`
* `LOCK-STATUS.json` — `sealed_by:harness sealed_at:2026-09-26T22:30:00Z instrument:harness`
* `HARNESS_PREFLIGHT_2026-09-26.json` — `qa_proof_refreshed: 2026-09-26 §33-36` → refreshed to `e6754e1` in this audit (see proof/)

## Orphans / ai_computed_metrics / B.prev=A

* `orphans[]==0` — `smoke.sh [5]` + `test_matrix_seals 18cell` + `verify_result.json orphans:[]`
* `ai_computed_metrics:false` — every receipt `Literal[False]` enforced, `grep -r` shows only `False` in `axiom_harness/` (no AI in engine)
* `B.prev=A` — `MANIFEST.json` hashes `sort_keys True`, `write_manifest` canonical, `test_matrix_seals` chain per cell

## Evidence Files (read-only)

* `proof/phase1-browser/*.png` — 12-page `1280/390` + `N=5 parallel` (commit `7df9aae`)
* `proof/HARNESS_PREFLIGHT_2026-09-26.*` — refreshed to `e6754e1` + this audit
* `outputs/EXPORT-001/deliverable.zip + manifest-sha256.txt` — `22 files, sha256sum -c OK` (commit `e6754e1`)
* `LOCK-STATUS.json` — `PER_OFF_ECA_OFF` (commit `3719d88`)
* `.agents/plans/2026-09-26-final-build-5033370-live.md.sha256 → c55a0ed4: OK`

## Stop Condition

**Phase 4 audit green — §35 A→Z trace complete both directions, who+when hallmarked, 149 passed + 5/5 + cold-run re-verified (see below), orphans 0, B.prev=A, no Phase 5, no World-A, no commercial repo — ready for `push live` on your confirm.**

*Audit performed read-only — no maths/thresholds/tests/receipts modified in this file.*
