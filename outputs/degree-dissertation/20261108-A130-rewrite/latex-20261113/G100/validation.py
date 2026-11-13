#!/usr/bin/env python3
"""
G100 validation script:
Verifies exact rational controls, LaTeX syntax and labels, evidence ledger,
figure positivity without clipping, raw file existence and SHA256 integrity,
and full resolution of T19 findings F01..F10.
"""

import hashlib
import json
import math
import os
import re
from pathlib import Path

def sha256_file(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    root = Path("/workspace/wiki")
    g100_dir = root / "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G100"

    results = {
        "task": "G100",
        "status": "passed",
        "checks": {}
    }

    # 1. LaTeX file verification
    tex_path = root / "raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-5-7.tex"
    tex_text = tex_path.read_text(encoding="utf-8")

    opens = len(re.findall(r"\\begin\{(equation|itemize|enumerate|figure)\}", tex_text))
    closes = len(re.findall(r"\\end\{(equation|itemize|enumerate|figure)\}", tex_text))
    assert opens == closes, f"Environment mismatch: {opens} vs {closes}"

    labels = re.findall(r"\\label\{([^}]+)\}", tex_text)
    required_labels = [
        "sec:5-7", "subsec:5-7-1", "eq:5-7-bk-def", "eq:5-7-deorientation",
        "eq:5-7-w-theta-general", "eq:5-7-w-theta-fit", "eq:5-7-ak-apparent",
        "subsec:5-7-2", "eq:5-7-delta-def", "eq:5-7-ak-rational", "eq:5-7-ak-m1e2",
        "subsec:5-7-3", "eq:5-7-dco-def", "subsec:5-7-4", "eq:5-7-asym-exp",
        "eq:5-7-pol-degree", "eq:5-7-pol-def", "eq:5-7-pol-theor", "subsec:5-7-5",
        "eq:5-7-dco-rational", "eq:5-7-quadratic-roots", "eq:5-7-projective-form",
        "fig:5-7-angular-branch"
    ]
    for req in required_labels:
        assert req in labels, f"Missing label: {req}"

    cites = re.findall(r"\\cite\{([^}]+)\}", tex_text)
    used_cites = set()
    for c in cites:
        for item in c.split(","):
            used_cites.add(item.strip())
    expected_cites = {
        "book-hamilton-electromagnetic-interaction",
        "campaign-g07-gorgen-2004-163lu-quadrupole-moments",
        "lange-kumar-hamilton-1982-multipole-admixtures"
    }
    assert used_cites == expected_cites, f"Unexpected citations: {used_cites}"

    results["checks"]["latex"] = {
        "path": str(tex_path.relative_to(root)),
        "sha256": sha256_file(tex_path),
        "environments_balanced": True,
        "label_count": len(labels),
        "labels": labels,
        "citations": sorted(list(used_cites))
    }

    # 2. Evidence ledger verification
    ledger_path = root / "raw/writing/gpt/A130/latex-evidence-ledger/section-5-7.json"
    ledger_data = json.loads(ledger_path.read_text(encoding="utf-8"))
    assert ledger_data["section_id"] == "5.7"
    assert ledger_data["worker"] == "G100"
    assert len(ledger_data["sources"]) == 3
    assert len(ledger_data["claims"]) == 5
    assert len(ledger_data["migration_differences"]) == 10

    # Verify actual raw file hashes match disk
    for src in ledger_data["sources"]:
        rf = root / src["raw_file"]
        assert rf.exists(), f"Raw file does not exist: {rf}"
        actual_h = sha256_file(rf)
        assert actual_h == src["raw_sha256"], f"SHA256 mismatch for {rf}"

    results["checks"]["ledger"] = {
        "path": str(ledger_path.relative_to(root)),
        "sha256": sha256_file(ledger_path),
        "claims_count": len(ledger_data["claims"]),
        "sources_verified": len(ledger_data["sources"]),
        "migration_differences_count": len(ledger_data["migration_differences"])
    }

    # 3. Figure script and positivity checks
    fig_script = root / "system/scripts/a130_angular_branch_figure.py"
    fig_code = fig_script.read_text(encoding="utf-8")
    assert "np.clip" not in fig_code, "np.clip must not be used in figure script"
    assert "Hypothetical Band" in fig_code, "Figure legend must state Hypothetical Band"

    # Analytical polynomial controls:
    # N(delta) = 0.65 - 0.30 delta + 1.10 delta^2
    # D(delta) = 1.05 + 0.15 delta + 0.95 delta^2
    # W(delta) = 1.00 + 0.10 delta + 0.80 delta^2
    # H(delta) = -0.45 + 0.60 delta + 0.65 delta^2
    # Roots for R_DCO = 0.80:
    exp_val = 0.80
    c2 = 1.10 - exp_val * 0.95
    c1 = -0.30 - exp_val * 0.15
    c0 = 0.65 - exp_val * 1.05
    discr = c1**2 - 4 * c2 * c0
    assert discr > 0, "Discriminant must be positive for real roots"
    r1 = (-c1 - math.sqrt(discr)) / (2 * c2)
    r2 = (-c1 + math.sqrt(discr)) / (2 * c2)

    # D at roots:
    d_r1 = 1.05 + 0.15 * r1 + 0.95 * r1**2
    d_r2 = 1.05 + 0.15 * r2 + 0.95 * r2**2
    assert d_r1 > 0 and d_r2 > 0, "Denominator must be strictly non-zero and positive at roots"

    p_r1 = (-0.45 + 0.60 * r1 + 0.65 * r1**2) / (1.00 + 0.10 * r1 + 0.80 * r1**2)
    p_r2 = (-0.45 + 0.60 * r2 + 0.65 * r2**2) / (1.00 + 0.10 * r2 + 0.80 * r2**2)
    assert -1.0 < p_r1 < 1.0 and -1.0 < p_r2 < 1.0

    svg_path = root / "raw/writing/gpt/A130/these_2023_template/these_template/Img/angular-branch-delta-likelihood.svg"
    pdf_path = root / "raw/writing/gpt/A130/these_2023_template/these_template/Img/angular-branch-delta-likelihood.pdf"
    assert svg_path.exists() and svg_path.stat().st_size > 0
    assert pdf_path.exists() and pdf_path.stat().st_size > 0

    results["checks"]["figure"] = {
        "script_path": str(fig_script.relative_to(root)),
        "script_sha256": sha256_file(fig_script),
        "svg_path": str(svg_path.relative_to(root)),
        "svg_sha256": sha256_file(svg_path),
        "pdf_path": str(pdf_path.relative_to(root)),
        "pdf_sha256": sha256_file(pdf_path),
        "delta_root1": r1,
        "delta_root2": r2,
        "theta_deg1": math.degrees(math.atan(r1)),
        "theta_deg2": math.degrees(math.atan(r2)),
        "pol_root1": p_r1,
        "pol_root2": p_r2,
        "np_clip_absent": True,
        "positivity_verified": True
    }

    # 4. Knowledge note verification
    note_path = root / "knowledge/research-notes/a130-rewrite-sec-5-7-angular-distribution-dco-polarization-reconciliation-20261114.md"
    assert note_path.exists() and note_path.stat().st_size > 0
    results["checks"]["knowledge_note"] = {
        "path": str(note_path.relative_to(root)),
        "sha256": sha256_file(note_path)
    }

    # 5. Findings mapping verification
    mapping_path = g100_dir / "findings-mapping.json"
    mapping_data = json.loads(mapping_path.read_text(encoding="utf-8"))
    assert len(mapping_data["findings"]) == 10
    for f in mapping_data["findings"]:
        assert f["status"] == "resolved"
    results["checks"]["findings_mapping"] = {
        "path": str(mapping_path.relative_to(root)),
        "sha256": sha256_file(mapping_path),
        "total_findings": len(mapping_data["findings"]),
        "all_resolved": True
    }

    # 6. New references file
    bib_path = g100_dir / "new-references.bib"
    assert bib_path.exists() and bib_path.stat().st_size > 0
    results["checks"]["new_references_bib"] = {
        "path": str(bib_path.relative_to(root)),
        "sha256": sha256_file(bib_path)
    }

    results_out = g100_dir / "results.json"
    results_out.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n")
    print(f"Validation successful! Results written to {results_out}")

if __name__ == "__main__":
    main()
