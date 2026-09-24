# BUYER STORY V1 — AXIOM HARNESS
**Order:** Problem → Solution → How it Works → What Buyer Gets → Why Matters → Boundaries

## THE PROBLEM
AI experiments are often difficult to reproduce, compare, audit and explain after the fact. Teams run models through informal chats, lose the experimental conditions, and cannot show after the fact what was tested under which inputs, with which actors, and what evidence was preserved. Failures and unknowns are often lost.

## THE SOLUTION
Axiom Harness provides a controlled environment for running, comparing and sealing AI experiments. It does not promise perfect AI — it provides the discipline around the AI: controlled conditions, isolated execution, and sealed evidence.

## HOW IT WORKS
**Control → Sandbox → Run → Compare → Timeline → Seal → Export**

- **Control:** The organisation defines the experiment — model, context, environment, information sources, permissions, schedule, parallel conditions.
- **Sandbox:** Each run executes in an isolated, governed environment (terminal substrate — runtime contract, not visual).
- **Run / Sequence / Parallel:** One run, a sequence, or parallel isolated conditions (including data/language/audio/sensors/live as configured).
- **Compare (Live Room):** Multiple actors/models/humans run under the same controlled context for side-by-side comparison.
- **Timeline:** Every prompt, response, tool call, event and sensor reading is preserved in order with timestamps.
- **Seal:** The 5-file canonical seal (`SCENARIO.json`, `scenario.csv`, `DECISION_SUMMARY.json`, `MANIFEST.json`, `verify_result.json`) with chain `B.prev=A` and `ai_computed_metrics:false`.
- **Export:** Documented evidence/export pack for review.

## WHAT THE BUYER GETS
A **reproducible experiment record** rather than an informal conversation log — with provenance, receipts, and sealed results that can be re-verified (`sha256sum -c`, `MANIFEST` canonical `sort_keys`).

Specifically V1 delivers: Control, Sandbox, Run/Sequence/Parallel, Live Room, Timeline, Sealed Evidence, Export, and governed upstream actors (`ECA/PER` via transport `per_eca_state`, `MOCK` explicitly `MOCK`).

## WHY IT MATTERS
The organisation can inspect what happened, under what conditions, with which actors, producing which outputs, and preserve the result — including failures and unknowns — for internal governance, audit, or collaborative review. Harness does not certify truth; it provides the controlled execution and evidence layer so others can judge.

## BOUNDARIES
- Harness records evidence; it does not magically certify the truth of an experiment.
- Harness does not claim consciousness, hallucination elimination, or guaranteed compliance.
- Upstream actor correctness (e.g., ECA `GateOk`) is owned by that actor, not by Harness execution.
- `ECA/PER` in V1 are `OFF` (transport only); `MOCK` is explicitly `MOCK`; `LIVE` is `BLOCKED` without credentials (`failed_policy: MATRIX_BLOCKED_UNTIL_SWITCH_WIRED` in `adapters/per_eca.py`).
- Engineering figure `108/108` on fresh clones `522b4fd` is reproducibility, not accuracy.

## WHO ASKS THIS STORY
(See `V1_CAPABILITY_MATRIX.md` for capabilities, `V1_LIMITATIONS.md` for boundaries, `COMMERCIAL_CLAIM_REGISTER.md` for claim classification.)

