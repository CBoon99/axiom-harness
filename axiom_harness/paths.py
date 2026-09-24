"""Paths — jail + allowed roots (review gap 4, contest hardening).

Decodes %2e etc, rejects absolute, normalizes, then resolve().relative_to.
"""
from pathlib import Path
from urllib.parse import unquote

STAGING_ROOT = Path(__file__).resolve().parents[1]
# Portability fix (REPAIR PHASE 2): repository-root discovery — no absolute/name-dependent assertion.
# Harness must run from any clone path containing expected Staging layout (axiom_harness/ + missions/ + tests/)
# Previously asserted "Axiom Harness-Master - Dont Touch/Staging" in path — forced exact absolute directory name.
# Now assert structure, not name: STAGING_ROOT must contain axiom_harness/ and be a Staging checkout.
if not (STAGING_ROOT / "axiom_harness").is_dir() or not (STAGING_ROOT / "missions").is_dir():
    raise RuntimeError(f"STAGING_ROOT mis-located {STAGING_ROOT}: expected Staging layout (axiom_harness/ + missions/)")

# inside Master, writable
STAGING_DOCS = STAGING_ROOT / "docs"
MISSIONS = STAGING_ROOT / "missions"
OUTPUTS = STAGING_ROOT / "outputs"  # gitignored staging outputs

ALLOWED_SCRIPT_PREFIXES = ["scripts/factory_", "AXIOM_"]  # allowlist — factory + AXIOM_* (TECH_SPEC §35)

def _decoded(p: str) -> str:
    # iterative unquote until stable — catches %2525252e depth>3
    prev = None
    cur = p
    for _ in range(10):
        if cur == prev:
            break
        prev = cur
        cur = unquote(cur)
        if "%" not in cur:
            break
    # second pass while still changing (defense in depth)
    while cur != prev:
        prev = cur
        cur = unquote(cur)
    return cur

def is_safe_relative(p: str) -> bool:
    d = _decoded(p)
    # reject absolute, backslash, double-slash, encoded traversal residue
    if d.startswith("/") or d.startswith("\\") or "\\" in d or "//" in d:
        return False
    # reject any .. segment after decode
    if ".." in d.split("/"):
        return False
    if ".." in d.split("\\"):
        return False
    # final normalization via resolve().relative_to
    try:
        (STAGING_ROOT / d).resolve().relative_to(STAGING_ROOT.resolve())
        return True
    except Exception:
        return False

def jail_for_experiment(experiment_id: str) -> Path:
    return OUTPUTS / experiment_id / "sandbox"
