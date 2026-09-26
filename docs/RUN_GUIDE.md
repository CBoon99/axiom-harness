# RUN GUIDE — Axiom Lab Harness — 2026-09-26

**15-step, explicit STOP conditions — House Order §20.**

1. **PRE-RUN CHECK** — `git status --porcelain` clean except `Favorable errors/* + docs/BEST_PRACTICE + math/` untracked existence logs; `MASTER.md` `CURRENT HUMAN READ` says safe.
2. **INPUT FREEZE** — hash inputs via `WTF-005A-HASH-v3` `sort_keys True` — writes `INPUT_MANIFEST`.
3. **CONFIGURATION FREEZE** — `MasterMission frozen=True protected_namespaces=()` + `protocol` hash — no `AXIOM_` hard-code.
4. **ENVIRONMENT CHECK** — `paths.py is_safe_relative` + `AXIOM_STRICT_MODE=1` + `PYTHONPATH`.
5. **TEST/RUN CREATION** — `RUN-<PHASE>-<SCALE>-<PURPOSE>` new ID, never reuse.
6. **EXECUTION** — `HARNESS-CONTROL → SANDBOX/TERMINAL jailed (unshare --net Linux)` via `api/main.py POST /master/* 201/422`.
7. **RECEIPT CAPTURE** — `RECEIPT-<RUN>-NNN` with `INPUT_HASH/OUTPUT_HASH/METHOD_VERSION/STATUS/PATH`.
8. **OUTPUT VERIFICATION** — `outputs/<RUN>/` 5-file seal exists.
9. **HASH VERIFICATION** — `sha256sum -c manifest-sha256.txt` + `B.prev=A` chain.
10. **RESULT CLASSIFICATION** — `LIFECYCLE COMPLETE + OUTCOME PASSED/FAILED/PARTIALLY_VALID` per `STATUS_VOCABULARY.md`.
11. **FINDINGS** — `FINDINGS.md` per acceptance.
12. **HUMAN_INSIGHT** — `HUMAN_INSIGHT.md` (`INTERPRETATION`, not `OBSERVED`).
13. **SEAL** — `WTF-005A-HASH-v3` + `hallmark sealed_by:harness`.
14. **INDEX UPDATE** — `INDEX.json` spine `EXPERIMENTS/PHASES/RUNS/TESTS/PACKS/RECEIPTS`.
15. **CLOSEOUT** — `STATUS.md` `ARCHIVED` or `HISTORICAL` — no `latest`.

**STOP conditions:** missing input freeze, orphans[]!=0, `ai_computed_metrics:true`, `B.prev=A` break, `provider_call_count!=0`, `AXIOM_ hard-code` via `rg`, `file://` headless non-white screenshot not read back.

*House Order §20 — no maths changed.*
