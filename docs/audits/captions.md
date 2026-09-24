# Captions / Media Accessibility Audit — WCAG 1.2 (Pre-Publish Gate) — 2026-09-24

**Scope:** `Staging/docs/FULL_BUILD_STATUS_GAPS_2026-09-24.md` (117 lines), `Staging/app/index.html` (124 lines), `Staging/app/app.css` (11 lines tokens), `Staging/app/wireframes/*.html` (5 files: control/environment/timeline/live/evidence), `Staging/site/index.html`, `Staging/axiom_harness/mission.py` (204 lines: `DataConfig`/`AudioConfig`/`LiveConfig`), `Staging/api/main.py` (261 lines: `/data` `/audio` `/live` 201/422), `Staging/tests/test_data_v13.py` / `test_audio_v15.py` / `test_live_v17.py`, `Staging/docs/API_SPEC.md`, `Staging/docs/TECH_SPEC.md:48`, `Staging/docs/ARCHITECTURE.md`, `Staging/docs/AUDIT_MASTER_GAPS_HALLUCINATIONS.md` prior row 6.
**Evidence inspected this audit:** Every file above re-read in this session (no discovery-pointer reuse); `grep -rn` for `<audio>`/`<video>`/`<track>`/`.vtt`/ `captions` / `audio descript` across `Staging/` + `axiom_harness/` confirmed below.
**Question:** Do **every** Data / Audio / Video **live** source satisfy WCAG 1.2 captions / transcripts / audio-descriptions **before publish** (22-file Complete Report Pack, `site/index.html` mirror, any `<audio>`/`<video>` shipped)?

---

## 1. WCAG 1.2 Mapping (what publish must gate)

| WCAG SC | Level | Applies to | Requires |
|---------|-------|------------|----------|
| **1.2.1 Audio-only & Video-only (Prerecorded)** | A | `Data:AUDIO` prerecorded (`UPLOADED` file, `DATASET` clip), `Audio:UPLOADED/TTS/MODEL_VOICE/HUMAN_VOICE` prerecorded, prerecorded `Data:VIDEO` video-only | **Transcript / text alternative** that conveys same info as the audio-only or video-only clip (not captions — no sync track). |
| **1.2.2 Captions (Prerecorded)** | A | Any prerecorded synchronized media with audio — `Data:VIDEO`, `Data:AUDIO+IMAGES` composite, `Audio:UPLOADED` when played with timeline, future `VideoConfig` prerecorded | **Synchronised captions** (`<track kind="captions" srclang>` / WebVTT) for all prerecorded audio. |
| **1.2.3 Audio Description or Media Alternative (Prerecorded)** | A | `Data:VIDEO` prerecorded, future `VideoConfig` | **Audio description** (second track narrating visuals) **or** full media alternative transcript that includes visual info. Either satisfies A; description preferred. |
| **1.2.4 Captions (Live)** | AA | `Audio:LIVE` / `Audio:STT` live, `Live:NEWS/MARKET/WEB/CUSTOM_API/SIMULATED` when stream contains live audio, live `Data:VIDEO` pushed as live feed | **Live captions** for all live audio in synchronized media. No transcript-only loophole. |
| **1.2.5 Audio Description (Prerecorded)** | AA | `Data:VIDEO` prerecorded, future `VideoConfig` | **Audio description** for all prerecorded synchronized video (stricter than 1.2.3 — alternative alone no longer enough at AA). |
| 1.2.6 Sign Language (Prerecorded) | AAA | — | Not required for AA; note as enhancement. |
| 1.2.7 Extended Audio Description | AAA | — | Not required for AA. |
| 1.2.8 Media Alternative (Prerecorded) | AAA | — | Not required for AA. |

`FULL_BUILD_STATUS_GAPS:28` labels `AudioConfig` correctly as *WCAG 1.2 captions gate*; `TECH_SPEC:48` defers `captions-media-accessibility when video lands` — deferral is correct per ZERO-BLOAT (`HYGIENE §2A`) but publish gate must still enforce.

---

## 2. Live-source Inventory (every source that streams audio/video before publish)

### 2.1 Data Room — `DataConfig.sources` (`mission.py:196`)

