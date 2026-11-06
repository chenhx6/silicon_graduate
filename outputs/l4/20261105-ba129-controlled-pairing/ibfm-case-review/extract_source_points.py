"""Recover published theory points from exact vector PDFs, without model input.

Only the arXiv archive and its two extracted figure members are read.
Axis tick labels and legend assignments were independently inspected in the
paper's pp. 6/7. PDF coordinates use top-left origin, with y increasing down.
No model energy, fit parameter, prediction JSON or exploratory marker JSON
is read by this script. It refuses to overwrite the frozen source result.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import tarfile

import numpy as np
import pymupdf

ROOT = Path("/workspace/wiki")
OUT = ROOT / "outputs/l4/20261105-ba129-controlled-pairing/ibfm-case-review"
ARCHIVE = ROOT / "raw/papers/gpt/query/20261105-nomura2017-input-audit/nomura2017-v2-source.tar.gz"
FIGURES = ROOT / "tmp/ba129-controlled-pairing/source-figure-replay"
EXPECTED_ARCHIVE = "f7ed6dc746f50f16169d8796e4d12becd8827eaf4ac2ee4d5f1ff9cd04690faf"

# Path indices are locators in PyMuPDF get_drawings() for the SHA-locked files.
# Tick labels and series names are from the original figure labels/legends.
SPEC = {
    "even.level.pdf": {
        "sha256": "ae54ff0a2122e33d393ad1bf96f393669d9c874de1d4f1ad5317f1a905a1f4a1",
        "locator": "paper p.6 Fig.3(a), N=72, theoretical 128Ba",
        "target_N": 72,
        "y_ticks": [(42+2*i, i*.5) for i in range(9)],
        "x_ticks": [(32+2*i, 72+2*i) for i in range(5)],
        "series": [
            ("2_1+", 4, 0, 2, 3, "circle"),
            ("4_1+", 8, 0, 8, 9, "square"),
            ("6_1+", 12, 0, 14, 15, "diamond"),
            ("0_2+", 0, 1, 20, 21, "triangle_down"),
            ("2_2+", 4, 1, 26, 27, "triangle_left"),
        ],
    },
    "ba.level.pdf": {
        "sha256": "b6006a11da9e56b14e31f286cedfe339fda90626bba7632fd934cc78ba861ef2",
        "locator": "paper p.7 Fig.5(c), N=73, theoretical negative-parity 129Ba",
        "target_N": 73,
        # Use the explicitly readable 0.0,0.5,1.0,1.5 tick labels.
        "y_ticks": [(197+2*i, i*.5) for i in range(4)],
        "x_ticks": [(187+2*i, 73+2*i) for i in range(5)],
        "series": [
            ("7/2_1-", 7, 0, 151, 152, "triangle_left"),
            ("9/2_1-", 9, 0, 157, 158, "triangle_down"),
            ("11/2_1-", 11, 0, 163, 164, "circle"),
            ("13/2_1-", 13, 0, 169, 170, "triangle_up"),
            ("15/2_1-", 15, 0, 175, 176, "square"),
            ("17/2_1-", 17, 0, 181, 182, "star"),
        ],
    },
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def line_start(path):
    assert path["items"][0][0] == "l"
    return np.array(tuple(path["items"][0][1]), float)


def marker_anchor(path, kind):
    r = path["rect"]
    bbox_mid = np.array([(r.x0+r.x1)/2, (r.y0+r.y1)/2])
    vertices = None
    if kind == "circle":
        assert all(item[0] == "c" for item in path["items"])
        # Mean of evenly spaced Bezier endpoints, excluding a repeated closure.
        vertices = np.array([tuple(item[1]) for item in path["items"]])
        anchor = vertices.mean(axis=0)
        method = "mean of 8 circular Bezier segment start points"
    elif kind == "square":
        assert path["items"][0][0] == "re"
        anchor = bbox_mid
        method = "rectangle center"
    else:
        assert all(item[0] == "l" for item in path["items"])
        # Each start is one vertex; the repeated closing endpoint is excluded.
        vertices = np.array([tuple(item[1]) for item in path["items"]])
        if kind == "star":
            assert len(vertices) == 10
            outer = vertices[::2]
            anchor = outer.mean(axis=0)
            radii = np.linalg.norm(outer-anchor, axis=1)
            assert np.ptp(radii) < 1e-5
            method = "five outer star tips determine rotational center"
        elif kind.startswith("triangle"):
            assert len(vertices) == 3
            anchor = bbox_mid
            method = "tip/base midpoint marker anchor, checked against connecting path"
        elif kind == "diamond":
            assert len(vertices) == 4
            anchor = vertices.mean(axis=0)
            method = "opposite-vertex symmetry center"
        else:
            raise ValueError(kind)
    return anchor, bbox_mid, None if vertices is None else vertices.mean(axis=0), method


def extract():
    archive_bytes = ARCHIVE.read_bytes()
    assert sha(archive_bytes) == EXPECTED_ARCHIVE
    records = []
    with tarfile.open(ARCHIVE) as tar:
        for name, spec in SPEC.items():
            raw = tar.extractfile(name).read()
            assert sha(raw) == spec["sha256"]
            assert (FIGURES/name).read_bytes() == raw
            doc = pymupdf.open(stream=raw, filetype="pdf")
            page = doc[0]
            drawings = page.get_drawings()
            yticks = []
            for index, energy in spec["y_ticks"]:
                a, b = drawings[index]["items"][0][1:3]
                assert abs(a.y-b.y) < 1e-5 and abs(abs(a.x-b.x)-4) < 1e-5
                yticks.append(dict(path_index=index, E_MeV=energy, y_pt=a.y))
            # Calibrate from the two outer labeled ticks; remaining ticks validate
            # linearity. No regression to model or marker energies.
            y0, y1 = yticks[0], yticks[-1]
            slope = (y1["E_MeV"]-y0["E_MeV"])/(y1["y_pt"]-y0["y_pt"])
            intercept = y0["E_MeV"]-slope*y0["y_pt"]
            tick_error_keV = max(abs(1000*(intercept+slope*t["y_pt"]-t["E_MeV"])) for t in yticks)
            assert tick_error_keV < .002
            xticks = []
            for index, number in spec["x_ticks"]:
                a, b = drawings[index]["items"][0][1:3]
                assert abs(a.x-b.x) < 1e-5 and abs(abs(a.y-b.y)-4) < 1e-5
                xticks.append(dict(path_index=index, neutron_number=number, x_pt=a.x))
            xslope = (xticks[-1]["neutron_number"]-xticks[0]["neutron_number"])/(xticks[-1]["x_pt"]-xticks[0]["x_pt"])
            xintercept = xticks[0]["neutron_number"]-xslope*xticks[0]["x_pt"]
            points = []
            for label, tj, ordinal, line_index, marker_index, kind in spec["series"]:
                line = drawings[line_index]
                marker = drawings[marker_index]
                assert marker["fill"] == line["color"]
                anchor, bbox, centroid, method = marker_anchor(marker, kind)
                graph_point = line_start(line)
                disagreement = float(np.linalg.norm(anchor-graph_point))
                assert disagreement < 2e-5
                number = float(xintercept+xslope*anchor[0])
                assert abs(number-spec["target_N"]) < 2e-6
                e = float(1000*(intercept+slope*anchor[1]))
                # The encoded energies lie on a 1-keV grid, within extraction
                # arithmetic precision. This does not prove author rounding mode.
                grid_error = abs(e-round(e))
                assert grid_error < .002
                points.append(dict(
                    state=label, two_J=tj, ordinal=ordinal,
                    path_index=marker_index, connecting_path_index=line_index,
                    fill_rgb=list(marker["fill"]), marker_kind=kind,
                    marker_anchor_pt=anchor.tolist(),
                    connecting_path_point_pt=graph_point.tolist(),
                    marker_vs_line_distance_pt=disagreement,
                    anchor_method=method, bounding_box_midpoint_pt=bbox.tolist(),
                    vertex_mean_pt=None if centroid is None else centroid.tolist(),
                    encoded_neutron_number=number, recovered_energy_keV=e,
                    reported_plot_grid_energy_keV=round(e),
                    distance_to_1keV_grid_keV=grid_error,
                    bounding_box_energy_bias_keV=float(1000*slope*(bbox[1]-anchor[1])),
                    vertex_mean_energy_bias_keV=None if centroid is None else float(1000*slope*(centroid[1]-anchor[1])),
                ))
            records.append(dict(
                figure=name, sha256=sha(raw), locator=spec["locator"],
                pdf_page_size_pt=list(page.rect), target_N=spec["target_N"],
                axis=dict(y_ticks=yticks, x_ticks=xticks,
                          energy_MeV_equals_intercept_plus_slope_y=dict(intercept=intercept,slope=slope),
                          N_equals_intercept_plus_slope_x=dict(intercept=xintercept,slope=xslope),
                          other_y_tick_max_residual_keV=tick_error_keV),
                points=points,
            ))
    return {
        "review_date_utc": datetime.now(timezone.utc).isoformat(),
        "run_directory_date_retained": "20261105",
        "archive": str(ARCHIVE.relative_to(ROOT)),
        "archive_sha256": EXPECTED_ARCHIVE,
        "independence": "No prediction, model solve, experimental energies or parent marker JSON read. Tick/legend assignments from original figures. Frozen before case comparison.",
        "precision": {
            "numeric_extraction_acceptance_keV": .002,
            "observed_plot_energy_grid_keV": 1,
            "round_to_nearest_sensitivity_half_width_keV": .5,
            "boundary": "The half-keV range is a declared rounding sensitivity, not an author error bar or confidence interval. Original numerical table and plotting rounding rule are unavailable.",
        },
        "figures": records,
    }


if __name__ == "__main__":
    result = extract()
    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT/"source-points-frozen.json"
    with target.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print("SOURCE-ONLY FROZEN SHA256", sha(target.read_bytes()))
    for figure in result["figures"]:
        print(figure["locator"])
        print("axis", figure["axis"]["energy_MeV_equals_intercept_plus_slope_y"])
        for point in figure["points"]:
            print(point["state"], point["recovered_energy_keV"],
                  "bbox bias", point["bounding_box_energy_bias_keV"],
                  "vertex-mean bias", point["vertex_mean_energy_bias_keV"])
