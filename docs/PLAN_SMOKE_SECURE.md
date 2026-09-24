# Plan — Get code secure + smoke-clean before next build

## Goal
Make `Axiom Harness-Master - Dont Touch/Staging/` **secure and all-working** before any V1.1/V2 room is cut. That means: close the 2 remaining contest jail/allowlist would-fails, prove the Harness API is honest (health not hard-coded, seal gate checks `model_version/per_eca_state`, pressure allowlist), and land a **repeatable smoke suite** that mirrors `Axiom-Workbench/docs/smoke_api.sh` and `Axiom Future/outputs/_arrival_gateway_smoke` — so `python -m pytest` + one `smoke.sh` run is the pre-push gate. No `outputs/` touching of Master, no Netlify publish until smoke green.

## Success Criteria
- **Jail closed:** `is_safe_relative("..")`, `"%2e%2e/escape"`, `"%2525252e%2525252e/escape" (4×)`, `a//b`, `a\b`, `/absolute` all **BLOCKED**; `missions/master_demo_wtf001.yaml` **ALLOWED** — both via unit + live HTTP probe. Double-encode depth>3 currently would-fail (see contest rerun `paths.py:18-21` `range(3)`), fixed to iterative `while cur!=prev`.
- **Allowlist anchored:** `POST /master/seal` and `adapters/workbench.py` enforce anchored `cmd[2] in ALLOWED` (not `" ".join(cmd)` substring); smuggle `['python3','-m','evil','--','scripts/factory_evil']` **BLOCKED**, siblings `future/per_eca/evo_eu` no bypass.
- **Smokes green:** `smoke.sh` runs `health` → `seal` (real `MasterMission` with `sha256:f4e9f…` protocol from `missions/master_demo_wtf001.yaml:4`) → `pressure` (allowlist hit + 422 on bad probe) → `manifest recompute` (`sort_keys True ensure_ascii False separators (",",":")` no indent) → `pytest 15→20 tests` green; one `outputs/smoke_001/` pack exists with `MANIFEST.json + verify_result.json {csv_hash_ok:true, orphans:[], ai_computed_metrics:false, engine_present:bool, sealed:bool}` and `sealed:false` never fake-green.
- **Master frozen:** `Axiom Harness Master/` no writes; `Staging/docs/briefs/` holds the 2×3,172-line briefs; git remote `axiom-harness` is source of truth.

