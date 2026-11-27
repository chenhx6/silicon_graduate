#!/usr/bin/env python3
"""Read-only consistency checks for optional research-cycle records; no scientific adjudication."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
from typing import Any

SCHEMA = "wiki-research-cycle-v1"
BLOCK = re.compile(r"^```research-cycle\s*\n(.*?)^```\s*$", re.M | re.S)
KINDS = {"direct-report", "author-interpretation", "model-result", "task-inference"}
OUTCOMES = {"supports", "limits", "refutes", "no-material-change", "not-executed"}
SHA256 = re.compile(r"[0-9a-fA-F]{64}\Z")


def validate_record(record: Any) -> list[str]:
    """Check internal commitments only; source truth and physical conditions require direct audit."""
    errors: list[str] = []

    def problem(where: str, message: str) -> None:
        errors.append(f"{where}: {message}")

    def text(obj: dict, key: str, where: str) -> None:
        if not isinstance(obj.get(key), str) or not obj[key].strip():
            problem(where, f"nonempty {key} required")

    def objects(value: Any, where: str) -> list[dict]:
        if not isinstance(value, list):
            problem(where, "array required")
            return []
        if any(not isinstance(x, dict) for x in value):
            problem(where, "all entries must be objects")
        return [x for x in value if isinstance(x, dict)]

    if not isinstance(record, dict):
        return ["record: object required"]
    if record.get("schema") != SCHEMA:
        problem("record", f"schema must be {SCHEMA}")
    text(record, "question", "record")
    hypotheses = objects(record.get("hypotheses"), "hypotheses")
    if not hypotheses:
        problem("hypotheses", "at least one retained candidate required")
    ids: set[str] = set()
    parents: dict[str, str | None] = {}
    for i, h in enumerate(hypotheses):
        where = f"hypotheses[{i}]"
        for key in ("id", "claim", "alternative", "prediction", "falsifier", "minimum_check", "null_value"):
            text(h, key, where)
        hid = h.get("id")
        if isinstance(hid, str):
            if hid in ids:
                problem(where, "duplicate hypothesis ID")
            ids.add(hid)
            parent = h.get("parent")
            if parent is not None and not isinstance(parent, str):
                problem(where, "parent must be an ID or null")
                parent = None
            parents[hid] = parent
        if h.get("disposition") == "rejected":
            text(h, "rejection_reason", where)
            text(h, "revival_condition", where)
        novelty = h.get("novelty")
        if not isinstance(novelty, dict):
            problem(where, "novelty boundary required")
        else:
            if not isinstance(novelty.get("status"), str) or novelty.get("status") not in {"not-checked", "search-incomplete", "bounded-search"}:
                problem(where, "novelty status must retain search boundary, never assert universal priority")
            text(novelty, "limits", where + ".novelty")
            if novelty.get("status") == "bounded-search":
                for key in ("queries", "closest_work"):
                    if not isinstance(novelty.get(key), list) or not novelty[key]:
                        problem(where, f"bounded-search requires {key}")
                text(novelty, "searched_at", where + ".novelty")
    for hid, parent in parents.items():
        if parent is not None and parent not in ids:
            problem(hid, "unknown hypothesis parent")
        visited = {hid}
        while parent in parents:
            if parent in visited:
                problem(hid, "hypothesis tree contains a cycle")
                break
            visited.add(parent)
            parent = parents[parent]
    cycles = objects(record.get("cycles"), "cycles")
    if not cycles:
        problem("cycles", "at least one action record required")
    cycle_ids: set[str] = set()
    for i, c in enumerate(cycles):
        where = f"cycles[{i}]"
        for key in ("id", "selection_reason", "belief_revision", "next_action"):
            text(c, key, where)
        cid = c.get("id")
        if isinstance(cid, str):
            if cid in cycle_ids:
                problem(where, "duplicate cycle ID")
            cycle_ids.add(cid)
        if not isinstance(c.get("hypothesis_id"), str) or c.get("hypothesis_id") not in ids:
            problem(where, "unknown hypothesis_id")
        outcome = c.get("outcome")
        if not isinstance(outcome, str) or outcome not in OUTCOMES:
            problem(where, "invalid outcome")
        action = c.get("action")
        if not isinstance(action, dict):
            problem(where, "action object required")
            action = {}
        text(action, "description", where + ".action")
        if not isinstance(action.get("state"), str) or action.get("state") not in {"planned", "executed"}:
            problem(where, "action state must be planned or executed")
        if action.get("state") != "executed" and c.get("promote") is True:
            problem(where, "planned work cannot be promoted")
        if action.get("state") != "executed" and outcome != "not-executed":
            problem(where, "planned action cannot support a research outcome")
        if action.get("state") == "executed":
            text(action, "artifact", where + ".action")
            if outcome == "not-executed":
                problem(where, "executed action conflicts with not-executed outcome")
        evidence = objects(c.get("evidence", []), where + ".evidence")
        if action.get("state") == "executed" and not evidence:
            problem(where, "executed action requires evidence locators")
        lineages: set[str] = set()
        for j, e in enumerate(evidence):
            ew = f"{where}.evidence[{j}]"
            for key in ("source_id", "locator", "lineage"):
                text(e, key, ew)
            if not isinstance(e.get("kind"), str) or e.get("kind") not in KINDS:
                problem(ew, "claim kind required")
            if e.get("kind") == "direct-report" and isinstance(e.get("lineage"), str):
                lineages.add(e["lineage"])
        claimed = c.get("independent_lineages_claimed", 0)
        if type(claimed) is not int or claimed < 0 or claimed > len(lineages):
            problem(where, "independent support exceeds distinct declared direct-report lineages")
        verification = c.get("verification")
        if not isinstance(verification, dict):
            problem(where, "verification scope required")
        else:
            if not isinstance(verification.get("basis"), str) or verification.get("basis") not in {"direct-source", "independent-reference", "same-implementation", "not-performed"}:
                problem(where, "invalid verification basis")
            text(verification, "scope", where + ".verification")
            if action.get("state") == "executed" and verification.get("basis") == "not-performed" and c.get("promote") is True:
                problem(where, "unverified result cannot be promoted")
        if outcome == "refutes":
            text(c, "failure_constraint", where)
        absent = c.get("absent_companion")
        if absent is not None:
            if not isinstance(absent, dict):
                problem(where, "absent_companion must be an object")
            elif absent.get("used_as_falsifier") is True:
                if absent.get("sensitivity") != "adequate":
                    problem(where, "missing signal needs adequate sensitivity before falsification")
                text(absent, "sensitivity_evidence", where + ".absent_companion")
        validation = c.get("validation")
        if validation is not None:
            if not isinstance(validation, dict):
                problem(where, "validation must be an object")
                continue
            for key in ("input_sha256", "evaluator_sha256", "baseline_evaluator_sha256"):
                if not isinstance(validation.get(key), str) or not SHA256.fullmatch(validation[key]):
                    problem(where, f"validation needs valid {key}")
            if validation.get("evaluator_sha256") != validation.get("baseline_evaluator_sha256"):
                problem(where, "changed evaluator needs a new baseline before comparison")
            if not isinstance(validation.get("scope"), str) or validation.get("scope") not in {"exploratory", "internal-recovery", "independent-check"}:
                problem(where, "invalid validation scope")
            dev = validation.get("development_ids")
            confirm = validation.get("confirmation_ids")
            for key, value in (("development_ids", dev), ("confirmation_ids", confirm)):
                if not isinstance(value, list) or any(not isinstance(x, str) or not x.strip() for x in value):
                    problem(where, f"{key} must be an array of nonempty IDs")
            if validation.get("scope") == "independent-check":
                if not confirm:
                    problem(where, "independent check needs confirmation IDs")
                if isinstance(dev, list) and isinstance(confirm, list) and all(isinstance(x, str) for x in dev + confirm):
                    if set(dev) & set(confirm):
                        problem(where, "development and confirmation data overlap")
                if validation.get("confirmation_used_for_selection") is not False:
                    problem(where, "selection-used confirmation is no longer unseen")
                if isinstance(verification, dict) and verification.get("basis") not in ("independent-reference", "direct-source"):
                    problem(where, "same-implementation recovery cannot claim independent validation")
                text(validation, "independence_basis", where + ".validation")
    return errors


def load_records(path: Path) -> list[Any]:
    content = path.read_text(encoding="utf-8-sig")
    if path.suffix.lower() == ".json":
        return [json.loads(content)]
    blocks = BLOCK.findall(content)
    if not blocks:
        raise ValueError("no research-cycle block found")
    return [json.loads(block) for block in blocks]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("paths", type=Path, nargs="+")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    reports = []
    for value in args.paths:
        path = (root / value).resolve() if not value.is_absolute() else value.resolve()
        issues: list[str] = []
        count = 0
        try:
            relative = path.relative_to(root)
            if not relative.parts or relative.parts[0] not in {"knowledge", "outputs", "tmp", "system"}:
                raise ValueError("input must be a knowledge page, receipt, test fixture or temporary record")
            if path.suffix.lower() not in {".md", ".json"}:
                raise ValueError("only Markdown or JSON is supported")
            for count, record in enumerate(load_records(path), 1):
                issues.extend(f"record[{count}]: {issue}" for issue in validate_record(record))
        except (OSError, UnicodeError, ValueError) as exc:
            issues.append(str(exc))
        reports.append({"path": str(path), "records": count, "issues": issues})
    ok = not any(report["issues"] for report in reports)
    print(json.dumps({"ok": ok, "reports": reports, "boundary": "record consistency only; no source truth, priority, physical validity or capability certification"}, ensure_ascii=False, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
