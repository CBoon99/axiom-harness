# HARNESS V1 VERIFICATION — 2026-09-24
**Reference commit:** `c2ff3b39c4bfc4b85ecd8fbeb67c944c55432161` (GATE 4) — HEAD `c2ff3b3` on branch `main`
**Fresh clones:** `/tmp/fresh-harness` (generic /tmp) and `/tmp/Axiom Harness-Master - Dont Touch/Staging` (exact-path)
**Python:** `3.9.6`, `pytest 7.4.3`, `pydantic` (installed), `anthropic` not required for Harness V1

## 1. VERSION-CONTROL AUDIT
`git log --oneline --decorate -10`:
```
c2ff3b3 (HEAD -> main) GATE 4 — DUPLICATE SCAN + FREEZE_V3_ON_HOLD — PASS
f39594b GATE 3 — BOUNDARY TESTS — PASS
52804a7 GATE 2 — MATH MODULAR MAP — REGISTRY ONLY — PASS
19ccf2d GATE 1 — HERO/DOCS — PASS
9f3ceb7 Fresh-clone finding: API cannot boot outside this exact folder name
d075059 ABSOLUTE FULL REPORT — 2026-09-24 — ECA forensic + repair
```
Per-gate commits: Gate 1 `19ccf2d`, Gate 2 `52804a7`, Gate 3 `f39594b`, Gate 4 `c2ff3b3` — each gate separate commit. **GATE_COMMIT_REQUIREMENT = MET** (not bundled). Earlier summary table incorrectly collapsed to `52804a7` — corrected here.

## 2. CLEAN WORKTREE
`git status --short` on `c2ff3b3`:
```
?? Favorable errors/AI_ERROR_*.csv/.md (8 files)
?? docs/AUDIT_MASTER_GAPS_HALLUCINATIONS.md
?? docs/BRIEF_REVOLUTIONARY_V3_SYNTHESIZED.md
```
- Modified tracked files: **0**
- Untracked: 10 files — classified as **intentional evidence artefacts** (Favorable errors forensic copies + 2 docs not part of V1 product commit `axiom_harness/`/`tests/`/`app/`/`api/`). V1 product commit is `axiom_harness/` + `tests/` + `missions/` + `docs/ARCHITECTURE.md` etc.; `Favorable errors/` and `docs/AUDIT_MASTER*` are excluded evidence, not V1 product.
- No staged changes. Worktree clean for V1 product.

## 3. FRESH CLONE
Clone 1 (generic): `git clone Staging /tmp/fresh-harness` → `STAGING_ROOT` assert `Axiom Harness-Master - Dont Touch/Staging` fails → **9 collection errors** (not dependency, path check `axiom_harness/paths.py:10`).

Clone 2 (exact-path): `git clone Staging "/tmp/Axiom Harness-Master - Dont Touch/Staging"` → clone SHA `c2ff3b3`, contains exactly committed files (no `sim/`, no sibling `Axiom PER`/`ECA` working trees, no `PYTHONPATH`, no cached modules beyond fresh pip).

Verification: `ls /tmp/fresh-harness/sim` → No such file (correct — Harness has no `sim` dependency).

## 4. COMPLETE TEST (fresh clone exact-path)

| Field | Value |
|-------|-------|
| COMMIT | `c2ff3b39c4bfc4b85ecd8fbeb67c944c55432161` |
| PYTHON_VERSION | `3.9.6` |
| DEPENDENCY_VERSIONS | `pytest 7.4.3`, `pydantic` (installed 2.x), `anthropic` not required, `uvicorn` for `api/` not exercised by `pytest tests/` |
| TEST_COMMAND | `/tmp/Axiom Harness-Master - Dont Touch/Staging` `python3 -m pytest -q` |
| PASS | `105` |
| FAIL | `3` (`test_matrix_seals.py` 3 tests: `test_18cell_each_has_seal`, `test_18cell_outputs_exist`, `test_manifests_canonical_per_cell` — each `FileNotFoundError: outputs/18cell` missing) |
| ERROR | `0` (when path correct) |
| WARNING | `2` (pydantic `model_matrix`/`model_version` protected namespace) |

**Why not 108:** Local working tree `Staging` has `108 passed` because `outputs/18cell/` exists locally (pre-generated 18-cell matrix evidence, not committed — intentionally excluded as evidence artefact per `BRIEF` 4 locks). Fresh clone has no `outputs/18cell/` → 3 fail. Core harness tests (boundary, jail, health, seal, schedule, parallel, data, language, audio, sensors, live, patches, etc.) **105/105 pass** on fresh clone.

## 5. DEPENDENCY PROVENANCE (outside stdlib, from fresh clone)

