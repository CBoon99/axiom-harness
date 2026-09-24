# Axiom-Harness — MEMORY.md

> Durable operator memory for Axiom-Harness · Read by every session before work
> Complements `WORKING.md` (which is the append-only action ledger)
> Last updated: 2026-09-24T05:38 UTC · Session: sunny-fornax

---

## 1. Operator & Authority

| Item | Value |
|------|-------|
| Operator | Carl Boon — Founder & Chief Systems Architect, BoonMind Labs |
| Authority | `Documents/agent-standards/AGENT_STANDARDS.md §9` + `BML-OVERRIDE-PROTOCOL-V1.md` — A1 approval/commit separation, A2 sovereign methodology override (reframe-first) |
| Methodology Canonical | `Documents/agent-standards/BML-METHODOLOGY-CANONICAL-V1.md` (doc_id BML-METHODOLOGY-CANONICAL-V1) — **read-only**, never fork |
| Contact | info@boonmind.io · gsrf@boonmind.io |

**Locked names:** BoonMind Labs · Zero Overshoot · Axiom Workbench · GSRF (method) · Candidate_Zero / Reference_Standard (eval labels) · BoonMind Hub (internal). When in doubt — **Push Back or Ask**, do not invent.

---

## 2. Thesis (From Methodology §1.1 — pointer, not copy)

> Modern systems fail via **uncontrolled overshoot** — mid-band resonance, hallucination loop-drift, affiliate distortion, emotional dysregulation. BoonMind Labs builds **governors** — closed-loop control layers that clamp chaotic inputs to pre-declared, bounded, cryptographically verifiable setpoints.

Harness exists to **govern harness execution** — same pathology, different surface: bulk Axiom runs without path escape, without recomputing metrics in LLM, without inventing wins.

---

## 3. BML Quad — Invariant for Every Run

Every product, including this harness, implements the identical four-stage control pipeline (Methodology §2):

1. **Pre-Declared Rules (Setpoint Lock)** — mission_id, domain, column_mapping, loss_weights, thresholds, pack caps frozen BEFORE data
2. **Frozen Evaluator (Static Controller)** — `axiom_wb` baselines + metrics; cannot retune mid-run
3. **Deterministic Engine (Governor)** — causal only, gap-aware, `path jail`, `sha256`
4. **Honest Cryptographic Verdict** — `loss` published equals `clear_win`; `FINAL_REPORT.md` cites ledger or writes `NOT IN ARTEFACTS`

No stage is complete because an agent says so — completion requires evidence (GABS §1).

---

## 4. Harness Invariants (What Must Never Break)

### 4.1 Engine is upstream, read-only
* Engine path: `Documents/Axiom-Workbench/axiom_wb/` — never copy, never vendor, never reimplement `wear_proxy` etc. here.
* `Documents/Axiom-Workbench` is the **evidence root** for sealed packs. Harness `outputs/` is ephemeral; promotion is explicit copy to `docs/evidence/` or back to upstream `docs/evidence/lab_home/`.

### 4.2 No AI math
* `ai_computed_metrics` is always `false`. See `core_types.py:422`, `pipeline.py:375`, `package.py:457`, `verify.py:113`.
* LLM may: read mission packet → invoke factory via service bridge (`python3 -m axiom_wb evaluate`) → read files → format FINAL_REPORT from files → inventory + hash.
* LLM may NOT: invent scores, do arithmetic in prompt, reimplement GSRF/EMA, estimate numbers, generate synthetic plots.

### 4.3 Evidence hierarchy
* **Ledger > narrative.** If prose and `SUMMARY.csv` / `DECISION_SUMMARY.json` disagree, fix prose, not ledger.
* **Red lights stay.** Failures from factory ledgers appear in FINAL_REPORT — never stripped.
* **Orphan check:** every number in FINAL_REPORT must appear verbatim in ledger corpus — `verify.py:NUM_RE` — or mission is `failed_policy`.

### 4.4 Local-first
* Product root `Documents/Axiom-Harness/` is local-only until Carl says `push live` / `go push` (AGENT_STANDARDS §4).
* No VPS as default evidence store. No auto `web_publish`.
* No `../Axiom-Harness` duplication outside this root.

