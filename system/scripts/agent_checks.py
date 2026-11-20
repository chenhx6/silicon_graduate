#!/usr/bin/env python3
"""Capture verification output, replay assertions, and inspect Python structure."""

import argparse
import ast
from contextlib import closing
import hashlib
import json
from pathlib import Path
import re
import sqlite3
import subprocess
import tempfile
import tokenize


ROOT = Path(__file__).resolve().parents[2]
SCHEMA = "wiki-agent-check/v1"
ERROR_WORDS = re.compile(r"\b(?:error|failed|failure|traceback|panic)\b", re.IGNORECASE)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def preview(data):
    lines = data.decode("utf-8", errors="replace").splitlines()
    entries = [(number, line) for number, line in enumerate(lines, 1) if line.strip()]
    flagged = [(number, line) for number, line in entries if ERROR_WORDS.search(line)]
    sample = sorted(dict([*flagged[:8], *entries[-8:]]).items())
    return {
        "lines": len(lines),
        "preview": [{"line": number, "text": line[:320]} for number, line in sample],
    }


def capture(command, label, root=ROOT):
    if not command:
        raise ValueError("provide a command after --")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,47}", label):
        raise ValueError("label must be 1–48 letters, digits, underscores or hyphens")
    cache = (root / "tmp" / "agent-checks").resolve()
    if not cache.is_relative_to((root / "tmp").resolve()):
        raise ValueError("check receipts must resolve below tmp/")
    cache.mkdir(parents=True, exist_ok=True)
    directory = Path(tempfile.mkdtemp(prefix=f"{label}-", dir=cache))
    log = directory / "output.log"
    with log.open("wb") as stream:
        try:
            process = subprocess.run(command, stdout=stream, stderr=subprocess.STDOUT, check=False)
            return_code = process.returncode
        except FileNotFoundError:
            stream.write(b"Command executable not found.\n")
            return_code = 127
        except PermissionError:
            stream.write(b"Command executable could not be started due to permissions.\n")
            return_code = 126
    data = log.read_bytes()
    result = {
        "schema": SCHEMA, "label": label, "executable": Path(command[0]).name,
        "return_code": return_code, "exit_code": return_code if return_code >= 0 else 128 - return_code,
        "output_bytes": len(data), "output_sha256": sha256(data), **preview(data),
    }
    receipt = directory / "receipt.json"
    receipt.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return {**result, "receipt": str(receipt), "log": str(log)}


def read_run(receipt):
    receipt_bytes = receipt.read_bytes()
    run = json.loads(receipt_bytes)
    if run.get("schema") != SCHEMA:
        raise ValueError("expected an agent check receipt")
    log = receipt.parent / "output.log"
    data = log.read_bytes()
    if sha256(data) != run["output_sha256"]:
        raise ValueError("captured output differs from its receipt")
    return run, data.decode("utf-8", errors="replace"), sha256(receipt_bytes)


def find(receipt, query, limit):
    words = re.findall(r"\w+", query)
    if not words or not 1 <= limit <= 50:
        raise ValueError("provide searchable terms and a limit from 1 to 50")
    _, text, digest = read_run(receipt)
    with closing(sqlite3.connect(":memory:")) as connection:
        connection.execute("CREATE VIRTUAL TABLE output USING fts5(line UNINDEXED, text)")
        connection.executemany(
            "INSERT INTO output(line, text) VALUES (?, ?)", enumerate(text.splitlines(), 1),
        )
        expression = " AND ".join(f'"{word}"' for word in words)
        matches = connection.execute(
            "SELECT line, text FROM output WHERE output MATCH ? ORDER BY rank, line LIMIT ?",
            (expression, limit),
        ).fetchall()
    return {
        "receipt_sha256": digest, "query": query,
        "hits": [{"line": number, "text": text[:1000]} for number, text in matches],
    }


