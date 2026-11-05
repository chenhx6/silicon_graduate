#!/usr/bin/env python3
"""
strutinsky_shell_correction_calculator.py
=========================================
Strutinsky Energy Smoothing Method, Plateau Condition & Ground State
Microscopic Shell Correction Energy Engine.

Physics & Formulation:
----------------------
1. Total Energy Macroscopic-Microscopic Decomposition:
   E_total = E_LDM + delta_U_p + delta_U_n + delta_P
   where delta_U is the Strutinsky shell correction energy:
     delta_U = sum_{i=1}^N eps_i - integral_{-inf}^{lambda_tilde} eps * g_tilde(eps) deps

2. Strutinsky Gaussian Smoothing with Hermite Curvature Polynomials:
   Smooth level density g_tilde(eps):
     g_tilde(eps) = (1 / (gamma * sqrt(pi))) * sum_i exp(-u_i^2) * P_M(u_i)
   where:
     u_i = (eps - eps_i) / gamma
     P_M(u) = 35/16 - (35/8)*u^2 + (21/8)*u^4 - 0.5*u^6   (for 6th-order M = 3)
     gamma: Smoothing parameter ~ 1.0 - 1.4 * hbar*omega_0 (~ 8 - 10 MeV).

3. Smooth Fermi Energy lambda_tilde:
   Determined by particle number conservation:
     N = integral_{-inf}^{lambda_tilde} g_tilde(eps) deps

4. The Plateau Condition:
   Physical delta_U must be stationary against variations in smoothing parameter gamma:
     d(delta_U) / d(gamma) ~ 0 on the plateau region gamma in [8, 12] MeV.
   - Double magic nuclei (e.g. 208Pb, 132Sn): delta_U ~ -10 to -14 MeV (deep shell stabilization).
   - Mid-shell deformed nuclei (e.g. 130Ba): delta_U_sph > 0, driving prolate deformation.

References:
  - V. M. Strutinsky, Nucl. Phys. A 95, 420 (1967); Nucl. Phys. A 122, 1 (1968).
  - M. Brack et al., Rev. Mod. Phys. 44, 320 (1972).
  - W. Greiner and J. A. Maruhn, Nuclear Models, Springer (1996).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def strutinsky_curvature_polynomial(u: float) -> float:
    """6th-order (M=3) Hermite curvature correction polynomial P_3(u)."""
    u2 = u ** 2
    u4 = u2 ** 2
    u6 = u4 * u2
    return (35.0 / 16.0) - (35.0 / 8.0) * u2 + (21.0 / 8.0) * u4 - 0.5 * u6


def smooth_level_density(
    energy: float,
    single_particle_levels: List[float],
    gamma_smoothing_MeV: float = 8.5
) -> float:
    """
    Computes Strutinsky smoothed level density g_tilde(eps) in MeV^-1.
    """
    inv_gamma = 1.0 / max(gamma_smoothing_MeV, 1.0)
    g_sum = 0.0

    for eps_i in single_particle_levels:
        u = (energy - eps_i) * inv_gamma
        if abs(u) < 4.0:
            exp_term = math.exp(- u ** 2)
            poly = strutinsky_curvature_polynomial(u)
            g_sum += exp_term * poly

    return g_sum * inv_gamma / math.sqrt(math.pi)


def calculate_strutinsky_shell_correction(
    single_particle_levels: List[float],
    particle_number: int,
    gamma_smoothing_MeV: float = 8.5,
    degeneracy: int = 2
) -> Dict[str, Any]:
    """
    Calculates the Strutinsky shell correction energy delta_U for a given set of levels.
    """
    eps = sorted(single_particle_levels)
    n_pairs = particle_number // degeneracy
    if n_pairs > len(eps):
        raise ValueError("Not enough single-particle levels to accommodate particle number")

    # 1. Discrete energy sum E_disc = 2 * sum_{i=1}^{N/2} eps_i
    E_discrete = degeneracy * sum(eps[:n_pairs])

    # 2. Search for smooth Fermi level lambda_tilde: N = int_{-inf}^{lambda} g_tilde(e) de
    # Approximate integration via Simpson/trapezoidal grid
    e_min = eps[0] - 3.0 * gamma_smoothing_MeV
    e_max = eps[-1] + 3.0 * gamma_smoothing_MeV
    steps = 400
    de = (e_max - e_min) / float(steps)

    cum_particles = 0.0
    smooth_energy = 0.0
    lambda_tilde = eps[n_pairs - 1]
    found_lambda = False

    prev_g = smooth_level_density(e_min, eps, gamma_smoothing_MeV)

    for i in range(1, steps + 1):
        e_curr = e_min + i * de
        g_curr = smooth_level_density(e_curr, eps, gamma_smoothing_MeV)

        # Trapezoid integration for particle count (multiplied by degeneracy)
        dn = 0.5 * (prev_g + g_curr) * de * degeneracy
        dE_smooth = 0.5 * (prev_g * (e_curr - de) + g_curr * e_curr) * de * degeneracy

        cum_particles += dn
        smooth_energy += dE_smooth

        if not found_lambda and cum_particles >= float(particle_number):
            lambda_tilde = e_curr
            found_lambda = True
            break

        prev_g = g_curr

    delta_U = E_discrete - smooth_energy

    return {
        "particle_number": particle_number,
        "gamma_smoothing_MeV": gamma_smoothing_MeV,
        "discrete_sum_energy_MeV": round(E_discrete, 2),
        "smooth_energy_MeV": round(smooth_energy, 2),
        "smooth_fermi_energy_lambda_MeV": round(lambda_tilde, 2),
        "shell_correction_delta_U_MeV": round(delta_U, 2)
    }


def scan_strutinsky_plateau(
    single_particle_levels: List[float],
    particle_number: int,
    gamma_range: List[float] = [6.0, 7.5, 9.0, 10.5, 12.0]
) -> Dict[str, Any]:
    """
    Verifies the plateau condition: d(delta_U) / d(gamma) ~ 0 across smoothing range.
    """
    results = []
    for g in gamma_range:
        res = calculate_strutinsky_shell_correction(single_particle_levels, particle_number, g)
        results.append({
            "gamma_MeV": g,
            "delta_U_MeV": res["shell_correction_delta_U_MeV"],
            "lambda_tilde_MeV": res["smooth_fermi_energy_lambda_MeV"]
        })

    du_vals = [r["delta_U_MeV"] for r in results]
    plateau_drift = max(du_vals) - min(du_vals)
    has_plateau = (plateau_drift < 1.5)  # within 1.5 MeV variation

    return {
        "plateau_scan": results,
        "plateau_variation_MeV": round(plateau_drift, 2),
        "plateau_condition_satisfied": has_plateau
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   STRUTINSKY SHELL CORRECTION ENERGY & PLATEAU CONDITION ANALYZER")
    lines.append("=" * 72)

    sc = summary["shell_correction"]
    lines.append(f" SHELL CORRECTION CALCULATION (N = {sc['particle_number']}, gamma = {sc['gamma_smoothing_MeV']} MeV):")
    lines.append(f"   Discrete Single-Particle Sum   : {sc['discrete_sum_energy_MeV']} MeV")
    lines.append(f"   Smooth Strutinsky Energy       : {sc['smooth_energy_MeV']} MeV")
    lines.append(f"   Smooth Fermi Energy lambda     : {sc['smooth_fermi_energy_lambda_MeV']} MeV")
    lines.append(f"   Shell Correction Energy delta_U: {sc['shell_correction_delta_U_MeV']} MeV")
    lines.append("-" * 72)

    if "plateau_check" in summary:
        pc = summary["plateau_check"]
        lines.append(f" PLATEAU STABILITY AUDIT (Total Drift = {pc['plateau_variation_MeV']} MeV):")
        lines.append(
            "   Plateau Condition Status       : "
            f"{'PASS (stationary within the supplied gamma scan)' if pc['plateau_condition_satisfied'] else 'Drift detected'}"
        )
        lines.append("   " + "-" * 56)
        lines.append(f"   {'gamma (MeV)':<14} {'delta_U (MeV)':<18} {'lambda_tilde (MeV)':<18}")
        lines.append("   " + "-" * 56)
        for pt in pc["plateau_scan"]:
            lines.append(f"   {pt['gamma_MeV']:<14.1f} {pt['delta_U_MeV']:<18.2f} {pt['lambda_tilde_MeV']:<18.2f}")
        lines.append("-" * 72)

    lines.append(" Physical Significance:")
    lines.append("   - Separates microscopic quantum shell fluctuations from smooth liquid drop energy.")
    lines.append("   - Explains the ~ -12 MeV shell depression for double magic nuclei (208Pb).")
    lines.append(
        "   - A small drift in this finite scan supports the plateau diagnostic "
        "for the supplied spectrum; it does not certify a physical PES or "
        "experimental minimum."
    )
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Strutinsky Shell Correction Energy & Plateau Condition Calculator."
    )
    parser.add_argument("-N", "--particles", type=int, default=82, help="Particle number (default: 82 for magic shell)")
    parser.add_argument("-g", "--gamma", type=float, default=8.5, help="Smoothing parameter gamma in MeV (default: 8.5)")
    parser.add_argument("--demo-pb", action="store_true", help="Run benchmark magic shell calculation (simulating 208Pb magic shell)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    # Synthetic realistic single-particle spectrum with a large magic gap at N = 82 (4 MeV gap)
    sp_spectrum = []
    # Below gap (82 particles / 2 = 41 levels): spacing ~ 0.8 MeV
    for i in range(41):
        sp_spectrum.append(-45.0 + i * 0.85)
    # Magic gap at N = 82
    top_below = sp_spectrum[-1]
    # Above gap (25 levels): spacing ~ 0.9 MeV starting 4.2 MeV above top_below
    for i in range(25):
        sp_spectrum.append(top_below + 4.2 + i * 0.90)

    res = calculate_strutinsky_shell_correction(sp_spectrum, args.particles, args.gamma)
    plat = scan_strutinsky_plateau(sp_spectrum, args.particles)

    summary = {
        "shell_correction": res,
        "plateau_check": plat
    }

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
