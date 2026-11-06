#!/usr/bin/env python3
"""Bounded audit of one archived report; no core imports, network, or fitting.

Run with Python -B. --write creates new JSON/CSV files beside this script and
refuses to overwrite either. Publisher text/images are never exported here.
Marker centres are approximate graphical data, not new experimental results.
No error bars are interpreted as statistical uncertainties.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import pymupdf


HERE = Path(__file__).resolve().parent
ROOT = next(
    p for p in HERE.parents
    if (p / "README.md").is_file() and (p / "raw").is_dir() and (p / "system").is_dir()
)
COLLECTION = ROOT / "raw/papers/gpt/query/20261106-ba129-independent-branch-data"
PDF = COLLECTION / "kumar-branch-report.pdf"
METADATA = COLLECTION / "inspire-lookup-0.json"
ENSDF_DIR = ROOT / (
    "raw/papers/gpt/learning-daily/"
    "20261016-DAY15-ado-angular-distribution-geometry"
)
REACTION = ENSDF_DIR / "nndc-129ba-129056013-201408-09194d4feed3.ens"
ADOPTED = ENSDF_DIR / "nndc-129ba-129056001-201408-15d8e353eb23.ens"
EXPECTED_PDF = "210c65109df9b2d203f95643e0fb89746a20f836265c802bb0f2010aabb5eda1"
EXPECTED_REACTION = "09194d4feed3bbda013c551ce5ba9ecf55a25799e8c46ec22f23685df1c1ef19"
EXPECTED_ADOPTED = "15d8e353eb23d55847dc0d0127591fd2fb23e6da63ae98146747aecb233f65f6"
DOCUMENT_KEY = "ba29e364d79767347c64c5000a8a1159"
SPINS = [6.5, 7.5, 8.5, 9.5, 10.5, 12.5]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fact(value: F) -> int:
    assert value.denominator == 1 and value >= 0
    return math.factorial(int(value))


def cg_squared(j1: F, j2: F, final_j: F, m1: F, m2: F) -> F:
    """Exact squared CG via Racah's factorial sum, not the tested Eq. 3 ratio.

    Uses CG(j1 m1, j2 m2 | final_j, m1+m2)^2 =
    (2 final_j+1) * 3j(j1,j2,final_j;m1,m2,-m1-m2)^2.
    All phases cancel in this squared quantity. Arguments are exact Fractions.
    """
    m3 = -m1 - m2
    if final_j < abs(j1 - j2) or final_j > j1 + j2:
        return F(0)
    if abs(m1) > j1 or abs(m2) > j2 or abs(m3) > final_j:
        return F(0)
    tri = (j1 + j2 - final_j, j1 - j2 + final_j, -j1 + j2 + final_j)
    prefactor = F(math.prod(fact(v) for v in tri), fact(j1 + j2 + final_j + 1))
    for j, m in [(j1, m1), (j2, m2), (final_j, m3)]:
        prefactor *= fact(j + m) * fact(j - m)
    total = F(0)
    for z in range(int(j1 + j2 + final_j) + 1):
        terms = (
            F(z), j1 + j2 - final_j - z, j1 - m1 - z, j2 + m2 - z,
            final_j - j2 + m1 + z, final_j - j1 - m2 + z,
        )
        if any(v < 0 for v in terms):
            continue
        total += F((-1) ** z, math.prod(fact(v) for v in terms))
    return (2 * final_j + 1) * prefactor * total * total


def rotational_ratio(spin: F, k: F) -> F:
    return 2 * k * k * (2 * spin - 1) / (
        (spin + 1) * (spin + k - 1) * (spin - k - 1)
    )


def exact_checks() -> dict:
    count = 0
    for k in (F(9, 2), F(11, 2)):
        for two_i in range(int(2 * k) + 4, 28, 2):
            spin = F(two_i, 2)
            c1 = cg_squared(spin, F(2), spin - 1, k, F(0))
            c2 = cg_squared(spin, F(2), spin - 2, k, F(0))
            assert c1 / c2 == rotational_ratio(spin, k)
            count += 1

    normalization_count = 0
    for j, k in [(F(9, 2), F(1, 2)), (F(13, 2), F(9, 2)),
                 (F(15, 2), F(11, 2))]:
        assert cg_squared(j, F(0), j, k, F(0)) == 1
        assert cg_squared(j, F(1), j, k, F(0)) == k * k / (j * (j + 1))
        assert sum(cg_squared(j, F(2), j + n, k, F(0)) for n in range(-2, 3)) == 1
        normalization_count += 3

    # Construct physical photon rates with positive B values, in units where
    # a_M1=1 and a_E2=0.6967. This tests the missing lambda independently of
    # any figure or nuclear transition assignment.
    rate_count = 0
    for e1, e2, bm, be2, q_ratio in [
        (F(3, 10), F(6, 10), F(2), F(1), F(3)),
        (F(1, 5), F(7, 10), F(1, 3), F(2), F(162, 25)),
        (F(4, 5), F(9, 10), F(5), F(3), F(1, 2)),
    ]:
        a = F(6967, 10000)
        w_m1 = e1**3 * bm
        w_e2_1 = a * e1**5 * q_ratio * be2
        w_e2_2 = a * e2**5 * be2
        lam = w_e2_2 / (w_m1 + w_e2_1)
        fraction = w_e2_1 / (w_m1 + w_e2_1)
        proxy = a * e2**5 / e1**3 / lam
        assert fraction == lam * q_ratio * (e1 / e2)**5
        assert proxy * (1 - fraction) == bm / be2
        assert fraction != q_ratio * (e1 / e2)**5
        rate_count += 1

    assert cg_squared(F(13, 2), F(2), F(9, 2), F(11, 2), F(0)) == 0
    return {
        "exact_rotational_CG_ratio_cases": count,
        "exact_CG_scalar_vector_completeness_controls": normalization_count,
        "exact_photon_rate_lambda_identity_cases": rate_count,
        "K_11_over_2_I_13_over_2_deltaI2_CG_is_zero": True,
        "printed_Eq3_missing_lambda_under_Eq2_definition": True,
    }


# Rectangles isolate data markers, excluding legends. They are geometrical
# selectors for the hash-pinned source, not fitted physics parameters.
PANELS = {
    "fig2_upper": dict(box=(115, 415, 255, 446), left=110.42276,
                       ticks=(400, 450), labels=(456, 463), xspan=(113, 288)),
    "fig3_upper": dict(box=(325, 176, 468, 203), left=321.90076,
                       ticks=(156, 206), labels=(212, 220), xspan=(325, 502)),
    "fig2_lower": dict(box=(115, 484, 255, 510), left=110.42276,
                       ticks=(464, 510), labels=(518, 525), xspan=(113, 288)),
    "fig3_lower": dict(box=(325, 245, 468, 261), left=321.90076,
                       ticks=(220, 262), labels=(275, 283), xspan=(325, 502)),
}


def extract_panels(page: pymupdf.Page) -> tuple[dict, dict]:
    drawings = page.get_drawings()
    spans = [
        span for block in page.get_text("dict")["blocks"]
        for line in block.get("lines", []) for span in line["spans"]
    ]
    results, diagnostics = {}, {}
    for name, config in PANELS.items():
        ticks = []
        for drawing in drawings:
            if len(drawing["items"]) != 1 or drawing["color"] != (0., 0., 0.):
                continue
            item = drawing["items"][0]
            if item[0] != "l":
                continue
            a, b = item[1:]
            if (abs(a.x - config["left"]) < .01 and abs(a.y - b.y) < .001
                    and 3 < a.x - b.x < 4 and config["ticks"][0] < a.y < config["ticks"][1]):
                ticks.append(a.y)
        ticks.sort(reverse=True)
        assert len(ticks) == 4
        yscale, yoffset = np.polyfit(ticks, [0, 1, 2, 3], 1)
        labels = []
        for span in spans:
            try:
                number = float(span["text"])
            except ValueError:
                continue
            x0, y0, x1, _ = span["bbox"]
            if (6 <= number <= 14 and config["labels"][0] < y0 < config["labels"][1]
                    and config["xspan"][0] < x0 < config["xspan"][1]):
                labels.append(((x0 + x1) / 2, number))
        assert len(labels) >= 10
        xscale, xoffset = np.polyfit(*zip(*labels), 1)
        box = pymupdf.Rect(config["box"])
        results[name] = {}
        max_spin_error = 0.
        for series, color in [
            ("present", (0., 0., 0.)),
            ("previous", (0., 1., 0.) if "upper" in name else (1., 0., 0.)),
        ]:
            markers = sorted(
                [d for d in drawings if d["fill"] == color and box.contains(d["rect"])],
                key=lambda d: d["rect"].x0,
            )
            assert len(markers) == 6
            points = []
            for drawing, expected_spin in zip(markers, SPINS):
                rect = drawing["rect"]
                spin = float(xscale * (rect.x0 + rect.x1) / 2 + xoffset)
                max_spin_error = max(max_spin_error, abs(spin - expected_spin))
                assert abs(spin - expected_spin) < .025
                points.append(float(yscale * (rect.y0 + rect.y1) / 2 + yoffset))
            results[name][series] = points
        diagnostics[name] = {
            "points_per_series": 6,
            "max_spin_axis_residual": max_spin_error,
            "max_y_tick_calibration_residual": float(
                max(abs(yscale * np.array(ticks) + yoffset - np.arange(4)))
            ),
        }
    return results, diagnostics


def read_gamma(lines: list[str], number: int) -> dict:
    line = lines[number - 1]
    assert line[5:8] == "  G"
    return {
        "line": number, "E_keV": float(line[9:19]),
        "RI": float(line[21:29]), "multipolarity": line[31:41].strip(),
    }


def branch_and_gate_checks(panels: dict) -> tuple[list[dict], dict]:
    lines = REACTION.read_text().splitlines()
    specs = [
        (13, 132, 133, 139), (15, 143, 144, 149),
        (17, 195, 196, 199), (19, 206, 207, 211),
        (21, 255, 256, 258), (25, 367, 368, 370),
    ]
    rows = []
    for n, (two_i, level_line, gamma1_line, gamma2_line) in enumerate(specs):
        g1, g2 = read_gamma(lines, gamma1_line), read_gamma(lines, gamma2_line)
        e1, e2 = g1["E_keV"] / 1000, g2["E_keV"] / 1000
        coef = .6967 * e2**5 / e1**3
        q = float(rotational_ratio(F(two_i, 2), F(9, 2)))
        printed_fraction = q * (e1 / e2)**5
        b0 = panels["fig2_upper"]["present"][n]
        old_b0 = coef * g1["RI"] / g2["RI"]
        row = {
            "two_I": two_i,
            "candidate_parent_keV_ENSDF": float(lines[level_line - 1][9:19]),
            "candidate_E_deltaI1_keV_ENSDF": g1["E_keV"],
            "candidate_E_deltaI2_keV_ENSDF": g2["E_keV"],
            "reaction_level_line": level_line,
            "reaction_gamma1_line": gamma1_line,
            "reaction_gamma2_line": gamma2_line,
            "fig2_upper_present_approx": b0,
            "fig3_upper_present_approx": panels["fig3_upper"]["present"][n],
            "fig2_upper_previous_approx": panels["fig2_upper"]["previous"][n],
            "fig3_upper_previous_approx": panels["fig3_upper"]["previous"][n],
            "ENSDF_1992_RI_deltaI1_over_deltaI2": g1["RI"] / g2["RI"],
            "ENSDF_1992_delta_zero_proxy": old_b0,
            "conditional_inverse_present_RI_deltaI1_over_deltaI2": b0 / coef,
            "fig2_lower_present_approx": panels["fig2_lower"]["present"][n],
            "fig2_lower_previous_approx": panels["fig2_lower"]["previous"][n],
            "Eq3_printed_fraction_K9over2_using_candidate_energies": printed_fraction,
            "fraction_with_lambda_present_K9over2": printed_fraction * coef / b0,
            "amended_lower_present_central_algebra": b0 - coef * printed_fraction,
            "amended_lower_previous_central_algebra": old_b0 - coef * printed_fraction,
            "mapping_status": "candidate_ENSDF_1992_pairs_not_a_new_report_energy_table",
            "experimental_uncertainty": None,
            "eligibility": "conditional_graphic_audit_only_not_validated_branch_data",
        }
        rows.append(row)
    old_error = max(abs(r["ENSDF_1992_delta_zero_proxy"] -
                        r["fig2_upper_previous_approx"]) for r in rows)
    assert old_error < .003

    # Restricted negative-parity cascade, inferred from E_level-E_gamma.
    # It is a topological test, not a completeness or gate-correction claim.
    level_lines = {9: 79, 11: 97, 13: 132, 15: 143, 17: 195,
                   19: 206, 21: 255, 23: 262, 25: 367}
    energies = {i: float(lines[n - 1][9:19]) for i, n in level_lines.items()}
    gamma_lines = {11: [98], 13: [133, 139], 15: [144, 149],
                   17: [196, 199], 19: [207, 211], 21: [256, 258],
                   23: [263], 25: [368, 370]}
    edges = {}
    largest_residual = 0.
    for two_i, glines in gamma_lines.items():
        edges[two_i] = []
        for lineno in glines:
            target_e = energies[two_i] - read_gamma(lines, lineno)["E_keV"]
            daughter = min(energies, key=lambda i: abs(energies[i] - target_e))
            residual = abs(energies[daughter] - target_e)
            assert residual < .25 and daughter < two_i
            largest_residual = max(largest_residual, residual)
            edges[two_i].append(daughter)

    def endpoints(i: int) -> set[int]:
        if i == 9:
            return {9}
        return set().union(*(endpoints(d) for d in edges[i]))

    assert all(endpoints(i) == {9} for i in edges)
    return rows, {
        "previous_upper_vs_ENSDF_proxy_max_abs_difference": old_error,
        "previous_lower_vs_amended_K9over2_formula_max_abs_difference": max(
            abs(r["fig2_lower_previous_approx"] -
                r["amended_lower_previous_central_algebra"]) for r in rows
        ),
        "present_amended_K9over2_central_fractions_above_one_two_I": [
            r["two_I"] for r in rows if r["fraction_with_lambda_present_K9over2"] > 1
        ],
        "restricted_cascade_edges_in_two_I": edges,
        "restricted_cascade_all_routes_end_at_182keV_9over2minus": True,
        "max_edge_energy_closure_residual_keV": largest_residual,
        "gate_174p1_to_ENSDF_173p6_assignment": "plausible_but_unconfirmed",
        "gate_common_downstream_is_not_proof_of_corrected_intensities": True,
        "central_admissibility_checks_are_not_statistical_rejections": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    inputs = [PDF, METADATA, REACTION, ADOPTED]
    hashes_before = {str(p.relative_to(ROOT)): sha256(p) for p in inputs}
    assert sha256(PDF) == EXPECTED_PDF
    assert sha256(REACTION) == EXPECTED_REACTION
    assert sha256(ADOPTED) == EXPECTED_ADOPTED
    lookup = json.loads(METADATA.read_text())
    hits = lookup["hits"]["hits"]
    assert lookup["hits"]["total"] == 1 and len(hits) == 1
    assert str(hits[0]["id"]) == "2765575"
    metadata = hits[0]["metadata"]
    assert any(d["key"] == DOCUMENT_KEY for d in metadata["documents"])
    assert metadata["publication_info"][0]["year"] == 2024
    assert metadata["imprints"][0]["date"] == "2024"
    with pymupdf.open(PDF) as document:
        assert len(document) == 2
        panels, geometry = extract_panels(document[1])
        pdf_metadata = {
            k: document.metadata[k] for k in ["creationDate", "modDate", "creator", "producer"]
        }
    algebra = exact_checks()
    rows, branch_checks = branch_and_gate_checks(panels)
    max_repeat = max(
        abs(a - b) for series in ["present", "previous"]
        for a, b in zip(panels["fig2_upper"][series], panels["fig3_upper"][series])
    )
    assert max_repeat < .008
    hashes_after = {str(p.relative_to(ROOT)): sha256(p) for p in inputs}
    assert hashes_before == hashes_after
    results = {
        "status": "bounded_source_audit_completed_not_physical_model_validation",
        "run_label": "20261106",
        "checked_at_actual_tool_clock": datetime.now(timezone.utc).isoformat(),
        "hashes_sha256": hashes_before,
        "input_hashes_unchanged_during_check": True,
        "bibliography": {
            "canonical_INSPIRE_id": 2765575,
            "document_key": DOCUMENT_KEY,
            "publication_info": metadata["publication_info"],
            "imprints": metadata["imprints"],
            "PDF_has_no_printed_publication_year": True,
            "pdf_file_metadata_is_not_publication_date": pdf_metadata,
            "PDF_authors": ["S. Kumar", "Mallicka Kundu", "P. S. Rawat",
                            "Ksh. Rojeeta Devi", "H. Chutani", "M. Goyal"],
            "INSPIRE_author_list_omits_Ksh_Rojeeta_Devi": True,
            "metadata_locator": "inspire-lookup-0.json: hits.hits[0].metadata",
        },
        "source_setup_verified_visually_PDF_page1_Experimental_Details": {
            "reaction": "121Sb(12C,p3n)129Ba",
            "beam_energy_MeV": 66,
            "target_mg_per_cm2": 1.2,
            "197Au_backing_mg_per_cm2": 10.0,
            "facility": "IUAC, New Delhi",
            "array": "INGA",
            "Compton_suppressed_clover_detectors": 18,
            "LEPS_detectors": 2,
            "reported_total_coincidences": None,
            "acquisition_date": None,
        },
        "independent_exact_checks": algebra,
        "graphical_digitization": {
            "method": "vector_marker_centres_calibrated_against_drawn_ticks",
            "spins": SPINS,
            "panels": panels,
            "axis_diagnostics": geometry,
            "upper_panels_max_abs_difference": max_repeat,
            "independent_acquisitions_represented_by_two_present_series": 1,
            "experimental_uncertainties_extracted": False,
            "experimental_covariances_available": False,
            "digitization_residual_is_not_measurement_uncertainty": True,
        },
        "conditional_branch_checks": branch_checks,
        "limitations": [
            "No numeric intensity or transition-energy pair table in the two-page report.",
            "Fig1 gate shown; report does not establish that this alone produced every plotted ratio.",
            "Efficiency, angular-correlation, timing, background and gate-path corrections unspecified.",
            "Candidate energies used in inversion come from 2014 ENSDF/1992 measurement lineage.",
            "Printed Eq3 does not certify the authors' actual numerical prescription.",
            "Lower curves and Donau calculations are model-dependent, not independent delta data.",
            "No new statistical errors, absolute strengths, lifetime, delta sign, or mode verdict.",
        ],
        "new_artifact_write_scope": str(HERE.relative_to(ROOT)),
        "source_images_or_extracted_text_written_to_output": False,
        "software": {"numpy": np.__version__, "pymupdf": pymupdf.VersionBind},
    }
    if args.write:
        result_path = HERE / "source-audit-results.json"
        csv_path = HERE / "conditional-graphic-checks.csv"
        assert not result_path.exists() and not csv_path.exists(), "Refusing overwrite"
        with result_path.open("x") as stream:
            json.dump(results, stream, indent=2, allow_nan=False)
            stream.write("\n")
        with csv_path.open("x", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    print(json.dumps({
        "exact_checks": algebra,
        "upper_panel_max_difference": max_repeat,
        "conditional_branch_checks": branch_checks,
        "input_hashes_unchanged": True,
        "wrote_results": args.write,
    }, indent=2))


if __name__ == "__main__":
    main()
