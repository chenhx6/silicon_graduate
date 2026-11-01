#!/usr/bin/env python3
"""
In-Beam Gamma-Gamma Coincidence Matrix Gating & Level Intensity Balancer.

Based on:
  - Wu Zhihua (2005), "Nuclear Physics Experimental Methods" (Section 10.3)
  - D. C. Radford, Nucl. Instr. Meth. A 361, 297 (1995) (Radware ESCL8R algorithms)

Features:
  1. Standard 3-point background-subtracted 1D spectrum projection from 2D coincidence matrix.
  2. Standard Radware HPGe array efficiency calibration formula.
  3. Rigorous level intensity balance checker with internal conversion (BrIcc) correction.
"""

import numpy as np
import json
import argparse
import sys
from typing import Dict, Any, List


def three_point_background_subtraction(peak_slice, bg_left_slice, bg_right_slice,
                                       w_peak, w_bg_left, w_bg_right):
    """
    Standard 3-point background subtraction for 1D gated slice from 2D coincidence matrix.
    S(E) = Peak(E) - f_B * [BG_left(E) + BG_right(E)]
    where f_B = w_peak / (w_bg_left + w_bg_right)
    """
    p = np.array(peak_slice, dtype=float)
    bl = np.array(bg_left_slice, dtype=float)
    br = np.array(bg_right_slice, dtype=float)
    
    total_bg_width = w_bg_left + w_bg_right
    if total_bg_width <= 0:
        raise ValueError("Background gate widths must be positive.")
        
    f_B = w_peak / total_bg_width
    subtracted = p - f_B * (bl + br)
    
    # Propagate Poisson counting uncertainties
    # var(S) = var(P) + f_B^2 * (var(BL) + var(BR)) approx P + f_B^2 * (BL + BR)
    errors = np.sqrt(np.maximum(1.0, p) + (f_B**2) * np.maximum(1.0, bl + br))
    
    return subtracted, errors, f_B


def hpge_efficiency_radware(E_gamma_keV, A=7.5, B=0.8, C=0.0, D=5.2, E_param=-0.7, F=0.05, G=15.0):
    """
    Radware standard parameterization for HPGe detector array efficiency.
    ln(eff) = [ (A + B*x + C*x^2)^(-G) + (D + E*y + F*y^2)^(-G) ]^(-1/G)
    where x = ln(E / 100 keV), y = ln(E / 1000 keV).
    """
    E = np.maximum(20.0, np.array(E_gamma_keV, dtype=float))
    x = np.log(E / 100.0)
    y = np.log(E / 1000.0)
    
    term_low = (A + B * x + C * x**2)
    term_high = (D + E_param * y + F * y**2)
    
    # Guard against negative values in log domain
    term_low = np.maximum(0.1, term_low)
    term_high = np.maximum(0.1, term_high)
    
    ln_eff = ((term_low**(-G)) + (term_high**(-G)))**(-1.0 / G)
    # Return relative efficiency (typically normalized to 1.0 or 100 at 1 MeV or 1.33 MeV)
    eff = np.exp(ln_eff)
    return eff / 100.0 # Normalized scale


