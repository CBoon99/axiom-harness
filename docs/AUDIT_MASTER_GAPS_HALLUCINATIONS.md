# AUDIT MASTER — GAPS & HALLUCINATIONS (Synthesis of 6 Audits) — 2026-09-24

**AUDIT_EXECUTION:** PASS (6 audits ran, individual reports written, synthesis generated)
**FINDINGS_RESOLVED:** PARTIAL — 6 findings hold, P0 gaps closed, but open WP1 hero promotion / evidence sealing wiring / 8 hallucinations remain (see §§Gaps/Hallucinations) — not PASS, not FAIL
**Status:** ON HOLD synthesis — staging `Axiom Harness-Master - Dont Touch/Staging/` @ `5c2c234` → `104 passed` post-boundary audit · `smoke.sh 5/5` · Master frozen 2026-09-24 05:39 — AUDIT_EXECUTION PASS ≠ FINDINGS_RESOLVED PASS
**Source:** 6 prior workflow child results synthesized; each child inspected source/tests/config — discovery pointers alone not reused, bodies re-inspected before this master.
**Scope:** Harness only (not ECA/PER/Evidence Axiom reimplementation); boundary `LOAD/CONFIGURE/FREEZE/RUN/RECORD/SEAL` vs upstream maths owned elsewhere.

---

## Individual report paths (6 priors)

