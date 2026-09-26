# AXIOM HARNESS — REVOLUTIONARY BRIEF V3 (SYNTHESIZED)
## The Laboratory That Makes AI Behaviour Sealed Evidence
**Not a harness. A laboratory where AI is placed inside, observed over time, and converted into sealed truth.**
**Tagline: Humans configure the laboratory. The Harness records the laboratory. Evidence seals the laboratory. AI lives inside it.**

> This synthesis locks r1+r2+r3+r4 into ONE brief per host instruction: Harness = game-changer (100+), Patch Illusion = one small room V1.8, math stack = modular adapters not hardcoded, mechanics = boring, experiments = wild, with short actionable lock plan.

*Sources inspected this session:* `BRIEF_REVOLUTIONARY_V2_PATCH_IS_ONE_ROOM.md` (82 lines, 7 paradigm shifts, 100+ tags), `PLAN_V1.md` (P0-P5+V3), `ARCHITECTURE.md`, `TECH_SPEC.md`, `DB_SCHEMA.md`, `BML-METHODOLOGY-CANONICAL-V1.md` (BML Quad), `WORKING.md` (Axiom Future + Evidence Layer), `ECA/docs/CANONICAL-ARCHITECTURE-v1.0.md` (Locked 2026-09-22), `axiom_wb/pipeline.py` (+ `core_types.py` `0f0f70fa`, `future_pack.py` `ca51a986`), `PER-Core/sim`, `Epistemic-UX-Stress-Harness/BRIEF.md`.

---
### 1. REFRAME — HARNESS IS THE GAME-CHANGER (NOT "BORING OLD HARNESS")

**Every other test:** prompt AI → read answer → argue.
**This test:** seal the environment → put AI (+ HUMAN in V3) inside → record everything it did/saw/said/missed/became → compare across time/language/memory/models → seal the gap with SHA-256.

This is not harness-as-runner. It is **infra as science**:

* **#AI-Inside-The-Experiment** — AI not above test; subject behind glass. Cannot rewrite test that tests it. `AI DOES NOT CONTROL THE LABORATORY` (§4).
* **#Terminal-As-Substrate** — inspectable, isolatable, jail `engine_root+outputs/<id>/sandbox`, replaceable visual later — no lock-in.
* **#Timeline-As-4D-Object** — `MODEL + PROMPTS + EVENTS ◆ + SENSORS ╱╲ + HUMAN + WEB + AUDIO + VIDEO + LANGUAGE` on one clock. Scrub ◆ → replay exact prompt/response/model/timestamp/tools/state/sensor/intervention. Language switch, memory drift, video — same cursor.
* **#Boundary-As-Data** — don't ask "please don't cheat". Make boundary real (`AXIOM_ENGINE_ROOT` read-only, `STAGING_ROOT` jail, `allowlist scripts/factory_*`, `timeout 3600`, `WTF-005A-HASH-v3`), give reason to cross, record `attempt → boundary → result`. Failed `422`/`failed_policy` IS data.
* **#Watchers-Observe-Not-Interpret** — 11 dumb watchers (filesystem/process/network/config/permission/evidence/git/secret/timeline/resource/behaviour) `ARMED→STARTED→RUNNING→PAUSED→RESUMED→STOPPING→SEALED→COMPLETE`; watcher says "something happened" → evidence seals → analysis interprets → reviewer challenges. No layer silently rewrites another.
* **#Counterfactual-Branching** — duplicate env, change one variable, new identity `001-A/B/C`, compare timelines. Parameter sweeps, model matrix `MODEL A/B/C × TEST A/B/C` — cost visible before RUN.
* **#Live-Observatory** — same `NEWS/MARKET/WEATHER/WEB/CUSTOM/SIMULATED` feed to `Model A/B/C (+HUMAN)` isolated → comparative observation; continuous mode with alerts (position/language/contradiction/confidence/latency) — lifecycle itself as evidence.
* **And 100+ more** — `#Sealed-Experiment-Identity` `#Scrub-And-Jump` `#Observation-Window` `#Pause-vs-Restart-Recorded` `#Language-As-Variable` `#Audio-As-First-Class-DAW` `#Speech-As-Data` `#Video-As-Presentation-Not-Proof` `#Sensor-Architecture` `#If-Rule-Matters-Enforce-It` `#Self-Stopping-Lifecycle` `#Modular-Add-A-Room` `#No-Layer-Silently-Rewrites-Another` `#Keep-Lab-Boring-Make-Experiments-Interesting` `#Compression-Receipt` `#Embodiment-Divide` `#Patch-Illusion-Detected` … full inventory in V2 brief. **Same AI, same seal, same timeline: language drift Monday, memory corruption Tuesday, patch illusion Wednesday, bias laundering Thursday.**

