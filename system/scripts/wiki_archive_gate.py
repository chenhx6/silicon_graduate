#!/usr/bin/env python3
"""Deterministic raw-archive and source-to-raw reconciliation checks."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Iterable

try:
    from .wiki_lint import parse_frontmatter_text
except ImportError:
    from wiki_lint import parse_frontmatter_text


RAW_ROOT = Path("raw")
SOURCE_ROOT = Path("knowledge/sources")
ARCHIVE_TYPES = ("papers", "theses", "notes", "figures", "data", "reports")
SHA256_RE = re.compile(r"[a-fA-F0-9]{64}")
PROVENANCE_ONLY_FIELDS = {"library_file", "actual_body_file", "public_staging_file", "staging_file"}


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


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8-sig")
    metadata, _, errors = parse_frontmatter_text(text)
    if errors:
        raise ValueError(f"invalid source frontmatter: {path}: {'; '.join(errors)}")
    return metadata


def safe_relative(root: Path, value: str) -> Path:
    candidate = Path(value)
    if candidate.is_absolute():
        candidate = candidate.resolve()
    else:
        candidate = (root / candidate).resolve()
    try:
        return candidate.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"path outside repository: {value}") from exc


def manifest_entries(root: Path, manifest: Path) -> list[dict[str, object]]:
    try:
        payload = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"invalid manifest {manifest}: {exc}") from exc
    entries = payload.get("files") if isinstance(payload, dict) else None
    if not isinstance(entries, list) or not entries:
        raise ValueError(f"manifest has no nonempty files list: {manifest}")
    retrieved_at = payload.get("retrieved_at")
    if not isinstance(retrieved_at, str):
        raise ValueError(f"manifest lacks retrieved_at: {manifest}")
    try:
        recorded_time = datetime.fromisoformat(retrieved_at.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError(f"manifest has invalid retrieved_at: {manifest}") from exc
    if recorded_time.tzinfo is None:
        raise ValueError(f"manifest retrieved_at lacks timezone: {manifest}")
    normalized: list[dict[str, object]] = []
    seen: set[Path] = set()
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            raise ValueError(f"manifest entry {index} is not an object: {manifest}")
        path_value = entry.get("path")
        expected = entry.get("sha256")
        if not isinstance(path_value, str) or not path_value.strip() or not isinstance(expected, str):
            raise ValueError(f"manifest entry {index} lacks path/sha256: {manifest}")
        if not SHA256_RE.fullmatch(expected):
            raise ValueError(f"manifest entry {index} has invalid sha256: {manifest}")
        relative = safe_relative(root, path_value)
        if relative in seen or (root / relative).resolve() == manifest.resolve():
            raise ValueError(f"duplicate or self-referencing manifest entry: {path_value}")
        seen.add(relative)
        origin = entry.get("url") or entry.get("source")
        if not isinstance(origin, str) or not origin.strip():
            raise ValueError(f"manifest entry {index} lacks url or source provenance: {manifest}")
        normalized.append({
            "path": path_value,
            "sha256": expected.lower(),
            "size": entry.get("size"),
            "manifest": str(manifest),
        })
    return normalized


def check_manifest(root: Path, manifest: Path) -> list[dict[str, object]]:
    failures: list[dict[str, object]] = []
    try:
        entries = manifest_entries(root, manifest)
    except ValueError as exc:
        return [{"kind": "manifest", "manifest": str(manifest), "error": str(exc)}]
    for entry in entries:
        try:
            relative = safe_relative(root, str(entry["path"]))
        except ValueError as exc:
            failures.append({"kind": "path", "manifest": str(manifest), "error": str(exc)})
            continue
        if not relative.parts or relative.parts[0] != RAW_ROOT.name:
            failures.append(
                {
                    "kind": "path",
                    "manifest": str(manifest),
                    "path": str(relative),
                    "error": "archived manifest entry must be under raw/",
                }
            )
            continue
        path = root / relative
        if not path.is_file():
            failures.append(
                {
                    "kind": "missing",
                    "manifest": str(manifest),
                    "path": str(relative),
                    "error": "archived file is missing",
                }
            )
            continue
        actual = sha256(path)
        expected_size = entry.get("size")
        if expected_size is not None and (
            type(expected_size) is not int or expected_size != path.stat().st_size
        ):
            failures.append({
                "kind": "size",
                "manifest": str(manifest),
                "path": str(relative),
                "error": "manifest size differs from archived file",
            })
        if actual != entry["sha256"]:
            failures.append(
                {
                    "kind": "hash",
                    "manifest": str(manifest),
                    "path": str(relative),
                    "expected": entry["sha256"],
                    "actual": actual,
                }
            )
    return failures


def source_pages(root: Path, paths: Iterable[str] | None = None) -> list[Path]:
    if paths is None:
        return sorted((root / SOURCE_ROOT).rglob("*.md"))
    result: list[Path] = []
    for value in paths:
        relative = safe_relative(root, value)
        path = root / relative
        if path.suffix == ".md" and relative.parts[:2] == SOURCE_ROOT.parts and path.is_file():
            result.append(path)
    return sorted(set(result))


def check_source_page(root: Path, page: Path) -> list[dict[str, object]]:
    try:
        metadata = frontmatter(page)
    except (OSError, ValueError) as exc:
        return [{"kind": "source-metadata", "source": str(page), "error": str(exc)}]
    raw_file = metadata.get("raw_file")
    if not isinstance(raw_file, str) or not raw_file.strip():
        return [{
            "kind": "source-unarchived",
            "source": str(page),
            "error": "source requires raw_file; archive available metadata when full text is inaccessible",
        }]
    try:
        relative = safe_relative(root, raw_file)
    except ValueError as exc:
        return [{"kind": "source-path", "source": str(page), "error": str(exc)}]
    raw_path = root / relative
    failures: list[dict[str, object]] = []
    if not relative.parts or relative.parts[0] != RAW_ROOT.name:
        return [
            {
                "kind": "source-path",
                "source": str(page),
                "raw_file": str(relative),
                "error": "source raw_file must be under raw/",
            }
        ]
    if not raw_path.is_file():
        failures.append(
            {
                "kind": "source-missing",
                "source": str(page),
                "raw_file": str(relative),
                "error": "source raw_file does not exist",
            }
        )
        return failures
    expected = metadata.get("raw_sha256")
    if not isinstance(expected, str) or not SHA256_RE.fullmatch(expected):
        failures.append({
            "kind": "source-hash-missing",
            "source": str(page),
            "raw_file": str(relative),
            "error": "source requires a 64-character raw_sha256 for its file or manifest",
        })
    elif expected:
        actual = sha256(raw_path)
        if not isinstance(expected, str) or actual.lower() != expected.lower():
            failures.append(
                {
                    "kind": "source-hash",
                    "source": str(page),
                    "raw_file": str(relative),
                    "expected": expected,
                    "actual": actual,
                }
            )
    if raw_path.name == "manifest.json":
        failures.extend(check_manifest(root, raw_path))
    for key, value in metadata.items():
        if key == "raw_file" or key in PROVENANCE_ONLY_FIELDS or not key.endswith("_file") or not value:
            continue
        if not isinstance(value, str):
            failures.append({"kind": "companion-path", "source": str(page), "field": key,
                             "error": "companion archive path must be a string"})
            continue
        try:
            companion = safe_relative(root, value)
            if not companion.parts or companion.parts[0] != "raw":
                raise ValueError("companion artifact must be under raw/")
            companion_path = root / companion
            if not companion_path.is_file():
                raise ValueError("companion artifact is missing")
            companion_hash = metadata.get(key[:-5] + "_sha256")
            if not isinstance(companion_hash, str) or not SHA256_RE.fullmatch(companion_hash):
                raise ValueError("companion artifact requires a SHA-256")
            if sha256(companion_path) != companion_hash.lower():
                raise ValueError("companion artifact hash mismatch")
            if companion_path.name == "manifest.json":
                failures.extend(check_manifest(root, companion_path))
        except (OSError, ValueError) as exc:
            failures.append({"kind": "companion-archive", "source": str(page), "field": key,
                             "path": value, "error": str(exc)})
    return failures


def all_manifests(root: Path) -> list[Path]:
    return sorted(
        path
        for kind in ARCHIVE_TYPES
        for path in root.glob(f"raw/{kind}/gpt/learning-daily/**/manifest.json")
    )


def manifest_kind(path: Path) -> str:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return "invalid"
    if not isinstance(payload, dict):
        return "invalid"
    if "files" in payload or payload.get("archive_type") == "research-archive-v1":
        return "archive"
    if ("version" in payload and isinstance(payload.get("results"), list)) or "sources" in payload:
        return "legacy-receipt"
    if {"file", "sha256", "retrieved_at"}.issubset(payload):
        return "legacy-receipt"
    return "invalid"


def manifests(root: Path) -> list[Path]:
    return [path for path in all_manifests(root) if manifest_kind(path) != "legacy-receipt"]


def changed_paths(root: Path) -> list[str]:
    commands = [
        ["git", "-C", str(root), "diff", "--name-only", "--diff-filter=ACMRT", "-z", "--"],
        ["git", "-C", str(root), "diff", "--cached", "--name-only", "--diff-filter=ACMRT", "-z", "--"],
        ["git", "-C", str(root), "ls-files", "--others", "--exclude-standard", "-z", "--"],
    ]
    paths: set[str] = set()
    for command in commands:
        result = subprocess.run(command, capture_output=True, check=False, timeout=30)
        if result.returncode:
            raise ValueError("cannot determine changed archive scope: " + result.stderr.decode(errors="replace").strip())
        paths.update(value.decode("utf-8") for value in result.stdout.split(b"\0") if value)
    return sorted(paths)


def changed_archive_scope(root: Path) -> list[str]:
    paths = set(changed_paths(root))
    paths.update(str(path) for path in manifests(root))
    for page in source_pages(root):
        metadata = frontmatter(page)
        if metadata.get("archive_required") is True:
            paths.add(str(page))
    return sorted(paths)


def run_check(root: Path, paths: list[str] | None, full: bool) -> dict[str, object]:
    root = root.resolve()
    if not full and paths is None:
        raise ValueError("explicit paths are required for a bounded archive check")
    failures: list[dict[str, object]] = []
    for value in paths or []:
        try:
            relative = safe_relative(root, value)
        except ValueError as exc:
            failures.append({"kind": "requested-path", "path": value, "error": str(exc)})
            continue
        if not (root / relative).is_file():
            failures.append({"kind": "requested-missing", "path": value, "error": "requested file does not exist"})
    if failures:
        return {"ok": False, "scope": "paths", "checked_sources": [], "checked_manifests": [],
                "failure_count": len(failures), "failures": failures}
    pages = source_pages(root, None if full else paths)
    checked_sources = []
    for page in pages:
        checked_sources.append(str(page))
        failures.extend(check_source_page(root, page))

    checked_manifests = manifests(root) if full else [
        root / Path(value) for value in (paths or []) if Path(value).name == "manifest.json"
    ]
    unique_manifests = sorted({path.resolve() for path in checked_manifests if path.is_file()})
    for manifest in unique_manifests:
        try:
            relative = safe_relative(root, str(manifest))
            if relative.parts[0] != "raw":
                raise ValueError("archive manifest must be under raw/")
            failures.extend(check_manifest(root, manifest))
        except ValueError as exc:
            failures.append({"kind": "manifest-path", "path": str(manifest), "error": str(exc)})

    return {
        "ok": not failures,
        "scope": "full" if full else "paths",
        "checked_sources": checked_sources,
        "checked_manifests": [str(path) for path in unique_manifests],
        "failure_count": len(failures),
        "failures": failures,
    }


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]
    argv = [item for item in argv if item != "--"]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["check"])
    parser.add_argument("--root", default=None)
    scope = parser.add_mutually_exclusive_group()
    scope.add_argument("--full", action="store_true", help="check every source page and archived learning manifest")
    scope.add_argument("--changed", action="store_true", help="check changed sources and all registered learning manifests")
    parser.add_argument("paths", nargs="*")
    args = parser.parse_intermixed_args(argv)
    root = repo_root(args.root)
    if not args.full and not args.changed and not args.paths:
        parser.error("provide explicit files, --changed, or --full")
    try:
        selected = args.paths
        if args.changed:
            selected = sorted(set(selected + changed_archive_scope(root)))
        result = run_check(root, selected or [], args.full)
        if args.changed or args.full:
            result["legacy_receipts_not_archive_validated"] = [
                str(path) for path in all_manifests(root) if manifest_kind(path) == "legacy-receipt"
            ]
    except (OSError, ValueError, subprocess.TimeoutExpired) as exc:
        result = {"ok": False, "failure_count": 1, "failures": [{"kind": "archive-check", "error": str(exc)}]}
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
