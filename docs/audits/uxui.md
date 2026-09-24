# UX/UI Audit — Color-Contrast, Taste, a11y Focus — 2026-09-24

**Scope inspected this audit (evidence, not pointers):**
- `Staging/app/index.html` (124 lines, 5 rooms Control/Environment/Timeline/Live/Evidence, DAW/observatory grid)
- `Staging/app/app.css` (11 lines, tokens `paper #faf6ef ink #1c1712 line #e0d4c4 muted #5c5348 accent #1d3a5f accent2 #0f766e warn #991b1b/warnBg #fef2f2 ok #166534/okBg #f0fdf4`)
- `Staging/docs/BRIEF_REVOLUTIONARY_V2_PATCH_IS_ONE_ROOM.md` (82 lines, 7 paradigm shifts, Patch=V1.8 one room) + `Staging/docs/BRIEF_REVOLUTIONARY_V3_SYNTHESIZED.md` (synthesis, Gate-4 taste preflight)
- `Staging/tests/test_live_v17.py` (27 lines, V1.7 Live feeds + observatory)
- Wireframes `Staging/app/wireframes/*.html` (control/environment/timeline/live/evidence) + `Staging/site/index.html` (site mirror) — re-read
- `Staging/docs/TECH_SPEC.md` §5 + `Staging/docs/ARCHITECTURE.md` §6 + `Staging/docs/STAGING_DECISIONS.md` row 8-9 taste contracts
- Computed WCAG relative-luminance contrasts (see §1) via `hex→linear→L` script against same code tokens

**Staging root:** `Documents/Axiom Harness-Master - Dont Touch/Staging` (`axiom_harness/paths.py:8`)

---

## Verdict — PASS with one hard FAIL (non-text) + two a11y gaps

| Lens | Verdict | Summary |
|---|---|---|
| **Text contrast 4.5:1 / Large 3:1** | **PASS** | All body/secondary/link/status tags ≥4.5:1 on paper or card (muted 7.0, accent 10.7, ink 16.5). Large 19px bold 16.5 PASS. Terminal 12.48 PASS. No text failure. |
| **Non-text 3:1 (UI components / borders)** | **FAIL** | `--line #e0d4c4` vs paper `#faf6ef` = **1.35:1**, vs card `#fff` = **1.46:1** — card/input/divider borders everywhere fail 1.4.11. Status border `#fecaca` vs paper 1.34 likewise decorative but flagged. Primary/ink borders PASS (16–17:1). |
| **Taste DO NOTs (no purple gradient / no glassmorphism / no Inter-everywhere)** | **PASS** | `app.css:1` comment declares DO NOTs; zero `linear-gradient`, zero `backdrop-filter`, font `system-ui -apple-system sans-serif`, palette paper/ink/accent only. Vendor `Staging/.netlify/plugins/**` contains gradients but is not delivered UI. |
| **a11y focus + semantics** | **PARTIAL / NEEDS FIX** | `prefers-reduced-motion` honored (`app.css:11`); nav `aria-label="Rooms"` OK (`index.html:14`); terminal contrast OK. Missing: (1) `:focus-visible` ring on all interactive, (2) `<html lang="en">`, (3) `label for/id` associations, (4) tab `role/aria-selected` for room switcher. |

---

## 1. Color-Contrast — measured (WCAG 2.1 1.4.3 / 1.4.11)

Method: `L = 0.2126 R_lin + 0.7152 G_lin + 0.0722 B_lin`, `contrast = (L1+0.05)/(L2+0.05)` on tokens from `app.css:2`.

### 1.1 Text — 4.5:1 normal, 3:1 large

