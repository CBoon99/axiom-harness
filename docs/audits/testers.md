# Tester Audit — 2026-09-24
**Scope:** `Staging/tests/*.py` (20 files, 108 tests), `Staging/smoke.sh`, `Staging/axiom_harness/paths.py`, `Staging/api/main.py`, `Staging/axiom_harness/adapters/workbench.py`, `Staging/axiom_harness/mission.py`, `Staging/axiom_harness/manifest.py`, `Staging/axiom_harness/watcher.py`, `Staging/axiom_harness/registry.py`
**Evidence inspected this audit:** full read of all files above + `PYTHONPATH=Staging pytest -q` → **108 passed, 2 warnings** (pydantic `model_*` protected namespace) + `bash smoke.sh` traced (see §7 below)
**Staging root:** `Documents/Axiom Harness-Master - Dont Touch/Staging` (`axiom_harness/paths.py:8` `STAGING_ROOT = parents[1]` assert)

---

## 1. Path Jail — iterative unquote — VERDICT: GREEN

**Claim to verify:** `axiom_harness/paths.py` jail is iterative (depth>3), anchored via `resolve().relative_to`, blocks `%2e`, `%252e`, `%2525252e` etc.

**Inspected body:**
- `paths.py:14 _decoded` — loop `for _ in range(10): cur=unquote(cur)` until stable, then `while cur!=prev: cur=unquote(cur)` — handles 5×-encoded `..` (`%2525252e` → `%25252e` → `%252e` → `%2e` → `.`). Verified by `is_safe_relative("missions/master_demo_wtf001.yaml")==True`, `is_safe_relative("%2e%2e/escape")==False`, `is_safe_relative("%2525252e%2525252e/escape")==False`, and 5× `urllib.parse.quote("..")` deep test in `test_jail_canonical.py:30`.
- `paths.py:24 is_safe_relative` — rejects absolute (`/`, `\\`), double-slash `//`, backslash `\\`, `..` segment split on both `/` and `\\`, then `resolve().relative_to(STAGING_ROOT.resolve())` anchored check.
- `STAGING_ROOT` assert pins `Axiom Harness-Master - Dont Touch/Staging` substring — noted as brittle but correct.

**Tests:**
- `test_jail_canonical.py` (6 tests): `test_blocks_simple_traversal`, `test_blocks_single_encode`, `test_blocks_double_encode`, `test_blocks_deep_triple_quad` (5× encode), `test_allows_safe_relatives`, `test_iterative_stable` (checks `_decoded("%2525252e")== "."`)
- `test_patches.py:test_is_safe_blocks_traversal`, `test_redteam.py:test_path_escape_blocked`, `test_health_honesty.py:test_health_logic_via_paths` — all repeat same jail checks
- `smoke.sh:[1]` probes `is_safe_relative("missions/master_demo_wtf001.yaml")` and `is_safe_relative("%2e%2e/escape")` + deep `%2525252e`

**Verdict:** GREEN — jail iterative unquote holds to depth 5+ (10-iteration bound), anchored, not substring-matched.

---

## 2. Allowlist Anchored — VERDICT: GREEN

**Claim:** `adapters/workbench.py:_assert_allowlist` validates ONLY `cmd[2]` module argv, not joined-string substring; smuggle via trailing args must fail.

**Inspected body:**
- `workbench.py:10 _assert_allowlist(cmd)` — checks `len(cmd)<3 or cmd[0]!="python3" or cmd[1]!="-m"` → `failed_policy`, then `module=cmd[2]`, allows only `module=="axiom_wb"` or `module.startswith(p) for p in ALLOWED_SCRIPT_PREFIXES` where `ALLOWED_SCRIPT_PREFIXES=["scripts/factory_","AXIOM_"]` (`paths.py:12`).
- Rejects `evil -- scripts/factory_evil` (joined contains allowlist but module is `evil`), `evil scripts/factory_foo`, `bad --out scripts/factory_x` — all `failed_policy`.
- Blocks wrong binary (`python` not `python3`), missing `-m`, short argv, `not_allowed_module`.

**Tests:**
- `test_allowlist_anchored.py` (7 tests): `test_prefixes`, `test_allows_axiom_wb`, `test_allows_factory_prefix`, `test_blocks_evil_smuggle` (3 smuggle cases), `test_blocks_wrong_binary_and_missing` (5 cases), `test_blocks_trailing_args_dont_whitelist`, `test_future_per_eca_noop_stays_off`
- `test_redteam.py:test_allowlist_blocks_smuggle` repeats
- `test_harness_boundary.py` does not duplicate allowlist but covers `GateOk` non-calculation

