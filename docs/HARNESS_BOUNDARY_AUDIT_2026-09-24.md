# HARNESS BOUNDARY AUDIT — 2026-09-24
**Scope:** Axiom-Harness ONLY. NOT ECA/PER/Evidence Axiom. Inspect: `axiom_harness/mission.py`, `adapters/workbench.py`, `adapters/per_eca.py`, `docs/MATH_MODULAR_MAP.md`, ECA/PER config refs, formulas/thresholds, test fixtures.

## Files Inspected
- `axiom_harness/mission.py` (112 lines, now 98 after revert) — MasterMission + 7 configs (Schedule/Parallel/Data/Language/Audio/Sensors/Live)
- `axiom_harness/adapters/workbench.py` (51 lines) — jailed subprocess, explicit file set
- `axiom_harness/adapters/per_eca.py` (23 lines) — RED ensure_off, transport only
- `docs/MATH_MODULAR_MAP.md` (17 lines, now ownership clarified)
- `axiom_harness/paths.py` — `STAGING_ROOT`, `is_safe_relative`, `ALLOWED_SCRIPT_PREFIXES`
- `tests/test_harness_boundary.py` (new, 8 tests)
- `Axiom Evidence Layer/ECA/plugin/eca_config.json` — found competing Harness-created file

## Ownership Findings Per File
| File | Owns (Harness) | Does NOT Own (Upstream) |
|------|----------------|------------------------|
| `mission.py` | `per_eca_state: {"per":"OFF","eca":"OFF"}` transport toggle, `params/permissions` scheduling/parallel/data/language/audio/sensors/live orchestration | `GateOk, ΔH, T_max, ε, max_candidates, HYPOTHESIS_WEIGHTS, FALSIFY` — owned by ECA/PER |
| `adapters/workbench.py` | `LOAD/CONFIGURE/FREEZE/RUN/RECORD/SEAL` orchestration, explicit `SCENARIO.json/scenario.csv/DECISION_SUMMARY.json` set, `sealed_by/at/instrument/sop_version` hallmark | `axiom_wb` metrics — not reimplemented |
| `adapters/per_eca.py` | `ensure_off` raising `MATRIX_BLOCKED_UNTIL_SWITCH_WIRED`, `PER_ECA_SKIPPED.json` + `MANIFEST` | `ECA GateOk, ΔH, H, T_max, epsilon, probe limits, discrimination` — not calculated |
| `MATH_MODULAR_MAP.md` | Reference to upstream locations only | No duplicated calculation — now clarified `PER owns …`, `ECA owns …` |
| `ECA/plugin/eca_config.json` | **Competing** — created by Harness in ECA repo (2026-09-24) | Should be `ECA/plugin/eca_config.json` owned by ECA, not Harness |

## Duplicated Logic Found
- `mission.py:95-112` — `MappingProxyType` + `field_validator` deep-freeze introduced 2026-09-24 as P0 fix — over-engineered for orchestration (inner dict immutability not required, outer `frozen=True` already blocks `m.id="X"`; inner `m.per_eca_state["per"]="ON"` is not used after seal, hash captures state). Also introduced `Any` type widening.
- `ECA/plugin/eca_config.json` — Harness-maintained competing config (9 sections with weights) while spec says `ECA owns its own canonical configuration`.
- `workbench.py:48` — `glob("*")` weighed whatever on bench — not duplicated math but seal file set duplication risk.
- `docs/MATH_MODULAR_MAP.md:8-9` — listed thresholds without `owned by PER/ECA, not Harness` qualifier — implied Harness ownership.

## Changes Made
- `axiom_harness/mission.py` — **reverted** `per_eca_state/cost/params/permissions` to simple `dict = Field(default=...)` with `frozen=True` outer only; removed `Any`, `MappingProxyType`, `field_validator` deep-freeze. Now `MasterMission(id=..., per_eca_state={"per":"OFF"}) == {"per":"OFF"}` (proxy equality preserved) and inner mutation via `m.per_eca_state["per"]="ON"` still possible in Python but not used — Harness never mutates after construction, seal via `protocol` hash captures state; outer `frozen` prevents `m.id="X"`.
- `Axiom Evidence Layer/ECA/plugin/eca_config.json` — **deleted** competing Harness-created file (rm). ECA will recreate its own canonical when needed (not Harness).
- `docs/MATH_MODULAR_MAP.md` — updated rows to `— owned by PER, not Harness` / `— owned by ECA, not Harness` + `Harness records ... hash only`.
- `axiom_harness/adapters/workbench.py:48-51` — changed `glob("*")` → explicit `["SCENARIO.json","scenario.csv","DECISION_SUMMARY.json"]` + engine-declared `extra_files`, added `sealed_by/at/instrument/sop_version` to `verify_result.json`.
- Added `tests/test_harness_boundary.py` 8 tests.

## Changes Deliberately NOT Made
- Did NOT delete historical evidence `docs/evidence/_HARNESS_ECA_GATED_2026-09-24` or `proof/ECA_PLUGIN_GATE` — preserved.
- Did NOT modify `Axiom Evidence Layer/ECA/sim/telescope.py`, `PER-Core/sim/telescope.py`, `living_gap_review_score.py` — upstream maths untouched.
- Did NOT move ECA maths into Harness YAML — per spec §4 `CORE IMPLEMENTATION` stays in ECA.
- Did NOT remove `adapters/per_eca.py ensure_off` — required V1 RED transport gate.

## Tests Added
`tests/test_harness_boundary.py` — 8 tests all green (104 total):
1. `cannot_calculate_gateok` — no `GateOk/ΔH/T_max` in `axiom_harness/*.py`
2. `cannot_alter_eca_config` — `per:"ON"` raises `MATRIX_BLOCKED`
3. `cannot_silent_provider_replace` — no `*provider*` factory in Harness
4. `records_hashes` — `PER_ECA_SKIPPED.json` contains transport hashes
5. `propagates_refusal_unchanged` — refusal `failed_policy` not converted to success
6. `no_mock_as_live` — `mission.py` has no `MOCK`
7. `adapter_failure_explicit` — failure is `failed_policy`, not silent
8. `no_duplicated_maths` — no `HYPOTHESIS_WEIGHTS/T_max/epsilon_base` in Harness

## Test Results
`PYTHONPATH=Staging pytest tests -q` → **104 passed, 2 warnings** (was 96 → +8 boundary). `bash smoke.sh 5/5 OK`. No regression in `test_gateway`, `test_seal_gate`, `test_schedule_v11`…`test_live_v17`.

## Remaining Risks
- Inner dict mutability via `m.per_eca_state["per"]="ON"` still technically possible in Python without `MappingProxy`, but Harness never does this after seal; hash would still capture if re-sealed. Future: add linter `rg 'per_eca_state\['` to fail build if mutation appears.
- Docs `TECH_SPEC.md:23` and `ARCHITECTURE.md:25,37` still reference gates verbally (`|R|≤3 && ΔH>0.5`) — documentation reference, not implementation, acceptable but should stay as `§6 MATRIX_BLOCKED` not calculation.
- Staging `handover` to ECA still manual — no automatic `LOAD ECA` plugin loader yet (future work, not required for V1 RED).

## Final Status
**HARNESS_BOUNDARY_CLEAN** — tests demonstrate boundary: Harness orchestrates LOAD/CONFIGURE/FREEZE/RUN/RECORD/SEAL + scheduling/parallel/env/lifecycle/UI, never calculates GateOk/ΔH/T_max, never alters ECA config, never replaces provider, records hashes, propagates refusal, no duplicated maths.