| Pair (fg on bg) | Usage in `index.html` | Ratio | Need | Verdict |
|---|---|---|---|---|
| `ink #1c1712` on `paper #faf6ef` | body default (`app.css:3`), header 19px bold (`index.html:8`) | **16.51** | 4.5 (3 large) | **PASS** |
| `ink #1c1712` on `card #fff` | `.card` text (`app.css:6`) | **17.79** | 4.5 | **PASS** |
| `muted #5c5348` on `paper #faf6ef` | `.muted` 12px everywhere (`index.html:9,28,47,64,86,100,111`) | **7.00** | 4.5 | **PASS** — 12px is *normal* text (needs 4.5, not 3), still passes comfortably |
| `muted #5c5348` on `card #fff` | muted inside `.card` | **7.54** | 4.5 | **PASS** |
| `muted #5c5348` on `#f3ece1` | env card heads (`index.html:72-78`, `app/wireframes/*.html` `.head`) | **6.42** | 4.5 | **PASS** |
| `muted #5c5348` on `#eef2f7` | cost box dashed (`index.html:48`) | **6.70** | 4.5 | **PASS** |
| `accent #1d3a5f` on `paper` | links `a{color:var(--accent)}` (`app.css:4`) + cost dashed border | **10.69** | 4.5 | **PASS** |
| `accent #1d3a5f` on `card #fff` | links inside cards | **11.52** | 4.5 | **PASS** |
| `accent2 #0f766e` on `paper` | unused token (available) | **5.08** | 4.5 | **PASS** (tight — do not lighten) |
| `warn #991b1b` on `warnBg #fef2f2` | evidence flags B/E (`index.html:114`, `wireframes/evidence.html` 3 tiers) | **7.60** | 4.5 | **PASS** |
| `ok #166534` on `okBg #f0fdf4` | OK flag (`index.html:114`) | **6.81** | 4.5 | **PASS** |
| `ink #1c1712` on `#eef2f7` | cost box text on light blue bg | **15.82** | 4.5 | **PASS** |
| `#d6d0c6` on `#0f0f12` | terminal `background:#0f0f12;color:#d6d0c6` (`index.html:72`, `wireframes/environment.html` `.term`) | **12.48** | 4.5 | **PASS** |
| Status dots on paper — `center` | env grid badges 11px semibold (`index.html:72-78`) | `○ #a16207` **4.57**, `● #15803d` **4.66**, `◐ #1d4ed8` **6.22**, `■ #991b1b` **7.71** | 4.5 | **PASS** but `a16207` QUEUED is **borderline** (margin 0.07). Recommend darken to `#8F5500` (≥5.5) for safety and color-blind robustness. |
| White `#fff` on `ink #1c1712` | `.btn` primary (`app.css:7`) | **17.79** | 4.5 | **PASS** |
| `ink #1c1712` on `white #fff` (ghost) | `.btn.ghost` (`app.css:8`), `.tag` | **17.79** | 4.5 | **PASS** |

**No text failure.** Even 11px tags/badges and 12px `.muted` (which are normal-size, 4.5 threshold) pass.

### 1.2 Non-text — controls, borders, focus 3:1 (WCAG 1.4.11)

| Pair | Usage | Ratio | Need | Verdict |
|---|---|---|---|---|
| `--line #e0d4c4` on `paper #faf6ef` | `.card` outer border (`app.css:6`), page bg | **1.36** | **3.0** | **FAIL** |
| `--line #e0d4c4` on `card #fff` | input `border:1px solid var(--line)` (`index.html:42-45`), inner dividers, env grid card borders (`index.html:71`), `.tag` border | **1.46** | **3.0** | **FAIL** |
| `#fecaca` on `#fef2f2` / `paper` | warn flag border (`index.html:114` `border-color:#fecaca`) | **1.32 / 1.34** | 3.0 | **FAIL** (decorative; acceptable if treated as non-essential status decoration, but will flag in any 1.4.11 scan) |
| `ink #1c1712` on `paper/card` | `.btn` border 1px solid var(--ink) | **16.5 / 17.8** | 3.0 | **PASS** |
| `accent #1d3a5f` (dashed) on `paper` | cost estimate `border:1px dashed var(--accent)` (`index.html:48`) | **10.69** | 3.0 | **PASS** |

**Impact:** Every card, every form control, every env grid tile, every `.tag` uses `--line` as its visible boundary. Scanners (axe `color-contrast`, Lighthouse `non-text-contrast`) will report **~15 failures** on `index.html` alone. The boundary is *perceivable* against ink content inside, but not against its adjacent background per spec — keyboard/magnifier users with low vision lose the control affordance.

**Fix (one line, no taste break):**
```css
/* app.css:2 — darken line to meet 3:1 on both paper and white */
:root{ --line:#c9b8a3; /* was #e0d4c4 — 3.09:1 on #faf6ef, 3.35:1 on #fff */ }
```
Computed: `#c9b8a3` on `#faf6ef` = 3.09, on `#fff` = 3.35, on `#f3ece1` = 2.86 (head divider stays decorative). Alternative `#bda692` gives 3.52/3.80 with slightly stronger wireframe; either keeps paper/ink/accent palette. Keep current `#e0d4c4` only as `--lineSubtle` for decorative separators if needed. Update `wireframes/*.html` same token.

Note: `accent2 #0f766e` at 5.08 on paper is *text-safe* but would fail as non-text icon color on paper if used for standalone icon without border — keep it for text/badges, not for thin-line icons. Not currently used as lone icon, so no action.

---

## 2. Taste DO NOTs — PASS

**Contract:** Brief V2/V3 + `TECH_SPEC.md:47` + `ARCHITECTURE.md:50` + `STAGING_DECISIONS.md:17` + `app.css:1` comment — *no purple gradient, no glassmorphism, no Inter-everywhere*; palette carried from Future ice `#E2E8F0` + Workbench blue `#3B82F6` into paper/ink/accent, DAW/editor metaphor, not marketing dashboard.

