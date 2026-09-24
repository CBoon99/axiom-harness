# AXIOM HARNESS — FULL BUILD STATUS, HOW, WHERE WE ARE, WHAT'S LEFT, GAPS

**Date:** 2026-09-24 — **Status:** ON HOLD — **Staging:** `Axiom Harness-Master - Dont Touch/Staging/` (git `axiom-harness` 5c2c234, 96 tests + smoke 5/5) — **Master:** `Axiom Harness-Master - Dont Touch/` FROZEN 2026-09-24 05:39 — **Briefs:** (1)&(2) 3172 lines identical (now logged as duplicate) — **Revolutionary brief V2:** `BRIEF_REVOLUTIONARY_V2_PATCH_IS_ONE_ROOM.md` (Patch is ONE room V1.8, not product)

---

## 1. WHAT WE ARE BUILDING — FULL DETAIL

Not a harness. A **sealed 4D laboratory** where AI is inside, observed over time, converted to sealed evidence. This is not how people test AI. Ever.

**One-liner:** Humans configure the laboratory. The Harness records the laboratory. The evidence layer seals the laboratory. AI lives inside it. Golden rule: **AI DOES NOT CONTROL THE LABORATORY** — proposal → human approves → Harness executes → recorded, no silent mutation.

**Stack (locked, §74):**
`HUMAN → HARNESS-CONTROL → CONFIG (sealed hash WTF-001/RUNSET-0047) → SEALED ENV → BOON AI/other models → SANDBOX/TERMINAL/TOOLS/DATA/SENSORS → EVENT+TRANSCRIPT+STATE → EVIDENCE LAYER → ANALYSIS → REPORT/REVIEW/EXPORT`

**Four locks:** Execution Boundary (AI cannot control Workbench), Computation Boundary (deterministic `axiom_wb` only), Deterministic Eval Boundary (fixed), Provenance Boundary (`B.prev=A` chain + `orphans:[] ai_computed_metrics:false` + `WTF-005A-HASH-v3` `sort_keys True ensure_ascii False (",",":")` no indent).

**Philosophy:** Keep laboratory boring (bounded, recorded, versioned, sealed, reproducible, modular, auditable, fail-closed) — make experiments interesting (psychology, physics, sci-fi, quantum — same AI tested language drift Monday / memory Tuesday / patch Wednesday / bias Thursday with same seal/chain).

**Core paradigm 7 shifts (§1):** #AI-Inside-The-Experiment, #AI-Does-Not-Control-The-Laboratory, #AI-Proposes-Harness-Disposes, #Keep-Lab-Boring-Make-Experiments-Interesting, #No-Layer-Silently-Rewrites-Another, #Unpredictability-Allowed-Unobserved-Authority-Not, #Don't-Make-AI-Behave-Like-Subject / #Make-Boundary-Real-Then-Watch

