#!/usr/bin/env python3
"""Schematic single-j Coriolis matrix-element magnitudes and band diagnostics.

The spin/energy sequence in main() is synthetic, not 131La measurement data.
The attenuation xi is an external phenomenological input; this calculator does
not derive it from pairing. A frequency decrease is a candidate backbend,
not a unique identification of a broken pair or quasiparticle configuration.
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
    for name, value in (("j", j), ("I", I), ("A_rot_keV", A_rot_keV), ("xi", xi)):
        if not math.isfinite(value):
            raise ValueError(f"{name} must be finite")
    if j < 0 or I < 0 or A_rot_keV <= 0 or not 0 <= xi <= 1:
        raise ValueError("Require nonnegative spins, positive A_rot and 0 <= xi <= 1")
    if not all(abs(2*v-round(2*v)) < 1e-9 for v in (j, I)):
        raise ValueError("Spins must be integer or half-integer")
    if (round(2*j)-round(2*I)) % 2:
        raise ValueError("I and j must have the same integer/half-integer parity")
    k_vals = []
    cur_k = 0.0 if round(2*j) % 2 == 0 else 0.5
    while cur_k < min(j, I):
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
            "value_kind": "matrix-element-magnitude-in-single-j-basis",
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

    if not all(math.isfinite(v) for v in spins + energies_keV + [J0_harris, J1_harris, K_band]):
        raise ValueError("Band inputs must be finite")
    if any(b <= a for a, b in zip(spins, spins[1:])):
        raise ValueError("Spins must increase strictly")
    if any(b <= a for a, b in zip(energies_keV, energies_keV[1:])):
        raise ValueError("Level energies must increase strictly")
    if any(I < abs(K_band) for I in spins):
        raise ValueError("Band projection magnitude cannot exceed total spin")
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
        "evidence_boundary": "Finite-difference band descriptors; no experimental identity or unique pair-breaking inference",
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
        "   Schematic single-j elements and SYNTHETIC band example",
        "=" * 74,
        f" CORIOLIS MATRIX ELEMENTS AT SPIN I = {I_spin:.1f} (Orbital j = {j_orbital:.1f}):",
        "   K -> K+1        Unattenuated (xi=1.0)    Attenuated (input xi)    Reduction",
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
        f"   Backbending Status   : {'FREQUENCY DECREASE CANDIDATE (heuristic)' if diag['backbending_observed'] else 'Smooth rotational upbending'}",
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
        "   - The reported elements are magnitudes in an ideal single-j basis.",
        "   - xi is a supplied phenomenological scale; no microscopic origin is fitted here.",
        "   - The demo levels are synthetic; a frequency decrease alone does not identify",
        "     a specific quasiparticle configuration or prove a band crossing.",
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

    # Synthetic energy sequence for demonstrating a frequency decrease; not nuclear data.
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
