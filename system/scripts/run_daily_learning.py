#!/usr/bin/env python3
"""Run one unattended daily learning turn inside the Wiki Docker container.

The runner owns execution bookkeeping only. Scientific content decisions remain in
the Codex prompt and repository workflows. It never stages or commits files.
"""

from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

from wiki_knowledge_writeback import snapshot_knowledge, validate_writeback


TIMEZONE = ZoneInfo("Asia/Shanghai")
TOTAL_DAYS = 30
CYCLE_NAME = "2026-09-30-day-substantive"
SESSION_MODE = "new-session-per-run"
PHASES = (
    (1, 1, "baseline-and-research-contract"),
    (2, 10, "nuclear-structure-framework"),
    (11, 14, "gamma-spectroscopy-and-level-schemes"),
    (15, 17, "angular-correlation-polarization-and-mixing-ratio"),
    (18, 20, "lifetimes-strengths-and-deformation"),
    (21, 21, "experimental-evidence-exam"),
    (22, 23, "wobbling-and-signature-partners"),
    (24, 25, "chirality-and-shape-coexistence"),
    (26, 26, "octupole-and-magnetic-rotation"),
    (27, 27, "cross-mass-region-comparison"),
    (28, 28, "independent-l3-research"),
    (29, 29, "research-design-defense"),
    (30, 30, "final-exam-and-prospectus"),
)

# The runner itself is already inside the isolated Wiki Docker container. A
# nested workspace-write sandbox would invoke bubblewrap again and fails on the
# current container kernel, so the child Codex process uses the container's
# explicit full-access mode while retaining approval mode `never` and the
# prompt's `/workspace/wiki` boundary.
CODEX_SANDBOX = "danger-full-access"

REQUIRED_REPORT_HEADINGS = (
    "## Run state",
    "## Candidate pool and selection",
    "## Sources and evidence",
    "## Theory/analysis exercise",
    "## Counter-evidence and missing companion observables",
    "## Knowledge Impact and Learning Decision",
    "## Durable knowledge delta",
    "## Open questions and belief revision",
    "## L0–L4 state",
    "## Verification and continuation",
)
@dataclass(frozen=True)
class Paths:
    root: Path
    daily_root: Path
    state_file: Path
    prompt_file: Path
    lock_file: Path


def phase_for_day(day_index: int) -> str:
    if not 1 <= day_index <= TOTAL_DAYS:
        raise ValueError(f"day_index must be in 1..{TOTAL_DAYS}")
    for first, last, phase in PHASES:
        if first <= day_index <= last:
            return phase
    raise AssertionError("phase table does not cover day_index")


def validate_root(root: Path) -> None:
    required = (root / "README.md", root / "knowledge", root / ".git")
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise RuntimeError("Wiki root is incomplete: " + ", ".join(missing))


def validate_codex_home() -> Path:
    codex_home = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))).expanduser()
    if not codex_home.is_dir():
        raise RuntimeError(f"CODEX_HOME is not a directory: {codex_home}")
    if not os.access(codex_home, os.R_OK | os.W_OK):
        raise RuntimeError(f"CODEX_HOME is not readable and writable: {codex_home}")
    return codex_home


def build_resume_command(root: Path, session_id: str) -> list[str]:
    """Build the explicit command for discussing or resuming one daily run."""

    if not session_id.strip():
        raise ValueError("session_id must be non-empty")
    return [
        "codex",
        "resume",
        session_id,
        "-C",
        str(root),
        "-s",
        CODEX_SANDBOX,
        "-a",
        "never",
    ]


def get_paths(root: Path) -> Paths:
    return Paths(
        root=root,
        daily_root=root / "outputs" / "learning-daily",
        state_file=root / "outputs" / "learning-milestones" / "2026-09-one-month-state.json",
        prompt_file=root / "system" / "prompts" / "daily-learning.md",
        lock_file=Path("/tmp/wiki-one-month-daily-learning.lock"),
    )