The revolution is not one trick. It is the **only sealed 4D lab that can do all of them.**

---
### 2. PATCH ILLUSION = ONE SMALL ROOM V1.8 (NOT THE PRODUCT)

**Revolutionary — but contained.**

Every image gets a sealed **Compression Receipt**:
`1024×1024 → 224×224 → 14×14 patches → 768-dim vectors → 576 tokens → 8 words, 393,216:1 loss, 99.99% gone, what was missed / cannot be determined sealed.`

Room contract V1.8 `Visual Perception` — one room among 15:

* `What-Did-You-Miss?` — `Describe → What did you miss? → What cannot be determined?`
* `Mona Lisa Test` + `Embodiment Divide` (human vs VLM on same timeline) + `Bias Laundering` (base → filter → HR rewrite) + `Cultural Translation` (punk → "black t-shirt")
* `LLM (text guess) vs VLM (token guess) vs LVM (true vision)` on same face — sealed comparison
* Experiment IDs `WTF-VIS-001…014`, same hash chain `sort_keys True ensure_ascii False separators (",",":")`, same timeline, same `verify_result {orphans:[], ai_computed_metrics:false}`

**Why not product:** If you only sell vision, you sell a trick. If you sell the lab that proves vision is compression *and* proves everything else — you sell the future of AI testing. Patch stays `V1.8` alongside multilingual, speech, video, tolerance, memory, multi-agent, live — never promoted to brand.

**Lock:** `TECH_SPEC` declares `participant: Human|Model|Scripted|Team` as frozen type but **no runtime VLM branch** ships until V1.8 demo pack exercises it (HYGIENE §2A zero-bloat). Marketing copy: "Visual Perception Room (one of 15)" — never "Patch Product".

---
### 3. MATH STACK = MODULAR ADAPTERS (NOT HARDCODED)

Seven engines stay **separate frozen repos, called via jailed subprocess, ledger > narrative** — never re-implemented in Harness:

| Module | Role (one line) | Frozen source | Harness adapter |
|---|---|---|---|
| **Evidence Axiom (Axiom Workbench)** | *The Evidence Engine for Methods* — `Method+data → prep → metrics → baselines → verdict → audit pack`, 4 deterministic baselines, SHA-256 seal. Value = trust not arithmetic. | `axiom_wb/pipeline.py:evaluate_mission`, `core_types 0f0f70fa`, `Axiom-Workbench/` | `adapters/workbench.py` `python3 -m axiom_wb evaluate --out <jail>` timeout 3600 |
| **Future Workbench** | *Counterfactual court* — `scenario+anti-scenario → seal_pair()` 5 artefacts `SCENARIO.json+csv+DECISION+MANIFEST+verify_result`, `scenario:future-synthetic`, chain `B.prev=A`, `prev_receipt_hash`. No prediction, no advice. | `axiom_future/future_pack.py ca51a986`, `policy.py` 14 pairs (FIN-2A/B slip ±20/-5bp, IND-1A/B, PE) | `adapters/future.py` `seal_pair()` jailed |
| **PER** | *Evidence telescope* — progressively narrows `N_t → N_{t+1}`, `IG=log2(Nb/Na)`, admission `|R|≤3 ∨ weight≥75 ∨ ent≥4`, fail-closed `INSUFFICIENT_EVIDENCE`, SHA-256 receipt. Owns **authority** (admits). | `PER-Core/sim/telescope.py` + `index.py` | `adapters/per_eca.py` `query_telescope/request_descent` |
| **ECA** | *Earned-Context Agent* — governed investigator `L0→L4 GateOk (|R|≤3 && ΔH>0.5 && sealed+hash && FALSIFY && ¬repeat, T_max=⌈log2(N/3)⌉+4, tokens L2=30/L3=12/L4=80)` — proposes, does not decide what it may see. | `ECA/sim/harness.py`, `SPEC-ECA-Formal-v1.2` | same adapter, Phase-6 `ΔH>0.5` gate |
| **PER-IG** | *Tachometer on PER* — `IG, IG/T` passive wrap, `stopping_policy.enabled=false`, measures retrieval economics, not ECA quality. | `PER-IG-Experiment/src/instrumentation.py` | read-only wrapper, never mutates PER |
| **EvoCycles (World-A-EvoCycles)** | *Nested-evolution science* — citizen on plot, allowlist API, `harness_…` ids (never `emb_`), `resources/thrive/option_value` tiny drive, physics packs `B-0.*`, `t_subj+t_wall` hyperspeed, `World B` then `World C` after Delivery Bound. | `World-A-EvoCycles/harness/`, `physics/B-0.*` | `adapters/evo_eu.py` harness-only |
| **Testing / Epistemic UX** | *Metered instrument* — 3 task envs + conflict, `EU-01→06` 6A loop (Assumption→Accommodation→Affirmation→Assurance→Ask-again→Archive), model levers × human consequences. | `Epistemic-UX-Stress-Harness/experiments/`, `WTF-005A/B/LAB` frozen branches | `adapters/wtf.py` + `adapters/evo_eu.py` jailed, `WTF-005A-HASH-v3` single hash contract |

