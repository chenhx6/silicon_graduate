#!/usr/bin/env python3
"""Cross-platform Nature Skills updater with staging, hashes and rollback."""
from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

REMOTE = "https://github.com/Yuan1z0825/nature-skills.git"
MANIFEST = ".nature-skills-install.txt"
DANGEROUS = {".exe", ".dll", ".sys", ".ocx", ".cpl", ".msi", ".jar", ".class",
             ".iso", ".img", ".dmg", ".bin", ".zip", ".7z", ".rar", ".bat", ".cmd",
             ".ps1", ".vbs", ".vbe", ".wsf", ".hta", ".reg", ".lnk", ".url"}


def run(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    p = subprocess.run(["git", "-C", str(repo), *args], text=True,
                       capture_output=True, check=False)
    if check and p.returncode:
        raise RuntimeError(p.stderr.strip() or f"git {' '.join(args)} failed")
    return p


def tree_digest(path: Path) -> tuple[str, dict[str, str]]:
    files: dict[str, str] = {}
    for item in sorted(path.rglob("*")):
        if not item.is_file() or any(part in {"__pycache__", ".pytest_cache"} for part in item.parts):
            continue
        if item.name == ".DS_Store" or item.suffix.lower() in {".pyc", ".pyo"}:
            continue
        files[item.relative_to(path).as_posix()] = hashlib.sha256(item.read_bytes()).hexdigest().upper()
    payload = "\n".join(f"{name}|{files[name]}" for name in sorted(files))
    return hashlib.sha256(payload.encode()).hexdigest().upper(), files


def safe_name(name: str) -> bool:
    return bool(name) and name not in {".", ".."} and all(c.isalnum() or c in "._-" for c in name)


def skills(source: Path) -> list[Path]:
    root = source / "skills"
    if not root.is_dir():
        raise RuntimeError(f"skills directory not found: {root}")
    found = []
    for item in sorted(root.iterdir()):
        if not item.is_dir() or not (item / "SKILL.md").is_file():
            continue
        if not safe_name(item.name) or (not item.name.startswith("nature-") and item.name != "_shared"):
            raise RuntimeError(f"unexpected skill directory: {item.name}")
        if item.is_symlink():
            raise RuntimeError(f"symlink is not allowed: {item}")
        found.append(item)
    if not found:
        raise RuntimeError("no Nature Skills with SKILL.md were found")
    for item in found:
        for child in item.rglob("*"):
            if child.is_symlink():
                raise RuntimeError(f"symlink is not allowed: {child}")
            if child.is_file():
                if child.stat().st_size > 10 * 1024 * 1024 or child.suffix.lower() in DANGEROUS:
                    raise RuntimeError(f"unsupported file in skill tree: {child}")
    return found


def read_manifest(path: Path) -> tuple[str | None, dict[str, str]]:
    commit, hashes = None, {}
    if not path.is_file():
        return commit, hashes
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("# commit="):
            commit = line.split("=", 1)[1]
        elif line.startswith("# hash|"):
            _, name, value = line.split("|", 2)
            hashes[name] = value
    return commit, hashes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-only", action="store_true")
    parser.add_argument("--rollback", action="store_true")
    parser.add_argument("--no-pull", action="store_true")
    parser.add_argument("--repo-path", type=Path, default=Path.home() / "ai-skills" / "nature-skills")
    parser.add_argument("--destination-path", type=Path, default=Path.home() / ".codex" / "skills")
    parser.add_argument("--backup-root", type=Path, default=Path.home() / ".local" / "state" / "NatureSkillsUpdater")
    args = parser.parse_args()
    if sum((args.check_only, args.rollback, args.no_pull)) > 1:
        print("Use only one of --rollback, --check-only and --no-pull", file=sys.stderr)
        return 2
    repo, dest, backup = (p.expanduser().resolve() for p in (args.repo_path, args.destination_path, args.backup_root))
    lock = backup / "update.lock"
    try:
        backup.mkdir(parents=True, exist_ok=True)
        if args.rollback:
            previous = backup / "previous"
            names_file = previous / "managed-names.txt"
            if not names_file.is_file():
                raise RuntimeError("no previous Nature Skills backup is available")
            current_names = [p.name for p in dest.iterdir() if p.is_dir() and p.name.startswith("nature-")] if dest.is_dir() else []
            for name in current_names:
                shutil.rmtree(dest / name)
            for name in names_file.read_text(encoding="utf-8").splitlines():
                src = previous / "skills" / name
                if not src.is_dir():
                    raise RuntimeError(f"rollback backup is incomplete: {name}")
                shutil.copytree(src, dest / name)
            if (previous / "manifest.txt").is_file():
                shutil.copy2(previous / "manifest.txt", dest / MANIFEST)
            print("Rollback completed. Restart Codex to reload the restored skills.")
            return 0
        if lock.exists():
            raise RuntimeError(f"another updater appears to be running: {lock}")
        lock.mkdir(parents=True)
        try:
            if not repo.exists():
                if args.no_pull or args.check_only:
                    raise RuntimeError(f"Nature Skills clone not found: {repo}")
                repo.parent.mkdir(parents=True, exist_ok=True)
                run(repo.parent, "clone", REMOTE, str(repo))
            if not (repo / ".git").exists():
                raise RuntimeError(f"not a Git checkout: {repo}")
            remote = run(repo, "remote", "get-url", "origin").stdout.strip().rstrip("/").lower()
            if remote != REMOTE.lower():
                raise RuntimeError(f"unexpected origin: {remote}")
            if run(repo, "diff", "--quiet", check=False).returncode or run(repo, "diff", "--cached", "--quiet", check=False).returncode:
                raise RuntimeError("Nature Skills clone has tracked or staged changes")
            if not args.check_only and not args.no_pull:
                run(repo, "fetch", "--prune", "origin", "main")
                if run(repo, "merge-base", "--is-ancestor", "HEAD", "refs/remotes/origin/main", check=False).returncode:
                    raise RuntimeError("upstream history diverged; update stopped")
                run(repo, "pull", "--ff-only", "origin", "main")
            source_skills = skills(repo)
            manifest_path = dest / MANIFEST
            old_commit, old_hashes = read_manifest(manifest_path)
            current = {p.name: tree_digest(dest / p.name)[0] for p in source_skills if (dest / p.name).is_dir()}
            expected = {p.name: tree_digest(p)[0] for p in source_skills}
            if args.check_only:
                ok = current == expected and set(old_hashes) >= set(expected)
                for name in sorted(expected): print(("MATCH   " if current.get(name) == expected[name] else "MISSING ") + name)
                return 0 if ok else 1
            dest.mkdir(parents=True, exist_ok=True)
            stage = Path(tempfile.mkdtemp(prefix="nature-skills-", dir=backup))
            previous = backup / "previous"
            old = backup / ("old-" + datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S"))
            try:
                for item in source_skills:
                    shutil.copytree(item, stage / item.name)
                for item in source_skills:
                    if tree_digest(item)[0] != tree_digest(stage / item.name)[0]:
                        raise RuntimeError(f"staging verification failed: {item.name}")
                old.mkdir(parents=True)
                (old / "skills").mkdir()
                managed = list(old_hashes) or [p.name for p in dest.iterdir() if p.is_dir() and p.name.startswith("nature-")]
                for name in managed:
                    if (dest / name).is_dir(): shutil.move(str(dest / name), str(old / "skills" / name))
                if manifest_path.is_file(): shutil.copy2(manifest_path, old / "manifest.txt")
                for item in source_skills: shutil.move(str(stage / item.name), str(dest / item.name))
                lines = ["# Managed by update_nature_skills.py", f"# source={repo}", f"# commit={run(repo, 'rev-parse', 'HEAD').stdout.strip()}", f"# updated_at={datetime.now(timezone.utc).isoformat()}"]
                lines += [p.name for p in source_skills] + [f"# hash|{p.name}|{expected[p.name]}" for p in source_skills]
                manifest_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
                if previous.exists(): shutil.move(str(previous), str(backup / "previous-old"))
                shutil.move(str(old), str(previous))
                print(f"Update completed: {len(source_skills)} skills")
                return 0
            except Exception:
                for item in source_skills:
                    if (dest / item.name).exists(): shutil.rmtree(dest / item.name)
                for item in (old / "skills").iterdir() if (old / "skills").exists() else []:
                    shutil.move(str(item), str(dest / item.name))
                raise
            finally:
                shutil.rmtree(stage, ignore_errors=True)
        finally:
            lock.rmdir()
    except Exception as exc:
        print(f"UPDATE STOPPED SAFELY\nReason: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
