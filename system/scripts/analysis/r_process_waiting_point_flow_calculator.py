#!/usr/bin/env python3
"""
r_process_waiting_point_flow_calculator.py
=========================================
Astrophysical r-Process (n, gamma) - (gamma, n) Equilibrium, Waiting Point
Abundance Distribution & Universal Peak Generator.

Physics & Formulation:
----------------------
1. Fast (n, gamma) <-> (gamma, n) Equilibrium (Saha Equation):
   In extreme astrophysical neutron star mergers (T_9 ~ 1.0 - 2.5, n_n ~ 10^20 - 10^26 cm^-3):
   Neutron capture and photodisintegration balance rapidly before beta-decay:
     Y(Z, A+1) / Y(Z, A) = n_n * (2*pi*hbar^2 / (m_u * k_B * T))^(3/2) *
                           [ G(Z, A+1) / (2 * G(Z, A)) ] * ((A+1)/A)^(3/2) *
                           exp( S_n(Z, A+1) / (k_B * T) )

2. Waiting Point Separation Energy S_n^0:
   Abundance along isotopic chain peaks where Y(A+1) / Y(A) ~ 1:
     S_n^0 ~ (T_9 / 11.605) * [ 78.29 + 3.45 * log10(T_9) - log10(n_n) ] MeV
   Typically S_n^0 ~ 2.0 - 3.5 MeV.

3. Magic Shell Bottlenecks & Universal Abundance Peaks:
   At closed neutron shells N = 50, 82, 126, S_n drops sharply below S_n^0:
     - Flow stalls at "waiting points" until slow beta-decay occurs (t_1/2 ~ 50 - 200 ms).
     - Generates the three prominent r-process solar abundance peaks:
         A ~ 80  (N = 50 shell)
         A ~ 130 (N = 82 shell, e.g. 130Cd)
         A ~ 195 (N = 126 shell, platinum/gold peak).

References:
  - E. M. Burbidge, G. R. Burbidge, W. A. Fowler, and F. Hoyle, Rev. Mod. Phys. 29, 547 (1957) [B^2FH].
  - C. Freiburghaus et al., Astrophys. J. 525, L121 (1999).
  - C. A. Bertulani, Nuclear Physics in a Nutshell, Princeton (2007).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_waiting_point_separation_energy(
    temperature_T9: float = 1.5,
    neutron_density_cm3: float = 1.0e24
) -> float:
    """
    Computes characteristic waiting point neutron separation energy S_n^0 (MeV).
    """
    T9 = max(temperature_T9, 0.1)
    log_nn = math.log10(max(neutron_density_cm3, 1e15))
    log_t9 = math.log10(T9)

    # S_n^0 = k_B * T * ln(10) * [ 34.005 + 1.5 * log10(T9) - log10(nn) ]
    bracket = 34.005 + 1.5 * log_t9 - log_nn
    s_n_0 = (T9 / 11.6045) * math.log(10.0) * bracket
    return max(round(s_n_0, 3), 0.5)


def calculate_isotopic_saha_equilibrium(
    Z_element: int,
    A_list: List[int],
    S_n_list: List[float],
    temperature_T9: float = 1.5,
    neutron_density_cm3: float = 1.0e24
) -> Dict[str, Any]:
    """
    Computes normalized relative abundances Y(A) along an isotopic chain under (n, gamma)-(gamma, n) balance.
    """
    if len(A_list) != len(S_n_list):
        raise ValueError("A_list and S_n_list length mismatch")

    T9 = max(temperature_T9, 0.1)
    k_B_T_MeV = T9 / 11.6045  # MeV

    # Pre-exponential factor C(T) = (2*pi*hbar^2 / (m_u * k_B * T))^(3/2)
    # C(T9) ~ 9.87e-35 * T9^(-3/2) cm^3
    c_factor = 9.87e-35 * (T9 ** (-1.5))
    log10_factor = math.log10(c_factor * neutron_density_cm3)

    # Relative abundances starting at A_list[0] = 1.0
    rel_abundances = [1.0]
    log_y = 0.0

    for i in range(len(A_list) - 1):
        sn = S_n_list[i + 1]
        # Y(A+1) / Y(A) = n_n * C(T) * exp(S_n / kT)
        # log10(ratio) = log10(n_n * C(T)) + (S_n / kT) / ln(10)
        log10_ratio = log10_factor + (sn / k_B_T_MeV) / math.log(10.0)
        # Cap ratio to avoid overflow
        log10_ratio = max(min(log10_ratio, 20.0), -20.0)
        log_y += log10_ratio
        rel_abundances.append(10.0 ** log_y)

    # Normalize to 100%
    total_y = sum(rel_abundances)
    norm_y = [round((y / total_y) * 100.0, 3) for y in rel_abundances]

    # Identify waiting point (peak of isotopic abundance)
    max_idx = norm_y.index(max(norm_y))
    a_wait = A_list[max_idx]
    sn_wait = S_n_list[max_idx]

    s_n_0_theo = calculate_waiting_point_separation_energy(temperature_T9, neutron_density_cm3)

    data_points = []
    for a, sn, y in zip(A_list, S_n_list, norm_y):
        data_points.append({"A": a, "S_n_MeV": sn, "abundance_percent": y})

    return {
        "element_Z": Z_element,
        "temperature_T9": temperature_T9,
        "neutron_density_cm3": f"{neutron_density_cm3:.2e}",
        "equilibrium_S_n_0_target_MeV": s_n_0_theo,
        "waiting_point_isotope_A": a_wait,
        "waiting_point_S_n_MeV": sn_wait,
        "waiting_point_abundance_percent": norm_y[max_idx],
        "isotopic_abundance_chain": data_points
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   ASTROPHYSICAL r-PROCESS (n,gamma)-(gamma,n) EQUILIBRIUM ANALYZER")
    lines.append("=" * 72)
    lines.append(f" ENVIRONMENT: Temperature T_9 = {summary['temperature_T9']} (k_B*T = {summary['temperature_T9']/11.605*1e3:.1f} keV), n_n = {summary['neutron_density_cm3']} cm^-3")
    lines.append(f"   Theoretical Waiting Point S_n^0 : {summary['equilibrium_S_n_0_target_MeV']} MeV")
    lines.append(f"   Identified Waiting Point Isotope: Z = {summary['element_Z']}, A = {summary['waiting_point_isotope_A']} (S_n = {summary['waiting_point_S_n_MeV']} MeV)")
    lines.append(f"   Peak Isotopic Abundance Fraction: {summary['waiting_point_abundance_percent']}%")
    lines.append("-" * 72)
    lines.append(" ISOTOPIC CHAIN EQUILIBRIUM ABUNDANCE PROFILE:")
    lines.append(f"   {'Mass A':<10} {'S_n (MeV)':<16} {'Abundance Y(A) %':<20} {'Status':<18}")
    lines.append("   " + "-" * 62)
    for row in summary["isotopic_abundance_chain"]:
        is_wp = "[WAITING POINT]" if row["A"] == summary["waiting_point_isotope_A"] else ""
        lines.append(f"   {row['A']:<10} {row['S_n_MeV']:<16.2f} {row['abundance_percent']:<20.3f} {is_wp:<18}")
    lines.append("-" * 72)
    lines.append(" Physical Significance:")
    lines.append("   - (n, gamma) and (gamma, n) balance traps abundance at S_n ~ S_n^0.")
    lines.append("   - Magic shells (N=50, 82, 126) create S_n cliffs that stall the flow.")
    lines.append("   - Stagnation waiting points generate the three solar r-process abundance peaks (A~80, 130, 195).")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Astrophysical r-Process Waiting Point Abundance Calculator."
    )
    parser.add_argument("-Z", type=int, default=48, help="Element proton number Z (default: 48 for Cd isotopes)")
    parser.add_argument("--T9", type=float, default=1.5, help="Temperature in 10^9 K (default: 1.5)")
    parser.add_argument("--nn", type=float, default=1.0e24, help="Neutron density in cm^-3 (default: 1e24)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    # Cadmium isotopic chain near N = 82 (A ~ 126 to 134)
    # S_n drops from ~4.5 MeV down to ~1.8 MeV across N = 82 shell gap at 130Cd
    A_vals = [126, 127, 128, 129, 130, 131, 132, 133]
    Sn_vals = [4.8, 3.8, 4.2, 3.2, 3.0, 1.2, 1.5, 0.9]  # classic drop at 131Cd (N=83)

    summary = calculate_isotopic_saha_equilibrium(args.Z, A_vals, Sn_vals, args.T9, args.nn)

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
