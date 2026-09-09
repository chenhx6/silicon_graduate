#!/usr/bin/env python3
"""Clear tracked knowledge files that differ only by CRLF/LF line endings."""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(["git", "-C", str(root), *args], text=True,
                            capture_output=True, check=False)
    if check and result.returncode:
        raise RuntimeError(result.stderr.strip() or f"git {' '.join(args)} failed")
    return result


def status_records(root: Path, path: str | None = None) -> list[tuple[str, str, str | None]]:
    args = ["status", "--porcelain=v1", "-z", "--untracked-files=no", "--"]
    args.append(path or "knowledge")
    raw = git(root, *args).stdout
    parts = raw.split("\0")
    records: list[tuple[str, str, str | None]] = []
    i = 0
    while i < len(parts):
        item = parts[i]
        i += 1
        if not item:
            continue
        if len(item) < 4:
            raise RuntimeError(f"Unable to parse git status record: {item!r}")
        code, name = item[:2], item[3:]
        other = None
        if code[0] in "RC":
            if i >= len(parts) or not parts[i]:
                raise RuntimeError(f"Missing rename target for {name}")
            other, i = parts[i], i + 1
        records.append((code, name, other))
    return records


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        root = Path(git(Path.cwd(), "rev-parse", "--show-toplevel").stdout.strip()).resolve()
        refreshed = restored = would_restore = kept = staged = unsafe = 0
        for code, name, other in status_records(root):
            paths = [name] + ([other] if other else [])
            knowledge = [p.replace("\\", "/") for p in paths
                         if p.replace("\\", "/").startswith("knowledge/")
                         and p.lower().endswith(".md")]
            if not knowledge:
                continue
            path = knowledge[0]
            if code == " M":
                diff = git(root, "diff", "--ignore-cr-at-eol", "--quiet", "--", path,
                           check=False)
                if diff.returncode == 0:
                    if args.dry_run:
                        would_restore += 1
                        print(f"[WOULD-RESTORE] {path}")
                        continue
                    refresh = git(root, "update-index", "--refresh", "--", path, check=False)
                    if refresh.returncode > 1:
                        raise RuntimeError(refresh.stderr.strip() or f"update-index failed: {path}")
                    current = status_records(root, path)
                    if not current:
                        refreshed += 1
                        print(f"[REFRESHED] {path}")
                    elif len(current) == 1 and current[0][0] == " M":
                        restore = git(root, "restore", "--", path, check=False)
                        if restore.returncode:
                            raise RuntimeError(restore.stderr.strip() or f"restore failed: {path}")
                        if not status_records(root, path):
                            restored += 1
                            print(f"[RESTORED] {path}")
                        else:
                            unsafe += 1
                            print(f"[REVIEW-UNSAFE] still-dirty-after-restore {path}")
                    else:
                        unsafe += 1
                        print(f"[REVIEW-UNSAFE] mixed {path}")
                elif diff.returncode == 1:
                    kept += 1
                    print(f"[KEEP-SUBSTANTIVE] {path}")
                else:
                    raise RuntimeError(diff.stderr.strip() or f"diff failed: {path}")
            elif code == "M ":
                staged += 1
                print(f"[STAGED-NOT-TOUCHED] {path}")
            else:
                unsafe += 1
                print(f"[REVIEW-UNSAFE] {code} {' -> '.join(knowledge)}")
        print(f"Refreshed: {refreshed}")
        print(f"Restored: {restored}")
        print(f"Would restore: {would_restore}")
        print(f"Kept substantive: {kept}")
        print(f"Staged not touched: {staged}")
        print(f"Unsafe/mixed: {unsafe}")
        print(git(root, "status", "-sb").stdout, end="")
        return 1 if kept or unsafe else 0
    except Exception as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
