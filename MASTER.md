# MASTER — Axiom Lab Harness — Human Entry Point — 2026-09-26

**Version:** HOUSE ORDER V1 — Status: `CURRENT` — Owner: Carl Boon — Harness root: `Staging/`

## 1 What Axiom Lab Harness is
A permanently understandable, repeatable **laboratory environment** (`LAB`) that governs `Axiom-Workbench` deterministic engine runs, `PER` hypercube bisection (`C=∏|Aj|, ΔH>0.5`), `ECA` `EARNED_CONTEXT_LOCK`, and `WTF` sequential intelligence experiments as bolt-on isolated rooms (`frozen Optional` unions) — all evidenced via `WTF-005A-HASH-v3 + B.prev=A`.

## 2 What it is for
To let a stranger tomorrow `find experiment → define new experiment → freeze inputs → execute → capture receipts → verify → reproduce` without Carl explaining verbally. Evidence `ledger>narrative, orphan[]=0`.

## 3 What it is NOT
- Not a model — `BOON AI / LVM` runs *inside* `SANDBOX`, not as lab.
- Not a vector RAG — `0 raw tokens until |R|≤3`.
- Not a marketing benchmark — `Null/failure receipts matter`.

## 4 Laboratory boundaries
`HUMAN → HARNESS-CONTROL → EXPERIMENT CONFIG → SEALED ENV → BOON AI/other → SANDBOX/TERMINAL/TOOLS/DATA/SENSORS → EVENT+TRANSCRIPT+STATE → EVIDENCE LAYER → ANALYSIS → REPORT/REVIEW/EXPORT`. `AI DOES NOT CONTROL THE LABORATORY` (`proposal → human approve → harness executes → recorded`).

## 5 Trust model
`Zero-Trust Epistemic Airgap` — `EARNED_CONTEXT_LOCK.md` state machine, `8 hardened locks` (`NFC jail → SHA-256 lockfile → unshare --net → frozen extra=forbid → Literal[False] → Enum allowlist → Decimal verifier → canonical root`), `ai_computed_metrics:false` hallmarked, `sealed_by/at/instrument/sop_version`.

## 6 Evidence model
`5-file seal` (`SCENARIO.json, scenario.csv, DECISION_SUMMARY, MANIFEST, verify_result`) per `RUN` → `22-file pack` (`deliverable.zip + MANIFEST + verify.html + trail.html`) — `B.prev=A` chain, `sort_keys True ensure_ascii False separators (",",":")`.

## 7 Experiment lifecycle
`PLANNED → READY (freeze) → RUNNING → COMPLETE + PASSED/FAILED/PARTIALLY_VALID → ARCHIVED/HISTORICAL` — lifecycle ≠ outcome (see `STATUS_VOCABULARY.md`).

## 8 Naming system
`EXP-<DOMAIN>-<NNN>` + `TEST-<DOMAIN>-<NNN>` + `P00_<NAME>` + `RUN-<PHASE>-<SCALE>-<PURPOSE>` + `PACK-…` + `RECEIPT-…` ([NAMING_STANDARD.md](docs/NAMING_STANDARD_2026-09-26.md)) — historical `WTF-001/HUMAN-2026` stays `HISTORICAL`.

## 9 Where experiments live
`missions/master_demo_wtf001.yaml` (demo), `outputs/` (sealed runs `18cell/WTF-005A-RUN-01..18, _HARNESS_ECA_GATED, smoke_001`), `methods/` (future).

## 10 Where tests live
`tests/test_*.py` (20 files, `test_harness_boundary 12 + test_multi_agent_v18 6 + test_video_v19 5 + test_films_v2 5 + test_observatory_external 7 + test_human_v3 5 + test_export_v1 3` — `139 passed` HEAD `f024fee`).

## 11 Where receipts live
`outputs/<RUN>/` (`RECEIPT-<RUN>-NNN` → `manifest-sha256.txt + deliverable.zip + verify.html + trail.html`), indexed in `INDEX.json` (next).

## 12 Where archived material lives
`archive/experiments/runs/tests/generated/superseded/deprecated/` — not yet populated; historical `outputs/18cell` stays in place per §33 (do not move if breaks hashes).

## 13 How to create a new experiment
Create `experiments/EXP-<DOMAIN>-<NNN>/` with `MASTER.md + INDEX.md + EXPERIMENT.json + METHOD.md + STATUS.md + CHANGELOG.md` per §7, then `PXX_<NAME>/PHASE_SUMMARY.md` — never loose scripts.

## 14 How to create a new test
Define `tests/test_<domain>_*.py` as `TEST_ID/PURPOSE/SCOPE/PRECONDS/INPUTS/EXPECTED/PASS/FAIL/STOP/RECEIPTS/RESULT/LIMITATIONS` per §10-11 — `frozen Optional` bolt-on.

## 15 How to run a test
`PYTHONPATH="$PWD" /Library/Developer/CommandLineTools/usr/bin/python3 -m pytest -q` → `139 passed` — pre-run check `is_safe_relative iterative unquote` + ` rg GateOk →0`.

