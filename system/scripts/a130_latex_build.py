#!/usr/bin/env python3
"""
a130_latex_build.py
Multi-pass XeLaTeX + BibTeX build script for A130 doctoral thesis template.
Stores artifacts in tmp/a130-latex-build/ and copies final reviewable PDF to Thesis.pdf.
Tracks SHA-256 of all production inputs (tex/bib/img/style).
Audits fatal errors, missing citations, undefined references, overfull/underfull boxes, and missing glyphs.
"""

import os
import sys
import re
import shutil
import subprocess
import argparse
import json
import hashlib
import datetime

def parse_args():
    parser = argparse.ArgumentParser(description="Build A130 LaTeX Thesis")
    parser.add_argument("--workdir", default="raw/writing/gpt/A130/these_2023_template/these_template",
                        help="Root directory containing Thesis.tex")
    parser.add_argument("--build-dir", default="tmp/a130-latex-build",
                        help="Directory for compilation artifacts")
    parser.add_argument("--tex", default="Thesis.tex",
                        help="Main TeX file name")
    parser.add_argument("--passes", type=int, default=4,
                        help="Number of compilation passes (1: xelatex, 2: bibtex, 3: xelatex, 4: xelatex)")
    parser.add_argument("--report-json", default="outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G76/build_report.json",
                        help="Path to save structured JSON build report")
    return parser.parse_args()

def hash_file(fpath):
    h = hashlib.sha256()
    with open(fpath, 'rb') as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def scan_production_inputs(workdir):
    workdir = str(workdir)
    input_hashes = {}
    scan_exts = ('.tex', '.bib', '.bst', '.bbx', '.cbx', '.sty', '.cls', '.cfg', '.pdf', '.png', '.jpg', '.eps')
    for root, dirs, files in os.walk(workdir):
        # Skip temporary build or inactive folders
        if '_demo_inactive' in root or '.git' in root or 'tmp' in root:
            continue
        for fname in sorted(files):
            if fname.lower().endswith(scan_exts):
                # Don't hash generated Thesis.pdf as input
                if fname == 'Thesis.pdf' and root == workdir:
                    continue
                fpath = os.path.join(root, fname)
                rel_path = os.path.relpath(fpath, workdir)
                input_hashes[rel_path] = {
                    "size_bytes": os.path.getsize(fpath),
                    "sha256": hash_file(fpath)
                }

    # Combined hash of inputs
    manifest_bytes = json.dumps(input_hashes, sort_keys=True).encode('utf-8')
    overall_sha = hashlib.sha256(manifest_bytes).hexdigest()
    return input_hashes, overall_sha