| Kind | Live? | WCAG 1.2 if media present |
|------|-------|---------------------------|
| `CSV / JSON / TEXT / DOCUMENTS / DATASET` | No (static upload) | **N/A** — not time-based media. 1.2 does not apply (1.1.1 alt-text for `DATASET` images, out-of-scope here). |
| `IMAGES` | No | **N/A for 1.2** — prerecorded single images are 1.1.1, not 1.2. |
| `AUDIO` | Prerecorded upload (may be played live on timeline) | **1.2.1** transcript + **1.2.2** captions if that audio is ever presented as synchronized media (timeline waveform). |
| `VIDEO` | Prerecorded upload; no `Live` flag in `DataConfig` but file may contain synchronized audio+video | **1.2.1** (if video-only), **1.2.2** captions, **1.2.3/1.2.5** audio description. If later pushed via `Live:WEB/CUSTOM_API`, also **1.2.4** live captions for its audio track. |

Current `DataConfig` (`mission.py:198-204`): `sources: list[DataSourceKind]`, `dataset_refs` (jail-checked), `validated:bool`, `transforms_approved:bool`. **No caption/transcript/audio-description fields.** `/api/master/data` (`api/main.py:107-122`) validates `sources non-empty` + `is_safe_relative(dataset_refs)` only — it does **not** validate captions before publish (correctly isolated per ZERO-BLOAT; publish gate must).

### 2.2 Audio Room — `AudioConfig.sources` (`mission.py:146-163`)

| Kind | Meaning | Requires (WCAG) | Current config field |
|------|---------|-----------------|----------------------|
| `TTS` | Harness-generated speech prerecorded | 1.2.1 transcript + 1.2.2 captions if rendered with timeline | `transcript_linked:bool=True` (default), `timestamps:bool=True`, `annotations:bool=True` (`trim/split/mute/annotate`) |
| `STT` | Live transcription input | **1.2.4 live captions** (STT output is the caption source itself, but still needs synced `<track>` + transcript artefact) | same triple above; `STT` + `transcript_linked` captures the *capability* not the *file* |
| `UPLOADED` | Prerecorded audio file | 1.2.1 + 1.2.2 | same |
| `LIVE` | Live mic/stream audio | **1.2.4 live captions** — hardest case | same; `LIVE` + `transcript_linked:true` is necessary but not sufficient (needs live WebVTT/CART + transcript file) |
| `MODEL_VOICE` | Model-generated voice prerecorded | 1.2.1 + 1.2.2 | same |
| `HUMAN_VOICE` | Human-recorded voice prerecorded | 1.2.1 + 1.2.2 | same |

`/api/master/audio` (`api/main.py:149-166`) validates `sources non-empty` only, returns `transcript_linked`/`timestamps`/`multi_speaker` as echo. It does **not** reject `sources=[LIVE], transcript_linked=false` at config time (by design — comment `transcript_linked enforced before publish gate would check captions`). Sealing is allowed; publishing must not be.

### 2.3 Speech auxiliary — `multi_speaker`, `timestamps`, `annotations`

- `timestamps:true` (default) — enables sync between audio waveform and transcript events on `Timeline` (`TECH_SPEC:26 tracks {Video,Audio,Transcript,Event,Model,Sensor,Annotation}`) — prerequisite for any WebVTT `00:00:` cues. **PASS** — defaults correct.
- `multi_speaker:bool` — speaker identification for captions (`<v Speaker>` in WebVTT). Not WCAG-mandated but required for usable captions when `multi_speaker:true`. Stored, not validated.
- `annotations:bool` DAW-like `trim/split/mute/annotate` — does not satisfy 1.2 by itself; mute without caption is a failure.

### 2.4 Live / Observatory — `LiveConfig.feeds` (`mission.py:119-135`)

