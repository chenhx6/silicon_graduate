import json
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest

from system.scripts import agent_checks


class CaptureTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)

    def test_raw_failure_and_exit_code_survive_capture_and_search(self):
        run = agent_checks.capture([
            sys.executable, "-c",
            "import sys; print('header', flush=True); print('error: missing figure', file=sys.stderr); "
            "print('final line'); sys.exit(3)",
        ], "failure", self.root)
        self.assertEqual(run["exit_code"], 3)
        self.assertEqual(Path(run["log"]).read_text(), "header\nerror: missing figure\nfinal line\n")
        self.assertIn({"line": 2, "text": "error: missing figure"}, run["preview"])
        with sqlite3.connect(":memory:") as connection:
            if connection.execute("SELECT sqlite_compileoption_used('ENABLE_FTS5')").fetchone()[0]:
                self.assertEqual(agent_checks.find(Path(run["receipt"]), "missing figure", 3)["hits"], [
                    {"line": 2, "text": "error: missing figure"},
                ])

    def test_saved_json_assertions_can_accept_or_reject_the_same_run(self):
        run = agent_checks.capture(
            [sys.executable, "-c", 'print(\'{"round": 2, "verified": true, "hits": []}\')'], "fixture", self.root,
        )
        receipt = Path(run["receipt"])
        expectations = self.root / "expected.json"
        expectations.write_text(json.dumps({"exit_code": 0, "stdout_json": {"round": 2}, "excludes": ["Traceback"]}))
        before = agent_checks.evaluate(receipt, expectations)
        self.assertTrue(before["passed"])
        expectations.write_text(json.dumps({"stdout_json": {"round": 3, "verified": 1}}))
        after = agent_checks.evaluate(receipt, expectations)
        self.assertFalse(after["passed"])
        self.assertTrue(all(not check["passed"] for check in after["checks"]))
        self.assertEqual(before["receipt_sha256"], after["receipt_sha256"])
        self.assertNotEqual(before["expectations_sha256"], after["expectations_sha256"])

    def test_editing_a_captured_log_invalidates_its_receipt(self):
        run = agent_checks.capture([sys.executable, "-c", "print('original')"], "modified", self.root)
        Path(run["log"]).write_text("replacement\n")
        with self.assertRaisesRegex(ValueError, "differs from its receipt"):
            agent_checks.read_run(Path(run["receipt"]))


class StructureTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)

    def test_call_sites_exclude_comments_and_strings(self):
        source = self.root / "sample.py"
        source.write_text("# file.write_text('comment')\ntext = 'file.write_text()'\nfile.write_text(text)\n")
        matches = agent_checks.calls([source], "write_text", 10)
        self.assertEqual(matches["total"], 1)
        self.assertEqual(matches["hits"][0]["line"], 3)
        self.assertEqual(matches["hits"][0]["callee"], "file.write_text")

    def test_ast_comparison_separates_formatting_and_changed_definitions(self):
        before = self.root / "before.py"
        after = self.root / "after.py"
        before.write_text("def operate(value):\n    return value + 1\n")
        after.write_text("def operate(value):\n    return (value+1)  # same syntax tree\n")
        self.assertTrue(agent_checks.compare(before, after)["ast_equal"])
        after.write_text("def operate(value):\n    return value + 2\n")
        result = agent_checks.compare(before, after)
        self.assertFalse(result["ast_equal"])
        self.assertEqual(result["changed_definitions"], ["operate"])
