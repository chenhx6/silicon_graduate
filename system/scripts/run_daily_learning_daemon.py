#!/usr/bin/env python3
"""Run the Wiki daily-learning runner from inside the Docker container.

This process is the container-local clock.  It intentionally has no Docker,
PowerShell, cron, host scheduler or network-control dependency: it waits for
the next Asia/Shanghai trigger and invokes ``run_daily_learning.py`` directly
as a child process.
"""

from __future__ import annotations

import argparse
import fcntl
import json
import os
import signal
import subprocess
import sys
import tempfile
import time
from contextlib import contextmanager
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Iterator
from zoneinfo import ZoneInfo


TIMEZONE = ZoneInfo("Asia/Shanghai")
TOTAL_DAYS = 30
CYCLE_NAME = "2026-09-30-day-substantive"
SCHEDULE_ID = "wiki-daily-learning"
SCHEDULE_NAME = "Wiki 30-day substantive daily learning"
DEFAULT_HOUR = 22
DEFAULT_MINUTE = 0
DEFAULT_POLL_SECONDS = 30
DEFAULT_LOCK_FILE = Path("/tmp/wiki-one-month-daily-learning-daemon.lock")
STATE_NAME = "2026-09-one-month-scheduler-state.json"
LOG_NAME = "2026-09-one-month-scheduler.jsonl"
MODEL_PRIORITY = (
    ("gpt-6-luna", "max"),
    ("gpt-6-sol", "high"),
    ("gpt-6-astra", "medium"),
)


def get_state_path(root: Path) -> Path:
    return root / "outputs" / "learning-milestones" / STATE_NAME


def get_log_path(root: Path) -> Path:
    return root / "outputs" / "learning-milestones" / LOG_NAME


def next_trigger(
    now: datetime,
    hour: int = DEFAULT_HOUR,
    minute: int = DEFAULT_MINUTE,
) -> datetime:
    """Return the next wall-clock trigger in ``now``'s timezone."""

    if now.tzinfo is None:
        raise ValueError("now must be timezone-aware")
    target = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if target <= now:
        target += timedelta(days=1)
    return target


def next_due(
    now: datetime,
    marker: dict[str, Any],
    hour: int = DEFAULT_HOUR,
    minute: int = DEFAULT_MINUTE,
) -> datetime:
    """Return the next due time, catching up a missed trigger once per day."""

    if now.tzinfo is None:
        raise ValueError("now must be timezone-aware")
    today = now.date().isoformat()
    target = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    last_date = marker.get("last_scheduled_date")
    last_status = marker.get("last_status")

    if last_date == today and last_status == "running":
        return now
    if target <= now and last_date != today:
        return now
    if target > now:
        return target
    return target + timedelta(days=1)


def build_runner_command(
    root: Path,
    model: str,
    no_search: bool,
    reasoning_effort: str | None = None,
) -> list[str]:
    command = [
        str(root / "system" / "scripts" / "run_daily_learning_schedule.sh"),
        "--root",
        str(root),
        "--day-index",
        "auto",
        "--mode",
        "daily-learning",
        "--model",
        model,
    ]
    if reasoning_effort:
        command += ["--reasoning-effort", reasoning_effort]
    if no_search:
        command.append("--no-search")
    return command


def read_json(path: Path, default: dict[str, Any]) -> dict[str, Any]:
    if not path.exists():
        return dict(default)
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"cannot read JSON state {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise RuntimeError(f"JSON state must be an object: {path}")
    return value


def write_json_atomic(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_name, path)
    finally:
        try:
            os.unlink(tmp_name)
        except FileNotFoundError:
            pass


def scheduler_default_state() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "cycle": CYCLE_NAME,
        "schedule_id": SCHEDULE_ID,
        "schedule_name": SCHEDULE_NAME,
        "project_root": None,
        "counting_policy": "30 successful substantive days; acceptance-only runs are excluded",
        "last_scheduled_date": None,
        "last_status": None,
        "last_runner_exit": None,
        "updated_at": None,
    }


def learning_cycle_complete(root: Path) -> bool:
    """Return whether the substantive 30-day runner has no day left to execute."""

    path = root / "outputs" / "learning-milestones" / "2026-09-one-month-state.json"
    state = read_json(path, {"next_day_index": 1, "status": "not-started"})
    try:
        next_day = int(state.get("next_day_index", 1))
    except (TypeError, ValueError) as exc:
        raise RuntimeError(f"invalid next_day_index in {path}") from exc
    return state.get("status") == "complete" or next_day > TOTAL_DAYS


def now_local() -> datetime:
    return datetime.now(TIMEZONE)


