#!/usr/bin/env python3
"""Hold the Wiki learning locks and queue timed reminders to one existing session.

This clock creates no Codex session and changes no course state or run receipt.
Queue exit 0 means accepted for queuing, not observed delivery. A timeout or a
restart during an in-flight call has an unknown outcome and is not resent.
Fresh Wiki-local Farmer cancellation/error markers stop this clock; Farmer
recovery markers temporarily reserve session recovery for Farmer alone.
The container and its Codex app server must remain available.
"""
from __future__ import annotations

import argparse
import fcntl
import json
import math
import os
import re
import signal
import subprocess
import sys
import tempfile
import time
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import date, datetime, time as daytime, timedelta
from pathlib import Path
from typing import Any, Callable, Iterator
from uuid import UUID
from zoneinfo import ZoneInfo


TIMEZONE = ZoneInfo("Asia/Shanghai")
LOCK_PATHS = (
    Path("/tmp/wiki-one-month-daily-learning-daemon.lock"),
    Path("/tmp/wiki-one-month-daily-learning.lock"),
)
HEARTBEAT_SECONDS = 60
QUEUE_TIMEOUT_SECONDS = 30
MAX_QUEUE_ATTEMPTS = 3
RETRY_SECONDS = (15, 30)
TERMINAL_EVENT_STATUSES = {"queued", "skipped", "exhausted", "unknown"}
FARMER_MAX_AGE_SECONDS = 120


@dataclass(frozen=True)
class SessionSpec:
    root: Path
    receipt: Path
    thread: str
    run_date: date
    day_index: int
    study_started_at: datetime
    deadline: datetime
    closeout_end: datetime
    checkpoint_hours: float
    receipt_status: str


@dataclass(frozen=True)
class ClockEvent:
    event_id: str
    kind: str
    at: datetime


@dataclass(frozen=True)
class QueueResult:
    returncode: int | None
    stdout: str = ""
    stderr: str = ""
    timed_out: bool = False


class LockBusy(RuntimeError):
    pass


def local_now() -> datetime:
    return datetime.now(TIMEZONE)


def no_symlinks(path: Path) -> None:
    """Reject links in all existing components before reading or writing a path."""
    cursor = Path(path.anchor)
    for part in path.parts[1:]:
        cursor /= part
        if cursor.is_symlink():
            raise ValueError(f"symlink is not allowed: {cursor}")


def aware_datetime(value: Any, field: str) -> datetime:
    if not isinstance(value, str):
        raise ValueError(f"{field} must be an ISO timestamp with an explicit timezone")
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"invalid {field}: {value}") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError(f"{field} must have an explicit timezone")
    return parsed.astimezone(TIMEZONE)


def read_object(path: Path) -> dict[str, Any]:
    no_symlinks(path)
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"JSON object required: {path}")
    return value


