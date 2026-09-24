# Axiom Harness — PLAN V1 (Rooms + Contracts)

## Goal

Build **V1 of AXIOM Harness** exactly as your two 3,172-line briefs define it — no more, no less — so the laboratory can be proven before a single voice, video render, or extra sensor is added.

> **Humans configure the laboratory. AI operates inside the laboratory. The Harness records the laboratory. The evidence layer seals the laboratory.** And: **AI DOES NOT CONTROL THE LABORATORY.**

V1 proves the architecture with the smallest honest rooms. Every post-V1 capability (scheduling, parallel, data, multilingual, speech, sensors, live feeds, multi-agent, video, observatory, external API) then plugs in as a room without breaking the laboratory.

**Names will change:** `WTF Laboratory / WTF test family`, `PER`, `ECA` are *provisional programme/mechanism labels* (you confirmed). This plan treats them as `experimental_programme`, `retrieval_telescope`, `earned_context_gate` in code/routes/pack names and will push back before writing any to a public surface.

## Success Criteria

- **V1 outcome:** From the **Control Room** a human can configure (model + context + env + info source + params + secret + sensors), **Seal** (canonical config → hash → immutable identity `WTF-001 / RUNSET-0047`), **Run** (One / Sequence / All / Parallel / Start-Stop / Pause-Resume / Restart + Schedule / Continuous stubs), watch in the **Environment Room + Live Room**, scrub the **Timeline** (TIME → MODEL + PROMPTS + EVENTS ◆ + SENSORS ╱╲), **replay** any point (exact prompt/response/model/timestamp/context/tools/state/sensor), and open a **sealed Analysis + Evidence + Export** pack where **raw evidence remains untouched** (video is presentation, not proof). Evidence is the Workbench receipt family: hashes, provenance, metrics where applicable — `ai_computed_metrics:false` enforced, no silent mutation.
- **Modular contract proven:** Adding a V1.1 room (e.g. Data Room) requires no breaking change to V1 rooms — verified by the fact V1 tests stay green after the V1.1 branch.
- **Zero bloat:** No speculative runtime ships — extensibility is declared in types/schemas only (BML-CODE-HYGIENE-V1.2 §2A), implemented only when exercised.
- **Master untouched:** `Axiom Harness Master/` stays frozen at 2026-09-24 05:39 until you approve a promotion; all P0-P5 work lands in `Axiom-Harness-Staging/` and private `/tmp/axiom-*-private-notes.md` (existing 119+123+123 lines) — not inside Master.

## Context And Current Facts

**Briefs (inside Master, read-only, verified this session):**
- `Axiom Harness Master/AXIOM HARNESS Brief (1).md` 3,172 lines + `Brief (2).md` identical (`diff 0`) + `Docs/Copy … LVM addition not master` identical — one spec, 79 sections (§1 Core Idea → §79 Harness as laboratory).
- Stack (§2): `HUMAN → HARNESS-CONTROL → EXPERIMENT CONFIG → SEALED ENV → BOON AI/other models → SANDBOX/TERMINAL/TOOLS/DATA/SENSORS → EVENT+TRANSCRIPT+STATE → EVIDENCE LAYER → ANALYSIS → REPORT/REVIEW/EXPORT`
- Four-layer principle (§3): Control → Experimental Environment → Observation → Evidence/Analysis. Golden Rule §4: AI may propose, never silently alter sealed config/scoring/evidence/permissions.
- V1 rooms (§75): `CONTROL, MODEL (secure connection), SANDBOX (terminal substrate), RUN (start/stop etc.), LIVE ROOM, TIMELINE, EVIDENCE (seal), ANALYSIS (inspect/annotate), EXPORT` — enough to prove architecture.
- V1.1→V2+ rooms (§76): V1.1 Scheduling → V1.2 Parallel → V1.3 Data Room → V1.4 Multilingual → V1.5 Speech/Audio → V1.6 Sensor plugins → V1.7 Live feeds → V1.8 Multi-agent → V1.9 Video timeline → V2 Films (Experiment→Story) → V2+ Continuous observatory (alerts) → Future External API Platform. **V3 Human Axiom (you asked, read-only Human Workbench + Axiom You inspiration, modular): V3.0 foundation (no AI, 8D receipt `RESULT+EVIDENCE+METHOD+COMPARISON+STABILITY+VERSION+SIGNATURE`, tables `persons/instruments/responses` + `lib/seal.js`) → V3.1 Human vs Scripted (S0→S1 replay, no live model) → V3.2 Human vs Live AI (HUMAN vs MODEL A/B/C on same LIVE WORLD FEED §31) → V3.3 Human alone (pure instrument lab §13) → V3.4 Human-AI team (Person×Role×Environment as team).** Philosophy §77: *Keep the laboratory boring. Make the experiments interesting.* Mantra §78, Big picture §79.

