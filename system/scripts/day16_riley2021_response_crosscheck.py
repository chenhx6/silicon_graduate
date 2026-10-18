#!/usr/bin/env python3
"""Cross-check the published grid, current passive-layer input and kinematics."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.contract.read_text())
    assert cfg["identity"] == "RILEY2021-SOURCE-RESPONSE-CROSSCHECK-01"
    for key in ["PDF", "source_asolid", "source_parser", "geometry_doc"]:
        assert sha(Path(cfg[key])) == cfg[key+"_sha256"]
    counts, total = {}, 1
    for name, row in cfg["table1"].items():
        intervals = (Fraction(row["max"])-Fraction(row["min"]))/Fraction(row["step"])
        assert intervals.denominator == 1
        counts[name] = int(intervals)+1
        total *= counts[name]
    assert total == cfg["paper_reported_grid_points"]
    doc = Path(cfg["geometry_doc"]).read_text()
    source = Path(cfg["source_parser"]).read_text()
    assert "holeL    thickB   thickC   capS   capT   thickO" in doc
    assert "usePassive         = true;" in source
    assert "pPg->passThick1 = ((G4double)y) * mm;" in source
    assert "pPg->passThick2 = ((G4double)z) * mm;" in source
    assert "pPg->passThick3 = ((G4double)Z) * mm;" in source
    shape_rows = []
    for line_number, line in enumerate(Path(cfg["source_asolid"]).read_text().splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        values = line.split()
        assert len(values) == 9
        shape, sides, record = map(int, values[:3])
        if sides == 0 and record == 1:
            hole, back, coaxial, space, capsule, outer = map(Fraction, values[3:])
            paper_ii = list(map(Fraction, cfg["table2_coaxial_back_outer_mm"]["array_II"]))
            shape_rows.append({"shape": shape, "source_line": line_number,
                "coaxial_back_outer_mm": list(map(float, [coaxial, back, outer])),
                "matches_paper_array_II_tuple": [coaxial, back, outer] == paper_ii,
                "hole_front_depth_mm": float(hole), "capsule_spacing_mm": float(space),
                "capsule_thickness_mm": float(capsule)})
    assert len(shape_rows) == 2 and all(r["matches_paper_array_II_tuple"] for r in shape_rows)
    first = list(map(Fraction, cfg["table2_coaxial_back_outer_mm"]["array_I"]))
    second = list(map(Fraction, cfg["table2_coaxial_back_outer_mm"]["array_II"]))
    me = float(cfg["electron_rest_energy_keV"])
    kinematics = []
    for energy in cfg["reported_gamma_labels_keV"]:
        backscatter = energy/(1+2*energy/me)
        assert 0 < backscatter < min(energy, me/2)
        kinematics.append({"incident_gamma_keV": energy,
            "backscattered_photon_180deg_keV": backscatter,
            "Compton_edge_recoil_electron_keV": energy-backscatter,
            "d_backscatter_d_incident": 1/(1+2*energy/me)**2})
    result = {"identity": cfg["identity"], "contract_sha256": sha(args.contract),
        "script_sha256": sha(Path(__file__)), "inclusive_grid_axis_counts": counts,
        "inclusive_grid_total": total, "paper_count_matches": True,
        "nominal_energy_grid_combinations": total*cfg["energies_per_grid_point"],
        "number_of_independent_experiments_from_grid": None,
        "table2_II_over_I_ratios_coaxial_back_outer": [float(b/a) for a, b in zip(first, second)],
        "actual_asolid_shapes": shape_rows, "current_default_passive_layers_enabled": True,
        "current_array_is_paper_12quad_or_original_producer": False,
        "free_electron_Compton_kinematics": kinematics,
        "backscatter_difference_for_paper_1172_1173_labels_keV":
            kinematics[1]["backscattered_photon_180deg_keV"]-kinematics[0]["backscattered_photon_180deg_keV"],
        "source_inputs_after_analysis_unchanged": all(sha(Path(cfg[k])) == cfg[k+"_sha256"]
                                                     for k in ["PDF", "source_asolid", "source_parser", "geometry_doc"]),
        "figure_counts_digitized": False, "new_experimental_fit_Q_or_CI": False}
    assert result["source_inputs_after_analysis_unchanged"]
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")
    print(json.dumps(result, indent=2, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
