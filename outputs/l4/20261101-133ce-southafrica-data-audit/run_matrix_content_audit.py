#!/usr/bin/env python3
from datetime import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[3]
AUDIT_DIRECTORY = Path(__file__).resolve().parent
MACRO = AUDIT_DIRECTORY / "compare_matrix_snapshot.C"
RESULT = AUDIT_DIRECTORY / "matrix-content-audit.json"
MANIFEST = ROOT / "raw/data/SouthAfrica/133Ce/analysis/provenance/manifest.json"


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main():
    if sys.byteorder != "little":
        raise ValueError("current matrix comparison requires a little-endian host")
    subprocess.run(["root", "-l", "-b", "-q", str(MACRO)], cwd=ROOT, check=True)
    result = json.loads(RESULT.read_text(encoding="utf-8"))
    paths = sorted({
        item[key] for item in result["comparisons"]
        for key in ("root_file", "matrix_file")
    })
    files = []
    for value in paths:
        path = (ROOT / value).resolve()
        if not path.is_relative_to(ROOT / "raw/data/SouthAfrica"):
            raise ValueError("matrix input is outside the authorized dataset")
        files.append({
            "path": str(path.relative_to(ROOT)),
            "size": path.stat().st_size,
            "sha256": sha256(path),
            "source": "User-supplied SouthAfrica fixed input snapshot; original producer remains to be reconstructed.",
        })
    if MANIFEST.exists():
        existing = json.loads(MANIFEST.read_text(encoding="utf-8"))
        if existing.get("files") != files:
            raise ValueError("registered matrix inputs changed; preserve the old manifest and create a new version")
    else:
        payload = {
            "schema_version": 1,
            "archive_type": "research-archive-v1",
            "retrieved_at": datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(),
            "retrieved_at_basis": "Local user-data fingerprint registration; not original acquisition time.",
            "visibility": "private",
            "scope": "Five supplied ROOT representations and eight candidate m4b inputs only.",
            "files": files,
        }
        MANIFEST.parent.mkdir(parents=True, exist_ok=True)
        with MANIFEST.open("x", encoding="utf-8") as handle:
            json.dump(payload, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
    result.update({
        "created_at": datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(),
        "visibility": "private",
        "input_manifest": str(MANIFEST.relative_to(ROOT)),
        "input_manifest_sha256": sha256(MANIFEST),
        "analysis_code_sha256": sha256(MACRO),
        "wrapper_code_sha256": sha256(Path(__file__)),
        "scope": "Bin-content identity, not event provenance, calibrated energy, detector efficiency or nuclear-structure interpretation.",
    })
    RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "comparisons": len(result["comparisons"]),
        "input_files": len(files),
        "manifest": str(MANIFEST.relative_to(ROOT)),
        "manifest_sha256": result["input_manifest_sha256"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
