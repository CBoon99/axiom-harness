# STAGING_DECISIONS — V1 rooms + V3 Human Axiom

**Briefs:** `Axiom Harness Master/AXIOM HARNESS Brief (1+2).md` 3,172 lines §1-§79 — one spec. **Staging** `Axiom-Harness-Staging/` is writable; **Master** `Axiom Harness Master/` frozen 2026-09-24 until `push live`.

| # | Decision | Chosen (V1) | Why (§ evidence) | V3 impact (phased) | Rejected |
|---|----------|-------------|------------------|---------------------|----------|
| 1 | Layering | **Rooms + contracts** on one `EXPERIMENT` object (Identity/Protocol/Config/Model/Env/Permissions/Data/Sensors/Timeline/Transcript/Audio/Video/Events/Evidence/Analysis/Reviews/Reports/Renders §55) | §49, §74 `Add a room without breaking laboratory` — V1 proves 9 rooms, each later room plugs in | V3 adds `participant HUMAN/SCRIPTED/TEAM` as a participant enum value on same object — no new object | Monolith |
| 2 | Visual substrate | **Terminal as runtime** (§13, p516) | §13 inspectable/reproducible/replaceable — richer visual later without contract change | V3 human room reuses same terminal transcript view — human answers rendered as transcript events | Hard-coded rich visual V1 |
| 3 | API surface | **UI → API → Harness → Environment** (§51) | Future External API Platform §76 is same engine with external client | `GET /master/human/{id}/trail` is same pattern as `GET /master/evidence/{id}` | UI→hard-coded impl |
| 4 | Secret | **Secret Manager outside AI** `••••` (§11) | Capability without secret; record shows capability existed without leaking | Human Axiom needs no secret — same manager returns `OFF` for human | Key in transcript/env |
| 5 | Bloat | **Pre-declare in types, ship runtime only when exercised** (HYGIENE §2A) + `O(1)` step | §2A ZERO-BLOAT — V1 declares `HUMAN/SCRIPTED/TEAM` as reserved enum values with no handler until V3.x demo pack exercises them | Each V3.x ships one handler + one `Human` nav room + three tests — no speculative branches in V1 | Ship V3 stubs as runtime |
| 6 | Naming | **Generic in code** (`experimental_programme / retrieval_telescope / earned_context_gate`) until you lock new names | You confirmed WTF/PER/ECA rename — code never hard-codes them in routes/packs/heroes | V3 `human_axiom` stays generic until you name Human Human brand | Hard-code `WTF/PER/ECA` |
| 7 | Staging location | **Sibling `Axiom-Harness-Staging/`** until `push live` | Honors `-do not touch` Master | Same — V3 branches stay in Staging worktrees with `isolation:true` | Build in Master |
| 8 | UX affordance | **Rooms as nav + timeline as editor** (§53, §26 `tracks`, §18-19 DAW metaphor) | Researcher answers *What am I running / what does AI see/do / what is sealed / what evidence supports?* | V3 live comparative timeline `HUMAN vs MODEL A/B/C` (§31 same feed, isolated contexts) fits same editor | Engineering dashboard |

**Per decision, paper artefacts now in this folder:** `PLAN_V1.md` 190 lines, `TECH_SPEC.md` (§49 rooms + watchers lifecycle ARMED→COMPLETE), `DB_SCHEMA.md` (participants`, `events`, `EXPERIMENT` chain `prev_receipt_hash` + V3 `persons/instruments/responses` reserved), `API_SPEC.md` (OpenAPI 3.1 stub + V3 `GET /human/{id}/trail` reserved), `wireframes/*.html` 5 files (Control/Environment/Timeline/Live/Evidence — `taste` checked, no purple gradient / glassmorphism / Inter-everywhere).

**Next (still P0):** No code until you approve this decision table. Then P1 scaffold `axiom_harness/mission.py frozen=True` + `manifest.py` + `watcher.py` etc. with V3 enum values reserved but no handler.
