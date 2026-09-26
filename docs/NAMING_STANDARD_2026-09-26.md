# Naming Standard — Axiom Lab Harness — 2026-09-26

**Scope:** House Order §3 — permanent convention. Historical IDs remain HISTORICAL (§33).

## EXPERIMENT
`EXP-<DOMAIN>-<NNN>` — frozen at creation, never reused
- `EXP-ECA-001` — ECA gate
- `EXP-HARNESS-001` — Harness V1
- `EXP-WTF-001` maps to legacy `WTF-001` (kept as HISTORICAL alias)
- `EXP-HUMAN-001` maps to `HUMAN-2026-08-01` instrument family

## TEST
`TEST-<DOMAIN>-<NNN>` — first-class property checks (§10-11)
- `TEST-INPUT-BOUNDARY-001` — is_safe_relative iterative unquote
- `TEST-PROVENANCE-001` — ai_computed_metrics:false Literal[False]
- `TEST-DETERMINISM-001` — same inputs → same procedure (not same model output)
- `TEST-TRACEABILITY-001` — B.prev=A chain
- Taxonomy (§11): `TEST-INGESTION/PROVENANCE/INTEGRITY/BOUNDARY/DETERMINISM/REPEATABILITY/ISOLATION/CONFIGURATION/FAIL-CLOSED/TRACEABILITY/RESOURCE/SECURITY/REGRESSION-xxx` — extend, never duplicate because old exists

## PHASE
`P00_<NAME>` — zero-padded
- `P00_BASELINE`, `P01_ACQUISITION`, `P02_FIND`, `P03_REPEATABILITY`, `P04_HUMAN` — maps to §76 V1.1→V3

## RUN
`RUN-<PHASE>-<SCALE>-<PURPOSE>` — new ID per execution, re-run gets new RUN_ID
- `RUN-P01-100-ACQUISITION` — 100 acquire
- `RUN-P03-250-FIND` — 250 find
- `RUN-P03-250-REPEATABILITY` — repeat

## BATCH
`BATCH-<NNN>-<DESCRIPTION>` — operational grouping of RUNS
- `BATCH-001-SEAL` — 18cell WTF-005A seal

## PACK
`PACK-<EXPERIMENT>-<RUN>-<NNN>` — bounded sealed deliverable
- `PACK-EXP-WTF-001-RUN-P01-100-001` → `outputs/WTF-001/deliverable.zip`

## RECEIPT
`RECEIPT-<RUN>-<NNN>` — lowest verification
- `RECEIPT-RUN-P01-100-001` — input_hash + output_hash + method_version

## Forbidden
Never use: `run1/run2/test-final/latest/new/new2/final/final-final/final-clean/backup-final` — never use `latest` as identity, never reuse an ID, superseding execution gets new ID.

## Historical handling
- Legacy `WTF-001`, `HUMAN-2026-08-01`, `WTF-005A-RUN-01` remain HISTORICAL per §33 (do not move if breaks B.prev=A)
- New experiments/tests from today use this standard exclusively
