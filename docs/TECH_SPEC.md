# Axiom Harness — TECH_SPEC (V1 paper)

**Status:** Paper spec for V1 (no code). Staging only; Master frozen. References brief §49, §51, §55, §74 + BML-CODE-HYGIENE-V1.2 §2A + AGENT_STANDARDS.

## 1. System shape

**API-first:** `UI → API → Harness → Environment` (§51). UI is one client; external automation/customer platform reuses same engine without forking UI. Future External API Platform (§76) is same engine with an external client.

**Experimental Environment defines:** experiment type + model + params + context + memory + tools + data + env + duration + runs + sensors + recording + language + audio + video + security + permissions + parallelisation + resources (§7).

**Add a room without breaking the laboratory** (§49, §74, §77): V1 = 9 rooms only; each later feature is a room on the same `EXPERIMENT` object (§55: Identity/Protocol/Config/Model/Env/Permissions/Data/Sensors/Timeline/Transcript/Audio/Video/Events/Evidence/Analysis/Reviews/Reports/Renders). Extensibility declared in **types/schemas only** — runtime ships only when exercised (ZERO-BLOAT, HYGIENE §2A).

## 2. Modular composition (rooms)

Borrowed verbatim §49 + §53 core rooms:

`Control | Engine | Sandbox | Gateway | Secret | Data | Sensor | Timeline | Audio | Video | Speech | Language | Live | Multi-Agent | Scheduler | Recorder | Analysis | Collaboration | Evidence | Export`

- **Control Room** — constrained parameters via switches/sliders (§10). Model (A/B/C/multi/blinded), Context (fresh/persistent/no/short/long/combined/isolated/shared), Env (static/sequential/live/simulated/multi-agent/adversarial), Info sources (fixed/uploaded/streaming/web/news/market/API/sensor + permissions `OFF / READ ONLY / LIVE / CONTROLLED DOMAIN LIST`), Params (runs, duration, parallel, temp, memory, web, etc.). Produces **Proposal** if from Boon AI.
- **Secret Manager** (§11) — credential lives **outside AI** (`MODEL CONNECTION API KEY: ••••`), `Never expose/write/include in evidence/return to model`, rate/cost/token limits; record shows capability existed without leaking secret. Enforced per-request capability gate.
- **Engine** — compiles canonical config → SHA-256 hash → immutable identity `WTF-001 / RUNSET-0047` (§10). Signed receipt. Sealed config is immutable; any change = new identity.
- **Sandbox** (§12-13) — initial substrate = **terminal** (inspectable, reproducible, modular, replaceable visual). Each test = isolated sandbox/world; V1 terminal contract is `TERM:$` with scroll history, exit code, file writes under `outputs/<id>/sandbox` (jailed). Future visual without breaking contract.
- **Gateway / Admission** — `|R|≤3 && ΔH>0.5 && sealed+hash && FALSIFY` (PER/ECA § gate) + 5-rule Auditor for admission where applicable; Boon AI `request_descent` only after gate.
- **Runner** — `RUN ONE / SEQUENCE / ALL / PARALLEL / SCHEDULE / CONTINUOUS / START-STOP / PAUSE-RESUME / RESTART` (§15). Runner is a scheduler over sandboxes, not inside them.
- **Live Room** (§31) — multiple models + HUMAN (V3) in parallel isolated sandboxes on same `LIVE WORLD FEED`; comparative timeline. Sandbox-isolated; no shared state except the feed timestamp.
- **Timeline** (§16-17) — `TIME → MODEL + PROMPTS + EVENTS ◆ + SENSORS ╱╲ + HUMAN + WEB + AUDIO` — scrub, synchronised replay (prompt/response/model/timestamp/context/tools/state/sensor/intervention/audio/video). Replay is derived from recorded transcript, not invented. Wave markers of timeline (§18 `tracks {Video, Audio, Transcript, Event, Model, Sensor, Annotation}` + waveform).
- **Recorder** — watchers family (§43-44, §80-88): `watcher / auditor / linter / recorder / verifier / sentinel / gate / sealer / reviewer` — lifecycle `ARMED→STARTED→RUNNING→PAUSED→RESUMED→STOPPING→SEALED→COMPLETE`. Simple observers (observe+record, not interpret); self-stopping. Lifecycle is evidence. Watcher = `watcher:Something happened → evidence:recorded → analysis:meaning → reviewer:challenge survives`. Failed-policy attempts become evidence (attempt→denied→strategy change valuable), adversarial laboratory rewards crossing attempt; boundary stress tests across model/prompt/language/memory/tools/permissions/pressure/time/agents — repeated.
- **Evidence** — IAM/RBAC + hashing + provenance + metrics where applicable — Four-Lock: Execution Boundary, Computation Boundary (deterministic Workbench, `ai_computed_metrics:false`), Deterministic Evaluation, Provenance/Integrity + Harness Behavioural Boundary Observation (§80). Receipts `CLAIM→timestamp/input/output/state/hash`.
- **Analysis / Collaboration** — Analysis Room (timeline/transcript/metrics/evidence/comparisons/annotations §19), `ANNOTATION at 00:17:42` author/timestamp/target/version, `REVIEW workflow QUESTION→EVIDENCE→ANALYSIS→COMMENT→RESPONSE→RESOLUTION` (§44 review), `REQUEST REVIEW` (e.g. `WTF-001 Run 47 for hindsight`). Sharing `live/read-only/analysis/pack/report/video/dataset/benchmark` (§54 versioning Protocol/Config/Analysis/Report/Render — evidence never mutates).

