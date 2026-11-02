#!/usr/bin/env python3
"""
seniority_scheme_half_filled_isomer_calculator.py
=================================================
Nuclear Seniority Scheme (v), Fractional Parentage B(E2) Vanishing Factor in Half-Filled
High-j Shells & Seniority Isomer Lifetime Engine.

Physics & Formulation:
----------------------
1. The Seniority Quantum Number (v):
   In identical nucleon configurations j^n (e.g. h_11/2 in Sn/Te, g_9/2 in Ru/Pd, i_13/2 in Pb),
   particles interact predominantly through the short-range pairing force.
   The seniority quantum number v represents the number of unpaired nucleons that are not coupled
   to J=0 pairs.
   - For even-even nuclei: ground state has v = 0 (J = 0^+);
     lowest excited states have v = 2 with spins J = 2, 4, 6, ..., (2j - 1).
   - In a pure pairing force, all v = 2 states are degenerate, separated from the v = 0 ground state
     by the pairing energy gap:
       Delta_pair = G * (2j + 1) / 2

2. Fractional Parentage & B(E2) Vanishing Factor:
   Racah algebra and second quantization prove that the reduced electric quadrupole transition
   probability between states of the same seniority (v -> v, Delta_v = 0) scales with nucleon number n as:
     B(E2; j^n, v, J -> v, J') = [ (2j + 1 - 2n) / (2j + 1 - 2v) ]^2 * B(E2; j^v, v, J -> v, J')

3. The Half-Filled Shell Isomer Mechanism:
   Notice the numerator:
     F_seniority(j, n) = (2j + 1 - 2n)
   When the j-shell is exactly half-filled:
     n_half = (2j + 1) / 2 = j + 1/2
   The factor drops strictly to zero:
     F_seniority(j, n_half) == 0  =>  B(E2; j^n_half, v=2 -> v=2) == 0.0 !
   Because the dominant collective E2 de-excitation channel is canceled by particle-hole symmetry,
   the highest-spin state in the v=2 multiplet (e.g. J = 2j - 1, such as 10^+ in h_11/2 or 8^+ in g_9/2)
   cannot decay rapidly. Its lifetime increases by 3 to 6 orders of magnitude, forming a **Seniority Isomer**!

4. Transition Probability & Isomer Half-Life:
   The E2 decay constant:
     lambda(E2) = 1.225e9 * (E_gamma_MeV^5) * B(E2_e2_b2)  s^-1
     T_1/2 = ln(2) / lambda(E2)
   The seniority hindrance factor:
     HF_seniority = [ (2j + 1 - 2v) / (2j + 1 - 2n) ]^2

References:
  - A. Bohr and B. R. Mottelson, *Nuclear Structure*, Vol. I, §3-4 (pp. 314–332).
  - A. K. Jain et al., *Nuclear Isomers: A Primer*, Springer (2021), Ch. 3 & Ch. 5.
  - K. L. G. Heyde, *Basic Ideas and Concepts in Nuclear Physics*, Ch. 8.
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_seniority_fractional_factor(
    j_orbital: float,
    n_particles: int,
    v_seniority: int = 2
) -> Dict[str, Any]:
    """
    Calculates the Racah seniority fractional parentage factor for Delta_v = 0 E2 transitions:
      F = (2j + 1 - 2n) / (2j + 1 - 2v)
    """
    if j_orbital <= 0.5:
        raise ValueError("Orbital angular momentum j must be at least 3/2.")
    if int(round(2.0 * j_orbital)) % 2 == 0:
        raise ValueError("Orbital j must be half-integer (e.g. 1.5, 2.5, 5.5).")

    two_j_plus_1 = int(round(2.0 * j_orbital + 1.0))

    if not (0 <= n_particles <= two_j_plus_1):
        raise ValueError(f"Number of particles n must be between 0 and 2j+1 = {two_j_plus_1}.")

    denominator = float(two_j_plus_1 - 2 * v_seniority)
    if abs(denominator) < 1e-6:
        raise ValueError("Invalid seniority v for this shell.")

    numerator = float(two_j_plus_1 - 2 * n_particles)
    fractional_factor = numerator / denominator
    b_e2_scaling_factor = fractional_factor ** 2

    n_half = float(two_j_plus_1) / 2.0
    is_half_filled = (n_particles == int(n_half))

    return {
        "j_orbital": j_orbital,
        "shell_capacity_2j_plus_1": two_j_plus_1,
        "n_particles": n_particles,
        "v_seniority": v_seniority,
        "half_filled_occupancy": int(n_half),
        "is_half_filled": is_half_filled,
        "fractional_parentage_factor": round(fractional_factor, 4),
        "b_e2_scaling_factor": round(b_e2_scaling_factor, 6),
        "is_seniority_cancellation": is_half_filled
    }


def calculate_seniority_v2_multiplet_spins(
    j_orbital: float
) -> List[int]:
    """Returns the allowed even spins J = 2, 4, 6, ..., (2j - 1) for seniority v = 2."""
    max_J = int(round(2.0 * j_orbital - 1.0))
    return [J for J in range(2, max_J + 1, 2)]


def evaluate_seniority_isomer_properties(
    j_orbital: float,
    n_particles: int,
    E_gamma_keV: float = 100.0,
    B_E2_base_Wu: float = 5.0,
    A_mass: float = 130.0
) -> Dict[str, Any]:
    """
    Evaluates B(E2) transition strength, isomer half-life T_1/2, and hindrance factor.
    """
    frac_res = calculate_seniority_fractional_factor(j_orbital, n_particles, v_seniority=2)
    b_scale = frac_res["b_e2_scaling_factor"]

    # Weisskopf single-particle unit: B_sp(E2) = 0.0594 * A^(4/3) e^2 fm^4 = 0.0594 * A^(4/3) * 1e-4 e^2 b^2
    B_sp_e2_fm4 = 0.05940 * (A_mass ** (4.0 / 3.0))
    B_sp_e2_b2 = B_sp_e2_fm4 * 1e-4

    B_E2_base_e2_b2 = B_E2_base_Wu * B_sp_e2_b2
    B_E2_actual_e2_b2 = B_E2_base_e2_b2 * b_scale
    B_E2_actual_Wu = B_E2_base_Wu * b_scale

    E_gamma_MeV = E_gamma_keV * 1e-3

    if B_E2_actual_e2_b2 > 1e-12:
        # lambda = 1.225e9 * E^5 * B(E2) s^-1
        decay_constant_s1 = 1.225e9 * (E_gamma_MeV ** 5) * B_E2_actual_e2_b2
        t12_sec = math.log(2.0) / decay_constant_s1
    else:
        # Exact cancellation at half-filled shell
        t12_sec = float("inf")

    # Base half-life for v=2, n=2
    decay_base_s1 = 1.225e9 * (E_gamma_MeV ** 5) * B_E2_base_e2_b2
    t12_base_sec = math.log(2.0) / decay_base_s1 if decay_base_s1 > 0 else float("inf")

    hindrance_factor = (t12_sec / t12_base_sec) if t12_base_sec > 0 else float("inf")

    # Time formatting
    if math.isinf(t12_sec):
        t12_str = "Infinity (Exact B(E2)=0 Cancellation)"
    elif t12_sec < 1e-6:
        t12_str = f"{t12_sec * 1e9:.2f} ns"
    elif t12_sec < 1e-3:
        t12_str = f"{t12_sec * 1e6:.2f} us"
    elif t12_sec < 1.0:
        t12_str = f"{t12_sec * 1e3:.2f} ms"
    else:
        t12_str = f"{t12_sec:.2f} s"

    spins_v2 = calculate_seniority_v2_multiplet_spins(j_orbital)
    max_isomer_spin = spins_v2[-1] if spins_v2 else None

    return {
        "fractional_factor": frac_res,
        "A_mass": A_mass,
        "E_gamma_keV": E_gamma_keV,
        "max_multiplet_spin_J": max_isomer_spin,
        "B_E2_base_Wu": B_E2_base_Wu,
        "B_E2_actual_Wu": round(B_E2_actual_Wu, 4),
        "B_E2_actual_e2_b2": round(B_E2_actual_e2_b2, 8),
        "T12_actual_sec": t12_sec,
        "T12_formatted": t12_str,
        "hindrance_factor": round(hindrance_factor, 2) if not math.isinf(hindrance_factor) else None,
        "isomer_status": "Seniority Isomer (B(E2) canceled)" if frac_res["is_half_filled"] else "Normal Seniority Decay"
    }


def format_text_report(iso_res: Dict[str, Any]) -> str:
    frac = iso_res["fractional_factor"]
    lines = [
        "=" * 76,
        "   NUCLEAR SENIORITY SCHEME & HALF-FILLED SHELL ISOMER SUITE",
        "   Based on Bohr & Mottelson Vol. I §3-4 & Jain Nuclear Isomers Ch. 3, 5 (2021)",
        "=" * 76,
        f" SHELL MODEL CONFIGURATION: j = {frac['j_orbital']} (Shell Capacity: {frac['shell_capacity_2j_plus_1']} particles)",
        f"   Occupancy n                 : {frac['n_particles']} particles (Half-Filled Shell: n = {frac['half_filled_occupancy']})",
        f"   Seniority Quantum Number v  : {frac['v_seniority']} (Unpaired nucleons)",
        f"   Seniority v=2 Multiplet     : J = {calculate_seniority_v2_multiplet_spins(frac['j_orbital'])}^+ (Isomer Spin: {iso_res['max_multiplet_spin_J']}^+)",
        "-" * 76,
        " FRACTIONAL PARENTAGE & B(E2) TRANSITION REDUCTION:",
        f"   Fractional Formula          : F = (2j + 1 - 2n) / (2j + 1 - 2v) = ({frac['shell_capacity_2j_plus_1']} - {2*frac['n_particles']}) / ({frac['shell_capacity_2j_plus_1']} - {2*frac['v_seniority']})",
        f"   Linear Parentage Factor F   : {frac['fractional_parentage_factor']:.4f}",
        f"   B(E2) Scaling Factor F^2    : {frac['b_e2_scaling_factor']:.6f}",
        f"   Exact Cancellation Status   : {frac['is_seniority_cancellation']} (F == 0 at half-filled shell)",
        "-" * 76,
        f" SENIORITY ISOMER LIFETIME & DE-EXCITATION (E_gamma = {iso_res['E_gamma_keV']:.1f} keV, A = {iso_res['A_mass']:.0f}):",
        f"   Base B(E2; v=2, n=2)        : {iso_res['B_E2_base_Wu']:.2f} W.u.",
        f"   Effective B(E2) Strength    : {iso_res['B_E2_actual_Wu']:.4f} W.u.  ({iso_res['B_E2_actual_e2_b2']:.2e} e^2 b^2)",
        f"   Isomer Half-Life T_1/2      : {iso_res['T12_formatted']}",
        f"   Seniority Hindrance Factor  : " + (f"{iso_res['hindrance_factor']:.2f}" if iso_res['hindrance_factor'] is not None else "Infinity"),
        f"   Isomer Classification       : {iso_res['isomer_status']}",
        "-" * 76,
        " Methodological & Shell-Model Guidelines:",
        "   - Seniority isomers occur in j >= 7/2 shells (g_9/2, h_11/2, i_13/2) at mid-shell n = j + 1/2.",
        "   - Classic benchmarks: 8+ in 210Po (h_9/2), 10+ in 130Sn (h_11/2), 8+ in 94Ru (g_9/2).",
        "   - In half-filled shells, core polarization or weak Delta_v=2 mixing breaks exact zero.",
        "=" * 76
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Nuclear Seniority Scheme & Half-Filled Shell Isomer Calculator"
    )
    parser.add_argument("--j-orbital", type=float, default=5.5, help="Single-j orbital (default: 5.5 for h11/2)")
    parser.add_argument("--n-particles", type=int, default=6, help="Particle occupancy n (default: 6 for half-filled h11/2)")
    parser.add_argument("--E-gamma", type=float, default=100.0, help="Gamma transition energy in keV (default: 100.0 keV)")
    parser.add_argument("--preset", type=str, default=None,
                        choices=["130Sn_h11/2", "134Te_h11/2", "210Po_h9/2", "94Ru_g9/2"],
                        help="Benchmark preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")

    args = parser.parse_args()

    j_val = args.j_orbital
    n_val = args.n_particles
    e_gam = args.E_gamma
    a_mass = 130.0

    if args.preset == "130Sn_h11/2":
        # 130Sn: 10 neutron holes in h11/2 (n = 10 out of 12)
        j_val, n_val, e_gam, a_mass = 5.5, 10, 65.0, 130.0
    elif args.preset == "134Te_h11/2":
        # 134Te: 2 valence protons in h11/2 (n = 2 out of 12)
        j_val, n_val, e_gam, a_mass = 5.5, 2, 297.0, 134.0
    elif args.preset == "210Po_h9/2":
        # 210Po: 2 valence protons in h9/2 (n = 2 out of 10)
        j_val, n_val, e_gam, a_mass = 4.5, 2, 84.0, 210.0
    elif args.preset == "94Ru_g9/2":
        # 94Ru: 4 proton holes in g9/2 (n = 4 out of 10)
        j_val, n_val, e_gam, a_mass = 4.5, 4, 145.0, 94.0

    res = evaluate_seniority_isomer_properties(j_val, n_val, E_gamma_keV=e_gam, A_mass=a_mass)

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res))


if __name__ == "__main__":
    main()
