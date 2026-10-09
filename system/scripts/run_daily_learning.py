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
import time as time_module
from dataclasses import dataclass
from datetime import datetime, time, timedelta
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

from wiki_knowledge_writeback import snapshot_knowledge, validate_writeback


TIMEZONE = ZoneInfo("Asia/Shanghai")
TOTAL_DAYS = 30
CYCLE_NAME = "2026-09-30-day-substantive"
DEFAULT_CLOSEOUT_TIME = "15:00"
DEFAULT_SCHEDULE_START_TIME = "16:00"
MIN_CURRENT_STUDY_BLOCK_MINUTES = 90
MIN_FORWARD_CARD_BLOCK_MINUTES = 120
RUNTIME_SNAPSHOT_START = "<!-- DAILY_LEARNING_RUNTIME_SNAPSHOT_START -->"
RUNTIME_SNAPSHOT_END = "<!-- DAILY_LEARNING_RUNTIME_SNAPSHOT_END -->"
CURRICULUM_COVERAGE_MARKER = "<!-- DAILY_LEARNING_CURRICULUM_COVERAGE_V1 -->"
TIME_GATE_CONTRACT_MARKER = "<!-- DAILY_LEARNING_TIME_GATE_V1 -->"
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
    # `--thread-source` belongs to the `exec` subcommand in current Codex CLI.
    # Placing it before `exec` makes the CLI reject the invocation as an
    # unexpected global argument and prevents the nightly run from starting.
    command += ["exec", "--thread-source", "scheduled", "--json", "-o", str(last_message), "-"]
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


def planned_closeout_for_run_date(run_date: str) -> datetime:
    """Return the scheduled-run preview for the following day's closeout."""

    run_day = datetime.fromisoformat(run_date).date()
    hour, minute = (int(part) for part in DEFAULT_CLOSEOUT_TIME.split(":"))
    return datetime.combine(run_day + timedelta(days=1), time(hour, minute), tzinfo=TIMEZONE)


def next_scheduled_start_for_run_date(run_date: str) -> datetime:
    """Return the next daily 16:00 trigger after this run's scheduled date."""

    run_day = datetime.fromisoformat(run_date).date()
    hour, minute = (int(part) for part in DEFAULT_SCHEDULE_START_TIME.split(":"))
    return datetime.combine(run_day + timedelta(days=1), time(hour, minute), tzinfo=TIMEZONE)


