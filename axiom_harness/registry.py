"""Registry — 7 door table (read-only contracts, never hard-code WTF/PER/ECA in routes).

Pin hashes for upstream drift detection (PLAN_V1 Risks).
"""
REGISTRY = {
    "workbench": {"path": "Axiom-Workbench/", "seal": "DELIVERY 22-file zip", "hash_pin": "core_types 0f0f70fa"},
    "future": {"path": "Axiom Future/", "seal": "5-file SCENARIO+csv+manifest+verify+zip chain B.prev=A", "hash_pin": "policy.py ca51a986"},
    "per": {"path": "Axiom Evidence Layer/PER-Core", "gate": "owner:axiom-harness |R|<=3 OR weight>=75 OR ent>=4, ΔH>0.5", "mode": "OFF in V1"},
    "eca": {"path": "Axiom Evidence Layer/ECA", "gate": "owner:axiom-harness |R|<=3 && ΔH>0.5 && sealed+hash && FALSIFY", "mode": "OFF in V1"},
    "evocycles": {"path": "World-A-EvoCycles/", "seal": "harness/run.py receipts 220", "mode": "harness-only"},
    "epistemic": {"path": "Epistemic-UX-Stress-Harness/WTF-005A", "contract": "WTF-005A-HASH-v3 sort_keys True ensure_ascii False", "mode": "leaf"},
    "human": {"path": "Human Workbench/", "receipt": "RESULT+EVIDENCE+METHOD+COMPARISON+STABILITY+VERSION+SIGNATURE", "mode": "V3 reserved"},
}

def list_doors():
    return list(REGISTRY.keys())
