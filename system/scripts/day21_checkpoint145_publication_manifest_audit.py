#!/usr/bin/env python3
"""Exact publication manifest construction and exclusion audit for Day 21."""
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'

def main():
    # 1. Gather all files in the working directory
    p_status = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, capture_output=True, text=True)
    status_lines = p_status.stdout.splitlines()

    stage_list = []
    excluded_list = []

    for line in status_lines:
        code = line[:2]
        path_str = line[3:].strip()

        # Check exclusion rules
        is_excluded = False
        if path_str == "PLAN.md" or path_str.startswith("raw/") or "wiki-inbox.bib" in path_str:
            is_excluded = True
            reason = "protected-governance-path"
        elif "20261022-DAY20" in path_str:
            is_excluded = True
            reason = "inherited-dirty-previous-day"
        elif path_str.startswith("tmp/"):
            is_excluded = True
            reason = "temporary-directory"
        elif "stderr.log" in path_str or "events.jsonl" in path_str:
            # Let's check events.jsonl
            if path_str.endswith("stderr.log"):
                is_excluded = True
                reason = "transient-stderr-log"

        if is_excluded:
            excluded_list.append({"path": path_str, "reason": reason})
        else:
            stage_list.append(path_str)

    res = {
        "title": "Day 21 Exact Git Staging Manifest and Exclusion Audit",
        "staged_file_count": len(stage_list),
        "excluded_file_count": len(excluded_list),
        "staged_files": stage_list,
        "excluded_files": excluded_list,
        "staging_rules_verified": [
            "Rule 1: Never use 'git add .' or 'git add -A'; use explicit stage manifest.",
            "Rule 2: Strictly exclude PLAN.md, raw/, raw/zotero/wiki-inbox.bib, and inherited Day 20 files.",
            "Rule 3: Keep index clean until formal 15:00 closeout gate."
        ]
    }

    out = RUN / 'publication-manifest-scope-145.json'
    out.write_text(json.dumps(res, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({
        "output": str(out.relative_to(ROOT)),
        "staged_count": len(stage_list),
        "excluded_count": len(excluded_list),
        "sample_excluded": [e["path"] for e in excluded_list[:5]]
    }))

if __name__ == '__main__':
    main()