def load_spec(root: Path, receipt: Path, thread: str, checkpoint_hours: float) -> SessionSpec:
    if not math.isfinite(checkpoint_hours) or not 2 <= checkpoint_hours <= 3:
        raise ValueError("--checkpoint-hours must be between 2 and 3")
    try:
        if str(UUID(thread)) != thread:
            raise ValueError("--thread must be a canonical UUID")
    except (ValueError, AttributeError) as exc:
        raise ValueError("--thread must be a canonical UUID") from exc
    root = root.expanduser().absolute()
    no_symlinks(root)
    root = root.resolve(strict=True)
    if not all((root / item).exists() for item in ("README.md", ".git", "knowledge")):
        raise ValueError(f"incomplete Wiki root: {root}")
    if ".." in receipt.parts:
        raise ValueError("receipt path must not contain ..")
    receipt = receipt if receipt.is_absolute() else root / receipt
    no_symlinks(receipt)
    receipt = receipt.resolve(strict=True)
    try:
        relative = receipt.relative_to(root / "outputs" / "learning-daily")
    except ValueError as exc:
        raise ValueError("receipt must be inside root/outputs/learning-daily/<run>/run.json") from exc
    if (len(relative.parts) != 2 or relative.name != "run.json"
            or not re.search(r"-run-\d+$", relative.parts[0])):
        raise ValueError("receipt must be root/outputs/learning-daily/<name>-run-N/run.json")
    document = read_object(receipt)
    if document.get("session_id") != thread:
        raise ValueError("--thread must equal receipt.session_id")
    if document.get("project_root", str(root)) != str(root):
        raise ValueError("receipt.project_root does not match --root")
    run_date = date.fromisoformat(document["run_date"])
    day_index = document.get("day_index")
    if type(day_index) is not int or not 1 <= day_index <= 30:
        raise ValueError("receipt.day_index must be an integer in 1..30")
    deadline = aware_datetime(document.get("overnight_until"), "overnight_until")
    expected = datetime.combine(run_date + timedelta(days=1), daytime(15), tzinfo=TIMEZONE)
    if deadline != expected:
        raise ValueError("overnight_until must equal run_date + 1 day at 15:00 Asia/Shanghai")
    closeout_end = deadline + timedelta(hours=1)
    if document.get("closeout_window_ends_at") is not None:
        if aware_datetime(document["closeout_window_ends_at"], "closeout_window_ends_at") != closeout_end:
            raise ValueError("closeout_window_ends_at must equal overnight_until + 1 hour")
    started = aware_datetime(document.get("started_at"), "started_at")
    if started.date() != run_date or started >= deadline:
        raise ValueError("started_at must belong to run_date and precede the deadline")
    return SessionSpec(root, receipt, thread, run_date, day_index, started, deadline,
                       closeout_end, checkpoint_hours, str(document.get("status", "unknown")))


def plan_events(spec: SessionSpec) -> list[ClockEvent]:
    events = []
    interval = timedelta(hours=spec.checkpoint_hours)
    index = 1
    while spec.study_started_at + index * interval < spec.deadline:
        events.append(ClockEvent(f"checkpoint-{index:03d}", "checkpoint", spec.study_started_at + index * interval))
        index += 1
    events += [
        ClockEvent("closeout", "closeout", spec.deadline),
        ClockEvent("closeout-reminder", "closeout-reminder", spec.deadline + timedelta(minutes=45)),
        ClockEvent("overdue", "overdue", spec.closeout_end),
    ]
    return events


def message_for(spec: SessionSpec, event: ClockEvent, now: datetime) -> str:
    prefix = (f"[Wiki clock {event.event_id}] Day {spec.day_index}; "
              f"queued_snapshot_at={now.astimezone(TIMEZONE).isoformat()}; "
              f"research cutoff={spec.deadline.isoformat()}. ")
    delivery = ("Read run.json first; if completed, record delivery only. "
                "Ack this ID in observed_clock_executions; refresh actual time. ")
    boundary = (f"Keep day_index={spec.day_index}. "
                f"Day {spec.day_index + 1} may only be an uncredited preview in partial_day_indices; "
                f"do not credit it or open Day {spec.day_index + 2}. "
                if spec.day_index < 30 else "Keep day_index=30; do not open another course card. ")
    if event.kind == "checkpoint":
        action = ("Continue the existing task in this same session. Refresh the clock, candidate pool, "
                  "evidence gaps, source locators and information gain; save a recoverable checkpoint "
                  "in this run's files. Card completion is not the end of this study window. "
                  "With under 90 minutes left, finish current analysis without new sources/cards. ")
    elif event.kind == "closeout":
        action = ("The research cutoff has arrived. Stop all new research now and use the reserved "
                  "15:00-16:00 hour for the daily report, canonical knowledge writeback, card audit, "
                  "runner validation, receipt, next-day plan prompt and authorized publication. "
                  "Advance course state only after validation and publication gates pass. ")
    elif event.kind == "closeout-reminder":
        action = ("The run receipt is not completed at 15:45. Perform bounded closeout only: "
                  "finish checks, next-day plan prompt, publication and an honest resumable receipt "
                  "before 16:00. Keep unresolved items explicit; stop adding research. ")
    else:
        action = ("The reserved closeout hour has ended and the run receipt remains incomplete. "
                  "Record the overdue/partial state and exact resume command; do not invent completion "
                  "or advance the course. This clock will release its locks and stop. ")
    message = prefix + delivery + action + boundary + "Do not create a new session or restart a daemon from this reminder."
    if len(message.encode("utf-8")) >= 1000:
        raise ValueError("clock message must be under 1000 UTF-8 bytes")
    return message