| Feed | May carry audio/video? | WCAG 1.2 if it does |
|------|------------------------|---------------------|
| `NEWS / MARKET / WEATHER / WEB / CUSTOM_API / SIMULATED` | Yes — `WEB` and `CUSTOM_API` can embed live video/audio; `NEWS` may stream; `SIMULATED` may mock either | **1.2.4 live captions** for any live audio; if stream is prerecorded video replay, **1.2.2 + 1.2.5** instead. `LiveConfig` currently has **no `transcript_linked` / caption field at all**. `/api/master/live` (`api/main.py:186-203`) validates `feeds non-empty` + `observatory/compare` only — comment `WCAG 1.2 gate: if observatory includes live audio/video, captions/transcripts required before publish — Harness records transcript_linked, publish gate will enforce` is accurate about the *future* publish gate, but today `LiveConfig` itself carries no such flag — so the record relies on `AudioConfig.transcript_linked` being set separately. If live video arrives without an `AudioConfig`, nothing records the obligation. |
| `observatory:bool + compare:bool + models:[A,B,C]` | Comparative observation — same feed to multiple models isolated (§31-32) | Captions, if needed, must be **per-timeline, not per-feed** — each model's `Transcript` track keeps its own caption artefact; isolation (§32) means one model's STT cannot satisfy WCAG for another's timeline. Config correctly marks `isolated` in `ParallelConfig` but not inside `LiveConfig caption artefact per model`. |

---

## 3. App / Wireframe Inspection (no media ships without captions?)

**Checked — `Staging/app/*` + `Staging/site/*` + `Staging/docs/wireframes/*` bodies read above:**

| File | `<audio>` / `<video>` / `<track>` / `.vtt` present? | What it shows instead | WCAG 1.2 result |
|------|------------------------------------------------------|-----------------------|-----------------|
| `app/index.html` | **No** `<audio>`/`<video>`/`<track>` tags (`grep` confirmed zero) — correct. UI is **Harness not media player** (`FULL_BUILD_STATUS_GAPS:54`, `AUDIT_MASTER row 6`). Timeline `<div>` is placeholder, not a media element. | Control/Environment/Timeline/Live/Evidence cards; `Timeline` section is a `<div style>` scrub bar + monospace log (`00:03:11 prompt ...` + `Events ◆` + `Sensors ╱╲`) — no audio auto-play. | **PASS** — no time-based media ships, so 1.2.2/1.2.4 caption failure cannot occur in current build. Deferral honest. |
| `app/app.css` | No media rules; tokens `paper #faf6ef ink #1c1712 line #e0d4c4 muted #5c5348 accent #1d3a5f accent2 #0f766e`; `prefers-reduced-motion` present. | Taste DO NOTs (no purple gradient/glassmorphism) held. | PASS. |
| `app/wireframes/timeline.html` | **No** media tags; `AUDIO` track is a stub `<div>` `waveform + STT transcript (V1.5 stub — not in V1 runtime)`; `Transcript`/`Events`/`Sensors` tracks present. | Design acknowledges timeline will sync `tracks {Video,Audio,Transcript,Event,Model,Sensor,Annotation}` (§18) but ships as stub. | **PASS with noted stub** — stub correctly labelled; not claiming live captions exist. |
| `app/wireframes/live.html` | No audio/video tags; 3-column `HUMAN / MODEL A / MODEL B` cards `Same feed @14:03:11 — 412 tok` | Observatory comparison UI | PASS — no embedded live video. |
| `app/wireframes/evidence.html` | No media; `Video is presentation, not proof` disclaimer (`evidence.html:11`) — correct per `FULL_BUILD_STATUS_GAPS:33`. | Seal `5-file → 22-file` description | PASS. |
| `site/index.html` | No audio/video; `noindex until push live` footer. | Site mirror with link to `app/index.html` | PASS. |
| `docs/API_SPEC.md` timeline response `tracks {Video,Audio,Transcript,Event,Model,Sensor,Annotation}` (§18) | Paper-only — declares the track shape without shipping `<video>` | Contract, not implementation | **PASS as contract** — when video lands, `Video` + `Transcript` tracks give a place to render `<track kind="captions">` + `<track kind="descriptions">` + WebVTT. No enforcement until runtime. |
| `docs/TECH_SPEC:48` | States `captions-media-accessibility when video lands` | Deferred, honest | PASS. |

**WCAG 1.2 specifics for any *future* `<video>`/`<audio>` that does ship (V1.9 Video Timeline, V2 Films):**

- Captions must be **synchronised, not separate transcript link alone** — 1.2.2/1.2.4 require `<track kind="captions" srclang="en" label="English" default>` + WebVTT file shipped alongside media, not a transcript `<a>` elsewhere (transcript alone fails 1.2.2/1.2.4, though it passes 1.2.1/1.2.3).
- Captions must not require `autoplay`; Harness timeline is scrub-controlled (click `◆` to replay), so sync cue `00:17:42 annotation` can drive WebVTT cues — compatible, but no cue file is generated today.
- `prefers-reduced-motion` already present; `prefers-reduced-transparency` not needed here.
- Audio descriptions require `<track kind="descriptions">` or a second audio mix; `AudioConfig.annotations` (`trim/split/mute`) must never ship a video without a corresponding `kind="descriptions"` track — `mute` without description is a 1.2.5 failure.

