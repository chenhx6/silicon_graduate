#!/usr/bin/env python3
"""Load Wiki literature credentials, then run the existing Python MCP launcher."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import shlex
import sys


def read_api_key(path: Path, variable: str) -> str:
    """Read one allowlisted credential; never execute dotenv contents."""
    if variable not in {"WEB_OF_SCIENCE_API_KEY", "ELSEVIER_API_KEY"}:
        raise ValueError("Unsupported credential variable")
    if not path.is_file():
        return ""
    result = ""
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        entry = line.strip()
        if entry.startswith("export "):
            entry = entry[7:].lstrip()
        name, separator, value = entry.partition("=")
        if not separator or name.strip() != variable:
            continue
        try:
            tokens = shlex.split(value, comments=True, posix=True)
        except ValueError:
            raise ValueError(f"Invalid {variable} quoting") from None
        if len(tokens) > 1:
            raise ValueError(f"{variable} must be a single value")
        result = tokens[0] if tokens else ""
    return result


def read_wos_key(path: Path) -> str:
    """Compatibility entry point for existing WoS permission tooling."""
    return read_api_key(path, "WEB_OF_SCIENCE_API_KEY")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("launcher", type=Path, help="Existing Python MCP launcher")
    args = parser.parse_args()
    launcher = args.launcher.resolve()
    if not launcher.is_file() or launcher == Path(__file__).resolve():
        parser.error("Expected an existing, separate Python launcher")
    env = os.environ.copy()
    wiki_root = Path(__file__).resolve().parents[2]
    for source, target in (("WEB_OF_SCIENCE_API_KEY", "WOS_API_KEY"),
                           ("ELSEVIER_API_KEY", "ELSEVIER_API_KEY")):
        if env.get(target, "").strip():
            continue
        key = env.get(source, "").strip()
        if not key:
            try:
                key = read_api_key(wiki_root / "raw/personal/.env", source)
            except (OSError, UnicodeError, ValueError):
                print(f"Cannot load {source} from the local dotenv file", file=sys.stderr)
                return 2
        if key:
            env[target] = key
    env["WIKI_PAPER_SEARCH_WORKDIR"] = str(wiki_root / "raw/papers/gpt/_incoming")
    # The existing launcher retains all other provider settings. Expanded access
    # requires its own explicit configuration; this wrapper enables Starter only.
    os.execve(sys.executable, [sys.executable, str(launcher)], env)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
