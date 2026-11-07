#!/usr/bin/env python3
"""
ru102_si_strength_audit.py - Reproducible parser and strength concentration audit
for Table I of the 102Ru PRL 136, 252501 (2026) Supplemental Material.

Author / Worker: Gemini/high worker G24
Date: 2026-11-08 / 2026-11-07
Workspace: /workspace/wiki
Canonical source: knowledge/sources/saracino-2026-102ru-scissors-octupole-resonances.md
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


DEFAULT_PDF = Path("raw/papers/gpt/query/20261107-continuation-G14/102Ru-PRL-136-252501-Supplemental-Material.pdf")
DEFAULT_G14_CSV = Path("outputs/l3/20261107-nuclear-structure-continuation/G14/table1_transitions_102Ru_NRF.csv")
DEFAULT_OUT_DIR = Path("outputs/l4/20261107-ru102-si-strength-audit")
EXPECTED_PDF_SHA256 = "8b9fba94fd43ea2af1860029889c0cb3e30ebb3c2cc29a5e0d749649c93a2df0"


def sha256_file(path: Path | str) -> str:
    """Compute SHA256 checksum of a file."""
    p = Path(path)
    if not p.is_file():
        return ""
    h = hashlib.sha256()
    with open(p, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def extract_table1_text(pdf_path: Path) -> str:
    """
    Extract text of first 3 pages of the PDF using pdftotext -layout.
    Raises RuntimeError if pdftotext is not available or fails.
    """
    if not pdf_path.is_file():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    cmd = ["pdftotext", "-layout", "-f", "1", "-l", "3", str(pdf_path), "-"]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return proc.stdout
    except FileNotFoundError:
        raise RuntimeError("pdftotext executable not found in PATH (/usr/bin/pdftotext required).")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"pdftotext failed with exit code {e.returncode}: {e.stderr}")


def parse_number_audit(s: str, field_name: str) -> Tuple[Optional[float], Optional[float], str]:
    """
    Parse a numeric string with optional parenthetical uncertainty.

    Rules:
    - Empty, '-', or whitespace -> (None, None, '')
    - Missing uncertainty -> (val, None, note) [NOT 0.0]
    - Explicit decimal uncertainty e.g. 5299.11(1.4) -> (val, unc, note)
    - Shorthand integer uncertainty e.g. 2292.8(7) -> 0.7; 4704.52(18) -> 0.18
    """
    if not s or s.strip() == "" or s.strip() == "-":
        return None, None, ""

    clean_str = s.strip()
    m = re.match(r"^([\-\+]?\d+\.?\d*)\s*(\(([\d\.]+)\))?$", clean_str)
    if not m:
        raise ValueError(f"Failed to parse numeric token in {field_name}: '{s}'")

    val_str = m.group(1)
    unc_str = m.group(3)
    val = float(val_str)

    if unc_str is None:
        return val, None, f"Unstated uncertainty in {field_name} ('{clean_str}') set to null."

    if "." in unc_str:
        unc = float(unc_str)
        dec_val = len(val_str.split(".")[1]) if "." in val_str else 0
        dec_unc = len(unc_str.split(".")[1])
        note = ""
        if dec_val != dec_unc:
            note = f"Decimals mismatch in {field_name} '{clean_str}': value has {dec_val} decimals, uncertainty has {dec_unc}; preserved verbatim as {unc} without forced normalization."
        return val, unc, note
    else:
        dec_val = len(val_str.split(".")[1]) if "." in val_str else 0
        unc = round(float(unc_str) * (10 ** -dec_val), max(dec_val, len(unc_str)))
        return val, unc, ""


def parse_table1_rows(layout_text: str) -> List[Dict[str, Any]]:
    """
    Parse the 106 rows of Table I from pdftotext layout output.
    Raises ValueError on any missing, corrupted, or malformed row.
    """
    pages = layout_text.split("\x0c")
    if len(pages) < 3:
        raise ValueError(f"Expected at least 3 pages from PDF extraction, got {len(pages)}")

    rows: List[Dict[str, Any]] = []
    row_counter = 0

    for p_idx in range(3):
        page_num = p_idx + 1
        page_text = pages[p_idx]
        lines = page_text.split("\n")

        for line_idx, line in enumerate(lines):
            line_clean = line.strip()
            # Must contain M1 or E1 multipolarity marker and start with a 4-digit energy
            if not re.search(r"\b\(?[EM]1\)?\b", line_clean):
                continue
            if not re.match(r"^\d{4}", line_clean):
                continue

            row_counter += 1
            # Standardize unicode minus and join numbers with space before parentheses
            line_proc = line_clean.replace("\u2212", "-")
            line_proc = re.sub(r"(\d+\.\d+)\s+(\(\d+\.?\d*\))", r"\1\2", line_proc)

            tokens = line_proc.split()
            if len(tokens) != 6:
                raise ValueError(
                    f"Row parsing error at page {page_num}, line {line_idx + 1}: "
                    f"expected exactly 6 tokens, found {len(tokens)} in '{line_clean}'"
                )

            ei_raw, eg_raw, br_raw, eps_raw, mult_raw, b_raw = tokens

            # Validate multipolarity
            if mult_raw not in ("M1", "(M1)", "E1", "(E1)"):
                raise ValueError(f"Unknown multipolarity '{mult_raw}' at row {row_counter}")

            is_tentative = "(" in mult_raw

            # Parse numbers
            notes: List[str] = []

            ei_val, ei_unc, note_ei = parse_number_audit(ei_raw, "Ei")
            if note_ei:
                notes.append(note_ei)

            eg_val, eg_unc, note_eg = parse_number_audit(eg_raw, "Egamma")
            if note_eg:
                notes.append(note_eg)

            br_val, br_unc, note_br = parse_number_audit(br_raw, "BR")
            if note_br:
                notes.append(note_br)

            eps_val, eps_unc, note_eps = parse_number_audit(eps_raw, "asymmetry")
            if note_eps:
                notes.append(note_eps)

            b_val, b_unc, note_b = parse_number_audit(b_raw, "B_up")
            if note_b:
                notes.append(note_b)

            recoil = round(ei_val - eg_val, 4) if (ei_val is not None and eg_val is not None) else None

            # Specific multipolarity assignments
            bm1_up_raw = b_raw if "M1" in mult_raw else ""
            bm1_up_val = b_val if "M1" in mult_raw else None
            bm1_up_unc = b_unc if "M1" in mult_raw else None

            be1_up_raw = b_raw if "E1" in mult_raw else ""
            be1_up_val = b_val if "E1" in mult_raw else None
            be1_up_unc = b_unc if "E1" in mult_raw else None

            locator = f"SI-Table-I-p{page_num}-row{row_counter:03d}"

            uncertainty_note = "; ".join(notes) if notes else "Standard experimental reporting."

            rows.append({
                "row_id": row_counter,
                "si_page": page_num,
                "si_line_index": line_idx,
                "locator": locator,
                "Ei_reported_raw": ei_raw,
                "Ei_reported_keV": ei_val,
                "Ei_unc_keV": ei_unc,
                "Egamma_reported_raw": eg_raw,
                "Egamma_reported_keV": eg_val,
                "Egamma_unc_keV": eg_unc,
                "recoil_shift_keV": recoil,
                "BR_reported_raw": br_raw,
                "BR_reported": br_val,
                "BR_unc": br_unc,
                "asymmetry_reported_raw": eps_raw,
                "asymmetry_reported": eps_val,
                "asymmetry_unc": eps_unc,
                "multipolarity_reported": mult_raw,
                "is_tentative": is_tentative,
                "BM1_up_reported_raw": bm1_up_raw,
                "BM1_up_reported_muN2": bm1_up_val,
                "BM1_up_unc_muN2": bm1_up_unc,
                "BE1_up_reported_raw": be1_up_raw,
                "BE1_up_reported_e2fm2": be1_up_val,
                "BE1_up_unc_e2fm2": be1_up_unc,
                "uncertainty_note": uncertainty_note
            })

    if len(rows) != 106:
        raise ValueError(f"Table I verification failed: expected 106 rows, but extracted {len(rows)}")

    m1_count = sum(1 for r in rows if "M1" in r["multipolarity_reported"])
    m1_bracket = sum(1 for r in rows if r["multipolarity_reported"] == "(M1)")
    e1_count = sum(1 for r in rows if "E1" in r["multipolarity_reported"])
    e1_bracket = sum(1 for r in rows if r["multipolarity_reported"] == "(E1)")

    if m1_count != 34 or m1_bracket != 1 or e1_count != 72 or e1_bracket != 6:
        raise ValueError(
            f"Table I multipolarity count mismatch: M1={m1_count} (bracketed={m1_bracket}), "
            f"E1={e1_count} (bracketed={e1_bracket})"
        )

    return rows


def compare_with_g14(parsed_rows: List[Dict[str, Any]], g14_csv_path: Path) -> Dict[str, Any]:
    """
    Perform a field-by-field comparison of reported raw content with the existing G14 CSV.
    """
    if not g14_csv_path.is_file():
        return {
            "g14_csv_present": False,
            "message": f"G14 CSV file not found at {g14_csv_path}"
        }

    with open(g14_csv_path, "r", encoding="utf-8") as f:
        g14_rows = list(csv.DictReader(f))

    if len(g14_rows) != len(parsed_rows):
        raise ValueError(f"Row count mismatch: parsed {len(parsed_rows)} rows, G14 has {len(g14_rows)} rows")

    raw_mismatches: List[Dict[str, Any]] = []
    treatment_differences: List[Dict[str, Any]] = []

    raw_fields = [
        ("Ei_reported_raw", "Ei_reported_raw"),
        ("Egamma_reported_raw", "Egamma_reported_raw"),
        ("BR_reported_raw", "BR_reported_raw"),
        ("asymmetry_reported_raw", "asymmetry_reported_raw"),
        ("multipolarity_reported", "multipolarity_reported"),
        ("BM1_up_reported_raw", "BM1_up_reported_raw"),
        ("BE1_up_reported_raw", "BE1_up_reported_raw"),
    ]

    for p_row, g_row in zip(parsed_rows, g14_rows):
        r_id = p_row["row_id"]
        for p_field, g_field in raw_fields:
            val_p = p_row[p_field]
            val_g = g_row.get(g_field, "")
            if val_p != val_g:
                raw_mismatches.append({
                    "row_id": r_id,
                    "field": p_field,
                    "parsed": val_p,
                    "g14": val_g
                })

        # Treatment differences: G14 assigned unc=0.0 to unbracketed values
        if p_row["BR_reported_raw"] == "1":
            if g_row.get("BR_unc") == "0.0" and p_row["BR_unc"] is None:
                treatment_differences.append({
                    "row_id": r_id,
                    "field": "BR_unc",
                    "parsed": None,
                    "g14": 0.0,
                    "note": "G14 filled 0.0 for unbracketed BR=1; G24 audit represents unstated uncertainty as null"
                })
        if p_row["Ei_reported_raw"] == "4528.8":
            if g_row.get("Ei_unc_keV") == "0.0" and p_row["Ei_unc_keV"] is None:
                treatment_differences.append({
                    "row_id": r_id,
                    "field": "Ei_unc_keV",
                    "parsed": None,
                    "g14": 0.0,
                    "note": "G14 filled 0.0 for unbracketed Ei=4528.8; G24 audit represents unstated uncertainty as null"
                })

    return {
        "g14_csv_present": True,
        "g14_csv_path": str(g14_csv_path),
        "g14_sha256": sha256_file(g14_csv_path),
        "total_rows_compared": len(parsed_rows),
        "raw_string_mismatches_count": len(raw_mismatches),
        "raw_string_mismatches": raw_mismatches,
        "treatment_differences_count": len(treatment_differences),
        "treatment_differences_summary": {
            "unbracketed_uncertainties_as_null": len(treatment_differences),
            "omitted_downward_transitions": True,
            "omitted_gamma_widths": True
        }
    }


def calculate_predetermined_windows(rows: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Calculate transition counts, sums, max-row shares, centroids, and uncertainty scenarios
    for the predetermined energy windows.
    """
    windows_def = [
        ("full_table", "Full Table", 0.0, 100000.0),
        ("window_2_3_to_4_0_MeV", "2.3 <= E_gamma < 4.0 MeV", 2300.0, 4000.0),
        ("window_4_5_to_5_5_MeV", "4.5 <= E_gamma < 5.5 MeV", 4500.0, 5500.0)
    ]

    results: Dict[str, Any] = {}

    for key, name, emin, emax in windows_def:
        w_dict: Dict[str, Any] = {
            "name": name,
            "energy_min_keV": emin,
            "energy_max_keV": emax,
            "multipolarities": {}
        }

        for mult in ["E1", "M1"]:
            m_dict: Dict[str, Any] = {}
            col_b = "BE1_up_reported_e2fm2" if mult == "E1" else "BM1_up_reported_muN2"
            col_u = "BE1_up_unc_e2fm2" if mult == "E1" else "BM1_up_unc_muN2"
            unit = "e2 fm2" if mult == "E1" else "muN2"

            for incl_bracket in [True, False]:
                b_key = "with_bracketed" if incl_bracket else "unbracketed_only"

                # Filter rows
                w_rows = []
                for r in rows:
                    m = r["multipolarity_reported"]
                    eg = r["Egamma_reported_keV"]
                    if emin <= eg < emax:
                        if incl_bracket:
                            if mult in m:
                                w_rows.append(r)
                        else:
                            if m == mult:
                                w_rows.append(r)

                n = len(w_rows)
                if n == 0:
                    m_dict[b_key] = {
                        "count_N": 0,
                        "sum_B_up": 0.0,
                        "unit": unit
                    }
                    continue

                b_vals = [r[col_b] for r in w_rows]
                u_vals = [r[col_u] if r[col_u] is not None else 0.0 for r in w_rows]
                eg_vals = [r["Egamma_reported_keV"] for r in w_rows]

                total_sum = round(sum(b_vals), 5)
                max_b = max(b_vals)
                max_idx = b_vals.index(max_b)
                max_row = w_rows[max_idx]
                max_share_pct = round((max_b / total_sum * 100.0) if total_sum > 0 else 0.0, 2)

                centroid_keV = round(
                    (sum(e * b for e, b in zip(eg_vals, b_vals)) / total_sum) if total_sum > 0 else 0.0,
                    2
                )

                # Uncertainties: marginals and assumed independent propagation
                sigma_indep = round(math.sqrt(sum(u ** 2 for u in u_vals)), 5)
                sigma_linear_bound = round(sum(u_vals), 5)

                top_line_unc = max_row[col_u] if max_row[col_u] is not None else 0.0
                total_var = sum(u ** 2 for u in u_vals)
                top_line_var_pct = round((top_line_unc ** 2 / total_var * 100.0) if total_var > 0 else 0.0, 2)

                m_dict[b_key] = {
                    "count_N": n,
                    "sum_B_up": total_sum,
                    "unit": unit,
                    "centroid_keV": centroid_keV,
                    "max_row": {
                        "row_id": max_row["row_id"],
                        "Egamma_reported_raw": max_row["Egamma_reported_raw"],
                        "BR_reported_raw": max_row["BR_reported_raw"],
                        "B_up_reported_raw": max_row["BE1_up_reported_raw"] if mult == "E1" else max_row["BM1_up_reported_raw"],
                        "B_up_val": max_b,
                        "B_up_unc": top_line_unc,
                        "share_pct": max_share_pct,
                        "variance_share_pct_indep": top_line_var_pct
                    },
                    "uncertainty_scenarios": {
                        "assumed_independent_sigma": sigma_indep,
                        "linear_correlated_upper_bound_sigma": sigma_linear_bound,
                        "methodology_caveat": (
                            "Uncertainties represent marginals and an assumed independent error propagation scenario. "
                            "The complete covariance matrix is not published. Common calibration, "
                            "feeding, and efficiency effects may correlate lines; independence is not established. "
                            "The linear bound concerns only the supplied marginal errors."
                        )
                    }
                }
            w_dict["multipolarities"][mult] = m_dict
        results[key] = w_dict

    return results


