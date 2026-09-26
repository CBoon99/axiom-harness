# VERIFICATION GUIDE — Axiom Lab Harness — 2026-09-26

**Independent verifier checks (§21) — House Order only.**

For any `RUN-<PHASE>-<SCALE>-<PURPOSE>`:

1. **What was tested:** `TEST_ID` from `tests/test_*.py` + `TEST-...` taxonomy (§11).
2. **What input:** `INPUT_MANIFEST` hash `WTF-005A-HASH-v3` — `sha256sum -c`.
3. **What version:** `harness_version` `f024fee` + `method_version` `WTF-005A-HASH-v3 / Human 8D`.
4. **What configuration:** `MasterMission` `protocol` + `AXIOM_STRICT_MODE=1` + `HARNESS_PORT`.
5. **What output:** `outputs/<RUN>/` 5-file + `deliverable.zip` if `PACK`.
6. **Whether altered:** `HEX_RE` stripped before `NUM_RE` orphan check — `verify.py` canonical `sort_keys` — `manifest-sha256.txt` must `sha256sum -c` pass.
7. **Hashes match:** `B.prev=A` chain `prev_receipt_hash` across `DB_SCHEMA experiments/sandboxes/events/timelines/evidences`.
8. **Receipts complete:** `RECEIPT-<RUN>-NNN` exists per `RECEIPT_INDEX`.
9. **Reported result matches artefact:** `FINDINGS.md` numbers must appear in `DECISION_SUMMARY.json`/`scenario.csv` or `orphans[]` → `failed_policy`.
10. **Reproducible:** New `RUN_ID` with same `INPUT_MANIFEST` → `OUTPUT_HASH` should match (deterministic procedure, model stochasticity measured per `§26`).
11. **Claim vs evidence:** `OBSERVED` (raw `RUN`) vs `DERIVED` vs `INTERPRETATION` vs `HYPOTHESIS` — verifier travels `REQUIREMENT→EXPERIMENT→METHOD→RUN→RECEIPT→FINDING` both directions (§25).

*House Order §21 — read-only.*
