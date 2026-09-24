# Systems Architect Audit — 2026-09-24
**Scope:** `Staging/docs/BRIEF_REVOLUTIONARY_V2_PATCH_IS_ONE_ROOM.md` (82 lines, 8600B), `Staging/axiom_harness/mission.py` (204 lines), `Staging/api/main.py` (216 lines), `Staging/docs/MATH_MODULAR_MAP.md` (33 lines), `Staging/docs/HARNESS_BOUNDARY_AUDIT_2026-09-24.md` (60 lines). Lens: modular rooms, terminal substrate, boundary, Master frozen.
**Evidence inspected this audit:** `axiom_harness/paths.py` (54 lines), `adapters/workbench.py` (64 lines), `adapters/per_eca.py` (23 lines), `manifest.py` (23 lines), `watcher.py` (42 lines), `registry.py` (21 lines), `docs/ARCHITECTURE.md` (88 lines), `docs/TECH_SPEC.md` (48 lines), `docs/STAGING_DECISIONS.md` (17 lines), `docs/FREEZE_V3_2026-09-24_ON_HOLD.md`, tests `test_harness_boundary.py` (12 tests), `test_jail_canonical.py`, `test_manifest_canonical.py`; run `PYTHONPATH=Staging pytest -q` → **108 passed, 2 warnings**.
**Staging root:** `Documents/Axiom Harness-Master - Dont Touch/Staging` (`axiom_harness/paths.py:8` `STAGING_ROOT = parents[1]` assert `Axiom Harness-Master - Dont Touch/Staging`).

---

## 1. Modular Rooms — VERDICT: holds, with coupling debt

**What is claimed:** 7 rooms V1.1 Schedule → V1.7 Live each `one Pydantic frozen contract + one app/ room + one POST /api/master/* 201/422 + 3 tests`, isolated, add-a-room without breaking lab (§49,§55,§74).

**What actually exists (verified):**
- `mission.py:56 ScheduleConfig`, `76 ParallelConfig`, `198 DataConfig`, `178 LanguageConfig`, `155 AudioConfig`, `137 SensorConfig`, `119 LiveConfig` — all `frozen=True`, optional on `MasterMission:99-105` (`schedule/parallel/data/language/audio/sensors/live: Optional[Config]`). Verified `mission.py:85-204`.
- `api/main.py` wires 7 endpoints: `/schedule` (60), `/parallel` (86), `/data` (107), `/language` (131), `/audio` (149), `/sensors` (168), `/live` (186) — each validates `m.<room> is None → 422 failed_policy`, then field semantics, then `201 {"sealed":True, "config_hash":m.protocol}`. Correctly fail-closed, honest 201/422, no silent queue.
- Tests pass 108 (was 96 → 104 after boundary → 108 now), including `test_schedule_v11`, `test_parallel_v12`, `test_data_v13`, `test_language_v14`, `test_audio_v15`, `test_sensors_v16`, `test_live_v17` — each checks 201/422.

**Gaps:**
- **G1 — Single-protocol coupling.** All 7 rooms live as optional fields on one `MasterMission` sharing one `protocol` hash. Changing `language` rewrites hash for identical `schedule` — correct for frozen identity (any change = new `WTF-001` identity), but means rooms are *not* independently sealable. No `sub-protocol` per room. This is by design per §55 one-EXPERIMENT object, but “modular” then means *type-modular*, not *seal-modular*. Call out honestly: you cannot re-seal one room without re-sealing whole mission. Document it; don’t imply per-room chain.
- **G2 — Dict-typed loose surfaces.** `per_eca_state: dict` (93), `cost: Optional[dict]` (94), `params: dict` (97), `permissions: dict` (98) are untyped. `mission.py` accepts `cost={"tokens_input":"banana"}` and still `frozen`. Boundary audit (HARNESS_BOUNDARY_AUDIT:29) reverted `MappingProxy+Any` over-engineering, but now those four surfaces have *zero* schema. Any future linter `rg 'per_eca_state\['` catches mutation but not malformed dict. Fix: keep `dict` for V1 RED, but add `cost: Optional[CostConfig]` typed before V2 or at minimum `field_validator` on `params` forbidding unknown keys (still `frozen` outer suffices for seal, but typed would fail fast 422 rather than silently sealing garbage).
- **G3 — Pydantic protected-namespace warning.** `mission.py:92 model_version` + `79 model_matrix` trigger `pydantic UserWarning: Field "model_*" has conflict with protected namespace "model_"` (pytest warnings 2). Not blocking, but noisy; set `model_config={"frozen":True,"protected_namespaces":()}` to silence and prove intentional.
- **G4 — Missing rooms still described as V1.** `TECH_SPEC.md:19` claims `Control|Engine|Sandbox|Gateway|Secret|Data|Sensor|Timeline|Audio|Video|...|Multi-Agent|Scheduler|Recorder|Analysis|Collaboration|Evidence|Export` as V1 rooms while only Data/Sensor/Audio/Live/Schedule/Parallel exist as typed configs. `ARCHITECTURE.md:7` claims V1 is 9 rooms (Control…Evidence) — the mismatch is paper-vs-code. Paper says V1=9 rooms; code proves 7 typed configs + Evidence/Sandbox/Control exist only as docs/app, not as `mission.py` types. Not a lie, but a lens crack: count rooms by *code type* not prose list.