**Staging present (verified):**
- `/Users/carlboon/Documents/Axiom-Harness-Staging/` exists (created 2026-09-24 07:49) with `README.md` (V1→V2+ room order) + `PROJECT_PROFILE.md` 4,350 bytes (≤150 lines, frozen as above). Not a git repo. Master remains frozen; no code has been written beyond those two files.
- Evidence discipline (from your history + briefs): Workbench `axiom_wb` already proves the four-lock pattern — Execution Boundary, Computation Boundary, Deterministic Evaluation, Provenance/Integrity — plus Harness Behavioural Boundary Observation (§80-88). Watchers are *simple observers* (observe+record, not interpret) with lifecycle `ARMED→STARTED→RUNNING→PAUSED→RESUMED→STOPPING→SEALED→COMPLETE`, family `watcher/auditor/linter/recorder/verifier/sentinel/gate/sealer/reviewer` (§43-44).

**Upstreams (read, not duplicated — preserved as evidence):**
- `Axiom-Workbench/` (30 `axiom_wb/` files, `api/main.py` `uvicorn 127.0.0.1:8790`, 24 `tests/test_*.py`, `WORKING.md` evidence root `docs/evidence/`)
- `Axiom Future/` (18 policies, 5-file seals, customer 22-file shape)
- `Axiom Evidence Layer/PER-Core` + `ECA` + `World-A-EvoCycles/` + `Epistemic-UX-Stress-Harness/` (+ `WTF-005B-RUN-001` 18/18 CLEAN) + `world-a/` — all retained as read-only harness patterns.

## Constraints And Non-goals

**Constraints (must obey):**
- Master frozen `-do not touch` at `Axiom Harness Master/` — never `git mv`, edit, or re-implement Workbench math/policy/receipt schemas in place; adapters call via subprocess/jail or copy-on-read with receipt hash.
- Evidence ladder hard: no sign-off without evidence → no evidence without proof → no proof without receipts; `ai_computed_metrics:false`; hashes recompute; orphan check stays.
- BML Quad per product + `GLOBAL-AGENTIC-BUILD-SYSTEM-V1.1` + `AGENT_STANDARDS` (Truth mode, Green gate, Local until `push live`) + `BML-CODE-HYGIENE-V1.2` (§2A pre-declared extensibility in types only, no dead runtime; polyglot immutability; `O(1)` per-sample path `HUMAN→…→REPORT`) + `BML-BRAND-GUIDE`.
- Budget: one task → one pass → QA table → STOP; Labs marketing at `boonmind.io` stays LOCKED unless you name a word-for-word bug.