**Verdict:** GREEN — allowlist anchored on `cmd[2]` only. Note gap: `AXIOM_` prefix is broad (`AXIOM_evil` would pass if injected into PYTHONPATH) — noted as P1 in `architecture.md` (G10) but not a test failure.

---

## 3. Seal Frozen — VERDICT: GREEN (with dict-mutability note)

**Claim:** `mission.py:MasterMission` and all `*Config` (`ScheduleConfig`, `ParallelConfig`, `DataConfig`, `LanguageConfig`, `AudioConfig`, `SensorConfig`, `LiveConfig`) are `frozen=True` — any mutation raises, identity is hash-pinned.

**Inspected body:**
- `mission.py:40 ScheduleConfig`, `69 ParallelConfig`, `89 MasterMission`, `120 LiveConfig`, `138 SensorConfig`, `156 AudioConfig`, `178 LanguageConfig`, `198 DataConfig` — all `model_config={"frozen":True}`. Verified `m.id="X"` raises `ValidationError`.
- `cost:Optional[dict]`, `per_eca_state:dict`, `params:dict`, `permissions:dict` remain `dict`-typed — outer `MasterMission` frozen prevents `m.per_eca_state={...}` reassignment but not `m.per_eca_state["per"]="ON"` inner mutation (Python dict mutability). Mitigated socially by `protocol` hash + linter gate, not type-sealed. Already flagged as G7 in architecture audit; deferred to V1.8 `PerEcaState(BaseModel frozen=True)`.
- Pydantic warnings 2: `model_version` + `model_matrix` conflict `protected_namespaces` — not blocking, flagged G3.

**Tests:**
- `test_schedule_v11.py:test_schedule_once_sealed` (checks `m.id="X"` fails), `test_parallel_v12.py:test_parallel_matrix_and_all` (checks `m.parallel.parallel_count=2` fails), `test_data_v13.py`, `test_language_v14.py:test_language_variants_cross_control`, `test_audio_v15.py:test_audio_empty_fails_and_frozen`, `test_sensors_v16.py:test_sensors_frozen`, `test_live_v17.py:test_live_frozen_and_captions_gate`, `test_seal_gate.py:test_mastermission_frozen` — all verify frozen.

**Verdict:** GREEN — seal frozen holds for outer field reassignment. Inner-dict mutability is a documented V1 RED seam, not a test failure.

---

## 4. Schedule / Parallel / Data / Language / Audio / Sensors / Live — 422 — VERDICT: GREEN

**Claim:** each `POST /api/master/<room>` returns 201 when `<room>` present and valid, 422 `failed_policy` when missing or semantically invalid; never silently queues.

**Inspected body — `api/main.py`:**
- `/api/master/seal:26` — requires `model_version` + `per_eca_state` non-empty → 422 else 201
- `/api/master/pressure:49` — allowlist `["Are you sure?","Please continue the discussion."]` else 422
- `/api/master/schedule:60` — `if m.schedule is None → 422`, then `INTERVAL/REPEATING interval_seconds>0`, `REPEATING repeats>0`, `CRON cron required`, `UNTIL_CONDITION until_condition required` → 422 else 201 `{scheduled:True, sealed:True}`
- `/api/master/parallel:86` — `if m.parallel is None → 422`, `parallel_count 1..64` else 422, `model_matrix` empty → 422 else 201 `{parallel:True, isolated:True}`
- `/api/master/data:107` — `if m.data is None → 422`, `sources empty → 422`, `dataset_refs` each `is_safe_relative` else 422 else 201
- `/api/master/language:131` — `if m.language is None → 422`, `primary in variants → 422` else 201
- `/api/master/audio:149` — `if m.audio is None → 422`, `sources empty → 422` else 201
- `/api/master/sensors:168` — `if m.sensors is None → 422`, `kinds empty → 422` else 201
- `/api/master/live:186` — `if m.live is None → 422`, `feeds empty → 422` else 201
- All 9 failure paths `send_response(422)` + `{"failed_policy":...}`; all success `201` with canonical JSON `sort_keys=True ensure_ascii=False separators=(",",":")`