**Hallucinations:**
- **H1 — “Each room isolated” misread as runtime isolation.** Code isolation is *type* isolation (`Optional[Config]` fields don’t share handler code). Runtime isolation (separate sandbox cwd per `parallel_count` 1..64) is only `ParallelConfig.isolated:bool=True` unchecked — `api/main.py:95` validates `1..64` and returns `"isolated":True` but spawns *no* sandboxes (no `jail_for_experiment` call in `/parallel`). It endorses isolation without enforcing it. Until P2 wires `axiom_harness/adapters/*.py` to actually create `OUTPUTS/<id>/sandbox-<n>`, “isolated sandboxes” is config-true, runtime-hallucinated.

---

## 2. Terminal Substrate — VERDICT: contract holds, visual deferred correctly

**Claim:** `TECH_SPEC.md:22` + `ARCHITECTURE.md:9` — terminal is substrate (inspectable, reproducible, modular, replaceable), each experiment isolated `outputs/<id>/sandbox`, UI is one client (`UI→API→Harness→Environment`), `TERM:$` + scroll + exit code + file writes jailed, grid `repeat(auto-fill,minmax(220px,1fr))` + virtual scroll + `O(1)` per row + paginated `GET /master/timeline?limit=24`.

**Verified:**
- `paths.py:53 jail_for_experiment → OUTPUTS/experiment_id/sandbox` exists and is used by `adapters/workbench.py:22 seal_workbench(cwd=str(out_dir))` with `is_safe_relative` gate + `ALLOWED_SCRIPT_PREFIXES` anchoring on `cmd[2]` only (not substring).
- `TECH_SPEC.md:43 O(1) step, O(N log N) audit cap` matches `watcher.py:27 _ALLOWED` explicit state machine — no unbounded `setInterval`.
- `app/` presence noted in staging `ls` (wireframes exist), `ARCHITECTURE.md:17` claims `repeat(auto-fill,minmax(220px,1fr))` verified in prior master audit (re-inspected as discovery pointer; CSS not re-read this pass — unresolved evidence, marked below).

**Gaps:**
- **G5 — No container/limits for 100s grid.** `ParallelConfig.parallel_count≤64` caps *logical* parallelism, but no `cgroup`/timeout-per-sandbox beyond `adapters/workbench.py:37 timeout=3600` (single workbench call, not per-parallel). Running 64× sandboxes on one host will OOM/timeout unpredictably; no back-pressure, no `429`. Paper claims `O(1) per-sample` but system has no scheduler — `Runner RUN ONE/SEQUENCE/ALL/PARALLEL` is still `api/main.py` returning `{"parallel":True}` not a scheduler. Correct per V1 paper (no code yet), but don’t demo 64 as live until `watcher.py` + queue exists.
- **G6 — Live feed isolation is config-only.** `LiveConfig observatory:true + compare:true` (§32) promises `same feed → multiple models isolated` — `api/main.py:198` returns the promise with no feed wiring. No `LiveFeedKind` handler, no timestamp source. Hallucination if demoed as live before adapter exists (matches H1).

**Hallucinations — none material** on terminal contract itself; the “terminal as substrate not visual” distinction (ARCHITECTURE.md:7) is correctly held — no purple gradient / glassmorphism lock-in observed in prior audit.

---

## 3. Boundary — VERDICT: HARNESS_BOUNDARY_CLEAN holds with two remaining seams