def analyze_log(log_path):
    issues = {
        "fatal_errors": [],
        "missing_citations": [],
        "missing_references": [],
        "overfull_hboxes": [],
        "overfull_vboxes": [],
        "underfull_hboxes": [],
        "underfull_vboxes": [],
        "missing_glyphs": [],
        "overfull_by_file": {}
    }

    if not os.path.exists(log_path):
        return issues

    with open(log_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
        lines = content.splitlines()

    file_stack = []

    for i, line in enumerate(lines):
        # Track active tex file
        openings = re.findall(r'\(([^()\s]+\.tex)', line)
        for op in openings:
            file_stack.append(op)

        if line.startswith("! "):
            context = [line]
            for offset in range(1, 4):
                if i + offset < len(lines):
                    context.append(lines[i + offset])
            issues["fatal_errors"].append("\n".join(context))
        elif "LaTeX Warning: Citation" in line and "undefined" in line:
            m = re.search(r"Citation [`']([^']+)['`] on page (\d+)", line)
            if m:
                issues["missing_citations"].append({"key": m.group(1), "page": int(m.group(2))})
            else:
                issues["missing_citations"].append({"raw": line.strip()})
        elif "LaTeX Warning: Reference" in line and "undefined" in line:
            m = re.search(r"Reference [`']([^']+)['`] on page (\d+)", line)
            if m:
                issues["missing_references"].append({"ref": m.group(1), "page": int(m.group(2))})
            else:
                issues["missing_references"].append({"raw": line.strip()})
        elif line.startswith("Overfull \\hbox"):
            curr_file = os.path.basename(file_stack[-1]) if file_stack else "unknown"
            item = {"file": curr_file, "message": line.strip()}
            issues["overfull_hboxes"].append(item)
            issues["overfull_by_file"].setdefault(curr_file, []).append(line.strip())
        elif line.startswith("Overfull \\vbox"):
            issues["overfull_vboxes"].append(line.strip())
        elif line.startswith("Underfull \\hbox"):
            issues["underfull_hboxes"].append(line.strip())
        elif line.startswith("Underfull \\vbox"):
            issues["underfull_vboxes"].append(line.strip())
        elif "Missing character: There is no" in line:
            curr_file = os.path.basename(file_stack[-1]) if file_stack else "unknown"
            issues["missing_glyphs"].append({"file": curr_file, "message": line.strip()})

    return issues

def analyze_blg(blg_path):
    blg_info = {
        "errors": [],
        "warnings": []
    }
    if not os.path.exists(blg_path):
        return blg_info
    with open(blg_path, 'r', encoding='utf-8', errors='replace') as f:
        for line in f:
            line_str = line.strip()
            if line_str.startswith("Warning--"):
                blg_info["warnings"].append(line_str)
            elif line_str.startswith("Error") or "error" in line_str.lower():
                blg_info["errors"].append(line_str)
    return blg_info

def get_pdf_info(pdf_path):
    if not os.path.exists(pdf_path):
        return None
    size = os.path.getsize(pdf_path)
    pages = None
    try:
        p = subprocess.run(["pdfinfo", pdf_path], capture_output=True, text=True)
        if p.returncode == 0:
            for line in p.stdout.splitlines():
                if line.startswith("Pages:"):
                    pages = int(line.split()[1])
    except Exception:
        pass
    return {"path": pdf_path, "size_bytes": size, "page_count": pages}

def main():
    args = parse_args()
    workdir = os.path.abspath(str(args.workdir))
    build_dir = os.path.abspath(str(args.build_dir))
    os.makedirs(build_dir, exist_ok=True)

    jobname = os.path.splitext(args.tex)[0]

    start_time = datetime.datetime.now(datetime.timezone.utc)
    print(f"=== Starting A130 LaTeX Build at {start_time.isoformat()} ===")
    print(f"Workdir:   {workdir}")
    print(f"BuildDir:  {build_dir}")
    print(f"Main TeX:  {args.tex}")

    # 1. Scan production inputs before build
    input_hashes_pre, input_overall_sha = scan_production_inputs(workdir)
    print(f"Production inputs tracked: {len(input_hashes_pre)} files (manifest SHA: {input_overall_sha[:12]})")

    pass_results = []

    # Pass 1: xelatex
    cmd1 = ["xelatex", f"-output-directory={build_dir}", "-interaction=nonstopmode", args.tex]
    print(f"\n--- Pass 1: {' '.join(cmd1)} ---")
    p1 = subprocess.run(cmd1, cwd=workdir, capture_output=True, text=True)
    pass_results.append({"pass": 1, "cmd": cmd1, "returncode": p1.returncode})
    print(f"Pass 1 finished with code {p1.returncode}")

    # Pass 2: bibtex (must run in build_dir so openout_any=p allows writing .bbl and .blg)
    env = os.environ.copy()
    env['BSTINPUTS'] = f".:{workdir}:{workdir}/Style:{workdir}/Biblio:{env.get('BSTINPUTS', '')}:"
    env['BIBINPUTS'] = f".:{workdir}:{workdir}/Biblio:{env.get('BIBINPUTS', '')}:"
    cmd2 = ["bibtex", jobname]
    print(f"\n--- Pass 2: {' '.join(cmd2)} in {build_dir} ---")
    p2 = subprocess.run(cmd2, cwd=build_dir, env=env, capture_output=True, text=True)
    pass_results.append({"pass": 2, "cmd": cmd2, "returncode": p2.returncode})
    print(f"Pass 2 finished with code {p2.returncode}")
    if p2.stdout:
        print("BibTeX output tail:\n" + "\n".join(p2.stdout.splitlines()[-10:]))

    # Pass 3: xelatex
    cmd3 = ["xelatex", f"-output-directory={build_dir}", "-interaction=nonstopmode", args.tex]
    print(f"\n--- Pass 3: {' '.join(cmd3)} ---")
    p3 = subprocess.run(cmd3, cwd=workdir, capture_output=True, text=True)
    pass_results.append({"pass": 3, "cmd": cmd3, "returncode": p3.returncode})
    print(f"Pass 3 finished with code {p3.returncode}")

    # Pass 4: xelatex
    cmd4 = ["xelatex", f"-output-directory={build_dir}", "-interaction=nonstopmode", args.tex]
    print(f"\n--- Pass 4: {' '.join(cmd4)} ---")
    p4 = subprocess.run(cmd4, cwd=workdir, capture_output=True, text=True)
    pass_results.append({"pass": 4, "cmd": cmd4, "returncode": p4.returncode})
    print(f"Pass 4 finished with code {p4.returncode}")

    # Analyze outputs
    log_path = os.path.join(build_dir, f"{jobname}.log")
    blg_path = os.path.join(build_dir, f"{jobname}.blg")
    pdf_in_build = os.path.join(build_dir, f"{jobname}.pdf")
    pdf_in_workdir = os.path.join(workdir, f"{jobname}.pdf")

    log_analysis = analyze_log(log_path)
    blg_analysis = analyze_blg(blg_path)

    pdf_info = None
    if os.path.exists(pdf_in_build):
        shutil.copy2(pdf_in_build, pdf_in_workdir)
        pdf_info = get_pdf_info(pdf_in_workdir)
        print(f"\nSUCCESS: Generated PDF copied to {pdf_in_workdir}")
        print(f"Size: {pdf_info['size_bytes']} bytes, Pages: {pdf_info['page_count']}")
    else:
        print(f"\nFAILURE: PDF was not generated at {pdf_in_build}", file=sys.stderr)

    end_time = datetime.datetime.now(datetime.timezone.utc)

    # Determine audit status
    fatal_cnt = len(log_analysis["fatal_errors"])
    missing_cite_cnt = len(log_analysis["missing_citations"])
    missing_ref_cnt = len(log_analysis["missing_references"])
    overfull_cnt = len(log_analysis["overfull_hboxes"])
    missing_glyph_cnt = len(log_analysis["missing_glyphs"])

    if fatal_cnt > 0 or not pdf_info:
        audit_verdict = "FATAL_FAILURE"
    elif missing_cite_cnt > 0 or missing_ref_cnt > 0:
        audit_verdict = "INCOMPLETE_REFERENCES"
    elif overfull_cnt > 0 or missing_glyph_cnt > 0:
        audit_verdict = "COMPILED_WITH_LAYOUT_ISSUES"
    else:
        audit_verdict = "CLEAN_PASS"

    report = {
        "build_started_at_utc": start_time.isoformat(),
        "build_finished_at_utc": end_time.isoformat(),
        "workdir": workdir,
        "build_dir": build_dir,
        "jobname": jobname,
        "production_inputs": {
            "total_files": len(input_hashes_pre),
            "manifest_sha256": input_overall_sha,
            "files": input_hashes_pre
        },
        "passes": pass_results,
        "pdf_info": pdf_info,
        "log_path": log_path,
        "blg_path": blg_path,
        "audit_verdict": audit_verdict,
        "fatal_errors_count": fatal_cnt,
        "fatal_errors": log_analysis["fatal_errors"][:10],
        "missing_citations_count": missing_cite_cnt,
        "missing_citations": log_analysis["missing_citations"],
        "missing_references_count": missing_ref_cnt,
        "missing_references": log_analysis["missing_references"],
        "overfull_hboxes_count": overfull_cnt,
        "overfull_hboxes": log_analysis["overfull_hboxes"],
        "overfull_by_file": log_analysis["overfull_by_file"],
        "overfull_vboxes_count": len(log_analysis["overfull_vboxes"]),
        "underfull_hboxes_count": len(log_analysis["underfull_hboxes"]),
        "missing_glyphs_count": missing_glyph_cnt,
        "missing_glyphs": log_analysis["missing_glyphs"],
        "bibtex_warnings_count": len(blg_analysis["warnings"]),
        "bibtex_warnings": blg_analysis["warnings"],
        "bibtex_errors_count": len(blg_analysis["errors"]),
        "bibtex_errors": blg_analysis["errors"]
    }

    os.makedirs(os.path.dirname(os.path.abspath(args.report_json)), exist_ok=True)
    with open(args.report_json, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"\nReport saved to: {args.report_json}")
    print(f"Audit Verdict:        {audit_verdict}")
    print(f"  Fatal Errors:       {fatal_cnt}")
    print(f"  Missing Citations:  {missing_cite_cnt}")
    print(f"  Missing References: {missing_ref_cnt}")
    print(f"  Overfull \\hbox:     {overfull_cnt}")
    print(f"  Missing Glyphs:     {missing_glyph_cnt}")
    print(f"  BibTeX Errors:      {len(blg_analysis['errors'])}")
    print(f"  BibTeX Warnings:    {len(blg_analysis['warnings'])}")

    return 0 if (pdf_info and fatal_cnt == 0) else 1

if __name__ == "__main__":
    sys.exit(main())