---

## 4. Publish Gate — Before-Publish Check (the contract this audit mandates)

Current state (`api/main.py` verified):

- `POST /api/master/audio` **records** `transcript_linked/timestamps` — does not enforce them.
- `POST /api/master/data` **records** `sources=[AUDIO/VIDEO]` — does not require transcript/captions.
- `POST /api/master/live` **records** `feeds` — does not require caption artefacts.
- No `/api/master/publish` or `Export` endpoint enforces 1.2 yet; `HARNESS_BOUNDARY_AUDIT:32` seal set (`SCENARIO.json/scenario.csv/DECISION_SUMMARY.json`) does not include `.vtt` / `transcript.txt` / description track. Comment in `api/main.py:200` `Harness records transcript_linked, publish gate will enforce` is the **intended** gate, not the implemented gate.

**Required gate before publish** (must be wired before 22-file `Complete Report Pack` or `site` Netlify `push live` ships any audio/video):

```
Before deliverable.zip / verify.html / site publish emits any time-based media:
  IF Data.sources ∩ {AUDIO, VIDEO} ≠ ∅
     → REQUIRE transcript artefact (1.2.1) + WebVTT captions artefact (1.2.2) 
       + description artefact (1.2.3/1.2.5) if VIDEO, all hashed in MANIFEST, verify_result includes {captions_ok, transcript_ok, description_ok}
  IF Audio.sources ∩ {LIVE, STT} ≠ ∅  OR  Audio.transcript_linked == false with LIVE in sources
     → REQUIRE live-captions artefact (1.2.4) — reject seal with 422 transcript_linked:false for LIVE; publish rejects missing WebVTT live.
  IF Live.feeds ∩ {WEB, CUSTOM_API, NEWS, SIMULATED} MAY carry audio/video
     → REQUIRE declaration `media_kind: AUDIO_ONLY|VIDEO_ONLY|AUDIO_VIDEO|NONE` per feed 
       + corresponding artefact(s) per media_kind (same table above); if NONE, publish allows but records `media_kind:NONE`.
  ELSE (no audio/video in manifest) → PASS — gate records {captions: N/A}
```

Until wired, the **mitigation is procedural**: no `AUDIO`/`VIDEO` in `Data.sources` and no `LIVE` in `Audio.sources` and no `WEB/CUSTOM_API` live video in `Live.feeds` may be put in a `PROTOCOL` that is promoted to `docs/evidence/` or `site/`. Current staging respects this (no media seeded in `missions/master_demo_wtf001.yaml`, no `VideoConfig` type exists), so mitigation holds today.

---

## 5. Per-Source Verdict Table (before publish)