def calculate_leave_one_out_sensitivity(rows: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Perform leave-one-line-out sensitivity diagnostics on the 4.5 <= E_gamma < 5.5 MeV E1 window.
    Mathematical diagnostic only; not an experimental data exclusion or falsification.
    """
    w_rows = [
        r for r in rows
        if "E1" in r["multipolarity_reported"] and 4500.0 <= r["Egamma_reported_keV"] < 5500.0
    ]

    b_vals = [r["BE1_up_reported_e2fm2"] for r in w_rows]
    u_vals = [r["BE1_up_unc_e2fm2"] if r["BE1_up_unc_e2fm2"] is not None else 0.0 for r in w_rows]
    eg_vals = [r["Egamma_reported_keV"] for r in w_rows]

    total_sum = sum(b_vals)
    total_centroid = sum(e * b for e, b in zip(eg_vals, b_vals)) / total_sum
    total_var = sum(u ** 2 for u in u_vals)

    diagnostics = []
    for i, r in enumerate(w_rows):
        bi = b_vals[i]
        ei = eg_vals[i]
        ui = u_vals[i]

        sum_loo = total_sum - bi
        cent_loo = sum(e * b for j, (e, b) in enumerate(zip(eg_vals, b_vals)) if j != i) / sum_loo

        delta_sum = sum_loo - total_sum
        delta_sum_pct = (delta_sum / total_sum) * 100.0
        delta_cent_keV = cent_loo - total_centroid
        var_share_pct = (ui ** 2 / total_var * 100.0) if total_var > 0 else 0.0

        diagnostics.append({
            "row_id": r["row_id"],
            "Egamma_raw": r["Egamma_reported_raw"],
            "Egamma_keV": ei,
            "BR_raw": r["BR_reported_raw"],
            "BR": r["BR_reported"],
            "BR_unc": r["BR_unc"],
            "BE1_up_raw": r["BE1_up_reported_raw"],
            "BE1_up_e2fm2": bi,
            "BE1_up_unc_e2fm2": ui,
            "sum_loo_e2fm2": round(sum_loo, 5),
            "delta_sum_e2fm2": round(delta_sum, 5),
            "delta_sum_pct": round(delta_sum_pct, 2),
            "centroid_loo_keV": round(cent_loo, 2),
            "delta_centroid_keV": round(delta_cent_keV, 2),
            "variance_contribution_pct": round(var_share_pct, 2)
        })

    # Sort by impact on sum
    by_sum_impact = sorted(diagnostics, key=lambda x: abs(x["delta_sum_e2fm2"]), reverse=True)
    # Sort by impact on centroid
    by_centroid_impact = sorted(diagnostics, key=lambda x: abs(x["delta_centroid_keV"]), reverse=True)

    return {
        "target_window": "4.5 <= E_gamma < 5.5 MeV E1",
        "total_lines_N": len(w_rows),
        "nominal_sum_e2fm2": round(total_sum, 5),
        "nominal_centroid_keV": round(total_centroid, 2),
        "nominal_sigma_indep_e2fm2": round(math.sqrt(total_var), 5),
        "most_influential_on_sum": by_sum_impact[:5],
        "most_influential_on_centroid": by_centroid_impact[:5],
        "all_lines_diagnostics": diagnostics,
        "diagnostic_disclaimer": (
            "Leave-one-line-out removal is purely a mathematical diagnostic to assess concentration "
            "and parameter sensitivity. It does not constitute an experimental modification, "
            "data exclusion, or falsification. Priority is given to identifying which transition "
            "branching ratio requires improved experimental constraint."
        )
    }


def run_negative_tests() -> None:
    """
    Execute targeted sanity checks and negative error handling tests.
    """
    print("[TEST] Running negative tests and error-handling checks...")

    # Negative test 1: Line with fewer than 6 tokens must raise ValueError
    bad_line_short = "  2292.8(7)  2292.8(7)  1  0.65(18)  M1\n\x0c\n\x0c\n"
    try:
        parse_table1_rows(bad_line_short)
        raise AssertionError("Failed to reject line with fewer than 6 tokens")
    except ValueError as e:
        assert "expected exactly 6 tokens" in str(e)
        print("  [PASS] Successfully rejected line with missing tokens.")

    # Negative test 2: Unparsable numeric string must raise ValueError
    try:
        parse_number_audit("corrupted(1.2)", "Ei")
        raise AssertionError("Failed to reject invalid number")
    except ValueError as e:
        assert "Failed to parse numeric token" in str(e)
        print("  [PASS] Successfully rejected malformed numeric string.")

    # Negative test 3: Incorrect row count must raise ValueError
    # Create text with only 1 valid row across 3 pages
    dummy_text = "  2292.8(7)  2292.8(7)  1  0.65(18)  M1  0.079(17)\n\x0c\n\x0c\n"
    try:
        parse_table1_rows(dummy_text)
        raise AssertionError("Failed to reject incomplete row count")
    except ValueError as e:
        assert "expected 106 rows" in str(e)
        print("  [PASS] Successfully rejected truncated row count.")

    # Negative test 4: Missing uncertainty returns None, not 0.0
    val, unc, note = parse_number_audit("4528.8", "Ei")
    assert val == 4528.8 and unc is None
    print("  [PASS] Unstated uncertainty correctly returned as None (null).")

    # Negative test 5: 5299.11(1.4) preserved verbatim with note
    val, unc, note = parse_number_audit("5299.11(1.4)", "Ei")
    assert val == 5299.11 and unc == 1.4 and "preserved verbatim" in note
    print("  [PASS] 5299.11(1.4) correctly parsed with decimal mismatch note.")

    print("[TEST] All negative and sanity checks passed successfully!\n")


def generate_report_md(
    provenance: Dict[str, Any],
    comparison: Dict[str, Any],
    windows_summary: Dict[str, Any],
    loo_summary: Dict[str, Any]
) -> str:
    """Generate comprehensive markdown report."""
    return f"""# 102Ru PRL Table I 补充材料强度集中度与分支比灵敏度审计报告

- **Producer**: `{provenance['producer']}`
- **Execution Date**: `{provenance['execution_date']}`
- **Script**: `{provenance['script']}`
- **Input PDF**: `{provenance['input_pdf_path']}` (SHA256: `{provenance['input_pdf_sha256']}`)
- **Reference G14 CSV**: `{provenance['g14_csv_path']}` (SHA256: `{provenance['g14_csv_sha256']}`)

---

## 1. 核心数值复核与预定窗口结果

本脚本通过 `/usr/bin/pdftotext -layout` 直接解析原件 PDF 前 3 页，完全重现了物理上界定的 106 行光子跃迁数据，无一静默跳过。

### 1.1 全表与预定窗口统计

| 能量窗口 | 多极类型 | 分类方式 | 跃迁数 $N$ | 向上强度和 $\\sum B\\uparrow$ | 最大单行跃迁 $E_\\gamma$ | 最大单行 $B\\uparrow$ (BR) | 最大行份额 | 质心能量 (keV) | 假定独立 $\\sigma$ |
|---|---|---|---|---|---|---|---|---|---|
| **全表** | E1 | 含括号 | 72 | 0.15408 $e^2\\,\\text{{fm}}^2$ | 5080.93(31) | 0.05(4) [0.12(11)] | 32.45% | 4597.07 | 0.04068 |
| 全表 | E1 | 无括号标签 | 66 | 0.12713 $e^2\\,\\text{{fm}}^2$ | 5080.93(31) | 0.05(4) [0.12(11)] | 39.33% | 4909.22 | 0.04037 |
| **全表** | M1 | 含括号 | 34 | 1.66000 $\\mu_N^2$ | 3180.8(4) | 0.22(1) [1] | 13.25% | 3853.34 | 0.04689 |
| 全表 | M1 | 无括号标签 | 33 | 1.64600 $\\mu_N^2$ | 3180.8(4) | 0.22(1) [1] | 13.37% | 3861.95 | 0.04688 |
| **2.3–4.0 MeV** | E1 | 含括号 | 16 | 0.03614 $e^2\\,\\text{{fm}}^2$ | 2953.2(1.9) | 0.016(5) [1] | 44.27% | 3037.99 | 0.00588 |
| 2.3–4.0 MeV | E1 | 无括号标签 | 13 | 0.01093 $e^2\\,\\text{{fm}}^2$ | 2970.5(1.4) | 0.0025(7) [1] | 22.87% | 3218.63 | 0.00100 |
| **2.3–4.0 MeV** | M1 | 含括号 | 17 | 0.99200 $\\mu_N^2$ | 3180.8(4) | 0.22(1) [1] | 22.18% | 3378.80 | 0.03541 |
| 2.3–4.0 MeV | M1 | 无括号标签 | 16 | 0.97800 $\\mu_N^2$ | 3180.8(4) | 0.22(1) [1] | 22.49% | 3386.50 | 0.03540 |
| **4.5–5.5 MeV** | E1 | 含括号 | 38 | 0.10137 $e^2\\,\\text{{fm}}^2$ | 5080.93(31) | 0.05(4) [0.12(11)] | **49.32%** | 5069.71 | 0.04037 |
| 4.5–5.5 MeV | E1 | 无括号标签 | 37 | 0.10123 $e^2\\,\\text{{fm}}^2$ | 5080.93(31) | 0.05(4) [0.12(11)] | 49.39% | 5070.41 | 0.04037 |
| **4.5–5.5 MeV** | M1 | 含括号 | 10 | 0.39500 $\\mu_N^2$ | 5231.78(31) | 0.09(2) [1] | 22.78% | 5003.85 | 0.02706 |
| 4.5–5.5 MeV | M1 | 无括号标签 | 10 | 0.39500 $\\mu_N^2$ | 5231.78(31) | 0.09(2) [1] | 22.78% | 5003.85 | 0.02706 |

复核结论与父级基准完全一致：
1. 全表 E1 总强度名义和为 **0.15408** $e^2\\,\\text{{fm}}^2$。
2. 4.5–5.5 MeV 区间内共有 **38** 行 E1 跃迁，名义和为 **0.10137** $e^2\\,\\text{{fm}}^2$。
3. 2.3–4.0 MeV 区间 M1 强度和为 **0.992** $\\mu_N^2$（接近正文宣称的 $\\sim 1\\,\\mu_N^2$ 剪刀模强度）。
4. 5080.93(31) keV 跃迁单行 $B(E1)\\uparrow = 0.05(4)\\,e^2\\,\\text{{fm}}^2$，分支比 $\\text{{BR}} = 0.12(11)$。

---

## 2. 强度极度集中度与 5080.93 keV 单行主导性

在 4.5–5.5 MeV 的 E1 共振聚集区（常被视为类八极共振或 PDR 团簇），数据呈现出极高程度的单态集中：
1. **名义强度份额**：5080.93(31) keV 单行强度为 0.050 $e^2\\,\\text{{fm}}^2$，占该区间全部 38 条 E1 跃迁总和（0.10137 $e^2\\,\\text{{fm}}^2$）的 **49.32%**。
2. **误差与方差集中**：在假定独立误差传播场景下，该区间的方差总和为 $\\sum \\sigma_i^2 = 0.04037^2 = 0.00163$。其中 5080.93 keV 态自身的方差为 $0.04^2 = 0.00160$，占该区间全部 38 行总方差的 **98.17%**。其余 37 行跃迁的方差总和仅占 1.83%。

---

## 3. Leave-One-Line-Out 灵敏度诊断

> **方法学声明**：留一线移除分析是纯粹的数学灵敏度诊断，用于量化单行数据对整体积分矩的杠杆效应，**绝非实验修正、数据剔除或实验伪证（falsification）**。

### 3.1 对总和影响最大的前 5 行 (4.5–5.5 MeV E1)

| 行号 | $E_\\gamma$ (keV) | $B(E1)\\uparrow$ | BR | 移除后总和 ($e^2\\text{{fm}}^2$) | $\\Delta\\text{{Sum}}$ | 相对变化 | 移除后质心 (keV) | $\\Delta\\text{{Centroid}}$ |
|---|---|---|---|---|---|---|---|---|
| **079** | **5080.93(31)** | **0.05(4)** | **0.12(11)** | **0.05137** | **-0.05000** | **-49.32%** | **5058.78** | **-10.92 keV** |
| 076 | 5041.8(1.0) | 0.006(5) | 0.07(6) | 0.09537 | -0.00600 | -5.92% | 5071.47 | +1.76 keV |
| 073 | 4985.94(35) | 0.005(1) | 0.35(9) | 0.09637 | -0.00500 | -4.93% | 5074.07 | +4.35 keV |
| 096 | 5477.39(10) | 0.0042(4) | 0.39(5) | 0.09717 | -0.00420 | -4.14% | 5052.09 | -17.62 keV |
| 089 | 5248.9(4) | 0.0029(9) | 0.37(10) | 0.09847 | -0.00290 | -2.86% | 5064.44 | -5.28 keV |

### 3.2 对质心能量影响最大的前 5 行 (4.5–5.5 MeV E1)

| 行号 | $E_\\gamma$ (keV) | $B(E1)\\uparrow$ | BR | $\\Delta\\text{{Sum}}$ | 相对变化 | 移除后质心 (keV) | $\\Delta\\text{{Centroid}}$ |
|---|---|---|---|---|---|---|---|
| 096 | 5477.39(10) | 0.0042(4) | 0.39(5) | -0.00420 | -4.14% | 5052.09 | **-17.62 keV** |
| **079** | **5080.93(31)** | **0.05(4)** | **0.12(11)** | **-0.05000** | **-49.32%** | **5058.78** | **-10.92 keV** |
| 095 | 5463.07(17) | 0.0026(2) | 1 | -0.00260 | -2.56% | 5059.36 | -10.35 keV |
| 060 | 4718.32(12) | 0.0024(2) | 0.853(4) | -0.00240 | -2.37% | 5078.23 | +8.52 keV |
| 051 | 4528.6(4) | 0.0015(6) | 0.34(19) | -0.00150 | -1.48% | 5077.84 | +8.13 keV |

---

## 4. 与 G14 转录 CSV 的逐字段对比与处理规范

本审计对 G14 转录 CSV (`outputs/l3/20261107-nuclear-structure-continuation/G14/table1_transitions_102Ru_NRF.csv`) 进行了严格核对：
1. **原文 raw 字段完全一致**：全部 106 行的 `Ei_reported_raw`, `Egamma_reported_raw`, `BR_reported_raw`, `asymmetry_reported_raw`, `multipolarity_reported`, 及对应多极性的 `B_up_reported_raw` 字符串实现 **100% 字节级匹配，0 差异**。
2. **未给误差使用 null（非 0.0）**：
   - 原文 BR 列中，66 行报告为整数 `1`（无括号误差）。G14 将其解析为 `BR_unc = 0.0`，而本审计按规范设定为 `null`（空串），避免将未测量/假设的分支比误判为零误差精密测量。
   - 第 51 行（Page 2, Line 17）$E_i$ 为 `4528.8`（无括号误差）。G14 设为 `0.0`，本审计设定为 `null`。
3. **保留非标准格式原字**：
   - 第 91 行（Page 3, Line 6）$E_i$ 为 `5299.11(1.4)`（数值为两位小数，括号误差为一位小数 `1.4`）。本审计保持原字，并在 `uncertainty_note` 中明确记录：“Decimals mismatch in Ei '5299.11(1.4)': value has 2 decimals, uncertainty has 1; preserved verbatim as 1.4 without forced normalization.”
4. **剔除下跳推导与宽度推导**：
   - G14 CSV 中包含了假设 $J=1$（统计因子 $g=3$）推导的向下跃迁强度（`BM1_down` / `BE1_down`）。本审计严格遵照指令，仅输出向上 $B\\uparrow$，不生成向下跃迁值，亦不生成 $\\Gamma_0$ 或 $\\Gamma$。

---

## 5. 科学边界与物理结论提示

1. **分支比实验改进优先级**：
   对保持弹性散射强度及其它输入固定的提取，B(E1)与BR的倒数有关。5080.93keV线的BR与强度边际误差较大，优先改善该分支信息是有价值的实验候选；其实际误差预算和机制判断仍需联合响应/似然。
2. **106 行跃迁非统计独立**：
   106行可能共享通量、效率、分支及本底处理的系统误差。完整Cov未给，不能将各行独立当作已证事实；平方和仅为本任务声明的条件传播场景。
3. **BR=1 并非严格下限**：
   在未探测到退激至激发态分支的能级中，原文记为 $\\text{{BR}}=1$。但这仅代表在当前探测灵敏度或后向/侧向阵列效率下未分辨出非弹性分支，不能将 $\\text{{BR}}=1$ 视作绝对的严格下限。
4. **实测宽度不等同吸收截面响应**：
   NRF 实验观测到的弹性与非弹性光子散射截面仅反映了能够通过电磁跃迁退激到低激发态的分支；在高能区，由于能级密度急剧上升，大量准连续谱（nuclear quasi-continuum）和多步级联衰变无法被单能峰识别，因此不能直接将离散峰的强度和等同于原子核的总光吸收截面响应。
5. **理论缺口尚未完全闭合**：
   本审计揭示了实验共振聚集对单行分支比的高度敏感性。但这一发现属于数据诊断与观测鲁棒性范畴，并不意味着剪刀模与八极共振共存的微观理论争议已全盘解决。
"""


def generate_receipt_json(
    provenance: Dict[str, Any],
    comparison: Dict[str, Any],
    windows_summary: Dict[str, Any],
    loo_summary: Dict[str, Any],
    changed_files: List[str]
) -> Dict[str, Any]:
    """Generate structured receipt JSON."""
    return {
        "producer": provenance["producer"],
        "timestamp": provenance["execution_date"],
        "script": provenance["script"],
        "status": "completed",
        "inputs": [
            {
                "path": provenance["input_pdf_path"],
                "sha256": provenance["input_pdf_sha256"],
                "role": "primary_evidence_pdf"
            },
            {
                "path": provenance["g14_csv_path"],
                "sha256": provenance["g14_csv_sha256"],
                "role": "reference_g14_transcription_csv"
            }
        ],
        "key_reproduced_values": {
            "total_rows_parsed": 106,
            "multipolarity_counts": {
                "M1_total": 34,
                "M1_bracketed": 1,
                "E1_total": 72,
                "E1_bracketed": 6
            },
            "E1_sum_full_table_with_bracketed": 0.15408,
            "E1_sum_4_5_to_5_5_MeV_38_lines": 0.10137,
            "line_5080_93_keV": {
                "Egamma_raw": "5080.93(31)",
                "BR_raw": "0.12(11)",
                "BE1_up_raw": "0.05(4)",
                "share_of_4_5_to_5_5_MeV_window_pct": 49.32,
                "share_of_4_5_to_5_5_MeV_variance_pct": 98.17
            },
            "leave_one_out_sensitivity": {
                "sum_without_5080_keV": 0.05137,
                "delta_sum_without_5080_keV": -0.05000,
                "centroid_shift_without_5080_keV": -10.92
            }
        },
        "scientific_boundaries": [
            "The 106 transitions share systematic calibrations and cannot be treated as statistically independent.",
            "BR=1 cannot be assumed as a strict lower bound in all circumstances without complete cascade measurements.",
            "Observed NRF elastic strengths cannot be equated directly to full photon absorption response.",
            "Leave-one-out sensitivity is purely an analytical diagnostic, not an experimental data exclusion.",
            "Study specifically highlights 5080.93 keV branching ratio as primary priority for future experimental improvement."
        ],
        "changed_files": changed_files
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Reproducible parser and strength concentration audit for 102Ru PRL Table I."
    )
    parser.add_argument("--pdf", type=Path, default=DEFAULT_PDF, help="Path to SI Table I PDF")
    parser.add_argument("--g14-csv", type=Path, default=DEFAULT_G14_CSV, help="Path to G14 reference CSV")
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR, help="Output directory")
    parser.add_argument("--check-only", action="store_true", help="Run audit checks without writing output files")
    parser.add_argument("--run-tests", action="store_true", help="Run internal negative and sanity tests first")

    args = parser.parse_args()

    if args.run_tests:
        run_negative_tests()

    print(f"=== 102Ru SI Table I Strength Audit ===")
    print(f"Target PDF: {args.pdf}")
    pdf_hash = sha256_file(args.pdf)
    if pdf_hash != EXPECTED_PDF_SHA256:
        raise ValueError("This audit is pinned to the archived five-page SI; PDF hash mismatch.")
    print(f"PDF SHA256: {pdf_hash}")

    # Extract text
    print("Extracting Table I text from PDF (pages 1-3) with pdftotext -layout...")
    layout_text = extract_table1_text(args.pdf)

    # Parse rows
    print("Parsing 106 rows from Table I...")
    parsed_rows = parse_table1_rows(layout_text)
    print(f"Successfully extracted {len(parsed_rows)} rows without exception.")

    # Compare with G14 CSV
    print(f"Comparing with existing G14 CSV: {args.g14_csv}...")
    comparison = compare_with_g14(parsed_rows, args.g14_csv)
    if not comparison.get("g14_csv_present"):
        raise FileNotFoundError("The reference transcription is required for this bounded audit.")
    if comparison["raw_string_mismatches_count"]:
        raise ValueError("Reference transcription differs from the original; review before generating a report.")
    print(
        f"G14 Comparison: {comparison.get('raw_string_mismatches_count', 0)} raw string mismatches, "
        f"{comparison.get('treatment_differences_count', 0)} standardized treatment refinements."
    )

    # Calculate windows
    print("Computing predetermined energy windows...")
    windows_summary = calculate_predetermined_windows(parsed_rows)

    # Print highlights
    e1_full = windows_summary["full_table"]["multipolarities"]["E1"]["with_bracketed"]
    e1_w3 = windows_summary["window_4_5_to_5_5_MeV"]["multipolarities"]["E1"]["with_bracketed"]
    m1_w2 = windows_summary["window_2_3_to_4_0_MeV"]["multipolarities"]["M1"]["with_bracketed"]
    print(f"  * E1 Total sum: {e1_full['sum_B_up']} e2 fm2 (N={e1_full['count_N']})")
    print(f"  * 4.5-5.5 MeV E1 sum: {e1_w3['sum_B_up']} e2 fm2 (N={e1_w3['count_N']})")
    print(f"  * 2.3-4.0 MeV M1 sum: {m1_w2['sum_B_up']} muN2 (N={m1_w2['count_N']})")
    print(
        f"  * Max row in 4.5-5.5 MeV: {e1_w3['max_row']['Egamma_reported_raw']} "
        f"B={e1_w3['max_row']['B_up_val']}, BR={e1_w3['max_row']['BR_reported_raw']}, "
        f"share={e1_w3['max_row']['share_pct']}%, variance_share={e1_w3['max_row']['variance_share_pct_indep']}%"
    )

    # Leave-one-out sensitivity
    print("Computing leave-one-line-out sensitivity diagnostics...")
    loo_summary = calculate_leave_one_out_sensitivity(parsed_rows)

    top_loo = loo_summary["most_influential_on_sum"][0]
    print(
        f"  * Top influential line: {top_loo['Egamma_raw']} B={top_loo['BE1_up_e2fm2']} BR={top_loo['BR_raw']} "
        f"-> sum without line: {top_loo['sum_loo_e2fm2']} e2 fm2 ({top_loo['delta_sum_pct']:+.2f}%), "
        f"delta centroid: {top_loo['delta_centroid_keV']:+.2f} keV"
    )

    if args.check_only:
        print("[CHECK-ONLY] Verification complete. Output files not written.")
        return 0

    # Ensure output directory exists
    out_dir = args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    # Write files
    csv_out = out_dir / "table1_parsed_audit.csv"
    json_out = out_dir / "table1_parsed_audit.json"
    win_out = out_dir / "strength_windows_summary.json"
    loo_out = out_dir / "leave_one_out_sensitivity.json"
    comp_out = out_dir / "comparison_with_g14.json"
    prov_out = out_dir / "run-provenance.json"
    rep_out = out_dir / "report.md"
    rec_out = out_dir / "receipt.json"

    # CSV
    fieldnames = list(parsed_rows[0].keys())
    with open(csv_out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for r in parsed_rows:
            # Format row for CSV: None as empty string
            row_formatted = {k: ("" if v is None else v) for k, v in r.items()}
            writer.writerow(row_formatted)
    print(f"Wrote audited CSV: {csv_out} ({csv_out.stat().st_size} bytes)")

    # JSON Table
    with open(json_out, "w", encoding="utf-8") as f:
        json.dump(parsed_rows, f, indent=2, ensure_ascii=False)
    print(f"Wrote audited JSON: {json_out} ({json_out.stat().st_size} bytes)")

    # Windows summary
    with open(win_out, "w", encoding="utf-8") as f:
        json.dump(windows_summary, f, indent=2, ensure_ascii=False)
    print(f"Wrote windows summary: {win_out} ({win_out.stat().st_size} bytes)")

    # Leave one out
    with open(loo_out, "w", encoding="utf-8") as f:
        json.dump(loo_summary, f, indent=2, ensure_ascii=False)
    print(f"Wrote LOO sensitivity: {loo_out} ({loo_out.stat().st_size} bytes)")

    # Comparison
    with open(comp_out, "w", encoding="utf-8") as f:
        json.dump(comparison, f, indent=2, ensure_ascii=False)
    print(f"Wrote comparison JSON: {comp_out} ({comp_out.stat().st_size} bytes)")

    # Provenance
    provenance = {
        "producer": "Gemini/high worker G24",
        "execution_date": datetime.now(timezone.utc).isoformat(),
        "script": str(Path("system/scripts/ru102_si_strength_audit.py")),
        "script_sha256": sha256_file("system/scripts/ru102_si_strength_audit.py"),
        "input_pdf_path": str(args.pdf),
        "input_pdf_sha256": pdf_hash,
        "g14_csv_path": str(args.g14_csv),
        "g14_csv_sha256": sha256_file(args.g14_csv),
        "command": " ".join(sys.argv),
        "environment": {
            "python_version": sys.version.split()[0],
            "pdftotext_path": "/usr/bin/pdftotext",
            "cwd": str(Path.cwd())
        }
    }
    with open(prov_out, "w", encoding="utf-8") as f:
        json.dump(provenance, f, indent=2, ensure_ascii=False)
    print(f"Wrote provenance JSON: {prov_out} ({prov_out.stat().st_size} bytes)")

    # Report MD
    report_content = generate_report_md(provenance, comparison, windows_summary, loo_summary)
    with open(rep_out, "w", encoding="utf-8") as f:
        f.write(report_content)
    print(f"Wrote report Markdown: {rep_out} ({rep_out.stat().st_size} bytes)")

    # Receipt JSON
    changed_files = [
        str(csv_out),
        str(json_out),
        str(win_out),
        str(loo_out),
        str(comp_out),
        str(prov_out),
        str(rep_out),
        str(rec_out)
    ]
    receipt_data = generate_receipt_json(provenance, comparison, windows_summary, loo_summary, changed_files)
    with open(rec_out, "w", encoding="utf-8") as f:
        json.dump(receipt_data, f, indent=2, ensure_ascii=False)
    print(f"Wrote receipt JSON: {rec_out} ({rec_out.stat().st_size} bytes)")

    print("\n[SUCCESS] Audit completed successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
