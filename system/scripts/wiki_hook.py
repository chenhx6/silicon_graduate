#!/usr/bin/env python3
"""Explicit, read-only lifecycle checks for the Wiki workspace."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


PROTECTED = (Path(".git"), Path(".codex"), Path("raw/zotero/wiki-inbox.bib"))
GIT_TIMEOUT_SECONDS = 30


def repo_root(requested: str | None = None) -> Path:
    if requested:
        return Path(requested).resolve()
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        text=True,
        capture_output=True,
        check=True,
    )
    return Path(result.stdout.strip()).resolve()


def relative_candidate(root: Path, value: str) -> Path:
    candidate = Path(value)
    if not candidate.is_absolute():
        candidate = root / candidate
    candidate = candidate.resolve(strict=False)
    try:
        relative = candidate.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"path outside repository: {value}") from exc
    if not relative.parts:
        raise ValueError("repository root is not an editable path")
    for blocked in PROTECTED:
        if relative == blocked or blocked in relative.parents:
            raise ValueError(f"protected path: {relative.as_posix()}")
    return relative


def parse_paths(argv_paths: list[str], stdin: str = "") -> list[str]:
    values = list(argv_paths)
    if not values and stdin.strip():
        text = stdin.strip()
        try:
            payload = json.loads(text)
        except json.JSONDecodeError:
            values = [line.strip() for line in text.splitlines() if line.strip()]
        else:
            if isinstance(payload, str):
                values = [payload]
            elif isinstance(payload, list):
                values = [str(item) for item in payload]
            elif isinstance(payload, dict):
                for key in ("path", "file", "paths", "files"):
                    item = payload.get(key)
                    if isinstance(item, str):
                        values.append(item)
                    elif isinstance(item, list):
                        values.extend(str(entry) for entry in item)
    return values


def status_payload(root: Path) -> dict[str, object]:
    def run(args: list[str]) -> subprocess.CompletedProcess[str]:
        try:
            return subprocess.run(args, text=True, capture_output=True, check=False, timeout=GIT_TIMEOUT_SECONDS)
        except subprocess.TimeoutExpired:
            return subprocess.CompletedProcess(args, 124, "", "timed out")

    branch = run(["git", "-C", str(root), "branch", "--show-current"]).stdout.strip()
    head = run(["git", "-C", str(root), "rev-parse", "--short", "HEAD"]).stdout.strip()
    status_result = run(["git", "-C", str(root), "status", "--short"])
    status = status_result.stdout.splitlines()
    dirty_probe = run(["git", "-C", str(root), "diff-index", "--quiet", "HEAD", "--"])
    return {
        "root": str(root),
        "branch": branch,
        "head": head,
        "changed_count": len(status),
        "recent_paths": [line[3:] for line in status[:5]],
        "status_ok": status_result.returncode == 0,
        "status_error": status_result.stderr.strip(),
        "working_tree_dirty": dirty_probe.returncode == 1,
    }


def changed_paths(root: Path) -> list[Path]:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "diff-index", "--name-only", "HEAD", "--"],
            text=True,
            capture_output=True,
            check=False,
            timeout=GIT_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        return []
    paths: list[Path] = []
    for line in result.stdout.splitlines():
        if not line:
            continue
        raw = line.strip()
        try:
            paths.append(relative_candidate(root, raw))
        except ValueError:
            continue
    return paths


def after_edit(root: Path, paths: list[str] | None = None) -> dict[str, object]:
    try:
        diff = subprocess.run(
            ["git", "-C", str(root), "diff", "--check"],
            text=True,
            capture_output=True,
            check=False,
            timeout=GIT_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        diff = subprocess.CompletedProcess([], 124, "", "timed out")
    candidates = [relative_candidate(root, item) for item in paths] if paths else changed_paths(root)
    shell_checks: list[dict[str, object]] = []
    for relative in candidates:
        if relative.suffix not in {".sh", ".bash"} and relative.name not in {"pre-commit", "pre-push"}:
            continue
        result = subprocess.run(["bash", "-n", str(root / relative)], text=True, capture_output=True, check=False, timeout=5)
        shell_checks.append({"path": relative.as_posix(), "ok": result.returncode == 0, "stderr": result.stderr.strip()})
    ok = diff.returncode == 0 and all(item["ok"] for item in shell_checks)
    return {"ok": ok, "diff_check": diff.returncode == 0, "diff_stderr": diff.stderr.strip(), "shell_checks": shell_checks}


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]
    argv = [item for item in argv if item != "--"]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("event", choices=["session-start", "session-summary", "before-edit", "after-edit", "stop", "notify"])
    parser.add_argument("--root", default=None)
    parser.add_argument("message", nargs="*")
    args = parser.parse_intermixed_args(argv)
    root = repo_root(args.root)
    if args.event in {"session-start", "session-summary"}:
        payload = status_payload(root)
        payload["event"] = args.event
        print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
        return 0
    if args.event == "notify":
        print(json.dumps({"event": "notify", "message": " ".join(args.message) or os.environ.get("CODEX_HOOK_MESSAGE", "")}, ensure_ascii=False))
        return 0
    if args.event == "before-edit":
        values = parse_paths(args.message, sys.stdin.read())
        errors: list[str] = []
        accepted: list[str] = []
        for value in values:
            try:
                accepted.append(relative_candidate(root, value).as_posix())
            except ValueError as exc:
                errors.append(str(exc))
        print(json.dumps({"event": "before-edit", "ok": not errors and bool(values), "accepted": accepted, "errors": errors}, ensure_ascii=False, sort_keys=True))
        return 0 if not errors and bool(values) else 1
    result = after_edit(root, args.message or None)
    result["event"] = args.event
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
