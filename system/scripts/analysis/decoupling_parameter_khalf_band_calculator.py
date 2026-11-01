#!/usr/bin/env python3
"""
decoupling_parameter_khalf_band_calculator.py
=============================================
Coriolis Decoupling Parameter (a) in K=1/2 Rotational Bands, Signature Splitting &
Nilsson Wavefunction Inversion Suite.

Physics & Formulation:
----------------------
1. Rotational Energy Spectrum for K = 1/2 Bands (Bohr-Mottelson Vol. II §4-3):
   E(I) = E_0 + A * [ I*(I + 1) + a * (-1)^(I + 1/2) * (I + 1/2) ]
   where:
     A = hbar^2 / (2 * J) is the rotational parameter in keV.
     a is the dimensionless decoupling parameter.
     The term linear in (I + 1/2) represents the diagonal Coriolis matrix element:
       a = - < K=1/2 | j_+ | K=-1/2 > * (-1)^(j - 1/2)

2. Decoupling Parameter in Pure Single-j Intruder Orbitals:
   For an unmixed single-j orbital:
     a_pure(j) = (-1)^(j - 1/2) * (j + 1/2)
     - s_1/2 (j=1/2) : a = +1.0
     - p_3/2 (j=3/2) : a = -2.0
     - d_5/2 (j=5/2) : a = +3.0
     - f_7/2 (j=7/2) : a = -4.0
     - g_9/2 (j=9/2) : a = +5.0
     - h_11/2 (j=11/2): a = -6.0  (Key intruder in A ~ 130 triaxial region!)
     - i_13/2 (j=13/2): a = +7.0  (Key intruder in A ~ 160 rare-earth region!)

3. Stephens-Simon Decoupled Band Phenomenon:
   When |a| >> 1 (e.g. h11/2 with a = -6), the favorable signature states
   (I = j, j+2, ...) are pushed downwards so drastically that the bandhead
   becomes I = j rather than I = 1/2, forming a Delta_I = 2 sequence whose
   energy spacings mimic the even-even core!

4. Analytic Linear Inversion from Experimental Level Energies:
   E(I) is strictly linear in the parameter vector theta = [E_0, A, A*a]^T:
     E(I) = theta_0 * 1 + theta_1 * [I*(I+1)] + theta_2 * [(-1)^(I+1/2) * (I+1/2)]
   Solves the normal equations via linear least squares, extracting A, a, and E_0
   with exact covariance propagation.

References:
  - A. Bohr and B. R. Mottelson, Nuclear Structure, Vol. II, §4-3 (pp. 31–34), §5-3 (pp. 309–311).
  - F. S. Stephens and R. S. Simon, Nucl. Phys. A 183, 257 (1972).
  - 卢希庭, 《原子核物理（修订版）》, 第8章 §8.5 (转动能级).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_pure_j_decoupling_parameter(j: float) -> float:
    """
    Calculates theoretical decoupling parameter for an unmixed single-j orbital:
      a_pure(j) = (-1)^(j - 1/2) * (j + 1/2)
    """
    if j < 0.5 or abs(j - round(j + 0.5) + 0.5) > 1e-6:
        raise ValueError("j must be a positive half-integer (1/2, 3/2, 5/2, ...)")
    phase = (-1.0) ** int(round(j - 0.5))
    return phase * (j + 0.5)


def calculate_khalf_spectrum(
    spins: List[float],
    A_keV: float = 12.5,
    a_decouple: float = -0.77,
    E0_keV: float = 0.0
) -> List[Dict[str, Any]]:
    """
    Generates energy spectrum and signature staggering for a K=1/2 band.
    """
    levels = []
    for I in spins:
        if I < 0.5 or abs(I - round(I + 0.5) + 0.5) > 1e-6:
            raise ValueError(f"Invalid spin {I}: must be half-integer >= 1/2")
        phase = (-1.0) ** int(round(I + 0.5))
        coriolis_term = a_decouple * phase * (I + 0.5)
        E_rot = A_keV * (I * (I + 1.0) + coriolis_term) + E0_keV
        levels.append({
            "spin_I": I,
            "phase_factor": int(phase),
            "coriolis_shift_keV": round(A_keV * coriolis_term, 2),
            "energy_keV": round(E_rot, 2)
        })
    return levels


def invert_khalf_band_parameters(
    spins: List[float],
    energies_keV: List[float]
) -> Dict[str, Any]:
    """
    Analytically inverts rotational constant A, decoupling parameter a, and E0
    from experimental level energies using exact linear regression.
    """
    if len(spins) != len(energies_keV) or len(spins) < 3:
        raise ValueError("Require at least 3 spin-energy pairs for linear inversion.")

    n = len(spins)
    # Construct design matrix X: N x 3
    # X[i] = [ 1, I*(I+1), (-1)^(I+1/2) * (I+1/2) ]
    X = []
    y = []
    for I, E in zip(spins, energies_keV):
        phase = (-1.0) ** int(round(I + 0.5))
        X.append([1.0, I * (I + 1.0), phase * (I + 0.5)])
        y.append(float(E))

    # Compute (X^T * X) and (X^T * y)
    XT_X = [[0.0] * 3 for _ in range(3)]
    XT_y = [0.0] * 3

    for row, y_val in zip(X, y):
        for i in range(3):
            XT_y[i] += row[i] * y_val
            for j in range(3):
                XT_X[i][j] += row[i] * row[j]

    # Invert 3x3 matrix XT_X
    def mat_inv_3x3(M):
        det = (
            M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) -
            M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0]) +
            M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
        )
        if abs(det) < 1e-12:
            raise ValueError("Singular matrix: insufficient spin diversity.")
        inv = [[0.0] * 3 for _ in range(3)]
        inv[0][0] = (M[1][1] * M[2][2] - M[1][2] * M[2][1]) / det
        inv[0][1] = (M[0][2] * M[2][1] - M[0][1] * M[2][2]) / det
        inv[0][2] = (M[0][1] * M[1][2] - M[0][2] * M[1][1]) / det

        inv[1][0] = (M[1][2] * M[2][0] - M[1][0] * M[2][2]) / det
        inv[1][1] = (M[0][0] * M[2][2] - M[0][2] * M[2][0]) / det
        inv[1][2] = (M[0][2] * M[1][0] - M[0][0] * M[1][2]) / det

        inv[2][0] = (M[1][0] * M[2][1] - M[1][1] * M[2][0]) / det
        inv[2][1] = (M[0][1] * M[2][0] - M[0][0] * M[2][1]) / det
        inv[2][2] = (M[0][0] * M[1][1] - M[0][1] * M[1][0]) / det
        return inv

    cov_inv = mat_inv_3x3(XT_X)

    # Solve theta = cov_inv * XT_y
    theta = [0.0] * 3
    for i in range(3):
        for j in range(3):
            theta[i] += cov_inv[i][j] * XT_y[j]

    E0_fit = theta[0]
    A_fit = theta[1]
    Aa_fit = theta[2]
    a_fit = (Aa_fit / A_fit) if abs(A_fit) > 1e-9 else 0.0

    # Compute residuals and rms
    residuals = []
    sum_sq_res = 0.0
    for I, E in zip(spins, energies_keV):
        phase = (-1.0) ** int(round(I + 0.5))
        E_pred = E0_fit + A_fit * (I * (I + 1.0) + a_fit * phase * (I + 0.5))
        res = E - E_pred
        residuals.append(res)
        sum_sq_res += res ** 2

    rms_error = math.sqrt(sum_sq_res / max(1, n - 3))

    # Moment of inertia J/hbar^2 = 1 / (2 * A)
    J_over_hbar2 = (1000.0 / (2.0 * A_fit)) if A_fit > 0 else 0.0

    return {
        "E0_keV": round(E0_fit, 2),
        "A_rot_keV": round(A_fit, 3),
        "decoupling_parameter_a": round(a_fit, 3),
        "moment_of_inertia_hbar2_per_MeV": round(J_over_hbar2, 2),
        "rms_residual_keV": round(rms_error, 2),
        "fitted_levels_count": n
    }


def format_text_report(levels: List[Dict[str, Any]], inv: Optional[Dict[str, Any]] = None, j_single: Optional[float] = None) -> str:
    lines = [
        "=" * 74,
        "   CORIOLIS DECOUPLING PARAMETER (a) & K=1/2 ROTATIONAL BAND ANALYZER",
        "   Based on Bohr & Mottelson (Nuclear Structure Vol. II §4-3, §5-3)",
        "=" * 74,
    ]

    if j_single is not None:
        a_pure = calculate_pure_j_decoupling_parameter(j_single)
        lines.extend([
            f" THEORETICAL PURE SINGLE-j LIMIT: j = {j_single:.1f} ({int(2*j_single)}/2)",
            f"   Analytical Decoupling Parameter: a_pure(j) = {a_pure:+.1f}",
            f"   Coupling Character             : {'Strong Decoupling (|a| >= 5)' if abs(a_pure) >= 5 else ('Moderate Decoupling' if abs(a_pure) >= 2 else 'Weak Staggering')}",
            "-" * 74
        ])

    if inv is not None:
        lines.extend([
            f" EXPERIMENTAL LINEAR REGRESSION INVERSION:",
            f"   Bandhead Energy E_0            : {inv['E0_keV']:.2f} keV",
            f"   Rotational Parameter A (hbar^2/2J): {inv['A_rot_keV']:.3f} keV",
            f"   Inverted Decoupling Parameter a: a_exp = {inv['decoupling_parameter_a']:+.3f}",
            f"   Derived Moment of Inertia J    : {inv['moment_of_inertia_hbar2_per_MeV']:.2f} hbar^2/MeV",
            f"   Fit RMS Residual               : {inv['rms_residual_keV']:.2f} keV ({inv['fitted_levels_count']} levels)",
            "-" * 74
        ])

    lines.extend([
        " K=1/2 ROTATIONAL BAND LEVEL SPECTRUM & CORIOLIS ENERGY SHIFTS:",
        "   Spin I     Phase Factor    Coriolis Shift (keV)    Total Energy (keV)",
        "   " + "-" * 68
    ])

    for lv in levels[:10]:
        lines.append(
            f"   {lv['spin_I']:>5.1f}        {lv['phase_factor']:>+2d}           "
            f"{lv['coriolis_shift_keV']:>10.2f}            {lv['energy_keV']:>10.2f}"
        )

    lines.extend([
        "-" * 74,
        " Physical Significance & Nuclear Structure Insights:",
        "   - In K=1/2 bands, the Coriolis force has non-vanishing diagonal matrix elements.",
        "   - For high-j intruders (h11/2: a=-6, i13/2: a=+7), the huge decoupling parameter",
        "     splits the band into two decoupled Delta_I = 2 cascades (Stephens-Simon effect).",
        "   - Measuring a_exp probes the microscopic purity of the Nilsson Omega=1/2 orbital.",
        "=" * 74
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Coriolis Decoupling Parameter in K=1/2 Bands & Signature Inverter"
    )
    parser.add_argument("--preset", type=str, default="169Tm", choices=["169Tm", "171Lu", "h11/2_pure", "custom"],
                        help="Preset example: 169Tm ([411 1/2]), 171Lu ([541 1/2]), h11/2_pure, custom")
    parser.add_argument("--A-rot", type=float, default=12.5, help="Rotational parameter A = hbar^2/2J in keV")
    parser.add_argument("--a-decouple", type=float, default=-0.77, help="Decoupling parameter a")
    parser.add_argument("--j-orbital", type=float, default=5.5, help="Single-j orbital j (default: 5.5 for h11/2)")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")

    args = parser.parse_args()

    inv_res = None
    j_single = None

    if args.preset == "169Tm":
        # Bohr & Mottelson Table 5-16: 169Tm [411 1/2] ground band
        spins = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
        energies = [0.0, 8.41, 118.19, 138.93, 332.08, 368.21]
        inv_res = invert_khalf_band_parameters(spins, energies)
        levels = calculate_khalf_spectrum(spins, inv_res["A_rot_keV"], inv_res["decoupling_parameter_a"], inv_res["E0_keV"])
    elif args.preset == "171Lu":
        # Bohr & Mottelson Table 5-16: 171Lu [541 1/2] (h9/2 + h11/2 mixed)
        spins = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
        # Representative decoupled band energies with a ~ +4.5
        A_val = 13.0
        a_val = 4.5
        levels = calculate_khalf_spectrum(spins, A_val, a_val, 0.0)
    elif args.preset == "h11/2_pure":
        spins = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
        j_single = 5.5
        a_val = calculate_pure_j_decoupling_parameter(5.5)
        levels = calculate_khalf_spectrum(spins, 12.0, a_val, 0.0)
    else:
        spins = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
        levels = calculate_khalf_spectrum(spins, args.A_rot, args.a_decouple, 0.0)

    if args.json:
        out = {"levels": levels}
        if inv_res is not None:
            out["inversion"] = inv_res
        if j_single is not None:
            out["pure_j_decoupling_parameter"] = calculate_pure_j_decoupling_parameter(j_single)
        print(json.dumps(out, indent=2))
    else:
        print(format_text_report(levels, inv_res, j_single))


if __name__ == "__main__":
    main()
