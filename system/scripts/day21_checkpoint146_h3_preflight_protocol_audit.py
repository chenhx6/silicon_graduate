#!/usr/bin/env python3
"""Quantitative H3 protocol pre-flight audit against Gitee remote for Day 21."""
import datetime
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'

def run_cmd(name, argv):
    t0 = datetime.datetime.now(datetime.timezone.utc).isoformat()
    p = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True)
    return {
        "name": name,
        "argv": argv,
        "exit_code": p.returncode,
        "stdout": p.stdout,
        "stderr": p.stderr,
        "at_utc": t0
    }

def main():
    events = []

    # Event 1: branch
    e_branch = run_cmd("branch", ["git", "branch", "--show-current"])
    events.append(e_branch)
    assert e_branch["stdout"].strip() == "main"

    # Event 2: remote
    e_remote = run_cmd("remote", ["git", "remote", "-v"])
    events.append(e_remote)
    assert "gitee.com" in e_remote["stdout"]

    # Event 3: fetch
    e_fetch = run_cmd("fetch", ["git", "fetch", "origin", "main"])
    events.append(e_fetch)
    assert e_fetch["exit_code"] == 0

    # Event 4: ancestor check
    e_anc = run_cmd("ancestor", ["git", "merge-base", "--is-ancestor", "origin/main", "HEAD"])
    events.append(e_anc)
    assert e_anc["exit_code"] == 0

    # Event 5: dry-run push
    e_dry = run_cmd("push_dry_run", ["git", "push", "--dry-run", "origin", "HEAD:main"])
    events.append(e_dry)
    assert e_dry["exit_code"] == 0

    res = {
        "title": "Day 21 H3 Protocol Pre-Flight Verification",
        "phase": "pre-flight-check",
        "h3_status": "passed",
        "events": events,
        "compliance_summary": {
            "branch_is_main": True,
            "origin_is_gitee": True,
            "fetch_succeeded": True,
            "origin_main_is_ancestor_of_head": True,
            "push_dry_run_succeeded": True,
            "non_force_refspec_ready": "HEAD:main"
        }
    }

    out = RUN / 'h3-preflight-scope-146.json'
    out.write_text(json.dumps(res, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({
        "output": str(out.relative_to(ROOT)),
        "h3_passed": res["h3_status"] == "passed",
        "events_count": len(events)
    }))

if __name__ == '__main__':
    main()
