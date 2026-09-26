# LAB GUIDE — How to Use Axiom Lab Harness — 2026-09-26
**Status:** CURRENT — Owner: Carl Boon — Harness root: `Staging/`
**Parent docs:** `MASTER.md` (what lab is) → `INDEX.md/json` (spine) → this guide (how to use)
**Applies to:** Axiom-Workbench + PER + ECA + WTF as bolt-on `frozen Optional` rooms

## 1 What to read first (3 files, 5 minutes)
1. `docs/CURRENT_HUMAN_READ.md` — fast briefing (HEAD, what is proven, what is not, safe vs dangerous)
2. `MASTER.md` — human entry point (§1-9: what harness is, trust model, boundaries)
3. `INDEX.md` + `INDEX.json` — spine: find any EXPERIMENT / TEST / RUN / PACK / RECEIPT without searching filesystem

## 2 How the lab is organised (copy best-practice, not trial-and-error)
Based on `docs/BEST_PRACTICE_LAB_SYSTEMS_2026-09-26.md` (Bika/Senaite, Benchpress, OpenLIMS, LaminDB, FAIR):

- **LIMS for samples/workflows, ELN for notes, Scheduler for runs — connected via API.** Harness does same: 9 rooms `CONTROL / MODEL / SANDBOX / RUN / LIVE / TIMELINE / EVIDENCE / ANALYSIS / EXPORT` connected via `POST /api/master/* 201/422` (see `docs/CONCEPTUAL_ARCHITECTURE_2026-09-26.md`), not siloed scripts.
- **Polyglot modular:** Benchpress `instrument → ingestion → core API → ELN/LIMS → Dashboard, every step traceable`. Harness: `SANDBOX/TERMINAL/TOOLS/DATA/SENSORS → EVENT+TRANSCRIPT+STATE → EVIDENCE LAYER → ANALYSIS → REPORT` (§12 RENDERS_ARE_EVIDENCE).
- **FAIR + lineage + lakehouse:** LaminDB pattern — Harness uses `WTF-005A-HASH-v3 sort_keys True ensure_ascii False (",",":") + B.prev=A chain + SHA-256 manifest + ledger>narrative` — already FAIR (see `docs/DOCUMENTATION_STANDARD_2026-09-26.md` §26).
- **Audit trail on every mutation:** OpenLIMS/Benchling — Harness keeps `sealed_by/at/instrument/sop_version + RECEIPT_ID + smokes 5/5 + ai_computed_metrics:false` hallmark.
- **Self-hosted, RBAC, frozen config:** `AXIOM_STRICT_MODE=1` canary + `Path(__file__).parents[1]` + `frozen=True protected_namespaces=()` configs (see `docs/SETUP.md`).

**Rule:** Keep laboratory boring, make experiments interesting. Mechanics bounded/recorded/versioned/sealed — experiments wild.

## 3 How to set up (lab + data)
See `docs/SETUP.md` (no verbally-remembered steps):

- **Required:** `Staging/` with `axiom_harness/ missions/ tests/ app/ docs/ proof/ outputs/` + Python `/Library/Developer/CommandLineTools/usr/bin/python3 pydantic 2.5.0` + `agent-browser 0.34.0 Chrome 152`
- **Env:** `STAGING_ROOT = Path(__file__).parents[1]` asserts `axiom_harness/` exists; optional `AXIOM_ENGINE_ROOT` only if `AXIOM_STRICT_MODE=0`; `HARNESS_PORT` defaults
- **Isolation:** `axiom_harness/paths.py is_safe_relative iterative unquote depth 10 + resolve().relative_to` — verify `test_jail_canonical`
- **Data boundary:** inputs frozen via `WTF-005A-HASH-v3` into `INPUT_MANIFEST`; never store blobs in chat — keep `outputs/<RUN>/sandbox/<file>` + `MANIFEST` pointers (lakehouse pattern). For PER/ECA math, see `math/HARDENED_LOCKS.md + PER_ECA_TECHNICAL_REFERENCE.md` — hash-only, not copied.

Verify setup: `env PYTHONPATH="$PWD" PATH="/Library/Developer/CommandLineTools/usr/bin:$PATH" bash smoke.sh` → `5/5`

## 4 How to define + run an experiment (15 steps)
See `docs/RUN_GUIDE.md` (§20) + `docs/HUMAN_OPERATING_GUIDE.md`:

