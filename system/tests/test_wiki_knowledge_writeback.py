from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "system" / "scripts"))

from wiki_knowledge_writeback import snapshot_knowledge, validate_writeback  # noqa: E402


class KnowledgeWritebackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="wiki-writeback-", dir=ROOT / "tmp"))
        (self.root / "outputs" / "learning-daily").mkdir(parents=True)
        (self.root / "knowledge" / "projects").mkdir(parents=True)
        (self.root / "knowledge" / "sources").mkdir(parents=True)
        self.page = self.root / "knowledge" / "projects" / "example.md"
        self.source = self.root / "knowledge" / "sources" / "example-source.md"
        self.page.write_text(
            "# Example\n\nNew anchor sentence.\n\n[[example-source]]\n",
            encoding="utf-8",
        )
        self.source.write_text(
            "# Source\n\nSRC-1: PDF p. 4 reports the observation.\n",
            encoding="utf-8",
        )
        self.report = self.root / "outputs" / "learning-daily" / "2026-09-23.md"

    def write_report(self, status: str) -> None:
        block = {
            "status": status,
            "reason": "No new evidence after checking the current page." if status == "verified-no-op" else None,
            "items": [
                {
                    "knowledge": "knowledge/projects/example.md",
                    "summary": "Example durable mapping.",
                    "anchor": "New anchor sentence.",
                    "sources": [
                        {"path": "knowledge/sources/example-source.md", "locator": "SRC-1"}
                    ],
                }
            ],
        }
        self.report.write_text(
            "## Durable knowledge delta\n\n```knowledge-writeback\n"
            + json.dumps(block, ensure_ascii=False, indent=2)
            + "\n```\n",
            encoding="utf-8",
        )

    def test_updated_requires_real_page_change(self) -> None:
        self.write_report("updated")
        before = snapshot_knowledge(self.root)
        self.page.write_text(self.page.read_text(encoding="utf-8") + "\nA changed row.\n", encoding="utf-8")
        result = validate_writeback(self.report, self.root, before=before)
        self.assertTrue(result["valid"], result)
        self.assertEqual(result["changed_paths"], ["knowledge/projects/example.md"])

    def test_updated_without_page_change_fails(self) -> None:
        self.write_report("updated")
        result = validate_writeback(self.report, self.root, before=snapshot_knowledge(self.root))
        self.assertFalse(result["valid"])
        self.assertIn("no mapped knowledge page changed", result["error"])

    def test_verified_noop_requires_grounded_pages_and_locator(self) -> None:
        self.write_report("verified-no-op")
        result = validate_writeback(self.report, self.root, before=snapshot_knowledge(self.root))
        self.assertTrue(result["valid"], result)
        self.assertEqual(result["mode"], "verified-no-op")

    def test_unmapped_knowledge_change_is_rejected(self) -> None:
        self.write_report("verified-no-op")
        before = snapshot_knowledge(self.root)
        extra = self.root / "knowledge" / "projects" / "unmapped.md"
        extra.write_text("# accidental change\n", encoding="utf-8")
        result = validate_writeback(self.report, self.root, before=before)
        self.assertFalse(result["valid"])
        self.assertIn("must be listed", result["error"])

    def test_bad_locator_is_rejected(self) -> None:
        self.write_report("verified-no-op")
        text = self.report.read_text(encoding="utf-8").replace("SRC-1", "NO-SUCH-LOCATOR")
        self.report.write_text(text, encoding="utf-8")
        result = validate_writeback(self.report, self.root)
        self.assertFalse(result["valid"])
        self.assertIn("locator/claim ID not found", result["error"])


if __name__ == "__main__":
    unittest.main()
