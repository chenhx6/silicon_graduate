#!/usr/bin/env python3
"""
gamma_cascade_calorimetry_calculator.py
=======================================
Compound Nucleus Multi-Step Gamma-Ray Cascade Calorimetry & Multiplicity
Filter Analyzer.

Physics & Formulation:
----------------------
1. Entry State (E*, I) Distribution after Particle Evaporation:
   - Residual entry excitation energy: E_entry = E_yrast(I) + Delta_E_stat
   - Yrast line approximation: E_yrast(I) = (hbar^2 / (2 * J_eff)) * I*(I + 1)
     where J_eff ~ 0.85 * J_rigid.

2. Two-Stage Cascade De-excitation Model:
   - Stage 1: Statistical Cooling Cascade (quasicontinuum E1):
     Carries away excitation energy with minimal spin change:
       M_stat ~ Delta_E_stat / <E_gamma_stat>   (<E_gamma_stat> ~ 1.5 - 2.5 MeV)
       Delta_I_stat ~ 0 - 1 hbar
   - Stage 2: Collective Yrast Cascade (stretched E2 transitions):
     Carries away angular momentum along rotational bands:
       M_coll = (I_entry - I_ground) / 2
   Total multiplicity:
     M_gamma = M_stat + M_coll
   Total sum energy:
     E_sum = E_entry - E_ground

3. 4pi Calorimeter Array Response (e.g. BGO / BaF2 Ball):
   - Measured fold k relates to true multiplicity M_gamma via binomial response:
     <k> = Omega_eff * M_gamma
     where Omega_eff is the total array detection efficiency (~ 0.70 - 0.90).
   - Measured total energy H relates to E_sum via absorption fraction f_abs (~ 0.85).

4. 2D (E_sum, M_gamma) Reaction Channel Triage:
   Separates competing evaporation channels (e.g. 3n, 4n, 5n) based on entry centroids:
     E_sum(4n) > E_sum(5n) by ~ S_n (~ 8 MeV).

References:
  - F. S. Stephens, Rev. Mod. Phys. 47, 43 (1975).
  - M. Jaaskelainen et al., Nucl. Instrum. Methods 204, 385 (1983) [Spin Spectrometer].
  - 吴治华, 《原子核物理实验方法》, 第三版.
  - IAEA-RIPL Handbook on Reaction Data Calculations.
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_yrast_energy(spin_I: float, A_mass: int) -> float:
    """Computes rigid-body-like Yrast energy in MeV: E = (hbar^2 / 2J) * I(I+1)."""
    # J_rigid = 0.01389 * A^(5/3) / hbar^2 [MeV^-1]
    # hbar^2 / (2*J) = 1.0 / (2 * 0.01389 * A^(5/3)) * (1 / 0.85)
    r_factor = 0.01389 * (A_mass ** (5.0 / 3.0)) * 0.85
    A_rot = 1.0 / (2.0 * max(r_factor, 1e-4))
    return A_rot * spin_I * (spin_I + 1.0)


def simulate_gamma_cascade(
    entry_spin_I: float,
    entry_excitation_MeV: float,
    A_mass: int = 130,
    mean_stat_energy_MeV: float = 2.0,
    array_efficiency: float = 0.80,
    array_energy_absorption: float = 0.85
) -> Dict[str, Any]:
    """
    Simulates statistical E1 + collective E2 gamma-ray cascade from an entry state (E*, I).
    """
    e_yrast = calculate_yrast_energy(entry_spin_I, A_mass)

    # Delta_E above Yrast
    delta_e_stat = max(entry_excitation_MeV - e_yrast, 0.0)

    # Stage 1: Statistical E1 cooling
    M_stat = delta_e_stat / mean_stat_energy_MeV if delta_e_stat > 0 else 0.0
    M_stat = round(M_stat, 1)

    # Stage 2: Collective stretched E2
    M_coll = max(entry_spin_I / 2.0, 0.0)
    M_coll = round(M_coll, 1)

    total_multiplicity = M_stat + M_coll
    total_energy_sum = entry_excitation_MeV

    # Calorimeter response
    measured_mean_fold = total_multiplicity * array_efficiency
    measured_mean_energy = total_energy_sum * array_energy_absorption

    return {
        "A_mass": A_mass,
        "entry_spin_I": entry_spin_I,
        "entry_excitation_MeV": entry_excitation_MeV,
        "yrast_energy_at_spin_MeV": round(e_yrast, 2),
        "energy_above_yrast_MeV": round(delta_e_stat, 2),
        "statistical_E1_multiplicity": M_stat,
        "collective_E2_multiplicity": M_coll,
        "total_true_multiplicity": round(total_multiplicity, 1),
        "total_cascade_energy_MeV": round(total_energy_sum, 2),
        "measured_mean_fold": round(measured_mean_fold, 1),
        "measured_mean_sum_energy_MeV": round(measured_mean_energy, 2)
    }


def compare_evaporation_channel_entry_points(
    compound_excitation_MeV: float,
    A_cn: int,
    channels: List[int] = [3, 4, 5],  # number of evaporated neutrons xn
    S_n_MeV: float = 8.0,
    T_neutron_MeV: float = 1.5
) -> List[Dict[str, Any]]:
    """
    Computes expected centroid in (E_sum, M_gamma) space for xn evaporation residues.
    """
    results = []
    for xn in channels:
        # Each evaporated neutron carries away S_n + 2*T
        e_removed = xn * (S_n_MeV + 2.0 * T_neutron_MeV)
        e_entry = max(compound_excitation_MeV - e_removed, 1.0)

        # Average angular momentum removed per neutron ~ 1.5 hbar
        # Assume initial CN spin ~ 35 hbar
        cn_spin = 35.0
        spin_entry = max(cn_spin - xn * 1.5, 2.0)

        casc = simulate_gamma_cascade(spin_entry, e_entry, A_cn - xn)

        results.append({
            "channel": f"{xn}n",
            "residual_A": A_cn - xn,
            "entry_excitation_MeV": round(e_entry, 2),
            "entry_spin_hbar": round(spin_entry, 1),
            "total_multiplicity_M": casc["total_true_multiplicity"],
            "calorimeter_mean_fold": casc["measured_mean_fold"],
            "calorimeter_sum_energy_MeV": casc["measured_mean_sum_energy_MeV"]
        })

    return results


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   GAMMA-RAY CASCADE CALORIMETRY & MULTIPLICITY FILTER ANALYZER")
    lines.append("=" * 72)

    if "single_cascade" in summary:
        sc = summary["single_cascade"]
        lines.append(f" ENTRY STATE PARAMETERS: E* = {sc['entry_excitation_MeV']} MeV, I = {sc['entry_spin_I']} hbar (A = {sc['A_mass']})")
        lines.append(f"   Yrast Line Energy at Spin I    : {sc['yrast_energy_at_spin_MeV']} MeV")
        lines.append(f"   Thermal Energy above Yrast     : {sc['energy_above_yrast_MeV']} MeV")
        lines.append(f"   Statistical E1 Cooling Photons : M_stat = {sc['statistical_E1_multiplicity']}")
        lines.append(f"   Collective E2 Yrast Cascade    : M_coll = {sc['collective_E2_multiplicity']}")
        lines.append(f"   Total True Cascade Multiplicity: M_gamma = {sc['total_true_multiplicity']}")
        lines.append(f"   Calorimeter Measured Fold <k>  : {sc['measured_mean_fold']}")
        lines.append(f"   Calorimeter Measured Sum Energy: {sc['measured_mean_sum_energy_MeV']} MeV")
        lines.append("-" * 72)

    if "channel_triage" in summary:
        lines.append(" EVAPORATION CHANNEL SEPARATION IN (E_sum, M_gamma) SPACE:")
        lines.append(f"   {'Channel':<10} {'Entry E* (MeV)':<16} {'Entry Spin (hbar)':<18} {'True M_gamma':<14} {'Meas. Fold':<12}")
        lines.append("   " + "-" * 66)
        for ch in summary["channel_triage"]:
            lines.append(f"   {ch['channel']:<10} {ch['entry_excitation_MeV']:<16.2f} {ch['entry_spin_hbar']:<18.1f} {ch['total_multiplicity_M']:<14.1f} {ch['calorimeter_mean_fold']:<12.1f}")
        lines.append("-" * 72)

    lines.append(" Physical Significance:")
    lines.append("   - Statistical E1 cools excitation while collective E2 sheds angular momentum.")
    lines.append("   - (E_sum, Fold) gating isolates target xn reaction channels without particle detectors.")
    lines.append("   - Fundamental technique in BGO balls, Gammasphere, and CAGRA filter arrays.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Gamma Cascade Calorimetry & Multiplicity Filter Analyzer."
    )
    parser.add_argument("-E", "--entry-e", type=float, default=24.0, help="Entry state excitation energy E* in MeV (default: 24.0)")
    parser.add_argument("-I", "--entry-spin", type=float, default=22.0, help="Entry state spin I in hbar (default: 22.0)")
    parser.add_argument("-A", "--mass", type=int, default=130, help="Mass number A (default: 130)")
    parser.add_argument("--triage", action="store_true", help="Perform xn channel entry separation scan")
    parser.add_argument("--cn-e", type=float, default=58.0, help="Compound nucleus excitation energy in MeV for triage")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    casc = simulate_gamma_cascade(args.entry_spin, args.entry_e, args.mass)
    summary = {"single_cascade": casc}

    if args.triage or args.entry_e == 24.0:
        triage_data = compare_evaporation_channel_entry_points(args.cn_e, args.mass + 4)
        summary["channel_triage"] = triage_data

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