def evaluate(receipt, expectations):
    run, text, digest = read_run(receipt)
    expected_bytes = expectations.read_bytes()
    expected = json.loads(expected_bytes)
    allowed = {"exit_code", "contains", "excludes", "stdout_json"}
    if not isinstance(expected, dict) or not expected or expected.keys() - allowed:
        raise ValueError("expected a nonempty JSON object of supported checks")
    checks = []
    if "exit_code" in expected:
        if type(expected["exit_code"]) is not int or expected["exit_code"] < 0:
            raise ValueError("exit_code must be a nonnegative integer")
        checks.append({"check": "exit_code", "passed": run["exit_code"] == expected["exit_code"]})
    for key in ("contains", "excludes"):
        values = expected.get(key, [])
        if not isinstance(values, list) or any(not isinstance(value, str) or not value for value in values):
            raise ValueError(f"{key} must contain nonempty strings")
        checks.extend({"check": key, "value": value, "passed": (value in text) == (key == "contains")} for value in values)
    if "stdout_json" in expected:
        fields = expected["stdout_json"]
        if not isinstance(fields, dict) or not fields:
            raise ValueError("stdout_json must contain at least one field")
        try:
            actual = json.loads(text)
        except ValueError:
            actual = None
        checks.extend(
            {"check": "stdout_json", "key": key, "passed": (
                isinstance(actual, dict) and key in actual
                and json.dumps(actual[key], sort_keys=True) == json.dumps(value, sort_keys=True)
            )}
            for key, value in fields.items()
        )
    if not checks:
        raise ValueError("expected at least one assertion")
    return {
        "receipt_sha256": digest, "expectations_sha256": sha256(expected_bytes),
        "passed": all(check["passed"] for check in checks), "checks": checks,
    }


def python_tree(path):
    with tokenize.open(path) as source:
        return ast.parse(source.read(), filename=str(path), type_comments=True)


def calls(paths, name, limit):
    if not re.fullmatch(r"[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*", name) or not 1 <= limit <= 500:
        raise ValueError("provide a callable name and a limit from 1 to 500")
    matches = []
    for path in paths:
        tree = python_tree(path)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                callee = ast.unparse(node.func)
                if callee == name or ("." not in name and callee.endswith("." + name)):
                    matches.append({"file": str(path), "line": node.lineno, "column": node.col_offset + 1, "callee": callee})
    matches.sort(key=lambda match: (match["file"], match["line"], match["column"]))
    return {"query": name, "total": len(matches), "hits": matches[:limit]}


def definitions(tree):
    named = {}
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            named.setdefault(node.name, []).append(ast.dump(node))
    return named


def compare(before, after):
    old, new = python_tree(before), python_tree(after)
    old_defs, new_defs = definitions(old), definitions(new)
    return {
        "ast_equal": ast.dump(old) == ast.dump(new),
        "added_definitions": sorted(new_defs.keys() - old_defs.keys()),
        "removed_definitions": sorted(old_defs.keys() - new_defs.keys()),
        "changed_definitions": sorted(name for name in old_defs.keys() & new_defs if old_defs[name] != new_defs[name]),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    run = commands.add_parser("capture")
    run.add_argument("label")
    run.add_argument("argv", nargs=argparse.REMAINDER)
    search = commands.add_parser("find")
    search.add_argument("receipt", type=Path)
    search.add_argument("query")
    search.add_argument("--limit", type=int, default=8)
    audit = commands.add_parser("evaluate")
    audit.add_argument("receipt", type=Path)
    audit.add_argument("expectations", type=Path)
    scan = commands.add_parser("calls")
    scan.add_argument("name")
    scan.add_argument("files", nargs="+", type=Path)
    scan.add_argument("--limit", type=int, default=40)
    diff = commands.add_parser("compare")
    diff.add_argument("before", type=Path)
    diff.add_argument("after", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "capture":
            result = capture(args.argv[1:] if args.argv[:1] == ["--"] else args.argv, args.label)
            status = result["exit_code"]
        elif args.command == "evaluate":
            result = evaluate(args.receipt, args.expectations)
            status = int(not result["passed"])
        elif args.command == "find":
            result, status = find(args.receipt, args.query, args.limit), 0
        elif args.command == "calls":
            result, status = calls(args.files, args.name, args.limit), 0
        else:
            result, status = compare(args.before, args.after), 0
    except (OSError, ValueError, KeyError, TypeError, AttributeError, SyntaxError, sqlite3.Error) as error:
        parser.exit(2, f"agent_checks: {error}\n")
    print(json.dumps(result, indent=2))
    return status


if __name__ == "__main__":
    raise SystemExit(main())
