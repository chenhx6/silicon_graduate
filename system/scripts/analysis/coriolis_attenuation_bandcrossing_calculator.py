#!/usr/bin/env python3
"""
coriolis_attenuation_bandcrossing_calculator.py
===============================================
Coriolis Interaction Attenuation, Particle-Rotor Band Coupling &
Quasiparticle Band Crossing (Backbending) Analyzer.

Physics & Formulation:
----------------------
1. The Particle-Rotor Hamiltonian & Coriolis Coupling:
   H = H_intr + [ hbar^2 / (2 * J_0) ] * (I - j)^2
     = H_intr + [ hbar^2 / (2 * J_0) ] * [ I(I+1) - K^2 + j^2 - Omega^2 ] + H_cor
   where the Coriolis operator is:
     H_cor = - [ hbar^2 / (2 * J_0) ] * ( I_+ * j_- + I_- * j_+ )

2. Off-Diagonal Coriolis Matrix Elements & Attenuation Factor xi:
   <I, K+1 | H_cor | I, K> = - xi * [ hbar^2 / (2 * J_0) ] *
                             sqrt( (I - K) * (I + K + 1) * (j - K) * (j + K + 1) )
   - Standard Bohr-Mottelson Rotor: xi = 1.0 (overestimates decoupling in odd-A nuclei).
   - Realistic Attenuated Value: xi ~ 0.60 - 0.85
     Physical Origins of Attenuation:
     * Residual pairing reduction factor: (u_1 * u_2 + v_1 * v_2)
     * Core polarization by odd nucleon deformation
     * Delta_N = 2 cross-shell mixing

3. Rotational Alignment & Backbending Analysis:
   - Aligned angular momentum: I_x = sqrt( (I + 0.5)^2 - K^2 )
   - Rotational frequency: hbar_omega = (E(I) - E(I-2)) / 2
   - Kinematical moment of inertia: J^(1) = hbar * I_x / omega  (in hbar^2/MeV)
   - Dynamical moment of inertia:   J^(2) = hbar * (dI_x / d_omega)
   - Harris Reference subtraction: J_ref = J_0 + J_1 * omega^2
     i_x(omega) = I_x(omega) - ( J_0 * omega + J_1 * omega^3 )

References:
  - A. Bohr and B. R. Mottelson, Nuclear Structure, Vol. II: Nuclear Deformations (1975), §4-3.
  - K. Heyde, Basic Ideas and Concepts in Nuclear Physics, IOP (1999), Ch 8.
  - S. Frauendorf, Rev. Mod. Phys. 73, 463 (2001).
  - 卢希庭, 《原子核物理（修订版）》, 第8章 (集体模型与转动能级).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_coriolis_matrix_elements(
    j: float,
    I: float,
    A_rot_keV: float = 15.0,
    xi: float = 0.75
) -> List[Dict[str, Any]]:
    """
    Calculates off-diagonal Coriolis matrix elements <I, K+1 | H_cor | I, K>
    across the K-manifold (K = 1/2, 3/2, ..., j-1).
    """
    k_vals = []
    cur_k = 0.5
    while cur_k < j:
        k_vals.append(cur_k)
        cur_k += 1.0

    elements = []
    for k in k_vals:
        k_next = k + 1.0
        # sqrt( (I - K)*(I + K + 1)*(j - K)*(j + K + 1) )
        geom_I = (I - k) * (I + k + 1.0)
        geom_j = (j - k) * (j + k + 1.0)
        if geom_I <= 0.0 or geom_j <= 0.0:
            val_unatt = 0.0
        else:
            val_unatt = A_rot_keV * math.sqrt(geom_I * geom_j)

        val_att = xi * val_unatt
        elements.append({
            "K_initial": k,
            "K_final": k_next,
            "unattenuated_matrix_element_keV": val_unatt,
            "attenuated_matrix_element_keV": val_att,
            "attenuation_factor_xi": xi
        })
    return elements


def analyze_backbending_alignment(
    spins: List[float],
    energies_keV: List[float],
    J0_harris: float = 30.0,
    J1_harris: float = 40.0,
    K_band: float = 0.5
) -> Dict[str, Any]:
    """
    Extracts rotational frequency hbar*omega, aligned angular momentum i_x,
    kinematical moment of inertia J^(1), and identifies backbending crossing frequency.
    """
    if len(spins) != len(energies_keV) or len(spins) < 3:
        raise ValueError("Spins and energies must have at least 3 points.")

    n = len(spins)
    points = []
    backbend_detected = False
    crossing_omega_MeV = None
    max_alignment = 0.0

    for i in range(1, n):
        I = spins[i]
        I_prev = spins[i-1]
        delta_I = I - I_prev
        if delta_I <= 0:
            continue

        dE_keV = energies_keV[i] - energies_keV[i-1]
        hbar_omega_MeV = (dE_keV / (1000.0 * delta_I))

        I_mid = 0.5 * (I + I_prev)
        I_x = math.sqrt(max(0.0, (I_mid + 0.5)**2 - K_band**2))

        J1_exp = (I_x / max(1e-6, hbar_omega_MeV)) # in hbar^2/MeV

        # Harris reference: I_ref = J0 * omega + J1 * omega^3
        omega = hbar_omega_MeV
        I_ref = J0_harris * omega + J1_harris * (omega**3)
        i_x = I_x - I_ref
        max_alignment = max(max_alignment, i_x)

        points.append({
            "spin_mid": I_mid,
            "hbar_omega_MeV": hbar_omega_MeV,
            "I_x_hbar": I_x,
            "J1_moment_of_inertia": J1_exp,
            "Harris_I_ref": I_ref,
            "aligned_angular_momentum_ix": i_x
        })

    # Detect backbending (decrease of hbar_omega with increasing spin)
    for k in range(1, len(points)):
        d_omega = points[k]["hbar_omega_MeV"] - points[k-1]["hbar_omega_MeV"]
        if d_omega < -0.015:
            backbend_detected = True
            crossing_omega_MeV = points[k-1]["hbar_omega_MeV"]
            break

    return {
        "harris_reference_parameters": {
            "J0_hbar2_per_MeV": J0_harris,
            "J1_hbar4_per_MeV3": J1_harris,
            "K_bandhead": K_band
        },
        "backbending_diagnostics": {
            "backbending_observed": backbend_detected,
            "crossing_frequency_hbar_omega_MeV": crossing_omega_MeV,
            "maximum_quasiparticle_alignment_ix": max_alignment
        },
        "trajectory": points
    }


def format_text_report(cor_elem: List[Dict[str, Any]], bb_res: Dict[str, Any], I_spin: float, j_orbital: float) -> str:
    diag = bb_res["backbending_diagnostics"]
    har = bb_res["harris_reference_parameters"]
    pts = bb_res["trajectory"]

    lines = [
        "=" * 74,
        "   CORIOLIS ATTENUATION, PARTICLE-ROTOR COUPLING & BACKBENDING SUITE",
        "   Based on Bohr & Mottelson (Nuclear Structure Vol II) & Heyde",
        "=" * 74,
        f" CORIOLIS MATRIX ELEMENTS AT SPIN I = {I_spin:.1f} (Orbital j = {j_orbital:.1f}):",
        "   K -> K+1        Unattenuated (xi=1.0)    Attenuated (xi=0.75)    Reduction",
        "   " + "-" * 70
    ]

    for e in cor_elem:
        red = (1.0 - e["attenuation_factor_xi"]) * 100.0
        lines.append(
            f"   K={e['K_initial']:<4.1f}-> {e['K_final']:<4.1f}:   "
            f"{e['unattenuated_matrix_element_keV']:>10.2f} keV          "
            f"{e['attenuated_matrix_element_keV']:>10.2f} keV        "
            f"-{red:.1f}%"
        )

    lines.extend([
        "-" * 74,
        f" ROTATIONAL ALIGNMENT & BACKBENDING TRAJECTORY (Harris J0={har['J0_hbar2_per_MeV']:.1f}, J1={har['J1_hbar4_per_MeV3']:.1f}):",
        f"   Backbending Status   : {'BACKBENDING / BAND-CROSSING CONFIRMED!' if diag['backbending_observed'] else 'Smooth rotational upbending'}",
        f"   Crossing Frequency   : {diag['crossing_frequency_hbar_omega_MeV']} MeV" if diag['crossing_frequency_hbar_omega_MeV'] else "   Crossing Frequency   : N/A",
        f"   Peak Alignment i_x   : {diag['maximum_quasiparticle_alignment_ix']:.2f} hbar",
        "",
        "   Spin (hbar)    hbar*omega (MeV)    I_x (hbar)    J^(1) (hbar^2/MeV)    i_x (hbar)",
        "   " + "-" * 70
    ])

    for p in pts[:8]:
        lines.append(
            f"     {p['spin_mid']:>5.1f}          {p['hbar_omega_MeV']:>7.3f}        "
            f"{p['I_x_hbar']:>7.2f}        {p['J1_moment_of_inertia']:>8.1f}          "
            f"{p['aligned_angular_momentum_ix']:>6.2f}"
        )

    lines.extend([
        "-" * 74,
        " Physical & Microscopic Synthesis:",
        "   - Pure independent-particle rotor (xi=1) overestimates Coriolis decoupling.",
        "   - Attenuation factor xi ~ 0.75 arises from pairing gap Delta and core polarization.",
        "   - At hbar*omega_c, Coriolis force breaks the high-j pair, creating a sharp backbend",
        "     in J^(1) and transferring ~ 8-10 hbar of alignment to the yrast sequence.",
        "=" * 74
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Coriolis Interaction Attenuation & Band Crossing Analyzer"
    )
    parser.add_argument("--spin", "-I", type=float, default=15.5,
                        help="Total nuclear spin (default: 15.5)")
    parser.add_argument("--j-orbital", "-j", type=float, default=5.5,
                        help="Valence nucleon angular momentum j (default: 5.5, h11/2)")
    parser.add_argument("--arot", type=float, default=15.0,
                        help="Rotational parameter hbar^2 / 2J in keV (default: 15.0 keV)")
    parser.add_argument("--xi", type=float, default=0.75,
                        help="Coriolis attenuation factor (default: 0.75)")
    parser.add_argument("--json", action="store_true",
                        help="Output pure JSON")

    args = parser.parse_args()

    cor_elem = calculate_coriolis_matrix_elements(
        j=args.j_orbital,
        I=args.spin,
        A_rot_keV=args.arot,
        xi=args.xi
    )

    # Representative experimental yrast band crossing in 131La (pi h11/2 band)
    demo_spins = [5.5, 7.5, 9.5, 11.5, 13.5, 15.5, 17.5, 19.5, 21.5, 23.5, 25.5]
    # Energies with backbending around 19.5 -> 21.5
    demo_energies = [0.0, 180.0, 480.0, 910.0, 1470.0, 2160.0, 2980.0, 3650.0, 4200.0, 4850.0, 5600.0]

    bb_res = analyze_backbending_alignment(
        spins=demo_spins,
        energies_keV=demo_energies,
        J0_harris=25.0,
        J1_harris=35.0,
        K_band=0.5
    )

    if args.json:
        print(json.dumps({"coriolis_elements": cor_elem, "backbending": bb_res}, indent=2))
    else:
        print(format_text_report(cor_elem, bb_res, args.spin, args.j_orbital))


if __name__ == "__main__":
    main()
