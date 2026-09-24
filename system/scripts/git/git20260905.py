#!/usr/bin/env python3
"""Explicit manifest-based commit and non-force publication helper."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path


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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--manifest", default="outputs/degree-dissertation-ingest-20260905.manifest.json")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
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
            path = rel.replace("\\", "/")
            if path.startswith(("raw/", ".git/", ".codex/", ".agents/")) or path in ("PLAN.md", "raw/zotero/wiki-inbox.bib"):
                print(f"GIT20260905_STATUS=manifest-invalid\nProtected path is not stageable: {rel}")
                return 25
            candidate = (root / rel).resolve()
            if root not in candidate.parents and candidate != root:
                print(f"GIT20260905_STATUS=manifest-invalid\nPath escapes Wiki root: {rel}")
                return 25
        cached = [x for x in run(root, "diff", "--cached", "--name-only").stdout.splitlines() if x]
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
        changed = []
        for rel in allowed:
            if run(root, "status", "--porcelain=v1", "--", rel).stdout.strip():
                changed.append(rel)
        if not changed:
            print("GIT20260905_STATUS=nothing-to-commit\nNo manifest-listed file has a worktree change.")
            return 0
        print("Manifest-listed changed paths:\n" + "\n".join(f"  {p}" for p in changed))
        if args.dry_run:
            print("GIT20260905_STATUS=dry-run-ok\nNo files were staged, committed, fetched, or pushed.")
            return 0
        for rel in changed:
            run(root, "add", "--", rel)
        staged = [x for x in run(root, "diff", "--cached", "--name-only").stdout.splitlines() if x]
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
