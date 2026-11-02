#!/usr/bin/env python3
"""
schiffer_true_two_body_matrix_elements_calculator.py
====================================================
Schiffer-True Universal Two-Body Matrix Element (TBME) theta_12 Angle Parameterization,
Pandya Particle-Hole Inversion & Nordheim Odd-Odd Chiral Bandhead Coupling Engine.

Physics & Formulation:
----------------------
1. Semiclassical Angle theta_12 Between Nucleon Angular Momenta:
   For two nucleons in orbitals j_1 and j_2 coupled to total angular momentum J (|j_1 - j_2| <= J <= j_1 + j_2):
   The semiclassical angle theta_12 between the two vectors j_1 and j_2 is:
     cos(theta_12) = [ J(J + 1) - j_1(j_1 + 1) - j_2(j_2 + 1) ] / [ 2 * sqrt( j_1(j_1 + 1) * j_2(j_2 + 1) ) ]
     - J = 0 (for j_1 = j_2): cos(theta_12) = -1.0 => theta_12 = 180 deg (antiparallel, maximum pairing overlap).
     - J ~ sqrt(2) * j: cos(theta_12) ~ 0.0 => theta_12 ~ 90 deg (perpendicular).
     - J = J_max = j_1 + j_2: cos(theta_12) -> +1.0 => theta_12 -> 0 deg (parallel alignment).

2. Schiffer-True Universal Empirical Curve (Schiffer & True 1976):
   J. P. Schiffer and W. W. True (Rev. Mod. Phys. 48, 191, 1976) discovered that when plotted against
   theta_12, experimental two-body matrix elements (TBMEs) across the entire nuclear chart collapse
   onto a universal functional shape:
     V_pp(theta_12) = v_pair * delta_{J, 0} + v_1 * cos(theta_12) + v_2 * P_2(cos(theta_12))
   - Deep attractive minimum at theta_12 = 180 deg (J = 0): Pairing gap V_0 ~ -1.5 to -2.5 MeV.
   - Secondary attractive minimum at theta_12 -> 0 deg (J = J_max): Co-planar spatial overlap.
   - Weak or slightly repulsive interaction at intermediate angles theta_12 ~ 90 deg.

3. Pandya Transformation for Particle-Hole Multiplets (Chiral Bandheads):
   In odd-odd nuclei with valence proton particle and neutron hole (e.g. 134Pr, 128Cs with pi h_11/2 (x) nu h_11/2^-1):
   The particle-hole matrix elements are related to particle-particle matrix elements by the exact Pandya transformation:
     V_ph(J) = - sum_{J'} (2*J' + 1) * Wigner_6j(j_1, j_2, J; j_1, j_2, J') * V_pp(J')
   The particle-hole transformation inverts the spectrum:
   The lowest energy states are shifted to J = |j_1 - j_2| and J = j_1 + j_2 (aligned bandhead)!

4. Nordheim Coupling Rules for Odd-Odd Bandheads:
   The Nordheim number N_Nordheim = (j_p - l_p) + (j_n - l_n):
   - Strong rule: If N_Nordheim = 0 => Ground state spin is J_gs = |j_p - j_n|.
   - Weak rule  : If N_Nordheim = +/- 1 => J_gs favors maximum alignment J = j_p + j_n or intermediate spin.
   In 134Pr (pi h_11/2 with j_p - l_p = +1/2, nu h_11/2^-1 with j_n - l_n = +1/2):
     N_Nordheim = +1 => favors the aligned chiral bandhead I_0 = 10^+ or 11^+!

References:
  - J. P. Schiffer and W. W. True, Rev. Mod. Phys. 48, 191 (1976).
  - A. Bohr and B. R. Mottelson, *Nuclear Structure*, Vol. I, §3-4 (pp. 314–332).
  - S. P. Pandya, Phys. Rev. 103, 956 (1956).
  - L. W. Nordheim, Phys. Rev. 78, 294 (1950).
  - A. Gargano et al., *The Nuclear Shell Model 70 Years after Its Advent*, Achievements and Prospects (2023).
"""

