# HANDOFF — FULL ACCOUNT — 2026-09-24

**For the next agent: read this file first. Everything below is verified against the Staging tree on disk. Do not re-derive from summary — run the commands listed.**

**Master frozen:** `Axiom Harness-Master - Dont Touch/` FROZEN `2026-09-24 05:39` — do not touch until `push live`. Contains `AXIOM HARNESS Brief (1).md` + `(2).md` each `3172` lines, `diff 0`, `sha256:0a0d0502…` identical, plus `Docs/Copy of AXIOM HARNESS Brief LVM addition not master.md` also identical but marked not master. Provenance: both briefs are the one spec §1-§79 — do not treat as two specs.

**Staging writable:** `Axiom Harness-Master - Dont Touch/Staging/` on disk — paper alias `Axiom-Harness-Staging/` (older docs use the alias; same directory, not a sibling). Git remote `origin` `https://github.com/CBoon99/axiom-harness` + alias `axiom-harness` in older notes. `STAGING_ROOT = Path(__file__).resolve().parents[1]` in `axiom_harness/paths.py:8` — portable since `522b4fd` (structure check `axiom_harness/ + missions/` not name substring). Previously asserted human-readable path substring — broke fresh clone at generic `/tmp` — fixed in REPAIR PHASE 2.

**Briefs define:** `HUMAN → HARNESS-CONTROL → EXPERIMENT CONFIG → SEALED ENV → BOON AI/other models → SANDBOX/TERMINAL/TOOLS/DATA/SENSORS → EVENT+TRANSCRIPT+STATE → EVIDENCE LAYER → ANALYSIS → REPORT/REVIEW/EXPORT`. Golden Rule: **AI DOES NOT CONTROL THE LABORATORY** — `proposal → human approve → harness executes → recorded`, no silent mutation. Philosophy §77: *Keep laboratory boring. Make experiments interesting.* Stack §55: one `EXPERIMENT` object (Identity/Protocol/Config/Model/Env/Permissions/Data/Sensors/Timeline/Transcript/Audio/Video/Events/Evidence/Analysis/Reviews/Reports/Renders).

---

## Where we started

- Empty Staging with only `README.md` + `PROJECT_PROFILE.md` (P0 planning). No `axiom_harness/`, no tests, no API. Master witness only.
- Upstreams read-only, never reimplemented: `Axiom-Workbench/axiom_wb` (deterministic engine), `Axiom Future/*` (seal_pair B.prev=A), `Axiom Evidence Layer/PER-Core` + `ECA` + `ECA/sim/telescope.py` + `World-A-EvoCycles/` + `Epistemic-UX-Stress-Harness/` + `world-a/` — all preserved as evidence, not duplicated. Provisional labels `WTF/PER/ECA` kept but code uses generic `experimental_programme/retrieval_telescope/earned_context_gate` until brand lock — `Push Back or Ask`.
- BML methodology locked: Quad + `GLOBAL-AGENTIC-BUILD-SYSTEM-V1.1` + `BML-CODE-HYGIENE-V1.2` + `AGENT_STANDARDS` + brand guide. Budget: one task → one pass → QA → STOP. Local only until `push live`. Every gate separate commit, never amend.

---

## What was built — gate sequence (all on Staging `main`, local only)

```
19ccf2d GATE 1 — HERO/DOCS — PASS
52804a7 GATE 2 — MATH MODULAR MAP — REGISTRY ONLY — PASS
f39594b GATE 3 — BOUNDARY TESTS — PASS         (was 96 → 104 after boundary tests)
c2ff3b3 GATE 4 — DUPLICATE SCAN + FREEZE_V3_ON_HOLD — PASS
307bf6f HARNESS V1 FINAL ACCEPTANCE — REPRODUCIBLE PASS
522b4fd REPAIR PHASE 2 — V1 REPRODUCIBILITY — 18cell generated + path portability
52b6b6e HARNESS V1 VERIFICATION — FRESH CLONE 105/108 (before repair, portability failure)
01c99af GATE 5 — 8-SKILL RIP-APART — PASS
ef3573e COMMERCIAL LOCK — AXIOM HARNESS V1
70b8cf1 TIGHTEN GATE SEMANTICS — reporting correction only (no product change)
b2fca7e DOCS ONLY — ECA provenance separation — HEAD 2026-09-24 20:18 (this handoff base)
```

