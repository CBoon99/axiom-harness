# WORKING — Axiom Lab Harness Staging — Active Risks & Gates — 2026-09-26

## Active Known Risks (do not hide)
- **None open** — previous `per_eca_state inner dict mutability` + `AXIOM_ broad` both closed in Phase 1–2 (see below). Remaining risk is only human `EXP-HUMAN-001 80×8D` not yet calibrated (research, not build — starts when pilot subjects exist, never blocks LIVE per plan).

## Closed Risks (Phase 1–3)
- **per_eca_state inner mutability — CLOSED 2026-09-26 Phase 2 `3719d88`:** `axiom_harness/mission.py` `MasterMission.per_eca_state: PerEcaState` now `FrozenDict` `Literal["OFF","ON"]` with `Field(frozen=True)` inner — `m.per_eca_state.per = "ON"` raises `ValidationError: Instance is frozen`, `m.per_eca_state["per"]="ON"` raises `TypeError`. Verified by `tests/test_per_eca_gated.py::test_frozen_inner_immutable` (4 tests). `LOCK-STATUS.json next_authorized_action=PER_OFF_ECA_OFF` + `adapters/per_eca.py ensure_off + gate_ok` keeps `CORPUS ON / PER OFF / ECA OFF` until `ReceiptIndex + Telescope(|R|<=3) + ΔH>0.5 + GateOk` wired (hash-only, no duplicated T_max).
- **AXIOM_ broad allowlist — CLOSED 2026-09-26 Phase 1 `7df9aae`:** `axiom_harness/paths.py ALLOWED_SCRIPT_PREFIXES=["scripts/factory_","AXIOM_WB_"]` only (G10 narrow). `tests/test_allowlist_anchored + test_patches` migrated to `AXIOM_WB_` first, then tighten — `AXIOM_test`/`AXIOM_EVO` now correctly `failed_policy`, `AXIOM_WB_test` passes. G8 `owner:axiom-harness` stayed narrow throughout.

## Narrow Gates Held (G8/G10)
- **G8 owner:axiom-harness:** `axiom_harness/registry.py` asserts `owner == "axiom-harness"` — all events must carry qualifier — held from `f024fee` through `a26399e`.
- **G10 AXIOM_WB_ narrow:** `ALLOWED_SCRIPT_PREFIXES=["scripts/factory_","AXIOM_WB_"]` — held since `7df9aae`, verified `143→147→149` green.

## Verification (final HEAD `a26399e`)
- `PYTHONPATH="$PWD" /Library/Developer/CommandLineTools/usr/bin/python3 -m pytest -q` → **149 passed 0 warnings** (139 Phase 1 base + 4 hallmark `test_receipt_signature` + 4 gated `test_per_eca_gated` + 2 export 22-file `test_export_22_file_pack + test_sha256sum_c`)
- `env PYTHONPATH="$PWD" PATH="/Library/Developer/CommandLineTools/usr/bin:$PATH" bash smoke.sh` → **5/5** (`health jail OK, seal validates, pressure allowlist OK, manifest canonical OK, orphans 0 + ai_computed_metrics:false + sealed_by/at/instrument/sop_version`)
- `B.prev=A` chain — `tests/test_matrix_seals 18cell` + `smoke [5]` — `orphans[]==0` — `ai_computed_metrics:false` hallmarked `sealed_by:harness sealed_at:ISO instrument:axiom_wb|per_eca|evo_eu|future sop_version:1.0-PATCH-ILLUSION`
- `proof/phase1-browser/` — 12-page `1280/390` + `N=5 parallel isolated` (commit `7df9aae`) — file:// `app/index.html 200` `ai_computed_metrics:false`
- `POST /master/export → outputs/EXPORT-001/deliverable.zip` — **22 files** `sha256sum -c manifest-sha256.txt: OK` (`delivery-sheet.csv + verify.html + trail.html + 5-file seal + 8 docs + 3 plot families`) — commit `e6754e1`
- `fresh clone cold-run` — `git clone file://Staging → /tmp/stranger-cold-evidence-1790432499` — `MASTER.md → LAB_GUIDE.md → SETUP one-liner → 149 passed + 5/5 + file:// 200` — green unaided (re-verified Phase 4)

## House Order Current State (for next agent)
- **Plan sealed:** `.agents/plans/2026-09-26-final-build-5033370-live.md` `c55a0ed4: OK` (commit `c6a880a`)
- **Phase 1 `7df9aae`:** env hardening — AXIOM_WB narrow, hallmarks, .python-version 3.9.6, SETUP one-liner, 143 passed + browser 12-page
- **Phase 2 `3719d88`:** PER/ECA gated — FrozenDict, PerConfig/EcaConfig, LOCK-STATUS.json, POST /per+/eca+/seal OFF, 147 passed
- **Phase 3 `e6754e1`:** Export real — VisualConfig Layer 4 `393,216:1` one room, 22-file pack, 149 passed
- **Phase 4 `a26399e`:** Audit §35 A→Z + sync — `HARNESS_AUDIT_2026-09-26.md` read-only trace both directions, who+when hallmarked, `WORKING.md` + `README.md` + `MASTER.md` to `a26399e`, preflight refresh to `a26399e`, final QA `149 passed + 5/5 + cold-run green` — **pushed to origin/main**
- **Deep Dive `HARNESS_TECHNICAL_DEEP_DIVE_2026-09-26.md` (8 agents + critic):** seal ready `SEAL-DEMO-2026-09-26` 5-file canonical hallmarks + 22-file `shasum OK`, `149 passed + 5/5 + cold-run green` multi-agent isolated, code quality `frozen 15 rooms` + hygiene `AXIOM_WB_ + is_safe_relative`, security `jail + allowlist + LOCK-STATUS + frozen`, tech `3.9.6 + pydantic 2.5.0 + Chrome 152`, UX `paper #faf6ef ink #1c1712 12-page`, modular scaling `16 rooms 7 doors 15 POST 1..64`, gaps filled (see deep-dive §8-9 — 20 false-negative unresolved, all non-blocking)
- **Next:** `55b52cf` synced `WORKING.md` to `a26399e` + this deep-dive — lab **LIVE-ready** for first experiments (`POST /master/seal` → `outputs/<RUN>/` → `deliverable.zip`), no Phase 5 tonight, no World-A.

*Updated per House Order §35-36 2026-09-26 Deep Dive — 149 passed — final HEAD 55b52cf.*
