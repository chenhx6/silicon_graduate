#!/usr/bin/env python3
"""Find passages in archived PDFs and replay labeled literature screening."""

import argparse
from collections import Counter
from dataclasses import dataclass
import hashlib
import json
import math
import os
from pathlib import Path
import re
import subprocess
import tempfile
import unicodedata
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[2]
GREEK = dict(zip("αβγδελμστ", "alpha beta gamma delta epsilon lambda mu sigma tau".split()))
TOKEN = re.compile(r"[a-z][a-z0-9]*|\d+(?:\.\d+)?|[\u3400-\u9fff]+")
STOPWORDS = set("a an and are as at be by for from in is it of on or that the this to was were with".split())
LABELS = {"relevant", "irrelevant"}
RECEIPT_SCHEMA = "wiki-literature-evidence/v1"


def terms(text):
    text = unicodedata.normalize("NFKC", text).casefold()
    for symbol, name in GREEK.items():
        text = text.replace(symbol, f" {name} ")
    for token in TOKEN.findall(text):
        if token[0] >= "\u3400" and token[0] <= "\u9fff" and len(token) > 1:
            yield from (token[index:index + 2] for index in range(len(token) - 1))
        elif token not in STOPWORDS:
            yield token


def file_hash(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_json(path):
    with Path(path).open(encoding="utf-8") as handle:
        return json.load(handle)


def raw_pdf(root, name):
    original = root / name
    resolved = original.resolve(strict=True)
    raw_root = (root / "raw").resolve()
    if not resolved.is_relative_to(raw_root) or not resolved.is_file() or resolved.suffix.lower() != ".pdf":
        raise ValueError(f"expected an archived PDF under raw/: {name}")
    return resolved, (Path("raw") / resolved.relative_to(raw_root)).as_posix()


def extract_pdf(path, options):
    result = subprocess.run(
        ["pdftotext", "-enc", "UTF-8", *options, str(path), "-"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120, check=False,
    )
    if result.returncode:
        raise ValueError(f"pdftotext failed for {path.name}: {result.stderr.decode('utf-8', errors='replace').strip()}")
    return result.stdout


def pdf_pages(path, digest, directory):
    directory.mkdir(parents=True, exist_ok=True)
    cache = directory / f"{digest}.json"
    try:
        pages = read_json(cache)
        if isinstance(pages, list) and pages and all(isinstance(page, str) for page in pages):
            return pages
    except (FileNotFoundError, ValueError):
        pass
    pages = extract_pdf(path, ["-layout"]).decode("utf-8").split("\f")
    if len(pages) > 1 and not pages[-1].strip():
        pages.pop()
    if file_hash(path) != digest:
        raise ValueError(f"original changed during extraction: {path.name}")
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=directory, delete=False) as temporary:
        temporary_path = Path(temporary.name)
        try:
            json.dump(pages, temporary, ensure_ascii=False)
            temporary.close()
            os.replace(temporary_path, cache)
        finally:
            temporary_path.unlink(missing_ok=True)
    return pages


def pdf_layout(root, name, page_number):
    if page_number < 1:
        raise ValueError("PDF pages start at 1")
    path, relative = raw_pdf(root, name)
    digest = file_hash(path)
    page_argument = str(page_number)
    raw = extract_pdf(path, ["-f", page_argument, "-l", page_argument, "-bbox-layout"])
    page = ElementTree.fromstring(raw).find(".//{*}page")
    if page is None:
        raise ValueError(f"no layout returned for PDF page {page_number}")
    if file_hash(path) != digest:
        raise ValueError(f"original changed during extraction: {path.name}")
    blocks = []
    for block in page.findall(".//{*}block"):
        lines = [
            " ".join("".join(word.itertext()) for word in line.findall("{*}word"))
            for line in block.findall("{*}line")
        ]
        if any(lines):
            blocks.append({
                "bbox_pt": [float(block.attrib[key]) for key in ("xMin", "yMin", "xMax", "yMax")],
                "lines": lines,
            })
    return {
        "raw_file": relative, "sha256": digest, "pdf_page": page_number,
        "width_pt": float(page.attrib["width"]), "height_pt": float(page.attrib["height"]),
        "coordinate_origin": "top-left", "blocks": blocks,
    }


@dataclass
class Passage:
    pdf: str
    sha256: str
    page: int
    start_line: int
    text: str
    counts: Counter


def page_passages(pdf, digest, page, text):
    lines = text.splitlines()
    for offset in range(0, len(lines), 12):
        excerpt = "\n".join(lines[offset:offset + 18])
        counts = Counter(terms(excerpt))
        if counts:
            yield Passage(pdf, digest, page, offset + 1, excerpt, counts)
        if offset + 18 >= len(lines):
            break


def rank_passages(passages, query, limit):
    query_counts = Counter(terms(query))
    if not query_counts:
        raise ValueError("query must contain at least one searchable term")
    if not passages:
        return []
    lengths = [sum(passage.counts.values()) for passage in passages]
    average = sum(lengths) / len(lengths)
    frequencies = Counter(term for passage in passages for term in query_counts.keys() & passage.counts.keys())
    weights = {
        term: math.log1p((len(passages) - count + 0.5) / (count + 0.5))
        for term, count in frequencies.items()
    }
    scores = []
    for passage, length in zip(passages, lengths):
        matched = query_counts.keys() & passage.counts.keys()
        normalizer = 1.2 * (0.25 + 0.75 * length / average)
        score = sum(
            weights[term] * (2.2 * passage.counts[term]) / (passage.counts[term] + normalizer)
            for term in sorted(matched)
        )
        if score:
            scores.append((score, len(matched), passage, sorted(matched)))
    scores.sort(key=lambda hit: (-hit[0], -hit[1], hit[2].pdf, hit[2].page, hit[2].start_line))
    output = []
    seen_pages = set()
    for score, _, passage, matched in scores:
        location = (passage.sha256, passage.page)
        if location in seen_pages:
            continue
        seen_pages.add(location)
        output.append({
            "raw_file": passage.pdf, "sha256": passage.sha256, "pdf_page": passage.page,
            "extractor_line": passage.start_line, "matched_terms": matched,
            "search_score": round(score, 6), "excerpt": passage.text,
        })
        if len(output) == limit:
            break
    return output


def evidence(root, pdfs, query, limit, gap=None, prior=None):
    if not 1 <= limit <= 100:
        raise ValueError("limit must be between 1 and 100")
    if not list(terms(query)):
        raise ValueError("query must contain at least one searchable term")
    previous = set()
    parent = None
    expected = {}
    if prior:
        prior_bytes = Path(prior).read_bytes()
        parent = json.loads(prior_bytes)
        if parent.get("schema") != RECEIPT_SCHEMA or not gap or not gap.strip():
            raise ValueError("a follow-up requires an evidence receipt and a specific evidence gap")
        expected = {item["raw_file"]: item["sha256"] for item in parent["corpus"]}
        pdfs = [*expected, *pdfs]
        previous = {tuple(location) for location in parent["seen_locations"]}

    cache = (root / "tmp" / "literature-learning" / "poppler-layout-v1").resolve()
    if not cache.is_relative_to((root / "tmp").resolve()):
        raise ValueError("PDF extraction cache must resolve under tmp/")
    corpus = []
    passages = []
    visited = set()
    for name in dict.fromkeys(pdfs):
        path, relative = raw_pdf(root, name)
        digest = file_hash(path)
        expected_digest = expected.get(name, expected.get(relative))
        if expected_digest is not None and digest != expected_digest:
            raise ValueError(f"original differs from the earlier receipt: {relative}")
        if digest in visited:
            continue
        visited.add(digest)
        pages = pdf_pages(path, digest, cache)
        unsearchable = []
        for number, text in enumerate(pages, 1):
            candidates = list(page_passages(relative, digest, number, text))
            if not candidates:
                unsearchable.append(number)
            passages.extend(candidates)
        corpus.append({
            "raw_file": relative, "sha256": digest, "pdf_pages": len(pages),
            "pages_without_searchable_text": unsearchable,
        })
    if not corpus:
        raise ValueError("provide at least one archived PDF")
    hits = rank_passages(passages, query, limit)
    discovered = {(hit["sha256"], hit["pdf_page"]) for hit in hits}
    for hit in hits:
        hit["page_in_earlier_results"] = (hit["sha256"], hit["pdf_page"]) in previous
    receipt = {
        "schema": RECEIPT_SCHEMA, "query": query, "round": parent["round"] + 1 if parent else 1,
        "gap": gap, "parent_receipt_sha256": hashlib.sha256(prior_bytes).hexdigest() if parent else None,
        "corpus": corpus, "hits": hits, "seen_locations": sorted(previous | discovered),
    }
    return receipt


@dataclass
class Candidate:
    identifier: str
    record: dict
    label: str | None
    counts: Counter


def read_candidates(document, labels):
    records = document.get("results") if isinstance(document, dict) else document
    if not isinstance(records, list) or not records:
        raise ValueError("provide a candidate list or a get-paper manifest with results")
    if not isinstance(labels, dict):
        raise ValueError("labels must map candidate IDs to relevant or irrelevant")
    candidates = []
    visited = set()
    for record in records:
        if not isinstance(record, dict) or not isinstance(record.get("title"), str):
            raise ValueError("each candidate must have a title")
        title = record["title"].strip()
        identifier = record.get("id") or record.get("doi") or record.get("arxiv_id") or record.get("url") or title
        if not title or not isinstance(identifier, str) or not identifier.strip() or identifier in visited:
            raise ValueError(f"empty or duplicate candidate identity: {identifier!r}")
        visited.add(identifier)
        label = labels.get(identifier, record.get("label"))
        if label is not None and (not isinstance(label, str) or label not in LABELS):
            raise ValueError(f"invalid screening label for {identifier}")
        abstract = record.get("abstract") or ""
        if not isinstance(abstract, str):
            raise ValueError(f"abstract must be text for {identifier}")
        counts = Counter(terms(f"{title} {title} {abstract}"))
        candidates.append(Candidate(identifier, record, label, counts))
    unknown = set(labels) - visited
    if unknown:
        raise ValueError("labels refer to missing candidates: " + ", ".join(sorted(unknown)))
    return candidates


class ScreeningModel:
    def __init__(self):
        self.counts = {label: Counter() for label in LABELS}

    def add(self, candidate):
        self.counts[candidate.label].update(candidate.counts)

    def rank(self, candidates):
        positive = self.counts["relevant"]
        negative = self.counts["irrelevant"]
        vocabulary = positive.keys() | negative.keys()
        if not positive or not negative:
            return [(candidate, None) for candidate in candidates]
        positive_total = positive.total() + len(vocabulary)
        negative_total = negative.total() + len(vocabulary)
        weights = {
            term: math.log((positive[term] + 1) / positive_total) - math.log((negative[term] + 1) / negative_total)
            for term in vocabulary
        }
        results = []
        for candidate in candidates:
            known = candidate.counts.keys() & vocabulary
            score = sum(weights[term] * candidate.counts[term] for term in sorted(known))
            results.append((candidate, score / max(sum(candidate.counts.values()), 1)))
        return sorted(results, key=lambda item: -item[1])


def screen(candidates):
    model = ScreeningModel()
    unlabeled = []
    label_counts = Counter()
    for candidate in candidates:
        if candidate.label is None:
            unlabeled.append(candidate)
        else:
            label_counts[candidate.label] += 1
            model.add(candidate)
    return {
        "candidate_count": len(candidates), "labels": dict(label_counts),
        "ranking": [
            {"screen_id": candidate.identifier, "screen_rank": index,
             "screen_score": None if score is None else round(score, 6), "record": candidate.record}
            for index, (candidate, score) in enumerate(model.rank(unlabeled), 1)
        ],
    }


def retrieval_curve(order, positive_count):
    found = 0
    curve = []
    for examined, candidate in enumerate(order, 1):
        if candidate.label == "relevant":
            found += 1
            curve.append({"reviewed": examined, "found": found, "recall": found / positive_count})
    return curve


def replay(candidates, seed_ids):
    if any(candidate.label is None for candidate in candidates):
        raise ValueError("replay requires a pool with known labels for every candidate")
    seed_set = set(seed_ids)
    seeds = [candidate for candidate in candidates if candidate.identifier in seed_set]
    if len(seeds) != len(seed_set) or {candidate.label for candidate in seeds} != LABELS:
        raise ValueError("replay requires existing seed IDs with both relevant and irrelevant labels")
    model = ScreeningModel()
    for seed in seeds:
        model.add(seed)
    pool = [candidate for candidate in candidates if candidate.identifier not in seed_set]
    positive_count = sum(candidate.label == "relevant" for candidate in pool)
    if not positive_count:
        raise ValueError("replay requires at least one relevant candidate outside the seeds")
    remaining = pool.copy()
    active = []
    while remaining:
        selected, _ = model.rank(remaining)[0]
        remaining.remove(selected)
        active.append(selected)
        model.add(selected)
    return {
        "seed_ids": [candidate.identifier for candidate in seeds], "held_out_count": len(pool),
        "held_out_relevant": positive_count,
        "baseline": retrieval_curve(pool, positive_count), "adaptive": retrieval_curve(active, positive_count),
        "baseline_order": [candidate.identifier for candidate in pool],
        "adaptive_order": [candidate.identifier for candidate in active],
    }


def add_search_args(command):
    command.add_argument("--query", required=True)
    command.add_argument("--limit", type=int, default=12)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    initial = commands.add_parser("evidence", help="rank passages in explicit archived PDFs")
    initial.add_argument("pdf", nargs="+")
    add_search_args(initial)
    followup = commands.add_parser("followup", help="search again for an explicit evidence gap")
    followup.add_argument("receipt")
    followup.add_argument("--gap", required=True)
    followup.add_argument("--pdf", action="append", default=[])
    add_search_args(followup)
    layout = commands.add_parser("layout", help="locate text blocks and coordinates on one archived PDF page")
    layout.add_argument("pdf")
    layout.add_argument("--page", required=True, type=int)
    rank = commands.add_parser("screen", help="rank unscreened records from prior decisions")
    simulate = commands.add_parser("replay", help="compare active screening to the supplied order")
    for command in (rank, simulate):
        command.add_argument("candidates")
        command.add_argument("--labels")
    simulate.add_argument("--seed", action="append", required=True)
    args = parser.parse_args()
    try:
        if args.command == "evidence":
            result = evidence(ROOT, args.pdf, args.query, args.limit)
        elif args.command == "followup":
            result = evidence(ROOT, args.pdf, args.query, args.limit, args.gap, args.receipt)
        elif args.command == "layout":
            result = pdf_layout(ROOT, args.pdf, args.page)
        else:
            manifest_bytes = Path(args.candidates).read_bytes()
            label_bytes = Path(args.labels).read_bytes() if args.labels else None
            labels = json.loads(label_bytes) if label_bytes is not None else {}
            candidates = read_candidates(json.loads(manifest_bytes), labels)
            result = screen(candidates) if args.command == "screen" else replay(candidates, args.seed)
            result["candidate_manifest_sha256"] = hashlib.sha256(manifest_bytes).hexdigest()
            result["label_manifest_sha256"] = hashlib.sha256(label_bytes).hexdigest() if label_bytes is not None else None
    except FileNotFoundError as error:
        message = "pdftotext is required for PDF searches (install Poppler)" if error.filename == "pdftotext" else str(error)
        parser.exit(2, f"literature_learning: {message}\n")
    except (OSError, ValueError, KeyError, TypeError, AttributeError, ElementTree.ParseError, subprocess.TimeoutExpired) as error:
        parser.exit(2, f"literature_learning: {error}\n")
    print(json.dumps(result, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