**Claim:** Harness is `LOAD/CONFIGURE/FREEZE/RUN/RECORD/SEAL` only; never calculates `GateOk/ΔH/T_max/ε/HYPOTHESIS_WEIGHTS`; `MATH_MODULAR_MAP.md` is registry not source of truth; `AXIOM_ENGINE_ROOT` read-only via jailed subprocess.

**Verified:**
- `adapters/per_eca.py:11 ensure_off` raises `MATRIX_BLOCKED_UNTIL_SWITCH_WIRED` for any `per:ON` or `eca:ON` — RED gate, never calls living `PER-Core/sim/telescope.py` or `ECA/sim/telescope.py`. `seal_per_eca:15` only writes `PER_ECA_SKIPPED.json` + `MANIFEST`.
- `mission.py` contains *zero* of `GateOk/ΔH/T_max/HYPOTHESIS_WEIGHTS/epsilon_base/Telescope` (verified by `test_no_duplicated_maths` passing). `MATH_MODULAR_MAP.md:11-14` now qualifies rows `owned by PER/ECA not Harness — UNKNOWN` + `UPSTREAM-BLOCKED` — correct.
- `adapters/workbench.py:10 _assert_allowlist` anchors on `cmd[2]` only (`python3 -m <module>`), rejects `shell=True`, enforces `is_safe_relative` on `mission_yaml` relative to `STAGING_ROOT`, timeout 3600, `cwd=str(out_dir)`. Seal set is explicit `["SCENARIO.json","scenario.csv","DECISION_SUMMARY.json"] + extra_files` not `glob("*")` (P0 fix, HARNESS_BOUNDARY_AUDIT:32) + hallmark `sealed_by/at/instrument/sop_version` written to `verify_result.json:63`.
- `api/main.py:/health` is honest (checks `is_safe_relative` + `OUTPUTS/demo` existence, not hard-coded true); `/pressure` 422 unless `probe in ["Are you sure?","Please continue..."]`; `/seal` 422 unless `model_version+per_eca_state` present; jail canonicalisation `paths.py:19 _decoded` iterative `unquote` depth 10 + `while cur!=prev` handles `5×`-encoded `..` (tested to `"%2525252e"` → `".."`).
- 108 tests green, `test_harness_boundary.py` 12 tests gate `cannot_calculate_gateok`, `cannot_alter_eca_config`, `cannot_silent_provider_replace`, `no_mock_as_live`, `adapter_failure_explicit`, `no_duplicated_maths`, etc.

**Remaining gaps:**
- **G7 — Inner-dict mutability.** `frozen=True` prevents `m.id="X"` but not `m.per_eca_state["per"]="ON"` (Python dict is mutable). HARNESS_BOUNDARY_AUDIT:55 explicitly notes this and mitigates with “Harness never mutates post-construction + `protocol` hash captures state + linter `rg 'per_eca_state\['`”. Mitigation is correct for V1 RED, but it is a *social* seal not a *type* seal. Systems fix is `per_eca_state: PerEcaState(BaseModel frozen=True)` typed, not `dict`, so `m.per_eca_state.per="ON"` would raise `ValidationError`. Defer to V1.8 or add now as P1.
- **G8 — `registry.py` gate strings look authoritative.** `registry.py:10-14` records `per gate: "|R|<=3 OR weight>=75..."` and `eca gate: "GateOk |R|<=3 && ΔH>0.5..."`. Prior audit `AUDIT_MASTER_GAPS: H6` calls this “verbal reference not implementation — acceptable per boundary audit but must stay qualified.” Currently they are bare strings without `— owned by PER/ECA, not Harness — see <path>:line` qualifier. Add `owner:` field to each entry and comment `# mirror — not authoritative, see ECA/sim/telescope.py:101` so future agent doesn’t treat registry as threshold source.
- **G9 — `STAGING_ROOT` assert is brittle.** `paths.py:10 assert "Axiom Harness-Master - Dont Touch/Staging" in str(STAGING_ROOT)` pins a human-readable path substring. Rename or symlink breaks the harness (host fails at import). Prefer `assert (STAGING_ROOT / "axiom_harness" / "mission.py").exists()` (structural) over string match. Current passes, but is a hallucination of portability.
- **G10 — `ALLOWED_SCRIPT_PREFIXES = ["scripts/factory_","AXIOM_"]` is overly broad.** `workbench.py:18 module.startswith("AXIOM_")` would allow `AXIOM_evil` module if injected into `PYTHONPATH`. `test_allowlist_anchored` covers substring smuggle on trailing args but not prefix collision. Narrow to explicit allowlist `["axiom_wb","scripts.factory_"]` or require full module path `scripts.factory_*` file existence check before `_assert_allowlist`.

