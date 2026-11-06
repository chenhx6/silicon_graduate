#!/usr/bin/env python3
"""Archive the two missing official Ba adopted datasets; no search or fitting.

Existing 136Ba objects and Nomura source files are reused in place. This script
creates a new raw collection and refuses to overwrite it. Publisher material
is written only to that raw collection, never to the benchmark output folder.
"""

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

from bs4 import BeautifulSoup
import requests

ROOT = Path(__file__).resolve().parents[4]
RAW = ROOT / "raw/papers/gpt/query/20261106-ba-spin-moment-benchmark"


def now():
    return datetime.now(timezone.utc).isoformat()


def archive_get(mass, kind):
    url = (
        f"https://www.nndc.bnl.gov/ensnds/{mass}/Ba/adopted.pdf"
        if kind == "adopted.pdf" else
        f"https://www.nndc.bnl.gov/ensdf/DatasetFetchServlet?datasource=ensdf&mass={mass}&nucmass=isMass&searchType=ensdfIndex"
    )
    start = now()
    response = requests.get(url, timeout=45)
    response.raise_for_status()
    data = response.content
    if kind.endswith("pdf") and not data.startswith(b"%PDF"):
        raise ValueError("NNDC response is not a PDF")
    path = RAW / f"nndc{mass}-{kind}"
    with path.open("xb") as stream:
        stream.write(data)
    return {
        "path": str(path.relative_to(ROOT)), "url": url,
        "final_url": response.url, "request_method": "GET",
        "requested_at": start, "retrieved_at": now(),
        "http_status": response.status_code, "content_type": response.headers.get("Content-Type"),
        "size": len(data), "sha256": hashlib.sha256(data).hexdigest(),
        "archive_required": True,
    }


def main():
    if RAW.exists():
        raise FileExistsError(f"Refusing to overwrite collection: {RAW}")
    RAW.mkdir(parents=True)
    manifest = {
        "archive_type": "research-archive-v1", "archive_required": True,
        "retrieved_at": now(), "run_date_label": "2026-11-06",
        "acquisition_context": "Independent static-moment benchmark for the fixed Ba IBFM chain",
        "learning_candidate": True, "learning_topic": "Ba-quadrupole-calibration-and-independent-EM-constraints",
        "collection_reason": "Verify 137Ba calibration moment and cross-check the directly tabulated 135Ba negative-parity moment.",
        "files": [],
        "evidence_boundary": "Evaluated summaries, not newly acquired nuclear measurements; source keys and alternatives retained.",
    }
    try:
        jobs = [(mass, kind) for mass in (135, 137) for kind in ("index.html", "adopted.pdf")]
        with ThreadPoolExecutor(max_workers=4) as pool:
            futures = [pool.submit(archive_get, mass, kind) for mass, kind in jobs]
            for future in futures:
                manifest["files"].append(future.result())
        for mass in (135, 137):
            index_path = RAW / f"nndc{mass}-index.html"
            dataset_id = f"{mass}056001,{mass}BA"
            if dataset_id not in index_path.read_text():
                raise ValueError(f"Adopted dataset {dataset_id} not verified by official index")
            url = "https://www.nndc.bnl.gov/ensdf/EnsdfDispatcherServlet"
            parameters = {
                "dbclass": "ensdf", "page-source": "singular",
                "chooseit": "ENSDF text format", "datasetcheck": dataset_id,
            }
            requested = now()
            response = requests.post(url, data=parameters, timeout=45)
            response.raise_for_status()
            retrieved = now()
            data = response.content
            wire = RAW / f"nndc{mass}-adopted.response.html"
            with wire.open("xb") as stream:
                stream.write(data)
            wire_hash = hashlib.sha256(data).hexdigest()
            manifest["files"].append({
                "path": str(wire.relative_to(ROOT)), "url": url,
                "request_method": "POST", "request_parameters": parameters,
                "requested_at": requested, "retrieved_at": retrieved,
                "http_status": response.status_code, "content_type": response.headers.get("Content-Type"),
                "size": len(data), "sha256": wire_hash, "archive_required": True,
            })
            blocks = BeautifulSoup(data, "html.parser").find_all("pre")
            if len(blocks) != 1:
                raise ValueError("Expected one ENSDF pre block")
            text = blocks[0].get_text().encode("utf-8")
            ens = RAW / f"nndc{mass}-adopted-text.ens"
            with ens.open("xb") as stream:
                stream.write(text)
            manifest["files"].append({
                "path": str(ens.relative_to(ROOT)), "source": str(wire.relative_to(ROOT)),
                "derived_from_sha256": wire_hash, "retrieved_at": retrieved,
                "created_at_utc": now(), "archive_required": True,
                "extraction": "Exact UTF-8 text of the sole HTML pre element, without stripping or reflow.",
                "size": len(text), "sha256": hashlib.sha256(text).hexdigest(),
            })
        manifest["status"] = "retrieved"
    except Exception as exc:
        manifest["status"] = "partial"
        manifest["failure"] = f"{type(exc).__name__}: {exc}"
        raise
    finally:
        manifest["completed_at_actual_clock"] = now()
        with (RAW / "manifest.json").open("x") as stream:
            json.dump(manifest, stream, indent=2)
            stream.write("\n")
    print(json.dumps({"collection": str(RAW.relative_to(ROOT)), "files": len(manifest["files"]),
                      "status": manifest["status"]}, indent=2))


if __name__ == "__main__":
    main()