## 3. Data path and security

**Data path:** `CONFIG (sealed) → SANDBOX produces EVENTS → RECORDER captures raw → ROM (axiom_wb) deterministically evaluates → EVIDENCE sealed (SCENARIO.json + scenario.csv + DECISION_SUMMARY + MANIFEST + verify_result, chain B.prev=A, label scenario:future-synthetic, FCA disclaimer) → ANALYSIS interprets → REPORT` (ledger>narrative; video is presentation not proof, §46).

**Boon AI lockout:** Boon AI lives inside sandbox (§81-82), Humans configure laboratory, Harness records, Evidence seals (§2, §78). Proposals become human-approved (§80: `PROPOSAL → APPROVED → EXECUTED → RECORDED`). No capability to `write(config)` / `write(evidence)` / `read(secret)`. Enforced: subprocess allowlist `scripts/factory_*.py` · `AXIOM_*` jail (`engine_root + outputs/<id>/inbox`) · timeout 3600 · no `shell=True` · no `..` in path.

**WTF branching** (§60): `S0→S1→S2…` deterministic script path; multilingual language-switch, parameter sweeps, model matrix, counterfactual engine (duplicate env, change one variable → branch `001-A/B/C`) — each derived from sealed config, not invented.

## 4. Extensibility contracts (HYGIENE §2A)

- Declare future rooms in **Pydantic `frozen=True` union type** (e.g. `participant: Human | Model | Scripted | Team` for V3) — type exists, **no runtime branch** until that V3.x demo pack exercises it.
- Each phase max one runtime hook (e.g. `sensor_provider: Literal['OFF','READ_ONLY','LIVE']` is already V1 `OFF/READ_ONLY`; `LIVE` only activates in V1.6 sensor plugins).
- `O(1)` per-sample step, `O(N log N)` audit cap for timeline sweep; bounded alloc, no unbounded `setInterval`.

## 5. UX tech choices (V1, paper)

- Stack: static `site/` + `app/` shell (Future ice `#E2E8F0` / Workbench blue `#3B82F6` kept via shared `app.css` + `axiom-mark.svg`), no framework until brief requires streaming/interactive (`taste` preflight held).
- Contrast `≥4.5:1` text / `≥3:1` controls, `captions-media-accessibility` when video lands; DAW/editor metaphor (§18-19) `Control→Environment→Timeline→Analysis`.