def queue_command(spec: SessionSpec, message: str) -> list[str]:
    return ["codex", "-C", str(spec.root), "queue", "--thread", spec.thread, "--message", message]


def output_text(value: str | bytes | None) -> str:
    if isinstance(value, bytes):
        value = value.decode("utf-8", errors="replace")
    return (value or "")[-2000:]


def queue_message(command: list[str], timeout: int) -> QueueResult:
    try:
        result = subprocess.run(command, text=True, capture_output=True, check=False, timeout=timeout)
        return QueueResult(result.returncode, output_text(result.stdout), output_text(result.stderr))
    except subprocess.TimeoutExpired as exc:
        return QueueResult(None, output_text(exc.stdout), output_text(exc.stderr), timed_out=True)
    except OSError as exc:
        return QueueResult(None, stderr=str(exc))


@contextmanager
def acquire_locks(paths: tuple[Path, ...] = LOCK_PATHS) -> Iterator[None]:
    handles = []
    try:
        for path in paths:
            no_symlinks(path)
            handle = path.open("a", encoding="utf-8")
            handles.append(handle)
            try:
                fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError as exc:
                raise LockBusy(f"learning lock is already held: {path}") from exc
        yield
    finally:
        for handle in reversed(handles):
            handle.close()


def write_atomic(path: Path, value: dict[str, Any]) -> None:
    no_symlinks(path)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        Path(temporary).unlink(missing_ok=True)


def identity(spec: SessionSpec) -> dict[str, Any]:
    return {"receipt": str(spec.receipt), "thread": spec.thread, "run_date": spec.run_date.isoformat(),
            "day_index": spec.day_index, "study_started_at": spec.study_started_at.isoformat(),
            "deadline": spec.deadline.isoformat(), "closeout_end": spec.closeout_end.isoformat(),
            "checkpoint_hours": spec.checkpoint_hours}


def first_clock_start(state: dict[str, Any], events_path: Path, thread: str,
                      now: datetime) -> tuple[datetime, str]:
    """Keep the first actual clock start, including migration of existing clocks."""
    if state.get("first_supervisor_started_at") is not None:
        return aware_datetime(state["first_supervisor_started_at"], "first_supervisor_started_at"), "persisted"
    candidates = []
    if state.get("supervisor_started_at") is not None:
        candidates.append(aware_datetime(state["supervisor_started_at"], "supervisor_started_at"))
    no_symlinks(events_path)
    if events_path.is_file():
        with events_path.open(encoding="utf-8") as handle:
            for line in handle:
                try:
                    item = json.loads(line)
                    if (isinstance(item, dict) and item.get("event") == "clock-started"
                            and item.get("thread") == thread):
                        candidates.append(aware_datetime(item.get("timestamp"), "clock-started timestamp"))
                        break
                except (ValueError, TypeError):
                    continue
    return (min(candidates), "legacy-start-records") if candidates else (now, "first-start")


