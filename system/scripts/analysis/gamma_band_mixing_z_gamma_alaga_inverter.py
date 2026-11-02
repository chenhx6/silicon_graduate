#!/usr/bin/env python3
"""
gamma_band_mixing_z_gamma_alaga_inverter.py
===========================================
Collective Model Gamma-Vibrational Band Mixing, Mikhailov z_gamma Parameter &
Alaga Branching Rule Inverter.

Physics & Formulation:
----------------------
1. Alaga Branching Rules (Alaga et al. 1955):
   For E2 transitions from a state I_gamma in the gamma-vibrational band (K = 2) to states I_g1, I_g2
   in the ground-state rotational band (K = 0):
     B(E2; I_gamma -> I_g)_Alaga = B_0(E2) * <I_gamma, 2, K=2, -2 | I_g, 0>^2
   The unperturbed branching ratio of transition rates is:
     R_Alaga = [ B(E2; I_gamma -> I_g1) / B(E2; I_gamma -> I_g2) ] * (E_gamma1 / E_gamma2)^5

2. Mikhailov Band-Mixing Expansion (Mikhailov 1966, Bohr-Mottelson Vol. II §4-2):
   Coriolis coupling and Delta_K = 2 mixing between the gamma-vibrational band and the ground-state band
   introduce angular-momentum-dependent corrections to the E2 matrix elements:
     M(E2; I_gamma -> I_g) = M_0 * <I_gamma, 2, 2, -2 | I_g, 0> * [ 1.0 + z_gamma * ( I_g(I_g + 1) - I_gamma(I_gamma + 1) ) ]
   where z_gamma is the dimensionless Mikhailov band-mixing parameter.

   For the 2_gamma^+ bandhead de-exciting to the ground band:
     - To 0_g^+:  I_g(I_g+1) - I_gamma(I_gamma+1) = 0 - 6 = -6
         M(2_gamma -> 0_g) = M_0 * sqrt(1/5) * [ 1.0 - 6.0 * z_gamma ]
     - To 2_g^+:  I_g(I_g+1) - I_gamma(I_gamma+1) = 6 - 6 = 0
         M(2_gamma -> 2_g) = M_0 * sqrt(2/7) * [ 1.0 + 0.0 ]
     - To 4_g^+:  I_g(I_g+1) - I_gamma(I_gamma+1) = 20 - 6 = +14
         M(2_gamma -> 4_g) = M_0 * sqrt(1/70) * [ 1.0 + 14.0 * z_gamma ]

   The perturbed B(E2) ratio becomes:
     R_B(E2)(z_gamma) = [ B(E2; 2_gamma -> 0_g) / B(E2; 2_gamma -> 2_g) ] = (7 / 10) * [ 1.0 - 6.0 * z_gamma ]^2

3. Inversion of z_gamma and Rotational-Vibrational Coupling h_2:
   From measured experimental B(E2) ratio R_exp = B(E2; 2_gamma -> 0_g) / B(E2; 2_gamma -> 2_g):
     z_gamma = (1.0 - sqrt( R_exp / 0.700 )) / 6.0
   The microscopic rotational-vibrational coupling matrix element h_2 (in keV):
     h_2 = z_gamma * [ E(2_gamma^+) - E(2_g^+) ] / sqrt(6)

4. Structural Rigidity Classification:
   - z_gamma < 0.015 : Rigid axial rotor (negligible gamma-coupling).
   - 0.015 <= z_gamma <= 0.045 : Standard well-deformed rotor with moderate gamma-vibrations (e.g. 166Er, 168Er).
   - z_gamma > 0.060 : Strong mixing / gamma-softness / onset of triaxiality (e.g. A ~ 130 Ba/Xe isotopes).

References:
  - G. Alaga, K. Alder, A. Bohr, and B. R. Mottelson, Mat. Fys. Medd. Dan. Vid. Selsk. 29, no. 9 (1955).
  - V. M. Mikhailov, Izv. Akad. Nauk SSSR, Ser. Fiz. 30, 1334 (1966) [Bull. Acad. Sci. USSR, Phys. Ser. 30, 1392 (1966)].
  - A. Bohr and B. R. Mottelson, *Nuclear Structure*, Vol. II, §4-2 (pp. 140–155).
  - 卢希庭, 《原子核物理（修订版）》, 原子能出版社 (2000), 第8章 §8.4.
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_alaga_cg_coefficient(I_gamma: int, I_g: int) -> float:
    """
    Computes Clebsch-Gordan coefficient <I_gamma, 2, K=2, -2 | I_g, 0> for gamma-to-ground transitions.
    Analytical formulas from Bohr & Mottelson Vol. II:
    """
    if I_gamma == 2:
        if I_g == 0:
            return math.sqrt(1.0 / 5.0) # ~ 0.44721
        elif I_g == 2:
            return math.sqrt(2.0 / 7.0) # ~ 0.53452
        elif I_g == 4:
            return math.sqrt(1.0 / 70.0) # ~ 0.11952
        else:
            return 0.0
    elif I_gamma == 3:
        if I_g == 2:
            return math.sqrt(5.0 / 14.0) # ~ 0.59761
        elif I_g == 4:
            return math.sqrt(2.0 / 21.0) # ~ 0.30861
        else:
            return 0.0
    elif I_gamma == 4:
        if I_g == 2:
            return math.sqrt(3.0 / 35.0) # ~ 0.29277
        elif I_g == 4:
            return math.sqrt(10.0 / 77.0) # ~ 0.36037
        elif I_g == 6:
            return math.sqrt(5.0 / 462.0) # ~ 0.10403
        else:
            return 0.0
    else:
        # Approximate scaling
        return 0.30


def invert_z_gamma_from_branching(
    R_exp_B_E2: float,
    E_2gamma_keV: float = 821.1,
    E_2g_keV: float = 79.8,
    I_gamma: int = 2
) -> Dict[str, Any]:
    """
    Inverts Mikhailov band-mixing parameter z_gamma from experimental B(E2; 2_gamma -> 0_g) / B(E2; 2_gamma -> 2_g).
    """
    if R_exp_B_E2 <= 0.0:
        raise ValueError("Branching ratio R_exp must be strictly positive.")

    # Alaga baseline for 2_gamma -> 0_g vs 2_gamma -> 2_g is 7/10 = 0.700
    R_alaga = 0.7000

    # R_exp = 0.700 * (1 - 6 * z_gamma)^2
    # 1 - 6 * z_gamma = sqrt(R_exp / 0.700)
    # z_gamma = (1 - sqrt(R_exp / 0.700)) / 6.0
    ratio_frac = R_exp_B_E2 / R_alaga
    z_gamma = (1.0 - math.sqrt(ratio_frac)) / 6.0

    # Rotational-vibrational coupling matrix element h2
    dE_keV = E_2gamma_keV - E_2g_keV
    h2_keV = z_gamma * dE_keV / math.sqrt(6.0)

    # Classification
    if z_gamma < 0.015:
        classif = "Rigid Axial Rotor (Negligible gamma-mixing)"
    elif z_gamma <= 0.045:
        classif = "Well-Deformed Prolate Rotor (Harmonic gamma-vibrations)"
    elif z_gamma <= 0.075:
        classif = "Transitional Nucleus (Moderate gamma-softness)"
    else:
        classif = "Gamma-Soft / Triaxial Asymmetric Core (Strong band mixing)"

    # Predict branching to 4_g^+
    # M(2_gamma -> 4_g) = sqrt(1/70) * (1 + 14 * z_gamma)
    # B(2_gamma -> 4_g) / B(2_gamma -> 2_g) = (1/20) * [ (1 + 14*z_gamma) / 1.0 ]^2 = 0.050 * (1 + 14*z_gamma)^2
    R_4g_predicted = 0.050 * ((1.0 + 14.0 * z_gamma) ** 2)

    return {
        "I_gamma": I_gamma,
        "experimental_B_E2_ratio": R_exp_B_E2,
        "unperturbed_Alaga_ratio": R_alaga,
        "alaga_deviation_pct": round(((R_exp_B_E2 - R_alaga) / R_alaga) * 100.0, 2),
        "inverted_z_gamma": round(z_gamma, 5),
        "rotational_vibrational_h2_keV": round(h2_keV, 2),
        "gamma_ground_band_energy_gap_keV": round(dE_keV, 1),
        "predicted_B_E2_4g_to_2g_ratio": round(R_4g_predicted, 4),
        "structural_classification": classif
    }


def format_text_report(inv_res: Dict[str, Any]) -> str:
    lines = [
        "=" * 76,
        "   GAMMA-BAND MIKHAILOV z_gamma MIXING & ALAGA BRANCHING SUITE",
        "   Based on Alaga (1955), Mikhailov (1966) & Bohr-Mottelson Vol. II §4-2",
        "=" * 76,
        f" GAMMA-TO-GROUND TRANSITIONS FOR STATE I_gamma = {inv_res['I_gamma']}^+:",
        f"   Experimental B(E2; 0_g / 2_g): {inv_res['experimental_B_E2_ratio']:.4f}",
        f"   Unperturbed Alaga Ratio     : {inv_res['unperturbed_Alaga_ratio']:.4f}",
        f"   Alaga Rule Deviation        : {inv_res['alaga_deviation_pct']:+.2f}%",
        "-" * 76,
        " INVERTED MIKHAILOV PARAMETER & ROT-VIB COUPLING:",
        f"   Mikhailov Mixing Parameter  : z_gamma = {inv_res['inverted_z_gamma']:.5f}",
        f"   Rot-Vib Coupling Matrix h_2 : {inv_res['rotational_vibrational_h2_keV']:.2f} keV  (Band Gap Delta_E = {inv_res['gamma_ground_band_energy_gap_keV']:.1f} keV)",
        f"   Predicted B(E2; 4_g / 2_g)  : {inv_res['predicted_B_E2_4g_to_2g_ratio']:.4f}  (Alaga unperturbed: 0.0500)",
        f"   Structural Phase Assignment : {inv_res['structural_classification']}",
        "-" * 76,
        " Methodological Significance:",
        "   - Alaga rule assumes pure K=2; Delta_K=2 Coriolis mixing reduces 0_g/2_g ratio by (1 - 6*z_gamma)^2.",
        "   - In well-deformed rare earths, z_gamma ~ 0.02 - 0.04 reflects harmonic vibration-rotation coupling.",
        "   - Large z_gamma (> 0.06) directly signals the onset of triaxiality and gamma-softness in A~130.",
        "=" * 76
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Gamma-Vibrational Mikhailov z_gamma Band-Mixing Inverter"
    )
    parser.add_argument("--ratio", type=float, default=0.540, help="Measured B(E2; 2_gamma -> 0_g) / B(E2; 2_gamma -> 2_g) (default: 0.540)")
    parser.add_argument("--E-gamma-bandhead", type=float, default=821.1, help="E(2_gamma) in keV (default: 821.1)")
    parser.add_argument("--E-ground-2plus", type=float, default=79.8, help="E(2_g) in keV (default: 79.8)")
    parser.add_argument("--preset", type=str, default="168Er_gamma_band",
                        choices=["168Er_gamma_band", "166Er_gamma_band", "154Sm_gamma_band", "130Ba_gamma_soft"],
                        help="Benchmark preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")

    args = parser.parse_args()

    r_val = args.ratio
    eg_val = args.E_gamma_bandhead
    e2g_val = args.E_ground_2plus

    if args.preset == "168Er_gamma_band":
        r_val, eg_val, e2g_val = 0.540, 821.1, 79.8
    elif args.preset == "166Er_gamma_band":
        r_val, eg_val, e2g_val = 0.525, 785.9, 80.6
    elif args.preset == "154Sm_gamma_band":
        r_val, eg_val, e2g_val = 0.450, 1440.0, 82.0
    elif args.preset == "130Ba_gamma_soft":
        r_val, eg_val, e2g_val = 0.320, 908.1, 357.4 # Strong gamma-soft mixing

    res = invert_z_gamma_from_branching(r_val, E_2gamma_keV=eg_val, E_2g_keV=e2g_val)

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res))


if __name__ == "__main__":
    main()
