# HARNESS PREFLIGHT — 2026-09-26 — READ-ONLY

**Lab:** Axiom Lab Harness (Harness-Master - Dont Touch / Staging) — Governance House-Order Preflight
**Standard:** Could a stranger enter tomorrow and run without Carl explaining verbally?
**Safety:** READ-ONLY — no maths/thresholds/tests/receipts changed, no deploy/push.

## 1. Authoritative Root
- **Harness root:** `/Users/carlboon/Documents/Axiom Harness-Master - Dont Touch/Staging`
- **Parent product:** `Axiom Lab Harness` (siblings: `Documents/Axiom-Workbench/`, `Documents/Axiom Future/`, `Documents/Axiom Evidence Layer/`, `Documents/world-a/`)
- **Harness root discovery:** `STAGING_ROOT = Path(__file__).resolve().parents[1]` + assert `axiom_harness/` + `missions/` structure exists (not name substring — fixed 522b4fd)
- **Git:** `origin https://github.com/CBoon99/axiom-harness` — HEAD `a26399e6a7c876a3ce60550952c38bb4406dc593` `a26399e Tidy — docs: LAB_GUIDE + how to use/setup/data/test/output/naming` (149 passed, 0 warnings) — ahead 0 on `origin/main`, `Everything up-to-date` at this preflight — previous `f024fee Hardening — registry gate owner:axiom-harness`
- **Current HEAD log:** `5c88711` ← `f024fee` ← `edaf935 Noise fix` ← `c4cddcc V3 Human` ← `b99f059 Sync` ← `5f99870 Export` ← `58c8d11 V2+` ← `4a172ec V2` ← `041b12f V1.9` ← `9412cde Polish` ← `ff5cc63 V1.8.1` ← `d479fe9 V1.8`

## 2. Estate Counts (read-only)
- **File count:** 320 (find . -not -path .git/.pytest_cache/.netlify/__pycache__ -type f) — was 26,490 in prior full-disk count
- **Directory count:** 85 — was 2,686 full-disk
- **Tree count:** 406 entries (CURRENT_TREE→PROPOSED_TREE, 402→406)
- **Relevant hashes (sha256 16-char):**
  - `axiom_harness/mission.py 15541bb7ad94bb12`
  - `axiom_harness/manifest.py bf6edb0f073d1c38`
  - `axiom_harness/paths.py 8281e6ae9574f4da`
  - `api/main.py c110248424674b89`
  - `app/index.html 23186fa253343a83`
  - `Working master hashes:` `math/HARDENED_LOCKS.md 71e3be70`, `PER_ECA 5bb83c6e`, `WTF dc78ac17`, `WTF-005A-HASH-v3 sort_keys True ensure_ascii False separators (",",":")`

## 3. Roots
- **Execution entry points:** `app/index.html` + `app/multi_agent.html` + `app/video.html` + `app/films.html` + `app/observatory.html` + `app/external_api.html` + `app/human.html` + `api/main.py` (`HARNESS_PORT` `HTTPServer` `H`) + `missions/master_demo_wtf001.yaml`
- **Test roots:** `tests/` — 22 files: `test_per_eca_gated.py, test_receipt_signature.py` added: `test_allowlist_anchored.py, test_audio_v15.py, test_data_v13.py, test_export_v1.py, test_films_v2.py, test_gateway.py, test_harness_boundary.py (12), test_health_honesty.py, test_human_v3.py (5), test_jail_canonical.py, test_language_v14.py, test_live_v17.py, test_lvm_pause_live_scalable.py, test_manifest_canonical.py, test_manifest.py, test_matrix_seals.py (18cell), test_multi_agent_v18.py (6), test_no_touch.py, test_observatory_external_v2plus.py (7), test_parallel_v12.py` — plus `test_video_v19.py`
- **Experiment roots:** `missions/` (e.g. `missions/master_demo_wtf001.yaml`), `outputs/` (sealed runs: `_HARNESS_ECA_GATED_2026-09-24`, `18cell/WTF-005A-RUN-01..18`, `smoke_001`, `EXPORT-001`, `demo`)
- **Evidence / receipt roots:** `outputs/` (5-file `SCENARIO.json+scenario.csv+DECISION_SUMMARY+MANIFEST+verify_result` per run + `deliverable.zip` + `manifest-sha256.txt` + `verify.html` + `trail.html`), `proof/` (preflight + organisation reports)
- **Archive roots:** `archive/Favorable-errors-2026-09-24/` (10 files) + `archive/README.md` — populated in §33 sweep (docs/AI_ERROR_* retained canonical), `outputs/18cell` + `outputs/_HARNESS_ECA_GATED` remain in place per §14 (do not move hashes)
- **Documentation roots:** `docs/` (20+ md: `ARCHITECTURE.md, PLAN_V1.md, DB_SCHEMA.md, API_SPEC.md, HANDOFF_2026-09-24_FULL_ACCOUNT.md, HARNESS_BOUNDARY_AUDIT, HARNESS_V1_FINAL_ACCEPTANCE` etc), `Staging/docs/BEST_PRACTICE_LAB_SYSTEMS_2026-09-26.md`, `docs/WTF_SEQUENTIAL_INTELLIGENCE_BRAINSTORM_2026-09-23.md`, `docs/CANONICAL_WIREFRAMES.md`, `README.md, PROJECT_PROFILE.md, WORKING.md, MEMORY.md`
- **Configuration roots:** `axiom_harness/mission.py` (`MasterMission` frozen 11 rooms), `axiom_harness/manifest.py` (`WTF-005A-HASH-v3`), `axiom_harness/paths.py` (`is_safe_relative iterative unquote, ALLOWED_SCRIPT_PREFIXES`), `axiom_harness/registry.py` (`REGISTRY 7 doors + owner:axiom-harness`), `AXIOM_STRICT_MODE` env
- **Generated-output roots:** `outputs/` (gitignored), `Complete-Report-Pack/` (empty until export), `/tmp/full11-* + /tmp/v18*` (headless screenshots 4.6K–190K, 22 images)
- **Temporary/working roots:** `/tmp` (`full11-*.png`, `human*.png`), `/tmp/preflight_*`

