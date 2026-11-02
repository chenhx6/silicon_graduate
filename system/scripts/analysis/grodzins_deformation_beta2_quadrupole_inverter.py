#!/usr/bin/env python3
"""
grodzins_deformation_beta2_quadrupole_inverter.py
=================================================
Grodzins Product Rule, B(E2; 0+ -> 2+) to Quadrupole Deformation beta_2 Inverter,
Intrinsic / Spectroscopic Quadrupole Moments & Superfluid Pairing MOI Reduction.

Physics & Formulation:
----------------------
1. Quadrupole Deformation Parameter beta_2 Inversion:
   For an even-even nucleus (Z, A) with measured B(E2; 0_1^+ -> 2_1^+) (in e^2 b^2):
     R_0 = 1.2 * A^(1/3) fm
     beta_2 = [ (4 * pi) / (3 * Z * R_0^2) ] * sqrt[ B(E2; 0+ -> 2+) / e^2 ]
   where B(E2) is converted to e^2 fm^4 (1 e^2 b^2 = 10^4 e^2 fm^4).

2. Intrinsic and Spectroscopic Quadrupole Moments:
   Under the rotational model:
     Intrinsic quadrupole moment Q_0 (in e*b):
       Q_0 = sqrt[ (16 * pi / 5) * B(E2; 0+ -> 2+) ]
     Spectroscopic quadrupole moment of the 2_1^+ state:
       Q_s(2_1^+) = - (2 / 7) * Q_0
     (Negative Q_s indicates prolate deformation beta_2 > 0; positive indicates oblate).

3. Grodzins Empirical Product Rule (Grodzins 1962, Raman 2001):
   Global nuclear systematics across even-even nuclei reveals that the product of 2_1^+ excitation energy
   and B(E2; 0+ -> 2+) scales universally with Z and A:
     E(2_1^+) * B(E2; 0+ -> 2+) = C_G * Z^2 * A^(-2/3)   (C_G = 2.57 +/- 0.45 keV e^2 b^2)
   The dimensionless Grodzins ratio:
     G = [ E(2_1^+) * B(E2) ] / [ 2.57 * Z^2 * A^(-2/3) ]
     - G ~ 0.8 - 1.2 : Well-behaved collective rotor or vibrator following global systematics.
     - G >> 1.5      : Spherical magic / semi-magic shell closure (e.g. 132Sn, 208Pb) where E(2+) is elevated.
     - G << 0.7      : Superdeformed or highly collective transitional state.

4. Superfluid Pairing Reduction of the Moment of Inertia:
   - Experimental moment of inertia from rotational spectrum:
       J_exp = 3 * hbar^2 / E(2_1^+)  (in hbar^2 / MeV)
   - Classical rigid-sphere rotor moment of inertia:
       J_rig = (2 / 5) * [ (A * m_u) / hbar_c^2 ] * R_0^2 * (1.0 + 0.31 * beta_2)
   - BCS Pairing Reduction Ratio:
       J_exp / J_rig ~ 0.30 - 0.55
   As pointed out in Bohr & Mottelson Vol. II §4-2 and Lu Xiting §8.4, pairing correlations drastically
   quench the moment of inertia below the rigid-body value, confirming nuclear superfluidity.

References:
  - 卢希庭, 《原子核物理（修订版）》, 原子能出版社 (2000), 第8章 §8.4 (形变核转动能谱与形变参量, 印刷 pp. 205–212).
  - A. Bohr and B. R. Mottelson, *Nuclear Structure*, Vol. II, §4-2.
  - L. Grodzins, Phys. Lett. 2, 88 (1962).
  - S. Raman, C. W. Nestor, Jr., and P. Tikkanen, At. Data Nucl. Data Tables 78, 1 (2001).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def invert_beta2_and_quadrupole(
    Z: int,
    A: int,
    B_E2_e2_b2: float,
    E_2plus_keV: Optional[float] = None
) -> Dict[str, Any]:
    """
    Inverts quadrupole deformation parameter beta_2, intrinsic Q_0, spectroscopic Q_s(2+),
    Grodzins ratio G, and superfluid pairing moment of inertia reduction J_exp / J_rig.
    """
    if Z <= 0 or A <= 0:
        raise ValueError("Z and A must be strictly positive.")
    if B_E2_e2_b2 <= 0.0:
        raise ValueError("B(E2) transition strength must be strictly positive.")

    m_u_MeV = 931.494 # MeV / c^2
    hbar_c_MeV_fm = 197.327 # MeV * fm

    # Nuclear touching radius R_0 in fm
    R0_fm = 1.20 * (float(A) ** (1.0 / 3.0))

    # Convert B(E2) from e^2 b^2 to e^2 fm^4 (1 b = 100 fm^2 => 1 b^2 = 10^4 fm^4)
    B_E2_fm4 = B_E2_e2_b2 * 1.0e4

    # beta_2 = [ 4 * pi / (3 * Z * R_0^2) ] * sqrt( B(E2) / e^2 )
    beta2 = (4.0 * math.pi / (3.0 * float(Z) * (R0_fm ** 2))) * math.sqrt(B_E2_fm4)

    # Intrinsic quadrupole moment Q_0 in e*b: Q_0 = sqrt[ (16 * pi / 5) * B(E2) ]
    Q0_eb = math.sqrt((16.0 * math.pi / 5.0) * B_E2_e2_b2)

    # Spectroscopic quadrupole moment for J=2 state in K=0 band: Q_s(2+) = - (2/7) * Q_0
    Qs_2plus_eb = - (2.0 / 7.0) * Q0_eb

    # Rigid-sphere moment of inertia J_rig (in hbar^2 / MeV):
    # J_rig = (2/5) * [ M_tot / hbar_c^2 ] * R_0^2 * (1 + 0.31*beta_2)
    M_tot_MeV = float(A) * m_u_MeV
    J_rig = (2.0 / 5.0) * (M_tot_MeV / (hbar_c_MeV_fm ** 2)) * (R0_fm ** 2) * (1.0 + 0.31 * beta2)

    # Grodzins product rule & experimental MOI if E(2+) is supplied:
    grodzins_theoretical_keV_b2 = 2.57 * (float(Z) ** 2) * (float(A) ** (-2.0 / 3.0))
    grodzins_ratio = None
    J_exp = None
    pairing_reduction = None

    if E_2plus_keV is not None and E_2plus_keV > 0.0:
        prod = E_2plus_keV * B_E2_e2_b2
        grodzins_ratio = prod / grodzins_theoretical_keV_b2

        # J_exp = 3 * hbar^2 / E(2+) in hbar^2 / MeV
        # E(2+) = 6 * (hbar^2 / 2*J) = 3 * hbar^2 / J => J = 3 * 1000 / E(2+)_keV
        J_exp = 3000.0 / E_2plus_keV
        pairing_reduction = J_exp / J_rig

    # Deformation classification
    if beta2 >= 0.30:
        def_class = "Super-Deformed / Highly Deformed Rotor (beta2 >= 0.30)"
    elif beta2 >= 0.20:
        def_class = "Well-Deformed Prolate Rotor (0.20 <= beta2 < 0.30)"
    elif beta2 >= 0.10:
        def_class = "Transitional / Moderately Deformed (0.10 <= beta2 < 0.20)"
    else:
        def_class = "Near-Spherical / Vibrational (beta2 < 0.10)"

    return {
        "Z": Z,
        "A": A,
        "B_E2_e2_b2": B_E2_e2_b2,
        "E_2plus_keV": E_2plus_keV,
        "nuclear_radius_R0_fm": round(R0_fm, 3),
        "quadrupole_deformation_beta2": round(beta2, 4),
        "intrinsic_quadrupole_moment_Q0_eb": round(Q0_eb, 3),
        "spectroscopic_quadrupole_moment_Qs_eb": round(Qs_2plus_eb, 3),
        "deformation_classification": def_class,
        "grodzins_theoretical_keV_b2": round(grodzins_theoretical_keV_b2, 1),
        "grodzins_ratio": round(grodzins_ratio, 3) if grodzins_ratio is not None else None,
        "J_rigid_rotor_hbar2_MeV": round(J_rig, 2),
        "J_experimental_hbar2_MeV": round(J_exp, 2) if J_exp is not None else None,
        "superfluid_pairing_reduction_ratio": round(pairing_reduction, 3) if pairing_reduction is not None else None
    }


def format_text_report(res: Dict[str, Any]) -> str:
    lines = [
        "=" * 76,
        "   GRODZINS PRODUCT RULE & QUADRUPOLE DEFORMATION beta_2 INVERTER",
        "   Based on Lu Xiting §8.4, Bohr & Mottelson Vol. II §4-2 & Raman (2001)",
        "=" * 76,
        f" NUCLEUS: (Z={res['Z']}, A={res['A']})",
        f"   Nuclear Radius R_0          : {res['nuclear_radius_R0_fm']:.3f} fm",
        f"   B(E2; 0_1^+ -> 2_1^+)       : {res['B_E2_e2_b2']:.4f} e^2 b^2",
    ]

    if res["E_2plus_keV"] is not None:
        lines.append(f"   2_1^+ Excitation Energy     : {res['E_2plus_keV']:.1f} keV")

    lines.extend([
        "-" * 76,
        " INVERTED DEFORMATION PARAMETERS & QUADRUPOLE MOMENTS:",
        f"   Quadrupole Deformation beta2: {res['quadrupole_deformation_beta2']:.4f}  [{res['deformation_classification']}]",
        f"   Intrinsic Quadrupole Q_0    : {res['intrinsic_quadrupole_moment_Q0_eb']:.3f} e*b",
        f"   Spectroscopic Quadrupole Q_s: {res['spectroscopic_quadrupole_moment_Qs_eb']:.3f} e*b (Negative = Prolate)",
        "-" * 76,
        " GRODZINS SYSTEMATIC SCALING & RIGIDITY RATIO:",
        f"   Theoretical Grodzins Scaling: {res['grodzins_theoretical_keV_b2']:.1f} keV e^2 b^2",
    ])

    if res["grodzins_ratio"] is not None:
        lines.append(f"   Grodzins Ratio G            : {res['grodzins_ratio']:.3f} (Collective rule: G ~ 1.0)")

    lines.extend([
        "-" * 76,
        " MOMENT OF INERTIA & SUPERFLUID PAIRING REDUCTION:",
        f"   Classical Rigid Rotor J_rig : {res['J_rigid_rotor_hbar2_MeV']:.2f} hbar^2/MeV",
    ])

    if res["J_experimental_hbar2_MeV"] is not None:
        lines.append(f"   Experimental MOI J_exp      : {res['J_experimental_hbar2_MeV']:.2f} hbar^2/MeV")
        lines.append(f"   Superfluid Ratio J_exp/J_rig: {res['superfluid_pairing_reduction_ratio']:.3f} (BCS pairing quenches MOI by 45-70%)")

    lines.extend([
        "-" * 76,
        " Methodological Significance:",
        "   - Grodzins product E(2+)*B(E2) universally characterizes collective nuclear rigidity.",
        "   - Prolate nuclei have Q_s(2+) < 0; oblate nuclei have Q_s(2+) > 0.",
        "   - J_exp < J_rig is the historical macroscopic proof of nuclear BCS superfluidity.",
        "=" * 76
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Grodzins Product Rule & Quadrupole Deformation beta_2 Inverter"
    )
    parser.add_argument("--Z", "-Z", type=int, default=62, help="Proton number Z (default: 62 for Sm)")
    parser.add_argument("--A", "-A", type=int, default=154, help="Mass number A (default: 154)")
    parser.add_argument("--BE2", type=float, default=4.35, help="B(E2; 0+ -> 2+) in e^2 b^2 (default: 4.35)")
    parser.add_argument("--E2", type=float, default=82.0, help="E(2_1^+) energy in keV (default: 82.0 keV)")
    parser.add_argument("--preset", type=str, default="154Sm",
                        choices=["154Sm", "134Ce", "132Sn", "208Pb"],
                        help="Benchmark preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")

    args = parser.parse_args()

    z_val, a_val = args.Z, args.A
    be2_val = args.BE2
    e2_val = args.E2

    if args.preset == "154Sm":
        z_val, a_val, be2_val, e2_val = 62, 154, 4.35, 82.0
    elif args.preset == "134Ce":
        z_val, a_val, be2_val, e2_val = 58, 134, 0.78, 409.2
    elif args.preset == "132Sn":
        z_val, a_val, be2_val, e2_val = 50, 132, 0.011, 4041.0
    elif args.preset == "208Pb":
        z_val, a_val, be2_val, e2_val = 82, 208, 0.30, 4085.0

    res = invert_beta2_and_quadrupole(z_val, a_val, be2_val, e2_val)

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res))


if __name__ == "__main__":
    main()
