#!/usr/bin/env python3
"""
nolen_schiffer_isospin_anomaly_calculator.py
============================================
Nolen-Schiffer Isospin Anomaly (NSA), Coulomb Displacement Discrepancy &
Charge-Symmetry-Breaking (CSB) Nuclear Force Analyzer.

Physics & Formulation:
----------------------
1. The Nolen-Schiffer Anomaly (Nolen & Schiffer 1969):
   When calculating Coulomb displacement energy Delta_E_C in mirror nuclei
   (e.g. 41Sc - 41Ca, 17F - 17O, 209Bi - 208Pb_IAS) with wave functions constrained
   by electron scattering charge radii:
     Delta_E_C^theory systematically underestimates Delta_E_C^exp by ~ 5 - 8% (300 - 800 keV)!

2. Detailed Coulomb Energy Decomposition:
   Delta_E_C^theory = Delta_E_direct + Delta_E_exchange + Delta_E_so + Delta_E_finite_size
   - Direct Hartree Coulomb term:
       Delta_E_dir ~ (6/5) * (e^2 / R_0) * (Z_core / A^(1/3))
   - Fock exchange term (Pauli correlation):
       Delta_E_ex ~ - 0.96 * (e^2 / R_0) * (Z_core^(1/3) / A^(1/3))
   - Electromagnetic spin-orbit term:
       Delta_E_so ~ - 0.05 - 0.15 MeV (depending on j = l +/- 1/2).

3. Residual Nolen-Schiffer Anomaly & Charge-Symmetry-Breaking (CSB):
   Delta_E_NSA = Delta_E_C^exp - Delta_E_C^theory ~ 300 - 800 keV
   Resolved by:
     - u-d quark mass difference (m_d - m_u ~ 3 MeV).
     - rho0 - omega meson mixing in one-boson-exchange nuclear force:
         <rho0 | H | omega> ~ - 4500 keV^2 -> V_CSB ~ 300 - 500 keV.

References:
  - J. A. Nolen and J. P. Schiffer, Ann. Rev. Nucl. Sci. 19, 361 (1969).
  - S. Shlomo, Rep. Prog. Phys. 41, 957 (1978).
  - G. A. Miller, B. M. K. Nefkens, and I. Slaus, Phys. Rep. 194, 1 (1990) [CSB review].
  - 卢希庭, 《原子核物理（修订版）》, 第3章.
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple

E2_MEV_FM = 1.439965

BENCHMARK_MIRRORS = {
    "41Sc_41Ca": {"Z_parent": 20, "A": 41, "Delta_E_C_exp_MeV": 7.278, "r_ch_fm": 3.48},
    "17F_17O":   {"Z_parent": 8,  "A": 17, "Delta_E_C_exp_MeV": 3.543, "r_ch_fm": 2.70},
    "39Ca_39K":  {"Z_parent": 19, "A": 39, "Delta_E_C_exp_MeV": 7.305, "r_ch_fm": 3.44},
    "209Bi_IAS": {"Z_parent": 82, "A": 209,"Delta_E_C_exp_MeV": 18.826,"r_ch_fm": 5.50}
}


def calculate_theoretical_coulomb_displacement(
    Z_core: int,
    A_mass: int,
    r_charge_fm: Optional[float] = None,
    j_spin: float = 3.5,
    l_orbital: int = 3
) -> Dict[str, float]:
    """
    Computes direct, exchange, and electromagnetic spin-orbit components
    of Coulomb displacement energy.
    """
    # Equivalent uniform sphere radius R_0 = sqrt(5/3) * r_ch
    if r_charge_fm is not None:
        R_0 = math.sqrt(5.0 / 3.0) * r_charge_fm
    else:
        R_0 = 1.20 * (A_mass ** (1.0 / 3.0))

    Z_bar = Z_core + 0.5
    A13 = A_mass ** (1.0 / 3.0)

    # 1. Direct Hartree term
    # E_dir = (6/5) * (e^2 / R_0) * Z_bar
    delta_E_dir = (1.2 * E2_MEV_FM * Z_bar) / max(R_0, 1.0)

    # 2. Fock exchange term
    # E_ex ~ - (3/4pi) * (3*pi^2)^(1/3) * (e^2/R0) * Z_bar^(1/3) ~ -0.96 * e^2/R0 * Z^(1/3)
    delta_E_ex = - 0.96 * (E2_MEV_FM / max(R_0, 1.0)) * (Z_bar ** (1.0 / 3.0))

    # 3. Electromagnetic spin-orbit term (Thomas precession)
    # Proportional to <l . s> = 0.5 * [j(j+1) - l(l+1) - 3/4]
    ls_val = 0.5 * (j_spin * (j_spin + 1.0) - l_orbital * (l_orbital + 1.0) - 0.75)
    # Typically ~ -0.05 to -0.15 MeV
    delta_E_so = - 0.08 * (ls_val / max(j_spin, 0.5)) * (Z_bar / 20.0) / (A13 ** 2)

    # Total theoretical Coulomb displacement
    delta_E_theory = delta_E_dir + delta_E_ex + delta_E_so

    return {
        "equivalent_radius_R0_fm": round(R_0, 3),
        "direct_coulomb_MeV": round(delta_E_dir, 3),
        "exchange_coulomb_MeV": round(delta_E_ex, 3),
        "electromagnetic_spin_orbit_MeV": round(delta_E_so, 4),
        "total_theoretical_coulomb_MeV": round(delta_E_theory, 3)
    }


def evaluate_nolen_schiffer_anomaly(
    Z_core: int,
    A_mass: int,
    Delta_E_C_exp_MeV: float,
    r_charge_fm: Optional[float] = None
) -> Dict[str, Any]:
    """
    Computes the residual Nolen-Schiffer anomaly and extracts required
    Charge-Symmetry-Breaking (CSB) potential strength.
    """
    th = calculate_theoretical_coulomb_displacement(Z_core, A_mass, r_charge_fm)
    e_theory = th["total_theoretical_coulomb_MeV"]

    # Residual anomaly: Delta_E_NSA = Delta_E_exp - Delta_E_theory
    delta_nsa_MeV = Delta_E_C_exp_MeV - e_theory
    delta_nsa_keV = delta_nsa_MeV * 1e3

    discrepancy_percent = (delta_nsa_MeV / Delta_E_C_exp_MeV) * 100.0

    # Inferred rho-omega mixing matrix element required to resolve anomaly
    # V_CSB ~ delta_E_NSA
    v_csb_required_keV = delta_nsa_keV

    return {
        "nucleus_system": f"Z_core={Z_core}, A={A_mass}",
        "experimental_Delta_E_C_MeV": Delta_E_C_exp_MeV,
        "theoretical_coulomb_breakdown": th,
        "nolen_schiffer_anomaly_MeV": round(delta_nsa_MeV, 3),
        "nolen_schiffer_anomaly_keV": round(delta_nsa_keV, 1),
        "underestimation_percentage": round(discrepancy_percent, 2),
        "required_CSB_potential_keV": round(v_csb_required_keV, 1),
        "csb_mechanism_verdict": f"Charge-Symmetry-Breaking (CSB) force needed (+{v_csb_required_keV:.1f} keV) to resolve {discrepancy_percent:.1f}% underestimation"
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   NOLEN-SCHIFFER ISOSPIN ANOMALY & CSB NUCLEAR FORCE ANALYZER")
    lines.append("=" * 72)
    lines.append(f" MIRROR SYSTEM: {summary['nucleus_system']}")
    lines.append(f"   Experimental Displacement Delta_E_C : {summary['experimental_Delta_E_C_MeV']} MeV")
    lines.append("-" * 72)

    th = summary["theoretical_coulomb_breakdown"]
    lines.append(" THEORETICAL COULOMB MULTIPOLE DECOMPOSITION:")
    lines.append(f"   Equivalent Radius R_0          : {th['equivalent_radius_R0_fm']} fm")
    lines.append(f"   Direct Hartree Coulomb         : {th['direct_coulomb_MeV']} MeV")
    lines.append(f"   Fock Exchange Correlation      : {th['exchange_coulomb_MeV']} MeV")
    lines.append(f"   Electromagnetic Spin-Orbit     : {th['electromagnetic_spin_orbit_MeV']} MeV")
    lines.append(f"   Net Theoretical Coulomb Energy : {th['total_theoretical_coulomb_MeV']} MeV")
    lines.append("-" * 72)
    lines.append(" NOLEN-SCHIFFER ANOMALY & CSB INFERENCE:")
    lines.append(f"   Residual Anomaly Delta_E_NSA   : +{summary['nolen_schiffer_anomaly_keV']} keV ({summary['nolen_schiffer_anomaly_MeV']} MeV)")
    lines.append(f"   Theoretical Underestimation    : {summary['underestimation_percentage']}%")
    lines.append(f"   Inferred CSB Potential Need    : {summary['required_CSB_potential_keV']} keV")
    lines.append(f"   Diagnosis                      : {summary['csb_mechanism_verdict']}")
    lines.append("-" * 72)
    lines.append(" Physical Significance:")
    lines.append("   - Classical Coulomb force systematically fails to explain mirror displacement.")
    lines.append("   - Requires fundamental Charge-Symmetry-Breaking (CSB) forces (rho0-omega mixing).")
    lines.append("   - Proves that nuclear forces are not 100% charge-symmetric at the 1% scale.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Nolen-Schiffer Isospin Anomaly & CSB Calculator."
    )
    parser.add_argument("-Z", "--zcore", type=int, default=20, help="Core proton number Z (default: 20 for 41Sc-41Ca)")
    parser.add_argument("-A", "--mass", type=int, default=41, help="Mass number A (default: 41)")
    parser.add_argument("--exp-ec", type=float, default=7.278, help="Experimental Delta_E_C in MeV (default: 7.278)")
    parser.add_argument("--r-ch", type=float, default=3.48, help="Charge radius in fm (default: 3.48)")
    parser.add_argument("--preset", type=str, choices=list(BENCHMARK_MIRRORS.keys()), help="Select benchmark mirror system")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    z, a, ec, rch = args.zcore, args.mass, args.exp_ec, args.r_ch
    if args.preset:
        bm = BENCHMARK_MIRRORS[args.preset]
        z, a, ec, rch = bm["Z_parent"], bm["A"], bm["Delta_E_C_exp_MeV"], bm["r_ch_fm"]

    summary = evaluate_nolen_schiffer_anomaly(z, a, ec, rch)

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