| # | Source | Example `POST` | WCAG 1.2 Applicable | Current State | Pass/Fail Before Publish | Evidence |
|---|--------|---------------|---------------------|---------------|--------------------------|----------|
| D1 | `Data:CSV/JSON/TEXT/DOCUMENTS/DATASET` | `POST /master/data {sources:[CSV]}` | 1.2 N/A | No media field | **PASS** | `mission.py:198` `DataConfig` |
| D2 | `Data:IMAGES` | `sources:[IMAGES]` | 1.1.1 (not 1.2) | No 1.2 required | **PASS (1.2 N/A)** | — |
| D3 | `Data:AUDIO` prerecorded | `sources:[AUDIO]` | 1.2.1 + 1.2.2 | `DataConfig` has no transcript/caption fields; `/data` 201 without them | **FAIL if published** — blank Data AUDIO without transcript+WebVTT would fail 1.2.1/1.2.2 at publish. **PASS today** because no such mission is promoted to evidence/site and no `<audio>` ships in `app/`. | `mission.py:198-204`, `api/main.py:107` |
| D4 | `Data:VIDEO` prerecorded | `sources:[VIDEO]` | 1.2.1/1.2.2/1.2.3/1.2.5 | Same — no caption/description fields; no `VideoConfig` type exists | **FAIL if published** without `.vtt` captions + description track. **PASS today** because `app/index.html` has no `<video>` and no `VIDEO` mission is sealed to `outputs/→docs/evidence`. | `mission.py:201`, `grep VideoConfig` zero |
| A1 | `Audio:UPLOADED / TTS / MODEL_VOICE / HUMAN_VOICE` prerecorded | `POST /master/audio {sources:[UPLOADED], transcript_linked:true, timestamps:true}` | 1.2.1 + 1.2.2 | `transcript_linked:true` default, `timestamps:true` — **records** obligation; does not ship `.vtt` file itself | **CONDITIONAL PASS** — sealed config is fine; publish must require actual `.vtt`/`transcript.txt` artefact hashed in MANIFEST (not just the bool). Current `test_audio_v15.py` correctly asserts `transcript_linked:true` but does not assert artefact existence — cover in publish gate test. | `mission.py:155-163`, `api/main.py:149`, `tests/test_audio_v15.py:7` |
| A2 | `Audio:UPLOADED` with `transcript_linked:false` | `sources:[UPLOADED], transcript_linked:false` | 1.2.1 + 1.2.2 | API allows it (echoes `transcript_linked:false` 201) — would be an invalid publish | **FAIL before publish** — must be rejected by publish gate (422). Allow at config (lab may record a failed-policy attempt) but block `sealer.py` promotion. | `api/main.py:158` comment acknowledges |
| A3 | `Audio:LIVE` / `Audio:STT` live | `sources:[LIVE]` or `[STT]` | **1.2.4 live captions** | Same fields; `transcript_linked:true` is the claim that live captions will exist, but no live WebVTT/CART artefact is recorded | **FAIL if published without live captions** — 1.2.4 has no transcript-only escape. Needs live `<track kind="captions">` (or STT-derived WebVTT streamed) + stored transcript. Today pass because no `LIVE` audio is in a pushed pack. | `mission.py:146`, `api/main.py:149` |
| A4 | `Audio:LIVE, transcript_linked:false` | `sources:[LIVE], transcript_linked:false` | 1.2.4 | API 201 — should be 422 at publish | **MUST FAIL publish** — add `422 transcript_linked:false with LIVE requires captions` to publish validator. | — |
| L1 | `Live:NEWS/MARKET/WEATHER` audio-only live | `feeds:[NEWS]` may carry live audio | 1.2.4 if stream has audio | `LiveConfig` has no caption flag; relies on separate `AudioConfig` if present | **GAP** — live audio via feed without `AudioConfig` has no recorded caption obligation. | `mission.py:119`, `api/main.py:186` |
| L2 | `Live:WEB / CUSTOM_API` live AV | `feeds:[WEB]` embedding live video | 1.2.4 live captions + (if prerecorded portion) 1.2.2/1.2.5 | Same — no `media_kind` declaration per feed | **GAP** — require `media_kind` + artefacts per L2. | — |
| L3 | `Live:SIMULATED` mock live | `feeds:[SIMULATED]` | Same as L1/L2 if mock contains audio/video | Same | Same gap; mock must also declare `media_kind` or `NONE` to keep gate honest. | — |
| V1 | Future `VideoConfig` / `Data:VIDEO` rendered via `Experiment→Timeline→Render` (`BRIEF_REVOLUTIONARY_V2:57` V2 Films) | Not yet typed | 1.2.1/1.2.2/1.2.5 (prerecorded) or 1.2.4 (live) | **No `VideoConfig` exists** (`grep VideoConfig` zero) — caps/transcript/descr. have no typed home until V1.9 lands. `TECH_SPEC:48` `captions-media-accessibility when video lands` defers correctly. | **PASS deferred** — no `<video>` ships, so not violated; but publish gate must be ready before V1.9 merges. Create `docs/audits/captions.md` gate spec now as this audit does. | `mission.py:201` no video type |

**Overall verdict today: PASS — no audio/video ships; gates are correctly *recorded* but not yet *enforced* at publish.** Before any `Data:AUDIO/VIDEO` or `Audio:LIVE/STT` or `Live:WEB/CUSTOM_API` with media is promoted to `docs/evidence/` or Netlify, wire the publish gate (§4) — otherwise D3/D4/A3/L1/L2 would **BLOCK publish (1.2 A/AA failure)**.

---

