#!/usr/bin/env python3
"""
linear_momentum_transfer_incomplete_fusion_calculator.py
========================================================
Heavy-Ion Linear Momentum Transfer (LMT), Incomplete Fusion (ICF) &
Binary Fission Fragment Folding Angle Simulator.

Physics & Formulation:
----------------------
1. Incident Projectile Kinematics:
   - Beam velocity: v_0 = c * sqrt(2 * E_lab / (A_p * m_u))
   - Full incident momentum: p_0 = A_p * m_u * v_0
   - Complete Fusion recoil velocity:
     v_rec_CF = v_0 * A_p / (A_p + A_t)

2. Incomplete Fusion (ICF) & Fractional LMT:
   Fractional linear momentum transfer:
     rho = Delta_p / p_0 = v_rec / v_rec_CF
   Transferred projectile mass:
     A_trans = rho * A_p
   Escaped spectator mass:
     A_spec = A_p - A_trans
   Compound excitation energy:
     E_ex = E_cm_trans + Q_fus(A_trans + A_t)

3. Binary Fission Fragment Folding Angle (theta_fold):
   In the frame of the moving recoil nucleus, symmetric binary fission emits
   fragments back-to-back (180 deg) with velocity:
     v_frag = sqrt(2 * TKE / (A_f1 * m_u))   (TKE from Viola systematics)
   In the laboratory frame, the forward boost bends the opening angle:
     tan(theta_fold / 2) = v_frag / v_rec
     theta_fold = 2 * arctan(v_frag / v_rec)
   - Zero momentum transfer (v_rec = 0): theta_fold = 180 deg.
   - Complete fusion (v_rec maximum): theta_fold is minimal (typically 150 - 165 deg).
   - Incomplete fusion: theta_fold intermediate between CF and 180 deg.

References:
  - V. E. Viola et al., Phys. Rev. C 26, 178 (1982).
  - M. B. Tsang et al., Phys. Rev. C 28, 2163 (1983).
  - 林承键, 《重离子核反应》, 科学出版社.
  - C. A. Bertulani and P. Danielewicz, Introduction to Nuclear Reactions, CRC Press.
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple

U_MEV = 931.494
C_LIGHT_KM_S = 299792.458


def calculate_linear_momentum_transfer(
    A_p: int,
    Z_p: int,
    A_t: int,
    Z_t: int,
    E_lab_MeV: float,
    fractional_LMT: float = 1.0,
    TKE_fission_MeV: Optional[float] = None
) -> Dict[str, Any]:
    """
    Computes kinematics of complete vs incomplete fusion and predicts
    the fission fragment folding angle theta_fold.
    """
    rho = max(min(fractional_LMT, 1.0), 0.05)

    # Incident beam velocity in units of c
    m_p_total = A_p * U_MEV
    # Relativistic beta: E_tot = m_p + E_lab
    gamma_beam = 1.0 + (E_lab_MeV / m_p_total)
    beta_0 = math.sqrt(max(1.0 - 1.0 / (gamma_beam ** 2), 1e-6))

    # Transferred mass
    A_trans = round(rho * float(A_p), 1)
    A_spec = round(float(A_p) - A_trans, 1)
    Z_trans = round(rho * float(Z_p), 1)

    # Recoil velocity under full momentum transfer
    # v_rec_CF / c = p_0 / (M_CN * c) ~ (A_p * beta_0) / (A_p + A_t)
    beta_rec_CF = (float(A_p) * beta_0) / float(A_p + A_t)
    beta_rec_actual = rho * beta_rec_CF

    # Fission TKE estimate if not supplied (Viola systematics)
    Z_cn = int(round(Z_trans + Z_t))
    A_cn = int(round(A_trans + A_t))

    if TKE_fission_MeV is None:
        coul_param = (Z_cn ** 2) / (A_cn ** (1.0 / 3.0))
        tke = 0.1189 * coul_param + 7.3
    else:
        tke = TKE_fission_MeV

    # Fragment velocity in CM frame (symmetric fission A_f = A_cn / 2)
    # TKE = 2 * (1/2 * m_f * v_f^2) = m_f * v_f^2
    m_frag = 0.5 * A_cn * U_MEV
    beta_frag = math.sqrt(max(tke / m_frag, 1e-6))

    # Folding angle: tan(theta_fold / 2) = beta_frag / beta_rec_actual
    if beta_rec_actual > 1e-6:
        tan_half = beta_frag / beta_rec_actual
        theta_fold_rad = 2.0 * math.atan(tan_half)
        theta_fold_deg = math.degrees(theta_fold_rad)
    else:
        theta_fold_deg = 180.0

    # Energy transferred
    E_trans_MeV = rho * E_lab_MeV

    return {
        "projectile": f"Z={Z_p}, A={A_p}",
        "target": f"Z={Z_t}, A={A_t}",
        "E_lab_MeV": E_lab_MeV,
        "energy_per_nucleon_MeV_u": round(E_lab_MeV / float(A_p), 2),
        "beam_velocity_beta": round(beta_0, 4),
        "fractional_LMT_rho": round(rho, 3),
        "transferred_mass_A_trans": A_trans,
        "spectator_mass_A_spec": A_spec,
        "recoil_velocity_CF_beta": round(beta_rec_CF, 4),
        "actual_recoil_velocity_beta": round(beta_rec_actual, 4),
        "actual_recoil_velocity_percent_c": round(beta_rec_actual * 100.0, 2),
        "fission_TKE_MeV": round(tke, 1),
        "fission_fragment_beta": round(beta_frag, 4),
        "predicted_folding_angle_deg": round(theta_fold_deg, 1),
        "reaction_regime": "Complete_Fusion (100% LMT)" if rho >= 0.98 else f"Incomplete_Fusion ({rho*100:.0f}% LMT)"
    }


def scan_folding_angle_vs_lmt(
    A_p: int,
    Z_p: int,
    A_t: int,
    Z_t: int,
    E_lab_MeV: float,
    lmt_fractions: List[float] = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5]
) -> List[Dict[str, Any]]:
    """
    Computes the opening of the fission folding angle as LMT decreases.
    """
    results = []
    for rho in lmt_fractions:
        res = calculate_linear_momentum_transfer(A_p, Z_p, A_t, Z_t, E_lab_MeV, rho)
        results.append({
            "fractional_LMT_rho": rho,
            "transferred_mass_A": res["transferred_mass_A_trans"],
            "recoil_velocity_percent_c": res["actual_recoil_velocity_percent_c"],
            "folding_angle_deg": res["predicted_folding_angle_deg"]
        })
    return results


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   LINEAR MOMENTUM TRANSFER (LMT) & FISSION FOLDING ANGLE ANALYZER")
    lines.append("=" * 72)

    lmt = summary["lmt_kinematics"]
    lines.append(f" REACTION: {lmt['projectile']} + {lmt['target']} @ E_lab = {lmt['E_lab_MeV']} MeV ({lmt['energy_per_nucleon_MeV_u']} MeV/u)")
    lines.append(f"   Beam Velocity beta (v/c)       : {lmt['beam_velocity_beta']}")
    lines.append(f"   Fractional LMT (Delta_p / p_0) : {lmt['fractional_LMT_rho']} ({lmt['reaction_regime']})")
    lines.append(f"   Transferred Mass A_trans       : {lmt['transferred_mass_A_trans']} u (Spectator: {lmt['spectator_mass_A_spec']} u)")
    lines.append(f"   Compound Recoil Velocity       : {lmt['actual_recoil_velocity_percent_c']}% of c (beta = {lmt['actual_recoil_velocity_beta']})")
    lines.append(f"   Fission TKE                    : {lmt['fission_TKE_MeV']} MeV (Fragment beta = {lmt['fission_fragment_beta']})")
    lines.append(f"   Binary Fission Folding Angle   : theta_fold = {lmt['predicted_folding_angle_deg']} deg")
    lines.append("-" * 72)

    if "lmt_scan" in summary:
        lines.append(" FOLDING ANGLE DEPENDENCE ON FRACTIONAL LMT:")
        lines.append(f"   {'LMT (rho)':<12} {'A_trans (u)':<16} {'Recoil (v/c %)':<18} {'theta_fold (deg)':<16}")
        lines.append("   " + "-" * 62)
        for pt in summary["lmt_scan"]:
            lines.append(f"   {pt['fractional_LMT_rho']:<12.2f} {pt['transferred_mass_A']:<16.1f} {pt['recoil_velocity_percent_c']:<18.2f} {pt['folding_angle_deg']:<16.1f}")
        lines.append("-" * 72)

    lines.append(" Physical Significance:")
    lines.append("   - Missing linear momentum signals pre-equilibrium and projectile breakup emission.")
    lines.append("   - Folding angle theta_fold separates complete fusion (sharp angle) from ICF (wider).")
    lines.append("   - Crucial diagnostic for high-energy in-beam heavy-ion reaction mechanisms.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Linear Momentum Transfer & Fission Folding Angle Analyzer."
    )
    parser.add_argument("-Zp", type=int, required=True, help="Projectile atomic number Z_p")
    parser.add_argument("-Ap", type=int, required=True, help="Projectile mass number A_p")
    parser.add_argument("-Zt", type=int, required=True, help="Target atomic number Z_t")
    parser.add_argument("-At", type=int, required=True, help="Target mass number A_t")
    parser.add_argument("-E", "--elab", type=float, required=True, help="Beam energy E_lab in MeV")
    parser.add_argument("--lmt", type=float, default=1.0, help="Fractional LMT rho (default: 1.0 for CF)")
    parser.add_argument("--tke", type=float, default=None, help="Fission TKE in MeV (default: Viola)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    lmt_res = calculate_linear_momentum_transfer(
        args.Ap, args.Zp, args.At, args.Zt, args.elab, args.lmt, args.tke
    )
    scan_res = scan_folding_angle_vs_lmt(args.Ap, args.Zp, args.At, args.Zt, args.elab)

    summary = {
        "lmt_kinematics": lmt_res,
        "lmt_scan": scan_res
    }

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
