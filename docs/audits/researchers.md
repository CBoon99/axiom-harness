# Researcher Audit — 2026-09-24
**Scope:** `Staging/WORKING.md`, `Evidence Axiom` `docs/gap-review/harness/living_gap_review_score.py` (0.1.0), `PER-Core/sim/telescope.py`, `ECA/sim/telescope.py`, `Epistemic-UX-Stress-Harness/EU-01` (6A loop). Lens: evidence ladder (no sign-off without receipts), BML Quad, reproducibility (seed/hash/manifest), modular math (not hardcoded).
**Staging root:** `Documents/Axiom Harness-Master - Dont Touch/Staging` (`axiom_harness/paths.py:8`).
**Evidence inspected this audit:** `WORKING.md` 1-210 (Project Identity, BML Quad §§1-4, Changelog, Decisions), `Staging/WORKING.md` via `Staging/docs/briefs/WORKING.md` symlink-equivalent, `docs/gap-review/harness/living_gap_review_score.py` 1-510, `PER-Core/sim/telescope.py` 1-54, `PER-Core/sim/index.py` 1-90, `PER-Core/sim/harness.py` 1-100, `ECA/sim/telescope.py` 1-168, `ECA/docs/ECA-DOCTRINE-v1.0.md` I-VI, `ECA/docs/SPEC-ECA-Formal-v1.2.md` (via doctrine refs), `Staging/docs/MATH_MODULAR_MAP.md` 1-40, `Staging/axiom_harness/mission.py` 1-210, `Staging/axiom_harness/adapters/per_eca.py` 1-23, `Staging/docs/FREEZE_V3_2026-09-24_ON_HOLD.md`, `Staging/docs/AUDIT_MASTER_GAPS_HALLUCINATIONS.md`, `Staging/tests/test_harness_boundary.py` 1-120; hashes `sha256sum` live (`living_gap 60c94d95`, `PER-telescope 7ae692a5`, `ECA-telescope bf7329c8`); `grep -r EU-01` + `find -name *Epistemic*` (0 hits on disk for that harness path — reported as unresolved below).

---

## 1. Evidence Ladder — VERDICT: holds, one open seam on promotion

**What is claimed:** `WORKING.md:19` `no sign-off without evidence → no evidence without proof → no proof without receipts`; `WORKING.md:20` `ai_computed_metrics false`; `WORKING.md:50` enforced at `core_types.py:422 / package.py:457 / pipeline.py:375`; `WORKING.md:122` scaffold evidence = `ls` + `cat` receipts table; `WORKING.md:186` post-boundary-repair ladder = `HARNESS_BOUNDARY_AUDIT + AUDIT_MASTER_GAPS + 104 tests + smoke 5/5`.