Each gate is a separate commit (never bundled). Current HEAD `b2fca7e2944a62bc85c17ac8aa32daa00039a0bd` is **13 ahead of origin/main** — not pushed (local only per rule). `git push origin main` still pending your `push live`.

**Interleaved forensic commits** (not gates but evidence):
`405069a FORENSIC AUDIT — ERROR TO FAVOURABLE METRIC BIAS` + `30ce29f AUDIT SUPPLEMENT — HIDDEN / USER-DISCOVERED` + `d075059 ABSOLUTE FULL REPORT — ECA forensic + repair` + `9f3ceb7 Fresh-clone finding: API cannot boot outside this exact folder name` + `cea9728 Boundary repair — HARNESS_BOUNDARY_CLEAN` — these introduced `Favorable errors/*.csv/.md` (8 files) that remain **untracked** (intentional evidence artefacts, not V1 product). Plus `docs/BRIEF_REVOLUTIONARY_V3_SYNTHESIZED.md` untracked (synthesis brief r1+r2+r3+r4).

---

## Current product (HEAD b2fca7e — verified this handoff)

**Code:**
- `axiom_harness/mission.py` 204 lines — `MasterMission` + 7 configs `ScheduleConfig ONCE/INTERVAL/REPEATING/CONTINUOUS/UNTIL/CRON` + `ParallelConfig ONE/SEQUENCE/ALL/PARALLEL 1..64` + `DataConfig CSV/JSON/TEXT/DOCUMENTS/DATASET/IMAGES/AUDIO/VIDEO` + `LanguageConfig 10 codes EN..PT` + `AudioConfig 6 kinds TTS/STT/UPLOADED/LIVE/MODEL_VOICE/HUMAN_VOICE` + `SensorConfig 6 kinds PHYSICAL..IOT` + `LiveConfig 6 feeds NEWS/MARKET/WEATHER/WEB/CUSTOM/SIMULATED` — all `frozen=True`, optional on `MasterMission` (zero-bloat: type exists, runtime only when V3.x demo pack exercises). `participant HUMAN/SCRIPTED/TEAM` reserved for V3, no handler in V1. Dict surfaces `per_eca_state/cost/params/permissions` are plain `dict` (outer frozen only, inner mutable noted in boundary audit — see Remaining risks).
- `axiom_harness/paths.py` 54 lines — `STAGING_ROOT` structure check, iterative `unquote` while-loop depth 10 + `resolve().relative_to` jail (handles `%2525252e` x5+), `is_safe_relative()`, `ALLOWED_SCRIPT_PREFIXES = ["scripts/factory_","AXIOM_"]` anchored on `cmd[2]` only, `jail_for_experiment() → OUTPUTS/<id>/sandbox`.
- `axiom_harness/manifest.py` 23 lines — single canonical hash `WTF-005A-HASH-v3` `sort_keys True ensure_ascii False separators (",",":")` no indent `SHA-256(canonical_messages_bytes)` — used by card·request·receipt·verifier·audit. `write_manifest()` + `write_run_pointer(B.prev=A)`.
- `axiom_harness/adapters/workbench.py` 64 lines — jailed subprocess `python3 -m <module>`, explicit file set `[SCENARIO.json,scenario.csv,DECISION_SUMMARY.json] + extra_files` (not `glob("*")`), `sealed_by/at/instrument/sop_version` hallmark in `verify_result.json`, `AXIOM_ENGINE_ROOT` read-only, timeout `3600`, no `shell=True`.
- `axiom_harness/adapters/per_eca.py` 23 lines — `ensure_off()` raises `MATRIX_BLOCKED_UNTIL_SWITCH_WIRED` for any `per:ON` or `eca:ON` (V1 RED transport gate), `seal_per_eca()` writes `PER_ECA_SKIPPED.json` + `MANIFEST` only — never calculates `GateOk/ΔH/T_max`.
- `api/main.py` 216 lines — 7 endpoints `POST /master/schedule|parallel|data|language|audio|sensors|live` each `201 {sealed:true, config_hash}` or `422 failed_policy`, plus `GET /api/master/health` (honest `engine_present` + `is_safe_relative` not hard-coded true) and `POST /master/seal|pressure|data|…`. Future `V3 GET /master/human/{id}/trail` reserved in `API_SPEC.md` only.
- `missions/master_demo_wtf001.yaml` + `outputs/18cell/WTF-005A-RUN-01..18` (18 cells: 12 primary + 4 prevalence + 2 duplicate T18) generated deterministically via `seal_workbench` if missing — canonical `sort_keys` manifests, `sha256sum -c MANIFEST` green.