def local_date() -> str:
    return datetime.now(TIMEZONE).date().isoformat()


def read_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {
            "schema_version": 1,
            "cycle": CYCLE_NAME,
            "counting_policy": "30 successful substantive days; acceptance-only runs are excluded",
            "next_day_index": 1,
            "last_success": None,
            "last_run_id": None,
            "status": "not-started",
        }
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"cannot read state file {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise RuntimeError(f"state file must contain an object: {path}")
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


def next_run_number(daily_root: Path, run_date: str) -> int:
    pattern = re.compile(rf"^{re.escape(run_date)}-run-(\d+)$")
    numbers = []
    for child in daily_root.glob(f"{run_date}-run-*"):
        match = pattern.match(child.name)
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers, default=0) + 1


def extract_session_id(lines: list[str]) -> str | None:
    for line in lines:
        try:
            value = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(value, dict):
            continue
        for key in ("thread_id", "threadId", "session_id", "sessionId"):
            candidate = value.get(key)
            if isinstance(candidate, str) and candidate:
                return candidate
        nested = value.get("thread")
        if isinstance(nested, dict):
            candidate = nested.get("id")
            if isinstance(candidate, str) and candidate:
                return candidate
    return None


def extract_failure_reason(lines: list[str]) -> str | None:
    messages: list[str] = []
    for line in lines:
        try:
            value = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(value, dict) or value.get("type") not in {"error", "turn.failed"}:
            continue
        error = value.get("error")
        if isinstance(error, dict) and isinstance(error.get("message"), str):
            messages.append(error["message"])
        elif isinstance(error, str):
            messages.append(error)
        if isinstance(value.get("message"), str):
            messages.append(value["message"])
    return " | ".join(messages) if messages else None


def build_command(
    root: Path,
    model: str,
    last_message: Path,
    enable_search: bool,
    reasoning_effort: str | None = None,
) -> list[str]:
    command = [
        "codex",
        "-C",
        str(root),
        "-m",
        model,
        "-s",
        CODEX_SANDBOX,
        "-a",
        "never",
    ]
    if reasoning_effort:
        command += ["-c", f"model_reasoning_effort={reasoning_effort}"]
    if enable_search:
        command.append("--search")
    command += ["exec", "--json", "-o", str(last_message), "-"]
    return command


def report_signature(path: Path) -> str | None:
    if not path.is_file():
        return None
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return None


