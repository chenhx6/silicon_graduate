#!/usr/bin/env python3
"""Printed Lv2019 line identities and conditional same-parent algebra.

No event analysis, covariance, confidence interval, or scientific certification.
Run from the Wiki root. Inputs are explicit transcriptions, not OCR inferences.
"""
import json
from pathlib import Path


def calculate():
    # Lv2019 arXiv1907.12809v1, pp.9-10 Table I, Fig.1 on p.3.
    d5 = {27: 3111.0, 29: 3358.9, 31: 3650.0, 33: 4008.2, 35: 4414.5}
    d6 = {27: 3609.0, 29: 3782.0, 31: 4007.8, 33: 4290.2,
          35: 4599.6, 37: 4971.2, 39: 5411.6}
    lines = [
        (31, "D5", 27, 896.8, .79, "E2"),
        (33, "D5", 29, 931.3, .50, "E2"),
        (35, "D5", 31, 949.6, .69, "E2"),
        (37, "D5", 33, 963.0, .53, "E2"),
        (35, "D6", 31, 591.8, .60, None),
        (37, "D6", 33, 681.0, .55, None),
        (39, "D6", 35, 812.0, .18, None),
    ]
    rows = []
    for twice_i, final_band, twice_f, energy, intensity, multipole in lines:
        final_energy = (d5 if final_band == "D5" else d6)[twice_f]
        rows.append({
            "initial_band": "D6", "twice_initial_spin": twice_i,
            "final_band": final_band, "twice_final_spin": twice_f,
            "initial_level_keV": d6[twice_i], "final_level_keV": final_energy,
            "gamma_keV": energy, "relative_Igamma": intensity,
            "printed_multipolarity": multipole,
            "energy_closure_residual_keV": d6[twice_i]-final_energy-energy,
            "locator": "LV19 arxiv v1 PDF pp.9-10 Table I; p.3 Fig.1",
        })
    # Same-parent D6 31/2: explicit relative photon intensities, not branches.
    ein, eout_mixed, eout_e2 = 225.8, 648.9, 896.8
    iin, iout_mixed, iout_e2 = 3.8, 1.8, .79
    return {
        "source": "10.1103/PhysRevC.100.024314; arxiv1907.12809v1",
        "scope": "printed line identities, energy closure, conditional central algebra only",
        "line_rows": rows,
        "same_parent_31over2": {
            "level_keV": 4007.8,
            "relative_photon_I_896over225": iout_e2/iin,
            "E2_coefficient": iout_e2/iin*(ein/eout_e2)**5,
            "E2_formula": "B(E2,896.8)/B(E2 component,225.8) = coefficient/f_E2(225.8)",
            "M1_coefficient": iout_mixed/iin*(ein/eout_mixed)**3,
            "M1_formula": "B(M1,648.9)/B(M1,225.8) = coefficient*(1+delta225^2)/(1+delta649^2)",
            "assumptions": ["matching parent and line identities", "photon-intensity convention",
                            "mixed lines restricted to M1/E2", "896.8 treated as assigned E2",
                            "common intensity normalization cancels, but other response errors do not"],
            "missing": ["actual mixing ratios", "gate/response compatibility", "joint covariance"],
        },
        "table_boundaries": {
            "31over2_and_33over2_D6_inband_DeltaI2_rows": "not listed in this Table I; not a global non-observation claim",
            "591point8_681_812_multipolarity_cells": "blank; not new measured pure-E2 assignments",
            "934point9_966point3_under_D6": "same parent energies and values also appear under D5; Fig.1 does not identify these as extra D6 parents",
            "998point1_line": {"printed_parent_keV": 5412.6,
                               "other_D6_39over2_parent_keV": 5411.6,
                               "printed_gamma_keV": 998.1,
                               "using_other_parent_residual_keV": 5411.6-d5[35]-998.1},
        },
        "actual_absolute_B": None,
        "experimental_CI": None,
        "original_MU07_branch_binding": None,
        "scientific_certification": False,
    }


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    output = root / "outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/followup-line-contract-052.json"
    result = calculate()
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"output": str(output.relative_to(root)),
                      "central_energy_closures": len(result["line_rows"]),
                      "scope": result["scope"]}, ensure_ascii=False))
