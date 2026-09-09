from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from system.scripts.wiki_farmer import (
    backoff_seconds,
    classify_error,
    parse_session_events,
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

    def test_backoff_caps(self) -> None:
        self.assertEqual(backoff_seconds(1), 2)
        self.assertEqual(backoff_seconds(11), 4)
        self.assertEqual(backoff_seconds(99), 10)


if __name__ == "__main__":
    unittest.main()
