"""Manifest canonical WTF-005A-HASH-v3 — sort_keys True ensure_ascii False separators no indent."""
import unittest, tempfile, json, hashlib
from pathlib import Path
from axiom_harness.manifest import sha256_file, write_manifest, write_run_pointer

class TestManifestCanonical(unittest.TestCase):
    def test_sha256_known(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td)/"a.txt"
            p.write_text("hello")
            self.assertEqual(sha256_file(p), "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824")

    def test_write_manifest_wtf005a_hash_v3(self):
        with tempfile.TemporaryDirectory() as td:
            a = Path(td)/"a.txt"; a.write_text("a")
            b = Path(td)/"b.txt"; b.write_text("b")
            out = Path(td)/"MANIFEST.json"
            m = write_manifest([a,b], out)
            raw = out.read_text()
            self.assertNotIn("\n  ", raw)
            self.assertEqual(raw, json.dumps(json.loads(raw), sort_keys=True, ensure_ascii=False, separators=(",",":")))
            self.assertIn('"files"', raw)
            self.assertIn('","', raw)
            for entry in m["files"]:
                self.assertIn("sha256", entry)
                p = Path(entry["path"])
                self.assertEqual(entry["sha256"], sha256_file(p))

    def test_ensure_ascii_false(self):
        # manifest uses ensure_ascii False per WTF-005A-HASH-v3
        raw = json.dumps({"k":"café — naïve ☺"}, sort_keys=True, ensure_ascii=False, separators=(",",":"))
        self.assertIn("café", raw)
        self.assertNotIn("\\u", raw)
        # also verify write_manifest roundtrip uses same kwargs
        with tempfile.TemporaryDirectory() as td:
            p = Path(td)/"a.txt"; p.write_text("hello")
            out = Path(td)/"MANIFEST.json"
            write_manifest([p], out)
            raw2 = out.read_text()
            self.assertEqual(raw2, json.dumps(json.loads(raw2), sort_keys=True, ensure_ascii=False, separators=(",",":")))
            h = hashlib.sha256(p.read_bytes()).hexdigest()
            j = json.loads(raw2)
            self.assertEqual(j["files"][0]["sha256"], h)

    def test_run_pointer_canonical(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td)/"ptr.json"
            write_run_pointer("WTF-005A-RUN-01", "abc123", out)
            raw = out.read_text()
            self.assertNotIn("\n  ", raw)
            self.assertEqual(raw, json.dumps(json.loads(raw), sort_keys=True, ensure_ascii=False, separators=(",",":")))
            j = json.loads(raw)
            self.assertEqual(j["experiment_id"], "WTF-005A-RUN-01")
            self.assertEqual(j["prev_receipt_hash"], "abc123")

    def test_manifest_recompute_detects_tamper(self):
        with tempfile.TemporaryDirectory() as td:
            a = Path(td)/"a.txt"; a.write_text("hello")
            out = Path(td)/"MANIFEST.json"
            write_manifest([a], out)
            h_before = json.loads(out.read_text())["files"][0]["sha256"]
            a.write_text("tampered")
            self.assertNotEqual(sha256_file(a), h_before)

    def test_manifest_truncated_fails_roundtrip(self):
        with tempfile.TemporaryDirectory() as td:
            a = Path(td)/"a.txt"; a.write_text("hello")
            out = Path(td)/"MANIFEST.json"
            write_manifest([a], out)
            raw = out.read_text()
            out.write_text(raw[:10])
            with self.assertRaises(Exception):
                json.loads(out.read_text())
            # original raw must have been valid
            self.assertEqual(raw, json.dumps(json.loads(raw), sort_keys=True, ensure_ascii=False, separators=(",",":")))
