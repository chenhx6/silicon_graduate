import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from local_literature_archive import digest
from local_literature_recovery import copy_original, run


class RecoveryTests(unittest.TestCase):
    def test_preview_then_copy_preserves_original_identity_and_scope(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            original = root / "tmp/original.txt"
            original.parent.mkdir()
            original.write_bytes(b"Original data")
            page = root / "knowledge/sources/test.md"
            page.parent.mkdir(parents=True)
            sha = digest(original)
            page.write_text(f"---\ntype: source\nraw_file: raw/notes/missing.txt\n"
                            f"raw_sha256: {sha}\nreading_depth: skimmed\n---\n"
                            "# Source\n\nPDF page 5; historical scope.\n")
            receipt = root / "receipt.json"
            receipt.write_text(json.dumps({"items": [{
                "source": "knowledge/sources/test.md", "expected_sha256": sha,
                "recorded_raw_file": "raw/notes/missing.txt",
                "verified_matching_files": ["tmp/original.txt"]}]}))
            self.assertEqual(run(root, receipt)["ready"], 1)
            self.assertFalse((root / "raw/notes/missing.txt").exists())
            self.assertEqual(run(root, receipt, True)["reconciled"], 1)
            self.assertEqual((root / "raw/notes/missing.txt").read_bytes(), original.read_bytes())
            self.assertIn("PDF page 5; historical scope.", page.read_text())
            self.assertIn("reading_depth: skimmed", page.read_text())
            self.assertEqual(run(root, receipt, True)["reconciled"], 1)

    def test_existing_different_bytes_and_stale_candidates_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source"
            destination = root / "destination"
            source.write_bytes(b"right")
            destination.write_bytes(b"other")
            with self.assertRaisesRegex(ValueError, "destination conflict"):
                copy_original(source, destination, digest(source))
            self.assertEqual(destination.read_bytes(), b"other")
            with self.assertRaisesRegex(ValueError, "candidate hash mismatch"):
                copy_original(source, root / "new", "0" * 64)
            self.assertFalse((root / "new").exists())


if __name__ == "__main__":
    unittest.main()
