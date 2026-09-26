"""Mission — frozen pre-declared rules (BML Quad Stage 1).

Pydantic frozen=True identity: any change = new id, not a patch.
V3 HUMAN/SCRIPTED/TEAM reserved as enum values with no handler until V3.x demo pack exercises them (zero-bloat, HYGIENE §2A).
"""
from __future__ import annotations

from enum import Enum
from typing import Literal, Optional
from pydantic import BaseModel, Field, field_validator


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


class ScheduleKind(str, Enum):
    ONCE = "ONCE"
    INTERVAL = "INTERVAL"
    REPEATING = "REPEATING"
    CONTINUOUS = "CONTINUOUS"
    UNTIL_CONDITION = "UNTIL_CONDITION"
    CRON = "CRON"


class ScheduleConfig(BaseModel):
    model_config = {"frozen": True, "protected_namespaces": ()}

    kind: ScheduleKind
    start_at: Optional[str] = Field(default=None, description="ISO8601 start")
    end_at: Optional[str] = Field(default=None, description="ISO8601 end or null for continuous")
    interval_seconds: Optional[int] = Field(default=None, description=">0 for INTERVAL/REPEATING")
    repeats: Optional[int] = Field(default=None, description="count for REPEATING")
    duration_seconds: Optional[int] = Field(default=None, description="fixed duration per run")
    until_condition: Optional[str] = Field(default=None, description="condition id for UNTIL_CONDITION")
    cron: Optional[str] = Field(default=None, description="cron for CRON kind")


class ParallelMode(str, Enum):
    ONE = "ONE"
    SEQUENCE = "SEQUENCE"
    ALL = "ALL"
    PARALLEL = "PARALLEL"


class ParallelConfig(BaseModel):
    model_config = {"frozen": True, "protected_namespaces": ()}

    mode: ParallelMode = Field(default=ParallelMode.PARALLEL)
    parallel_count: int = Field(default=1, ge=1, le=64, description="isolated sandboxes, §14 — capped 64 for cost")
    model_matrix: Optional[list[str]] = Field(default=None, description="§62 model set — e.g. [A,B,C,D] — each gets timeline")
    isolated: bool = Field(default=True, description="each sandbox isolated context/memory/tools")


class PerEcaState(BaseModel):
    model_config = {"frozen": True, "protected_namespaces": ()}
    per: Literal["OFF", "ON"] = Field(default="OFF", description="PER toggle — Literal OFF|ON, frozen inner")
    eca: Literal["OFF", "ON"] = Field(default="OFF", description="ECA toggle — Literal OFF|ON, frozen inner")

    def __getitem__(self, key):
        if key in ("per", "eca"):
            return getattr(self, key)
        raise KeyError(key)

    def get(self, key, default=None):
        return getattr(self, key) if key in ("per", "eca") else default

    def __contains__(self, key):
        return key in ("per", "eca")

    def __eq__(self, other):
        if isinstance(other, dict):
            return self.per == other.get("per") and self.eca == other.get("eca")
        if isinstance(other, PerEcaState):
            return self.per == other.per and self.eca == other.eca
        return False


class PerConfig(BaseModel):
    model_config = {"frozen": True, "protected_namespaces": ()}
    enabled: bool = Field(default=False, description="PER bolt-on — frozen Optional, behind ensure_off + LOCK-STATUS gate")
    mode: Literal["OFF", "ON"] = Field(default="OFF", description="PER mode — OFF until ReceiptIndex+Telescope+ΔH gates wired")


class EcaConfig(BaseModel):
    model_config = {"frozen": True, "protected_namespaces": ()}
    enabled: bool = Field(default=False, description="ECA bolt-on — frozen Optional, behind ensure_off + LOCK-STATUS gate")
    mode: Literal["OFF", "ON"] = Field(default="OFF", description="ECA mode — OFF until GateOk wired")


class VisualConfig(BaseModel):
    model_config = {"frozen": True, "protected_namespaces": ()}
    enabled: bool = Field(default=False, description="Visual Layer 4 — frozen Optional, one room only, 393,216:1")
    layer: Literal[4] = Field(default=4, description="Layer 4 only — verified not to touch World-A")
    compression_ratio: int = Field(default=393216, description="393,216:1 — 1024x1024 → 224x224 → 14x14 patches → 576 tokens")
    isolated: bool = Field(default=True, description="each visual isolated context")


