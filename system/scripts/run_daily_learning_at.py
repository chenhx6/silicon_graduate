#!/usr/bin/env python3
"""Wait in the foreground, then run one date-specific daily-learning prompt."""

from __future__ import annotations

import argparse
import fcntl
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from run_daily_learning_daemon import (  # noqa: E402
    DEFAULT_LOCK_FILE,
    MODEL_PRIORITY,
    SCHEDULE_ID,
    SCHEDULE_NAME,
    append_event,
    get_log_path,
    get_state_path,
    is_retryable_model_error,
    read_json,
    scheduler_default_state,
    write_json_atomic,
)

ROOT_PATH = Path("/workspace/wiki")
TIMEZONE = ZoneInfo("Asia/Shanghai")
RUNNER = ROOT_PATH / "system/scripts/run_daily_learning.py"
DAY_STATE = ROOT_PATH / "outputs/learning-milestones/2026-09-one-month-state.json"
SOURCE = "manual-foreground-waiter"


def local_now() -> datetime:
    return datetime.now(TIMEZONE)


def parse_target(value: str) -> datetime:
    try:
        return datetime.strptime(value, "%Y-%m-%d %H:%M").replace(tzinfo=TIMEZONE)
    except ValueError as exc:
        raise ValueError("--at must use YYYY-MM-DD HH:MM in Asia/Shanghai") from exc


def current_day_index() -> int:
    try:
        state = json.loads(DAY_STATE.read_text(encoding="utf-8"))
        index = int(state["next_day_index"])
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        raise RuntimeError(f"cannot read next_day_index from {DAY_STATE}: {exc}") from exc
    if not 1 <= index <= 30:
        raise RuntimeError(f"next_day_index is outside the plan: {index}")
    return index


def prompt_context(prompt: Path) -> tuple[str | None, int | None]:
    content = prompt.read_text(encoding="utf-8")
    date_match = re.search(r"(?m)^-\s*`run_date`:\s*(\d{4}-\d{2}-\d{2})\s*$", content)
    day_match = re.search(r"(?m)^-\s*`day_index`:\s*(\d+)\s*$", content)
    return (
        date_match.group(1) if date_match else None,
        int(day_match.group(1)) if day_match else None,
    )


def validate_prompt(prompt: Path, run_date: str, day_index: int) -> None:
    if not prompt.is_file() or not prompt.read_text(encoding="utf-8").strip():
        raise RuntimeError(f"prompt is missing or empty: {prompt}")
    prompt_date, prompt_day = prompt_context(prompt)
    if prompt_date and prompt_date != run_date:
        raise RuntimeError(f"prompt date {prompt_date} does not match run date {run_date}")
    if prompt_day and prompt_day != day_index:
        raise RuntimeError(f"prompt day {prompt_day} does not match Wiki state {day_index}")


def command_for(root: Path, prompt: Path, day: int, model: str, effort: str) -> list[str]:
    return [
        sys.executable, str(root / "system/scripts/run_daily_learning.py"),
        "--root", str(root), "--day-index", str(day), "--mode", "daily-learning",
        "--model", model, "--reasoning-effort", effort, "--prompt-file", str(prompt),
        "--until", "10:00", "--max-continuations", "96",
    ]


def receipt_from(stdout: str) -> dict[str, Any]:
    try:
        value = json.loads(stdout.strip())
        if isinstance(value, dict):
            return value
    except json.JSONDecodeError:
        pass
    return {}


def record(root: Path, event: str, **fields: Any) -> None:
    append_event(
        get_log_path(root), event,
        source=SOURCE, schedule_id=SCHEDULE_ID, schedule_name=SCHEDULE_NAME,
        project_root=str(root), **fields,
    )


def set_scheduler_state(root: Path, scheduled_date: str, status: str, exit_code: int | None = None,
                        model: str | None = None, effort: str | None = None) -> None:
    path = get_state_path(root)
    state = read_json(path, scheduler_default_state())
    state.update({
        "cycle": "2026-09-30-day-substantive",
        "schedule_id": SCHEDULE_ID,
        "schedule_name": SCHEDULE_NAME,
        "project_root": str(root),
        "session_scope": "one-new-session-for-each-schedule-run",
        "counting_policy": "30 successful substantive days; acceptance-only runs are excluded",
        "last_scheduled_date": scheduled_date,
        "last_status": status,
        "last_runner_exit": exit_code,
        "updated_at": local_now().isoformat(),
    })
    if model:
        state["last_model"] = model
    if effort:
        state["last_reasoning_effort"] = effort
    write_json_atomic(path, state)


