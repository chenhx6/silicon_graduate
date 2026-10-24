#!/usr/bin/env python3
"""Audit and pre-validation of the single Day 21 card-credit transition delta."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'
STATE_FILE = ROOT / 'outputs/learning-milestones/2026-09-one-month-state.json'

def main():
    state_before = json.loads(STATE_FILE.read_text())
    assert state_before["next_day_index"] == 21
    assert state_before["completed_day_count"] == 20
    assert state_before["status"] == "active"

    # Define state after 15:00 closeout
    state_after = dict(state_before)
    state_after["next_day_index"] = 22
    state_after["last_success"] = "2026-10-23"
    state_after["last_run_id"] = "2026-10-23-day-21-01"
    state_after["completed_day_count"] = 21

    credit_delta = {
        "transition_id": "2026-10-23-day-21-01/formal-Day21",
        "session_id": "01a167eb-3c9c-74c0-a0a0-12720a4e1f4d",
        "state_before": state_before,
        "state_after": state_after,
        "coverage_delta": {
            "completed_day_indices": [21],
            "partial_day_indices": [],
            "curriculum_cards_completed": 1,
            "next_day_index": 22
        },
        "invariants_enforced": [
            "Invariant 1 (Single Credit): Exactly one formal day card [21] credited in this run.",
            "Invariant 2 (No Day 22 Preview/Credit): partial_day_indices is empty; no Day 22 opened or credited.",
            "Invariant 3 (No Early Award): This draft is validated only and not committed to state file until actual 15:00 cutoff."
        ]
    }

    out = RUN / 'card-credit-draft-scope-147.json'
    out.write_text(json.dumps(credit_delta, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({
        "output": str(out.relative_to(ROOT)),
        "before_next": state_before["next_day_index"],
        "after_next": state_after["next_day_index"],
        "before_count": state_before["completed_day_count"],
        "after_count": state_after["completed_day_count"]
    }))

if __name__ == '__main__':
    main()