def farmer_snapshot(spec: SessionSpec, first_started_at: datetime, now: datetime) -> dict[str, Any]:
    """Read only root/tmp/farmer/state.json, matching wiki_farmer.runtime_paths."""
    path = spec.root / "tmp" / "farmer" / "state.json"
    result: dict[str, Any] = {"path": str(path), "observation": "unknown", "action": "continue",
                              "status": None, "event_at": None, "reason": "snapshot-missing"}
    try:
        no_symlinks(path)
        age = now.timestamp() - path.stat().st_mtime
        result["file_age_seconds"] = age
        if age > FARMER_MAX_AGE_SECONDS:
            return {**result, "observation": "ignored", "reason": "snapshot-stale"}
        if age < -5:
            return {**result, "reason": "snapshot-from-future"}
        states = read_object(path)
        record = states.get(spec.thread)
        if not isinstance(record, dict):
            return {**result, "reason": "thread-missing"}
        status = record.get("status")
        if not isinstance(status, str):
            raise ValueError("Farmer thread status is not a string")
        event_at = aware_datetime(record.get("last_event_timestamp"), "Farmer last_event_timestamp")
        result.update(status=status, event_at=event_at.isoformat())
        if event_at < first_started_at:
            return {**result, "observation": "ignored", "reason": "event-before-clock-start"}
        action = {"cancelled": "stop-cancelled", "manual-attention-required": "stop-manual",
                  "recovery-pending": "pause", "waiting-retry": "pause"}.get(status, "continue")
        return {**result, "observation": "observed", "action": action, "reason": "fresh-thread-event"}
    except FileNotFoundError:
        return result
    except (OSError, ValueError, TypeError) as exc:
        return {**result, "reason": "snapshot-unreadable", "error": str(exc)[:400]}


