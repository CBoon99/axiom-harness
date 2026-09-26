# SETUP — Axiom Lab Harness — 2026-09-26

**No magic steps — every verbally-remembered step now written.**

## Required
- `Staging/` root with `axiom_harness/ + missions/ + tests/ + app/ + docs/ + proof/ + outputs/`
- Python `/Library/Developer/CommandLineTools/usr/bin/python3` (`3.9.6`, pinned in `.python-version`) with `pydantic 2.5.0 + pytest 7.4.3` (default `python3` has no pydantic due to `platform.mac_ver ''`) — verify `pydantic.__version__ == "2.5.0"` via that binary
- `agent-browser 0.34.0 + Chrome 152` at `~/.agent-browser/browsers`

## One-liner (stranger cold run)
```bash
PYTHONPATH="$PWD" PATH="/Library/Developer/CommandLineTools/usr/bin:$PATH" /Library/Developer/CommandLineTools/usr/bin/python3 -m pytest -q
env PYTHONPATH="$PWD" PATH="/Library/Developer/CommandLineTools/usr/bin:$PATH" bash smoke.sh
```
Pinned: `.python-version` `3.9.6` — use CLT python only, never `python` or system `python3` without PATH override.

## Environment
- **Mandatory:** `STAGING_ROOT = Path(__file__).parents[1]` asserts `axiom_harness/` exists
- **Optional:** `AXIOM_ENGINE_ROOT` (only if `AXIOM_STRICT_MODE=0` — default `1` locks to `Path(__file__).parents[1]` per `config.py:14`), `HARNESS_PORT` (default `api/main.py` `HTTPServer` port), `AXIOM_STRICT_MODE`
- Verify: `env PYTHONPATH="$PWD" PATH="/Library/Developer/CommandLineTools/usr/bin:$PATH" bash smoke.sh` → `5/5` (`health jail OK, seal validates, pressure allowlist OK, manifest canonical OK, orphans 0`)

## Isolation verified
`axiom_harness/paths.py is_safe_relative iterative unquote depth 10 + resolve().relative_to` + `MANUAL jail_for_experiment` `outputs/<id>/sandbox` — verified via `test_jail_canonical`.

## First smoke
`PYTHONPATH="$PWD" /Library/Developer/CommandLineTools/usr/bin/python3 -m pytest -q` → `139 passed` HEAD `f024fee` — `file://` headless `agent-browser doctor` → `8 pass` with `require_escalated`.

## Healthy vs failure
- **Healthy:** `139 passed, 2 warnings→0` after `protected_namespaces=()`, `smoke 5/5`, `B.prev=A` chain.
- **Failure:** `Operation not permitted` on socket without `require_escalated`, `ModuleNotFoundError` without `PYTHONPATH`, `orangs[]` orphan → `failed_policy`.

## Logs / receipts
`outputs/<RUN>/` (`RECEIPT`, `manifest-sha256.txt`), `proof/HARNESS_PREFLIGHT_*.json`, `/tmp/full11-*.png` (22 headless), `/tmp/v18* + /tmp/human.png`.

*House Order §19 — read-only.*
