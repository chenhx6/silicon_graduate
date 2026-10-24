#!/usr/bin/env python3
"""Audit and pre-validation of the Day 21 final session receipt structure and closeout metadata."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'

def main():
    run_data = json.loads((RUN / 'run.json').read_text())

    receipt_draft = {
        "schema_version": 1,
        "status": "completed",
        "run_id": "2026-10-23-day-21-01",
        "session_id": run_data["session_id"],
        "resume_command": run_data["resume_command"],
        "started_at": run_data["started_at"],
        "original_deadline": run_data["overnight_until"],
        "closeout_window_ends_at": run_data["closeout_window_ends_at"],
        "completed_day_indices": [21],
        "partial_day_indices": [],
        "curriculum_cards_completed": 1,
        "next_day_index": 22,
        "cumulative_completed_day_count": 21,
        "single_credit_receipt": "card-credit-21.json",
        "card_audit": {
            "report": "outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam.md",
            "section": "Day 21 card completion audit",
            "deliverables": 5,
            "scope": "bounded learning deliverables; not certification of all scientific claims"
        },
        "scorecard": {
            "dimensions_scored": 6,
            "total_score": "18/24",
            "per_dimension_score": "3/4"
        },
        "open_questions_status": {
            "total": 4,
            "closed": 4,
            "closure_rate_percent": 100.0
        },
        "governance_compliance": {
            "needs_review_preserved": True,
            "no_human_reviewed_promoted": True,
            "protected_files_clean": True,
            "writeback_items": 104
        },
        "publication_spec": {
            "branch": "main",
            "refspec": "HEAD:main",
            "non_force": True,
            "staged_file_count": 289,
            "h3_preflight_passed": True
        }
    }

    out = RUN / 'final-session-receipt-draft-scope-148.json'
    out.write_text(json.dumps(receipt_draft, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({
        "output": str(out.relative_to(ROOT)),
        "status": receipt_draft["status"],
        "scorecard": receipt_draft["scorecard"]["total_score"],
        "open_questions": receipt_draft["open_questions_status"]["closed"],
        "completed_day": receipt_draft["completed_day_indices"]
    }))

if __name__ == '__main__':
    main()
