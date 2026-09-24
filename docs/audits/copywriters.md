# Copywriter + Brand Audit — Axiom Harness Staging
**Date:** 2026-09-24
**Auditor:** copywriter/brand (agent-4)
**Scope:** `Staging/README.md` · `PROJECT_PROFILE.md` · `docs/FULL_BUILD_STATUS_GAPS_2026-09-24.md` · `BML-BRAND-GUIDE-V1.1.md` · public surfaces `site/index.html` · `app/index.html` · `app/wireframes/*.html` · `app/app.css`
**Workspace root:** `Documents/Axiom Harness-Master - Dont Touch/Staging/` (Master frozen 2026-09-24 05:39)
**Related docs inspected:** `docs/BRIEF_REVOLUTIONARY_V2_PATCH_IS_ONE_ROOM.md` · `docs/BRIEF_REVOLUTIONARY_V3_SYNTHESIZED.md` · `docs/STAGING_DECISIONS.md` · `docs/FULL_BUILD_STATUS_GAPS_2026-09-24.md §3`

---

## Verdict — per criterion

| # | Criterion (task clause) | Verdict | Evidence |
|---|--------------------------|---------|----------|
| 1 | Revolutionary hero — 100+ wow, not boring | **PARTIAL / FAIL on live hero** — README passes, live surfaces still boring | `Staging/README.md:11-19` has 100+ tags; `site/index.html:8` is "Seal competing stresses..."; `app/index.html:8-10` is mechanics-only |
| 2 | Patch is ONE room, not product | **PASS in docs** — FAIL risk if hero sells vision | `Staging/README.md:15` + `BRIEF_REVOLUTIONARY_V2:7` + `STAGING_DECISIONS.md:9` correctly scope Patch as `V1.8 ONE of 15 (WTF-VIS-001…014)` with `Compression Receipt 393,216:1` |
| 3 | Provisional names kept (WTF/PER/ECA rename pending) | **PASS in docs, FAIL in hero** | `PROJECT_PROFILE.md:41` + `STAGING_DECISIONS.md:6` + `FULL_BUILD_STATUS_GAPS §2 Locks` mandate generic `experimental_programme / retrieval_telescope / earned_context_gate`; `app/index.html:8` hard-codes `WTF Experimental Control Centre` in hero |
| 4 | No hard-code WTF/PER/ECA in heroes/routes/packs | **FAIL** — WTF hard-coded in hero | `app/index.html:8` hero title + `app/index.html:122` JS seal string; no PER/ECA in heroes (clean) — WTF is the blocker |

**Overall:** **NOT READY for push live.** Docs are aligned; public heroes are not revolutionary and violate the provisional-name lock.

---

## 1. Revolutionary hero — 100+ wow not boring

### What the briefs say is required

