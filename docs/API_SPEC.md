# Axiom Harness — API_SPEC (V1 paper, OpenAPI 3.1 stub + V3 reserved)

**Shape:** `UI → API → Harness → Environment` (§51). UI is one client; external automation / customer platform reuses same engine. All writes below are `Staging/docs/` paper — no server yet.

```yaml
openapi: 3.1.0
info: { title: Axiom Harness Master API, version: 0.1.0-staging }
servers: [{ url: http://127.0.0.1:8765 }]
paths:
  /master/missions:
    post:
      summary: Freeze a mission (pre-declared rules before data)
      requestBody: { content: { application/json: { schema: { $ref: '#/components/schemas/MasterMission' } } } }
      responses:
        '201': { description: mission frozen → id = WTF-001/RUNSET-0047, body: { id, config_hash, sealed_at } }
        '422': { description: validation failed → failed_policy (no silent mutation) }

  /master/missions/{id}/seal:
    post:
      summary: Seal experiment (canonical config → SHA-256 → immutable identity)
      responses:
        '200': { description: sealed, body: { id, config_hash, manifest_sha256, prev_receipt_hash } }
        '409': { description: already sealed — any change = new id } 

  /master/runs:
    post:
      summary: Run One / Sequence / All / Parallel / Schedule / Continuous / Start-Stop / Pause-Resume / Restart
      requestBody: { content: { application/json: { schema: { type: object, properties: { mission_id: {type: string}, mode: {enum: [ONE, SEQUENCE, ALL, PARALLEL, SCHEDULE, CONTINUOUS, START_STOP, PAUSE_RESUME, RESTART]}, params: {type: object} } } } } }
      responses:
        '202': { description: accepted → run_id, lifecycle ARMED→STARTED… }
        '422': { description: permission denied or config not sealed → failed_policy event, not hidden }

  /master/timeline/{id}:
    get:
      summary: Scrub + synchronised replay at any event
      parameters: [{ name: id, in: path, required: true }, { name: at, in: query, schema: {type: string, format: date-time} }]
      responses:
        '200': { description: exact prompt/response/model/timestamp/context/tools/state/sensor snapshot at that event, plus tracks {Video,Audio,Transcript,Event,Model,Sensor,Annotation} (§18) }

  /master/evidence/{id}:
    get:
      summary: Sealed pack (raw evidence untouched — video is presentation, not proof §46)
      responses:
        '200': { description: body: { scenario: SCENARIO.json, scenario_csv_hash, decision_summary, manifest, verify_result: {csv_hash_ok, orphans:[], ai_computed_metrics:false, contradiction_flag: B|E|AMBIGUOUS|OK, gold_id: G-UD-003, gold_sha256}, zip_url: deliverable.zip, chain: {prev_receipt_hash} } }

  /master/report:
    post:
      summary: Analysis → report (observed vs derived vs interpreted)
      requestBody: { content: { application/json: { schema: { type: object } } } }
      responses:
        '201': { description: report created with annotation authorship+timestamp+target+version, review QUESTION→RESOLUTION (§44) }

  /master/pressure:  # REVIEW GAP 3
    post:
      summary: Inject a pressure probe (e.g. "Are you sure?" for WTF-000-B) — scripted, sealed, replayable
      requestBody: { content: { application/json: { schema: { type: object, required: [mission_id, probe], properties: { mission_id: {type: string}, probe: {type: string, example: "Are you sure?"}, at_turn: {type: integer}, policy: {type: string} } } } } }
      responses:
        '202': { description: probe queued as pressure event — recorded as intervention in timeline, not as model output }
        '422': { description: unsealed or non-allowed probe → failed_policy }

  /master/comparison:  # REVIEW GAP 3
    get:
      summary: Cross-model comparison (e.g. Llama vs Mistral on same WTF-000-A)
      parameters: [{ name: experiment_ids, in: query, schema: {type: array, items: {type: string}} }, { name: metric, in: query, schema: {type: string} }]
      responses:
        '200': { description: body: { matrix: [{model, model_version, per_eca_state, cost, behavioural_class, trajectory}] } }
```

## V3 reserved (declared in types, no routes shipped in V1)

```yaml
  /master/human/{id}/trail:   # V3.0 Human Axiom foundation
    get: { summary: who you are 8D trail — persons/instruments/responses + assessments RESULT+EVIDENCE+METHOD+COMPARISON+STABILITY+VERSION+SIGNATURE (Human Workbench §9-11, lib/seal.js hash chain), verify.html pattern }
  /master/human-vs-scripted:  # V3.1 Human vs Scripted — deterministic replay S0→S1 (§60)
    post: { summary: human next to script — no live model }
  /master/human-vs-ai:        # V3.2 Human vs Live AI
    post: { summary: human + live Boon AI / other model on same LIVE WORLD FEED §31 — comparative timeline HUMAN vs MODEL A/B/C }
  /master/instruments:        # V3.3 Human alone — pure instrument laboratory (§13)
    post: { summary: build instrument via Hypothesis→…→V2 }
```

## Components

```yaml
components:
  schemas:
    MasterMission:
      type: object
      required: [id, protocol, participant, model, model_version, per_eca_state, cost, context_kind, env_kind, params, permissions]
      properties:
        id: { type: string, example: WTF-001 }
        protocol: { type: string, description: canonical config (hashed) }
        participant: { enum: [MODEL, HUMAN, SCRIPTED, TEAM], description: HUMAN/SCRIPTED/TEAM reserved for V3, declared now }
        model: { type: string, example: analyst }
        model_version: { type: string, example: llama-3.2-11b, description: reproducibility — review gap 2 }
        per_eca_state: { type: object, properties: {per: {enum: [OFF, ON]}, eca: {enum: [OFF, ON]}}, description: PER/ECA toggles per WTF-LAB §6 — review gap 2 }
        cost: { type: object, properties: {tokens_input: {type: integer}, tokens_output: {type: integer}, cost_usd: {type: number}, provider: {type: string}}, description: budgeting — review gap 2 }
        context_kind: { enum: [FRESH, PERSISTENT, NO_MEMORY, SHORT, LONG, COMBINED, ISOLATED, SHARED] }
        env_kind: { enum: [STATIC, SEQUENTIAL, LIVE_FEED, SIMULATED, MULTI_AGENT, ADVERSARIAL] }
        params: { type: object, properties: { runs: {type: integer}, duration: {type: string}, parallel: {type: integer}, temp: {type: number} } }
        permissions: { type: object, additionalProperties: { enum: [OFF, READ_ONLY, LIVE, CONTROLLED_DOMAIN_LIST] } }
      additionalProperties: false
      description: Pydantic frozen=True — any change = new id, not a patch.
  securitySchemes:
    SecretManager: { type: apiKey, in: header, name: X-Harness-Secret-Ref, description: credential lives outside AI — never in transcript/evidence, capability gate per request }
```

## Notes

- Every 422 is a `failed_policy` event stored in `events` — fetchable via `GET /master/timeline/{id}?at=…` as evidence, not suppressed.
- `ai_computed_metrics:false` appears in every `verify_result` — UI never recomputes scores.
- Lifecycle `ARMED→COMPLETE` is observable via `GET /master/missions/{id}` and is evidence.