class MasterMission(BaseModel):
    model_config = {"frozen": True, "protected_namespaces": ()}

    id: str = Field(description="WTF-001 / RUNSET-0047 or HUMAN-2026-08-01 style")
    protocol: str = Field(description="canonical config (hashed) — identity §10")
    participant: ParticipantKind = Field(default=ParticipantKind.MODEL)
    model: str = Field(default="analyst", description="model A/B/C when participant=MODEL")
    model_version: str = Field(default="llama-3.2-11b", description="reproducibility — added per review gap 2")
    per_eca_state: PerEcaState = Field(default_factory=PerEcaState, description="PER/ECA toggles per WTF-LAB §6 — FrozenDict Literal OFF|ON, inner immutable")
    cost: Optional[dict] = Field(default=None, description="{tokens_input, tokens_output, cost_usd, provider} — review gap 2")
    context_kind: ContextKind
    env_kind: EnvKind
    params: dict = Field(default_factory=dict, description="runs, duration, parallel, temp, memory, web, cost_estimate")
    permissions: dict = Field(default_factory=dict, description="source_kind → permission_kind map")
    schedule: Optional[ScheduleConfig] = Field(default=None, description="V1.1 Scheduling — room 15, isolated, no core mutation")
    parallel: Optional[ParallelConfig] = Field(default=None, description="V1.2 Parallel — room 14, isolated, §14 + model matrix §62")
    data: Optional["DataConfig"] = Field(default=None, description="V1.3 Data Room — §29, isolated, AI proposes Harness executes")
    language: Optional["LanguageConfig"] = Field(default=None, description="V1.4 Multilingual — §20-22, language as experimental variable, §21 cross-language")
    audio: Optional["AudioConfig"] = Field(default=None, description="V1.5 Speech/Audio — §18-19, first-class audio modality")
    sensors: Optional["SensorConfig"] = Field(default=None, description="V1.6 Sensors — §28, identity/source/timestamp/permission/status/policy/schema")
    live: Optional["LiveConfig"] = Field(default=None, description="V1.7 Live feeds + Observatory — §30-32, same stream isolated contexts")
    multi_agent: Optional["MultiAgentConfig"] = Field(default=None, description="V1.8 Multi-agent — A Analyst B Critic C Maker D Observer E Adversary, isolated")
    video: Optional["VideoConfig"] = Field(default=None, description="V1.9 Video Timeline — §24 upload/live_feed/synthetic, presentation not proof §70")
    films: Optional["FilmsConfig"] = Field(default=None, description="V2 Films — Experiment→Story §25/27, isolated render")
    observatory: Optional["ObservatoryConfig"] = Field(default=None, description="V2+ Observatory — Risk/Alerts per-feed §66-67, isolated")
    external_api: Optional["ExternalAPIConfig"] = Field(default=None, description="Future External API — §51 GET /human/{id}/trail reserved, isolated")
    human: Optional["HumanConfig"] = Field(default=None, description="V3 Human Axiom — persons/instruments/responses §105-114, isolated")
    per: Optional["PerConfig"] = Field(default=None, description="V1.10 PER — frozen Optional bolt-on, gated OFF until LOCK-STATUS wired")
    eca: Optional["EcaConfig"] = Field(default=None, description="V1.10 ECA — frozen Optional bolt-on, gated OFF until GateOk wired")
    visual: Optional["VisualConfig"] = Field(default=None, description="V2 Visual Layer 4 — frozen Optional, one room 393,216:1, verified not to touch World-A")
    # pressure/comparison are V1 gaps but reserved — no handler until exercised
    # cost estimate shown before GO (§15) lives in params.cost_estimate

    @field_validator("per_eca_state", mode="before")
    @classmethod
    def _validate_per_eca_state(cls, v):
        if isinstance(v, dict) and len(v) == 0:
            raise ValueError("failed_policy: per_eca_state empty — requires per+eca")
        if v is None:
            raise ValueError("failed_policy: per_eca_state missing")
        return v


