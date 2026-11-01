#!/usr/bin/env python3
"""
abrasion_ablation_fragmentation_calculator.py
============================================
Relativistic Heavy-Ion Projectile Fragmentation Abrasion-Ablation Model &
Goldhaber Momentum Distribution Simulator.

Physics & Formulation:
----------------------
1. Geometric Abrasion Stage (Glauber Clean-Cut Geometry):
   At relativistic beam energies (E_beam >= 100 MeV/nucleon):
   Projectiles and targets slice off participant nucleons in geometric overlap:
     R_p = r_0 * A_p^(1/3), R_t = r_0 * A_t^(1/3)  (r_0 ~ 1.2 fm)
   Overlap fraction at impact parameter b:
     F_overlap(b) ~ [ (R_p + R_t - b) / (2 * R_p) ]^2  (for b in |Rp - Rt| to Rp + Rt)
   Pre-fragment spectator mass:
     A_pre(b) = A_p * [ 1 - F_overlap(b) ]
     Z_pre(b) = A_pre(b) * (Z_p / A_p)

2. Pre-Fragment Excitation Energy:
   Clean-cut surface area excess creates excitation:
     E*(b) = epsilon_hole * [ A_p - A_pre(b) ]   (epsilon_hole ~ 13.3 MeV/removed nucleon)

3. Statistical Ablation Stage:
   The hot pre-fragment cools by evaporating nucleons (mean energy loss ~ S_n + 2T ~ 12 MeV/nucleon):
     Delta_A_abl = E*(b) / 12.0
   Final isotope residue mass:
     A_final = A_pre(b) - Delta_A_abl

4. Goldhaber Momentum Width:
   In projectile rest frame, Fermi momentum fluctuations yield Gaussian width:
     sigma_p^2 = sigma_0^2 * [ A_final * (A_p - A_final) / (A_p - 1) ]
   where sigma_0 = p_Fermi / sqrt(5) ~ 85 - 90 MeV/c.

References:
  - J. J. Gaimard and K. H. Schmidt, Nucl. Phys. A 531, 709 (1991) [EPAX / Abrasion-Ablation].
  - A. S. Goldhaber, Phys. Lett. B 53, 306 (1974).
  - C. A. Bertulani and P. Danielewicz, Introduction to Nuclear Reactions, CRC Press.
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple

HBAR_C_MEV_FM = 197.327


def calculate_geometric_abrasion(
    A_p: int,
    Z_p: int,
    A_t: int,
    Z_t: int,
    impact_parameter_fm: float,
    r0_fm: float = 1.20
) -> Dict[str, float]:
    """
    Computes pre-fragment mass, charge, and excitation energy at impact parameter b.
    """
    R_p = r0_fm * (A_p ** (1.0 / 3.0))
    R_t = r0_fm * (A_t ** (1.0 / 3.0))
    b = max(impact_parameter_fm, 0.0)

    # Check overlap condition
    if b >= (R_p + R_t):
        # Peripheral grazing: no abrasion
        f_overlap = 0.0
    elif b <= abs(R_p - R_t):
        # Central absorption
        f_overlap = 1.0 if R_t >= R_p else (R_t / R_p) ** 2
    else:
        # Partial overlap approximation
        f_overlap = ((R_p + R_t - b) / (2.0 * R_p)) ** 1.5
        f_overlap = max(min(f_overlap, 1.0), 0.0)

    A_part = f_overlap * float(A_p)
    A_pre = max(float(A_p) - A_part, 1.0)
    Z_pre = A_pre * (float(Z_p) / float(A_p))

    # Pre-fragment excitation energy: ~13.3 MeV per sheared nucleon
    epsilon_hole = 13.3  # MeV/nucleon
    E_excitation = A_part * epsilon_hole

    return {
        "impact_parameter_b_fm": round(b, 2),
        "R_p_fm": round(R_p, 2),
        "R_t_fm": round(R_t, 2),
        "overlap_fraction": round(f_overlap, 4),
        "abraded_participants_A": round(A_part, 1),
        "pre_fragment_mass_A_pre": round(A_pre, 1),
        "pre_fragment_charge_Z_pre": round(Z_pre, 1),
        "pre_fragment_excitation_MeV": round(E_excitation, 1)
    }


def simulate_ablation_cooling(
    A_pre: float,
    Z_pre: float,
    E_excitation_MeV: float,
    A_projectile: int,
    mean_evap_energy_MeV: float = 12.0,
    sigma_0_MeV_c: float = 88.0
) -> Dict[str, Any]:
    """
    Simulates statistical particle evaporation and computes final fragment properties
    and Goldhaber momentum width.
    """
    # Evaporated nucleons
    delta_A_abl = E_excitation_MeV / mean_evap_energy_MeV
    A_final = max(round(A_pre - delta_A_abl), 1)

    # Final charge: predominantly neutrons evaporated due to Coulomb barrier
    delta_Z_abl = 0.40 * delta_A_abl
    Z_final = max(round(Z_pre - delta_Z_abl), 1)

    # Goldhaber momentum width
    # sigma_p^2 = sigma_0^2 * [ A_f * (A_p - A_f) / (A_p - 1) ]
    if A_final < A_projectile and A_projectile > 1:
        sigma_sq = (sigma_0_MeV_c ** 2) * (A_final * (A_projectile - A_final)) / float(A_projectile - 1)
        sigma_p = math.sqrt(max(sigma_sq, 0.0))
    else:
        sigma_p = 0.0

    return {
        "evaporated_nucleons_A_abl": round(delta_A_abl, 1),
        "final_fragment_A": A_final,
        "final_fragment_Z": Z_final,
        "final_fragment_N": A_final - Z_final,
        "goldhaber_momentum_width_MeV_c": round(sigma_p, 1)
    }


def scan_fragmentation_yields(
    A_p: int = 136,
    Z_p: int = 54,
    A_t: int = 9,
    Z_t: int = 4,
    num_b_steps: int = 15
) -> Dict[str, Any]:
    """
    Scans impact parameters from peripheral to central collisions to map fragment production.
    """
    r0 = 1.20
    R_p = r0 * (A_p ** (1.0 / 3.0))
    R_t = r0 * (A_t ** (1.0 / 3.0))
    b_max = R_p + R_t

    # Total reaction cross section: sigma_R = pi * (R_p + R_t)^2 * 10 [mb]
    sigma_R_mb = math.pi * (b_max ** 2) * 10.0

    db = b_max / float(num_b_steps)
    fragments = []

    for i in range(1, num_b_steps):
        b = i * db
        abr = calculate_geometric_abrasion(A_p, Z_p, A_t, Z_t, b)
        abl = simulate_ablation_cooling(
            abr["pre_fragment_mass_A_pre"], abr["pre_fragment_charge_Z_pre"],
            abr["pre_fragment_excitation_MeV"], A_p
        )

        # Differential cross section weight dsigma = 2*pi*b*db
        dsigma_mb = 2.0 * math.pi * b * db * 10.0

        fragments.append({
            "b_fm": round(b, 2),
            "A_pre": abr["pre_fragment_mass_A_pre"],
            "E_star_MeV": abr["pre_fragment_excitation_MeV"],
            "A_final": abl["final_fragment_A"],
            "Z_final": abl["final_fragment_Z"],
            "sigma_p_MeV_c": abl["goldhaber_momentum_width_MeV_c"],
            "dsigma_mb": round(dsigma_mb, 1)
        })

    return {
        "projectile": f"Z={Z_p}, A={A_p}",
        "target": f"Z={Z_t}, A={A_t}",
        "total_reaction_cross_section_mb": round(sigma_R_mb, 1),
        "impact_parameter_profile": fragments
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   HEAVY-ION PROJECTILE FRAGMENTATION (ABRASION-ABLATION) ANALYZER")
    lines.append("=" * 72)
    lines.append(f" REACTION: {summary['projectile']} + {summary['target']}")
    lines.append(f"   Total Geometric Reaction Cross Sec : sigma_R = {summary['total_reaction_cross_section_mb']} mb")
    lines.append("-" * 72)
    lines.append(f" {'b (fm)':<8} {'A_pre':<8} {'E* (MeV)':<12} {'A_final':<10} {'Z_final':<10} {'sigma_p (MeV/c)':<16} {'dsigma (mb)':<12}")
    lines.append(" " + "-" * 70)

    for row in summary["impact_parameter_profile"][:12]:
        lines.append(
            f" {row['b_fm']:<8.2f} {row['A_pre']:<8.1f} {row['E_star_MeV']:<12.1f} "
            f"{row['A_final']:<10} {row['Z_final']:<10} {row['sigma_p_MeV_c']:<16.1f} {row['dsigma_mb']:<12.1f}"
        )
    lines.append("-" * 72)
    lines.append(" Physical Significance:")
    lines.append("   - Geometric clean-cut abrasion calculates spectator pre-fragment mass.")
    lines.append("   - Statistical ablation cooling evaporatively populates neutron-deficient/rich exotic beams.")
    lines.append("   - Goldhaber momentum width sigma_p predicts in-flight fragment momentum acceptance.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Heavy-Ion Abrasion-Ablation Fragmentation Simulator."
    )
    parser.add_argument("-Zp", type=int, default=54, help="Projectile charge Z_p (default: 54 for 136Xe)")
    parser.add_argument("-Ap", type=int, default=136, help="Projectile mass A_p (default: 136)")
    parser.add_argument("-Zt", type=int, default=4, help="Target charge Z_t (default: 4 for 9Be)")
    parser.add_argument("-At", type=int, default=9, help="Target mass A_t (default: 9)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    summary = scan_fragmentation_yields(args.Ap, args.Zp, args.At, args.Zt)

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
