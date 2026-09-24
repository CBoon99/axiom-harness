# EXPLAINER — Master Summary (for packs & seal) — updated to b2fca7e 2026-09-24 (was 5c2c234 pass)

**Product:** AXIOM Harness — WTF Experimental Control Centre & AI Observation Platform (BoonMind Labs)
**Tagline:** Humans configure. Harness records. Evidence seals.
**Stack:** HUMAN → HARNESS-CONTROL → EXPERIMENT CONFIG → SEALED ENV → BOON AI/other models → SANDBOX/TERMINAL/TOOLS/DATA/SENSORS → EVENT+TRANSCRIPT+STATE → EVIDENCE LAYER → ANALYSIS → REPORT/REVIEW/EXPORT
**Golden Rule:** AI DOES NOT CONTROL THE LABORATORY — proposal → human approve → harness executes → recorded (engine read-only at Axiom-Workbench/axiom_wb/).
**HEAD:** `b2fca7e` `axiom-harness` main — `108 passed, 2 warnings, smoke 5/5` — `HARNESS_V1_REPRODUCIBLE_PASS` (`docs/HARNESS_V1_FINAL_ACCEPTANCE_2026-09-24.md` authoritative) — see `docs/HANDOFF_2026-09-24_FULL_ACCOUNT.md`. Before `522b4fd` repair was `105/108` path + `outputs/18cell` missing — now generated deterministically.

**V1 (proven, 108/108):** Control + Model/Secret (••••) + Sandbox (terminal `outputs/<id>/sandbox` jailed — `is_safe_relative` iterative unquote, allowlist `scripts/factory_* + AXIOM_*` on `cmd[2]`, `STAGING_ROOT` structure check) + Run (One/Seq/All/Parallel/Pause-Resume/Restart — `ParallelConfig 1..64`) + Live Room + Timeline (scrub+◆+╱╲) + Evidence 5-file seal (SCENARIO.json, scenario.csv, DECISION_SUMMARY, MANIFEST, verify_result) chain B.prev=A `WTF-005A-HASH-v3 sort_keys True ensure_ascii False (",",":")` + 7 rooms V1.1→V1.7 `POST /master/schedule|parallel|data|language|audio|sensors|live 201/422` + Analysis + Export 22-file pack. Zero-bloat: future rooms declared as `frozen=True` unions only. `V1.8 Multi-agent next`.

**V1.1→V2+ (plug-in rooms):** Scheduling → Parallel → Data → Multilingual → Speech/Audio → Sensors → Live feeds+Observatory → Multi-agent → Video timeline → Films (Experiment→Story) → Observatory → External API. Each adds one room without breaking V1 (one `EXPERIMENT` object).

**V3 Human Axiom (phased):** V3.0 foundation (no AI, 8D receipt RESULT+EVIDENCE+METHOD+COMPARISON+STABILITY+VERSION+SIGNATURE, Human Workbench 80 dilemmas), V3.1 Human vs Scripted (S0→S1), V3.2 Human vs Live AI (same LIVE WORLD FEED), V3.3 Human alone, V3.4 Human-AI team (Person×Role×Environment).

**Packs & Seal:** Every run emits MANIFEST (canonical WTF-005A-HASH-v3 sort_keys True ensure_ascii False separators (",",":") no indent, SHA-256 per file), verify_result {csv_hash_ok, orphans:[], ai_computed_metrics:false, engine_present, sealed}, and chain B.prev=A (Future seal). 18-cell WTF matrix (12 primary + 4 prevalence + 2 duplicate T18) driven via public harness `python3 -m axiom_wb`, honest `sealed:false` when engine missing on host, not fake-green. Environment grid is scalable 100s (repeat auto-fill minmax 220px, virtual scroll, NST nested terminals), not 3 fixed windows.

This doc is copied into every sealed pack's `docs/` for reviewer inspection.
