
import json
import datetime
from pathlib import Path

run_file = Path("outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/run.json")
data = json.loads(run_file.read_text())

now_dt = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
hard_deadline = datetime.datetime.fromisoformat("2026-10-24T15:00:00+08:00")
next_start = datetime.datetime.fromisoformat("2026-10-24T16:00:00+08:00")
mins_to_deadline = int((hard_deadline - now_dt).total_seconds() / 60)
mins_to_next_start = int((next_start - now_dt).total_seconds() / 60)

decision = "finish-current-no-new-unit" if mins_to_deadline <= 90 else "continue-current-or-partial"

data["last_closeout_snapshot"] = {
    "now_local": now_dt.isoformat(),
    "hard_deadline": "2026-10-24T15:00:00+08:00",
    "next_scheduled_start": "2026-10-24T16:00:00+08:00",
    "minutes_to_deadline": mins_to_deadline,
    "minutes_to_next_start": mins_to_next_start,
    "minimum_current_block_minutes": 90,
    "minimum_forward_card_block_minutes": 120,
    "can_continue_current": False if mins_to_deadline <= 90 else True,
    "can_complete_forward_card": False,
    "decision": decision,
    "day22_opened": False,
    "forward_card_prohibited_by_user": True
}

run_file.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")

res = {
    "title": "Day 21 90-Minute Boundary Transition Audit",
    "now_local": now_dt.isoformat(),
    "minutes_to_deadline": mins_to_deadline,
    "decision": decision,
    "protocol_enforced": [
        "No new source or card may be opened.",
        "Bounded analyses across Checkpoints 104-143 are completely frozen.",
        "System remains in active monitoring state until 15:00 hard deadline.",
        "15:00-16:00 buffer dedicated strictly to final card completion audit, run receipt delivery, course state credit award, and explicit path publication."
    ]
}

out = Path("outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/boundary-transition-scope-144.json")
out.write_text(json.dumps(res, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"now": now_dt.isoformat(), "mins_to_deadline": mins_to_deadline, "decision": decision}))
