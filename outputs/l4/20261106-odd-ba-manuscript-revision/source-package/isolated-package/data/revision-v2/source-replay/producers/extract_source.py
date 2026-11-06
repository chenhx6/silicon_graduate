"""Freeze Fig. 5(c) source energies for 135/137Ba before kernel comparison.

Reads source PDF/TeX bytes only, plus the previous extractor as a method hash.
No kernel, model spectrum, chain contract, or prediction file is imported/read.
All new files are created exclusively beside this script.
"""

from datetime import datetime, timezone
import csv
import hashlib
import json
import math
from pathlib import Path
import tarfile

import pymupdf

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
RAW = ROOT / "raw/papers/gpt/query/20261105-nomura2017-input-audit"
PAPER = ROOT / "raw/papers/2017_Nomura et al_Shape-phase transitions in odd-mass γ -soft nuclei with mass A ≈ 130.pdf"
ARCHIVE = RAW / "nomura2017-v2-source.tar.gz"
TEX = RAW / "arxiv-v2-v4.tex"
METHOD = ROOT / "outputs/l4/20261105-ba129-controlled-pairing/ibfm-case-review/extract_source_points.py"
EXPECTED = {
    "paper": "481e6a9e0f6b01e9c5db5e2b06d9b350dba0638393c7da7f532c3040e9efaea9",
    "archive": "f7ed6dc746f50f16169d8796e4d12becd8827eaf4ac2ee4d5f1ff9cd04690faf",
    "figure": "b6006a11da9e56b14e31f286cedfe339fda90626bba7632fd934cc78ba861ef2",
}
SERIES = (
    (7, "triangle_left", 151, 152, (0.0, 0.5, 0.0)),
    (9, "triangle_down", 157, 158, (0.75, 0.75, 0.0)),
    (11, "circle", 163, 164, (0.0, 0.0, 0.0)),
    (13, "triangle_up", 169, 170, (0.0, 0.0, 1.0)),
    (15, "square", 175, 176, (1.0, 0.0, 0.0)),
    (17, "star", 181, 182, (0.0, 0.75, 0.75)),
)
TARGETS = ((135, 79, 3), (137, 81, 4))
EXTRACTION_TOL_KEV = 0.002


def digest(data):
    return hashlib.sha256(data).hexdigest()


def record(path):
    data = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)), "sha256": digest(data), "size_bytes": len(data)}


def mean(points):
    return tuple(sum(p[i] for p in points) / len(points) for i in (0, 1))


def marker_anchor(path, kind):
    rect = path["rect"]
    bbox = ((rect.x0 + rect.x1) / 2, (rect.y0 + rect.y1) / 2)
    if kind == "circle":
        assert all(item[0] == "c" for item in path["items"])
        anchor = mean([tuple(item[1]) for item in path["items"]])
        method = "mean of circular Bezier segment starts"
    elif kind == "square":
        assert path["items"][0][0] == "re"
        anchor, method = bbox, "rectangle center"
    else:
        assert all(item[0] == "l" for item in path["items"])
        vertices = [tuple(item[1]) for item in path["items"]]
        if kind == "star":
            assert len(vertices) == 10
            outer = vertices[::2]
            anchor = mean(outer)
            radii = [math.dist(p, anchor) for p in outer]
            assert max(radii) - min(radii) < 0.0001
            method = "mean of five outer star tips, not bounding-box midpoint"
        else:
            assert len(vertices) == 3
            anchor, method = bbox, "tip/base midpoint, not triangle centroid"
    return anchor, bbox, method