---

## 5. Related Projects (Pointers — not copies)

| Project | Path | Relationship |
|---------|------|--------------|
| Axiom-Workbench | `Documents/Axiom-Workbench/` | **Upstream court** — deterministic evaluator, 4 phases of methodology embodied in code |
| agent-standards | `Documents/agent-standards/` | **Live standards** — AGENT_STANDARDS, GABS v1.1, BML-CODE-HYGIENE, BRAND-GUIDE, METHODOLOGY canonical |
| BoonMind-Methodology | `Documents/BoonMind-Methodology/` | **Git-tracked Methodology repo** — live, own remote; stale copy `BoonMind-Methodology (read this first)/` is gitignored, do not read |
| Boon Global Mind | `Documents/Boon Global Mind/` | **MIND-MANIFEST** — always-load pointer tier (~800 bytes); load full only when pointer fires |
| Epistemic-UX-Stress-Harness | `Documents/Epistemic-UX-Stress-Harness/` | Peer harness — separate surface, do not conflate |
| Axiom Evidence Layer | `Documents/Axiom Evidence Layer/` | Evidence symlink tree (`PER-Core`, `CUAD-RealData`) — read-only data source |

---

## 6. Operator Constraints (Remember Every Session)

1. **Budget:** Carl is budget-constrained (2026-08-15 lock). One task → one pass → QA table → STOP. No second marketing pass. No "improve tone." If unsure: ASK once.
2. **Labs marketing LOCKED.** Do not touch `BoonMind Labs/site` homepage/product framing unless Carl names a specific bug. Text changes = WORD-FOR-WORD only.
3. **Cost hygiene:** Meta/sitemap/string replace/301 = cheap path. Top model only for architecture, novel bugs, claim/legal, or Carl-named hard problems. No repo-wide archaeology unless asked.
4. **STOP conditions:** After QA table, STOP. Residual → list for Carl; no auto-expand. No "while I'm here" unless 1-line in named files.
5. **Push Back or Ask:** Brand / IP / history / naming — stop, do not hallucinate name, date, or claim. Permission to stop rather than invent.
6. **10 terminal windows:** Carl runs 10 terminals — context may be split across windows; if something seems out of context, check.

---

## 7. Harness Lifecycle (GABS v1.1 — applied to harness itself)

For any new harness feature (bulk runner, evidence promotion, new domain adapter):

```
UNDERSTAND → CLASSIFY RISK → RETRIEVE MINIMUM CONTEXT → DISCOVER → PLAN → CHALLENGE
→ SECURITY/PRIVACY REVIEW (if needed) → PREPARE SAFE ENV → BUILD → BUILDER SELF-CHECK
→ TECHNICALLY VERIFY → INDEPENDENT PRODUCT TEST → RECONCILE DOCS → ASSEMBLE EVIDENCE
→ ACCEPTANCE → RELEASE → POST-RELEASE OBSERVATION → LEARNING CAPTURE
```

* No agent may treat implementation as completion. Completion requires evidence.
* Builder ≠ accepter. Green tests ≠ human approval (AGENT_STANDARDS §3).

---

## 8. Learned Invariants (Append over time — never delete history)

| Date | Invariant | Source |
|------|-----------|--------|
| 2026-09-24 | `Axiom-Harness` root must stay dedicated child — `Documents/` is home-like, never scaffold there directly | `greenfield-project-scaffolding:5` |
| 2026-09-24 | Methodology is read-only — cite by doc_id + path, never fork wording | `BML-METHODOLOGY-CANONICAL-V1:0` |
| 2026-09-24 | WORKING.md is append-only ledger — every action gets a row in §4 changelog | Operator: "save everything all actions in working.md" |
| 2026-09-24 | Harness calls engine, never reimplements it — prevents Frozen Evaluator violation | Methodology §2 Stage 2 + BINDING_RULES R2/R3 |

---

*Append new memory below — never overwrite above. WORKING.md holds the action log; this file holds the durable invariants those actions taught.*
