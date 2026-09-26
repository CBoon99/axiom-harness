# ARCHITECTURE — Axiom Lab Harness — 2026-09-26

```
LAB (Axiom Lab Harness / Staging)
  → HARNESS (axiom_harness/ + api/ + app/ — boring, jailed, hash-sealed)
  → EXPERIMENTS (missions/ + outputs/WTF-001 + Human Axiom)
  → METHODS (WTF-005A-HASH-v3 + Human 8D)
  → TESTS (tests/test_*.py 139)
  → EXECUTION (POST /master/* jailed, unshare --net Linux)
  → RECEIPTS (outputs/*/manifest-sha256.txt + verify_result.json)
  → PACKS (deliverable.zip)
  → REPORTING (FINISH: proof/HARNESS_V1_FINAL_ACCEPTANCE_2026-09-24.md)
  → ARCHIVE (archive/ — not yet populated)
```

**Planes:**
- **Control Plane:** `MASTER.md + INDEX.json + HUMAN_OPERATING_GUIDE + SETUP.md` — makes decisions (`proposal → human approve`).
- **Execution Plane:** `SANDBOX/TERMINAL` (`axiom_harness/paths.py is_safe_relative + workbench allowlist`) — executes, does not decide.
- **Evidence Plane:** `outputs/ + manifest.py B.prev=A + verify.py orphan[]` — records.
- **Reporting Plane:** `FINDINGS.md + HUMAN_INSIGHT.md + deliverable.zip` — interprets, never overwrites evidence.

18-cell matrix: 12 primary + 4 prevalence + 2 duplicate (§18-20) — WTF as leaf, not harness.

*House Order §27 — no maths changed.*
