#!/usr/bin/env python3
"""
davydov_wobbling_rotor_calculator.py
====================================
Davydov-Filippov Triaxial Rotor & Quantum Particle-Rotor Wobbling Analyzer.

Physics & Formulation:
----------------------
1. Davydov-Filippov Model for Even-Even Triaxial Nuclei:
   Hamiltonian: H = sum_{k=1}^3 A_k * R_k^2  where A_k = hbar^2 / (2 * J_k)
   Hydrodynamic Moments of Inertia (Bohr-Mottelson):
     J_k = 4 * B * beta_2^2 * sin^2(gamma - (2*pi/3)*k)
   Exact Eigenvalues for I = 2+:
     E(2_1, 2_2+) = 2*(A1 + A2 + A3) -/+ 2 * sqrt(A1^2 + A2^2 + A3^2 - A1*A2 - A2*A3 - A3*A1)
   Energy Ratio R_42 = E(4_1^+) / E(2_1^+)
   Gamma-vibrational bandhead E(2_2^+)
   Transition Ratios:
     B(E2; 2_2 -> 0_1) / B(E2; 2_1 -> 0_1) = (1 - X) / (1 + X)
     B(E2; 2_2 -> 2_1) / B(E2; 2_1 -> 0_1) = (10/7) * (8/9 * sin^2(3*gamma)) / [1 - 8/9*sin^2(3*gamma) + X]
     where X = sqrt(1 - 8/9 * sin^2(3*gamma))

2. Quantum Particle-Rotor Wobbling Motion (Odd-A Nuclei, Frauendorf & Donau 2014):
   Hamiltonian: H = sum_{k=1}^3 A_k * (I_k - j_k)^2
   Axis 1: Medium axis (largest moment of inertia, J_1 > J_2, J_3, so A_1 < A_2, A_3).
   - Transverse Wobbling (TW):
     The odd quasiparticle aligns along a short axis perpendicular to the main rotation axis
     (j along axis 3, core rotates around axis 1).
     Wobbling phonon frequency:
       hbar*omega_TW(I) = sqrt{[2I*(A2 - A1) + 2*j*A1] * [2I*(A3 - A1) - 2*j*(A3 - A1)]}
       Signature: hbar*omega_TW decreases with increasing spin I!
   - Longitudinal Wobbling (LW):
     The odd quasiparticle aligns along the same axis as the collective rotation (j along axis 1).
     Wobbling phonon frequency:
       hbar*omega_LW(I) = sqrt{[2*(I - j)*(A2 - A1) + A2] * [2*(I - j)*(A3 - A1) + A3]}
       Signature: hbar*omega_LW increases with increasing spin I!

3. Experimental Wobbling Frequency Extraction:
   hbar*omega_wob_exp(I) = E(I, n_w=1) - 0.5 * [E(I-1, n_w=0) + E(I+1, n_w=0)]

4. Wobbling vs Signature Partner Falsification Metric:
   - For true wobbling: B(E2; I -> I-1)_out / B(E2; I -> I-2)_in is large (~0.2 - 0.6),
     and B(M1; I -> I-1)_out is small (< 0.1 W.u.).
   - For signature partner / cranking band: B(M1) is huge (~ 0.5 - 2.0 W.u.) and
     B(E2)_out is severely hindered.

References:
  - A. S. Davydov and G. F. Filippov, Nucl. Phys. 8, 237 (1958).
  - S. Frauendorf and F. Donau, Phys. Rev. C 89, 014322 (2014).
  - C. M. Petrache, "Chirality and Wobbling in Atomic Nuclei", Springer (2024).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_hydrodynamic_inertias(
    gamma_deg: float,
    beta2: float = 0.25,
    hbar2_over_2B: float = 20.0
) -> Tuple[float, float, float]:
    """
    Computes rotational constants A_k = hbar^2 / (2 * J_k) [keV]
    using Bohr-Mottelson hydrodynamic irrotational flow:
    J_k = 4 * B * beta_2^2 * sin^2(gamma - 2*pi*k / 3)
    Returns (A1, A2, A3) in keV.
    """
    gamma_rad = math.radians(gamma_deg)
    A_list = []

    for k in (1, 2, 3):
        angle = gamma_rad - (2.0 * math.pi * k / 3.0)
        sin_val = math.sin(angle)
        denom = 4.0 * (beta2 ** 2) * (sin_val ** 2)
        if denom < 1e-4:
            denom = 1e-4
        A_k = hbar2_over_2B / denom
        A_list.append(A_k)

    return A_list[0], A_list[1], A_list[2]


def davydov_filippov_energies_and_be2(gamma_deg: float, E2_1_keV: float = 100.0) -> Dict[str, Any]:
    """
    Computes exact Davydov-Filippov energy levels (in keV) and B(E2) ratios
    as a function of triaxial parameter gamma (degrees).
    Normalized to E(2_1^+) = E2_1_keV.
    """
    gamma_rad = math.radians(gamma_deg)
    sin3g = math.sin(3.0 * gamma_rad)
    arg = 1.0 - (8.0 / 9.0) * (sin3g ** 2)

    if arg < 0:
        arg = 0.0
    sqrt_term = math.sqrt(arg)

    # E(2_1) factor = (1 - sqrt_term), E(2_2) factor = (1 + sqrt_term)
    if 1.0 - sqrt_term < 1e-6:
        E2_2_over_E2_1 = float("inf")
    else:
        E2_2_over_E2_1 = (1.0 + sqrt_term) / (1.0 - sqrt_term)

    E2_2_keV = E2_1_keV * E2_2_over_E2_1

    # R_42 approximation in Davydov model
    # R_42 varies from 3.333 (gamma=0) to 2.667 (gamma=30)
    R_42 = (10.0 / 3.0) - (2.0 / 3.0) * (sin3g ** 2) / (1.0 + sqrt_term)
    E4_1_keV = E2_1_keV * R_42

    # B(E2) branching ratios
    if 1.0 + sqrt_term > 0:
        be2_22_to_01_ratio = (1.0 - sqrt_term) / (1.0 + sqrt_term)
    else:
        be2_22_to_01_ratio = 0.0

    denom_be2 = 1.0 - (8.0 / 9.0) * (sin3g ** 2) + sqrt_term
    if denom_be2 > 1e-6:
        be2_22_to_21_ratio = (10.0 / 7.0) * ((8.0 / 9.0) * (sin3g ** 2)) / denom_be2
    else:
        be2_22_to_21_ratio = 0.0

    return {
        "gamma_deg": gamma_deg,
        "E2_1_keV": E2_1_keV,
        "E2_2_keV": round(E2_2_keV, 2),
        "E4_1_keV": round(E4_1_keV, 2),
        "E2_2_over_E2_1": round(E2_2_over_E2_1, 3),
        "R_42": round(R_42, 3),
        "B_E2_22_to_01_over_21_to_01": round(be2_22_to_01_ratio, 4),
        "B_E2_22_to_21_over_21_to_01": round(be2_22_to_21_ratio, 4),
        "triaxial_regime": "Axial" if gamma_deg < 5.0 else ("Maximal_Triaxial" if abs(gamma_deg - 30.0) < 5.0 else "Triaxial")
    }


def frauendorf_wobbling_frequency(
    I: float,
    j: float,
    A1: float,
    A2: float,
    A3: float,
    mode: str = "TW"
) -> Dict[str, Any]:
    """
    Computes theoretical wobbling frequency hbar*omega_wob (in keV) for spin I
    under Transverse (TW) or Longitudinal (LW) wobbling model (Frauendorf & Donau 2014).
    Assumes A1 < A2, A3 (axis 1 has largest moment of inertia).
    """
    if mode.upper() == "TW":
        # Transverse wobbling: j perpendicular to rotation axis (j along axis 3)
        term1 = 2.0 * I * (A2 - A1) + 2.0 * j * A1
        term2 = 2.0 * I * (A3 - A1) - 2.0 * j * (A3 - A1)

        prod = term1 * term2
        if prod > 0:
            omega = math.sqrt(prod)
            status = "stable"
        else:
            omega = 0.0
            status = "unstable_or_realigned"

        return {
            "I": I,
            "j": j,
            "mode": "Transverse_Wobbling (TW)",
            "omega_wob_keV": round(omega, 2),
            "status": status,
            "term1_keV": round(term1, 2),
            "term2_keV": round(term2, 2)
        }
    else:
        # Longitudinal wobbling: j along rotation axis (axis 1)
        term1 = 2.0 * (I - j) * (A2 - A1) + A2
        term2 = 2.0 * (I - j) * (A3 - A1) + A3

        prod = term1 * term2
        if prod > 0:
            omega = math.sqrt(prod)
            status = "stable"
        else:
            omega = 0.0
            status = "unstable"

        return {
            "I": I,
            "j": j,
            "mode": "Longitudinal_Wobbling (LW)",
            "omega_wob_keV": round(omega, 2),
            "status": status,
            "term1_keV": round(term1, 2),
            "term2_keV": round(term2, 2)
        }


def extract_experimental_wobbling_sequence(
    yrast_band: List[Tuple[float, float]],  # List of (I, E_keV) for n_w = 0
    wobbling_band: List[Tuple[float, float]]  # List of (I, E_keV) for n_w = 1
) -> List[Dict[str, Any]]:
    """
    Extracts experimental wobbling energy:
    hbar*omega_wob(I) = E(I, n_w=1) - 0.5 * [E(I-1, n_w=0) + E(I+1, n_w=0)]
    """
    yrast_dict = {round(item[0], 1): item[1] for item in yrast_band}
    results = []

    for I_wob, E_wob in wobbling_band:
        I_prev = round(I_wob - 1.0, 1)
        I_next = round(I_wob + 1.0, 1)

        if I_prev in yrast_dict and I_next in yrast_dict:
            E_ref = 0.5 * (yrast_dict[I_prev] + yrast_dict[I_next])
            omega_exp = E_wob - E_ref
            results.append({
                "I": I_wob,
                "E_wob_keV": E_wob,
                "E_ref_interpolated_keV": round(E_ref, 2),
                "omega_wob_exp_keV": round(omega_exp, 2)
            })

    return results


def classify_wobbling_trend(omega_seq: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Analyzes whether experimental wobbling frequency decreases with spin I (TW)
    or increases with spin I (LW).
    """
    if len(omega_seq) < 2:
        return {"trend": "Insufficient_Data", "slope_keV_per_hbar": 0.0}

    spins = [item["I"] for item in omega_seq]
    omegas = [item["omega_wob_exp_keV"] for item in omega_seq]

    # Linear regression slope
    n = len(spins)
    mean_i = sum(spins) / n
    mean_w = sum(omegas) / n
    num = sum((spins[k] - mean_i) * (omegas[k] - mean_w) for k in range(n))
    den = sum((spins[k] - mean_i) ** 2 for k in range(n))
    slope = num / den if den != 0 else 0.0

    if slope < -5.0:
        verdict = "Transverse_Wobbling (TW) Candidate (Frequency decreases with I)"
    elif slope > +5.0:
        verdict = "Longitudinal_Wobbling (LW) Candidate (Frequency increases with I)"
    else:
        verdict = "Flat_or_Transitional_Wobbling"

    return {
        "slope_keV_per_hbar": round(slope, 3),
        "verdict": verdict,
        "min_omega_keV": min(omegas),
        "max_omega_keV": max(omegas),
        "num_points": n
    }


