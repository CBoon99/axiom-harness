# Top Lab Systems — Best Practice Research (Online + GitHub)
**Date:** 2026-09-26
**Sources inspected:** bmcs_matmod 10_lims_eln_review.md (Bika/Senaite, OpenLIMS, Chemotion, AiiDA/Airflow), Benchpress (nathanielazevedo/benchpress README+system_design — polyglot modular lab automation), OpenLIMS (Mokey2002/OpenLIMS Medium), LaminDB (lamindb SKILL.md — lakehouse + lineage + FAIR), Scispot, Benchling whitepapers, FAIR Data Principles (LabManager, SciSure, Medium), BioLP-bench

## Synthesis for Axiom Harness — Don't Learn by Mistakes

**Best practice from top labs (copy, don't trial-and-error):**

1. **LIMS for samples/workflows, ELN for notes, Project tool for scheduling — connected via APIs** (bmcs_matmod review). *For Harness:* keep 9 rooms (CONTROL/MODEL/SANDBOX/RUN/LIVE/TIMELINE/EVIDENCE/ANALYSIS/EXPORT) as ELN + LIMS + Scheduler, connect via `POST /api/master/*` REST, not hard-coded calls.

2. **Polyglot modular architecture — physical instrument → ingestion → core API → ELN/LIMS → Dashboard, every step traceable/auditable/open** (Benchpress system_design: "Dashboard · ELN · LIMS · Designer · AI" layers, `sample → instrument run → results linked to notebook entry without leaving app, full audit trail"). *For Harness:* keep `SANDBOX/TERMINAL/TOOLS/DATA/SENSORS → EVENT+TRANSCRIPT+STATE → EVIDENCE LAYER` as ingestion → core API → dashboard same layering.

3. **FAIR + lineage + lakehouse: queryable, traceable, reproducible, findable** (LaminDB: lakehouse + lineage tracking + feature stores + ontologies + LIMS+ELN in one Python API). *For Harness:* keep `MANIFEST WTF-005A-HASH-v3 sort_keys, B.prev=A chain, SHA-256 sealed packet, ledger>narrative, orphan[]` — already FAIR.

4. **Audit trail on every mutation: who did what, when, with timestamp + user + procedural notes** (OpenLIMS, Bika, Benchling, SciSure). *For Harness:* keep `smoke 5/5` (health jail, seal gate, pressure, manifest, orphans+ai_computed_metrics:false) + `sealed_by/at/instrument/sop_version` hallmark.

5. **Self-hosted, open-source, RBAC + MFA, ISO 15189/HL7/FHIR where relevant, MIT** (OpenLIMS, BPA). *For Harness:* keep `AXIOM_STRICT_MODE=1` canary + read-only `Path(__file__).parents[1]` + `W_OK` check, ` Lite` vs ` STRICT` env override, `frozen=True` configs.

**Copy these, don't invent:**
- Benchpress: one connected system, not three silos — Harness already does `EXPERIMENT` as one object (§55) with `Identity/Protocol/Config/.../Renders` — keep it.
- Benchpress + LaminDB: metadata lakehouse + lineage > storing blobs in DB (OneDrive/Google Drive links) — Harness already `outputs/<id>/sandbox/<file>` jailed + `MANIFEST` pointers.
- Best practice worst-practice invert: don't store results in chat transcript (evidence-in-pack ≠ evidence-in-request rule §25) — Harness already enforces.

## How Harness already matches & what to bolt next (future-proof)
- Matches: 9 rooms V1.1-V1.8 covered, 114 passed, 8 hardened locks L1-L8, hash-only math `math/*`, browser N=5 headless.
- Bolt next as planned `V1.9 Video` etc as `frozen Optional[RoomConfig]=None` — same modular pattern Benchpress uses for Designer/AI.

> This research was online + GitHub only, not trial-and-error. Copy the architectures, not the mistakes.