def append_event(path: Path, event: str, **fields: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    record = {"timestamp": now_local().isoformat(), "event": event, **fields}
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        handle.flush()


def is_retryable_model_error(reason: str | None) -> bool:
    if not reason:
        return False
    lowered = reason.lower()
    markers = (
        "capacity",
        "overloaded",
        "rate limit",
        "rate_limit",
        "temporarily unavailable",
        "service unavailable",
        "model not found",
        "model unavailable",
        "unknown model",
    )
    return any(marker in lowered for marker in markers)


def _receipt_from_stdout(stdout: str) -> dict[str, Any]:
    try:
        value = json.loads(stdout.strip())
    except json.JSONDecodeError:
        value = None
    if isinstance(value, dict) and "status" in value:
        return value
    for line in reversed(stdout.splitlines()):
        try:
            value = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict) and "status" in value:
            return value
    return {}


def run_once_result(
    root: Path,
    model: str,
    no_search: bool,
    log_path: Path,
    reasoning_effort: str | None = None,
) -> dict[str, Any]:
    command = build_runner_command(root, model, no_search, reasoning_effort)
    append_event(
        log_path,
        "runner-started",
        schedule_id=SCHEDULE_ID,
        schedule_name=SCHEDULE_NAME,
        project_root=str(root),
        session_scope="one-new-session-for-each-schedule-run",
        model=model,
        reasoning_effort=reasoning_effort,
        command=command,
    )
    result = subprocess.run(
        command,
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
        shell=False,
    )
    # The runner owns detailed events/stderr.  Keep this scheduler log limited
    # to exit metadata so credentials or source text cannot be duplicated here.
    receipt = _receipt_from_stdout(result.stdout)
    reason = receipt.get("failure_reason")
    if not isinstance(reason, str):
        reason = result.stderr[-2000:] if result.stderr else None
    retryable = result.returncode != 0 and is_retryable_model_error(reason)
    append_event(
        log_path,
        "runner-finished",
        schedule_id=SCHEDULE_ID,
        schedule_name=SCHEDULE_NAME,
        project_root=str(root),
        session_scope="one-new-session-for-each-schedule-run",
        model=model,
        reasoning_effort=reasoning_effort,
        exit_code=result.returncode,
        status="completed" if result.returncode == 0 else "failed",
        retryable=retryable,
        session_id=receipt.get("session_id"),
        resume_command=receipt.get("resume_command"),
        overnight_until=receipt.get("overnight_until"),
        continuation_count=receipt.get("continuation_count"),
        failure_reason=reason,
    )
    return {
        "exit_code": result.returncode,
        "retryable": retryable,
        "failure_reason": reason,
        "model": model,
        "reasoning_effort": reasoning_effort,
        "session_id": receipt.get("session_id"),
        "resume_command": receipt.get("resume_command"),
        "overnight_until": receipt.get("overnight_until"),
        "continuation_count": receipt.get("continuation_count"),
    }


def run_once(root: Path, model: str, no_search: bool, log_path: Path) -> int:
    return int(run_once_result(root, model, no_search, log_path)["exit_code"])


def run_profile_chain(
    root: Path,
    profiles: tuple[tuple[str, str | None], ...],
    no_search: bool,
    log_path: Path,
) -> dict[str, Any]:
    last: dict[str, Any] = {"exit_code": 1, "retryable": False}
    for index, (model, effort) in enumerate(profiles):
        last = run_once_result(root, model, no_search, log_path, effort)
        if last["exit_code"] == 0 or not last["retryable"] or index == len(profiles) - 1:
            return last
        next_model, next_effort = profiles[index + 1]
        append_event(
            log_path,
            "model-fallback",
            from_model=model,
            from_reasoning_effort=effort,
            to_model=next_model,
            to_reasoning_effort=next_effort,
            reason=last.get("failure_reason"),
        )
    return last


@contextmanager
def scheduler_lock(path: Path) -> Iterator[None]:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise RuntimeError(f"another daily-learning daemon holds {path}") from exc
        yield


def install_signal_handlers(stop: dict[str, bool]) -> None:
    def request_stop(signum: int, _frame: Any) -> None:
        stop["requested"] = True
        print(f"daily-learning daemon received signal {signum}", file=sys.stderr, flush=True)

    signal.signal(signal.SIGTERM, request_stop)
    signal.signal(signal.SIGINT, request_stop)


def validate_root(root: Path) -> None:
    required = (
        root / "README.md",
        root / ".git",
        root / "system" / "scripts" / "run_daily_learning.py",
    )
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise RuntimeError("Wiki root is incomplete: " + ", ".join(missing))


