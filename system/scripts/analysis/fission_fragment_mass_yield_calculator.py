#!/usr/bin/env python3
"""
fission_fragment_mass_yield_calculator.py
=========================================
Multi-Modal Nuclear Fission Fragment Mass Yield, Viola TKE Systematics &
Prompt Neutron Sawtooth Multiplicity Simulator.

Physics & Formulation:
----------------------
1. Multi-Modal Random Neck Rupture (Brosa Model):
   Mass distribution is a superposition of distinct fission modes:
   - Standard I (ST-I): Driven by spherical N=82, Z=50 (132Sn core); peak at A_H ~ 134.
   - Standard II (ST-II): Driven by deformed N ~ 88 shell; peak at A_H ~ 141.
   - Superlong (SL): Symmetric fission through elongated neck; peak at A_CN / 2.
   Y(A) = w_1 * Y_ST1(A) + w_2 * Y_ST2(A) + w_SL * Y_SL(A)

2. Viola Systematics for Total Kinetic Energy (TKE):
   <TKE> = 0.1189 * (Z_CN^2 / A_CN^(1/3)) + 7.3 MeV (Viola et al. 1985)
   Mode-dependent TKE:
     TKE_ST1 > TKE_ST2 > TKE_SL

3. Prompt Neutron Multiplicity Sawtooth Curve nu_bar(A):
   Deformation energy at scission converts to fragment excitation energy.
   - Near 132Sn (spherical magic shell): minimal scission deformation -> nu_bar drops to ~ 0.5.
   - Near A ~ 115 (light) and A ~ 155 (heavy): high scission elongation -> nu_bar rises to ~ 2.5 - 3.5.
   Total prompt neutron multiplicity:
     nu_tot = sum_A Y(A) * nu_bar(A)

References:
  - U. Brosa, S. Grossmann, and A. Muller, Phys. Rep. 197, 167 (1990).
  - V. E. Viola, K. W. Kwiatkowski, and M. Walker, Phys. Rev. C 31, 1550 (1985).
  - R. Vandenbosch and J. R. Huizenga, Nuclear Fission, Academic Press (1973).
  - W. Greiner and J. A. Maruhn, Nuclear Models, Springer (1996).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_viola_tke(Z_cn: int, A_cn: int) -> Dict[str, float]:
    """
    Computes average total kinetic energy <TKE> (MeV) using Viola systematics:
    <TKE> = 0.1189 * (Z^2 / A^(1/3)) + 7.3
    """
    coul_param = (Z_cn ** 2) / (A_cn ** (1.0 / 3.0))
    tke_avg = 0.1189 * coul_param + 7.3

    # Mode-dependent TKE offsets (Brosa model)
    tke_st1 = tke_avg + 12.0  # Compact scission, high Coulomb repulsion
    tke_st2 = tke_avg - 2.0   # Intermediate elongation
    tke_sl = tke_avg - 20.0   # Extremely elongated neck, low TKE

    return {
        "coulomb_parameter_Z2_over_A13": round(coul_param, 2),
        "mean_viola_TKE_MeV": round(tke_avg, 2),
        "TKE_Standard_I_MeV": round(tke_st1, 2),
        "TKE_Standard_II_MeV": round(tke_st2, 2),
        "TKE_Superlong_MeV": round(tke_sl, 2)
    }


def brosa_gaussian_pair(A: float, A_cn: int, A_mean_H: float, sigma: float) -> float:
    """Computes symmetric pair of Gaussians for light and heavy fragments."""
    A_mean_L = float(A_cn) - A_mean_H
    g_H = math.exp(-0.5 * ((A - A_mean_H) / sigma) ** 2)
    g_L = math.exp(-0.5 * ((A - A_mean_L) / sigma) ** 2)
    norm = math.sqrt(2.0 * math.pi) * sigma
    return 0.5 * (g_H + g_L) / norm


def sawtooth_neutron_multiplicity(A_frag: float, A_cn: int) -> float:
    """
    Models the universal sawtooth prompt neutron multiplicity nu_bar(A):
    - Dips to minimum near A ~ 132 (magic 132Sn).
    - Peaks near complementary light fragment A ~ (A_cn - 132) and high-A ~ 155.
    """
    # Scale to light fragment
    if A_frag > float(A_cn) / 2.0:
        # Heavy fragment
        dist_magic = abs(A_frag - 132.0)
        nu = 0.5 + 2.2 * (1.0 - math.exp(-0.06 * (dist_magic ** 1.3)))
    else:
        # Light fragment
        A_comp = float(A_cn) - A_frag
        dist_comp = abs(A_comp - 132.0)
        nu = 0.8 + 2.0 * (1.0 - math.exp(-0.05 * (dist_comp ** 1.3)))

    return max(min(nu, 4.0), 0.2)


def calculate_fission_fragment_distribution(
    Z_cn: int = 92,
    A_cn: int = 236,
    w_st1: float = 0.20,
    w_st2: float = 0.78,
    w_sl: float = 0.02
) -> Dict[str, Any]:
    """
    Computes mass yield curve Y(A), TKE, and prompt neutron sawtooth curve.
    """
    tot_weight = w_st1 + w_st2 + w_sl
    w1 = w_st1 / tot_weight
    w2 = w_st2 / tot_weight
    w_sym = w_sl / tot_weight

    # Mode centroids and widths
    A_H_st1 = 134.5
    sigma_st1 = 3.5

    A_H_st2 = 141.5
    sigma_st2 = 5.5

    A_sym = float(A_cn) / 2.0
    sigma_sl = 8.0

    mass_grid = [A for A in range(60, A_cn - 60 + 1)]
    yields = []
    nu_bars = []

    total_yield = 0.0
    total_neutrons = 0.0

    for A in mass_grid:
        # Standard I
        y1 = brosa_gaussian_pair(float(A), A_cn, A_H_st1, sigma_st1)
        # Standard II
        y2 = brosa_gaussian_pair(float(A), A_cn, A_H_st2, sigma_st2)
        # Superlong symmetric
        g_sl = math.exp(-0.5 * ((float(A) - A_sym) / sigma_sl) ** 2) / (math.sqrt(2.0 * math.pi) * sigma_sl)

        y_total = 200.0 * (w1 * y1 + w2 * y2 + w_sym * g_sl)  # Normalized to 200% yield
        nu_val = sawtooth_neutron_multiplicity(float(A), A_cn)

        yields.append(round(y_total, 4))
        nu_bars.append(round(nu_val, 3))

        total_yield += y_total
        total_neutrons += (y_total / 200.0) * nu_val

    tke_info = calculate_viola_tke(Z_cn, A_cn)

    # Find light and heavy peak centroids
    idx_mid = len(mass_grid) // 2
    light_yields = yields[:idx_mid]
    heavy_yields = yields[idx_mid:]

    max_light_idx = light_yields.index(max(light_yields))
    max_heavy_idx = heavy_yields.index(max(heavy_yields)) + idx_mid

    A_peak_light = mass_grid[max_light_idx]
    A_peak_heavy = mass_grid[max_heavy_idx]

    return {
        "compound_nucleus": f"Z={Z_cn}, A={A_cn}",
        "mode_weights": {"Standard_I": round(w1, 3), "Standard_II": round(w2, 3), "Superlong": round(w_sym, 3)},
        "peak_light_fragment_A": A_peak_light,
        "peak_heavy_fragment_A": A_peak_heavy,
        "asymmetry_peak_ratio_A_H_over_A_L": round(float(A_peak_heavy) / float(A_peak_light), 3),
        "mean_prompt_neutron_multiplicity": round(total_neutrons * 2.0, 2),  # per fission event
        "TKE_systematics": tke_info,
        "mass_sample_points": [
            {"A": mass_grid[i], "yield_percent": yields[i], "nu_bar": nu_bars[i]}
            for i in range(0, len(mass_grid), 5)
        ]
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   FISSION FRAGMENT MASS YIELD, VIOLA TKE & NEUTRON SAWTOOTH ANALYZER")
    lines.append("=" * 72)
    lines.append(f" FISSIONING SYSTEM: {summary['compound_nucleus']}")
    lines.append(f"   Mode Weights: ST-I = {summary['mode_weights']['Standard_I']}, ST-II = {summary['mode_weights']['Standard_II']}, Superlong = {summary['mode_weights']['Superlong']}")
    lines.append(f"   Asymmetric Peak Fragment (Light): A_L = {summary['peak_light_fragment_A']}")
    lines.append(f"   Asymmetric Peak Fragment (Heavy): A_H = {summary['peak_heavy_fragment_A']} (Ratio = {summary['asymmetry_peak_ratio_A_H_over_A_L']})")
    lines.append(f"   Mean Prompt Neutron Multiplicity: nu_tot = {summary['mean_prompt_neutron_multiplicity']} n/fission")
    lines.append("-" * 72)

    tke = summary["TKE_systematics"]
    lines.append(" TOTAL KINETIC ENERGY (TKE) VIOLA SYSTEMATICS:")
    lines.append(f"   Coulomb Parameter Z^2 / A^(1/3) : {tke['coulomb_parameter_Z2_over_A13']}")
    lines.append(f"   Mean Fission TKE                : {tke['mean_viola_TKE_MeV']} MeV")
    lines.append(f"   Standard I (Compact Scission)   : {tke['TKE_Standard_I_MeV']} MeV")
    lines.append(f"   Standard II (Intermediate)      : {tke['TKE_Standard_II_MeV']} MeV")
    lines.append(f"   Superlong (Elongated Neck)      : {tke['TKE_Superlong_MeV']} MeV")
    lines.append("-" * 72)
    lines.append(" MASS YIELD & PROMPT NEUTRON SAWTOOTH PROFILE (Sample):")
    lines.append(f"   {'Fragment A':<12} {'Mass Yield Y(A) %':<20} {'nu_bar(A) (n/frag)':<20}")
    lines.append("   " + "-" * 55)
    for pt in summary["mass_sample_points"][:12]:
        lines.append(f"   {pt['A']:<12} {pt['yield_percent']:<20.3f} {pt['nu_bar']:<20.3f}")
    lines.append("-" * 72)
    lines.append(" Physical Significance:")
    lines.append("   - Shell effects in 132Sn anchor the heavy peak at A ~ 134-140.")
    lines.append("   - Scission deformation differences generate the universal neutron sawtooth.")
    lines.append("   - Predicts fragment distributions for nuclear power and reactor anti-neutrinos.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Fission Fragment Mass Yield, Viola TKE & Neutron Sawtooth Simulator."
    )
    parser.add_argument("-Z", type=int, default=92, help="Fissioning nucleus charge Z (default: 92 for U)")
    parser.add_argument("-A", type=int, default=236, help="Fissioning nucleus mass A (default: 236 for 235U+n)")
    parser.add_argument("--w-st1", type=float, default=0.20, help="Weight of Standard I mode (default: 0.20)")
    parser.add_argument("--w-st2", type=float, default=0.78, help="Weight of Standard II mode (default: 0.78)")
    parser.add_argument("--w-sl", type=float, default=0.02, help="Weight of Superlong symmetric mode (default: 0.02)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    summary = calculate_fission_fragment_distribution(args.Z, args.A, args.w_st1, args.w_st2, args.w_sl)

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
