#!/usr/bin/env python3
"""
spontaneous_fission_wkb_action_calculator.py
============================================
Spontaneous Fission (SF) Double-Humped Barrier WKB Quantum Penetration Action,
Hill-Wheeler Transmission & Half-Life Systematics Engine.

Physics Formulation:
--------------------
1. Double-Humped Fission Barrier & Hill-Wheeler Transmission:
   Based on 卢希庭《原子核物理（修订版）》第 4 章 §4.4, C. A. Bertulani "Introduction to Nuclear Reactions"
   Chapter 11, P. Möller et al. (Phys. Rev. C 79, 064304, 2009), and W. J. Swiatecki (1955):
   In actinide and superheavy nuclei, macroscopic liquid-drop energy combined with
   microscopic Strutinsky shell corrections creates a double-humped fission barrier:
     - Inner barrier A: Height E_A, parabolic curvature hbar * omega_A;
     - Intermediate well II: Depth E_II (fission isomer state);
     - Outer barrier B: Height E_B, parabolic curvature hbar * omega_B.

2. Hill-Wheeler Penetration Probabilities:
   For ground-state zero-point vibration energy E_0 ~ 0.5 - 1.0 MeV:
     P_A = 1.0 / [ 1.0 + exp( 2*pi * (E_A - E_0) / (hbar * omega_A) ) ]
     P_B = 1.0 / [ 1.0 + exp( 2*pi * (E_B - E_0) / (hbar * omega_B) ) ]
   Effective two-barrier penetration factor:
     P_tot = (P_A * P_B) / 4.0

3. Action Integral S_eff & Decay Constant:
   S_eff = -ln(P_tot) = 2*pi*(E_A - E_0)/(hbar*omega_A) + 2*pi*(E_B - E_0)/(hbar*omega_B) + ln(4)
   Assault frequency of the zero-point vibration:
     nu_0 = omega_0 / (2*pi) ~ 1.0e21 s^-1.
   Decay constant: lambda_SF = nu_0 * P_tot.
   Spontaneous fission half-life:
     T_1/2_SF = ln(2) / lambda_SF = [ ln(2) / nu_0 ] * exp(S_eff).

4. Swiatecki Systematics & Shell Correction Shielding:
   Swiatecki demonstrated that spontaneous fission half-lives follow:
     log10(T_1/2 [yr]) = a_sf * [ Z^2 / A - (Z^2 / A)_0 ] - k_shell * delta_U
   where ground-state shell stabilization energy delta_U (MeV) raises the inner barrier,
   preventing immediate spontaneous collapse and creating the "Island of Stability"!
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "238U_spontaneous_fission": {
        "description": "238U spontaneous fission benchmark (T1/2_exp ~ 8.2e15 yr)",
        "nucleus": "238U",
        "Z_charge": 92,
        "A_mass": 238,
        "E_A_MeV": 6.30,
        "hw_A_MeV": 1.00,
        "E_B_MeV": 5.65,
        "hw_B_MeV": 0.51,
        "E_0_MeV": 0.80,
        "delta_U_MeV": 2.2
    },
    "252Cf_spontaneous_fission": {
        "description": "252Cf commercial spontaneous fission neutron source (T1/2_exp = 85.7 yr)",
        "nucleus": "252Cf",
        "Z_charge": 98,
        "A_mass": 252,
        "E_A_MeV": 5.30,
        "hw_A_MeV": 1.05,
        "E_B_MeV": 5.05,
        "hw_B_MeV": 0.60,
        "E_0_MeV": 0.80,
        "delta_U_MeV": 1.5
    },
    "240Pu_spontaneous_fission": {
        "description": "240Pu reactor-grade plutonium fission benchmark (T1/2_exp ~ 1.14e11 yr)",
        "nucleus": "240Pu",
        "Z_charge": 94,
        "A_mass": 240,
        "E_A_MeV": 6.05,
        "hw_A_MeV": 1.02,
        "E_B_MeV": 5.15,
        "hw_B_MeV": 0.54,
        "E_0_MeV": 0.80,
        "delta_U_MeV": 2.0
    },
    "294Og_superheavy_sf": {
        "description": "294Og superheavy element Z=118 fission stability estimate",
        "nucleus": "294Og",
        "Z_charge": 118,
        "A_mass": 294,
        "E_A_MeV": 6.80,
        "hw_A_MeV": 0.90,
        "E_B_MeV": 4.50,
        "hw_B_MeV": 0.80,
        "E_0_MeV": 0.90,
        "delta_U_MeV": 5.8
    }
}


def calculate_sf_hill_wheeler_transmission(barrier_height_MeV, barrier_hw_MeV, energy_MeV):
    """
    Hill-Wheeler penetration probability through an inverted parabolic barrier:
      P = 1.0 / [ 1.0 + exp( 2*pi * (E_B - E) / hw ) ]
    """
    arg = 2.0 * math.pi * (barrier_height_MeV - energy_MeV) / max(1e-4, barrier_hw_MeV)
    if arg > 100.0:
        return float(math.exp(-arg)), float(arg)
    elif arg < -30.0:
        return 1.0, float(arg)
    else:
        P = 1.0 / (1.0 + math.exp(arg))
        return float(P), float(arg)


def calculate_double_hump_sf_half_life(E_A_MeV, hw_A_MeV, E_B_MeV, hw_B_MeV, E_0_MeV=0.80, nu_0=1.0e21):
    """
    Calculates two-barrier transmission, effective action S_eff, and spontaneous fission half-life.
    """
    P_A, arg_A = calculate_sf_hill_wheeler_transmission(E_A_MeV, hw_A_MeV, E_0_MeV)
    P_B, arg_B = calculate_sf_hill_wheeler_transmission(E_B_MeV, hw_B_MeV, E_0_MeV)

    if P_A > 0 and P_B > 0:
        P_tot = (P_A * P_B) / 4.0
        S_eff = arg_A + arg_B + math.log(4.0)
    else:
        P_tot = 1e-100
        S_eff = 230.0

    t_half_s = math.log(2.0) / (nu_0 * P_tot)
    seconds_per_year = 365.25 * 86400.0
    t_half_yr = t_half_s / seconds_per_year
    log10_t_half_yr = math.log10(max(1e-30, t_half_yr))

    return {
        "inner_barrier": {
            "E_A_MeV": float(E_A_MeV),
            "hw_A_MeV": float(hw_A_MeV),
            "penetration_P_A": float(P_A),
            "action_S_A": float(arg_A)
        },
        "outer_barrier": {
            "E_B_MeV": float(E_B_MeV),
            "hw_B_MeV": float(hw_B_MeV),
            "penetration_P_B": float(P_B),
            "action_S_B": float(arg_B)
        },
        "effective_action_S_eff": float(S_eff),
        "total_penetration_P_tot": float(P_tot),
        "T_half_seconds": float(t_half_s),
        "T_half_years": float(t_half_yr),
        "log10_T_half_years": float(log10_t_half_yr)
    }


def calculate_fissility_and_swiatecki(Z_charge, A_mass, delta_U_MeV=0.0):
    """
    Calculates macroscopic fissility parameter x and Swiatecki fissility theta.
    """
    fissility_Z2_over_A = (Z_charge**2) / float(A_mass)
    fissility_crit = 50.883 * (1.0 - 1.7826 * ((A_mass - 2 * Z_charge) / A_mass)**2)
    fissility_parameter_x = fissility_Z2_over_A / fissility_crit

    return {
        "Z2_over_A": float(fissility_Z2_over_A),
        "critical_fissility_limit": float(fissility_crit),
        "fissility_parameter_x": float(fissility_parameter_x),
        "shell_stabilization_delta_U_MeV": float(delta_U_MeV)
    }


def run_spontaneous_fission_analysis(nucleus, Z_charge, A_mass, E_A_MeV, hw_A_MeV, E_B_MeV, hw_B_MeV,
                                     E_0_MeV=0.80, delta_U_MeV=0.0):
    """
    Full execution pipeline for spontaneous fission simulation.
    """
    sf_res = calculate_double_hump_sf_half_life(E_A_MeV, hw_A_MeV, E_B_MeV, hw_B_MeV, E_0_MeV)
    swiatecki = calculate_fissility_and_swiatecki(Z_charge, A_mass, delta_U_MeV)

    return {
        "nucleus": nucleus,
        "Z_charge": Z_charge,
        "A_mass": A_mass,
        "zero_point_energy_E0_MeV": float(E_0_MeV),
        "fissility_systematics": swiatecki,
        "quantum_penetration": sf_res
    }


def format_text_report(res, title="Spontaneous Fission Barrier & Half-Life Engine"):
    fiss = res["fissility_systematics"]
    qp = res["quantum_penetration"]
    in_b = qp["inner_barrier"]
    out_b = qp["outer_barrier"]

    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Nucleus: {res['nucleus']} (Z = {res['Z_charge']}, A = {res['A_mass']})")
    lines.append("=" * 76)
    lines.append(f"  Fissility Parameter (Z^2 / A)   : {fiss['Z2_over_A']:.2f} (x = {fiss['fissility_parameter_x']:.3f} of critical {fiss['critical_fissility_limit']:.1f})")
    lines.append(f"  Shell Stabilization Energy deltaU: {fiss['shell_stabilization_delta_U_MeV']:.2f} MeV")
    lines.append(f"  Zero-Point Vibration Energy E_0 : {res['zero_point_energy_E0_MeV']:.2f} MeV")
    lines.append("-" * 76)
    lines.append("Double-Humped Fission Barrier Penetration Breakdown:")
    lines.append(f"  Inner Barrier A (Height, hw)    : E_A = {in_b['E_A_MeV']:.2f} MeV, hw_A = {in_b['hw_A_MeV']:.2f} MeV")
    lines.append(f"    Action S_A / Penetration P_A  : S_A = {in_b['action_S_A']:.2f} -> P_A = {in_b['penetration_P_A']:.2e}")
    lines.append(f"  Outer Barrier B (Height, hw)    : E_B = {out_b['E_B_MeV']:.2f} MeV, hw_B = {out_b['hw_B_MeV']:.2f} MeV")
    lines.append(f"    Action S_B / Penetration P_B  : S_B = {out_b['action_S_B']:.2f} -> P_B = {out_b['penetration_P_B']:.2e}")
    lines.append("-" * 76)
    lines.append(f"  Total WKB Action Integral S_eff : {qp['effective_action_S_eff']:.2f}")
    lines.append(f"  Total Penetration Factor P_tot  : {qp['total_penetration_P_tot']:.2e}")
    lines.append(f"  Spontaneous Fission Half-Life   : {qp['T_half_years']:.2e} years (log10(T1/2) = {qp['log10_T_half_years']:+.2f})")
    lines.append(f"  Equivalent Half-Life (Seconds)  : {qp['T_half_seconds']:.2e} s")
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Spontaneous Fission Double-Humped Barrier WKB Action & Half-Life Simulator."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load experimental preset")
    parser.add_argument("--nucleus", type=str, default="Heavy-Nucleus", help="Nucleus name")
    parser.add_argument("--charge-z", type=int, help="Atomic number Z")
    parser.add_argument("--mass-a", type=int, help="Mass number A")
    parser.add_argument("--ea", type=float, default=6.0, help="Inner barrier height in MeV")
    parser.add_argument("--hwa", type=float, default=1.0, help="Inner barrier curvature in MeV")
    parser.add_argument("--eb", type=float, default=5.5, help="Outer barrier height in MeV")
    parser.add_argument("--hwb", type=float, default=0.55, help="Outer barrier curvature in MeV")
    parser.add_argument("--e0", type=float, default=0.8, help="Zero point energy in MeV")
    parser.add_argument("--deltau", type=float, default=2.0, help="Shell correction energy in MeV")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        nuc = p["nucleus"]
        Z = p["Z_charge"]
        A = p["A_mass"]
        ea = p["E_A_MeV"]
        hwa = p["hw_A_MeV"]
        eb = p["E_B_MeV"]
        hwb = p["hw_B_MeV"]
        e0 = p.get("E_0_MeV", 0.80)
        deltau = p.get("delta_U_MeV", 2.0)
        title = f"Preset: {args.preset} ({p['description']})"
    elif args.charge_z and args.mass_a:
        nuc = args.nucleus
        Z = args.charge_z
        A = args.mass_a
        ea = args.ea
        hwa = args.hwa
        eb = args.eb
        hwb = args.hwb
        e0 = args.e0
        deltau = args.deltau
        title = "Custom User Input"
    else:
        return parser.print_help()

    res = run_spontaneous_fission_analysis(
        nucleus=nuc,
        Z_charge=Z,
        A_mass=A,
        E_A_MeV=ea,
        hw_A_MeV=hwa,
        E_B_MeV=eb,
        hw_B_MeV=hwb,
        E_0_MeV=e0,
        delta_U_MeV=deltau
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