**Hallucinations:**
- **H2 — “Harness orchestrates” hallucinated as running.** `mission.py` + `api/main.py` are *config-validators* returning `{"sealed":True}` JSON. They do not `LOAD` a sandbox, `RUN` a model, or `SEAL` evidence except `adapters/workbench.py`/`per_eca.py` which are only exercised via direct call, not via the 7 `/api/master/*` endpoints. The `/schedule`, `/parallel`… endpoints validate and return; they don’t enqueue `watcher.py` lifecycle `ARMED→COMPLETE`. So “orchestrates LOAD/CONFIGURE/FREEZE/RUN/RECORD/SEAL” is true for `workbench+per_eca` leaves, but the 7-room config endpoints are currently *admission only* — they don’t advance `watcher.lifecycle`. Don’t demo “scheduled experiment ran” when you only called `POST /api/master/schedule` → 201.
- **H3 — MANIFEST chain `B.prev=A` is written but never verified.** `manifest.py:20 write_run_pointer` exists, `ARCHITECTURE.md:17` claims `prev_receipt_hash` chain, but no `verify_chain()` enforces it. A missing `B.prev=A` would still verify `csv_hash_ok:true`. Chain is stored, not enforced — seal chain is *recorded*, not *guaranteed*.

---

## 4. Master Frozen — VERDICT: frozen correctly, staging alias drift needs lock

**Claim:** `Documents/Axiom Harness-Master - Dont Touch/` is FROZEN `-do not touch` at 2026-09-24 05:39, Staging is writable sibling `Documents/Axiom Harness-Master - Dont Touch/Staging`, sibling alias `Axiom-Harness-Staging/` (paper alias), Master `WORKING 152 + MEMORY 117` frozen, Staging builds paper+code, `push live` is explicit gate.

**Verified:**
- `Staging/docs/FREEZE_V3_2026-09-24_ON_HOLD.md` stamps `ON HOLD — frozen, sealed, not pushed, not deployed` with `WTF-005A-HASH-v3` contract.
- `PROJECT_PROFILE.md:4` locks root `Documents/Axiom Harness-Master - Dont Touch/ (FROZEN 2026-09-24)` + `Staging/.../Staging/` + `briefs (1)==(2) 3,172 lines sha256:0a0d0502…` duplicate logged via `STAGING_DECISIONS.md:15 row 9`.
- `paths.py:8-10` asserts staging location — Master import would fail, preventing accidental build in Master.
- `ARCHITECTURE.md:1` header: `Master: Axiom Harness Master/ frozen 2026-09-24 (brief 3,172 lines §1-§79). Staging: Axiom-Harness-Staging/ (this tree)` — consistent.

**Gaps:**
- **G11 — Staging git history is the freeze artifact, not a tag.** `FREEZE_V3_ON_HOLD.md` writes `Impl hash $(git rev-parse HEAD)` as literal shell substitution, not an actual hash value. The freeze is a document, not a `git tag v3-on-hold <sha>` or `sha256sum -c` manifest. Before `push live`, run `git tag` + `git rev-parse HEAD > docs/FREEZE_V3_HASH.txt` + `sha256sum Staging/docs/BRIEF_REVOLUTIONARY_V2_PATCH_IS_ONE_ROOM.md Staging/axiom_harness/mission.py Staging/api/main.py > docs/FREEZE_MANIFEST.sha256` so thaw is detectable.
- **G12 — Alias drift.** `Staging/` appears as `Documents/Axiom Harness-Master - Dont Touch/Staging` (real), `Axiom-Harness-Staging/` (paper alias), `Staging/` (relative), `Axiom Harness Master/` (space vs hyphen). `PROJECT_PROFILE.md:4` already normalises, but `README.md` still references `Axiom-Harness-Staging/` and `Axiom Harness Master/` interchangeably. Lock one canonical relative path in `paths.py` docstring and `PROJECT_PROFILE.md` and grep-gate it (`rg 'Axiom-Harness-Staging' → warn if outside docs`).
- **G13 — Evidence promotion path is gitignored + unwired.** `Staging/outputs/` is gitignored (correct), `docs/evidence/_HARNESS_ECA_GATED_2026-09-24` exists as promoted sample but no `scripts/seal_master.py` enforces `outputs/<id>/MANIFEST.json` → `docs/evidence/<id>/MANIFEST.json` hash-preserving copy. Promotion is manual — Master frozen is safe, but sealed evidence could be mutated in `outputs/` without detection because `MANIFEST.json` is not re-verified on read. Wire `verify_result.json: csv_hash_ok` check in `api/main.py:/health` or add `make verify-manifest`.