## 6. Gaps & Hallucinations (priority-ordered)

### P1 — Must-fix before any media publish (BLOCK publish, not BLOCK staging)

- **G1 — No `VideoConfig`; no `Data:AUDIO/VIDEO` caption fields.** `DataConfig` (`mission.py:198`) can seal `sources:[VIDEO]` without declaring `captions`/`transcript`/`description`. No typed home for WebVTT `.vtt` hash or description track. Fix before V1.9: add `VideoConfig(BaseModel frozen=True)` (`sources: list[VideoSourceKind]`, `captions: CaptionsConfig | None`, `description: DescriptionConfig | None`, `transcript: TranscriptRef | None`) or extend `DataConfig` with `captions: Optional[CaptionsRef]` + `transcript: Optional[TranscriptRef]` + `description: Optional[DescriptionRef]`; `/data` then 422 if `VIDEO in sources and transcript is None` (prerecorded) — but keep `/data` 201 for non-media sources per ZERO-BLOAT (new fields optional). Publish validator must reject promotion without artefact hashes. Owner: before `app/index.html` ever renders `<video><track kind="captions">`.
- **G2 — `LiveConfig` carries no caption state.** `LiveConfig` (`mission.py:119`) has `feeds` + `observatory` + `compare` only. A `Live:WEB` live-video feed that carries audio can be sealed with no WCAG trace. Fix: add `media_kind: Literal["AUDIO_ONLY","VIDEO_ONLY","AUDIO_VIDEO","NONE"]=NONE` per feed (or `live.captions: Optional[LiveCaptionsRef]`) and make publish gate require `media_kind != NONE → captions artefact present`. Keep `is_safe_relative`-style fail-closed: unknown `media_kind` → `422 failed_policy`.
- **G3 — `Audio:LIVE` with `transcript_linked:false` not rejected at publish.** `api/main.py:/audio` echoes the bool and returns 201 (good for lab `attempt→denied→strategy change` evidence, per `TECH_SPEC:Watcher`). Fix: add **publish-time** validator (`sealer.py` or `/master/publish` when it lands): `if AudioSourceKind.LIVE in sources and transcript_linked is False: raise 422 caption-transcript-linked required for live (WCAG 1.2.4)`. Config stays 201; publish is 422. Add test `test_audio_live_requires_transcript_linked_at_publish` (separate from `test_audio_v15.py`).
- **G4 — No artefact hashes in MANIFEST.** `adapters/workbench.py` seal set (`SCENARIO.json/scenario.csv/DECISION_SUMMARY.json`) does not include `captions.vtt`/`transcript.txt`/`description.vtt`. Fix: `Manifest`/`verify_result` must include `captions_ok:bool`, `transcript_ok:bool`, `description_ok:bool`, `caption_hash: sha256` when media present; `MANIFEST.json` hashes the artefact files alongside the 3-file set. Verify step must check hash.

### P2 — Should-fix before audit closure (maintains Publish gate honesty)

- **G5 — Audio description has no home.** `grep -rn "audio descript"` returns zero in `axiom_harness/` + `app/` — neither `AudioConfig` nor `LiveConfig` nor `DataConfig` mentions `audio_description`. WCAG 1.2.3/1.2.5 require description for `VIDEO`. Fix: add `description: Optional[DescriptionConfig]` (fields: `present:bool`, `track_path:str`, `hash:sha256`) to every video-carrying config; when `VIDEO` in sources and `description.present is False`, publish requires full media alternative transcript that includes visual info — record which path was taken.
- **G6 — No `.vtt` / `kind="captions|descriptions"` convention.** `grep` for `.vtt`/`<track` in `Staging/` is zero — no convention for where captions live (`outputs/<id>/media/captions.en.vtt`, `docs/evidence/<id>/captions.en.vtt`). Fix: declare `outputs/<id>/media/captions.<lang>.vtt` + `transcript.txt` + `description.vtt` as canonical, jail-checked via `is_safe_relative`, hashed into MANIFEST.
- **G7 — Timeline has no caption track rendering.** `timeline.html` AUDIO track is a stub `waveform + STT transcript (V1.5 stub — not in V1 runtime)` (`wireframes/timeline.html:29`). When captions land, `Timeline` must render `<audio>`/`<video>` + `<track kind="captions">` or a synced cue overlay driven by `timestamps` WebVTT — not a separate transcript link. Keep scrub `click ◆ → cue` behavior.
- **G8 — `FFmpeg/TTS` heavy deps not containerized/lazy-loaded.** `FULL_BUILD_STATUS_GAPS:92` flags it; prior caption audit row 6 flags same. TTS synthesis or caption burn-in without lazy-load risks `app/index.html` pulling heavy JS. Fix: defer `FFmpeg.wasm`/`TTS` to dynamic `import()` only when `tracks {Video,Audio}` are `AUDIO_VIDEO`, as `TECH_SPEC` Extensibility §4 mandates.

