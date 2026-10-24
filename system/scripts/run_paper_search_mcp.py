#!/usr/bin/env python3
"""Load the Wiki's WoS credential, then run the existing Python MCP launcher."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import shlex
import sys


def read_wos_key(path: Path) -> str:
    """Read only WEB_OF_SCIENCE_API_KEY; never execute dotenv contents."""
    if not path.is_file():
        return ""
    result = ""
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        entry = line.strip()
        if entry.startswith("export "):
            entry = entry[7:].lstrip()
        name, separator, value = entry.partition("=")
        if not separator or name.strip() != "WEB_OF_SCIENCE_API_KEY":
            continue
        try:
            tokens = shlex.split(value, comments=True, posix=True)
        except ValueError:
            raise ValueError("Invalid WEB_OF_SCIENCE_API_KEY quoting") from None
        if len(tokens) > 1:
            raise ValueError("WEB_OF_SCIENCE_API_KEY must be a single value")
        result = tokens[0] if tokens else ""
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("launcher", type=Path, help="Existing Python MCP launcher")
    args = parser.parse_args()
    launcher = args.launcher.resolve()
    if not launcher.is_file() or launcher == Path(__file__).resolve():
        parser.error("Expected an existing, separate Python launcher")
    env = os.environ.copy()
    if not env.get("WOS_API_KEY", "").strip():
        key = env.get("WEB_OF_SCIENCE_API_KEY", "").strip()
        if not key:
            try:
                key = read_wos_key(Path(__file__).resolve().parents[2] / "raw/personal/.env")
            except (OSError, UnicodeError, ValueError):
                print("Cannot load WEB_OF_SCIENCE_API_KEY from the local dotenv file", file=sys.stderr)
                return 2
        if key:
            env["WOS_API_KEY"] = key
    # The existing launcher retains all other provider settings. Expanded access
    # requires its own explicit configuration; this wrapper enables Starter only.
    os.execve(sys.executable, [sys.executable, str(launcher)], env)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
