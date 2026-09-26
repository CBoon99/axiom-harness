# ECA — Existence Log

- stack: ECA
- exists: true (technique placeholder, not engine)
- source_path: `Axiom Evidence Layer/ECA/plugin/` (all plugin/**/*.py cat|sha256)
- implementation_hash: `e3c508b2695f38425f4dc0cfdcb545e66ae62d8dcfc7df80f27c621aae20c719` (from HANDOFF — cat plugin/**/*.py | sha256, e.g. __init__.py 97c6be8c…)
- config_hash: `1be70761bcdc55d644e99fc15a47d97b449e94f58e25e180351528de392675c3` (`ECA/plugin/config/eca.v1.json` `eca-v1.0.0-20230901`)
- historical_blocked: `ECA/sim/telescope.py` `bf7329c836d8b8208bb06b2e132c9c4fd6315aee2669b09b697b92a3ccf1a508` — HISTORICAL / BLOCKED
- version: eca-v1.0.0 / plugin 1.0.0 `model claude-sonnet-4-5-20250929`
- status: UPSTREAM-BLOCKED — not Harness-certified, Harness records hash only, never calculates GateOk/ΔH/T_max
