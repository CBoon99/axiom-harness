# HARNESS HOUSE ORDER CHANGELOG — §33-36 — 2026-09-26

## §33 — Duplicate & Orphan Audit
- Classified `docs/AI_ERROR_*` (8) vs `Favorable errors/AI_ERROR_*` (8) as byte-identical duplicates (SHA per pair: 23fcceb9, faaf30d1, 51ac3a68, a504b914, bf6bc757, 032afed8, 96b85fee, 733e7898). No test references `Favorable errors/` path.
- Classified `math/HARDENED_LOCKS.md` x3 and `math/*/EXISTS.md` x5 as intentional hash-only existence logs (71e3be70) — not duplicates.
- Orphans: 0 (`verify.py orphan[]==0, smoke 5/5`).

## §33 — Tree Cleanup (no deletion)
- `git mv "Favorable errors" archive/Favorable-errors-2026-09-24` — 10 files (8 AI_ERROR + ABSOLUTE_FULL_REPORT.md + TABLE_OF_FIGURES.md), history preserved.
- `archive/README.md` added — explains canonical `docs/AI_ERROR_*` retained, SHA list, intentional duplicates documented.

## §36 — Tree Reports
- `CURRENT_TREE.txt` generated before (402 entries, find . -not -path .git/.pytest_cache/.netlify/__pycache__ | sort).
- `PROPOSED_TREE.txt` generated after (406 entries) — net +4 (archive/README + WORKING + 2 reports).

## §36 — Organisation Report
- `HARNESS_ORGANISATION_REPORT_2026-09-26.md` + `.json` added — before/after, audit, naming/output conformance, best-practice, QA.

## §36 — Risk Logging
- `WORKING.md` added at Staging root — logs `per_eca_state` inner dict mutability risk (frozen outer, mutable inner, ensure_off gate) + `G8 owner:axiom-harness` / `G10 broad AXIOM_` gates held until test migration.

## QA & Preflight Refresh
- `proof/HARNESS_PREFLIGHT_2026-09-26.md` + `.json` refreshed: HEAD `f024fee` → `5c88711` (`5c8871190b49ccec8833ae7a0f34247cbc4eab4b`), file counts 320/85, 139 passed 0 warnings, 5/5 smoke, hashes pinned.

*No maths/tests/receipts changed. Archive preserves history. Next authorized: `§35 Final Audit A→Z` (read-only) when requested.*
