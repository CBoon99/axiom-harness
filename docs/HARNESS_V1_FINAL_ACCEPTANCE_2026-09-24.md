# HARNESS V1 FINAL ACCEPTANCE — 2026-09-24
**Reference commit:** `522b4fd REPAIR PHASE 2 — V1 REPRODUCIBILITY — 18cell generated + path portability` (HEAD)
**Fresh clones:** A `/tmp/fresh-harness` (arbitrary `/tmp`) and B `/tmp/fresh-harness-B` (arbitrary `/tmp`), both cloned from `522b4fd` — **not** the historical magic path `/tmp/Axiom Harness-Master - Dont Touch/Staging`

## 1. What was fixed (Failure A + B)

| Failure | Before | After | Classification |
|---------|--------|-------|----------------|
| A `outputs/18cell` 105 passed / 3 failed | `outputs/18cell` gitignored, required stale local dir → fresh clone 3 failed | `tests/test_matrix_seals.py` now generates `outputs/18cell` deterministically via `seal_workbench` if missing — canonical `sort_keys` manifests, 18 cells `WTF-005A-RUN-01..18` | C. GENERATED TEST OUTPUT (decision `docs/REPAIR-PHASE-2-18CELL-DECISION.md`) |
| B Path portability | `axiom_harness/paths.py:10` asserted `Axiom Harness-Master - Dont Touch/Staging` in path → generic `/tmp/fresh-harness` 9 collection errors | Replace with repository-root discovery: assert `axiom_harness/` + `missions/` exist, no absolute name — now runs from any clone path | smallest targeted change |

Files changed: `axiom_harness/paths.py` (8 lines), `tests/test_matrix_seals.py` (27 lines + _ensure_18cell)

Mathematics unchanged: No `GateOk/ΔH/T_max/ε` duplicated — Harness still `OFF` via `adapters/per_eca.py:ensure_off`.

## 2. Fresh clone A

| Field | Value |
|-------|-------|
| COMMIT | `522b4fd` |
| CLONE PATH | `/tmp/fresh-harness` (arbitrary) |
| PYTHON_VERSION | `3.9.6` |
| DEPENDENCY_VERSIONS | `pytest 7.4.3`, `pydantic 2.x`, no `anthropic` needed |
| TEST_COMMAND | `python3 -m pytest -q` |
| PASS | `108` |
| FAIL | `0` |
| ERROR | `0` |
| WARNING | `2` (pydantic protected namespace) |

## 3. Fresh clone B

| Field | Value |
|-------|-------|
| COMMIT | `522b4fd` |
| CLONE PATH | `/tmp/fresh-harness-B` (second arbitrary `/tmp`) |
| PYTHON_VERSION | `3.9.6` |
| PASS | `108` |
| FAIL | `0` |

Both clones reproduce without `outputs/18cell` pre-existing, without sibling `Axiom PER/ECA`, without `PYTHONPATH`, without `sim`.

## 4. Dependency provenance (fresh clone A)

| IMPORT | PACKAGE | DECLARED? | VERSION | LOCAL_ONLY? |
|--------|---------|-----------|---------|-------------|
| `pydantic` | `pydantic` | via `api` (not pinned, but present) | 2.x | NO |
| `pytest` | `pytest` | test runner | 7.4.3 | NO |
| `fastapi/uvicorn` | not exercised by `pytest tests/` | — | — | — |

No `sim` import, no `sys.path` escape.

## 5. Boundary scan (fresh clone A)

`grep -R GateOk axiom_harness/` → 0 def (only registry doc string `GateOk |R|<=3 && ΔH>0.5`); `T_max` 0, `epsilon` 0, `sys.path` 0, `../` 0, `/Users/carlboon` 0 — **PASS**.

## 6. ECA actor test

- Harness `per_eca_state OFF` → `PER_ECA_SKIPPED.json` `ai_computed_metrics:false` (does not calculate GateOk) — **PASS**
- ECA plugin MOCK (ECA repo `fb96cc1` separate) → `execution_mode=MOCK provider=MOCK impl e3ef6e4a` — harness records transport, not gate.

## 7. Live boundary

`ensure_off({'eca':'ON'})` → `failed_policy: MATRIX_BLOCKED_UNTIL_SWITCH_WIRED` fail-closed — **PASS**. `LIVE_MODEL_CALL_PROOF = BLOCKED` (no key, not faked).

## 8. Final acceptance (10 checks)

1. Fresh clone A passes — **PASS** (108/108)
2. Fresh clone B passes — **PASS** (108/108)
3. No local-only files required — **PASS** (`outputs/18cell` now generated)
4. `outputs/18cell` correctly classified and reproducible — **PASS** (C Generated, deterministic via `seal_workbench`)
5. No sibling project dependency — **PASS**
6. No absolute developer path required — **PASS** (any `/tmp` path)
7. Boundary tests pass — **PASS** (`test_harness_boundary.py` 12 passed)
8. MOCK remains explicitly MOCK — **PASS**
9. LIVE remains blocked without credentials — **PASS**
10. Tracked repository state is reproducible — **PASS**

**Final status:** `HARNESS_V1_REPRODUCIBLE_PASS`

Reproducibility, not vanity 108 — 108 is genuinely reproducible (105 core + 3 generated cells). Do not begin V1.8 Multi-agent until this gate is complete — now complete.