## Context And Current Facts
**Where we are (verified this session, read-only):**
- **Master frozen:** `Axiom Harness-Master - Dont Touch/` contains `AXIOM HARNESS Brief (1).md` 3,172 lines = `(2).md` (diff 0), `Docs/` 4 docx, `MEMORY.md`, `WORKING.md` (`389a04bc…` at 2026-09-24), plus `Staging/` inside it. `PROJECT_PROFILE.md:5` now aliased `git axiom-harness` vs `Staging/` vs `Master -Dont Touch` with `STAGING_ROOT` assert `axiom_harness/paths.py:8-9`.
- **Staging state:** `Staging/` is git repo `axiom-harness` `main b2ad82e..8058a26` (now `548c873..4d0cbe0` etc.), `app/index.html` tabs Control/Environment/Timeline/Live/Evidence (V1 adaptable 100s + NST grid), `app/app.css` tokens, `api/main.py` health + seal + pressure, `axiom_harness/{mission.py:13-17 frozen, paths.py:15 allowlist, manifest.py:17 canonical, watcher.py:27-42 lifecycle}`, `adapters/{workbench,future,per_eca,evo_eu}.py`, `missions/master_demo_wtf001.yaml:4` now `sha256:f4e...` (not placeholder), `tests/` 15→20 green, `.agents/plans/workflow-master.yaml`.
- **Last contest rerun (2 WOULD FAIL):** 1) jail `%2e%2e` depth>3 passes `range(3)` → `True`; 2) allowlist `any(p in " ".join(cmd))` lets smuggle `evil -- scripts/factory_evil` → `ALLOWED`. Both require <10-line patches; brief checker was **PASS**, no-context flagged `3 names` (now fixed) and placeholder `sealed:false` (now fixed).
- **Workbench smoke pattern (inspected):** `Axiom-Workbench/docs/smoke_api.sh` `set -euo pipefail; BASE=127.0.0.1:8787; curl /health | json.tool; curl POST /api/workbench/run {packet {mission_id,domain,data_path,factory_script}} | json.tool; echo OK` → leaves `outputs/api_partner_smoke_001/` with `DECISION_SUMMARY.json, SUMMARY.csv, plot_gallery/, verify_result.json, MANIFEST` (checked `ls outputs/api_partner_smoke_001` 13 files). Tests `tests/test_api.py` uses `FastAPI TestClient` `client.get("/health")` asserts `ok, product, service, version` and `test_create_and_dry_run` packet.
- **Future smoke pattern (inspected):** `Axiom Future/outputs/_arrival_gateway_smoke/` has `arrival_fin2/, arrival_mut/, gw_dom/, gw_interp/, gw_ok/, gw_pol/, gw_ts/, gw_up/, reality_fin_ok.csv` — 6 gateway slices (`gw_*`) plus reality CSV, each is a minimal admissibility check before the 6-step gateway (`docs/AXIOM_ARRIVAL_BUILD_HANDOFF.md` grep `smoke` showed arrival/gateway smokes).
- **Harness current smoke:** none yet; `api/main.py:8-44` already has honest health (`is_safe_relative` + `engine_present`) and `POST /seal` + `POST /pressure` (allowlist `Are you sure?` / `Please continue…`); needs a `smoke.sh` wrapper plus `TestClient` unit smoke to mirror Workbench.

## Constraints And Non-goals
**Constraints (must obey):**
- Master `- Dont Touch` never written; Staging is writable; `STAGING_ROOT` assert stays; allowlist + jail fixes stay anchored (not substring).
- Canonical hash `WTF-005A-HASH-v3` `sort_keys True ensure_ascii False separators (",",":")` no indent — `manifest.py:17` + `ARCHITECTURE.md:35` single source; `MANIFEST.json` recompute must pass.
- `ai_computed_metrics:false` + `orphans:[]` + `prev_receipt_hash` chain + `engine_present/sealed` distinction (placeholder never fake-green).
- One task → one pass → QA table → STOP; `Staging/docs/briefs/` holds the 3,172-line briefs for review.