class Supervisor:
    def __init__(self, spec: SessionSpec, *, clock: Callable[[], datetime] = local_now,
                 queue: Callable[[list[str], int], QueueResult] = queue_message,
                 sleeper: Callable[[float], None] = time.sleep):
        self.spec, self.clock, self.queue, self.sleeper = spec, clock, queue, sleeper
        self.events = plan_events(spec)
        self.state_path = spec.receipt.parent / "clock-state.json"
        self.events_path = spec.receipt.parent / "clock-events.jsonl"
        no_symlinks(self.events_path)
        self.state = read_object(self.state_path) if self.state_path.exists() else {
            "schema_version": 1, **identity(spec), "sent_event_ids": [],
            "events": {event.event_id: {"status": "pending", "attempts": 0} for event in self.events},
            "queue_success_semantics": "exit 0 means queued; delivery has not been observed",
        }
        if any(self.state.get(key) != value for key, value in identity(spec).items()):
            raise ValueError("clock state identity differs from the receipt or requested schedule")
        records, sent = self.state.get("events"), self.state.get("sent_event_ids")
        if (not isinstance(records, dict) or set(records) != {event.event_id for event in self.events}
                or not isinstance(sent, list) or any(not isinstance(item, str) for item in sent)
                or len(sent) != len(set(sent))):
            raise ValueError("invalid clock event ledger; refusing to risk duplicate reminders")
        for record in records.values():
            if (not isinstance(record, dict) or type(record.get("attempts")) is not int
                    or not 0 <= record["attempts"] <= MAX_QUEUE_ATTEMPTS
                    or record.get("status") not in TERMINAL_EVENT_STATUSES | {"pending", "retry-wait", "in-flight"}):
                raise ValueError("invalid clock event record")
        if set(sent) != {key for key, record in records.items() if record["status"] == "queued"}:
            raise ValueError("sent_event_ids disagrees with queued event records")

    def log(self, kind: str, **fields: Any) -> None:
        no_symlinks(self.events_path)
        item = {"timestamp": self.clock().astimezone(TIMEZONE).isoformat(), "event": kind, **fields}
        with self.events_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(item, ensure_ascii=False) + "\n")
            handle.flush()

    def save(self) -> None:
        write_atomic(self.state_path, self.state)

    def start(self) -> None:
        restarted = self.state_path.exists()
        now = self.clock().astimezone(TIMEZONE)
        first_started, origin = first_clock_start(self.state, self.events_path, self.spec.thread, now)
        self.state["first_supervisor_started_at"] = first_started.isoformat()
        self.state.setdefault("first_start_origin", origin)
        self.state.update({"status": "running", "pid": os.getpid(),
                           "supervisor_started_at": now.isoformat(),
                           "session_execution_observed": False})
        for event_id, record in self.state["events"].items():
            if record["status"] == "in-flight":
                record.update(status="unknown", reason="restart during queue call; acceptance unknown; not resent")
                self.log("queue-outcome-unknown", event_id=event_id, reason=record["reason"])
        self.save()
        self.log("clock-resumed" if restarted else "clock-started", **identity(self.spec))

    def farmer_control(self, now: datetime) -> str:
        first_started = aware_datetime(self.state["first_supervisor_started_at"], "first_supervisor_started_at")
        observation = farmer_snapshot(self.spec, first_started, now)
        previous = self.state.get("farmer_observation") or {}
        keys = ("observation", "action", "status", "event_at", "reason")
        self.state["farmer_observation"] = observation
        self.state["queue_paused"] = observation["action"] == "pause"
        if any(previous.get(key) != observation.get(key) for key in keys):
            self.log("farmer-observed", **observation)
        if observation["action"] == "stop-cancelled":
            self.finish("interrupted", "fresh Farmer cancellation; no automatic continuation")
        elif observation["action"] == "stop-manual":
            self.finish("manual-attention-required", "fresh Farmer terminal error; no automatic continuation")
        return observation["action"]

    def heartbeat(self, now: datetime, receipt_status: str) -> None:
        phase = ("waiting-for-recorded-study-start" if now < self.spec.study_started_at
                 else "study-window" if now < self.spec.deadline
                 else "closeout-window" if now < self.spec.closeout_end else "window-ended")
        self.state.update(heartbeat_at=now.isoformat(), phase=phase, receipt_status=receipt_status)
        self.save()
        self.log("clock-heartbeat", phase=phase, receipt_status=receipt_status,
                 session_execution_observed=False)

    def skip(self, event: ClockEvent, reason: str) -> None:
        record = self.state["events"][event.event_id]
        if record["status"] not in TERMINAL_EVENT_STATUSES:
            record.update(status="skipped", reason=reason)
            self.save()
            self.log("reminder-skipped", event_id=event.event_id, reason=reason)

    def completed_receipt(self, current: SessionSpec) -> bool:
        """Final run completion ends delivery; card completion stays running."""
        if current.receipt_status != "completed":
            return False
        self.heartbeat(self.clock().astimezone(TIMEZONE), current.receipt_status)
        for event in self.events:
            self.skip(event, "run receipt completed; no new queued messages")
        self.finish("completed", "run receipt completed; reminder delivery stopped")
        return True

    def pending_checkpoints(self) -> list[str]:
        """Keep at most one unacknowledged routine reminder in the broker."""
        entries = read_object(self.spec.receipt).get("observed_clock_executions", [])
        acknowledged: set[str] = set()
        if isinstance(entries, list):
            for entry in entries:
                if (isinstance(entry, dict)
                        and isinstance(entry.get("clock_event_id"), str)
                        and entry.get("same_session_id", self.spec.thread) == self.spec.thread):
                    acknowledged.add(entry["clock_event_id"])
        pending = []
        for event in self.events:
            if event.kind != "checkpoint":
                continue
            record = self.state["events"][event.event_id]
            if event.event_id in acknowledged:
                record["delivery_observed"] = True
            elif record["status"] in {"queued", "unknown"}:
                pending.append(event.event_id)
        self.state["pending_checkpoint_ids"] = pending
        self.save()
        return pending

    def attempt(self, event: ClockEvent, now: datetime, receipt_status: str) -> None:
        record = self.state["events"][event.event_id]
        if record["status"] in TERMINAL_EVENT_STATUSES:
            return
        if record["status"] == "retry-wait" and now < aware_datetime(record["next_at"], "next_at"):
            return
        maximum = 1 if event.kind == "overdue" else MAX_QUEUE_ATTEMPTS
        if record["attempts"] >= maximum:
            record.update(status="exhausted", reason="bounded queue attempts exhausted")
            self.save()
            return
        if self.farmer_control(self.clock().astimezone(TIMEZONE)) != "continue":
            self.save()
            return
        current = load_spec(self.spec.root, self.spec.receipt, self.spec.thread, self.spec.checkpoint_hours)
        if identity(current) != identity(self.spec):
            raise ValueError("receipt timing or identity changed before queue call")
        if self.completed_receipt(current):
            return
        if event.kind == "checkpoint":
            pending = self.pending_checkpoints()
            if pending:
                self.skip(event, "unacknowledged checkpoint already queued; coalesced")
                self.log("checkpoint-coalesced", event_id=event.event_id, pending_event_ids=pending)
                return
        command = queue_command(self.spec, message_for(self.spec, event, now))
        record.update(status="in-flight", attempts=record["attempts"] + 1, attempted_at=now.isoformat())
        self.save()
        self.log("queue-attempt-started", event_id=event.event_id, attempt=record["attempts"])
        result = self.queue(command, QUEUE_TIMEOUT_SECONDS)
        finished = self.clock().astimezone(TIMEZONE)
        outcome = {"attempt": record["attempts"], "finished_at": finished.isoformat(),
                   "returncode": result.returncode, "timed_out": result.timed_out,
                   "stdout": output_text(result.stdout), "stderr": output_text(result.stderr)}
        record.setdefault("attempt_history", []).append(outcome)
        if result.timed_out:
            record.update(status="unknown", reason="queue timed out; acceptance unknown; not resent")
        elif result.returncode == 0:
            record.update(status="queued", queued_at=finished.isoformat(), delivery_observed=False)
            self.state["sent_event_ids"].append(event.event_id)
        elif record["attempts"] >= maximum:
            record.update(status="exhausted", reason="bounded queue attempts exhausted")
        else:
            record.update(status="retry-wait", next_at=(finished + timedelta(seconds=RETRY_SECONDS[record["attempts"] - 1])).isoformat())
        self.save()
        self.log("queue-result", event_id=event.event_id, status=record["status"], **outcome)
        self.heartbeat(finished, receipt_status)

    def tick(self) -> bool:
        now = self.clock().astimezone(TIMEZONE)
        current = load_spec(self.spec.root, self.spec.receipt, self.spec.thread, self.spec.checkpoint_hours)
        if identity(current) != identity(self.spec):
            raise ValueError("receipt timing or identity changed while the clock was running")
        if self.completed_receipt(current):
            return False
        if current.receipt_status in {"stopped", "cancelled", "interrupted"}:
            self.heartbeat(now, current.receipt_status)
            self.finish("interrupted", f"run receipt records {current.receipt_status}; no automatic restart")
            return False
        control = self.farmer_control(now)
        if control.startswith("stop-"):
            return False
        self.heartbeat(now, current.receipt_status)
        if control == "pause":
            if now >= self.spec.closeout_end:
                for event in self.events:
                    self.skip(event, "closeout hour ended while Farmer owns recovery; no clock queue")
                self.finish("window-ended", "closeout hour ended during Farmer recovery")
                return False
            return True
        checkpoints = [event for event in self.events if event.kind == "checkpoint" and event.at <= now]
        latest = checkpoints[-1] if checkpoints and now < self.spec.deadline else None
        for event in checkpoints:
            if event != latest:
                self.skip(event, "missed checkpoint superseded; no catch-up burst" if latest else "research cutoff reached")
        for event in self.events:
            if event.at > now or event.kind == "checkpoint" and event != latest:
                continue
            if now >= self.spec.closeout_end and event.kind != "overdue":
                self.skip(event, "closeout hour ended; only one overdue reminder is permitted")
                continue
            if event.kind in {"closeout-reminder", "overdue"} and current.receipt_status == "completed":
                self.skip(event, "run receipt is completed")
                continue
            self.attempt(event, now, current.receipt_status)
            if self.state["status"] != "running":
                return False
            if self.state.get("queue_paused"):
                break
        if now >= self.spec.closeout_end:
            self.finish("window-ended", "reserved closeout hour ended")
            return False
        return True

    def sleep_seconds(self) -> float:
        now = self.clock().astimezone(TIMEZONE)
        times = [self.spec.closeout_end]
        if self.state.get("heartbeat_at"):
            times.append(aware_datetime(self.state["heartbeat_at"], "heartbeat_at")
                         + timedelta(seconds=HEARTBEAT_SECONDS))
        for event in self.events:
            if self.state.get("queue_paused"):
                break
            record = self.state["events"][event.event_id]
            if record["status"] not in TERMINAL_EVENT_STATUSES:
                times.append(aware_datetime(record["next_at"], "next_at") if record["status"] == "retry-wait" else event.at)
        return min(HEARTBEAT_SECONDS, max(0.1, min((at - now).total_seconds() for at in times)))

    def finish(self, status: str, reason: str) -> None:
        self.state.update(status=status, stop_reason=reason, stopped_at=self.clock().astimezone(TIMEZONE).isoformat(),
                          notification_errors=[key for key, record in self.state["events"].items()
                                               if record["status"] in {"unknown", "exhausted"}])
        self.save()
        self.log("clock-stopped", status=status, reason=reason,
                 notification_errors=self.state["notification_errors"])

    def run(self, stop: dict[str, int | None]) -> int:
        self.start()
        while not stop["signal"]:
            keep_running = self.tick()
            if stop["signal"]:
                break
            if not keep_running:
                if self.state["status"] == "completed":
                    return 0
                if self.state["status"] == "interrupted":
                    return 130
                if self.state["status"] == "manual-attention-required":
                    return 3
                return 1 if self.state["notification_errors"] else 0
            self.sleeper(self.sleep_seconds())
        self.finish("interrupted", f"received signal {stop['signal']}")
        return 128 + int(stop["signal"])


