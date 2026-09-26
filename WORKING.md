# WORKING — Axiom Lab Harness Staging — Active Risks & Gates — 2026-09-26

## Active Known Risks (do not hide)
- **per_eca_state inner dict mutability:** `axiom_harness/mission.py` `MasterMission.per_eca_state: dict = Field(default={"per":"OFF","eca":"OFF"})` is outer `frozen=True` but inner dict remains mutable (`mission.per_eca_state["per"]="ON"` would mutate without error). Risk: silent PER/ECA ON bypass despite `frozen` + `adapters/per_eca.py ensure_off()` gate. Mitigation: `ensure_off()` raises `HarnessBoundaryError` if ON, + `test_harness_boundary` checks, but inner mutation still possible until migrated to `FrozenDict` / `Literal` enum. Owner: Carl — accept as known risk until V1.10 PER wiring.
- **AXIOM_ broad allowlist:** `axiom_harness/paths.py ALLOWED_SCRIPT_PREFIXES` keeps broad `AXIOM_` (G10) until tests migrate to `AXIOM_WB_`. Broad match could allow non-workbench scripts. Gate kept narrow at `axiom_harness/registry.py owner:axiom-harness` (G8) as constraint. Plan: tighten to `AXIOM_WB_` only after `test_allowlist_anchored` + `test_patches` migrate.

## Narrow Gates Held (G8/G10)
- **G8 owner:axiom-harness:** `axiom_harness/registry.py` asserts `owner == "axiom-harness"` — all events must carry qualifier.
- **G10 AXIOM_ broad:** See risk above — intentionally broad until migration.

## Verification (this commit)
- `PYTHONPATH="$PWD" /Library/Developer/CommandLineTools/usr/bin/python3 -m pytest -q` → 139 passed
- `smoke.sh` → 5/5

*Updated per House Order §36 2026-09-26.*
