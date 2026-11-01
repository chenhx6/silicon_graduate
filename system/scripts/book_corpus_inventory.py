#!/usr/bin/env python3
"""Read-only PDF census; emit counts and navigation, never extracted body text.

Run from any directory:
  python3 system/scripts/book_corpus_inventory.py --root . --output \
    outputs/learning-milestones/20261102-book-corpus-inventory.json

The output contains no run timestamp or filesystem mtime. With unchanged inputs,
script and PyMuPDF version it is byte reproducible. It does not award reading
credit or run OCR. All page numbers are one-based physical PDF pages.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor
import hashlib
import json
from pathlib import Path
import re
import sys

import pymupdf


SCHEMA = "book-corpus-inventory-v1"
DEFAULT_OUTPUT = "outputs/learning-milestones/20261102-book-corpus-inventory.json"
SPARSE_THRESHOLD = 100


def digest(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def ranges(numbers: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    for number in sorted(set(numbers)):
        if result and number == result[-1][1] + 1:
            result[-1][1] = number
        else:
            result.append([number, number])
    return result


def warning_count() -> int:
    message = pymupdf.TOOLS.mupdf_warnings(reset=True)
    return len(message.splitlines())


def rectangle_union_area(rectangles: list[tuple[float, ...]]) -> float:
    """Integrate disjoint x slabs so tiled/overlapping scans count only once."""
    edges = sorted({rect[0] for rect in rectangles} |
                   {rect[2] for rect in rectangles})
    area = 0.0
    for left, right in zip(edges, edges[1:]):
        intervals = sorted(
            (bottom, top) for x0, bottom, x1, top in rectangles
            if x0 < right and x1 > left
        )
        height = 0.0
        end = float("-inf")
        for bottom, top in intervals:
            height += max(0.0, top - max(bottom, end))
            end = max(end, top)
        area += (right - left) * height
    return area


def inspect_pdf(arguments: tuple[str, str, str]) -> dict:
    root_string, relative, book_id = arguments
    path = Path(root_string) / relative
    pymupdf.TOOLS.mupdf_display_errors(False)
    pymupdf.TOOLS.mupdf_display_warnings(False)
    warning_count()
    before = digest(path)
    result = {
        "id": book_id,
        "raw_file": relative,
        "raw_sha256": before,
        "size_bytes": path.stat().st_size,
        "archive_required": True,
        "inspection_status": "ok",
        "page_count": None,
        "bookmarks": [],
        "pages": [],
    }
    try:
        with pymupdf.open(path) as document:
            result["open_warning_lines"] = warning_count()
            if document.needs_pass:
                raise ValueError("password required")
            result["page_count"] = len(document)
            result["pdf_metadata"] = document.metadata
            result["pdf_page_label_rules"] = document.get_page_labels()
            result["bookmarks"] = [
                {
                    "level": level,
                    "title": title,
                    "pdf_page": page,
                    "destination_in_bounds": 1 <= page <= len(document),
                }
                for level, title, page in document.get_toc(simple=True)
            ]
            result["navigation_warning_lines"] = warning_count()
            for index in range(len(document)):
                warning_count()
                row = {"pdf_page": index + 1}
                try:
                    page = document[index]
                    # Explicit flags avoid embedding raster bytes in a text result.
                    text = page.get_text(
                        "text", flags=pymupdf.TEXTFLAGS_TEXT, sort=False
                    )
                    nonspace = sum(not char.isspace() for char in text)
                    row.update(
                        native_text_chars=len(text),
                        native_text_nonwhitespace_chars=nonspace,
                        replacement_chars=text.count("\ufffd"),
                        pdf_page_label=page.get_label(),
                    )
                    images = page.get_image_info(hashes=False, xrefs=False)
                    page_area = page.rect.get_area()
                    rectangles = [
                        tuple(pymupdf.Rect(image["bbox"]) & page.rect)
                        for image in images
                        if not (pymupdf.Rect(image["bbox"]) & page.rect).is_empty
                    ]
                    largest = max(
                        (
                            (pymupdf.Rect(image["bbox"]) & page.rect).get_area()
                            / page_area
                            for image in images
                        ),
                        default=0.0,
                    ) if page_area else 0.0
                    coverage = (
                        rectangle_union_area(rectangles) / page_area
                        if page_area else 0.0
                    )
                    row["raster_image_count"] = len(images)
                    row["largest_raster_page_area_fraction"] = round(largest, 6)
                    row["raster_union_page_area_fraction"] = round(coverage, 6)
                    if nonspace < SPARSE_THRESHOLD and coverage >= 0.5:
                        route = "ocr_or_visual_transcription_required"
                    elif nonspace == 0:
                        route = "no_text_visual_triage"
                    elif nonspace < SPARSE_THRESHOLD:
                        route = "sparse_text_visual_triage"
                    elif text.count("\ufffd") / max(nonspace, 1) >= 0.01:
                        route = "encoding_quality_review"
                    elif coverage >= 0.8:
                        route = "text_on_scan_quality_review"
                    else:
                        route = "native_text_available"
                    row["access_route"] = route
                except Exception as error:
                    row["error"] = f"{type(error).__name__}: {error}"
                    row["access_route"] = "page_inspection_failed"
                    result["inspection_status"] = "partial"
                row["parser_warning_lines"] = warning_count()
                result["pages"].append(row)
    except Exception as error:
        result["inspection_status"] = "failed"
        result["error"] = f"{type(error).__name__}: {error}"
    result["unchanged_during_inspection"] = digest(path) == before
    if not result["unchanged_during_inspection"]:
        result["inspection_status"] = "input_changed"
    pages = result["pages"]
    result["native_text_chars_total"] = sum(
        page.get("native_text_chars", 0) for page in pages
    )
    result["access_route_counts"] = dict(sorted(Counter(
        page["access_route"] for page in pages
    ).items()))
    result["access_route_pdf_ranges"] = {
        route: ranges([
            page["pdf_page"] for page in pages if page["access_route"] == route
        ])
        for route in sorted(result["access_route_counts"])
    }
    result["zero_native_text_pdf_ranges"] = ranges([
        page["pdf_page"] for page in pages
        if page.get("native_text_nonwhitespace_chars") == 0
    ])
    result["sparse_native_text_pdf_ranges"] = ranges([
        page["pdf_page"] for page in pages
        if 0 < page.get("native_text_nonwhitespace_chars", SPARSE_THRESHOLD)
        < SPARSE_THRESHOLD
    ])
    result["parser_warning_pdf_ranges"] = ranges([
        page["pdf_page"] for page in pages if page["parser_warning_lines"]
    ])
    result["raster_image_pdf_ranges"] = ranges([
        page["pdf_page"] for page in pages if page.get("raster_image_count", 0)
    ])
    result["formula_figure_table_boundary"] = {
        "not_certified_pdf_ranges": (
            [[1, result["page_count"]]] if result["page_count"] else []
        ),
        "meaning": (
            "No equation, figure or table is certified by this inventory. "
            "Raster ranges identify embedded images, not their scientific role; "
            "vector figures and formulas may exist on any other page. OCR output "
            "and PDF text must be checked against rendered pages before use."
        ),
    }
    return result


def scalar(lines: list[str], key: str) -> tuple[str | None, int | None]:
    if not lines or lines[0].lstrip("\ufeff") != "---":
        return None, None
    for index, line in enumerate(lines[1:], 2):
        if line == "---":
            break
        if line.startswith(key + ":"):
            value = line.split(":", 1)[1].strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                value = value[1:-1]
            return value or None, index
    return None, None


def source_records(root: Path, books: list[dict]) -> list[dict]:
    """Map literal raw paths or matching hashes; do not infer reading completion."""
    records = []
    for source in sorted((root / "knowledge/sources").rglob("*.md")):
        text = source.read_text(encoding="utf-8-sig")
        lines = text.splitlines()
        raw_file, raw_line = scalar(lines, "raw_file")
        raw_hash, hash_line = scalar(lines, "raw_sha256")
        matches = []
        for book in books:
            bases = []
            if raw_file == book["raw_file"]:
                bases.append("raw_file_exact")
            if book["raw_file"] in text and raw_file != book["raw_file"]:
                bases.append("raw_path_mentioned")
            if raw_hash and raw_hash.lower() == book["raw_sha256"]:
                bases.append("raw_sha256_exact")
            if bases:
                matches.append({"book_id": book["id"], "match_basis": bases})
        if not matches:
            continue
        headings = [
            {"line": index, "heading": line.lstrip("#").strip()}
            for index, line in enumerate(lines, 1)
            if re.match(r"^#{2,6} ", line)
        ]
        records.append({
            "source_page": source.relative_to(root).as_posix(),
            "source_page_sha256": digest(source),
            "raw_file_claimed": raw_file,
            "raw_file_line": raw_line,
            "raw_sha256_claimed": raw_hash,
            "raw_sha256_line": hash_line,
            "reading_depth_claimed": scalar(lines, "reading_depth")[0],
            "review_status_existing": scalar(lines, "review_status")[0],
            "pages_field_claimed": scalar(lines, "pages")[0],
            "matches": matches,
            "existing_headings": headings,
            "claim_table_row_count": sum(
                bool(re.match(r"^\|\s*[A-Z][A-Z0-9-]*\s*\|", line))
                for line in lines
            ),
            "completion_credit_from_inventory": 0,
        })
    return records


def link_records(root: Path, sources: list[dict], books: list[dict]) -> list[dict]:
    """Discover record candidates in knowledge; an occurrence is not verification."""
    needles: dict[str, set[str]] = defaultdict(set)
    for source in sources:
        for match in source["matches"]:
            needles[Path(source["source_page"]).stem].add(match["book_id"])
    for book in books:
        needles[book["raw_file"]].add(book["id"])
    records = []
    for path in sorted((root / "knowledge").rglob("*.md")):
        if path.name == "book-corpus-coverage-ledger.md":
            continue
        hits: dict[str, list[int]] = defaultdict(list)
        for number, line in enumerate(
            path.read_text(encoding="utf-8-sig").splitlines(), 1
        ):
            for needle, book_ids in needles.items():
                if needle in line:
                    for book_id in book_ids:
                        hits[book_id].append(number)
        if hits:
            records.append({
                "path": path.relative_to(root).as_posix(),
                "file_sha256": digest(path),
                "book_matches": [
                    {"book_id": book_id, "lines": sorted(set(numbers))}
                    for book_id, numbers in sorted(hits.items())
                ],
                "status": "reference_candidate_not_reading_credit",
            })
    return records


def build(root: Path, jobs: int) -> dict:
    corpus = root / "raw/books"
    if not corpus.is_dir():
        raise ValueError("raw/books directory does not exist")
    paths = sorted(
        (path for path in corpus.rglob("*")
         if path.is_file() and path.suffix.lower() == ".pdf"),
        key=lambda path: path.relative_to(root).as_posix(),
    )
    arguments = [
        (str(root), path.relative_to(root).as_posix(), f"B{index:02d}")
        for index, path in enumerate(paths, 1)
    ]
    books = []
    # Processes isolate MuPDF state; --jobs 1 provides a sequential reference run.
    if jobs == 1:
        results = map(inspect_pdf, arguments)
        for book in results:
            books.append(book)
            print(f'{book["id"]}: {book["page_count"]} pages '
                  f'({book["inspection_status"]})', file=sys.stderr, flush=True)
    else:
        with ProcessPoolExecutor(max_workers=jobs) as executor:
            for book in executor.map(inspect_pdf, arguments):
                books.append(book)
                print(f'{book["id"]}: {book["page_count"]} pages '
                      f'({book["inspection_status"]})', file=sys.stderr, flush=True)
    if [path.relative_to(root).as_posix() for path in paths] != sorted(
        path.relative_to(root).as_posix() for path in corpus.rglob("*")
        if path.is_file() and path.suffix.lower() == ".pdf"
    ):
        raise ValueError("PDF membership changed during inspection")
    sources = source_records(root, books)
    by_id = {book["id"]: book for book in books}
    for source in sources:
        for match in source["matches"]:
            book = by_id[match["book_id"]]
            claimed = source["raw_sha256_claimed"]
            match["claimed_hash_matches_this_pdf"] = (
                claimed.lower() == book["raw_sha256"] if claimed else None
            )
    duplicates: dict[str, list[str]] = defaultdict(list)
    for book in books:
        duplicates[book["raw_sha256"]].append(book["id"])
    return {
        "schema": SCHEMA,
        "corpus_root": "raw/books",
        "producer": {
            "script": "system/scripts/book_corpus_inventory.py",
            "script_sha256": digest(Path(__file__).resolve()),
            "pymupdf_version": pymupdf.VersionBind,
            "mupdf_version": pymupdf.VersionFitz,
            "python_version": sys.version.split()[0],
            "text_flags": pymupdf.TEXTFLAGS_TEXT,
            "timestamp_policy": "no run timestamps or filesystem times",
        },
        "measurement_contract": {
            "page_numbering": "one-based physical PDF page; not printed folio",
            "chars": "len(page.get_text('text', flags=TEXTFLAGS_TEXT, sort=False))",
            "nonwhitespace_chars": "count Unicode characters with not char.isspace()",
            "native_text": (
                "Existing PDF text layer; may include historical OCR. "
                "No OCR is run and no extracted body text is saved."
            ),
            "sparse_threshold_nonwhitespace_chars": SPARSE_THRESHOLD,
            "ocr_route": (
                "<100 nonwhitespace chars and raster union >=50% of page area. "
                "OCR or visual transcription is required for text access on any "
                "nonblank content there. Includes covers/possible blank scans; "
                "render before choosing OCR vs explicit blank exemption."
            ),
            "other_visual_triage": (
                "Zero/sparse text without a large raster is not automatically OCR "
                "failure: inspect for blank, vector figure, formula or front matter."
            ),
            "largest_raster": (
                "Largest individual displayed image rectangle clipped to page, "
                "not a union or an exact ink-area estimate."
            ),
            "raster_union": (
                "Union of clipped displayed image rectangles, including tiled "
                "scans and excluding double counting of overlaps; not ink area."
            ),
            "reading_credit": "None; extraction, bookmarks and source labels do not prove study.",
            "metadata_privacy": "PDF metadata/bookmarks and counts only; no extracted body text.",
        },
        "summary": {
            "pdf_count": len(books),
            "unique_sha256_count": len(duplicates),
            "physical_pdf_pages": sum(book["page_count"] or 0 for book in books),
            "inspected_page_rows": sum(len(book["pages"]) for book in books),
            "bookmark_count": sum(len(book["bookmarks"]) for book in books),
            "source_page_count_matched": len(sources),
            "pdfs_with_exact_raw_file_source": len({
                match["book_id"] for source in sources
                for match in source["matches"]
                if "raw_file_exact" in match["match_basis"]
            }),
            "access_route_page_counts": dict(sorted(sum(
                (Counter(book["access_route_counts"]) for book in books), Counter()
            ).items())),
            "inspection_failures": [
                book["id"] for book in books if book["inspection_status"] != "ok"
            ],
            "newly_read_chapters": 0,
            "inventory_implies_whole_library_read": False,
        },
        "duplicate_groups": [
            {"sha256": sha, "book_ids": ids}
            for sha, ids in sorted(duplicates.items()) if len(ids) > 1
        ],
        "books": books,
        "source_records": sources,
        "knowledge_reference_candidates": link_records(root, sources, books),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[2]
    )
    parser.add_argument("--output", type=Path, default=Path(DEFAULT_OUTPUT))
    parser.add_argument("--jobs", type=int, default=1)
    options = parser.parse_args()
    if options.jobs < 1:
        parser.error("--jobs must be positive")
    root = options.root.resolve()
    output = (root / options.output).resolve()
    try:
        output.relative_to(root)
        output.relative_to(root / "raw")
    except ValueError:
        if not output.is_relative_to(root):
            parser.error("--output must be inside the repository")
    else:
        parser.error("--output cannot be under raw/")
    if output.suffix.lower() != ".json":
        parser.error("--output must be a JSON file")
    if output == Path(__file__).resolve():
        parser.error("--output cannot overwrite this script")
    data = build(root, options.jobs)
    payload = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    output.parent.mkdir(parents=True, exist_ok=True)
    changed = not output.exists() or output.read_text(encoding="utf-8") != payload
    if changed:
        output.write_text(payload, encoding="utf-8", newline="\n")
    print(json.dumps({
        "output": output.relative_to(root).as_posix(),
        "changed": changed,
        **data["summary"],
    }, ensure_ascii=False, indent=2))
    return 1 if data["summary"]["inspection_failures"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
