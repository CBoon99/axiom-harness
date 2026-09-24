# REPAIR PHASE 2 — 18CELL DECISION — 2026-09-24
**Reference commit:** `c2ff3b39c4bfc4b85ecd8fbeb67c944c55432161`
**Failures:** `105 passed / 3 failed` on fresh exact-path clone — all 3 in `tests/test_matrix_seals.py` due to `outputs/18cell/` missing

## Investigation

- `outputs/18cell/` locally: 18 dirs `WTF-005A-RUN-01`..`18`, each `workbench/` with `MANIFEST.json`, `verify_result.json` (`engine_present:false`, `sealed:false`, `ai_computed_metrics:false`), `SCENARIO.json`, etc. Generated 2026-09-24 12:15 via `workbench` sealing (placeholder seals — no real `axiom_wb` engine).
- `.gitignore`: `outputs/` is gitignored — fresh clone has no `outputs/18cell/` (intentionally excluded).
- `tests/test_matrix_seals.py` `test_18cell_outputs_exist` asserts `OUTPUTS / "18cell"` exists with 18 cells; `test_18cell_each_has_seal` iterates it; `test_manifests_canonical_per_cell` iterates it. Tests require stale local outputs, not generation.
- `PLAN_V1.md` § P0 era mentions matrix seals but does not mandate `outputs/18cell/` as **required V1 product artefact**. `PROJECT_PROFILE.md` V1 proves architecture via Control/Sandbox/Run/Live/Timeline/Seal/Export — 18cell is **sample evidence** (12 primary +4 prevalence +2 duplicate) for explainer, not V1 product contract. `BRIEF_REVOLUTIONARY` describes matrix as example, not gate.
- No committed inputs generate 18cell deterministically — it is pre-generated local evidence, not a deterministic fixture from committed `missions/` or `scenario` inputs.

## Classification

**C. GENERATED TEST OUTPUT** — with nuance of **D. HISTORICAL / EVIDENCE-ONLY ARTEFACT**

- Not **A. REQUIRED V1 PRODUCT ARTEFACT**: `outputs/` is gitignored, V1 product is `axiom_harness/` + `tests/` + `missions/` + `docs/` — 18cell is sample run outputs, not product.
- Not **B. COMMITTED DETERMINISTIC TEST FIXTURE**: No committed `outputs/18cell/` and no deterministic generation from committed inputs is recorded; fixture would be stale.
- **C**: Tests should generate `outputs/18cell` deterministically during test (via `seal_workbench` loop), or test generation logic itself, not require stale directory.
- Also **D**: The 18 directories are historical evidence of a prior run — preserved locally but not part of V1 reproducibility gate. **E**: Should not be a V1 gate as currently written (requires stale outputs).

## Determination

Per `BRIEF` 4 locks and `PLAN_V1`, V1 reproducibility gate is **Control→Seal→Verify** (5-file seal, chain, `ai_computed_metrics:false`), not 18-cell matrix output. Therefore:

- **Do NOT commit `outputs/18cell/` as product artefact** to make tests pass (would be arbitrary pre-generated local outputs).
- **Fix:** `tests/test_matrix_seals.py` must **generate** `outputs/18cell` deterministically during the test if missing (via `seal_workbench` for each of 18 cells), or reclassify those 3 tests as **evidence-only / historical** and exclude from V1 product gate while preserving evidence locally.

**Chosen fix (smallest targeted):** Update `test_matrix_seals.py` to generate `outputs/18cell` deterministically if missing (loop 18 `seal_workbench` calls), and treat missing directory as generation trigger, not failure. This makes tests reproducible from repository without committing stale outputs, while preserving existing evidence `outputs/18cell/` if present. Alternative (reclassify as skipped) would hide the 12+4+2 breakdown, so generation is preferred.

**Hashes:** No committed inputs/outputs to hash for 18cell — generation is via `axiom_harness/adapters/workbench.py:seal_workbench` (deterministic placeholder seals). After fix, `MANIFEST.json` per cell remains canonical `sort_keys True`.

**Fresh-clone test after fix:** Must pass `108/108` on any clone path (exact + arbitrary) without requiring pre-existing `outputs/18cell/`.

## Path portability note

`axiom_harness/paths.py:10` asserts `STAGING_ROOT` contains `Axiom Harness-Master - Dont Touch/Staging` — this forces exact absolute directory name. Not contractual per `PLAN_V1` (which says `STAGING_ROOT = Path(__file__).resolve().parents[1]`). Fresh generic `/tmp/fresh-harness` fails collection (9 errors) while exact-path `/tmp/Axiom Harness-Master - Dont Touch/Staging` passes. Classification: **hard-coded path assumption — should be replaced with repository-root discovery** (see separate path fix).

