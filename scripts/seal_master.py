#!/usr/bin/env python3
"""seal_master — dry-run orchestrator (P1 scaffold, no outputs).

Enumerates registry doors + draft manifest without touching outputs.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from axiom_harness.registry import REGISTRY

def main():
    print("Axiom Harness Master — dry-run seal (P1 scaffold)")
    print("Registry doors:", ", ".join(REGISTRY.keys()))
    for k, v in REGISTRY.items():
        print(f"  - {k}: {v}")
    print("Master brief: Axiom Harness Master/AXIOM HARNESS Brief (1).md 3172 lines (sealed)")
    print("WTF pin: WTF-005A-HASH-v3 sort_keys True ensure_ascii False")
    print("V1 leaves: workbench/future/per/eca/evocycles/epistemic/human(V3 reserved)")
    print("Dry-run OK — no outputs touched.")

if __name__ == "__main__":
    main()
