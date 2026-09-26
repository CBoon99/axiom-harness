# Status Vocabulary — Axiom Lab Harness — 2026-09-26

**Scope:** House Order §4 — one authoritative vocabulary, lifecycle ≠ outcome.

## Lifecycle Status (where in workflow)
- `PLANNED` — defined, not yet ready (no input freeze)
- `READY` — input/config/environment frozen, can run
- `RUNNING` — execution in progress
- `PAUSED` — intentionally paused, can resume
- `BLOCKED` — dependency missing (e.g. `MATRIX_BLOCKED_UNTIL_SWITCH_WIRED` per_eca OFF)
- `CANCELLED` — stopped before completion by human
- `COMPLETE` — run finished (says nothing about success — must pair with OUTCOME)
- `SUPERSEDED` — replaced by new RUN_ID with new method/version
- `ARCHIVED` / `HISTORICAL` — closed, indexed, not active (§14/§33)

## Outcome Status (what the evidence says)
- `PASSED` — `PASS_CONDITION` met, `orphans[]==0`, `verify_result PASS`
- `FAILED` — `FAIL_CONDITION` met or `verify_result failed_policy`
- `PARTIALLY_VALID` — some artefacts valid, some missing/invalid
- `REFUSED` — `ΔH≤0.5` or `C<N` fail-closed `INSUFFICIENT_EVIDENCE` (§6.3-6.5)
- `BLOCKED` (outcome) — cannot evaluate due to missing input/proof (re-use lifecycle term only where block is outcome)

## Combined (never collapse)
- A completed run is `LIFECYCLE: COMPLETE + OUTCOME: PASSED` or `COMPLETE + FAILED` or `COMPLETE + PARTIALLY_VALID`
- Do NOT use `COMPLETE` to mean `PASSED`
- Do NOT use one field for both

## Usage
- `EXPERIMENT/MASTER` → `STATUS` = lifecycle
- `RUN` → `LIFECYCLE_STATUS + OUTCOME_STATUS`
- `TEST` execution → `RESULT` `PASSED/FAILED` + `RECEIPT_ID`
- `PACK` → `VALIDATION_STATUS` `PASSED/FAILED/PARTIALLY_VALID`

Examples:
- `RUN-P01-100-ACQUISITION — LIFECYCLE COMPLETE, OUTCOME PASSED, 18cell/WTF-005A-RUN-01 verified`
- `RUN-P03-250-FIND — LIFECYCLE COMPLETE, OUTCOME FAILED, ΔH≤0.5 91% refusal (firewall, not failure to run)`