def falsify_wobbling_vs_signature_partner(
    be2_out_over_in: Optional[float] = None,
    b_m1_out_w_u: Optional[float] = None,
    delta_mixing_ratio: Optional[float] = None
) -> Dict[str, Any]:
    """
    Tests whether an observed Delta_I = 1 inter-band transition satisfies wobbling criteria
    or is a falsified pseudo-wobbling signature partner band.

    Criteria (Petrache 2024):
    1. B(E2)_out / B(E2)_in must be significant (> 0.1, typically 0.2 - 0.7).
    2. B(M1)_out must be small (< 0.1 W.u.). If B(M1)_out ~ 0.5 - 2.0 W.u., it is a magnetic rotation / signature partner!
    3. Multipolarity mixing ratio delta(E2/M1) must be large (|delta| > 1.0).
    """
    tests = []
    score = 0
    total = 0

    if be2_out_over_in is not None:
        total += 1
        if be2_out_over_in >= 0.15:
            tests.append(f"PASS: B(E2)_out/B(E2)_in = {be2_out_over_in:.3f} >= 0.15 (collective E2 phonon nature)")
            score += 1
        else:
            tests.append(f"FAIL: B(E2)_out/B(E2)_in = {be2_out_over_in:.3f} < 0.15 (lacks collective E2 wobbling strength)")

    if b_m1_out_w_u is not None:
        total += 1
        if b_m1_out_w_u <= 0.15:
            tests.append(f"PASS: B(M1)_out = {b_m1_out_w_u:.3f} W.u. <= 0.15 (M1 is hindered as expected for wobbling)")
            score += 1
        else:
            tests.append(f"FAIL: B(M1)_out = {b_m1_out_w_u:.3f} W.u. > 0.15 (Huge M1 indicates single-particle signature partner / shears mechanism)")

    if delta_mixing_ratio is not None:
        total += 1
        if abs(delta_mixing_ratio) >= 1.0:
            tests.append(f"PASS: |delta(E2/M1)| = {abs(delta_mixing_ratio):.2f} >= 1.0 (E2 dominant)")
            score += 1
        else:
            tests.append(f"FAIL: |delta(E2/M1)| = {abs(delta_mixing_ratio):.2f} < 1.0 (M1 dominant, atypical for pure wobbling)")

    if total == 0:
        verdict = "INSUFFICIENT_ELECTROMAGNETIC_DATA"
    elif score == total:
        verdict = "ROBUST_WOBBLING_CONFIRMED"
    elif score == 0:
        verdict = "REJECTED_AS_WOBBLING (Signature Partner or Magnetic Rotation)"
    else:
        verdict = "AMBIGUOUS_NEED_PRECISE_LIFETIMES"

    return {
        "verdict": verdict,
        "score": f"{score}/{total}",
        "diagnostic_checks": tests
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   DAVYDOV-FILIPPOV TRIAXIAL ROTOR & WOBBLING ANALYZER")
    lines.append("=" * 72)

    if "davydov" in summary:
        df = summary["davydov"]
        lines.append(f" TRIAXIAL ROTOR CHARACTERISTICS (gamma = {df['gamma_deg']:.1f} deg):")
        lines.append(f"   Regime                         : {df['triaxial_regime']}")
        lines.append(f"   E(2_1^+) Energy                : {df['E2_1_keV']:.1f} keV")
        lines.append(f"   E(2_2^+) Gamma Bandhead        : {df['E2_2_keV']:.1f} keV (Ratio = {df['E2_2_over_E2_1']:.3f})")
        lines.append(f"   E(4_1^+) Energy                : {df['E4_1_keV']:.1f} keV (R_42 = {df['R_42']:.3f})")
        lines.append(f"   B(E2; 2_2->0_1) / B(E2; 2_1->0_1): {df['B_E2_22_to_01_over_21_to_01']:.4f}")
        lines.append(f"   B(E2; 2_2->2_1) / B(E2; 2_1->0_1): {df['B_E2_22_to_21_over_21_to_01']:.4f}")
        lines.append("-" * 72)

    if "wobbling_model" in summary:
        wm = summary["wobbling_model"]
        lines.append(" FRAUENDORF-DONAU WOBBLING PHONON MODEL:")
        lines.append(f"   Mode                           : {wm['mode']}")
        lines.append(f"   Spin I = {wm['I']}, Particle j = {wm['j']}")
        lines.append(f"   Predicted Wobbling Energy      : {wm['omega_wob_keV']:.1f} keV (Status: {wm['status']})")
        lines.append("-" * 72)

    if "experimental_trend" in summary:
        et = summary["experimental_trend"]
        lines.append(" EXPERIMENTAL WOBBLING SEQUENCE ANALYSIS:")
        lines.append(f"   Trajectory Slope               : {et['slope_keV_per_hbar']:.3f} keV/hbar")
        lines.append(f"   Verdict                        : {et['verdict']}")
        lines.append(f"   Energy Range                   : {et['min_omega_keV']:.1f} - {et['max_omega_keV']:.1f} keV")
        lines.append("-" * 72)

    if "falsification" in summary:
        fa = summary["falsification"]
        lines.append(" WOBBLING VS SIGNATURE PARTNER FALSIFICATION AUDIT:")
        lines.append(f"   Final Classification           : {fa['verdict']} ({fa['score']})")
        for chk in fa["diagnostic_checks"]:
            lines.append(f"     * {chk}")
        lines.append("-" * 72)

    lines.append(" Physical Significance:")
    lines.append("   - Transverse wobbling requires hbar*omega_wob to decrease with spin I.")
    lines.append("   - Longitudinal wobbling requires hbar*omega_wob to increase with spin I.")
    lines.append("   - True wobbling is accompanied by strong Delta_I=1 collective E2 transitions.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Davydov-Filippov Triaxial Rotor & Quantum Wobbling Motion Analyzer."
    )
    parser.add_argument("--gamma", type=float, default=25.0, help="Triaxial deformation angle gamma in degrees (default: 25.0)")
    parser.add_argument("--E2-1", type=float, default=100.0, help="E(2_1^+) energy in keV (default: 100.0)")
    parser.add_argument("--spin-I", type=float, default=13.5, help="Total spin I for odd-A nucleus")
    parser.add_argument("--spin-j", type=float, default=6.5, help="Quasiparticle spin j (e.g. 6.5 for i13/2)")
    parser.add_argument("--A1", type=float, default=12.0, help="Rotational constant A1 = hbar^2/(2*J1) in keV (default: 12.0)")
    parser.add_argument("--A2", type=float, default=25.0, help="Rotational constant A2 in keV (default: 25.0)")
    parser.add_argument("--A3", type=float, default=45.0, help="Rotational constant A3 in keV (default: 45.0)")
    parser.add_argument("--mode", type=str, default="TW", choices=["TW", "LW"], help="Wobbling mode: TW (Transverse) or LW (Longitudinal)")
    parser.add_argument("--be2-ratio", type=float, default=None, help="Experimental B(E2)_out / B(E2)_in ratio")
    parser.add_argument("--bm1-out", type=float, default=None, help="Experimental B(M1)_out in W.u.")
    parser.add_argument("--delta-mix", type=float, default=None, help="Multipolarity mixing ratio delta(E2/M1)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    df_res = davydov_filippov_energies_and_be2(args.gamma, args.E2_1)
    wob_res = frauendorf_wobbling_frequency(args.spin_I, args.spin_j, args.A1, args.A2, args.A3, args.mode)
    fals_res = falsify_wobbling_vs_signature_partner(args.be2_ratio, args.bm1_out, args.delta_mix)

    summary = {
        "davydov": df_res,
        "wobbling_model": wob_res,
        "falsification": fals_res
    }

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
