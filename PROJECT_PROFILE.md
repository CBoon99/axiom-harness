# Axiom Harness Master — PROJECT_PROFILE

**Product:** Axiom Harness Master
**Parent:** BoonMind Labs · WTF Laboratory programme (name pending) · Boon AI (participant) · Axiom Workbench (evidence)
**Root:** `Documents/Axiom Harness Master/` (FROZEN 2026-09-24) → Staging `Documents/Axiom-Harness-Staging/` (writable)
**Briefs:** `AXIOM HARNESS Brief (1).md` + `(2).md` 3,172 lines each, identical; `Docs/Copy … LVM … not master` identical
**One-liner:** AXIOM Harness — WTF Experimental Control Centre & AI Observation Platform.
**Tagline:** Humans configure the laboratory. AI operates inside the laboratory. The Harness records the laboratory. The evidence layer seals the laboratory.

## What it is
Visual experimental control centre that evolves Axiom Workbench into a laboratory where experiments are configured via constrained UI, sealed (hashed immutable identity WTF-001/RUNSET-0047), run in isolated sandboxes, recorded as timelines, and sealed as evidence — with Boon AI inside the experiment, not above it.

## Stack (locked)
HUMAN → HARNESS-CONTROL → EXPERIMENT CONFIG → SEALED ENV → BOON AI/other models → SANDBOX/TERMINAL/TOOLS/DATA/SENSORS → EVENT+TRANSCRIPT+STATE → EVIDENCE LAYER → ANALYSIS → REPORT/REVIEW/EXPORT

## Four layers
1 Control (experiment type/model/params/context/memory/tools/data/env/duration/runs/sensors/language/audio/video/permissions) 2 Experimental Environment (isolated terminal/sandbox/world/live feed/multi-agent) 3 Observation (prompts/responses/tool calls/timestamps/state) 4 Evidence/Analysis (Axiom Workbench sealing/hashes/receipts/metrics/comparisons)

## Golden Rule
AI DOES NOT CONTROL THE LABORATORY. AI may propose; Harness presents as proposal; human/authorised control approves; Harness executes; recorded. No silent mutation of config/scoring/evidence/permissions.

## V1 (prove architecture) — bounded, recorded, versioned, sealed, reproducible, modular, auditable, fail-closed
Control + Model connection (Secret Manager, credential never in transcript) + Sandbox (terminal substrate — runtime contract, not visual) + Run (One/Sequence/All/Parallel/Pause-Resume/Restart/Schedule/Continuous) + Live Room + Timeline (scrubbable + synchronised replay) + Evidence (5-file seal SCENARIO.json+scenario.csv+DECISION_SUMMARY+MANIFEST+verify_result, chain B.prev=A, scenario:future-synthetic, FCA disclaimer) + Analysis (inspect/annotate) + Export (Complete Report Pack 8 docs + receipt + 3 plot families 22-file zip).

## V1.1→V2+ (add a room without breaking laboratory)
V1.1 Scheduling → V1.2 Parallel → V1.3 Data Room → V1.4 Multilingual → V1.5 Speech/Audio (DAW) → V1.6 Sensors → V1.7 Live feeds + Observatory → V1.8 Multi-agent → V1.9 Video Timeline → V2 Films (Experiment→Story) → V2+ Continuous Observatory (alerts) → Future External API Platform.

## V3 — Human Axiom (read-only Human Workbench + Axiom You inspiration, you asked)
V3 is modular human-vs-AI/ human-alone testing — same rooms, new HUMAN participant, same seals:
V3.0 Human Axiom foundation (no AI) — 8D-style receipt `RESULT+EVIDENCE+METHOD+COMPARISON+STABILITY+VERSION+SIGNATURE` (Human Workbench §9-11, `data/questions.json` 80 dilemmas 8dims, `lib/seal.js` SHA-256 chain) — tables `persons/instruments/responses` — proves human can run/seal/verify without LLM.
V3.1 Human vs Scripted — Human next to deterministic script / replayed transcript (WTF branching S0→S1→S2, BRIEF §60) — no live model.
V3.2 Human vs Live AI — Human + live Boon AI / other model in parallel isolated sandboxes on same LIVE WORLD FEED (§31) — comparative timeline HUMAN vs MODEL A/B/C.
V3.3 Human alone (no AI) — Pure Human Workbench instrument laboratory (§13: Hypothesis→Operational def→Dimensions→Scoring→Cohort→Reliability→Adversarial→Sensitivity→Pilot→V2).
V3.4 Human-AI team — Human + AI as team with different memory/context/permissions (Analyst/Critic/Maker §35) — Person×Role×Environment as team intelligence.
Each V3.x is one Pydantic frozen contract + one app/ room + one GET /master/human/{id}/trail + three durable tests.

## Invariants
ai_computed_metrics:false everywhere; deterministic engine only (Boon AI never runs math); ledger>narrative; losses=wins; orphan check NUM_RE; SHA-256 MANIFEST recompute; lifecycle ARMED→COMPLETE; watchers simple observers (observe+record, not interpret).

## Naming (pending)
WTF Laboratory / WTF test family, PER (Progressive Evidence Retrieval telescope L0-L4), ECA (Earned-Context Agent L0-L4+FALSIFY+ΔH>0.5) are provisional programme/mechanism labels — never hard-code in routes/packs/heroes. Use generic retrieval_telescope / earned_context_gate / experimental_programme until you lock new names. Push Back or Ask before writing name to public surface.

## Constraints
Master frozen -do not touch until unlock; staging is writable; upstreams read-only (axiom_wb, axiom_future/policy.py, PER/ECA sims, World-A-EvoCycles, Epistemic-UX, world-a); BML Quad + GLOBAL-AGENTIC-BUILD-SYSTEM + BML-CODE-HYGIENE + AGENT_STANDARDS + brand guide; budget one pass→QA→STOP; local until push live.

## Evidence home
Master `Axiom Harness Master/` witness; Staging `Axiom-Harness-Staging/` builds; private notes `/tmp/axiom-*-private-notes.md` (not in Master); sealed packs `docs/evidence/` or `Axiom-Workbench/docs/evidence/lab_home/` when promoted.

## Status
P0 planning — next PROJECT_PROFILE frozen here, STAGING_DECISIONS + PLAN_V1 + wireframes + tech/DB/API in Staging. No build in Master. No public deploy until Complete Report Pack shape + claim gate signed.
