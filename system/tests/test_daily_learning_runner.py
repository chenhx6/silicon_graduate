from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime, timedelta
from pathlib import Path
from unittest.mock import patch


import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "system" / "scripts"))
import run_daily_learning  # noqa: E402


def coverage_report(
    completed: list[int],
    partial: list[int],
    *,
    day7_scorecard: bool = False,
    day7_reflect: bool = False,
) -> str:
    run_state = [
        "## Run state",
        f"- completed_day_indices: [{', '.join(str(day) for day in completed)}]",
        f"- partial_day_indices: [{', '.join(str(day) for day in partial)}]",
    ]
    body: list[str] = []
    for day in completed:
        run_state.append(f"- Day {day} card audit: complete")
        body.extend(
            [
                f"### Day {day} card completion audit",
                "| Day-card deliverable | Evidence / artifact | Status |",
                "| --- | --- | --- |",
                "| Recall | report section | complete |",
                "| Anchor source | SRC-1 | complete |",
                "| Quantitative exercise | Table 1 | complete |",
                "| Counter-evidence | SRC-2 | complete |",
            ]
        )
    if 7 in completed:
        if day7_scorecard:
            run_state.append("- Day 7 scorecard: complete")
            body.extend(
                [
                    "## Day 7 scorecard",
                    "| 理论 | 3 |",
                    "| 判图 | 3 |",
                    "| 误差 | 2 |",
                    "| 证据分层 | 4 |",
                    "| 反证 | 3 |",
                    "| 可证伪问题 | 3 |",
                ]
            )
        if day7_reflect:
            run_state.append("- Day 7 weekly REFLECT: complete")
            body.extend(["## Day 7 weekly REFLECT", "Completed weekly reflection."])
    return "\n".join([*run_state, *body]) + "\n"


