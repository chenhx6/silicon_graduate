#!/usr/bin/env python3
import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "raw/data/SouthAfrica"
MANIFEST = Path(__file__).with_name("fixed-input-reclassification-plan.json")
RECEIPT = Path(__file__).with_name("fixed-input-reclassification-receipt.json")
MOVES = [
    ("133Ce/analysis/matrices", "133Ce_iThemba2019/mat/root"),
    ("133Ce/calibration", "133Ce_iThemba2019/calibration/source-spectra"),
]


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def make_plan():
    if MANIFEST.exists() or RECEIPT.exists():
        raise ValueError("plan or receipt already exists; inspect it before another action")
    entries = []
    for source, destination in MOVES:
        source_root = DATA / source
        destination_root = DATA / destination
        if not source_root.is_dir() or destination_root.exists():
            raise ValueError(f"invalid move boundary: {source} -> {destination}")
        for path in sorted(source_root.rglob("*")):
            if path.is_symlink():
                raise ValueError(f"symlink requires separate review: {path}")
            if not path.is_file():
                continue
            target = destination_root / path.relative_to(source_root)
            entries.append({
                "source": str(path.relative_to(ROOT)),
                "destination": str(target.relative_to(ROOT)),
                "size": path.stat().st_size,
                "sha256": sha256(path),
            })
    return {
        "created_at": datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(),
        "authorization": "User explicitly requested fixed processed matrices and original calibration under 133Ce_iThemba2019; later analyses under 133Ce.",
        "classification": "Immutable as-supplied snapshot; this does not certify original producer, reaction or event provenance.",
        "directory_moves": MOVES,
        "files": entries,
        "deletions": [],
    }


def apply_plan():
    if RECEIPT.exists():
        raise ValueError("receipt exists; the reclassification has already been attempted")
    plan = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if plan["directory_moves"] != [list(pair) for pair in MOVES]:
        raise ValueError("directory move scope does not match the authorized task")
    current_sources = set()
    expected_destinations = {}
    for source, destination in MOVES:
        source_root = DATA / source
        destination_root = DATA / destination
        if not source_root.is_dir() or destination_root.exists():
            raise ValueError(f"directory move boundary changed: {source}")
        for path in source_root.rglob("*"):
            if path.is_symlink():
                raise ValueError(f"symlink requires separate review: {path}")
            if path.is_file():
                relative = str(path.relative_to(ROOT))
                current_sources.add(relative)
                expected_destinations[relative] = str(
                    (destination_root / path.relative_to(source_root)).relative_to(ROOT)
                )
    if current_sources != {entry["source"] for entry in plan["files"]}:
        raise ValueError("source file inventory changed since the dry run")
    for entry in plan["files"]:
        if expected_destinations[entry["source"]] != entry["destination"]:
            raise ValueError("file destination does not match the authorized directory move")
        source = ROOT / entry["source"]
        target = ROOT / entry["destination"]
        if not source.is_file() or target.exists() or sha256(source) != entry["sha256"]:
            raise ValueError(f"pre-move verification failed: {source}")
    for source, destination in MOVES:
        target = DATA / destination
        target.parent.mkdir(parents=True, exist_ok=True)
        (DATA / source).rename(target)
    failures = []
    for entry in plan["files"]:
        source = ROOT / entry["source"]
        target = ROOT / entry["destination"]
        if source.exists() or not target.is_file() or sha256(target) != entry["sha256"]:
            failures.append(entry["destination"])
    receipt = {
        "verified_at": datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(),
        "file_count": len(plan["files"]),
        "byte_count": sum(entry["size"] for entry in plan["files"]),
        "deletions": 0,
        "overwrites": 0,
        "passed": not failures,
        "failures": failures,
        "rollback": "Verify hashes, then reverse the two directory_moves; no content was rewritten.",
    }
    RECEIPT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return receipt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if args.apply:
        receipt = apply_plan()
        print(json.dumps(receipt, ensure_ascii=False))
        return 0 if receipt["passed"] else 1
    plan = make_plan()
    MANIFEST.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"plan": str(MANIFEST), "file_count": len(plan["files"]),
                      "byte_count": sum(entry["size"] for entry in plan["files"])}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