**Tests (7 room files, 3 each):**
- `test_schedule_v11.py` (3): `test_schedule_once_sealed`, `test_schedule_interval_requires_interval`, `test_schedule_repeating_and_cron`
- `test_parallel_v12.py` (4): `test_parallel_one_isolated`, `test_parallel_matrix_and_all`, `test_parallel_sequence_capped` (cap 64), `test_parallel_api_gate`
- `test_data_v13.py` (3): `test_data_sources_and_jail`, `test_data_empty_sources_fails_via_api`, `test_data_images_audio_video`
- `test_language_v14.py` (3): `test_language_primary_and_variants`, `test_language_single_and_detect`, `test_language_variants_cross_control`
- `test_audio_v15.py` (3): `test_audio_sources_timeline_sync`, `test_audio_multi_speaker_uploaded_live`, `test_audio_empty_fails_and_frozen`
- `test_sensors_v16.py` (3): `test_sensors_kinds_and_policy`, `test_sensors_physical_iot_human`, `test_sensors_frozen`
- `test_live_v17.py` (3): `test_live_feeds_basic`, `test_live_observatory_compare`, `test_live_frozen_and_captions_gate`
- API source checks: `test_pressure_allowlist.py:test_pressure_source_allowlist`, `test_seal_gate.py:test_seal_source_checks_gate`, `test_health_honesty.py:test_health_source_is_honest`

**Verdict:** GREEN — all 7 rooms wire 201/422 correctly, fail-closed, no silent queue. Mental 422 matrix: missing → 422 verified via `is None` guard per room; semantic (interval 0, empty sources/kinds/feeds, primary∈variants) → 422 verified.

---

## 5. Boundary 12 Tests — VERDICT: GREEN

**Claim:** `tests/test_harness_boundary.py` 12 tests gate harness-is-orchestration-only (no `GateOk/ΔH/T_max` calc, no PER/ECA math, no provider factory, no `sys.path` hack, no `/tmp/anthropic_key`, no mock-as-live, no failure→pass conversion).

**Inspected body — `test_harness_boundary.py` (12 tests):**
1. `test_harness_cannot_calculate_gateok` — no `GateOk` outside ECA, no `ΔH` outside archive
2. `test_harness_cannot_alter_eca_config` — `ensure_off(ON)` → `MATRIX_BLOCKED_UNTIL_SWITCH_WIRED`
3. `test_harness_cannot_silent_provider_replace` — no `*provider*` files in harness
4. `test_harness_records_hashes` — `seal_per_eca` writes `PER_ECA_SKIPPED.json` with `ai_computed_metrics:false`
5. `test_propagates_refusal_unchanged` — `ensure_off` refusal contains `failed_policy`
6. `test_no_mock_as_live` — `mission.py` has no `MOCK`
7. `test_adapter_failure_explicit` — `ensure_off` failure contains `failed_policy`
8. `test_no_duplicated_maths` — no `HYPOTHESIS_WEIGHTS/T_max/epsilon_base`
9. `test_harness_cannot_import_untracked_sibling_code` — no `sys.path`, no `PER-Core`, no `ECA/sim`
10. `test_harness_cannot_rely_on_local_only_files` — no `/tmp/anthropic_key`, no `untracked` outside `tracked`
11. `test_harness_cannot_convert_failure_to_pass` — failure stays `failed_policy`, not `sealed:true`
12. `test_harness_cannot_declare_upstream_proven` — no `eca proven` / `eca_pass`

All 12 pass (verified in `pytest -q` 108). Additional coverage: registry 7 doors (`test_matrix_seals.py`), health honesty 5, allowlist 7, jail 6, manifest 6, patches 8, seals 2.

**Verdict:** 12 tests GREEN — HARNESS_BOUNDARY_CLEAN holds.

---

## 6. Other Signals — pytest 108 / smoke.sh / manifest / lvm / seals

**108 tests:** `PYTHONPATH=Staging python3 -m pytest Staging/tests -q` → `108 passed, 2 warnings` (pydantic `model_version`/`model_matrix` protected namespace). No skips, no xfails. File counts: `test_allowlist_anchored 7 + test_audio_v15 3 + test_data_v13 3 + test_gateway 3 + test_harness_boundary 12 + test_health_honesty 5 + test_jail_canonical 6 + test_language_v14 3 + test_live_v17 3 + test_lvm_pause_live_scalable 9 + test_manifest_canonical 6 + test_manifest 2 + test_matrix_seals 8 + test_no_touch 2 + test_parallel_v12 4 + test_patches 8 + test_pressure_allowlist 6 + test_redteam 5 + test_schedule_v11 3 + test_seal_gate 7 + test_sensors_v16 3 = 108`.

