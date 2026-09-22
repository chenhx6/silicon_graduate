from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime, timedelta
from pathlib import Path
from unittest.mock import patch
from zoneinfo import ZoneInfo

import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "system" / "scripts"))
import run_daily_learning_daemon  # noqa: E402


TZ = ZoneInfo("Asia/Shanghai")


class DailyLearningDaemonTests(unittest.TestCase):
    def test_next_trigger_before_target_is_same_day(self) -> None:
        now = datetime(2026, 9, 22, 21, 59, 30, tzinfo=TZ)
        self.assertEqual(
            run_daily_learning_daemon.next_trigger(now),
            datetime(2026, 9, 22, 22, 0, tzinfo=TZ),
        )

    def test_next_trigger_at_or_after_target_rolls_to_next_day(self) -> None:
        now = datetime(2026, 9, 22, 22, 0, tzinfo=TZ)
        self.assertEqual(
            run_daily_learning_daemon.next_trigger(now),
            datetime(2026, 9, 23, 22, 0, tzinfo=TZ),
        )
        later = datetime(2026, 9, 22, 23, 30, tzinfo=TZ)
        self.assertEqual(
            run_daily_learning_daemon.next_trigger(later),
            datetime(2026, 9, 23, 22, 0, tzinfo=TZ),
        )

    def test_due_time_catches_up_after_missed_trigger(self) -> None:
        now = datetime(2026, 9, 22, 23, 0, tzinfo=TZ)
        marker = {"last_scheduled_date": None, "last_status": None}
        self.assertEqual(
            run_daily_learning_daemon.next_due(now, marker),
            now.replace(hour=23, minute=0, second=0, microsecond=0),
        )

    def test_due_time_waits_after_today_was_scheduled(self) -> None:
        now = datetime(2026, 9, 22, 23, 0, tzinfo=TZ)
        marker = {"last_scheduled_date": "2026-09-22", "last_status": "failed"}
        self.assertEqual(
            run_daily_learning_daemon.next_due(now, marker),
            datetime(2026, 9, 23, 22, 0, tzinfo=TZ),
        )

    def test_running_marker_is_retryable_after_restart(self) -> None:
        now = datetime(2026, 9, 22, 23, 0, tzinfo=TZ)
        marker = {"last_scheduled_date": "2026-09-22", "last_status": "running"}
        self.assertEqual(run_daily_learning_daemon.next_due(now, marker), now)

    def test_learning_cycle_complete_after_day_30(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            state_path = root / "outputs" / "learning-milestones" / "2026-09-one-month-state.json"
            state_path.parent.mkdir(parents=True)
            state_path.write_text(
                json.dumps({"next_day_index": 31, "status": "complete"}),
                encoding="utf-8",
            )
            self.assertTrue(run_daily_learning_daemon.learning_cycle_complete(root))

    def test_build_runner_command_is_docker_local(self) -> None:
        command = run_daily_learning_daemon.build_runner_command(
            Path("/workspace/wiki"), "gpt-5.6-sol", False, "max"
        )
        self.assertEqual(command[:4], [sys.executable, "/workspace/wiki/system/scripts/run_daily_learning.py", "--root", "/workspace/wiki"])
        self.assertIn("--day-index", command)
        self.assertIn("auto", command)
        self.assertIn("--reasoning-effort", command)
        self.assertIn("max", command)
        self.assertNotIn("docker", " ".join(command).lower())
        self.assertNotIn("powershell", " ".join(command).lower())

    def test_model_priority_is_astra_sol_terra(self) -> None:
        self.assertEqual(
            run_daily_learning_daemon.MODEL_PRIORITY,
            (
                ("gpt-6-astra", "low"),
                ("gpt-5.6-sol", "max"),
                ("gpt-5.6-terra", "max"),
            ),
        )

    def test_capacity_error_is_retryable_but_science_failure_is_not(self) -> None:
        self.assertTrue(run_daily_learning_daemon.is_retryable_model_error("model at capacity"))
        self.assertTrue(run_daily_learning_daemon.is_retryable_model_error("service unavailable"))
        self.assertFalse(run_daily_learning_daemon.is_retryable_model_error("failed-verification"))
        self.assertFalse(run_daily_learning_daemon.is_retryable_model_error("permission denied"))

    def test_profile_chain_falls_back_in_order(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            log_path = root / "scheduler.jsonl"
            responses = [
                type(
                    "Completed",
                    (),
                    {
                        "returncode": 1,
                        "stdout": json.dumps({"status": "failed-verification", "failure_reason": "model at capacity"}) + "\n",
                        "stderr": "",
                    },
                )(),
                type(
                    "Completed",
                    (),
                    {"returncode": 0, "stdout": json.dumps({"status": "completed"}) + "\n", "stderr": ""},
                )(),
            ]
            with patch.object(
                run_daily_learning_daemon.subprocess,
                "run",
                side_effect=responses,
            ) as run:
                result = run_daily_learning_daemon.run_profile_chain(
                    root,
                    (("gpt-6-astra", "low"), ("gpt-5.6-sol", "max")),
                    False,
                    log_path,
                )
            self.assertEqual(result["exit_code"], 0)
            self.assertEqual(run.call_count, 2)
            self.assertIn("gpt-6-astra", " ".join(run.call_args_list[0].args[0]))
            self.assertIn("gpt-5.6-sol", " ".join(run.call_args_list[1].args[0]))
            events = [json.loads(line) for line in log_path.read_text().splitlines()]
            self.assertIn("model-fallback", [event["event"] for event in events])

    def test_run_once_records_result_without_shell(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            log_path = root / "scheduler.jsonl"
            completed = type("Completed", (), {"returncode": 0, "stdout": "{}\n", "stderr": ""})()
            with patch.object(run_daily_learning_daemon.subprocess, "run", return_value=completed) as run:
                result = run_daily_learning_daemon.run_once(
                    root, "gpt-5.6-sol", False, log_path
                )
            self.assertEqual(result, 0)
            run.assert_called_once()
            self.assertFalse(run.call_args.kwargs["shell"])
            events = [json.loads(line) for line in log_path.read_text().splitlines()]
            self.assertEqual(events[-1]["event"], "runner-finished")
            self.assertEqual(events[-1]["exit_code"], 0)

    def test_next_trigger_preserves_timezone(self) -> None:
        now = datetime(2026, 9, 22, 10, 0, tzinfo=TZ)
        target = run_daily_learning_daemon.next_trigger(now, hour=7, minute=15)
        self.assertEqual(target.utcoffset(), timedelta(hours=8))


if __name__ == "__main__":
    unittest.main()
