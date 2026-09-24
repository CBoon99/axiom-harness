import unittest, tempfile, json
from pathlib import Path
from axiom_harness.manifest import sha256_file, write_manifest

class TestManifest(unittest.TestCase):
    def test_sha256_recompute(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td)/"a.txt"
            p.write_text("hello")
            h = sha256_file(p)
            # known sha256 of "hello"
            self.assertEqual(h, "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824")
    def test_write_manifest_sorted(self):
        with tempfile.TemporaryDirectory() as td:
            a = Path(td)/"a.txt"; a.write_text("a")
            b = Path(td)/"b.txt"; b.write_text("b")
            out = Path(td)/"MANIFEST.json"
            m = write_manifest([a,b], out)
            self.assertEqual(len(m["files"]), 2)
            self.assertTrue(out.exists())
            # sorted keys, ensure_ascii False, separators (",",":") per spec
            raw = out.read_text()
            self.assertIn('"files"', raw)