`SET UP NEW EXPERIMENT → DEFINE METHOD (METHOD.md) → DEFINE INPUT BOUNDARY → DEFINE ACCEPTANCE → FREEZE INPUTS (hash) → CREATE RUN (RUN-<PHASE>-<SCALE>-<PURPOSE>) → EXECUTE (HARNESS-CONTROL → SANDBOX jailed POST /master/*) → CAPTURE RECEIPTS (RECEIPT-<RUN>-NNN INPUT_HASH/OUTPUT_HASH/METHOD_VERSION/STATUS) → VERIFY (orphans[]==0 + B.prev=A + sha256sum -c) → FINDINGS → HUMAN_INSIGHT (INTERPRETATION not OBSERVED) → SEAL → INDEX UPDATE → CLOSE/ARCHIVE`

Agent role: see `docs/AGENT_OPERATING_GUIDE.md` (may inspect/hash/verify, may NOT silently change intent/criteria/evidence, STOP→MARK UNKNOWN→REPORT).

## 5 How to test + verify (independent)
See `docs/VERIFICATION_GUIDE.md` (§21 — 11 checks):

- `PYTHONPATH="$PWD" /Library/Developer/CommandLineTools/usr/bin/python3 -m pytest -q` → `139 passed` at `f024fee` (HEAD)
- For any RUN: check `TEST_ID + INPUT_MANIFEST hash + harness_version + config + outputs/<RUN>/ 5-file + manifest-sha256 + B.prev=A + RECEIPT + FINDINGS vs DECISION_SUMMARY + reproducibility (new RUN_ID same inputs → same OUTPUT_HASH)`

## 6 What output looks like (packs + file naming)
See `docs/EXPERIMENT_GOVERNANCE_2026-09-26.md` + `docs/NAMING_STANDARD_2026-09-26.md` + `docs/DOCUMENTATION_STANDARD_2026-09-26.md`:

- **Per RUN (5-file seal):** `SCENARIO.json + scenario.csv + DECISION_SUMMARY + MANIFEST (WTF-005A-HASH-v3) + verify_result.json` + `B.prev=A` chain — `outputs/<RUN>/`
- **Per PACK (22-file):** `deliverable.zip + MANIFEST + verify.html + trail.html` + 8 docs + 3 plot families — see `docs/DOCUMENTATION_STANDARD_2026-09-26.md`
- **Naming:** `EXP-<DOMAIN>-<NNN>` frozen never reused (`EXP-WTF-001` HISTORICAL alias `WTF-001`), `TEST-<DOMAIN>-<NNN>` taxonomy (§11), `RUN-<PHASE>-<SCALE>-<PURPOSE>`, `RECEIPT-<RUN>-NNN`, `PACK-EXPORT-NNN` — all in `docs/NAMING_STANDARD_2026-09-26.md`
- **Indexes:** `EXPERIMENT_INDEX.md` / `TEST_INDEX.md` / `RECEIPT_INDEX.md` at root + `INDEX.json` spine — every entity discoverable without `find`

## 7 Where to find things
- Spine: `MASTER.md` (root), `INDEX.md/json` (root), `EXPERIMENT_INDEX.md` / `TEST_INDEX.md` / `RECEIPT_INDEX.md` (root)
- Setup/Run/Verify: `docs/SETUP.md` / `docs/RUN_GUIDE.md` / `docs/VERIFICATION_GUIDE.md`
- How to use: this file + `docs/HUMAN_OPERATING_GUIDE.md` + `docs/AGENT_OPERATING_GUIDE.md`
- Change/Incident: `docs/CHANGE_CONTROL.md` / `docs/INCIDENT_RESPONSE.md`
- Best practice copy: `docs/BEST_PRACTICE_LAB_SYSTEMS_2026-09-26.md` — do not re-trial architectures
- Math (hash-only existence): `math/HARDENED_LOCKS.md` etc — tweakable modules, not engine
- Proof: `proof/HARNESS_PREFLIGHT_2026-09-26.md/json` — `5/5 smoke + 11-page headless`

## 8 Quick commands
```bash
PYTHONPATH="$PWD" /Library/Developer/CommandLineTools/usr/bin/python3 -m pytest -q   # 139 passed
env PYTHONPATH="$PWD" PATH="/Library/Developer/CommandLineTools/usr/bin:$PATH" bash smoke.sh  # 5/5
agent-browser open "file://$PWD/app/index.html"  # require_escalated on macOS
sha256sum -c outputs/<RUN>/manifest-sha256.txt
```
