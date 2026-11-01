#!/usr/bin/env python3
"""Illustrative TRK sum and axial GDR splitting parameterization.

Phenomenological widths, enhancement and axis-ratio assumptions are not fitted
to experimental data. Forward/inverse consistency is not a measured deformation
uncertainty. This is not a general three-axis triaxial GDR calculation.
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
    if not isinstance(A, int) or not isinstance(Z, int) or A <= 0 or not 0 <= Z <= A:
        raise ValueError("Require integer A > 0 and 0 <= Z <= A")
    if not math.isfinite(kappa_mec) or kappa_mec < 0:
        raise ValueError("Enhancement kappa must be finite and nonnegative")
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
    calculate_trk_sum_rule(Z, A)
    if not math.isfinite(beta_2) or not 0 <= beta_2 < 1:
        raise ValueError("This illustrative prolate model requires 0 <= beta2 < 1")
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
        "calculation_status": "illustrative-axial-parameterization",
        "evidence_boundary": "Assumed deformation, widths and enhancement; not measured nuclear data",
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
    if not all(math.isfinite(v) and v > 0 for v in (E1_MeV, E2_MeV)):
        raise ValueError("Peak energies must be finite and positive")
    if E2_MeV < E1_MeV:
        raise ValueError("The prolate-axis convention requires E2 >= E1")
    ratio = E2_MeV / E1_MeV
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
    lines.append("   ILLUSTRATIVE GDR & TRK PARAMETERIZATION - NOT FITTED DATA")
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
    lines.append("   - Enhancement is a supplied model parameter, not a measured or unique MEC contribution.")
    lines.append("   - This axial two-mode demonstration does not implement general triaxial three-mode response.")
    lines.append("   - Inverting the same model is an algebra check, not an experimental uncertainty estimate.")
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
