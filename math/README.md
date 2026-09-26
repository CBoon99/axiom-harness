# Math / Code Stack — Existence Log (Not Engine)

> This folder logs the *existence* of upstream maths, it does NOT contain the maths.
> Technique to keep AI out of engine/code, not a core modular engine. Never hard-code values here.

**Why this exists:** Per Carl 2026-09-25 — lock maths down modularly to keep AI out of engine/code BEFORE the math is handed over. Same pattern for ECA / PER / AXIOM.

**Rule:** This is a technique to keep AI out, not the engine itself. Record `IMPLEMENTATION_HASH + CONFIG_HASH + VERSION` only (registry). Never copy `wear_proxy`, `GateOk`, `ΔH`, `HYPOTHESIS_WEIGHTS` etc into `axiom_harness/`.

**Structure:**
```
math/
  README.md           — this file (technique)
  upstreams/          — hashes for generic upstream pointers (Axiom-Workbench, etc)
  axiom/              — Axiom Workbench engine hash placeholder
  per/                — PER-Core telescope hash placeholder
  eca/                — ECA plugin hash placeholder
```

**For each stack (do same):**
1. Create `math/<stack>/EXISTS.md` — records `exists: true`, `source_path`, `implementation_hash` (sha256), `config_hash`, `version`, `status: UPSTREAM-BLOCKED`
2. Never write the formula — only the hash + pointer
3. Harness may `LOAD` the hash, never `CALCULATE` the result

**From HANDOFF/MEMORY:**
- Single hash `WTF-005A-HASH-v3` via `axiom_harness/manifest.py:15` is the only harness-owned hash
- Upstreams: `Axiom-Workbench/axiom_wb`, `PER-Core/sim/telescope.py`, `ECA/plugin/` — all `UPSTREAM-BLOCKED` until you hand over

**Next:** When Carl hands math, fill `math/<stack>/EXISTS.md` with real sha256s, keep `axiom_harness/*.py` doing `rg GateOk → 0`