import math
import json
import argparse
import sys
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))
from surface_delta_interaction_pandya_calculator import calculate_wigner_6j


def calculate_semiclassical_angle_theta12(
    j1: float,
    j2: float,
    J_total: int
) -> Tuple[float, float]:
    """
    Computes cos(theta_12) and theta_12 in degrees for two angular momenta j1, j2 coupled to J.
    """
    j1_len = math.sqrt(j1 * (j1 + 1.0))
    j2_len = math.sqrt(j2 * (j2 + 1.0))

    if j1_len <= 0.0 or j2_len <= 0.0:
        return 0.0, 90.0

    num = float(J_total * (J_total + 1)) - j1 * (j1 + 1.0) - j2 * (j2 + 1.0)
    den = 2.0 * j1_len * j2_len

    cos_th = num / den
    cos_th_clamped = max(-1.0, min(1.0, cos_th))
    th_deg = math.degrees(math.acos(cos_th_clamped))
    return cos_th_clamped, th_deg


def calculate_schiffer_true_pp_spectrum(
    j1: float,
    j2: float,
    v_pair_MeV: float = -2.20,
    v1_MeV: float = 0.85,
    v2_MeV: float = -0.65
) -> Dict[str, Any]:
    """
    Computes universal particle-particle Schiffer-True two-body matrix elements V_pp(J).
    """
    is_identical = abs(j1 - j2) < 1e-4
    j_min = int(round(abs(j1 - j2)))
    j_max = int(round(j1 + j2))

    matrix_elements = {}
    tbme_list = []

    for J in range(j_min, j_max + 1):
        if is_identical and (J % 2 != 0):
            continue # Pauli principle forbids odd J for identical nucleons in single j-shell

        cos_th, th_deg = calculate_semiclassical_angle_theta12(j1, j2, J)

        # Legendre polynomials: P1(x) = x, P2(x) = 0.5 * (3*x^2 - 1)
        p2 = 0.5 * (3.0 * (cos_th ** 2) - 1.0)

        # Pairing delta term at J=0
        v_pair_term = v_pair_MeV if J == 0 else 0.0

        v_val = v_pair_term + v1_MeV * cos_th + v2_MeV * p2
        matrix_elements[J] = v_val

        tbme_list.append({
            "spin_J": J,
            "cos_theta_12": round(cos_th, 4),
            "angle_theta_12_deg": round(th_deg, 1),
            "V_pp_MeV": round(v_val, 4),
            "V_pp_keV": round(v_val * 1000.0, 1)
        })

    # Ground state spin is the lowest energy state
    sorted_by_energy = sorted(tbme_list, key=lambda x: x["V_pp_MeV"])
    j_ground = sorted_by_energy[0]["spin_J"]

    return {
        "j1": j1,
        "j2": j2,
        "multiplet_type": "particle_particle",
        "ground_state_spin_J": j_ground,
        "parameters": {"v_pair_MeV": v_pair_MeV, "v1_MeV": v1_MeV, "v2_MeV": v2_MeV},
        "spectrum": tbme_list,
        "raw_dict": matrix_elements
    }