| IMPORT | PACKAGE / SOURCE | DECLARED? | VERSION | SOURCE_REPOSITORY | LOCAL_ONLY? |
|--------|------------------|-----------|---------|-------------------|-------------|
| `pydantic` | `pydantic` pip | via `api/requirements`? not pinned in `pyproject.toml` (Harness has no `pyproject.toml`) | 2.x | PyPI | NO |
| `pytest` | `pytest` pip | test runner, not product dep | `7.4.3` | PyPI | NO |
| `fastapi`/`uvicorn` | `api/main.py` | not exercised by `pytest tests/` | — | PyPI | NO |
| `anthropic` | not imported by Harness (only by ECA `plugin/provider`) | NO (Harness `per_eca` is `OFF`) | — | — | — |

No `sim/` import, no `Axiom PER`/`ECA` working tree import. **Harness runs from fresh clone without sibling projects.**

## 6. BOUNDARY SCAN (fresh clone exact-path, `grep -R`)

| Pattern | Matches | Verdict |
|---------|---------|---------|
| `GateOk` | `axiom_harness/registry.py` string `"GateOk |R|<=3 && ΔH>0.5 && sealed+hash && FALSIFY"` (documentation in registry, not implementation) | **no duplicated calculation** — `grep -R "def GateOk" axiom_harness/` → 0 |
| `ΔH` | same registry string only | 0 impl |
| `T_max` | 0 in `axiom_harness/` | 0 |
| `epsilon` | 0 | 0 |
| `max_candidates` | 0 | 0 |
| `ECA thresholds` | registry doc string only | doc, not code |
| `PER telescope logic` | 0 | 0 |
| `ECA provider logic` | 0 (`adapters/per_eca.py` has `ensure_off` only) | 0 |
| `sys.path` | 0 in `axiom_harness/` | 0 |
| `PYTHONPATH` | 0 (`echo $PYTHONPATH` empty) | 0 |
| `../` `../../` | 0 | 0 |
| absolute local `/Users/carlboon` | 0 | 0 |
| sibling `Axiom PER`, `ECA` import | 0 (only `registry.py` path string, not import) | doc |

**Result:** No duplicated upstream mathematics, no sys.path escape.

## 7. ECA ACTOR TEST (Harness against MOCK ECA)

Harness V1 `per_eca_state={per:OFF,eca:OFF}` → `adapters/per_eca.py:seal_per_eca` writes `PER_ECA_SKIPPED.json` with `{"per_eca_state": OFF, "ai_computed_metrics": false}` + `MANIFEST`. Does **not** calculate `GateOk`.

Separate ECA plugin MOCK (ECA repo `fb96cc1`):
- `ECAPlugin.load(mode='MOCK').run('industrial ZO loss')` → `execution_mode=MOCK provider=MOCK implementation_hash=e3ef6e4a3f50 config_hash=sha256:90386780894253c1 run_id=run-... result=REFUSED/CLAIM` (fresh clone `10 passed`).
- Harness receipt does not contain ECA `GateOk` — it contains `per_eca_state` transport + `sealed_by/at/instrument`.

**Proven:** Harness does not calculate ECA GateOk (boundary scan 0), records upstream identity via `per_eca_state` hash, preserves `ai_computed_metrics:false`.

## 8. LIVE BOUNDARY
`LIVE without credential must fail closed` — Harness `per_eca_state={eca:ON}` → `ensure_off` raises `failed_policy: MATRIX_BLOCKED_UNTIL_SWITCH_WIRED` — **fail closed, no seal** (test `test_harness_boundary.py::test_per_eca_on_blocked` PASS).

**Status:** `LIVE_MODEL_CALL_PROOF = BLOCKED` (no ANTHROPIC_API_KEY supplied, no fake; separate from Harness V1).

## 9. SEAL THE RESULT

| Field | Value |
|-------|-------|
| HARNESS_REFERENCE_COMMIT | `c2ff3b39c4bfc4b85ecd8fbeb67c944c55432161` |
| FRESH_CLONE_PASS | `105` |
| FRESH_CLONE_FAIL | `3` (all `outputs/18cell` missing — intentional evidence not committed) |
| DEPENDENCY_BOUNDARY | `PASS` (no sibling import, runs from exact-path clone) |
| UPSTREAM_BOUNDARY | `PASS` (0 GateOk/ΔH/T_max impl in Harness) |
| MOCK_INTEGRATION | `PASS` (ECA MOCK `execution_mode=MOCK provider=MOCK` via ECA plugin; Harness `OFF` correctly blocks) |
| LIVE_BOUNDARY | `PASS` (fail-closed `MATRIX_BLOCKED`) |
| WORKTREE_STATUS | `CLEAN` (0 modified, 10 untracked intentional evidence artefacts excluded) |

## 10. FINAL STATUS

**HARNESS_V1_REPRODUCIBILITY_FAIL** — not because Harness calculates upstream maths (it does not), but because **fresh clone cannot reproduce `108 passed` without `outputs/18cell/` evidence artefact** (3 tests fail) and **cannot run from generic `/tmp/fresh-harness` path** (STAGING_ROOT assert). Core harness (105 tests) **is reproducible** from exact-path clone, but full `108` suite is not without committed evidence.

Do not begin V1.8 Multi-agent until `outputs/18cell/` is either committed as evidence or tests are reclassified to exclude pre-generated cell outputs from V1 product gate.

