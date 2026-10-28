"""Conditional radiative ratios from original2015 Table I; not a new fit."""
import json
import math
from pathlib import Path

ROWS = [
    # I, Ei_keV, E_M1_keV, I_M1, sigma, E_E2_keV, I_E2, sigma
    [15.5, 4292.7, 429.7, 11.0, .3, 762.7, 1.58, .08],
    [16.5, 4704.1, 410.8, 7.60, .24, 840.6, 1.63, .07],
    [17.5, 5028.6, 325.1, 10.83, .25, 735.9, .50, .03],
]


def reconstruct(row, delta=0.):
    spin, excitation, em, im, sim, ee, ie, sie = row
    ratio = .697*(ee/1000)**5/(em/1000)**3*(im/ie)/(1+delta**2)
    # This is only a declared Cov(I_M1,I_E2)=0 intensity-only sensitivity.
    intensity_sigma = ratio*math.hypot(sim/im, sie/ie)
    return {
        "initial_spin": spin, "initial_excitation_keV_as_printed": excitation,
        "M1_gamma_keV": em, "E2_gamma_keV": ee,
        "photon_intensity_ratio": im/ie, "delta_assumed": delta,
        "B_M1_over_B_E2_muN2_per_e2b2": ratio,
        "intensity_only_sigma_if_Cov0": intensity_sigma,
    }


result = {
    "schema_version": 1,
    "inputs": ROWS,
    "source": "Garg2015 original printed054325-2 Table I, not erratum",
    "formula_source": "Paul1991 physicalPDF6 printed609 Eq6; PA91-D25-A005-01",
    "convention": "Radiative photon intensities, pure E2 denominator; .697 assumes MeV and returns muN2/(e2b2). M1 fraction of mixed numerator is 1/(1+delta^2).",
    "central_delta0": [reconstruct(row) for row in ROWS],
    "delta_sensitivity_no_fit": [reconstruct(ROWS[-1], d) for d in [0., .5, 1., 2.]],
    "boundaries": [
        "No measured delta or new multipolarity selection is supplied.",
        "No lifetime or absolute B is inferred.",
        "Cov0 errors exclude shared normalizers, efficiency/energy Cov and model systematics; not a reconstructed experimental CI.",
        "No independent ICC convention for the original producer was recovered; radiative and total branches must not be mixed.",
        "Printed Ei and E_gamma are not silently repaired by energy subtraction.",
        "2019 erratum body remains unacquired; comparison concerns original2015 Fig7 only.",
    ],
}

if __name__ == "__main__":
    Path(__file__).with_suffix(".json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(result,ensure_ascii=False,indent=2))
