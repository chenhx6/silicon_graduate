#!/usr/bin/env python3
"""
internal_pair_creation_ipc_calculator.py
========================================
Internal Pair Creation (IPC) Coefficients, Electron-Positron (e+ e-) Angular
Correlation & High-Energy E0/E1/M1/E2 Transition Analyzer.

Physics & Formulation:
----------------------
1. Internal Pair Creation Threshold:
   Allowed only when transition energy E_gamma > 2 * m_e * c^2 = 1.022 MeV.
   Total kinetic energy of pair: T_+ + T_- = E_gamma - 2 * m_e * c^2.

2. Born Approximation for IPC Coefficients alpha_pi = Gamma_pi / Gamma_gamma:
   - E1 multipole:
     alpha_pi(E1) ~ (alpha / pi) * (2/3) * [ ln(2 * E_gamma / m_e) - 5/3 ]
   - M1 multipole:
     alpha_pi(M1) ~ (alpha / pi) * (2/3) * [ ln(2 * E_gamma / m_e) - 8/3 ]
   - E2 multipole:
     alpha_pi(E2) ~ (alpha / pi) * (4/15) * [ ln(2 * E_gamma / m_e) - 29/15 ]
   Unlike electronic internal conversion (which drops as E^-3.5), IPC coefficients
   GROW logarithmically with energy, dominating at E_gamma > 5 - 10 MeV.

3. Pure Electric Monopole (E0) Pair Decay:
   For 0+ -> 0+ transitions (e.g. 16O 6.05 MeV, 4He 20.21 MeV, 40Ca 3.35 MeV),
   single gamma emission is forbidden (Gamma_gamma = 0).
   Pair transition width:
     Gamma_pi(E0) = (2 * alpha^2 / (3 * pi)) * m_e * c^2 * rho^2(E0) * Omega_pi(E0)

4. Electron-Positron (e+ e-) Angular Correlation dW / d(theta):
   theta: opening angle between emitted electron and positron.
   - E0 multipole: dW/d(theta) ~ sin(theta) * (1 + cos(theta))  (symmetric, broad peak around 90 deg).
   - E1 multipole: Forward peaked (small theta ~ 20 - 45 deg).
   - M1 multipole: Intermediate to backward peaked (~ 100 - 140 deg).
   - Hypothetical particle (X17 boson) anomaly signature:
       theta_peak = 2 * arcsin(m_X / E_gamma).

References:
  - M. E. Rose, Phys. Rev. 76, 678 (1949).
  - P. Schlüter, G. Soff, and W. Greiner, Phys. Rep. 75, 327 (1981).
  - 卢希庭, 《原子核物理（修订版）》, 第5章 电磁跃迁.
  - A. J. Krasznahorkay et al., Phys. Rev. Lett. 116, 042501 (2016).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple

M_E_MEV = 0.51099895
TWO_M_E_MEV = 1.0219979
ALPHA_QED = 1.0 / 137.035999


def calculate_ipc_coefficient(
    E_gamma_MeV: float,
    multipolarity: str = "E1"
) -> Dict[str, Any]:
    """
    Computes Internal Pair Creation coefficient alpha_pi = Gamma_pi / Gamma_gamma.
    """
    if E_gamma_MeV <= TWO_M_E_MEV:
        return {
            "E_gamma_MeV": E_gamma_MeV,
            "multipolarity": multipolarity,
            "alpha_pi": 0.0,
            "status": "Below_Pair_Creation_Threshold (E < 1.022 MeV)"
        }

    k = E_gamma_MeV / M_E_MEV
    ln_2k = math.log(max(2.0 * k, 1.0))
    mult = multipolarity.upper()

    if mult == "E1":
        # Rose formula for E1
        alpha_pi = (ALPHA_QED / math.pi) * (2.0 / 3.0) * (ln_2k - (5.0 / 3.0))
    elif mult == "M1":
        # Rose formula for M1
        alpha_pi = (ALPHA_QED / math.pi) * (2.0 / 3.0) * (ln_2k - (8.0 / 3.0))
    elif mult == "E2":
        # Rose formula for E2
        alpha_pi = (ALPHA_QED / math.pi) * (4.0 / 15.0) * (ln_2k - (29.0 / 15.0))
    elif mult == "M2":
        alpha_pi = (ALPHA_QED / math.pi) * (4.0 / 15.0) * (ln_2k - (34.0 / 15.0))
    elif mult == "E0":
        # For E0, single gamma is forbidden
        return {
            "E_gamma_MeV": E_gamma_MeV,
            "multipolarity": "E0 (Pure Monopole)",
            "alpha_pi": float("inf"),
            "status": "Single_Gamma_Forbidden (Decays purely by e-e+ pairs and conversion electrons)"
        }
    else:
        alpha_pi = (ALPHA_QED / math.pi) * (1.0 / 3.0) * ln_2k

    alpha_pi = max(alpha_pi, 1e-6)

    return {
        "E_gamma_MeV": E_gamma_MeV,
        "multipolarity": mult,
        "pair_excess_energy_MeV": round(E_gamma_MeV - TWO_M_E_MEV, 4),
        "alpha_pi": round(alpha_pi, 6),
        "alpha_pi_percentage": round(alpha_pi * 100.0, 4),
        "status": "Above_Threshold (Pair production active)"
    }


def calculate_angular_correlation(
    E_gamma_MeV: float,
    multipolarity: str = "E1",
    theta_deg: float = 90.0,
    m_X_boson_MeV: Optional[float] = None
) -> Dict[str, Any]:
    """
    Computes angular distribution dW/d(theta) for e+ e- pairs at opening angle theta (deg).
    Also checks hypothetical X17 resonance angle if mass is given.
    """
    if E_gamma_MeV <= TWO_M_E_MEV:
        return {"error": "Energy below threshold"}

    theta_rad = math.radians(theta_deg)
    sin_th = math.sin(theta_rad)
    cos_th = math.cos(theta_rad)
    mult = multipolarity.upper()

    # Standard QED angular correlation functions
    if mult == "E0":
        # E0 distribution: symmetric, broad maximum near 90 deg
        dw_dtheta = sin_th * (1.0 + 0.5 * (cos_th ** 2))
    elif mult == "E1":
        # E1 forward peaked: 1 - cos(theta) suppression at 180
        denom = max(1.0 - 0.9 * cos_th, 0.05)
        dw_dtheta = sin_th / (denom ** 1.5)
    elif mult == "M1":
        # M1 peaked at intermediate to large angles
        denom = max(1.0 + 0.7 * cos_th, 0.05)
        dw_dtheta = sin_th * (1.0 + cos_th ** 2) / (denom ** 0.5)
    else:
        dw_dtheta = sin_th

    # X17 boson anomaly check: two-body decay resonance peak angle
    x17_info = {}
    if m_X_boson_MeV is not None and m_X_boson_MeV < E_gamma_MeV:
        ratio = m_X_boson_MeV / E_gamma_MeV
        if ratio < 1.0:
            theta_res_rad = 2.0 * math.asin(ratio)
            theta_res_deg = math.degrees(theta_res_rad)
            x17_info = {
                "boson_mass_mX_MeV": m_X_boson_MeV,
                "resonance_peak_angle_deg": round(theta_res_deg, 1),
                "is_near_peak": abs(theta_deg - theta_res_deg) < 5.0
            }

    return {
        "E_gamma_MeV": E_gamma_MeV,
        "multipolarity": mult,
        "opening_angle_deg": theta_deg,
        "differential_rate_arbitrary_units": round(dw_dtheta, 4),
        "exotic_boson_resonance": x17_info
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   INTERNAL PAIR CREATION (IPC) & e+ e- CORRELATION ANALYZER")
    lines.append("=" * 72)

    ipc = summary["ipc_coefficient"]
    lines.append(f" TRANSITION PARAMETERS: E_gamma = {ipc['E_gamma_MeV']} MeV, Multipolarity = {ipc['multipolarity']}")
    lines.append(f"   Status                         : {ipc['status']}")
    if "alpha_pi" in ipc and ipc["alpha_pi"] != float("inf"):
        lines.append(f"   Pair Kinetic Energy Available  : {ipc['pair_excess_energy_MeV']} MeV")
        lines.append(f"   IPC Coefficient alpha_pi       : {ipc['alpha_pi']:.6f} ({ipc['alpha_pi_percentage']}%)")
    lines.append("-" * 72)

    if "angular_distribution" in summary:
        ang = summary["angular_distribution"]
        lines.append(" e+ e- OPENING ANGLE CORRELATION dW/d(theta):")
        lines.append(f"   Opening Angle theta            : {ang['opening_angle_deg']} deg")
        lines.append(f"   Differential Rate dW/d(theta)  : {ang['differential_rate_arbitrary_units']}")
        if "exotic_boson_resonance" in ang and ang["exotic_boson_resonance"]:
            x = ang["exotic_boson_resonance"]
            lines.append("   ATOMKI X17 BOSON RESONANCE HYPOTHESIS:")
            lines.append(f"     Hypothetical Boson Mass m_X  : {x['boson_mass_mX_MeV']} MeV")
            lines.append(f"     Predicted Resonant Peak Angle: {x['resonance_peak_angle_deg']} deg")
            lines.append(f"     Observation Match Near Peak  : {x['is_near_peak']}")
        lines.append("-" * 72)

    lines.append(" Physical Significance:")
    lines.append("   - IPC dominates high-energy transitions (E > 5-10 MeV), growing with energy.")
    lines.append("   - Pure E0 transitions (0+ -> 0+) decay solely via IPC and internal conversion.")
    lines.append("   - e+ e- angular correlations distinguish multipolarities and test ATOMKI anomaly.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Internal Pair Creation (IPC) & e+ e- Angular Correlation Analyzer."
    )
    parser.add_argument("-E", "--energy", type=float, required=True, help="Transition energy E_gamma in MeV")
    parser.add_argument("-L", "--mult", type=str, default="E1", choices=["E0", "E1", "M1", "E2", "M2"],
                        help="Transition multipolarity (default: E1)")
    parser.add_argument("--theta", type=float, default=90.0, help="Opening angle in degrees (default: 90.0)")
    parser.add_argument("--mX", type=float, default=None, help="Hypothetical boson mass in MeV (e.g. 17.0 for ATOMKI)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    ipc_res = calculate_ipc_coefficient(args.energy, args.mult)
    ang_res = calculate_angular_correlation(args.energy, args.mult, args.theta, args.mX)

    summary = {
        "ipc_coefficient": ipc_res,
        "angular_distribution": ang_res
    }

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
