#!/usr/bin/env python3
"""
two_quasiparticle_even_even_wobbling_analyzer.py
================================================
Two-Quasiparticle Wobbling Mode Analyzer in Even-Even Triaxial Nuclei,
Transverse Wobbling Frequency Inversion & Interband E2/M1 Signature Engine.

Physics Formulation:
--------------------
1. Two-Quasiparticle Alignment in Triaxial Even-Even Rotor:
   Based on Q. B. Chen & S. Frauendorf (Phys. Rev. Lett. 123, 232502, 2019),
   S. Y. Wang, F. Q. Chen, C. Liu et al. (Phys. Lett. B 808, 135634, 2020),
   and "Chirality and Wobbling in Atomic Nuclei" (CRC Press 2025) Ch. 10 & 11:
   In even-even triaxial nuclei, after backbending (first band crossing),
   two high-j quasiparticles (e.g. two h_11/2 protons in 130Ba or 136Nd, or two i_13/2
   neutrons in the rare-earth region) align their angular momenta along the short (s)
   axis of the triaxial core (gamma ~ -20 deg to -30 deg).
   The coupled quasiparticle spin is:
     j_12 = j_1 + j_2 ~ 10 hbar (for two h_11/2 nucleons).

2. Transverse Wobbling in Even-Even Core:
   The total angular momentum is I = R + j_12.
   The collective triaxial core rotates primarily about the intermediate (m) axis,
   which has the largest moment of inertia J_m > J_s, J_l.
   The ground-state sequence of this configuration forms the yrast two-quasiparticle
   band (zero-phonon wobbler, n_w = 0).
   The collective oscillation of the total spin vector I away from the principal axis plane
   constitutes the one-phonon wobbling excitation (n_w = 1).

3. Wobbling Frequency & Energy Spacing:
   In the harmonic approximation:
     E(I, n_w) = E_yrast(I) + (n_w + 1/2) * hbar * omega_w(I)
   The wobbling energy spacing is:
     E_wob(I) = E(n_w=1, I) - 0.5 * [ E(n_w=0, I+1) + E(n_w=0, I-1) ]
   For Transverse Wobbling (TW), the wobbling frequency decreases with spin I:
     hbar * omega_w(I) ~ omega_rot(I) * sqrt( [ (J_m - J_s)(J_m - J_l) ] / [ J_s * J_l ] )
   where omega_rot(I) = (I - j_12) / J_m.

4. Interband E2/M1 Transition Ratios:
   The hallmark signature of wobbling is the dominant, collective Delta I = 1 E2 transition
   connecting the n_w = 1 wobbling band to the n_w = 0 yrast band:
     B(E2, n_w=1, I -> n_w=0, I-1) / B(E2, n_w=1, I -> n_w=1, I-2) ~ (2 / I) * [ sin(gamma + 30) / sin(gamma - 60) ]^2
   This ratio is large (~ 0.2 - 0.8), while the M1 transition rate B(M1) is suppressed,
   distinctly separating wobbling from single-particle quasiparticle excitations.
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "130Ba_two_quasiparticle_wobbler": {
        "description": "130Ba two-quasiparticle wobbler (Wang et al. PLB 808, 135634, 2020)",
        "nucleus": "130Ba",
        "quasiparticle_config": "pi(h_11/2)^2",
        "j_aligned": 10.0,
        "gamma_deg": -25.0,
        "J_m_hbar2_per_MeV": 28.0,
        "J_s_hbar2_per_MeV": 12.0,
        "J_l_hbar2_per_MeV": 6.0,
        "yrast_levels": [
            {"I": 10, "energy_keV": 3280.0},
            {"I": 12, "energy_keV": 3950.0},
            {"I": 14, "energy_keV": 4720.0},
            {"I": 16, "energy_keV": 5580.0},
            {"I": 18, "energy_keV": 6530.0}
        ],
        "wobbling_levels": [
            {"I": 11, "energy_keV": 4120.0, "be2_out_in_ratio": 0.48, "mixing_ratio_delta": -2.8},
            {"I": 13, "energy_keV": 4790.0, "be2_out_in_ratio": 0.41, "mixing_ratio_delta": -2.4},
            {"I": 15, "energy_keV": 5540.0, "be2_out_in_ratio": 0.35, "mixing_ratio_delta": -2.0},
            {"I": 17, "energy_keV": 6380.0, "be2_out_in_ratio": 0.30, "mixing_ratio_delta": -1.7}
        ]
    },
    "136Nd_two_quasiparticle_wobbler": {
        "description": "136Nd predicted 2-qp transverse wobbler (Chen & Frauendorf PRL 123, 232502, 2019)",
        "nucleus": "136Nd",
        "quasiparticle_config": "pi(h_11/2)^2",
        "j_aligned": 9.5,
        "gamma_deg": -22.0,
        "J_m_hbar2_per_MeV": 32.0,
        "J_s_hbar2_per_MeV": 14.0,
        "J_l_hbar2_per_MeV": 8.0,
        "yrast_levels": [
            {"I": 10, "energy_keV": 3450.0},
            {"I": 12, "energy_keV": 4150.0},
            {"I": 14, "energy_keV": 4960.0},
            {"I": 16, "energy_keV": 5880.0},
            {"I": 18, "energy_keV": 6900.0}
        ],
        "wobbling_levels": [
            {"I": 11, "energy_keV": 4350.0, "be2_out_in_ratio": 0.52, "mixing_ratio_delta": -3.1},
            {"I": 13, "energy_keV": 5040.0, "be2_out_in_ratio": 0.44, "mixing_ratio_delta": -2.6},
            {"I": 15, "energy_keV": 5830.0, "be2_out_in_ratio": 0.38, "mixing_ratio_delta": -2.1},
            {"I": 17, "energy_keV": 6720.0, "be2_out_in_ratio": 0.32, "mixing_ratio_delta": -1.8}
        ]
    },
    "spurious_quasiparticle_counterexample": {
        "description": "Spurious single-particle band with rising energy and zero interband E2",
        "nucleus": "Fake-Nucleus",
        "quasiparticle_config": "unaligned",
        "j_aligned": 4.0,
        "gamma_deg": -10.0,
        "J_m_hbar2_per_MeV": 25.0,
        "J_s_hbar2_per_MeV": 20.0,
        "J_l_hbar2_per_MeV": 18.0,
        "yrast_levels": [
            {"I": 10, "energy_keV": 3000.0},
            {"I": 12, "energy_keV": 3600.0},
            {"I": 14, "energy_keV": 4300.0},
            {"I": 16, "energy_keV": 5100.0},
            {"I": 18, "energy_keV": 6000.0}
        ],
        "wobbling_levels": [
            {"I": 11, "energy_keV": 3950.0, "be2_out_in_ratio": 0.02, "mixing_ratio_delta": -0.15},
            {"I": 13, "energy_keV": 4850.0, "be2_out_in_ratio": 0.03, "mixing_ratio_delta": -0.20},
            {"I": 15, "energy_keV": 5850.0, "be2_out_in_ratio": 0.02, "mixing_ratio_delta": -0.18}
        ]
    }
}


def calculate_two_quasiparticle_wobbling_energies(yrast_levels, wobbling_levels):
    """
    Calculates experimental wobbling excitation energy E_wob(I) = E(wob, I) - 0.5 * [E(yrast, I-1) + E(yrast, I+1)].
    """
    yrast_dict = {lvl["I"]: lvl["energy_keV"] for lvl in yrast_levels}
    wob_results = []

    for w in wobbling_levels:
        I_w = w["I"]
        E_w = w["energy_keV"]
        I_minus = I_w - 1
        I_plus = I_w + 1

        if I_minus in yrast_dict and I_plus in yrast_dict:
            E_yrast_interp = 0.5 * (yrast_dict[I_minus] + yrast_dict[I_plus])
            E_wob = E_w - E_yrast_interp
        elif I_minus in yrast_dict:
            E_wob = E_w - yrast_dict[I_minus]
        else:
            E_wob = 0.0

        wob_results.append({
            "I": I_w,
            "energy_keV": E_w,
            "E_wob_keV": float(E_wob),
            "be2_out_in_ratio": float(w.get("be2_out_in_ratio", 0.0)),
            "mixing_ratio_delta": float(w.get("mixing_ratio_delta", 0.0))
        })

    return wob_results


def evaluate_wobbling_slope_and_criteria(wob_results, J_m, J_s, J_l, j_aligned, gamma_deg):
    """
    Evaluates the frequency slope d(E_wob)/dI, theoretical E2 branching ratio, and confirms wobbling status.
    """
    if len(wob_results) < 2:
        return {"status": "insufficient_data", "confidence_pct": 0.0}

    spins = [w["I"] for w in wob_results]
    ewobs = [w["E_wob_keV"] for w in wob_results]
    be2_ratios = [w["be2_out_in_ratio"] for w in wob_results]

    # Linear regression slope: d(E_wob)/dI
    slope_keV_per_hbar, intercept = np.polyfit(spins, ewobs, 1)

    # Theoretical ratio prefactor from triaxial geometry (using intrinsic |gamma| deformation)
    gamma_rad = math.radians(abs(gamma_deg))
    num = math.sin(gamma_rad + math.pi / 6.0)
    den = math.sin(gamma_rad - math.pi / 3.0)
    c_geom = 2.0 * (num / den)**2 if den != 0.0 else 2.0

    theo_ratios = [c_geom / float(spin) for spin in spins]
    mean_exp_ratio = float(np.mean(be2_ratios))
    mean_theo_ratio = float(np.mean(theo_ratios))

    # Criteria scoring:
    # 1. Decreasing wobbling frequency slope (Transverse Wobbling): slope < -10 keV/hbar
    slope_score = 0.0
    if slope_keV_per_hbar < -10.0:
        slope_score = 40.0
    elif slope_keV_per_hbar < 0.0:
        slope_score = 25.0
    else:
        slope_score = 0.0

    # 2. Enhanced B(E2)_out / B(E2)_in ratio (> 0.20)
    ratio_score = 0.0
    if mean_exp_ratio >= 0.25:
        ratio_score = 40.0
    elif mean_exp_ratio >= 0.15:
        ratio_score = 25.0
    elif mean_exp_ratio >= 0.08:
        ratio_score = 10.0
    else:
        ratio_score = 0.0

    # 3. Intermediate axis dominance: J_m > J_s, J_l
    moi_score = 20.0 if (J_m > J_s and J_m > J_l) else 0.0

    total_confidence = slope_score + ratio_score + moi_score

    if total_confidence >= 75.0:
        verdict = "CONFIRMED_TWO_QUASIPARTICLE_TRANSVERSE_WOBBLING"
    elif total_confidence >= 50.0:
        verdict = "CANDIDATE_TWO_QUASIPARTICLE_WOBBLING"
    else:
        verdict = "REJECTED_SPURIOUS_OR_SINGLE_PARTICLE_BAND"

    return {
        "slope_dE_wob_dI_keV_per_hbar": float(slope_keV_per_hbar),
        "is_transverse_trend": bool(slope_keV_per_hbar < 0.0),
        "geometric_c_factor": float(c_geom),
        "mean_experimental_be2_ratio": mean_exp_ratio,
        "mean_theoretical_be2_ratio": mean_theo_ratio,
        "confidence_score_pct": float(total_confidence),
        "wobbling_verdict": verdict
    }


def run_two_qp_wobbling_analysis(nucleus, quasiparticle_config, j_aligned, gamma_deg,
                                  J_m, J_s, J_l, yrast_levels, wobbling_levels):
    """
    Complete execution pipeline for two-quasiparticle even-even wobbling analysis.
    """
    wob_eval = calculate_two_quasiparticle_wobbling_energies(yrast_levels, wobbling_levels)
    verdict = evaluate_wobbling_slope_and_criteria(wob_eval, J_m, J_s, J_l, j_aligned, gamma_deg)

    return {
        "nucleus": nucleus,
        "configuration": quasiparticle_config,
        "parameters": {
            "j_aligned_hbar": float(j_aligned),
            "gamma_deg": float(gamma_deg),
            "J_m_hbar2_per_MeV": float(J_m),
            "J_s_hbar2_per_MeV": float(J_s),
            "J_l_hbar2_per_MeV": float(J_l)
        },
        "evaluated_levels": wob_eval,
        "wobbling_verdict": verdict
    }


def format_text_report(res, title="Two-Quasiparticle Even-Even Wobbling Mode Analyzer"):
    nuc = res["nucleus"]
    cfg = res["configuration"]
    p = res["parameters"]
    wv = res["wobbling_verdict"]

    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Nucleus: {nuc} | Configuration: {cfg} (j_align = {p['j_aligned_hbar']:.1f} hbar, gamma = {p['gamma_deg']:.1f} deg)")
    lines.append("=" * 76)
    lines.append(f"  Moments of Inertia [J_m, J_s, J_l] : [{p['J_m_hbar2_per_MeV']:.1f}, {p['J_s_hbar2_per_MeV']:.1f}, {p['J_l_hbar2_per_MeV']:.1f}] hbar^2/MeV")
    lines.append(f"  Intermediate Axis Dominance        : {'YES (J_m is largest)' if (p['J_m_hbar2_per_MeV'] > p['J_s_hbar2_per_MeV'] and p['J_m_hbar2_per_MeV'] > p['J_l_hbar2_per_MeV']) else 'NO'}")
    lines.append("-" * 76)
    lines.append("Wobbling Energy Spacings & Interband E2/M1 Properties:")
    lines.append("  Spin I (hbar)   E_level (keV)   E_wob (keV)    B(E2)_out/B(E2)_in    delta(E2/M1)")
    for lvl in res["evaluated_levels"]:
        lines.append(f"    {lvl['I']:4.1f}          {lvl['energy_keV']:8.1f}       {lvl['E_wob_keV']:7.1f}            {lvl['be2_out_in_ratio']:6.3f}            {lvl['mixing_ratio_delta']:6.2f}")
    lines.append("-" * 76)
    lines.append("Physics Diagnostics & Verification Verdict:")
    lines.append(f"  Wobbling Frequency Slope d(E_wob)/dI: {wv['slope_dE_wob_dI_keV_per_hbar']:.2f} keV/hbar ({'Decreasing -> Transverse Wobbling' if wv['is_transverse_trend'] else 'Rising -> Non-transverse/spurious'})")
    lines.append(f"  Mean Experimental B(E2) Ratio       : {wv['mean_experimental_be2_ratio']:.3f} (Theory expectation ~ {wv['mean_theoretical_be2_ratio']:.3f})")
    lines.append(f"  Evaluation Confidence Score         : {wv['confidence_score_pct']:.1f}%")
    lines.append(f"  Final Physical Verdict              : {wv['wobbling_verdict']}")
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Two-Quasiparticle Wobbling Mode Analyzer in Even-Even Triaxial Nuclei."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load experimental benchmark preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        nucleus = p["nucleus"]
        cfg = p["quasiparticle_config"]
        j_align = p["j_aligned"]
        gamma = p["gamma_deg"]
        J_m = p["J_m_hbar2_per_MeV"]
        J_s = p["J_s_hbar2_per_MeV"]
        J_l = p["J_l_hbar2_per_MeV"]
        yrast = p["yrast_levels"]
        wob = p["wobbling_levels"]
        title = f"Preset: {args.preset} ({p['description']})"
    else:
        return parser.print_help()

    res = run_two_qp_wobbling_analysis(
        nucleus=nucleus,
        quasiparticle_config=cfg,
        j_aligned=j_align,
        gamma_deg=gamma,
        J_m=J_m,
        J_s=J_s,
        J_l=J_l,
        yrast_levels=yrast,
        wobbling_levels=wob
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
