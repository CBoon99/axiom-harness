"""Manifest — SHA-256 writer (single canonical WTF-005A-HASH-v3).

Ensures MANIFEST.json recomputes correctly; P2 will use stripped canonical [{role,content}].
"""
import json, hashlib
from pathlib import Path

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def write_manifest(files: list, out: Path):
    manifest = {"files": [{"path": str(f), "sha256": sha256_file(Path(f))} for f in files]}
    out.write_text(json.dumps(manifest, sort_keys=True, ensure_ascii=False, separators=(",", ":")))
    return manifest

def write_run_pointer(experiment_id: str, prev_receipt_hash, out: Path):
    ptr = {"experiment_id": experiment_id, "prev_receipt_hash": prev_receipt_hash}
    out.write_text(json.dumps(ptr, sort_keys=True, ensure_ascii=False, separators=(",", ":")))
    return ptr