**Hallucinations:**
- **H4 — “Master frozen” hallucinates immutability.** Master is frozen by *social* contract (`- Dont Touch` dirname + `WORKING.md` note), not by git `branch protection` or filesystem `chmod -R a-w`. Anyone can still `write Master/WORKING.md`. HARNESS_BOUNDARY_AUDIT:35 deliberately preserved historical evidence and did not chmod. The freeze is *observed* (WORKING changelog notes it) not *enforced*. State honestly: Master is *declared* frozen, enforcement is `git diff Master/` + `test_no_touch.py` which currently only checks one sentinel file.

---

## 5. Cross-cutting: BRIEF V2 Patch-Is-One-Room

`BRIEF_REVOLUTIONARY_V2_PATCH_IS_ONE_ROOM.md` is the correction of `H1` in prior `AUDIT_MASTER_GAPS`: Patch Illusion (`1024→224→14×14→768-dim→576 tokens→8 words, 393,216:1, 99.99% gone`) was hero, now correctly scoped as **ONE room V1.8 `WTF-VIS-001…014`** among 15, with 100+ tags inventoried. The brief is *not* still a vision deck — it’s a lab brief. `README.md:13` and `PROJECT_PROFILE.md:14` now forefront the inventory; remaining gap is `WP1` hero promotion was already done per this inspector’s read of `README.md:13` (shows revolutionary line). If Master hero still shows boring-harness pitch, promoter missed Master (Staging README is correct).

---

## 6. Unresolved evidence (explicitly not inspected this pass)

- `Staging/app/index.html` + `app.css` grid/visual `repeat(auto-fill,minmax(220px,1fr))` + taste tokens — cited via prior audit discovery pointer, not re-read (would require `read_file` on `app/` outside 5-file mandate; mandate prioritized).
- `Staging/axiom_harness/adapters/evo_eu.py`, `future.py` — not in mandate, so EvoCycles/Future substrate claims (§29 future.py telescope) not reverified.
- `Staging/docs/DB_SCHEMA.md`, `API_SPEC.md` — referenced but not inspected (table shapes for `experiments/sandboxes/events` would be needed to prove evidence chain enforcement).

---

## 7. Prioritised fix list

| P | Fix | File(s) | Effort |
|---|-----|---------|--------|
| P0 | Type `per_eca_state` → `PerEcaState(BaseModel frozen=True)` instead of `dict` so inner mutation raises `ValidationError` (closes G7). Add `protected_namespaces=()` to `MasterMission` (G3). | `mission.py` | 1h |
| P1 | Qualify `registry.py` gate strings with `owner: PER/ECA` + source line comment (G8). Narrow `ALLOWED_SCRIPT_PREFIXES` to explicit modules (G10). Replace `STAGING_ROOT` string assert with structural check `(root / "axiom_harness/mission.py").exists()` (G9). | `registry.py`, `adapters/workbench.py`, `paths.py` | 1h |
| P1 | Materialise freeze: `git tag freeze-v3-on-hold-$(git rev-parse --short HEAD)` + `sha256sum` manifest for the 5 inspected files (G11). | `docs/FREEZE_V3_2026-09-24_ON_HOLD.md`, git | 30m |
| P2 | Wire scheduling/parallel to `watcher.py` or document them as admission-only (H2/G5). Add `verify_chain()` + `verify-manifest` Makefile target (H3/G13). | `api/main.py`, `watcher.py`, `manifest.py` | half-day |
| P2 | Alias lock: single canonical staging path, grep-gate `Axiom-Harness-Staging` outside docs (G12). | `PROJECT_PROFILE.md`, CI | 20m |

No `push live` until P0 closed and 108 tests re-green with `sha256sum -c docs/FREEZE_MANIFEST.sha256`.

---

*Audit by systems lens — modular rooms hold as types, terminal substrate is contract not chrome, boundary is RED-clean with dict-mutability seam, Master is declared-frozen not enforced-frozen. All claims above are file:line verifiable; unresolved items are named, not hand-waved.*