**Docs (Staging):**
- `docs/ARCHITECTURE.md` (88 lines) — 9 rooms V1 + plug-in chain V1.1→V2+ + V3 Human Axiom, one-way glass `CONFIG→SANDBOX→RECORDER→ROM→EVIDENCE→ANALYSIS`, canonical contracts §3, `taste` preflight held.
- `docs/TECH_SPEC.md` (48 lines) — `UI→API→Harness→Environment`, 20-room list, lifecycle `ARMED→COMPLETE`, jail/timeout/allowlist.
- `docs/DB_SCHEMA.md` — enums `participant_kind MODEL/HUMAN/SCRIPTED/TEAM`, `lifecycle ARMED..COMPLETE`, tables `experiments/sandboxes/events/timelines/evidences/annotations/reviews` + V3 `persons/instruments/responses` reserved, `experiments.per_eca_state` + `cost` + `model_version` columns (review gap 2).
- `docs/API_SPEC.md` — OpenAPI 3.1 stub + V3 reserved, every `422` is `failed_policy` stored as `events` evidence, `ai_computed_metrics:false` in every `verify_result`.
- `docs/MATH_MODULAR_MAP.md` — **REGISTRY ONLY** (this handoff corrected to actual hashes below) — never source of truth, never duplicated maths. `Harness records IMPLEMENTATION_HASH + CONFIG_HASH only`.
- `docs/BRIEF_REVOLUTIONARY_V2_PATCH_IS_ONE_ROOM.md` + `docs/BRIEF_REVOLUTIONARY_V3_SYNTHESIZED.md` (untracked synthesis) — **Patch Illusion is ONE room V1.8** among 15, not product. 100+ wow tags (#AI-Inside-The-Experiment #Timeline-As-4D-Object #Boundary-As-Data …) are experiment family `WTF-VIS-001…014`.
- `docs/HARNESS_BOUNDARY_AUDIT_2026-09-24.md` — `HARNESS_BOUNDARY_CLEAN` (8 → 12 boundary tests).
- `docs/HARNESS_V1_VERIFICATION_2026-09-24.md` — 105/108 on `c2ff3b3` (before repair, path + 18cell failures).
- `docs/HARNESS_V1_FINAL_ACCEPTANCE_2026-09-24.md` — `HARNESS_V1_REPRODUCIBLE_PASS` on `522b4fd` — **authoritative** (108/108 on two arbitrary `/tmp` clones).
- `docs/FREEZE_V3_2026-09-24_ON_HOLD.md` — `ON HOLD` stamp at `c2ff3b3` (`ef3573e` after correction) — hallmark `sealed_by:harness sealed_at:2026-09-24T00:00:00Z instrument:axiom_wb sop_version:1.0-PATCH-ILLUSION`.
- `docs/BRIEF_REVOLUTIONARY_V3_SYNTHESIZED.md` §6 short actionable lock plan Gate 0→5 (see file).
- `docs/audits/*.md` (8-skill rip-apart) — `architecture/testers/color-contrast+ux/copy/researchers/auditors` etc. + master `AUDIT_MASTER_GAPS_HALLUCINATIONS.md`.
- `docs/commercial/*` — `COMMERCIAL_ONE_PAGER_V1.md` + `BUYER_STORY + POSITIONING + CLAIM_REGISTER + CAPABILITY_MATRIX + LIMITATIONS` (V1 honest claim gate).
- `docs/wireframes/*.html` — Control/Environment/Timeline/Live/Evidence (taste DO NOTs respected).
- `Favorable errors/*.csv/.md` ×8 — forensic audit artefacts (untracked, evidence only).

**Tests:**
- `108 passed, 2 warnings` on HEAD (`pytest -q` in Staging — verified this handoff). Warnings are Pydantic `protected_namespaces` for `model_matrix`/`model_version` (cosmetic, not blocking). Before boundary: 96 → after boundary audit 104 → after schedule→live rooms 108. Includes `test_harness_boundary.py` (12), `test_jail_canonical.py`, `test_manifest_canonical.py`, `test_matrix_seals.py` (3 cells now generate), `test_schedule_v11` … `test_live_v17`, `test_seal_gate`, `test_gateway`, etc. `smoke.sh 5/5 OK`.

**Sealed evidence:**
- `docs/evidence/_HARNESS_ECA_GATED_2026-09-24/` — 6-file seal `SCENARIO.json + scenario.csv + DECISION_SUMMARY.json + MANIFEST.json + ECA_GATED_RESULTS.json + verify_result.json` (`ai_computed_metrics:false`, `orphans:[]`, `sealed:true`, `B.prev=A` chain, `scenario:future-synthetic` + FCA disclaimer). Canonical experiment observed (not built by Harness): 62-claim `GR-PARA-03 (40) + DRIFT-03 (10) + PLUG-CHAT (12)` + `AGENT-01 (4)` → RAW `42/66` correct → GATED `62/66` via ECA `|R|≤3 && ΔH>0.5` — mirrored to `outputs/_HARNESS_ECA_GATED_2026-09-24` + `proof/L9_LIVE_TRANSCRIPT.md`. Harness observed gate, did not become ECA.

---

## Hashes & single contract (pinned)

**Single hash contract:** `WTF-005A-HASH-v3` via `axiom_harness/manifest.py:15` — `sort_keys True ensure_ascii False separators (",",":")` no indent `UTF-8 SHA-256(canonical_messages_bytes)` — card·request·receipt·verifier·audit all use one function. Never `sort_keys true` with indent 2 (broke canonical). Never `orjson` drift.

**Upstream registry (MATH_MODULAR_MAP.md — actual hashes at HEAD):**

| Project | Canonical file | Implementation hash (full sha256) | Config hash | Version | Status |
|---|---|---|---|---|---|
| Evidence Axiom | `docs/gap-review/harness/living_gap_review_score.py` | `60c94d95173a34ab…` (16 shown) | `evidence_layer_freeze_retrieval_v1` scorer `0.1.0` | 0.1.0 | UPSTREAM-BLOCKED — not Harness-certified |
| PER | `PER-Core/sim/telescope.py` | `7ae692a5cfbe5fcf…` | UNKNOWN (weights in code `HYPOTHESIS_WEIGHTS`) | UNKNOWN | UPSTREAM-BLOCKED |
| **ECA CURRENT CANONICAL** | `ECA/plugin/` (all `plugin/**/*.py` cat\|sha256) | `e3c508b2695f38425f4dc0cfdcb545e66ae62d8dcfc7df80f27c621aae20c719` (e.g. `__init__.py 97c6be8c…`) | `1be70761bcdc55d644e99fc15a47d97b449e94f58e25e180351528de392675c3` `ECA/plugin/config/eca.v1.json` `eca-v1.0.0-20230901` | `eca-v1.0.0` / plugin `1.0.0` `model claude-sonnet-4-5-20250929` | **UPSTREAM-BLOCKED / NOT CERTIFIED** — Harness records hash only, does not certify |
| ECA HISTORICAL / BLOCKED | `ECA/sim/telescope.py` | `bf7329c836d8b8208bb06b2e132c9c4fd6315aee2669b09b697b92a3ccf1a508` | — | `L0→L4 GateOk` | HISTORICAL / BLOCKED |
| Future Workbench | `axiom_wb/pipeline.py` | `e8fbd398675f7112…` | `seal_pair B.prev=A` via `manifest.py:20` | UNKNOWN | UPSTREAM-BLOCKED read-only |

Harness **does not certify** any upstream — boundary is `Harness owns LOAD/CONFIGURE/FREEZE/RUN/RECORD/SEAL only, does not calculate GateOk/ΔH/T_max, not certify upstream`. Verified `rg GateOk axiom_harness/*.py → 0 hits` (registry doc string only, not impl). Competing Harness-created `ECA/plugin/eca_config.json` was deleted `rm` 2026-09-24 — ECA owns its own canonical `config/eca.v1.json`.

**Harness orchestration hashes:** `ScheduleConfig` + `ParallelConfig` + `DataConfig` + `LanguageConfig` + `AudioConfig` + `SensorConfig` + `LiveConfig` all `frozen=True` → hashed via `MasterMission.protocol` `WTF-005A-HASH-v3`. Correctly `HARNESS-OWNED` in map. No `ECA maths/PER maths/Evidence Axiom maths` reproduced as Harness logic.

---

## What remains (ordered, do not reorder without Carl)

**On HOLD before V1.8:** `FREEZE_V3_2026-09-24_ON_HOLD.md` — awaiting full skill audit before un-holding. Do not begin V1.8 Multi-agent until audit gaps closed.

**V1.8 Multi-agent (next):** `Agent A Analyst B Critic C Maker D Observer E Adversary`, isolated contexts, `GET /master/multi-agent` style — one Pydantic frozen contract `MultiAgentConfig` + one `app/` room + one endpoint + three durable tests. Zero-bloat: declare in types, ship runtime only when V1.8 demo pack runs.

**V1.9 Video Timeline → V2 Films (Experiment→Story) → V2+ Continuous Observatory (alerts) → Future External API Platform** — each `one contract + one room + one GET + three tests` on same `EXPERIMENT` object (§55) — `Add a room without breaking laboratory`.

**V3 Human Axiom (phased, after V2):** `V3.0 foundation (no AI, 8D receipt RESULT+EVIDENCE+METHOD+COMPARISON+STABILITY+VERSION+SIGNATURE, tables persons/instruments/responses, lib/seal.js)` → `V3.1 Human vs Scripted S0→S1` → `V3.2 Human vs Live AI (same LIVE WORLD FEED §31, comparative HUMAN vs MODEL A/B/C)` → `V3.3 Human alone` → `V3.4 Human-AI team` (Person×Role×Environment). Each one `GET /master/human/{id}/trail`.

**Remaining risks / gaps (from 8-skill audit + boundary):**
- Pydantic `protected_namespaces` warning for `model_matrix/model_version` — set `model_config={"protected_namespaces":()}` to silence.
- Inner dict mutability `m.per_eca_state["per"]="ON"` possible (outer `frozen` only) — mitigated by never mutating post-seal + hash captures state + linter `rg 'per_eca_state\['` — future: typed `PerEcaState(BaseModel frozen=True)`.
- `ALLOWED_SCRIPT_PREFIXES ["scripts/factory_","AXIOM_"]` broad — narrow to explicit `["axiom_wb","scripts.factory_"]` + file existence check before allowlist.
- `LiveConfig` + `ParallelConfig.isolated` are config-true, runtime-hallucinated until adapters actually spawn `OUTPUTS/<id>/sandbox-<n>` per `parallel_count` and wire live feed timestamp source. Do not demo 64 as live until queue + backpressure exists.
- Brief duplicate `(1)==(2)` — now logged as `docs/briefs/BRIEF_DUPLICATE_LOG.md`, but any new agent must still `diff` + `sha256sum` both briefs before building.
- Provider deprecation `deepseek-v4-flash-0731 → 410 EOL` — need dynamic fallback routing (not yet).
- `£120k vs 120,000` paraphrase not allowlisted — `60 ↔ sixty` works but other numeric synonyms may false-refuse.
- Video heavy deps `FFmpeg/TTS` — plan is containerize + lazy-load (Docker), not shipped.
- Until `seal_pair + RECEIPT_INDEX/Telescope/ΔH + GateOk` wired, Phase 0 `Corpus ON / PER OFF / ECA OFF` only — live `ReceiptIndex` not yet ( `MATRIX_BLOCKED_UNTIL_SWITCH_WIRED` correct).

**GATE 5 findings were `FINDINGS_RESOLVED PARTIAL not PASS`** in raw audit — now tightened to `PASS` at `70b8cf1` but audit `G1 G7 G8` remain as documented residual debt above (call out honestly, don't hide).

---

## How to pick up (next agent — exact commands, exact files)

**0. Do not edit Master.** `Axiom Harness-Master - Dont Touch/` is witness. All work in `Axiom Harness-Master - Dont Touch/Staging/`. `STAGING_ROOT` must be under `.../Axiom Harness-Master - Dont Touch/Staging`.

**1. Verify HEAD:**
```
cd "Documents/Axiom Harness-Master - Dont Touch/Staging"
git log --oneline -5   # expect b2fca7e HEAD, 70b8cf1, ef3573e, 01c99af, 307bf6f
git status             # expect ahead 13, untracked Favorable errors/* + docs/BRIEF_REVOLUTIONARY_V3_SYNTHESIZED.md
python3 -m pytest -q   # expect 108 passed, 2 warnings (pydantic protected_namespaces)
bash smoke.sh          # expect SMOKE:0 5/5
sha256sum "Axiom Harness-Master - Dont Touch/AXIOM HARNESS Brief (1).md" "Axiom Harness-Master - Dont Touch/AXIOM HARNESS Brief (2).md" | cut -c1-16
# expect 0a0d0502 identical, diff 0
cat Axiom\ Evidence\ Layer/ECA/plugin/__init__.py | sha256sum  # 97c6be8c…
cat Axiom\ Evidence\ Layer/ECA/plugin/config/eca.v1.json | sha256sum  # 1be70761…
find Axiom\ Evidence\ Layer/ECA/plugin -name "*.py" -exec cat {} \; | sha256sum  # e3c508b2…
sha256sum "Axiom Evidence Layer/ECA/sim/telescope.py"  # bf7329c8…
```

**2. Read in order (every file is the authority, not this handoff):**
1) `docs/HANDOFF_2026-09-24_FULL_ACCOUNT.md` (this file) — pickup only
2) `docs/MATH_MODULAR_MAP.md` — upstream registry (hashes) — **REGISTRY ONLY**
3) `docs/HARNESS_BOUNDARY_AUDIT_2026-09-24.md` — what Harness owns vs does not
4) `docs/HARNESS_V1_FINAL_ACCEPTANCE_2026-09-24.md` — reproducible PASS (authoritative over `HARNESS_V1_VERIFICATION` which is pre-repair FAIL)
5) `docs/FREEZE_V3_2026-09-24_ON_HOLD.md` — ON HOLD stamp (do not un-hold without audit closure)
6) `docs/BRIEF_REVOLUTIONARY_V3_SYNTHESIZED.md` + `docs/BRIEF_REVOLUTIONARY_V2_PATCH_IS_ONE_ROOM.md` — game-changer framing (Patch is one room)
7) `docs/ARCHITECTURE.md` + `docs/TECH_SPEC.md` + `docs/DB_SCHEMA.md` + `docs/API_SPEC.md` — V1 paper contracts
8) `docs/PLAN_V1.md` + `docs/STAGING_DECISIONS.md` — decisions 1→9
9) `docs/commercial/COMMERCIAL_ONE_PAGER_V1.md` — V1 honest claim gate (no hard-coded WTF/PER/ECA in public surface)
10) `docs/audits/*.md` + `docs/AUDIT_MASTER_GAPS_HALLUCINATIONS.md` — 8-skill rip-apart gaps
11) `Axiom Harness-Master - Dont Touch/WORKING.md` — Master changelog (append-only)