**How (modular rooms — Add-A-Room-Without-Breaking-Lab, HYGIENE §2A zero-bloat):**
- **V1 base (prove architecture):** Control + Secret Manager (`API KEY ••••` capability not secret) + Sandbox (terminal substrate — runtime contract, not visual) + Run (One/Sequence/All/Parallel/Pause-Resume/Restart/Schedule/Continuous) + Live Room + Timeline (scrubbable `◆/╱╲` + synchronised replay) + Evidence (5-file seal `SCENARIO.json/scenario.csv/DECISION_SUMMARY/MANIFEST/verify_result`, chain `B.prev=A`) + Analysis + Export (Complete Report Pack 22-file: 8 docs + receipt + 3 plot families).
- **V1.1 Scheduling (§15):** Once/repeated/intervals/fixed/continuous/until/end-date — overnight, 24h, week-long, recurring, background. `ScheduleKind {ONCE,INTERVAL,REPEATING,CONTINUOUS,UNTIL,CRON}` + `ScheduleConfig frozen` + `POST /api/master/schedule 201/422`.
- **V1.2 Parallel (§14+§62):** Model Matrix, `ParallelMode {ONE,SEQUENCE,ALL,PARALLEL}`, `parallel_count 1..64` isolated sandboxes, `model_matrix [A-D]` each timeline. `POST /api/master/parallel`.
- **V1.3 Data Room (§29):** CSV/JSON/text/docs/dataset/images/audio/video, `dataset_refs` jail-checked `is_safe_relative`, AI proposes → Harness executes only approved, every transform recorded. `POST /api/master/data`.
- **V1.4 Multilingual (§20-22):** Language as variable, `LanguageCode {EN,ID,ES,FR,DE,ZH,JA,AR,HI,PT}`, `variants` parallel runs same model/experiment different language, `keep_params_constant`, `detect_switch`. `POST /api/master/language`.
- **V1.5 Speech/Audio (§18-19):** TTS/STT/uploaded/live/model/human voice, `multi_speaker`, `timestamps`, `transcript_linked` (WCAG 1.2 captions gate), DAW-like `trim/split/mute/annotate`. `POST /api/master/audio`.
- **V1.6 Sensors (§28):** `PHYSICAL/ENVIRONMENTAL/DIGITAL/AI/HUMAN/IOT`, `identities/policy/ALWAYS|ON_EVENT|MANUAL/schema`. `POST /api/master/sensors`.
- **V1.7 Live feeds+Observatory (§30-32):** `NEWS/MARKET/WEATHER/WEB/CUSTOM/SIMULATED`, `observatory isolated compare`, same stream to A/B/C. `POST /api/master/live`. Glass window §33.
- **V1.8 Multi-agent (§35)** next, **V1.9 Video Timeline**, **V2 Films** (`Experiment→Story` render, video is presentation not proof), **V2+ Continuous Observatory** (alerts), **Future External API Platform** (UI→API→Harness→Environment).
- **V1.8 Patch Illusion Room (ONE of 15, not product):** Visual Perception — `1024×1024→224×224→14×14→768-dim→576 tokens→8 words (393,216:1, 99.99% gone)` compression receipt, `What-Did-You-Miss` (`Describe → missed → cannot-determine`), `Mona Lisa`, `Embodiment Divide` (human vs VLM same timeline), `Bias Laundering` (base→filter→HR rewrite), `Cultural Translation`, `LLM vs VLM vs LVM` matrix — family WTF-VIS-001…014. Lock 5 Compression Boundary. Revolutionary but one room.
- **V3 Human Axiom (future):** Same rooms, `participant HUMAN/SCRIPTED/TEAM`, `GET /master/human/{id}/trail` — 8D receipt, tables `persons/instruments/responses`.
- **Evidence:** `EXPERIMENT` first-class object (Identity/Protocol/Config/Model/Env/Permissions/Data/Sensors/Timeline/Transcript/Audio/Video/Events/Evidence/Analysis/Reviews/Reports/Renders). Versioning, collaboration, review QUESTION→RESOLUTION, sharing layers. Watchers (11 types) observe not interpret, `attempt→boundary→result`, `Failed-Policy-Events-Are-Data`, `If-Rule-Matters-Enforce-It`, lifecycle `ARMED→COMPLETE`.

**Commercial bigger vision (internal till finish):** AI Behavioural Audit, Sequential Intelligence Testing, Long-Horizon Agent Testing, Multilingual Benchmark, Red Teaming, Incident Reconstruction, Live Observatory — Controlled lab → reproducible env → sealed evidence. Not selling till full lab with AI inside but unable to run code/maths, per/eca/evidence axiom maths locked.

---

## 2. HOW WE BUILD (METHOD + LOCKS)

**BML Quad:** Pre-declared Rules → Frozen Evaluator (`axiom_wb` EMA span20/SMA20/median11/lowpass α0.1, `verify.py` orphan check) → Deterministic Engine (`AXIOM_ENGINE_ROOT` read-only, `outputs/{id}/inbox` only, no `..` shell) → Honest Hashed Verdict (`ledger>narrative`, `ai_computed_metrics:false` at 3 points).

**Locks:** `STAGING_ROOT=Path(__file__).resolve().parents[1]` + assert `Axiom Harness-Master - Dont Touch/Staging`, iterative `unquote` while-loop depth 10 + `resolve().relative_to` jail (handles `%2525252e` x5+), anchored `allowlist ["scripts/factory_","AXIOM_"]` on `cmd[2]` only, single hash `WTF-005A-HASH-v3`, generic code names `experimental_programme/retrieval_telescope/earned_context_gate`, ledger>narrative, frozen `Pydantic frozen=True` → new `id` not patch.

**Build tracked:** `Master WORKING.md` (append-only changelog) + `STAGING_DECISIONS.md` (8 rows) + `MASTER-PER-ECA-COMMERCIAL` + BML-CODE-HYGIENE zero-bloat (type exists, runtime only when V1.8 demo pack runs).

---

## 3. WHERE WE ARE (DONE, FROZEN)

