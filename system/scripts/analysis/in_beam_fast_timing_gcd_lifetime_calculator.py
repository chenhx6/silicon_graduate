#!/usr/bin/env python3
"""
in_beam_fast_timing_gcd_lifetime_calculator.py
==============================================
In-Beam Electronic Fast-Timing Generalized Centroid Difference (GCD) Method,
Prompt Response Function (PRF) Walk Calibration & Picosecond Nuclear Lifetime Engine.

Physics Formulation:
--------------------
1. Electronic Fast-Timing in Nuclear Spectroscopy:
   Based on J.-M. Régis et al. (Nucl. Instrum. Methods A 606, 466, 2009; NIM A 726, 191, 2013),
   吴治华《原子核物理实验方法》第 9, 14 章, and 汪晓莲等《粒子探测技术》第 8 章:
   Fast scintillators (LaBr3(Ce), CeBr3, BaF2) coupled to fast PMTs and constant fraction
   discriminators (CFD) measure excited-state lifetimes down to ~ 5 - 10 ps.

2. Prompt Response Function (PRF) Time Walk:
   Detector rise-time fluctuations and PMT transit-time dispersion cause the prompt centroid
   to depend strongly on gamma-ray energy E_gamma:
     PRF(E_gamma) = a0 / sqrt(E_gamma) + c0 * E_gamma + d0
   where typical LaBr3(Ce) parameters are a0 ~ 450 ps*keV^(1/2), c0 ~ -0.02 ps/keV.

3. Generalized Centroid Difference (GCD) Method:
   For a cascade feeding -> Level(tau) -> decay:
   By setting symmetric gates in the 2D energy-time coincidence matrix:
     Gate 1: Start on E_feed, Stop on E_decay -> Centroid C1 = Delta_PRF(E_feed, E_decay) + tau
     Gate 2: Start on E_decay, Stop on E_feed -> Centroid C2 = -Delta_PRF(E_feed, E_decay) - tau
   The centroid difference Delta C = C1 - C2 completely eliminates absolute time zero-point drift:
     Delta C = 2 * tau + 2 * Delta_PRF(E_feed, E_decay)
   The extracted lifetime is:
     tau = [ Delta C - 2 * (PRF(E_feed) - PRF(E_decay)) ] / 2.0

4. Transition Strength Inversion:
   From extracted lifetime tau, gamma energy E_decay, and mass number A:
     T_gamma = 1.0 / ( tau * (1.0 + alpha_tot) )
     B(E2) [W.u.] and B(M1) [W.u.] are directly evaluated.
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "134Ce_fast_timing_2plus": {
        "description": "134Ce in-beam fast-timing 2_1+ state (4+ -> 2+ -> 0+, tau_lit ~ 62 ps)",
        "nucleus": "134Ce",
        "A_mass": 134,
        "E_feed_keV": 638.0,
        "E_decay_keV": 409.0,
        "C1_ps": 75.4,
        "sigma_C1_ps": 1.8,
        "C2_ps": -72.6,
        "sigma_C2_ps": 1.8,
        "a0_walk": 450.0,
        "c0_walk": -0.020,
        "E_level_keV": 409.0,
        "alpha_tot": 0.022
    },
    "135Pr_wobbler_fast_timing": {
        "description": "135Pr transverse wobbling candidate fast timing (tau_lit ~ 1.5 ps)",
        "nucleus": "135Pr",
        "A_mass": 135,
        "E_feed_keV": 850.0,
        "E_decay_keV": 728.0,
        "C1_ps": 2.8,
        "sigma_C1_ps": 0.8,
        "C2_ps": -2.4,
        "sigma_C2_ps": 0.8,
        "a0_walk": 450.0,
        "c0_walk": -0.020,
        "E_level_keV": 728.0,
        "alpha_tot": 0.005
    },
    "60Co_prompt_zero_calibration": {
        "description": "60Co prompt cascade calibration (1173 keV -> 1332 keV, tau ~ 1 ps)",
        "nucleus": "60Ni",
        "A_mass": 60,
        "E_feed_keV": 1173.2,
        "E_decay_keV": 1332.5,
        "C1_ps": 1.9,
        "sigma_C1_ps": 0.5,
        "C2_ps": -1.7,
        "sigma_C2_ps": 0.5,
        "a0_walk": 450.0,
        "c0_walk": -0.020,
        "E_level_keV": 1332.5,
        "alpha_tot": 0.0001
    }
}


def calculate_prf_walk(E_gamma_keV, a0=450.0, c0=-0.020, d0=0.0):
    """
    Calculates prompt response function (PRF) time walk in ps at energy E_gamma:
      PRF(E) = a0 / sqrt(E) + c0 * E + d0.
    """
    if E_gamma_keV <= 0:
        return 0.0
    return (a0 / math.sqrt(E_gamma_keV)) + (c0 * E_gamma_keV) + d0


def calculate_gcd_lifetime(C1_ps, C2_ps, sigma_C1_ps, sigma_C2_ps, E_feed_keV, E_decay_keV,
                           a0_walk=450.0, c0_walk=-0.020):
    """
    Applies the Generalized Centroid Difference (GCD) equation to extract lifetime tau and uncertainty.
    """
    walk_feed = calculate_prf_walk(E_feed_keV, a0_walk, c0_walk)
    walk_decay = calculate_prf_walk(E_decay_keV, a0_walk, c0_walk)
    delta_walk = walk_feed - walk_decay

    delta_C = C1_ps - C2_ps
    sigma_delta_C = math.sqrt(sigma_C1_ps**2 + sigma_C2_ps**2)

    tau_extracted_ps = (delta_C - 2.0 * delta_walk) / 2.0
    sigma_tau_ps = sigma_delta_C / 2.0

    return {
        "E_feed_keV": float(E_feed_keV),
        "E_decay_keV": float(E_decay_keV),
        "walk_feed_ps": float(walk_feed),
        "walk_decay_ps": float(walk_decay),
        "delta_walk_ps": float(delta_walk),
        "delta_C_ps": float(delta_C),
        "sigma_delta_C_ps": float(sigma_delta_C),
        "tau_extracted_ps": float(tau_extracted_ps),
        "sigma_tau_ps": float(sigma_tau_ps)
    }


def invert_transition_strengths(tau_ps, sigma_tau_ps, E_decay_keV, A_mass, delta_mix=0.0, alpha_tot=0.0):
    """
    Converts extracted lifetime into transition rates and B(E2) / B(M1) in Weisskopf units.
    """
    if tau_ps <= 0:
        return None

    tau_s = tau_ps * 1e-12
    sigma_tau_s = sigma_tau_ps * 1e-12
    E_MeV = E_decay_keV / 1000.0

    T_total = 1.0 / (tau_s * (1.0 + alpha_tot))

    T_W_M1 = 3.15e13 * (E_MeV**3)
    T_W_E2 = 1.22e9 * (A_mass**(4.0 / 3.0)) * (E_MeV**5)

    d2 = delta_mix**2
    T_M1 = T_total / (1.0 + d2)
    T_E2 = T_total * d2 / (1.0 + d2) if d2 > 0 else (T_total if abs(delta_mix) > 10.0 else 0.0)

    B_M1_Wu = (T_M1 / T_W_M1) if T_W_M1 > 0 else 0.0
    B_E2_Wu = (T_E2 / T_W_E2) if T_W_E2 > 0 else 0.0

    rel_err = sigma_tau_ps / max(1e-4, tau_ps)
    sigma_B_E2 = B_E2_Wu * rel_err
    sigma_B_M1 = B_M1_Wu * rel_err

    return {
        "T_total_s": float(T_total),
        "B_E2_Wu": float(B_E2_Wu),
        "sigma_B_E2_Wu": float(sigma_B_E2),
        "B_M1_Wu": float(B_M1_Wu),
        "sigma_B_M1_Wu": float(sigma_B_M1)
    }


def run_fast_timing_gcd_analysis(nucleus, A_mass, E_feed_keV, E_decay_keV,
                                 C1_ps, sigma_C1_ps, C2_ps, sigma_C2_ps,
                                 a0_walk=450.0, c0_walk=-0.020, alpha_tot=0.0, delta_mix=0.0):
    """
    Complete execution pipeline for GCD fast timing.
    """
    gcd_res = calculate_gcd_lifetime(
        C1_ps=C1_ps,
        C2_ps=C2_ps,
        sigma_C1_ps=sigma_C1_ps,
        sigma_C2_ps=sigma_C2_ps,
        E_feed_keV=E_feed_keV,
        E_decay_keV=E_decay_keV,
        a0_walk=a0_walk,
        c0_walk=c0_walk
    )

    strengths = invert_transition_strengths(
        tau_ps=gcd_res["tau_extracted_ps"],
        sigma_tau_ps=gcd_res["sigma_tau_ps"],
        E_decay_keV=E_decay_keV,
        A_mass=A_mass,
        delta_mix=delta_mix,
        alpha_tot=alpha_tot
    )

    return {
        "nucleus": nucleus,
        "A_mass": A_mass,
        "gcd_analysis": gcd_res,
        "transition_strengths": strengths
    }


def format_text_report(res, title="In-Beam Fast-Timing GCD Lifetime Engine"):
    gcd = res["gcd_analysis"]
    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Nucleus: {res['nucleus']} (A = {res['A_mass']})")
    lines.append(f"Cascade: E_feed = {gcd['E_feed_keV']:.1f} keV -> Level -> E_decay = {gcd['E_decay_keV']:.1f} keV")
    lines.append("=" * 76)
    lines.append("Prompt Response Function (PRF) Walk Correction:")
    lines.append(f"  PRF Walk at E_feed              : {gcd['walk_feed_ps']:+.2f} ps")
    lines.append(f"  PRF Walk at E_decay             : {gcd['walk_decay_ps']:+.2f} ps")
    lines.append(f"  Instrumental Walk Difference    : {gcd['delta_walk_ps']:+.2f} ps")
    lines.append("-" * 76)
    lines.append("Centroid Measurements & GCD Inversion:")
    lines.append(f"  Forward Centroid C1             : {gcd['delta_C_ps']/2.0 + gcd['delta_walk_ps']:+.2f} ps")
    lines.append(f"  Centroid Difference Delta C     : {gcd['delta_C_ps']:+.2f} +- {gcd['sigma_delta_C_ps']:.2f} ps")
    lines.append(f"  Extracted Nuclear Lifetime tau  : {gcd['tau_extracted_ps']:.2f} +- {gcd['sigma_tau_ps']:.2f} ps")
    lines.append("-" * 76)
    if res["transition_strengths"]:
        st = res["transition_strengths"]
        lines.append("Deduced Transition Strengths:")
        lines.append(f"  Total Transition Rate T_gamma   : {st['T_total_s']:.2e} s^-1")
        if st["B_E2_Wu"] > 0:
            lines.append(f"  Deduced B(E2) Strength          : {st['B_E2_Wu']:.2f} +- {st['sigma_B_E2_Wu']:.2f} W.u.")
        if st["B_M1_Wu"] > 0:
            lines.append(f"  Deduced B(M1) Strength          : {st['B_M1_Wu']:.4f} +- {st['sigma_B_M1_Wu']:.4f} W.u.")
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="In-Beam Fast-Timing Generalized Centroid Difference (GCD) Picosecond Lifetime Engine."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load experimental preset")
    parser.add_argument("--nucleus", type=str, default="Nucleus", help="Nucleus name")
    parser.add_argument("--mass-a", type=int, help="Mass number A")
    parser.add_argument("--efeed", type=float, help="Feeding transition energy in keV")
    parser.add_argument("--edecay", type=float, help="Decay transition energy in keV")
    parser.add_argument("--c1", type=float, help="Centroid C1 in ps")
    parser.add_argument("--c2", type=float, help="Centroid C2 in ps")
    parser.add_argument("--sigc", type=float, default=2.0, help="Uncertainty on centroids in ps")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        nucleus = p["nucleus"]
        A_mass = p["A_mass"]
        E_feed = p["E_feed_keV"]
        E_decay = p["E_decay_keV"]
        c1 = p["C1_ps"]
        sig1 = p.get("sigma_C1_ps", 2.0)
        c2 = p["C2_ps"]
        sig2 = p.get("sigma_C2_ps", 2.0)
        a0 = p.get("a0_walk", 450.0)
        c0 = p.get("c0_walk", -0.020)
        alpha_tot = p.get("alpha_tot", 0.0)
        title = f"Preset: {args.preset} ({p['description']})"
    elif args.efeed and args.edecay and args.c1 and args.c2:
        nucleus = args.nucleus
        A_mass = args.mass_a if args.mass_a else 134
        E_feed = args.efeed
        E_decay = args.edecay
        c1 = args.c1
        sig1 = args.sigc
        c2 = args.c2
        sig2 = args.sigc
        a0 = 450.0
        c0 = -0.020
        alpha_tot = 0.0
        title = "Custom User Input"
    else:
        return parser.print_help()

    res = run_fast_timing_gcd_analysis(
        nucleus=nucleus,
        A_mass=A_mass,
        E_feed_keV=E_feed,
        E_decay_keV=E_decay,
        C1_ps=c1,
        sigma_C1_ps=sig1,
        C2_ps=c2,
        sigma_C2_ps=sig2,
        a0_walk=a0,
        c0_walk=c0,
        alpha_tot=alpha_tot
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
