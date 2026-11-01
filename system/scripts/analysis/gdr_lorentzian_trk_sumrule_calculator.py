#!/usr/bin/env python3
"""
gdr_lorentzian_trk_sumrule_calculator.py
========================================
Giant Dipole Resonance (GDR) Lorentzian Line Shape, Deformation Splitting &
Thomas-Reiche-Kuhn (TRK) Classical Sum Rule Analyzer.

Physics & Formulation:
----------------------
1. Thomas-Reiche-Kuhn (TRK) Classical Energy-Weighted Sum Rule:
   sigma_0 = integral_0^inf sigma_abs(E) dE = 59.74 * (N * Z / A) MeV*mb
   With meson-exchange-current (MEC) enhancement kappa_TRK ~ 0.20 - 0.40:
     sigma_int = sigma_0 * (1 + kappa_TRK)

2. Average Spherical GDR Centroid:
   E_GDR_sph ~ 31.2 * A^(-1/3) + 20.6 * A^(-1/6) MeV   (Berman & Fultz 1975)
   For 208Pb: E_GDR ~ 13.5 MeV.

3. Deformed GDR Splitting (Danos Model):
   In axially deformed nuclei, oscillation splits into two distinct modes:
   - Mode 1 (along long axis z, K=0): E_1 = E_GDR / (1 + 0.66 * beta_2)
   - Mode 2 (perpendicular, K=1):      E_2 = E_GDR / (1 - 0.33 * beta_2)
   Axis ratio a/b ~ (1 + 0.63*beta_2) / (1 - 0.315*beta_2)
   Danos frequency ratio: E_2 / E_1 = 0.911 * (a/b) + 0.089.
   Inverts ground-state quadrupole deformation beta_2 directly from peak split!

4. Double Lorentzian Cross Section sigma_abs(E):
   sigma_abs(E) = sum_{k=1}^2 [ sigma_k * E^2 * Gamma_k^2 / ((E^2 - E_k^2)^2 + E^2 * Gamma_k^2) ]
   Area ratio: sigma_1 * Gamma_1 : sigma_2 * Gamma_2 = 1 : 2 (for prolate).

References:
  - W. Thomas, Naturwissenschaften 13, 627 (1925); F. Reiche and W. Kuhn, Z. Phys. 34, 510 (1925).
  - M. Danos, Nucl. Phys. 5, 23 (1958) [GDR in deformed nuclei].
  - B. L. Berman and S. C. Fultz, Rev. Mod. Phys. 47, 713 (1975).
  - 卢希庭, 《原子核物理（修订版）》, 第5章.
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_trk_sum_rule(Z: int, A: int, kappa_mec: float = 0.25) -> Dict[str, float]:
    """
    Computes classical TRK sum rule sigma_0 and MEC enhanced sum in MeV*mb.
    """
    N = A - Z
    sigma_0_MeV_mb = 59.74 * (float(N * Z) / float(A))
    sigma_enhanced = sigma_0_MeV_mb * (1.0 + kappa_mec)

    return {
        "A": A,
        "Z": Z,
        "N": N,
        "classical_TRK_sum_MeV_mb": round(sigma_0_MeV_mb, 1),
        "MEC_enhancement_kappa": kappa_mec,
        "total_enhanced_sum_MeV_mb": round(sigma_enhanced, 1)
    }


def calculate_deformed_gdr_splitting(
    Z: int,
    A: int,
    beta_2: float = 0.25
) -> Dict[str, Any]:
    """
    Computes GDR split peak energies E1 and E2 and inverts deformation.
    """
    A13 = A ** (1.0 / 3.0)
    A16 = A ** (1.0 / 6.0)
    E_sph = 31.2 / A13 + 20.6 / A16

    # Axis ratio a/b for prolate/oblate
    a_over_b = (1.0 + 0.63 * beta_2) / max(1.0 - 0.315 * beta_2, 0.1)

    # Danos relation: E2 / E1 = 0.911 * (a/b) + 0.089
    ratio_e2_e1 = 0.911 * a_over_b + 0.089

    # Constraint on centroid: (1/3) * E1 + (2/3) * E2 ~ E_sph
    E1 = 3.0 * E_sph / (1.0 + 2.0 * ratio_e2_e1)
    E2 = E1 * ratio_e2_e1

    # Typical widths
    Gamma1 = 3.2 + 0.8 * abs(beta_2)
    Gamma2 = 4.5 + 1.2 * abs(beta_2)

    # Peak heights ensuring TRK sum rule fulfillment
    trk = calculate_trk_sum_rule(Z, A)
    sig_tot = trk["total_enhanced_sum_MeV_mb"]
    # Integral of Lorentzian ~ (pi/2) * sigma_k * Gamma_k
    # (pi/2) * [ sigma1*Gamma1 + sigma2*Gamma2 ] = sig_tot
    # With area ratio 1:2 for prolate (beta_2 > 0)
    area1 = sig_tot / 3.0
    area2 = 2.0 * sig_tot / 3.0

    sigma1 = (2.0 / math.pi) * area1 / Gamma1
    sigma2 = (2.0 / math.pi) * area2 / Gamma2

    return {
        "spherical_GDR_centroid_MeV": round(E_sph, 2),
        "quadrupole_deformation_beta2": round(beta_2, 3),
        "axis_ratio_a_over_b": round(a_over_b, 3),
        "E1_low_mode_MeV": round(E1, 2),
        "Gamma1_width_MeV": round(Gamma1, 2),
        "sigma1_peak_mb": round(sigma1, 1),
        "E2_high_mode_MeV": round(E2, 2),
        "Gamma2_width_MeV": round(Gamma2, 2),
        "sigma2_peak_mb": round(sigma2, 1),
        "peak_splitting_Delta_E_MeV": round(abs(E2 - E1), 2),
        "energy_ratio_E2_over_E1": round(ratio_e2_e1, 3)
    }


def invert_beta2_from_gdr_peaks(E1_MeV: float, E2_MeV: float) -> float:
    """
    Inverts quadrupole deformation beta_2 from measured GDR peak positions E1, E2.
    """
    ratio = E2_MeV / max(E1_MeV, 0.1)
    # Danos: ratio = 0.911 * (a/b) + 0.089 -> a/b = (ratio - 0.089) / 0.911
    a_over_b = (ratio - 0.089) / 0.911
    # a/b ~ (1 + 0.63*beta) / (1 - 0.315*beta)
    # a/b - 0.315 * beta * a/b = 1 + 0.63 * beta
    # beta * (0.63 + 0.315 * a/b) = a/b - 1
    beta_inv = (a_over_b - 1.0) / (0.63 + 0.315 * a_over_b)
    return round(beta_inv, 3)


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   GIANT DIPOLE RESONANCE (GDR) & TRK SUM RULE ANALYZER")
    lines.append("=" * 72)

    trk = summary["trk_sum"]
    lines.append(f" NUCLEUS: Z = {trk['Z']}, N = {trk['N']}, A = {trk['A']}")
    lines.append(f"   Classical TRK Sum Rule sigma_0 : {trk['classical_TRK_sum_MeV_mb']} MeV*mb")
    lines.append(f"   MEC Enhanced Sum (kappa={trk['MEC_enhancement_kappa']}) : {trk['total_enhanced_sum_MeV_mb']} MeV*mb")
    lines.append("-" * 72)

    gdr = summary["deformed_gdr"]
    lines.append(" DEFORMED GDR DOUBLE-LORENTZIAN SPLITTING (Danos Model):")
    lines.append(f"   Spherical Equivalent Centroid  : {gdr['spherical_GDR_centroid_MeV']} MeV")
    lines.append(f"   Quadrupole Deformation beta_2  : {gdr['quadrupole_deformation_beta2']} (Axis Ratio a/b = {gdr['axis_ratio_a_over_b']})")
    lines.append(f"   Peak 1 (Long Axis, K=0)        : E1 = {gdr['E1_low_mode_MeV']} MeV, Gamma1 = {gdr['Gamma1_width_MeV']} MeV, sigma1 = {gdr['sigma1_peak_mb']} mb")
    lines.append(f"   Peak 2 (Short Axis, K=1)       : E2 = {gdr['E2_high_mode_MeV']} MeV, Gamma2 = {gdr['Gamma2_width_MeV']} MeV, sigma2 = {gdr['sigma2_peak_mb']} mb")
    lines.append(f"   GDR Splitting Delta_E = E2 - E1: {gdr['peak_splitting_Delta_E_MeV']} MeV (Ratio = {gdr['energy_ratio_E2_over_E1']})")
    lines.append("-" * 72)

    if "inversion" in summary:
        lines.append(f" DEFORMATION INVERSION TEST:")
        lines.append(f"   Reconstructed beta_2 from Peaks: {summary['inversion']['reconstructed_beta2']}")
        lines.append("-" * 72)

    lines.append(" Physical Significance:")
    lines.append("   - TRK sum rule is enhanced by ~25% due to sub-nucleonic meson exchange currents.")
    lines.append("   - GDR splits into two peaks in deformed nuclei, providing an optical caliper for beta_2.")
    lines.append("   - Decoupled K=0 and K=1 modes reflect prolate vs oblate elongation.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Giant Dipole Resonance (GDR) & TRK Sum Rule Analyzer."
    )
    parser.add_argument("-Z", type=int, default=68, help="Proton number Z (default: 68 for 166Er)")
    parser.add_argument("-A", type=int, default=166, help="Mass number A (default: 166)")
    parser.add_argument("--beta2", type=float, default=0.30, help="Quadrupole deformation beta_2 (default: 0.30)")
    parser.add_argument("--kappa", type=float, default=0.25, help="MEC enhancement factor (default: 0.25)")
    parser.add_argument("--invert", action="store_true", help="Demonstrate inversion from peaks")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    trk_res = calculate_trk_sum_rule(args.Z, args.A, args.kappa)
    gdr_res = calculate_deformed_gdr_splitting(args.Z, args.A, args.beta2)

    summary = {
        "trk_sum": trk_res,
        "deformed_gdr": gdr_res
    }

    if args.invert or args.beta2 == 0.30:
        b_inv = invert_beta2_from_gdr_peaks(gdr_res["E1_low_mode_MeV"], gdr_res["E2_high_mode_MeV"])
        summary["inversion"] = {"reconstructed_beta2": b_inv}

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