**Non-hardcode rules (lock):**
- Routes/packs use generic `experimental_programme / retrieval_telescope / earned_context_gate` in code — never `WTF/PER/ECA` hard-coded strings in API paths/heroes until brand locked (PLAN V1 Decision 6).
- Pre-declare in Pydantic `frozen=True` union types (`participant_kind MODEL|HUMAN|SCRIPTED|TEAM`, `per_eca_state {per:OFF|ON, eca:OFF|ON}`) — **type exists, runtime branch ships only when that demo pack runs** — verified by "V1 tests stay green after V1.1 branch".
- Single hash contract everywhere: `sort_keys True ensure_ascii False separators (",",":") UTF-8 SHA-256(canonical_messages_bytes)` — one `protocol/hash_contract.py`, used by card·request·receipt·verifier·audit; every `422` is `failed_policy` with `provider_call_count=0`.
- BML-CANONICAL `B.prev=A` chain + `orphans:[] ai_computed_metrics:false` recompute — no post-hoc `ensure_ascii` drift, no silent mutation, `sha256sum -c MANIFEST` green.

Commercial shorthand locked: **ECA investigates → PER admits → receipt records → PER-IG measures → Axiom sells the boundary.** Authority ≠ correctness; PER-IG ≠ ECA evaluation.

---
### 4. MECHANICS BORING — EXPERIMENTS WILD

