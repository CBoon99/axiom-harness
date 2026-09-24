"""Mission — frozen pre-declared rules (BML Quad Stage 1).

Pydantic frozen=True identity: any change = new id, not a patch.
V3 HUMAN/SCRIPTED/TEAM reserved as enum values with no handler until V3.x demo pack exercises them (zero-bloat, HYGIENE §2A).
"""
from __future__ import annotations

from enum import Enum
from typing import Literal, Optional
from pydantic import BaseModel, Field


class ParticipantKind(str, Enum):
    MODEL = "MODEL"
    HUMAN = "HUMAN"       # V3.0 reserved — no handler in V1
    SCRIPTED = "SCRIPTED" # V3.1 reserved
    TEAM = "TEAM"         # V3.4 reserved


class ContextKind(str, Enum):
    FRESH = "FRESH"
    PERSISTENT = "PERSISTENT"
    NO_MEMORY = "NO_MEMORY"
    SHORT = "SHORT"
    LONG = "LONG"
    COMBINED = "COMBINED"
    ISOLATED = "ISOLATED"
    SHARED = "SHARED"


class EnvKind(str, Enum):
    STATIC = "STATIC"
    SEQUENTIAL = "SEQUENTIAL"
    LIVE_FEED = "LIVE_FEED"
    SIMULATED = "SIMULATED"
    MULTI_AGENT = "MULTI_AGENT"
    ADVERSARIAL = "ADVERSARIAL"


class PermissionKind(str, Enum):
    OFF = "OFF"
    READ_ONLY = "READ_ONLY"
    LIVE = "LIVE"
    CONTROLLED_DOMAIN_LIST = "CONTROLLED_DOMAIN_LIST"


class MasterMission(BaseModel):
    model_config = {"frozen": True}

    id: str = Field(description="WTF-001 / RUNSET-0047 or HUMAN-2026-08-01 style")
    protocol: str = Field(description="canonical config (hashed) — identity §10")
    participant: ParticipantKind = Field(default=ParticipantKind.MODEL)
    model: str = Field(default="analyst", description="model A/B/C when participant=MODEL")
    model_version: str = Field(default="llama-3.2-11b", description="reproducibility — added per review gap 2")
    per_eca_state: dict = Field(default={"per": "OFF", "eca": "OFF"}, description="PER/ECA toggles per WTF-LAB §6 — review gap 2")
    cost: Optional[dict] = Field(default=None, description="{tokens_input, tokens_output, cost_usd, provider} — review gap 2")
    context_kind: ContextKind
    env_kind: EnvKind
    params: dict = Field(default_factory=dict, description="runs, duration, parallel, temp, memory, web, cost_estimate")
    permissions: dict = Field(default_factory=dict, description="source_kind → permission_kind map")
    # pressure/comparison are V1 gaps but reserved — no handler until exercised
    # cost estimate shown before GO (§15) lives in params.cost_estimate
