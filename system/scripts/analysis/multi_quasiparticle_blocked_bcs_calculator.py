#!/usr/bin/env python3
"""
multi_quasiparticle_blocked_bcs_calculator.py
=============================================
Multi-Quasiparticle (2qp, 4qp, 6qp) Blocked BCS Pairing Gap Reduction,
High-K Isomer Energy & Residual Interaction Calculator.

Physics & Formulation:
----------------------
1. Blocked BCS Gap Equation:
   When valence quasiparticles occupy orbitals {k_b} (b = 1, ..., M):
     (2 / G) = sum_{k not in {k_b}} [ 1 / sqrt((eps_k - lambda_b)^2 + Delta_b^2) ]
     N_part = M + 2 * sum_{k not in {k_b}} v_k^2
   where:
     v_k^2 = 0.5 * [ 1 - (eps_k - lambda_b) / E_k ]
     E_k = sqrt((eps_k - lambda_b)^2 + Delta_b^2)

2. Pairing Collapse via Blocking:
   Each blocked state eliminates a level near the Fermi surface from pair scattering:
     Delta_2qp ~ 0.70 - 0.85 * Delta_0
     Delta_4qp ~ 0.40 - 0.60 * Delta_0
     Delta_6qp -> 0 (Pairing collapse to normal Fermi gas)

3. Multi-Quasiparticle State Excitation Energy:
   E_x(K^pi) = sum_{b=1}^M E_k_b(Delta_b) + [E_condensation(Delta_0) - E_condensation(Delta_b)] + Delta_E_residual
   where:
     K = sum_b Omega_b
     pi = prod_b pi_b
     E_cond = -0.5 * Delta^2 / d_level (condensation energy)

4. Residual Interaction (Gallagher-Moszkowski + Like-Nucleon force):
   Delta_E_residual ~ sum_{pairs} V_res(sigma_1 . sigma_2)

References:
  - P. M. Walker and G. D. Dracoulis, Nature 402, 35 (1999).
  - A. Bohr and B. R. Mottelson, Nuclear Structure, Vol. II, Benjamin (1975).
  - P. Ring and P. Schuck, The Nuclear Many-Body Problem, Springer (1980).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def solve_unblocked_bcs(
    single_particle_energies: List[float],
    pairing_G_MeV: float = 0.18,
    target_particles: int = 10,
    max_iter: int = 100
) -> Tuple[float, float]:
    """
    Solves unblocked BCS gap Delta_0 and Fermi level lambda_0.
    Returns (Delta_0, lambda_0) in MeV.
    """
    eps = sorted(single_particle_energies)
    n_levels = len(eps)

    # Initial guess: lambda midway around target_particles
    mid_idx = min(max(target_particles // 2, 0), n_levels - 1)
    lam = eps[mid_idx]
    delta = 1.0  # initial gap guess

    for _ in range(max_iter):
        # 1. Update lambda to match particle number N = 2 * sum v_k^2
        for _ in range(15):
            n_calc = sum(1.0 - (e - lam) / math.sqrt((e - lam)**2 + delta**2) for e in eps)
            dn_dlam = sum((delta**2) / (((e - lam)**2 + delta**2)**1.5) for e in eps)
            diff = n_calc - target_particles
            if abs(diff) < 1e-4:
                break
            lam -= diff / max(dn_dlam, 1e-4)

        # 2. Update delta from gap equation 2/G = sum 1 / E_k
        sum_inv_e = sum(1.0 / math.sqrt((e - lam)**2 + delta**2) for e in eps)
        target_inv_g = 2.0 / max(pairing_G_MeV, 1e-4)

        # Secant/Newton step on delta
        f_val = sum_inv_e - target_inv_g
        df_ddelta = - sum(delta / (((e - lam)**2 + delta**2)**1.5) for e in eps)
        delta_step = f_val / min(df_ddelta, -1e-4)

        new_delta = delta - delta_step
        if new_delta <= 0.05:
            new_delta = 0.05

        if abs(new_delta - delta) < 1e-4:
            delta = new_delta
            break
        delta = new_delta

    return delta, lam


def solve_blocked_bcs(
    single_particle_energies: List[float],
    blocked_indices: List[int],
    pairing_G_MeV: float = 0.18,
    target_particles: int = 10
) -> Tuple[float, float]:
    """
    Solves blocked BCS equation omitting blocked levels from pair scattering.
    """
    eps = sorted(single_particle_energies)
    m_blocked = len(blocked_indices)
    active_eps = [eps[i] for i in range(len(eps)) if i not in blocked_indices]

    active_particles = max(target_particles - m_blocked, 0)

    if len(active_eps) == 0 or active_particles <= 0:
        return 0.0, 0.0

    delta_b, lam_b = solve_unblocked_bcs(active_eps, pairing_G_MeV, active_particles)
    return delta_b, lam_b


def calculate_multi_quasiparticle_energy(
    quasiparticle_orbitals: List[Dict[str, Any]],  # list of {"name": str, "energy_MeV": float, "Omega": float, "parity": int}
    core_G_pairing_MeV: float = 0.18,
    target_particles: int = 10,
    residual_interaction_MeV: float = -0.20
) -> Dict[str, Any]:
    """
    Calculates multi-quasiparticle state properties, blocked gap Delta_b,
    total K^pi, and excitation energy.
    """
    # Synthetic single-particle spectrum around Fermi surface
    sp_energies = [-3.0, -2.2, -1.5, -0.8, -0.2, 0.4, 1.1, 1.8, 2.5, 3.2, 4.0, 4.8]

    # Unblocked reference
    delta_0, lam_0 = solve_unblocked_bcs(sp_energies, core_G_pairing_MeV, target_particles)

    # Map QP orbitals to levels
    m_qp = len(quasiparticle_orbitals)
    blocked_idx = list(range(4, 4 + m_qp))  # block levels around Fermi surface

    delta_b, lam_b = solve_blocked_bcs(sp_energies, blocked_idx, core_G_pairing_MeV, target_particles)

    # Total K and parity
    total_K = sum(qp["Omega"] for qp in quasiparticle_orbitals)
    total_parity = 1
    for qp in quasiparticle_orbitals:
        total_parity *= qp.get("parity", 1)

    # Quasiparticle energies under blocked field
    qp_energies_sum = 0.0
    for qp in quasiparticle_orbitals:
        e_sp = qp["energy_MeV"]
        E_qp = math.sqrt((e_sp - lam_b)**2 + delta_b**2)
        qp_energies_sum += E_qp

    # Condensation energy loss: E_cond ~ 0.5 * (Delta_0^2 - Delta_b^2) / d_level
    d_level = 0.6  # mean level spacing in MeV
    e_cond_loss = 0.5 * (delta_0**2 - delta_b**2) / d_level

    # Net excitation energy
    E_excitation = qp_energies_sum + e_cond_loss + residual_interaction_MeV

    gap_reduction_percent = (1.0 - delta_b / max(delta_0, 1e-4)) * 100.0

    return {
        "multi_quasiparticle_type": f"{m_qp}-quasiparticle ({m_qp}qp)",
        "total_K": round(total_K, 1),
        "total_parity": "+" if total_parity > 0 else "-",
        "state_label": f"K^pi = {total_K:.0f}{'+' if total_parity > 0 else '-'}" if total_K.is_integer() else f"K^pi = {total_K:.1f}{'+' if total_parity > 0 else '-'}",
        "unblocked_pairing_gap_Delta0_MeV": round(delta_0, 3),
        "blocked_pairing_gap_Delta_b_MeV": round(delta_b, 3),
        "pairing_gap_reduction_percent": round(gap_reduction_percent, 1),
        "quasiparticle_sum_energy_MeV": round(qp_energies_sum, 3),
        "condensation_energy_loss_MeV": round(e_cond_loss, 3),
        "residual_interaction_shift_MeV": round(residual_interaction_MeV, 3),
        "predicted_excitation_energy_MeV": round(E_excitation, 3)
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   MULTI-QUASIPARTICLE BLOCKED BCS PAIRING & HIGH-K ISOMER ANALYZER")
    lines.append("=" * 72)
    lines.append(f" STATE CONFIGURATION: {summary['multi_quasiparticle_type']}, {summary['state_label']}")
    lines.append("-" * 72)
    lines.append(" SELF-CONSISTENT PAIRING BLOCKING EFFECT:")
    lines.append(f"   Unblocked Ground State Gap Delta_0: {summary['unblocked_pairing_gap_Delta0_MeV']} MeV")
    lines.append(f"   Blocked Multi-QP Gap Delta_b      : {summary['blocked_pairing_gap_Delta_b_MeV']} MeV")
    lines.append(f"   Pairing Gap Quenching / Collapse  : {summary['pairing_gap_reduction_percent']}% reduction")
    lines.append("-" * 72)
    lines.append(" ENERGY BALANCE DECOMPOSITION:")
    lines.append(f"   Quasiparticle Intrinsic Sum       : {summary['quasiparticle_sum_energy_MeV']} MeV")
    lines.append(f"   Condensation Energy Penalty       : {summary['condensation_energy_loss_MeV']} MeV")
    lines.append(f"   Residual p-n / p-p Interaction    : {summary['residual_interaction_shift_MeV']} MeV")
    lines.append(f"   Total Predicted Excitation Energy : {summary['predicted_excitation_energy_MeV']} MeV")
    lines.append("-" * 72)
    lines.append(" Physical Significance:")
    lines.append("   - Pauli blocking by unpaired quasiparticles quenches BCS pairing gap.")
    lines.append("   - Pairing reduction increases dynamic moment of inertia J(2).")
    lines.append("   - Crucial for identifying high-K isomers in 178Hf, 130Ba, and 134Ce.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Multi-Quasiparticle Blocked BCS Pairing & High-K Isomer Calculator."
    )
    parser.add_argument("--num-qp", type=int, default=2, choices=[2, 4, 6], help="Number of quasiparticles (2, 4, 6)")
    parser.add_argument("--omegas", type=str, default="3.5,4.5", help="Comma-separated Omega values (default: 3.5,4.5 for K=8)")
    parser.add_argument("--parities", type=str, default="1,1", help="Comma-separated parities (+1 or -1)")
    parser.add_argument("--G", type=float, default=0.18, help="Pairing force G in MeV (default: 0.18)")
    parser.add_argument("--v-res", type=float, default=-0.25, help="Residual interaction shift in MeV (default: -0.25)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    om_list = [float(x.strip()) for x in args.omegas.split(",")]
    par_list = [int(x.strip()) for x in args.parities.split(",")]

    qps = []
    for idx, (om, p) in enumerate(zip(om_list, par_list)):
        qps.append({
            "name": f"qp_{idx+1}",
            "energy_MeV": 0.2 * (idx + 1),
            "Omega": om,
            "parity": p
        })

    summary = calculate_multi_quasiparticle_energy(qps, args.G, target_particles=10, residual_interaction_MeV=args.v_res)

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
