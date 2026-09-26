# HUMAN OPERATING GUIDE — Axiom Lab Harness — 2026-09-26

## Set up new EXPERIMENT → close
`SET UP NEW EXPERIMENT → DEFINE METHOD (METHOD.md) → DEFINE INPUT BOUNDARY → DEFINE ACCEPTANCE → FREEZE INPUTS (hash) → CREATE RUN (RUN_ID) → EXECUTE (python3 -m axiom_wb jailed) → CAPTURE RECEIPTS → VERIFY (orphans[] + B.prev=A + sha256sum -c) → WRITE FINDINGS → WRITE HUMAN_INSIGHT → SEAL (WTF-005A-HASH-v3) → INDEX (INDEX.json) → CLOSE/ARCHIVE`

## Inspect failure
`INDEX.json → RUN_ID → RECEIPT_INDEX → verify_result.json failed_policy → INCIDENT_RESPONSE.md INCIDENT_ID → logs outputs/<RUN>/`

## Reproduce a run
New `RUN_ID` (never reuse), same `INPUT_MANIFEST + METHOD_VERSION + HARNESS_VERSION` from old `RECEIPT`, `PYTHONPATH="$PWD" /Library/Developer/CommandLineTools/usr/bin/python3 -m pytest tests/test_<id>.py` — compare `OUTPUT_HASH`.

## Compare two runs
`diff -r outputs/RUN-A outputs/RUN-B` + `diff MANIFEST` + `HARNESS_V1_FINAL_ACCEPTANCE_2026-09-24.md` style.

## Verify a hash
`sha256sum -c manifest-sha256.txt` or `python3 axiom_harness/manifest.py` `WTF-005A-HASH-v3`.

## Authoritative version
`MASTER.md` + `INDEX.json` `status: CURRENT/HISTORICAL/SUPERSEDED` — never filename alone.

## Superseded / ambiguous
`SUPERSEDED` gets new `EXPERIMENT_ID`; `UNKNOWN` → `STOP, MARK UNKNOWN, REPORT` per `AGENT_OPERATING_GUIDE.md`.

## Safe stop
`POST /master/human` etc. `failed_policy 422` leaves no `B.prev=A` — kill with `STOP` (not `delete`), preserve `RECEIPT`.

*House Order §18 — no maths changed.*
