# Upstreams — Existence Log

- technique: keep AI out of engine/code/math BEFORE handover
- not_core_modular_engine: true — this is a technique, not engine
- rule: never hard-code — record hash only, so we can tweak/debug without forking
- stacks: eca/ per/ axiom/ each have EXISTS.md with hash placeholders
- harness_rule: `rg GateOk axiom_harness/ → 0` kept green