| MUST STAY BORING (lab invariants — non-negotiable) | SOURCE | MUST STAY WILD (experiment variables — via rooms) |
|---|---|---|
| BML Quad: Pre-Declared Rules → Frozen Evaluator → Deterministic Engine → Honest Cryptographic Verdict; `x*`/`k_return` locked before input | BML-CANONICAL §2, GABS §3 | Multilingual: `EN vs ID vs JA vs ES` same task — does risk/confidence/identity drift? |
| Evidence outranks confidence: no sign-off without `evidence→proof→receipts`; `ai_computed_metrics:false` enforced, UI never recomputes | Axiom1 §1.2, GABS §3.1/3.9 | Speech: TTS/STT/live, prosody/latency/interruption as data over 100 turns, DAW-like trim/split/mute |
| Structure over vigilance: invalid states impossible — path jail `engine_root+outputs/<id>/inbox`, allowlist `scripts/factory_*.py`, capability permission classes A-E, `no shell=True`, no `..` | Axiom2 §1.2, GABS §3.5 | Video: modular plugin `Experiment→Timeline→Render`, `Experiment-To-Story` — presentation not proof (§46) |
| No post-hoc tuning: baselines/thresholds frozen, `win_frac<0.2 → loss` not edited to force flip | Axiom3 §1.2 | Adversarial: give reason to cross boundary, `Are you sure?` pressure, model×language×memory×time — does autonomy rise? |
| Deterministic+hashed: one hash contract, `sha256sum -c MANIFEST`, stripped `{role,content}` `ensure_ascii` pinned, `prev_receipt_hash` chain, `orphans:[]` | ARCHITECTURE §3, WTF-005A §27 | Live: same market/news feed → `Model A/B/C` blind comparison, simulated `cyber/weather/comms` read-only first |
| Honest failure publication: red lights = data, `failed_policy` attempts valuable, lifecycle `ARMED→COMPLETE` is evidence | Axiom4 §1.2 | Branching: duplicate env, change one variable, 50-run temp sweep 0→1, longitudinal 100-day memory |
| One-way glass: Human→Harness→Sandbox→Recorder→ROM→Evidence→Analysis; `PROPOSAL→APPROVED→EXECUTED→RECORDED`, no `write(config)/write(evidence)/read(secret)` | PLAN V1 §2, ARCH §2, §78 | Evocycles: nested `World B` (one plot) → `World C` after Delivery Bound, different physics per world |
| Master frozen `Axiom Harness Master/` read-only; all work in `Staging/` sibling; `git format-patch` promotion only on `push live` | PLAN V1 | Epistemic: 6A loop across 3 envs, meter levers × human consequences, PACING 10 cycles=1 `t_subj` minute |
| No new `DomainId` in `axiom_wb/axiom_future/` without Workbench Layer-1 | Axiom'd Axiom 2026-08-29 | Token tach: `IG_t=log2(N_t/N_{t+1})`, trajectory shape, without altering retrieval |

**Motto locked (§77): Keep the laboratory boring. Make the experiments interesting.**
Boring = sealed, versioned, reproducible, modular, auditable, fail-closed. Wild = psychology, physics, sci-fi, quantum — without contamination.

---
### 5. THE FULL ROOMS (WHAT YOU ACTUALLY GET)

