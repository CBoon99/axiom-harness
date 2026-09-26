# Canonical Wireframes — Decision

**Date:** 2026-09-26
**Decision:** `docs/wireframes/*.html` is canonical for scalable Environment grid + Control GO/STOP/SCHEDULE + Evidence Compression receipt (`math/` hashes). `app/index.html` is canonical for live Control (Seal/GO/STOP/Run/Pause/Resume + comboboxes). `app/wireframes/` mirrors `docs/wireframes/` for dev convenience, with `app/wireframes/control.html` being a copy of `app/index.html` (live Control).

**Sync:** `cp docs/wireframes/*.html app/wireframes/` + `cp app/index.html app/wireframes/control.html` — commit `app/wireframes/` as mirror. No more drift.
