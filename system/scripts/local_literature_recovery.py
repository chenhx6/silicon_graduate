#!/usr/bin/env python3
"""Explicit, receipt-driven local archival recovery; no network or overwrites."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import tempfile

from local_literature_archive import digest, now, safe_path, source_metadata, atomic_json

MANIFEST = "raw/reports/gpt/20261107-local-literature-recovery/manifest.json"


def set_field(text, key, value):
    """Change only a single-line field, preserving the body and its locators."""
    lines = text.splitlines(keepends=True)
    end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    value = json.dumps(value, ensure_ascii=False)
    for i in range(1, end):
        if re.match(r"^" + re.escape(key) + r":", lines[i]):
            lines[i] = f"{key}: {value}\n"
            return "".join(lines)
    lines.insert(end, f"{key}: {value}\n")
    return "".join(lines)


def copy_original(source, destination, expected):
    """Exclusive creation: an existing different object is never overwritten."""
    if digest(source) != expected:
        raise ValueError(f"candidate hash mismatch: {source}")
    if destination.exists():
        if not destination.is_file() or digest(destination) != expected:
            raise ValueError(f"destination conflict: {destination}")
        return False
    destination.parent.mkdir(parents=True, exist_ok=True)
    with source.open("rb") as incoming, destination.open("xb") as outgoing:
        shutil.copyfileobj(incoming, outgoing)
    if digest(destination) != expected:
        raise ValueError(f"copied hash mismatch: {destination}; retained for investigation")
    return True


def run(root, receipt, apply=False):
    root = Path(root).resolve()
    payload = json.loads(Path(receipt).read_text(encoding="utf-8"))
    rows = []
    entries = []
    moment = now()
    for item in payload["items"]:
        relative = item["source"]
        if not relative.startswith("knowledge/sources/") or ".." in Path(relative).parts:
            raise ValueError("source outside source directory")
        page = root / relative
        if page.is_symlink() or not page.resolve().is_relative_to(root / "knowledge/sources"):
            raise ValueError("source symlink or path escape")
        before = page.read_text(encoding="utf-8-sig")
        meta, _ = source_metadata(page)
        expected = item["expected_sha256"].lower()
        candidates = item["verified_matching_files"]
        if not candidates:
            rows.append({"source": relative, "status": "separate-version-review"})
            continue
        if str(meta.get("raw_sha256", "")).lower() != expected:
            raise ValueError(f"source identity changed since audit: {relative}")
        candidate = None
        for value in candidates:
            p = Path(value)
            if p.is_absolute() or ".." in p.parts or "personal" in p.parts:
                continue
            current = root
            for part in p.parts:
                current /= part
                if current.is_symlink():
                    raise ValueError(f"candidate symlink: {value}")
            if current.is_file() and current.resolve().is_relative_to(root) and digest(current) == expected:
                candidate = current
                break
        if candidate is None:
            raise ValueError(f"no matching candidate remains: {relative}")
        target_relative = (candidate.relative_to(root).as_posix()
                            if candidate.relative_to(root).parts[0] == "raw"
                            else item["recorded_raw_file"])
        destination = safe_path(root, target_relative)
        # Validate conflicts even in preview.
        if destination.exists() and digest(destination) != expected:
            raise ValueError(f"destination conflict: {target_relative}")
        entry = {"path": target_relative, "sha256": expected,
                 "size": candidate.stat().st_size,
                 "source": f"Local recovery of original bytes from {candidate.relative_to(root).as_posix()}; identity/provenance in {relative}",
                 "source_page": relative}
        url = meta.get("source_url") or meta.get("canonical_source", "")
        if isinstance(url, str) and url.startswith(("https://", "http://")):
            entry["url"] = url
        entries.append(entry)
        # Standalone code copies need their adjacent legal notices as well.
        if candidate.suffix.lower() in {".cc", ".cxx", ".cpp", ".for", ".f"}:
            for parent in (candidate.parent, candidate.parent.parent):
                for notice in sorted(parent.iterdir()):
                    if (not notice.is_file() or notice.is_symlink() or
                        not re.match(r"^(?:license|copying|notice)(?:[._-]|$)", notice.name, re.I) or
                        notice.stat().st_size > 1_000_000):
                        continue
                    notice_relative = str(Path(target_relative).parent /
                                          (Path(relative).stem + "-" + notice.name))
                    notice_target = safe_path(root, notice_relative)
                    notice_hash = digest(notice)
                    if any(e["path"] == notice_relative for e in entries):
                        continue
                    if notice_target.exists() and digest(notice_target) != notice_hash:
                        raise ValueError(f"notice destination conflict: {notice_relative}")
                    entries.append({"path": notice_relative, "sha256": notice_hash,
                                    "size": notice.stat().st_size, "role": "license",
                                    "source": f"Adjacent legal notice from {notice.relative_to(root).as_posix()}",
                                    "source_page": relative})
                    if apply:
                        copy_original(notice, notice_target, notice_hash)
        changed = set_field(before, "raw_file", target_relative)
        changed = set_field(changed, "raw_storage_status", "archived-local")
        changed = set_field(changed, "archive_required", True)
        changed = set_field(changed, "updated", moment[:10])
        heading = "## Local archive reconciliation — 2026-11-07"
        if heading not in changed:
            note = (f"\n\n{heading}\n\n"
                    f"Recovered/located original bytes at `{target_relative}`; SHA-256 matches the previously recorded identity. "
                    f"Recovery manifest: `{MANIFEST}`. Local recovery time: {moment}. "
                    "Earlier statements that raw was an unfilled slot describe the historical acquisition stage; "
                    "the current frontmatter records the completed local archive. "
                    "Reading scope, version attribution, claims and citation key are unchanged. "
                    "The main-file recovery does not certify every supplementary artifact is present.\n")
            # Display current availability before the historical notes.
            pos = re.search(r"(?m)^# .+\n", changed)
            if pos:
                changed = changed[:pos.end()] + note + changed[pos.end():]
            else:
                changed += note
        if apply:
            copied = copy_original(candidate, destination, expected)
            if page.read_text(encoding="utf-8-sig") != before:
                raise ValueError(f"source changed concurrently: {relative}")
            fd, temporary = tempfile.mkstemp(prefix=".recovery-", dir=page.parent)
            try:
                with os.fdopen(fd, "w", encoding="utf-8") as stream:
                    stream.write(changed)
                os.replace(temporary, page)
            finally:
                Path(temporary).unlink(missing_ok=True)
        else:
            copied = not destination.exists()
        rows.append({"source": relative, "status": "reconciled" if apply else "ready",
                     "raw_file": target_relative, "sha256": expected,
                     "copied" if apply else "copy_needed": copied})
    if apply:
        manifest_path = safe_path(root, MANIFEST)
        existing = json.loads(manifest_path.read_text()) if manifest_path.exists() else None
        manifest = {"archive_type": "research-archive-v1", "retrieved_at": moment,
                    "recovered_at": moment, "retrieval_event": "local archival recovery, not a remote download",
                    "original_remote_retrieval_time": "See original source/acquisition records; not inferred from recovery time",
                    "files": entries}
        if existing:
            if existing["files"] != entries:
                raise ValueError("existing recovery manifest differs; preserve it and reconcile explicitly")
        else:
            atomic_json(manifest_path, manifest)
    return {"applied": apply, "recovery_time": moment, "manifest": MANIFEST,
            "reconciled": sum(r["status"] == "reconciled" for r in rows),
            "ready": sum(r["status"] == "ready" for r in rows), "items": rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    parser.add_argument("--receipt", required=True)
    parser.add_argument("--apply", action="store_true", help="Explicitly perform the approved migration")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    result = run(args.root, args.receipt, args.apply)
    atomic_json(Path(args.output), result)
    print(json.dumps({k: v for k, v in result.items() if k != "items"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
