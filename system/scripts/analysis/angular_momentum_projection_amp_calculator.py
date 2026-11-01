#!/usr/bin/env python3
"""
angular_momentum_projection_amp_calculator.py
=============================================
Quantum Angular Momentum Projection (AMP) from Deformed Intrinsic States &
Peierls-Yoccoz Rotational Spectrum Generator.

Physics & Formulation:
----------------------
1. Broken Rotational Symmetry in Deformed States:
   Deformed mean-field states |Phi> (Nilsson, HF, HFB) break rotational invariance:
     [H, J^2] != 0 -> |Phi> is a wave packet over angular momenta I = 0, 2, 4, ...

2. Angular Momentum Projection Operator P_MK^I:
   P_MK^I = (2I + 1) / (8 * pi^2) * integral D_MK^I*(alpha, beta, gamma) * R(alpha, beta, gamma) dOmega
   For axially symmetric K=0 deformed states:
     P_00^I = (2I + 1) / 2 * integral_0^pi d(beta) * sin(beta) * d_00^I(beta) * exp(-i * beta * J_y)

3. Overlap Kernels (Norm and Hamiltonian):
   - Norm kernel: n(beta) = <Phi | exp(-i * beta * J_y) | Phi>
   - Hamiltonian kernel: h(beta) = <Phi | H * exp(-i * beta * J_y) | Phi>
   Gaussian Overlap Approximation (GOA):
     n(beta) ~ exp( - 0.5 * <J_y^2> * beta^2 )

4. Projected Energy Spectrum & Peierls-Yoccoz Inertia:
   E(I) = H_00^I / N_00^I ~ E_int + (hbar^2 / (2 * J_PY)) * I*(I + 1)
   where J_PY = <J_y^2> / (2 * delta_H) is the Peierls-Yoccoz moment of inertia.
   Note: J_PY < J_Thouless-Valatin (cranking) because cranking includes dynamic time-odd polarization!

References:
  - R. E. Peierls and J. Yoccoz, Proc. Phys. Soc. A 70, 381 (1957).
  - P. Ring and P. Schuck, The Nuclear Many-Body Problem, Chapter 11, Springer (1980).
  - 卢希庭, 《原子核物理（修订版）》, 第4章.
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def legendre_polynomial(l: int, x: float) -> float:
    """Computes Legendre polynomial P_l(x) = d_00^l(beta) where x = cos(beta)."""
    if l == 0:
        return 1.0
    elif l == 1:
        return x
    p0 = 1.0
    p1 = x
    for k in range(1, l):
        p_next = ((2 * k + 1) * x * p1 - k * p0) / (k + 1)
        p0 = p1
        p1 = p_next
    return p1


def calculate_amp_kernels_goa(
    beta_rad: float,
    Jy2_expectation: float = 35.0,
    E_intrinsic_MeV: float = -120.0,
    A_rot_peierls_MeV: float = 0.025
) -> Tuple[float, float]:
    """
    Computes Gaussian Overlap norm kernel n(beta) and Hamiltonian kernel h(beta).
    """
    # Norm kernel n(beta) = exp(-0.5 * <Jy^2> * beta^2)
    n_beta = math.exp(-0.5 * Jy2_expectation * (beta_rad ** 2))

    # Hamiltonian kernel h(beta) = n(beta) * [ E_int + A_rot * <Jy^2> * beta^2 ]
    h_beta = n_beta * (E_intrinsic_MeV + A_rot_peierls_MeV * Jy2_expectation * (beta_rad ** 2))
    return n_beta, h_beta


def project_rotational_spectrum(
    max_spin_I: int = 10,
    Jy2_expectation: float = 35.0,
    E_intrinsic_MeV: float = -120.0,
    A_rot_peierls_MeV: float = 0.025,
    num_beta_steps: int = 500
) -> List[Dict[str, Any]]:
    """
    Integrates the projection integrals over beta in [0, pi] for even spins I = 0, 2, 4, ...
    """
    d_beta = math.pi / float(num_beta_steps)
    spectrum = []

    E_ground = None
    for I in range(0, max_spin_I + 1, 2):
        norm_integral = 0.0
        h_integral = 0.0

        for k in range(num_beta_steps):
            beta_val = (k + 0.5) * d_beta
            sin_beta = math.sin(beta_val)
            cos_beta = math.cos(beta_val)

            # Wigner d_00^I(beta) is identical to Legendre polynomial P_I(cos beta)
            d00 = legendre_polynomial(I, cos_beta)

            n_b, h_b = calculate_amp_kernels_goa(beta_val, Jy2_expectation, E_intrinsic_MeV, A_rot_peierls_MeV)

            weight = sin_beta * d00 * d_beta
            norm_integral += n_b * weight
            h_integral += h_b * weight

        prefactor = (2 * I + 1) / 2.0
        N_I = prefactor * norm_integral
        H_I = prefactor * h_integral

        if abs(N_I) > 1e-12:
            e_proj = H_I / N_I
        else:
            e_proj = E_intrinsic_MeV

        if E_ground is None:
            E_ground = e_proj

        e_exc_keV = (e_proj - E_ground) * 1e3

        # Analytical Peierls-Yoccoz comparison: E ~ A_rot * I*(I+1)
        e_analytic_keV = A_rot_peierls_MeV * I * (I + 1) * 1e3

        spectrum.append({
            "spin_I": I,
            "projected_norm_N_I": round(N_I, 4),
            "projected_total_energy_MeV": round(e_proj, 3),
            "excitation_energy_keV": round(e_exc_keV, 1),
            "analytic_peierls_yoccoz_keV": round(e_analytic_keV, 1),
            "residual_deviation_keV": round(e_exc_keV - e_analytic_keV, 1)
        })

    return spectrum


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   ANGULAR MOMENTUM PROJECTION (AMP) & ROTATIONAL SPECTRUM ANALYZER")
    lines.append("=" * 72)
    lines.append(f" INTRINSIC STATE DEFORMATION PROPERTIES:")
    lines.append(f"   Intrinsic Fluctuation <J_y^2>  : {summary['Jy2_expectation']} hbar^2")
    lines.append(f"   Intrinsic Base Energy          : {summary['E_intrinsic_MeV']} MeV")
    lines.append(f"   Peierls-Yoccoz Rotational Param: A_rot = {summary['A_rot_peierls_MeV']*1e3:.2f} keV")
    lines.append("-" * 72)
    lines.append(" PROJECTED ROTATIONAL BAND SPECTRUM (K = 0):")
    lines.append(f"   {'Spin I':<8} {'Norm N_I':<12} {'Total E (MeV)':<16} {'E_ex (keV)':<14} {'Analytic PY (keV)':<18}")
    lines.append("   " + "-" * 66)
    for lv in summary["projected_spectrum"]:
        lines.append(f"   {lv['spin_I']:<8} {lv['projected_norm_N_I']:<12.4f} {lv['projected_total_energy_MeV']:<16.3f} {lv['excitation_energy_keV']:<14.1f} {lv['analytic_peierls_yoccoz_keV']:<18.1f}")
    lines.append("-" * 72)
    lines.append(" Physical Significance:")
    lines.append("   - AMP restores rotational symmetry broken by deformed mean-field states.")
    lines.append("   - Derives clean I(I+1) rotational bands from intrinsic wave packets.")
    lines.append("   - Peierls-Yoccoz inertia underpins triaxial projected shell models (TPSM).")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Angular Momentum Projection (AMP) & Rotational Spectrum Analyzer."
    )
    parser.add_argument("--max-spin", type=int, default=10, help="Maximum spin I to project (default: 10)")
    parser.add_argument("--jy2", type=float, default=35.0, help="Intrinsic <Jy^2> dispersion in hbar^2 (default: 35.0)")
    parser.add_argument("--e-int", type=float, default=-120.0, help="Intrinsic state energy in MeV (default: -120.0)")
    parser.add_argument("--a-rot", type=float, default=0.025, help="Peierls-Yoccoz rotational constant in MeV (default: 0.025)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    spec = project_rotational_spectrum(args.max_spin, args.jy2, args.e_int, args.a_rot)
    summary = {
        "Jy2_expectation": args.jy2,
        "E_intrinsic_MeV": args.e_int,
        "A_rot_peierls_MeV": args.a_rot,
        "projected_spectrum": spec
    }

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
