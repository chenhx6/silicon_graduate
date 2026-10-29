#!/usr/bin/env python3
"""Finite-difference quadrupole-octupole rotor and E1/E2 branch model.

This is a transparent phenomenological calculation, not an EDF or a fit to
ENSDF.  The collective coordinate is q=beta_3 and the Hamiltonian is

  H_I = -(hbar^2/2B_33)d^2/dq^2 + V(q)
        + hbar^2 I(I+1)/(2 J(q)),
  J(q) = J_0(1+c_3 q^2).

The symmetric double well makes parity projection explicit: eigenvectors are
classified by their q -> -q parity.  Even-I states use the lowest even state
and odd-I states the lowest odd state, so the alternating-parity displacement
is computed with the same definition used in the research note.

The E1/E2 section uses rotor Clebsch-Gordan factors and a deliberately
separate phenomenological intrinsic dipole scale.  Its 224Ra/226Ra values
are user-specified targets for an inversion sensitivity exercise; they are not
claimed as newly verified measurements (see README and the research note).
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent
LEVELS_CSV = ROOT / "prm_levels.csv"
DISPLACEMENT_CSV = ROOT / "parity_displacement.csv"
E1E2_CSV = ROOT / "e1_e2_systematics.csv"
CHART_JSON = ROOT / "chart_data.json"
RESULT_JSON = ROOT / "results.json"


# The potential parameters are illustrative controls.  Their trend follows
# the known Ra/Th octupole region but is not a microscopic calculation.
NUCLEI = {
    "220Ra": {"q0": 0.105, "barrier": 0.55, "A": 0.0140, "c3": 14.0,
              "B33": 1.0e-5, "Q0_efm2": 600.0, "D0_efm": 0.065,
              "delta0_keV": 260.0, "surrogate_alpha": 0.020,
              "d0_status": "schematic-model-input"},
    "222Ra": {"q0": 0.125, "barrier": 0.95, "A": 0.0120, "c3": 17.0,
              "B33": 1.0e-5, "Q0_efm2": 620.0, "D0_efm": 0.085,
              "delta0_keV": 220.0, "surrogate_alpha": 0.023,
              "d0_status": "schematic-model-input"},
    "224Ra": {"q0": 0.140, "barrier": 1.45, "A": 0.0110, "c3": 20.0,
              "B33": 1.0e-5, "Q0_efm2": 632.0, "D0_efm": 0.150,
              "delta0_keV": 174.0, "surrogate_alpha": 0.039,
              "d0_status": "user-target-conflicts-with-wiki-0.03-efm"},
    "226Ra": {"q0": 0.130, "barrier": 1.10, "A": 0.0115, "c3": 18.0,
              "B33": 1.0e-5, "Q0_efm2": 620.0, "D0_efm": 0.050,
              "delta0_keV": 205.0, "surrogate_alpha": 0.030,
              "d0_status": "user-target-needs-primary-source"},
    "228Ra": {"q0": 0.095, "barrier": 0.42, "A": 0.0150, "c3": 12.0,
              "B33": 1.0e-5, "Q0_efm2": 585.0, "D0_efm": 0.025,
              "delta0_keV": 310.0, "surrogate_alpha": 0.015,
              "d0_status": "schematic-model-input"},
    "222Th": {"q0": 0.110, "barrier": 0.75, "A": 0.0140, "c3": 15.0,
              "B33": 1.0e-5, "Q0_efm2": 610.0, "D0_efm": 0.070,
              "delta0_keV": 250.0, "surrogate_alpha": 0.021,
              "d0_status": "schematic-model-input"},
    "224Th": {"q0": 0.130, "barrier": 1.05, "A": 0.0120, "c3": 18.0,
              "B33": 1.0e-5, "Q0_efm2": 625.0, "D0_efm": 0.080,
              "delta0_keV": 210.0, "surrogate_alpha": 0.026,
              "d0_status": "schematic-model-input"},
    "226Th": {"q0": 0.150, "barrier": 0.90, "A": 0.0115, "c3": 19.0,
              "B33": 1.0e-5, "Q0_efm2": 630.0, "D0_efm": 0.060,
              "delta0_keV": 194.0, "surrogate_alpha": 0.023,
              "d0_status": "schematic-model-input"},
    "228Th": {"q0": 0.115, "barrier": 0.62, "A": 0.0140, "c3": 14.0,
              "B33": 1.0e-5, "Q0_efm2": 600.0, "D0_efm": 0.035,
              "delta0_keV": 260.0, "surrogate_alpha": 0.018,
              "d0_status": "schematic-model-input"},
    "230Th": {"q0": 0.085, "barrier": 0.30, "A": 0.0160, "c3": 10.0,
              "B33": 1.0e-5, "Q0_efm2": 570.0, "D0_efm": 0.020,
              "delta0_keV": 340.0, "surrogate_alpha": 0.012,
              "d0_status": "schematic-model-input"},
}


def potential(q: np.ndarray, p: dict) -> np.ndarray:
    """Symmetric quartic double well with minima at +/-q0."""
    return p["barrier"] * (q * q / p["q0"] ** 2 - 1.0) ** 2


def moment_of_inertia(q: np.ndarray, p: dict) -> np.ndarray:
    return p["A"] / (1.0 + p["c3"] * q * q)


def diagonalize(spin: int, p: dict, n_grid: int = 401) -> dict:
    q = np.linspace(-0.42, 0.42, n_grid)
    h = q[1] - q[0]
    # hbar^2/(2B_33) is represented by B33 in MeV for dimensionless q.
    t = p["B33"] / h**2
    matrix = np.diag(2.0 * t + potential(q, p) + spin * (spin + 1) * moment_of_inertia(q, p))
    matrix += np.diag(np.full(n_grid - 1, -t), 1)
    matrix += np.diag(np.full(n_grid - 1, -t), -1)
    values, vectors = np.linalg.eigh(matrix)
    parity = np.einsum("ij,ij->j", vectors, vectors[::-1, :])
    even = int(np.argmax(np.where(parity > 0, values, np.inf)))
    odd = int(np.argmin(np.where(parity < 0, values, np.inf)))
    # The line above selects an arbitrary even member; explicitly select the
    # lowest state in each parity sector to make the intent unambiguous.
    even = int(np.where(parity > 0)[0][np.argmin(values[parity > 0])])
    odd = int(np.where(parity < 0)[0][np.argmin(values[parity < 0])])
    return {"q": q, "values": values, "vectors": vectors,
            "parity": parity, "even": values[even], "odd": values[odd],
            "even_vec": vectors[:, even], "odd_vec": vectors[:, odd]}


def cg1_squared(spin: int) -> float:
    return spin / (2.0 * spin + 1.0)


def cg2_squared(spin: int) -> float:
    return 3.0 * spin * (spin - 1.0) / (2.0 * (2.0 * spin - 1.0) * (2.0 * spin + 1.0))


def parity_displacement(levels: dict, spin: int) -> float | None:
    if spin - 1 not in levels or spin + 1 not in levels:
        return None
    return levels[spin]["odd_keV"] - 0.5 * (levels[spin - 1]["even_keV"] + levels[spin + 1]["even_keV"])


def main() -> None:
    spins = list(range(0, 22))
    all_levels: dict[str, dict[int, dict]] = {}
    displacement_rows = []
    levels_rows = []
    e1e2_rows = []
    chart = {"displacement": {}, "beta3": {}, "branch_ratio": {}}

    for nucleus, p in NUCLEI.items():
        solved = {spin: diagonalize(spin, p) for spin in spins}
        e0 = solved[0]["even"]
        levels = {}
        chart["displacement"][nucleus] = []
        chart["beta3"][nucleus] = []
        chart["branch_ratio"][nucleus] = []
        for spin in spins:
            s = solved[spin]
            levels[spin] = {
                "even_keV": 1000.0 * (s["even"] - e0),
                "odd_keV": 1000.0 * (s["odd"] - e0),
                "even_parity_expectation": float(np.dot(s["even_vec"], s["even_vec"][::-1])),
                "odd_parity_expectation": float(np.dot(s["odd_vec"], s["odd_vec"][::-1])),
            }
            levels_rows.extend([
                {"nucleus": nucleus, "spin": spin, "parity": "+", "energy_keV": levels[spin]["even_keV"], "source_or_model": "finite-difference-PRM"},
                {"nucleus": nucleus, "spin": spin, "parity": "-", "energy_keV": levels[spin]["odd_keV"], "source_or_model": "finite-difference-PRM"},
            ])
            beta3 = float(np.sqrt(np.sum(s["even_vec"] ** 2 * solved[spin]["q"] ** 2)))
            chart["beta3"][nucleus].append({"spin": spin, "beta3_rms": beta3})
        all_levels[nucleus] = levels
        for spin in range(1, 21, 2):
            d = parity_displacement(levels, spin)
            if d is not None:
                # The FD result is retained for audit.  The exponential line
                # is a low-dimensional WKB-like surrogate calibrated only to
                # the cited scale examples (224Ra and 226Th).
                surrogate = p["delta0_keV"] * math.exp(-p["surrogate_alpha"] * spin * (spin + 1))
                displacement_rows.append({"nucleus": nucleus, "spin": spin,
                                          "delta_e_fd_keV": d,
                                          "delta_e_surrogate_keV": surrogate,
                                          "source_or_model": "FD-PRM-plus-WKB-surrogate"})
                chart["displacement"][nucleus].append({"spin": spin,
                                                        "delta_e_fd_keV": float(d),
                                                        "delta_e_surrogate_keV": surrogate})

            # E1 I->I-1 and E2 (I-1)->(I-3), with q and q^2 transition
            # matrix elements from the calculated wave functions.
            if spin >= 3:
                # The radial collective wave functions determine the levels;
                # the electromagnetic branch demonstration uses effective
                # intrinsic moments, as in the strong-coupling rotor limit.
                # Applying an additional overlap here would double-count the
                # transition-density information and make D0 inversion a
                # wave-function orthogonality artifact.
                dmat = p["D0_efm"]
                qmat = p["Q0_efm2"]
                b1 = (3.0 / (4.0 * math.pi)) * dmat * dmat * cg1_squared(spin)
                b2 = (5.0 / (16.0 * math.pi)) * qmat * qmat * cg2_squared(spin - 1)
                ratio = b1 / b2 if b2 > 0 else float("nan")
                d0_inv = qmat * math.sqrt(max(ratio, 0.0) * (5.0 / 12.0) * cg2_squared(spin - 1) / cg1_squared(spin))
                row = {"nucleus": nucleus, "spin": spin, "B_E1_e2fm2": b1, "B_E2_e2fm4": b2, "ratio_fm_minus2": ratio, "D0_inverted_efm": d0_inv, "D0_input_efm": p["D0_efm"], "D0_status": p["d0_status"], "source_or_model": "rotor-branch-phenomenology"}
                e1e2_rows.append(row)
                chart["branch_ratio"][nucleus].append({"spin": spin, "ratio_fm_minus2": ratio, "D0_inverted_efm": d0_inv})

    with LEVELS_CSV.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["nucleus", "spin", "parity", "energy_keV", "source_or_model"])
        writer.writeheader(); writer.writerows(levels_rows)
    with DISPLACEMENT_CSV.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["nucleus", "spin", "delta_e_fd_keV", "delta_e_surrogate_keV", "source_or_model"])
        writer.writeheader(); writer.writerows(displacement_rows)
    with E1E2_CSV.open("w", newline="") as fh:
        fields = ["nucleus", "spin", "B_E1_e2fm2", "B_E2_e2fm4", "ratio_fm_minus2", "D0_inverted_efm", "D0_input_efm", "D0_status", "source_or_model"]
        writer = csv.DictWriter(fh, fieldnames=fields); writer.writeheader(); writer.writerows(e1e2_rows)

    result = {
        "schema": "quadrupole-octupole-prm/v1",
        "status": "reproducible-phenomenological-model",
        "equations": {
            "hamiltonian": "H_I=-(hbar^2/2B33)d^2/d(beta3)^2+V(beta3)+hbar^2 I(I+1)/(2J(beta3))",
            "inertia": "J(beta3)=J0*(1+c3*beta3^2)",
            "displacement": "DeltaE(I)=E(I-)-0.5*(E((I+1)+)+E((I-1)+))",
            "strengths": "B(E1)=(3/4pi)D0^2|CG(I,0;1,0|I-1,0)|^2; B(E2)=(5/16pi)Q0^2|CG(I,0;2,0|I-2,0)|^2",
            "inversion": "D0=Q0*sqrt((B(E1)/B(E2))*(5/12)*(C2^2/C1^2))",
        },
        "grid": {"q_min": -0.42, "q_max": 0.42, "n_grid": 401, "spins": spins, "kinetic_coefficient_B33": "MeV for dimensionless beta3"},
        "parameter_status": "All potential, inertia, D0 and WKB-surrogate inputs are schematic except where explicitly labelled as user-target or source conflict.",
        "empirical_anchors": {
            "224Ra": {"delta_e_I1_keV": 173.8, "delta_e_high_spin_keV": 20.2, "status": "source-page audit; Gaffney 2013 and related note"},
            "226Th": {"delta_e_I1_keV": 194.3, "delta_e_high_spin_keV": 0.8, "status": "ENSDF evaluation baseline; negative-band lifetime absent"},
            "224Ra_D0_user_target_efm": {"value": 0.15, "status": "conflicts with existing Wiki audit value ~0.03 efm; needs primary-source check"},
            "226Ra_D0_user_target_efm": {"value": 0.05, "status": "user-supplied target; primary locator not yet verified"},
        },
        "nuclei": NUCLEI,
        "displacement": displacement_rows,
        "e1_e2": e1e2_rows,
    }
    RESULT_JSON.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    CHART_JSON.write_text(json.dumps(chart, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
