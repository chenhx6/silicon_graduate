#!/usr/bin/env python3
"""
rmf_symmetry_energy_slope_calculator.py
=======================================
Relativistic Mean Field (RMF) Nuclear Symmetry Energy S(rho), Density Slope L &
Neutron Star Core-Crust Transition Functional.

Physics & Formulation:
----------------------
1. Asymmetric Nuclear Matter EOS:
   E/A(rho, delta) = E_0(rho) + S(rho) * delta^2
   where delta = (rho_n - rho_p) / rho is isospin asymmetry.

2. RMF Microscopic Symmetry Energy S(rho):
   S(rho) = (k_F^2 / (6 * sqrt(k_F^2 + M*(rho)^2))) + (g_rho^2 / (8 * m_rho^2)) * rho
   where:
     k_F = (1.5 * pi^2 * rho)^(1/3)
     M*(rho): Effective Dirac nucleon mass.
     g_rho / m_rho: Isovector rho-meson coupling.

3. Macroscopic Symmetry Parameters at Saturation rho_0 ~ 0.153 fm^-3:
   - Symmetry energy at saturation: J = S(rho_0) ~ 31 - 38 MeV.
   - Density slope parameter:
       L = 3 * rho_0 * [ dS/drho ]_{rho_0} ~ 40 - 120 MeV.
   - Pure neutron matter pressure:
       P_PNM(rho_0) = (1 / 3) * rho_0 * L  (in MeV/fm^3).

4. Neutron Star Crust-Core Transition & Radius:
   Transition density rho_t from dynamical RPA instability:
     rho_t ~ 0.096 - 0.0005 * L  (in fm^-3)
   Neutron star radius scaling (1.4 M_sun):
     R_NS ~ 11.5 + 0.025 * L km.

References:
  - B. D. Serot and J. D. Walecka, Adv. Nucl. Phys. 16, 1 (1986).
  - M. Centelles et al., Phys. Rev. Lett. 102, 122502 (2009).
  - C. J. Horowitz and J. Piekarewicz, Phys. Rev. Lett. 86, 5647 (2001).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple

HBAR_C_MEV_FM = 197.327
RHO_0_DEFAULT = 0.153  # fm^-3

RMF_MODELS = {
    "NL3":      {"name": "NL3 (Lalazissis 1997)",     "J_MeV": 37.4, "L_MeV": 118.5, "M_star_ratio": 0.595, "g_rho": 8.97},
    "NL3_star": {"name": "NL3* (Lalazissis 2009)",    "J_MeV": 38.6, "L_MeV": 122.0, "M_star_ratio": 0.594, "g_rho": 9.10},
    "DD_ME2":   {"name": "DD-ME2 (Lalazissis 2005)",   "J_MeV": 32.3, "L_MeV": 51.2,  "M_star_ratio": 0.572, "g_rho": 7.30},
    "FSUGold":  {"name": "FSUGold (Todd-Rutel 2005)", "J_MeV": 32.6, "L_MeV": 60.5,  "M_star_ratio": 0.610, "g_rho": 7.80}
}


def calculate_rmf_symmetry_energy(
    rho: float,
    J_val_MeV: float = 32.5,
    L_val_MeV: float = 55.0,
    rho_0: float = 0.153
) -> Dict[str, float]:
    """
    Computes S(rho), slope L, pure neutron matter pressure, and crust-core transition.
    """
    x = (rho - rho_0) / (3.0 * rho_0)

    # Quadratic expansion S(rho) = J + L*x + 0.5*K_sym*x^2
    K_sym_MeV = -100.0  # typical curvature
    S_rho = J_val_MeV + L_val_MeV * x + 0.5 * K_sym_MeV * (x ** 2)

    # Pressure P = (1/3) * rho * [ L + K_sym * x ]
    P_PNM = (1.0 / 3.0) * rho * (L_val_MeV + K_sym_MeV * x)
    # Convert MeV/fm^3 to dyn/cm^2: 1 MeV/fm^3 = 1.6022e33 dyn/cm^2
    P_dyn = P_PNM * 1.6022e33

    # Crust-core transition density rho_t
    rho_t = 0.096 - 0.00045 * L_val_MeV
    rho_t = max(min(rho_t, 0.11), 0.05)

    # Predicted 1.4 M_sun neutron star radius
    R_ns_km = 11.5 + 0.022 * L_val_MeV

    return {
        "density_rho_fm3": round(rho, 4),
        "density_ratio_rho_over_rho0": round(rho / rho_0, 3),
        "symmetry_energy_S_MeV": round(S_rho, 2),
        "symmetry_energy_at_saturation_J_MeV": J_val_MeV,
        "slope_parameter_L_MeV": L_val_MeV,
        "P_PNM_MeV_fm3": round(P_PNM, 3),
        "P_PNM_dyn_cm2": P_dyn,
        "crust_core_transition_density_fm3": round(rho_t, 4),
        "predicted_NS_radius_1p4Msun_km": round(R_ns_km, 2)
    }


def scan_symmetry_energy_curve(
    J_val_MeV: float = 32.5,
    L_val_MeV: float = 55.0,
    rho_0: float = 0.153
) -> List[Dict[str, float]]:
    """
    Traces S(rho) from sub-saturation (0.2 rho_0) to supra-saturation (3.0 rho_0).
    """
    curve = []
    for step in range(2, 31, 2):
        rho = 0.1 * step * rho_0
        res = calculate_rmf_symmetry_energy(rho, J_val_MeV, L_val_MeV, rho_0)
        curve.append({
            "rho_over_rho0": res["density_ratio_rho_over_rho0"],
            "density_fm3": res["density_rho_fm3"],
            "S_rho_MeV": res["symmetry_energy_S_MeV"],
            "P_PNM_MeV_fm3": res["P_PNM_MeV_fm3"]
        })
    return curve


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   RMF NUCLEAR SYMMETRY ENERGY S(rho), SLOPE L & EOS ANALYZER")
    lines.append("=" * 72)

    pt = summary["saturation_point"]
    lines.append(f" NUCLEAR MATTER EQUATION OF STATE (Saturation rho_0 = {RHO_0_DEFAULT} fm^-3):")
    lines.append(f"   Bulk Symmetry Energy J         : {pt['symmetry_energy_at_saturation_J_MeV']} MeV")
    lines.append(f"   Symmetry Energy Slope L        : {pt['slope_parameter_L_MeV']} MeV")
    lines.append(f"   Pure Neutron Matter Pressure   : P_PNM = {pt['P_PNM_MeV_fm3']} MeV/fm^3 ({pt['P_PNM_dyn_cm2']:.2e} dyn/cm^2)")
    lines.append(f"   Crust-Core Transition Density  : rho_t = {pt['crust_core_transition_density_fm3']} fm^-3")
    lines.append(f"   Predicted 1.4 M_sun NS Radius  : R_NS = {pt['predicted_NS_radius_1p4Msun_km']} km")
    lines.append("-" * 72)

    if "density_scan" in summary:
        lines.append(" SYMMETRY ENERGY DENSITY DEPENDENCE S(rho):")
        lines.append(f"   {'rho / rho_0':<14} {'Density (fm^-3)':<16} {'S(rho) (MeV)':<16} {'P_PNM (MeV/fm^3)':<16}")
        lines.append("   " + "-" * 62)
        for row in summary["density_scan"]:
            lines.append(f"   {row['rho_over_rho0']:<14.1f} {row['density_fm3']:<16.3f} {row['S_rho_MeV']:<16.2f} {row['P_PNM_MeV_fm3']:<16.3f}")
        lines.append("-" * 72)

    lines.append(" Physical Significance:")
    lines.append("   - Slope L dictates neutron skin thickness in 208Pb and neutron star radii.")
    lines.append("   - Stiff models (NL3, L ~ 118 MeV) predict large R_NS ~ 14 km and thick skin.")
    lines.append("   - Soft models (DD-ME2, L ~ 51 MeV) agree with PREX-II and GW170817 constraints.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="RMF Nuclear Symmetry Energy S(rho) & Slope L Analyzer."
    )
    parser.add_argument("--model", type=str, default="DD_ME2", choices=list(RMF_MODELS.keys()),
                        help="Select standard RMF parameter set (NL3, NL3_star, DD_ME2, FSUGold)")
    parser.add_argument("--J", type=float, default=None, help="Custom bulk symmetry energy J in MeV")
    parser.add_argument("--L", type=float, default=None, help="Custom slope parameter L in MeV")
    parser.add_argument("--rho", type=float, default=0.153, help="Density rho in fm^-3 (default: 0.153)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    mod = RMF_MODELS[args.model]
    j_val = args.J if args.J is not None else mod["J_MeV"]
    l_val = args.L if args.L is not None else mod["L_MeV"]

    pt_res = calculate_rmf_symmetry_energy(args.rho, j_val, l_val)
    curve_res = scan_symmetry_energy_curve(j_val, l_val)

    summary = {
        "model_preset": mod["name"],
        "saturation_point": pt_res,
        "density_scan": curve_res
    }

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