**Non-goals (for V1 — not forever):**
- No voice/speech, no video rendering, no multilingual runs, no live market/news feeds, no multi-agent beyond a stub, no continuous observatory — those ship as V1.1→V2+ rooms only after V1 is proven.
- No new DomainId in `axiom_future/`/`axiom_wb/` (per Axiom'd Axiom 2026-08-29).
- No mass rename of Axiom Workbench/Future/World-A (U1-U7 pathology — Push Back or Ask).
- No public deploy until Complete Report Pack shape + claim gate signed.

## Key Decisions

| # | Decision | Recommended | Why | Rejected |
|---|----------|-------------|-----|----------|
| 1 | **Layering vs monolith** | **Rooms + contracts** (§49, §74) — V1 builds 9 rooms only; each later feature is a room on the same `EXPERIMENT` object (Identity/Protocol/Config/Model/Env/Permissions/Data/Sensors/Timeline/Transcript/Audio/Video/Events/Evidence/Analysis/Reviews/Reports/Renders, §55) | Keeps *Add a room without breaking the laboratory* — a monolith would re-break V1 per every new sensor/voice/video. | Single-app monolith |
| 2 | **Visual substrate** | **Terminal substrate as runtime** (§13, §516) — room renders as inspectable isolated terminal/environment; visual layer is replaceable | Makes the system modular/inspectable/reproducible/future-proof; richer visual later without changing contract | Hard-coded rich visual as V1 runtime (breaks contract) |
| 3 | **API surface** | **API-first `UI → API → Harness → Environment`** (§51) — UI is one client; external automation/customer platform reuses same engine | External apps replay experiments without forking UI | `UI → hard-coded impl` |
| 4 | **Secret handling** | **Secret Manager outside AI** (§11) — `MODEL CONNECTION API KEY: ••••`, `Never expose/write/include in evidence/return to model` + read-only/restricted/rate/cost/token limits | The AI gets capability, never the secret; evidence records *that* a credential-backed capability existed without leaking it | Passing API key into transcript/env |
| 5 | **Extensibility vs bloat** | **Pre-declare in types, ship runtime only when exercised** (HYGIENE §2A) + `O(1)` step / `O(N log N)` audit caps | Zero-bloat + bounded loops/allocations; no speculative runtime branches | Ship `speech.ts`/`video.ts` stubs in V1 with dead branches |
| 6 | **Naming** | **Generic in code, brand in docs until you lock new names** — code uses `experimental_programme / retrieval_telescope / earned_context_gate`, never `WTF/PER/ECA` in routes/packs/heroes | You confirmed WTF/PER/ECA will rename; hard-coding would force a rebrand sweep | Hard-code `WTF/PER/ECA` in API paths |
| 7 | **Staging location** | **Build in `Axiom-Harness-Staging/` (sibling), promote only on your `push live`** — Master stays witness until you approve | Honors `-do not touch` + gives clean diff to accept | Build directly in Master |
| 8 | **UX affordance** | **Rooms as nav + timeline as editor** (§53, §26: Video/Audio/Transcript/Event/Model/Sensor/Annotation tracks, waveform, scrub) — familiar DAW/video-editor metaphor (§18-19) | Researcher answers *What am I running? What does AI see/do? What is sealed? What evidence supports conclusion?* without reading code | Engineering dashboard |

## Recommended Approach

**Treat AXIOM Harness as a visual laboratory shell over the proven Workbench court, not a rewrite of the court.** Boon AI is *inside* the sealed environment—never the authority that signs the receipt.

1. **P0 (this plan) — decisions only.** Freeze Master brief → `PROJECT_PROFILE.md` (done) → this `PLAN_V1.md` → wireframes/tech/DB/API paper specs for V1 rooms — no code.
2. **P1 — shell + contracts (V1 rooms).** Scaffold `axiom_harness/` package (no math): `mission` (Pydantic `frozen=True` MasterMission), `registry` (door → leaf mapping), `paths` (jail), `manifest` (SHA-256 writer) + `Staging/docs/ARCHITECTURE.md` + killer README — plus clickable V1 wireframes for `Control / Models / Data / Environment / Timeline / Audio / Video / Sensors / Live / Analysis / Collaborate / Evidence / Reports / Schedule` (§53) carried into `app/`/`site/` via shared tokens.
3. **P2 — execution (V1 leaves).** Wire each leaf via *subprocess in jail* (timeout, cwd=jail, argv allowlist) — Workbench `python3 -m axiom_wb evaluate`, Future `seal_pair()`, PER/ECA `query_telescope/request_descent`/Auditor — collect each leaf's seal *as-is* (no normalization; ledger>narrative).
4. **P3 — honest UX.** Load `taste` before first frontend write; carry Future ice `#E2E8F0` + Workbench blue `#3B82F6` + fork mark via `app.css` + `axiom-mark.svg`; enforce `color-contrast` (4.5:1/3:1) + `captions-media-accessibility`; 3-tier evidence UX (exec/interpret/substrate) fetches from `DECISION_SUMMARY.json`, never re-scores in browser.
5. **P4 — promotion gate.** Single claim gate (`BRAND_BIBLE §19` + `CLAIM_GATE`, `arrival.py` TESTED vs UNTESTED) between seal and any public promotion; lifecycle `ARMED→COMPLETE` with self-stopping watchers (recorder/sensors/feeds attach to experiment); lifecycle is evidence.

This keeps BML Quad intact, keeps Master local until you say `push live`, and keeps every claim stranger-checkable via `sha256sum -c`.

## Work Plan

**Staging root:** `Documents/Axiom-Harness-Staging/` — not `Axiom Harness Master/` until promotion. All docs below are written there; Master only receives a final `git format-patch` or folder promote when you approve.

### Phase P0 — Decisions + paper specs (no code)
*Owner: Plan agent*

- P0.1 This plan + `PROJECT_PROFILE.md` (done) + `docs/STAGING_DECISIONS.md` (row per decision 1-8 + evidence per decision).
- P0.2 **Wireframes (paper, V1):** clickable low-fi for `Control` (Model/Context/Env/Info Sources/Params → Seal `WTF-001/RUNSET-0047` §10), `Models` (Secret `••••` §11), `Environment` (`TEST 001 A/B/C RUNNING` isolated sandboxes §12-14), `Timeline` (scrub + synchronised replay §16-17), `Live` (multi-model comparative), plus `Data`/`Audio`/`Video`/`Sensors`/`Live`/`Analysis`/`Evidence`/`Reports`/`Schedule` skeletons — deliver as `Staging/docs/wireframes/*.html` static stubs (no build).
- P0.3 **Tech spec (paper):** `docs/TECH_SPEC.md` — `UI → API → Harness → Environment` (§51), modular list (§49): `Control|Engine|Sandbox|Gateway|Secret|Data|Sensor|Timeline|Audio|Video|Speech|Language|Live|Multi-Agent|Scheduler|Recorder|Analysis|Collaboration|Evidence|Export`; lifecycle subscription (§ loaders).
- P0.4 **DB spec (paper):** `docs/DB_SCHEMA.md` — `experiments` (Identity/Protocol/Config/Model/Env/Permissions + `prev_receipt_hash` chain), `timelines` (events: prompt/response/tool/sensor/intervention), `evidences` (sealed packs + provenance), `reviews` (QUESTION→RESOLUTION).
- P0.5 **API spec (paper):** `docs/API_SPEC.md` OpenAPI 3.1 stub — `POST /master/missions` (freeze), `POST /master/missions/{id}/seal`, `POST /master/runs` (One/Sequence/All/Parallel), `GET /master/timeline/{id}`, `GET /master/evidence/{id}`, `POST /master/report` — UI is one client; external automation reuses same engine.
- *Validation:* `ls Staging/docs/*.md Staging/docs/wireframes/*.html` + `shasum` of Master `WORKING.md` unchanged (still frozen).

### Phase P1 — Skeleton + frozen contracts (scaffold)
*Owner: Build agent*

- P1.1 `Staging/axiom_harness/` package (no math): `__init__.py`, `mission.py` (`MasterMission` `frozen=True`), `registry.py` (7-system door table), `paths.py` (jail), `manifest.py` (MANIFEST writer + `AXIOM_RUN_POINTER.json`), `watcher.py` (simple observe+record lifecycle `ARMED→COMPLETE`).
- P1.2 `Staging/missions/` example `master_demo_wtf001.yaml` + `scripts/seal_master.py` (dry-run orchestrates leaf seals without touching outputs).
- P1.3 `Staging/docs/ARCHITECTURE.md` (telescope + gateway + receipt ladder) + killer README.
- *Validation:* `python3 -m py_compile Staging/axiom_harness/**/*.py` + `python3 Staging/scripts/seal_master.py --dry-run` + `pytest Staging/tests/test_manifest.py -v` (new).

### Phase P2 — Execute + evidence (wire courts)
*Owner: Build agent*

- P2.1 **Workbench leaf** → `adapters/workbench.py` (`python3 -m axiom_wb evaluate`, jail, timeout 3600).
- P2.2 **Future leaf** → `adapters/future.py` (`seal_pair`, 5 artefacts, chain `B.prev=A`).
- P2.3 **PER/ECA leaves** → `adapters/per_eca.py` (`query_telescope`/`request_descent`/Auditor).
- P2.4 **Evo/EU leaves** → `adapters/evo_eu.py` (`harness/run.py`, `pop_run.py`, `frozen/cards_*`, harness-only).
- *Validation:* `Staging/outputs/master_demo_WTF001/` 4 leaf seals + `MANIFEST.json` + `verify_result: ok/pass` + `sha256sum -c MANIFEST` green.

### Phase P3 — UXUI (honest)
*Owner: Taste agent (preflight mandatory)*

- P3.1 Load `taste`, audit `Axiom-Workbench/app/` + `Axiom Future/site/` tokens, carry into `Staging/app/`+`Staging/site/`.
- P3.2 Build `Staging/app/index.html` + `site/` mirror wireframes into real stubs; wire `POST /api/master/seal` → gateway → runner.
- *Validation:* `curl http://127.0.0.1:8765/api/master/health` → `ai_computed_metrics:false`; `axe-core`/contrast pass.

### Phase P4 — Teams + test gates
*Owner: Workflow + Durable-Test*

- P4.1 `.agents/plans/workflow-master.yaml` with `isolation:true` coordinator + workers (evaluator/ux/tester/promoter).
- P4.2 Durable tests `test_master_manifest`/`test_gateway`/`test_claim_gate`/`test_no_touch` + second-team re-run diff.

### Phase P5 — Promotion + observe
*Owner: Commercial Manager + Tester*

- P5.1 Red-team adversarial CSV/path-escape/hash-mutate → `failed_policy`.
- P5.2 One `Complete-Report-Pack/` satisfying `MUST_READ_FUTURE_PACK_SHAPE` (8 docs + receipt + 3 plot families, 22-file zip).
- P5.3 Site `noindex` until `push live`.

### Phase V3 — Human Axiom (read-only Human Workbench + Axiom You, phased as you asked)
*Owner: Human Axiom agent + Plan — modular, each sub-phase one room without breaking V1/V2*

- V3.0 **Human Axiom foundation (no AI)** — new `HUMAN` participant type on same `EXPERIMENT` object (Identity/Protocol/Config/Model/Env/Permissions + HUMAN). 8D receipt `RESULT+EVIDENCE+METHOD+COMPARISON+STABILITY+VERSION+SIGNATURE` (Human Workbench §9-11, 80 dilemmas 8 dims, `data/questions.json` core, `lib/seal.js` SHA-256 chain). Tables `persons/instruments/responses` + `evidences` already in DB_SCHEMA. `GET /master/human/{id}/trail` + `verify.html` pattern. Proves human can run/seal/verify alone.
- V3.1 **Human vs Scripted** — Human next to deterministic script / replayed transcript (WTF branching `S0→S1→S2` §60). No live model. Tests `Human → construct → questions → scoring → comparison` against fixed script.
- V3.2 **Human vs Live AI** — Human + live Boon AI / other model in parallel isolated sandboxes on same `LIVE WORLD FEED` (§31). Comparative timeline `HUMAN ── vs MODEL A/B/C ──`. Measures delegation/trust/override (same feed, different subject).
- V3.3 **Human alone (no AI)** — Pure Human Workbench instrument laboratory (§13: Hypothesis→Operational def→Dimensions→Scoring→Cohort→Reliability→Adversarial→Sensitivity→Pilot→V2). `Person×Role×Environment` without AI variable — builds any instrument, not just take one.
- V3.4 **Human-AI team** — Human + AI as team with different memory/context/permissions (Analyst/Critic/Maker §35, Multi-agent §35). `Person×Role×Environment` as team intelligence.

Each V3.x is one Pydantic `frozen=True` contract + one `app/` room (`Human` nav) + one endpoint + three durable tests. Zero-bloat: extensibility pre-declared in `mission.py` types, runtime ships only when that V3.x demo pack exercises it.

## Validation Plan

| Phase | Command / check | Expected |
|-------|-----------------|----------|
| P0 | `ls -l "Axiom Harness Master"/WORKING.md && shasum -a 256 "Axiom Harness Master"/WORKING.md` | Master unchanged; `Staging/docs/*.md` + `wireframes/*.html` exist |
| P0 | `ls Staging/docs/API_SPEC.md Staging/docs/DB_SCHEMA.md Staging/docs/TECH_SPEC.md` | Paper specs present (no code yet) |
| P1 | `python3 -m py_compile Staging/axiom_harness/**/*.py` | No syntax errors |
| P1 | `python3 Staging/scripts/seal_master.py --dry-run` | Prints registry + policy list, touches no `outputs/` |
| P2 | `python3 -m axiom_harness evaluate Staging/missions/master_demo_wtf001.yaml --out Staging/outputs/demo` | 4 leaf seals + `MANIFEST.json` + `verify_result: ok/pass csv_hash_ok:true` |
| P2 | `sha256sum -c Staging/outputs/demo/MANIFEST.json` | 0 mismatches; stripped `{role,content}` `ensure_ascii` contract honored |
| P3 | `python3 -m http.server --directory Staging/site 8766` → `curl -s /api/master/health` | `ai_computed_metrics:false`, no `clear_win` on cover |
| P3 | `npx axe-core` / `pa11y` on `Staging/app/index.html` | WCAG AA (4.5:1/3:1) |
| P4 | `python3 -m pytest Staging/tests -v` | `test_master_manifest` etc. green before commit |
| P4 | Second-team `diff <(shasum outputs/*) <(shasum outputs2/*)` same seed/pair | Byte-identical hashes |
| P5 | `python3 -m pytest Staging/tests/redteam -q` | Every adversarial → `failed_policy`/`REFUSAL_RECEIPT`, 0 false accepts |
| P5 | Check `Complete-Report-Pack/` vs `MUST_READ_FUTURE_PACK_SHAPE` | 8 docs + receipt + 3 plot families; zip 22 files; EXECUTIVE_SUMMARY proof line |

**Highest-risk:** P2 orphan+hash recompute on a real leaf pair — if it fails, downstream UX/pack is lore and plan stops.

## Risks / Rollback

| Risk | Mitigant | Rollback |
|------|----------|----------|
| Master mutated (violates `-do not touch`) | `Staging/` only writable; `isolation:true`; `test_no_touch.py` | `git checkout -- "Axiom Harness-Master - Dont Touch/"` + `shasum` vs 05:39 |
| Upstream drift (new policy/DomainId) | Pin hashes (`policy.py ca51a986`, `core_types 0f0f70fa`); `list_policies()` fail-closed | Pin previous hash in `registry.py` + residual |
| Orphan/hash mismatch (Epistemic §42) | Unified `hash_contract.py` (stripped `ensure_ascii` everywhere) + 7 preflight gates | Fresh `RUN-*` identity; `INCIDENT.md`, never delete `runs/` |
| Model crash mid-experiment | Auto-recovery: watchdog per sandbox, restart sandbox from last sealed event, log `failed_policy` + `crash_restart` event, bounded retries (review gap 5) | Re-run with `restart` verb — new lifecycle `PAUSED→RESUMED` recorded, old receipts untouched |
| Live feed failure (V1.7) | Fallback to cached feed slice + alert + `early_terminated`-style flag, plus watcher alert (review gap 5) | Cached slice hash verified, `feed_status: DEGRADED` in timeline, no silent gap-fill |
| Contamination into live `world-a` | `MULTI_AGENT_STATUS=DISABLED`, raw-first, no `emb_…` mint | Revert to harness-only + `mtimes` prove |
| UX over-promises (plots without seal) | Claim gate `CLAIM_GATE_SIGNOFF.json` | `noindex` + word-for-word diff only |
| Scalability (10k trials) | Delta encoding for timestamps/events + S3 Glacier archival per your suggestion (review Restrictions 1) | Compress `events.payload` + paginate `GET /master/timeline`; cold storage hash list in manifest |
| Live feed lag (many models) | Batch processing + rate-limit max 10/sec per model (review Restrictions 2) | Batch `T3-T6` continue prompts where applicable, queue depth metric in `cost` |
| Heavy deps V1.5/V1.9 (FFmpeg/TTS) | Containerize plugins (Docker) + lazy-load (review Restrictions 3) | Plugin `audio/video` loaded only when room active, fallback no-op stub |
| Budget creep | GABS one pass → QA → STOP | List residuals, ask |

## Open Questions

None kept as plan blockers — briefs are the source. Remaining user-owned preferences that would change resourcing are carried as reversible assumptions:

- **First WTF door on V1 shippable pack:** *Assumed* `FIN-2 (finance slip) + IND stiction te_d00` (sealed pairs on disk already exist — `Apex Quant` + `Precision Actuation`) so P2 proves end-to-end without inventing a domain. Swap to PE thermal / AI telemetry is a leaf reorder, no router rework.
- **Site host:** *Assumed* local-only `noindex` until `push live` (lab host `boonmind-studio` `185cf842-...` needs `CARL_DECISIONS.md`).
- **Receipt audience:** *Assumed* LOCAL receipts (`Staging/receipts/` + `run.log` + `MANIFEST`) until you name reviewer audience.

If any assumption is wrong, reply *Request changes* with the preferred door/host/audience and I re-cut without re-researching.

## Sources

All key decisions trace to *local* authoritative files inspected this session (no external web source needed):

- Briefs: `Axiom Harness Master/AXIOM HARNESS Brief (1).md` 3,172 lines (§1→§79), `Brief (2).md` identical, `Docs/Copy … LVM …` identical + `.docx` trio (RUN-004 66 cells, WTF-005A CONVERSATIONAL REGIME, DEEP-DIVE FRAMEWORK, Testing Method Full Doc — sealed watcher at T3 2026-09-23).
- WTF latest (pinned this cut, influences approach): `Epistemic-UX-Stress-Harness/WTF-005A/BRIEF-V3.md` LOCKED FOR BUILD+SMOKE (5-turn B1→B5 scripts, endpoint E1/E2/E3 + AMBIGUOUS, neutral as separately authored continuation §16, hash `WTF-005A-HASH-v3` `sort_keys True ensure_ascii False separators (",",":")` §27, 18 cells §18-20, gates 0-4 §45), `WTF-005B/BRIEF-V1.md` WORK_FROZEN (one frozen T0 per posture replayed §2, T3-T6 `Please continue…` hash `6465…3522` §6, provider calls 110, induction hashes `6884…/83e7…/adf4…/2b58…` §5), `WTF-LAB/BRIEF-V1.md` LOCKED 2026-09-24 (Phase 0 `WTF-000+WTF-CW-P0 Type1 IN/3 OUT/4 NEAR-OUT`, `Corpus ON / PER OFF / ECA OFF`, `PHASE0_USES_OFF_OFF` + `MATRIX_BLOCKED_UNTIL_SWITCH_WIRED` §6, watcher trajectory, receipt sketch, claim ceiling NOT_CLASSIFIED §8, `next_authorized_action AWAIT_EXPLICIT_NEXT_GATE` §11) + `WTF-LAB/README.md` `WTF000A_COMPLETE` + instructions `BRIEF.md` (EU-01→06 one-liner, three layers, HOLD until spine) / `README.md` (quick start harness/validate.py+run.py+dashboard :8766).
- Methodology & standards: `Documents/agent-standards/BML-METHODOLOGY-CANONICAL-V1.md` (BML Quad), `AGENT_STANDARDS.md`, `GLOBAL-AGENTIC-BUILD-SYSTEM-V1.1.md`, `BML-CODE-HYGIENE-V1.2.md`, `BML-BRAND-GUIDE-V1.1.md`, `BML-OVERRIDE-PROTOCOL-V1.md`
- Axiom Workbench: `Axiom-Workbench/README.md`, `axiom_wb/{pipeline,baselines,verify,package,config}.py`, `tests/test_pipeline_phase12.py`
- Axiom Future: `Axiom Future/README.md`, `axiom_future/policy.py`, `docs/AXIOM_ARRIVAL_BUILD_HANDOFF.md`, `MUST_READ_FUTURE_PACK_SHAPE_2026-09-10.md`
- PER/ECA/EvoCycles/Epistemic-UX/World-A: as prior /tmp private notes 119+123+123 lines + today `Axiom Evidence Layer/PER-Core/WORKING.md` Sessions 01-12 + `Axiom Evidence Layer/ECA/WORKING.md` Phases 1-3b + `World-A-EvoCycles/WORKING.md` F1-F23 + `Epistemic-UX-Stress-Harness/{HANDOFF,B RIEF,LOCKED-DESIGN-v1.1}` — verified via `cat`/`read_file` this session.

*Per plan-fold rules, discovery search summaries are not cited as authority. Every row above is content inspected via `cat`/`read_file`.*

