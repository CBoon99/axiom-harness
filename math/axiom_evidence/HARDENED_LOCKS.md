# Axiom Workbench — 8 Hard Locks (Keep AI Out of Engine/Code/Math)

> Saved verbatim from Carl 2026-09-25 — modular technique to keep AI out, not core engine. Source: Documents/Axiom-Workbench/axiom_wb/
> Each lock is hash-locked where applicable; never hard-code values — tweak via manifest/lockfile.

## Lock 1: Path Jail — Symlink, Unicode & Path Traversal Lockdown
**Closes:** UTF-8 division slashes \u2215/\u2200, symlinks inside root pointing outside, UNC \\?\ paths
**File:** `axiom_wb/paths.py` — `resolve_jail_path()`
```python
import os, sys, re, unicodedata
from pathlib import Path

class PathJailError(SecurityError): pass

def resolve_jail_path(user_path: str, root: Path) -> Path:
    normalized = unicodedata.normalize("NFC", str(user_path)).replace("\\", "/")
    parts = [p for p in normalized.split("/") if p]
    if ".." in parts or "." in parts or "~" in parts:
        raise PathJailError("Directory traversal token detected")
    if re.search(r"[\x00-\x1f\x7f-\x9f;|&$`\n\r]|\$\(|<\(|>\(", normalized):
        raise PathJailError("Unsafe shell/control characters in path")
    resolved_root = root.resolve(strict=True)
    candidate = (resolved_root / normalized).resolve(strict=False)
    if candidate.is_symlink():
        raise PathJailError("Symlinks are strictly forbidden")
    try:
        candidate.relative_to(resolved_root)
    except ValueError:
        raise PathJailError(f"Path escape attempt: {candidate} outside {resolved_root}")
    return candidate
```

## Lock 2: Factory Allowlist — Cryptographic Hash Verification
**Closes:** AI writing `scripts/factory_*.py` matching regex and executing arbitrary logic
**Files:** `axiom_wb/paths.py & constants.py` + SHA-256 Manifest Lockfile
```python
import hashlib, json, re
from pathlib import Path

FACTORY_PATTERN = re.compile(r"^scripts/factory_[A-Za-z0-9_\-]+\.py$")

def verify_factory_script(rel_path: str, engine_root: Path, manifest_path: Path) -> Path:
    norm = rel_path.replace("\\", "/").strip("/")
    if not FACTORY_PATTERN.match(norm) or norm.count("/") != 1:
        raise PathJailError(f"Script {norm} violates factory naming policy")
    script_path = (engine_root / norm).resolve(strict=True)
    if not manifest_path.exists():
        raise SecurityError("Factory lockfile manifest missing")
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    expected_hash = manifest.get(norm)
    if not expected_hash:
        raise SecurityError(f"Unregistered factory script: {norm}")
    actual_hash = hashlib.sha256(script_path.read_bytes()).hexdigest()
    if actual_hash != expected_hash:
        raise SecurityError(f"Factory script tampering detected! Hash mismatch on {norm}")
    return script_path
```

## Lock 3: Subprocess Isolation — OS Namespace & Sandbox Jail
**Closes:** Network exfiltration, fork bombs, memory exhaustion
**File:** `axiom_wb/bridge.py`
```python
import os, subprocess, signal
from pathlib import Path

def execute_factory_isolated(factory_path: Path, engine_dir: Path, timeout_sec: int = 30) -> str:
    argv = [
        "unshare", "--net",
        sys.executable, "-I", "-B",
        str(factory_path)
    ]
    def preexec_limits():
        import resource
        resource.setrlimit(resource.RLIMIT_AS, (1 * 1024 * 1024 * 1024, 1 * 1024 * 1024 * 1024))
        resource.setrlimit(resource.RLIMIT_NPROC, (10, 10))
        os.setsid()
    try:
        proc = subprocess.Popen(
            argv,
            cwd=str(engine_dir),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            preexec_fn=preexec_limits,
            start_new_session=True
        )
        stdout, stderr = proc.communicate(timeout=timeout_sec)
        if proc.returncode != 0:
            raise RuntimeError(f"Factory execution failed (code {proc.returncode}): {stderr}")
        return stdout
    except subprocess.TimeoutExpired:
        os.killpg(proc.pid, signal.SIGKILL)
        raise TimeoutExpired(f"Factory process exceeded {timeout_sec}s limit")
```

## Lock 4: Mission Text Lockdown — Strict Schema & Pydantic Immutability
**Closes:** Prompt injection via format strings / AST eval in mission payloads
**File:** `axiom_wb/axiom_mission.py`
```python
from pydantic import BaseModel, ConfigDict, field_validator
import re

class MissionPacket(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid", str_strip_whitespace=True)
    mission_id: str
    target_metric: str

    @field_validator("*", mode="before")
    @classmethod
    def reject_code_injection_patterns(cls, v: object) -> object:
        if isinstance(v, str):
            if re.search(r"[;|&$`\x00]|\$\(|<\(|>\(|\{\{|%\{|eval\(|exec\(", v):
                raise ValueError("Code/Template injection character in mission parameter")
        return v
```

## Lock 5: Type-Level Metric Locking — Literal[False] Invariant
**Closes:** `model_construct()` / monkey-patch bypass of `ai_computed_metrics`
**Files:** `axiom_wb/core_types.py & pipeline.py`
```python
from typing import Literal
from pydantic import BaseModel, ConfigDict, field_validator

class EvaluationResult(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    ai_computed_metrics: Literal[False] = False
    metric_value: float
    execution_hash: str

    @field_validator("ai_computed_metrics", mode="before")
    @classmethod
    def enforce_false_literal(cls, v: object) -> bool:
        if v is not False:
            raise ValueError("CRITICAL SECURITY VIOLATION: ai_computed_metrics cannot be True")
        return False
```

## Lock 6: Provenance Protection — Strict Engine Allowlist
**Closes:** Blacklist bypass (`claude/deepseek/llama/vllm` or `G P T`)
**File:** `axiom_wb/core_types.py`
```python
from enum import Enum
from pydantic import BaseModel, ConfigDict, field_validator
import math

class DeterministicEngineSource(str, Enum):
    NUMPY_KERNEL = "numpy_kernel"
    SCIPY_STATS = "scipy_stats"
    NATIVE_CPP = "native_cpp_bridge"
    FACTORY_DETERMINISTIC = "factory_deterministic"

class MetricResult(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    source: DeterministicEngineSource
    value: float

    @field_validator("value")
    @classmethod
    def validate_finite_number(cls, v: float) -> float:
        if not math.isfinite(v):
            raise ValueError("Metric value must be a finite numerical float")
        return v
```

## Lock 7: Deterministic Report Verifier — Canonical Floating-Point Matching
**Closes:** Rounding false positives + orphan hallucinated numbers
**File:** `axiom_wb/verify.py`
```python
import re, json
from decimal import Decimal
from pathlib import Path

NUM_RE = re.compile(r"([-+]?(?:\d+\.\d+|\d+)(?:[eE][-+]?\d+)?)")
HEX_RE = re.compile(r"\b[a-fA-F0-9]{16,}\b")

def canonicalize_number(val_str: str) -> str:
    try:
        d = Decimal(val_str)
        return f"{d.normalize():f}"
    except Exception:
        return val_str

def verify_report_integrity(report_text: str, artifact_paths: list[Path], float_tol: float = 1e-4) -> tuple[bool, list[str]]:
    ground_truth_text = " ".join([p.read_text(encoding="utf-8") for p in artifact_paths if p.exists()])
    report_clean = HEX_RE.sub("", report_text)
    corpus_clean = HEX_RE.sub("", ground_truth_text)
    corpus_raw_numbers = set(NUM_RE.findall(corpus_clean))
    corpus_floats = []
    for n in corpus_raw_numbers:
        try: corpus_floats.append(float(n))
        except ValueError: pass
    report_numbers = NUM_RE.findall(report_clean)
    orphans = []
    for num_str in report_numbers:
        try:
            val_float = float(num_str)
            matches = any(math.isclose(val_float, c, abs_tol=float_tol) for c in corpus_floats)
            if not matches:
                orphans.append(num_str)
        except ValueError:
            if num_str not in corpus_raw_numbers:
                orphans.append(num_str)
    is_valid = len(orphans) == 0
    return is_valid, orphans
```

## Lock 8: Immutable Engine Root & Environment Isolation
**Closes:** `AXIOM_ENGINE_ROOT` env hijack to malicious directory
**File:** `axiom_wb/config.py`
```python
import os
from pathlib import Path

_CANONICAL_SERVICE_ROOT = Path(__file__).resolve().parents[1]

def service_root() -> Path:
    if os.getenv("AXIOM_STRICT_MODE", "1") == "1":
        root = _CANONICAL_SERVICE_ROOT
    else:
        env_override = os.getenv("AXIOM_SERVICE_ROOT")
        root = Path(env_override).resolve() if env_override else _CANONICAL_SERVICE_ROOT
    if hasattr(os, "access") and hasattr(os, "W_OK"):
        if os.access(root / "axiom_wb", os.W_OK):
            pass
    return root
```

### Summary Stack
```
[ LAYER 1: PATH JAIL ]       NFC + symlink prohibition
[ LAYER 2: FACTORY LOCK ]    SHA-256 lockfile hash verification
[ LAYER 3: OS SUBPROCESS ]   unshare --net + prlimit 1GB/10 procs
[ LAYER 4: MISSION INGRESS ] frozen + extra=forbid + injection regex
[ LAYER 5: METRIC LOCK ]     Literal[False] at type level
[ LAYER 6: PROVENANCE ]      Enum allowlist (No LLM strings)
[ LAYER 7: VERIFIER ]        Decimal/float ground-truth match
[ LAYER 8: ENGINE ROOT ]     Canonical path + env override protected
```

*Locked modularly — same pattern to be applied to ECA/PER/AXIOM stacks in math/ — hashes not hard-coded values so you can tweak/debug.*