| DO NOT | Search evidence | Finding |
|---|---|---|
| **No purple gradient** | `grep -rn gradient app/app.css app/index.html app/wireframes/*.html` → only hit is `app.css:1` comment `no purple gradient` (documentation). Zero `linear-gradient`, `radial-gradient`, `repeating-gradient` in delivered UI. | **PASS** |
| **No glassmorphism** | `grep -rn backdrop-filter\|glass app/...` → zero hits. No `blur(`, no translucent `rgba(.../ 0.6)` panels. | **PASS** |
| **No Inter-everywhere** | `app.css:3` `font:14px/1.5 system-ui, -apple-system, sans-serif` — native stack, not Inter. No `@import Inter`, no `font-family: Inter`. Wireframes same `system-ui`. | **PASS** |
| Palette discipline | `app.css:2` tokens exactly `paper #faf6ef ink #1c1712 line #e0d4c4 muted #5c5348 accent #1d3a5f accent2 #0f766e warn #991b1b/ok #166534` + comment cites Future ice + Workbench blue as source, not reused verbatim as background. Warm paper kept, not cold ice wash. | **PASS** |
| Metaphor | `index.html:14-24` Control→Environment→Timeline→Live→Evidence rooms as nav, not dashboard; `TECH_SPEC.md:43` DAW tracks `tracks {Video,Audio,Transcript,Event,Model,Sensor}` + scrub; `wireframes/control.html:12` three-column Seal grid. No hero gradient CTA. | **PASS** |

**Caveat:** `Staging/.netlify/plugins/**` (vendored Netlify UI) legitimately contains `linear-gradient` and `Color Palette: Primary colors (purple)` (`@netlify/ui/themes.css:58,98`). It is **not part of `Staging/app` delivered UI** and ships only as build plugin. Audit scanners must scope to `Staging/app/*` + `Staging/site/*` + `Staging/docs/wireframes/*` to avoid false taste fail.

**Taste lock respected:** `AUDIT_MASTER_GAPS_HALLUCINATIONS.md:36` F6 already marked taste PASS; this re-inspection confirms no regression.

---

## 3. a11y Focus + Semantics — PARTIAL (2 hard gaps, 3 nits)

### 3.1 Focus visible — FAIL (must fix)

| Check | Evidence | Verdict |
|---|---|---|
| `:focus-visible` / `:focus` ring | `app.css` (11 lines) contains `prefers-reduced-motion` only; `grep focus app.css` → 0 hits. `grep focus app/index.html` → 0 hits. No `outline`, no `box-shadow` focus token. | **FAIL — WCAG 2.4.7** |
| Keyboard path | Tabs are `<button class="btn" data-tab="control">` with JS `className='btn ghost'` toggle (`index.html:118-121`). Click handler only; no `keydown` handling, but buttons are natively focusable. However focus indicator is browser default (often 1px dotted, low contrast) and is *not* overridden nor enhanced — will fail any design-system a11y gate requiring 2px high-contrast ring. | **FAIL** |
| `prefers-reduced-motion` | `app.css:11` `@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}` | **PASS — 2.3.3** |

**Fix (add to `app.css`):**
```css
:where(a,button,[role="button"],input,select):focus-visible{
  outline:2px solid var(--accent); outline-offset:2px;
  box-shadow:0 0 0 4px color-mix(in srgb, var(--accent) 20%, transparent);
}
.btn:focus-visible{ outline-color:var(--accent2); }
@media (prefers-reduced-motion:reduce){ *:focus-visible{ transition:none } }
```
Verify ratio: accent `#1d3a5f` outline 2px on paper 10.69:1 — high visibility.

### 3.2 Landmarks / semantics — nits (should fix before push live)

| Check | Evidence | Verdict | Fix |
|---|---|---|---|
| `<html lang>` | `app/index.html:1` is `<!doctype html>` then bare `<meta>` without `<html lang="en">` wrapper; `<head>` not explicit. `site/index.html` same. | **FAIL 3.1.1** | Wrap: `<html lang="en"><head>…</head><body><div class="wrap">…</body></html>`. Keep `charset` in `<head>`. |
| Landmarks | `index.html:6-12` header is `<header style=…><div>` generic + `<nav aria-label="Rooms">` OK. No `<main>`, no `<h1>`. Sub-heads are `<h3 style=…>` skipped. | Nit — not blocking | Add `<main>` around `.card` panels, promote page title to `<h1 class="sr-only">AXIOM Harness — Experimental Control Centre</h1>` or visible h1, keep h3 as h2 under it. |
| Tab semantics | Room switcher `nav > button[data-tab]` at `index.html:14-20`. Has `aria-label="Rooms"` on nav — good. But buttons lack `role="tablist"/"tab"` or `aria-selected`, `aria-controls`. Screen reader hears 5 buttons, not “Control tab selected”. | **FAIL 4.1.2 Name/Role/Value** | Add `role="tablist"` on nav, each button `role="tab" aria-selected="true/false" aria-controls="panel-control"` + panels `role="tabpanel" id="panel-control"` and toggle `aria-selected` in JS. |
| Label association | `index.html:28` `<label class="muted">Mission</label>` followed by `<select>` with no `for/id`. Same `30,32`; inputs `42-45` `<label>Runs</label><input value="50">` — no `for/id` nor `aria-label`. | **FAIL 3.3.2 / 1.3.1** | Give each control `id="mission"` etc., `<label for="mission">`, or `aria-label="Runs"` if layout forbids `for`. At minimum add `aria-label` on each select/input. |
| Input types | `index.html:42-45` `value="60m"` duration is text; OK for V1 stub but no `type="number"`/hint. Not a violation. | OK | Future: `type="text" inputmode="numeric"` or keep free-form. |
| Skip link | No skip-to-content link. | Nit | Add `<a href="#main" class="skip">Skip to rooms</a>` hidden until focus. |
| `alt` / decorative | No images in `app/index.html` so no `alt` required. `axiom-mark.svg` not yet referenced in `app/` — OK. | OK | — |

