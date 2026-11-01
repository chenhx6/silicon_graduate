#!/usr/bin/env python3
"""
clover_compton_addback_polarization_calculator.py
=================================================
Clover HPGe Detector Compton Add-Back Enhancement, Linear Polarimetry &
Geometric Asymmetry Correction Analyzer.

Physics & Formulation:
----------------------
1. Clover Four-Crystal Array:
   Consists of four coaxial HPGe crystals (1, 2, 3, 4) in a 2x2 grid.
   - Direct mode: Energy deposited in single crystal alone.
   - Add-back mode: Energy summed across adjacent crystals firing in coincidence:
       E_total = E_i + E_j
     Add-back enhancement factor F_addback = Peak_Addback / Peak_Direct ~ 1.2 - 1.6
     at E_gamma > 1 MeV.

2. Compton Polarimetry & Klein-Nishina Scattering:
   Photons scatter preferentially perpendicular to their electric field polarization vector:
     - N_perp: Scattering perpendicular to beam reaction plane (crystals 1<->3, 2<->4).
     - N_para: Scattering parallel to beam reaction plane (crystals 1<->2, 3<->4).

3. Geometric Asymmetry Correction a_geom:
   Evaluated with unpolarized calibration source (e.g. 152Eu, 60Co):
     a_geom = N_perp_unpol / N_para_unpol (typically 0.95 - 1.05)
   Corrected experimental asymmetry:
     A_corr = (N_perp - a_geom * N_para) / (N_perp + a_geom * N_para)

4. Polarization Sensitivity Q(E_gamma) & True Linear Polarization P:
   P = A_corr / Q(E_gamma)
   Clover sensitivity parametrization:
     Q(E_gamma) ~ 0.22 * exp(-0.00035 * E_gamma_keV)  (for E_gamma in 200 - 2000 keV)
   - P > 0: Electric character (E1, E2).
   - P < 0: Magnetic character (M1, M2).

References:
  - G. Duchene et al., Nucl. Instrum. Methods A 432, 481 (1999) [The EUROGAM Clover].
  - P. M. Jones et al., Nucl. Instrum. Methods A 362, 556 (1995).
  - 吴治华, 《原子核物理实验方法》, 第三版.
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_clover_addback_factor(E_gamma_keV: float) -> Dict[str, float]:
    """
    Computes Compton add-back enhancement factor F_addback as a function of E_gamma.
    """
    E = max(E_gamma_keV, 50.0)
    # Empirical parameterization for 50x70 mm EUROGAM Clover
    # F ~ 1.05 + 0.48 * (1 - exp(-E / 650.0))
    f_addback = 1.05 + 0.48 * (1.0 - math.exp(-E / 650.0))
    percent_gain = (f_addback - 1.0) * 100.0

    return {
        "E_gamma_keV": E_gamma_keV,
        "addback_factor_F": round(f_addback, 3),
        "photopeak_efficiency_gain_percent": round(percent_gain, 1)
    }


def calculate_polarization_sensitivity(E_gamma_keV: float) -> float:
    """
    Computes Clover Compton polarization sensitivity factor Q(E_gamma).
    """
    E = max(E_gamma_keV, 100.0)
    # Empirical sensitivity: peaks around 300-500 keV (~0.22) and drops slowly
    q_val = 0.24 * math.exp(-0.00040 * E) + 0.02
    return max(min(q_val, 0.35), 0.05)


def analyze_clover_polarization(
    N_perp: float,
    N_parallel: float,
    E_gamma_keV: float,
    a_geom: float = 1.00,
    N_perp_err: Optional[float] = None,
    N_parallel_err: Optional[float] = None
) -> Dict[str, Any]:
    """
    Computes corrected Compton scattering asymmetry, linear polarization P,
    and assigns electromagnetic transition character (Electric vs Magnetic).
    """
    s_perp = math.sqrt(N_perp) if N_perp_err is None else N_perp_err
    s_para = math.sqrt(N_parallel) if N_parallel_err is None else N_parallel_err

    # Corrected asymmetry: A = (N_perp - a*N_para) / (N_perp + a*N_para)
    num = N_perp - a_geom * N_parallel
    den = N_perp + a_geom * N_parallel

    if den <= 0:
        return {"error": "Total scattering counts must be positive"}

    A_corr = num / den

    # Error propagation on asymmetry:
    # dA / dN_perp = 2*a*N_para / den^2
    # dA / dN_para = - 2*a*N_perp / den^2
    dA_dperp = (2.0 * a_geom * N_parallel) / (den ** 2)
    dA_dpara = (-2.0 * a_geom * N_perp) / (den ** 2)
    s_A = math.sqrt((dA_dperp * s_perp) ** 2 + (dA_dpara * s_para) ** 2)

    # Polarization sensitivity Q
    Q_factor = calculate_polarization_sensitivity(E_gamma_keV)

    # Linear polarization: P = A_corr / Q
    P_val = A_corr / Q_factor
    s_P = s_A / Q_factor

    # Parity assignment
    if P_val > 2.0 * s_P and P_val > 0.05:
        em_type = "Electric (E1, E2) [Positive Polarization]"
    elif P_val < -2.0 * s_P and P_val < -0.05:
        em_type = "Magnetic (M1, M2) [Negative Polarization]"
    else:
        em_type = "Ambiguous / Mixed Parity (P consistent with 0 within 2-sigma)"

    return {
        "E_gamma_keV": E_gamma_keV,
        "N_perpendicular": N_perp,
        "N_parallel": N_parallel,
        "geometric_factor_a_geom": a_geom,
        "corrected_asymmetry_A": round(A_corr, 4),
        "asymmetry_uncertainty": round(s_A, 4),
        "polarization_sensitivity_Q": round(Q_factor, 4),
        "linear_polarization_P": round(P_val, 4),
        "polarization_uncertainty": round(s_P, 4),
        "electromagnetic_character": em_type
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   CLOVER COMPTON ADDBACK & LINEAR POLARIMETRY ANALYZER")
    lines.append("=" * 72)

    ab = summary["addback"]
    lines.append(f" COMPTON ADDBACK PERFORMANCE (E_gamma = {ab['E_gamma_keV']} keV):")
    lines.append(f"   Add-Back Factor F_addback      : {ab['addback_factor_F']}")
    lines.append(f"   Full-Energy Efficiency Gain    : +{ab['photopeak_efficiency_gain_percent']}%")
    lines.append("-" * 72)

    if "polarization" in summary:
        pol = summary["polarization"]
        lines.append(" COMPTON POLARIMETRY & TRANSITION PARITY AUDIT:")
        lines.append(f"   Perpendicular Scattering N_perp: {pol['N_perpendicular']}")
        lines.append(f"   Parallel Scattering N_para     : {pol['N_parallel']}")
        lines.append(f"   Geometric Calibration a_geom   : {pol['geometric_factor_a_geom']}")
        lines.append(f"   Corrected Asymmetry A_corr     : {pol['corrected_asymmetry_A']} +/- {pol['asymmetry_uncertainty']}")
        lines.append(f"   Polarization Sensitivity Q     : {pol['polarization_sensitivity_Q']}")
        lines.append(f"   Linear Polarization P          : {pol['linear_polarization_P']} +/- {pol['polarization_uncertainty']}")
        lines.append(f"   Assigned Character             : {pol['electromagnetic_character']}")
        lines.append("-" * 72)

    lines.append(" Physical Significance:")
    lines.append("   - Add-back restores full photopeak efficiency lost to inter-crystal Compton scatter.")
    lines.append("   - Clover acts as an intrinsic polarimeter without external scatterers.")
    lines.append("   - Essential for resolving E1/M1 and E2/M2 parity ambiguities in in-beam level schemes.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Clover HPGe Addback & Linear Polarimetry Analyzer."
    )
    parser.add_argument("-E", "--energy", type=float, default=600.0, help="Gamma energy in keV (default: 600.0)")
    parser.add_argument("--n-perp", type=float, default=12500.0, help="Perpendicular scattering counts N_perp")
    parser.add_argument("--n-para", type=float, default=9800.0, help="Parallel scattering counts N_para")
    parser.add_argument("--a-geom", type=float, default=1.00, help="Geometric asymmetry factor (default: 1.00)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    ab_res = calculate_clover_addback_factor(args.energy)
    pol_res = analyze_clover_polarization(args.n_perp, args.n_para, args.energy, args.a_geom)

    summary = {
        "addback": ab_res,
        "polarization": pol_res
    }

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