def dry_run(spec: SessionSpec) -> dict[str, Any]:
    return {"status": "dry-run", **identity(spec), "locks": [str(path) for path in LOCK_PATHS],
            "command_shape": queue_command(spec, "<one reminder under 1000 UTF-8 bytes>"),
            "events": [{"id": event.event_id, "kind": event.kind, "at": event.at.isoformat()}
                       for event in plan_events(spec)],
            "heartbeat_seconds": HEARTBEAT_SECONDS, "queue_timeout_seconds": QUEUE_TIMEOUT_SECONDS,
            "queue_max_attempts": MAX_QUEUE_ATTEMPTS,
            "farmer_snapshot": str(spec.root / "tmp/farmer/state.json"),
            "farmer_max_age_seconds": FARMER_MAX_AGE_SECONDS,
            "delivery_boundary": "Queue acceptance is not observed delivery; requires a live container/app server."}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--thread", required=True)
    parser.add_argument("--checkpoint-hours", type=float, default=2)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    supervisor = None
    previous_handlers = {}
    try:
        spec = load_spec(args.root, args.receipt, args.thread, args.checkpoint_hours)
        if args.dry_run:
            print(json.dumps(dry_run(spec), ensure_ascii=False, indent=2))
            return 0
        stop: dict[str, int | None] = {"signal": None}
        for signum in (signal.SIGTERM, signal.SIGINT):
            previous_handlers[signum] = signal.signal(signum, lambda received, _frame: stop.update(signal=received))
        with acquire_locks(LOCK_PATHS):
            supervisor = Supervisor(spec)
            try:
                result = supervisor.run(stop)
            except (OSError, ValueError, KeyError, TypeError) as exc:
                supervisor.finish("failed", str(exc))
                raise
            print(json.dumps({"status": supervisor.state["status"], "clock_state": str(supervisor.state_path),
                              "notification_errors": supervisor.state.get("notification_errors", [])}))
            return result
    except LockBusy as exc:
        print(json.dumps({"status": "overlap-blocked", "error": str(exc)}), file=sys.stderr)
        return 75
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"status": "clock-error", "error": str(exc)}), file=sys.stderr)
        return 2
    finally:
        for signum, handler in previous_handlers.items():
            signal.signal(signum, handler)


if __name__ == "__main__":
    raise SystemExit(main())
