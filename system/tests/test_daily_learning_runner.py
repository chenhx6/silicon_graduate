from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "system" / "scripts"))
import run_daily_learning  # noqa: E402


class DailyLearningRunnerTests(unittest.TestCase):
    def test_phase_table_covers_all_days(self) -> None:
        self.assertEqual(run_daily_learning.phase_for_day(1), "baseline-and-research-contract")
        self.assertEqual(run_daily_learning.phase_for_day(30), "final-exam-and-prospectus")
        with self.assertRaises(ValueError):
            run_daily_learning.phase_for_day(31)

    def test_build_command_uses_workspace_write_and_persistent_exec(self) -> None:
        command = run_daily_learning.build_command(
            Path("/workspace/wiki"), "gpt-5.6-sol", Path("/tmp/last.md"), True
        )
        self.assertEqual(command[:8], ["codex", "-C", "/workspace/wiki", "-m", "gpt-5.6-sol", "-s", "workspace-write", "-a"])
        self.assertIn("never", command)
        self.assertIn("--search", command)
        self.assertIn("exec", command)
        self.assertNotIn("--ephemeral", command)

    def test_session_id_extraction_accepts_common_jsonl_shapes(self) -> None:
        lines = [
            json.dumps({"type": "started", "thread_id": "thread-a"}),
            json.dumps({"thread": {"id": "thread-b"}}),
        ]
        self.assertEqual(run_daily_learning.extract_session_id(lines), "thread-a")

    def test_state_defaults_and_atomic_roundtrip(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            state = run_daily_learning.read_state(path)
            self.assertEqual(state["next_day_index"], 1)
            state["next_day_index"] = 2
            run_daily_learning.write_json_atomic(path, state)
            self.assertEqual(run_daily_learning.read_state(path)["next_day_index"], 2)

    def test_dry_run_checks_root_prompt_and_returns_command(self) -> None:
        paths = run_daily_learning.get_paths(REPO_ROOT)
        with patch.object(run_daily_learning.shutil, "which", return_value="/usr/bin/codex"):
            result = run_daily_learning.dry_run(paths, "gpt-5.6-sol", True)
        self.assertEqual(result["status"], "dry-run-ok")
        self.assertEqual(result["day_index"], 1)
        self.assertIn("workspace-write", result["command"])
        self.assertFalse(result["cycle_complete"])

    def test_report_validation_requires_all_daily_headings(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "daily.md"
            path.write_text("## Run state\n", encoding="utf-8")
            result = run_daily_learning.validate_report(path)
            self.assertFalse(result["valid"])
            self.assertIn("## Sources and evidence", result["missing_headings"])

    def test_report_signature_changes_when_report_changes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "daily.md"
            self.assertIsNone(run_daily_learning.report_signature(path))
            path.write_text("first\n", encoding="utf-8")
            first = run_daily_learning.report_signature(path)
            path.write_text("second\n", encoding="utf-8")
            self.assertNotEqual(first, run_daily_learning.report_signature(path))

    def test_completed_state_dry_run_does_not_request_day_31_phase(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths = run_daily_learning.get_paths(root)
            (root / "README.md").write_text("root\n", encoding="utf-8")
            (root / "knowledge").mkdir()
            (root / ".git").mkdir()
            paths.prompt_file.parent.mkdir(parents=True)
            paths.prompt_file.write_text("prompt\n", encoding="utf-8")
            run_daily_learning.write_json_atomic(
                paths.state_file,
                {"next_day_index": 31, "status": "complete"},
            )
            with patch.object(run_daily_learning.shutil, "which", return_value="/usr/bin/codex"):
                result = run_daily_learning.dry_run(paths, "gpt-5.6-sol", True)
            self.assertEqual(result["status"], "cycle-complete")
            self.assertIsNone(result["phase"])

    def test_preflight_result_preserves_exit_and_tail(self) -> None:
        completed = type("Completed", (), {"returncode": 0, "stdout": '{"ok":true}', "stderr": ""})()
        with patch.object(run_daily_learning.subprocess, "run", return_value=completed):
            result = run_daily_learning.run_preflight(REPO_ROOT)
        self.assertEqual(result["exit"], 0)
        self.assertIn("ok", result["stdout_tail"])
