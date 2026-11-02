#!/usr/bin/env python3
"""
coriolis_anti_pairing_gap_quenching_moi_engine.py
================================================
Coriolis Anti-Pairing (CAP) Dynamic Pairing Gap Quenching, Superfluid-to-Normal Phase
Transition & Triaxial Moments of Inertia Expansion Engine.

Physics Formulation:
--------------------
1. Mottelson-Valatin Coriolis Anti-Pairing (CAP) Effect:
   Based on A. Bohr & B. R. Mottelson "Nuclear Structure" Vol. II §4-3 & §6-3,
   "Chirality and Wobbling in Atomic Nuclei" (CRC Press 2025) Ch. 2 & Ch. 9 (PDF pp. 204–221),
   B. R. Mottelson & J. G. Valatin (Phys. Rev. Lett. 5, 511, 1960), and S. Frauendorf (RMP 73, 463, 2001):
   In superfluid deformed nuclei, time-reversed nucleon pairs (j, -j) experiencing Coriolis forces
   -2 * omega_rot x v are subjected to opposing rotational torques that unbind Cooper pairs.
   The self-consistent monopole pairing gap Delta(omega) quenches monotonically with rotational
   frequency omega:
     Delta(omega) = Delta_0 * sqrt( max( 0.0, 1.0 - (omega / omega_crit)^2 ) )
   where omega_crit is the critical CAP frequency where superfluidity completely collapses (Delta -> 0),
   driving a second-order quantum phase transition from nuclear superfluid to normal Fermi liquid.

2. Non-Linear Moment of Inertia Expansion:
   At low frequency, the moments of inertia J_k reflect irrotational fluid flow (J_irr ~ 0.3 - 0.5 * J_rig).
   As the pairing gap collapses, the moments of inertia expand non-linearly towards the rigid-body limit:
     J_k(Delta) = J_rig,k * [ 1.0 - ( 1.0 - J_irr,k / J_rig,k ) * (Delta(omega) / Delta_0) ]
   For triaxial nuclei, the intermediate (m) axis experiences the fastest expansion, creating the
   dynamical momentum space asymmetry that drives high-spin chiral bifurcation and wobbling motion.

3. Self-Consistent Spin Mapping:
   Since spin I = J_m(Delta(omega)) * omega, the system self-consistently maps the rotational
   frequency to angular momentum I, locating the critical CAP phase transition spin I_CAP.
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "163Lu_TSD_superfluid_to_normal_phase_transition": {
        "description": "163Lu TSD band CAP pairing collapse (Delta_0 = 0.95 MeV, omega_crit = 0.45 MeV/hbar, I_CAP ~ 36 hbar)",
        "nucleus": "163Lu",
        "delta_0_MeV": 0.95,
        "omega_crit_MeV": 0.45,
        "J_rigid_hbar2_per_MeV": {"J_s": 45.0, "J_m": 72.0, "J_l": 20.0},
        "J_irrotational_ratio": 0.40,
        "spins_to_evaluate": [10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0]
    },
    "130Ba_transitional_triaxial_cap": {
        "description": "130Ba transitional triaxial nucleus CAP quenching (Delta_0 = 1.15 MeV, omega_crit = 0.38 MeV/hbar)",
        "nucleus": "130Ba",
        "delta_0_MeV": 1.15,
        "omega_crit_MeV": 0.38,
        "J_rigid_hbar2_per_MeV": {"J_s": 22.0, "J_m": 35.0, "J_l": 12.0},
        "J_irrotational_ratio": 0.45,
        "spins_to_evaluate": [6.0, 10.0, 14.0, 18.0, 22.0, 26.0, 30.0]
    },
    "rigid_rotor_zero_pairing_limit": {
        "description": "Pure rigid rotor with zero pairing (Delta_0 = 0.0 MeV, normal Fermi state)",
        "nucleus": "Rigid-Limit",
        "delta_0_MeV": 0.0,
        "omega_crit_MeV": 0.50,
        "J_rigid_hbar2_per_MeV": {"J_s": 30.0, "J_m": 50.0, "J_l": 15.0},
        "J_irrotational_ratio": 1.00,
        "spins_to_evaluate": [10.0, 20.0, 30.0, 40.0]
    }
}


def calculate_cap_pairing_gap(omega_rot_MeV, delta_0_MeV, omega_crit_MeV):
    """
    Calculates dynamic pairing gap Delta(omega) and quenching fraction.
    """
    if delta_0_MeV <= 0.0:
        return {"delta_MeV": 0.0, "quenching_fraction": 1.0, "is_superfluid": False}

    ratio = abs(omega_rot_MeV) / max(1e-4, omega_crit_MeV)
    if ratio >= 1.0:
        delta_val = 0.0
        q_frac = 1.0
        is_super = False
    else:
        delta_val = delta_0_MeV * math.sqrt(1.0 - (ratio**2))
        q_frac = 1.0 - (delta_val / delta_0_MeV)
        is_super = True

    return {
        "delta_MeV": float(delta_val),
        "quenching_fraction": float(q_frac),
        "is_superfluid": is_super
    }


def calculate_cap_moments_of_inertia(delta_val, delta_0_MeV, J_rig_dict, irr_ratio):
    """
    Calculates principal moments of inertia [J_s, J_m, J_l] as pairing gap collapses.
    """
    moi_dict = {}
    delta_ratio = (delta_val / delta_0_MeV) if delta_0_MeV > 0 else 0.0

    for axis in ["J_s", "J_m", "J_l"]:
        j_rig = J_rig_dict[axis]
        j_irr = j_rig * irr_ratio
        # Interpolation from irrotational to rigid
        j_act = j_rig * (1.0 - (1.0 - (j_irr / j_rig)) * delta_ratio)
        moi_dict[axis] = float(j_act)

    return moi_dict


def solve_spin_state_cap(spin_I, delta_0_MeV, omega_crit_MeV, J_rig_dict, irr_ratio):
    """
    Self-consistently iterates to find rotational frequency omega that yields spin I = J_m(omega) * omega.
    """
    # Iterative bisection / root finding for omega
    w_low = 0.0
    w_high = max(1.2, omega_crit_MeV * 2.0)

    for _ in range(60):
        w_mid = 0.5 * (w_low + w_high)
        gap_info = calculate_cap_pairing_gap(w_mid, delta_0_MeV, omega_crit_MeV)
        moi = calculate_cap_moments_of_inertia(gap_info["delta_MeV"], delta_0_MeV, J_rig_dict, irr_ratio)
        i_calc = moi["J_m"] * w_mid

        if i_calc < spin_I:
            w_low = w_mid
        else:
            w_high = w_mid

    w_sol = 0.5 * (w_low + w_high)
    final_gap = calculate_cap_pairing_gap(w_sol, delta_0_MeV, omega_crit_MeV)
    final_moi = calculate_cap_moments_of_inertia(final_gap["delta_MeV"], delta_0_MeV, J_rig_dict, irr_ratio)

    # Wobbling factor: sqrt( (J_m - J_s)(J_m - J_l) / (J_s * J_l) )
    js, jm, jl = final_moi["J_s"], final_moi["J_m"], final_moi["J_l"]
    if jm > js and jm > jl and js > 0 and jl > 0:
        wob_factor = math.sqrt(((jm - js) * (jm - jl)) / (js * jl))
        hw_wob_keV = w_sol * wob_factor * 1000.0
    else:
        wob_factor = 0.0
        hw_wob_keV = 0.0

    return {
        "spin_I": float(spin_I),
        "rotational_frequency_MeV": float(w_sol),
        "pairing_gap_MeV": float(final_gap["delta_MeV"]),
        "gap_quenching_pct": float(final_gap["quenching_fraction"] * 100.0),
        "is_superfluid": final_gap["is_superfluid"],
        "moments_of_inertia": final_moi,
        "wobbling_frequency_keV": float(hw_wob_keV)
    }


def run_cap_analysis(nucleus, delta_0_MeV, omega_crit_MeV, J_rig_dict, irr_ratio, spins):
    """
    Complete execution pipeline for Coriolis Anti-Pairing analysis across spin range.
    """
    spin_results = []
    for I in spins:
        pt = solve_spin_state_cap(I, delta_0_MeV, omega_crit_MeV, J_rig_dict, irr_ratio)
        spin_results.append(pt)

    # Determine critical transition spin I_CAP where gap drops below 5%
    I_cap = None
    for pt in spin_results:
        if not pt["is_superfluid"] or pt["pairing_gap_MeV"] < 0.05 * delta_0_MeV:
            I_cap = pt["spin_I"]
            break

    return {
        "nucleus": nucleus,
        "parameters": {
            "initial_pairing_gap_Delta0_MeV": float(delta_0_MeV),
            "critical_CAP_frequency_MeV": float(omega_crit_MeV),
            "irrotational_fluid_ratio": float(irr_ratio),
            "rigid_body_MOI": J_rig_dict
        },
        "critical_transition_spin_I_CAP": I_cap,
        "spin_evolution": spin_results
    }


def format_text_report(res, title="Coriolis Anti-Pairing (CAP) Dynamic Gap Quenching Engine"):
    nuc = res["nucleus"]
    p = res["parameters"]
    evol = res["spin_evolution"]
    I_c = res["critical_transition_spin_I_CAP"]

    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Nucleus: {nuc} | Delta_0 = {p['initial_pairing_gap_Delta0_MeV']:.2f} MeV, omega_crit = {p['critical_CAP_frequency_MeV']:.2f} MeV/hbar")
    lines.append("=" * 76)
    lines.append("Rigid-Body Reference Moments of Inertia [J_s, J_m, J_l]:")
    r = p["rigid_body_MOI"]
    lines.append(f"  Rigid Limit: J_s = {r['J_s']:.1f}, J_m = {r['J_m']:.1f}, J_l = {r['J_l']:.1f} hbar^2/MeV (Irr fluid base = {p['irrotational_fluid_ratio']*100:.0f}%)")
    lines.append(f"  CAP Phase Transition Threshold : {f'I_CAP ~ {I_c:.1f} hbar' if I_c is not None else 'None in range'}")
    lines.append("-" * 76)
    lines.append("Spin-Dependent Dynamic Pairing Gap Quenching & MOI Expansion:")
    lines.append("  Spin I (hbar)  omega (MeV)   Delta (MeV)   Quench (%)   Phase         J_m (hbar^2/MeV)  hbar*w_wob (keV)")
    for pt in evol:
        ph_str = "Superfluid" if pt["is_superfluid"] else "NORMAL (Rigid)"
        lines.append(f"    {pt['spin_I']:4.1f}          {pt['rotational_frequency_MeV']:6.3f}        {pt['pairing_gap_MeV']:6.3f}       {pt['gap_quenching_pct']:5.1f}%     {ph_str:13}     {pt['moments_of_inertia']['J_m']:6.2f}            {pt['wobbling_frequency_keV']:7.1f}")
    lines.append("-" * 76)
    lines.append("Physics Impact: Coriolis Anti-Pairing drives non-linear expansion of J_m,")
    lines.append("stabilizing high-spin triaxial wobbling before final band termination.")
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Coriolis Anti-Pairing Dynamic Gap Quenching & MOI Expansion Engine."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load benchmark preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        nucleus = p["nucleus"]
        d0 = p["delta_0_MeV"]
        w_c = p["omega_crit_MeV"]
        j_rig = p["J_rigid_hbar2_per_MeV"]
        irr = p["J_irrotational_ratio"]
        spins = p["spins_to_evaluate"]
        title = f"Preset: {args.preset} ({p['description']})"
    else:
        return parser.print_help()

    res = run_cap_analysis(
        nucleus=nucleus,
        delta_0_MeV=d0,
        omega_crit_MeV=w_c,
        J_rig_dict=j_rig,
        irr_ratio=irr,
        spins=spins
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