## 4. Current Test Status (real run, no new logic)
- **Command:** `PYTHONPATH="$PWD" /Library/Developer/CommandLineTools/usr/bin/python3 -m pytest -q`
- **Result:** `149 passed in 0.52s` (149 = 108 V1.1-V1.7 + 6 V1.8 + 5 V1.9 + 5 V2 + 7 V2+ + 3 Export + 5 Human + boundary), `0 warnings` after `edaf935 protected_namespaces=()`
- **Smoke:** `env PYTHONPATH="$PWD" PATH="/Library/Developer/CommandLineTools/usr/bin:$PATH" bash smoke.sh` → `5/5` (`health jail OK, seal validates, pressure allowlist OK, manifest canonical OK, orphans 0 + ai_computed_metrics:false`) — verified at 07:41 and 10:11

## 5. Current Git/Repository State
- **HEAD:** `5c8871190b49ccec8833ae7a0f34247cbc4eab4b` (`5c88711`) — refreshed from `f024fee` for §33-36 sweep
- **Remote:** `origin https://github.com/CBoon99/axiom-harness` — `f024fee..5c88711 main → main` (pushed), next will be §33-36 governance commit
- **Dirty (before §33 sweep):** `Favorable errors/AI_ERROR_* (8 csv/md)` was duplicate of `docs/AI_ERROR_*` — now resolved to `archive/Favorable-errors-2026-09-24/` (10 files, git mv). Remaining `docs/*.md` + `math/` classified `KEEP` (existence logs)

## 6. Deployment Status (detectable)
- **Staging local:** `file://` headless via `agent-browser 0.34.0 / Chrome 152` — `doctor 8 pass` with `require_escalated` (without = `Operation not permitted` on socket)
- **Netlify world-a:** `https://world-a.netlify.app` — live per `world-a/README.md`, not `curl`-verified for stub drift in this preflight (unresolved, §35 K)
- **Axiom Workbench engine:** `../Axiom-Workbench/axiom_wb` read-only at `Path(__file__).parents[1]`, `AXIOM_ENGINE_ROOT` override only if `AXIOM_STRICT_MODE=0`

## 7. Documentation State
- **Authoritative briefs:** `AXIOM HARNESS Brief (1).md 3172 lines` + `Copy LVM addition 4122 lines` (`+950 Patch Illusion Lab` as one room) — 79 sections + LVM as one room, not second spec
- **Indexes:** `docs/PLAN_V1:26` mirrors 9 rooms, `mission.py MasterMission frozen`, `METHOD.md/STATUS.md` per experiment not yet standardized — will be `EXP-<DOMAIN>-<NNN>` going forward per House Order §7
- **Naming today:** Historical `WTF-001 + HUMAN-2026` + new `EXP-*` future — drift noted, will keep historical as `HISTORICAL` per §15

## 8. Obvious Orphan/Duplicate/Obsolete (read-only audit — refreshed §33)
- **Duplicates resolved:** `docs/AI_ERROR_* (8)` vs `Favorable errors/AI_ERROR_* (8)` byte-identical (SHA 23fcceb9, faaf30d1, 51ac3a68, a504b914, bf6bc757, 032afed8, 96b85fee, 733e7898) → moved `Favorable errors/` → `archive/Favorable-errors-2026-09-24/` (10 files, git mv), canonical `docs/AI_ERROR_*` retained. Historical `Axiom Harness Brief (1).md` vs `(2).md` identical `0a0d0502` kept HISTORICAL per §15.
- **Orphans:** 0 active (`verify.py orphan[]==0, smoke 5/5`) — see `archive/README.md` intentional duplicates (`math/HARDENED_LOCKS.md` x3 71e3be70 `math/*/EXISTS.md` x5)
- **Stale:** `docs/wireframes` vs `app/wireframes` drift resolved 2026-09-26
- **No deletions** — archive preserves history via `git mv`, see `HARNESS_HOUSE_ORDER_CHANGELOG.md` + `HARNESS_ORGANISATION_REPORT_2026-09-26.md`

## 9. Read-Only Confirmation
No files moved, no maths changed, no tests altered, no receipts rewritten, no push — this file is the preflight evidence.
