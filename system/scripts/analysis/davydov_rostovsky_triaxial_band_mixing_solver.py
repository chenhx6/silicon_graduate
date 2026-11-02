#!/usr/bin/env python3
"""
davydov_rostovsky_triaxial_band_mixing_solver.py
================================================
Davydov-Rostovsky Non-Adiabatic Triaxial Rotor Beta- and Gamma-Band Mixing Engine,
Mikhailov Expansion Parameter Inversion & Interband B(E2) Alaga Rule Deviation Suite.

Physics Formulation:
--------------------
1. Non-Adiabatic Rotational-Vibrational Coupling:
   Based on A. S. Davydov & V. S. Rostovsky (Nucl. Phys. 60, 529, 1964),
   A. Bohr & B. R. Mottelson "Nuclear Structure" Vol. II §4-2 (pp. 140–165),
   and W. Greiner & J. A. Maruhn "Nuclear Models" Ch. 6:
   In transitional and soft triaxial nuclei, centrifugal stretching and Coriolis forces
   couple the ground-state rotational band (g) with the beta-vibrational band (K=0) and
   gamma-vibrational band (K=2).
   The wavefunctions are perturbed as:
     |I M, g> = |I M 0, g> - z_beta * sqrt[I(I+1)] * |I M 0, beta> - z_gamma * sqrt[(I-1)I(I+1)(I+2)] * |I M 2, gamma>
   where z_beta and z_gamma are the non-adiabatic mixing parameters.

2. Deviation of Interband B(E2) Ratios from Alaga Rules:
   In the unperturbed adiabatic limit (Alaga rule):
     B(E2; 2_gamma -> 0_g) / B(E2; 2_gamma -> 2_g) = <2 2 2 -2 | 0 0>^2 / <2 2 2 -2 | 2 0>^2 = 7 / 10 = 0.700.
   In real nuclei, the gamma-band mixing parameter z_gamma systematically suppresses this ratio:
     R_gamma(z_gamma) = 0.700 * [ (1 - 2*z_gamma) / (1 + z_gamma) ]^2.
   Measuring the experimental branching ratio R_exp allows direct analytical inversion of z_gamma:
     sqrt( R_exp / 0.700 ) = (1 - 2*z_gamma) / (1 + z_gamma)
     ==> z_gamma = [ 1 - sqrt(R_exp / 0.700) ] / [ 2 + sqrt(R_exp / 0.700) ].

3. Microscopic Coupling Hamiltonian Matrix Element h_2:
   The first-order perturbation matrix element connecting the gamma band to the ground band is:
     h_2 = z_gamma * [ E(2_gamma) - E(2_g) ] / sqrt(6)  [keV].
   The non-adiabatic softness parameter mu is given by:
     mu = [ E(2_g) / E(0_beta) ]^(1/4).
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "152Sm_classic_transitional_nucleus": {
        "description": "152Sm classic rotational-vibrational transitional benchmark (Bohr Vol 2)",
        "nucleus": "152Sm",
        "E_2g_keV": 121.78,
        "E_4g_keV": 366.5,
        "E_2gamma_keV": 1085.87,
        "E_0beta_keV": 684.7,
        "exp_be2_gamma_ratio": 0.540
    },
    "130Ba_gamma_soft_triaxial": {
        "description": "130Ba triaxial gamma-soft transitional nucleus (R_exp = 0.485)",
        "nucleus": "130Ba",
        "E_2g_keV": 357.2,
        "E_4g_keV": 908.1,
        "E_2gamma_keV": 1187.5,
        "E_0beta_keV": 890.0,
        "exp_be2_gamma_ratio": 0.485
    },
    "rigid_rotor_zero_mixing_limit": {
        "description": "Rigid adiabatic rotor reference limit (R_exp = 0.700, z_gamma = 0)",
        "nucleus": "Rigid-Rotor-Ref",
        "E_2g_keV": 100.0,
        "E_4g_keV": 333.3,
        "E_2gamma_keV": 1200.0,
        "E_0beta_keV": 1500.0,
        "exp_be2_gamma_ratio": 0.700
    }
}


def invert_gamma_mixing_parameter(exp_ratio):
    """
    Inverts z_gamma from experimental ratio B(E2; 2_gamma -> 0_g) / B(E2; 2_gamma -> 2_g).
    Formula: sqrt(R / 0.700) = (1 - 2*z) / (1 + z)
    """
    alaga_base = 0.700
    r = max(1e-4, exp_ratio)
    sqrt_term = math.sqrt(r / alaga_base)

    # z = (1 - sqrt_term) / (2 + sqrt_term)
    z_gamma = (1.0 - sqrt_term) / (2.0 + sqrt_term)
    return float(z_gamma)


def calculate_davydov_rostovsky_parameters(E_2g, E_2gamma, E_0beta, exp_ratio):
    """
    Calculates non-adiabatic parameters z_gamma, h_2 coupling, softness mu, and predicted branching.
    """
    z_g = invert_gamma_mixing_parameter(exp_ratio)

    # Coupling matrix element h_2 in keV: h_2 = z_gamma * delta_E / sqrt(6)
    delta_E_gamma = E_2gamma - E_2g
    h2_keV = z_g * delta_E_gamma / math.sqrt(6.0)

    # Softness parameter mu: [ E(2_g) / E(0_beta) ]^(1/4)
    softness_mu = ((E_2g / max(1.0, E_0beta))**0.25) if E_0beta > 0 else 0.0

    # Predicted ratio for 2_gamma -> 4_g / 2_gamma -> 2_g
    # Alaga base for 2_gamma -> 4_g / 2_gamma -> 2_g is 0.050
    # Mikhailov formula: R_42 = 0.050 * [ (1 + 4*z_gamma) / (1 + z_gamma) ]^2
    r_42_pred = 0.050 * (((1.0 + 4.0 * z_g) / (1.0 + z_g))**2)

    # Alaga suppression percentage
    suppression_pct = ((0.700 - exp_ratio) / 0.700) * 100.0

    return {
        "alaga_unperturbed_ratio": 0.700,
        "experimental_ratio": float(exp_ratio),
        "alaga_suppression_pct": float(suppression_pct),
        "z_gamma_mixing_parameter": float(z_g),
        "coupling_matrix_element_h2_keV": float(h2_keV),
        "non_adiabatic_softness_mu": float(softness_mu),
        "predicted_ratio_2gamma_to_4g_vs_2g": float(r_42_pred)
    }


def run_davydov_rostovsky_analysis(nucleus, E_2g, E_4g, E_2gamma, E_0beta, exp_ratio):
    """
    Complete execution pipeline for Davydov-Rostovsky non-adiabatic band mixing analysis.
    """
    res = calculate_davydov_rostovsky_parameters(E_2g, E_2gamma, E_0beta, exp_ratio)
    return {
        "nucleus": nucleus,
        "experimental_energies_keV": {
            "E_2g": float(E_2g),
            "E_4g": float(E_4g),
            "E_2gamma": float(E_2gamma),
            "E_0beta": float(E_0beta)
        },
        "mixing_results": res
    }


def format_text_report(res, title="Davydov-Rostovsky Triaxial Band Mixing Solver"):
    nuc = res["nucleus"]
    eg = res["experimental_energies_keV"]
    m = res["mixing_results"]
    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Nucleus: {nuc} | E(2_g) = {eg['E_2g']:.1f} keV, E(2_gamma) = {eg['E_2gamma']:.1f} keV, E(0_beta) = {eg['E_0beta']:.1f} keV")
    lines.append("=" * 76)
    lines.append("Interband B(E2) Branching Ratio Deviation from Alaga Rule:")
    lines.append(f"  Ideal Alaga Unperturbed Ratio   : B(E2; 2_gamma -> 0_g) / B(E2; 2_gamma -> 2_g) = {m['alaga_unperturbed_ratio']:.4f}")
    lines.append(f"  Experimental Observed Ratio     : R_exp = {m['experimental_ratio']:.4f} ({m['alaga_suppression_pct']:+5.2f}% Alaga deviation)")
    lines.append("-" * 76)
    lines.append("Non-Adiabatic Mikhailov / Davydov-Rostovsky Parameters:")
    lines.append(f"  Gamma-Band Mixing Parameter z_g : z_gamma = {m['z_gamma_mixing_parameter']:+.5f}")
    lines.append(f"  Rot-Vib Coupling Matrix Element : h_2 = {m['coupling_matrix_element_h2_keV']:.2f} keV  [<gamma|H_c|g> = h_2 * sqrt(6)]")
    lines.append(f"  Dynamic Softness Parameter mu   : mu = {m['non_adiabatic_softness_mu']:.4f}  (Rigid limit = 0.0)")
    lines.append(f"  Predicted Ratio (2_gamma -> 4_g): B(E2; 2_g -> 4_g) / B(E2; 2_g -> 2_g) = {m['predicted_ratio_2gamma_to_4g_vs_2g']:.4f}")
    lines.append("-" * 76)
    lines.append("Physical Implication: Centrifugal Coriolis coupling mixes K=0 and K=2 bands,")
    lines.append("explaining the universal systematic suppression of interband E2 transitions.")
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Davydov-Rostovsky Triaxial Band Mixing Solver."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load benchmark preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        nuc = p["nucleus"]
        e2g = p["E_2g_keV"]
        e4g = p["E_4g_keV"]
        e2gamm = p["E_2gamma_keV"]
        e0b = p["E_0beta_keV"]
        r_exp = p["exp_be2_gamma_ratio"]
        title = f"Preset: {args.preset} ({p['description']})"
    else:
        return parser.print_help()

    res = run_davydov_rostovsky_analysis(
        nucleus=nuc,
        E_2g=e2g,
        E_4g=e4g,
        E_2gamma=e2gamm,
        E_0beta=e0b,
        exp_ratio=r_exp
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