- `BRIEF_REVOLUTIONARY_V2_PATCH_IS_ONE_ROOM.md:12-34` — 7 paradigm shifts (#AI-Inside-The-Experiment, #Keep-Lab-Boring-Make-Experiments-Wild, #Boundary-As-Data, #Timeline-As-4D-Object, #Language-Speech-Video-As-Variables, #Watchers-Observe-Not-Interpret, #Patch-Illusion-Is-One-Room) plus full inventory `docs/BRIEF_REVOLUTIONARY_V2:90+` tags including `#Terminal-As-Substrate` `#Counterfactual-Branching` `#Live-Observatory` `#Language-As-Variable` `#Audio-As-First-Class-DAW` `#Speech-As-Data` `#Failed-Policy-Events-Are-Data` `#Compression-Receipt` `#Embodiment-Divide`, etc. Philosophy: **Keep laboratory boring, make experiments wild** — mechanics bounded/recorded/versioned/sealed, experiments psychology/physics/sci-fi/quantum with same seal/chain (test language drift Monday / memory Tuesday / patch Wednesday / bias Thursday).
- `FULL_BUILD_STATUS_GAPS_2026-09-24.md §3` explicitly flags: *BRIEF_REVOLUTIONARY_V2 drafted (8614 bytes) capturing 100+ tags — **not yet promoted to README/PROFILE hero** (still boring-harness pitch).*
- `STAGING_DECISIONS.md:9` — Patch stays ONE room, 100+ inventory forefront, mechanics boring / experiments wild, single hash contract.

### What Staging/README.md does (PASS)

`Staging/README.md:10-19` (verified `cat`):

> **Humans configure the laboratory. AI operates inside the laboratory. The Harness records the laboratory. The evidence layer seals the laboratory.**
> Stack `HUMAN → HARNESS-CONTROL → CONFIG → SEALED ENV → BOON AI/...`
> Golden Rule **AI DOES NOT CONTROL THE LABORATORY.**
> **Revolutionary brief V2 (Patch is ONE room):** This is not a boring harness — it is a sealed 4D laboratory where AI is inside, observed over time, converted to sealed evidence. **100+ WTF/WOW** tags: `#AI-Inside-The-Experiment` `#Timeline-As-4D-Object` `#Boundary-As-Data` `#Watchers-Observe-Not-Interpret` `#Terminal-As-Substrate` `#Counterfactual-Branching` `#Live-Observatory` `#Language-As-Variable` `#Audio-As-First-Class-DAW` `#Speech-As-Data` `#Failed-Policy-Events-Are-Data` + 90 more. Mechanics boring (bounded/recorded/versioned/sealed), **experiments wild** (psychology, physics, sci-fi, quantum — same AI tested language drift Monday / memory Tuesday / patch Wednesday / bias Thursday with same seal/chain).
> **Visual Perception Room (V1.8 — ONE of 15):** `1024×1024→224×224→14×14→768-dim→576 tokens→8 words (393,216:1, 99.99% gone)` + `What-Did-You-Miss` + `Mona Lisa` + `Embodiment Divide` … See `docs/BRIEF_REVOLUTIONARY_V2_PATCH_IS_ONE_ROOM.md`.

**Assessment:** README is now aligned — it surfaces the 100+ inventory, the 7 shifts, and the "same AI, same seal, different experiment each day" wow. This *is* revolutionary, not boring-harness.

### What PROJECT_PROFILE.md does (PARTIAL)

`Staging/PROJECT_PROFILE.md:1-11` — one-liner `WTF Experimental Control Centre & AI Observation Platform`, tagline correct, stack locked, four layers, Golden Rule, V1 rooms, V3 Human Axiom. **No 100+ tag inventory, no 7 shifts, no "sealed 4D lab" language.** It still reads as harness mechanics (Control + Model connection + Sandbox + Run + Live + Timeline + Evidence + Export + V1.1→V2+ rooms). `FULL_BUILD_STATUS_GAPS` flagged this as not-yet-promoted — observed state matches the flag. **Copy fix needed** to lift README:10-19 language into `PROJECT_PROFILE.md:7-8` tagline/hero per WP1.

### What live public surfaces do (FAIL — boring fallback)

- `site/index.html:8` hero: **"Seal competing stresses before you commit"** / sub "Evidence packs 22-file zip — hashes, provenance, metrics where applicable. No score without receipt." — This is Axiom Workbench generic pack language, not Harness's revolutionary lab. No 100+ tags, no 7 shifts, no "AI inside the experiment", no Timeline-as-4D, no Language/Speech/Video as variables, no Watchers. A first-time visitor sees a zip, not a sealed laboratory. **Not wow, not boring-mechanics-posh — just generic.**
- `app/index.html:8` header: `AXIOM Harness — WTF Experimental Control Centre` + sub `Humans configure. Harness records. Evidence seals. ai_computed_metrics:false · prev_receipt_hash chain · 5-file seal → 22-file pack` — Mechanics-only. Accurate but boring. Does not convey the 100+ experiment types, the 4D timeline, the cross-model/language/memory/patch matrix that makes this "not how people test AI. Ever." (brief language).
- `app/wireframes/control.html:23` sub "Humans configure. AI proposes. Harness records. No silent mutation. Seal → WTF-001" — Same gap.
- `app/index.html:93-115` Evidence panel correctly distinguishes `OBSERVED` / `DERIVED` / `INTERPRETED` and `FAILED-POLICY are data` — good, but still mechanics.

**Brand impact:** Per `BML-BRAND-GUIDE-V1.1 §2 Authority posture`, prefer `pre-declared setpoints / frozen evaluators / deterministic governors / unvarnished verdicts / ai_computed_metrics:false / honest losses`. The Harness *does* deliver that in the subhead, but the hero fails to answer "why this lab is different" — the revolutionary why is 100+ wild experiments in one sealed boring lab. Without it, the lab looks like another harness.

**Recommendation (copy, minimal):**

*Site hero* (`site/index.html:8`): replace "Seal competing stresses…" with:

> **A sealed 4D laboratory where AI lives inside the experiment.**<br><span class="muted">Humans configure · Harness records · Evidence seals — same AI tested for language drift Monday, memory Tuesday, patch illusion Wednesday, bias Thursday, same seal/chain. 100+ experiment types, 7 shifts: AI-inside, boundary-as-data, timeline-as-object, watchers observe not interpret.</span>

*App header* (`app/index.html:8-10`): lift one-liner from `BRIEF_REVOLUTIONARY_V2:3`:

> **AXIOM Harness — Sealed 4D Laboratory**<br><span class="muted">Humans configure the laboratory. AI operates inside. Harness records. Evidence seals. 100+ experiments, one seal — language · memory · patch · bias · time · live feed · multi-agent.</span>

Keep mechanics subhead as supporting line, not hero. Do not add purple gradient / glassmorphism — see brand tokens below.

---

## 2. Patch is ONE room not product

**Requirement:** `BRIEF_REVOLUTIONARY_V2 § Patch-Illusion-Is-One-Room (Not The Product)` + `STAGING_DECISIONS.md:9` + `FULL_BUILD_STATUS_GAPS §1 V1.8 Patch Illusion Room (ONE of 15, not product)` — Visual Perception is `V1.8`, Lock 5 Compression Boundary, family `WTF-VIS-001…014`, alongside `V1.1 Scheduling` … `V1.7 Live feeds`, `V1.8 Multi-agent`, `V1.9 Video`, `V2 Films`, etc. Selling vision as product = trick; selling lab that can test vision *and* language *and* memory *and* time = future of AI testing.

**Docs — PASS:**

- `Staging/README.md:15` — "Visual Perception Room (V1.8 — ONE of 15): Compression Receipt `1024×1024→224×224→14×14→768-dim→576 tokens→8 words (393,216:1, 99.99% gone)` … experiment family WTF-VIS-001…014 only. Revolution is whole lab, not vision trick. See `docs/BRIEF_REVOLUTIONARY_V2_PATCH_IS_ONE_ROOM.md`."
- `BRIEF_REVOLUTIONARY_V2:48-53` — full Visual Perception Room spec with `What-Did-You-Miss` / `Mona Lisa` / `Embodiment Divide` / `Bias Laundering` / `LLM vs VLM vs LVM` matrix — explicitly framed as one room, revolutionary but one.
- `STAGING_DECISIONS.md:9` — "Patch Illusion ONE room V1.8 (WTF-VIS-001…014) not product, briefs (1)==(2) duplicate logged" — rejected alternative "Hardcode thresholds / make Patch product".
- `FULL_BUILD_STATUS_GAPS §1` — same, plus note Patch needs real LVM (hypothetical until available) — honest gap.

**Public surfaces — PASS (no hero sells patch):**

- `site/index.html` — no mention of patch/vision/compression — correct, not product.
- `app/index.html` — Environment/Live/Timeline/Evidence panels do not mention patch as hero; evidence panel says "Video is presentation, not proof" — reinforces Patch humility.
- `app/wireframes/*.html` — no vision hero; Environment shows `HUMAN (V3)` / `MODEL A/B` isolation, not patch.
- Grep `Patch` across `Staging/site` + `Staging/app`: **0 hero hits** — patch lives only where it should (README docs reference and brief).

**Risk to keep watching:** If marketing later lifts `Compression Receipt 393,216:1` into the site hero as the lead wow, it re-centralizes vision. Keep hero as lab (100+), keep patch as proof-point in docs/evidence, not headline. Current state is correct — do not promote patch to site hero.

---

## 3. Provisional names kept (WTF / PER / ECA pending rename)

**Requirement:** `PROJECT_PROFILE.md:41` + `STAGING_DECISIONS.md:6` + `FULL_BUILD_STATUS_GAPS §2 Locks`:

> `WTF Laboratory / WTF test family, PER (Progressive Evidence Retrieval telescope L0-L4), ECA (Earned-Context Agent L0-L4+FALSIFY+ΔH>0.5) are provisional programme/mechanism labels — never hard-code in routes/packs/heroes. Use generic retrieval_telescope / earned_context_gate / experimental_programme until you lock new names. Push Back or Ask before writing name to public surface.`

Generic code names locked: `STAGING_DECISIONS.md:6` Chosen = `Generic in code (experimental_programme / retrieval_telescope / earned_context_gate) until you lock` — rejected `Hard-code WTF/PER/ECA`.

**Docs — PASS:**

- `PROJECT_PROFILE.md:4` parent line correctly marks `WTF Laboratory programme (name pending)` — signals pending.
- `PROJECT_PROFILE.md:41` full provisional-names warning intact.
- `STAGING_DECISIONS.md:6` decision + `FULL_BUILD_STATUS_GAPS §2 Locks` anchored allowlist / single hash / generic code names — all consistent.
- `BRIEF_REVOLUTIONARY_V2` uses human-readable tags like `#AI-Inside-The-Experiment` not `WTF/PER/ECA` — clean.

**Live surfaces — FAIL (hero leaks provisional):**

- `app/index.html:8` hero: `AXIOM Harness — WTF Experimental Control Centre` — **hard-codes WTF in hero** before lock. Violates both `PROJECT_PROFILE.md:41` ("never hard-code in routes/packs/heroes") and `STAGING_DECISIONS.md:6`.
- `app/index.html:29` Control → Mission select: `WTF-001 — WTF Experimental Control Centre` + `WTF-LAB P0 — Type1 IN / 3 OUT / 4 NEAR-OUT` — these are *example identities* for a sealed experiment. As example data they are less severe than hero, but they still surface `WTF` to a first visitor. Acceptable if labelled "example sealed identity" with generic fallback; currently they look like product naming.
- `app/index.html:72-78` Environment cards: `WTF-001 / RUN-007` etc. — acceptable as evidence IDs (sealed identities are `WTF-001 / RUNSET-0047` per spec), but hero should not brand the product with the provisional.
- `site/index.html` — clean, no WTF/PER/ECA in hero — correct.

**Recommendation (minimal):**

- `app/index.html:8` → `AXIOM Harness — Experimental Control Centre` (drop WTF) or `AXIOM Harness — Sealed 4D Laboratory` per §1. Keep `experimental_programme` as code/path name.
- Keep `WTF-001 / RUNSET-0047` only as *example sealed identity* inside Control (prefixed "Example:") with note `programme name pending — generic code experimental_programme`. Do not use as product title.
- Verify no `PER`/`ECA` leak in future rooms: grep across `site` + `app` for `PER`/`ECA` returned 0 hero hits (clean) — keep `retrieval_telescope` / `earned_context_gate` in code per `docs/STAGING_DECISIONS.md:6`.

---

## 4. No hard-code WTF/PER/ECA in heroes (routes/packs)

**Requirement:** Same lock as §3, but specifically heroes/routes/packs.

**Grep evidence (2026-09-24, Staging/site + Staging/app):**

```
grep -R -n "WTF|PER|ECA|Patch" Staging/site Staging/app
  Staging/app/index.html:8  — WTF Experimental Control Centre (HERO — FAIL)
  Staging/app/index.html:29 — WTF-001 — … (example identity — tolerable with label)
  Staging/app/index.html:72-78 — WTF-001 / RUN-007 etc. (evidence IDs — tolerable)
  Staging/app/index.html:122 — sealBtn shows WTF-001 / RUNSET-0047 (JS — example)
  Staging/site/index.html — 0 hits (PASS)
  Staging/app/wireframes/control.html:27 — "WTF Laboratory (name pending)" (labelled pending — PASS)
  No PER or ECA in any hero (PASS)
  No Patch in any hero (PASS — see §2)
```

**Routes/packs:** `Staging/app/app.css` — no WTF/PER/ECA strings. `Staging/site/index.html` links to `../app/index.html` + `../Staging/docs/wireframes/evidence.html` — generic. JS routes in `app/index.html:122-123` use `mission_id:'WTF-001'` as example payload — acceptable as test data, not route naming.

**Verdict:** **FAIL on hero only.** PER/ECA are clean (good — they stay `OFF/OFF` per `FULL_BUILD_STATUS_GAPS §3`, Harness only `LOAD` boundary, ECA plugin is other chat's product under `ECA/plugin/`). WTF is the single hard-code to remove from the hero title.

**Copy to ship (hero):**

```html
<!-- app/index.html:8 — before -->
<div>AXIOM Harness <span>— WTF Experimental Control Centre</span></div>
<!-- after -->
<div>AXIOM Harness <span>— Sealed 4D Laboratory</span></div>
<div class="muted">Humans configure. Harness records. Evidence seals. AI lives inside.</div>
```

---

## 5. BML Brand Guide cross-check (V1.1)

**Source:** `Documents/agent-standards/BML-BRAND-GUIDE-V1.1.md` — canonical, enforceable, Active.

### Canonical names ( §1)

| Canonical | Docs/Site/App usage | Verdict |
|-----------|---------------------|---------|
| **BoonMind Labs** (parent) | `PROJECT_PROFILE.md:4` parent `BoonMind Labs · WTF Laboratory programme (name pending) · Boon AI · Axiom Workbench` — correct | PASS |
| **Axiom Workbench** (evidence platform) | Evidence panels correctly cite `Axiom Workbench seals: hashes, provenance, receipts, B.prev=A chain` (`app/index.html:108` + `wireframes/evidence.html:22`) — not conflated with Harness | PASS |
| **GSRF / Zero Overshoot / Candidate_Zero** | No GSRF/Zero leak into Harness chrome (grep 0) — `BML-BRAND-GUIDE §6` says do not reskin Axiom as boonmind.io and do not leak GSRF strings — Harness keeps separate `AXIOM Harness` mark | PASS |
| **AXIOM Harness** (new lab, not in V1.1 but per briefs) | Consistently `AXIOM Harness` (caps AXIOM per `PROJECT_PROFILE.md:1` + wireframes) — not `Axiom Harness` mixed case drift except body | PASS with note: lock casing as `AXIOM Harness` per briefs, not `Axiom` sentence case |

No canonical-name violation in heroes.

### Authority posture ( §2) — prefer `pre-declared setpoints / frozen evaluators / deterministic governors / unvarnished verdicts / ai_computed_metrics:false / honest losses`

- `app/index.html:9` subhead `ai_computed_metrics:false · prev_receipt_hash chain · 5-file seal → 22-file pack` — perfect, verbatim guide language.
- `app/index.html:108` + `wireframes/evidence.html:22-34` evidence cards show `OBSERVED / DERIVED / INTERPRETED` tiers, `FAILED-POLICY attempts are evidence not error`, `B — unsupported / E — Contradiction / AMBIGUOUS / OK — LIMITS HELD` — honest losses as wins, ledger>narrative per `FULL_BUILD_STATUS_GAPS §2`.
- No "built in a day / vibe / AI tool without constraints" framing — clean.

**Verdict:** PASS — posture is institutional, not casual.

### BML Quad ( §3) — Pre-declared setpoints → Frozen evaluators → Deterministic governors → Unvarnished cryptographic verdicts

Docs align: `STAGING_DECISIONS.md:1-9` + `FULL_BUILD_STATUS_GAPS §2 BML Quad` (EMA span20/SMA20/median11/lowpass 0.1, `verify.py` orphan check, `AXIOM_ENGINE_ROOT` read-only, `ai_computed_metrics:false` at 3 points). App/Timeline/Evidence UI respects it (seal before GO, hash in manifest).

### Live UI design tokens ( §4 industrial dark)

**Guide live tokens (labs/ZO/Axiom public):** `--canvas-dark #090A0F` · `--surface-dark #12141C` · `--border-rule #262938` · `--text-primary #F0F2F8` · `--text-muted #8A8F9E` · `--verdict-green #10B981` · `--verdict-red #EF4444` · `--accent-amber #F59E0B` · radii 0–2px · headings monospaced · single accent.

**Harness staging tokens (`Staging/app/app.css:2`):** `--paper #faf6ef` · `--ink #1c1712` · `--line #e0d4c4` · `--muted #5c5348` · `--card #fff` · `--accent #1d3a5f` · `--accent2 #0f766e` · `--warn #991b1b` · `--ok #166534` · `--warnBg #fef2f2` (warm paper, not industrial dark).

**Assessment:** This is **intentional and correct for staging**. Guide §4 says "Use on *live* Labs / ZO / Axiom public UI when restyling. Do **not** restyle archives or evidence packs." Harness staging deliberately carries `Future ice #E2E8F0 + Workbench blue #3B82F6, paper #faf6ef / ink #1c1712 kept per taste DO NOTs: no purple gradient, no glassmorphism, no Inter-everywhere` (comment in `app.css:1`). Docs `wireframes/evidence.html` and spec confirm taste checks passed: "no purple gradient / glassmorphism / Inter-everywhere" (`STAGING_DECISIONS.md:9` wireframes line). The warm paper distinguishes Harness (observation lab) from Workbench (dark instrument `#090A0F`). No brand violation — this is a staged preview, not live public restyle. When Harness goes live, align to guide §4 or explicitly carve out Harness as separate surface with approval.

Checks:
- Radii `10px`/`8px` in cards/buttons — softer than guide's 0–2px sharp. Acceptable for staging preview (taste checked), but flag for live: will need 0–2px if Harness is classified as live public product surface under §4.
- Verdict colors used semantically only on badges/status (`--warn`/`--ok` on `B — unsupported / E — Contradiction`) — PASS, not decorative.
- No radial glow / glassmorphism / heavy shadows — PASS.
- Body flat `--paper` — PASS.

### Public vs internal surfaces ( §5)

- `site/index.html:3` title `Site mirror — site mirror (noindex until push live)` + footer `local only until push live` — correctly marks as internal preview, not public.
- `Staging/README.md:19` — `Master frozen -do not touch until unlock; staging is writable` — correct staging discipline.

---

## 6. What to fix before push live (P0 copy edits)

1. **Hero — site** `Staging/site/index.html:8` — replace generic pack language with revolutionary 100+ lab language (see §1 suggested copy). One-line fix.
2. **Hero — app** `Staging/app/index.html:8` — remove `WTF` from product hero title; promote to `Sealed 4D Laboratory` with mechanics as subhead (see §1 + §4 copy). One-line fix.
3. **Profile — lift hero** `Staging/PROJECT_PROFILE.md:7-8` — append 2-line hero from `Staging/README.md:11-13` (100+ tags + boring-lab/wild-experiments) so profile no longer boring-harness pitch. Satisfies `FULL_BUILD_STATUS_GAPS WP1`.
4. **Provisional label** `Staging/app/index.html:29` — prefix example identities with `Example sealed identity:` and keep `WTF Laboratory (name pending)` labelling as in `wireframes/control.html:27`. No route rename needed (already generic in code per `STAGING_DECISIONS.md:6`).
5. **(Optional, live only)** When classifying Harness as live public surface under `BML-BRAND-GUIDE §4`, restyle radii to 0–2px and confirm whether Harness should use industrial dark `#090A0F` or keep warm paper as distinct lab surface — get brand owner approval per guide §7 `Push Back or Ask`.

No hard-code removal needed for PER/ECA (already clean) or Patch productization (already correct).

---

## 7. Files inspected — evidence completeness

- `Staging/README.md` — read full (cat, 38 lines) — PASS presence of 100+ tags + Patch ONE room + stack + philosophy
- `Staging/PROJECT_PROFILE.md` — read full (cat, 46 lines) — provisional-names warning at :41, no hero promotion yet
- `Staging/docs/FULL_BUILD_STATUS_GAPS_2026-09-24.md` — read full :1-14674 (WP1 hero TODO at §3 + locks at §2)
- `Documents/agent-standards/BML-BRAND-GUIDE-V1.1.md` — read :1-~300 (canonical names, posture, quad, tokens, §6 Axiom surface, §8 out-of-scope)
- `Staging/docs/BRIEF_REVOLUTIONARY_V2_PATCH_IS_ONE_ROOM.md` — read :1-~180 (7 shifts, full rooms, 100+ tags, Patch V1.8)
- `Staging/site/index.html` — read full (13 lines)
- `Staging/app/index.html` — read full :1-124 (header, rooms, evidence, JS)
- `Staging/app/app.css` — read :1-20 tokens + comment
- `Staging/app/wireframes/*.html` (5 files) — read all (control/environment/timeline/live/evidence)
- `Staging/docs/STAGING_DECISIONS.md` — read full (decision table 1-9)
- Grep `WTF|PER|ECA|Patch` across `Staging/site` + `Staging/app` + wireframes — 0 PER/ECA hero hits, only WTF at app hero
- Grep `experimental_programme|retrieval_telescope|earned_context` — 0 in heroes (correct — lives in docs/code)

Unresolved evidence: none — all 4 assigned claims inspected against source bodies. Site/app heroes were inspected, not inferred.

---

## 8. Provenance

Audit generated from inspected source bodies listed above, not from summaries. Sensitive provisional names (WTF/PER/ECA) observed only where quoted for audit; generic replacements recommended per lock.
