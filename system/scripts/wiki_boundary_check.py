#!/usr/bin/env python3
"""Read-only enforcement of the Wiki's canonical path contract.

The check deliberately does not inspect or hash raw evidence.  It verifies the
repository's content boundaries, known knowledge migrations, output page types,
and (when QMD is available) the collection root/pattern used for retrieval.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path
from typing import Any, Callable, Sequence


REQUIRED_DIRS = ("raw", "knowledge", "outputs", "system", "tools", "tmp")
FORBIDDEN_DIRS = ("docs/plans",)
MOVED_KNOWLEDGE = {
    "outputs/learning-milestones/2026-09-a130-thesis-evidence-matrix.md":
        "knowledge/projects/a130-thesis-evidence-matrix.md",
}
KNOWLEDGE_PAGE_TYPES = {
    "source",
    "nucleus",
    "band",
    "experiment",
    "method",
    "model",
    "observable",
    "concept",
    "project",
    "synthesis",
    "research-note",
}
OUTPUT_ROOTS = {
    "degree-dissertation",
    "high-spin",
    "l3",
    "l4",
    "learning-daily",
    "learning-milestones",
    "learning-weekly",
    "literature-acquisition",
    "paper-cards",
    "plans",
    "self-tests",
}


def _relative(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def _issue(code: str, path: str, message: str) -> dict[str, str]:
    return {"code": code, "path": path, "message": message}


def _frontmatter_type(path: Path) -> str | None:
    """Read only the small frontmatter prefix; never treat body prose as type."""

    try:
        with path.open("r", encoding="utf-8-sig") as handle:
            first = handle.readline()
            if first.strip() != "---":
                return None
            for _ in range(80):
                line = handle.readline()
                if not line or line.strip() == "---":
                    break
                match = re.match(r"^\s*type\s*:\s*['\"]?([A-Za-z0-9_-]+)", line)
                if match:
                    return match.group(1)
    except (OSError, UnicodeError):
        return None
    return None


def _run_qmd(command: Sequence[str], root: Path) -> tuple[int, str, str]:
    try:
        result = subprocess.run(
            list(command), cwd=root, text=True, capture_output=True, check=False
        )
    except OSError as exc:
        return 127, "", str(exc)
    return result.returncode, result.stdout, result.stderr


def check_qmd(
    root: Path,
    runner: Callable[[Sequence[str], Path], tuple[int, str, str]] | None = None,
) -> tuple[list[dict[str, str]], list[dict[str, str]], dict[str, Any]]:
    """Check the collection without requiring QMD in unit-test fixtures."""

    errors: list[dict[str, str]] = []
    warnings: list[dict[str, str]] = []
    details: dict[str, Any] = {"checked": False, "available": False}
    qmd = shutil.which("qmd")
    if not qmd:
        warnings.append(_issue("QMD_UNAVAILABLE", ".qmd", "qmd executable not found; use rg/direct read until it is available"))
        return errors, warnings, details

    # A temporary/public clone may not have initialized the ignored project-local
    # QMD config yet.  Do not inspect a caller's global QMD index in that case.
    if not (root / ".qmd" / "index.yml").is_file():
        warnings.append(_issue("QMD_UNCONFIGURED", ".qmd", "project-local QMD config is absent; collection scope check deferred"))
        return errors, warnings, details

    runner = runner or _run_qmd
    command = [qmd, "collection", "show", "nuclear-knowledge"]
    code, stdout, stderr = runner(command, root)
    details.update({"checked": True, "available": True, "command": command, "exit": code})
    if code != 0:
        errors.append(_issue("QMD_COLLECTION", ".qmd", (stderr or stdout).strip() or "nuclear-knowledge collection could not be inspected"))
        return errors, warnings, details

    path_match = re.search(r"(?m)^\s*Path:\s*(.+?)\s*$", stdout)
    pattern_match = re.search(r"(?m)^\s*Pattern:\s*(.+?)\s*$", stdout)
    expected_path = str((root / "knowledge").resolve())
    actual_path = path_match.group(1).strip() if path_match else None
    actual_pattern = pattern_match.group(1).strip() if pattern_match else None
    details.update({"path": actual_path, "pattern": actual_pattern})
    if actual_path is None:
        errors.append(_issue("QMD_COLLECTION_PATH_MISSING", ".qmd", "QMD did not report a collection path"))
    elif Path(actual_path).resolve() != Path(expected_path).resolve():
        errors.append(_issue("QMD_COLLECTION_PATH", ".qmd", f"nuclear-knowledge points to {actual_path!r}; expected {expected_path!r}"))
    if actual_pattern != "**/*.md":
        errors.append(_issue("QMD_COLLECTION_PATTERN", ".qmd", f"nuclear-knowledge pattern is {actual_pattern!r}; expected '**/*.md'"))
    return errors, warnings, details


def scan_boundary(
    root: Path,
    *,
    check_qmd_enabled: bool = True,
    qmd_runner: Callable[[Sequence[str], Path], tuple[int, str, str]] | None = None,
) -> dict[str, Any]:
    """Return a JSON-serializable boundary report without changing the tree."""

    root = root.resolve()
    errors: list[dict[str, str]] = []
    warnings: list[dict[str, str]] = []
    checks: dict[str, Any] = {}

    missing = [directory for directory in REQUIRED_DIRS if not (root / directory).is_dir()]
    checks["required_dirs"] = {"expected": list(REQUIRED_DIRS), "missing": missing}
    for directory in missing:
        errors.append(_issue("REQUIRED_DIR_MISSING", directory, f"required canonical directory is missing: {directory}/"))

    forbidden_present = [directory for directory in FORBIDDEN_DIRS if (root / directory).exists()]
    checks["forbidden_dirs"] = {"expected_absent": list(FORBIDDEN_DIRS), "present": forbidden_present}
    for directory in forbidden_present:
        errors.append(_issue("LEGACY_PATH_PRESENT", directory, "legacy path is not canonical; use outputs/plans/ and remove only with explicit user direction"))

    checks["moved_knowledge"] = {}
    for old, new in MOVED_KNOWLEDGE.items():
        old_exists = (root / old).exists()
        new_exists = (root / new).exists()
        checks["moved_knowledge"][old] = {"old_exists": old_exists, "canonical": new, "canonical_exists": new_exists}
        if old_exists:
            errors.append(_issue("DURABLE_KNOWLEDGE_IN_OUTPUTS", old, f"durable knowledge must live at {new}"))
        if not new_exists:
            errors.append(_issue("KNOWLEDGE_MIGRATION_MISSING", new, f"canonical knowledge page is missing after migration from {old}"))

    outputs = root / "outputs"
    output_unknown: list[str] = []
    output_knowledge_pages: list[str] = []
    if outputs.is_dir():
        for child in outputs.iterdir():
            if child.name.startswith("."):
                continue
            if child.is_dir() and child.name not in OUTPUT_ROOTS and not (
                child.name.startswith("degree-dissertation")
                or child.name.startswith("high-spin")
            ):
                output_unknown.append(_relative(root, child))
        for path in outputs.rglob("*.md"):
            page_type = _frontmatter_type(path)
            if page_type in KNOWLEDGE_PAGE_TYPES:
                relative = _relative(root, path)
                output_knowledge_pages.append(relative)
                errors.append(_issue("KNOWLEDGE_PAGE_IN_OUTPUTS", relative, f"frontmatter type {page_type!r} belongs under knowledge/; keep only a report or receipt in outputs/"))
    checks["outputs"] = {
        "allowed_roots": sorted(OUTPUT_ROOTS),
        "unknown_roots": output_unknown,
        "knowledge_page_types_in_outputs": output_knowledge_pages,
    }
    for path in output_unknown:
        errors.append(_issue("OUTPUT_ROOT_UNCLASSIFIED", path, "unlisted outputs/ category; classify it as a report, audit, receipt, scheduler state or plan in the path contract before writing here"))

    if check_qmd_enabled:
        qmd_errors, qmd_warnings, qmd_details = check_qmd(root, qmd_runner)
        errors.extend(qmd_errors)
        warnings.extend(qmd_warnings)
        checks["qmd"] = qmd_details
    else:
        checks["qmd"] = {"checked": False, "reason": "disabled"}

    return {
        "schema_version": 1,
        "root": str(root),
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
        "checks": checks,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--json", action="store_true", help="emit JSON (default is also JSON for automation)")
    parser.add_argument("--skip-qmd", action="store_true", help="skip the optional QMD collection probe")
    args = parser.parse_args()
    result = scan_boundary(args.root, check_qmd_enabled=not args.skip_qmd)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
