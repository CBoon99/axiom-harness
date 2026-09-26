# Conceptual Architecture — Axiom Lab Harness — 2026-09-26

**Scope:** House Order §2 — establish unambiguous terms. No maths/tests changed.

## Definitions

- **LAB:** The permanent governed environment — `Axiom Lab Harness / Staging` (`STAGING_ROOT = axiom_harness/ + missions/`). Provides governance, evidence plane, and reproducibility guarantees. Not an experiment.
- **EXPERIMENT:** A bounded scientific question — e.g. `EXP-WTF-001` / `WTF-001` / `Human 8D — 80 dilemmas`. Has `EXPERIMENT.json` contract (`purpose, owner, hypothesis, input_boundary, output_boundary, stop_conditions, acceptance_criteria`). Answers: *What are we trying to learn?*
- **PHASE:** A logical stage within an experiment — `P01_ACQUISITION, P02_FIND` etc. Aggregates `RUNS`/`TESTS`/`PACKS`. Has `PHASE_SUMMARY.md`.
- **BATCH:** A grouping of `RUNS` executed together — `BATCH-001-DESCRIPTION`. Provides operational batching, not scientific identity.
- **RUN:** One execution of an `EXPERIMENT`/`PHASE` against frozen inputs — `RUN-P01-100-ACQUISITION`. Has `RUN_SUMMARY.md + INPUT_MANIFEST + OUTPUT_MANIFEST + RECEIPT_INDEX`. Gets a new ID if re-executed (never reuse).
- **TEST:** A first-class property check — `TEST-INPUT-BOUNDARY-001` / `TEST-PROVENANCE-001`. Answers: *Does this specific property hold?* (`PASS/FAIL` vs experiment's *What did we learn?*). Distinct from experiments.
- **PACK:** A bounded sealed deliverable — `PACK-EXP-WTF-001-RUN-P01-100-001` (`deliverable.zip + MANIFEST + verify.html + trail.html` per `media-qc-delivery`). `PACK = result set + evidence output` for one `RUN` slice.
- **RECEIPT:** Lowest-level verification record — `RECEIPT-RUN-001`. Answers: *What happened, when, under what config, input hash, output hash, what failed/succeeded?* Never rewritten; corrections create new receipt.
- **ARTEFACT:** Any file produced by a `RUN`/`TEST` — `SCENARIO.json, scenario.csv, DECISION_SUMMARY.json, MANIFEST.json, verify_result.json, deliverable.zip`.
- **EVIDENCE:** `ARTEFACT` that is hashed and sealed via `WTF-005A-HASH-v3` + `B.prev=A` chain — `ledger > narrative`, `orphans[] = 0`, `ai_computed_metrics:false`.
- **METHOD:** The frozen procedure used — `METHOD.md` + `method_version` (`WTF-005A-HASH-v3`, `Human 8D` instrument). Versioned; changing it creates new `METHOD_VERSION`, not a rerun.
- **RESULT:** Raw output of a `RUN`/`TEST` — `DECISION_SUMMARY + MANIFEST`.
- **FINDING:** Interpreted `RESULT` per `acceptance_criteria` — `FINDINGS.md`.
- **HUMAN_INSIGHT:** Human interpretation of `FINDINGS` — `HUMAN_INSIGHT.md`. Never automatically evidence; classified `INTERPRETATION`.
- **ARCHIVE:** Classified obsolete/superseded material — `archive/experiments/runs/tests/generated/superseded` — left `HISTORICAL` in place if moving would break `B.prev=A` hashes.

## Hierarchy

```
LAB
  ↓
EXPERIMENT (EXP-...)
  ↓
PHASE (P00_...)
  ↓
BATCH (BATCH-...)
  ↓
RUN (RUN-...)
  ↓
TEST (TEST-...-NNN)
  ↓
PACK (PACK-...-NNN)
  ↓
RECEIPT (RECEIPT-...-NNN)
  ↓
ARTEFACT / EVIDENCE (hashed, B.prev=A)
```

**Interpretation layers alongside:**
```
EXPERIMENT → MASTER.md
PHASE → PHASE_SUMMARY.md
RUN → RUN_SUMMARY.md
RESULT → FINDINGS.md
INTERPRETATION → HUMAN_INSIGHT.md
```

All terms are single-meaning — no word means different things in different docs.
