# Archive — Axiom Lab Harness — 2026-09-26
Historical evidence retired from active tree per House Order §33. Nothing deleted — all archived with original SHA preserved, chain intact.

## What is archived and why
- `Favorable-errors-2026-09-24/` — duplicate of `docs/AI_ERROR_*` (8 files + 2 docs). Original location `Favorable errors/` (space in name) caused path/CI fragility. Canonical retained at `docs/AI_ERROR_*.csv/md` (SHA identical: 23fcceb9, faaf30d1, 51ac3a68, a504b914, bf6bc757, 032afed8, 96b85fee, 733e7898). This archive is HISTORICAL, read-only, never used for verification.

## Other intentional duplicates (NOT archived — documented here)
- `math/HARDENED_LOCKS.md` + `math/axiom_future/HARDENED_LOCKS.md` + `math/axiom_evidence/HARDENED_LOCKS.md` — same SHA `71e3be7041eb8b13` — intentional hash-only existence logs per technique WTF-005A-HASH-v3, each module copies the pinned math for verification.
- `math/*/EXISTS.md` — 5 files `8-9 bytes` — intentional existence probes, not duplicates.

## Orphan / dead-file audit result (2026-09-26)
- Orphans found: 0 active orphans (`verify.py orphan[]==0, smoke 5/5`). All `outputs/*/verify_result.json` green.
- Dead files archived: 0 deleted, 10 moved (above). Remaining `docs/*.md` all referenced via `MASTER.md → INDEX.md → LAB_GUIDE.md` or `INDEX.json`.

*House Order §33 — no deletion, only archive.*
