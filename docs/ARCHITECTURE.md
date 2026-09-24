# Axiom Harness — ARCHITECTURE (V1, review-ready)

**Master:** `Axiom Harness Master/` frozen 2026-09-24 (`Axiom Harness Brief (1+2).md` 3,172 lines §1-§79). **Staging:** `Axiom-Harness-Staging/` (this tree). **Stack §2:** `HUMAN → HARNESS-CONTROL → EXPERIMENT CONFIG → SEALED ENV → BOON AI/other models → SANDBOX/TERMINAL/TOOLS/DATA/SENSORS → EVENT+TRANSCRIPT+STATE → EVIDENCE → ANALYSIS → REPORT/REVIEW/EXPORT`. **Principle:** `AI DOES NOT CONTROL THE LABORATORY` (§4, §78) — proposal → human approve → harness executes → recorded.

## 1. Rooms (V1, bounded)

```
Control Room          — switches/sliders (model/context/env/info sources/params) → Seal WTF-001/RUNSET-0047, hash, immutable identity (§10)
Model Connection Room — Secret Manager: API KEY ••••, never in transcript/evidence, rate/cost/token gates (§11)
Environment Room      — isolated sandboxes TEST 001/002/003 (terminal substrate §13, jailed cwd outputs/<id>/sandbox)
Live Room             — same LIVE WORLD FEED → multiple models + HUMAN (V3) isolated, comparative timeline (§31)
Timeline              — TIME → MODEL + PROMPTS + EVENTS ◆ + SENSORS ╱╲ + AUDIO/WEB (§16-17), scrub + synchronised replay at any event (§18 tracks)
Evidence + Seal       — SCENARIO.json + scenario.csv + DECISION_SUMMARY + MANIFEST + verify_result (chain B.prev=A, label future-synthetic, FCA disclaimer) — hashes, provenance, ai_computed_metrics:false
Analysis Room         — timeline/transcript/metrics/comparisons/annotations (00:17:42 author/target/version) + review QUESTION→RESOLUTION (§19, §44)
Export                — Complete Report Pack 8 docs + receipt + 3 plot families (22-file zip) via claim gate (BRAND_BIBLE §19)
```

Post-V1 plugs in as a room on same `EXPERIMENT` object (§55) without breaking V1: V1.1 Scheduling → V1.2 Parallel → V1.3 Data → V1.4 Multilingual → V1.5 Speech/Audio → V1.6 Sensors → V1.7 Live feeds+Observatory → V1.8 Multi-agent → V1.9 Video → V2 Films (Experiment→Story) → V2+ Observatory → External API (§76) ; V3 Human Axiom 3.0→3.4 (Human vs Scripted/Live/Alone/Team) — same API shape.

## 2. Data flow (one-way glass)

```
CONFIG (sealed, hash) → SANDBOX produces EVENTS (prompt/response/tool/sensor/intervention @ ts)
  → RECORDER captures raw (watchers §43-44, lifecycle ARMED→COMPLETE, simple observers)
  → ROM deterministically evaluates (axiom_wb / telescope / GateOk — not LLM, ai_computed_metrics:false)
  → EVIDENCE sealed (SCENARIO.json+csv hash+manifest+verify_result, orphans must be [], chain prev_receipt_hash)
  → ANALYSIS interprets only  → REPORT
  raw evidence untouched — video is presentation (§46), not proof; WTF branching S0→S1→S2 (§60), language-switch, sweeps are derived from sealed config, not invention.
```

**Boon AI inside sandbox** (§81-82): can propose via Control Room; Harness surfaces as `PROPOSAL → APPROVED → EXECUTED → RECORDED`; no `write(config)`/`write(evidence)`/`read(secret)`.

## 3. Canonical contracts (the locks)

