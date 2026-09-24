"""Paths — jail + allowed roots (review gap 4, contest hardening).

Decodes %2e etc, rejects absolute, normalizes, then resolve().relative_to.
"""
from pathlib import Path
from urllib.parse import unquote

STAGING_ROOT = Path(__file__).resolve().parents[1]

# inside Master, writable
STAGING_DOCS = STAGING_ROOT / "docs"
MISSIONS = STAGING_ROOT / "missions"
OUTPUTS = STAGING_ROOT / "outputs"  # gitignored staging outputs

ALLOWED_SCRIPT_PREFIXES = ["scripts/factory_", "AXIOM_"]  # allowlist — factory + AXIOM_* (TECH_SPEC §35)

def _decoded(p: str) -> str:
    # iteratively unquote to catch %252e
    prev = None
    cur = p
    for _ in range(3):
        if cur == prev:
            break
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