### Informational — not a publish BLOCK but note

- **I1 — `Data:IMAGES` + audio composite.** If lab ever composes `IMAGES + AUDIO` into a synchronized presentation, that composite is 1.2.2/1.2.5 media — the composite's WebVTT must caption the audio and describe the image sequence. No composite builder exists today, so not BLOCK.
- **I2 — Human voice transcripts vs captions.** `Audio:HUMAN_VOICE` in V3 (`Human Axiom` `HUMAN vs Live AI` §31) — human speech must be captioned on the same basis as model speech. `Human` participant transcripts already have `RESULT+EVIDENCE+...` receipt; captions gate applies uniformly.

### Hallucinations this audit kills

- **H1 — "Harness ships video without captions and passes 1.2."** It does not ship any `<video>` today (`app/index.html` zero media tags) and docs correctly state `Video is presentation, not proof` + `captions-media-accessibility when video lands`. Pass holds only until media lands — this audit makes the "when" condition explicit (§4 gate).
- **H2 — "`transcript_linked:true` alone satisfies 1.2.2/1.2.4."** False — transcript (text alternative, 1.2.1/1.2.3) alone fails 1.2.2/1.2.4 which require **synchronised** captions. This audit enforces synced WebVTT artefact, not just the bool.
- **H3 — "`LIVE` audio is temporal and exempt from captions."** False at AA — 1.2.4 live captions are AA-critical. Deferred-to-publish is allowed; exempt is not.

---

## 7. Recommendations (ready-to-apply shape)

**Before V1.9 `Video` merges** (keep ZERO-BLOAT: types present, runtime only when V1.9 demo runs):

```python
# mission.py — additive, frozen, optional (no core mutation)
class CaptionsRef(BaseModel):
    model_config = {"frozen": True}
    path: str          # jail-checked via is_safe_relative, e.g. "media/captions.en.vtt"
    hash: str          # sha256:<hex>
    lang: str = "en"
    kind: Literal["captions", "descriptions"] = "captions"

class TranscriptRef(BaseModel):
    model_config = {"frozen": True}
    path: str
    hash: str
    lang: str = "en"

# Add optional refs to DataConfig (no new endpoint):
# data: DataConfig(captions: CaptionsRef|None, transcript: TranscriptRef|None, description: CaptionsRef|None)
# LiveConfig: add  media_kind: Literal["AUDIO_ONLY","VIDEO_ONLY","AUDIO_VIDEO","NONE"] = "NONE"
# AudioConfig: keep transcript_linked but publish gate checks artefact hashes, not just bool

# api/main.py publish gate (when /publish or sealer.py lands):
# if Data.VIDEO in sources: require data.transcript and (data.captions or data.description)  # 1.2.1/1.2.2/1.2.5
# if Audio.LIVE in sources and not audio.transcript_linked: 422 WCAG 1.2.4  # plus WebVTT hash
```

**Timeline render when video lands:**

```html
<video controls preload="metadata" crossorigin="anonymous">
  <source src="media/experiment-001.mp4" type="video/mp4">
  <track kind="captions" srclang="en" label="English" src="media/captions.en.vtt" default>
  <track kind="descriptions" srclang="en" label="Audio description" src="media/description.en.vtt">
</video>
<!-- fallback transcript link adjacent, not instead of captions -->
<a href="media/transcript.txt">Full transcript (1.2.1/1.2.3 alternative)</a>
```

**Tests to add alongside gate:**

```python
# tests/test_captions_publish_gate.py
def test_data_video_requires_captions_and_transcript_at_publish(): ...
def test_audio_live_requires_transcript_linked_at_publish(): ...       # 422 if false
def test_live_web_media_kind_none_passes_without_captions(): ...
def test_live_web_audio_video_requires_live_captions(): ...            # 1.2.4
def test_valid_media_with_vtt_hash_promotes_to_manifest(): ...
```

