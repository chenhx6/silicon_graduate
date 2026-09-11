#!/usr/bin/env python3
"""Monitor Wiki Codex rollout JSONL and queue one recovery per transient failure."""

from __future__ import annotations

import argparse
import json
import os
import re
import signal
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable


RECOVERABLE_CODES = {"server_overloaded", "rate_limit_exceeded", "temporarily_unavailable"}
RECOVERABLE_PATTERNS = ("selected model is at capacity", "temporarily unavailable", "service unavailable", "rate limit", "timed out", "connection reset")
TERMINAL_PATTERN = re.compile(r"auth|permission|cancel|context.*(length|window)|invalid.*(model|parameter)|unknown", re.I)


def inside(child: str | Path, root: str | Path) -> bool:
    try:
        Path(child).resolve().relative_to(Path(root).resolve())
        return True
    except ValueError:
        return False


def classify_error(error: dict[str, object] | None) -> str | None:
    if not error:
        return None
    code = str(error.get("codex_error_info") or error.get("code") or "")
    message = str(error.get("message") or "")
    combined = f"{code} {message}"
    if TERMINAL_PATTERN.search(combined):
        return None
    if code in RECOVERABLE_CODES:
        return code
    lowered = message.lower()
    return "transient-message" if any(item in lowered for item in RECOVERABLE_PATTERNS) else None


