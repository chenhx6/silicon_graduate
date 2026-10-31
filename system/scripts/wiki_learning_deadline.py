#!/usr/bin/env python3
"""Pure resolver for Wiki learning session deadlines, baselines, and active runs.

This module holds no locks, creates no sessions, starts no daemons, and mutates
no files. It provides shared, auditable validation for:
1. Schedule deadlines, including explicit immutable user override sidecars.
2. Baseline knowledge snapshots, including explicit reconstructed entry witnesses.
3. Active running receipts to prevent unintended duplicate runs.
"""

from __future__ import annotations

import hashlib
import json
import re
from datetime import date, datetime, time as daytime, timedelta
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


TIMEZONE = ZoneInfo("Asia/Shanghai")
DEFAULT_CLOSEOUT_TIME = "15:00"
DEFAULT_SCHEDULE_START_TIME = "16:00"
TOTAL_DAYS = 30
SESSION_MODE = "new-session-per-run"


def _bytes(path: Path) -> bytes:
    cursor = Path(path.absolute().anchor)
    for part in path.absolute().parts[1:]:
        cursor /= part
        if cursor.is_symlink():
            raise RuntimeError(f"symlink is not allowed: {cursor}")
    return path.read_bytes()


def _object(path: Path) -> dict[str, Any]:
    value = json.loads(_bytes(path))
    if not isinstance(value, dict):
        raise RuntimeError(f"JSON object required: {path}")
    return value


def _bound_object(run_dir: Path, name: Any, expected_hash: Any) -> tuple[dict[str, Any], Path, str]:
    if not isinstance(name, str) or not name or Path(name).name != name or name in {".", ".."}:
        raise RuntimeError("bound evidence must be a run-local filename")
    if not isinstance(expected_hash, str) or not re.fullmatch(r"[0-9a-f]{64}", expected_hash):
        raise RuntimeError("bound evidence requires an explicit sha256")
    path = run_dir / name
    raw = _bytes(path)
    actual = hashlib.sha256(raw).hexdigest()
    if actual != expected_hash:
        raise RuntimeError(f"bound evidence sha256 mismatch: {path.name}")
    value = json.loads(raw)
    if not isinstance(value, dict):
        raise RuntimeError(f"JSON object required: {path}")
    return value, path, actual


