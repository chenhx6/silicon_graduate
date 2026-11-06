"""Acquire only the explicitly listed primary sources for this bounded audit."""
import sys
sys.dont_write_bytecode = True
import concurrent.futures
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path("/workspace/wiki")
RAW = ROOT / "raw/papers/gpt/query/20261106-spin-invariant-precedents"
OUT = Path(__file__).resolve().parent


def utc():
    return datetime.now(timezone.utc).isoformat()


def fetch(spec):
    request = urllib.request.Request(
        spec["url"], headers={"User-Agent": "Research-source-audit/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            data = response.read()
            meta = {
                **spec, "retrieved_at": utc(), "resolved_url": response.url,
                "http_status": response.status,
                "content_type": response.headers.get("Content-Type", ""),
            }
        if spec.get("kind") == "pdf" and not data.startswith(b"%PDF"):
            return None, {**meta, "status": "unexpected-non-PDF-body", "size": len(data)}
        return data, meta
    except Exception as error:
        return None, {**spec, "attempted_at": utc(), "status": "access-failed",
                      "error": str(error)}


def main():
    specs = json.loads(Path(sys.argv[1]).read_text())
    RAW.mkdir(parents=True, exist_ok=True)
    manifest_path = RAW / "manifest.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {
        "archive_type": "research-archive-v1", "retrieved_at": utc(),
        "archive_required": True,
        "acquisition_context": "source-definition-and-precedent-audit",
        "learning_candidate": True,
        "learning_topic": "finite-spin quadrupole invariants and odd-A IBFM proxies",
        "collection_reason": "Primary evidence for definitions, scope and existing comparisons.",
        "files": [], "access_attempts": [],
    }
    known = {x["path"] for x in manifest["files"]}
    pending = []
    for spec in specs:
        target = RAW / spec["filename"]
        if target.parent != RAW:
            raise ValueError("filename must be a basename")
        if str(target.relative_to(ROOT)) in known:
            print("Already archived:", spec["filename"])
        else:
            if target.exists():
                raise FileExistsError(target)
            pending.append(spec)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(fetch, pending))
    for data, meta in results:
        if data is None:
            manifest["access_attempts"].append(meta)
            print("ACCESS:", meta["filename"], meta["status"], meta.get("error", ""))
            continue
        path = RAW / meta.pop("filename")
        with path.open("xb") as handle:
            handle.write(data)
        entry = {
            **meta, "path": str(path.relative_to(ROOT)),
            "sha256": hashlib.sha256(data).hexdigest(), "size": len(data),
            "archive_required": True, "learning_candidate": True,
            "learning_topic": manifest["learning_topic"],
            "collection_reason": meta.get("reason", manifest["collection_reason"]),
        }
        manifest["files"].append(entry)
        print("ARCHIVED:", path.name, len(data), entry["sha256"])
    manifest["updated_at"] = utc()
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