def closeout_snapshot(
    now: datetime,
    deadline: datetime,
    next_scheduled_start: datetime,
    minimum_current_block_minutes: int = MIN_CURRENT_STUDY_BLOCK_MINUTES,
    minimum_forward_card_block_minutes: int = MIN_FORWARD_CARD_BLOCK_MINUTES,
) -> dict[str, Any]:
    """Describe the useful study runway without conflating it with the next trigger."""

    if now.tzinfo is None or deadline.tzinfo is None or next_scheduled_start.tzinfo is None:
        raise ValueError("now, deadline, and next_scheduled_start must be timezone-aware")
    if minimum_current_block_minutes < 0 or minimum_forward_card_block_minutes < 0:
        raise ValueError("minimum study block minutes must be non-negative")
    current = now.astimezone(TIMEZONE)
    hard_deadline = deadline.astimezone(TIMEZONE)
    next_start = next_scheduled_start.astimezone(TIMEZONE)
    remaining_minutes = int((hard_deadline - current).total_seconds() // 60)
    next_start_gap_minutes = int((next_start - current).total_seconds() // 60)
    can_continue_current = current < hard_deadline and remaining_minutes >= minimum_current_block_minutes
    can_complete_forward_card = (
        current < hard_deadline and remaining_minutes >= minimum_forward_card_block_minutes
    )
    if current >= hard_deadline:
        decision = "closeout-only"
    elif can_complete_forward_card:
        decision = "continue-or-advance"
    elif can_continue_current:
        decision = "continue-current-or-partial"
    else:
        decision = "finish-current-no-new-unit"
    return {
        "now_local": current.isoformat(),
        "hard_deadline": hard_deadline.isoformat(),
        "next_scheduled_start": next_start.isoformat(),
        "minutes_to_deadline": remaining_minutes,
        "minutes_to_next_start": next_start_gap_minutes,
        "minimum_current_block_minutes": minimum_current_block_minutes,
        "minimum_forward_card_block_minutes": minimum_forward_card_block_minutes,
        "can_continue_current": can_continue_current,
        "can_complete_forward_card": can_complete_forward_card,
        "decision": decision,
    }


def format_runtime_schedule_snapshot(
    snapshot: dict[str, Any],
    day_index: int,
    next_day_index: int | None = None,
) -> str:
    next_day = (
        next_day_index
        if next_day_index is not None
        else day_index + 1 if day_index < TOTAL_DAYS else None
    )
    if next_day is not None and not 1 <= next_day <= TOTAL_DAYS:
        next_day = None
    forward_line = (
        f"- Next card candidate: Day {next_day} ({day_topic(next_day)})."
        if next_day is not None
        else "- Next card candidate: none; Day 30 is the final card."
    )
    if next_day is not None and next_day > day_index + 1:
        forward_instruction = (
            "The requested card and its immediate forward card are already complete. This run may credit only those contiguous cards; do not credit another card. Continue a bounded high-value issue or preview without advancing the curriculum."
        )
    else:
        forward_instruction = (
            "If closeout_decision is continue-or-advance, continue the current high-value issue; if both selected slots are saturated, inspect the next card and complete it only if its full deliverable fits the window."
        )
    return "\n".join(
        (
            RUNTIME_SNAPSHOT_START,
            "## Runtime schedule snapshot",
            f"- now_local: {snapshot['now_local']}",
            f"- hard_deadline: {snapshot['hard_deadline']}",
            f"- next_scheduled_start: {snapshot['next_scheduled_start']}",
            f"- minutes_to_deadline: {snapshot['minutes_to_deadline']}",
            f"- minutes_to_next_start: {snapshot['minutes_to_next_start']}",
            f"- closeout_decision: {snapshot['decision']}",
            forward_line,
            forward_instruction,
            "If closeout_decision is continue-current-or-partial, stay within the current issue or do one bounded preview; do not claim a whole next card.",
            "If closeout_decision is finish-current-no-new-unit, finish only the current bounded analysis and do not open another source/card. If it is closeout-only, stop research and finalize.",
            "Before ending early for evidence saturation, refresh the clock and candidate pool; saturation of the two selected slots alone is not schedule-level saturation while a viable next-card route remains.",
            RUNTIME_SNAPSHOT_END,
        )
    )


def ensure_curriculum_coverage_contract(prompt: str) -> str:
    if CURRICULUM_COVERAGE_MARKER in prompt:
        return prompt
    contract = "\n".join(
        (
            CURRICULUM_COVERAGE_MARKER,
            "## Curriculum card completion record",
            "In the report's Run state include exactly these two machine-readable list lines:",
            "- completed_day_indices: [N, ...]",
            "- partial_day_indices: [N, ...]",
            "Count a card only after every deliverable on that Day card is complete. For every completed day, add `- Day N card audit: complete` under Run state and a `### Day N card completion audit` table with at least four Day-matrix deliverables, each linked to an evidence locator/artifact and marked complete. Partial previews go only in partial_day_indices. List cards contiguously from the requested day; at most one next-day card may be advanced in one run.",
            "For a completed Day 7 card also include these exact audit lines:",
            "- Day 7 scorecard: complete",
            "- Day 7 weekly REFLECT: complete",
            "",
        )
    )
    return prompt.rstrip() + "\n\n" + contract


def ensure_schedule_gate_contract(prompt: str) -> str:
    if TIME_GATE_CONTRACT_MARKER in prompt:
        return prompt
    contract = "\n".join(
        (
            TIME_GATE_CONTRACT_MARKER,
            "## 时间判断与学习收束",
            "候选问题或来源达到局部证据饱和时，先读取最新 Runtime schedule snapshot；手动恢复且没有新快照时，调用当前时间工具，并按 Asia/Shanghai 与回执中的 overnight_until 比较。",
            "距离硬截止至少 120 分钟：继续当前高信息问题；若当前选定问题已饱和，检查下一张未完成日卡，只有其全部交付项能在剩余时段完成时才整卡前移。",
            "距离硬截止 90–119 分钟：继续当前问题或做有边界的预览，不给下一日卡完整学分。少于 90 分钟：不打开新来源或新卡，只完成当前分析。硬截止后停止研究，用 15:00–16:00 收束。",
            "不能仅因两个候选槽位饱和而提前结束；须重建候选池、检查下一张可行日卡，并记录时间快照和决定。用户明确停止、硬证据/数据/权限阻塞或运行故障可提前结束，但必须保留未完成状态和续接命令。",
            "每次调用生成的新 Runtime snapshot 优先于本文件中的旧快照。课程学分只沿连续完整日卡推进；部分预览不得推进 next_day_index。",
            "",
        )
    )
    return prompt.rstrip() + "\n\n" + contract


def inject_runtime_schedule_snapshot(
    prompt: str,
    snapshot: dict[str, Any],
    day_index: int,
    next_day_index: int | None = None,
) -> str:
    block = format_runtime_schedule_snapshot(snapshot, day_index, next_day_index)
    pattern = re.compile(
        re.escape(RUNTIME_SNAPSHOT_START) + r".*?" + re.escape(RUNTIME_SNAPSHOT_END),
        flags=re.DOTALL,
    )
    prompt = pattern.sub("", prompt).rstrip()
    return prompt + "\n\n" + block + "\n"


def continuation_limit_reached(
    continuation_count: int,
    max_continuations: int,
    now: datetime,
    deadline: datetime,
) -> bool:
    """A continuation cap before the hard deadline is not a completed study window."""

    if continuation_count < 0 or max_continuations < 0:
        raise ValueError("continuation counts must be non-negative")
    if now.tzinfo is None or deadline.tzinfo is None:
        raise ValueError("now and deadline must be timezone-aware")
    return continuation_count >= max_continuations and now.astimezone(TIMEZONE) < deadline.astimezone(TIMEZONE)


def closeout_window_end(deadline: datetime) -> datetime:
    if deadline.tzinfo is None:
        raise ValueError("deadline must be timezone-aware")
    return deadline.astimezone(TIMEZONE) + timedelta(hours=1)


def should_run_closeout_turn(now: datetime, deadline: datetime) -> bool:
    """Use the reserved hour after research cutoff for one no-new-research turn."""

    if now.tzinfo is None or deadline.tzinfo is None:
        raise ValueError("now and deadline must be timezone-aware")
    current = now.astimezone(TIMEZONE)
    hard_deadline = deadline.astimezone(TIMEZONE)
    return hard_deadline <= current < closeout_window_end(hard_deadline)


def next_continuation_action(
    now: datetime,
    deadline: datetime,
    continuation_count: int,
    max_continuations: int,
    closeout_completed: bool,
) -> str:
    """Choose a study turn, roll over a bounded batch, close out, or finalize."""

    if now.tzinfo is None or deadline.tzinfo is None:
        raise ValueError("now and deadline must be timezone-aware")
    current = now.astimezone(TIMEZONE)
    hard_deadline = deadline.astimezone(TIMEZONE)
    if current < hard_deadline:
        if continuation_limit_reached(
            continuation_count, max_continuations, current, hard_deadline
        ):
            return "rollover"
        return "study"
    return "finalize" if closeout_completed else "closeout"


def parse_curriculum_coverage(report_text: str, starting_day_index: int) -> dict[str, Any]:
    """Parse contiguous completed/partial curriculum cards from the Run state section."""

    if not 1 <= starting_day_index <= TOTAL_DAYS:
        return {"valid": False, "error": "starting day index is outside the 30-day plan"}

    run_state_match = re.search(
        r"(?ms)^## Run state\s*\n(.*?)(?=^## |\Z)", report_text
    )
    if not run_state_match:
        return {"valid": False, "error": "curriculum coverage must be recorded under ## Run state"}
    run_state_text = run_state_match.group(1)

    def parse_list(field: str) -> list[int] | None:
        match = re.search(rf"(?m)^- {re.escape(field)}: \[([0-9, ]*)\]\s*$", run_state_text)
        if not match:
            return None
        payload = match.group(1).strip()
        if not payload:
            return []
        try:
            values = [int(value.strip()) for value in payload.split(",")]
        except ValueError:
            return None
        return values

    completed = parse_list("completed_day_indices")
    partial = parse_list("partial_day_indices")
    if completed is None or partial is None:
        return {"valid": False, "error": "Run state must list completed_day_indices and partial_day_indices"}
    if len(set(completed)) != len(completed) or len(set(partial)) != len(partial):
        return {"valid": False, "error": "day card indices must not be duplicated"}
    if any(not 1 <= day <= TOTAL_DAYS for day in completed + partial):
        return {"valid": False, "error": "day card index is outside the 30-day plan"}
    expected_completed = list(range(starting_day_index, starting_day_index + len(completed)))
    if completed != expected_completed:
        return {"valid": False, "error": "completed day cards must form a contiguous sequence from the requested day"}
    expected_partial_day = starting_day_index + len(completed)
    if partial and partial != [expected_partial_day]:
        return {"valid": False, "error": "at most the first incomplete day card may be marked partial"}
    if len(completed) > 2:
        return {"valid": False, "error": "a single run may complete only its requested card and one forward card"}
    if not completed and partial != [starting_day_index]:
        return {"valid": False, "error": "the requested day must be completed or explicitly marked partial"}
    for completed_day in completed:
        audit_marker = f"- Day {completed_day} card audit: complete"
        if audit_marker not in run_state_text:
            return {
                "valid": False,
                "error": f"Day {completed_day} credit requires its card audit to be complete under ## Run state",
            }
        audit = re.search(
            rf"(?ms)^### Day {completed_day} card completion audit\s*\n(.*?)(?=^### |^## |\Z)",
            report_text,
        )
        if not audit:
            return {
                "valid": False,
                "error": f"Day {completed_day} credit requires a card completion audit table",
            }
        audit_rows = [
            line
            for line in audit.group(1).splitlines()
            if line.startswith("|") and not re.match(r"^\|\s*:?-{3,}", line)
        ]
        data_rows = audit_rows[1:] if audit_rows else []
        if len(data_rows) < 4 or any(
            len([part.strip() for part in row.strip("|").split("|")]) < 3
            or not [part.strip() for part in row.strip("|").split("|")][1]
            or [part.strip() for part in row.strip("|").split("|")][-1].lower() != "complete"
            for row in data_rows
        ):
            return {
                "valid": False,
                "error": f"Day {completed_day} card audit needs at least four completed deliverables with evidence locators",
            }
    if 7 in completed:
        required_day7_markers = (
            "- Day 7 scorecard: complete",
            "- Day 7 weekly REFLECT: complete",
            "## Day 7 scorecard",
            "## Day 7 weekly REFLECT",
        )
        if any(marker not in report_text for marker in required_day7_markers):
            return {"valid": False, "error": "Day 7 credit requires its six-item scorecard and weekly REFLECT"}
        score_categories = ("理论", "判图", "误差", "证据分层", "反证", "可证伪问题")
        for category in score_categories:
            pattern = rf"(?m)^\|\s*{re.escape(category)}\s*\|\s*[0-4]\s*\|"
            if not re.search(pattern, report_text):
                return {"valid": False, "error": f"Day 7 scorecard is missing a valid 0–4 row for {category}"}
        reflect = re.search(
            r"(?ms)^## Day 7 weekly REFLECT\s*\n(.*?)(?=^## |\Z)",
            report_text,
        )
        if not reflect or not reflect.group(1).strip():
            return {"valid": False, "error": "Day 7 weekly REFLECT section must contain content"}
    next_day_index = starting_day_index + len(completed)
    return {
        "valid": True,
        "completed_day_indices": completed,
        "partial_day_indices": partial,
        "curriculum_cards_completed": len(completed),
        "next_day_index": min(next_day_index, TOTAL_DAYS + 1),
        "error": None,
    }


def validate_curriculum_coverage(path: Path, starting_day_index: int) -> dict[str, Any]:
    if not path.is_file():
        return {"valid": False, "error": f"daily report is missing: {path}"}
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return {"valid": False, "error": f"cannot read daily report: {exc}"}
    return parse_curriculum_coverage(text, starting_day_index)


def update_state_for_curriculum_cards(
    state: dict[str, Any],
    run_id: str,
    run_date: str,
    coverage: dict[str, Any],
) -> dict[str, Any]:
    """Advance only through contiguous, fully completed curriculum cards."""

    if not coverage.get("valid"):
        raise ValueError(coverage.get("error") or "curriculum coverage is invalid")
    completed = coverage.get("completed_day_indices", [])
    updated = dict(state)
    if not completed:
        return updated
    next_day_index = int(coverage["next_day_index"])
    updated.update(
        {
            "schema_version": 1,
            "cycle": CYCLE_NAME,
            "counting_policy": "30 fully completed substantive curriculum cards; a run may complete multiple contiguous cards; acceptance-only runs are excluded",
            "next_day_index": min(next_day_index, TOTAL_DAYS + 1),
            "completed_day_count": min(next_day_index - 1, TOTAL_DAYS),
            "last_success": run_date,
            "last_run_id": run_id,
            "status": "complete" if next_day_index > TOTAL_DAYS else "active",
        }
    )
    return updated


def render_continuation_prompt(
    paths: Paths,
    run_id: str,
    run_date: str,
    day_index: int,
    continuation_number: int,
    deadline: datetime,
    now: datetime | None = None,
) -> str:
    template = paths.continuation_prompt_file.read_text(encoding="utf-8")
    template = ensure_schedule_gate_contract(
        ensure_curriculum_coverage_contract(template)
    )
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
    current = now or datetime.now(TIMEZONE)
    snapshot = closeout_snapshot(
        current,
        deadline,
        next_scheduled_start_for_run_date(run_date),
    )
    report_path = paths.daily_root / f"{daily_file_stem(run_date, day_index)}.md"
    coverage = validate_curriculum_coverage(report_path, day_index)
    next_day_index = (
        int(coverage["next_day_index"])
        if coverage.get("valid")
        else day_index
    )
    return inject_runtime_schedule_snapshot(template, snapshot, day_index, next_day_index)


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
    window_deadline: datetime | None = None,
    runtime_now: datetime | None = None,
) -> str:
    phase = phase_for_day(day_index)
    template_path = prompt_file or paths.prompt_file
    template = template_path.read_text(encoding="utf-8")
    substitutions = {
        "{{RUN_ID}}": run_id,
        "{{RUN_DATE}}": run_date,
        "{{DAY_INDEX}}": str(day_index),
        "{{DAY_TOPIC}}": day_topic(day_index),
        "{{PHASE}}": phase,
        "{{SCHEDULE_ID}}": SCHEDULE_ID,
        "{{SCHEDULE_NAME}}": SCHEDULE_NAME,
        "{{OUTPUT_DIR}}": str(
            paths.daily_root / f"{daily_file_stem(run_date, day_index)}-run-{run_id.rsplit('-', 1)[-1]}"
        ),
        "{{REPORT_FILE}}": str(paths.daily_root / f"{daily_file_stem(run_date, day_index)}.md"),
        "{{STATE_FILE}}": str(paths.state_file),
        "{{WINDOW_CLOSEOUT_AT}}": (
            window_deadline.isoformat() if window_deadline else "not applicable for acceptance-only runs"
        ),
    }
    for old, new in substitutions.items():
        template = template.replace(old, new)
    if mode == "daily-learning" and window_deadline is not None:
        template = re.sub(
            r"(?m)^- `window_closeout_at`: .*?$",
            f"- `window_closeout_at`: {window_deadline.isoformat()}",
            template,
        )
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
    elif mode == "daily-learning":
        template = ensure_schedule_gate_contract(template)
        template = ensure_curriculum_coverage_contract(template)
        if window_deadline is not None and runtime_now is not None:
            snapshot = closeout_snapshot(
                runtime_now,
                window_deadline,
                next_scheduled_start_for_run_date(run_date),
            )
            report_path = paths.daily_root / f"{daily_file_stem(run_date, day_index)}.md"
            coverage = validate_curriculum_coverage(report_path, day_index)
            next_day_index = (
                int(coverage["next_day_index"])
                if coverage.get("valid")
                else day_index
            )
            template = inject_runtime_schedule_snapshot(
                template, snapshot, day_index, next_day_index
            )
    return template


def prepare_next_prompt(paths: Paths, next_run_date: str, next_day_index: int) -> Path:
    """Materialize the next day's ASCII-named prompt after a successful day."""

    prompt_dir = paths.daily_root / "prompts"
    canonical_path = prompt_dir / f"{daily_file_stem(next_run_date, next_day_index)}.md"
    compact_date = next_run_date.replace("-", "")
    existing = sorted(prompt_dir.glob(f"{compact_date}-DAY{next_day_index}-*.md"))
    path = canonical_path if canonical_path.exists() else existing[0] if existing else canonical_path
    if path.exists():
        existing = path.read_text(encoding="utf-8")
        updated = ensure_schedule_gate_contract(
            ensure_curriculum_coverage_contract(existing)
        )
        if updated != existing:
            path.write_text(updated, encoding="utf-8")
    else:
        prompt_run_id = f"prompt-{next_run_date}-day-{next_day_index:02d}"
        prompt = render_prompt(
            paths,
            prompt_run_id,
            next_run_date,
            next_day_index,
            "daily-learning",
            window_deadline=planned_closeout_for_run_date(next_run_date),
        )
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(prompt, encoding="utf-8")
    return path


def run_checks(
    root: Path,
    report_path: Path,
    report_before: str | None = None,
    knowledge_before: dict[str, str] | None = None,
    day_index: int | None = None,
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
    curriculum_coverage = (
        validate_curriculum_coverage(report_path, day_index)
        if day_index is not None
        else None
    )
    return {
        "preflight": preflight,
        "report_exists": report_path.is_file(),
        "report_changed": report_after is not None and report_after != report_before,
        "report_valid": report_validation["valid"],
        "report_missing_headings": report_validation["missing_headings"],
        "durable_knowledge": durable_knowledge,
        "curriculum_coverage": curriculum_coverage,
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


def resume_running_receipt(paths: Paths, receipt_path: Path, args: argparse.Namespace) -> int:
    """Recover a crashed runner around the same still-running daily-learning session.

    This path never creates a Codex session. It resumes the session ID already
    recorded in the run receipt, then uses the ordinary report, writeback,
    curriculum, prompt and state-update gates below.
    """

    root = paths.root.resolve()
    validate_root(root)
    receipt_path = receipt_path.expanduser().resolve(strict=True)
    try:
        relative = receipt_path.relative_to((root / "outputs" / "learning-daily").resolve())
    except ValueError as exc:
        raise RuntimeError("--resume-receipt must be inside outputs/learning-daily") from exc
    if len(relative.parts) != 2 or receipt_path.name != "run.json" or not re.search(
        r"-run-\d+$", receipt_path.parent.name
    ):
        raise RuntimeError("--resume-receipt must be <daily-run-dir>/run.json")

    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    if not isinstance(receipt, dict):
        raise RuntimeError("resume receipt must contain a JSON object")
    if receipt.get("project_root") != str(root) or receipt.get("session_mode") != SESSION_MODE:
        raise RuntimeError("resume receipt root/session contract does not match this Wiki runner")
    session_id = receipt.get("session_id")
    if not isinstance(session_id, str) or not session_id.strip():
        raise RuntimeError("running receipt has no session_id; refusing to create a replacement session")
    run_dir = receipt_path.parent
    receipt_status = receipt.get("status")
    if receipt_status == "failed-verification":
        # A direct user continuation may still own the persistent session writer
        # when a recovered runner tries to attach. Permit retry only for this
        # precise pre-closeout, same-session lock conflict; other verification
        # failures require a different recovery decision.
        previous_runs = receipt.get("continuation_runs", [])
        last_run = previous_runs[-1] if isinstance(previous_runs, list) and previous_runs else None
        last_number = last_run.get("number") if isinstance(last_run, dict) else None
        prior_stderr = run_dir / f"continuation-{int(last_number):03d}-stderr.log" if type(last_number) is int else None
        retryable_writer_conflict = (
            receipt.get("closeout_turn") is None
            and receipt.get("study_window_closed") is not True
            and isinstance(prior_stderr, Path)
            and prior_stderr.is_file()
            and "already has an active writer" in prior_stderr.read_text(encoding="utf-8", errors="replace")
            and session_id in prior_stderr.read_text(encoding="utf-8", errors="replace")
        )
        if not retryable_writer_conflict:
            raise RuntimeError(
                f"failed-verification receipt is not the recognized pre-closeout same-session writer conflict: {receipt_status}"
            )
        receipt.setdefault("runner_recovery_history", []).append(
            {
                "at": datetime.now(TIMEZONE).isoformat(),
                "status": "retrying-after-same-session-writer-conflict",
                "stderr_file": str(prior_stderr),
                "same_session_id": session_id,
                "replacement_session_created": False,
            }
        )
    elif receipt_status != "running":
        raise RuntimeError(f"only a running or specifically recoverable receipt can be resumed; status={receipt_status!r}")
    run_id = receipt.get("run_id")
    run_date = receipt.get("run_date")
    day_index = receipt.get("day_index")
    if not isinstance(run_id, str) or not isinstance(run_date, str) or type(day_index) is not int:
        raise RuntimeError("resume receipt is missing run identity fields")
    state = read_state(paths.state_file)
    if int(state.get("next_day_index", 1)) != day_index:
        raise RuntimeError(
            f"resume day_index={day_index} does not match course next_day_index={state.get('next_day_index')}"
        )
    if not run_id.startswith(f"{run_date}-day-{day_index:02d}-"):
        raise RuntimeError("resume receipt run_id/date/path do not match")
    schedule_deadline = datetime.fromisoformat(str(receipt.get("overnight_until")))
    expected_deadline = planned_closeout_for_run_date(run_date)
    if schedule_deadline != expected_deadline:
        raise RuntimeError("resume receipt deadline is not run_date + 1 at 15:00 Asia/Shanghai")
    baseline_path = run_dir / "baseline.json"
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    if baseline.get("run_id") != run_id or baseline.get("day_index") != day_index:
        raise RuntimeError("resume baseline identity does not match the receipt")
    if baseline.get("report_existed_before") is not False:
        raise RuntimeError("resume requires a verified baseline showing the report was absent at entry")
    knowledge_before = baseline.get("knowledge_sha256_before")
    if not isinstance(knowledge_before, dict) or not knowledge_before:
        raise RuntimeError("resume baseline has no original knowledge-page snapshot")
    report_path = paths.daily_root / f"{daily_file_stem(run_date, day_index)}.md"
    if Path(str(receipt.get("report"))).resolve() != report_path.resolve():
        raise RuntimeError("resume report path does not match the canonical daily report")
    report_before = None
    if receipt.get("closeout_turn") is not None:
        raise RuntimeError("receipt already records a closeout turn; use final reconciliation, not study resume")

    run_dir = receipt_path.parent
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
        write_json_atomic(receipt_path, receipt)
        print(json.dumps(receipt, ensure_ascii=False, indent=2))
        return 3

    events_path = run_dir / "events.jsonl"
    stderr_path = run_dir / "stderr.log"
    continuation_runs = receipt.get("continuation_runs", [])
    if not isinstance(continuation_runs, list):
        raise RuntimeError("resume receipt continuation_runs must be a list")
    continuation_count = int(receipt.get("continuation_batch_count", 0))
    continuation_total = int(receipt.get("continuation_count", 0))
    continuation_batches = int(receipt.get("continuation_batches", 1))
    turn_number = max(
        (int(item.get("number", 0)) for item in continuation_runs if isinstance(item, dict)),
        default=0,
    )
    closeout_window_missed = bool(receipt.get("closeout_window_missed", False))
    closeout_turn: dict[str, Any] | None = None
    final_returncode = 0
    lines: list[str] = []
    last_continuation_prompt: Path | None = None

    previous_recovery = receipt.get("runner_recovery")
    if isinstance(previous_recovery, dict):
        receipt.setdefault("runner_recovery_history", []).append(previous_recovery)
    receipt["runner_recovery"] = {
        "recovered_at": datetime.now(TIMEZONE).isoformat(),
        "reason": "the original daily runner exited after a successful continuation before the study loop could continue",
        "same_session_resumed": True,
        "replacement_session_created": False,
        "prior_continuation_count": continuation_total,
    }
    write_json_atomic(receipt_path, receipt)

    with paths.lock_file.open("a", encoding="utf-8") as lock_handle:
        try:
            fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise RuntimeError(f"another daily runner holds {paths.lock_file}") from exc

        while True:
            continuation_now = datetime.now(TIMEZONE)
            action = next_continuation_action(
                continuation_now,
                schedule_deadline,
                continuation_count,
                args.max_continuations,
                closeout_completed=closeout_turn is not None,
            )
            if action == "finalize":
                break
            if action == "rollover":
                continuation_batches += 1
                continuation_count = 0
                receipt.update(
                    {
                        "continuation_batches": continuation_batches,
                        "continuation_batch_count": 0,
                        "continuation_count": continuation_total,
                        "last_closeout_snapshot": closeout_snapshot(
                            continuation_now,
                            schedule_deadline,
                            next_scheduled_start_for_run_date(run_date),
                        ),
                    }
                )
                write_json_atomic(receipt_path, receipt)
                continue

            is_closeout = action == "closeout"
            if is_closeout:
                closeout_window_missed = not should_run_closeout_turn(continuation_now, schedule_deadline)
            else:
                continuation_count += 1
                continuation_total += 1
            turn_number += 1
            turn_snapshot = closeout_snapshot(
                continuation_now,
                schedule_deadline,
                next_scheduled_start_for_run_date(run_date),
            )
            continuation_prompt = render_continuation_prompt(
                paths,
                run_id,
                run_date,
                day_index,
                turn_number,
                schedule_deadline,
                now=continuation_now,
            )
            continuation_prompt_path = run_dir / f"continuation-{turn_number:03d}-prompt.md"
            continuation_prompt_path.write_text(continuation_prompt, encoding="utf-8")
            last_continuation_prompt = continuation_prompt_path
            continuation_events = run_dir / f"continuation-{turn_number:03d}-events.jsonl"
            continuation_stderr = run_dir / f"continuation-{turn_number:03d}-stderr.log"
            continuation_last = run_dir / f"continuation-{turn_number:03d}-last-message.md"
            command = build_resume_exec_command(
                root,
                args.model,
                session_id,
                continuation_last,
                not args.no_search,
                args.reasoning_effort,
            )
            continuation_rc, continuation_lines = run_resume_turn(
                root,
                command,
                continuation_prompt,
                continuation_events,
                continuation_stderr,
            )
            lines.extend(continuation_lines)
            continuation_runs.append(
                {
                    "number": turn_number,
                    "study_continuation_number": continuation_total if not is_closeout else None,
                    "kind": "closeout" if is_closeout else "study",
                    "returncode": continuation_rc,
                    "events": str(continuation_events),
                    "prompt": str(continuation_prompt_path),
                    "last_message": str(continuation_last),
                    "time_snapshot": turn_snapshot,
                    "runner_recovery": True,
                }
            )
            if is_closeout:
                closeout_turn = {
                    "number": turn_number,
                    "returncode": continuation_rc,
                    "prompt": str(continuation_prompt_path),
                    "events": str(continuation_events),
                    "window_missed": closeout_window_missed,
                    "time_snapshot": turn_snapshot,
                    "runner_recovery": True,
                }
            receipt.update(
                {
                    "continuation_count": continuation_total,
                    "continuation_batch_count": continuation_count,
                    "continuation_batches": continuation_batches,
                    "continuation_runs": continuation_runs,
                    "session_id": session_id,
                    "last_closeout_snapshot": turn_snapshot,
                    "last_continuation_prompt": str(continuation_prompt_path),
                    "closeout_turn": closeout_turn,
                    "closeout_window_missed": closeout_window_missed,
                }
            )
            write_json_atomic(receipt_path, receipt)
            if continuation_rc != 0:
                final_returncode = continuation_rc
                break
            if is_closeout:
                break
            if datetime.now(TIMEZONE) < schedule_deadline:
                time_module.sleep(2)

        checks = run_checks(root, report_path, report_before, knowledge_before, day_index=day_index)
        coverage = checks.get("curriculum_coverage") or {}
        coverage_valid = bool(coverage.get("valid"))
        requested_card_complete = day_index in coverage.get("completed_day_indices", [])
        window_closed = closeout_turn is not None
        closeout_on_time = window_closed and not closeout_window_missed
        deliverables_passed = (
            final_returncode == 0
            and checks["preflight"]["exit"] == 0
            and checks["report_exists"]
            and checks["report_changed"]
            and checks["report_valid"]
            and checks["durable_knowledge"]["valid"]
            and checks["lint_exit"] == 0
            and checks["git_diff_check_exit"] == 0
            and coverage_valid
            and window_closed
            and closeout_on_time
        )
        success = deliverables_passed and requested_card_complete
        receipt["resume_command"] = build_resume_command(root, session_id)
        next_day_index = int(coverage.get("next_day_index", day_index + 1))
        next_prompt_file: Path | None = None
        next_prompt_error: str | None = None
        if deliverables_passed and next_day_index <= TOTAL_DAYS:
            try:
                next_prompt_file = prepare_next_prompt(
                    paths,
                    datetime.now(TIMEZONE).date().isoformat(),
                    next_day_index,
                )
            except Exception as exc:
                deliverables_passed = success = False
                next_prompt_error = str(exc)
        if next_prompt_error:
            run_status = "failed-verification"
        elif success:
            run_status = "completed"
        elif deliverables_passed:
            run_status = "completed-partial"
        else:
            run_status = "failed-verification"
        receipt.update(
            {
                "status": run_status,
                "counted_in_substantive_test": success,
                "exit_code": final_returncode,
                "session_id": session_id,
                "failure_reason": extract_failure_reason(lines),
                "checks": checks,
                "finished_at": datetime.now(TIMEZONE).isoformat(),
                "continuation_count": continuation_total,
                "continuation_batch_count": continuation_count,
                "continuation_batches": continuation_batches,
                "continuation_runs": continuation_runs,
                "closeout_turn": closeout_turn,
                "closeout_window_missed": closeout_window_missed,
                "study_window_closed": window_closed,
                "closeout_on_time": closeout_on_time,
                "completed_day_indices": coverage.get("completed_day_indices", []),
                "partial_day_indices": coverage.get("partial_day_indices", []),
                "curriculum_cards_completed": coverage.get("curriculum_cards_completed", 0),
                "next_day_index": next_day_index,
                "deliverables_passed": deliverables_passed,
                "next_prompt_file": str(next_prompt_file) if next_prompt_file else None,
                "next_prompt_error": next_prompt_error,
            }
        )
        if success:
            state = update_state_for_curriculum_cards(state, run_id, run_date, coverage)
            write_json_atomic(paths.state_file, state)
        write_json_atomic(receipt_path, receipt)
        print(json.dumps(receipt, ensure_ascii=False, indent=2))
        return 0 if deliverables_passed else 1


def finalize_interactive_closeout(paths: Paths, receipt_path: Path) -> int:
    """Finalize a closeout performed in the already-active receipt session.

    This is the normal runner's state/prompt gate for the case where its exec
    parent cannot attach to a thread already owned by the interactive Codex
    writer. It creates no session and advances course state only after the same
    report, writeback, lint, diff, closeout-time and card checks as main().
    """

    root = paths.root.resolve()
    validate_root(root)
    receipt_path = receipt_path.expanduser().resolve(strict=True)
    try:
        relative = receipt_path.relative_to((root / "outputs" / "learning-daily").resolve())
    except ValueError as exc:
        raise RuntimeError("--finalize-receipt must be inside outputs/learning-daily") from exc
    if len(relative.parts) != 2 or receipt_path.name != "run.json" or not re.search(r"-run-\d+$", receipt_path.parent.name):
        raise RuntimeError("--finalize-receipt must be <daily-run-dir>/run.json")
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    if not isinstance(receipt, dict):
        raise RuntimeError("finalize receipt must contain a JSON object")
    if receipt.get("status") == "completed":
        print(json.dumps({"status": "already-completed", "receipt": str(receipt_path)}, ensure_ascii=False))
        return 0
    if receipt.get("status") not in {"running", "failed-verification"}:
        raise RuntimeError(f"receipt cannot be finalized from status={receipt.get('status')!r}")
    session_id = receipt.get("session_id")
    if not isinstance(session_id, str) or not session_id:
        raise RuntimeError("receipt has no existing session_id")
    if os.environ.get("CODEX_SESSION_ID") != session_id:
        raise RuntimeError("interactive closeout must run in the same CODEX_SESSION_ID as the receipt")
    run_id = receipt.get("run_id")
    run_date = receipt.get("run_date")
    day_index = receipt.get("day_index")
    if not isinstance(run_id, str) or not isinstance(run_date, str) or type(day_index) is not int:
        raise RuntimeError("receipt is missing run identity fields")
    if day_index != int(read_state(paths.state_file).get("next_day_index", 1)):
        raise RuntimeError("receipt day_index does not match current course next_day_index")
    deadline = datetime.fromisoformat(str(receipt.get("overnight_until")))
    expected_deadline = planned_closeout_for_run_date(run_date)
    closeout_end = closeout_window_end(deadline)
    now = datetime.now(TIMEZONE)
    if deadline != expected_deadline or not (deadline <= now < closeout_end):
        raise RuntimeError("interactive finalization is allowed only in the run's recorded 15:00–16:00 closeout window")

    run_dir = receipt_path.parent
    baseline = json.loads((run_dir / "baseline.json").read_text(encoding="utf-8"))
    if baseline.get("run_id") != run_id or baseline.get("day_index") != day_index or baseline.get("report_existed_before") is not False:
        raise RuntimeError("original run baseline identity/report state is not eligible for closeout")
    knowledge_before = baseline.get("knowledge_sha256_before")
    if not isinstance(knowledge_before, dict) or not knowledge_before:
        raise RuntimeError("original knowledge snapshot is missing from baseline")
    report_path = paths.daily_root / f"{daily_file_stem(run_date, day_index)}.md"
    if Path(str(receipt.get("report"))).resolve() != report_path.resolve():
        raise RuntimeError("receipt report path does not match canonical daily report")
    attestation_path = run_dir / "interactive-closeout-attestation.json"
    if not attestation_path.is_file():
        raise RuntimeError("interactive closeout attestation is missing")
    attestation = json.loads(attestation_path.read_text(encoding="utf-8"))
    if (
        attestation.get("status") != "closeout-turn-completed"
        or attestation.get("run_id") != run_id
        or attestation.get("session_id") != session_id
        or attestation.get("closeout_event_id") != "closeout"
        or attestation.get("hard_deadline") != deadline.isoformat()
    ):
        raise RuntimeError("interactive closeout attestation does not match receipt identity/deadline")
    closeout_at = datetime.fromisoformat(str(attestation.get("closeout_at")))
    if not (deadline <= closeout_at < closeout_end) or closeout_at > now:
        raise RuntimeError("attested closeout timestamp is outside the recorded closeout window")
    report_hash = hashlib.sha256(report_path.read_bytes()).hexdigest()
    if attestation.get("report_sha256") != report_hash:
        raise RuntimeError("report changed after interactive closeout attestation")
    report_text = report_path.read_text(encoding="utf-8")
    if f"closeout_event_id: `closeout`" not in report_text or session_id not in report_text:
        raise RuntimeError("daily report does not identify the same-session closeout event")

    clock_state_path = run_dir / "clock-state.json"
    if not clock_state_path.is_file():
        raise RuntimeError("run-local session clock state is missing")
    clock_state = json.loads(clock_state_path.read_text(encoding="utf-8"))
    if (
        clock_state.get("thread") != session_id
        or clock_state.get("run_date") != run_date
        or clock_state.get("day_index") != day_index
        or clock_state.get("deadline") != deadline.isoformat()
        or clock_state.get("events", {}).get("closeout", {}).get("status") != "queued"
    ):
        raise RuntimeError("run-local clock ledger does not prove the same-session closeout reminder was queued")

    preflight = run_preflight(root)
    if preflight["exit"] != 0:
        raise RuntimeError("automation preflight failed during interactive closeout: " + preflight["stderr_tail"])
    checks = run_checks(root, report_path, None, knowledge_before, day_index=day_index)
    coverage = checks.get("curriculum_coverage") or {}
    coverage_valid = bool(coverage.get("valid"))
    requested_card_complete = day_index in coverage.get("completed_day_indices", [])
    closeout_on_time = not bool(attestation.get("window_missed", False))
    deliverables_passed = (
        checks["preflight"]["exit"] == 0
        and checks["report_exists"]
        and checks["report_changed"]
        and checks["report_valid"]
        and checks["durable_knowledge"]["valid"]
        and checks["lint_exit"] == 0
        and checks["git_diff_check_exit"] == 0
        and coverage_valid
        and closeout_on_time
    )
    success = deliverables_passed and requested_card_complete
    next_day_index = int(coverage.get("next_day_index", day_index + 1))
    next_prompt_file: Path | None = None
    next_prompt_error: str | None = None
    if deliverables_passed and next_day_index <= TOTAL_DAYS:
        try:
            next_prompt_file = prepare_next_prompt(paths, datetime.now(TIMEZONE).date().isoformat(), next_day_index)
        except Exception as exc:
            deliverables_passed = success = False
            next_prompt_error = str(exc)

    continuation_runs = receipt.get("continuation_runs", [])
    if not isinstance(continuation_runs, list):
        raise RuntimeError("receipt continuation_runs must be a list")
    existing_closeout = receipt.get("closeout_turn")
    turn_number = max((int(item.get("number", 0)) for item in continuation_runs if isinstance(item, dict)), default=0)
    if existing_closeout is None:
        turn_number += 1
        continuation_runs.append(
            {
                "number": turn_number,
                "study_continuation_number": None,
                "kind": "closeout",
                "returncode": 0,
                "prompt": str(attestation_path),
                "events": None,
                "last_message": None,
                "time_snapshot": attestation.get("time_snapshot"),
                "interactive_session_closeout": True,
            }
        )
    closeout_turn = {
        "number": turn_number,
        "returncode": 0,
        "prompt": str(attestation_path),
        "events": None,
        "window_missed": bool(attestation.get("window_missed", False)),
        "time_snapshot": attestation.get("time_snapshot"),
        "interactive_session_closeout": True,
    }
    run_status = "completed" if success else "completed-partial" if deliverables_passed else "failed-verification"
    receipt.update(
        {
            "status": run_status,
            "counted_in_substantive_test": success,
            "exit_code": 0,
            "resume_command": build_resume_command(root, session_id),
            "checks": checks,
            "finished_at": datetime.now(TIMEZONE).isoformat(),
            "continuation_count": int(receipt.get("continuation_count", 0)),
            "continuation_batch_count": int(receipt.get("continuation_batch_count", 0)),
            "continuation_batches": int(receipt.get("continuation_batches", 1)),
            "continuation_runs": continuation_runs,
            "closeout_turn": closeout_turn,
            "closeout_window_missed": bool(attestation.get("window_missed", False)),
            "study_window_closed": True,
            "closeout_on_time": closeout_on_time,
            "completed_day_indices": coverage.get("completed_day_indices", []),
            "partial_day_indices": coverage.get("partial_day_indices", []),
            "curriculum_cards_completed": coverage.get("curriculum_cards_completed", 0),
            "next_day_index": next_day_index,
            "deliverables_passed": deliverables_passed,
            "next_prompt_file": str(next_prompt_file) if next_prompt_file else None,
            "next_prompt_error": next_prompt_error,
            "interactive_closeout_attestation": str(attestation_path),
        }
    )
    if success:
        state = read_state(paths.state_file)
        if int(state.get("next_day_index", 1)) == day_index:
            state = update_state_for_curriculum_cards(state, run_id, run_date, coverage)
            write_json_atomic(paths.state_file, state)
        elif not (int(state.get("next_day_index", 1)) == next_day_index and state.get("last_run_id") == run_id):
            raise RuntimeError("course state changed unexpectedly during interactive closeout")
    write_json_atomic(receipt_path, receipt)
    print(json.dumps(receipt, ensure_ascii=False, indent=2))
    return 0 if deliverables_passed else 1


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
    parser.add_argument(
        "--resume-receipt",
        type=Path,
        default=None,
        help="recover an interrupted runner loop using the existing run.json session_id; never creates a new session",
    )
    parser.add_argument(
        "--finalize-receipt",
        type=Path,
        default=None,
        help="run ordinary validation/state/prompt gates for a closeout already performed in the same interactive receipt session",
    )
    parser.add_argument(
        "--until",
        default=None,
        help="explicitly override the default run-date+1 15:00 closeout (HH:MM Asia/Shanghai)",
    )
    parser.add_argument("--max-continuations", type=int, default=96)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    paths = get_paths(root)
    try:
        if args.max_continuations < 0:
            raise ValueError("--max-continuations must be non-negative")
        if args.mode == "daily-learning" and args.max_continuations == 0:
            raise ValueError("daily-learning requires --max-continuations greater than zero")
        schedule_deadline = parse_deadline(args.until) if args.until else None
        result = dry_run(paths, args.model, not args.no_search, args.reasoning_effort, args.mode)
        if args.dry_run:
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return 0
        validate_root(root)
        if args.resume_receipt is not None and args.finalize_receipt is not None:
            raise RuntimeError("--resume-receipt and --finalize-receipt are mutually exclusive")
        if args.finalize_receipt is not None:
            if args.mode != "daily-learning" or args.prepare_prompt is not None or args.prompt_file is not None:
                raise RuntimeError("--finalize-receipt requires daily-learning mode and cannot prepare/override a prompt")
            return finalize_interactive_closeout(paths, args.finalize_receipt)
        if args.resume_receipt is not None:
            if args.mode != "daily-learning" or args.prepare_prompt is not None or args.prompt_file is not None:
                raise RuntimeError("--resume-receipt requires the daily-learning mode and cannot prepare/override a prompt")
            return resume_running_receipt(paths, args.resume_receipt, args)
        state = read_state(paths.state_file)
        state_next_day_index = int(state.get("next_day_index", 1))
        day_index = state_next_day_index if args.day_index == "auto" else int(args.day_index)
        if args.prepare_prompt is not None:
            if args.day_index == "auto":
                day_index = int(state.get("next_day_index", 1))
            prompt_date = local_date()
            prompt_run_id = f"prompt-{prompt_date}-day-{day_index:02d}"
            prompt_deadline = (
                schedule_deadline
                if args.until and schedule_deadline
                else planned_closeout_for_run_date(prompt_date)
                if args.mode == "daily-learning"
                else None
            )
            prompt = render_prompt(
                paths,
                prompt_run_id,
                prompt_date,
                day_index,
                args.mode,
                window_deadline=prompt_deadline,
            )
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
        if args.mode == "daily-learning" and day_index != state_next_day_index:
            raise RuntimeError(
                f"daily-learning must start at next_day_index={state_next_day_index}; requested day_index={day_index}"
            )
        phase = phase_for_day(day_index)
        run_date = local_date()
        if schedule_deadline is None and args.mode == "daily-learning":
            schedule_deadline = planned_closeout_for_run_date(run_date)
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
        run_started_at = datetime.now(TIMEZONE)
        initial_closeout_snapshot = (
            closeout_snapshot(
                run_started_at,
                schedule_deadline,
                next_scheduled_start_for_run_date(run_date),
            )
            if args.mode == "daily-learning" and schedule_deadline is not None
            else None
        )
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
            "continuation_batch_count": 0,
            "continuation_batches": 1,
            "counted_in_substantive_test": False,
            "session_mode": SESSION_MODE,
            "session_reuse": False,
            "session_scope": "one-new-session-for-each-schedule-run",
            "codex_home": str(validate_codex_home()),
            "status": "running",
            "started_at": run_started_at.isoformat(),
            "report": str(report_path),
            "completed_day_indices": [],
            "partial_day_indices": [],
            "curriculum_cards_completed": 0,
            "closeout_window_ends_at": (
                closeout_window_end(schedule_deadline).isoformat() if schedule_deadline else None
            ),
            "last_closeout_snapshot": initial_closeout_snapshot,
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
            prompt = render_prompt(
                paths,
                run_id,
                run_date,
                day_index,
                args.mode,
                args.prompt_file,
                window_deadline=schedule_deadline,
                runtime_now=run_started_at if args.mode == "daily-learning" else None,
            )
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
            continuation_total = 0
            continuation_batches = 1
            turn_number = 0
            last_continuation_prompt: Path | None = None
            closeout_turn: dict[str, Any] | None = None
            closeout_window_missed = False
            if (
                schedule_deadline is not None
                and args.mode == "daily-learning"
                and final_returncode == 0
                and session_id
            ):
                while True:
                    continuation_now = datetime.now(TIMEZONE)
                    action = next_continuation_action(
                        continuation_now,
                        schedule_deadline,
                        continuation_count,
                        args.max_continuations,
                        closeout_completed=closeout_turn is not None,
                    )
                    if action == "finalize":
                        break
                    if action == "rollover":
                        continuation_batches += 1
                        continuation_count = 0
                        receipt.update(
                            {
                                "continuation_batches": continuation_batches,
                                "continuation_batch_count": 0,
                                "continuation_count": continuation_total,
                                "last_closeout_snapshot": closeout_snapshot(
                                    continuation_now,
                                    schedule_deadline,
                                    next_scheduled_start_for_run_date(run_date),
                                ),
                            }
                        )
                        write_json_atomic(run_dir / "run.json", receipt)
                        continue
                    is_closeout = action == "closeout"
                    if is_closeout:
                        closeout_window_missed = not should_run_closeout_turn(
                            continuation_now, schedule_deadline
                        )
                    else:
                        continuation_count += 1
                        continuation_total += 1
                    turn_number += 1
                    turn_snapshot = closeout_snapshot(
                        continuation_now,
                        schedule_deadline,
                        next_scheduled_start_for_run_date(run_date),
                    )
                    continuation_prompt = render_continuation_prompt(
                        paths,
                        run_id,
                        run_date,
                        day_index,
                        turn_number,
                        schedule_deadline,
                        now=continuation_now,
                    )
                    continuation_prompt_path = run_dir / f"continuation-{turn_number:03d}-prompt.md"
                    continuation_prompt_path.write_text(continuation_prompt, encoding="utf-8")
                    last_continuation_prompt = continuation_prompt_path
                    continuation_events = run_dir / f"continuation-{turn_number:03d}-events.jsonl"
                    continuation_stderr = run_dir / f"continuation-{turn_number:03d}-stderr.log"
                    continuation_last = run_dir / f"continuation-{turn_number:03d}-last-message.md"
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
                            "number": turn_number,
                            "study_continuation_number": continuation_total if not is_closeout else None,
                            "kind": "closeout" if is_closeout else "study",
                            "returncode": continuation_rc,
                            "events": str(continuation_events),
                            "prompt": str(continuation_prompt_path),
                            "last_message": str(continuation_last),
                            "time_snapshot": turn_snapshot,
                        }
                    )
                    if is_closeout:
                        closeout_turn = {
                            "number": turn_number,
                            "returncode": continuation_rc,
                            "prompt": str(continuation_prompt_path),
                            "events": str(continuation_events),
                            "window_missed": closeout_window_missed,
                            "time_snapshot": turn_snapshot,
                        }
                    receipt.update(
                        {
                            "continuation_count": continuation_total,
                            "continuation_batch_count": continuation_count,
                            "continuation_batches": continuation_batches,
                            "continuation_runs": continuation_runs,
                            "session_id": session_id,
                            "last_closeout_snapshot": turn_snapshot,
                            "last_continuation_prompt": str(continuation_prompt_path),
                            "closeout_turn": closeout_turn,
                            "closeout_window_missed": closeout_window_missed,
                        }
                    )
                    write_json_atomic(run_dir / "run.json", receipt)
                    if continuation_rc != 0:
                        final_returncode = continuation_rc
                        break
                    if is_closeout:
                        break
                    if datetime.now(TIMEZONE) < schedule_deadline:
                        time_module.sleep(2)

            checks = run_checks(
                root,
                report_path,
                report_before,
                knowledge_before,
                day_index=day_index if args.mode == "daily-learning" else None,
            )
            coverage = checks.get("curriculum_coverage") or {}
            coverage_valid = args.mode != "daily-learning" or bool(coverage.get("valid"))
            requested_card_complete = (
                args.mode != "daily-learning"
                or day_index in coverage.get("completed_day_indices", [])
            )
            window_closed = args.mode != "daily-learning" or closeout_turn is not None
            closeout_on_time = (
                args.mode != "daily-learning"
                or (window_closed and not closeout_window_missed)
            )
            deliverables_passed = (
                final_returncode == 0
                and checks["preflight"]["exit"] == 0
                and checks["report_exists"]
                and checks["report_changed"]
                and checks["report_valid"]
                and checks["durable_knowledge"]["valid"]
                and checks["lint_exit"] == 0
                and checks["git_diff_check_exit"] == 0
                and coverage_valid
                and window_closed
                and closeout_on_time
            )
            success = deliverables_passed and requested_card_complete
            if session_id:
                receipt["resume_command"] = build_resume_command(root, session_id)
            next_prompt_file: Path | None = None
            next_prompt_error: str | None = None
            next_day_index = int(coverage.get("next_day_index", day_index + 1))
            if deliverables_passed and args.mode == "daily-learning" and next_day_index <= TOTAL_DAYS:
                try:
                    next_prompt_file = prepare_next_prompt(
                        paths,
                        datetime.now(TIMEZONE).date().isoformat(),
                        next_day_index,
                    )
                except Exception as exc:
                    deliverables_passed = False
                    success = False
                    next_prompt_error = str(exc)
            if next_prompt_error:
                run_status = "failed-verification"
            elif success:
                run_status = "completed"
            elif deliverables_passed:
                run_status = "completed-partial"
            else:
                run_status = "failed-verification"
            receipt.update(
                {
                    "status": run_status,
                    "counted_in_substantive_test": success and args.mode == "daily-learning",
                    "exit_code": final_returncode,
                    "session_id": session_id,
                    "failure_reason": extract_failure_reason(lines),
                    "checks": checks,
                    "finished_at": datetime.now(TIMEZONE).isoformat(),
                    "continuation_count": continuation_total,
                    "continuation_batch_count": continuation_count,
                    "continuation_batches": continuation_batches,
                    "continuation_runs": continuation_runs,
                    "closeout_turn": closeout_turn,
                    "closeout_window_missed": closeout_window_missed,
                    "study_window_closed": window_closed,
                    "closeout_on_time": closeout_on_time,
                    "completed_day_indices": coverage.get("completed_day_indices", []),
                    "partial_day_indices": coverage.get("partial_day_indices", []),
                    "curriculum_cards_completed": coverage.get("curriculum_cards_completed", 0),
                    "next_day_index": next_day_index,
                    "deliverables_passed": deliverables_passed,
                    "next_prompt_file": str(next_prompt_file) if next_prompt_file else None,
                    "next_prompt_error": next_prompt_error,
                }
            )
            if success and args.mode == "daily-learning":
                state = update_state_for_curriculum_cards(
                    state,
                    run_id,
                    run_date,
                    coverage,
                )
                write_json_atomic(paths.state_file, state)
            write_json_atomic(run_dir / "run.json", receipt)
            print(json.dumps(receipt, ensure_ascii=False, indent=2))
            return 0 if deliverables_passed else 1
    except Exception as exc:
        print(json.dumps({"status": "runner-error", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