def calculate_schiffer_true_ph_pandya_spectrum(
    j1: float,
    j2: float,
    v_pair_MeV: float = -2.20,
    v1_MeV: float = 0.85,
    v2_MeV: float = -0.65
) -> Dict[str, Any]:
    """
    Computes particle-hole two-body spectrum by applying exact Pandya transformation to Schiffer-True TBMEs.
    """
    pp_res = calculate_schiffer_true_pp_spectrum(j1, j2, v_pair_MeV, v1_MeV, v2_MeV)
    pp_dict = pp_res["raw_dict"]

    j_min = int(round(abs(j1 - j2)))
    j_max = int(round(j1 + j2))

    ph_list = []
    for J in range(j_min, j_max + 1):
        # V_ph(J) = - sum_{J'} (2*J' + 1) * Wigner_6j(j1, j2, J; j1, j2, J') * V_pp(J')
        val_ph = 0.0
        for J_prime, v_pp in pp_dict.items():
            w6j = calculate_wigner_6j(j1, j2, float(J), j1, j2, float(J_prime))
            val_ph += - (2.0 * float(J_prime) + 1.0) * w6j * v_pp

        cos_th, th_deg = calculate_semiclassical_angle_theta12(j1, j2, J)
        ph_list.append({
            "spin_J": J,
            "cos_theta_12": round(cos_th, 4),
            "angle_theta_12_deg": round(th_deg, 1),
            "V_ph_MeV": round(val_ph, 4),
            "V_ph_keV": round(val_ph * 1000.0, 1)
        })

    sorted_ph = sorted(ph_list, key=lambda x: x["V_ph_MeV"])
    j_bandhead = sorted_ph[0]["spin_J"]

    return {
        "j1": j1,
        "j2": j2,
        "multiplet_type": "particle_hole_pandya",
        "favored_bandhead_spin_J": j_bandhead,
        "spectrum": ph_list
    }


def evaluate_nordheim_coupling_rule(
    j_p: float,
    l_p: int,
    j_n: float,
    l_n: int
) -> Dict[str, Any]:
    """
    Evaluates Nordheim empirical coupling rules for odd-odd ground state spins.
    """
    # Nordheim number: N = (j_p - l_p) + (j_n - l_n)
    d_p = j_p - float(l_p) # +1/2 if j = l + 1/2, -1/2 if j = l - 1/2
    d_n = j_n - float(l_n)
    N_nordheim = d_p + d_n

    j_diff = int(round(abs(j_p - j_n)))
    j_sum = int(round(j_p + j_n))

    if abs(N_nordheim) < 1e-4:
        rule_type = "Strong Nordheim Rule (N = 0)"
        favored_spin = j_diff
        explanation = f"Intrinsically opposite spin-orbit couplings favor antiparallel alignment: J = |j_p - j_n| = {j_diff}."
    else:
        rule_type = "Weak Nordheim Rule (N = +/- 1)"
        favored_spin = j_sum
        explanation = f"Parallel spin-orbit couplings favor maximum alignment or intermediate coupling: J ~ j_p + j_n = {j_sum}."

    return {
        "j_proton": j_p,
        "l_proton": l_p,
        "j_neutron": j_n,
        "l_neutron": l_n,
        "nordheim_number_N": int(round(N_nordheim)),
        "rule_classification": rule_type,
        "predicted_favored_spin_J": favored_spin,
        "possible_spin_range": [j_diff, j_sum],
        "physics_explanation": explanation
    }


