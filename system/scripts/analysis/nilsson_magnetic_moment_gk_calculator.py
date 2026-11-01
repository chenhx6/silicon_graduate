#!/usr/bin/env python3
"""
nilsson_magnetic_moment_gk_calculator.py
========================================
Single-Particle Nilsson Magnetic Dipole Moment mu, Gyromagnetic Factors (g_K, g_R) &
B(M1)/B(E2) Branching Ratio Inversion Engine.

Physics & Formulation:
----------------------
1. Magnetic Dipole Moment mu in Deformed Odd-A Nuclei:
   mu(I, K) = g_R * I + (g_K - g_R) * [ K^2 / (I + 1) ]  (for K != 1/2)
   Bandhead moment (I = K):
     mu(K) = [ K / (K + 1) ] * (g_R + K * g_K)
   Collective rotational g-factor: g_R ~ Z / A ~ 0.35 - 0.45.

2. Intrinsic Nilsson g_K Factor:
   K * g_K = g_l * Lambda + g_s_eff * Sigma
   where:
     Sigma = Omega - Lambda = +/- 1/2.
     Proton:  g_l = 1.0, g_s_free = +5.586, g_s_eff ~ 0.70 * g_s_free = +3.910.
     Neutron: g_l = 0.0, g_s_free = -3.826, g_s_eff ~ 0.70 * g_s_free = -2.678.

3. K = 1/2 Decoupling Magnetic Term b_0:
   For Omega = 1/2 bands, Coriolis interaction modifies magnetic moment:
     mu(I, 1/2) = g_R * I + [ 0.25 / (I + 1) ] * (g_K - g_R) * [ 1 + (2*I + 1) * (-1)^(I + 0.5) * b_0 ]

4. B(M1) / B(E2) Ratio and Inversion from Branching:
   Theoretical ratio:
     B(M1; I -> I-1) / B(E2; I -> I-2) = (12 / (5 * Q_0^2)) * (g_K - g_R)^2 * [ 1 / (I^2 - 1) ]  (mu_N^2 / e^2 b^2)
   Experimental extraction from in-beam intensities:
     B(M1)/B(E2) = 0.697 * [ E_gamma^5(I->I-2) / E_gamma^3(I->I-1) ] * [ I_gamma(I->I-1) / I_gamma(I->I-2) ] * (1 / (1 + delta^2))
   Inverts |g_K - g_R| directly from experimental data to identify Nilsson orbital!

References:
  - A. Bohr and B. R. Mottelson, Nuclear Structure, Vol. II, Benjamin (1975).
  - K. L. G. Heyde, Basic Ideas and Concepts in Nuclear Physics, IoP (2004).
  - 卢希庭, 《原子核物理（修订版）》, 第4章.
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_nilsson_gk(
    Omega: float,
    Lambda: int,
    A_mass: int,
    Z_charge: int,
    is_neutron: bool = False,
    quenching_factor: float = 0.70
) -> Dict[str, float]:
    """
    Computes theoretical intrinsic g_K factor and collective g_R factor.
    """
    Sigma = round(Omega - float(Lambda), 1)

    # Bare g factors
    if is_neutron:
        g_l = 0.0
        g_s_free = -3.826
    else:
        g_l = 1.0
        g_s_free = +5.586

    g_s_eff = quenching_factor * g_s_free

    # K * g_K = g_l * Lambda + g_s_eff * Sigma
    K = Omega
    K_gK = g_l * float(Lambda) + g_s_eff * Sigma
    g_K = K_gK / max(K, 0.5)

    # Collective rotational g_R ~ Z / A
    g_R = float(Z_charge) / float(A_mass)

    return {
        "Omega_K": K,
        "Lambda": Lambda,
        "Sigma": Sigma,
        "g_l": g_l,
        "g_s_effective": round(g_s_eff, 3),
        "g_K": round(g_K, 4),
        "g_R": round(g_R, 4),
        "g_K_minus_g_R": round(g_K - g_R, 4)
    }


def calculate_magnetic_dipole_moment(
    spin_I: float,
    Omega_K: float,
    g_K: float,
    g_R: float,
    b_0: float = 0.0
) -> float:
    """
    Computes nuclear magnetic dipole moment mu in nuclear magnetons (mu_N).
    """
    if abs(Omega_K - 0.5) < 1e-4:
        # K = 1/2 decoupled formula
        term = (0.25 / (spin_I + 1.0)) * (g_K - g_R) * (1.0 + (2.0 * spin_I + 1.0) * ((-1.0) ** int(round(spin_I + 0.5))) * b_0)
        mu = g_R * spin_I + term
    else:
        # K != 1/2 standard formula
        mu = g_R * spin_I + (g_K - g_R) * ((Omega_K ** 2) / (spin_I + 1.0))

    return round(mu, 3)


def invert_gk_from_bm1_be2(
    spin_I: float,
    E_gamma_cross_keV: float,  # I -> I-2 (E2 crossover)
    E_gamma_step_keV: float,   # I -> I-1 (M1+E2 stopover)
    I_gamma_cross: float,
    I_gamma_step: float,
    Q_0_eb: float = 3.5,
    delta_mix: float = 0.0,
    g_R: float = 0.40
) -> Dict[str, Any]:
    """
    Inverts |g_K - g_R| from measured in-beam crossover to stopover branching ratio.
    """
    e_cross_MeV = E_gamma_cross_keV * 1e-3
    e_step_MeV = E_gamma_step_keV * 1e-3

    # B(M1)/B(E2) experimental:
    # 0.697 * (E_cross^5 / E_step^3) * (I_step / I_cross) * (1 / (1 + delta^2))
    energy_factor = (e_cross_MeV ** 5) / (e_step_MeV ** 3)
    intensity_ratio = I_gamma_step / max(I_gamma_cross, 1e-6)
    delta_corr = 1.0 / (1.0 + delta_mix ** 2)

    bm1_over_be2 = 0.697 * energy_factor * intensity_ratio * delta_corr

    # B(M1)/B(E2) = (12 / (5 * Q0^2)) * (gK - gR)^2 / (I^2 - 1)
    # (gK - gR)^2 = bm1_over_be2 * (5 * Q0^2 / 12) * (I^2 - 1)
    geom = (5.0 * (Q_0_eb ** 2) / 12.0) * (spin_I ** 2 - 1.0)
    gk_minus_gr_sq = bm1_over_be2 * geom
    gk_minus_gr = math.sqrt(max(gk_minus_gr_sq, 0.0))

    # Candidate g_K values
    gk_sol_plus = g_R + gk_minus_gr
    gk_sol_minus = g_R - gk_minus_gr

    return {
        "spin_I": spin_I,
        "B_M1_over_B_E2_exp": round(bm1_over_be2, 4),
        "extracted_abs_gK_minus_gR": round(gk_minus_gr, 4),
        "candidate_gK_positive_branch": round(gk_sol_plus, 4),
        "candidate_gK_negative_branch": round(gk_sol_minus, 4),
        "collective_gR_assumed": g_R
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   NILSSON MAGNETIC MOMENT mu, g_K FACTOR & B(M1)/B(E2) ANALYZER")
    lines.append("=" * 72)

    gk = summary["nilsson_gk"]
    lines.append(f" NILSSON INTRINSIC CONFIGURATION: Omega = {gk['Omega_K']}, Lambda = {gk['Lambda']}, Sigma = {gk['Sigma']}")
    lines.append(f"   Orbital g-factor g_l           : {gk['g_l']}")
    lines.append(f"   Effective Spin g_s (Quenched)  : {gk['g_s_effective']}")
    lines.append(f"   Intrinsic g_K Factor           : {gk['g_K']}")
    lines.append(f"   Collective Rotational g_R      : {gk['g_R']}")
    lines.append(f"   Intrinsic Difference (g_K - g_R): {gk['g_K_minus_g_R']}")
    lines.append("-" * 72)
    lines.append(" MAGNETIC DIPOLE MOMENT mu ACROSS BAND (mu_N):")
    for pt in summary["magnetic_moments"]:
        lines.append(f"   Spin I = {pt['I']:<6.1f} : mu = {pt['mu_muN']:+.3f} mu_N")
    lines.append("-" * 72)

    if "inversion" in summary:
        inv = summary["inversion"]
        lines.append(" IN-BEAM BRANCHING RATIO INVERSION (|g_K - g_R|):")
        lines.append(f"   Spin I                         : {inv['spin_I']} hbar")
        lines.append(f"   Measured B(M1)/B(E2) Ratio     : {inv['B_M1_over_B_E2_exp']} mu_N^2 / (e*b)^2")
        lines.append(f"   Extracted |g_K - g_R|          : {inv['extracted_abs_gK_minus_gR']}")
        lines.append(f"   Candidate g_K Solutions       : {inv['candidate_gK_positive_branch']} or {inv['candidate_gK_negative_branch']}")
        lines.append("-" * 72)

    lines.append(" Physical Significance:")
    lines.append("   - g_K is uniquely determined by single-particle orbital Sigma and Lambda.")
    lines.append("   - Sign of (g_K - g_R) dictates M1/E2 delta mixing ratio sign.")
    lines.append("   - Absolute test of quasiparticle purity in deformed odd-A bands.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Nilsson Magnetic Moment mu, g_K & B(M1)/B(E2) Analyzer."
    )
    parser.add_argument("--omega", type=float, default=2.5, help="Nilsson Omega quantum number (default: 2.5 for 5/2)")
    parser.add_argument("--lambda-val", type=int, default=2, help="Nilsson Lambda quantum number (default: 2)")
    parser.add_argument("-A", "--mass", type=int, default=131, help="Mass number A (default: 131)")
    parser.add_argument("-Z", "--charge", type=int, default=56, help="Charge number Z (default: 56 for Ba)")
    parser.add_argument("--neutron", action="store_true", help="Compute for valence neutron instead of proton")
    parser.add_argument("--invert", action="store_true", help="Perform in-beam branching ratio inversion")
    parser.add_argument("--e-cross", type=float, default=750.0, help="E2 crossover energy in keV (default: 750.0)")
    parser.add_argument("--e-step", type=float, default=380.0, help="M1+E2 stopover energy in keV (default: 380.0)")
    parser.add_argument("--i-cross", type=float, default=40.0, help="Intensity of E2 crossover (default: 40.0)")
    parser.add_argument("--i-step", type=float, default=100.0, help="Intensity of M1+E2 stopover (default: 100.0)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    gk_res = calculate_nilsson_gk(args.omega, args.lambda_val, args.mass, args.charge, args.neutron)

    # Calculate moments for band members
    moments = []
    for dI in range(4):
        I_val = args.omega + dI
        mu_val = calculate_magnetic_dipole_moment(I_val, args.omega, gk_res["g_K"], gk_res["g_R"])
        moments.append({"I": I_val, "mu_muN": mu_val})

    summary = {
        "nilsson_gk": gk_res,
        "magnetic_moments": moments
    }

    if args.invert or args.e_cross != 750.0:
        inv_res = invert_gk_from_bm1_be2(
            args.omega + 2.0, args.e_cross, args.e_step, args.i_cross, args.i_step, g_R=gk_res["g_R"]
        )
        summary["inversion"] = inv_res

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