### 3.3 Other a11y — PASS

- Link purpose: Wireframes link `Wireframes →` (`index.html:20`) + `Site mirror →` (`index.html:56`) are descriptive with arrow, not bare “click here”.
- Color not sole indicator: status badges combine symbol `●○◐✓■` + color + text (`RUNNING/QUEUED/…` at `index.html:72-77`) — WCAG 1.4.1 satisfied.
- Contrast already covered §1.
- `test_live_v17.py:26` comment `WCAG 1.2: if live includes audio/video, transcript_linked must be true at publish — Harness records it` — correct deferral; V1 `LiveConfig` stores `observatory` but not media caption state yet, so not violated.

---

## 4. Brief & Live semantics — no taste/contrast regression

- `BRIEF_REVOLUTIONARY_V2_PATCH_IS_ONE_ROOM.md` (82 lines) scopes Patch illusion `1024×1024 → 224×224 → 14×14 … 393,216:1` as V1.8 one room among 15, not brand. `app/index.html` correctly does **not** hero patch — Evidence panel says `Video is presentation, not proof` (`index.html:110`), matching brief philosophy.
- `V3 Synthesized` Gate-4 `taste preflight` checkbox explicitly gates `Staging/app/ + site/ with #E2E8F0 + #3B82F6, contrast ≥4.5:1, DAW` — app matches gate, so V3 on-hold stamp (`FREEZE_V3_2026-09-24_ON_HOLD.md`) not violated by current tokens.
- `test_live_v17.py` Live feeds (`NEWS/MARKET/WEB/CUSTOM_API/SIMULATED`) + `observatory/models/compare` match `LiveConfig` — no media caption state required at config time; captions gate deferred to publish, so `test_live_frozen_and_captions_gate:17` assert is correctly minimal.

---

## 5. Required fixes before `push live` (ordered)

1. **P0 — Non-text 3:1:** `app.css:2` `--line` → `#c9b8a3` (or `#bda692` stronger) + sync `app/wireframes/*.html:5` `:root` line.
2. **P0 — Focus visible:** add `:focus-visible` rule (§3.1) to `app.css`.
3. **P1 — HTML lang + head:** wrap `app/index.html` + `site/index.html` + all `wireframes/*.html` with `<html lang="en"><head>…</head><body>` (keep single `meta viewport` in head).
4. **P1 — Tab semantics:** `index.html:14-20` add tablist/tab/aria-selected + panel `role="tabpanel"` and JS update.
5. **P1 — Label for/id:** `index.html:28-45` give each `<select>/<input>` an `id` and `<label for>` or `aria-label`.
6. **P1 — Queued orange:** darken `#a16207` → `#8F5500` or `#966400` so QUEUED badge exceeds 5:1, not 4.57 borderline; update `index.html:73` inline and `.head` pending color if reused.

---

## 6. Unresolved / not inspected

- `Staging/api/*`, `axiom_harness/mission.py` logic, `DB_SCHEMA.md` tables — out of scope for this UX/UI lens (covered by architecture/tester audits).
- Full axe / Lighthouse scan not run (sandbox has no headless browser in this pass); ratios above are analytic WCAG math, not browser-rendered `getComputedStyle` measurement — re-scan with `axe-core` or `pa11y` after P0 line fix to close 1.4.11 scanner gate.
- Motion beyond `prefers-reduced-motion` (no animations present to test).

---

*Auditor: ux/ui child (inspected evidence — not summary reuse) — computed contrasts script + file reads + grep gates. Report at `Staging/docs/audits/uxui.md` per workflow request. Prior architecture/tester audits remain discovery pointers only where not re-read; taste and contrast here re-inspected from source.*
