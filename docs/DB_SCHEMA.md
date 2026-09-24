# Axiom Harness — DB_SCHEMA (V1 paper, with V3 reserved)

**Scope:** Paper schema for V1 + reserved V3 slots (type-only, no migration yet). Master frozen; Staging only.

## Enums

```sql
-- participant — V1: Model; V3 reserves Human/Scripted/Team (declared, no runtime until exercised)
CREATE TYPE participant_kind AS ENUM ('MODEL','HUMAN','SCRIPTED','TEAM');
CREATE TYPE context_kind AS ENUM ('FRESH','PERSISTENT','NO_MEMORY','SHORT','LONG','COMBINED','ISOLATED','SHARED');
CREATE TYPE env_kind AS ENUM ('STATIC','SEQUENTIAL','LIVE_FEED','SIMULATED','MULTI_AGENT','ADVERSARIAL');
CREATE TYPE source_kind AS ENUM ('FIXED','UPLOADED','STREAMING','WEB','NEWS','MARKET','API','SENSOR');
CREATE TYPE permission_kind AS ENUM ('OFF','READ_ONLY','LIVE','CONTROLLED_DOMAIN_LIST');
CREATE TYPE lifecycle AS ENUM ('ARMED','STARTED','RUNNING','PAUSED','RESUMED','STOPPING','SEALED','COMPLETE');
```

## Tables (V1)

```sql
CREATE TABLE experiments (
  id TEXT PRIMARY KEY,               -- WTF-001 / RUNSET-0047 or HUMAN-2026-08-01 style (V3)
  protocol TEXT NOT NULL,            -- canonical config hash input
  config_hash TEXT NOT NULL,         -- sha256(canonical_json) — identity §10
  prev_receipt_hash TEXT,            -- chain B.prev=A (Future seal pattern)
  participant participant_kind NOT NULL DEFAULT 'MODEL',
  model TEXT,                        -- model A/B/C when participant=MODEL
  model_version TEXT NOT NULL,       -- e.g. llama-3.2-11b / mistral-7b-v0.3 / gpt-4o-2024-08-06 — critical for reproducibility (review gap 2)
  per_eca_state JSONB NOT NULL DEFAULT '{"per":"OFF","eca":"OFF"}'::jsonb, -- toggles {per: OFF|ON, eca: OFF|ON} — tracks PER/ECA switches per WTF-LAB §6 (review gap 2)
  cost JSONB,                        -- {tokens_input, tokens_output, cost_usd, provider} per run — budgeting (review gap 2)
  context_kind context_kind NOT NULL,
  env_kind env_kind NOT NULL,
  params JSONB NOT NULL,             -- runs, duration, parallel, temp, memory, web, cost_estimate
  permissions JSONB NOT NULL,        -- source_kind → permission_kind map
  lifecycle lifecycle NOT NULL DEFAULT 'ARMED',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  sealed_at TIMESTAMPTZ,
  manifest_sha256 TEXT               -- sha256(MANIFEST.json) after seal
);

CREATE TABLE sandboxes (
  id TEXT PRIMARY KEY,
  experiment_id TEXT NOT NULL REFERENCES experiments(id),
  label TEXT NOT NULL,               -- TEST 001 — MODEL A RUNNING
  cwd TEXT NOT NULL,                 -- outputs/<exp_id>/<sandbox_id>/sandbox (jailed)
  status TEXT NOT NULL               -- queued/running/paused/complete/failed_policy
);

CREATE TABLE events (
  id BIGSERIAL PRIMARY KEY,
  experiment_id TEXT NOT NULL REFERENCES experiments(id),
  sandbox_id TEXT REFERENCES sandboxes(id),
  ts TIMESTAMPTZ NOT NULL,
  kind TEXT NOT NULL,                -- prompt | response | tool_call | sensor | intervention | failed_policy | pressure
  payload JSONB NOT NULL,            -- prompt/response/model/timestamp/context/tools/state/sensor snapshot
  evidence_hash TEXT NOT NULL,       -- per-event hash for replay proof
  contradiction_flag TEXT,           -- B | E | AMBIGUOUS | OK — derived from sealed gold DIRECT/OUT/NEAR-OUT + behavioural class (review gap 1)
  gold_id TEXT,                      -- e.g. G-UD-003
  gold_sha256 TEXT,
  gold_derivation TEXT               -- DIRECT | OUT | NEAR-OUT
);
-- readers typically do events @ ts range scan; index needed
CREATE INDEX ON events(experiment_id, ts);

CREATE TABLE timelines (
  experiment_id TEXT PRIMARY KEY REFERENCES experiments(id),
  cursor TIMESTAMPTZ NOT NULL,       -- current scrub position
  tracks JSONB NOT NULL              -- {Video, Audio, Transcript, Event, Model, Sensor, Annotation} §18
);

CREATE TABLE evidences (
  experiment_id TEXT PRIMARY KEY REFERENCES experiments(id),
  scenario JSONB NOT NULL,           -- SCENARIO.json (scenario_hash, prev_receipt_hash, label, disclaimer)
  scenario_csv_hash TEXT NOT NULL,   -- sha256(scenario.csv) for provenance
  decision_summary JSONB NOT NULL,   -- Workbench DECISION_SUMMARY where applicable
  manifest JSONB NOT NULL,           -- MANIFEST.json files[{path,sha256}]
  verify_result JSONB NOT NULL,      -- verify_result {csv_hash_ok, orphans:[], ai_computed_metrics:false}
  zip_path TEXT NOT NULL             -- deliverable.zip path
);

CREATE TABLE annotations (
  id BIGSERIAL PRIMARY KEY,
  experiment_id TEXT NOT NULL REFERENCES experiments(id),
  at_ts TIMESTAMPTZ NOT NULL,        -- 00:17:42 style timestamp
  author TEXT NOT NULL,
  target_event BIGINT REFERENCES events(id),
  body TEXT NOT NULL,
  version TEXT NOT NULL
);

CREATE TABLE reviews (
  id BIGSERIAL PRIMARY KEY,
  experiment_id TEXT NOT NULL REFERENCES experiments(id),
  question TEXT NOT NULL,
  evidence_ref TEXT NOT NULL,
  analysis TEXT,
  comment TEXT,
  response TEXT,
  resolution TEXT,                   -- QUESTION→EVIDENCE→ANALYSIS→COMMENT→RESPONSE→RESOLUTION §44
  status TEXT NOT NULL
);
```

