#!/usr/bin/env python3
"""
heavy_ion_elastic_rainbow_scattering_calculator.py
==================================================
Heavy-Ion Semiclassical Deflection Function, Nuclear Rainbow Scattering &
Grazing Quarter-Point Angle Analyzer.

Physics & Formulation:
----------------------
1. Semiclassical Deflection Function Theta(l):
   Balances repulsive Coulomb force with attractive nuclear Woods-Saxon surface potential:
     Theta(l) = 2 * arctan(eta / l) - Theta_nuclear(l)
   where:
     eta = Z_p * Z_t * e^2 / (hbar * v): Sommerfeld parameter.
     k = sqrt(2 * mu * E_cm) / hbar: Asymptotic wave number.

2. Grazing Angular Momentum & Blair Quarter-Point Angle:
   Nuclear interaction radius: R_int = 1.25 * (A_p^(1/3) + A_t^(1/3)) fm.
   Coulomb barrier at contact: V_C = 1.44 * Z_p * Z_t / R_int MeV.
   Grazing angular momentum:
     l_grazing = k * R_int * sqrt(max(1.0 - V_C / E_cm, 0.0))
   Blair quarter-point angle (where sigma_el / sigma_Ruth = 0.25):
     theta_14 = 2 * arcsin(eta / sqrt(eta^2 + l_grazing^2))

3. Nuclear Rainbow Angle (theta_rainbow):
   Occurs at the local minimum of the deflection function where d(Theta)/dl = 0:
     theta_rainbow = min_l [ Theta(l) ]
   - For angles theta < theta_rainbow: Classically forbidden dark side (exponential decay).
   - For angles near theta_rainbow: Quantum Airy oscillations and rainbow peak.

4. Experimental Detector Placement:
   Placing Delta_E - E particle telescopes at theta ~ theta_14 maximizes transfer
   and deep-inelastic reaction cross sections while suppressing forward beam halo.

References:
  - C. A. Bertulani and P. Danielewicz, Introduction to Nuclear Reactions, CRC Press (2004).
  - 林承键, 《重离子核反应》, 科学出版社.
  - D. A. Goldberg and S. M. Smith, Phys. Rev. Lett. 29, 500 (1972) [Nuclear Rainbow].
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple

HBAR_C_MEV_FM = 197.327
U_MEV = 931.494
E2_MEV_FM = 1.439965


def calculate_scattering_kinematics(
    Z_p: int,
    A_p: int,
    Z_t: int,
    A_t: int,
    E_lab_MeV: float,
    r0_fm: float = 1.25
) -> Dict[str, float]:
    """
    Computes CM energy, wave number k, Sommerfeld parameter eta,
    grazing angular momentum, and Blair quarter-point angle.
    """
    E_cm = E_lab_MeV * float(A_t) / float(A_p + A_t)
    mu_amu = (A_p * A_t) / float(A_p + A_t)
    mu_MeV = mu_amu * U_MEV

    # Asymptotic wave number k [fm^-1]
    k_fm = math.sqrt(2.0 * mu_MeV * E_cm) / HBAR_C_MEV_FM

    # Velocity beta
    beta = math.sqrt(max(2.0 * E_cm / mu_MeV, 1e-6))

    # Sommerfeld parameter eta = Z1*Z2*e^2 / (hbar * c * beta)
    eta = (Z_p * Z_t * E2_MEV_FM) / (HBAR_C_MEV_FM * beta)

    # Strong absorption radius R_int
    R_int = r0_fm * (A_p ** (1.0 / 3.0) + A_t ** (1.0 / 3.0))
    V_C_contact = E2_MEV_FM * Z_p * Z_t / R_int

    # Grazing angular momentum
    if E_cm > V_C_contact:
        l_graz = k_fm * R_int * math.sqrt(1.0 - V_C_contact / E_cm)
    else:
        l_graz = 0.0

    # Blair quarter-point angle theta_1/4
    denom_angle = math.sqrt(eta ** 2 + l_graz ** 2)
    sin_half_14 = eta / denom_angle if denom_angle > 0 else 1.0
    theta_14_rad = 2.0 * math.asin(min(sin_half_14, 1.0))
    theta_14_deg = math.degrees(theta_14_rad)

    return {
        "E_cm_MeV": round(E_cm, 2),
        "wave_number_k_fm": round(k_fm, 3),
        "Sommerfeld_eta": round(eta, 2),
        "interaction_radius_R_int_fm": round(R_int, 2),
        "coulomb_barrier_contact_MeV": round(V_C_contact, 2),
        "grazing_angular_momentum_hbar": round(l_graz, 1),
        "blair_quarter_point_angle_deg": round(theta_14_deg, 1)
    }


def evaluate_deflection_function(
    l_hbar: float,
    kin: Dict[str, float],
    V_nuc_strength_MeV: float = 60.0,
    diffuseness_fm: float = 0.65
) -> float:
    """
    Computes semiclassical deflection angle Theta(l) in degrees:
    Theta(l) = 2*arctan(eta/l) - nuclear_deflection(l).
    """
    eta = kin["Sommerfeld_eta"]
    l_val = max(l_hbar, 0.5)

    # Coulomb term
    theta_coul_rad = 2.0 * math.atan(eta / l_val)

    # Nuclear attraction term: peaks near grazing
    l_graz = kin["grazing_angular_momentum_hbar"]
    dl = (l_val - l_graz) / 4.0
    # Bell-shaped nuclear deflection gradient
    theta_nuc_rad = (V_nuc_strength_MeV / max(kin["E_cm_MeV"], 10.0)) * math.exp(-0.5 * (dl ** 2))

    theta_net_rad = theta_coul_rad - theta_nuc_rad
    return math.degrees(theta_net_rad)


def scan_nuclear_rainbow(
    kin: Dict[str, float],
    l_max: Optional[float] = None
) -> Dict[str, Any]:
    """
    Scans deflection function Theta(l) to find the nuclear rainbow minimum.
    """
    l_graz = kin["grazing_angular_momentum_hbar"]
    l_upper = l_max if l_max is not None else max(l_graz * 2.0, 30.0)

    steps = 100
    dl = l_upper / float(steps)

    min_theta = float("inf")
    l_rainbow = 0.0
    curve = []

    for i in range(1, steps + 1):
        l_curr = i * dl
        theta = evaluate_deflection_function(l_curr, kin)
        curve.append({"l_hbar": round(l_curr, 1), "deflection_angle_deg": round(theta, 2)})

        if theta < min_theta:
            min_theta = theta
            l_rainbow = l_curr

    return {
        "l_rainbow_hbar": round(l_rainbow, 1),
        "rainbow_angle_deg": round(min_theta, 1),
        "is_rainbow_active": (min_theta < kin["blair_quarter_point_angle_deg"]),
        "sample_points": curve[::10]
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   HEAVY-ION DEFLECTION FUNCTION & RAINBOW SCATTERING ANALYZER")
    lines.append("=" * 72)

    kin = summary["kinematics"]
    lines.append(f" SCATTERING SYSTEM: E_cm = {kin['E_cm_MeV']} MeV (Sommerfeld eta = {kin['Sommerfeld_eta']})")
    lines.append(f"   Contact Radius R_int           : {kin['interaction_radius_R_int_fm']} fm (Barrier V_C = {kin['coulomb_barrier_contact_MeV']} MeV)")
    lines.append(f"   Grazing Angular Momentum       : l_grazing = {kin['grazing_angular_momentum_hbar']} hbar")
    lines.append(f"   Blair Quarter-Point Angle      : theta_1/4 = {kin['blair_quarter_point_angle_deg']} deg")
    lines.append("-" * 72)

    rb = summary["rainbow"]
    lines.append(" NUCLEAR RAINBOW EXTREMUM:")
    lines.append(f"   Rainbow Angular Momentum l_r   : {rb['l_rainbow_hbar']} hbar")
    lines.append(f"   Nuclear Rainbow Angle theta_r  : {rb['rainbow_angle_deg']} deg")
    lines.append(f"   Rainbow Phenomenon Status      : {'Active (Airy oscillations present)' if rb['is_rainbow_active'] else 'Coulomb dominated'}")
    lines.append("-" * 72)
    lines.append(" DEFLECTION FUNCTION PROFILE Theta(l) (Sample Points):")
    lines.append(f"   {'Angular Momentum l':<22} {'Deflection Angle Theta (deg)':<25}")
    lines.append("   " + "-" * 50)
    for pt in rb["sample_points"]:
        lines.append(f"   {pt['l_hbar']:<22.1f} {pt['deflection_angle_deg']:<25.2f}")
    lines.append("-" * 72)
    lines.append(" Physical Significance:")
    lines.append("   - Blair quarter-point angle marks the onset of strong absorption.")
    lines.append("   - Nuclear rainbow angle defines the classically allowed boundary.")
    lines.append("   - Guides telescope detector placement to capture maximum transfer yield.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Heavy-Ion Deflection Function & Rainbow Scattering Analyzer."
    )
    parser.add_argument("-Zp", type=int, required=True, help="Projectile charge Z_p")
    parser.add_argument("-Ap", type=int, required=True, help="Projectile mass A_p")
    parser.add_argument("-Zt", type=int, required=True, help="Target charge Z_t")
    parser.add_argument("-At", type=int, required=True, help="Target mass A_t")
    parser.add_argument("-E", "--elab", type=float, required=True, help="Beam energy E_lab in MeV")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    kin = calculate_scattering_kinematics(args.Zp, args.Ap, args.Zt, args.At, args.elab)
    rb = scan_nuclear_rainbow(kin)

    summary = {
        "kinematics": kin,
        "rainbow": rb
    }

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
