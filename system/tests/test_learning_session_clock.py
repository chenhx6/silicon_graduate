from __future__ import annotations

import contextlib
import io
import json
import os
import signal
import subprocess
import tempfile
import unittest
from datetime import datetime, timedelta
from pathlib import Path
from unittest.mock import patch

from system.scripts import run_learning_session_clock as clock


REPO_ROOT = Path(__file__).resolve().parents[2]
THREAD = "01a111fb-370d-7ed1-afe9-881ccc47caf4"


class FakeClock:
    def __init__(self, now: datetime):
        self.now = now

    def __call__(self) -> datetime:
        return self.now

    def advance(self, seconds: float) -> None:
        self.now += timedelta(seconds=seconds)


class FakeQueue:
    def __init__(self, results: list[clock.QueueResult] | None = None):
        self.results = list(results or [])
        self.calls: list[tuple[list[str], int]] = []

    def __call__(self, command: list[str], timeout: int) -> clock.QueueResult:
        self.calls.append((command, timeout))
        return self.results.pop(0) if self.results else clock.QueueResult(0, "queued")


class LearningSessionClockTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="learning-clock-test-", dir=REPO_ROOT / "tmp")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "wiki"
        (self.root / ".git").mkdir(parents=True)
        (self.root / "knowledge").mkdir()
        (self.root / "README.md").write_text("fixture\n", encoding="utf-8")
        self.run_dir = self.root / "outputs/learning-daily/20261007-DAY8-test-run-01"
        self.run_dir.mkdir(parents=True)
        self.receipt = self.run_dir / "run.json"
        self.document = {"session_id": THREAD, "project_root": str(self.root), "day_index": 8,
                         "run_date": "2026-10-07", "started_at": "2026-10-07T00:20:00+08:00",
                         "overnight_until": "2026-10-08T15:00:00+08:00",
                         "closeout_window_ends_at": "2026-10-08T16:00:00+08:00", "status": "running"}
        self.write_receipt()
        self.spec = clock.load_spec(self.root, self.receipt, THREAD, 2)
        self.now = FakeClock(self.spec.study_started_at)
        self.queue = FakeQueue()
        self.lock_paths = (self.root / "daemon.lock", self.root / "runner.lock")

    def write_receipt(self) -> None:
        self.receipt.write_text(json.dumps(self.document), encoding="utf-8")

    def supervisor(self, queue: FakeQueue | None = None) -> clock.Supervisor:
        result = clock.Supervisor(self.spec, clock=self.now, queue=queue or self.queue, sleeper=self.now.advance)
        result.start()
        return result

    def event_status(self, supervisor: clock.Supervisor, event_id: str) -> str:
        return supervisor.state["events"][event_id]["status"]

    def write_farmer(self, status: str, *, thread: str = THREAD,
                     event_at: datetime | None = None, age_seconds: float = 0) -> Path:
        path = self.root / "tmp/farmer/state.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({thread: {"status": status,
                                            "last_event_timestamp": (event_at or self.now()).isoformat()}}), encoding="utf-8")
        stamp = self.now().timestamp() - age_seconds
        os.utime(path, (stamp, stamp))
        return path

    def test_fresh_farmer_cancellation_stops_without_receipt_update(self) -> None:
        supervisor = self.supervisor()
        self.now.advance(2 * 3600)
        self.write_farmer("cancelled")
        with clock.acquire_locks(self.lock_paths):
            self.assertFalse(supervisor.tick())
        self.assertEqual(supervisor.state["status"], "interrupted")
        self.assertEqual(json.loads(self.receipt.read_text())["status"], "running")
        self.assertEqual(self.queue.calls, [])
        with clock.acquire_locks(self.lock_paths):
            pass

    def test_fresh_manual_farmer_error_stops_without_queuing(self) -> None:
        supervisor = self.supervisor()
        self.now.advance(2 * 3600)
        snapshot = self.write_farmer("manual-attention-required", age_seconds=120)
        before = (snapshot.read_bytes(), snapshot.stat().st_mtime_ns)
        self.assertFalse(supervisor.tick())
        self.assertEqual(supervisor.state["status"], "manual-attention-required")
        self.assertEqual(self.queue.calls, [])
        self.assertEqual((snapshot.read_bytes(), snapshot.stat().st_mtime_ns), before)

    def test_cancellation_is_rechecked_at_the_actual_queue_boundary(self) -> None:
        supervisor = self.supervisor()
        self.now.advance(2 * 3600)
        reader = clock.farmer_snapshot
        reads = []

        def cancel_between_checks(*args: object) -> dict[str, object]:
            reads.append(True)
            if len(reads) == 2:
                self.write_farmer("cancelled")
            return reader(*args)

        with patch.object(clock, "farmer_snapshot", side_effect=cancel_between_checks):
            self.assertFalse(supervisor.tick())
        self.assertEqual(len(reads), 2)
        self.assertEqual(self.queue.calls, [])

    def test_unrelated_thread_marker_does_not_cancel_this_clock(self) -> None:
        supervisor = self.supervisor()
        self.now.advance(2 * 3600)
        self.write_farmer("cancelled", thread="01a111fb-370d-7ed1-afe9-881ccc47caf5")
        self.assertTrue(supervisor.tick())
        self.assertEqual(len(self.queue.calls), 1)
        self.assertEqual(supervisor.state["farmer_observation"]["reason"], "thread-missing")

    def test_stale_snapshot_and_pre_start_marker_do_not_block_new_learning(self) -> None:
        supervisor = self.supervisor()
        self.now.advance(2 * 3600)
        self.write_farmer("cancelled", age_seconds=121)
        self.assertTrue(supervisor.tick())
        self.assertEqual(supervisor.state["farmer_observation"]["reason"], "snapshot-stale")
        self.write_farmer("cancelled", event_at=self.spec.study_started_at - timedelta(seconds=1))
        supervisor.tick()
        self.assertEqual(supervisor.state["farmer_observation"]["reason"], "event-before-clock-start")
        self.assertEqual(len(self.queue.calls), 1)

    def test_farmer_recovery_pauses_queue_and_running_resumes_latest_checkpoint(self) -> None:
        supervisor = self.supervisor()
        self.now.advance(2 * 3600)
        self.write_farmer("recovery-pending")
        self.assertTrue(supervisor.tick())
        self.assertTrue(supervisor.state["queue_paused"])
        self.assertEqual(self.queue.calls, [])
        self.assertEqual(supervisor.sleep_seconds(), 60)
        first_heartbeat = supervisor.state["heartbeat_at"]
        self.now.advance(60)
        self.write_farmer("waiting-retry")
        supervisor.tick()
        self.assertNotEqual(supervisor.state["heartbeat_at"], first_heartbeat)
        self.assertEqual(self.queue.calls, [])
        self.now.now = self.spec.study_started_at + timedelta(hours=6)
        self.write_farmer("running")
        supervisor.tick()
        self.assertFalse(supervisor.state["queue_paused"])
        self.assertEqual(supervisor.state["sent_event_ids"], ["checkpoint-003"])
        self.assertEqual(len(self.queue.calls), 1)

    def test_complete_farmer_event_resumes_paused_clock_without_course_credit(self) -> None:
        supervisor = self.supervisor()
        self.now.advance(2 * 3600)
        self.write_farmer("waiting-retry")
        supervisor.tick()
        self.now.advance(60)
        self.write_farmer("complete")
        self.assertTrue(supervisor.tick())
        self.assertFalse(supervisor.state["queue_paused"])
        self.assertEqual(supervisor.state["sent_event_ids"], ["checkpoint-001"])
        self.assertEqual(json.loads(self.receipt.read_text())["status"], "running")

    def test_first_actual_clock_start_survives_restart_and_new_running_event(self) -> None:
        supervisor = self.supervisor()
        first_start = supervisor.state["first_supervisor_started_at"]
        self.now.advance(2 * 3600)
        supervisor.tick()
        self.write_farmer("cancelled")
        self.assertFalse(supervisor.tick())
        self.now.advance(60)
        restarted = self.supervisor()
        self.assertEqual(restarted.state["first_supervisor_started_at"], first_start)
        self.assertFalse(restarted.tick())
        self.now.advance(60)
        self.write_farmer("running")
        resumed = self.supervisor()
        self.assertTrue(resumed.tick())
        self.assertEqual(resumed.state["first_supervisor_started_at"], first_start)
        self.assertEqual(resumed.state["sent_event_ids"], ["checkpoint-001"])
        self.assertEqual(len(self.queue.calls), 1)

    def test_legacy_clock_start_is_migrated_from_existing_start_records(self) -> None:
        supervisor = self.supervisor()
        original = supervisor.state.pop("first_supervisor_started_at")
        self.now.advance(2 * 3600)
        supervisor.state["supervisor_started_at"] = self.now().isoformat()
        supervisor.save()
        restarted = self.supervisor()
        self.assertEqual(restarted.state["first_supervisor_started_at"], original)

    def test_missing_or_corrupt_farmer_snapshot_is_unknown_not_user_stop(self) -> None:
        supervisor = self.supervisor()
        self.assertTrue(supervisor.tick())
        self.assertEqual(supervisor.state["farmer_observation"]["reason"], "snapshot-missing")
        self.now.advance(2 * 3600)
        path = self.write_farmer("cancelled")
        path.write_text("{broken", encoding="utf-8")
        os.utime(path, (self.now().timestamp(), self.now().timestamp()))
        self.assertTrue(supervisor.tick())
        self.assertEqual(supervisor.state["farmer_observation"]["observation"], "unknown")
        self.assertEqual(supervisor.state["farmer_observation"]["reason"], "snapshot-unreadable")
        self.assertEqual(len(self.queue.calls), 1)
        self.assertIn("farmer-observed", supervisor.events_path.read_text())

    def test_invalid_farmer_event_timestamp_is_unknown_not_cancellation(self) -> None:
        supervisor = self.supervisor()
        self.now.advance(2 * 3600)
        path = self.write_farmer("cancelled")
        data = json.loads(path.read_text())
        data[THREAD]["last_event_timestamp"] = "2026-10-07T02:20:00"
        path.write_text(json.dumps(data), encoding="utf-8")
        os.utime(path, (self.now().timestamp(), self.now().timestamp()))
        self.assertTrue(supervisor.tick())
        self.assertEqual(supervisor.state["farmer_observation"]["observation"], "unknown")
        self.assertEqual(len(self.queue.calls), 1)

    def test_recovery_pause_at_window_end_releases_without_queuing_overdue(self) -> None:
        supervisor = self.supervisor()
        self.now.now = self.spec.closeout_end
        self.write_farmer("recovery-pending")
        with clock.acquire_locks(self.lock_paths):
            self.assertFalse(supervisor.tick())
        self.assertEqual(supervisor.state["status"], "window-ended")
        self.assertEqual(self.queue.calls, [])
        with clock.acquire_locks(self.lock_paths):
            pass

    def test_requires_matching_canonical_uuid(self) -> None:
        for thread in ("invalid", "01a111fb-370d-7ed1-afe9-881ccc47caf5", THREAD.upper()):
            with self.subTest(thread=thread), self.assertRaises(ValueError):
                clock.load_spec(self.root, self.receipt, thread, 2)

    def test_rejects_naive_or_wrong_date_deadlines_and_invalid_interval(self) -> None:
        for deadline in ("2026-10-08T15:00:00", "2026-10-07T15:00:00+08:00", "2026-10-08T14:00:00+08:00"):
            self.document["overnight_until"] = deadline
            self.write_receipt()
            with self.subTest(deadline=deadline), self.assertRaises(ValueError):
                clock.load_spec(self.root, self.receipt, THREAD, 2)
        self.document["overnight_until"] = self.spec.deadline.isoformat()
        self.write_receipt()
        for interval in (0, 1, 4, float("nan"), float("inf")):
            with self.subTest(interval=interval), self.assertRaises(ValueError):
                clock.load_spec(self.root, self.receipt, THREAD, interval)

    def test_rejects_wrong_closeout_end_or_run_date_or_day(self) -> None:
        for field, value in (("closeout_window_ends_at", "2026-10-08T17:00:00+08:00"),
                             ("run_date", "not-a-date"), ("day_index", True)):
            original = self.document[field]
            self.document[field] = value
            self.write_receipt()
            with self.subTest(field=field), self.assertRaises(ValueError):
                clock.load_spec(self.root, self.receipt, THREAD, 2)
            self.document[field] = original
        self.write_receipt()

    def test_accepts_an_explicit_utc_deadline_for_the_same_instant(self) -> None:
        self.document["overnight_until"] = "2026-10-08T07:00:00Z"
        self.write_receipt()
        self.assertEqual(clock.load_spec(self.root, self.receipt, THREAD, 3).deadline, self.spec.deadline)

    def test_rejects_external_flat_and_symlink_receipts(self) -> None:
        for path in (self.root / "run.json", self.root / "outputs/learning-daily/run.json"):
            path.write_text(json.dumps(self.document), encoding="utf-8")
            with self.subTest(path=path), self.assertRaises(ValueError):
                clock.load_spec(self.root, path, THREAD, 2)
        alias = self.root / "outputs/learning-daily/alias-run-02"
        alias.symlink_to(self.run_dir, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symlink"):
            clock.load_spec(self.root, alias / "run.json", THREAD, 2)
        self.receipt.rename(self.run_dir / "original.json")
        self.receipt.symlink_to(self.run_dir / "original.json")
        with self.assertRaisesRegex(ValueError, "symlink"):
            clock.load_spec(self.root, self.receipt, THREAD, 2)

    def test_dry_run_is_read_only_and_never_queues_or_locks(self) -> None:
        before = {path: path.read_bytes() for path in self.run_dir.iterdir()}
        with patch.object(clock, "queue_message") as queue, patch.object(clock, "acquire_locks") as locks:
            with contextlib.redirect_stdout(io.StringIO()) as output:
                result = clock.main(["--root", str(self.root), "--receipt", str(self.receipt),
                                     "--thread", THREAD, "--dry-run"])
            queue.assert_not_called()
            locks.assert_not_called()
        self.assertEqual(result, 0)
        self.assertEqual(before, {path: path.read_bytes() for path in self.run_dir.iterdir()})
        plan = json.loads(output.getvalue())
        self.assertEqual(plan["deadline"], "2026-10-08T15:00:00+08:00")
        self.assertEqual(plan["events"][-1]["at"], "2026-10-08T16:00:00+08:00")

    def test_all_messages_preserve_session_course_boundary_and_byte_limit(self) -> None:
        for event in clock.plan_events(self.spec):
            message = clock.message_for(self.spec, event, event.at)
            self.assertLess(len(message.encode("utf-8")), 1000)
            self.assertIn("Keep day_index=8", message)
            self.assertIn("Day 9 may only be an uncredited preview", message)
            self.assertIn("do not credit it or open Day 10", message)
            command = clock.queue_command(self.spec, message)
            self.assertEqual(command[:7], ["codex", "-C", str(self.root), "queue", "--thread", THREAD, "--message"])
            self.assertNotIn("resume", command)
            self.assertNotIn("--model", command)

    def test_checkpoint_is_once_and_restart_does_not_repeat_it(self) -> None:
        supervisor = self.supervisor()
        self.assertTrue(supervisor.tick())
        self.assertEqual(self.queue.calls, [])
        self.now.advance(2 * 3600)
        supervisor.tick()
        supervisor.tick()
        restarted = self.supervisor()
        restarted.tick()
        self.assertEqual(len(self.queue.calls), 1)
        self.assertEqual(restarted.state["sent_event_ids"], ["checkpoint-001"])
        self.now.advance(2 * 3600)
        restarted.tick()
        self.assertEqual(len(self.queue.calls), 2)

    def test_missed_checkpoints_make_one_latest_reminder_without_a_burst(self) -> None:
        self.now.advance(10 * 3600)
        supervisor = self.supervisor()
        supervisor.tick()
        self.assertEqual(len(self.queue.calls), 1)
        self.assertEqual(supervisor.state["sent_event_ids"], ["checkpoint-005"])
        self.assertEqual(self.event_status(supervisor, "checkpoint-001"), "skipped")

    def test_card_or_receipt_completion_does_not_end_the_study_window(self) -> None:
        self.document["status"] = "completed"
        self.write_receipt()
        supervisor = self.supervisor()
        self.assertTrue(supervisor.tick())
        self.assertEqual(supervisor.state["status"], "running")
        self.now.now = self.spec.deadline
        self.assertTrue(supervisor.tick())
        self.assertEqual(self.event_status(supervisor, "closeout"), "queued")
        self.now.now = self.spec.deadline + timedelta(minutes=45)
        supervisor.tick()
        self.assertEqual(self.event_status(supervisor, "closeout-reminder"), "skipped")
        self.now.now = self.spec.closeout_end
        self.assertFalse(supervisor.tick())
        self.assertEqual(self.event_status(supervisor, "overdue"), "skipped")

    def test_closeout_reminder_and_overdue_are_once_and_receipt_is_untouched(self) -> None:
        original = self.receipt.read_bytes()
        supervisor = self.supervisor()
        for at in (self.spec.deadline, self.spec.deadline + timedelta(minutes=45), self.spec.closeout_end):
            self.now.now = at
            supervisor.tick()
        self.assertEqual(supervisor.state["sent_event_ids"], ["closeout", "closeout-reminder", "overdue"])
        self.assertEqual(supervisor.state["status"], "window-ended")
        self.assertEqual(self.receipt.read_bytes(), original)
        restarted = self.supervisor()
        self.assertFalse(restarted.tick())
        self.assertEqual(len(self.queue.calls), 3)

    def test_expired_closeout_is_not_replayed_after_1600(self) -> None:
        self.now.now = self.spec.closeout_end + timedelta(hours=1)
        supervisor = self.supervisor()
        self.assertFalse(supervisor.tick())
        self.assertEqual(supervisor.state["sent_event_ids"], ["overdue"])
        self.assertEqual(self.event_status(supervisor, "closeout"), "skipped")

    def test_overdue_failure_is_one_attempt_and_is_not_retried_on_restart(self) -> None:
        self.now.now = self.spec.closeout_end
        queue = FakeQueue([clock.QueueResult(3, stderr="unavailable")])
        supervisor = self.supervisor(queue)
        self.assertFalse(supervisor.tick())
        restarted = self.supervisor(queue)
        self.assertFalse(restarted.tick())
        self.assertEqual(len(queue.calls), 1)
        self.assertEqual(self.event_status(restarted, "overdue"), "exhausted")
        self.assertEqual(restarted.state["events"]["overdue"]["attempts"], 1)

    def test_rejected_queue_retries_are_bounded_and_outputs_are_saved(self) -> None:
        queue = FakeQueue([clock.QueueResult(7, "out", "rejected")] * 3)
        supervisor = self.supervisor(queue)
        self.now.advance(2 * 3600)
        supervisor.tick()
        supervisor.tick()
        self.assertEqual(len(queue.calls), 1)
        self.now.advance(15)
        supervisor.tick()
        self.now.advance(30)
        supervisor.tick()
        self.now.advance(60)
        supervisor.tick()
        self.assertEqual(len(queue.calls), 3)
        record = supervisor.state["events"]["checkpoint-001"]
        self.assertEqual(record["status"], "exhausted")
        self.assertEqual(record["attempt_history"][-1]["returncode"], 7)
        self.assertEqual(record["attempt_history"][-1]["stderr"], "rejected")
        self.assertEqual(supervisor.state["sent_event_ids"], [])

    def test_timeout_or_restart_in_flight_is_unknown_and_not_resent(self) -> None:
        queue = FakeQueue([clock.QueueResult(None, "partial", "timed out", timed_out=True)])
        supervisor = self.supervisor(queue)
        self.now.advance(2 * 3600)
        supervisor.tick()
        self.now.advance(60)
        supervisor.tick()
        self.assertEqual(len(queue.calls), 1)
        self.assertEqual(self.event_status(supervisor, "checkpoint-001"), "unknown")
        record = supervisor.state["events"]["checkpoint-001"]
        record.update(status="in-flight")
        supervisor.save()
        restarted = self.supervisor(queue)
        restarted.tick()
        self.assertEqual(len(queue.calls), 1)
        self.assertEqual(self.event_status(restarted, "checkpoint-001"), "unknown")

    def test_queue_uses_argv_capture_and_a_30_second_timeout(self) -> None:
        command = clock.queue_command(self.spec, "message")
        with patch.object(clock.subprocess, "run", return_value=subprocess.CompletedProcess(command, 0, "ok", "")) as run:
            result = clock.queue_message(command, clock.QUEUE_TIMEOUT_SECONDS)
            run.assert_called_once_with(command, text=True, capture_output=True, check=False, timeout=30)
        self.assertEqual(result.returncode, 0)
        with patch.object(clock.subprocess, "run", side_effect=subprocess.TimeoutExpired(command, 30, output=b"partial")):
            result = clock.queue_message(command, 30)
        self.assertTrue(result.timed_out)
        self.assertEqual(result.stdout, "partial")

    def test_both_locks_exclude_other_owners_and_partial_acquisition_releases(self) -> None:
        with clock.acquire_locks(self.lock_paths):
            with self.assertRaises(clock.LockBusy):
                with clock.acquire_locks(self.lock_paths):
                    self.fail("a second owner acquired held locks")
        with clock.acquire_locks((self.lock_paths[1],)):
            with self.assertRaises(clock.LockBusy):
                with clock.acquire_locks(self.lock_paths):
                    self.fail("held runner lock was acquired")
            with clock.acquire_locks((self.lock_paths[0],)):
                pass
        with clock.acquire_locks(self.lock_paths):
            pass

    def test_interrupt_preserves_receipt_releases_locks_and_sleeps_at_most_60s(self) -> None:
        original = self.receipt.read_bytes()
        stop: dict[str, int | None] = {"signal": None}
        delays = []

        def sleep_and_stop(seconds: float) -> None:
            delays.append(seconds)
            self.now.advance(seconds)
            stop["signal"] = signal.SIGTERM

        with clock.acquire_locks(self.lock_paths):
            supervisor = clock.Supervisor(self.spec, clock=self.now, queue=self.queue, sleeper=sleep_and_stop)
            result = supervisor.run(stop)
        self.assertEqual(result, 143)
        self.assertEqual(supervisor.state["status"], "interrupted")
        self.assertTrue(all(delay <= 60 for delay in delays))
        self.assertEqual(self.receipt.read_bytes(), original)
        with clock.acquire_locks(self.lock_paths):
            pass

    def test_user_stop_receipt_never_queues_an_automatic_continuation(self) -> None:
        self.document["status"] = "cancelled"
        self.write_receipt()
        supervisor = self.supervisor()
        self.now.advance(2 * 3600)
        self.assertFalse(supervisor.tick())
        self.assertEqual(supervisor.state["status"], "interrupted")
        self.assertEqual(self.queue.calls, [])

    def test_runtime_receipt_change_records_failure_before_releasing_locks(self) -> None:
        real_supervisor = clock.Supervisor
        held_during_failure = []

        class CheckedSupervisor(real_supervisor):
            def finish(inner, status: str, reason: str) -> None:
                if status == "failed":
                    try:
                        with clock.acquire_locks(self.lock_paths):
                            held_during_failure.append(False)
                    except clock.LockBusy:
                        held_during_failure.append(True)
                super().finish(status, reason)

        def change_receipt(seconds: float) -> None:
            self.now.advance(seconds)
            self.document["session_id"] = "01a111fb-370d-7ed1-afe9-881ccc47caf5"
            self.write_receipt()

        def make_supervisor(spec: clock.SessionSpec) -> clock.Supervisor:
            return CheckedSupervisor(spec, clock=self.now, queue=self.queue, sleeper=change_receipt)

        with patch.object(clock, "LOCK_PATHS", self.lock_paths), patch.object(clock, "Supervisor", side_effect=make_supervisor):
            with contextlib.redirect_stderr(io.StringIO()):
                result = clock.main(["--root", str(self.root), "--receipt", str(self.receipt), "--thread", THREAD])
        self.assertEqual(result, 2)
        self.assertEqual(held_during_failure, [True])
        self.assertEqual(json.loads((self.run_dir / "clock-state.json").read_text())["status"], "failed")
        self.assertEqual(self.queue.calls, [])
        with clock.acquire_locks(self.lock_paths):
            pass

    def test_heartbeat_distinguishes_waiting_and_does_not_claim_session_execution(self) -> None:
        self.now.now = self.spec.study_started_at - timedelta(minutes=10)
        supervisor = self.supervisor()
        supervisor.tick()
        self.assertEqual(supervisor.state["phase"], "waiting-for-recorded-study-start")
        self.assertFalse(supervisor.state["session_execution_observed"])
        self.now.now = self.spec.study_started_at
        supervisor.tick()
        self.assertEqual(supervisor.state["phase"], "study-window")

    def test_work_time_is_subtracted_from_the_next_heartbeat_wait(self) -> None:
        supervisor = self.supervisor()
        supervisor.tick()
        self.now.advance(10)
        self.assertEqual(supervisor.sleep_seconds(), 50)

    def test_state_symlinks_and_identity_corruption_fail_closed(self) -> None:
        supervisor = self.supervisor()
        supervisor.state["thread"] = "different"
        supervisor.save()
        with self.assertRaisesRegex(ValueError, "identity"):
            clock.Supervisor(self.spec)
        supervisor.state_path.unlink()
        supervisor.state_path.symlink_to(self.receipt)
        with self.assertRaisesRegex(ValueError, "symlink"):
            clock.Supervisor(self.spec)


if __name__ == "__main__":
    unittest.main()