def format_text_report(pp_res: Dict[str, Any], ph_res: Optional[Dict[str, Any]] = None, nord_res: Optional[Dict[str, Any]] = None) -> str:
    lines = [
        "=" * 76,
        "   SCHIFFER-TRUE TWO-BODY MATRIX ELEMENT (TBME) & PANDYA INVERSION SUITE",
        "   Based on Schiffer & True (1976), Bohr-Mottelson Vol. I §3-4 & Nordheim (1950)",
        "=" * 76,
        f" SHELL MODEL CONFIGURATION: j1 = {pp_res['j1']}, j2 = {pp_res['j2']}",
        f"   Particle-Particle Ground State: J = {pp_res['ground_state_spin_J']}^+",
    ]

    if ph_res is not None:
        lines.append(f"   Particle-Hole Favored Bandhead: J = {ph_res['favored_bandhead_spin_J']}^+ (Chiral Aligned Bandhead)")

    if nord_res is not None:
        lines.extend([
            "-" * 76,
            f" NORDHEIM ODD-ODD SPIN COUPLING RULES:",
            f"   Nordheim Number N           : {nord_res['nordheim_number_N']}  [{nord_res['rule_classification']}]",
            f"   Predicted Favored Spin      : J_fav = {nord_res['predicted_favored_spin_J']}^+  (Allowed: {nord_res['possible_spin_range'][0]}^+ to {nord_res['possible_spin_range'][1]}^+)",
            f"   Physics Origin              : {nord_res['physics_explanation']}",
        ])

    lines.extend([
        "-" * 76,
        " SCHIFFER-TRUE PARTICLE-PARTICLE MULTIPLET SPECTRUM V_pp(J):",
        "   Spin J     theta_12 (deg)     cos(theta)      V_pp (MeV)      V_pp (keV)",
    ])
    for pt in pp_res["spectrum"]:
        lines.append(f"     {pt['spin_J']:2d}+        {pt['angle_theta_12_deg']:6.1f} deg        {pt['cos_theta_12']:7.4f}       {pt['V_pp_MeV']:8.4f}        {pt['V_pp_keV']:7.1f} keV")

    if ph_res is not None:
        lines.extend([
            "-" * 76,
            " PANDYA-TRANSFORMED PARTICLE-HOLE MULTIPLET SPECTRUM V_ph(J):",
            "   Spin J     theta_12 (deg)     cos(theta)      V_ph (MeV)      V_ph (keV)",
        ])
        for pt in ph_res["spectrum"]:
            lines.append(f"     {pt['spin_J']:2d}+        {pt['angle_theta_12_deg']:6.1f} deg        {pt['cos_theta_12']:7.4f}       {pt['V_ph_MeV']:8.4f}        {pt['V_ph_keV']:7.1f} keV")

    lines.extend([
        "-" * 76,
        " Methodological Significance for Chiral Bandheads:",
        "   - Semiclassical angle theta_12 = 180 deg (J=0) maximizes pairing in p-p multiplets.",
        "   - Pandya transformation inverts p-h spectrum, shifting lowest energy to J ~ j1 + j2.",
        "   - Explains the 10+ / 11+ chiral doublet bandhead spin in 134Pr (pi h11/2 (x) nu h11/2^-1).",
        "=" * 76
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Schiffer-True TBME, Pandya Inversion & Nordheim Coupling Analyzer"
    )
    parser.add_argument("--j1", type=float, default=5.5, help="First orbital j1 (default: 5.5 for h11/2)")
    parser.add_argument("--j2", type=float, default=5.5, help="Second orbital j2 (default: 5.5 for h11/2)")
    parser.add_argument("--preset", type=str, default="pr134_chiral_bandhead",
                        choices=["h11_2_squared_te134", "pr134_chiral_bandhead", "g9_2_squared_mo92", "bi210_pb210_pandya"],
                        help="Benchmark preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")

    args = parser.parse_args()

    j1_val = args.j1
    j2_val = args.j2
    nord_info = None

    if args.preset == "pr134_chiral_bandhead":
        # 134Pr: pi h11/2 (l=5, j=11/2) (x) nu h11/2^-1 (l=5, j=11/2)
        j1_val, j2_val = 5.5, 5.5
        nord_info = evaluate_nordheim_coupling_rule(j_p=5.5, l_p=5, j_n=5.5, l_n=5)
    elif args.preset == "h11_2_squared_te134":
        # 134Te: 2 protons in h11/2
        j1_val, j2_val = 5.5, 5.5
    elif args.preset == "g9_2_squared_mo92":
        # 92Mo: 2 protons in g9/2 (l=4, j=9/2)
        j1_val, j2_val = 4.5, 4.5
    elif args.preset == "bi210_pb210_pandya":
        # 210Bi: pi h9/2 (l=5, j=9/2) (x) nu g9/2 (l=4, j=9/2)
        j1_val, j2_val = 4.5, 4.5
        nord_info = evaluate_nordheim_coupling_rule(j_p=4.5, l_p=5, j_n=4.5, l_n=4)

    pp_spec = calculate_schiffer_true_pp_spectrum(j1_val, j2_val)
    ph_spec = calculate_schiffer_true_ph_pandya_spectrum(j1_val, j2_val)

    if args.json:
        out = {"pp_spectrum": pp_spec, "ph_spectrum": ph_spec}
        if nord_info is not None:
            out["nordheim_rule"] = nord_info
        print(json.dumps(out, indent=2))
    else:
        print(format_text_report(pp_spec, ph_spec, nord_info))


if __name__ == "__main__":
    main()
