#!/usr/bin/env python3
"""
gallagher_moszkowski_coupling_calculator.py
===========================================
Gallagher-Moszkowski (GM) Coupling Rules, Residual p-n Interaction Splitting &
Newby Odd-Even Shift Analyzer for Deformed Odd-Odd Nuclei.

Physics & Formulation:
----------------------
1. Nilsson Orbitals for Deformed Odd-Odd Nuclei:
   Proton orbital:  Omega_p [N_p, n_z_p, Lambda_p], Sigma_p = +/- 1/2 (Omega_p = Lambda_p + Sigma_p)
   Neutron orbital: Omega_n [N_n, n_z_n, Lambda_n], Sigma_n = +/- 1/2 (Omega_n = Lambda_n + Sigma_n)

   Two intrinsic spin projections along symmetry axis:
     K_+ = Omega_p + Omega_n
     K_- = |Omega_p - Omega_n|

2. Gallagher-Moszkowski (GM) Rule:
   The residual attractive spin-spin interaction (-V_sigma * sigma_p . sigma_n) favors
   configurations where intrinsic nucleon spins are PARALLEL (Sigma_p * Sigma_n > 0):
   - If Sigma_p and Sigma_n have the SAME sign (both +1/2 or both -1/2):
       Parallel spin state corresponds to K_GM = K_+ = Omega_p + Omega_n.
   - If Sigma_p and Sigma_n have OPPOSITE signs:
       Parallel spin state corresponds to K_GM = K_- = |Omega_p - Omega_n|.
   The GM-favored K state forms the ground state bandhead!

3. GM Doublet Energy Splitting Delta_E_GM:
   Delta_E_GM = E(K_unfavored) - E(K_favored) ~ 100 - 350 keV
   Empirical delta-force approximation:
     Delta_E_GM ~ (V_0 / A) * (2*j_p + 1)*(2*j_n + 1) * Overlap_Factor

4. Newby Odd-Even Shift (E_N) for K = 0 Bands (when Omega_p == Omega_n):
   For K = 0 bands, rotational energies split into even and odd spin sequences:
     E(I, K=0) = A_rot * [ I*(I + 1) + a_N * (-1)^(I + 1) ]
   where a_N is the Newby decoupling parameter.

References:
  - C. J. Gallagher and S. A. Moszkowski, Phys. Rev. 111, 1282 (1958).
  - N. D. Newby, Phys. Rev. 125, 2063 (1962).
  - A. Bohr and B. R. Mottelson, Nuclear Structure, Vol. II, Benjamin (1975).
  - 卢希庭, 《原子核物理（修订版）》.
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def evaluate_gallagher_moszkowski_rule(
    Omega_p: float,
    Lambda_p: int,
    Omega_n: float,
    Lambda_n: int,
    A_mass: int = 130,
    A_rot_keV: float = 20.0
) -> Dict[str, Any]:
    """
    Evaluates Gallagher-Moszkowski favored K state and doublet splitting.
    Sigma = Omega - Lambda = +/- 0.5.
    """
    Sigma_p = round(Omega_p - float(Lambda_p), 1)
    Sigma_n = round(Omega_n - float(Lambda_n), 1)

    K_plus = Omega_p + Omega_n
    K_minus = abs(Omega_p - Omega_n)

    # Check if intrinsic spins are aligned
    same_sign = (Sigma_p * Sigma_n > 0)

    if same_sign:
        K_favored = K_plus
        K_unfavored = K_minus
        rule_reason = f"Sigma_p ({Sigma_p:+.1f}) and Sigma_n ({Sigma_n:+.1f}) have same sign -> K_+ is parallel spin favored"
    else:
        K_favored = K_minus
        K_unfavored = K_plus
        rule_reason = f"Sigma_p ({Sigma_p:+.1f}) and Sigma_n ({Sigma_n:+.1f}) have opposite signs -> K_- is parallel spin favored"

    # Empirical doublet splitting Delta_E_GM
    # Typical splitting ~ 150 - 250 keV in deformed rare-earth and A~130 nuclei
    # Overlap factor modulated by 1/A and (Omega_p + Omega_n)
    overlap = math.sqrt(max(Omega_p * Omega_n, 0.25))
    delta_E_GM_keV = 2500.0 * overlap / float(A_mass)

    # Bandhead rotational energies
    E_bandhead_fav = A_rot_keV * K_favored
    E_bandhead_unfav = A_rot_keV * K_unfavored + delta_E_GM_keV

    return {
        "proton_orbital": f"Omega={Omega_p}, Lambda={Lambda_p}, Sigma={Sigma_p:+.1f}",
        "neutron_orbital": f"Omega={Omega_n}, Lambda={Lambda_n}, Sigma={Sigma_n:+.1f}",
        "K_plus": K_plus,
        "K_minus": K_minus,
        "GM_favored_K": K_favored,
        "GM_unfavored_K": K_unfavored,
        "rule_explanation": rule_reason,
        "predicted_GM_splitting_keV": round(delta_E_GM_keV, 1),
        "bandhead_favored_energy_keV": round(E_bandhead_fav, 1),
        "bandhead_unfavored_energy_keV": round(E_bandhead_unfav, 1),
        "is_K_zero_band": (K_minus == 0.0)
    }


def calculate_newby_shift_spectrum(
    A_rot_keV: float = 20.0,
    Newby_aN_keV: float = 35.0,
    max_spin: int = 8
) -> List[Dict[str, Any]]:
    """
    Computes energy levels of a K = 0 odd-odd band with Newby odd-even shift:
    E(I) = A_rot * I*(I + 1) + a_N * (-1)^(I + 1)
    """
    levels = []
    E_0 = -Newby_aN_keV if Newby_aN_keV != 0 else 0.0  # normalize relative to baseline

    for I in range(0, max_spin + 1):
        e_rot = A_rot_keV * I * (I + 1)
        shift = Newby_aN_keV * ((-1.0) ** (I + 1))
        e_tot = e_rot + shift
        levels.append({
            "I": I,
            "parity": "odd_I" if (I % 2 != 0) else "even_I",
            "rotational_energy_keV": round(e_rot, 1),
            "newby_shift_keV": round(shift, 1),
            "total_energy_keV": round(e_tot, 1)
        })

    return levels


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   GALLAGHER-MOSZKOWSKI (GM) COUPLING & NEWBY SHIFT ANALYZER")
    lines.append("=" * 72)

    gm = summary["gm_rule"]
    lines.append(f" VALENCE QUASIPARTICLE ORBITALS:")
    lines.append(f"   Proton  : {gm['proton_orbital']}")
    lines.append(f"   Neutron : {gm['neutron_orbital']}")
    lines.append(f"   K Values: K_+ = {gm['K_plus']}, K_- = {gm['K_minus']}")
    lines.append("-" * 72)
    lines.append(" GALLAGHER-MOSZKOWSKI GROUND STATE PREDICTION:")
    lines.append(f"   Favored Ground State Bandhead  : K = {gm['GM_favored_K']}")
    lines.append(f"   Unfavored Excited Bandhead     : K = {gm['GM_unfavored_K']}")
    lines.append(f"   Physical Mechanism             : {gm['rule_explanation']}")
    lines.append(f"   Predicted Doublet Splitting    : {gm['predicted_GM_splitting_keV']} keV")
    lines.append(f"   K=0 Band Emergence             : {gm['is_K_zero_band']}")
    lines.append("-" * 72)

    if "newby_spectrum" in summary:
        lines.append(" NEWBY SHIFT ENERGY LEVELS (K = 0 Band):")
        lines.append(f"   {'Spin I':<10} {'Parity/Sequence':<18} {'Rotational (keV)':<18} {'Total (keV)':<15}")
        lines.append("   " + "-" * 60)
        for lv in summary["newby_spectrum"]:
            lines.append(f"   {lv['I']:<10} {lv['parity']:<18} {lv['rotational_energy_keV']:<18.1f} {lv['total_energy_keV']:<15.1f}")
        lines.append("-" * 72)

    lines.append(" Physical Significance:")
    lines.append("   - Residual spin-spin force drives parallel intrinsic nucleon spins.")
    lines.append(
        "   - Provides a model-based ground-state-spin screening rule for "
        "odd-odd deformed nuclei; measured level schemes and configuration "
        "evidence remain necessary."
    )
    lines.append("   - K=0 bands exhibit pronounced Newby odd-even energy staggering.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Gallagher-Moszkowski Coupling & Newby Shift Analyzer."
    )
    parser.add_argument("--omega-p", type=float, default=2.5, help="Proton Omega_p (default: 2.5 for 5/2[413])")
    parser.add_argument("--lambda-p", type=int, default=2, help="Proton Lambda_p (default: 2)")
    parser.add_argument("--omega-n", type=float, default=2.5, help="Neutron Omega_n (default: 2.5 for 5/2[532])")
    parser.add_argument("--lambda-n", type=int, default=3, help="Neutron Lambda_n (default: 3)")
    parser.add_argument("--A", type=int, default=130, help="Mass number A (default: 130)")
    parser.add_argument("--A-rot", type=float, default=20.0, help="Rotational constant A_rot in keV (default: 20.0)")
    parser.add_argument("--newby-shift", type=float, default=30.0, help="Newby shift a_N in keV for K=0 (default: 30.0)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    gm_res = evaluate_gallagher_moszkowski_rule(
        args.omega_p, args.lambda_p, args.omega_n, args.lambda_n, args.A, args.A_rot
    )
    summary = {"gm_rule": gm_res}

    if gm_res["is_K_zero_band"]:
        levels = calculate_newby_shift_spectrum(args.A_rot, args.newby_shift)
        summary["newby_spectrum"] = levels

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
