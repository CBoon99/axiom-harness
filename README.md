# Axiom-Harness-Staging — Staging for Axiom Harness Master

**Status:** `HARNESS_V1_REPRODUCIBLE_PASS` — **HEAD `e6754e1` 2026-09-26 22:15** — `149 passed 0 warnings, smoke 5/5` (`PYTHONPATH="$PWD" /Library/Developer/CommandLineTools/usr/bin/python3 -m pytest -q`) — gates `c6a880a plan seal c55a0ed4 → 7df9aae Phase 1 AXIOM_WB narrow + hallmarks 143 → 3719d88 Phase 2 FrozenDict + PerConfig/EcaConfig + LOCK-STATUS 147 → e6754e1 Phase 3 VisualConfig 393,216:1 + 22-file pack 149` + `HARNESS_AUDIT_2026-09-26.md §35 A→Z` — **Master (`Axiom Harness Master/`) FROZEN `-do not touch` at 2026-09-24 05:39** unchanged — this folder is the writable Staging where V1→V2+ built — **cold-run: `git clone file:// → 149 passed + 5/5 + file:// 200` green unaided.**

**Briefs (inside Master, read-only):**
- `Axiom Harness Master/AXIOM HARNESS Brief (1).md` 3,172 lines
- `Axiom Harness Master/AXIOM HARNESS Brief (2).md` identical
- `Docs/Copy of AXIOM HARNESS Brief LVM addition not master.md` identical, marked not master

**What Master will become (from briefs):**
> **Humans configure the laboratory. AI operates inside the laboratory. The Harness records the laboratory. The evidence layer seals the laboratory.**

Stack: `HUMAN → HARNESS-CONTROL → CONFIG → SEALED ENV → BOON AI/other models → SANDBOX/TERMINAL/TOOLS/DATA/SENSORS → EVENT+TRANSCRIPT+STATE → EVIDENCE LAYER → ANALYSIS → REPORT/REVIEW/EXPORT`

Golden Rule: **AI DOES NOT CONTROL THE LABORATORY.** Proposal → human approves → Harness executes → recorded.

**Revolutionary brief V2 (Patch is ONE room):** This is not a boring harness — it is a sealed 4D laboratory where AI is inside, observed over time, converted to sealed evidence. **100+ WTF/WOW** tags: `#AI-Inside-The-Experiment` `#Timeline-As-4D-Object` `#Boundary-As-Data` `#Watchers-Observe-Not-Interpret` `#Terminal-As-Substrate` `#Counterfactual-Branching` `#Live-Observatory` `#Language-As-Variable` `#Audio-As-First-Class-DAW` `#Speech-As-Data` `#Failed-Policy-Events-Are-Data` + 90 more. Mechanics boring (bounded/recorded/versioned/sealed), **experiments wild** (psychology, physics, sci-fi, quantum — same AI tested language drift Monday / memory Tuesday / patch Wednesday / bias Thursday with same seal/chain).

**Visual Perception Room (V1.8 — ONE of 15):** Compression Receipt `1024×1024→224×224→14×14→768-dim→576 tokens→8 words (393,216:1, 99.99% gone)` + `What-Did-You-Miss` + `Mona Lisa` + `Embodiment Divide` + `Bias Laundering` + `LLM vs VLM vs LVM` — experiment family WTF-VIS-001…014 only. Revolution is whole lab, not vision trick. See `docs/BRIEF_REVOLUTIONARY_V2_PATCH_IS_ONE_ROOM.md`.

**V1 (proven 108/108):** Control + Model connection (Secret Manager `••••`) + Sandbox (terminal substrate — jail `is_safe_relative` iterative unquote, allowlist `scripts/factory_* AXIOM_*` on `cmd[2]`, timeout 3600) + Run (One/Sequence/All/Parallel/Pause-Resume/Restart + `ParallelConfig 1..64`) + Live Room + Timeline (scrubbable `◆/╱╲` + synchronized replay) + Evidence (6-file seal `SCENARIO.json/scenario.csv/DECISION_SUMMARY/MANIFEST/ECA_GATED_RESULTS/verify_result` + chain `B.prev=A` + `WTF-005A-HASH-v3` `sort_keys True ensure_ascii False (",",":")`) + Analysis + Export (Complete Report Pack 22-file). Proven: V1.1 Scheduling → V1.2 Parallel → V1.3 Data → V1.4 Multilingual → V1.5 Speech/Audio → V1.6 Sensors → V1.7 Live feeds + Observatory — all `POST /master/* 201/422` + `frozen=True` — `smoke.sh 5/5`. Next V1.8 Multi-agent → V1.9 Video → V2 Films → V2+ Observatory → Future External API → V3 Human Axiom. See `docs/MATH_MODULAR_MAP.md` (registry) + `HARNESS_BOUNDARY_AUDIT_2026-09-24.md` (HARNESS_BOUNDARY_CLEAN) + `HARNESS_V1_FINAL_ACCEPTANCE_2026-09-24.md` (REPRODUCIBLE PASS).

**Philosophy:** Keep laboratory boring, make experiments interesting — bounded, recorded, versioned, sealed, reproducible, modular, auditable, fail-closed. Patch Illusion is one wild experiment among 100+ — not the product.

**How we keep Master untouched:**
- `Axiom Harness Master/` stays witness until you approve a promotion.
- This `Axiom-Harness-Staging/` is where `missions/`, `axiom_harness/`, `docs/`, `app/`, `site/`, `tests/` will land.
- Private recall notes stay in `/tmp/axiom-*-private-notes.md` (119 + 123 + 123 lines) — not in Master.

**Next:** V1.8 Multi-agent (`one frozen MultiAgentConfig + one app/ room + one POST /master/multi-agent 201/422 + three durable tests`) — see `docs/HANDOFF_2026-09-24_FULL_ACCOUNT.md` §How to pick up. Do not push to `origin/main` until `push live` / `go push` — local only, every gate separate commit, never amend.

Frozen docs: `docs/HARNESS_BOUNDARY_AUDIT_2026-09-24.md` (`HARNESS_BOUNDARY_CLEAN`) + `docs/MATH_MODULAR_MAP.md` (registry `ECA/plugin/ e3c508b2… + config 1be70761…` `HISTORICAL bf7329c8…`, not certified) + `docs/FREEZE_V3_2026-09-24_ON_HOLD.md` (`ON HOLD` at `b2fca7e` — do not un-hold without audit closure).

Superseded plan: `/tmp/plans/2026-09-24-axiom-harness-master-plan.md` → cut as `docs/PLAN_V1.md` (done, now historical — see `HANDOFF` for current state).