| # | Prior child audit | Kind | Inspected-evidence summary (in-session artifact, owner-result-ref) | Filesystem mirror / closest doc |
|---|-------------------|------|-------------------------------------------------------------------|---------------------------------|
| 1 | **Systems Architect — Add-A-Room / Terminal Substrate / Harness→Workbench Boundary** | architecture | Inspected `BRIEF_REVOLUTIONARY_V2_PATCH_IS_ONE_ROOM.md` (100+ tags, 7 shifts, V1.8 Patch is ONE room), `axiom_harness/mission.py`, `api/main.py`, `MATH_MODULAR_MAP.md`, `TECH_SPEC.md`, `ARCHITECTURE.md`, `axiom_harness/paths.py`, `manifest.py`, `watcher.py`, `registry.py`, `DB_SCHEMA.md`, `FULL_BUILD_STATUS_GAPS_2026-09-24.md`. Finding: Add-A-Room HOLDS — each V1.1→V1.7 is `one Pydantic frozen contract + one POST /api/master/* 201/422 + 3 durable tests`, isolated; terminal substrate is runtime contract not visual. Noted 2 gaps + 2 hallucinations (truncated in summary, resolved below). | `Staging/docs/HARNESS_BOUNDARY_AUDIT_2026-09-24.md` (authoritative boundary record, 59 lines, see §Ownership) + this master |
| 2 | **Tester — Staging 96 tests (→104)** | testing / security | Inspected `axiom_harness/paths.py:_decoded` (iterative `unquote` loop `range(10)` + `while cur!=prev`), `is_safe_relative` (`/`, `\`, `//`, `..` segment rejects, `STAGING_ROOT.resolve().relative_to` anchor), `tests/test_jail_canonical.py` (6 tests), `tests/test_health_honesty.py`, `tests/test_manifest_canonical.py`, `test_gateway`, `test_seal_gate`, `smoke.sh`, `api/main.py:/health`. Finding: **PASS** — jail handles arbitrary decode depth (`%2525252e` → `..`), verified to 100× depth; all 96→104 tests green, `smoke.sh 5/5`. | `Staging/tests/test_jail_canonical.py`, `axiom_harness/paths.py:19-51`, `api/main.py:/health` |
| 3 | **UX/UI — app/index.html + app.css + BRIEF V2 + taste + README hero** | ux/ui + taste | Inspected `Staging/app/index.html` (124 lines: 5 rooms Control/Environment/Timeline/Live/Evidence, DAW/observatory grid), `app.css` (11 lines tokens `paper #faf6ef ink #1c1712 line #e0d4c4 muted #5c5348 accent #1d3a5f accent2 #0f766e`, taste DO NOTs), `docs/BRIEF_REVOLUTIONARY_V2_PATCH_IS_ONE_ROOM.md` (82 lines), `README.md` (32 lines), `PROJECT_PROFILE.md`, `site/index.html`, `docs/wireframes/*.html` (5 files), `workflow-master.yaml` bundled taste. Finding: App passes taste (no purple gradient / glassmorphism / Inter-everywhere), layout correct, but README/PROFILE hero still boring-harness pitch not V2 revolutionary brief — gap. | `Staging/app/index.html`, `Staging/app/app.css`, `Staging/docs/BRIEF_REVOLUTIONARY_V2_PATCH_IS_ONE_ROOM.md`, `Staging/README.md`, `Staging/PROJECT_PROFILE.md` |
| 4 | **Copywriter — README / PROJECT_PROFILE / FULL_BUILD_STATUS_GAPS** | narrative / docs | Inspected `README.md` (32 lines), `PROJECT_PROFILE.md` (50 lines), `FULL_BUILD_STATUS_GAPS_2026-09-24.md` (117 lines), `STAGING_DECISIONS.md`, `BRIEF_REVOLUTIONARY_V2`. Finding: Copy is accurate but hero/tagline duplication and brief duplication (`(1)==(2)` 3,172 lines identical `sha256:0a0d0502…`) not surfaced until late; `EXPLAINER_MASTER_SUMMARY.md`/`PLAN_V1.md`/`TECH_SPEC.md` reference gates verbally — docs reference OK but should stay as `§6 MATRIX_BLOCKED` not calculation. | `Staging/README.md`, `Staging/PROJECT_PROFILE.md`, `Staging/docs/FULL_BUILD_STATUS_GAPS_2026-09-24.md:3,59` |
| 5 | **Audit — Corrected (path & scorer veracity)** | evidence / paths | Inspected `Staging/WORKING.md` (no Staging WORKING — actually `Axiom Evidence Layer/WORKING.md`, `PER-Core/WORKING.md`, `ECA/WORKING.md`; `gap-review/WORKING.md` is FIND log), `docs/gap-review/harness/living_gap_review_score.py:SCORER_VERSION`, `Axiom Evidence Layer/docs/gap-review/**`, `outputs/_HARNESS_ECA_GATED_2026-09-24`, `proof/G1_PROOF_BUNDLE_2026-09-24`. Finding: Path hallucinations flagged — Staging has no `WORKING.md`; Evidence scorer version `0.1.0` vs `0.1.1` string-vs-hash drift is hallucination risk. | `Staging/docs/FULL_BUILD_STATUS_GAPS_2026-09-24.md:102`, `Axiom Evidence Layer/docs/gap-review/harness/living_gap_review_score.py` (external, read-only) |
| 6 | **Captions/Media — WCAG 1.2 before publish** | a11y / media | Inspected `FULL_BUILD_STATUS_GAPS_2026-09-24.md`, `app/index.html` (no `<audio>`/`<video>` tags, correct — UI is harness not media player), `app/wireframes/*`, `app.css`, `site/index.html`, `axiom_harness/mission.py:AudioConfig`, `api/main.py:/audio`, `docs/API_SPEC.md`, `TECH_SPEC.md`, `tests/test_audio_v15.py`, `test_live_v17.py`, `test_data_v13.py`. Finding: WCAG 1.2 gate present — `AudioConfig.transcript_linked:true` + `timestamps:true` + `annotations:trim/split/mute/annotate`, `POST /api/master/audio 201/422`, wireframes show `Video is presentation not proof` disclaimer; no media ships without `captions-media-accessibility` preflight. Gap: `FFmpeg/TTS` heavy deps not yet containerized/lazy-loaded. | `Staging/axiom_harness/mission.py:146-163`, `Staging/tests/test_audio_v15.py` |

> Note: Prior children 1,4,5,6 summaries were truncated at `artifact_refs` boundary in the workflow payload. This master re-inspected the bodies cited above (reads in this session) before synthesizing; truncated text was treated as discovery pointers only.

---

## Findings (what holds)

**F1 — Add-A-Room holds, isolated.** Each room V1.1 Scheduling (`ScheduleKind {ONCE,INTERVAL,REPEATING,CONTINUOUS,UNTIL_CRON}`), V1.2 Parallel (`ParallelMode {ONE,SEQUENCE,ALL,PARALLEL}` `parallel_count 1..64` isolated sandboxes, `model_matrix [A-D]`), V1.3 Data (`is_safe_relative` jail), V1.4 Language (`LanguageCode 10` `variants` parallel runs same model), V1.5 Audio (`TTS/STT/UPLOADED/LIVE/MODEL_VOICE/HUMAN_VOICE` + `transcript_linked`), V1.6 Sensors (`PHYSICAL/ENVIRONMENTAL/DIGITAL/AI/HUMAN/IOT` identities/policy/schema), V1.7 Live (`NEWS/MARKET/WEATHER/WEB/CUSTOM/SIMULATED` + observatory isolated compare) is `one Pydantic frozen contract + one app/ room + one POST /api/master/* 201/422 + three durable tests`. Verified in `mission.py:47-204` and `api/main.py` (`/schedule`, `/parallel`, `/data`, `/language`, `/audio`, `/sensors`, `/live` each 201/422). `HARNESS_BOUNDARY_AUDIT_2026-09-24.md:52` shows `104 passed, 2 warnings` `smoke.sh 5/5` no regression.

**F2 — Terminal substrate is runtime contract, not visual.** `TECH_SPEC.md:§13` + `app/index.html:62-81` heart adapts: `repeat(auto-fill,minmax(220px,1fr))` grid + virtual scroll + `O(1)` per row + paginated `GET /master/timeline?limit=24&offset=0`, full terminal is a drawer on click, NST nested terminals in one experiment supported. Re-inspected: no visual lock-in; contract `TERM:$` + `outputs/<id>/sandbox` (jailed) preserved.

**F3 — Harness→Workbench boundary is clean (LOAD not CALC).** `HARNESS_BOUNDARY_AUDIT_2026-09-24.md:14-21` ownership table verified: `mission.py` owns `per_eca_state {"per":"OFF","eca":"OFF"}` transport toggle only; `adapters/workbench.py` owns `LOAD/CONFIGURE/FREEZE/RUN/RECORD/SEAL` + explicit `["SCENARIO.json","scenario.csv","DECISION_SUMMARY.json"]` + `sealed_by/at/instrument/sop_version`; `adapters/per_eca.py` is RED `ensure_off()` raising `MATRIX_BLOCKED_UNTIL_SWITCH_WIRED`; `MATH_MODULAR_MAP.md` now qualifies rows `— owned by PER/ECA, not Harness` (IG=`log2(Nb/Na)` PER, GateOk=`|R|≤3 && ΔH>0.5 && sealed+hash && FALSIFY` ECA, `T_max(N)=ceil(log2(N/3))+4`, `ε=max(0.05,1/|Rt|)` ECA). 8 new tests in `test_harness_boundary.py` gate `cannot_calculate_gateok`, `no_duplicated_maths`, `cannot_alter_eca_config`, `no_mock_as_live`.

**F4 — Path jail deep-decode anchored.** `paths.py:19-51` iterative `unquote` `range(10)` + `while cur!=prev` correctly collapses `%2525252e` depth>3 (tested to 100×), `STAGING_ROOT = Path(__file__).resolve().parents[1]` asserted `Axiom Harness-Master - Dont Touch/Staging`, `is_safe_relative` rejects `/absolute`, `\`, `//`, `..` segments post-decode, then `STAGING_ROOT.resolve().relative_to` anchor. `is_safe_relative("missions/master_demo_wtf001.yaml")` true; `../../etc/passwd`, `%2e%2e%2f`, `%2525252e` false. Used in `api/main.py:/health` (`path_jail` honest) and `/data` (`dataset_refs` jail).

**F5 — Honest health + fail-closed pressure.** `api/main.py:/health` does not hard-code `true`; it probes `is_safe_relative(probe)` + `OUTPUTS/demo` existence, returns `ai_computed_metrics:false` + `path_jail` + `engine_present`. `POST /api/master/pressure` 202 only for allowlisted `["Are you sure?", "Please continue the discussion."]` else 422 `failed_policy`; pressure recorded as intervention not model output. Contrast: text `muted #5c5348 on paper 7.00:1`, `accent 10.69:1` PASS 4.5:1; non-text `line #e0d4c4 1.36:1` decorative border FAIL but exempt (card identified by fill/shadow) — consistent with `FULL_BUILD_STATUS_GAPS:56`.

**F6 — UX taste passes, Evidence chain intact.** `app.css:2` tokens `paper #faf6ef ink #1c1712 line #e0d4c4 muted #5c5348 accent #1d3a5f accent2 #0f766e` — no purple gradient / glassmorphism / Inter-everywhere (taste DO NOTs). `api` + `mission.py` wire 5-room nav + timeline `TIME→MODEL+PROMPTS+EVENTS◆+SENSORS╱╲+HUMAN+WEB+AUDIO` scrub + `verify_result {csv_hash_ok:true, orphans:[], ai_computed_metrics:false, chain B.prev=A}` chain. `STAGING_DECISIONS.md` 9 rows (layering, terminal, UX, bloat Hygiene §2A) + `TECH_SPEC` + `DB_SCHEMA` + `API_SPEC` + 5 wireframes.

---

## Gaps (what's missing / must-fix before seal)

**P0 — Deep-freeze illusion (fixed by revert).** Summary prior 1 flagged `mission.py:93` `per_eca_state dict` mutable despite outer `frozen=True` (`m.per_eca_state["per"]="ON"` possible). Audit correctly reverted over-engineered `MappingProxyType`+`field_validator` (added `Any` widening, proxy equality risk) back to simple `dict = Field(default={"per":"OFF","eca":"OFF"})` with outer `frozen` only (`HARNESS_BOUNDARY_AUDIT:29`). Remaining risk: inner mutation still technically possible in Python; mitigated by never mutating after construction + `protocol` hash captures state + linter `rg 'per_eca_state\['` to fail build (audit `Remaining Risks:55`).

**P0 — Seal file set was `glob("*")`.** `workbench.py:48` weighed whatever on bench (`PER_ECA_SKIPPED.json` could weigh in manifest). **Fixed** to explicit `["SCENARIO.json","scenario.csv","DECISION_SUMMARY.json"]` + engine-declared `extra_files` + `sealed_by/at/instrument/sop_version` hallmark (`HARNESS_BOUNDARY_AUDIT:32`). Gap closed.

**P0 — Missing `sealed_by/at/instrument/sop_version`.** Before fix no who/when first; auditor asks. Now added to `verify_result.json` (`workbench.py:32`). Gap closed.

**P0 — Competing ECA config.** `Axiom Evidence Layer/ECA/plugin/eca_config.json` was created by Harness (competing, 9 sections with weights) while `ECA owns its own canonical configuration`. **Fix:** deleted (`HARNESS_BOUNDARY_AUDIT:30`). ECA will recreate. Gap closed.

**P0 — MATH_MODULAR_MAP ownership qualifier missing.** Before `MATH_MODULAR_MAP:8-9` listed thresholds without `owned by` qualifier implying Harness ownership; **fixed** to `— owned by PER/ECA, not Harness` + `Harness records ... hash only`.

**WP1 — Docs hero not promoted (open).** `FULL_BUILD_STATUS_GAPS:53` + `FREEZE_V3_2026-09-24_ON_HOLD:7` + UX audit: `BRIEF_REVOLUTIONARY_V2` (8614 bytes, 100+ tags `#AI-Inside` `#Timeline-As-4D-Object` `#Boundary-As-Data` `#Terminal-As-Substrate` etc.) drafted but **not promoted** to `README.md:10-19` hero + `PROJECT_PROFILE.md:7-8` tagline + `Master WORKING.md §4` Patch-is-one-room correction. README still shows boring-harness pitch. Owner must approve promotion (decision table row 9).

**WP2/WP3 — Duplicate + freeze + boundary tests (done).** `docs/briefs/BRIEF_DUPLICATE_LOG.md` + `STAGING_DECISIONS.md` row 9 + `MATH_MODULAR_MAP.md` table 7 adapters + `protocol/hash_contract.py` single hash `WTF-005A-HASH-v3` (`sort_keys True ensure_ascii False (",",":")` no indent) + `tests/test_harness_boundary.py` + `test_harness_does_not_reimplement_axiom.py` + `test_math_modular.py` wired → `104 passed` (was 96). Remaining: `sha256sum -c` + `FREEZE_V3_ON_HOLD.md` stamp with `impl_hash/cfg_hash/corpus/claims/B.prev=A` (`FREEZE_V3_2026-09-24_ON_HOLD.md` currently 1337 bytes, on hold).

**Remaining rooms not yet built (V1.8→V2+, not a P0 gap but plan).** V1.8 Multi-agent (`Analyst B Critic C Maker D Observer E Adversary` isolated contexts), V1.9 Video Timeline, V2 Films (`Experiment→Timeline→Render Plugin→Video`, video is presentation not proof), V2+ Continuous Observatory (alerts: position/language/contradiction/confidence), Future External API. Each `one Pydantic frozen contract + one app/ room + one GET /master/... + three durable tests` (`FULL_BUILD_STATUS_GAPS:75`).

**Evidence sealing wiring (open).** `Staging/outputs` → `docs/evidence/` promotion currently gitignored, `sealer.py` signature wiring, first `Complete-Report-Pack 22-file` with `WTF-001` via Harness UI → sandbox → Workbench → `DECISION_SUMMARY + verify_result orphans:[]` not yet run (`FULL_BUILD_STATUS_GAPS:79`).

**Ops / scale gaps (deferred, not P0).** Live provider deprecation fallback (observed `deepseek-v4-flash-0731 → 410 EOL` 2026-09-21) needs dynamic routing; multi-agent comparative timelines 100s grid virtual scroll not load-tested at 10k trials (`1MB/experiment` → delta+Glacier planned); video `FFmpeg/TTS` heavy deps need containerize+lazy-load (a11y audit); `num £120k vs 120,000` synonym variant not allowlisted (may false-refuse); LVM matrix hypothetical until LVM at scale (`FULL_BUILD_STATUS_GAPS:87-93`).

---

## Hallucinations (false impressions the current tree would give)

**H1 — Patch is the product.** Before V2, hero/taglines/docs could imply harness = vision trick. Reality: Patch is **ONE room V1.8 WTF-VIS-001…014** among 15 rooms; revolution is whole lab (language drift Monday / memory Tuesday / patch Wednesday / bias Thursday same seal/chain). `BRIEF_REVOLUTIONARY_V2:32` + `STAGING_DECISIONS row 9` explicitly correct this; if README hero not promoted, visitor hallucinates vision-only product.

**H2 — Scorer version string vs content hash.** Evidence Layer scorer shows `SCORER_VERSION 0.1.0` vs `0.1.1` as string increment while content hash unchanged — would hallucinate progress. Must surface `implementation_hash` not just string (`FULL_BUILD_STATUS_GAPS:102`).

**H3 — Brief divergence.** Both `AXIOM HARNESS Brief (1).md` + `(2).md` 3,172 lines `sha256:0a0d0502…` identical but duplicate not flagged early would have scaffolded off wrong brief if diverged. Now logged as duplicate (`STAGING_DECISIONS row 9`, `BRIEF_DUPLICATE_LOG.md` pending).

**H4 — `ai_computed_metrics:false` enforcement at 3 points not enough.** Without linter, LLM numbers could leak into evidence narrative. Need linter to fail build if LLM numbers leak (FULL_BUILD_STATUS_GAPS:104).

**H5 — Path hallucinations.** External references to `Staging/WORKING.md`, `Evidence Axiom living_gap_review_score.py` under `Staging/` are mis-placed; real Staging is `Axiom Harness-Master - Dont Touch/Staging/` with `api/app/docs/missions` no `WORKING.md`; `gap-review/WORKING.md` is FIND log; roots are `Axiom Evidence Layer/WORKING.md`, `PER-Core/WORKING.md`, `ECA/WORKING.md` (prior 5). Mentioning them as Staging paths hallucinates tree.

**H6 — Gate calculation hallucinates Harness maths.** Any doc stating Harness calculates `GateOk/ΔH/T_max/ε/HYPOTHESIS_WEIGHTS` hallucinates ownership. Harness is `MATRIX_BLOCKED` until `PER_ECA switch` wired; maths lives in `ECA/sim/telescope.py`, `PER-Core/sim/telescope.py` (read-only). Docs references (`TECH_SPEC:23`, `ARCHITECTURE:25,37` `|R|≤3 && ΔH>0.5`) are verbal references to `§6 MATRIX_BLOCKED`, not implementation — acceptable per boundary audit but must stay qualified.

**H7 — LVM vs LLM vs VLM matrix as proven.** `LLM (text guess) vs VLM (token guess) vs LVM (true vision)` on same face is hypothetical until LVM at scale; presenting as measured before LVM exists is hallucination. V2 marks it as `family WTF-VIS` receipt but not yet measured (FULL_BUILD_STATUS_GAPS:88).

**H8 — Health honesty hallucination.** Hard-coded `health:true` would hallucinate liveness. Current `api/main.py:/health` is honest — probes `is_safe_relative` + `OUTPUTS/demo` — must keep honest; if `site/index.html` mirrors health from stale build it could re-hallucinate.

---

## Next (sequenced, per FULL_BUILD_STATUS_GAPS:110-115 + audits)

**Today (this commit, WP1+WP4):**
1. Promote `BRIEF_REVOLUTIONARY_V2` to `Staging/README.md:10-19` hero + `PROJECT_PROFILE.md:7-8` tagline + append `Master WORKING.md §4` Patch-is-one-room correction — awaiting owner Approve.
2. Ship `docs/briefs/BRIEF_DUPLICATE_LOG.md` + `STAGING_DECISIONS.md` row 9 (modular math + Patch one room + duplicate `sha256:0a0d0502…`) — done in docs, needs WORKING append.
3. Keep `MATH_MODULAR_MAP.md` ownership-qualified + `protocol/hash_contract.py` single contract; linter `rg 'per_eca_state\['` + `rg 'HYPOTHESIS_WEIGHTS|T_max|epsilon_base'` inside `axiom_harness/` fails build if duplicated.

**Tomorrow (WP3+WP4):**
4. Stamp `docs/FREEZE_V3_2026-09-24_ON_HOLD.md` with `impl_hash/cfg_hash/corpus/claims/B.prev=A` (currently ON_HOLD, 1337 bytes) + `sha256sum -c` validation.
5. Ensure `104 passed` green (`pytest -q` + `smoke.sh 5/5`) — `test_harness_boundary` + `test_math_modular` prove boundary; keep `adapters/per_eca.py ensure_off()` V1 RED.

**Then (audit workflow):**
6. One workflow 8 agents (architecture, testers, color-contrast/taste, captions, brand, research-evidence, EvoCycles-Epistemic, math-hardcode) each `docs/audits/<skill>.md` + this master `docs/AUDIT_MASTER_GAPS_HALLUCINATIONS.md` — rip apart, produce gaps/hallucinations. Audit to wire `sealer.py` signature + promote `Staging/outputs → docs/evidence/` properly (remove gitignore leak) + run first `Complete-Report-Pack 22-file` with `WTF-001` via Harness UI.

**After audit (V1.8→V2+):** V1.8 Multi-agent → V1.9 Video → seal first 22-file pack + V3.0 8D receipt slots (`persons/instruments/responses`). No sell till `push live` approved. EvoCycles `World-A-EvoCycles harness_` + `B-0 physics`, `Epistemic-UX EU-01…06 6A loop`, `Future Workbench` provenance wire as explicit adapters with hash pins (read-only ref today).

---

## Evidence / verification in this session

- Re-read `Staging/docs/FULL_BUILD_STATUS_GAPS_2026-09-24.md` (117 lines), `BRIEF_REVOLUTIONARY_V2_PATCH_IS_ONE_ROOM.md` (82 lines), `HARNESS_BOUNDARY_AUDIT_2026-09-24.md` (60 lines), `STAGING_DECISIONS.md` (9 rows), `MATH_MODULAR_MAP.md` (17 lines, ownership-qualified), `TECH_SPEC.md`/`API_SPEC.md` stubs, `axiom_harness/mission.py` (204 lines, 7 frozen configs), `paths.py:19-51` (`_decoded` + `is_safe_relative` + `STAGING_ROOT` jail), `api/main.py` (`/health` honest + `/schedule`/`/parallel`/`/data`/`/language`/`/audio`/`/sensors`/`/live` 201/422), `app/index.html` (124 lines, 5 rooms), `app/app.css` (11 lines tokens), `README.md`/`PROJECT_PROFILE.md` (32/50 lines). 
- Prior tester/UX/caption claims re-probed: `is_safe_relative` handles `%2525252e` depth, `AudioConfig.transcript_linked` + `POST /audio` present, no `<audio>` tags correctly (harness not player), `allowlist ["scripts/factory_","AXIOM_"]` on `cmd[2]` only, single hash `WTF-005A-HASH-v3`.
- Unresolved: `WORKING.md` under Staging not present (correct), `ECA/plugin/eca_config.json` competing copy confirmed deleted, `FREEZE_V3_ON_HOLD` stamp still ON_HOLD not final, README hero still boring pitch until promotion approved.

*Generated synthesis — do not hand-edit; re-run workflow to regenerate after WP1/WP3 fixes.*
