from pathlib import Path

bad_files = [
    "outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/next-continuation-151.md",
    "system/scripts/day21_add_prompt_text_149.py",
    "system/scripts/day21_execute_closeout_and_publish.py",
    "system/scripts/day21_run_checks_151.py",
    "system/scripts/day21_update_handoff_151.py",
    "system/scripts/day21_update_report_151.py",
    "system/scripts/day21_update_run_151.py"
]

for f in bad_files:
    p = Path(f)
    if p.exists():
        lines = p.read_text(encoding="utf-8").splitlines()
        stripped = [l.rstrip() for l in lines]
        while stripped and stripped[-1] == "":
            stripped.pop()
        p.write_text(chr(10).join(stripped) + chr(10), encoding="utf-8")
        print(f"Cleaned {f}")
