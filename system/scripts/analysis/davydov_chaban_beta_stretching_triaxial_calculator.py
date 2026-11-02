#!/usr/bin/env python3
"""
davydov_chaban_beta_stretching_triaxial_calculator.py
====================================================
Davydov-Chaban Non-Adiabatic Triaxial Rotor Model, Dynamic Beta-Stretching Ratio p = beta / beta_0,
Deformability Parameter mu & Ground/Gamma/Beta Band Energies.

Physics & Formulation:
----------------------
1. Beyond the Rigid Asymmetric Rotor (Davydov & Chaban 1960):
   The Davydov-Filippov (DF) model assumes rigid triaxial shape (fixed beta_0, gamma_0).
   In reality, rotating nuclei undergo centrifugal stretching along the quadrupole deformation beta
   coordinate (beta-vibrational coupling).
   Davydov and Chaban (Nucl. Phys. 20, 499, 1960; Bohr & Mottelson Vol. II §4-2) extended the model
   by including collective beta-vibrations with harmonic restoring potential 0.5 * C * (beta - beta_0)^2.

2. The Deformability / Non-Adiabaticity Parameter mu:
   The coupling between rotation and beta-vibrations is governed by the dimensionless parameter mu:
     mu = (1 / beta_0) * [ hbar^2 / (B * C) ]^(1/4)
     - mu -> 0 : Rigid Davydov-Filippov rotor (no beta-stretching).
     - mu ~ 0.15 - 0.35 : Moderately soft triaxial nucleus (e.g. Ru, Pd, Pt, Ba isotopes).
     - mu >= 0.50 : Extremely beta-soft / transitional nucleus.

3. Equilibrium Stretching Equation & Root p_J:
   The dynamic deformation at spin J is beta(J) = p_J * beta_0, where the stretching factor p_J
   satisfies the fundamental quartic equilibrium equation (Davydov & Chaban Eq. 2.13):
     p^3 * (p - 1.0) = mu^4 * epsilon(J, gamma)
   where epsilon(J, gamma) is the Davydov-Filippov energy factor in units of hbar^2 / (4 * B * beta_0^2).

4. Davydov-Filippov Energy Factors epsilon(J, gamma):
   - For J = 2^+ doublet (yrast 2_1^+ and gamma-bandhead 2_2^+):
       epsilon(2_1^+) = [ 9 - sqrt(81 - 72 * sin^2(3*gamma)) ] / [ 4 * sin^2(3*gamma) ]
       epsilon(2_2^+) = [ 9 + sqrt(81 - 72 * sin^2(3*gamma)) ] / [ 4 * sin^2(3*gamma) ]
   - For J = 3^+ (odd-spin gamma band):
       epsilon(3_1^+) = epsilon(2_1^+) + epsilon(2_2^+) = 18 / [ 4 * sin^2(3*gamma) ]
   - For J = 4^+ (diagonalized from 2x2 asymmetric rotor block).

5. Total Excitation Energies in Davydov-Chaban Model:
   E(J, gamma, mu) = A_scale * [ (epsilon(J, gamma) / p_J^2) + (0.5 / mu^2) * (p_J - 1.0)^2 ]
   where A_scale = hbar^2 / (4 * B * beta_0^2) ~ E(2_1^+) / epsilon(2_1^+).

References:
  - A. S. Davydov and A. A. Chaban, Nucl. Phys. 20, 499 (1960).
  - A. S. Davydov and G. F. Filippov, Nucl. Phys. 8, 237 (1958).
  - A. Bohr and B. R. Mottelson, *Nuclear Structure*, Vol. II, §4-2 (pp. 175–195).
  - 卢希庭, 《原子核物理（修订版）》, 原子能出版社 (2000), 第8章 §8.4.
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def solve_chaban_stretching_parameter_p(mu: float, eps: float) -> float:
    """
    Solves quartic equilibrium equation p^3 * (p - 1) = mu^4 * eps for p >= 1.0.
    """
    if mu <= 1e-4 or eps <= 1e-4:
        return 1.0

    rhs = (mu ** 4) * eps
    from scipy.optimize import brentq

    def f(p_val):
        return (p_val ** 3) * (p_val - 1.0) - rhs

    # Upper bound: p_val cannot exceed 1.0 + 2.0 * sqrt(rhs) + 1.0
    p_upper = 1.0 + 2.0 * math.sqrt(max(rhs, 1e-4)) + 1.0
    return float(brentq(f, 1.0, p_upper))


def calculate_davydov_filippov_epsilon(gamma_deg: float) -> Dict[str, float]:
    """
    Computes dimensionless Davydov-Filippov energy factors epsilon(J, gamma)
    for 2_1+, 2_2+, 3_1+, 4_1+, 4_2+ states.
    """
    if not (0.0 < gamma_deg < 60.0):
        # Fallback for pure axial limits
        gamma_deg = max(0.5, min(59.5, gamma_deg))

    gamma_rad = math.radians(gamma_deg)
    sin3g = math.sin(3.0 * gamma_rad)
    sin3g_sq = sin3g ** 2

    # 2+ doublet
    disc_2 = max(0.0, 81.0 - 72.0 * sin3g_sq)
    eps_2_1 = (9.0 - math.sqrt(disc_2)) / (4.0 * sin3g_sq)
    eps_2_2 = (9.0 + math.sqrt(disc_2)) / (4.0 * sin3g_sq)

    # 3+ state: exactly sum of 2_1+ and 2_2+
    eps_3_1 = 18.0 / (4.0 * sin3g_sq)

    # 4+ doublet from 2x2 matrix:
    # Trace = 30 / sin^2(3g) + 20? Exact formulas:
    # In Davydov-Filippov (1958) Eq. (14):
    # epsilon(4_1, 4_2) = [ 50 - 20*sin^2(3g) +/- 2*sqrt(625 - 600*sin^2(3g) + 100*sin^4(3g)) ] / [ 4*sin^2(3g) ]
    disc_4 = max(0.0, 625.0 - 600.0 * sin3g_sq + 100.0 * (sin3g_sq ** 2))
    eps_4_1 = (50.0 - 20.0 * sin3g_sq - 2.0 * math.sqrt(disc_4)) / (4.0 * sin3g_sq)
    eps_4_2 = (50.0 - 20.0 * sin3g_sq + 2.0 * math.sqrt(disc_4)) / (4.0 * sin3g_sq)

    return {
        "2_1+": eps_2_1,
        "2_2+": eps_2_2,
        "3_1+": eps_3_1,
        "4_1+": eps_4_1,
        "4_2+": eps_4_2
    }


def calculate_davydov_chaban_spectrum(
    E_2plus_keV: float,
    gamma_deg: float = 22.0,
    mu_nonadiabatic: float = 0.25
) -> Dict[str, Any]:
    """
    Computes energy levels and dynamic beta-stretching factors in the Davydov-Chaban model.
    """
    if E_2plus_keV <= 0.0:
        raise ValueError("E(2+) must be strictly positive.")
    if mu_nonadiabatic < 0.0:
        raise ValueError("Deformability parameter mu must be nonnegative.")

    eps_dict = calculate_davydov_filippov_epsilon(gamma_deg)
    eps_2_1 = eps_dict["2_1+"]

    # In Davydov-Chaban, E(2_1+) = A_scale * [ eps_2_1 / p^2 + (0.5/mu^2)*(p - 1)^2 ]
    p_2_1 = solve_chaban_stretching_parameter_p(mu_nonadiabatic, eps_2_1)
    base_bracket_2_1 = (eps_2_1 / (p_2_1 ** 2)) + (0.5 / (max(mu_nonadiabatic, 1e-4) ** 2)) * ((p_2_1 - 1.0) ** 2)
    A_scale_keV = E_2plus_keV / max(base_bracket_2_1, 1e-6)

    levels = []
    for state_name, eps_val in eps_dict.items():
        p_val = solve_chaban_stretching_parameter_p(mu_nonadiabatic, eps_val)
        e_kin_bracket = eps_val / (p_val ** 2)
        e_pot_bracket = (0.5 / (max(mu_nonadiabatic, 1e-4) ** 2)) * ((p_val - 1.0) ** 2)
        total_e_keV = A_scale_keV * (e_kin_bracket + e_pot_bracket)
        stretching_pct = (p_val - 1.0) * 100.0

        levels.append({
            "state": state_name,
            "epsilon_DF": round(eps_val, 4),
            "stretching_factor_p": round(p_val, 4),
            "stretching_pct": round(stretching_pct, 2),
            "energy_keV": round(total_e_keV, 1)
        })

    # Energy ratios
    e_2_1 = [lv["energy_keV"] for lv in levels if lv["state"] == "2_1+"][0]
    e_4_1 = [lv["energy_keV"] for lv in levels if lv["state"] == "4_1+"][0]
    e_2_2 = [lv["energy_keV"] for lv in levels if lv["state"] == "2_2+"][0]

    r_42 = e_4_1 / e_2_1 if e_2_1 > 0 else 0.0
    r_gamma = e_2_2 / e_2_1 if e_2_1 > 0 else 0.0

    return {
        "E_2plus_reference_keV": E_2plus_keV,
        "gamma_deg": gamma_deg,
        "mu_deformability": mu_nonadiabatic,
        "energy_scale_A_keV": round(A_scale_keV, 2),
        "R_4_2_ratio": round(r_42, 3),
        "R_gamma_bandhead_ratio": round(r_gamma, 3),
        "levels": levels
    }


def format_text_report(chaban_res: Dict[str, Any]) -> str:
    lines = [
        "=" * 76,
        "   DAVYDOV-CHABAN NON-ADIABATIC TRIAXIAL ROTOR MODEL SUITE",
        "   Based on Davydov & Chaban (1960) & Bohr-Mottelson Vol. II §4-2",
        "=" * 76,
        f" MODEL PARAMETERS & CORE DEFORMABILITY:",
        f"   E(2_1^+) Reference Energy   : {chaban_res['E_2plus_reference_keV']:.1f} keV",
        f"   Triaxiality Parameter gamma : {chaban_res['gamma_deg']:.1f} deg",
        f"   Non-Adiabaticity mu (beta)  : {chaban_res['mu_deformability']:.3f}  (0.0 = Rigid Davydov-Filippov)",
        f"   Energy Ratio R_4/2          : {chaban_res['R_4_2_ratio']:.3f}  (Rotor: 3.333, Vibrator: 2.000)",
        f"   Gamma-Bandhead Ratio E(2_2)/E(2_1): {chaban_res['R_gamma_bandhead_ratio']:.3f}",
        "-" * 76,
        " SPECTRUM WITH DYNAMIC BETA-STRETCHING FACTOR p = beta / beta_0:",
        "   State       E_total (keV)    epsilon_DF    Stretching p    Delta_beta %",
    ]

    for lv in chaban_res["levels"]:
        lines.append(f"   {lv['state']:<8}    {lv['energy_keV']:10.1f}      {lv['epsilon_DF']:8.4f}       {lv['stretching_factor_p']:7.4f}        {lv['stretching_pct']:+6.2f}%")

    lines.extend([
        "-" * 76,
        " Methodological Significance:",
        "   - p^3*(p - 1) = mu^4 * epsilon dynamically models centrifugal stretching of triaxial shape.",
        "   - Explains simultaneously ground band, gamma-bandhead (2_2+), and odd-spin (3_1+) spacing.",
        "   - In A~130 nuclei (Ba, Ce), mu ~ 0.25 - 0.35 accounts for combined beta- and gamma-softness.",
        "=" * 76
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Davydov-Chaban Non-Adiabatic Triaxial Rotor Calculator"
    )
    parser.add_argument("--E2", type=float, default=237.2, help="E(2_1+) in keV (default: 237.2 for 112Ru)")
    parser.add_argument("--gamma", type=float, default=22.0, help="Triaxiality gamma in deg (default: 22.0 deg)")
    parser.add_argument("--mu", type=float, default=0.28, help="Non-adiabaticity parameter mu (default: 0.28)")
    parser.add_argument("--preset", type=str, default="112Ru_triaxial_chaban",
                        choices=["112Ru_triaxial_chaban", "190Pt_davydov_chaban", "168Er_rigid_chaban"],
                        help="Benchmark preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")

    args = parser.parse_args()

    e2_val = args.E2
    g_val = args.gamma
    mu_val = args.mu

    if args.preset == "112Ru_triaxial_chaban":
        e2_val, g_val, mu_val = 237.2, 22.0, 0.28
    elif args.preset == "190Pt_davydov_chaban":
        e2_val, g_val, mu_val = 295.8, 30.0, 0.32
    elif args.preset == "168Er_rigid_chaban":
        e2_val, g_val, mu_val = 79.8, 12.0, 0.10

    res = calculate_davydov_chaban_spectrum(e2_val, gamma_deg=g_val, mu_nonadiabatic=mu_val)

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res))


if __name__ == "__main__":
    main()