- **Master** frozen 05:39, **Staging** `5c2c234` `axiom-harness` main, `96 passed` (`74→77→81→84→87→90→93→96` as V1.1-1.7 added) + `smoke.sh 5/5` (jail/health/seal/pressure/manifest).
- **Docs:** `BRIEF_REVOLUTIONARY_V2` drafted (8614 bytes) capturing 100+ tags (#AI-Inside, #Timeline-As-4D-Object, #Boundary-As-Data, #Watchers-Observe-Not-Interpret, #Terminal-As-Substrate, #Counterfactual-Branching, #Live-Observatory, #Language-As-Variable, #Speech-As-Data, etc.) — **not yet promoted to README/PROFILE hero** (still boring-harness pitch). Memory has `axiom/full-inventory` + `axiom/revolutionary-brief-v2`.
- **Evidence Layer experiment (Harness-observed, not Harness-built):** 62-claim `GR-PARA-03 (40) + DRIFT-03 (10) + PLUG-CHAT (12)` + `AGENT-01 (4)` sealed (`WTF-005A/B` 18/18 earlier), `3WAY_ECA_GATED_2026-09-24` live `meta/llama-3.2-11b` via NVIDIA: **RAW 42/66 correct → GATED 62/66 (20 hallucinated Supported blocked via `|R|≤3 && ΔH>0.5`)**, `axiom 66/66`, `4 MODEL_EXECUTION_BLOCKED` transient API — sealed to `Axiom Evidence Layer/...` + mirrored `Staging/outputs/_HARNESS_ECA_GATED_2026-09-24` + `proof/L9_LIVE_TRANSCRIPT.md`. Harness observed gate, did not become ECA.
- **Audits:** Old-school bench review 26.6KB **8/10** would pass walk-through after P0; agent pre-lock workflow (163s+522s) found **no maths hard-locked wrong**, all thresholds tweakable via payload/constructor.
- **Contrast:** Text **PASS** 4.5:1 (`muted #5c5348 on paper 7.00:1`, `accent 10.69:1`), non-text `line #e0d4c4 1.36:1` decorative border **FAIL** but exempt (card identified by fill/shadow).
- **ECA plugin scaffold:** `ECA/plugin/` started (`__init__.py`, `config.py`, `provider/anthropic.py`, `receipt.py`, `eca_config.json`) — **other chat's product**, Harness only `LOAD` boundary (currently `OFF/OFF`).
- **Harness V1.1-1.7 APIs:** `POST /api/master/schedule/parallel/data/language/audio/sensors/live` each `201/422` validated, `missions/master_demo_wtf001.yaml` + `api/health` honest `engine_present`.
- **Duplicate brief:** Both `(1)&(2)` 3172 lines identical `sha256` — now to be logged, not yet done.

---

## 4. WHAT'S LEFT (TO FINISH INTERNAL LAB)

**P0 must-fix before seal (old-school P0):** Deep-freeze nested dicts (`mission.py:85` inner `per_eca_state` dict mutable), explicit file set not `glob("*")` for seal, signature `sealed_by/at/instrument/sop_version` on every seal, remove `*_noop` stubs (`future.py`, `per_eca.py`).

**Docs finish (WP1):** Promote `BRIEF_REVOLUTIONARY_V2` to `Staging/README.md:10-19` hero + `PROJECT_PROFILE.md:7-8` tagline + append `Master WORKING.md §4` with Patch-is-one-room correction — currently still boring pitch.

**Math modular map (WP2):** Grep literals `3,75,4,0.5,64` → `docs/MATH_MODULAR_MAP.md` table 7 adapters (Evidence Axiom, Future `seal_pair B.prev=A`, PER `IG=log2(Nb/Na)`, ECA `L0-L4 GateOk`, EvoCycles, Testing, Epistemic) + single hash contract `protocol/hash_contract.py` — verify no literal outside config.

**Boundary tests (WP3):** Add `test_harness_does_not_reimplement_axiom.py` + `test_math_modular.py` → ≥98 passed, keep `adapters/per_eca.py ensure_off()` V1 RED.

**Duplicate + freeze (WP4):** `docs/briefs/BRIEF_DUPLICATE_LOG.md` + `STAGING_DECISIONS.md` row 9 + `docs/FREEZE_V3_2026-09-24_ON_HOLD.md` with `impl_hash/cfg_hash/corpus/claims/B.prev=A`.

**Remaining rooms (V1.8→V2+, not yet built):** V1.8 Multi-agent (`Agent A Analyst B Critic C Maker D Observer E Adversary`, isolated contexts), V1.9 Video Timeline, V2 Films (`Experiment→Timeline→Render Plugin→Video`, video is presentation not proof), V2+ Continuous Observatory (alerts: position/language/contradiction/confidence), Future External API. Each `one Pydantic frozen contract + one app/ room + one GET /master/... + three durable tests`.

**EvoCycles / Epistemic / Future Workbench integration:** `World-A-EvoCycles` harness_ ids + `B-0 physics`, `Epistemic-UX EU-01…06 6A loop`, `Future Workbench` provenance — need explicit adapters (like `Axiom-Workbench`) with hash pins, not yet wired beyond read-only reference.

**Evidence sealing:** Promote `Staging/outputs` → `docs/evidence/` properly (currently gitignored), wire `sealer.py` signature, run first `Complete-Report-Pack 22-file` with `WTF-001` via Harness UI → sandbox → Workbench → `DECISION_SUMMARY + verify_result orphans:[]`.

**Stamp:** `ON HOLD — awaiting full skill audit` hallmark, then hand to audit.

---

## 5. WHAT WE DON'T KNOW — GAPS, HALLUCINATIONS, RISKS

**Unknowns:**
- Patch Illusion full `LLM vs VLM vs LVM` matrix needs real LVM (doesn't exist at scale) — hypothetical until available.
- `£120k vs 120,000` style paraphrase (`60 ↔ sixty` works) — other numeric synonym ` £120k` not yet allowlisted, may false-refuse.
- Live provider deprecation (BoonAI OBSERVED `deepseek-v4-flash-0731` → `410 EOL` 2026-09-21) — need dynamic fallback routing, not yet.
- Multi-agent comparative timelines have 100s grid virtual scroll but not load-tested at 10k trials (`1MB per experiment` → delta encoding + Glacier planned, not yet).
- Video rendering heavy deps `FFmpeg/TTS` — containerize + lazy-load planned, not shipped.
- Until `seal_pair` + `RECEIPT_INDEX/Telescope/ΔH` gates wired, Phase 0 `Corpus ON/PER OFF/ECA OFF` only — live ReceiptIndex not yet.

**Gaps (audit synthesis):**
- `mission.py:85` dict mutability (P0) — outer `frozen` but inner dict still `m.per_eca_state["per"]="ON"` possible — needs `MappingProxy` / nested frozen model.
- Seal file set `glob("*")` — should be explicit `["SCENARIO.json","scenario.csv","DECISION_SUMMARY.json"]` + engine-declared, else `PER_ECA_SKIPPED.json` could weigh in manifest.
- No `sealed_by/at/instrument/sop_version` — auditor asks who/when first.
- ECA `HYPOTHESIS_WEIGHTS {1:0.1..6:60}` `desc_candidates 3 weight 75 entropy 4` hard-coded defaults — tweakable via constructor but not yet surfaced as Harness `ECA_CONFIG_HASH` (other chat will do, Harness must not duplicate).

**Hallucinations risk:**
- Evidence Layer scorer `living_gap_review_score.py:SCORER_VERSION 0.1.0` vs `0.1.1` — version string vs content hash drift; must surface `implementation_hash` not just string.
- Brief duplicate not flagged early — would have scaffolded off wrong brief if they diverged.
- `ai_computed_metrics: false` currently enforced at 3 points — need linter to fail build if LLM numbers leak.

**Risks:** Over-configuring breaks reproducibility → mitigated by `frozen=True` + new `id`; mixing ECA rebuild into Harness → mitigated by boundary `LOAD ECA` only; hero too hypey dilutes mechanics → keep `Keep-Lab-Boring` as engineering mantra, wow as experiment list.

---

## 6. NEXT TO GET ON TRACK AND FINISH

1. **Today (this commit):** Docs hero (README/PROFILE/WORKING) + `BRIEF_DUPLICATE_LOG.md` + `MATH_MODULAR_MAP.md` + fix P0 dict freeze.
2. **Tomorrow:** `FREEZE_V3_ON_HOLD.md` stamp + `test_harness_does_not_reimplement_axiom + test_math_modular` → 98 passed + `sha256sum -c`.
3. **Then:** One workflow 8 agents (architecture, testers, color-contrast/taste, captions, brand, research-evidence, EvoCycles-Epistemic, math-hardcode) each `docs/audits/<skill>.md` + master `docs/AUDIT_MASTER_GAPS_HALLUCINATIONS.md` — rip apart, produce gaps/hallucinations.
4. **After audit:** V1.8 Multi-agent → V1.9 Video → seal first `Complete-Report-Pack` 22-file + V3.0 8D receipt slots. No sell till `push live` you approve.

*End — append next session below, never overwrite.*
