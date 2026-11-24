"""Validate explicit artifacts; upload to production PyPI only with --publish.

Read the token locally at publication time. Never put tokens into command
arguments, files in this project, or diagnostic output.
"""

import argparse
import os
from pathlib import Path
import re
import subprocess
import sys


def read_token(path):
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"\s*(?:export\s+)?PYPI_API_KEY\s*=\s*(.*?)\s*", line)
        if match:
            token = match[1].strip().strip("\"'")
            if token.startswith("pypi-") and not any(c.isspace() for c in token):
                return token
            raise ValueError(
                "PYPI_API_KEY is present but is not a valid token-shaped value."
            )
    raise ValueError(
        "PYPI_API_KEY was not found in the supplied local credential file."
    )


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifacts", nargs="+", type=Path)
    parser.add_argument("--publish", action="store_true")
    parser.add_argument("--token-file", type=Path)
    args = parser.parse_args(argv)
    files = [p.resolve() for p in args.artifacts]
    if any(
        not p.is_file() or not p.name.lower().startswith("multipolepdm-") for p in files
    ):
        parser.error("Supply explicit, existing multipolePDM release artifacts.")
    subprocess.run(
        [sys.executable, "-m", "twine", "check", "--strict", *map(str, files)], check=True
    )
    if not args.publish:
        print(
            "Local artifact validation only. No credentials read and no upload attempted."
        )
        return 0
    token = (
        read_token(args.token_file)
        if args.token_file
        else os.environ.get("PYPI_API_KEY", "")
    )
    if not token:
        parser.error(
            "Publication needs --token-file or PYPI_API_KEY in the process environment."
        )
    env = os.environ.copy()
    env.update(TWINE_USERNAME="__token__", TWINE_PASSWORD=token)
    completed = subprocess.run(
        [
            sys.executable,
            "-m",
            "twine",
            "upload",
            "--non-interactive",
            "--disable-progress-bar",
            "--repository-url",
            "https://upload.pypi.org/legacy/",
            *map(str, files),
        ],
        env=env,
        capture_output=True,
        text=True,
    )
    print((completed.stdout + completed.stderr).replace(token, "[redacted]"))
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