## 16 How to run an experiment
`SETUP.md → RUN_GUIDE.md` (PRE-RUN CHECK → INPUT FREEZE → CONFIG FREEZE → ENV CHECK → CREATE RUN → EXECUTE via `python3 -m axiom_wb` jailed → RECEIPT CAPTURE → VERIFY `orphans[]` → CLASSIFY → SEAL → INDEX → CLOSEOUT). Where `HARNESS_PORT` etc. exist, they are in `SETUP.md`.

## 17 How to verify a result
`VERIFICATION_GUIDE.md` — check `what tested, input hash, version, config, output, hash match, receipt completeness, B.prev=A chain, reproducibility, claim vs evidence` — `sha256sum -c MANIFEST`.

## 18 How to investigate failure
`INCIDENT_RESPONSE.md` — `INCIDENT_ID/DATE/SYSTEM/RUN/TEST/OBSERVED/EXPECTED/ROOT_CAUSE/CONTAINMENT/HISTORICAL_IMPACT/RECEIPTS/NEXT_ACTION` — preserve failure, new receipt on fix.

## 19 What agents may do
Inspect, index, classify, hash, verify, propose, summarize existing evidence, execute authorised `pytest`, create new `RUN` under standard ([AGENT_OPERATING_GUIDE.md]).

## 20 What agents may NOT do
Silently change intent/criteria/ground truth, overwrite history, remove failed tests, change thresholds/code during validation, declare commercial viability, convert `INTERPRETATION` → `OBSERVED` — when uncertain `STOP, MARK UNKNOWN, REPORT`.

## 21 What humans may do
Define `METHOD`, freeze inputs, approve `proposal→execute`, adjudicate `FINDINGS vs HUMAN_INSIGHT`, close/archive — per `HUMAN_OPERATING_GUIDE.md`.

## 22 What requires explicit human approval
New `EXPERIMENT`, `METHOD_VERSION` change, `PER/ECA` switch from `OFF`, `push live`, `ARCHIVE` move that would break `B.prev=A`, any `AXIOM_STRICT_MODE=0` override.

## 23 How historical material is protected
Never move if `receipt paths / hashes / manifests / references / reproduction` would break — leave `HISTORICAL` in place, surface via `INDEX` (§33-34). Never `latest` as identity.

## 24 What "sealed" means
`SHA-256` of canonical `sort_keys True ensure_ascii False` `WTF-005A-HASH-v3` at `manifest.py:15` + `hallmark sealed_by:harness sealed_at:ISO instrument:axiom_wb` + `ai_computed_metrics:false` enforced at `core_types.py:421` — correcting it creates new `RECEIPT`, never rewrites.

## 25 What "reproducible" means
Per HOUSE ORDER §24: *preserve enough about methods, inputs, config, analysis, outputs for independent reproduction/verification* — `REPPEATABLE (same lab), REPRODUCIBLE (different lab), VERIFIABLE (hash + receipt), DETERMINISTIC (same procedure, not same model output per 005 lesson), SEALED`.

## 26 Current laboratory state
- **Version:** `f024fee` (`edaf935 Noise fix → c4cddcc Human V3 → b99f059 Sync → 5f99870 Export`) — `139 passed 0 warnings`, `smoke 5/5`.
- **Maths:** `hardened 8 locks 71e3be70` copies to `axiom_future + axiom_evidence`, `math/*` hash-only.

## CURRENT HUMAN READ (honest, no marketing)
- **Working:** `V1.1-V1.9/V2/V2+/V3 Human/Export` bolt-ons — `app/*.html` 7 rooms + 5 wireframes, `POST /master/* 201/422` 9 endpoints, `B.prev=A` chain.
- **Broken:** `world-a.netlify.app` not `curl`-verified, `docs/wireframes vs app/wireframes` historically drifted (now `docs/CANONICAL_WIREFRAMES.md` fixes), `VisualConfig` not added (reverted per your cross-contam guard).
- **Proven:** `V1.7 18cell 5-file seal` + `ECA 66/66` + `36 cell blocks` + headless `22` screenshots `1280/390` reflow correct.
- **Not proven:** `V2+ Observatory` per-feed alerts live with real feed (stub only), `External API` generic `base_url` not yet wired to real `world-a` ingest.
- **Historical:** `WTF-001, HUMAN-2026, 18cell, _HARNESS_ECA_GATED` stays authoritative.
- **Blocked:** `PER/ECA` `OFF` until you wire `ReceiptIndex` + real `AXIOM_ENGINE_ROOT` maths (§6 hard locks prevent `GateOk` calc in Harness).
- **Safe to run:** `pytest -q`, `smoke.sh` (with `PYTHONPATH="$PWD" PATH="/Library/Developer/CommandLineTools/usr/bin:$PATH"`), `file://` browser `open/snapshot/screenshot` on `app/*.html`.
- **Requires approval:** `new EXPERIMENT`, `METHOD_VERSION` change, `PER/ECA ON`, `push live`, `ARCHIVE` move, `AXIOM_STRICT_MODE=0`.