def validate_report(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {"valid": False, "missing_headings": list(REQUIRED_REPORT_HEADINGS)}
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return {"valid": False, "missing_headings": list(REQUIRED_REPORT_HEADINGS)}
    missing = [heading for heading in REQUIRED_REPORT_HEADINGS if heading not in text]
    return {"valid": bool(text.strip()) and not missing, "missing_headings": missing}


def validate_durable_knowledge(
    report_path: Path,
    root: Path,
    knowledge_before: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Validate the structured report-to-knowledge writeback contract."""

    return validate_writeback(
        report_path,
        root,
        before=knowledge_before,
        allow_not_applicable=False,
    )


def run_preflight(root: Path) -> dict[str, Any]:
    result = subprocess.run(
        [sys.executable, "system/scripts/wiki_automation_preflight.py", "--root", str(root)],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "exit": result.returncode,
        "stdout_tail": result.stdout[-3000:],
        "stderr_tail": result.stderr[-1000:],
    }


def render_prompt(paths: Paths, run_id: str, run_date: str, day_index: int) -> str:
    phase = phase_for_day(day_index)
    template = paths.prompt_file.read_text(encoding="utf-8")
    substitutions = {
        "{{RUN_ID}}": run_id,
        "{{RUN_DATE}}": run_date,
        "{{DAY_INDEX}}": str(day_index),
        "{{PHASE}}": phase,
        "{{OUTPUT_DIR}}": str(paths.daily_root / f"{run_date}-run-{run_id.rsplit('-', 1)[-1]}"),
        "{{STATE_FILE}}": str(paths.state_file),
    }
    for old, new in substitutions.items():
        template = template.replace(old, new)
    return template


def run_checks(
    root: Path,
    report_path: Path,
    report_before: str | None = None,
    knowledge_before: dict[str, str] | None = None,
) -> dict[str, Any]:
    preflight = run_preflight(root)
    lint = subprocess.run(
        [sys.executable, "system/scripts/wiki_lint.py", "--fail-on", "error", "--no-git"],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )
    diff = subprocess.run(
        ["git", "diff", "--check"], cwd=root, text=True, capture_output=True, check=False
    )
    report_after = report_signature(report_path)
    report_validation = validate_report(report_path)
    durable_knowledge = validate_durable_knowledge(report_path, root, knowledge_before)
    return {
        "preflight": preflight,
        "report_exists": report_path.is_file(),
        "report_changed": report_after is not None and report_after != report_before,
        "report_valid": report_validation["valid"],
        "report_missing_headings": report_validation["missing_headings"],
        "durable_knowledge": durable_knowledge,
        "lint_exit": lint.returncode,
        "lint_tail": lint.stdout[-2000:] if lint.stdout else lint.stderr[-2000:],
        "git_diff_check_exit": diff.returncode,
        "git_diff_check_tail": diff.stdout[-1000:] + diff.stderr[-1000:],
    }


def dry_run(
    paths: Paths,
    model: str,
    enable_search: bool,
    reasoning_effort: str | None = None,
) -> dict[str, Any]:
    validate_root(paths.root)
    codex_home = validate_codex_home()
    if shutil.which("codex") is None:
        raise RuntimeError("codex executable was not found in PATH")
    if not paths.prompt_file.is_file():
        raise RuntimeError(f"prompt file is missing: {paths.prompt_file}")
    state = read_state(paths.state_file)
    day_index = int(state.get("next_day_index", 1))
    run_date = local_date()
    run_id = f"dry-run-{run_date}-day-{day_index:02d}"
    cycle_complete = state.get("status") == "complete" or day_index > TOTAL_DAYS
    return {
        "status": "cycle-complete" if cycle_complete else "dry-run-ok",
        "root": str(paths.root),
        "codex": shutil.which("codex"),
        "codex_home": str(codex_home),
        "session_mode": SESSION_MODE,
        "day_index": day_index,
        "phase": None if cycle_complete else phase_for_day(day_index),
        "command": build_command(
            paths.root,
            model,
            paths.daily_root / "last-message.md",
            enable_search,
            reasoning_effort,
        ),
        "state_file": str(paths.state_file),
        "run_id": run_id,
        "cycle_complete": cycle_complete,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--day-index", default="auto")
    parser.add_argument("--mode", choices=["daily-learning"], default="daily-learning")
    parser.add_argument("--model", default="gpt-5.6-sol")
    parser.add_argument("--reasoning-effort", choices=["low", "medium", "high", "max"], default=None)
    parser.add_argument("--no-search", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    paths = get_paths(root)
    try:
        result = dry_run(paths, args.model, not args.no_search, args.reasoning_effort)
        if args.dry_run:
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return 0
        validate_root(root)
        state = read_state(paths.state_file)
        day_index = int(state.get("next_day_index", 1)) if args.day_index == "auto" else int(args.day_index)
        if state.get("status") == "complete" or day_index > TOTAL_DAYS:
            print(
                json.dumps(
                    {
                        "status": "cycle-complete",
                        "cycle": CYCLE_NAME,
                        "counting_policy": "30 successful substantive days; acceptance-only runs are excluded",
                        "next_day_index": day_index,
                    },
                    ensure_ascii=False,
                    indent=2,
                )
            )
            return 0
        phase = phase_for_day(day_index)
        run_date = local_date()
        run_number = next_run_number(paths.daily_root, run_date)
        run_id = f"{run_date}-day-{day_index:02d}-{run_number:02d}"
        run_dir = paths.daily_root / f"{run_date}-run-{run_number:02d}"
        run_dir.mkdir(parents=True, exist_ok=False)
        report_path = paths.daily_root / f"{run_date}.md"
        report_before = report_signature(report_path)
        events_path = run_dir / "events.jsonl"
        stderr_path = run_dir / "stderr.log"
        last_message = run_dir / "last-message.md"
        receipt = {
            "schema_version": 1,
            "run_id": run_id,
            "run_date": run_date,
            "day_index": day_index,
            "phase": phase,
            "cycle": CYCLE_NAME,
            "run_kind": "substantive",
            "counted_in_substantive_test": True,
            "session_mode": SESSION_MODE,
            "session_reuse": False,
            "codex_home": str(validate_codex_home()),
            "status": "running",
            "started_at": datetime.now(TIMEZONE).isoformat(),
            "report": str(report_path),
        }
        write_json_atomic(run_dir / "run.json", receipt)
        with paths.lock_file.open("w", encoding="utf-8") as lock_handle:
            try:
                fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                receipt.update({"status": "overlap-blocked", "exit_code": 75})
                write_json_atomic(run_dir / "run.json", receipt)
                print(json.dumps(receipt, ensure_ascii=False, indent=2))
                return 75
            preflight = run_preflight(root)
            if preflight["exit"] != 0:
                receipt.update(
                    {
                        "status": "safe-suspended-preflight",
                        "preflight": preflight,
                        "exit_code": preflight["exit"],
                        "finished_at": datetime.now(TIMEZONE).isoformat(),
                    }
                )
                write_json_atomic(run_dir / "run.json", receipt)
                print(json.dumps(receipt, ensure_ascii=False, indent=2))
                return 3
            knowledge_before = snapshot_knowledge(root)
            prompt = render_prompt(paths, run_id, run_date, day_index)
            command = build_command(
                root,
                args.model,
                last_message,
                not args.no_search,
                args.reasoning_effort,
            )
            with events_path.open("w", encoding="utf-8") as events, stderr_path.open(
                "w", encoding="utf-8"
            ) as stderr:
                process = subprocess.run(
                    command,
                    cwd=root,
                    input=prompt,
                    text=True,
                    stdout=events,
                    stderr=stderr,
                    check=False,
                )
            lines = events_path.read_text(encoding="utf-8", errors="replace").splitlines()
            checks = run_checks(root, report_path, report_before, knowledge_before)
            success = (
                process.returncode == 0
                and checks["preflight"]["exit"] == 0
                and checks["report_exists"]
                and checks["report_changed"]
                and checks["report_valid"]
                and checks["durable_knowledge"]["valid"]
                and checks["lint_exit"] == 0
                and checks["git_diff_check_exit"] == 0
            )
            session_id = extract_session_id(lines)
            if session_id:
                receipt["resume_command"] = build_resume_command(root, session_id)
            receipt.update(
                {
                    "status": "completed" if success else "failed-verification",
                    "exit_code": process.returncode,
                    "session_id": session_id,
                    "failure_reason": extract_failure_reason(lines),
                    "checks": checks,
                    "finished_at": datetime.now(TIMEZONE).isoformat(),
                }
            )
            if success:
                state.update(
                    {
                        "schema_version": 1,
                        "cycle": CYCLE_NAME,
                        "counting_policy": "30 successful substantive days; acceptance-only runs are excluded",
                        "next_day_index": min(day_index + 1, TOTAL_DAYS + 1),
                        "last_success": run_date,
                        "last_run_id": run_id,
                        "status": "complete" if day_index == TOTAL_DAYS else "active",
                    }
                )
                write_json_atomic(paths.state_file, state)
            write_json_atomic(run_dir / "run.json", receipt)
            print(json.dumps(receipt, ensure_ascii=False, indent=2))
            return 0 if success else 1
    except Exception as exc:
        print(json.dumps({"status": "runner-error", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
