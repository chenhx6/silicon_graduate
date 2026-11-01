#!/usr/bin/env python3
"""
core_polarization_effective_charge_calculator.py
================================================
Microscopic Core Polarizability, Giant Quadrupole Resonance (GQR) Coupling &
Effective Nucleon Charges (e_p_eff, e_n_eff) Calculator.

Physics & Formulation:
----------------------
1. Bare vs Effective Charges:
   Bare charges: e_p_bare = 1.0 e, e_n_bare = 0.0 e.
   Valence nucleons polarize the inert core, virtually exciting Giant Quadrupole Resonances:
     e_p_eff = 1.0 + delta_e_p
     e_n_eff = 0.0 + delta_e_n

2. Particle-Vibration Coupling to GQRs (Bohr-Mottelson Vol. II):
   - Isoscalar Giant Quadrupole Resonance (ISGQR, T=0, protons and neutrons in phase):
     E_ISGQR = 64.0 * A^(-1/3) MeV
     Contributes isoscalar polarization charge delta_e^(0) ~ (Z / A) * chi_0 ~ +0.45 - 0.55 e
     (identical for protons and neutrons).
   - Isovector Giant Quadrupole Resonance (IVGQR, T=1, protons and neutrons out of phase):
     E_IVGQR = 130.0 * A^(-1/3) MeV
     Contributes isovector polarization charge delta_e^(1) ~ (1 - Z/A) * chi_1
     (+ for protons, - for neutrons).

   Net Theoretical Effective Charges:
     e_p_eff = 1.0 + delta_e^(0) - delta_e^(1) ~ 1.35 - 1.55 e
     e_n_eff = 0.0 + delta_e^(0) + delta_e^(1) ~ 0.45 - 0.65 e

3. Experimental Inversion from Single-Particle B(E2):
   B(E2; j_i -> j_f) = (e_eff)^2 * [(2*j_f + 1) / (4*pi)] * (j_f 2 j_i; 0.5 0 -0.5)^2 * <r^2>^2
   where <r^2> ~ (3/5) * R_0^2 = 0.6 * (1.2 * A^(1/3))^2 fm^2.
   Inverts e_eff from measured B(E2) or lifetime.

References:
  - A. Bohr and B. R. Mottelson, Nuclear Structure, Vol. II, Benjamin (1975).
  - K. L. G. Heyde, Basic Ideas and Concepts in Nuclear Physics, IoP (2004).
  - 卢希庭, 《原子核物理（修订版）》, 第4章.
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_microscopic_polarization_charges(
    Z_core: int,
    A_core: int,
    chi_0_isoscalar: float = 0.92,
    chi_1_isovector: float = 0.35
) -> Dict[str, Any]:
    """
    Computes theoretical core polarization charges delta_e_p and delta_e_n
    via coupling to ISGQR and IVGQR.
    """
    N_core = A_core - Z_core
    A13 = A_core ** (1.0 / 3.0)

    # GQR energies
    E_isgqr = 64.0 / max(A13, 1.0)
    E_ivgqr = 130.0 / max(A13, 1.0)

    # Isoscalar polarization charge: delta_e^(0) = (Z / A) * chi_0
    delta_e_0 = (float(Z_core) / float(A_core)) * chi_0_isoscalar

    # Isovector polarization charge: delta_e^(1) = ((N - Z) / A) * chi_1
    delta_e_1 = (float(N_core - Z_core) / float(A_core)) * chi_1_isovector

    # Total effective charges
    e_p_eff = 1.0 + delta_e_0 - delta_e_1
    e_n_eff = 0.0 + delta_e_0 + delta_e_1

    return {
        "core_nucleus": f"Z={Z_core}, A={A_core}",
        "E_ISGQR_MeV": round(E_isgqr, 2),
        "E_IVGQR_MeV": round(E_ivgqr, 2),
        "isoscalar_polarization_delta_e0": round(delta_e_0, 4),
        "isovector_polarization_delta_e1": round(delta_e_1, 4),
        "theoretical_proton_effective_charge_e": round(e_p_eff, 4),
        "theoretical_neutron_effective_charge_e": round(e_n_eff, 4),
        "polarization_charge_proton": round(e_p_eff - 1.0, 4),
        "polarization_charge_neutron": round(e_n_eff, 4)
    }


def invert_effective_charge_from_be2(
    B_E2_e2_fm4: float,
    j_initial: float,
    j_final: float,
    A_mass: int,
    is_neutron: bool = False
) -> Dict[str, Any]:
    """
    Inverts empirical effective charge e_eff from measured single-particle B(E2).
    """
    # Single particle radial matrix element <r^2> ~ (3/5) * R0^2
    R0 = 1.2 * (A_mass ** (1.0 / 3.0))
    r2_avg = 0.6 * (R0 ** 2)

    # Simple Clebsch-Gordan approximation for stretched/diagonal transition:
    # C^2 ~ 1 / (2*j_f + 1)
    # Reduced geometric factor G_geom = [(2*j_f + 1) / (4*pi)] * C^2 ~ 1 / (4*pi)
    geom_factor = 1.0 / (4.0 * math.pi)

    # B(E2) = (e_eff)^2 * geom_factor * (<r^2>)^2
    denom = geom_factor * (r2_avg ** 2)
    e_eff_sq = B_E2_e2_fm4 / max(denom, 1e-6)
    e_eff = math.sqrt(max(e_eff_sq, 0.0))

    bare_charge = 0.0 if is_neutron else 1.0
    delta_e_exp = e_eff - bare_charge

    return {
        "A_mass": A_mass,
        "valence_specie": "Neutron" if is_neutron else "Proton",
        "measured_B_E2_e2_fm4": B_E2_e2_fm4,
        "mean_square_radius_r2_fm2": round(r2_avg, 2),
        "extracted_effective_charge_e": round(e_eff, 3),
        "empirical_polarization_charge_delta_e": round(delta_e_exp, 3)
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   MICROSCOPIC CORE POLARIZATION & EFFECTIVE CHARGE ANALYZER")
    lines.append("=" * 72)

    th = summary["theory"]
    lines.append(f" INERT CORE COUPLING: {th['core_nucleus']}")
    lines.append(f"   Isoscalar GQR Energy (T=0)     : {th['E_ISGQR_MeV']} MeV")
    lines.append(f"   Isovector GQR Energy (T=1)     : {th['E_IVGQR_MeV']} MeV")
    lines.append(f"   Isoscalar Polarization delta_e : {th['isoscalar_polarization_delta_e0']} e")
    lines.append(f"   Isovector Polarization delta_e : {th['isovector_polarization_delta_e1']} e")
    lines.append("-" * 72)
    lines.append(" THEORETICAL PREDICTED EFFECTIVE CHARGES:")
    lines.append(f"   Proton  e_p_eff                : {th['theoretical_proton_effective_charge_e']} e (Bare = 1.0 e, delta_e = {th['polarization_charge_proton']} e)")
    lines.append(f"   Neutron e_n_eff                : {th['theoretical_neutron_effective_charge_e']} e (Bare = 0.0 e, delta_e = {th['polarization_charge_neutron']} e)")
    lines.append("-" * 72)

    if "experiment" in summary:
        exp = summary["experiment"]
        lines.append(" EMPIRICAL INVERSION FROM MEASURED B(E2):")
        lines.append(f"   Valence Specie                 : {exp['valence_specie']}")
        lines.append(f"   Measured B(E2)                 : {exp['measured_B_E2_e2_fm4']} e^2 fm^4")
        lines.append(f"   Extracted Effective Charge     : {exp['extracted_effective_charge_e']} e")
        lines.append(f"   Extracted Core Polarization    : {exp['empirical_polarization_charge_delta_e']} e")
        lines.append("-" * 72)

    lines.append(" Physical Significance:")
    lines.append("   - Unpaired valence nucleons virtually excite giant quadrupole resonances.")
    lines.append("   - Explains why neutrons carry substantial electric quadrupole strength (~0.5 e).")
    lines.append("   - Cornerstone calibration parameter for shell-model B(E2) calculations.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Core Polarization & Effective Charge Calculator."
    )
    parser.add_argument("-Z", type=int, default=82, help="Core proton number Z (default: 82 for 208Pb)")
    parser.add_argument("-A", type=int, default=208, help="Core mass number A (default: 208 for 208Pb)")
    parser.add_argument("--be2", type=float, default=None, help="Measured B(E2) in e^2 fm^4 for inversion")
    parser.add_argument("--neutron", action="store_true", help="Invert for valence neutron instead of proton")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    th_res = calculate_microscopic_polarization_charges(args.Z, args.A)
    summary = {"theory": th_res}

    if args.be2 is not None:
        exp_res = invert_effective_charge_from_be2(args.be2, 5.5, 4.5, args.A + 1, args.neutron)
        summary["experiment"] = exp_res
    elif args.Z == 82 and args.A == 208:
        # Benchmark 209Pb valence neutron 2g9/2 -> 3d5/2 B(E2) ~ 45 e^2 fm^4
        exp_res = invert_effective_charge_from_be2(45.0, 4.5, 2.5, 209, is_neutron=True)
        summary["experiment"] = exp_res

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
