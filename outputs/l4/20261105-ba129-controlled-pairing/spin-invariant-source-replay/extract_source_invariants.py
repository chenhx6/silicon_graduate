"""Source-only invariant-figure extraction: never reads kernel/case/probe files.

Tick labels and curve identities were inspected in the original figures.
Use vector coordinates, verify marker anchors against connecting paths, and
freeze the result before model comparison. Existing frozen output is protected.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import tarfile

import numpy as np
import pymupdf

ROOT = Path("/workspace/wiki")
OUT = ROOT/"outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-source-replay"
ARCHIVE = ROOT/"raw/papers/gpt/query/20261105-nomura2017-input-audit/nomura2017-v2-source.tar.gz"
FIGURES = ROOT/"tmp/ba129-controlled-pairing/source-figure-replay"
ARCHIVE_SHA = "f7ed6dc746f50f16169d8796e4d12becd8827eaf4ac2ee4d5f1ff9cd04690faf"

SPEC = [
    dict(member="even.qinvar.pdf",
         sha256="0665941852b4c34202bfbc5c7c1b28ac17149f53a2dd20c8afa87247388dcb23",
         panel="Fig.13(a), core Ba J=0", quantity="beta", units="dimensionless",
         y_ticks=[(24+2*i, .05*i) for i in range(6)],
         x_ticks=[(14+2*i, 72+2*i) for i in range(5)],
         line_path=2, marker_paths=list(range(3,8)), shape="circle", two_J=0,
         neutron_numbers=[72,74,76,78,80]),
    dict(member="even.qinvar.pdf",
         sha256="0665941852b4c34202bfbc5c7c1b28ac17149f53a2dd20c8afa87247388dcb23",
         panel="Fig.13(b), core Ba J=0", quantity="gamma", units="degree",
         y_ticks=[(63+2*i, 5*i) for i in range(7)],
         x_ticks=[(53+2*i, 72+2*i) for i in range(5)],
         line_path=41, marker_paths=list(range(42,47)), shape="circle", two_J=0,
         neutron_numbers=[72,74,76,78,80]),
    dict(member="oddn.qinvar.pdf",
         sha256="9133869676413bc163f2e945e31c2042ce4fd07ccd9f78db36f33b66860081d9",
         panel="Fig.14(a), odd Ba J=11/2", quantity="beta", units="dimensionless",
         y_ticks=[(36+2*i, .1*i) for i in range(6)],
         x_ticks=[(26+2*i, 73+2*i) for i in range(5)],
         line_path=20, marker_paths=[21], shape="triangle_down", two_J=11,
         neutron_numbers=[73]),
    dict(member="oddn.qinvar.pdf",
         sha256="9133869676413bc163f2e945e31c2042ce4fd07ccd9f78db36f33b66860081d9",
         panel="Fig.14(c), odd Ba J=11/2", quantity="gamma", units="degree",
         y_ticks=[(87+2*i, 5*i) for i in range(7)],
         x_ticks=[(77+2*i, 73+2*i) for i in range(5)],
         line_path=71, marker_paths=[72], shape="triangle_down", two_J=11,
         neutron_numbers=[73]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def freeze():
    assert sha(ARCHIVE.read_bytes()) == ARCHIVE_SHA
    panels = []
    with tarfile.open(ARCHIVE) as archive:
        for spec in SPEC:
            raw = archive.extractfile(spec["member"]).read()
            assert sha(raw) == spec["sha256"]
            assert raw == (FIGURES/spec["member"]).read_bytes()
            page = pymupdf.open(stream=raw, filetype="pdf")[0]
            drawings = page.get_drawings()
            yticks = []
            for path_index, value in spec["y_ticks"]:
                item = drawings[path_index]["items"][0]
                assert item[0] == "l" and abs(item[1].y-item[2].y) < 1e-6
                yticks.append(dict(path_index=path_index, value=value, y_pt=item[1].y))
            first, last = yticks[0], yticks[-1]
            slope = (last["value"]-first["value"])/(last["y_pt"]-first["y_pt"])
            intercept = first["value"]-slope*first["y_pt"]
            tick_residual = max(abs(intercept+slope*t["y_pt"]-t["value"]) for t in yticks)
            assert tick_residual < (1e-7 if spec["quantity"] == "beta" else 1e-5)
            xticks = []
            for path_index, number in spec["x_ticks"]:
                item = drawings[path_index]["items"][0]
                assert item[0] == "l" and abs(item[1].x-item[2].x) < 1e-6
                xticks.append(dict(path_index=path_index, neutron_number=number, x_pt=item[1].x))
            xslope = (xticks[-1]["neutron_number"]-xticks[0]["neutron_number"])/(xticks[-1]["x_pt"]-xticks[0]["x_pt"])
            xoffset = xticks[0]["neutron_number"]-xslope*xticks[0]["x_pt"]
            line = drawings[spec["line_path"]]
            graph_vertices = [tuple(line["items"][0][1])] + [tuple(x[2]) for x in line["items"]]
            points = []
            for i, (path_index, number) in enumerate(zip(spec["marker_paths"], spec["neutron_numbers"])):
                marker = drawings[path_index]
                assert marker["fill"] == line["color"]
                box = marker["rect"]
                bbox_center = np.array([(box.x0+box.x1)/2, (box.y0+box.y1)/2])
                if spec["shape"] == "circle":
                    assert len(marker["items"]) == 8 and all(t[0] == "c" for t in marker["items"])
                    center = np.mean([tuple(t[1]) for t in marker["items"]], axis=0)
                else:
                    assert len(marker["items"]) == 3 and all(t[0] == "l" for t in marker["items"])
                    center = bbox_center
                graph = np.array(graph_vertices[i])
                difference = float(np.linalg.norm(center-graph))
                # PyMuPDF exposes these transformed coordinates at float32-scale
                # resolution. Repeated independently transformed paths can differ
                # by roughly one coordinate ULP; do not confuse that with a
                # marker-centering or model discrepancy.
                coordinate_tolerance = float(3*np.finfo(np.float32).eps*max(1., float(np.max(abs(graph)))))
                assert difference < coordinate_tolerance
                assert abs(xoffset+xslope*center[0]-number) < 2e-6
                value = float(intercept+slope*center[1])
                points.append(dict(
                    neutron_number=number, isotope=f"{56+number}Ba", two_J=spec["two_J"],
                    marker_path=path_index, connecting_path=spec["line_path"],
                    center_pt=center.tolist(), curve_vertex_pt=graph.tolist(),
                    marker_curve_distance_pt=difference, fill_rgb=list(marker["fill"]),
                    coordinate_acceptance_pt=coordinate_tolerance,
                    marker_shape=spec["shape"], value=value,
                    display_rounded=round(value,5 if spec["quantity"] == "beta" else 3),
                ))
            panels.append(dict(
                member=spec["member"], sha256=spec["sha256"], panel=spec["panel"],
                quantity=spec["quantity"], units=spec["units"], points=points,
                axis=dict(y_ticks=yticks, x_ticks=xticks, y_slope=slope,
                          y_intercept=intercept, x_slope=xslope, x_intercept=xoffset,
                          remaining_tick_max_residual=tick_residual),
            ))
    result = dict(
        schema="nomura-invariant-source-only-v1",
        review_date_declared="2026-11-06",
        container_observed_utc=datetime.now(timezone.utc).isoformat(),
        archive=str(ARCHIVE.relative_to(ROOT)), archive_sha256=ARCHIVE_SHA,
        independence="This extractor reads only source archive/vector figures. No kernel, probe, case, previous marker JSON or target-model parameter is read.",
        precision="Vector coordinate arithmetic, not statistical uncertainty. Report beta to 5 decimals and gamma to 0.001 degree. Source numerical plotting table and rounding rule are unavailable.",
        extraction_history="The initial uniform 2e-5 pt marker/path guard failed on independent coordinate transforms (maximum 3.41197e-5 pt). It was replaced, before any probe read, by three float32 coordinate-resolution units. No axis or marker position was adjusted.",
        panels=panels,
    )
    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT/"source-invariants-frozen.json"
    payload = json.dumps(result, indent=2)+"\n"
    with target.open("x", encoding="utf-8") as stream:
        stream.write(payload)
    print("FROZEN SHA256", sha(target.read_bytes()))
    for panel in panels:
        print(panel["panel"], "axis", panel["axis"]["y_intercept"], panel["axis"]["y_slope"])
        for point in panel["points"]:
            print(point["isotope"],point["two_J"],panel["quantity"],point["value"])


if __name__ == "__main__":
    freeze()
