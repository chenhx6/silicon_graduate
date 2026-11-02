#!/usr/bin/env python3
"""
triaxial_superdeformed_wobbling_decayout_analyzer.py
====================================================
Triaxial Superdeformed (TSD) Wobbling Band Decayout Dynamics, Barrier Penetration
Tunneling & Intra-TSD vs Normal-Deformed Branching Competition Engine.

Physics Formulation:
--------------------
1. Triaxial Superdeformation in the A ~ 160-170 Region:
   Based on A. Bohr & B. R. Mottelson "Nuclear Structure" Vol. II §4-5,
   "Chirality and Wobbling in Atomic Nuclei" (CRC Press 2025) Ch. 10 (PDF pp. 215–230),
   S. W. Odegard et al. (Phys. Rev. Lett. 86, 5866, 2001), and H. Amro et al. (PRL 91, 162502, 2003):
   In odd-A lutetium isotopes (161, 163, 165, 167Lu), the pi i_13/2 intruder orbital stabilizes
   a pronounced triaxial superdeformed minimum (epsilon_2 ~ 0.38 - 0.42, gamma ~ 18 - 22 deg).
   The yrast TSD band corresponds to the zero-phonon wobbler (n_w = 0, TSD1).
   The excited TSD2 band is the quantized one-phonon wobbling excitation (n_w = 1).

2. Competing Decay Modes at Each Spin I:
   A state in the TSD2 wobbling band (I) de-excites via three competing pathways:
     a. Intra-band collective E2 decay: TSD2(I) -> TSD2(I - 2)
        Gamma_in = 1.225e-9 * E_in^5 * B(E2)_in  [eV]
     b. Inter-band wobbling E2 decay: TSD2(I) -> TSD1(I - 1)
        Gamma_wob = 1.225e-9 * E_wob^5 * B(E2)_wob  [eV]
     c. Tunneling decayout through deformation barrier into normal-deformed (ND) compound states:
        Gamma_decay_out = (D_TSD / 2*pi) * T_barrier(I)
        where T_barrier(I) = 1 / [ 1 + exp( 2*pi * (V_B(I) - Delta_E(I)) / (hbar * omega_barr) ) ].

3. Decayout Catastrophe & Wobbling Band Termination:
   At high spin (I > 25 hbar), Gamma_decay_out << Gamma_in + Gamma_wob, so the wobbling band
   maintains 100% in-TSD collective intensity.
   As spin drops towards I ~ 15 - 20 hbar, the excitation energy Delta_E(I) above ND states rises,
   the barrier thins, and Gamma_decay_out exponentially surges, dumping all TSD intensity into the
   ND ground-state well.
   The observable lower spin limit of the wobbling band is defined by the 50% decayout point:
     Gamma_decay_out(I_decay) ~ Gamma_in(I_decay) + Gamma_wob(I_decay).
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "163Lu_TSD2_wobbling_decayout": {
        "description": "163Lu TSD2 one-phonon wobbling band decayout (Odegard 2001, Amro 2003)",
        "nucleus": "163Lu",
        "deformation_params": {"epsilon2": 0.39, "gamma_deg": 19.5},
        "barrier_params": {"V_B_MeV": 1.85, "hbar_omega_barr_MeV": 0.42, "D_TSD_keV": 45.0},
        "transitions": [
            {"I": 39.5, "E_in_keV": 890.0, "E_wob_keV": 720.0, "Delta_E_ND_MeV": 1.10, "B_E2_in_W_u": 620.0, "B_E2_wob_W_u": 125.0},
            {"I": 35.5, "E_in_keV": 820.0, "E_wob_keV": 680.0, "Delta_E_ND_MeV": 1.25, "B_E2_in_W_u": 610.0, "B_E2_wob_W_u": 135.0},
            {"I": 31.5, "E_in_keV": 750.0, "E_wob_keV": 630.0, "Delta_E_ND_MeV": 1.40, "B_E2_in_W_u": 600.0, "B_E2_wob_W_u": 145.0},
            {"I": 27.5, "E_in_keV": 680.0, "E_wob_keV": 580.0, "Delta_E_ND_MeV": 1.55, "B_E2_in_W_u": 590.0, "B_E2_wob_W_u": 155.0},
            {"I": 23.5, "E_in_keV": 610.0, "E_wob_keV": 530.0, "Delta_E_ND_MeV": 1.70, "B_E2_in_W_u": 580.0, "B_E2_wob_W_u": 165.0},
            {"I": 19.5, "E_in_keV": 540.0, "E_wob_keV": 470.0, "Delta_E_ND_MeV": 1.82, "B_E2_in_W_u": 570.0, "B_E2_wob_W_u": 175.0},
            {"I": 15.5, "E_in_keV": 470.0, "E_wob_keV": 410.0, "Delta_E_ND_MeV": 1.95, "B_E2_in_W_u": 560.0, "B_E2_wob_W_u": 180.0}
        ]
    },
    "165Lu_TSD2_wobbling_decayout": {
        "description": "165Lu TSD2 wobbler with delayed decayout (Schonwasser 2003)",
        "nucleus": "165Lu",
        "deformation_params": {"epsilon2": 0.40, "gamma_deg": 20.0},
        "barrier_params": {"V_B_MeV": 1.95, "hbar_omega_barr_MeV": 0.40, "D_TSD_keV": 40.0},
        "transitions": [
            {"I": 37.5, "E_in_keV": 850.0, "E_wob_keV": 700.0, "Delta_E_ND_MeV": 1.15, "B_E2_in_W_u": 640.0, "B_E2_wob_W_u": 130.0},
            {"I": 33.5, "E_in_keV": 780.0, "E_wob_keV": 650.0, "Delta_E_ND_MeV": 1.30, "B_E2_in_W_u": 630.0, "B_E2_wob_W_u": 140.0},
            {"I": 29.5, "E_in_keV": 710.0, "E_wob_keV": 600.0, "Delta_E_ND_MeV": 1.45, "B_E2_in_W_u": 620.0, "B_E2_wob_W_u": 150.0},
            {"I": 25.5, "E_in_keV": 640.0, "E_wob_keV": 540.0, "Delta_E_ND_MeV": 1.62, "B_E2_in_W_u": 610.0, "B_E2_wob_W_u": 160.0},
            {"I": 21.5, "E_in_keV": 570.0, "E_wob_keV": 480.0, "Delta_E_ND_MeV": 1.78, "B_E2_in_W_u": 600.0, "B_E2_wob_W_u": 170.0},
            {"I": 17.5, "E_in_keV": 500.0, "E_wob_keV": 420.0, "Delta_E_ND_MeV": 1.92, "B_E2_in_W_u": 590.0, "B_E2_wob_W_u": 180.0}
        ]
    }
}


def calculate_transition_widths_and_tunneling(transitions, barrier_params):
    """
    Calculates partial decay widths (Gamma_in, Gamma_wob, Gamma_decay_out)
    and branching fractions for each spin state.
    """
    V_B = barrier_params["V_B_MeV"]
    hw_barr = barrier_params["hbar_omega_barr_MeV"]
    D_TSD_eV = barrier_params["D_TSD_keV"] * 1000.0

    results = []
    for t in transitions:
        I_val = t["I"]
        E_in_MeV = t["E_in_keV"] / 1000.0
        E_wob_MeV = t["E_wob_keV"] / 1000.0
        B_in_wu = t["B_E2_in_W_u"]
        B_wob_wu = t["B_E2_wob_W_u"]
        delta_E = t["Delta_E_ND_MeV"]

        # Standard E2 radiation width: Gamma(E2) = 1.225e-3 * E_MeV^5 * B(E2)_W.u. [eV]
        gamma_in_eV = 1.225e-3 * (E_in_MeV**5) * B_in_wu
        gamma_wob_eV = 1.225e-3 * (E_wob_MeV**5) * B_wob_wu
        gamma_tsd_eV = gamma_in_eV + gamma_wob_eV

        # Hill-Wheeler barrier penetration tunneling transmission
        exponent = 2.0 * math.pi * (V_B - delta_E) / hw_barr
        exp_clipped = np.clip(exponent, -50.0, 50.0)
        T_tunnel = 1.0 / (1.0 + math.exp(exp_clipped))
        gamma_decayout_eV = (D_TSD_eV / (2.0 * math.pi)) * T_tunnel

        gamma_tot_eV = gamma_tsd_eV + gamma_decayout_eV

        br_in = gamma_in_eV / max(1e-18, gamma_tot_eV)
        br_wob = gamma_wob_eV / max(1e-18, gamma_tot_eV)
        br_decayout = gamma_decayout_eV / max(1e-18, gamma_tot_eV)

        results.append({
            "I": I_val,
            "gamma_in_eV": float(gamma_in_eV),
            "gamma_wob_eV": float(gamma_wob_eV),
            "gamma_decayout_eV": float(gamma_decayout_eV),
            "gamma_total_eV": float(gamma_tot_eV),
            "branching_in": float(br_in),
            "branching_wob": float(br_wob),
            "branching_decayout": float(br_decayout),
            "transmission_T": float(T_tunnel)
        })

    return results


def evaluate_decayout_threshold(eval_transitions):
    """
    Finds the 50% decayout critical spin I_crit where decayout matches intra-TSD decay.
    """
    spins = [t["I"] for t in eval_transitions]
    br_decays = [t["branching_decayout"] for t in eval_transitions]

    I_50 = None
    for k in range(len(spins) - 1):
        if br_decays[k] <= 0.50 and br_decays[k+1] >= 0.50:
            # Linear interpolation for 50% crossing
            frac = (0.50 - br_decays[k]) / max(1e-6, br_decays[k+1] - br_decays[k])
            I_50 = spins[k] + frac * (spins[k+1] - spins[k])
            break

    if I_50 is None:
        I_50 = spins[-1] if br_decays[-1] >= 0.50 else spins[0]

    return {
        "critical_decayout_spin_I50": float(I_50),
        "max_wobbling_branching": float(max([t["branching_wob"] for t in eval_transitions])),
        "bandhead_retention_pct": float((1.0 - br_decays[-1]) * 100.0)
    }


def run_tsd_decayout_analysis(nucleus, deformation_params, barrier_params, transitions):
    """
    Complete execution pipeline for TSD wobbling decayout analysis.
    """
    eval_res = calculate_transition_widths_and_tunneling(transitions, barrier_params)
    threshold_res = evaluate_decayout_threshold(eval_res)
    return {
        "nucleus": nucleus,
        "deformation_params": deformation_params,
        "barrier_params": barrier_params,
        "evaluated_spins": eval_res,
        "decayout_threshold": threshold_res
    }


def format_text_report(res, title="TSD Wobbling Decayout & Tunneling Analyzer"):
    nuc = res["nucleus"]
    def_p = res["deformation_params"]
    barr_p = res["barrier_params"]
    th = res["decayout_threshold"]

    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Nucleus: {nuc} | Deformation: eps2 = {def_p['epsilon2']:.2f}, gamma = {def_p['gamma_deg']:.1f} deg | Barrier V_B = {barr_p['V_B_MeV']:.2f} MeV")
    lines.append("=" * 76)
    lines.append("Spin-Dependent Partial Widths and Branching Competition:")
    lines.append("  Spin I (hbar)   Gamma_in (eV)   Gamma_wob (eV)  Gamma_out (eV)   Br(in)   Br(wob)  Br(out)")
    for t in res["evaluated_spins"]:
        lines.append(f"    {t['I']:4.1f}          {t['gamma_in_eV']:9.3e}       {t['gamma_wob_eV']:9.3e}      {t['gamma_decayout_eV']:9.3e}     {t['branching_in']:5.3f}    {t['branching_wob']:5.3f}    {t['branching_decayout']:5.3f}")
    lines.append("-" * 76)
    lines.append("Decayout Catastrophe Diagnostics:")
    lines.append(f"  50% Decayout Threshold Spin I_50: {th['critical_decayout_spin_I50']:.1f} hbar (Wobbling band cutoff)")
    lines.append(f"  Peak Wobbling Branching Fraction: {th['max_wobbling_branching'] * 100.0:.1f}%")
    lines.append(f"  Bandhead In-TSD Retention       : {th['bandhead_retention_pct']:.1f}% (Remaining intensity entering ND states)")
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Triaxial Superdeformed (TSD) Wobbling Band Decayout Dynamics Analyzer."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load experimental preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        nucleus = p["nucleus"]
        def_p = p["deformation_params"]
        barr_p = p["barrier_params"]
        trans = p["transitions"]
        title = f"Preset: {args.preset} ({p['description']})"
    else:
        return parser.print_help()

    res = run_tsd_decayout_analysis(
        nucleus=nucleus,
        deformation_params=def_p,
        barrier_params=barr_p,
        transitions=trans
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
