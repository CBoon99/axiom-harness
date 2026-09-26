# HARNESS ORGANISATION REPORT — 2026-09-26 — House Order §36

**Date:** 2026-09-26 — **HEAD:** `5c8871190b49ccec8833ae7a0f34247cbc4eab4b` (`5c88711`) — **Base for sweep:** `5c88711 Tidy — docs: LAB_GUIDE + how to use/setup/data/test/output/naming` (139 passed, smoke 5/5)
**Standard:** Could a stranger enter tomorrow and run without Carl explaining verbally? (`MASTER.md → INDEX.md/json → LAB_GUIDE.md`)

## 1. Before / After Tree
- **Before (CURRENT_TREE.txt):** 402 entries (find . -not -path .git/.pytest_cache/.netlify/__pycache__ | sort) — includes `Favorable errors/` at root (space in name, 10 files, 8 duplicates of `docs/AI_ERROR_*` SHA-identical).
- **After (PROPOSED_TREE.txt):** 406 entries — `Favorable errors/` → `archive/Favorable-errors-2026-09-24/` (11 entries: 10 files + archive/README.md) + new `WORKING.md` + `HARNESS_ORGANISATION_REPORT*` + changelog.
- **Net:** `+4` (archive/README + WORKING + 2 reports), 0 deletions (archive preserves).

## 2. §33 Old-Files & Duplicate Audit (§33)

### Duplicates — classified
- **DUPLICATE resolved:** `docs/AI_ERROR_* (8)` ↔ `Favorable errors/AI_ERROR_* (8)` — SHA identical per pair (23fcceb9, faaf30d1, 51ac3a68, a504b914, bf6bc757, 032afed8, 96b85fee, 733e7898) + `ABSOLUTE_FULL_REPORT.md` + `TABLE_OF_FIGURES.md`. Action: moved `Favorable errors/` → `archive/Favorable-errors-2026-09-24/` via `git mv` (10 files, history preserved). Canonical retained: `docs/AI_ERROR_*.csv/md` (referenced via `INDEX.json` `RECEIPTS`). No test uses `Favorable errors/` path — verified `grep -r "Favorable errors" tests/` → 0 hits.
- **INTENTIONAL duplicates (NOT archived):**
  - `math/HARDENED_LOCKS.md` (71e3be7041eb8b13) ↔ `math/axiom_future/HARDENED_LOCKS.md` ↔ `math/axiom_evidence/HARDENED_LOCKS.md` — same SHA intentional: hash-only technique `WTF-005A-HASH-v3 sort_keys True ensure_ascii False (",",":")` copied to each module for existence verification (`math/README.md`). Compressed spec approach — do not deduplicate.
  - `math/*/EXISTS.md` (5 files, 8-9 bytes) — existence probes, intentional.
  - `docs/briefs/AXIOM_HARNESS_Brief.md` + `docs/briefs/Docs/Copy of AXIOM HARNESS Brief LVM addition not master.md` — historical briefs, kept per §15 HISTORICAL.
  - Basename collisions `control.html` (`app/wireframes/control.html` vs `app/multi_agent.html` etc behave as distinct rooms) — intentional room variants, not duplicates.

### Orphans — classified
- **Orphans found:** 0 active. `verify.py orphan[]==0` per `smoke.sh [5]` + `test_harness_boundary 12`. All `outputs/*/verify_result.json` green.
- **Dead files:** 0 deleted. Retired historical artifacts moved to `archive/` only.

### Archive populated
- `archive/Favorable-errors-2026-09-24/` (10 files) + `archive/README.md` (explains why archived, SHA list, intentional duplicates documented). Nothing deleted, history preserved via `git mv`.

## 3. Structural Movements (this sweep)
- `git mv "Favorable errors" archive/Favorable-errors-2026-09-24` (10 files R)
- `archive/README.md` added (audit log)
- `WORKING.md` added at Staging root (per_eca_state mutability risk + G8/G10 gates)
- `CURRENT_TREE.txt` (before, 402) + `PROPOSED_TREE.txt` (after, 406) generated
- `HARNESS_ORGANISATION_REPORT_2026-09-26.md/json` added (this file + json)
- `HARNESS_HOUSE_ORDER_CHANGELOG.md` added (movement log)
- `proof/HARNESS_PREFLIGHT_2026-09-26.md/json` refreshed to `5c88711` (was `f024fee`)

## 4. File Naming & Output Conformance
- **Naming standard:** `docs/NAMING_STANDARD_2026-09-26.md` — `EXP-<DOMAIN>-<NNN>` frozen never reused, `TEST-<DOMAIN>-<NNN>` taxonomy, `RUN-<PHASE>-<SCALE>-<PURPOSE>`, `RECEIPT-<RUN>-NNN`. Historical IDs (`WTF-001`, `HUMAN-2026`) kept HISTORICAL per §15.
- **Output packs:** `docs/DOCUMENTATION_STANDARD_2026-09-26.md` — per RUN `5-file seal` (`SCENARIO.json/csv + DECISION_SUMMARY + MANIFEST + verify_result B.prev=A`), per PACK `22-file deliverable.zip + verify.html + trail.html` — `INDEX.json` spine `EXPERIMENTS/PHASES/RUNS/TESTS/PACKS/RECEIPTS`.
- **How to use:** `docs/LAB_GUIDE.md` (8 sections, BEST_PRACTICE incorporated) + `docs/SETUP.md` + `docs/RUN_GUIDE.md` + `docs/VERIFICATION_GUIDE.md`.

## 5. Best-Practice Compliance (from docs/BEST_PRACTICE_LAB_SYSTEMS_2026-09-26.md)
- LIMS+ELN+Scheduler connected via `POST /api/master/* 201/422` — 9 rooms bounded.
- Polyglot modular `instrument→ingestion→core API→ELN/LIMS→Dashboard` traceable.
- FAIR+lineage `WTF-005A-HASH-v3 + B.prev=A + SHA-256 manifest`.
- Audit trail `sealed_by/at/instrument/sop_version + ai_computed_metrics:false`.
- Self-hosted frozen `AXIOM_STRICT_MODE=1 + protected_namespaces=()`.

## 6. QA — proof matches git state
- **Tests:** `PYTHONPATH="$PWD" /Library/Developer/CommandLineTools/usr/bin/python3 -m pytest -q` → `139 passed` (0 warnings after `edaf935 protected_namespaces=()`), HEAD `5c88711`.
- **Smoke:** `env PYTHONPATH="$PWD" PATH="/Library/Developer/CommandLineTools/usr/bin:$PATH" bash smoke.sh` → `5/5` (`health jail OK, seal validates, pressure allowlist OK, manifest canonical OK, orphans 0`).
- **Hashes:** `axiom_harness/mission.py 15541bb7ad94bb12`, `manifest.py bf6edb0f073d1c38`, `paths.py 8281e6ae9574f4da`, `api/main.py c110248424674b89`, `math/HARDENED_LOCKS.md 71e3be70`, `PER_ECA 5bb83c6e`, `WTF dc78ac17`, `WTF-005A-HASH-v3 sort_keys True ensure_ascii False (",",":")`.
- **Gates held:** `G8 owner:axiom-harness` (`axiom_harness/registry.py`), `G10 broad AXIOM_` retained with risk logged in `WORKING.md` + `docs/briefs/WORKING.md` until test migration.

*House Order §36 — no maths changed, no tests altered, no receipts rewritten, archive preserves history.*