def extract_page(page, label):
    drawings = page.get_drawings()
    yticks = []
    for i in range(5):
        index = 197 + 2 * i
        a, b = drawings[index]["items"][0][1:3]
        assert abs(a.y - b.y) < 0.0001
        yticks.append({"path_index": index, "label_MeV": i * 0.5, "y_pt": a.y})
    slope = 2.0 / (yticks[-1]["y_pt"] - yticks[0]["y_pt"])
    intercept = -slope * yticks[0]["y_pt"]
    tick_residual = max(abs(1000 * (intercept + slope * t["y_pt"] - t["label_MeV"])) for t in yticks)
    assert tick_residual < EXTRACTION_TOL_KEV
    xticks = []
    for i in range(5):
        index = 187 + 2 * i
        a, b = drawings[index]["items"][0][1:3]
        assert abs(a.x - b.x) < 0.0001
        xticks.append({"path_index": index, "label_N": 73 + 2 * i, "x_pt": a.x})
    xslope = 8 / (xticks[-1]["x_pt"] - xticks[0]["x_pt"])
    xintercept = 73 - xslope * xticks[0]["x_pt"]
    points = []
    for two_J, kind, line_index, first_marker, rgb in SERIES:
        line = drawings[line_index]
        assert tuple(line["color"]) == rgb
        assert len(line["items"]) == 4
        assert all(item[0] == "l" for item in line["items"])
        line_points = [tuple(line["items"][0][1])] + [tuple(x[2]) for x in line["items"]]
        for odd_A, N, i in TARGETS:
            marker = drawings[first_marker + i]
            assert tuple(marker["fill"]) == rgb
            anchor, bbox, method = marker_anchor(marker, kind)
            line_point = line_points[i]
            marker_line_keV = abs(1000 * slope * (anchor[1] - line_point[1]))
            assert marker_line_keV < EXTRACTION_TOL_KEV
            encoded_N = xintercept + xslope * anchor[0]
            assert abs(encoded_N - N) < 0.00001
            energy = 1000 * (intercept + slope * anchor[1])
            grid_energy = round(energy)
            grid_error = abs(energy - grid_energy)
            assert grid_error < EXTRACTION_TOL_KEV
            points.append({
                "odd_A": odd_A, "neutron_N": N, "two_J": two_J, "parity": -1,
                "source_legend_label": f"{two_J}/2-",
                "ordinal_printed_in_legend": False,
                "comparison_state_policy": "lowest kernel eigenstate at this J, fixed before comparison",
                "marker_kind": kind, "fill_rgb": list(rgb),
                "path_index": first_marker + i, "connecting_path_index": line_index,
                "marker_anchor_pt": list(anchor), "connecting_vertex_pt": list(line_point),
                "anchor_method": method, "encoded_N": encoded_N,
                "marker_line_energy_disagreement_keV": marker_line_keV,
                "bounding_box_energy_bias_keV": 1000 * slope * (bbox[1] - anchor[1]),
                "recovered_energy_keV": energy, "plot_grid_energy_keV": grid_energy,
                "distance_to_1keV_grid_keV": grid_error,
                "reference_state": "lowest displayed 11/2- at N=79 or 81; zero in Fig.5(c)",
            })
    return {
        "representation": label, "page_size_pt": list(page.rect),
        "coordinate_convention": "PDF points, top-left origin, y increases down",
        "y_ticks": yticks, "x_ticks": xticks,
        "energy_MeV_equals_intercept_plus_slope_y": {"intercept": intercept, "slope": slope},
        "N_equals_intercept_plus_slope_x": {"intercept": xintercept, "slope": xslope},
        "max_axis_tick_residual_keV": tick_residual,
        "points": sorted(points, key=lambda p: (p["odd_A"], p["two_J"])),
    }


def write_new(name, value):
    with (OUT / name).open("x", encoding="utf-8") as f:
        json.dump(value, f, indent=2, ensure_ascii=False, allow_nan=False)
        f.write("\n")


