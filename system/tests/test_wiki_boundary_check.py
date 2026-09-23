from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "system" / "scripts"))

import wiki_boundary_check  # noqa: E402


class WikiBoundaryCheckTests(unittest.TestCase):
    def make_root(self) -> Path:
        root = Path(tempfile.mkdtemp(prefix="wiki-boundary-", dir=ROOT / "tmp"))
        for name in wiki_boundary_check.REQUIRED_DIRS:
            (root / name).mkdir(parents=True)
        (root / ".qmd").mkdir()
        (root / ".qmd" / "index.yml").write_text("collections:\n", encoding="utf-8")
        (root / "knowledge" / "projects").mkdir()
        (root / "knowledge" / "projects" / "a130-thesis-evidence-matrix.md").write_text(
            "---\ntype: project\n---\n# matrix\n", encoding="utf-8"
        )
        return root

    def test_clean_contract_and_qmd_scope(self) -> None:
        root = self.make_root()

        def fake_qmd(command, cwd):
            self.assertEqual(cwd, root)
            return 0, "Collection: nuclear-knowledge\n  Path:     %s\n  Pattern:  **/*.md\n" % (root / "knowledge"), ""

        result = wiki_boundary_check.scan_boundary(root, qmd_runner=fake_qmd)
        self.assertTrue(result["ok"], json.dumps(result, ensure_ascii=False))
        self.assertEqual(result["checks"]["qmd"]["pattern"], "**/*.md")

    def test_rejects_legacy_plans_and_durable_page_in_outputs(self) -> None:
        root = self.make_root()
        (root / "docs" / "plans").mkdir(parents=True)
        output = root / "outputs" / "legacy.md"
        output.write_text("---\ntype: project\n---\n# wrong layer\n", encoding="utf-8")
        result = wiki_boundary_check.scan_boundary(root, check_qmd_enabled=False)
        codes = {issue["code"] for issue in result["errors"]}
        self.assertIn("LEGACY_PATH_PRESENT", codes)
        self.assertIn("KNOWLEDGE_PAGE_IN_OUTPUTS", codes)

    def test_allows_report_types_and_rejects_unlisted_output_root(self) -> None:
        root = self.make_root()
        (root / "outputs" / "custom-report").mkdir()
        (root / "outputs" / "custom-report" / "report.md").write_text(
            "---\ntype: output\n---\n# report\n", encoding="utf-8"
        )
        result = wiki_boundary_check.scan_boundary(root, check_qmd_enabled=False)
        self.assertFalse(result["ok"])
        self.assertIn("OUTPUT_ROOT_UNCLASSIFIED", {issue["code"] for issue in result["errors"]})


if __name__ == "__main__":
    unittest.main()