def check_level_intensity_balance(inflow_transitions, outflow_transitions):
    """
    Check topology intensity balance for an intermediate nuclear level:
      Total Inflow == Total Outflow
    
    Each transition dict contains:
      - "name": str
      - "net_area": float
      - "net_area_err": float
      - "efficiency": float (detector efficiency)
      - "alpha_tot": float (internal conversion coefficient, default 0.0)
    """
    def sum_intensity(trans_list):
        I_tot = 0.0
        var_tot = 0.0
        for t in trans_list:
            area = t["net_area"]
            d_area = t.get("net_area_err", np.sqrt(max(1.0, area)))
            eff = max(1e-6, t.get("efficiency", 1.0))
            alpha = t.get("alpha_tot", 0.0)
            
            # Photon emission intensity
            I_gamma = area / eff
            # Total transition intensity including conversion electrons
            I_t = I_gamma * (1.0 + alpha)
            I_tot += I_t
            
            dI_t = (d_area / eff) * (1.0 + alpha)
            var_tot += dI_t**2
        return I_tot, np.sqrt(var_tot)
        
    I_in, err_in = sum_intensity(inflow_transitions)
    I_out, err_out = sum_intensity(outflow_transitions)
    
    diff = I_out - I_in
    diff_err = np.sqrt(err_in**2 + err_out**2)
    sigma_discrepancy = diff / max(1e-6, diff_err)
    
    is_balanced = bool(abs(sigma_discrepancy) <= 3.0)
    
    return {
        "total_inflow": I_in,
        "inflow_err": err_in,
        "total_outflow": I_out,
        "outflow_err": err_out,
        "difference_out_minus_in": diff,
        "difference_err": diff_err,
        "sigma_discrepancy": sigma_discrepancy,
        "is_balanced_within_3sigma": is_balanced
    }


def format_text_report(balance: Dict[str, Any]) -> str:
    lines = [
        "=" * 74,
        "   IN-BEAM GAMMA-GAMMA COINCIDENCE MATRIX & LEVEL INTENSITY BALANCER",
        "   Based on Wu Zhihua (Experimental Nuclear Physics) & Radford (RadWare ESCL8R)",
        "=" * 74,
        f" LEVEL INTENSITY BALANCE VERIFICATION:",
        f"   Total Feeding Inflow : {balance['total_inflow']:.1f} +/- {balance['inflow_err']:.1f}",
        f"   Total Decay Outflow  : {balance['total_outflow']:.1f} +/- {balance['outflow_err']:.1f}",
        f"   Net Discrepancy      : {balance['difference_out_minus_in']:+.1f} +/- {balance['difference_err']:.1f}",
        f"   Statistical Pull     : {balance['sigma_discrepancy']:+.2f} sigma",
        f"   Status Assessment    : {'LEVEL IS BALANCED WITHIN 3-SIGMA!' if balance['is_balanced_within_3sigma'] else 'UNBALANCED! Check for missing transitions.'}",
        "-" * 74,
        " Physical & Methodological Synthesis:",
        "   - Intensity balancing accounts for gamma detection efficiency and internal conversion.",
        "   - A statistically significant positive difference (outflow > inflow) indicates unobserved",
        "     side feeding or unrecognized cascade branches populating the state.",
        "   - Negative difference indicates missing unobserved low-energy or highly-converted decays.",
        "=" * 74
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="In-Beam Gamma-Gamma Coincidence Matrix Gating & Level Intensity Balancer"
    )
    parser.add_argument("--in-area", type=float, default=7000.0,
                        help="Total inflow net peak area")
    parser.add_argument("--in-eff", type=float, default=0.045,
                        help="Average inflow detector efficiency")
    parser.add_argument("--in-icc", type=float, default=0.01,
                        help="Average inflow internal conversion coefficient (alpha)")
    parser.add_argument("--out-area", type=float, default=8800.0,
                        help="Total outflow net peak area")
    parser.add_argument("--out-eff", type=float, default=0.052,
                        help="Average outflow detector efficiency")
    parser.add_argument("--out-icc", type=float, default=0.015,
                        help="Average outflow internal conversion coefficient (alpha)")
    parser.add_argument("--json", action="store_true",
                        help="Output pure JSON")

    args = parser.parse_args()

    inflows = [{"name": "Inflow", "net_area": args.in_area, "efficiency": args.in_eff, "alpha_tot": args.in_icc}]
    outflows = [{"name": "Outflow", "net_area": args.out_area, "efficiency": args.out_eff, "alpha_tot": args.out_icc}]
    balance = check_level_intensity_balance(inflows, outflows)

    if args.json:
        print(json.dumps(balance, indent=2))
    else:
        print(format_text_report(balance))


if __name__ == "__main__":
    main()