def run_profiles(root: Path, prompt: Path, day: int, scheduled_date: str) -> int:
    final_code = 1
    final_model = final_effort = None
    for number, (model, effort) in enumerate(MODEL_PRIORITY, start=1):
        final_model, final_effort = model, effort
        command = command_for(root, prompt, day, model, effort)
        record(root, "runner-started", attempt=number, model=model, reasoning_effort=effort,
               command=command, prompt_file=str(prompt), day_index=day)
        result = subprocess.run(command, cwd=root, text=True, capture_output=True, check=False)
        receipt = receipt_from(result.stdout)
        reason = receipt.get("failure_reason")
        if not isinstance(reason, str):
            reason = result.stderr[-2000:] if result.stderr else None
        final_code = result.returncode
        retryable = final_code != 0 and is_retryable_model_error(reason)
        record(
            root, "runner-finished", attempt=number, model=model, reasoning_effort=effort,
            exit_code=final_code, status="completed" if final_code == 0 else "failed",
            retryable=retryable, session_id=receipt.get("session_id"),
            resume_command=receipt.get("resume_command"), report=receipt.get("report"),
            overnight_until=receipt.get("overnight_until"),
            continuation_count=receipt.get("continuation_count"), failure_reason=reason,
        )
        if result.stdout:
            sys.stdout.write(result.stdout)
            sys.stdout.flush()
        if result.stderr:
            sys.stderr.write(result.stderr)
            sys.stderr.flush()
        if final_code == 0 or not retryable or number == len(MODEL_PRIORITY):
            break
        next_model, next_effort = MODEL_PRIORITY[number]
        record(root, "model-fallback", from_model=model, from_reasoning_effort=effort,
               to_model=next_model, to_reasoning_effort=next_effort, reason=reason)
    set_scheduler_state(root, scheduled_date,
                        "completed" if final_code == 0 else "failed",
                        final_code, final_model, final_effort)
    record(root, "manual-waiter-finished", exit_code=final_code,
           finished_at=local_now().isoformat(), prompt_file=str(prompt), day_index=day,
           scheduled_date=scheduled_date)
    return final_code


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT_PATH)
    parser.add_argument("--at", required=True, help="YYYY-MM-DD HH:MM in Asia/Shanghai")
    parser.add_argument("--prompt-file", required=True, type=Path)
    parser.add_argument("--day-index", default="auto")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--run-now", action="store_true",
                        help="catch up immediately after the target, only on the same date")
    args = parser.parse_args()

    try:
        root = args.root.resolve(strict=True)
        if root != ROOT_PATH or not RUNNER.is_file():
            raise RuntimeError(f"launcher requires a complete Wiki at {ROOT_PATH}")
        prompt = args.prompt_file if args.prompt_file.is_absolute() else root / args.prompt_file
        prompt = prompt.resolve(strict=True)
        prompt.relative_to(root)
        target = parse_target(args.at)
        now = local_now()
        day = current_day_index() if args.day_index == "auto" else int(args.day_index)
        if day != current_day_index():
            raise RuntimeError(f"requested day_index {day} does not match next_day_index {current_day_index()}")
        if not 1 <= day <= 30:
            raise RuntimeError("day_index must be between 1 and 30")
        if args.run_now and (target > now or target.date() != now.date()):
            raise RuntimeError("--run-now requires a missed target from today's Asia/Shanghai date")
        if target <= now and not args.run_now and not args.dry_run:
            raise RuntimeError("target has passed; use --run-now only after checking for a same-day run")
        run_date = now.date().isoformat() if args.run_now else target.date().isoformat()
        validate_prompt(prompt, run_date, day)
        commands = [command_for(root, prompt, day, model, effort) for model, effort in MODEL_PRIORITY]
        if args.dry_run:
            print(json.dumps({
                "status": "dry-run-ok", "now": now.isoformat(), "target": target.isoformat(),
                "timezone": str(TIMEZONE), "run_date": run_date, "day_index": day,
                "prompt_file": str(prompt), "daemon_lock": str(DEFAULT_LOCK_FILE),
                "would_run_now": args.run_now, "runner_commands": commands,
            }, ensure_ascii=False, indent=2))
            return 0
    except Exception as exc:
        print(f"manual daily-learning launcher error: {exc}", file=sys.stderr)
        return 2

    with DEFAULT_LOCK_FILE.open("a", encoding="utf-8") as lock_handle:
        try:
            fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            record(root, "manual-waiter-lock-blocked", target=target.isoformat())
            print("daily daemon already holds the single-instance lock", file=sys.stderr)
            return 75
        record(root, "manual-waiter-started", pid=os.getpid(),
               target=target.isoformat(), prompt_file=str(prompt), day_index=day)
        print(f"Waiting in foreground for {target.isoformat()} (Asia/Shanghai).", flush=True)
        heartbeat = time.monotonic() + 60
        runner_started = False
        try:
            while not args.run_now:
                now = local_now()
                if now.date() != target.date():
                    raise RuntimeError("target date passed while waiting; stale prompt was not launched")
                remaining = (target - now).total_seconds()
                if remaining <= 0:
                    break
                if time.monotonic() >= heartbeat:
                    record(root, "manual-waiter-heartbeat", now=now.isoformat(),
                           remaining_seconds=int(remaining), target=target.isoformat())
                    print(f"Still waiting; {int(remaining)} seconds remain.", flush=True)
                    heartbeat = time.monotonic() + 60
                time.sleep(min(10, remaining))
            now = local_now()
            if now.date() != target.date():
                raise RuntimeError("system resumed after target date; stale prompt was not launched")
            if current_day_index() != day:
                raise RuntimeError("next_day_index changed while waiting; stale prompt was not launched")
            validate_prompt(prompt, now.date().isoformat(), day)
            record(root, "manual-waiter-launch-due", started_at=now.isoformat(),
                   target=target.isoformat(), prompt_file=str(prompt), day_index=day)
            set_scheduler_state(root, target.date().isoformat(), "running")
            runner_started = True
            return run_profiles(root, prompt, day, target.date().isoformat())
        except KeyboardInterrupt:
            if runner_started:
                set_scheduler_state(root, target.date().isoformat(), "failed", 130)
            record(root, "manual-waiter-interrupted", target=target.isoformat(),
                   phase="runner" if runner_started else "waiting")
            print("manual daily-learning waiter interrupted", file=sys.stderr, flush=True)
            return 130
        except Exception as exc:
            if runner_started:
                set_scheduler_state(root, target.date().isoformat(), "failed", 1)
            record(root, "manual-waiter-error", target=target.isoformat(), error=str(exc))
            print(f"manual daily-learning launcher error: {exc}", file=sys.stderr)
            return 2


if __name__ == "__main__":
    raise SystemExit(main())