def dry_run(
    root: Path,
    profiles: tuple[tuple[str, str | None], ...],
    no_search: bool,
    hour: int,
    minute: int,
) -> dict[str, Any]:
    validate_root(root)
    now = now_local()
    marker = read_json(get_state_path(root), scheduler_default_state())
    due = next_due(now, marker, hour, minute)
    return {
        "status": "dry-run-ok",
        "root": str(root),
        "schedule_id": SCHEDULE_ID,
        "schedule_name": SCHEDULE_NAME,
        "session_scope": "one-new-session-for-each-schedule-run",
        "timezone": str(TIMEZONE),
        "now": now.isoformat(),
        "next_due": due.isoformat(),
        "cycle_complete": learning_cycle_complete(root),
        "model_priority": [
            {"model": model, "reasoning_effort": effort} for model, effort in profiles
        ],
        "command": build_runner_command(root, profiles[0][0], no_search, profiles[0][1]),
        "lock_file": str(DEFAULT_LOCK_FILE),
        "state_file": str(get_state_path(root)),
        "log_file": str(get_log_path(root)),
    }


def daemon_loop(
    root: Path,
    profiles: tuple[tuple[str, str | None], ...],
    no_search: bool,
    hour: int,
    minute: int,
    poll_seconds: float,
    lock_path: Path,
    state_path: Path,
    log_path: Path,
) -> int:
    stop = {"requested": False}
    install_signal_handlers(stop)
    with scheduler_lock(lock_path):
        append_event(log_path, "daemon-started", root=str(root), hour=hour, minute=minute)
        while not stop["requested"]:
            if learning_cycle_complete(root):
                append_event(
                    log_path,
                    "cycle-complete",
                    cycle=CYCLE_NAME,
                    schedule_id=SCHEDULE_ID,
                    schedule_name=SCHEDULE_NAME,
                    project_root=str(root),
                )
                return 0
            marker = read_json(state_path, scheduler_default_state())
            now = now_local()
            due = next_due(now, marker, hour, minute)
            append_event(log_path, "waiting", next_due=due.isoformat())
            while not stop["requested"]:
                remaining = (due - now_local()).total_seconds()
                if remaining <= 0:
                    break
                time.sleep(min(max(remaining, 0.1), poll_seconds))
            if stop["requested"]:
                break

            marker.update(
                {
                    "schema_version": 1,
                    "cycle": CYCLE_NAME,
                    "schedule_id": SCHEDULE_ID,
                    "schedule_name": SCHEDULE_NAME,
                    "project_root": str(root),
                    "session_scope": "one-new-session-for-each-schedule-run",
                    "counting_policy": "30 successful substantive days; acceptance-only runs are excluded",
                    "last_scheduled_date": now_local().date().isoformat(),
                    "last_status": "running",
                    "last_runner_exit": None,
                    "updated_at": now_local().isoformat(),
                }
            )
            write_json_atomic(state_path, marker)
            result = run_profile_chain(root, profiles, no_search, log_path)
            exit_code = int(result["exit_code"])
            marker.update(
                {
                    "last_status": "completed" if exit_code == 0 else "failed",
                    "last_runner_exit": exit_code,
                    "last_model": result.get("model"),
                    "last_reasoning_effort": result.get("reasoning_effort"),
                    "updated_at": now_local().isoformat(),
                }
            )
            write_json_atomic(state_path, marker)
        append_event(log_path, "daemon-stopped")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--model", default=None)
    parser.add_argument("--reasoning-effort", choices=["low", "medium", "high", "max"], default=None)
    parser.add_argument("--no-search", action="store_true")
    parser.add_argument("--hour", type=int, default=DEFAULT_HOUR)
    parser.add_argument("--minute", type=int, default=DEFAULT_MINUTE)
    parser.add_argument("--poll-seconds", type=float, default=DEFAULT_POLL_SECONDS)
    parser.add_argument("--lock-file", type=Path, default=DEFAULT_LOCK_FILE)
    parser.add_argument("--state-file", type=Path, default=None)
    parser.add_argument("--log-file", type=Path, default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--once",
        action="store_true",
        help="invoke the runner once immediately; intended for an in-container test",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    state_path = (args.state_file or get_state_path(root)).resolve()
    log_path = (args.log_file or get_log_path(root)).resolve()
    profiles = (
        ((args.model, args.reasoning_effort),)
        if args.model
        else MODEL_PRIORITY
    )
    try:
        if args.dry_run:
            print(
                json.dumps(
                    dry_run(root, profiles, args.no_search, args.hour, args.minute),
                    ensure_ascii=False,
                    indent=2,
                )
            )
            return 0
        validate_root(root)
        if not 0 <= args.hour <= 23 or not 0 <= args.minute <= 59:
            raise ValueError("hour must be 0..23 and minute must be 0..59")
        if args.poll_seconds <= 0:
            raise ValueError("poll-seconds must be positive")
        if args.once:
            with scheduler_lock(args.lock_file):
                return int(run_profile_chain(root, profiles, args.no_search, log_path)["exit_code"])
        return daemon_loop(
            root,
            profiles,
            args.no_search,
            args.hour,
            args.minute,
            args.poll_seconds,
            args.lock_file,
            state_path,
            log_path,
        )
    except RuntimeError as exc:
        print(json.dumps({"status": "daemon-blocked", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 75
    except Exception as exc:
        print(json.dumps({"status": "daemon-error", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
