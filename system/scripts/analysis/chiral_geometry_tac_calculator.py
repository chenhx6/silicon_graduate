#!/usr/bin/env python3
"""
chiral_geometry_tac_calculator.py
=================================
3D Tilted Axis Cranking (TAC) Chiral Geometry & Non-Coplanar Volume Metric Solver.

Physics & Formulation:
----------------------
1. Trihedral Angular Momentum Vector Coupling (Frauendorf 2001 / Petrache 2024):
   - Short axis s (axis 1): Valence proton particle j_p (e.g. h11/2) aligns along s.
   - Intermediate axis m (axis 2): Collective core rotation R aligns along m (J_m largest).
   - Long axis l (axis 3): Valence neutron hole j_n (e.g. h11/2^-1) aligns along l.
   Total Angular Momentum:
     I = (j_p + R_s, R_m, j_n + R_l)

2. Chirality Volume Metric (Aplanarity Measure):
   Triple scalar product: chi = j_p . (R x j_n)
   Normalized volume metric:
     V_chiral = |chi| / (|j_p| * |j_n| * |R|)
   - V_chiral == 0: Planar geometry (Chirality forbidden).
   - V_chiral >= 0.35: Robust non-coplanar aplanar chiral geometry.

3. TAC Spherical Orientation Angles (theta_tilt, phi_tilt):
   cos(theta) = I_l / |I|
   tan(phi)   = I_m / I_s

4. Chiral Phase Evolution (Vibration vs Static Rotation vs Planar Collapse):
   - Chiral Vibration (Low spin): R is small, tunneling through planar barrier is rapid,
     energy splitting Delta_E(I) > 150 keV.
   - Static Chiral Rotation (Mid spin): Barrier thickens, Left/Right symmetry breaks,
     Delta_E(I) -> 0 (< 50 keV), twin bands are degenerate.
   - Planar Restoration (High spin): Coriolis forces realign j_p and j_n into the m-axis,
     V_chiral -> 0.

5. Electromagnetic Selection Rule:
   In static chirality, Left and Right states form symmetric/antisymmetric doublets:
     B(M1; I -> I-1)_in ~ B(M1; I -> I-1)_out
     B(E2; I -> I-2)_Band1 ~ B(E2; I -> I-2)_Band2

References:
  - S. Frauendorf and J. Meng, Nucl. Phys. A 617, 131 (1997).
  - S. Frauendorf, Rev. Mod. Phys. 73, 463 (2001).
  - K. Starosta et al., Phys. Rev. Lett. 86, 971 (2001).
  - C. M. Petrache, Chirality and Wobbling in Atomic Nuclei, Springer (2024).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_chiral_geometry(
    j_p: float = 5.5,
    j_n: float = 5.5,
    R_m: float = 8.0,
    R_s: float = 0.5,
    R_l: float = 0.5,
    J_m_moi: float = 30.0,
    J_s_moi: float = 12.0,
    J_l_moi: float = 8.0
) -> Dict[str, Any]:
    """
    Computes 3D angular momentum vectors and evaluates chiral aplanarity metric.
    """
    # Total vector components in intrinsic principal frame:
    I_s = j_p + R_s
    I_m = R_m
    I_l = j_n + R_l

    total_I = math.sqrt(I_s**2 + I_m**2 + I_l**2)

    # Core rotation vector R
    R_mag = math.sqrt(R_s**2 + R_m**2 + R_l**2)

    # j_p vector (along s axis)
    vec_jp = (j_p, 0.0, 0.0)
    # j_n vector (along l axis)
    vec_jn = (0.0, 0.0, j_n)
    # R vector
    vec_R = (R_s, R_m, R_l)

    # Cross product: vec_R x vec_jn = (R_m*j_n, -R_s*j_n, 0)
    cross_x = vec_R[1] * vec_jn[2] - vec_R[2] * vec_jn[1]
    cross_y = vec_R[2] * vec_jn[0] - vec_R[0] * vec_jn[2]
    cross_z = vec_R[0] * vec_jn[1] - vec_R[1] * vec_jn[0]

    # Triple product: vec_jp . (vec_R x vec_jn)
    triple_prod = vec_jp[0] * cross_x + vec_jp[1] * cross_y + vec_jp[2] * cross_z

    denom = j_p * j_n * max(R_mag, 1e-4)
    v_chiral = abs(triple_prod) / denom

    # Tilted angles
    theta_tilt_deg = math.degrees(math.acos(max(min(I_l / max(total_I, 1e-4), 1.0), -1.0)))
    phi_tilt_deg = math.degrees(math.atan2(I_m, I_s))

    # Rotational frequencies in hbar*omega (MeV)
    omega_s = R_s / max(J_s_moi, 0.1)
    omega_m = R_m / max(J_m_moi, 0.1)
    omega_l = R_l / max(J_l_moi, 0.1)
    omega_mag = math.sqrt(omega_s**2 + omega_m**2 + omega_l**2)

    # Phase classification
    if v_chiral < 0.15:
        chiral_phase = "Planar (Quasi-coplanar, chiral symmetry not broken)"
    elif R_mag < 4.0:
        chiral_phase = "Chiral_Vibration (Small collective R, high quantum tunneling between chiral partners)"
    elif R_mag <= 14.0:
        chiral_phase = "Static_Chiral_Rotation (Ideal aplanar trihedron, spontaneous chiral symmetry breaking)"
    else:
        chiral_phase = "Coriolis_Restoration (High spin realignment towards m-axis)"

    return {
        "j_proton": j_p,
        "j_neutron": j_n,
        "R_core_mag": round(R_mag, 2),
        "total_spin_I": round(total_I, 2),
        "spin_components_s_m_l": [round(I_s, 2), round(I_m, 2), round(I_l, 2)],
        "tilt_angle_theta_deg": round(theta_tilt_deg, 1),
        "tilt_angle_phi_deg": round(phi_tilt_deg, 1),
        "triple_scalar_product": round(triple_prod, 2),
        "chiral_volume_metric": round(v_chiral, 3),
        "rotational_frequency_omega_MeV": round(omega_mag, 3),
        "chiral_phase": chiral_phase
    }


def evaluate_chiral_doublet_criteria(
    delta_energy_keV: float,
    bm1_in_over_out: float = 1.1,
    be2_band1_over_band2: float = 1.05,
    I_spin: float = 13.0
) -> Dict[str, Any]:
    """
    Evaluates whether two experimental candidate bands satisfy the rigid 4-point
    chiral doublet criteria (Frauendorf 2001 / Petrache 2024).
    """
    checks = []
    score = 0
    total = 4

    # 1. Energy Degeneracy Test
    if delta_energy_keV <= 60.0:
        checks.append(f"PASS: Energy degeneracy Delta_E = {delta_energy_keV:.1f} keV <= 60 keV (Static Chiral degenerate doublet)")
        score += 1
    elif delta_energy_keV <= 150.0:
        checks.append(f"PASS: Energy splitting Delta_E = {delta_energy_keV:.1f} keV <= 150 keV (Chiral vibration regime)")
        score += 1
    else:
        checks.append(f"FAIL: Energy splitting Delta_E = {delta_energy_keV:.1f} keV > 150 keV (Too large for static chirality)")

    # 2. B(M1)_in vs B(M1)_out similarity
    ratio_m1 = bm1_in_over_out if bm1_in_over_out >= 1.0 else 1.0 / max(bm1_in_over_out, 1e-4)
    if ratio_m1 <= 2.0:
        checks.append(f"PASS: B(M1)_in / B(M1)_out = {bm1_in_over_out:.2f} ~ 1 (Intra-band and inter-band M1 comparable)")
        score += 1
    else:
        checks.append(f"FAIL: B(M1)_in / B(M1)_out = {bm1_in_over_out:.2f} differs by factor > 2")

    # 3. B(E2) Twin Band Identicalness
    ratio_e2 = be2_band1_over_band2 if be2_band1_over_band2 >= 1.0 else 1.0 / max(be2_band1_over_band2, 1e-4)
    if ratio_e2 <= 1.4:
        checks.append(f"PASS: B(E2)_Band1 / B(E2)_Band2 = {be2_band1_over_band2:.2f} ~ 1 (Twin bands share identical core quadrupole deformation)")
        score += 1
    else:
        checks.append(f"FAIL: B(E2) mismatch = {be2_band1_over_band2:.2f} (Different intrinsic quadrupole shapes)")

    # 4. Spin Alignment Plausibility
    if I_spin >= 10.0:
        checks.append(f"PASS: Total spin I = {I_spin} hbar lies within active chiral window")
        score += 1
    else:
        checks.append(f"FAIL: Spin I = {I_spin} too low for developed core rotation")

    if score == total:
        verdict = "ROBUST_CHIRAL_DOUBLET_CONFIRMED"
    elif score >= 2:
        verdict = "CHIRAL_VIBRATION_OR_CANDIDATE"
    else:
        verdict = "REJECTED_AS_CHIRAL_DOUBLET"

    return {
        "verdict": verdict,
        "score": f"{score}/{total}",
        "criteria_checks": checks
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   3D TILTED AXIS CRANKING (TAC) CHIRAL GEOMETRY ANALYZER")
    lines.append("=" * 72)

    cg = summary["geometry"]
    lines.append(" INTRINSIC ANGULAR MOMENTUM TRIHEDRON:")
    lines.append(f"   Valence Proton j_p (short s)   : {cg['j_proton']} hbar")
    lines.append(f"   Valence Neutron j_n (long l)   : {cg['j_neutron']} hbar")
    lines.append(f"   Core Rotation R (med m)        : {cg['R_core_mag']} hbar")
    lines.append(f"   Total Spin Vector |I|          : {cg['total_spin_I']} hbar [s={cg['spin_components_s_m_l'][0]}, m={cg['spin_components_s_m_l'][1]}, l={cg['spin_components_s_m_l'][2]}]")
    lines.append(f"   Tilted Cranking Angles         : theta = {cg['tilt_angle_theta_deg']} deg, phi = {cg['tilt_angle_phi_deg']} deg")
    lines.append(f"   Rotational Frequency hbar*omega: {cg['rotational_frequency_omega_MeV']} MeV")
    lines.append("-" * 72)
    lines.append(" NON-COPLANAR APLANARITY & CHIRAL VOLUME:")
    lines.append(f"   Triple Scalar Product          : {cg['triple_scalar_product']}")
    lines.append(f"   Normalized Chiral Volume Metric: {cg['chiral_volume_metric']}")
    lines.append(f"   Chiral Phase Status            : {cg['chiral_phase']}")
    lines.append("-" * 72)

    if "doublet_audit" in summary:
        da = summary["doublet_audit"]
        lines.append(" CHIRAL DOUBLET BANDS EXPERIMENTAL AUDIT:")
        lines.append(f"   Verdict                        : {da['verdict']} ({da['score']})")
        for chk in da["criteria_checks"]:
            lines.append(f"     * {chk}")
        lines.append("-" * 72)

    lines.append(" Physical Significance:")
    lines.append("   - Left and Right handed states can only exist when V_chiral > 0.")
    lines.append("   - At static chirality, B(M1)_in ~ B(M1)_out due to chiral parity doublet.")
    lines.append("   - A ~ 130 odd-odd nuclei (128,130Cs, 132La) represent world benchmarks.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="3D Tilted Axis Cranking (TAC) Chiral Geometry Analyzer."
    )
    parser.add_argument("--jp", type=float, default=5.5, help="Valence proton angular momentum j_p (default: 5.5 for h11/2)")
    parser.add_argument("--jn", type=float, default=5.5, help="Valence neutron angular momentum j_n (default: 5.5 for h11/2)")
    parser.add_argument("--Rm", type=float, default=8.0, help="Intermediate axis core rotation R_m (default: 8.0)")
    parser.add_argument("--Rs", type=float, default=0.5, help="Short axis core rotation R_s (default: 0.5)")
    parser.add_argument("--Rl", type=float, default=0.5, help="Long axis core rotation R_l (default: 0.5)")
    parser.add_argument("--delta-e-keV", type=float, default=None, help="Energy difference Delta_E between doublet bands in keV")
    parser.add_argument("--bm1-ratio", type=float, default=1.1, help="B(M1)_in / B(M1)_out ratio (default: 1.1)")
    parser.add_argument("--be2-ratio", type=float, default=1.05, help="B(E2)_Band1 / B(E2)_Band2 ratio (default: 1.05)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    geom = calculate_chiral_geometry(args.jp, args.jn, args.Rm, args.Rs, args.Rl)
    summary = {"geometry": geom}

    if args.delta_e_keV is not None:
        audit = evaluate_chiral_doublet_criteria(
            args.delta_e_keV, args.bm1_ratio, args.be2_ratio, geom["total_spin_I"]
        )
        summary["doublet_audit"] = audit

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
