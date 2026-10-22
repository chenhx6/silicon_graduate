#!/usr/bin/env python3
"""Explicit manifest-based commit and non-force publication helper."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path, PurePosixPath


def run(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    p = subprocess.run(["git", "-C", str(root), *args], text=True,
                       capture_output=True, check=False)
    if check and p.returncode:
        raise RuntimeError(f"git {' '.join(args)} failed ({p.returncode})\n{p.stdout}{p.stderr}")
    return p


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def repository_root(start: Path) -> Path:
    for candidate in (start.resolve(), *start.resolve().parents):
        if (candidate / '.git').exists():
            return candidate
    raise ValueError('No repository root found; refusing cwd fallback')


def validate_stage_path(root: Path, rel: str) -> None:
    # A manifest authorizes individual literal files, never directories/pathspecs.
    parts = PurePosixPath(rel).parts
    if (not parts or not rel or rel != PurePosixPath(rel).as_posix() or '\\' in rel
            or PurePosixPath(rel).is_absolute() or '..' in parts
            or parts[0] in ('raw', '.git', '.codex', '.agents', '.opencode')
            or rel == 'PLAN.md'):
        raise ValueError(f'Protected or invalid literal path: {rel!r}')
    cursor = root
    for part in parts:
        cursor = cursor / part
        if cursor.is_symlink():
            raise ValueError(f'Symlink is not stageable: {rel!r}')
    candidate = root / rel
    if root not in candidate.resolve().parents or not candidate.is_file():
        raise ValueError(f'Manifest requires an existing individual file: {rel!r}')


def changed_paths(root: Path) -> set[str]:
    # NUL-delimited bytes preserve Unicode, newlines, quotes and whitespace.
    result = subprocess.run(['git', '-C', str(root), 'status', '--porcelain=v1',
                             '-z', '--untracked-files=all'], capture_output=True, check=True)
    paths = set()
    for record in result.stdout.split(b'\0'):
        if not record:
            continue
        status = record[:2]
        if b'R' in status or b'C' in status or b'U' in status:
            raise ValueError('Rename/copy/conflict requires separate explicit review')
        if len(record) < 4 or record[2:3] != b' ':
            raise ValueError('Invalid porcelain status record')
        paths.add(os.fsdecode(record[3:]))
    return paths


def staged_paths(root: Path) -> list[str]:
    result = subprocess.run(['git', '-C', str(root), 'diff', '--cached',
                             '--name-only', '-z'], capture_output=True, check=True)
    return [os.fsdecode(p) for p in result.stdout.split(b'\0') if p]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--manifest", default="outputs/degree-dissertation-ingest-20260905.manifest.json")
    args = parser.parse_args()
    root = repository_root(Path(__file__).resolve().parent)
    try:
        manifest_path = (root / args.manifest).resolve()
        if root not in manifest_path.parents or not manifest_path.is_file():
            print(f"GIT20260905_STATUS=manifest-missing\nManifest not found: {args.manifest}")
            return 20
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if int(manifest.get("schema_version", 0)) != 1:
            print("GIT20260905_STATUS=manifest-invalid\nManifest schema_version must be 1.")
            return 22
        branch = run(root, "branch", "--show-current").stdout.strip()
        expected_branch = manifest.get("expected_branch", "main")
        if branch != expected_branch:
            print(f"GIT20260905_STATUS=wrong-branch\nExpected branch {expected_branch!r}, found {branch!r}.")
            return 23
        allowed = sorted(set(str(p) for p in manifest.get("allowed_paths", [])))
        if not allowed:
            print("GIT20260905_STATUS=manifest-invalid\nManifest allowed_paths is empty.")
            return 24
        for rel in allowed:
            try:
                validate_stage_path(root, rel)
            except ValueError as exc:
                print(f"GIT20260905_STATUS=manifest-invalid\n{exc}")
                return 25
        cached = staged_paths(root)
        if cached:
            print("GIT20260905_STATUS=preexisting-index-changes\n" + ", ".join(cached))
            return 26
        for protected in manifest.get("protected_paths", []):
            path = (root / str(protected["path"])).resolve()
            if digest(path) != str(protected["sha256"]).upper():
                print(f"GIT20260905_STATUS=protected-file-changed\nProtected file hash changed: {protected['path']}")
                return 28
        preflight = subprocess.run([sys.executable, str(root / "system/scripts/wiki_automation_preflight.py"),
                                    "--root", str(root)], text=True, capture_output=True, check=False)
        if preflight.returncode:
            print(f"GIT20260905_STATUS=git-unavailable\n{preflight.stdout}{preflight.stderr}")
            return 42
        all_changed = changed_paths(root)
        changed = [rel for rel in allowed if rel in all_changed]
        if not changed:
            print("GIT20260905_STATUS=nothing-to-commit\nNo manifest-listed file has a worktree change.")
            return 0
        print("Manifest-listed changed paths:\n" + "\n".join(f"  {p}" for p in changed))
        if args.dry_run:
            print("GIT20260905_STATUS=dry-run-ok\nNo files were staged, committed, fetched, or pushed.")
            return 0
        for rel in changed:
            run(root, "--literal-pathspecs", "add", "--", rel)
        staged = staged_paths(root)
        if set(staged) != set(changed):
            print("GIT20260905_STATUS=stage-boundary-failed\n" + ", ".join(staged))
            return 45
        if run(root, "diff", "--cached", "--check", check=False).returncode:
            return 46
        message = manifest.get("commit_message", "Ingest dissertation corpus")
        run(root, "commit", "-m", str(message))
        post = subprocess.run([sys.executable, str(root / "system/scripts/wiki_automation_preflight.py"), "--root", str(root)],
                              text=True, capture_output=True, check=False)
        if post.returncode:
            print(f"GIT20260905_STATUS=post-commit-preflight-failed\n{post.stdout}{post.stderr}")
            return 48
        fetch = run(root, "fetch", "origin", "main", check=False)
        if fetch.returncode:
            fetch = run(root, "fetch", "origin", "main", check=False)
        if fetch.returncode:
            print("GIT20260905_STATUS=final-not-pushed\nFresh fetch failed; commit exists locally.")
            return 50
        if run(root, "merge-base", "--is-ancestor", "origin/main", "HEAD", check=False).returncode:
            print("GIT20260905_STATUS=remote-drift\norigin/main is not an ancestor of HEAD.")
            return 51
        if run(root, "push", "--dry-run", "origin", "HEAD:main", check=False).returncode:
            print("GIT20260905_STATUS=final-not-pushed\nPush dry-run failed; no real push was attempted.")
            return 52
        push = run(root, "push", "origin", "HEAD:main", check=False)
        if push.returncode:
            print("GIT20260905_STATUS=final-not-pushed\nReal non-force push failed.")
            return 53
        print(f"GIT20260905_STATUS=published\nCommit={run(root, 'rev-parse', 'HEAD').stdout.strip()} Branch={branch} RefSpec=HEAD:main")
        return 0
    except Exception as exc:
        print(f"GIT20260905_STATUS=error\n{exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