def _knowledge_map(value: Any) -> dict[str, str]:
    if not isinstance(value, dict) or not value:
        raise RuntimeError("baseline knowledge snapshot is missing")
    for name, digest in value.items():
        if (not isinstance(name, str) or not name.startswith("knowledge/") or not name.endswith(".md")
                or ".." in Path(name).parts or Path(name).is_absolute()
                or not isinstance(digest, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", digest)):
            raise RuntimeError("invalid baseline knowledge path/hash")
    return value


def aware_datetime(value: Any, field: str = "timestamp") -> datetime:
    if isinstance(value, datetime):
        parsed = value
    elif isinstance(value, str):
        try:
            parsed = datetime.fromisoformat(value)
        except ValueError as exc:
            raise ValueError(f"invalid {field}: {value}") from exc
    else:
        raise ValueError(f"{field} must be an ISO timestamp or datetime object")
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError(f"{field} must have an explicit timezone")
    return parsed.astimezone(TIMEZONE)


def planned_closeout_for_run_date(run_date: str) -> datetime:
    """Return the default run_date + 1 15:00 Asia/Shanghai closeout timestamp."""
    run_day = datetime.fromisoformat(run_date).date()
    hour, minute = (int(part) for part in DEFAULT_CLOSEOUT_TIME.split(":"))
    return datetime.combine(run_day + timedelta(days=1), daytime(hour, minute), tzinfo=TIMEZONE)


def next_scheduled_start_for_run_date(run_date: str) -> datetime:
    """Return the next scheduled start time: run_date + 1 16:00 Asia/Shanghai."""
    run_day = datetime.fromisoformat(run_date).date()
    hour, minute = (int(part) for part in DEFAULT_SCHEDULE_START_TIME.split(":"))
    return datetime.combine(run_day + timedelta(days=1), daytime(hour, minute), tzinfo=TIMEZONE)


def closeout_window_end(deadline: datetime) -> datetime:
    """Closeout hour extends exactly one hour past the research deadline."""
    return deadline + timedelta(hours=1)


def _has_completed_manual_closeout(
    run_dir: Path,
    receipt: dict[str, Any],
    current: datetime,
) -> bool:
    """Recognize a verified manual closeout when the runner receipt is stale.

    A foreground runner can be interrupted after the Codex session continues
    elsewhere. In that case the session reconciliation writes a final-session
    receipt while the original run.json may still say ``running``. Only a
    sidecar with matching run identity, a completed status, and a past
    closeout timestamp can suppress the stale active-run guard.
    """
    completed_statuses = {"completed", "completed-content-final-not-pushed"}
    for sidecar in sorted(run_dir.glob("final-session-receipt-*.json"), reverse=True):
        try:
            evidence = _object(sidecar)
            if (
                evidence.get("run_id") != receipt.get("run_id")
                or evidence.get("day_index") != receipt.get("day_index")
                or evidence.get("status") not in completed_statuses
            ):
                continue
            closed_at = aware_datetime(evidence.get("closed_at"), "manual closeout closed_at")
        except (OSError, RuntimeError, ValueError, TypeError):
            continue
        if closed_at <= current:
            return True
    return False


def resolve_deadline_info(
    receipt_path: Path,
    receipt: dict[str, Any],
    root: Path,
) -> dict[str, Any]:
    """Resolve the original and effective deadline contract for a run receipt.

    When no override is present, effective deadline equals original planned 15:00.
    When an override sidecar is present, verifies identity, sha256 binding,
    original receipt snapshot, and explicit user authorization fields.
    Original receipt fields are preserved and never silently overwritten.
    """
    run_id = receipt.get("run_id")
    run_date = receipt.get("run_date")
    session_id = receipt.get("session_id")
    day_index = receipt.get("day_index")
    if not run_date or not session_id or type(day_index) is not int or not 1 <= day_index <= TOTAL_DAYS:
        raise RuntimeError("receipt is missing required identity fields")

    overnight_raw = receipt.get("overnight_until")
    if not overnight_raw:
        raise RuntimeError("receipt is missing overnight_until")
    recorded_overnight = aware_datetime(overnight_raw, "overnight_until")
    planned_default = planned_closeout_for_run_date(run_date)
    run_dir = receipt_path.parent
    try:
        relative = receipt_path.resolve().relative_to((root / "outputs/learning-daily").resolve())
    except ValueError as exc:
        raise RuntimeError("deadline receipt is outside the learning run directory") from exc
    if len(relative.parts) != 2 or relative.name != "run.json":
        raise RuntimeError("deadline receipt must be a run-local run.json")
    if receipt.get("project_root") not in (None, str(root.resolve())):
        raise RuntimeError("deadline receipt project_root mismatch")

    override_receipt_name = receipt.get("deadline_override_receipt")
    if not override_receipt_name:
        if any(receipt.get(k) is not None for k in (
            "effective_overnight_until", "effective_closeout_window_ends_at", "deadline_override_sha256"
        )):
            raise RuntimeError("effective deadline fields require an explicit override receipt")
        if recorded_overnight != planned_default:
            raise RuntimeError(
                f"receipt deadline {recorded_overnight.isoformat()} does not match "
                f"planned default {planned_default.isoformat()} without explicit override"
            )
        closeout_end = closeout_window_end(planned_default)
        if receipt.get("closeout_window_ends_at") is not None and aware_datetime(receipt["closeout_window_ends_at"]) != closeout_end:
            raise RuntimeError("closeout_window_ends_at must equal overnight_until + 1 hour")
        return {
            "original_deadline": planned_default,
            "effective_deadline": planned_default,
            "effective_closeout_end": closeout_end,
            "is_override": False,
            "override_receipt": None,
            "override_sha256": None,
            "authorization": None,
        }

    # Explicit override sidecar resolution
    if not isinstance(run_id, str) or not run_id:
        raise RuntimeError("override requires run_id")
    override_data, override_path, actual_override_sha = _bound_object(
        run_dir, override_receipt_name, receipt.get("deadline_override_sha256")
    )
    if override_data.get("schema_version") != 1:
        raise RuntimeError("unsupported deadline override schema_version")
    if override_data.get("run_id") != run_id:
        raise RuntimeError("deadline override run_id does not match receipt")
    if override_data.get("session_id") != session_id:
        raise RuntimeError("deadline override session_id does not match receipt")
    if override_data.get("authorization_kind") != "explicit-current-user-instruction" or not isinstance(override_data.get("user_instruction"), str) or not override_data["user_instruction"].strip():
        raise RuntimeError("deadline override requires explicit user authorization")
    recorded_at = aware_datetime(override_data.get("recorded_at"), "override recorded_at")

    # Check original and effective timestamps in override
    orig_str = override_data.get("original_research_deadline") or override_data.get("original_overnight_until")
    if not orig_str:
        raise RuntimeError("deadline override missing original_research_deadline")
    orig_deadline = aware_datetime(orig_str, "original_research_deadline")
    if orig_deadline != planned_default:
        raise RuntimeError("override original deadline does not equal default planned closeout")
    if recorded_overnight != orig_deadline or aware_datetime(receipt.get("closeout_window_ends_at")) != orig_deadline + timedelta(hours=1):
        raise RuntimeError("override must preserve original receipt timing fields")

    eff_str = override_data.get("effective_research_deadline") or override_data.get("effective_overnight_until")
    if not eff_str:
        raise RuntimeError("deadline override missing effective_research_deadline")
    eff_deadline = aware_datetime(eff_str, "effective_research_deadline")
    if eff_deadline <= orig_deadline:
        raise RuntimeError("effective override deadline must be after original deadline")
    if eff_deadline.date() != orig_deadline.date() or recorded_at >= eff_deadline:
        raise RuntimeError("override must be recorded before its effective cutoff on the original cutoff date")

    eff_end_str = override_data.get("effective_closeout_window_ends_at")
    if not eff_end_str:
        raise RuntimeError("deadline override missing effective_closeout_window_ends_at")
    eff_closeout_end = aware_datetime(eff_end_str, "effective_closeout_window_ends_at")
    if eff_closeout_end != eff_deadline + timedelta(hours=1):
        raise RuntimeError("effective_closeout_window_ends_at must equal effective_deadline + 1 hour")

    # Verify original receipt snapshot binding if present in sidecar
    snap_data, _, _ = _bound_object(run_dir, override_data.get("original_receipt_snapshot"), override_data.get("original_receipt_snapshot_sha256"))
    for key in ("run_id", "session_id", "run_date", "day_index"):
        if snap_data.get(key) != receipt.get(key):
            raise RuntimeError(f"original receipt snapshot {key} mismatch")
    if aware_datetime(snap_data.get("overnight_until")) != planned_default:
        raise RuntimeError("original receipt snapshot overnight_until mismatch")
    if aware_datetime(snap_data.get("closeout_window_ends_at")) != planned_default + timedelta(hours=1):
        raise RuntimeError("original receipt snapshot closeout end mismatch")

    # Verify receipt fields preserve original while exposing effective
    for key, expected in (("original_overnight_until", orig_deadline), ("effective_overnight_until", eff_deadline), ("effective_closeout_window_ends_at", eff_closeout_end)):
        if aware_datetime(receipt.get(key), key) != expected:
            raise RuntimeError(f"receipt {key} mismatch")

    return {
        "original_deadline": orig_deadline,
        "effective_deadline": eff_deadline,
        "effective_closeout_end": eff_closeout_end,
        "is_override": True,
        "override_receipt": override_receipt_name,
        "override_sha256": actual_override_sha,
        "authorization": override_data.get("user_instruction") or override_data.get("authorization_kind"),
    }


def resolve_baseline_knowledge(
    run_dir: Path, receipt: dict[str, Any], root: Path, *, now: datetime | None = None,
) -> tuple[dict[str, str], dict[str, Any]]:
    """Validate an original baseline or a hash-bound, explicitly reconstructed witness.

    Reconstruction does not manufacture a runner entry stat. The returned metadata
    keeps its historical HEAD/status evidence kind and its original observation time.
    """
    std_path = run_dir / "baseline.json"
    if std_path.is_file():
        baseline = _object(std_path)
        for key in ("run_id", "day_index"):
            if baseline.get(key) != receipt.get(key):
                raise RuntimeError("baseline.json identity does not match receipt")
        if baseline.get("session_id") not in (None, receipt.get("session_id")):
            raise RuntimeError("baseline.json session does not match receipt")
        if baseline.get("report_existed_before") is not False:
            raise RuntimeError("baseline.json does not prove report absent at entry")
        return _knowledge_map(baseline.get("knowledge_sha256_before")), {
            "kind": "standard-baseline", "path": str(std_path),
            "sha256": hashlib.sha256(std_path.read_bytes()).hexdigest(),
        }
    rec, rec_path, rec_sha = _bound_object(
        run_dir, receipt.get("baseline_reconstruction_receipt"),
        receipt.get("baseline_reconstruction_sha256"),
    )
    if rec.get("kind") != "reconstructed-entry-witness":
        raise RuntimeError("unsupported baseline reconstruction kind")
    for key in ("run_id", "session_id", "run_date", "day_index"):
        if rec.get(key) != receipt.get(key):
            raise RuntimeError(f"baseline reconstruction {key} mismatch")
    src, src_path, src_sha = _bound_object(run_dir, rec.get("source_baseline"), rec.get("source_baseline_sha256"))
    proof, proof_path, proof_sha = _bound_object(run_dir, rec.get("evidence_file"), rec.get("evidence_sha256"))
    observed = aware_datetime(src.get("observed_at"), "source baseline observed_at")
    reconstructed = aware_datetime(rec.get("recorded_at"), "reconstruction recorded_at")
    if reconstructed < observed:
        raise RuntimeError("baseline reconstruction predates its source")
    if reconstructed > aware_datetime(now or datetime.now(TIMEZONE), "baseline verification time"):
        raise RuntimeError("baseline reconstruction recorded_at cannot be in the future")
    if rec.get("source_observed_at") != src.get("observed_at") or rec.get("source_head") != src.get("head"):
        raise RuntimeError("baseline reconstruction source provenance mismatch")
    if not isinstance(src.get("head"), str) or not re.fullmatch(r"[0-9a-f]{40}", src["head"]):
        raise RuntimeError("baseline source HEAD must be a Git object identity")
    kb = _knowledge_map(src.get("knowledge_sha256"))
    if (proof.get("source_sha256") != src_sha or proof.get("head") != src["head"]
            or proof.get("observed_at") != src["observed_at"]
            or proof.get("source_path") != src_path.relative_to(root).as_posix()
            or proof.get("baseline_knowledge_count") != len(kb)
            or proof.get("head_tree_knowledge_md_count") != len(kb)):
        raise RuntimeError("baseline proof is not bound to the original snapshot")
    if proof.get("all_717_head_content_matches_after_explained_EOL") is not True:
        raise RuntimeError("baseline HEAD content verification is missing")
    mismatches = proof.get("baseline_vs_head_blob_mismatches")
    eol_proof = proof.get("mismatch_EOL_followup")
    if not isinstance(mismatches, list) or not isinstance(eol_proof, list):
        raise RuntimeError("baseline EOL evidence inventory is missing")
    if {x.get("path") for x in mismatches} != {x.get("path") for x in eol_proof}:
        raise RuntimeError("baseline mismatches lack corresponding EOL evidence")
    for item in eol_proof:
        if (item.get("path") not in kb or item.get("baseline_sha256") != kb[item["path"]]
                or item.get("current_matches_baseline") is not True
                or item.get("current_LF_normalized_equals_head") is not True):
            raise RuntimeError("baseline contains an unexplained content mismatch")
    report = Path(str(receipt.get("report"))).resolve().relative_to(root.resolve()).as_posix()
    witness = proof.get("report_absence_witness")
    if not isinstance(witness, dict):
        raise RuntimeError("baseline report absence witness is missing")
    status = src.get("status_porcelain")
    if not isinstance(status, str):
        raise RuntimeError("baseline captured porcelain is missing")
    ancestors = {p.as_posix() for p in Path(report).parents if p.as_posix() != "."}
    if (witness.get("report_relative_path") != report or witness.get("head_tree_absent") is not True
            or witness.get("captured_porcelain_has_exact_path") is not False
            or witness.get("captured_porcelain_untracked_ancestor_collapsing_report") != []
            or proof.get("head_tree_report_entries") != []
            or proof.get("report_status_entries") != [] or proof.get("knowledge_status_entries") != []
            or any(report in line or (line.startswith("?? ") and line[3:].rstrip("/") in ancestors)
                   for line in status.splitlines())):
        raise RuntimeError("baseline does not support report absence")
    if (witness.get("current_check_ignore_no_index_exit") != 1
            or not re.fullmatch(r"[0-9a-f]{64}", str(witness.get("head_gitignore_sha256", "")))
            or not isinstance(witness.get("boundary"), str) or not witness["boundary"].strip()):
        raise RuntimeError("baseline ignore-policy evidence or historical boundary is missing")
    return kb, {
        "kind": "reconstructed-entry-witness", "path": str(rec_path), "sha256": rec_sha,
        "source_baseline": str(src_path), "source_sha256": src_sha,
        "source_observed_at": src["observed_at"], "evidence_path": str(proof_path),
        "evidence_sha256": proof_sha, "report_absence_evidence_kind": "head-tree-status-and-ignore-policy",
        "boundary": witness["boundary"],
    }


def find_active_learning_receipt(
    daily_root: Path,
    root: Path,
    now: datetime | None = None,
) -> dict[str, Any] | None:
    """Scan for any running daily-learning receipt whose study or closeout window remains active.

    Returns None if no active run is in its window. Used to prevent duplicate
    runs or unintended session creation while an earlier run is actively ongoing.
    """
    current = aware_datetime(now, "now") if now else datetime.now(TIMEZONE)
    if not daily_root.is_dir():
        return None

    for run_dir in sorted(daily_root.glob("*-run-*"), reverse=True):
        if not run_dir.is_dir():
            continue
        receipt_file = run_dir / "run.json"
        if not receipt_file.is_file():
            continue
        receipt = _object(receipt_file)
        if (receipt.get("session_mode") != SESSION_MODE
                or receipt.get("project_root") != str(root.resolve())
                or receipt.get("schedule_id") != "wiki-daily-learning"):
            continue
        if receipt.get("status") not in {"running", "failed-verification"}:
            continue
        # Legacy incomplete receipts can lack identity/timing fields. Any
        # supported same-date extension has ended by 01:00 two days after
        # run_date, so historical entries past that bound cannot overlap now.
        # Recent invalid records still fail closed; no unverified raw timestamp
        # is used to authorize a new session.
        try:
            run_day = date.fromisoformat(receipt["run_date"])
        except (KeyError, ValueError, TypeError) as exc:
            raise RuntimeError(f"active receipt has invalid run_date: {receipt_file}") from exc
        latest_possible_end = datetime.combine(run_day + timedelta(days=2), daytime(1), tzinfo=TIMEZONE)
        if current >= latest_possible_end:
            continue
        if not receipt.get("session_id") and _has_completed_manual_closeout(run_dir, receipt, current):
            continue
        # Invalid effective metadata must fail closed rather than silently fall
        # back to an unverified raw timestamp and create a competing session.
        deadline_info = resolve_deadline_info(receipt_file, receipt, root)

        if current < deadline_info["effective_closeout_end"]:
            return {
                "run_dir": run_dir,
                "receipt_path": receipt_file,
                "receipt": receipt,
                "deadline_info": deadline_info,
            }

    return None
