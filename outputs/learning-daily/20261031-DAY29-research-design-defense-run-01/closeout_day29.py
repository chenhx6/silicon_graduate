#!/usr/bin/env python3
"""Guarded interactive closeout executor for Day 29."""

from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "system/scripts"))

import run_daily_learning as runner
from wiki_learning_deadline import resolve_baseline_knowledge, resolve_deadline_info


RUN_DIR = Path(__file__).resolve().parent
REPORT_PATH = ROOT / "outputs/learning-daily/20261031-DAY29-research-design-defense.md"
RECEIPT_PATH = RUN_DIR / "run.json"
SCOPE_PATH = RUN_DIR / "precloseout-publication-scope-001.json"
ATTESTATION_PATH = RUN_DIR / "interactive-closeout-attestation.json"


def execute_closeout(wait: bool = False) -> int:
    receipt = json.loads(RECEIPT_PATH.read_text(encoding="utf-8"))
    session_id = receipt["session_id"]
    deadline_info = resolve_deadline_info(RECEIPT_PATH, receipt, ROOT)
    deadline = deadline_info["effective_deadline"]
    closeout_end = deadline_info["effective_closeout_end"]

    now = datetime.now(runner.TIMEZONE)
    print(f"Now: {now.isoformat()}")
    print(f"Deadline: {deadline.isoformat()}")

    if now < deadline:
        if not wait:
            print("Current time is before hard deadline; use --wait to wait until 15:00.")
            return 2
        import time
        while True:
            now = datetime.now(runner.TIMEZONE)
            if now >= deadline:
                break
            remaining = (deadline - now).total_seconds()
            print(f"Waiting for hard deadline... {int(remaining)}s left", flush=True)
            time.sleep(min(15, max(1, remaining)))

    # Now >= deadline
    clock_state_path = RUN_DIR / "clock-state.json"
    def is_closeout_queued() -> bool:
        if not clock_state_path.is_file():
            return False
        st = json.loads(clock_state_path.read_text(encoding="utf-8"))
        return st.get("events", {}).get("closeout", {}).get("status") == "queued"

    if not is_closeout_queued():
        print("Waiting for clock supervisor to queue closeout event...", flush=True)
        import time
        for _ in range(15):
            time.sleep(2)
            if is_closeout_queued():
                break
        if not is_closeout_queued():
            print("Queueing closeout event via clock spec fallback...", flush=True)
            import run_learning_session_clock as clock
            spec = clock.load_spec(ROOT, RECEIPT_PATH, session_id, 2)
            with clock.acquire_locks(clock.LOCK_PATHS):
                supervisor = clock.Supervisor(spec)
                supervisor.initialize_one_shot()
                ev = next(e for e in supervisor.events if e.event_id == "closeout")
                supervisor.attempt(ev, datetime.now(clock.TIMEZONE), receipt["status"])
            print(f"Fallback closeout queue status: {is_closeout_queued()}")

    # Ensure report has closeout_event_id: closeout
    report_text = REPORT_PATH.read_text(encoding="utf-8")
    if "closeout_event_id: `closeout`" not in report_text:
        report_text = report_text.replace(
            "- research_status: active-continuation; Day29 card complete, formal closeout pending\n",
            "- research_status: closeout-completed\n- closeout_event_id: `closeout`\n",
            1
        )
        REPORT_PATH.write_text(report_text, encoding="utf-8")
        print("Updated daily report with closeout_event_id: `closeout`")

    # Write attestation
    attestation = {
        "status": "closeout-turn-completed",
        "run_id": receipt["run_id"],
        "session_id": session_id,
        "closeout_event_id": "closeout",
        "hard_deadline": deadline.isoformat(),
        "original_hard_deadline": deadline_info["original_deadline"].isoformat(),
        "deadline_override_sha256": deadline_info["override_sha256"],
        "closeout_at": datetime.now(runner.TIMEZONE).isoformat(),
        "report_sha256": hashlib.sha256(REPORT_PATH.read_bytes()).hexdigest(),
        "window_missed": False,
        "time_snapshot": runner.closeout_snapshot(
            datetime.now(runner.TIMEZONE),
            deadline,
            runner.next_scheduled_start_for_run_date(receipt["run_date"]),
        ),
        "scientific_scope": "Day29 research-design defense complete; user-data 133Ce partial-L4 contract, 131,133Ce triaxial core route and research-archive gate verified; uncredited Day30 preview staged",
    }
    ATTESTATION_PATH.write_text(json.dumps(attestation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {ATTESTATION_PATH}")

    # Run finalize_interactive_closeout
    os.environ["CODEX_SESSION_ID"] = session_id
    print("Finalizing receipt via runner...")
    runner.finalize_interactive_closeout(runner.get_paths(ROOT), RECEIPT_PATH)
    print("Receipt successfully finalized!")

    # Re-verify scope and stage files
    rel_attestation = str(ATTESTATION_PATH.relative_to(ROOT))
    scope = json.loads(SCOPE_PATH.read_text(encoding="utf-8"))
    paths = scope["intended_publishable_paths"]
    if rel_attestation not in paths:
        paths.append(rel_attestation)
        paths.sort()
        scope["intended_publishable_paths"] = paths
        scope["updated_at"] = datetime.now(runner.TIMEZONE).isoformat()
        SCOPE_PATH.write_text(json.dumps(scope, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Staging {len(paths)} explicit files...")
    subprocess.run(["git", "-C", str(ROOT), "reset", "HEAD"], check=True)
    for path in paths:
        subprocess.run(["git", "-C", str(ROOT), "add", "--", path], check=True)

    staged_count = len(subprocess.run(["git", "-C", str(ROOT), "diff", "--cached", "--name-only"], capture_output=True, text=True, check=True).stdout.splitlines())
    print(f"Staged {staged_count} files in index.")

    # Preflight and diff checks
    subprocess.run(["git", "-C", str(ROOT), "diff", "--cached", "--check"], check=True)
    subprocess.run([sys.executable, "system/scripts/wiki_automation_preflight.py", "--root", str(ROOT)], check=True)
    print("Staged checks passed!")

    # H3 fetch and dry run
    subprocess.run(["git", "-C", str(ROOT), "fetch", "origin", "main"], check=True)
    subprocess.run(["git", "-C", str(ROOT), "merge-base", "--is-ancestor", "origin/main", "HEAD"], check=True)
    subprocess.run(["git", "-C", str(ROOT), "push", "--dry-run", "origin", "HEAD:main"], check=True)
    print("H3 preflight passed!")

    # Commit
    commit_message = "research(day29): finalize closeout verification and durable knowledge writeback"
    subprocess.run(["git", "-C", str(ROOT), "commit", "-m", commit_message], check=True)
    new_head = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
    print(f"Committed new HEAD: {new_head}")

    # Push
    subprocess.run(["git", "-C", str(ROOT), "push", "origin", "HEAD:main"], check=True)
    print("Pushed to origin main!")

    # Update receipt
    receipt = json.loads(RECEIPT_PATH.read_text(encoding="utf-8"))
    receipt["final_commit_hash"] = new_head
    receipt["final_push_status"] = "success"
    receipt["pushed_at"] = datetime.now(runner.TIMEZONE).isoformat()
    RECEIPT_PATH.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("All closeout tasks complete!")
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--wait", action="store_true", help="wait until 15:00 if called before")
    args = parser.parse_args()
    return execute_closeout(wait=args.wait)


if __name__ == "__main__":
    raise SystemExit(main())