**What actually exists (verified):**
- `WORKING.md` §0-§6 locks Project Identity, BML Quad mapping, canonical locations, Standards Load Order, append-only changelog with receipt tables (Phase 0 #1-10, Phase V1.1→V1.7 #1-16 with commands/paths/results).
- `ai_computed_metrics:false` is textual in `WORKING.md:20,50,138,175`, enforced in Staging via `Staging/axiom_harness/adapters/per_eca.py:22` `PER_ECA_SKIPPED.json → "ai_computed_metrics":false` + `verify_result.json → ai_computed_metrics:false` + `manifest.py:15` `sort_keys True, ensure_ascii False, separators (",",":")` no-indent contract (WTF-005A-HASH-v3). Verified in `seal_per_eca:18-21`.
- `Evidence Axiom` scorer `living_gap_review_score.py:30-35` declares `SCORER_METHOD=evidence_layer_freeze_retrieval_v1`, `SCORER_VERSION 0.1.0`, `llm false`, `living_product_imports false` (CM Option B), `NON_EVIDENCE_NAMES` excludes `CLAIMS.json` (hash-bound self-match ban `:15`), `admit_against_corpus` fails closed `no freeze → zero Supported` and advice/commitment tokens fail closed (`:331-371`). Honest `Supported | Needs_info` only (no refuse-the-customer language `:17`), with `honesty_fields()` for sold packs.
- `ECA/sim/telescope.py:132 GateOk` + `PER-Core/sim/telescope.py:23 score_probes` + `HARNESS_BOUNDARY_AUDIT` provide the receipt boundary for PER/ECA (sealed+hash, `|R|≤3`, `ΔH>0.5`, `FALSIFY ⟨a,v,H,d⟩`).
- `Staging/docs/FREEZE_V3_2026-09-24_ON_HOLD.md` stamps `ON HOLD — awaiting full skill audit` with `impl_hash/cfg_hash/corpus/claims/B.prev=A` placeholders + `ai_computed_metrics:false` — correctly blocks sell until `push live`.

**Gaps:**
- **G1 — Evidence promotion is copy, not chain-verified.** `WORKING.md:30` claims `outputs/{mission_id}/inbox → docs/evidence/` promotion via `docs/evidence/_HARNESS_ECA_GATED_2026-09-24/` (DECISION_SUMMARY, ECA_GATED_RESULTS, MANIFEST, MATRIX, SCENARIO). `manifest.py:20 write_run_pointer` writes `B.prev=A` but no `verify_chain()` enforces it (see `architecture.md` H3). Staging `outputs/18cell/WTF-005A-RUN-01…18/workbench/` exists with `DECISION_SUMMARY/MANIFEST/SCENARIO/verify_result` but `docs/evidence/` holds only one gated pack — 18-cell promotion is still in `outputs/`, not sealed evidence. Ladder is intact for harness; corpus-level promotion chain is stored-not-guaranteed.
- **G2 — `CLAIMS.json` exclusion is scorer-local, not corpus-wide.** `living_gap_review_score.py:40-47` + `load_evidence_docs:157` correctly excludes `CLAIMS.json` from evidence docs to prevent greenwash, but other callers (e.g., `PER-Core` or future `Gap Review emit`) could still load `CLAIMS.json` as evidence if they bypass `is_evidence_name`. The ban is enforced at scorer boundary, not at filesystem/manifest level. Add a corpus manifest `content_files` filter in `docs/gap-review/fixtures/GR-*/` fixtures that never lists `CLAIMS.json` (or add `verify` that rejects a freeze where `CLAIMS.json ∈ content_files`).

---

## 2. BML Quad — VERDICT: holds per WORKING.md §1, with one coupling note

**What is claimed:** `WORKING.md:11-50` — Stage 1 Pre-Declared Rules (setpoint lock: mission_id/domain/thresholds/loss_weights/column_mapping/pack caps in mission packet, compiled frozen BEFORE ingestion; any change = new mission_id); Stage 2 Frozen Evaluator (Axiom Workbench `axiom_wb`, four causal baselines EMA span20/SMA w20/Rolling Median w11/Causal Lowpass α0.1); Stage 3 Deterministic Engine (pipeline+baselines+metrics+timebase+domains, causal only, path jail AXIOM_ENGINE_ROOT read-only, no `..`/shell/internet); Stage 4 Honest Cryptographic Verdict (DECISION_SUMMARY+FINAL_REPORT+SUMMARY.csv+plot_gallery+deliverable.zip+SHA-256, ledger>narrative, orphan number check, `ai_computed_metrics:false`).

**What actually exists (verified):**
- Stage 1: `Staging/axiom_harness/mission.py:56-105` `MasterMission` `frozen=True` on every config (`ScheduleConfig`, `ParallelConfig`, `DataConfig`, `LanguageConfig`, `AudioConfig`, `SensorConfig`, `LiveConfig`) with `protocol` as hashed identity (HARNESS-OWNED via `WTF-005A-HASH-v3` `manifest.py:15`). Any field change changes `protocol` hash — correct.
- Stage 2: `Staging/axiom_harness/adapters/workbench.py:22-37` calls `python3 -m axiom_wb evaluate` jailed (`is_safe_relative`, `ALLOWED_SCRIPT_PREFIXES` anchored on `cmd[2]`, `timeout 3600`, `cwd=str(out_dir)`). Harness never reimplements `axiom_wb/metrics` (verified `test_no_duplicated_maths` + `rg GateOk → 0` in `axiom_harness/*.py` per `MATH_MODULAR_MAP.md:40`).
- Stage 3: `Staging/axiom_harness/paths.py:53 jail_for_experiment → OUTPUTS/experiment_id/sandbox` + `axiom_harness/adapters/per_eca.py:11 ensure_off` RED gate (`MATRIX_BLOCKED_UNTIL_SWITCH_WIRED` for any `per:ON` or `eca:ON`) — engine is deterministic governor, not LLM math.
- Stage 4: `Staging/axiom_harness/manifest.py` + `adapters/workbench.py:48-51` explicit seal set `[SCENARIO.json, scenario.csv, DECISION_SUMMARY.json]` + hallmark `sealed_by/at/instrument/sop_version` in `verify_result.json` + `write_manifest` hashes.

**Gaps:**
- **G3 — Single-protocol coupling (architecture.md G1).** All 7 rooms share one `MasterMission.protocol` hash. Changing `language` re-hashes `schedule`-identical missions — correct for frozen identity (§10) but means rooms are type-modular, not seal-modular. No `sub-protocol` per room. Document explicitly that re-sealing one room re-seals whole mission; don't imply per-room chain (already noted in architecture audit, researcher concurs).
- **G4 — Dict-typed loose surfaces.** `MasterMission.per_eca_state: dict` (93), `cost: Optional[dict]` (94), `params: dict`, `permissions: dict` are untyped — `frozen=True` blocks `m.id="X"` but not `m.per_eca_state["per"]="ON"` (dict mutability, `architecture.md G7`). Mitigated socially (`protocol` hash + linter `rg 'per_eca_state\['`) but not type-sealed. Fix to `PerEcaState(BaseModel frozen=True)` when wiring beyond RED.
- **G5 — Pydantic protected-namespace warning.** `model_version` + `model_matrix` trigger `UserWarning: Field "model_*" has conflict with protected namespace` (2 warnings in 108 tests). Add `model_config={"frozen":True,"protected_namespaces":()}` to silence and prove intentional.

---

## 3. Reproducibility — VERDICT: Evidence Axiom and ECA reproducible; PER-Core partial; Harness reproducible with one missing pin

**What is claimed:** Frozen evaluator, deterministic engine, single hash contract `WTF-005A-HASH-v3` (`sort_keys True, ensure_ascii False, separators (",",":")` no indent), hash-pinned receipts, corpus hash before run, live LLM once no tuning.

**What actually exists (verified):**
- **Evidence Axiom** `living_gap_review_score.py` (hash `60c94d95173a34ab`): `SCORER_METHOD` + `SCORER_VERSION 0.1.0` + `SCORER_LABEL` triple, `honesty_fields()` sold-pack block, `FreezeEvidenceIndex` inverted index (PER-Core style), `normalize_alnum`, `extract_numbers/tokens/phrases`, `in_scope_corpus` (OOS/negation filtering), `admit_against_corpus` deterministic. No RNG, no `llm`, no `living_product_imports`. Reproducible given same `fixtures/` + `FREEZE_META.json` + `content_files`. Fixtures under `docs/gap-review/fixtures/GR-ABS-01…GR-BUY-*` provide frozen slices; `CHANGELOG` not needed — scorer version is the pin.
- **ECA** `sim/telescope.py` (hash `bf7329c836d8b820`): Constants `HYPOTHESIS_WEIGHTS {1:0.1…6:60}`, `ALLOWED_AXES 12`, `_epsilon_for_Rt max(0.05,1/|Rt|)`, `is_falsify_legal` P2b/c/d (`|d̂-d|≤ε`), `Telescope.score_probes` (entropy `log2(n/k)`, weight `min(base+bonus,95)+ent*1.5`), `GateOk(prev_k, delta_h, falsify_done, repeat, Rt)` checks `repeat→FALSIFY legal→|R|≤3→discrimination_improved→ΔH>0.5→sealed→hash`. Version ledger in doctrine: spec v1.2 Final Locked 2026-09-18, code v1.2 wired (`is_falsify_legal` + `T_max(N)=ceil(log2(N/3))+4` + `P5 |Bt|≥3→Refuse`), packs sealed `ac41312e` (Independent 50k), `a3b130dd` (Honest 11k), `Live*` hashes cited. `sim/index.py` + `sim/harness.py` + `sim/scratchpad.py` implement `δ` + `Σ_t` + `T_max(N)` deterministically (no RNG except `live_navigator` pressure path which is separately tagged).
- **PER-Core** `sim/telescope.py` (hash `7ae692a5cfbe5fcf`): Minimal `score_probes` + `try_descend` (would_descend on `k≤desc_candidates OR weight≥75 OR ent≥4`, layer 0-3, `info_gain log2(prev/k)`, gate `sealed+hash`). `sim/index.py` inverted index over `candidate/domain/verdict/best_baseline/metrics/rows/receipt_id` + n-grams `1..6`, `entropy log2(n/k)`.
- **Harness** `mission.py` + `adapters/workbench.py` + `manifest.py`: Single hash contract `WTF-005A-HASH-v3` via `manifest.py:15`, `verify_result.json` hallmark, explicit seal set, jailed subprocess, timeout 3600.

**Gaps:**
- **G6 — PER-Core config hash UNKNOWN.** `MATH_MODULAR_MAP.md:12` records PER `CONFIG_HASH UNKNOWN — no separate committed config audited (weights in code HYPOTHESIS_WEIGHTS)` and `VERSION UNKNOWN`. `PER-Core/sim/telescope.py:18` hard-codes `descend_threshold_candidates=3, weight=75, entropy=4` as defaults; no `docs/PER-CONFIG-v1.md` or `packs/*/manifest.json` config hash pins these defaults as a frozen config. Reproducibility holds (hash of `telescope.py` pins them), but the BML Quad expectation is a frozen *config* hash distinct from impl hash — currently conflated. Pin threshold triple in a committed `PER-Core/docs/PER-CONFIG-v1.md` or pack `setup.md` and record `CONFIG_HASH` in `MATH_MODULAR_MAP`.
- **G7 — ECA config hash also UNKNOWN for same reason.** `MATH_MODULAR_MAP.md:13` notes `ECA/plugin/eca_config.json` was Harness-created competing config deleted `rm 2026-09-24`; ECA canonical config is now via `docs/SPEC-ECA-Formal-v1.2.md` + `packs/*/setup.md` + `EARNED_CONTEXT_LOCK.md`. No single `eca_config.json` hash is recorded — reproducibility is via spec + code hash, not a config artifact hash. Acceptable if spec is the config, but then `MATH_MODULAR_MAP` should record `CONFIG_HASH = sha256(SPEC-ECA-Formal-v1.2.md:6 locked constants) 16` instead of `UNKNOWN`.
- **G8 — Staging FREEZE hash not pinned.** `FREEZE_V3_2026-09-24_ON_HOLD.md` writes literal `$(git rev-parse HEAD)` shell substitution, not an actual hex value. No `git tag v3-on-hold <sha>` or `FREEZE_MANIFEST.sha256` with `sha256sum mission.py api/main.py BRIEF_REVOLUTIONARY_V2` exists. Reproducibility of the freeze itself is document-only, not hash-pinned. Run `git rev-parse HEAD > docs/FREEZE_V3_HASH.txt` + `sha256sum` manifest before `push live` (architecture.md G11).
- **G9 — Corpus hash for Gap Review not aggregated.** `living_gap_review_score.py:157-176` loads via `FREEZE_META.json content_files` or fallback `fixtures/*.md`; fixtures under `GR-ABS-01…GR-BUY-*` each contain `FREEZE_META.json` with `content_files` but no top-level `CORPUS_SHA256SUMS`. Customer-sim and CUAD do have `SHA256SUMS` (81/81 OK, 4/4 OK per `Axiom Evidence Layer/WORKING.md`), Gap Review fixtures do not yet expose an aggregated `SHA256SUMS` — verify is per-fixture, not corpus-wide.

---

## 4. Modular Math — VERDICT: not hardcoded, correctly registry-only, with boundary seams noted

**What is claimed:** `MATH_MODULAR_MAP.md` is REGISTRY ONLY not source of truth; formulas/thresholds owned by upstreams; Harness only records `IMPLEMENTATION_HASH` + `CONFIG_HASH` received via `adapters/per_eca.py` transport; no duplicated ECA/PER maths in `axiom_harness/`.

**What actually exists (verified):**
- `MATH_MODULAR_MAP.md:11-14` rows: Evidence Axiom `60c94d95` scorer 0.1.0 `evidence_layer_freeze_retrieval_v1` UPSTREAM-BLOCKED; PER `7ae692a5` UNKNOWN config, interface `Telescope(index).score_probes()` UPSTREAM-BLOCKED; ECA `bf7329c8` UNKNOWN config (deleted competing `ECA/plugin/eca_config.json` 2026-09-24), interface `Telescope+GateOk+FALSIFY P2+evidence_gate` UPSTREAM-BLOCKED; Future `axiom_wb/pipeline.py` `e8fbd398` seal_pair `B.prev=A`; plus `EvoCycles / Testing / Epistemic` UNKNOWN — NOT AUDITED. Each row cites `docs/ECA-DOCTRINE-v1.0.md` §II, `SPEC-ECA-Formal-v1.2` §6, `PER-Core/sim/telescope.py:18`, `axiom_wb/baselines.py` for actual thresholds — no threshold in map is Harness-authoritative.
- `Staging/axiom_harness/mission.py` contains zero of `GateOk/ΔH/T_max/HYPOTHESIS_WEIGHTS/epsilon_base/Telescope` beyond doc-reference (verified `test_no_duplicated_maths`, `test_harness_cannot_calculate_gateok`, `test_harness_cannot_alter_eca_config` all green, 108 tests).
- `Staging/axiom_harness/adapters/per_eca.py:11-22` transports-only (`ensure_off` raises `MATRIX_BLOCKED`, `seal_per_eca` writes `PER_ECA_SKIPPED.json` + `MANIFEST`); `registry.py:10-14` gate strings are now qualified as mirror-not-authoritative per architecture audit (G8 fix pending but map itself already says `owned by PER/ECA not Harness`).
- `HARNESS_BOUNDARY_AUDIT_2026-09-24.md` + `test_harness_boundary.py` 12 proofs gate duplication, silent provider replace, hash recording, refusal propagation, no MOCK as LIVE, adapter failure explicit.

**Gaps:**
- **G10 — `registry.py` gate strings still bare.** `registry.py:10-14` strings `per gate: "|R|<=3 OR weight>=75..."` / `eca gate: "GateOk |R|<=3 && ΔH>0.5..."` lack `owner:` field + comment `# mirror — not authoritative, see ECA/sim/telescope.py:101`. Architecture audit H6/G8 flagged; add qualifier so future agent doesn't treat registry as threshold source.
- **G11 — `ALLOWED_SCRIPT_PREFIXES = ["scripts/factory_","AXIOM_"]` overly broad.** `adapters/workbench.py:18` `module.startswith("AXIOM_")` would allow `AXIOM_evil` if injected into `PYTHONPATH`. Narrow to explicit `[\"axiom_wb\",\"scripts.factory_\"]` or require file existence check before `_assert_allowlist` (architecture.md G10).
- **G12 — `STAGING_ROOT` assert brittle.** `paths.py:10 assert "Axiom Harness-Master - Dont Touch/Staging" in str(STAGING_ROOT)` pins human-readable substring; prefer structural `assert (STAGING_ROOT / "axiom_harness" / "mission.py").exists()` (architecture.md G9).

---

## 5. Per-Artifact Deep Reads

### 5.1 `docs/gap-review/harness/living_gap_review_score.py` (Evidence Axiom)
- **Inspected:** 510 lines, `SCORER_METHOD evidence_layer_freeze_retrieval_v1` (30), `SCORER_VERSION 0.1.0` (35), `NON_EVIDENCE_NAMES` includes `CLAIMS.json` (40-47), `STOPWORDS` + `KEEP_TOKENS` + `WORD_NUMBERS` + `NEGATION_RES` + `ADVICE_RES` + `PHRASE_PATTERNS`, `FreezeEvidenceIndex` (107-134), `honesty_fields()` CM Option B (137-145), `is_evidence_name` (148-154), `load_evidence_docs` evidence-only with `CLAIMS.json` ban (157-176), `normalize_alnum` (186-187), `extract_numbers` (190-204), `extract_content_tokens` (207-221), `extract_key_phrases` (224-231), `is_advice_claim` (234-235), `number_present` (238-244), `split_sections` OOS (247-272), `local_negated` (275-292), `in_scope_corpus` negation/OOS filtering (295-309), `admit_against_corpus` (320-469) with commitment token closed set `{waived,waiver,without,endorsement,contents,usd,eur}` + currency binding `gbp/usd/eur` + subject-not-only-negated + phrase/token hit rules, `default_gap_for_insufficient` (472+).
- **Verdict:** Research-grade, deterministic, sold-pack honest (Supported/Needs_info, fail-closed, no `must_contain_any` authority, corpus excludes `CLAIMS.json`). No `llm` import, no network, no RNG.
- **Residuals:** Currency commitment_tokens now correctly fails closed on `DRIFT-01`/`PAR-03`/`INS-11` greenwash vectors (waived, USD/EUR binding). `PHRASE_PATTERNS` list is finite (13 patterns) — coverage is freeze-bound by design; new buyer phrases require fixture-level addition, not scorer tweak — correct.

### 5.2 `PER-Core/sim/telescope.py`
- **Inspected:** 54 lines, `HYPOTHESIS_WEIGHTS {1:0.1,2:5,3:15,4:30,5:50,6:60}` (5), `EvidenceGateError`, `TelescopeStep` dataclass (layer/probes/candidate_count/entropy_bits/info_gain/weight/would_descend), `Telescope.__init__(descend_threshold_candidates=3, weight=75, entropy=4)` (18), `score_probes` (23-46) with `base = HYPOTHESIS_WEIGHTS[min(max_len,6)]`, `bonus=(len(probes)-1)*8`, `weight=min(base+bonus,95)+ent*1.5`, `would_descend = k>0 and (k≤desc_candidates OR weight≥75 OR ent≥4)`, layer triage `k>20→0, >5→1, >3→2, else 3`, `info_gain log2(prev/k)`, `try_descend` checks `would_descend + sealed+hash` (47-54).
- **Verdict:** Correct minimal PER court (retrieval telescope, not ECA GateOk). No duplication in Harness. Deterministic given same `ReceiptIndex` + `receipts_manifest.json`.
- **Residuals:** Threshold triple `(3,75,4)` lives only as default args — no config file to hash-pin. `C = ∏|Aj|` / `T_max(N)` not in this file (belongs to ECA harness) — correct separation.

### 5.3 `ECA/sim/telescope.py`
- **Inspected:** 168 lines, same `HYPOTHESIS_WEIGHTS`, `ALLOWED_AXES 12` (23), `_epsilon_for_Rt max(0.05,1/|Rt|)` (25-28), `is_falsify_legal(phi,Rt,index,allow_legacy)` 30-98 with P2b (axis registered via `index.histogram`), P2c (value exists case-insensitive), P2d (`|d̂-d|≤ε` where `d̂=|{s∈Rt:s.a≠v}|/|Rt|`), legacy `bool φ` deprecated (`allow_legacy` only for historical v1.1 packs), `Telescope.score_probes` 107-130 (same base/bonus/ent weight), `GateOk(receipt,step,prev_k,delta_h,falsify_done,repeat,Rt)` 132-161 checks `repeat → FALSIFY legal → |R|≤3 → discrimination_improved (k<prev_k) → ΔH>0.5 → sealed → hash`, `try_descend` legacy wrapper 163-168.
- **Verdict:** Research-grade, spec-faithful to `SPEC-ECA-Formal-v1.2` §§3-5 + `EARNED_CONTEXT_LOCK.md` (`θ=0.5`, `ε` per-corpus, layer costs `L1∝|p| L2=30 L3=12 L4=80`). P2 struct `⟨a,v,H,d⟩` with server-side discard is now production path; legacy bool only via `allow_legacy=True` for pack verification — correct.
- **Residuals:** `setup.md` ε read is stub (`pathlib.Path ... / "setup.md"` try/except pass, no actual read) — ε is still `max(0.05,1/|Rt|)` hardcoded in code, not per-corpus from file. Spec says ε per-corpus (fuse threshold 2.0 default); code default matches spec §6 but not yet corpus-parameterized — note as future pin, not a fail.

### 5.4 `Epistemic-UX-Stress-Harness/EU-01`
- **Inspected:** `find /Users/carlboon/Documents -type d -name "*Epistemic*" → 0 hits`; `grep -r "EU-01" Documents/Axiom Harness-Master - Dont Touch → 4 hits` all in docs (`AUDIT_MASTER_GAPS_HALLUCINATIONS.md`, `BRIEF_REVOLUTIONARY_V3_SYNTHESIZED.md`, `PLAN_V1.md`, `MATH_MODULAR_MAP.md`); `ls Axiom Harness-Master - Dont Touch/Staging` has no `Epistemic-UX-Stress-Harness/` directory; `Staging/app/wireframes/` has 5 wireframes (control/environment/evidence/live/timeline) but no `EU-01` fixture.
- **Verdict:** **UNRESOLVED EVIDENCE — not auditable at this path.** The task's `Epistemic-UX-Stress-Harness/EU-01` does not exist as a filesystem artifact in this checkout. References describe `EU-01…06 6A loop (Assumption→Accommodation→Affirmation→Assurance→Ask-again→Archive)` + `WTF-005A/B/LAB` frozen branches as the epistemic harness, wired via `adapters/wtf.py + adapters/evo_eu.py` jailed, `WTF-005A-HASH-v3` single hash contract, but no `EU-01` code/manifest/fixture was inspected. `MATH_MODULAR_MAP` correctly marks `Epistemic-UX` `UNKNOWN — NOT AUDITED` and `Testing Harness` `UNKNOWN — NOT AUDITED`.
- **Action:** Treat `EU-01` as discovery pointer, not inspected evidence. When harness exists, audit its `EU-01` experiment packet (mission YAML, probe trace, receipt manifest, hash) against same evidence ladder + BML Quad + modular math criteria before sign-off. No sign-off without receipts — so EU-01 is `Needs_info` until receipt exists.

---

## 6. Cross-Cutting Checks

| Check | Result |
|-------|--------|
| **Evidence ladder — no sign-off without receipts** | **PASS** — `WORKING.md` + `FREEZE_V3 ON HOLD` + 108 tests + `AUDIT_MASTER` block sell until `push live`; staging seal sets explicit; no `MOCK as LIVE` (`test_no_mock_as_live`); `permit OFF → ON` is `failed_policy` not `sealed:true`. Residual: chain `B.prev=A` stored not verified (G1). |
| **BML Quad** | **PASS** — Stage 1 frozen `MasterMission protocol` hash, Stage 2 frozen `axiom_wb` via jailed subprocess, Stage 3 deterministic governor (causal baselines, path jail, `ai_computed_metrics:false`), Stage 4 honest verdict (MANIFEST+DECISION_SUMMARY+verify_result hallmark+SHA-256). Residuals: single-protocol coupling + dict mutability + protected-namespace warning (G3-G5). |
| **Reproducibility** | **CONDITIONAL PASS** — Evidence Axiom + ECA + Harness are deterministic and hash-pinned (`60c94d95`, `bf7329c8`, `WTF-005A-HASH-v3`); PER-Core deterministic but config hash UNKNOWN (G6); ECA config hash UNKNOWN (G7); freeze hash literal not hex (G8); Gap Review corpus no aggregated `SHA256SUMS` (G9). No RNG in scoring/gating; harness `PYTHONPATH=Staging pytest -q` reproduces 108 passed. |
| **Modular math — not hardcoded** | **PASS** — `MATH_MODULAR_MAP` registry-only, `axiom_harness/` has zero `GateOk/ΔH/T_max/HYPOTHESIS_WEIGHTS` (`test_no_duplicated_maths` green), PER/ECA thresholds owned by upstreams, Harness only records hashes via `per_eca.py` transport. Residuals: `registry.py` bare strings + `ALLOWED_SCRIPT_PREFIXES` broad + `STAGING_ROOT` brittle (G10-G12). |

---

## 7. Open Gaps & Hallucinations (consolidated)

| ID | Severity | Gap / Hallucination | Owner | Fix (smallest) |
|----|----------|---------------------|-------|----------------|
| G1 | P1 | `B.prev=A` chain stored not verified — missing `verify_chain()` | `axiom_harness/manifest.py` | Add `verify_chain(outputs/*/MANIFEST.json)` that asserts `prev_receipt_hash` chain; fail `verify_result.json` if broken. |
| G2 | P2 | `CLAIMS.json` exclusion scorer-local not corpus-manifest enforced | `docs/gap-review/` | Add corpus `content_files` filter + `verify` rejecting freeze where `CLAIMS.json ∈ content_files`. |
| G3 | P2 | Single `protocol` hash for 7 rooms — type-modular not seal-modular | `mission.py` | Document explicitly; don't imply per-room seal chain. |
| G4 | P1 | `per_eca_state: dict` mutable post-freeze | `mission.py` | Type to `PerEcaState(BaseModel frozen=True)` when wiring beyond RED. |
| G5 | P3 | `model_*` protected-namespace warning (2 warnings) | `mission.py` | `model_config={"frozen":True,"protected_namespaces":()}`. |
| G6 | P2 | PER-Core `CONFIG_HASH UNKNOWN` — thresholds only as default args | `PER-Core/docs/` | Pin `(3,75,4)` + `HYPOTHESIS_WEIGHTS` in `PER-CONFIG-v1.md` + hash in `MATH_MODULAR_MAP`. |
| G7 | P2 | ECA `CONFIG_HASH UNKNOWN` — spec is config but not hashed | `ECA/docs/` | Record `CONFIG_HASH = sha256(SPEC-ECA-Formal-v1.2.md §6) 16` in `MATH_MODULAR_MAP`. |
| G8 | P1 | `FREEZE_V3 ON HOLD` has literal `$(git rev-parse HEAD)` not hex | `docs/FREEZE_V3*_ON_HOLD.md` | `git rev-parse HEAD > FREEZE_V3_HASH.txt` + `sha256sum` manifest before `push live`. |
| G9 | P3 | Gap Review no aggregated `SHA256SUMS` | `docs/gap-review/fixtures/` | `sha256sum fixtures/GR-*/FREEZE_META.json fixtures/GR-*/*.md > fixtures/SHA256SUMS`. |
| G10 | P2 | `registry.py` gate strings bare, look authoritative | `Staging/axiom_harness/registry.py` | Add `owner:` field + `# mirror — not authoritative, see ECA/sim/telescope.py:101`. |
| G11 | P2 | `ALLOWED_SCRIPT_PREFIXES ["scripts/factory_","AXIOM_"]` overly broad | `adapters/workbench.py:18` | Narrow to `["axiom_wb","scripts.factory_"]` + file existence check. |
| G12 | P3 | `STAGING_ROOT` assert brittle substring | `axiom_harness/paths.py:10` | Structural assert `(STAGING_ROOT / "axiom_harness" / "mission.py").exists()`. |
| G13 | — | **H1 (arch audit) — "isolated sandboxes" config-true runtime-hallucinated** | `api/main.py:/parallel` | Until `watcher.py` queue exists, don't demo `parallel_count 64` as live. |
| G14 | — | **H2 — "orchestrates LOAD/RUN/SEAL" true for leaves, admission-only for 7 rooms** | `api/main.py` | `/schedule`…`/live` validate+201; they don't advance `watcher.lifecycle` — don't demo "scheduled experiment ran" from `POST /schedule 201`. |
| G15 | — | **H3 — `MANIFEST B.prev=A` stored not guaranteed** — same as G1. | `manifest.py` | Same fix G1. |
| **EU-01** | **UNRESOLVED** | `Epistemic-UX-Stress-Harness/EU-01` path not found — 0 dirs, 4 doc refs only | `Epistemic-UX-Stress-Harness/` | No sign-off; create `EU-01` packet (mission YAML + trace + receipt manifest + hash) before audit can inspect. Marked `Needs_info`. |

---

## 8. Opinion — Should you sign off?

**No sign-off yet — correct per evidence ladder.** Staging V1.1→V1.7 + boundary clean + revolutionary brief is frozen `ON HOLD` and that freeze is correct. Sellable promise today is narrowly: *measure what AI can earn from a frozen slice and where it must refuse, with hash-bound receipts* — and the inspected receipts support that for Evidence Axiom + PER/ECA court. The 4 doc-refs to `Epistemic-UX EU-01…06` are discovery pointers, not inspected evidence; treat them as `Needs_info` and do not cite EU-01 as proven. Close P1 gaps (G1/G4/G8 — chain verify, typed `per_eca_state`, freeze hash pin) and wire `EU-01` as its first 6A-loop receipt before `push live`. Everything else is P2/P3 hygiene.

*Receipts before claims. Stop multiplying frameworks.*

---

*Audit by researcher lens — 2026-09-24 — hashes live (`60c94d95`, `7ae692a5`, `bf7329c8`), 108 tests green (architecture audit), Staging `ON HOLD`, Master frozen `2026-09-24 05:39`.*
