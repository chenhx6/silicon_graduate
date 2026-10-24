
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

# Check if checkpoint-010 already in observed_clock_executions
already_acked = any(e.get("clock_event_id") == "checkpoint-010" for e in data.get("observed_clock_executions", []))
if not already_acked:
    data.setdefault("observed_clock_executions", []).append({
        "clock_event_id": "checkpoint-010",
        "same_session_id": data["session_id"],
        "observed_at": now_dt.isoformat(),
        "queued_snapshot_at": "2026-10-24T12:40:25.111715+08:00",
        "action": "acknowledge-clock-checkpoint-010-continue-day21",
        "checkpoint": "131"
    })

data["last_closeout_snapshot"] = {
    "now_local": now_dt.isoformat(),
    "hard_deadline": "2026-10-24T15:00:00+08:00",
    "next_scheduled_start": "2026-10-24T16:00:00+08:00",
    "minutes_to_deadline": mins_to_deadline,
    "minutes_to_next_start": mins_to_next_start,
    "minimum_current_block_minutes": 90,
    "minimum_forward_card_block_minutes": 120,
    "can_continue_current": mins_to_deadline >= 90,
    "can_complete_forward_card": False,
    "decision": "continue-or-advance" if mins_to_deadline >= 120 else ("continue-current-or-partial" if mins_to_deadline >= 90 else "finish-current-no-new-unit"),
    "day22_opened": False,
    "forward_card_prohibited_by_user": True
}

run_file.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")

# Write clock-checkpoint-010-observation.json
obs_file = Path("outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/clock-checkpoint-010-observation.json")
obs_data = {
    "clock_event_id": "checkpoint-010",
    "observed_at": now_dt.isoformat(),
    "queued_snapshot_at": "2026-10-24T12:40:25.111715+08:00",
    "session_id": data["session_id"],
    "day_index": 21,
    "minutes_to_deadline": mins_to_deadline,
    "action": "acknowledge-clock-checkpoint-010-continue-day21",
    "active_checkpoint": "131",
    "status": "active-running",
    "notes": "Acknowledged clock-checkpoint-010; continuing substantive research within open study window."
}
obs_file.write_text(json.dumps(obs_data, indent=2, ensure_ascii=False) + "\n")

print(f"Acked checkpoint-010: mins_to_deadline={mins_to_deadline}, decision={data['last_closeout_snapshot']['decision']}")
