# Experiment Governance — §7-12 — 2026-09-26

**House Order §7 Experiment Standard:** Every NEW `EXP-<DOMAIN>-<NNN>/` starts with `MASTER.md + INDEX.md + INDEX.json + EXPERIMENT.json + METHOD.md + STATUS.md + CHANGELOG.md` + `PXX_<NAME>/PHASE_SUMMARY.md` where applicable. `EXPERIMENT.json` must have `experiment_id, display_name, purpose, owner, created_at, status, method_version, harness_version, environment_reference, input_boundary, output_boundary, hypothesis/question, stop_conditions, acceptance_criteria, reproducibility_requirements` — never loose scripts.

**§8 Phase:** `PXX_<NAME>/PHASE_SUMMARY.md + FINDINGS.md + HUMAN_INSIGHT.md + runs/<RUN_ID>/` — `PHASE_SUMMARY` aggregates only (`PURPOSE, INPUTS, RUNS INCLUDED, TESTS/PACKS, KEY RESULTS, VALIDATION, LIMITATIONS, BLOCKERS, CURRENT HUMAN READ, HASH REFERENCES`) — never invents evidence.

**§9 New Run:** `runs/<RUN_ID>/` with `RUN_SUMMARY.md + FINDINGS.md + HUMAN_INSIGHT.md + INPUT_MANIFEST + OUTPUT_MANIFEST + RECEIPT_INDEX` — before `COMPLETE`: input/config/env/method version recorded, inputs/outputs hashed, receipts exist, failures recorded, no artefact missing. Historical runs `GRANDFATHERED` — do NOT move; re-execution gets new `RUN_ID`.

**§10 Test Standard:** `TEST_ID/PURPOSE/SCOPE/PRECONDS/INPUTS/EXPECTED_BEHAVIOUR/OBSERVABLE/PASS/FAIL/STOP/RECEIPTS/RESULT/LIMITATIONS` — `TEST = Does this property hold?` vs `EXPERIMENT = What are we trying to learn?`

**§11 Taxonomy:** `TEST-INGESTION/PROVENANCE/INTEGRITY/BOUNDARY/DETERMINISM/REPEATABILITY/ISOLATION/CONFIGURATION/FAIL-CLOSED/TRACEABILITY/RESOURCE/SECURITY/REGRESSION-xxx`

**§12 Pack:** `PACK_ID/PARENT_RUN/PACK_TYPE/PURPOSE/INPUT_MANIFEST/OUTPUT_MANIFEST/METHOD_VERSION/CONFIGURATION/RESULT/PROVENANCE/RECEIPTS/HASHES/VALIDATION_STATUS` + optional `SUMMARY/METRICS/PLOTS/RAW/DERIVED/VERIFICATION/DECISION` — never mix `raw evidence / derived / interpretation / marketing` without boundary.

**§13 Receipt:** `RECEIPT-<RUN>-<NNN>` answers `What/When/Config/Input/Code/Output/Hash/Failed/Succeeded` — historical, never rewritten.

*No maths/tests changed.*
