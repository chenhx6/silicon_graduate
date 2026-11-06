#!/usr/bin/env python3
"""Archive official adopted datasets for 132,134,136Ba; never re-fetch 128/130Ba."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import re

from bs4 import BeautifulSoup
import requests

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
RAW = ROOT / "raw/papers/gpt/query/20261106-ba-core-E2-calibration"
MASSES = (132, 134, 136)
MANIFEST = RAW / "manifest.json"
UA = "WikiResearch/1.0 (official nuclear-data source verification)"


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def retrieve(job):
    name, url, parameters = job
    destination = RAW / name
    if destination.exists():
        return {"path": str(destination.relative_to(ROOT)), "skip": "already archived"}
    record = {
        "url": url,
        "request_method": "POST" if parameters else "GET",
        "request_parameters": parameters,
        "requested_at": now(),
        "archive_required": True,
    }
    try:
        response = requests.request(
            record["request_method"], url, data=parameters,
            headers={"User-Agent": UA}, timeout=(15, 50),
        )
        data = response.content
        with destination.open("xb") as handle:
            handle.write(data)
        record.update(
            path=str(destination.relative_to(ROOT)),
            retrieved_at=now(),
            final_url=response.url,
            http_status=response.status_code,
            content_type=response.headers.get("Content-Type"),
            size=len(data),
            sha256=digest(data),
            pdf_magic=data.startswith(b"%PDF"),
            artifact_kind="http-response-body",
            access_boundary="Pending identity/format inspection",
        )
    except requests.RequestException as exc:
        record.update(error_type=type(exc).__name__, retrieved_at=now(),
                      access_boundary="No response body acquired")
    return record


def save_records(records):
    if MANIFEST.exists():
        manifest = json.loads(MANIFEST.read_text())
    else:
        manifest = {
            "archive_type": "research-archive-v1",
            "archive_required": True,
            "retrieved_at": now(),
            "task_label": "20261106-ba-core-E2-calibration",
            "timestamp_policy": "Actual measured UTC; task label is not a retrieval timestamp",
            "acquisition_context": "focused first-2+ E2 isotope-chain calibration",
            "learning_candidate": True,
            "learning_topic": "even 128–136Ba first-2+ quadrupole strength provenance",
            "collection_reason": "Independent even-core input for single-j IBFM isotope-chain study",
            "files": [],
        }
    existing = {item["path"] for item in manifest["files"]}
    manifest["files"].extend(
        item for item in records if "sha256" in item and item["path"] not in existing
    )
    manifest["last_updated_at"] = now()
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    receipt_path = OUT / "acquisition.json"
    receipt = json.loads(receipt_path.read_text()) if receipt_path.exists() else []
    receipt.extend(records)
    receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--coulomb", action="store_true",
                        help="Fetch method summaries from already archived indexes")
    args = parser.parse_args()
    role = "coulomb" if args.coulomb else "adopted"
    identity = "COULOMB EXCITATION" if args.coulomb else "ADOPTED LEVELS, GAMMAS"
    RAW.mkdir(parents=True, exist_ok=True)
    jobs = []
    for a in (() if args.coulomb else MASSES):
        jobs.extend([
            (f"nndc{a}-index.html",
             "https://www.nndc.bnl.gov/ensdf/DatasetFetchServlet?"
             f"datasource=ensdf&mass={a}&nucmass=isMass&searchType=ensdfIndex", None),
            (f"nndc{a}-adopted.pdf",
             f"https://www.nndc.bnl.gov/ensnds/{a}/Ba/adopted.pdf", None),
        ])
    with ThreadPoolExecutor(max_workers=3) as pool:
        first = list(pool.map(retrieve, jobs))
    save_records(first)
    post_jobs = []
    selections = []
    for a in MASSES:
        soup = BeautifulSoup((RAW / f"nndc{a}-index.html").read_bytes(), "html.parser")
        matches = []
        for checkbox in soup.find_all("input", attrs={"name": "datasetcheck"}):
            value = checkbox.get("value", "")
            row = checkbox.find_parent("tr")
            text = row.get_text(" ", strip=True) if row else ""
            if value.endswith(f",{a}BA") and identity in text:
                matches.append((value, text))
        if len(matches) != 1:
            raise ValueError(f"{a}Ba {role} index selection: {len(matches)} matches")
        value, text = matches[0]
        selections.append({"mass": a, "datasetcheck": value, "index_row_text": text})
        parameters = {"dbclass": "ensdf", "page-source": "singular",
                      "chooseit": "ENSDF text format", "datasetcheck": value}
        post_jobs.append((f"nndc{a}-{role}.response.html",
                          "https://www.nndc.bnl.gov/ensdf/EnsdfDispatcherServlet",
                          parameters))
        if args.coulomb and a == 134:
            post_jobs.append(("nndc134-coulomb.pdf",
                              "https://www.nndc.bnl.gov/ensdf/EnsdfDispatcherServlet",
                              parameters | {"chooseit": "PDF Version"}))
    (OUT / f"{role}-dataset-selection.json").write_text(
        json.dumps(selections, ensure_ascii=False, indent=2) + "\n"
    )
    with ThreadPoolExecutor(max_workers=3) as pool:
        second = list(pool.map(retrieve, post_jobs))
    save_records(second)
    extracted = []
    for a in MASSES:
        wrapper = RAW / f"nndc{a}-{role}.response.html"
        soup = BeautifulSoup(wrapper.read_bytes(), "html.parser")
        pre = soup.find_all("pre")
        if len(pre) != 1:
            raise ValueError(f"{a}Ba response has {len(pre)} pre elements")
        text = pre[0].get_text()
        if not re.search(rf"^{a}BA\s+{re.escape(identity)}", text, re.MULTILINE):
            raise ValueError(f"{a}Ba extracted payload identity does not match")
        payload = text.encode("utf-8")
        destination = RAW / f"nndc{a}-{role}-text.ens"
        if destination.exists():
            if destination.read_bytes() != payload:
                raise ValueError("Existing extraction differs; no overwrite")
            continue
        with destination.open("xb") as handle:
            handle.write(payload)
        extracted.append({
            "path": str(destination.relative_to(ROOT)),
            "source": str(wrapper.relative_to(ROOT)),
            "derived_from_sha256": digest(wrapper.read_bytes()),
            "created_at_utc": now(),
            "artifact_kind": "derived-ensdf-text",
            "extraction": "Exact text content of sole HTML pre element, UTF-8; no strip, reflow or line normalization",
            "size": len(payload),
            "sha256": digest(payload),
            "archive_required": True,
            "access_boundary": "Official evaluated dataset extracted from archived wire HTML; not raw measurement data",
        })
    save_records(extracted)
    for item in first + second + extracted:
        print(json.dumps({k: item[k] for k in
                          ("path", "http_status", "size", "pdf_magic", "error_type", "skip")
                          if k in item}, ensure_ascii=False))


if __name__ == "__main__":
    main()
