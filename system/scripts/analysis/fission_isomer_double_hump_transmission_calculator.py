#!/usr/bin/env python3
"""
fission_isomer_double_hump_transmission_calculator.py
=====================================================
Double-Humped Fission Barrier Quantum Transmission, Fission Shape Isomer &
Subthreshold Intermediate Resonance Simulator.

Physics & Formulation:
----------------------
1. Double-Humped Fission Barrier Profile (Strutinsky 1967):
   Superposition of smooth liquid drop barrier and microscopic shell corrections:
   - Inner barrier A: Height V_A, curvature hbar*omega_A ~ 0.8 - 1.1 MeV.
   - Second minimum II (Superdeformed well, c/a ~ 2:1): Energy E_II ~ 2.0 - 3.0 MeV.
   - Outer barrier B: Height V_B, curvature hbar*omega_B ~ 0.5 - 0.7 MeV.

2. Quantum Penetration of Double Barrier (Cramer & Nix 1970):
   Individual Hill-Wheeler penetrabilities:
     T_A(E) = 1 / [ 1 + exp(2*pi * (V_A - E) / (hbar*omega_A)) ]
     T_B(E) = 1 / [ 1 + exp(2*pi * (V_B - E) / (hbar*omega_B)) ]
   Total transmission including intermediate phase phi(E):
     T(E) = (T_A * T_B) / [ 1 + 2*sqrt((1-T_A)*(1-T_B)) * cos(2*phi) + (1-T_A)*(1-T_B) ]
   Resonance condition: cos(2*phi) = -1 yields resonant transmission enhancement:
     T_res = 4 * T_A * T_B / (T_A + T_B)^2 -> 1.0 if T_A ~ T_B!

3. Fission Isomer (Class-II State) Lifetimes:
   The ground state in the second well decays via two competing channels:
   - Delayed spontaneous fission through outer barrier B: Gamma_fiss = (hbar*omega_II / (2*pi)) * T_B(E_II).
   - Back-decay via gamma emission through inner barrier A: Gamma_back = (hbar*omega_II / (2*pi)) * T_A(E_II) * P_gamma.
   Half-life:
     t_1/2 = ln(2) * hbar / (Gamma_fiss + Gamma_back)  (typically ns to ms).

4. Subthreshold Intermediate Resonance Clustering:
   Explains why sub-barrier neutron fission cross sections (e.g. 237Np(n,f), 240Pu(n,f))
   exhibit sharp clusters of resonances with spacing D_II ~ 1 - 2 keV, corresponding to
   the level density of Class-II states in the shallow second well.

References:
  - V. M. Strutinsky, Nucl. Phys. A 95, 420 (1967).
  - S. M. Polikanov et al., Sov. Phys. JETP 15, 1016 (1962) [Discovery of fission isomers].
  - S. Bjornholm and J. E. Lynn, Rev. Mod. Phys. 52, 725 (1980).
  - R. Vandenbosch and J. R. Huizenga, Nuclear Fission, Academic Press (1973).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple

HBAR_MEV_S = 6.582119569e-22


def calculate_hill_wheeler_barrier(E: float, V_barrier: float, hbar_omega: float) -> float:
    """Hill-Wheeler single-barrier penetrability."""
    arg = 2.0 * math.pi * (V_barrier - E) / max(hbar_omega, 0.05)
    if arg > 80.0:
        return math.exp(-arg)
    elif arg < -80.0:
        return 1.0
    return 1.0 / (1.0 + math.exp(arg))


def evaluate_double_barrier_transmission(
    energy_MeV: float,
    V_A: float = 6.0,
    hw_A: float = 0.9,
    E_II: float = 2.5,
    V_B: float = 5.5,
    hw_B: float = 0.6,
    phi_phase_rad: Optional[float] = None
) -> Dict[str, Any]:
    """
    Computes total quantum transmission probability T(E) through double-humped barrier.
    """
    T_A = calculate_hill_wheeler_barrier(energy_MeV, V_A, hw_A)
    T_B = calculate_hill_wheeler_barrier(energy_MeV, V_B, hw_B)

    # Second well action phase phi(E): phi ~ pi * (E - E_II) / hw_II
    hw_II = 0.8  # class-II vibrational phonon spacing
    if phi_phase_rad is None:
        phi = math.pi * max(energy_MeV - E_II, 0.0) / hw_II
    else:
        phi = phi_phase_rad

    cos2phi = math.cos(2.0 * phi)
    term1 = 1.0 - T_A
    term2 = 1.0 - T_B

    denom = 1.0 + 2.0 * math.sqrt(max(term1 * term2, 0.0)) * cos2phi + term1 * term2
    if denom <= 0:
        denom = 1e-12

    T_net = (T_A * T_B) / denom
    T_net = min(max(T_net, 1e-25), 1.0)

    # Resonant and non-resonant bounds
    T_res = 4.0 * T_A * T_B / ((T_A + T_B) ** 2) if (T_A + T_B) > 0 else 0.0
    T_valley = (T_A * T_B) / 4.0

    is_resonant = (cos2phi < -0.8)

    return {
        "energy_MeV": energy_MeV,
        "penetrability_T_A": round(T_A, 6),
        "penetrability_T_B": round(T_B, 6),
        "second_well_phase_rad": round(phi, 3),
        "total_transmission_T": round(T_net, 8),
        "peak_resonant_transmission": round(T_res, 6),
        "off_resonant_valley_transmission": round(T_valley, 8),
        "is_intermediate_resonance": is_resonant
    }


def calculate_fission_isomer_properties(
    V_A: float = 6.0,
    hw_A: float = 0.9,
    E_II: float = 2.5,
    V_B: float = 5.5,
    hw_B: float = 0.6,
    P_gamma_back: float = 0.005
) -> Dict[str, Any]:
    """
    Computes decay widths, half-life, and branching ratios for the fission shape isomer (Class-II GS).
    """
    hw_II = 0.8  # second well zero-point frequency in MeV
    f_attack = (hw_II / (2.0 * math.pi))  # attack frequency in MeV

    # Outer barrier penetration (fission)
    T_B_iso = calculate_hill_wheeler_barrier(E_II, V_B, hw_B)
    Gamma_fiss_MeV = f_attack * T_B_iso

    # Inner barrier penetration (back-decay to class-I)
    T_A_iso = calculate_hill_wheeler_barrier(E_II, V_A, hw_A)
    Gamma_back_MeV = f_attack * T_A_iso * P_gamma_back

    Gamma_tot_MeV = Gamma_fiss_MeV + Gamma_back_MeV

    if Gamma_tot_MeV > 0:
        half_life_sec = math.log(2.0) * HBAR_MEV_S / Gamma_tot_MeV
    else:
        half_life_sec = float("inf")

    branching_fission = Gamma_fiss_MeV / max(Gamma_tot_MeV, 1e-30)

    # Format half life
    if half_life_sec < 1e-6:
        hl_str = f"{half_life_sec * 1e9:.2f} ns"
    elif half_life_sec < 1e-3:
        hl_str = f"{half_life_sec * 1e6:.2f} us"
    elif half_life_sec < 1.0:
        hl_str = f"{half_life_sec * 1e3:.2f} ms"
    else:
        hl_str = f"{half_life_sec:.2f} s"

    return {
        "isomer_excitation_E_II_MeV": E_II,
        "inner_barrier_V_A_MeV": V_A,
        "outer_barrier_V_B_MeV": V_B,
        "fission_width_MeV": Gamma_fiss_MeV,
        "back_decay_gamma_width_MeV": Gamma_back_MeV,
        "total_decay_width_MeV": Gamma_tot_MeV,
        "isomer_half_life_seconds": half_life_sec,
        "formatted_half_life": hl_str,
        "fission_branching_ratio": round(branching_fission, 4)
    }


def scan_subthreshold_fission_cross_section(
    V_A: float = 6.0,
    hw_A: float = 0.9,
    E_II: float = 2.5,
    V_B: float = 5.5,
    hw_B: float = 0.6,
    E_start_MeV: float = 3.5,
    E_stop_MeV: float = 6.5,
    num_steps: int = 31
) -> List[Dict[str, Any]]:
    """
    Scans subthreshold fission transmission curve to show intermediate resonance clusters.
    """
    dE = (E_stop_MeV - E_start_MeV) / float(num_steps - 1)
    curve = []

    for i in range(num_steps):
        E = E_start_MeV + i * dE
        res = evaluate_double_barrier_transmission(E, V_A, hw_A, E_II, V_B, hw_B)
        curve.append({
            "energy_MeV": round(E, 3),
            "transmission_T": res["total_transmission_T"],
            "is_resonance": res["is_intermediate_resonance"]
        })
    return curve


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   DOUBLE-HUMPED FISSION BARRIER TRANSMISSION & ISOMER ANALYZER")
    lines.append("=" * 72)

    iso = summary["isomer"]
    lines.append(" FISSION SHAPE ISOMER (CLASS-II GROUND STATE):")
    lines.append(f"   Isomer Excitation Energy E_II  : {iso['isomer_excitation_E_II_MeV']} MeV (Superdeformed 2:1 well)")
    lines.append(f"   Inner Barrier V_A / Outer V_B  : V_A = {iso['inner_barrier_V_A_MeV']} MeV, V_B = {iso['outer_barrier_V_B_MeV']} MeV")
    lines.append(f"   Isomer Half-Life t_1/2         : {iso['formatted_half_life']} ({iso['isomer_half_life_seconds']:.2e} s)")
    lines.append(f"   Fission Branching Ratio        : {iso['fission_branching_ratio']*100:.2f}% (Delayed spontaneous fission)")
    lines.append("-" * 72)

    if "subthreshold_scan" in summary:
        lines.append(" SUBTHRESHOLD INTERMEDIATE RESONANCE TRANSMISSION (Sample):")
        lines.append(f"   {'Energy (MeV)':<16} {'Transmission T':<20} {'Resonance Status':<20}")
        lines.append("   " + "-" * 56)
        for pt in summary["subthreshold_scan"][:12]:
            lines.append(f"   {pt['energy_MeV']:<16.3f} {pt['transmission_T']:<20.4e} {'[RESONANCE PEAK]' if pt['is_resonance'] else 'Off-resonance'}")
        lines.append("-" * 72)

    lines.append(" Physical Significance:")
    lines.append("   - Superdeformed second well traps fission shape isomers (Polikanov 1962).")
    lines.append("   - Double-parabolic barrier interference creates subthreshold resonance clusters.")
    lines.append("   - Essential for actinide cross section evaluations in 235U, 237Np, and 242Am.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Double-Humped Fission Barrier Transmission & Isomer Analyzer."
    )
    parser.add_argument("--VA", type=float, default=6.0, help="Inner barrier height V_A in MeV (default: 6.0)")
    parser.add_argument("--hwA", type=float, default=0.9, help="Inner barrier curvature hbar*omega_A in MeV (default: 0.9)")
    parser.add_argument("--EII", type=float, default=2.5, help="Second minimum excitation E_II in MeV (default: 2.5)")
    parser.add_argument("--VB", type=float, default=5.5, help="Outer barrier height V_B in MeV (default: 5.5)")
    parser.add_argument("--hwB", type=float, default=0.6, help="Outer barrier curvature hbar*omega_B in MeV (default: 0.6)")
    parser.add_argument("--scan", action="store_true", help="Perform subthreshold energy transmission scan")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    iso_res = calculate_fission_isomer_properties(args.VA, args.hwA, args.EII, args.VB, args.hwB)
    summary = {"isomer": iso_res}

    if args.scan or args.VA == 6.0:
        scan_res = scan_subthreshold_fission_cross_section(args.VA, args.hwA, args.EII, args.VB, args.hwB)
        summary["subthreshold_scan"] = scan_res

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