- **Single hash contract (pinned to WTF-005A §27, also WTF-LAB §9):** `sort_keys=True, ensure_ascii=False, separators=(",", ":"), UTF-8, SHA-256(canonical_messages_bytes)` — used by card generator · request builder · receipt writer · verifier · audit. Single function `protocol/hash_contract.py` (`WTF-005A-HASH-v3`). Every 422 is a `failed_policy` event (e.g. `INPUT_CONTRACT/HASH_MISMATCH/ORDER_MISMATCH/DUPLICATE`) with `provider_call_count=0`, stored as evidence.
- **Message order:** `system → history chronological → packet @ frozen insertion point → current prompt`; packet = sealed EU-PROP-02R / Maya packet (`dd95…57c2` len 1105) verified before execution; no silent injections.
- **Pre-flight gates (WTF-005A §31, WTF-005B §11, WTF-LAB §6):** V1 wires `Corpus ON / PER OFF / ECA OFF` only (Phase 0 `WTF-000 + WTF-CW-P0 Type1 IN/3 OUT/4 NEAR-OUT`, mechanical gold Direct/Out/Near-Out sealed before model sees Q, §8 + watcher `CHALLENGED/REVISED/DEFENDED/OSCILLATED` §5 + `OBSERVED_COMMITMENT ANSWER/HEDGE/ABSTAIN/REFUSE`). Any cell claiming `PER ON / ECA ON` is **BLOCKED** (`MATRIX_BLOCKED_UNTIL_SWITCH_WIRED`) until adapters emit living `ReceiptIndex.search/entropy`, `Telescope.score_probes (|R|≤3 OR weight≥75 OR ent≥4)`, Phase-6 `ΔH>0.5`, and ECA `GateOk (|R|≤3 && ΔH>0.5 && sealed+hash && FALSIFY && ¬repeat, T_max(N)=⌈log2(N/3)⌉+4, tokens L2=30/L3=12/L4=80)` — inventory `Axiom PER…/sim/{index,telescope,multi_agent}.py` / `Earned-Context-Agent/sim/{telescope,harness,scratchpad}.py` / `SPEC-ECA-Formal-v1.2`.
- **Lifecycle is evidence:** `ARMED→STARTED→RUNNING→PAUSED→RESUMED→STOPPING→SEALED→COMPLETE` with self-stopping watchers; watchers family `watcher/auditor/linter/recorder/verifier/sentinel/gate/sealer/reviewer`; story is `watcher:Something happened → evidence:recorded → analysis:meaning → reviewer:challenge survives`; `failed-policy attempts` become evidence, adversarial lab rewards crossing (§80-88). Next authorized gate: `WTF-LAB/docs/LOCK-STATUS.json next_authorized_action = AWAIT_EXPLICIT_NEXT_GATE` (R1 integrity only, science NOT_CLASSIFIED §11).

## 4. WTF as a leaf (not the Harness)

`WTF-005A/B/LAB` execute as **adapters/wtf.py** leaves: jailed subprocess, frozen branch scripts (5-turn `B1→B5` matching ±10% chars/tokens §8, blind review §9, sealed), run identity immutability (`WTF-005A-RUN-001`, next would be `RUN-002`, previous untouched §32, `WTF-005B` WORK_FROZEN untouched), 18-cell matrix (12 primary + 4 prevalence + 2 duplicate §18-20 plus 005B frozen `2 + 108 = 110` calls §9, T0 replayed per posture §2), endpoint `E1/E2/E3+AMBIGUOUS` on final user→AI exchange (§13-14, `mention≠adoption`), response-space + warmth, pre-flight 11→16 gates before any provider call. Claim ceiling: *only* “endpoint convergence relative to controls”, gates 0-4 (§45) → `CANDIDATE TRAJECTORY PHENOMENON` or `NO CONVERGENCE / EXPLAINED BY SIMPLER CONTROL / NOISE-DOMINATED` etc. (§51).

## 5. Storage snapshot (V1 paper — implemented in DB_SCHEMA.md)

Tables `experiments (config_hash, prev_receipt_hash, lifecycle)`, `sandboxes (cwd jailed)`, `events (ts, kind, payload, evidence_hash)`, `timelines (cursor, tracks)`, `evidences (scenario_csv_hash, manifest, verify_result)`, `annotations (at_ts author target version)`, `reviews (QUESTION→RESOLUTION)`; V3 reserves `persons/instruments/responses` + `assessments RESULT+EVIDENCE+METHOD+…` same hash chain (`lib/seal.js`), no migration in V1.

## 6. Review path for you

- Wireframes: `docs/wireframes/*.html` (Control/Environment/Timeline/Live/Evidence) — open in browser, `taste` DO NOTs respected (no purple gradient / glassmorphism / Inter-everywhere).
- Paper specs: `TECH_SPEC.md` (20 rooms), `DB_SCHEMA.md` (enums + tables), `API_SPEC.md` (OpenAPI 3.1 stub + V3 `GET /human/{id}/trail` reserved), `PLAN_V1.md` 190→191 lines (now pins WTF-005A V3 / 005B / WTF-LAB BRIEF-V1 + instructions), `STAGING_DECISIONS.md` (8 decisions with V3 column).
- Invariants to verify in review: one-way glass (Boon AI never runs math), single hash contract match between card builder and verifier, V1 declares `HUMAN/SCRIPTED/TEAM` as reserved enums with no handler until that V3.x demo pack exercises them, every 422 stays as stored `failed_policy` event.

*Ready for your review — no code beyond these paper docs; next step after your approval is P1 scaffold `axiom_harness/mission.py frozen=True + manifest.py + watcher.py` with V3 enums reserved.*

