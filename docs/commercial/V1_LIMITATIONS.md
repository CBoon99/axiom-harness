# V1 LIMITATIONS — AXIOM HARNESS
**V1 is a controlled execution and evidence layer — not a truth machine.**

## What V1 does NOT claim

- **Truth / correctness** — Harness does not claim an experiment is scientifically valid merely because Harness ran. Correctness is empirical per deployment / upstream actor.
- **Consciousness detection** — not claimed.
- **Hallucination elimination** — not claimed; failures/unknowns are preserved, not eliminated.
- **Perfect AI behaviour** — not claimed.
- **Guaranteed compliance** — not claimed.
- **Every result is correct** — not claimed.
- **Upstream actor correct because Harness executed it** — `ECA GateOk` etc. owned by ECA, not Harness.
- **Commercial ECA proof without LIVE provider evidence** — `ECA/PER` in V1 are `OFF` (transport), `MOCK` is explicitly `MOCK`, `LIVE` is `BLOCKED` (`failed_policy: MATRIX_BLOCKED_UNTIL_SWITCH_WIRED` in `adapters/per_eca.py`) — no LIVE proof without `ANTHROPIC_API_KEY` + real request/response.
- **Unsupported ROI** — not claimed.
- **Unsupported accuracy percentages** — not claimed. `108/108` is engineering reproducibility (fresh clone `522b4fd` two arbitrary `/tmp` clones `Python 3.9.6` `pytest 7.4.3`), not accuracy/reliability.

## Boundaries

- Harness provides `CONTROL + ISOLATION + REPEATABILITY + PROVENANCE + MULTI-MODEL EXECUTION + RECEIPTS + SEALED RESULTS` — it records execution and evidence, does not magically make an experiment valid.
- Evidence is the `5-file seal` + chain + `ai_computed_metrics:false` + `MANIFEST` canonical `sort_keys` — video is presentation, not proof (if rendered).
- Upstream `ECA/PER` internal mathematics (`GateOk |R|<=3 && ΔH>0.5`, `T_max(N)=ceil(log2(N/3))+4`, `H`, `ε`, telescope) remains owned by those modules, not Harness.
- `V1.8` (Multi-agent), `V1.9` (Patch Visual), `V2/V3` are future — not part of V1 commercial promise.

## What to tell a buyer asking “does it make AI perfect?”

No — it makes AI experimentation **controlled, bounded, repeatable, provenance-backed, fail-closed, sealed, and auditable** so the organisation can see what happened and preserve it.