def backoff_seconds(attempt: int) -> int:
    return min(2 + 2 * ((max(attempt, 1) - 1) // 10), 10)


def parse_session_events(lines: list[str], project_root: str | Path) -> dict[str, object] | None:
    meta: dict[str, object] | None = None
    latest: dict[str, object] | None = None
    latest_started: dict[str, object] | None = None
    for line in lines:
        try:
            item = json.loads(line)
        except json.JSONDecodeError:
            continue
        if item.get("type") == "session_meta":
            meta = item.get("payload") or {}
        if item.get("type") == "event_msg" and (item.get("payload") or {}).get("type") in {"task_started", "task_complete", "turn_aborted"}:
            latest = item
            if item["payload"]["type"] == "task_started":
                latest_started = item
    if not meta or not inside(str(meta.get("cwd") or ""), project_root) or not latest:
        return None
    return {"id": meta.get("session_id") or meta.get("id"), "cwd": meta.get("cwd"), "latest": latest, "latest_started": latest_started}


def read_rollout(path: Path, project_root: Path) -> dict[str, object] | None:
    try:
        with path.open("rb") as handle:
            size = path.stat().st_size
            first_line = handle.readline().decode("utf-8", errors="replace")
            latest = None
            pending = b""
            cursor = size
            while cursor:
                start = max(0, cursor - 1048576)
                handle.seek(start)
                pending = handle.read(cursor - start) + pending
                parts = pending.split(b"\n")
                complete = parts if start == 0 else parts[1:]
                for raw_line in reversed(complete):
                    if b"event_msg" not in raw_line:
                        continue
                    try:
                        item = json.loads(raw_line.decode("utf-8", errors="replace"))
                    except json.JSONDecodeError:
                        continue
                    payload = item.get("payload") or {}
                    if payload.get("type") in {"task_started", "task_complete", "turn_aborted"}:
                        latest = item
                        break
                if latest is not None or start == 0:
                    break
                pending = parts[0]
                cursor = start
    except OSError:
        return None
    if latest is None:
        return None
    return parse_session_events([first_line, json.dumps(latest)], project_root)


def recovery_step(session: dict[str, object], previous: dict[str, object] | None, now: float, queue: Callable[[str, str], int], max_attempts: int | None = None) -> dict[str, object]:
    previous = dict(previous or {})
    event = session["latest"]
    payload = event.get("payload") or {}
    event_key = f"{session['id']}:{payload.get('turn_id')}:{event.get('timestamp')}"
    if payload.get("type") == "task_started":
        return {"status": "running", "event_key": event_key, "attempts": 0, "pending": False, "next_at": 0, "last_event_timestamp": event.get("timestamp")}
    if payload.get("type") == "turn_aborted":
        return {**previous, "status": "cancelled", "pending": False, "last_event_timestamp": event.get("timestamp")}
    if not payload.get("error"):
        return {**previous, "status": "complete", "pending": False, "last_event_timestamp": event.get("timestamp")}
    error_class = classify_error(payload.get("error"))
    if not error_class:
        return {**previous, "status": "manual-attention-required", "pending": False, "last_event_timestamp": event.get("timestamp")}
    if previous.get("event_key") != event_key:
        previous = {"event_key": event_key, "attempts": 0, "pending": False, "next_at": 0}
    if previous.get("pending"):
        return {**previous, "status": "recovery-pending", "error_class": error_class}
    if max_attempts is not None and int(previous.get("attempts", 0)) >= max_attempts:
        return {**previous, "status": "manual-attention-required", "error_class": error_class}
    if now < float(previous.get("next_at", 0)):
        return {**previous, "status": "waiting-retry", "error_class": error_class}
    message = "[farmer resume]\nContinue the existing task from the last completed checkpoint.\nPreserve the original objective, context, files, model, and current working state.\nDo not reinterpret the task or start a new one."
    exit_code = queue(str(session["id"]), message)
    attempts = int(previous.get("attempts", 0)) + 1
    return {**previous, "status": "recovery-pending" if exit_code == 0 else "waiting-retry", "error_class": error_class, "attempts": attempts, "pending": exit_code == 0, "next_at": now + backoff_seconds(attempts), "last_exit_code": exit_code, "last_action_at": datetime.now(timezone.utc).isoformat(), "last_event_timestamp": event.get("timestamp")}


def walk_rollouts(codex_home: Path) -> list[Path]:
    sessions = codex_home / "sessions"
    return list(sessions.rglob("*.jsonl")) if sessions.is_dir() else []


def runtime_paths(root: Path) -> tuple[Path, Path, Path]:
    runtime = root / "tmp" / "farmer"
    return runtime, runtime / "state.json", runtime / "pid"


def read_json(path: Path, fallback: object) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return fallback


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + f".{os.getpid()}.tmp")
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(path)


def process_once(root: Path, codex_home: Path, dry_run: bool = False, max_attempts: int | None = None) -> dict[str, object]:
    _, state_path, _ = runtime_paths(root)
    states = read_json(state_path, {})
    if not isinstance(states, dict):
        states = {}
    sessions: dict[str, object] = {}
    actions: list[dict[str, object]] = []
    now = time.time()
    latest_sessions: dict[str, tuple[tuple[str, float, str], dict[str, object]]] = {}
    for rollout in walk_rollouts(codex_home):
        session = read_rollout(rollout, root)
        if not session or not session.get("id"):
            continue
        session_id = str(session["id"])
        latest = session.get("latest") or {}
        timestamp = str(latest.get("timestamp") or "")
        try:
            mtime = rollout.stat().st_mtime
        except OSError:
            mtime = 0.0
        order = (timestamp, mtime, str(rollout))
        previous_session = latest_sessions.get(session_id)
        if previous_session is not None and previous_session[0] >= order:
            continue
        latest_sessions[session_id] = (order, session)

    for session_id, (_, session) in sorted(latest_sessions.items()):
        previous = states.get(session_id) if isinstance(states.get(session_id), dict) else None
        def queue(thread: str, message: str) -> int:
            if dry_run:
                actions.append({"thread": thread, "action": "queue", "message": message})
                return 0
            result = subprocess.run(["codex", "queue", "--thread", thread, "--message", message], text=True, capture_output=True, check=False, timeout=15)
            return result.returncode
        next_state = recovery_step(session, previous, now, queue, max_attempts)
        sessions[session_id] = {"cwd": session["cwd"], "status": next_state.get("status"), "event": (session["latest"].get("payload") or {}).get("type")}
        states[session_id] = next_state
    if not dry_run:
        write_json(state_path, states)
    return {"root": str(root), "sessions": sessions, "actions": actions, "dry_run": dry_run}


def pid_alive(pid: object) -> bool:
    try:
        os.kill(int(pid), 0)
        return True
    except (ValueError, OSError, TypeError):
        return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["once", "watch", "start", "ensure", "status", "stop"])
    parser.add_argument("--root", default=".")
    parser.add_argument("--codex-home", default=os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))
    parser.add_argument("--poll", type=float, default=2.0)
    parser.add_argument("--max-attempts", type=int, default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    root = Path(args.root).resolve()
    codex_home = Path(args.codex_home).expanduser().resolve()
    runtime, state_path, pid_path = runtime_paths(root)
    if args.command == "status":
        owner = read_json(pid_path, {})
        print(json.dumps({"running": pid_alive(owner.get("pid") if isinstance(owner, dict) else None), "owner": owner, "state": read_json(state_path, {})}, ensure_ascii=False, indent=2))
        return 0
    if args.command == "stop":
        owner = read_json(pid_path, {})
        if isinstance(owner, dict) and pid_alive(owner.get("pid")):
            os.kill(int(owner["pid"]), signal.SIGTERM)
        print(json.dumps({"stop_requested": owner.get("pid") if isinstance(owner, dict) else None}))
        return 0
    if args.command == "once":
        print(json.dumps(process_once(root, codex_home, args.dry_run, args.max_attempts), ensure_ascii=False, indent=2))
        return 0
    if args.command == "ensure":
        owner = read_json(pid_path, {})
        if isinstance(owner, dict) and pid_alive(owner.get("pid")):
            print(json.dumps({"running": True, "pid": owner["pid"]}))
            return 0
        if args.dry_run:
            print(json.dumps({"would_start": True}))
            return 0
        runtime.mkdir(parents=True, exist_ok=True)
        command = [sys.executable, str(Path(__file__).resolve()), "watch", "--root", str(root), "--codex-home", str(codex_home), "--poll", str(args.poll)]
        child = subprocess.Popen(command, cwd=root, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
        print(json.dumps({"started_pid": child.pid}))
        return 0
    runtime.mkdir(parents=True, exist_ok=True)
    if pid_alive(read_json(pid_path, {}).get("pid") if isinstance(read_json(pid_path, {}), dict) else None):
        raise SystemExit("farmer already running")
    write_json(pid_path, {"pid": os.getpid(), "root": str(root), "started_at": datetime.now(timezone.utc).isoformat()})
    try:
        while True:
            process_once(root, codex_home, False, args.max_attempts)
            time.sleep(max(args.poll, 0.5))
    except KeyboardInterrupt:
        return 0
    finally:
        owner = read_json(pid_path, {})
        if isinstance(owner, dict) and owner.get("pid") == os.getpid():
            pid_path.unlink(missing_ok=True)


if __name__ == "__main__":
    raise SystemExit(main())