**3. Before any code change:** `rg GateOk axiom_harness/ → 0`, `rg T_max axiom_harness/ → 0`, `rg HYPOTHESIS_WEIGHTS axiom_harness/ → 0` — if any hit outside `registry.py` doc string, stop (boundary violation).

**4. To continue:** implement `V1.8 Multi-agent` as one frozen `MultiAgentConfig` on `MasterMission` + one `api` endpoint `POST /master/multi-agent` (`201/422`) + three durable tests `tests/test_multi_agent_v18.py` — keep `per_eca OFF` until live `ReceiptIndex.search/entropy + ΔH>0.5 + GateOk` wiring lifts `MATRIX_BLOCKED`. Do not push to `origin/main` until Carl says `push live` / `go push` — `local until push` is locked. Every gate separate commit, never amend.

**5. Budget rule:** one task → one pass → QA table → STOP. Ask before second pass or marketing rewrite. Labs marketing `boonmind.io` stays LOCKED unless Carl names word-for-word bug.

---

## Evidence ladder & invariants (never break)

- BML Quad: `Pre-declared Rules → Frozen Evaluator → Deterministic Engine → Honest Hashed Verdict`
- Four locks: Execution Boundary + Computation Boundary (`ai_computed_metrics:false` everywhere, deterministic `axiom_wb` only — Boon AI never runs math) + Deterministic Evaluation + Provenance/Integrity (`sha256sum -c MANIFEST`, `orphans:[]`, `B.prev=A` chain)
- Harness owns `LOAD/CONFIGURE/FREEZE/RUN/RECORD/SEAL` only — never `GateOk/ΔH/T_max/ε/max_candidates` — does not certify upstream
- Single hash `WTF-005A-HASH-v3` `sort_keys True ensure_ascii False (",",":")` no indent — one function `axiom_harness/manifest.py:15`
- Generic code names `experimental_programme/retrieval_telescope/earned_context_gate` — never hard-code `WTF/PER/ECA` in routes/packs/heroes until brand lock
- Generic code names `experimental_programme/retrieval_telescope/earned_context_gate` — never hard-code `WTF/PER/ECA` in routes/packs/heroes until brand lock
- Every `422` is `failed_policy` event with `provider_call_count=0`, stored as evidence — never suppressed
- Lifecycle `ARMED→STARTED→RUNNING→PAUSED→RESUMED→STOPPING→SEALED→COMPLETE` is evidence — self-stopping watchers

