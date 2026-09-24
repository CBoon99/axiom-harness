# COMMERCIAL CLAIM REGISTER — AXIOM HARNESS V1
**Date:** 2026-09-24 — **Reference:** `522b4fd` + `307bf6f` `HARNESS_V1_REPRODUCIBLE_PASS`

Every statement classified `OBSERVED / DERIVED / DOCUMENTED_CAPABILITY / UNVERIFIED / NOT_CLAIMED`. Numerical claims require `SOURCE / SCOPE / DATE / EVIDENCE`.

| CLAIM_ID | EXACT WORDING | CLASS | SOURCE | SCOPE | DATE | EVIDENCE |
|----------|---------------|-------|--------|-------|------|----------|
| C01 | Run AI experiments under controlled conditions, preserve exactly what happened, and produce an auditable sealed record. | DOCUMENTED_CAPABILITY | `docs/commercial/COMMERCIAL_POSITIONING_V1.md` + `PLAN_V1.md` | V1 product | 2026-09-24 | `axiom_harness/mission.py` frozen, `adapters/workbench.py` seal, `manifest.py` |
| C02 | Control + Sandbox + Run/Sequence/Parallel + Live Room + Timeline + Sealed Evidence + Export + Governed Upstream Actors are V1 capabilities. | DOCUMENTED_CAPABILITY | `V1_CAPABILITY_MATRIX.md` | V1 only | 2026-09-24 | `tests/` 108 passed |
| C03 | Controlled, bounded, repeatable, provenance-backed, fail-closed, sealed, auditable. | DOCUMENTED_CAPABILITY | `COMMERCIAL_POSITIONING_V1.md` core language | V1 | 2026-09-24 | `paths.py` jail, `MANIFEST` canonical, `verify_result` `ai_computed_metrics:false` |
| C04 | Harness can execute upstream modules such as ECA/PER without taking ownership of their internal mathematics. | DOCUMENTED_CAPABILITY | `adapters/per_eca.py` `ensure_off` | V1 `per:OFF/eca:OFF` transport | 2026-09-24 | `tests/test_harness_boundary.py` 12 tests (cannot calculate GateOk/ΔH/T_max, cannot alter config, records hashes) |
| C05 | MOCK upstream is explicitly MOCK, never LIVE. | OBSERVED | `ECA/plugin/eca_plugin.py` (ECA repo `fb96cc1`) | ECA MOCK mode | 2026-09-24 | `execution_mode=MOCK provider=MOCK` `e3ef6e4a` |
| C06 | LIVE without credentials fails closed (MATRIX_BLOCKED). | OBSERVED | `adapters/per_eca.py` | Harness `eca:ON` | 2026-09-24 | `failed_policy: MATRIX_BLOCKED_UNTIL_SWITCH_WIRED` |
| C07 | Fresh-clone reproducibility: 108/108 on two arbitrary /tmp clones. | OBSERVED | `docs/HARNESS_V1_FINAL_ACCEPTANCE_2026-09-24.md` | Engineering reproducibility only | 2026-09-24 | `/tmp/fresh-harness` and `/tmp/fresh-harness-B` each `python3 -m pytest -q → 108 passed` at `522b4fd`, `Python 3.9.6` `pytest 7.4.3` |
| C08 | 108/108 is engineering reproducibility, not accuracy/reliability. | DERIVED | C07 | Scope clarification | 2026-09-24 | same evidence as C07, explicitly not `100% accurate` |
| C09 | V1.8 Multi-agent (Analyst/Critic/Maker) is future, not V1 promise. | DOCUMENTED_CAPABILITY | `PROJECT_PROFILE V3` | Future | 2026-09-24 | `commercial/` V1→Future story |
| C10 | Specific customer logos / market traction / deployments / ROI / accuracy percentages. | NOT_CLAIMED | — | — | — | Do not claim — no source |
| C11 | Harness certifies truth / consciousness / hallucination elimination / guaranteed compliance / that upstream is correct because Harness ran. | NOT_CLAIMED | — | — | — | Explicitly forbidden in `V1_LIMITATIONS.md` |
| C12 | Commercial ECA proof as LIVE without provider request/response. | UNVERIFIED (BLOCKED) | `ECA/plugin/provider/anthropic.py` | ECA LIVE | — | `LIVE_MODEL_CALL_PROOF = BLOCKED` (no `ANTHROPIC_API_KEY`) — not claimed |

**Customer categories (plausible, not invented, not ranked, no demand claim):** AI research teams, AI safety/evaluation teams, regulated organisations, internal AI governance teams, AI product teams, organisations conducting sensitive AI experimentation, independent researchers, consultancies needing reproducible AI evaluation.