class LiveFeedKind(str, Enum):
    NEWS = "NEWS"
    MARKET = "MARKET"
    WEATHER = "WEATHER"
    WEB = "WEB"
    CUSTOM_API = "CUSTOM_API"
    SIMULATED = "SIMULATED"


class LiveConfig(BaseModel):
    model_config = {"frozen": True, "protected_namespaces": ()}

    feeds: list[LiveFeedKind] = Field(default_factory=list, description="§30 live streams — NEWS/MARKET/WEATHER/WEB/CUSTOM/SIMULATED")
    observatory: bool = Field(default=False, description="§31-32 multi-model comparative observation, same feed isolated")
    models: Optional[list[str]] = Field(default=None, description="observatory model set — each isolated context")
    compare: bool = Field(default=True, description="parallel timeline compare §32")


class AgentRole(str, Enum):
    ANALYST = "Analyst"
    CRITIC = "Critic"
    MAKER = "Maker"
    OBSERVER = "Observer"
    ADVERSARY = "Adversary"


class MultiAgentConfig(BaseModel):
    model_config = {"frozen": True, "protected_namespaces": ()}

    enabled: bool = Field(default=False, description="V1.8 enable flag — default False, isolated §14")
    agents: list[AgentRole] = Field(
        default_factory=lambda: [
            AgentRole.ANALYST,
            AgentRole.CRITIC,
            AgentRole.MAKER,
            AgentRole.OBSERVER,
            AgentRole.ADVERSARY,
        ],
        description="5 agents A Analyst B Critic C Maker D Observer E Adversary — isolated §14/§62 — default ['A','B','C','D','E'] aliases",
    )
    isolated: bool = Field(default=True, description="each agent isolated context/memory/tools")
    parallel: int = Field(default=1, ge=1, le=16, description="parallel shards 1..16, isolated §14/§62")


class VideoSourceKind(str, Enum):
    UPLOAD = "UPLOAD"
    LIVE_FEED = "LIVE_FEED"
    SYNTHETIC = "SYNTHETIC"


class VideoConfig(BaseModel):
    model_config = {"frozen": True, "protected_namespaces": ()}

    enabled: bool = Field(default=False, description="V1.9 enable flag — default False, isolated §24")
    source: VideoSourceKind = Field(default=VideoSourceKind.UPLOAD, description="video source §24 upload/live_feed/synthetic")
    max_duration_sec: int = Field(default=60, ge=1, le=3600, description="max duration §26 1..3600, presentation not proof")
    transcription: bool = Field(default=False, description="model transcription enabled, captions required before publish §24-26")
    isolated: bool = Field(default=True, description="each video isolated context/memory")


class FilmsConfig(BaseModel):
    model_config = {"frozen": True, "protected_namespaces": ()}

    enabled: bool = Field(default=False, description="V2 Films enable — Experiment→Story §25/27, isolated")
    template: Literal["chronological", "comparative", "ghost"] = Field(default="chronological", description="story template §25")
    auto_chapters: bool = Field(default=True, description="auto chapters from timeline events §25")
    isolated: bool = Field(default=True, description="each film isolated render context")


class ObservatoryConfig(BaseModel):
    model_config = {"frozen": True, "protected_namespaces": ()}

    enabled: bool = Field(default=False, description="V2+ Observatory enable — Risk/Alerts per-feed §66-67, isolated")
    feeds: list[LiveFeedKind] = Field(default_factory=list, description="per-feed Risk/Alerts §66 NEWS/MARKET/WEATHER/WEB/CUSTOM/SIMULATED")
    alert_on_drift: bool = Field(default=True, description="alert ΔH>0.5 drift §66")
    alert_on_orphan: bool = Field(default=True, description="alert orphan[] §66")
    isolated: bool = Field(default=True, description="each alert isolated context")


