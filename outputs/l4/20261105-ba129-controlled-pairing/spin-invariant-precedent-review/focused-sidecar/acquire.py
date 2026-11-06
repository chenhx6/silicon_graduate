"""Acquire the two newly identified primary sources without changing old archives."""
import sys
sys.dont_write_bytecode = True
import concurrent.futures
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT=Path("/workspace/wiki")
OUT=Path(__file__).resolve().parent
RAW=ROOT/"raw/papers/gpt/query/20261106-spin-invariant-precedents/focused-sidecar"
SPECS=[
    {
        "filename":"frauendorf2026-systematic-tpsm-2609.10431v1.pdf",
        "url":"https://arxiv.org/pdf/2609.10431v1",
        "kind":"pdf",
        "title":"Systematic study of E2 matrix elements in the framework of the Triaxial Projected Shell Model",
        "access_scope":"Public author-deposited arXiv v1; preprint/proceedings status; local research copy.",
    },
    {
        "filename":"frauendorf2026-arxiv-record.html",
        "url":"https://arxiv.org/abs/2609.10431",
        "kind":"metadata",
        "title":"Primary arXiv bibliographic and version-history record",
        "access_scope":"Public arXiv record; preserve actual retrieval time separately from collection date.",
    },
    {
        "filename":"lawrie-orce2025-simple-ratios-publisher.pdf",
        "url":"https://uwcscholar.uwc.ac.za/bitstreams/dd87f780-b191-4fc4-99ae-c87324cf032a/download",
        "kind":"pdf",
        "title":"Triaxial nuclear shapes from simple ratios of electric-quadrupole matrix elements",
        "doi":"10.1016/j.adt.2025.101730",
        "access_scope":"Public institutional deposit of the publisher article; license checked in acquired original.",
    },
    {
        "filename":"lawrie-orce2025-crossref.json",
        "url":"https://api.crossref.org/works/10.1016/j.adt.2025.101730",
        "kind":"metadata",
        "title":"Primary DOI metadata for ADND164,101730",
        "access_scope":"Public Crossref metadata.",
    },
]


def now():
    return datetime.now(timezone.utc).isoformat()


def get(spec):
    try:
        req=urllib.request.Request(spec["url"],headers={"User-Agent":"Primary-source-research-audit/1.0"})
        with urllib.request.urlopen(req,timeout=45) as res:
            data=res.read()
            meta={**spec,"resolved_url":res.url,"http_status":res.status,
                  "content_type":res.headers.get("Content-Type",""),"retrieved_at":now()}
        if spec["kind"]=="pdf" and not data.startswith(b"%PDF"):
            return None,{**meta,"status":"unexpected-non-PDF-body","size":len(data)}
        return data,meta
    except Exception as exc:
        return None,{**spec,"attempted_at":now(),"status":"access-failed","error":str(exc)}


def main():
    if RAW.exists():
        raise FileExistsError("This acquisition preserves existing files; choose an explicit new collection if needed.")
    RAW.mkdir(parents=True)
    manifest={
        "archive_type":"research-archive-v1","archive_required":True,
        "retrieved_at":now(),"requested_collection_date":"2026-11-06",
        "acquisition_context":"focused-novelty-sidecar-primary-verification",
        "learning_candidate":True,"learning_topic":"angular-channel E2 observables versus complete quadrupole moments",
        "collection_reason":"Verify fresh 2026 TPSM and 2025 simple-ratio precedents from original full text.",
        "clock_note":"Timestamp fields are actual host UTC readings; do not replace them with the nominal directory date.",
        "files":[],"access_attempts":[],
    }
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results=list(pool.map(get,SPECS))
    for data,meta in results:
        if data is None:
            manifest["access_attempts"].append(meta)
            print("ACCESS FAILURE",meta["filename"],meta.get("error",meta["status"]))
            continue
        name=meta.pop("filename"); dest=RAW/name
        with dest.open("xb") as handle: handle.write(data)
        item={**meta,"path":str(dest.relative_to(ROOT)),"size":len(data),
              "sha256":hashlib.sha256(data).hexdigest(),"archive_required":True,
              "learning_candidate":True,"learning_topic":manifest["learning_topic"],
              "collection_reason":manifest["collection_reason"]}
        manifest["files"].append(item)
        print("ARCHIVED",name,len(data),item["sha256"])
    (RAW/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")


if __name__=="__main__":
    main()
