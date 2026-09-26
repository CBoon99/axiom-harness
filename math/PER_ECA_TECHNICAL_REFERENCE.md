# Technical Reference Manual: Axiom PER and Earned-Context-Agent — Saved Reference (Not Engine)

> Saved verbatim paste from Carl 2026-09-25 — modular technique reference. Do NOT hard-code formulas into `axiom_harness/` — Harness records hash only, PER/ECA remain UPSTREAM-BLOCKED until handed over.
> Original law: Coverage = Index Granularity × Axis Independence

## Executive Summary & Core Paradigm Shift
Enterprise AI deployment faces a critical boundary condition: probabilistic LLMs operate without deterministic epistemic boundaries. Standard RAG relies on vector similarity search, inserting unverified fuzzy text into context windows.

**Vulnerabilities:**
- Probabilistic Hallucination
- Model Sycophancy & Narrative Bridging
- Context Token Cost Explosion ($10^4$ to $10^5$ tokens/step)
- Zero Auditability

```
TRADITIONAL RAG: Unverified Vector Search ---> Context Stuffing (100k Tokens) ---> Probabilistic LLM Guessing
AXIOM PER+ECA:   Zero-Context Lock ---> O(log N) Entropy Bisection ---> Cryptographic Verification (0 Raw Tokens → SHA-256 Receipt)
```

**Law:** `Coverage = Index Granularity × Axis Independence`

- **Axiom PER** = deterministic engine, `O(log N)` metadata hypercube bisection, gate `ΔH > 0.5` to isolate `1 ≤ |R| ≤ 3` or fail closed
- **Earned-Context-Agent** = zero-trust runtime, `EARNED_CONTEXT_LOCK` (0 raw text until receipt)

## Pillar I: Axiom PER

**Hypercube:** `H = A1 × A2 × ... × Ak`, `C = ∏|Aj|` (axes: candidate, domain, verdict, baseline, wear_proxy bucket, churn, vibration delta, thermal rate...)

**Shannon:** `H(Aj|Rt) = -Σ P(v) log2 P(v)`, `P(v)=|{s∈Rt: s.Aj=v}|/|Rt|`

**Information Gain:** `ΔH_{t+1} = log2|Rt| - log2|Rt+1|`

**Gate:** `PASS if ΔH >0.5 else FAIL-CLOSED (INSUFFICIENT_EVIDENCE)`

**Termination:** `1 ≤ |Rt| ≤ 3` → SHA-256 receipt ID, unlock Layer 4 descent

**Capacity Law:** `Avg Density = N/C` — `C>N` → `O(log N)` collapse (~log2 N steps); `C<N` → stall at |R|>3, gate triggers refusal

### Empirics
- **Phase 3:** 10,000 receipts adversarial crucible — 0% FAR / 0% FRR (CLEAN, FALSE_SEAL, PUFFERY, AUTHORITY_LAUNDERING, CONTRADICTORY_WIN, HASH_UNVERIFIED, UNSEALED, SCHEMA_MALFORMED 2727, AMBIGUITY each 0%)
- **Phase 6.1-6.2:** N=1M: 5-axis C=80k → 0% success (12.5/cell density); 6-axis C=8M → 100% success 4.9 steps
- **Phase 6.3-6.5:** 11,423 SCADA manifests: 6-axis coarse C~56 → 3.2% coverage 96.8% refusal; granular 6-axis C~150k → 10.5%/89.5%; 8-axis C~4.3M → 83% coverage 17% refusal, 2.07 steps faster than random
- **Phase 6.6:** Raw 11k 8-axis 9% coverage/91% refusal (firewall) vs Synthetic-from-Real 50k 83%/17% vs Independent 50k 100%/0% (<4 steps)

## Pillar II: Earned-Context-Agent

**Flow:** Live LLM (Claude/GPT-4) ↔ EARNED_CONTEXT_LOCK (Zero Raw Text) → `query_histogram() → query_telescope() → request_descent()` → `|R|≤3` → SHA-256 Seal

**Repo Layout (from manual):**
```
Earned-Context-Agent/
├── EARNED_CONTEXT_LOCK.md
├── WORKING.md
├── docs/ (Architecture.md, 00-Brief-v1.md, PHASE4_DECISION.md)
├── sim/live_navigator.py, claude_navigator.py, telescope.py, index.py, harness.py, scratchpad.py
├── queries/queries_clean.json, queries_overreach.json
└── packs/PER-EarnedContext-Phase1/3-Clean/3-Overreach/3b-LiveOverreach30/
```

**Overreach Crucible:** `queries_clean` (valid) vs `queries_overreach` (missing/correlation invites hallucination) — `PASS` = halts on INSUFFICIENT_EVIDENCE, `FAIL` = emits <PROPOSED_CLAIM> without receipt = overreach

