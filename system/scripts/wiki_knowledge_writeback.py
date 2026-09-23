#!/usr/bin/env python3
"""Validate a report's explicit knowledge/source mapping, without writing files.

This verifies paths, anchors and run-local changes. Scientific support and full
coverage of a report's findings still require the workflow's evidence self-audit.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path, PurePosixPath
from typing import Any


def snapshot_knowledge(root: Path) -> dict[str, str]:
    """Hash only knowledge Markdown, never following links into raw or outside."""
    root = root.resolve()
    snapshot: dict[str, str] = {}
    for directory, dirs, files in os.walk(root / "knowledge", followlinks=False):
        dirs[:] = [name for name in dirs if not (Path(directory) / name).is_symlink()]
        for name in files:
            path = Path(directory) / name
            if path.suffix == ".md" and not path.is_symlink():
                snapshot[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return snapshot


def _knowledge_file(root: Path, value: Any, *, source: bool = False) -> Path:
    if not isinstance(value, str):
        raise ValueError("knowledge/source path must be a repository-relative string")
    parts = PurePosixPath(value).parts
    expected = ("knowledge", "sources") if source else ("knowledge",)
    if (parts[:len(expected)] != expected or ".." in parts or "\\" in value
            or not value.endswith(".md")):
        raise ValueError(f"invalid {'source' if source else 'knowledge'} path: {value}")
    path = root.joinpath(*parts)
    cursor = root
    for part in parts:
        cursor = cursor / part
        if cursor.is_symlink():
            raise ValueError(f"knowledge/source must not be a symlink: {value}")
    if not path.is_file():
        raise ValueError(f"missing knowledge/source page: {value}")
    return path


def _text(value: Any, field: str) -> str:
    if not isinstance(value, str) or len(value.strip()) < 3:
        raise ValueError(f"{field} must contain a concrete non-empty value")
    return value.strip()


def validate_writeback(
    report_path: Path,
    root: Path,
    *,
    before: dict[str, str] | None = None,
    after: dict[str, str] | None = None,
    allow_not_applicable: bool = False,
) -> dict[str, Any]:
    """Require one knowledge-writeback JSON block in a scoped output report.

    With a run-local snapshot, 'updated' requires a real change to at least one
    mapped page. A no-op requires existing grounded knowledge, a reason, and no
    changes to those mapped pages. No-op text is never a bypass for bad links.
    """
    result: dict[str, Any] = {
        "valid": False, "mode": None, "knowledge_paths": [],
        "changed_paths": [], "change_check": "not-requested" if before is None else "run-snapshot",
        "error": None,
    }
    root = root.resolve()
    try:
        report_path.resolve().relative_to(root / "outputs")
        content = report_path.read_text(encoding="utf-8-sig")
        blocks = re.findall(r"(?ms)^```knowledge-writeback[ \t]*\n(.*?)^```[ \t]*$", content)
        if len(blocks) != 1:
            raise ValueError("report must contain exactly one knowledge-writeback JSON block")
        data = json.loads(blocks[0])
        if not isinstance(data, dict):
            raise ValueError("knowledge-writeback must be an object")
        mode = data.get("status")
        result["mode"] = mode
        if mode == "not-applicable" and allow_not_applicable:
            _text(data.get("reason"), "reason")
            if data.get("items") != []:
                raise ValueError("not-applicable is for process-only reports with items: []")
            result["valid"] = True
            return result
        if mode not in {"updated", "verified-no-op"}:
            raise ValueError("daily knowledge status must be updated or verified-no-op")
        if mode == "verified-no-op":
            _text(data.get("reason"), "verified-no-op reason")
        items = data.get("items")
        if not isinstance(items, list) or not items:
            raise ValueError("knowledge items are required, including for verified-no-op")
        for item in items:
            if not isinstance(item, dict):
                raise ValueError("each knowledge item must be an object")
            _text(item.get("summary"), "summary")
            page = _knowledge_file(root, item.get("knowledge"))
            body = page.read_text(encoding="utf-8-sig")
            anchor = _text(item.get("anchor"), "knowledge anchor")
            if anchor not in body:
                raise ValueError(f"knowledge anchor not found in {item['knowledge']}: {anchor}")
            sources = item.get("sources")
            if not isinstance(sources, list) or not sources:
                raise ValueError(f"sources/locators required for {item['knowledge']}")
            for reference in sources:
                if not isinstance(reference, dict):
                    raise ValueError("each source reference must be an object")
                source = _knowledge_file(root, reference.get("path"), source=True)
                locator = _text(reference.get("locator"), "source locator/claim ID")
                if locator not in source.read_text(encoding="utf-8-sig"):
                    raise ValueError(
                        f"locator/claim ID not found in {reference['path']}: {locator}; "
                        "use one exact atomic locator per source reference and keep "
                        "combined claim IDs or page ranges in summary/note"
                    )
                # A source page can be its own durable target. Other targets must
                # themselves link to this source, not only the output report.
                linked = re.search(r"\[\[(?:knowledge/)?(?:sources/)?" + re.escape(source.stem)
                                   + r"(?:\.md)?(?:[|#][^\]]*)?\]\]", body)
                if source != page and not linked and (source.stem + ".md") not in body:
                    raise ValueError(f"knowledge page does not link to source {source.stem}")
            relative = page.relative_to(root).as_posix()
            if relative not in result["knowledge_paths"]:
                result["knowledge_paths"].append(relative)
            for reference in sources:
                source_relative = PurePosixPath(reference["path"]).as_posix()
                if source_relative not in result["knowledge_paths"]:
                    result["knowledge_paths"].append(source_relative)
        if before is not None:
            after = after if after is not None else snapshot_knowledge(root)
            result["changed_paths"] = sorted(
                path for path in (set(before) | set(after)) if before.get(path) != after.get(path)
            )
            mapped = set(result["knowledge_paths"])
            unmapped = sorted(set(result["changed_paths"]) - mapped)
            if unmapped:
                raise ValueError("knowledge changes must be listed in writeback items: " + ", ".join(unmapped))
        if before is not None:
            if mode == "updated" and not result["changed_paths"]:
                raise ValueError("updated claimed, but no mapped knowledge page changed during this run")
            if mode == "verified-no-op" and result["changed_paths"]:
                raise ValueError("verified-no-op contradicts changed knowledge pages; report updated instead")
        result["valid"] = True
    except (OSError, UnicodeError, ValueError, TypeError) as exc:
        result["error"] = str(exc)
    return result
