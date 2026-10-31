#!/usr/bin/env python3
"""Load Wiki literature credentials, then run the existing Python MCP launcher."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import sys

from personal_api_env import apply_personal_env, read_api_key


def read_wos_key(path: Path) -> str:
    """Return WoS key: prefer Institutional_Member_Plan, fallback Free_Trial_Plan."""
    key = read_api_key(path, "WEB_OF_SCIENCE_API_KEY_Institutional_Member_Plan")
    if not key:
        key = read_api_key(path, "WEB_OF_SCIENCE_API_KEY_Free_Trial_Plan")
    return key


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("launcher", type=Path, help="Existing Python MCP launcher")
    args = parser.parse_args()
    launcher = args.launcher.resolve()
    if not launcher.is_file() or launcher == Path(__file__).resolve():
        parser.error("Expected an existing, separate Python launcher")
    env = os.environ.copy()
    wiki_root = Path(__file__).resolve().parents[2]
    try:
        apply_personal_env(env, wiki_root / "raw/personal/.env")
    except (OSError, UnicodeError, ValueError):
        print("Cannot load allowlisted personal API settings from the local dotenv file",
              file=sys.stderr)
        return 2
    for source, target in (("ELSEVIER_API_KEY", "ELSEVIER_API_KEY"),
                           ("SPRINGER_META_API_KEY", "SPRINGER_API_KEY"),
                           ("SPRINGER_OPEN_ACCESS_API_KEY", "SPRINGER_OPENACCESS_API_KEY")):
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
    # WoS: prefer Institutional_Member_Plan (5/s, 5000/day), fallback Free_Trial_Plan (1/s, 50/day)
    if not env.get("WOS_API_KEY", "").strip():
        try:
            wos_key = read_wos_key(wiki_root / "raw/personal/.env")
        except (OSError, UnicodeError, ValueError):
            print("Cannot load WoS key from the local dotenv file", file=sys.stderr)
            return 2
        if wos_key:
            env["WOS_API_KEY"] = wos_key
    env["WIKI_PAPER_SEARCH_WORKDIR"] = str(wiki_root / "raw/papers/gpt/learning-daily")
    # The existing launcher retains all other provider settings. Only Starter API
    # is available; Expanded API is not subscribed.
    os.execve(sys.executable, [sys.executable, str(launcher)], env)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