---

## File map (absolute — Staging git root)

```
Axiom Harness-Master - Dont Touch/Staging/
  axiom_harness/
    mission.py          # frozen contracts (7 rooms + MasterMission)
    paths.py            # STAGING_ROOT + is_safe_relative + jail
    manifest.py         # WTF-005A-HASH-v3 + write_manifest + write_run_pointer
    watcher.py          # lifecycle ARMED→COMPLETE
    registry.py         # 7-door table (doc strings not authority)
    adapters/
      workbench.py      # jailed subprocess, explicit file set, hallmark
      per_eca.py        # ensure_off RED gate, transport only
  api/main.py           # 7 endpoints 201/422 + health honest
  missions/master_demo_wtf001.yaml
  outputs/
    18cell/WTF-005A-RUN-01..18/  # generated deterministically if missing
    _HARNESS_ECA_GATED_2026-09-24/ # 6-file seal mirror
  docs/
    HANDOFF_2026-09-24_FULL_ACCOUNT.md  # ← you are here
    MATH_MODULAR_MAP.md                 # ↑ read second
    HARNESS_BOUNDARY_AUDIT_2026-09-24.md
    HARNESS_V1_FINAL_ACCEPTANCE_2026-09-24.md  # authoritative PASS
    HARNESS_V1_VERIFICATION_2026-09-24.md      # pre-repair FAIL (historical)
    FREEZE_V3_2026-09-24_ON_HOLD.md
    BRIEF_REVOLUTIONARY_V2_PATCH_IS_ONE_ROOM.md
    BRIEF_REVOLUTIONARY_V3_SYNTHESIZED.md (untracked)
    ARCHITECTURE.md / TECH_SPEC.md / DB_SCHEMA.md / API_SPEC.md
    PLAN_V1.md / STAGING_DECISIONS.md / PROJECT_PROFILE.md
    EXPLAINER_MASTER_SUMMARY.md / FULL_BUILD_STATUS_GAPS_2026-09-24.md
    audits/architecture.md … + AUDIT_MASTER_GAPS_HALLUCINATIONS.md
    commercial/BUYER_STORY_V1.md … + evidence/_HARNESS_ECA_GATED_2026-09-24/
    wireframes/control.html environment.html timeline.html live.html evidence.html
  tests/
    test_harness_boundary.py (12) + test_jail_canonical.py + test_manifest_canonical.py
    test_matrix_seals.py (3 cells) + test_schedule_v11 … test_live_v17 (7×3)
    test_seal_gate.py + test_gateway.py + …
  Axiom Evidence Layer/ECA/plugin/  # upstream, NOT Harness — read-only
    __init__.py  97c6be8c…  | config.py  | provider/anthropic.py | receipt.py
    config/eca.v1.json  1be70761…  eca-v1.0.0-20230901  claude-sonnet-4-5-20250929
  Axiom Evidence Layer/ECA/sim/telescope.py  bf7329c8…  # HISTORICAL / BLOCKED
  PER-Core/sim/telescope.py                  # UPSTREAM-BLOCKED
  Axiom-Workbench/axiom_wb/pipeline.py       # UPSTREAM read-only
```

Master witness `Axiom Harness-Master - Dont Touch/` is not inside this git — it is the parent folder on disk (`WORKING.md` + `MEMORY.md` + `AXIOM HARNESS Brief (1+2).md`). `git status` in Staging never shows it (outside git). Verify Master separately: `ls "Axiom Harness-Master - Dont Touch"/WORKING.md && sha256sum "Axiom Harness-Master - Dont Touch"/"AXIOM HARNESS Brief (1).md"`.

---

## STOP

This handoff is the full account. Next agent: run the verification in §How to pick up, read the 11 files in order, then implement `V1.8 Multi-agent` exactly as `one frozen contract + one room + one endpoint + three tests` — or ask Carl before deviating. Do not push, do not touch Master, do not reimplement Workbench/ECA/PER maths.

*Generated 2026-09-24 from Staging HEAD b2fca7e — 108 passed, 2 warnings, smoke 5/5, ahead 13, local only.*
