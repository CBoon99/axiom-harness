# AXIOM HARNESS V1 — ONE PAGER
**BoonMind Labs — Governed Experimental / Evidence Execution Environment**

## The problem
AI experiments are often difficult to reproduce, compare, audit and explain after the fact. Teams run models informally, lose the conditions, and cannot show exactly what happened under which inputs, with which actors, and with what evidence preserved.

## The solution
Axiom Harness provides a controlled environment for running, comparing and sealing AI experiments. Define the experiment, freeze the conditions, run isolated actors/models, and preserve a sealed record.

## How it works
**Control → Sandbox → Run → Compare → Timeline → Seal → Export**

1. **Control** — define experiment, model, context, environment parameters.
2. **Sandbox** — keep runs isolated and governed.
3. **Run / Sequence / Parallel** — run controlled and repeated/parallel conditions.
4. **Live Room** — compare multiple actors/models/humans under controlled context.
5. **Timeline** — preserve event order and execution history.
6. **Sealed Evidence** — produce canonical seal and provenance record (`SCENARIO.json/scenario.csv/DECISION_SUMMARY.json/MANIFEST.json/verify_result.json`, chain `B.prev=A`, `ai_computed_metrics:false`).
7. **Export** — produce documented evidence/export pack.

## What the buyer gets (V1)
- Controlled, bounded, repeatable runs — not informal logs.
- Isolated execution with fail-closed boundaries.
- Provenance-backed receipts and sealed results.
- Multi-actor comparison under same conditions.
- An auditable record: what happened, under what conditions, with which actors, producing which outputs.

## Boundaries (what V1 does not claim)
- Does not claim truth, consciousness detection, hallucination elimination, perfect behaviour, guaranteed compliance, or that every result is correct.
- Does not certify an upstream actor (ECA/PER) as correct merely because Harness executed it.
- `ECA/PER` run as governed upstream actors (`per:OFF/eca:OFF` in V1, `MOCK` explicitly `MOCK`, `LIVE` blocked without credentials).
- **Engineering result:** `108/108` fresh-clone tests on `522b4fd` (two arbitrary `/tmp` clones, `Python 3.9.6` `pytest 7.4.3`) — a reproducibility figure, **not** an accuracy/reliability claim.

## Who it is for (plausible, not invented)
AI research teams, AI safety/evaluation teams, regulated organisations, internal AI governance teams, AI product teams, organisations conducting sensitive AI experimentation, independent researchers, consultancies needing reproducible AI evaluation.

## What V1 is and what comes next
- **V1** — controlled experimental execution + evidence/provenance.
- **V1.8** — Multi-agent room (Analyst / Critic / Maker / Observer / Adversary)
- **V1.9** — Patch Illusion Visual
- **V2/V3** — later expansion / Human Axiom

Future rooms add capability without redefining V1 promise.

## Cost to verify
Clone `Staging` at `522b4fd` to any directory, `pip install -r` (if pinned) or `pytest` with `pydantic`/`pytest` present, `python3 -m pytest -q` → `108 passed`.

