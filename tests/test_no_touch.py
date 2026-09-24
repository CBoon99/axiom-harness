import unittest
from pathlib import Path

STAGING = Path(__file__).resolve().parents[1]
MASTER = Path("/Users/carlboon/Documents/Axiom Harness-Master - Dont Touch")

class TestNoTouch(unittest.TestCase):
    def test_staging_not_master(self):
        self.assertNotEqual(STAGING.resolve(), MASTER.resolve())
        self.assertTrue((STAGING / "app").exists())
        self.assertTrue((MASTER / "AXIOM HARNESS Brief (1).md").exists())

    def test_no_upstream_write(self):
        # Staging must not have copied axiom_wb code — engine stays read-only upstream
        self.assertFalse((STAGING / "axiom_wb").exists())
        self.assertTrue((STAGING / "axiom_harness").exists())