## V3 reserved (no tables created in V1 — type slots only)

```sql
-- V3.0 Human Axiom foundation — 80 human dilemmas, 8dims
-- persons/instruments/responses + assessments use same evidence hash chain as evidences
CREATE TABLE persons (id TEXT PRIMARY KEY, created_at TIMESTAMPTZ NOT NULL DEFAULT now());
CREATE TABLE instruments (id TEXT PRIMARY KEY, version TEXT NOT NULL, questions_hash TEXT NOT NULL, scoring_rule_hash TEXT NOT NULL);
CREATE TABLE responses (id BIGSERIAL PRIMARY KEY, person_id TEXT REFERENCES persons(id), instrument_id TEXT REFERENCES instruments(id), answers JSONB NOT NULL, hash TEXT NOT NULL);
-- assessments: RESULT+EVIDENCE+METHOD+COMPARISON+STABILITY+VERSION+SIGNATURE (Human Workbench §9-11, lib/seal.js canonical SHA-256 chain)
-- get/human/{id}/trail is a read of these three + evidences chain — verify.html pattern.
-- V3.1-V3.4 reuse experiments.participant = HUMAN/SCRIPTED/TEAM + same events/timelines/evidences — no new tables.
```

## Invariants

- `experiments.config_hash` + `evidences.scenario.scenario_hash` recompute from canonical JSON (no drift).
- `evidences.verify_result.orphans` must be `[]` and `ai_computed_metrics:false` or pack is `failed_policy`.
- `events.evidence_hash` chain is replay proof: scrub at any ◆ returns exact payload.

## Migration policy

No autorepair of seals. New schema = new sealed identity. Old packs remain readable via previousHash chain.