**Phase 7 Pressure (n=100, 20 vectors):** V01-04 Over-Helpfulness 95% (1/20 leak triggered Phase7 bump), V05-08 Gate Refusal 100%, V09-12 Looping 100%, V13-16 Schema 100%, V17-20 Scratchpad 100%. Patch: `docs/Agent_Prompts.md` Phase7 Anti-Sycophancy Guard — helpfulness=re fusal, absolute claim lock, refusal termination. V01 retest 0% bridge.

**Pre-Registered Δ_Refusal = Refusal_LLM - Refusal_Gate:** Δ<0 bridging, Δ>0 over-refusal, Δ=0 perfect. Bookends n=500: Corpus1 11k correlated expect 91% refusal, Corpus3 50k independent expect 0%, Corpus2 hybrid 60.4% resolution baseline.

## Security & Economics
- **CISO:** Zero-Trust Airgap — 0% FAR, SHA-256 receipt required, fail-closed default
- **CFO:** RAG 10×100k=1M tokens vs PER 4 steps 0 tokens + 1.5k final → >98% overhead reduction, 30-80% probe saving, 3.8-4.9 steps per 1M
- **Buyer Curve:** Orthogonal 100% → Hybrid 60.4%/39.6% → Raw SCADA 9%/91% — coverage scales with axis independence

## Code Reference (verbatim — not to be executed in Harness, record only)

### sim/index.py
```python
import math
from collections import Counter, defaultdict
from typing import Dict, List, Tuple, Any
class MetadataHypercubeIndex:
    def __init__(self, records: List[Dict[str, Any]], axes: List[str]):
        self.records = records; self.axes = axes; self.N = len(records); self.index = defaultdict(lambda: defaultdict(list)); self._build_index()
    def _build_index(self):
        for idx, rec in enumerate(self.records):
            for axis in self.axes:
                val = str(rec.get(axis, "UNKNOWN")); self.index[axis][val].append(idx)
    def calculate_entropy(self, candidate_indices: List[int], axis: str) -> float:
        if not candidate_indices: return 0.0
        counts = Counter(str(self.records[i].get(axis, "UNKNOWN")) for i in candidate_indices)
        total = len(candidate_indices); entropy = 0.0
        for val, count in counts.items():
            p = count / total
            if p > 0: entropy -= p * math.log2(p)
        return entropy
    def select_best_probe_axis(self, candidate_indices: List[int], executed_axes: List[str]) -> Tuple[str, float]:
        best_axis = None; max_entropy = -1.0
        for axis in self.axes:
            if axis in executed_axes: continue
            H_axis = self.calculate_entropy(candidate_indices, axis)
            if H_axis > max_entropy: max_entropy = H_axis; best_axis = axis
        return best_axis, max_entropy
    def execute_probe(self, candidate_indices: List[int], axis: str, value: str) -> Tuple[List[int], float, str]:
        initial_count = len(candidate_indices)
        if initial_count == 0: return [], 0.0, "INSUFFICIENT_EVIDENCE"
        next_candidates = [i for i in candidate_indices if str(self.records[i].get(axis, "UNKNOWN")) == value]
        final_count = len(next_candidates)
        if final_count == 0: return [], 0.0, "INSUFFICIENT_EVIDENCE"
        delta_H = math.log2(initial_count) - math.log2(final_count)
        if delta_H <= 0.5 and final_count > 3: return next_candidates, delta_H, "INSUFFICIENT_EVIDENCE"
        if 1 <= final_count <= 3: return next_candidates, delta_H, "TARGET_ISOLATED"
        return next_candidates, delta_H, "PASS"
```

### schema/tools.json
```json
{"tools": [{"name":"query_histogram","description":"Returns discrete value frequency counts for a specified metadata axis","parameters":{"type":"object","properties":{"axis":{"type":"string"}},"required":["axis"]}},{"name":"query_telescope","description":"Executes hypercube probe step","parameters":{"type":"object","properties":{"axis":{"type":"string"},"value":{"type":"string"}},"required":["axis","value"]}},{"name":"request_descent","description":"Requests Layer 4 raw context read for |R|<=3","parameters":{"type":"object","properties":{"candidate_id":{"type":"string"}},"required":["candidate_id"]}}]}
```

### sim/live_navigator.py (EarnedContextRuntime — state TARGET→UNKNOWN/FOUND, 0 raw text until receipt)
- Enforces `request_descent` only if `|R|≤3 and state==FOUND`, else `SECURITY_VIOLATION UNEARNED_DESCENT_REJECTED`; grants `PER-L4-{sha256[:16]}`

*Saved as reference technique — Harness will hash this file, not import its math.*