def main():
    assert digest(PAPER.read_bytes()) == EXPECTED["paper"]
    assert digest(ARCHIVE.read_bytes()) == EXPECTED["archive"]
    with tarfile.open(ARCHIVE) as tar:
        figure_bytes = tar.extractfile("ba.level.pdf").read()
        assert tar.extractfile("v4.tex").read() == TEX.read_bytes()
    assert digest(figure_bytes) == EXPECTED["figure"]
    assert (OUT / "source-assets/ba.level.pdf").read_bytes() == figure_bytes
    original = pymupdf.open(stream=figure_bytes, filetype="pdf")
    canonical = pymupdf.open(PAPER)
    assert len(canonical) == 13
    raw = extract_page(original[0], "original ba.level.pdf member, Fig.5(c)")
    embedded = extract_page(canonical[6], "canonical archived arXiv-v2 paper physical p.7, Fig.5(c)")
    disagreement = max(abs(a["recovered_energy_keV"] - b["recovered_energy_keV"])
                       for a, b in zip(raw["points"], embedded["points"]))
    assert disagreement < EXTRACTION_TOL_KEV
    assert all(p["plot_grid_energy_keV"] == 0 for p in raw["points"] if p["two_J"] == 11)
    frozen = {
        "schema": "nomura2017-source-only-negative-energy-freeze/1",
        "frozen_at_utc": datetime.now(timezone.utc).isoformat(),
        "frozen_before_kernel_solve_or_spectrum_comparison": True,
        "prior_exposure_boundary": "Previous operator study exposed these Hamiltonian identities and lowest-11/2 state energies; no newly extracted source point was chosen or changed using a model spectrum.",
        "source_version": "canonical local PDF is arXiv:1704.07101v2, not a verified journal VoR",
        "source_files": [record(PAPER), record(ARCHIVE), record(TEX)],
        "original_figure_member": {"name": "ba.level.pdf", "sha256": EXPECTED["figure"], "size_bytes": len(figure_bytes)},
        "method_reference": record(METHOD),
        "extractor": record(Path(__file__)),
        "pymupdf_version": pymupdf.VersionBind,
        "legend_verification": "Original figure and canonical paper p.7 visually checked; theory is panel(c), negative parity; matching marker/color identities fixed without model input.",
        "selection_scope": "Only N=79 (135Ba) and N=81 (137Ba); all six displayed negative-parity theory series at each N.",
        "state_identity_boundary": "The negative-parity legend has spin/parity but no ordinal or wavefunction. Its unique series per J is compared to the requested lowest same-J state; no nearest-energy reassignment.",
        "energy_zero": {
            "source_observation": "11/2- plotted at zero in both target columns, while positive/negative parities have separate panels.",
            "comparison_definition": "E(J_1-) - E(11/2_1-) separately in each isotope",
            "absolute_excitation_from_positive_parity_ground_state_recovered": False,
            "free_shift_fit_performed": False,
            "locator": "Fig.5(c); TeX804-809 and853-856",
        },
        "precision": {
            "numeric_extraction_tolerance_keV": EXTRACTION_TOL_KEV,
            "observed_plot_grid_keV": 1,
            "nearest_rounding_sensitivity_half_width_keV": 0.5,
            "looser_one_grid_sensitivity_half_width_keV": 1.0,
            "rounding_rule_known": False,
            "boundary": "These are plot-resolution sensitivities, not author error bars, confidence intervals, or bounds on unprinted Hamiltonian parameter rounding.",
        },
        "source_evidence": [
            {"locator": "PDF p.2; TeX200-207", "fact": "NB equals valence fermion pairs; NF=1; proton and neutron bosons not distinguished."},
            {"locator": "PDF p.3 Table I; TeX301-302", "fact": "134Ba and136Ba core Hamiltonian rows are printed; no NB column."},
            {"locator": "PDF p.3 Table III; TeX392-393", "fact": "h11/2 occupations for135Ba and137Ba are printed."},
            {"locator": "PDF p.4 Table V; TeX503-518", "fact": "Negative-parity Gamma,Lambda and monopole rows are printed."},
            {"locator": "PDF p.4; TeX539-545", "fact": "Authors identify PBOS diagonalization; no executed input deck or eigenvectors in this archive."},
            {"locator": "PDF p.8; TeX918-927", "fact": "134Ba explicitly called corresponding even-even core of135Ba in the positive-parity E(5/4) discussion."},
            {"locator": "TeX889-913", "fact": "Detailed Ba135 Fig.9 is positive parity; it supplies no additional negative-parity energies for this audit."},
        ],
        "original_figure": raw,
        "canonical_embedded_figure": embedded,
        "max_original_vs_embedded_energy_difference_keV": disagreement,
        "no_kernel_modules_imported": True,
        "no_chain_or_prediction_file_read": True,
    }
    write_new("source-points-frozen.json", frozen)
    with (OUT / "source-points-frozen.csv").open("x", newline="", encoding="utf-8") as f:
        columns = ("odd_A", "neutron_N", "source_legend_label", "two_J",
                   "plot_grid_energy_keV", "recovered_energy_keV", "path_index",
                   "connecting_path_index", "reference_state")
        writer = csv.DictWriter(f, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(raw["points"])
    write_new("source-freeze.json", {
        "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_json": record(OUT / "source-points-frozen.json"),
        "source_csv": record(OUT / "source-points-frozen.csv"),
        "extractor": record(Path(__file__)),
        "source_point_count": len(raw["points"]),
        "kernel_comparison_has_not_run": True,
    })
    print("FROZEN", digest((OUT / "source-points-frozen.json").read_bytes()))
    for p in raw["points"]:
        print(p["odd_A"], p["source_legend_label"], p["plot_grid_energy_keV"], "keV",
              "extraction", p["recovered_energy_keV"])
    print("Original/canonical max disagreement keV:", disagreement)


if __name__ == "__main__":
    main()