class ExternalAPIConfig(BaseModel):
    model_config = {"frozen": True, "protected_namespaces": ()}

    enabled: bool = Field(default=False, description="Future External API enable — §51, isolated")
    base_url: str = Field(default="https://api.example.org", description="external API base — generic, not hard-coded provider")
    trail_path: str = Field(default="/human/{id}/trail", description="GET /human/{id}/trail reserved §51")
    isolated: bool = Field(default=True, description="each external call isolated")


class HumanConfig(BaseModel):
    model_config = {"frozen": True, "protected_namespaces": ()}

    enabled: bool = Field(default=False, description="V3 Human Axiom — persons/instruments/responses §105-114, isolated")
    persons: list[str] = Field(default_factory=list, description="person ids HUMAN-2026-08-01 style §107")
    instrument: str = Field(default="Human 8D — 80 dilemmas", description="instrument id + version §108")
    trail_path: str = Field(default="/human/{id}/trail", description="GET /human/{id}/trail read §112")
    isolated: bool = Field(default=True, description="each human trail isolated")


class SensorKind(str, Enum):
    PHYSICAL = "PHYSICAL"
    ENVIRONMENTAL = "ENVIRONMENTAL"
    DIGITAL = "DIGITAL"
    AI = "AI"
    HUMAN = "HUMAN"
    IOT = "IOT"


class SensorConfig(BaseModel):
    model_config = {"frozen": True, "protected_namespaces": ()}

    kinds: list[SensorKind] = Field(default_factory=list, description="§28 sensor families")
    identities: Optional[list[str]] = Field(default=None, description="sensor ids — recorded per timeline")
    recording_policy: str = Field(default="ALWAYS", description="ALWAYS / ON_EVENT / MANUAL — §28 policy")
    data_schema: Optional[str] = Field(default=None, description="schema ref for sensor payload")


class AudioSourceKind(str, Enum):
    TTS = "TTS"
    STT = "STT"
    UPLOADED = "UPLOADED"
    LIVE = "LIVE"
    MODEL_VOICE = "MODEL_VOICE"
    HUMAN_VOICE = "HUMAN_VOICE"


class AudioConfig(BaseModel):
    model_config = {"frozen": True, "protected_namespaces": ()}

    sources: list[AudioSourceKind] = Field(default_factory=list, description="§18 TTS/STT/uploaded/live/model/human voice")
    multi_speaker: bool = Field(default=False, description="multiple speakers + identification")
    timestamps: bool = Field(default=True, description="audio timestamps for timeline sync")
    transcript_linked: bool = Field(default=True, description="audio linked to transcript events, captions required before publish")
    annotations: bool = Field(default=True, description="trim/move/split/mute/replay/annotate §§18-19")


class LanguageCode(str, Enum):
    EN = "EN"
    ID = "ID"
    ES = "ES"
    FR = "FR"
    DE = "DE"
    ZH = "ZH"
    JA = "JA"
    AR = "AR"
    HI = "HI"
    PT = "PT"


class LanguageConfig(BaseModel):
    model_config = {"frozen": True, "protected_namespaces": ()}

    primary: LanguageCode = Field(default=LanguageCode.EN)
    variants: Optional[list[LanguageCode]] = Field(default=None, description="§22 parallel runs — same model/experiment different language")
    keep_params_constant: bool = Field(default=True, description="§21 control — other variables constant")
    detect_switch: bool = Field(default=True, description="detect unexpected language switching")


class DataSourceKind(str, Enum):
    CSV = "CSV"
    JSON = "JSON"
    TEXT = "TEXT"
    DOCUMENTS = "DOCUMENTS"
    DATASET = "DATASET"
    IMAGES = "IMAGES"
    AUDIO = "AUDIO"
    VIDEO = "VIDEO"


class DataConfig(BaseModel):
    model_config = {"frozen": True, "protected_namespaces": ()}

    sources: list[DataSourceKind] = Field(default_factory=list, description="§29 uploads — CSV/JSON/text/docs/dataset/images/audio/video")
    dataset_refs: Optional[list[str]] = Field(default=None, description="sandbox-relative refs, jail-checked at execution")
    validated: bool = Field(default=False, description="Harness validated schema — AI proposal not auto-executed")
    transforms_approved: bool = Field(default=False, description="AI proposes, Harness executes only if approved")