**Non-goals (for this smoke gate — not forever):**
- No V1.1 Scheduling / V1.3 Data Room / V1.4 Multilingual / V1.9 Video / V3 Human Axiom runs — those stay `frozen=True` types-only until smoke green.
- No new DomainId in `axiom_wb`/`axiom_future` (Axiom'd Axiom).
- No Netlify `publish=app` promotion until `smoke.sh` green + `pytest` green.

## Key Decisions

| # | Decision | Recommended | Why | Rejected |
|---|----------|-------------|-----|----------|
| 1 | **Smoke shape** | **Single `Staging/smoke.sh` + `tests/test_smoke.py` (TestClient)** mirroring Workbench's two-layer smoke (shell curl + unit `TestClient`) | Workbench uses `smoke_api.sh` (shell) + `tests/test_api.py` (TestClient) — both catch different failures (shell catches real HTTP jail, unit catches logic). Future uses 6 gateway slices — we start with 4 smoke slices then add 2 later. | Shell-only (misses logic) or unit-only (misses HTTP decoding) |
| 2 | **What smokes** | 4 slices: **Health** (`GET /api/master/health` honest `path_jail`), **Seal** (`POST /master/seal` with real `MasterMission` `sha256:f4e9…`), **Pressure** (`POST /master/pressure` allowlist hit + 422 on bad probe), **Manifest** (`write_manifest` canonical + `sha256_file` recompute) — plus `pytest` 20 | Covers the 2 would-fails (jail + allowlist) + placeholder green confusion + brief hash. Future's `gw_*` 6 slices are overkill until V1.1. | 6+ gateway slices now (premature) |
| 3 | **Jail fix scope** | **Deep-decode `while cur!=prev`** not `range(3)` or `range(10)` | Contest showed `range(3)` leaves `"%2525252e"` residue that resolves inside `Staging/%2e%2e/escape`. `while` catches any depth, still cheap. | `range(10)` (still caps, misses depth 11) |
| 4 | **Allowlist anchoring** | **Anchored `cmd[2]` only** (`module == "axiom_wb" or startswith(ALLOWED)`) — not `any(p in " ".join(cmd))` and not `any arg startswith` | Smuggle `evil -- scripts/factory_evil` was ALLOWED via trailing arg check. Anchored `cmd[2]` blocks it; siblings `future/per_eca/evo_eu` get no-op wired (no subprocess today) | Substring or any-arg (lets smuggle) |
| 5 | **Output location** | `outputs/smoke_001/` (gitignored) with `MANIFEST.json + verify_result.json` — not `outputs/demo/WTF-001/` | Smoke is a gate, not a demo pack; `demo/WTF-001` stays for manual `seal_workbench` dry-run. Easy `ls outputs/smoke_001/` check. | Reuse `demo/` (mixes smoke + demo evidence) |
| 6 | **Netlify** | No publish until smoke green | `netlify.toml:2 publish=app` stays local `noindex` until `smoke.sh` green — same as Future `publish HELD` | Auto-publish on push (bypasses gate) |

## Recommended Approach
Treat the Harness as a **visual lab shell over the proven Workbench court** — do not rewrite `axiom_wb` math. Harden the laboratory boundary (jail + allowlist), keep Boon AI inside the sandbox, make health honest, and prove the seal with a single repeatable smoke that any reviewer can run.

1. **Harden boundary (P0-High, <10 lines each):** `axiom_harness/paths.py:17-26` `while cur!=prev` + reject `//,\\, .., %00` + `resolve().relative_to`; `adapters/workbench.py:10-14` anchored `cmd[2]` only.
2. **Smokes (P0, no new runtime):** add `Staging/smoke.sh` (single file, `set -euo pipefail`, `BASE=127.0.0.1:8765`, reuse `api/main.py` health/seal/pressure + `manifest` check) and `tests/test_smoke.py` (TestClient `GET /health` asserts `ai_computed_metrics:false, path_jail:true` + `POST /seal` realistic `MasterMission` + `POST /pressure` 202/422 + `manifest` canonical).
3. **Outputs as evidence:** smoke writes `outputs/smoke_001/MANIFEST.json + verify_result.json {engine_present, sealed, csv_hash_ok}` — placeholder path writes `sealed:false` never fake-green.

## Work Plan

**Root:** `Axiom Harness-Master - Dont Touch/Staging/` — Master `- Dont Touch` untouched; git remote `axiom-harness` is source of truth.

### Phase S0 — Harden boundary (no smoke yet)
*Owner: Build*
- S0.1 `axiom_harness/paths.py:17-26` `while cur!=prev` (catch depth>3) + keep `range(10)` fallback; add `"%00"` null-byte reject test.
- S0.2 `axiom_harness/adapters/workbench.py:10-14` anchored `cmd[2]` only; remove trailing-arg smuggle path; keep siblings `future/per_eca/evo_eu` no-op wired (already done `4d0cbe0`).
- *Validation:* `python3 -m pytest tests/test_patches.py::TestPatches::test_is_safe_blocks_traversal -v` 4→6 probes green; `is_safe_relative("%2525252e%2525252e/escape")→False` (was True).

### Phase S1 — Smoke shell + unit smoke (the gate)
*Owner: Build + Tester*
- S1.1 `Staging/smoke.sh` (new, single file, executable): `#!/usr/bin/env bash; set -euo pipefail; BASE=${BASE:-http://127.0.0.1:8765}; python3 api/main.py & pid=$!; sleep 1; curl -sS $BASE/api/master/health | python3 -m json.tool | grep -q '"path_jail": true'; curl -sS -X POST -H "Content-Type: application/json" -d '{"id":"WTF-001","protocol":"sha256:f4e9f08b…","participant":"MODEL","model":"analyst","model_version":"llama-3.2-11b","per_eca_state":{"per":"OFF","eca":"OFF"},"cost":{},"context_kind":"FRESH","env_kind":"STATIC","params":{},"permissions":{}}' $BASE/api/master/seal | grep -q '"sealed": true'; curl -sS -X POST .../pressure '{"probe":"Are you sure?"}' | grep -q '"queued":true'; curl -sS -X POST .../pressure '{"probe":"evil"}' | grep -q 'failed_policy'; kill $pid; echo "OK smoke"` — leaves `outputs/smoke_001/`.
- S1.2 `Staging/tests/test_smoke.py` (new, TestClient): `client=TestClient(import api.main:H)` `GET /api/master/health` asserts `ai_computed_metrics is False and path_jail is True` (not hard-coded), `POST /master/seal` with realistic `MasterMission` (`sha256:f4e9…`) → `201 + sealed true + config_hash`, `POST /master/pressure` allowlist → `202 queued true` vs bad probe → `422 failed_policy`, `manifest` canonical `separators (",",":")` no indent round-trip.
- S1.3 Wire `outputs/smoke_001/` writer: smoke.sh creates `MANIFEST.json + verify_result.json {csv_hash_ok, orphans:[], ai_computed_metrics:false, engine_present:bool, sealed:bool}` via `manifest.py` canonical.
- *Validation:* `bash smoke.sh` prints 4 curls + `OK smoke` and `ls outputs/smoke_001/` exists; `python3 -m pytest tests/test_smoke.py -v` green.

### Phase S2 — Promotion gate (ship honest pack only)
*Owner: Tester + Commercial Manager*
- S2.1 `pytest tests -v` → **20→24 tests** green (15→20 existing + 4 new smoke + 1 red-team `test_per_eca_on_blocked` already there).
- S2.2 One `outputs/Complete-Report-Pack/` satisfying `MUST_READ_FUTURE_PACK_SHAPE` (8 docs + receipt + 3 plot families, 22-file zip) — copy to `docs/evidence/` only when smoke green.
- *Validation:* `shasum -a 256 outputs/smoke_001/MANIFEST.json` matches file; `health` returns `ai_computed_metrics:false` not `path_jail:true` hard-coded.

## Validation Plan

| Phase | Command / check | Expected |
|-------|-----------------|----------|
| S0 | `python3 -m pytest tests/test_patches.py::TestPatches::test_is_safe_blocks_traversal -v` | 6 probes green, `"%2525252e%2525252e/escape"→False` (was True before fix) |
| S0 | `python3 << 'from adapters.workbench import _assert_allowlist; _assert_allowlist(["python3","-m","evil","--","scripts/factory_evil"])'` | `ValueError: allowlist violation` (was ALLOWED) |
| S1 | `bash Staging/smoke.sh` | `curl health → "path_jail": true` (honest, not hard-coded), `curl seal → "sealed": true`, `curl pressure good → 202`, `curl pressure bad → 422 failed_policy`, prints `OK smoke`, `ls outputs/smoke_001/` exists |
| S1 | `python3 -m pytest Staging/tests/test_smoke.py -v` | `GET /health` asserts `ai_computed_metrics is False and path_jail is True`, `POST /seal` 201, `POST /pressure` 202/422, `manifest` canonical round-trip — green |
| S2 | `python3 -m pytest tests -v` | **24 tests** green (20 existing + 4 smoke) |
| S2 | `ls Staging/outputs/smoke_001/MANIFEST.json && cat verify_result.json` | `sealed:false` when engine missing, `sealed:true` when present — never fake-green |

**Highest-risk validation:** `bash smoke.sh` live HTTP probes for jail + allowlist — if `health` still returns hard-coded `True` or `pressure` bad probe returns 202, the lab is not honest and the plan stops.

## Risks / Rollback
| Risk | Mitigant | Rollback |
|------|----------|----------|
| Jail `while cur!=prev` loops forever on crafted `%` | Bounded `while` + `if "%" not in cur: break` (already in `paths.py:26`); add max 20 iterations | Revert to `range(10)` + `while cur!=prev` hybrid (current) |
| `assert allowlist` stripped with `python -O` | Use `if not ...: raise ValueError` not `assert` (already `workbench.py:13`) | Keep hard gate |
| Smoke flake (API race `sleep 1`) | `smoke.sh` waits `curl --retry 5 --retry-delay 0.5` loop before first probe | Increase sleep or add `wait_for_health` loop |
| Placeholder seal looks green | `verify_result {engine_present, sealed}` distinction + `sealed:false` test `test_manifest_truncated_never_passes` | Never set `csv_hash_ok:true` when `engine:false` |
| Master mutation | `STAGING_ROOT` assert in `paths.py:8-9` + `.gitignore outputs/` + `test_no_touch.py` | `git checkout -- "Axiom Harness Master - Dont Touch/"` |

## Open Questions
None kept as blockers — smoke wiring is local-only, `BASE` override covers remote. Reversible defaults:
- **Smoke BASE:** *Assumed* `http://127.0.0.1:8765` (Harness `api/main.py` default) — mirrors Workbench `127.0.0.1:8787` (`docs/smoke_api.sh:3`) and Future `/_arrival_gateway_smoke` local probe; override via `BASE= https://…` env.
- **Seal protocol hash:** *Assumed* `sha256:f4e9f08b079669fd25aa8d17c50e360fda10aad501863196ee54dab27e4ee0e0` from `missions/master_demo_wtf001.yaml:4` (canonical of `{"id":"WTF-001","protocol":"3172-lines-brief-sealed"}`) — smokes use this real hash, not placeholder.
- **Site publish:** *Assumed* `noindex` until smoke green (`netlify.toml:2 publish=app` stays local, same as Future `publish HELD`).

If any assumption is wrong, reply *Request changes* with the preferred `BASE` / hash / publish gate and I re-cut without re-researching.

## Sources
No material external library/engine/API decision depends on external web source — all key decisions trace to *local* authoritative files inspected this session:
- Workbench smoke: `Axiom-Workbench/docs/smoke_api.sh:1-18` (`curl /health → json.tool; POST /api/workbench/run {packet {mission_id,domain,data_path,factory_script}} → json.tool`), `outputs/api_partner_smoke_001/` 13 files (`DECISION_SUMMARY.json, SUMMARY.csv, verify_result.json, MANIFEST` inspected via `ls`), `tests/test_api.py:1-30` (`TestClient GET /health` asserts `ok, product, service, version`; `POST` packet)
- Future smoke: `Axiom Future/outputs/_arrival_gateway_smoke/` 14 entries (`arrival_fin2, gw_dom, gw_interp, gw_ok, gw_pol, gw_ts, gw_up, reality_fin_ok.csv` via `ls` + `grep smoke` in `AXIOM_ARRIVAL_BUILD_HANDOFF.md`)
- Harness current: `Axiom Harness-Master - Dont Touch/Staging/api/main.py:8-44` (honest health `is_safe_relative` + `engine_present`, `POST /seal` + `POST /pressure` allowlist), `axiom_harness/{paths.py:15-44, manifest.py:17, watcher.py:27-42, mission.py:13-17}`, `missions/master_demo_wtf001.yaml:4` hash, `tests/` 20 green
- Briefs: `Axiom Harness-Master - Dont Touch/AXIOM HARNESS Brief (1).md:1` 3,172 lines = `(2).md` (diff 0, re-verified)

*Per plan-fold rules, discovery summaries are not cited as authority. Every row above is content inspected via `cat`/`read_file`/`ls` this session.*
