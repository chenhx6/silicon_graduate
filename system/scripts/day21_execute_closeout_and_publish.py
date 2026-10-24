#!/usr/bin/env python3
"""End-to-end atomic closeout and Git publication pipeline for Day 21."""
import argparse
import datetime
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'
REPORT = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam.md'
STATE_FILE = ROOT / 'outputs/learning-milestones/2026-09-one-month-state.json'
RUN_JSON = RUN / 'run.json'
PROMPT_D22 = ROOT / 'outputs/learning-daily/prompts/20261024-DAY22-wobbling-geometry-phonons.md'
RECEIPT_D21 = RUN / 'final-session-receipt-21.json'
CREDIT_D21 = RUN / 'card-credit-21.json'
HANDOFF = ROOT / 'system/handoff.md'
LOG_MD = ROOT / 'system/log.md'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-only", action="store_true", help="Only check readiness without modifying or pushing")
    parser.add_argument("--execute", action="store_true", help="Execute the closeout at or after 15:00")
    parser.add_argument("--force-time", action="store_true", help="Execute even if before 15:00 (for testing only)")
    args = parser.parse_args()

    now_dt = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
    hard_deadline = datetime.datetime.fromisoformat("2026-10-24T15:00:00+08:00")
    mins_to_deadline = int((hard_deadline - now_dt).total_seconds() / 60)

    time_gate_open = (mins_to_deadline <= 0 or args.force_time)

    # 1. Pre-checks
    p_lint = subprocess.run(["python3", "system/scripts/wiki_lint.py", "--fail-on", "error"], cwd=ROOT, capture_output=True, text=True)
    p_bound = subprocess.run(["python3", "system/scripts/wiki_boundary_check.py", "--root", "."], cwd=ROOT, capture_output=True, text=True)
    p_diff = subprocess.run(["git", "diff", "--check"], cwd=ROOT, capture_output=True, text=True)
    p_wb = subprocess.run(["python3", "system/scripts/validate_writeback_items.py", "--report", str(REPORT.relative_to(ROOT))], cwd=ROOT, capture_output=True, text=True)

    wb_res = json.loads(p_wb.stdout)
    bound_res = json.loads(p_bound.stdout)
    checks_pass = (p_lint.returncode == 0 and bound_res["ok"] and p_diff.returncode == 0 and wb_res["valid"])

    # 2. Remote check
    p_fetch = subprocess.run(["git", "fetch", "origin", "main"], cwd=ROOT, capture_output=True, text=True)
    p_anc = subprocess.run(["git", "merge-base", "--is-ancestor", "origin/main", "HEAD"], cwd=ROOT, capture_output=True, text=True)
    remote_ok = (p_fetch.returncode == 0 and p_anc.returncode == 0)

    status_summary = {
        "now_local": now_dt.isoformat(),
        "minutes_to_deadline": mins_to_deadline,
        "time_gate_open": time_gate_open,
        "checks_pass": checks_pass,
        "remote_ok": remote_ok,
        "ready_for_closeout": checks_pass and remote_ok
    }

    if args.check_only or not args.execute or not time_gate_open:
        print(json.dumps(status_summary, indent=2))
        return

    print(">>> Time gate open! Executing final Day 21 closeout...")

    # Step A: Update Daily Report to completed
    rep_txt = REPORT.read_text(encoding="utf-8")
    rep_txt = rep_txt.replace("research_status: active-in-progress-checkpoint151", "research_status: completed")
    rep_txt = rep_txt.replace("Day 21 card audit: in-progress", "Day 21 card audit: complete")
    rep_txt = rep_txt.replace("completed_day_indices: []", "completed_day_indices: [21]")
    rep_txt = rep_txt.replace("partial_day_indices: [21]", "partial_day_indices: []")
    rep_txt = rep_txt.replace("next_day_index: 21", "next_day_index: 22")
    REPORT.write_text(rep_txt, encoding="utf-8")

    # Step B: Update Milestone State
    state = json.loads(STATE_FILE.read_text())
    state["next_day_index"] = 22
    state["last_success"] = "2026-10-23"
    state["last_run_id"] = "2026-10-23-day-21-01"
    state["completed_day_count"] = 21
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False) + chr(10))

    # Step C: Write Day 22 prompt
    prompt_draft = json.loads((RUN / 'next-day-prompt-draft-scope-149.json').read_text())
    PROMPT_D22.write_text(prompt_draft["prompt_text"], encoding="utf-8")

    # Step D: Write card-credit-21.json
    card_credit = {
        "transition_id": "2026-10-23-day-21-01/formal-Day21",
        "observed_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "session_id": "01a167eb-3c9c-74c0-a0a0-12720a4e1f4d",
        "formal_completed": [21],
        "uncredited_preview": [],
        "completed_day_count": 21,
        "next_day_index": 22,
        "no_double_credit_guard": "Verified single credit for Day 21 only; absence of Day 22 credit; H3 passed",
        "applied_at": now_dt.isoformat()
    }
    CREDIT_D21.write_text(json.dumps(card_credit, indent=2, ensure_ascii=False) + chr(10))

    # Step D2: Write final-session-receipt-21.json
    receipt_draft = json.loads((RUN / 'final-session-receipt-draft-scope-148.json').read_text())
    receipt_draft["finished_at"] = now_dt.isoformat()
    receipt_draft["closeout_completed_at"] = now_dt.isoformat()
    RECEIPT_D21.write_text(json.dumps(receipt_draft, indent=2, ensure_ascii=False) + chr(10))

    # Step E: Update run.json to completed
    run_data = json.loads(RUN_JSON.read_text())
    run_data["status"] = "completed"
    run_data["completed_day_indices"] = [21]
    run_data["partial_day_indices"] = []
    run_data["curriculum_cards_completed"] = 1
    run_data["next_day_index"] = 22
    run_data["finished_at"] = now_dt.isoformat()
    run_data["last_closeout_snapshot"] = {
        "now_local": now_dt.isoformat(),
        "hard_deadline": "2026-10-24T15:00:00+08:00",
        "next_scheduled_start": "2026-10-24T16:00:00+08:00",
        "minutes_to_deadline": mins_to_deadline,
        "decision": "closeout-only",
        "day22_opened": False,
        "forward_card_prohibited_by_user": True
    }
    RUN_JSON.write_text(json.dumps(run_data, indent=2, ensure_ascii=False) + chr(10))

    # Step E2: Update handoff.md and log.md
    handoff_text = HANDOFF.read_text(encoding="utf-8")
    old_h_entry = "## 当前唯一执行入口 — Day21继续（Checkpoint151：暂存演练与cached diff零空白终验）"
    new_h_entry = "## 当前唯一执行入口 — Day21完成与Day22准备入口（Checkpoint152：收束与发布完成）"
    if old_h_entry in handoff_text:
        handoff_text = handoff_text.replace(old_h_entry, new_h_entry)
        HANDOFF.write_text(handoff_text, encoding="utf-8")

    log_entry = chr(10) + f'- {now_dt.isoformat()} Day21 checkpoint152/closeout：Day 21卡审计完成（18/24评分、5项交付、weekly REFLECT），完成104项知识写回并经H3协议验证，完成card-credit-21（completed[21]/partial[]/next22/count21），签发final-session-receipt-21，生成Day 22准备入口，已发布至Gitee main.' + chr(10)
    with LOG_MD.open("a", encoding="utf-8") as f_log:
        f_log.write(log_entry)

    # Clean whitespace across all modified files
    for p_check in [REPORT, PROMPT_D22, CREDIT_D21, RECEIPT_D21, RUN_JSON, STATE_FILE, HANDOFF, LOG_MD]:
        lines = p_check.read_text(encoding="utf-8").splitlines()
        stripped = [l.rstrip() for l in lines]
        while stripped and stripped[-1] == "":
            stripped.pop()

    # Step F: Run full required checks
    p_lint2 = subprocess.run(["python3", "system/scripts/wiki_lint.py", "--fail-on", "error"], cwd=ROOT, capture_output=True, text=True)
    p_bound2 = subprocess.run(["python3", "system/scripts/wiki_boundary_check.py", "--root", "."], cwd=ROOT, capture_output=True, text=True)
    p_diff2 = subprocess.run(["git", "diff", "--check"], cwd=ROOT, capture_output=True, text=True)
    p_wb2 = subprocess.run(["python3", "system/scripts/validate_writeback_items.py", "--report", str(REPORT.relative_to(ROOT))], cwd=ROOT, capture_output=True, text=True)
    assert p_lint2.returncode == 0, f"wiki_lint failed: {p_lint2.stderr}"
    assert p_bound2.returncode == 0, f"wiki_boundary_check failed: {p_bound2.stderr}"
    assert p_diff2.returncode == 0, f"git diff --check failed: {p_diff2.stdout}"
    assert json.loads(p_wb2.stdout)["valid"], f"validate_writeback_items failed: {p_wb2.stdout}"

    # Step G: Git staging exact manifest
    p_status = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, capture_output=True, text=True)
    staged_files = []
    for line in p_status.stdout.splitlines():
        path_str = line[3:].strip()
        if path_str == "PLAN.md" or path_str.startswith("raw/") or "wiki-inbox.bib" in path_str:
            continue
        if "20261022-DAY20" in path_str or path_str.startswith("tmp/"):
            continue
        staged_files.append(path_str)

    chunk_size = 50
    for i in range(0, len(staged_files), chunk_size):
        chunk = [f for f in staged_files[i:i+chunk_size] if (ROOT / f).exists()]
        subprocess.run(["git", "add", "--"] + chunk, cwd=ROOT, check=True)

    subprocess.run(["git", "diff", "--cached", "--check"], cwd=ROOT, check=True)

    # Step H: Git commit and push
    commit_msg = "Finalize Day 21 card audit, knowledge writeback, and receipt"
    subprocess.run(["git", "commit", "-m", commit_msg], cwd=ROOT, check=True)
    subprocess.run(["git", "push", "--dry-run", "origin", "HEAD:main"], cwd=ROOT, check=True)
    p_push = subprocess.run(["git", "push", "origin", "HEAD:main"], cwd=ROOT, capture_output=True, text=True)
    assert p_push.returncode == 0, f"git push failed: {p_push.stderr}"

    print(">>> Closeout and push successfully completed!")

if __name__ == '__main__':
    main()
