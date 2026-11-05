"""Inspect mechanical PDF properties; optionally render whole-book contact sheets."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess

import pymupdf


def font_inventory(pdf):
    tool = shutil.which("pdffonts")
    if not tool:
        return {"status": "not_checked", "reason": "pdffonts unavailable"}
    run = subprocess.run([tool, str(pdf)], capture_output=True, text=True)
    if run.returncode:
        return {"status": "not_checked", "reason": run.stderr.strip()}
    # Parse columns from the right: emb, sub, uni, object-ID, generation.
    rows = [line.rsplit(None, 5) for line in run.stdout.splitlines()[2:] if line.strip()]
    if not rows or any(len(row) != 6 or row[1] not in {"yes", "no"} for row in rows):
        return {"status": "not_checked", "reason": "No parseable font inventory",
                "raw": run.stdout}
    missing = [row[0] for row in rows if row[1] != "yes"]
    return {"status": "pass" if not missing else "fail",
            "unembedded": missing, "raw": run.stdout}


def render_contacts(document, target):
    target.mkdir(parents=True, exist_ok=True)
    sheets = []
    for start in range(0, len(document), 24):
        board = pymupdf.open()
        canvas = board.new_page(width=840, height=1890)
        for number in range(start, min(start + 24, len(document))):
            row, col = divmod(number - start, 4)
            x, y = col * 210, row * 315
            canvas.insert_text((x + 6, y + 13), f"PDF {number + 1}", fontsize=10)
            page = document[number]
            pix = page.get_pixmap(matrix=pymupdf.Matrix(.5, .5), alpha=False)
            canvas.insert_image(pymupdf.Rect(x + 4, y + 20, x + 206, y + 311),
                                pixmap=pix, keep_proportion=True)
        path = target / f"pages-{start + 1:04d}-{min(start + 24, len(document)):04d}.png"
        canvas.get_pixmap(alpha=False).save(path)
        sheets.append({"path": str(path), "pages": [start + 1, min(start + 24, len(document))]})
        board.close()
    manifest = {"sheets": sheets, "visual_review_performed": False}
    (target / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--log", type=Path)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--contact-dir", type=Path)
    parser.add_argument("--page-size", choices=["a4", "any"], default="a4")
    args = parser.parse_args()
    issues, warnings = [], []
    with pymupdf.open(args.pdf) as document:
        if document.needs_pass or not len(document):
            raise SystemExit("PDF is encrypted or empty; inspect source before auditing.")
        wrong_pages, landscape_pages = [], []
        control_pages, broken_links, remote_links = [], [], []
        image_dpi = []
        for i, page in enumerate(document):
            short, long = sorted((page.rect.width, page.rect.height))
            if args.page_size == "a4" and not (
                abs(short - 595.276) < 1 and abs(long - 841.890) < 1
            ):
                wrong_pages.append(i + 1)
            if page.rect.width > page.rect.height:
                landscape_pages.append(i + 1)
            text = page.get_text()
            if "\ufffd" in text or any(ord(c) < 32 and c not in "\n\r\t" for c in text):
                control_pages.append(i + 1)
            for link in page.get_links():
                if link["kind"] == pymupdf.LINK_GOTO or (
                    link["kind"] == pymupdf.LINK_NAMED and "page" in link
                ):
                    if not 0 <= link.get("page", -1) < len(document):
                        broken_links.append({"page": i + 1, "target": link})
                elif link["kind"] in (pymupdf.LINK_GOTOR, pymupdf.LINK_LAUNCH, pymupdf.LINK_NAMED):
                    remote_links.append({"page": i + 1, "target": link})
            for image in page.get_image_info():
                width, height = pymupdf.Rect(image["bbox"]).width, pymupdf.Rect(image["bbox"]).height
                if width > 0 and height > 0:
                    dpi = min(image["width"] / width * 72, image["height"] / height * 72)
                    if dpi < 250:
                        image_dpi.append({"page": i + 1, "minimum_dpi": round(dpi, 1)})
        toc = document.get_toc()
        if wrong_pages:
            issues.append({"code": "page_size", "pages": wrong_pages})
        if control_pages:
            issues.append({"code": "suspect_unicode", "pages": control_pages})
        if broken_links:
            issues.append({"code": "invalid_internal_links", "items": broken_links})
        if not document.metadata.get("title", "").strip():
            issues.append({"code": "missing_title_metadata"})
        if not toc or any(item[0] > 3 for item in toc):
            issues.append({"code": "missing_or_excess_bookmark_levels"})
        bad_bookmarks = [item for item in toc if not 1 <= item[2] <= len(document)]
        if bad_bookmarks:
            issues.append({"code": "bookmark_destinations_need_review", "items": bad_bookmarks})
        if remote_links:
            warnings.append({"code": "nonlocal_or_named_links_need_review", "items": remote_links})
        if landscape_pages:
            warnings.append({"code": "landscape_pages_verify_intent", "pages": landscape_pages})
        if image_dpi:
            warnings.append({"code": "low_raster_dpi_hint", "items": image_dpi})
        fonts = font_inventory(args.pdf)
        if fonts["status"] != "pass":
            issues.append({"code": "font_embedding_not_confirmed", "details": fonts})
        log_findings = None
        if args.log:
            log_findings = [
                line for line in args.log.read_text(encoding="utf-8", errors="replace").splitlines()
                if re.search(
                    r"^!|Missing character|Overfull|Float too large|Undefined control sequence"
                    r"|undefined references|Reference .+undefined|Citation .+undefined"
                    r"|multiply defined|Rerun to get|Label\(s\) may have changed", line, re.I)
            ]
            if log_findings:
                issues.append({"code": "tex_log_findings", "lines": log_findings})
        else:
            warnings.append({"code": "build_log_not_checked"})
        contacts = render_contacts(document, args.contact_dir) if args.contact_dir else None
        report = {
            "mechanical_checks_passed": not issues, "pages": len(document),
            "bookmark_levels": dict(Counter(item[0] for item in toc)),
            "font_status": fonts, "issues": issues, "warnings": warnings,
            "log_findings": log_findings, "contact_sheets": contacts,
            "sha256": hashlib.sha256(args.pdf.read_bytes()).hexdigest(),
            "not_certified": ["translation fidelity", "content completeness",
                              "semantic reference correctness", "figure identity/crops",
                              "equation/table transcription", "visual review"]
        }
    serialized = json.dumps(report, ensure_ascii=False, indent=2, default=str) + "\n"
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(serialized, encoding="utf-8")
    print(serialized, end="")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
