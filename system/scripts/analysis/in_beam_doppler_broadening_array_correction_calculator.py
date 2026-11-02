#!/usr/bin/env python3
"""
in_beam_doppler_broadening_array_correction_calculator.py
=========================================================
In-Beam Relativistic Doppler Reconstruction, Finite Detector Opening Angle Broadening,
Recoil Velocity Dispersion & Neutron Evaporation Straggling Analyzer.

Physics & Formulation:
----------------------
1. Relativistic Doppler Transformation:
   When an excited nucleus moving with velocity vector beta = v / c emits a gamma ray of intrinsic energy E_0:
     E_lab(theta) = E_0 * [ sqrt(1 - beta^2) / (1 - beta * cos(theta)) ]
   where theta is the angle between the recoil trajectory and the photon emission direction.

2. Line Broadening Mechanisms:
   The total observed energy resolution FWHM_tot consists of intrinsic detector resolution
   and three kinematic broadening components:
     FWHM_tot = sqrt[ FWHM_intrinsic^2 + (Delta_E_theta)^2 + (Delta_E_beta)^2 + (Delta_E_strag)^2 ]

   a. Finite Detector Opening Angle Broadening (Delta_E_theta):
      A detector with full opening angle Delta_theta subtends a range of polar angles:
        Delta_E_theta = E_0 * [ (beta * sin(theta)) / (1 - beta * cos(theta)) ] * Delta_theta_rad
      - Maximum at theta = 90 deg (sin(theta) = 1.0) => dominant contributor in 90-deg rings!
      - Minimum at theta = 0 deg and 180 deg (sin(theta) = 0.0).

   b. Recoil Velocity Spread Broadening (Delta_E_beta):
      Dispersion Delta_beta arising from target thickness energy loss (dE/dx):
        Delta_E_beta = E_0 * | (cos(theta) - beta) / [ (1 - beta * cos(theta)) * sqrt(1 - beta^2) ] | * Delta_beta
      - Maximum at theta = 0 deg and 180 deg (|cos(theta)| = 1.0).
      - Minimum near theta = 90 deg.

   c. Recoil Angular Straggling from Neutron Evaporation (Delta_E_strag):
      When x neutrons are evaporated isotropically, each carrying momentum p_n ~ sqrt(2 * m_n * T_n):
        Total random recoil momentum kick: Delta_p_R ~ sqrt(x * 2 * m_n * T_n)
        Recoil deflection angle: Delta_theta_R ~ Delta_p_R / P_R = Delta_p_R / (M_R * beta * c)
        Doppler broadening contribution:
          Delta_E_strag ~ E_0 * beta * sin(theta) * Delta_theta_R

3. Optimization for In-Beam Experiment Proposals:
   - For standard HPGe arrays (Delta_theta ~ 7 - 10 deg): Delta_E_theta dominates at 90 deg.
   - For gamma tracking arrays (AGATA / GRETINA with pulse-shape analysis, Delta_theta ~ 1 - 2 deg):
     opening angle broadening is suppressed by a factor of 5-10, approaching the intrinsic HPGe limit (~2.0 keV).

References:
  - 吴治华, 《原子核物理实验方法（第三版）》, 原子能出版社 (2005), 第15章 §15.2 (印刷 pp. 421–445).
  - 汪晓莲等, 《粒子探测技术》, 中国科学技术大学出版社 (2009), 第5章 (高纯锗能谱测量).
  - P. J. Nolan and J. F. Sharpey-Schafer, Rep. Prog. Phys. 42, 1 (1979).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_doppler_broadening_budget(
    E0_keV: float,
    beta_recoil: float = 0.020,
    theta_deg: float = 90.0,
    opening_angle_deg: float = 8.0,
    delta_beta_relative_pct: float = 10.0,
    recoil_mass_amu: float = 134.0,
    num_neutrons: int = 4,
    T_neutron_MeV: float = 2.5,
    intrinsic_fwhm_keV: float = 2.0
) -> Dict[str, Any]:
    """
    Calculates the full relativistic Doppler shift, finite angle broadening,
    velocity dispersion, neutron recoil kick straggling, and total peak FWHM.
    """
    if E0_keV <= 0.0:
        raise ValueError("Gamma energy E0 must be strictly positive.")
    if not (0.0 < beta_recoil < 1.0):
        raise ValueError("Recoil velocity beta must be between 0 and 1.")
    if opening_angle_deg < 0.0:
        raise ValueError("Detector opening angle must be nonnegative.")

    theta_rad = math.radians(theta_deg)
    d_theta_rad = math.radians(opening_angle_deg)
    gamma_rel = 1.0 / math.sqrt(1.0 - beta_recoil ** 2)

    # 1. Relativistic shifted energy: E_lab = E0 * sqrt(1 - beta^2) / (1 - beta * cos(theta))
    denom = 1.0 - beta_recoil * math.cos(theta_rad)
    E_lab_keV = E0_keV * math.sqrt(1.0 - beta_recoil ** 2) / denom
    shift_keV = E_lab_keV - E0_keV

    # 2. Finite detector opening angle broadening:
    # Delta_E_theta = E0 * [ beta * sin(theta) / (1 - beta * cos(theta)) ] * Delta_theta
    dE_theta_keV = E0_keV * (beta_recoil * math.sin(theta_rad) / denom) * d_theta_rad

    # 3. Recoil velocity spread broadening:
    # Delta_beta = beta * (pct / 100)
    delta_beta = beta_recoil * (delta_beta_relative_pct / 100.0)
    dE_dbeta_factor = abs(math.cos(theta_rad) - beta_recoil) / (denom * math.sqrt(1.0 - beta_recoil ** 2))
    dE_beta_keV = E0_keV * dE_dbeta_factor * delta_beta

    # 4. Neutron evaporation kick straggling:
    # p_n = sqrt(2 * m_n * T_n), Delta_p_R ~ sqrt(x * 2 * m_n * T_n)
    # Recoil momentum: P_R = M_R * beta * c
    m_n_MeV = 939.565
    m_u_MeV = 931.494
    M_R_MeV = recoil_mass_amu * m_u_MeV

    delta_p_recoil_MeV = math.sqrt(float(num_neutrons) * 2.0 * m_n_MeV * T_neutron_MeV)
    P_recoil_MeV = M_R_MeV * beta_recoil # in MeV/c
    delta_theta_R_rad = delta_p_recoil_MeV / P_recoil_MeV if P_recoil_MeV > 0 else 0.0
    dE_strag_keV = E0_keV * beta_recoil * math.sin(theta_rad) * delta_theta_R_rad

    # Total peak width FWHM: quadrature sum
    fwhm_total_keV = math.sqrt(
        intrinsic_fwhm_keV ** 2 +
        dE_theta_keV ** 2 +
        dE_beta_keV ** 2 +
        dE_strag_keV ** 2
    )

    return {
        "E0_keV": E0_keV,
        "recoil_velocity_beta": beta_recoil,
        "detector_angle_deg": theta_deg,
        "detector_opening_angle_deg": opening_angle_deg,
        "E_lab_shifted_keV": round(E_lab_keV, 2),
        "Doppler_shift_keV": round(shift_keV, 2),
        "intrinsic_detector_fwhm_keV": intrinsic_fwhm_keV,
        "broadening_detector_angle_dE_theta_keV": round(dE_theta_keV, 2),
        "broadening_velocity_spread_dE_beta_keV": round(dE_beta_keV, 2),
        "broadening_neutron_straggling_dE_strag_keV": round(dE_strag_keV, 2),
        "total_observed_fwhm_keV": round(fwhm_total_keV, 2),
        "recoil_angular_straggling_deg": round(math.degrees(delta_theta_R_rad), 2)
    }


def compare_detector_rings(
    E0_keV: float,
    beta_recoil: float = 0.020,
    opening_angle_deg: float = 8.0,
    angles_deg: Optional[List[float]] = None
) -> List[Dict[str, Any]]:
    """Compares Doppler shift and broadening budget across standard detector ring angles."""
    if angles_deg is None:
        angles_deg = [30.0, 50.0, 90.0, 130.0, 150.0]

    rings = []
    for ang in angles_deg:
        res = calculate_doppler_broadening_budget(
            E0_keV, beta_recoil=beta_recoil, theta_deg=ang, opening_angle_deg=opening_angle_deg
        )
        rings.append({
            "angle_deg": ang,
            "E_lab_keV": res["E_lab_shifted_keV"],
            "shift_keV": res["Doppler_shift_keV"],
            "dE_theta_keV": res["broadening_detector_angle_dE_theta_keV"],
            "dE_beta_keV": res["broadening_velocity_spread_dE_beta_keV"],
            "total_fwhm_keV": res["total_observed_fwhm_keV"]
        })
    return rings


def format_text_report(bd: Dict[str, Any], rings: Optional[List[Dict[str, Any]]] = None) -> str:
    lines = [
        "=" * 76,
        "   IN-BEAM RELATIVISTIC DOPPLER BROADENING & ARRAY RESOLUTION SUITE",
        "   Based on Wu Zhihua Ch. 15, Wang Xiaolian Ch. 5 & Nolan (1979)",
        "=" * 76,
        f" RECOIL KINEMATICS & DETECTOR GEOMETRY:",
        f"   Intrinsic Gamma Energy E_0  : {bd['E0_keV']:.1f} keV",
        f"   Recoil Velocity beta = v/c  : {bd['recoil_velocity_beta']:.4f}  ({bd['recoil_velocity_beta']*100:.2f}% speed of light)",
        f"   Detector Polar Angle theta  : {bd['detector_angle_deg']:.1f} deg (Opening Angle: {bd['detector_opening_angle_deg']:.1f} deg)",
        f"   Shifted Lab Energy E_lab    : {bd['E_lab_shifted_keV']:.2f} keV (Doppler Shift: {bd['Doppler_shift_keV']:+.2f} keV)",
        "-" * 76,
        " DOPPLER BROADENING BUDGET & LINE WIDTH BREAKDOWN:",
        f"   Intrinsic HPGe Resolution   : {bd['intrinsic_detector_fwhm_keV']:.2f} keV",
        f"   Detector Angle Broadening   : {bd['broadening_detector_angle_dE_theta_keV']:.2f} keV  [E0 * beta * sin(theta) * Delta_theta]",
        f"   Velocity Spread Broadening  : {bd['broadening_velocity_spread_dE_beta_keV']:.2f} keV  [from target energy loss Delta_beta]",
        f"   Neutron Kick Straggling     : {bd['broadening_neutron_straggling_dE_strag_keV']:.2f} keV  (Recoil deflection: {bd['recoil_angular_straggling_deg']:.2f} deg)",
        f"   TOTAL OBSERVED PEAK FWHM    : {bd['total_observed_fwhm_keV']:.2f} keV  (Degradation factor: {bd['total_observed_fwhm_keV']/bd['intrinsic_detector_fwhm_keV']:.2f}x)",
        "-" * 76,
    ]

    if rings is not None:
        lines.extend([
            " DETECTOR ARRAY RING COMPARISON (30 deg to 150 deg):",
            "   Ring Angle     E_lab (keV)     Shift (keV)     dE_theta     dE_beta     Total FWHM",
        ])
        for r in rings:
            lines.append(f"     {r['angle_deg']:5.1f} deg    {r['E_lab_keV']:10.2f}    {r['shift_keV']:+10.2f}     {r['dE_theta_keV']:7.2f}     {r['dE_beta_keV']:7.2f}     {r['total_fwhm_keV']:8.2f} keV")
        lines.append("-" * 76)

    lines.extend([
        " Methodological Guidelines for In-Beam Experiment Design:",
        "   - At 90 deg, sin(theta) = 1.0 maximizes opening angle broadening; thin collimators are essential.",
        "   - At forward/backward angles (30/150 deg), angle broadening is small, but velocity spread dominates.",
        "   - Gamma tracking arrays (AGATA/GRETINA) reduce Delta_theta to ~1 deg, recovering intrinsic FWHM.",
        "=" * 76
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="In-Beam Relativistic Doppler Broadening Analyzer"
    )
    parser.add_argument("--E0", type=float, default=1000.0, help="Intrinsic gamma energy in keV (default: 1000.0 keV)")
    parser.add_argument("--beta", type=float, default=0.020, help="Recoil velocity v/c (default: 0.020)")
    parser.add_argument("--theta", type=float, default=90.0, help="Detector angle in deg (default: 90.0 deg)")
    parser.add_argument("--opening-angle", type=float, default=8.0, help="Detector full opening angle in deg (default: 8.0 deg)")
    parser.add_argument("--preset", type=str, default="134Ce_in_beam",
                        choices=["134Ce_in_beam", "agata_tracking_array", "gammasphere_standard"],
                        help="Benchmark preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")

    args = parser.parse_args()

    e0 = args.E0
    beta = args.beta
    theta = args.theta
    d_theta = args.opening_angle

    if args.preset == "134Ce_in_beam":
        e0, beta, theta, d_theta = 1000.0, 0.020, 90.0, 8.0
    elif args.preset == "agata_tracking_array":
        e0, beta, theta, d_theta = 1000.0, 0.025, 90.0, 1.2 # Tracking PSA position resolution
    elif args.preset == "gammasphere_standard":
        e0, beta, theta, d_theta = 1000.0, 0.020, 90.0, 7.5

    res = calculate_doppler_broadening_budget(e0, beta_recoil=beta, theta_deg=theta, opening_angle_deg=d_theta)
    rings = compare_detector_rings(e0, beta_recoil=beta, opening_angle_deg=d_theta)

    if args.json:
        out = {"budget": res, "rings_comparison": rings}
        print(json.dumps(out, indent=2))
    else:
        print(format_text_report(res, rings))


if __name__ == "__main__":
    main()
