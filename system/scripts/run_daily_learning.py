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
import time
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

from wiki_knowledge_writeback import snapshot_knowledge, validate_writeback


TIMEZONE = ZoneInfo("Asia/Shanghai")
TOTAL_DAYS = 30
CYCLE_NAME = "2026-09-30-day-substantive"
SCHEDULE_ID = "wiki-daily-learning"
SCHEDULE_NAME = "Wiki 30-day substantive daily learning"
SESSION_MODE = "new-session-per-run"
DAY_TITLES = {
    1: "基线考试与研究契约",
    2: "壳层-magic-gap-与单粒子轨道",
    3: "平均场-Nilsson-CSM-HFB-与投影模型",
    4: "配对-准粒子与组态变化",
    5: "β-γ-八极自由度与shape-coexistence",
    6: "转动-振动-alignment与signature",
    7: "第一次周考-集体运动口试",
    8: "角动量耦合-选择定则与多极性",
    9: "B(E2)-B(M1)-约化矩阵元与强度比",
    10: "电磁比值与集体模式判别",
    11: "反应布居-蒸发道与高自旋入口",
    12: "γγ符合-门条件-背景与能级纲图",
    13: "Doppler-correction-recoil与速度信息",
    14: "第二次周考-从谱到能级纲图",
    15: "ADO-角分布系数与几何修正",
    16: "DCO-RDCO-混合比与符号约定",
    17: "线偏振-P-A-Q与Compton响应",
    18: "DSAM-寿命到跃迁强度",
    19: "RDDS-fast-timing与时间响应",
    20: "B(E2)-Qt与形变系统学",
    21: "第三次周考-实验结论边界",
    22: "wobbling-几何-声子与观测量",
    23: "signature-partner-低自旋-wobbling与磁转动",
    24: "chirality-手征振动-静态手征与partner-bands",
    25: "chirality反例与shape-coexistence",
    26: "八极关联-E1-E3与磁反磁转动",
    27: "跨质量区迁移与不适用性",
    28: "独立-L3研究日与第四次周考",
    29: "研究设计答辩",
    30: "综合口试与月度prospectus",
}
DAY_FILE_TOPICS = {
    1: "baseline-research-contract",
    2: "shell-gap-single-particle",
    3: "mean-field-nilsson-csm-hfb-projection",
    4: "pairing-quasiparticle-configuration",
    5: "beta-gamma-octupole-shape-coexistence",
    6: "rotation-vibration-alignment-signature",
    7: "week-one-collective-motion-oral-exam",
    8: "angular-momentum-selection-rules-multipoles",
    9: "be2-bm1-reduced-matrix-elements-strengths",
    10: "electromagnetic-ratios-collective-modes",
    11: "reaction-population-evaporation-high-spin",
    12: "gamma-gamma-gating-background-level-scheme",
    13: "doppler-correction-recoil-velocity",
    14: "week-two-spectrum-to-level-scheme-exam",
    15: "ado-angular-distribution-geometry",
    16: "dco-rdco-mixing-ratio-convention",
    17: "linear-polarization-paq-compton",
    18: "dsam-lifetime-transition-strength",
    19: "rdds-fast-timing-time-response",
    20: "be2-qt-deformation-systematics",
    21: "week-three-experimental-boundaries-exam",
    22: "wobbling-geometry-phonon-observables",
    23: "signature-partner-low-spin-wobbling-magnetic-rotation",
    24: "chirality-vibration-static-partner-bands",
    25: "chirality-counterevidence-shape-coexistence",
    26: "octupole-e1-e3-magnetic-antimagnetic-rotation",
    27: "cross-mass-region-transferability",
    28: "independent-l3-research-week-four-exam",
    29: "research-design-defense",
    30: "final-oral-exam-monthly-prospectus",
}
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
    continuation_prompt_file: Path
    lock_file: Path


def phase_for_day(day_index: int) -> str:
    if not 1 <= day_index <= TOTAL_DAYS:
        raise ValueError(f"day_index must be in 1..{TOTAL_DAYS}")
    for first, last, phase in PHASES:
        if first <= day_index <= last:
            return phase
    raise AssertionError("phase table does not cover day_index")