class DailyLearningRunnerTests(unittest.TestCase):
    def test_closeout_snapshot_at_0400_preserves_eleven_hour_window(self) -> None:
        now = datetime(2026, 10, 6, 4, 0, tzinfo=run_daily_learning.TIMEZONE)
        deadline = datetime(2026, 10, 6, 15, 0, tzinfo=run_daily_learning.TIMEZONE)
        next_start = datetime(2026, 10, 6, 16, 0, tzinfo=run_daily_learning.TIMEZONE)
        snapshot = run_daily_learning.closeout_snapshot(now, deadline, next_start)
        self.assertEqual(snapshot["minutes_to_deadline"], 660)
        self.assertEqual(snapshot["minutes_to_next_start"], 720)
        self.assertEqual(snapshot["decision"], "continue-or-advance")
        self.assertTrue(snapshot["can_complete_forward_card"])

    def test_closeout_snapshot_uses_deadline_not_run_date(self) -> None:
        now = datetime(2026, 10, 5, 4, 0, tzinfo=run_daily_learning.TIMEZONE)
        deadline = datetime(2026, 10, 6, 15, 0, tzinfo=run_daily_learning.TIMEZONE)
        next_start = datetime(2026, 10, 6, 16, 0, tzinfo=run_daily_learning.TIMEZONE)
        snapshot = run_daily_learning.closeout_snapshot(now, deadline, next_start)
        self.assertEqual(snapshot["minutes_to_deadline"], 2100)
        self.assertEqual(snapshot["minutes_to_next_start"], 2160)
        self.assertEqual(snapshot["decision"], "continue-or-advance")

    def test_closeout_snapshot_keeps_partial_window_for_current_question(self) -> None:
        deadline = datetime(2026, 10, 6, 15, 0, tzinfo=run_daily_learning.TIMEZONE)
        next_start = datetime(2026, 10, 6, 16, 0, tzinfo=run_daily_learning.TIMEZONE)
        now = deadline - timedelta(minutes=90)
        snapshot = run_daily_learning.closeout_snapshot(now, deadline, next_start)
        self.assertEqual(snapshot["decision"], "continue-current-or-partial")
        self.assertTrue(snapshot["can_continue_current"])
        self.assertFalse(snapshot["can_complete_forward_card"])

    def test_closeout_snapshot_moves_to_closeout_when_window_is_short_or_expired(self) -> None:
        deadline = datetime(2026, 10, 6, 15, 0, tzinfo=run_daily_learning.TIMEZONE)
        next_start = datetime(2026, 10, 6, 16, 0, tzinfo=run_daily_learning.TIMEZONE)
        short = run_daily_learning.closeout_snapshot(
            deadline - timedelta(minutes=89), deadline, next_start
        )
        expired = run_daily_learning.closeout_snapshot(deadline, deadline, next_start)
        self.assertEqual(short["decision"], "finish-current-no-new-unit")
        self.assertEqual(expired["decision"], "closeout-only")

    def test_next_schedule_time_is_day_after_run_at_1600(self) -> None:
        self.assertEqual(
            run_daily_learning.next_scheduled_start_for_run_date("2026-10-05"),
            datetime(2026, 10, 6, 16, 0, tzinfo=run_daily_learning.TIMEZONE),
        )

    def test_render_prompt_injects_fresh_runtime_gate_into_existing_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths = run_daily_learning.get_paths(root)
            snapshot = root / "existing-prompt.md"
            snapshot.write_text("Existing Day 6 snapshot.\n", encoding="utf-8")
            now = datetime(2026, 10, 6, 4, 0, tzinfo=run_daily_learning.TIMEZONE)
            deadline = datetime(2026, 10, 6, 15, 0, tzinfo=run_daily_learning.TIMEZONE)
            prompt = run_daily_learning.render_prompt(
                paths,
                "2026-10-05-day-06-01",
                "2026-10-05",
                6,
                prompt_file=snapshot,
                window_deadline=deadline,
                runtime_now=now,
            )
        self.assertIn("Runtime schedule snapshot", prompt)
        self.assertIn("minutes_to_deadline: 660", prompt)
        self.assertIn("minutes_to_next_start: 720", prompt)
        self.assertIn("completed_day_indices", prompt)
        self.assertIn("DAILY_LEARNING_TIME_GATE_V1", prompt)

    def test_render_continuation_prompt_injects_current_clock_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths = run_daily_learning.get_paths(root)
            paths.continuation_prompt_file.parent.mkdir(parents=True)
            paths.continuation_prompt_file.write_text("Continue Day {{DAY_INDEX}}.\n", encoding="utf-8")
            now = datetime(2026, 10, 6, 14, 0, tzinfo=run_daily_learning.TIMEZONE)
            deadline = datetime(2026, 10, 6, 15, 0, tzinfo=run_daily_learning.TIMEZONE)
            paths.daily_root.mkdir(parents=True, exist_ok=True)
            report = paths.daily_root / f"{run_daily_learning.daily_file_stem('2026-10-05', 6)}.md"
            report.write_text(coverage_report([6], [7]), encoding="utf-8")
            prompt = run_daily_learning.render_continuation_prompt(
                paths, "run-1", "2026-10-05", 6, 1, deadline, now=now
            )
        self.assertIn("minutes_to_deadline: 60", prompt)
        self.assertIn("finish-current-no-new-unit", prompt)
        self.assertIn("Next card candidate: Day 7", prompt)

    def test_runtime_snapshot_stops_full_card_credit_after_one_forward_card(self) -> None:
        snapshot = {
            "now_local": "2026-10-05T18:00:00+08:00",
            "hard_deadline": "2026-10-06T15:00:00+08:00",
            "next_scheduled_start": "2026-10-06T16:00:00+08:00",
            "minutes_to_deadline": 1260,
            "minutes_to_next_start": 1320,
            "decision": "continue-or-advance",
        }
        prompt = run_daily_learning.format_runtime_schedule_snapshot(snapshot, 6, 8)
        self.assertIn("Next card candidate: Day 8", prompt)
        self.assertIn("do not credit another card", prompt)

    def test_continuation_limit_before_deadline_is_not_window_complete(self) -> None:
        deadline = datetime(2026, 10, 6, 15, 0, tzinfo=run_daily_learning.TIMEZONE)
        self.assertTrue(
            run_daily_learning.continuation_limit_reached(
                96, 96, deadline - timedelta(minutes=5), deadline
            )
        )
        self.assertFalse(
            run_daily_learning.continuation_limit_reached(96, 96, deadline, deadline)
        )

    def test_final_closeout_turn_uses_only_reserved_1500_to_1600_window(self) -> None:
        deadline = datetime(2026, 10, 6, 15, 0, tzinfo=run_daily_learning.TIMEZONE)
        self.assertFalse(
            run_daily_learning.should_run_closeout_turn(
                deadline - timedelta(seconds=1), deadline
            )
        )
        self.assertTrue(
            run_daily_learning.should_run_closeout_turn(
                deadline, deadline
            )
        )
        self.assertTrue(
            run_daily_learning.should_run_closeout_turn(
                deadline + timedelta(minutes=59), deadline
            )
        )
        self.assertFalse(
            run_daily_learning.should_run_closeout_turn(
                deadline + timedelta(hours=1), deadline
            )
        )

    def test_continuation_action_never_confuses_saturation_with_window_close(self) -> None:
        deadline = datetime(2026, 10, 6, 15, 0, tzinfo=run_daily_learning.TIMEZONE)
        self.assertEqual(
            run_daily_learning.next_continuation_action(
                deadline - timedelta(hours=11), deadline, 0, 96, False
            ),
            "study",
        )
        self.assertEqual(
            run_daily_learning.next_continuation_action(
                deadline - timedelta(minutes=1), deadline, 96, 96, False
            ),
            "rollover",
        )
        self.assertEqual(
            run_daily_learning.next_continuation_action(
                deadline - timedelta(minutes=1), deadline, 0, 96, False
            ),
            "study",
        )
        self.assertEqual(
            run_daily_learning.next_continuation_action(
                deadline, deadline, 96, 96, False
            ),
            "closeout",
        )
        self.assertEqual(
            run_daily_learning.next_continuation_action(
                deadline, deadline, 96, 96, True
            ),
            "finalize",
        )

    def test_curriculum_coverage_advances_only_complete_cards(self) -> None:
        full = run_daily_learning.parse_curriculum_coverage(
            coverage_report([6, 7], [], day7_scorecard=True, day7_reflect=True),
            6,
        )
        partial = run_daily_learning.parse_curriculum_coverage(
            coverage_report([6], [7]),
            6,
        )
        self.assertTrue(full["valid"], full)
        self.assertEqual(full["next_day_index"], 8)
        self.assertEqual(full["curriculum_cards_completed"], 2)
        self.assertTrue(partial["valid"], partial)
        self.assertEqual(partial["next_day_index"], 7)
        self.assertEqual(partial["curriculum_cards_completed"], 1)

    def test_curriculum_coverage_rejects_gaps_and_incomplete_day7_exam(self) -> None:
        skipped = run_daily_learning.parse_curriculum_coverage(
            coverage_report([6, 8], []),
            6,
        )
        incomplete_exam = run_daily_learning.parse_curriculum_coverage(
            coverage_report([6, 7], [], day7_scorecard=True), 6
        )
        self.assertFalse(skipped["valid"])
        self.assertFalse(incomplete_exam["valid"])

    def test_curriculum_state_advances_through_completed_forward_card(self) -> None:
        coverage = run_daily_learning.parse_curriculum_coverage(
            coverage_report([6, 7], [], day7_scorecard=True, day7_reflect=True),
            6,
        )
        state = {"next_day_index": 6, "completed_day_count": 5, "status": "active"}
        updated = run_daily_learning.update_state_for_curriculum_cards(
            state, "run-06", "2026-10-05", coverage
        )
        self.assertEqual(updated["next_day_index"], 8)
        self.assertEqual(updated["completed_day_count"], 7)
        self.assertEqual(state["next_day_index"], 6)

    def test_partial_forward_card_keeps_it_as_next_day(self) -> None:
        coverage = run_daily_learning.parse_curriculum_coverage(
            coverage_report([6], [7]),
            6,
        )
        state = {"next_day_index": 6, "completed_day_count": 5, "status": "active"}
        updated = run_daily_learning.update_state_for_curriculum_cards(
            state, "run-06", "2026-10-05", coverage
        )
        self.assertEqual(updated["next_day_index"], 7)
        self.assertEqual(updated["completed_day_count"], 6)

    def test_partial_primary_card_does_not_advance_state(self) -> None:
        coverage = run_daily_learning.parse_curriculum_coverage(
            coverage_report([], [6]),
            6,
        )
        state = {"next_day_index": 6, "completed_day_count": 5, "status": "active"}
        updated = run_daily_learning.update_state_for_curriculum_cards(
            state, "run-06", "2026-10-05", coverage
        )
        self.assertEqual(updated, state)

    def test_next_prompt_can_be_prepared_for_forward_advanced_day(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths = run_daily_learning.get_paths(root)
            paths.prompt_file.parent.mkdir(parents=True)
            paths.prompt_file.write_text("DAY {{DAY_INDEX}} {{WINDOW_CLOSEOUT_AT}}\n", encoding="utf-8")
            prompt_path = run_daily_learning.prepare_next_prompt(paths, "2026-10-06", 8)
            self.assertIn("DAY8", prompt_path.name)
            self.assertIn("DAY 8", prompt_path.read_text(encoding="utf-8"))

    def test_existing_prepared_prompt_gets_shared_time_gate_without_losing_notes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths = run_daily_learning.get_paths(root)
            path = paths.daily_root / "prompts" / "20261006-DAY7-collective-motion-oral-exam.md"
            path.parent.mkdir(parents=True)
            path.write_text("Existing Day 7 prompt.\nUser note: retain this.\n", encoding="utf-8")
            updated = run_daily_learning.prepare_next_prompt(paths, "2026-10-06", 7)
            content = updated.read_text(encoding="utf-8")
            self.assertEqual(updated, path)
        self.assertIn("Existing Day 7 prompt.", content)
        self.assertIn("User note: retain this.", content)
        self.assertIn("DAILY_LEARNING_TIME_GATE_V1", content)
        self.assertIn("DAILY_LEARNING_CURRICULUM_COVERAGE_V1", content)

    def test_completed_card_requires_an_audited_deliverable_table(self) -> None:
        invalid = run_daily_learning.parse_curriculum_coverage(
            "## Run state\n"
            "- completed_day_indices: [6]\n"
            "- partial_day_indices: []\n"
            "- Day 6 card audit: complete\n",
            6,
        )
        self.assertFalse(invalid["valid"])
        self.assertIn("card completion audit table", invalid["error"])

    def test_phase_table_covers_all_days(self) -> None:
        self.assertEqual(run_daily_learning.phase_for_day(1), "baseline-and-research-contract")
        self.assertEqual(run_daily_learning.phase_for_day(30), "final-exam-and-prospectus")
        with self.assertRaises(ValueError):
            run_daily_learning.phase_for_day(31)

    def test_daily_file_stem_uses_compact_date_day_and_chinese_topic(self) -> None:
        self.assertEqual(
            run_daily_learning.daily_file_stem("2026-09-24", 1),
            "20260924-DAY1-baseline-research-contract",
        )
        self.assertIn("beta-gamma", run_daily_learning.daily_file_stem("2026-09-24", 5))
        self.assertIn("γ", run_daily_learning.day_topic(5))

    def test_build_command_uses_full_access_search_and_new_session_exec(self) -> None:
        command = run_daily_learning.build_command(
            Path("/workspace/wiki"), "gpt-6-luna", Path("/tmp/last.md"), True
        )
        self.assertEqual(command[:8], ["codex", "-C", "/workspace/wiki", "-m", "gpt-6-luna", "-s", "danger-full-access", "-a"])
        self.assertIn("never", command)
        self.assertIn("--search", command)
        self.assertIn("exec", command)
        self.assertIn("--thread-source", command)
        self.assertIn("scheduled", command)
        self.assertLess(command.index("exec"), command.index("--thread-source"))
        self.assertNotIn("resume", command)
        self.assertNotIn("--ephemeral", command)

    def test_build_resume_command_targets_recorded_session(self) -> None:
        command = run_daily_learning.build_resume_command(Path("/workspace/wiki"), "session-123")
        self.assertEqual(command[:4], ["codex", "resume", "session-123", "-C"])
        self.assertIn("danger-full-access", command)
        self.assertIn("never", command)
        with self.assertRaises(ValueError):
            run_daily_learning.build_resume_command(Path("/workspace/wiki"), " ")

    def test_resume_exec_command_and_overnight_deadline(self) -> None:
        command = run_daily_learning.build_resume_exec_command(
            Path("/workspace/wiki"),
            "gpt-6-luna",
            "session-123",
            Path("/tmp/continuation.md"),
            True,
            "max",
        )
        self.assertIn("exec", command)
        self.assertIn("resume", command)
        self.assertIn("session-123", command)
        self.assertIn("--search", command)
        now = datetime(2026, 9, 24, 22, 0, tzinfo=run_daily_learning.TIMEZONE)
        deadline = run_daily_learning.parse_deadline("10:00", now)
        self.assertEqual(deadline.date().isoformat(), "2026-09-25")
        self.assertEqual(deadline.hour, 10)

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
            result = run_daily_learning.dry_run(paths, "gpt-6-luna", True)
        self.assertEqual(result["status"], "dry-run-ok")
        state = run_daily_learning.read_state(paths.state_file)
        self.assertEqual(result["day_index"], int(state.get("next_day_index", 1)))
        self.assertIn("danger-full-access", result["command"])
        self.assertEqual(result["session_mode"], "new-session-per-run")
        self.assertEqual(result["schedule_id"], "wiki-daily-learning")
        self.assertEqual(result["project_root"], str(REPO_ROOT))
        self.assertTrue(result["codex_home"])
        self.assertFalse(result["cycle_complete"])

    def test_report_validation_requires_all_daily_headings(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "daily.md"
            path.write_text("## Run state\n", encoding="utf-8")
            result = run_daily_learning.validate_report(path)
            self.assertFalse(result["valid"])
            self.assertIn("## Sources and evidence", result["missing_headings"])

    def test_acceptance_prompt_marks_run_non_counting_and_atomic(self) -> None:
        paths = run_daily_learning.get_paths(REPO_ROOT)
        prompt = run_daily_learning.render_prompt(
            paths,
            "2026-09-24-day-01-01",
            "2026-09-24",
            1,
            mode="acceptance",
        )
        self.assertIn("Acceptance-only execution contract", prompt)
        self.assertIn("exact atomic locator", prompt)

    def test_report_signature_changes_when_report_changes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "daily.md"
            self.assertIsNone(run_daily_learning.report_signature(path))
            path.write_text("first\n", encoding="utf-8")
            first = run_daily_learning.report_signature(path)
            path.write_text("second\n", encoding="utf-8")
            self.assertNotEqual(first, run_daily_learning.report_signature(path))

    def test_durable_knowledge_requires_resolvable_page_and_locator(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "outputs").mkdir()
            page = root / "knowledge" / "projects" / "example.md"
            page.parent.mkdir(parents=True)
            page.write_text("# durable\nAnchor.\n[[source]]\n", encoding="utf-8")
            source = root / "knowledge" / "sources" / "source.md"
            source.parent.mkdir(parents=True)
            source.write_text("SRC-1: PDF p. 4\n", encoding="utf-8")
            report = root / "outputs" / "daily.md"
            report.write_text(
                "## Durable knowledge delta\n\n"
                "```knowledge-writeback\n"
                '{"status":"updated","items":[{"knowledge":"knowledge/projects/example.md",'
                '"summary":"Added row","anchor":"Anchor.","sources":[{"path":"knowledge/sources/source.md",'
                '"locator":"SRC-1"}]}]}\n'
                "```\n",
                encoding="utf-8",
            )
            before = run_daily_learning.snapshot_knowledge(root)
            page.write_text(page.read_text(encoding="utf-8") + "Changed.\n", encoding="utf-8")
            result = run_daily_learning.validate_durable_knowledge(report, root, before)
            self.assertTrue(result["valid"], result)
            self.assertEqual(result["changed_paths"], ["knowledge/projects/example.md"])

    def test_durable_knowledge_rejects_output_only_delta(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "outputs").mkdir()
            report = root / "outputs" / "daily.md"
            report.write_text(
                "## Durable knowledge delta\n\n"
                "```knowledge-writeback\n"
                '{"status":"updated","items":[{"knowledge":"outputs/not-knowledge.md",'
                '"summary":"Wrong layer","anchor":"x","sources":[]}]}\n'
                "```\n",
                encoding="utf-8",
            )
            result = run_daily_learning.validate_durable_knowledge(report, root)
            self.assertFalse(result["valid"])
            self.assertIn("invalid knowledge path", result["error"])

    def test_verified_noop_still_requires_locator(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "outputs").mkdir()
            (root / "knowledge" / "projects").mkdir(parents=True)
            (root / "knowledge" / "sources").mkdir(parents=True)
            (root / "knowledge" / "projects" / "x.md").write_text("Anchor x.\n[[x-source]]\n", encoding="utf-8")
            (root / "knowledge" / "sources" / "x-source.md").write_text("SRC-X: PDF p. 1\n", encoding="utf-8")
            report = root / "outputs" / "daily.md"
            report.write_text(
                "## Durable knowledge delta\n\n"
                "```knowledge-writeback\n"
                '{"status":"verified-no-op","reason":"No change","items":[{"knowledge":"knowledge/projects/x.md",'
                '"summary":"No change after checking x.","anchor":"Anchor x.","sources":[{"path":"knowledge/sources/x-source.md",'
                '"locator":""}]}]}\n'
                "```\n",
                encoding="utf-8",
            )
            result = run_daily_learning.validate_durable_knowledge(report, root)
            self.assertFalse(result["valid"])
            self.assertIn("source locator", result["error"])

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
                result = run_daily_learning.dry_run(paths, "gpt-6-luna", True)
            self.assertEqual(result["status"], "cycle-complete")
            self.assertIsNone(result["phase"])

    def test_preflight_result_preserves_exit_and_tail(self) -> None:
        completed = type("Completed", (), {"returncode": 0, "stdout": '{"ok":true}', "stderr": ""})()
        with patch.object(run_daily_learning.subprocess, "run", return_value=completed):
            result = run_daily_learning.run_preflight(REPO_ROOT)
        self.assertEqual(result["exit"], 0)
        self.assertIn("ok", result["stdout_tail"])
