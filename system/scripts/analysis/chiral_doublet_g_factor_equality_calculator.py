#!/usr/bin/env python3
"""
chiral_doublet_g_factor_equality_calculator.py
==============================================
Nuclear Chiral Doublet Bands Magnetic Dipole Moments g-Factor Equality Theorem,
Aplanar Spin Geometry & Spurious Doublet Arbitration Engine.

Physics Formulation:
--------------------
1. The Grodner Chiral g-Factor Equality Theorem:
   Based on E. Grodner et al. (Phys. Rev. Lett. 120, 022502, 2018),
   E. Grodner in "Chirality and Wobbling in Atomic Nuclei" (CRC 2025) Chapter 7 (PDF pp. 156–166),
   and S. Frauendorf (Rev. Mod. Phys. 73, 463, 2001):
   In genuine chiral doublet bands, spontaneous time-reversal T combined with rotation R_y(pi)
   breaks the planar symmetry, forming degenerate left- |L> and right- |R> handed configurations.
   The laboratory eigenstates are symmetric and antisymmetric linear combinations:
     |Band 1> = ( |L> + |R> ) / sqrt(2)
     |Band 2> = ( |L> - |R> ) / sqrt(2)
   Because the magnetic dipole operator mu_hat is T-odd, the cross-terms vanish identically:
     <Band 1 | mu | Band 1> = <Band 2 | mu | Band 2>
   Theorem:
     For a genuine chiral partner band, the gyromagnetic factors g(I) of the two bands
     must be identical across the entire chiral spin window:
       g(Band 1, I) == g(Band 2, I).
   If g(Band 1) != g(Band 2) with statistical significance > 3-sigma, the candidate
   bands CANNOT be chiral partners (e.g. they are shape-coexistence or signature partners).

2. Microscopic g-Factor in 3D Aplanar Chiral Geometry:
   For odd-odd nuclei with valence proton j_p (short axis) and neutron hole j_n (long axis):
     g_chiral(I) = g_R + (g_p - g_R) * [ j_p^2 / (I*(I+1)) ] + (g_n - g_R) * [ j_n^2 / (I*(I+1)) ]
   where core collective g-factor is g_R ~ Z / A.

3. Statistical Arbitration & Hypothesis Testing:
   Null Hypothesis H0: g_1 == g_2 (Chiral symmetry established).
   Test statistic:
     Delta_g = |g_1 - g_2|
     sigma_Delta = sqrt( sigma_1^2 + sigma_2^2 )
     chi2_g = ( Delta_g / sigma_Delta )^2
     p-value = erfc( sqrt(chi2_g / 2.0) )
   - chi2_g <= 1.0 (p >= 0.317): Conclusive chiral equality;
   - chi2_g >= 9.0 (p <= 0.0027, > 3-sigma): Decisive rejection of chiral interpretation.
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "128Cs_chiral_doublet_benchmark": {
        "description": "128Cs experimental chiral doublet g-factor equality (Grodner PRL 2018)",
        "nucleus": "128Cs",
        "A_mass": 128,
        "Z_charge": 55,
        "spin_I": 11.0,
        "j_proton": 5.5,
        "j_neutron": 5.5,
        "g_proton": 1.30,
        "g_neutron": -0.20,
        "g1_measured": 0.58,
        "sigma_g1": 0.04,
        "g2_measured": 0.56,
        "sigma_g2": 0.05
    },
    "134Pr_chiral_candidate": {
        "description": "134Pr chiral doublet candidate at spin 12+ (pi h11/2 (x) nu h11/2^-1)",
        "nucleus": "134Pr",
        "A_mass": 134,
        "Z_charge": 59,
        "spin_I": 12.0,
        "j_proton": 5.5,
        "j_neutron": 5.5,
        "g_proton": 1.28,
        "g_neutron": -0.22,
        "g1_measured": 0.54,
        "sigma_g1": 0.05,
        "g2_measured": 0.52,
        "sigma_g2": 0.06
    },
    "spurious_pseudo_chiral_counterexample": {
        "description": "Spurious doublet counterexample (shape coexistence mistaken for chirality)",
        "nucleus": "Pseudo-Chiral",
        "A_mass": 130,
        "Z_charge": 56,
        "spin_I": 11.0,
        "j_proton": 5.5,
        "j_neutron": 5.5,
        "g_proton": 1.30,
        "g_neutron": -0.20,
        "g1_measured": 0.85,
        "sigma_g1": 0.04,
        "g2_measured": 0.32,
        "sigma_g2": 0.05
    }
}


def calculate_theoretical_chiral_gfactor(A_mass, Z_charge, spin_I, j_p, j_n, g_p=1.30, g_n=-0.20, g_R=None):
    """
    Calculates theoretical chiral g-factor from 3D orthogonal angular momentum geometry:
      g_chiral(I) = g_R + (g_p - g_R) * [ j_p^2 / (I*(I+1)) ] + (g_n - g_R) * [ j_n^2 / (I*(I+1)) ].
    """
    if g_R is None:
        g_R = float(Z_charge) / float(A_mass)

    I_norm = spin_I * (spin_I + 1.0)
    term_p = (g_p - g_R) * (j_p**2) / I_norm
    term_n = (g_n - g_R) * (j_n**2) / I_norm

    g_tot = g_R + term_p + term_n
    return {
        "g_R_core": float(g_R),
        "g_proton_term": float(term_p),
        "g_neutron_term": float(term_n),
        "g_chiral_theoretical": float(g_tot)
    }


def arbitrate_chiral_gfactor_equality(g1, sigma1, g2, sigma2):
    """
    Performs statistical test on H0: g1 == g2 (Chiral equality theorem).
    """
    delta_g = abs(g1 - g2)
    sigma_delta = math.sqrt(sigma1**2 + sigma2**2)
    chi2_val = (delta_g / sigma_delta)**2

    # p-value for 1 degree of freedom: erfc(sqrt(chi2/2))
    p_val = math.erfc(math.sqrt(chi2_val / 2.0))
    sigma_discrepancy = delta_g / sigma_delta

    if chi2_val <= 1.0:
        status = "chiral_equality_confirmed"
        verdict = f"Consistent with chiral equality theorem: Delta_g = {delta_g:.3f} +- {sigma_delta:.3f} (chi2 = {chi2_val:.2f}, {sigma_discrepancy:.1f}-sigma, p = {p_val:.3f})."
    elif chi2_val <= 4.0:
        status = "chiral_compatible_2sigma"
        verdict = f"Compatible within 2-sigma: Delta_g = {delta_g:.3f} +- {sigma_delta:.3f} (chi2 = {chi2_val:.2f}, {sigma_discrepancy:.1f}-sigma)."
    elif chi2_val >= 9.0:
        status = "chiral_equality_definitively_rejected"
        verdict = f"REJECTED (>3-sigma discrepancy): Delta_g = {delta_g:.3f} +- {sigma_delta:.3f} (chi2 = {chi2_val:.2f}, {sigma_discrepancy:.1f}-sigma, p = {p_val:.4e}). Candidate bands are NOT chiral partners!"
    else:
        status = "marginal_discrepancy"
        verdict = f"Marginal tension (2 - 3 sigma): chi2 = {chi2_val:.2f} ({sigma_discrepancy:.1f}-sigma). Higher precision g-factor data needed."

    return {
        "delta_g": float(delta_g),
        "sigma_delta_g": float(sigma_delta),
        "chi2_g": float(chi2_val),
        "sigma_discrepancy": float(sigma_discrepancy),
        "p_value": float(p_val),
        "status": status,
        "verdict": verdict
    }


def run_chiral_gfactor_analysis(nucleus, A_mass, Z_charge, spin_I, j_p, j_n,
                                g1, sigma1, g2, sigma2, g_p=1.30, g_n=-0.20, g_R=None):
    """
    Full execution pipeline for chiral g-factor analysis.
    """
    theo = calculate_theoretical_chiral_gfactor(A_mass, Z_charge, spin_I, j_p, j_n, g_p, g_n, g_R)
    arb = arbitrate_chiral_gfactor_equality(g1, sigma1, g2, sigma2)

    return {
        "nucleus": nucleus,
        "A_mass": A_mass,
        "Z_charge": Z_charge,
        "spin_I": float(spin_I),
        "measured_g_factors": {
            "band1_g1": float(g1),
            "sigma_g1": float(sigma1),
            "band2_g2": float(g2),
            "sigma_g2": float(sigma2)
        },
        "theoretical_model": theo,
        "arbitration": arb
    }


def format_text_report(res, title="Chiral Doublet g-Factor Equality Arbitrator"):
    meas = res["measured_g_factors"]
    theo = res["theoretical_model"]
    arb = res["arbitration"]

    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Nucleus: {res['nucleus']} at Spin I = {res['spin_I']:.1f}")
    lines.append("=" * 76)
    lines.append("Experimental Magnetic Dipole g-Factors:")
    lines.append(f"  Band 1 Measured g-Factor        : g1 = {meas['band1_g1']:+.4f} +- {meas['sigma_g1']:.4f}")
    lines.append(f"  Band 2 Measured g-Factor        : g2 = {meas['band2_g2']:+.4f} +- {meas['sigma_g2']:.4f}")
    lines.append(f"  Observed g-Factor Difference    : Delta_g = {arb['delta_g']:.4f} +- {arb['sigma_delta_g']:.4f}")
    lines.append("-" * 76)
    lines.append("3D Aplanar Chiral Model Prediction:")
    lines.append(f"  Core Rotational g_R             : {theo['g_R_core']:.4f}")
    lines.append(f"  Valence Proton Current Term     : {theo['g_proton_term']:+.4f}")
    lines.append(f"  Valence Neutron Current Term    : {theo['g_neutron_term']:+.4f}")
    lines.append(f"  Theoretical Chiral g-Factor     : g_chiral = {theo['g_chiral_theoretical']:+.4f}")
    lines.append("-" * 76)
    lines.append("Chiral Equality Hypothesis Test (H0: g1 == g2):")
    lines.append(f"  Test Statistic (chi^2)          : {arb['chi2_g']:.3f} ({arb['sigma_discrepancy']:.2f}-sigma discrepancy)")
    lines.append(f"  p-value                         : {arb['p_value']:.4e}")
    lines.append(f"  Arbitration Status              : {arb['status']}")
    lines.append(f"  Verdict                         : {arb['verdict']}")
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Chiral Doublet g-Factor Equality Theorem & Spurious Doublet Arbitrator."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load experimental preset")
    parser.add_argument("--nucleus", type=str, default="Chiral-Nucleus", help="Nucleus name")
    parser.add_argument("--mass-a", type=int, help="Mass number A")
    parser.add_argument("--charge-z", type=int, help="Atomic number Z")
    parser.add_argument("--spin-i", type=float, help="Spin I")
    parser.add_argument("--jp", type=float, default=5.5, help="Proton alignment j_p")
    parser.add_argument("--jn", type=float, default=5.5, help="Neutron alignment j_n")
    parser.add_argument("--g1", type=float, help="Measured g1 for Band 1")
    parser.add_argument("--sig1", type=float, default=0.04, help="Error on g1")
    parser.add_argument("--g2", type=float, help="Measured g2 for Band 2")
    parser.add_argument("--sig2", type=float, default=0.05, help="Error on g2")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        nuc = p["nucleus"]
        A = p["A_mass"]
        Z = p["Z_charge"]
        spin_I = p["spin_I"]
        jp = p["j_proton"]
        jn = p["j_neutron"]
        gp = p.get("g_proton", 1.30)
        gn = p.get("g_neutron", -0.20)
        g1 = p["g1_measured"]
        sig1 = p["sigma_g1"]
        g2 = p["g2_measured"]
        sig2 = p["sigma_g2"]
        title = f"Preset: {args.preset} ({p['description']})"
    elif args.g1 is not None and args.g2 is not None:
        nuc = args.nucleus
        A = args.mass_a if args.mass_a else 128
        Z = args.charge_z if args.charge_z else 55
        spin_I = args.spin_i if args.spin_i else 11.0
        jp = args.jp
        jn = args.jn
        gp = 1.30
        gn = -0.20
        g1 = args.g1
        sig1 = args.sig1
        g2 = args.g2
        sig2 = args.sig2
        title = "Custom User Input"
    else:
        return parser.print_help()

    res = run_chiral_gfactor_analysis(
        nucleus=nuc,
        A_mass=A,
        Z_charge=Z,
        spin_I=spin_I,
        j_p=jp,
        j_n=jn,
        g1=g1,
        sigma1=sig1,
        g2=g2,
        sigma2=sig2,
        g_p=gp,
        g_n=gn
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