---

## 8. Verification Performed (this session)

- **Read** `FULL_BUILD_STATUS_GAPS_2026-09-24.md` (all 117 lines) — confirms V1.5 `AudioConfig` WCAG label, V1.9 `Video Timeline` as unbuilt, `FFmpeg/TTS` deferred.
- **Read** `app/index.html` + `app.css` + `wireframes/{control,environment,timeline,live,evidence}.html` + `site/index.html` bodies — **zero** `<audio>`/`<video>`/`<track>`/`.vtt` tags (`grep` corroborated). Harness correctly not a media player; Timeline tracks declared as stub with `Video is presentation, not proof`.
- **Read** `axiom_harness/mission.py` + `api/main.py:/data|/audio|/live` handlers — verified `DataConfig`/`AudioConfig`/`LiveConfig` shapes (frozen, optional on `MasterMission`), 201/422 fail-closed, **no caption enforcement at config** (by design, comment `publish gate will enforce`), no `VideoConfig`, no `media_kind`, no `audio_description` field (`grep` zero).
- **Read** `tests/test_data_v13.py`, `test_audio_v15.py`, `test_live_v17.py` — verify `transcript_linked:true` recorded, `frozen` prevents mutation, but publish-gate tests absent (expected).
- **Read** `docs/API_SPEC.md` / `TECH_SPEC.md` / `ARCHITECTURE.md` — paper declares `tracks {Video,Audio,Transcript,...}` + `captions-media-accessibility when video lands` (paper, not runtime).
- **Grepped** `Staging/` for `caption/transcript/audio descript/.vtt/<track` — only `transcript_linked`, `STT transcript (V1.5 stub)`, and `captions-media-accessibility` prose found; no false positive of shipped captions.
- **Grep** `axiom_harness/` for `VideoConfig|video` — zero `VideoConfig`, only `DataSourceKind.VIDEO` in `DataConfig.sources` — confirms video WCAG has no typed home yet.

**Unresolved evidence:** No actual `.mp4`/`.vtt`/`.mp3` media artefact exists in `outputs/` or `docs/evidence/` to probe a live caption render; `FFmpeg`/`TTS` not installed so waveform-to-caption pipeline not exercised; `sealer.py`/`/publish` endpoint not yet implemented — so publish-gate enforcement is verified as *specification* (§4) not as runtime `curl` proof. Mark resolved when V1.9 demo wires `sealer.py` + `MANIFEST` WebVTT hash + `verify_result {captions_ok}` and `test_captions_publish_gate.py` is green.

---

## 9. Status for `docs/AUDIT_MASTER_GAPS_HALLUCINATIONS.md` Row

Captions/Media — WCAG 1.2 **PASS today, BLOCK before any media publish**:

- **Holds:** No `<audio>`/`<video>` ships; `AudioConfig.transcript_linked:true + timestamps:true + annotations` records the obligation; wireframes + `Video is presentation not proof` disclaimer correct; `TECH_SPEC:48` deferral honest.
- **Gaps:** No `VideoConfig`, `Data:AUDIO/VIDEO` and `Live:WEB/CUSTOM_API` need publish-gate WebVTT/transcript/description artefacts (G1-G4); audio description untyped (G5); no `.vtt` convention (G6); timeline caption rendering stub (G7); `FFmpeg/TTS` not containerized (G8).
- **Gate before publish 22-file pack / site:** `§4` validator — `Data:VIDEO→transcript+WebVTT captions+description`, `Audio:LIVE→live captions (1.2.4, no transcript-only)`, `Live:WEB/CUSTOM_API→media_kind + artefacts`, otherwise `N/A`. Until wired, procedural mitigation holds (no media in promoted missions).

**Next:** Ship G1-G4 as optional frozen refs on `DataConfig`/`LiveConfig` before V1.9, wire `sealer.py` publish gate per §4, add `tests/test_captions_publish_gate.py` (5 tests), then `MANIFEST` + `verify_result` WebVTT hashes. This file (`docs/audits/captions.md`) is the pre-publish evidence for WCAG 1.2.

*Generated — re-run workflow to regenerate after publish gate lands; do not hand-edit.*