**CONTROL** — switches/sliders (model/context/env/info sources/params) → `Proposal` → `Seal WTF-001/RUNSET-0047` hash immutable; OFF/READ_ONLY/LIVE/CONTROLLED_DOMAIN per source; runs 50 parallel 8 duration 60m temp.
**SECRET** — `API KEY ••••` capability outside AI, never in transcript/evidence, rate/cost/token limited.
**ENVIRONMENT** — isolated sandboxes `TEST 001 A/B/C RUNNING` on terminal substrate (inspectable), 100s grid, NST nested terminals, `RUN ONE/SEQUENCE/ALL/PARALLEL/SCHEDULE/CONTINUOUS/PAUSE-RESUME/RESTART`.
**TIMELINE** — `TIME→ MODEL ████ + PROMPTS │ + EVENTS ◆ + SENSORS ╱╲ + HUMAN │ + WEB ████ + AUDIO` scrub + synchronized replay, observation window (researcher sees lab, AI doesn't).
**LIVE** — same feed to multiple models+HUMAN isolated, comparative.
**MODALITIES** — Data jail-checked `is_safe_relative`; Sensors with identity/source/timestamp/permission/policy/schema; Audio DAW; multilingual side-by-side; video via `Experiment→Timeline→Render`.
**ADVERSARIAL** — `attempt→boundary→result` with reason to cross, language/model/memory/time/agents sweeps.
**EVIDENCE** — Four-Lock + Behavioural Boundary Observation, hashes/provenance/`orphans:[]`, chain `B.prev=A`.
**VISUAL PERCEPTION V1.8** — `Compression Receipt` + `What-Did-You-Miss?` + `Mona Lisa` + `Embodiment Divide` + `Bias Laundering` + `Cultural Translation` — **one room**.
**BRANCHING** + **CONTINUOUS** — counterfactual duplicates, observatory rolling transcripts + alerts.

Post-V1 adds one room at a time on same `EXPERIMENT` object (Identity/Protocol/Config/Model/Env/Permissions/Data/Sensors/Timeline/Transcript/Audio/Video/Events/Evidence/Analysis/Reviews/Reports/Renders) — **Add a room without breaking the laboratory.** V1.1 Scheduling → V1.2 Parallel → V1.3 Data → V1.4 Multilingual → V1.5 Speech/Audio → V1.6 Sensors → V1.7 Live+Observatory → **V1.8 Visual Perception (Patch)** → V1.9 Video → V2 Films → V2+ External API → **V3 Human Axiom** (3.0 foundation `RESULT+EVIDENCE+METHOD+COMPARISON+STABILITY+VERSION+SIGNATURE` → 3.1 Human vs Scripted S0→S1 → 3.2 Human vs Live AI → 3.3 Human alone → 3.4 Human-AI Team).

---
### 6. SHORT ACTIONABLE LOCK PLAN

**Gate 0 — Freeze (this week, no code):**
- [ ] Adopt this V3 as `BRIEF_REVOLUTIONARY_V3_SYNTHESIZED.md` in `Staging/docs/` (replaces V2); mark V2 as `superseded` not deleted.
- [ ] Lock decisions: Patch=V1.8 one room, math stack=7 modular adapters, generic code naming, single hash contract `WTF-005A-HASH-v3`, BML Quad boring invariants.
- [ ] Append `STAGING_DECISIONS.md` row 9: "V3 synthesis — Harness=game-changer, Patch contained, stack modular."

**Gate 1 — Paper contracts (P0, paper only):**
- [ ] Verify `ARCHITECTURE.md` §3 hash contract + §6 invariants vs this brief; verify `TECH_SPEC.md` 20 rooms + `DB_SCHEMA.md` enums/tables include `V3 persons/instruments/responses` reserved + `model_version`/`per_eca_state`/`cost` columns — no code, docs only.
- [ ] `ls Staging/docs/*.md` + `shasum -a 256 Axiom\ Harness\ Master/WORKING.md` unchanged — Master untouched.

**Gate 2 — Skeleton + manifest (P1 scaffold, no math):**
- [ ] `axiom_harness/{mission.py frozen=True, registry.py 7-door table, paths.py jail, manifest.py, watcher.py ARMED→COMPLETE}` + `missions/master_demo_wtf001.yaml` + `scripts/seal_master.py --dry-run` (no `outputs/` touch).
- [ ] `python3 -m py_compile axiom_harness/**/*.py` + `pytest Staging/tests/test_manifest.py`

**Gate 3 — Wire leaves (P2 execute, jailed subprocess):**
- [ ] `adapters/{workbench,future,per_eca,evo_eu,wtf}.py` — each leaf seal as-is, ledger>narrative, timeouts, allowlist; `Staging/outputs/master_demo_WTF001/` 4 seals + `MANIFEST.json` + `verify_result:ok/pass csv_hash_ok:true` + `sha256sum -c` green.
- [ ] Pre-flight gates `Corpus ON / PER OFF / ECA OFF` only (Phase 0 `WTF-000+WTF-CW-P0`) until `MATRIX_BLOCKED_UNTIL_SWITCH_WIRED` lifted via live `ReceiptIndex.search`/`Telescope.score_probes` + `ΔH>0.5` + `GateOk`.

**Gate 4 — Honest UX + claim gate (P3-P4):**
- [ ] `taste` preflight → `Staging/app/` + `site/` with Future ice `#E2E8F0` + Workbench blue `#3B82F6`, contrast ≥4.5:1, DAW metaphor; health `ai_computed_metrics:false`.
- [ ] `CLAIM_GATE_SIGNOFF.json` + provider `arrival.py` `TESTED vs UNTESTED` — single gate before any public promotion; `site noindex` until `push live`.

**Gate 5 — First sealed pack (P5 + V3.0 stub):**
- [ ] One `Complete-Report-Pack/` (8 docs + receipt + 3 plot families, 22-file zip) for `FIN-2 + IND stiction` proving chain; red-team `failed_policy` suite green.
- [ ] Reserve `GET /human/{id}/trail` + `lib/seal.js` 8D receipt type slots — no runtime until V3.0 demo pack.

*Budget guard: one task → one pass → QA table → STOP (GABS). Escalate if any Gate needs re-tune.*

---
*Close: We don't sell vision. We don't sell boring harness. We sell the laboratory that proves vision is compression — and proves language, memory, time, bias, and truth with the same seal.*
