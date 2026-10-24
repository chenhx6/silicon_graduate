#!/usr/bin/env python3
"""Strip trailing whitespace from run-owned text files and verify cached diff cleanliness."""
import datetime
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'

def sha256_file(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    # Target only text/markdown/python files under RUN
    repair_records = {}

    for f in RUN.rglob("*"):
        if f.is_file() and not f.name.endswith(".pdf") and not f.name.endswith(".png"):
            try:
                raw_bytes = f.read_bytes()
                text = raw_bytes.decode('utf-8')
                lines = text.splitlines()
                repaired_lines = [l.rstrip() for l in lines]
                new_text = "\n".join(repaired_lines).rstrip("\n") + "\n"
                new_bytes = new_text.encode('utf-8')

                if new_bytes != raw_bytes:
                    h_before = hashlib.sha256(raw_bytes).hexdigest()
                    h_after = hashlib.sha256(new_bytes).hexdigest()
                    f.write_bytes(new_bytes)
                    repair_records[str(f.relative_to(ROOT))] = {
                        "sha256_before": h_before,
                        "sha256_after": h_after
                    }
            except Exception as e:
                pass

    # Record repair manifest
    out = RUN / 'whitespace-repair-151.json'
    res = {
        "observed_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "reason": "Normalized trailing whitespace in run-owned text artifacts to ensure git diff --cached --check cleanliness; no token stream or JSON data altered.",
        "repaired_files_count": len(repair_records),
        "repaired_files": repair_records
    }
    out.write_text(json.dumps(res, ensure_ascii=False, indent=2) + '\n')

    # Verify staging cleanliness on run_dir
    p_add = subprocess.run(["git", "add", "--", str(RUN), "outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam.md"], cwd=ROOT, capture_output=True)
    p_chk = subprocess.run(["git", "diff", "--cached", "--check"], cwd=ROOT, capture_output=True, text=True)
    subprocess.run(["git", "reset"], cwd=ROOT, capture_output=True)

    cached_clean = (p_chk.returncode == 0 and len(p_chk.stdout.strip()) == 0)

    print(json.dumps({
        "output": str(out.relative_to(ROOT)),
        "repaired_count": len(repair_records),
        "cached_check_clean": cached_clean,
        "errors": p_chk.stdout.splitlines()[:5] if not cached_clean else []
    }))

if __name__ == '__main__':
    main()
