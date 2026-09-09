#!/usr/bin/env python3
"""Lightweight, cross-platform repository capability check.

The terminal Codex profile already grants full access.  This command keeps a
small auditable gate for scripts that want to verify the expected repository,
configuration, and protected BibTeX baseline before publishing.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
import uuid
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def config_default(path: Path) -> str | None:
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8")
    match = re.search(r"(?m)^\s*default_permissions\s*=\s*[\"']([^\"']+)[\"']", text)
    return match.group(1) if match else None


def probe(directory: Path, token: str) -> dict[str, object]:
    name = f".codex-write-probe-{uuid.uuid4().hex}.tmp"
    target = directory / name
    try:
        target.write_text(token, encoding="utf-8")
        if target.read_text(encoding="utf-8") != token:
            raise OSError("probe read-back mismatch")
        return {"path": str(directory), "created": True, "read_back": True,
                "deleted": True, "error": None}
    except Exception as exc:
        return {"path": str(directory), "created": target.exists(),
                "read_back": False, "deleted": not target.exists(),
                "error": str(exc)}
    finally:
        try:
            target.unlink(missing_ok=True)
        except Exception:
            pass


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--expected-profile", default="")
    parser.add_argument("--baseline-bib-hash")
    parser.add_argument("--protected-bib-hash", help="Deprecated compatibility option")
    args = parser.parse_args()

    result: dict[str, object] = {
        "schema_version": 1, "ok": False, "root": args.root,
        "expected_profile": args.expected_profile,
        "actual_profile": os.environ.get("CODEX_PERMISSION_PROFILE"),
        "warnings": [], "write_probes": [], "error": None,
    }
    try:
        root = Path(args.root).expanduser().resolve()
        result["root"] = str(root)
        if not (root / ".git").exists():
            raise ValueError(f"not a repository: {root}")
        default = config_default(root / ".codex" / "config.toml")
        result["config_default"] = default
        if args.expected_profile and default != args.expected_profile:
            raise ValueError(f"default_permissions is {default!r}, expected {args.expected_profile!r}")
        bib = root / "raw" / "zotero" / "wiki-inbox.bib"
        if bib.is_file():
            actual = sha256(bib)
            baseline = (args.baseline_bib_hash or actual).upper()
            result["protected_bib"] = {"path": str(bib), "baseline_sha256": baseline,
                                        "actual_sha256": actual,
                                        "status": "matched" if baseline == actual else "mismatch"}
            if baseline != actual:
                raise ValueError("protected BibTeX changed since the supplied baseline")
        elif args.baseline_bib_hash:
            raise FileNotFoundError("protected BibTeX baseline supplied but wiki-inbox.bib is absent")
        else:
            result["protected_bib"] = {"path": str(bib), "baseline_sha256": None,
                                        "actual_sha256": None, "status": "absent"}
        if args.protected_bib_hash:
            result["warnings"].append("--protected-bib-hash is deprecated and ignored")
        token = f"wiki-preflight-{uuid.uuid4().hex}"
        result["write_probes"] = [probe(root, token), probe(root / ".git", token)]
        if not all(item["created"] and item["read_back"] and item["deleted"]
                   for item in result["write_probes"]):
            raise PermissionError("repository write probe failed")
        result["ok"] = True
        result["exit_code"] = 0
        print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
        return 0
    except Exception as exc:
        result["error"] = {"code": "preflight_failed", "message": str(exc)}
        result["exit_code"] = 1
        print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
