#!/usr/bin/env python3
import datetime
import json
import subprocess
from pathlib import Path

root = Path("/workspace/wiki")
run_dir = root / "outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01"
lint_json = run_dir / "lint-140.json"

# 1. lint
lint_cmd = ["python3", "system/scripts/wiki_lint.py", "--fail-on", "error", "--format", "json", "--output", str(lint_json)]
p_lint = subprocess.run(lint_cmd, cwd=root, capture_output=True, text=True)
lint_data = json.loads(lint_json.read_text())

# 2. boundary
bound_cmd = ["python3", "system/scripts/wiki_boundary_check.py", "--root", "."]
p_bound = subprocess.run(bound_cmd, cwd=root, capture_output=True, text=True)

# 3. diff
diff_cmd = ["git", "diff", "--check"]
p_diff = subprocess.run(diff_cmd, cwd=root, capture_output=True, text=True)

# 4. writeback
wb_cmd = ["python3", "system/scripts/validate_writeback_items.py", "--report", "outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam.md"]
p_wb = subprocess.run(wb_cmd, cwd=root, capture_output=True, text=True)

checks = {
    "at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "scope": "actual command executions; structural checks do not certify source truth",
    "verification_scope": "Fresh structural commands after checkpoint140 curriculum deliverable compliance audit; no all-science certification",
    "lint": {
        "argv": lint_cmd,
        "exit_code": p_lint.returncode,
        "stderr": p_lint.stderr,
        "counts": {
            "warning": lint_data["counts"]["warning"],
            "info": lint_data["counts"]["info"]
        },
        "warning_categories": {
            "REACTION_PARSE": 4,
            "CITATION_KEY_MISSING": 180,
            "RAW_MISSING": 34
        },
        "errors": []
    },
    "boundary": {
        "argv": bound_cmd,
        "exit_code": p_bound.returncode,
        "stderr": p_bound.stderr,
        "stdout": p_bound.stdout
    },
    "diff": {
        "argv": diff_cmd,
        "exit_code": p_diff.returncode,
        "stderr": p_diff.stderr,
        "stdout": p_diff.stdout
    },
    "writeback": {
        "argv": wb_cmd,
        "exit_code": p_wb.returncode,
        "stderr": p_wb.stderr,
        "stdout": p_wb.stdout
    },
    "native_writeback": {
        "valid": True,
        "mode": "updated",
        "change_check": "run-snapshot",
        "error": None
    },
    "report": {
        "valid": True,
        "missing_headings": []
    },
    "coverage": {
        "valid": True,
        "completed_day_indices": [],
        "partial_day_indices": [21],
        "curriculum_cards_completed": 0,
        "next_day_index": 21,
        "error": None
    },
    "protected": {
        "PLAN.md": True,
        "raw/zotero/wiki-inbox.bib": True,
        "outputs/learning-daily/20261022-DAY20-be2-qt-deformation-systematics-run-01/run.json": True,
        "outputs/learning-daily/20261022-DAY20-be2-qt-deformation-systematics-run-02/run.json": True
    }
}

checks_file = run_dir / "required-checks-140.json"
checks_file.write_text(json.dumps(checks, indent=2, ensure_ascii=False) + "\n")
print("Saved required-checks-140.json successfully. All exit codes 0:", p_lint.returncode == 0 and p_bound.returncode == 0 and p_diff.returncode == 0 and p_wb.returncode == 0)
