# FRESH-CLONE FINDING — the entire API fails to import outside this exact folder name

**Date:** 2026-09-24 · **Verified independently, fresh clone, not taken from any prior audit.**

`docs/AUDIT_MASTER_GAPS_HALLUCINATIONS.md` reports `104 passed, 2 warnings` and calls the path
jail (`axiom_harness/paths.py`) "correctly anchored." **Reproduced locally: true, exactly
104 passed.** Reproduced from a fresh clone into a differently-named directory: **the entire
test suite fails to collect, and the API itself cannot import.**

## Root cause

```python
# axiom_harness/paths.py:8-10
STAGING_ROOT = Path(__file__).resolve().parents[1]
assert "Axiom Harness-Master - Dont Touch/Staging" in str(STAGING_ROOT) \
    or "Axiom Harness Master" in str(STAGING_ROOT), f"STAGING_ROOT mis-located {STAGING_ROOT}"
```

The security jail's root is not derived from a config value, an environment variable, or the
package's own install location in any portable way — it is a **hard string match on the literal
folder name Carl's Mac happens to have it in.** `api/main.py:5` imports this module directly.

## Verified

```
$ git clone .../Staging /tmp/fresh-harness
$ cd /tmp/fresh-harness && python3 -m pytest tests/ -q
Interrupted: 9 errors during collection
AssertionError: STAGING_ROOT mis-located /tmp/fresh-harness

$ python3 -c "from api import main"
AssertionError: STAGING_ROOT mis-located /tmp/fresh-harness
```

**This is not a test-only issue. The production API entrypoint (`api/main.py`) cannot boot at
all** the moment this code is deployed anywhere — a container, a CI runner, a colleague's laptop,
a renamed folder — that isn't named exactly `Axiom Harness-Master - Dont Touch/Staging` or
containing the substring `Axiom Harness Master`.

## Same class as today's other two findings, a third time, in a third project

BoonMind Trader (F1, F8, F10), ECA (`ea61f41`), and now this: **a green result — `104 passed` —
that depends on an environment-specific condition invisible to the report that claims it.**
`AUDIT_MASTER_GAPS_HALLUCINATIONS.md` re-read this exact file (`paths.py:19-51`) in its own §Evidence
section and called the anchor "correctly anchored" without cloning fresh to check what "anchored"
was anchored *to*. Same mechanism each time: a check ran, returned green, and nobody asked whether
the check could have returned anything else.

## Fix (not implemented here — report only)

`STAGING_ROOT` should be derived from an environment variable (`AXIOM_HARNESS_ROOT`) with the
current `Path(__file__).resolve().parents[1]` as a documented, non-asserted default — matching
the lazy-resolution pattern already proven correct today in a different project (BoonMind Trader
P16 rev 3, `boonmind/strategy_config.py`, dependency injection over a hard-coded assumption).

**Not implemented. No code changed. Report only.**
