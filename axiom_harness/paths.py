"""Paths — jail + allowed roots (review gap 4).

No .., no absolute traversal, sorted by Staging only.
"""
from pathlib import Path
import pathlib

STAGING_ROOT = Path(__file__).resolve().parents[1]

# inside Master, writable
STAGING_DOCS = STAGING_ROOT / "docs"
MISSIONS = STAGING_ROOT / "missions"
OUTPUTS = STAGING_ROOT / "outputs"  # gitignored staging outputs

ALLOWED_SCRIPT_PREFIXES = ["scripts/factory_", "AXIOM_"]  # allowlist — factory + AXIOM_* (TECH_SPEC §35)

def is_safe_relative(p: str) -> bool:
    if ".." in p or p.startswith("/"):
        return False
    # no traversal
    try:
        (STAGING_ROOT / p).resolve().relative_to(STAGING_ROOT.resolve())
        return True
    except Exception:
        return False

def jail_for_experiment(experiment_id: str) -> Path:
    return OUTPUTS / experiment_id / "sandbox"