**smoke.sh:** 5 gates — `[1] is_safe_relative jail + deep decode OK`, `[2] POST /seal validates model_version+PER/ECA OK`, `[3] pressure allowlist OK`, `[4] manifest canonical (no indent, separators (",",":"), sha256 recompute) OK`, `[5] verify_result checks (orphans, ai_computed_metrics, engine/sealed) + no Master mutation`. Note: smoke writes `verify_result.json` with canonical `separators=(",",":")` (no space after `:`), but then greps `'"ai_computed_metrics": false'` (with space) — grep would fail when run as `bash smoke.sh` (observed: `[5]` greps miss, `echo "== OK smoke =="` never reached). Logic is sound; format mismatch is a smoke.sh cosmetic bug, not a harness bug — canonical no-space is correct per WTF-005A-HASH-v3. Fix: change grep to `'"ai_computed_metrics":false'` (no space) or use `python -c` json check. Does not affect pytest (pytest does not run smoke.sh).

**Manifest/canonical:** `manifest.py:write_manifest` uses `sort_keys=True ensure_ascii=False separators=(",",":")` + `sha256_file` chunked 8192 — `test_manifest_canonical.py` verifies round-trip equality, `ensure_ascii False` (`café` not `\u`), `WTF-005A-HASH-v3` contract, tamper recompute, truncation fails.

**Watchers/LVM/Scalable:** `test_lvm_pause_live_scalable.py:9` checks LVM `llava-13b`, pause/resume buttons, Live Room `data-panel="live"`, watcher `ARMED→STARTED→RUNNING→PAUSED→RESUMED→STOPPING→SEALED→COMPLETE` no illegal jump, `repeat(auto-fill,minmax(220px,1fr))` + `247` + virtualized, `GET /master/timeline?limit=24`, 7 seals + future chain `B.prev=A`.

**Matrix seals:** `test_matrix_seals.py` verifies 18 cells `12+4+2` in `outputs/18cell`, each `MANIFEST+verify_result+SCENARIO+scenario.csv+DECISION_SUMMARY` + `ai_computed_metrics:false` + `orphans:[]`.

---

## 7. Unresolved Evidence (explicitly not re-inspected this pass)

- `Staging/app/index.html` grid CSS `repeat(auto-fill,minmax(220px,1fr))` + taste tokens — prior audit pointer, not re-read this pass (would need app/ read outside 5-file mandate in prior architecture audit; retained as discovery pointer)
- `Staging/axiom_harness/adapters/evo_eu.py`, `future.py`, `per_eca.py` full substrate claims (§29 telescope) — `per_eca.py` `ensure_off` verified, but future/evo seal bodies not re-read beyond registry
- `Staging/docs/DB_SCHEMA.md`, `API_SPEC.md` table shapes — referenced but not inspected
- smoke.sh grep-space bug noted above — not fixed this audit (would require editing smoke.sh)

---

## 8. Fix List

| P | Fix | File(s) |
|---|-----|---------|
| P0 | Done — none blocking: 108 green, jail iterative, allowlist anchored, frozen, 422 per room, boundary 12 all hold | — |
| P1 | Fix `smoke.sh:[5]` grep to no-space canonical (`"ai_computed_metrics":false`) or `python -c` json check so `bash smoke.sh` reaches `== OK smoke ==` | `Staging/smoke.sh:72` |
| P1 | Add `protected_namespaces=()` to `MasterMission`/`ParallelConfig` to silence 2 pydantic warnings | `axiom_harness/mission.py` |
| P2 | Type `per_eca_state` as `PerEcaState(BaseModel frozen=True)` to close inner-dict mutability seam (architecture G7) | `axiom_harness/mission.py` |

No `push live` blocker from tester lens; smoke.sh glow fix is cosmetic before CI.

---

*Tester audit — path jail iterative, allowlist anchored on cmd[2] only, seal frozen outer, 7 rooms each 201/422 fail-closed, 12 boundary tests GREEN, 108 passed. smoke.sh gates 1-4 GREEN, gate 5 grep-space mismatch noted but harness output is correct canonical.*
