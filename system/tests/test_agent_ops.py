from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from system.scripts.wiki_farmer import (
    backoff_seconds,
    classify_error,
    parse_session_events,
    process_once,
    read_rollout,
    recovery_step,
)
from system.scripts.wiki_hook import relative_candidate


class AgentOpsTests(unittest.TestCase):
    def test_hook_rejects_protected_and_external_paths(self) -> None:
        root = Path(tempfile.mkdtemp(prefix="wiki-hook-"))
        self.assertEqual(relative_candidate(root, "system/log.md").as_posix(), "system/log.md")
        with self.assertRaises(ValueError):
            relative_candidate(root, ".git/index")
        with self.assertRaises(ValueError):
            relative_candidate(root, "../outside")

    def test_farmer_classifies_transient_and_terminal_errors(self) -> None:
        self.assertEqual(classify_error({"codex_error_info": "server_overloaded", "message": "busy"}), "server_overloaded")
        self.assertEqual(classify_error({"message": "connection reset by peer"}), "transient-message")
        self.assertIsNone(classify_error({"message": "authentication failed"}))

    def test_farmer_scopes_sessions_and_queues_once(self) -> None:
        lines = [
            json.dumps({"type": "session_meta", "payload": {"session_id": "s1", "cwd": "/workspace/wiki"}}),
            json.dumps({"type": "event_msg", "timestamp": "2026-09-10T00:00:01Z", "payload": {"type": "task_complete", "turn_id": "t1", "error": {"codex_error_info": "server_overloaded", "message": "busy"}}}),
        ]
        session = parse_session_events(lines, "/workspace/wiki")
        self.assertIsNotNone(session)
        calls: list[str] = []
        first = recovery_step(session, {"event_key": "old"}, 100.0, lambda thread, message: calls.append(thread) or 0)
        second = recovery_step(session, first, 200.0, lambda thread, message: calls.append(thread) or 0)
        self.assertEqual(calls, ["s1"])
        self.assertTrue(first["pending"])
        self.assertEqual(second["status"], "recovery-pending")

    def test_farmer_uses_latest_rollout_when_session_has_duplicate_files(self) -> None:
        root = Path(tempfile.mkdtemp(prefix="wiki-farmer-"))
        codex_home = root / "codex"
        session_dir = codex_home / "sessions"
        session_dir.mkdir(parents=True)

        def write_rollout(path: Path, event: dict[str, object]) -> None:
            lines = [
                {"type": "session_meta", "payload": {"session_id": "s1", "cwd": str(root)}},
                event,
            ]
            path.write_text("\n".join(json.dumps(line) for line in lines) + "\n", encoding="utf-8")

        newer = session_dir / "newer.jsonl"
        older = session_dir / "older.jsonl"
        write_rollout(
            newer,
            {"type": "event_msg", "timestamp": "2026-09-11T05:00:00Z", "payload": {"type": "task_started", "turn_id": "t2"}},
        )
        write_rollout(
            older,
            {
                "type": "event_msg",
                "timestamp": "2026-09-11T04:00:00Z",
                "payload": {
                    "type": "task_complete",
                    "turn_id": "t1",
                    "error": {"codex_error_info": "server_overloaded", "message": "busy"},
                },
            },
        )

        with patch("system.scripts.wiki_farmer.walk_rollouts", return_value=[newer, older]):
            result = process_once(root, codex_home, dry_run=True)

        self.assertEqual(result["sessions"]["s1"]["status"], "running")
        self.assertEqual(result["actions"], [])

    def test_farmer_reads_oversized_session_metadata(self) -> None:
        root = Path(tempfile.mkdtemp(prefix="wiki-farmer-large-meta-"))
        rollout = root / "rollout.jsonl"
        meta = {
            "type": "session_meta",
            "payload": {"session_id": "s1", "cwd": str(root), "padding": "x" * 300_000},
        }
        event = {
            "type": "event_msg",
            "timestamp": "2026-09-11T05:30:00Z",
            "payload": {"type": "task_started", "turn_id": "t1"},
        }
        rollout.write_text("\n".join(json.dumps(line) for line in (meta, event)) + "\n", encoding="utf-8")

        session = read_rollout(rollout, root)

        self.assertIsNotNone(session)
        self.assertEqual(session["id"], "s1")
        self.assertEqual(session["latest"]["payload"]["type"], "task_started")

    def test_backoff_caps(self) -> None:
        self.assertEqual(backoff_seconds(1), 2)
        self.assertEqual(backoff_seconds(11), 4)
        self.assertEqual(backoff_seconds(99), 10)


if __name__ == "__main__":
    unittest.main()