def day_topic(day_index: int) -> str:
    if day_index not in DAY_TITLES:
        raise ValueError(f"day_index must be in 1..{TOTAL_DAYS}")
    return DAY_TITLES[day_index]


def daily_file_stem(run_date: str, day_index: int) -> str:
    compact_date = run_date.replace("-", "")
    if day_index not in DAY_FILE_TOPICS:
        raise ValueError(f"day_index must be in 1..{TOTAL_DAYS}")
    return f"{compact_date}-DAY{day_index}-{DAY_FILE_TOPICS[day_index]}"


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
        continuation_prompt_file=root / "system" / "prompts" / "daily-learning-continuation.md",
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


def next_run_number(daily_root: Path, run_date: str, day_index: int) -> int:
    prefix = daily_file_stem(run_date, day_index)
    pattern = re.compile(rf"^{re.escape(prefix)}-run-(\d+)$")
    numbers = []
    for child in daily_root.glob(f"{prefix}-run-*"):
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
    command += ["--thread-source", "scheduled", "exec", "--json", "-o", str(last_message), "-"]
    return command


def build_resume_exec_command(
    root: Path,
    model: str,
    session_id: str,
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
    command += ["exec", "resume", session_id, "--json", "-o", str(last_message), "-"]
    return command


def parse_deadline(value: str, now: datetime | None = None) -> datetime:
    """Parse an Asia/Shanghai HH:MM deadline, rolling to tomorrow when needed."""

    try:
        hour_text, minute_text = value.split(":", 1)
        hour, minute = int(hour_text), int(minute_text)
    except (ValueError, AttributeError) as exc:
        raise ValueError("--until must use HH:MM") from exc
    if not (0 <= hour <= 23 and 0 <= minute <= 59):
        raise ValueError("--until must use an hour 0..23 and minute 0..59")
    current = now or datetime.now(TIMEZONE)
    if current.tzinfo is None:
        current = current.replace(tzinfo=TIMEZONE)
    deadline = current.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if deadline <= current:
        deadline += timedelta(days=1)
    return deadline


def render_continuation_prompt(
    paths: Paths,
    run_id: str,
    run_date: str,
    day_index: int,
    continuation_number: int,
    deadline: datetime,
) -> str:
    template = paths.continuation_prompt_file.read_text(encoding="utf-8")
    substitutions = {
        "{{RUN_ID}}": run_id,
        "{{RUN_DATE}}": run_date,
        "{{DAY_INDEX}}": str(day_index),
        "{{DAY_TOPIC}}": day_topic(day_index),
        "{{CONTINUATION_NUMBER}}": str(continuation_number),
        "{{DEADLINE}}": deadline.isoformat(),
    }
    for old, new in substitutions.items():
        template = template.replace(old, new)
    return template


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


def render_prompt(
    paths: Paths,
    run_id: str,
    run_date: str,
    day_index: int,
    mode: str = "daily-learning",
    prompt_file: Path | None = None,
) -> str:
    phase = phase_for_day(day_index)
    template_path = prompt_file or paths.prompt_file
    template = template_path.read_text(encoding="utf-8")
    substitutions = {
        "{{RUN_ID}}": run_id,
        "{{RUN_DATE}}": run_date,
        "{{DAY_INDEX}}": str(day_index),
        "{{PHASE}}": phase,
        "{{SCHEDULE_ID}}": SCHEDULE_ID,
        "{{SCHEDULE_NAME}}": SCHEDULE_NAME,
        "{{OUTPUT_DIR}}": str(
            paths.daily_root / f"{daily_file_stem(run_date, day_index)}-run-{run_id.rsplit('-', 1)[-1]}"
        ),
        "{{REPORT_FILE}}": str(paths.daily_root / f"{daily_file_stem(run_date, day_index)}.md"),
        "{{STATE_FILE}}": str(paths.state_file),
    }
    for old, new in substitutions.items():
        template = template.replace(old, new)
    if mode == "acceptance":
        template += """

## Acceptance-only execution contract

This is a Day 1 instance acceptance run, not a substantive learning day. Do not
advance the 30-day state, do not claim formal Day 1 completion, and do not create
duplicate scientific knowledge when the canonical artifact already exists. Prefer a
grounded `verified-no-op` writeback with one exact atomic locator per source reference
if the required artifact is already present. The run must still produce all required
report headings and a resumable session receipt.
"""
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


def run_resume_turn(
    root: Path,
    command: list[str],
    prompt: str,
    events_path: Path,
    stderr_path: Path,
) -> tuple[int, list[str]]:
    events_path.parent.mkdir(parents=True, exist_ok=True)
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
    return process.returncode, lines


def dry_run(
    paths: Paths,
    model: str,
    enable_search: bool,
    reasoning_effort: str | None = None,
    mode: str = "daily-learning",
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
        "schedule_id": SCHEDULE_ID,
        "schedule_name": SCHEDULE_NAME,
        "project_root": str(paths.root),
        "codex": shutil.which("codex"),
        "codex_home": str(codex_home),
        "session_mode": SESSION_MODE,
        "mode": mode,
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
    parser.add_argument("--mode", choices=["daily-learning", "acceptance"], default="daily-learning")
    parser.add_argument("--model", default="gpt-6-luna")
    parser.add_argument("--reasoning-effort", choices=["low", "medium", "high", "max"], default="max")
    parser.add_argument("--no-search", action="store_true")
    parser.add_argument("--prompt-file", type=Path, default=None)
    parser.add_argument("--prepare-prompt", type=Path, default=None)
    parser.add_argument("--until", default=None, help="continue the same session until HH:MM Asia/Shanghai")
    parser.add_argument("--max-continuations", type=int, default=96)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    paths = get_paths(root)
    try:
        if args.max_continuations < 0:
            raise ValueError("--max-continuations must be non-negative")
        schedule_deadline = parse_deadline(args.until) if args.until else None
        result = dry_run(paths, args.model, not args.no_search, args.reasoning_effort, args.mode)
        if args.dry_run:
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return 0
        validate_root(root)
        state = read_state(paths.state_file)
        day_index = int(state.get("next_day_index", 1)) if args.day_index == "auto" else int(args.day_index)
        if args.prepare_prompt is not None:
            if args.day_index == "auto":
                day_index = int(state.get("next_day_index", 1))
            prompt_date = local_date()
            prompt_run_id = f"prompt-{prompt_date}-day-{day_index:02d}"
            prompt = render_prompt(paths, prompt_run_id, prompt_date, day_index, args.mode)
            prompt_path = args.prepare_prompt.resolve()
            prompt_path.relative_to(root)
            prompt_path.parent.mkdir(parents=True, exist_ok=True)
            prompt_path.write_text(prompt, encoding="utf-8")
            print(json.dumps({
                "status": "prompt-prepared",
                "mode": args.mode,
                "day_index": day_index,
                "prompt_file": str(prompt_path),
            }, ensure_ascii=False, indent=2))
            return 0
        if args.mode != "acceptance" and (state.get("status") == "complete" or day_index > TOTAL_DAYS):
            print(
                json.dumps(
                    {
                        "status": "cycle-complete",
                        "cycle": CYCLE_NAME,
                        "schedule_id": SCHEDULE_ID,
                        "schedule_name": SCHEDULE_NAME,
                        "project_root": str(root),
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
        file_stem = daily_file_stem(run_date, day_index)
        run_number = next_run_number(paths.daily_root, run_date, day_index)
        run_id = f"{run_date}-day-{day_index:02d}-{run_number:02d}"
        run_dir = paths.daily_root / f"{file_stem}-run-{run_number:02d}"
        run_dir.mkdir(parents=True, exist_ok=False)
        report_path = paths.daily_root / f"{file_stem}.md"
        report_before = report_signature(report_path)
        events_path = run_dir / "events.jsonl"
        stderr_path = run_dir / "stderr.log"
        last_message = run_dir / "last-message.md"
        run_kind = "acceptance-only" if args.mode == "acceptance" else "substantive"
        receipt = {
            "schema_version": 1,
            "run_id": run_id,
            "run_date": run_date,
            "day_index": day_index,
            "phase": phase,
            "cycle": CYCLE_NAME,
            "schedule_id": SCHEDULE_ID,
            "schedule_name": SCHEDULE_NAME,
            "project_root": str(root),
            "run_kind": run_kind,
            "acceptance_only": args.mode == "acceptance",
            "overnight_until": schedule_deadline.isoformat() if schedule_deadline else None,
            "max_continuations": args.max_continuations,
            "continuation_count": 0,
            "counted_in_substantive_test": False,
            "session_mode": SESSION_MODE,
            "session_reuse": False,
            "session_scope": "one-new-session-for-each-schedule-run",
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
            prompt = render_prompt(paths, run_id, run_date, day_index, args.mode, args.prompt_file)
            prompt_path = run_dir / "prompt.md"
            prompt_path.write_text(prompt, encoding="utf-8")
            receipt["prompt_file"] = str(prompt_path)
            write_json_atomic(run_dir / "run.json", receipt)
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
            session_id = extract_session_id(lines)
            continuation_runs: list[dict[str, Any]] = []
            final_returncode = process.returncode
            continuation_count = 0
            if (
                schedule_deadline is not None
                and args.mode == "daily-learning"
                and final_returncode == 0
                and session_id
            ):
                while (
                    datetime.now(TIMEZONE) < schedule_deadline
                    and continuation_count < args.max_continuations
                ):
                    continuation_count += 1
                    continuation_prompt = render_continuation_prompt(
                        paths,
                        run_id,
                        run_date,
                        day_index,
                        continuation_count,
                        schedule_deadline,
                    )
                    continuation_events = run_dir / f"continuation-{continuation_count:03d}-events.jsonl"
                    continuation_stderr = run_dir / f"continuation-{continuation_count:03d}-stderr.log"
                    continuation_last = run_dir / f"continuation-{continuation_count:03d}-last-message.md"
                    continuation_command = build_resume_exec_command(
                        root,
                        args.model,
                        session_id,
                        continuation_last,
                        not args.no_search,
                        args.reasoning_effort,
                    )
                    continuation_rc, continuation_lines = run_resume_turn(
                        root,
                        continuation_command,
                        continuation_prompt,
                        continuation_events,
                        continuation_stderr,
                    )
                    lines.extend(continuation_lines)
                    continuation_runs.append(
                        {
                            "number": continuation_count,
                            "returncode": continuation_rc,
                            "events": str(continuation_events),
                            "last_message": str(continuation_last),
                        }
                    )
                    receipt.update(
                        {
                            "continuation_count": continuation_count,
                            "continuation_runs": continuation_runs,
                            "session_id": session_id,
                        }
                    )
                    write_json_atomic(run_dir / "run.json", receipt)
                    if continuation_rc != 0:
                        final_returncode = continuation_rc
                        break
                    if datetime.now(TIMEZONE) < schedule_deadline:
                        time.sleep(2)
            checks = run_checks(root, report_path, report_before, knowledge_before)
            success = (
                final_returncode == 0
                and checks["preflight"]["exit"] == 0
                and checks["report_exists"]
                and checks["report_changed"]
                and checks["report_valid"]
                and checks["durable_knowledge"]["valid"]
                and checks["lint_exit"] == 0
                and checks["git_diff_check_exit"] == 0
            )
            if session_id:
                receipt["resume_command"] = build_resume_command(root, session_id)
            receipt.update(
                {
                    "status": "completed" if success else "failed-verification",
                    "counted_in_substantive_test": success and args.mode == "daily-learning",
                    "exit_code": final_returncode,
                    "session_id": session_id,
                    "failure_reason": extract_failure_reason(lines),
                    "checks": checks,
                    "finished_at": datetime.now(TIMEZONE).isoformat(),
                    "continuation_count": continuation_count,
                    "continuation_runs": continuation_runs,
                }
            )
            if success and args.mode == "daily-learning":
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
