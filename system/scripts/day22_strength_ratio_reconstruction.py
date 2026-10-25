#!/usr/bin/env python3
"""Reconstruct printed central strength ratios from line-bound photon inputs.

No raw-event refit, new uncertainty interval, cross-campaign averaging, or
independent evidence is produced. E2 comparisons assume the denominator
transition is pure E2. Intensities are efficiency-corrected photon yields;
do not multiply an additional internal-conversion ratio into this formula.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def e2_fraction(delta: float) -> float:
    return delta**2 / (1 + delta**2)


def e2_ratio(photon_ratio: float, numerator_keV: float, denominator_keV: float, delta: float) -> float:
    return photon_ratio * (denominator_keV / numerator_keV)**5 * e2_fraction(delta)


def m1_over_e2(r_e2: float, delta: float, numerator_keV: float) -> float:
    # LKH82 Eq2.6: delta=0.835 E(MeV) RME(E2)[eb]/RME(M1)[mu_N].
    return (0.835 * numerator_keV / 1000)**2 * r_e2 / delta**2


def reconstruct_energy_curve():
    # L22 SI p5 Table1. These are printed excitation energies, not digitized
    # theoretical curves. The I=33/2 side-band assignment is tentative.
    yrast = {7.5: 730.6, 9.5: 1390.8, 11.5: 2245.0,
             13.5: 3245.0, 15.5: 4320.6, 17.5: 5164.7}
    side = {8.5: 1477.9, 10.5: 2203.9, 12.5: 3000.3,
            14.5: 3955.2, 16.5: 5067.2}
    rows = []
    for spin, energy in side.items():
        average = (yrast[spin - 1] + yrast[spin + 1]) / 2
        rows.append({"I": spin, "side_energy_keV": energy,
                     "yrast_lower_energy_keV": yrast[spin - 1],
                     "yrast_upper_energy_keV": yrast[spin + 1],
                     "Ewob_neighbor_average_keV": energy - average,
                     "side_spin_tentative": spin == 16.5})
    # The neighboring-level average of A I(I+1) differs from same-I energy
    # by A. A spline and this estimator must not be silently interchanged.
    coefficient = 30.0  # arbitrary analytic control, keV
    spin = 10.5
    rotor = lambda i: coefficient * i * (i + 1)
    curvature_offset = (rotor(spin - 1) + rotor(spin + 1)) / 2 - rotor(spin)
    assert abs(curvature_offset - coefficient) < 1e-10
    return {
        "input_locator": "L22 SI p5 Table1, bands1 and3",
        "definition_locator": "M15 printed082501-3 Eq1",
        "rows": rows,
        "analytic_neighbor_average_curvature_offset_keV": curvature_offset,
        "boundaries": ["These computed central values are not a new measurement or a confidence interval",
                       "A downward curve is retained in the same dataset interpreted as TiP; energy slope alone does not resolve the interpretation",
                       "F14 uses a spline in its benchmark figure; do not silently equate that estimator with this neighboring-level average"],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    je_branches = []
    for delta in [-3.60, -0.19]:
        r = e2_ratio(0.14, 476, 627, delta)
        je_branches.append({"delta": delta, "fE2": e2_fraction(delta),
                            "BE2_476_over_627": r,
                            "BM1_476_over_BE2_627_muN2_per_e2b2": m1_over_e2(r, delta, 476)})
    lv_813_ratio = e2_ratio(6.4 / 3.7, 813.2, 726.0, -0.37)
    lv_747_ratio = e2_ratio(9.4 / 0.4, 747.3, 526.2, -0.47)
    matta_813_m1 = m1_over_e2(0.843, -1.54, 812.8)
    counterfactual = 0.843 * e2_fraction(-0.37) / e2_fraction(-1.54)
    result = {
        "scope": "same-parent, line-bound central-value reconstructions; not experimental CI",
        "formulas": {"fE2": "delta^2/(1+delta^2)",
                     "BE2a_over_BE2b": "I_gamma(a)/I_gamma(b)*(Eb/Ea)^5*fE2(a), b assumed E2",
                     "BM1a_over_BE2b": "(0.835*Ea_MeV)^2*BE2a/BE2b/delta_a^2"},
        "JE02": {
            "locator": "142503-2 Fig1; 142503-3 TableII; 142503-4 discussion",
            "parent": "TSD3 45/2+", "numerator": "476 keV -> TSD2 43/2+",
            "denominator": "627 keV -> TSD3 41/2+",
            "photon_ratio_printed": "0.14 +/-0.04", "branches": je_branches,
            "published_BE2_ratios": ["0.51 +/-0.13", "0.019 +0.024/-0.017"],
            "large_branch_over_small_central": je_branches[0]["BE2_476_over_627"] / je_branches[1]["BE2_476_over_627"],
            "polarization": "not obtained for 476 keV; model/band similarity selected large branch",
            "phonon_factor_from_published_ratios": 0.51 / 0.21,
            "phonon_factor_boundary": "different parent spins/denominators; benchmark dependence and Cov not reconstructed",
        },
        "L22_813": {
            "locator": "main p3 Table1 and p5 Fig4(d); SI p5 Table1",
            "parent": "band3 21/2- at 2203.9 keV",
            "numerator": "813.2 keV -> band1 19/2-", "denominator": "726.0 keV -> band3 17/2-",
            "input_photon_intensities": ["6.4(3)", "3.7(3)"], "delta": "-0.37 +0.10/-0.14",
            "reconstructed_BE2out_over_BE2in": lv_813_ratio,
            "reconstructed_BM1out_over_BE2in": m1_over_e2(lv_813_ratio, -0.37, 813.2),
            "published": {"rE2": "0.12(8)", "rM1": "0.4(3)"},
        },
        "L22_747_vs_526": {
            "locator": "main p3 final left-column paragraph; SI p2 Fig1 and p5 Table1",
            "parent": "band3 17/2- at 1477.9 keV",
            "numerator": "747.3 keV -> band1 15/2-", "denominator": "526.2 keV -> band2 13/2-",
            "input_photon_intensities": ["9.4(5)", "0.4(2)"], "delta747": "-0.47 +0.09/-0.22",
            "reconstructed_BE2_747_over_526": lv_747_ratio,
            "published": "0.7 +0.7/-0.5",
            "boundary": "both are interband branches; 526 multipolarity/Rac blank in SI table, E2 denominator assumed",
        },
        "M15_vs_L22": {
            "Matta_813_input": {"delta": -1.54, "rE2": 0.843, "E_keV": 812.8},
            "Matta_BM1out_over_BE2in_reconstructed": matta_813_m1,
            "Matta_BM1out_over_BE2in_printed": "0.164(14)",
            "conditional_fixed_input_rE2_at_Lv_delta": counterfactual,
            "fE2_old_over_new_central": e2_fraction(-1.54) / e2_fraction(-0.37),
            "actual_published_rE2_ratio_central": 0.843 / 0.12,
            "boundary": "5.84 is a fixed-other-input fraction sensitivity, not measured absolute B collapse; datasets differ",
        },
        "M15_asymmetry_descriptive_ratios": {
            "747_A_over_printed_sigma": 0.047 / 0.012,
            "813_A_over_printed_sigma": 0.054 / 0.034,
            "boundary": "descriptive ratios of reported marginal values, not new joint significance or calibrated P",
        },
        "energy_curve": reconstruct_energy_curve(),
        "uncertainty_boundary": "No joint photon-yield/mixing-ratio/calibration Cov; published intervals retained as source results only",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"JE02_branches": je_branches, "Lv813_rE2": lv_813_ratio,
                      "Lv747_over_526": lv_747_ratio, "Matta813_rM1": matta_813_m1,
                      "fixed_input_counterfactual": counterfactual}))


if __name__ == "__main__":
    main()
