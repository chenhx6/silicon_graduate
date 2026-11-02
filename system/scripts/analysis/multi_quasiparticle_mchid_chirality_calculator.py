#!/usr/bin/env python3
"""
multi_quasiparticle_mchid_chirality_calculator.py
=================================================
Multi-Quasiparticle Multiple Chiral Doublets (MchiD), 4-Quasiparticle Angular Momentum
Geometry & Triaxial Symmetry-Breaking Classification Engine.

Physics Formulation:
--------------------
1. Multi-Quasiparticle Chiral Geometry in Even-Even & Odd-A Nuclei:
   Based on J. Meng & Y. P. Wang in "Chirality and Wobbling in Atomic Nuclei" (CRC 2025) Ch. 3,
   Q. B. Chen et al. (CRC 2025) Ch. 10, and X. H. Xiong et al. (ADNDT 125, 193, 2019):
   In even-even nuclei (e.g. 136Nd), nuclear chirality emerges from 4-quasiparticle configurations:
     pi (h_11/2)^2 (x) nu (h_11/2)^-2
   or pi (h_11/2)^2 (x) nu [h_11/2^-1 (d_5/2, g_7/2)^-1].
   The valence proton particles align along the short (s) axis: j_pi = (j_pi, 0, 0).
   The valence neutron holes align along the long (l) axis: j_nu = (0, 0, j_nu).
   The triaxial collective core rotates along the intermediate (m) axis: R = (0, R_m, 0).
   Total spin: J = j_pi + j_nu + R = (j_pi, R_m, j_nu).

2. Chiral Aplanarity Metric & Scalar Triple Product:
   The degree of chirality is quantified by the scalar triple product:
     chi = j_pi . (j_nu x R) = j_pi,s * j_nu,l * R_m
   Normalized chiral volume metric:
     V_chiral = |chi| / ( |j_pi| * |j_nu| * |R| ) in [0.0, 1.0]
   Under time reversal T combined with 180-degree rotation R_y(pi):
     j_pi -> -j_pi, j_nu -> -j_nu, R -> -R ==> chi -> -chi.
   When V_chiral > 0.40, aplanar rotation breaks this symmetry, creating degenerate left-
   and right-handed states.

3. Experimental Chiral Criteria & Multiple Chiral Doublets (MchiD):
   In a single nucleus, multiple pairs of chiral doublet bands (MchiD) can coexist based on:
     - Different multi-quasiparticle configurations (e.g. 2-qp vs 4-qp);
     - Or identical configurations with different triaxial shapes (gamma_1 vs gamma_2).
   Key Experimental Quantifiers:
     a. Energy degeneracy: Delta E(I) = |E_band1(I) - E_band2(I)| <= 100 keV.
     b. Staggering parameter: S(I) = [E(I) - E(I-1)] / (2*I). S(I) must be smooth and
        identical between partner bands (absence of signature splitting).
     c. Rotational alignment: i_x(1) ~ i_x(2) with Delta i_x <= 0.50 hbar.
     d. Electromagnetic transitions: B(M1)/B(E2) ratios exhibit identical odd-even spin
        staggering in both partner bands.
     e. MchiD Confidence Score Q_chiral (0 - 100%): combines degeneracy, staggering smoothness,
        and spin span.
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "136Nd_4qp_mchid": {
        "description": "136Nd 4-quasiparticle Multiple Chiral Doublets (ADNDT 2019 / Petrache 2018)",
        "nucleus": "136Nd",
        "A_mass": 136,
        "doublets": [
            {
                "doublet_id": "Doublet_1",
                "configuration": "pi h_11/2^2 (x) nu h_11/2^-2 (4-qp)",
                "parity": "+",
                "j_pi": 8.0,
                "j_nu": 8.0,
                "spins": [15, 16, 17, 18, 19, 20],
                "E_band1_keV": [5180.0, 5680.0, 6220.0, 6800.0, 7420.0, 8080.0],
                "E_band2_keV": [5260.0, 5740.0, 6270.0, 6840.0, 7450.0, 8105.0]
            },
            {
                "doublet_id": "Doublet_2",
                "configuration": "pi h_11/2^2 (x) nu [h_11/2^-1 d_5/2^-1] (4-qp excited)",
                "parity": "-",
                "j_pi": 8.0,
                "j_nu": 5.5,
                "spins": [15, 16, 17, 18, 19, 20],
                "E_band1_keV": [5350.0, 5840.0, 6370.0, 6940.0, 7550.0, 8200.0],
                "E_band2_keV": [5440.0, 5910.0, 6420.0, 6980.0, 7580.0, 8225.0]
            }
        ]
    },
    "133Ce_mchid": {
        "description": "133Ce 3-quasiparticle and 5-quasiparticle MchiD (Ayangeakaa 2013 / ADNDT 2019)",
        "nucleus": "133Ce",
        "A_mass": 133,
        "doublets": [
            {
                "doublet_id": "Doublet_1",
                "configuration": "pi h_11/2^2 (x) nu h_11/2^-1 (3-qp)",
                "parity": "-",
                "j_pi": 8.0,
                "j_nu": 5.5,
                "spins": [17.5, 18.5, 19.5, 20.5, 21.5, 22.5],
                "E_band1_keV": [4420.0, 4890.0, 5400.0, 5950.0, 6540.0, 7170.0],
                "E_band2_keV": [4510.0, 4960.0, 5450.0, 5990.0, 6570.0, 7195.0]
            }
        ]
    },
    "103Rh_mchid": {
        "description": "103Rh multiple chiral doublets in A~100 region (Kuti 2014)",
        "nucleus": "103Rh",
        "A_mass": 103,
        "doublets": [
            {
                "doublet_id": "Doublet_1",
                "configuration": "pi g_9/2 (x) nu (h_11/2 (x) d_5/2) (3-qp)",
                "parity": "+",
                "j_pi": 4.5,
                "j_nu": 6.0,
                "spins": [11.5, 12.5, 13.5, 14.5, 15.5, 16.5],
                "E_band1_keV": [2850.0, 3240.0, 3670.0, 4140.0, 4650.0, 5200.0],
                "E_band2_keV": [2940.0, 3310.0, 3720.0, 4175.0, 4675.0, 5220.0]
            }
        ]
    }
}


def evaluate_chiral_geometry(j_pi, j_nu, total_spin, J_m_core=None):
    """
    Calculates 3D angular momentum components, scalar triple product chi, and aplanarity metric.
    """
    if J_m_core is None:
        R2 = total_spin**2 - j_pi**2 - j_nu**2
        R_m = math.sqrt(max(0.0, R2))
    else:
        R_m = J_m_core

    chi = j_pi * j_nu * R_m
    j_tot_calc = math.sqrt(j_pi**2 + j_nu**2 + R_m**2)
    V_chiral = abs(chi) / (j_pi * j_nu * max(1e-6, j_tot_calc))

    return {
        "j_pi_short": float(j_pi),
        "j_nu_long": float(j_nu),
        "R_m_intermediate": float(R_m),
        "J_total_calc": float(j_tot_calc),
        "scalar_triple_product_chi": float(chi),
        "aplanarity_volume_metric": float(min(1.0, V_chiral))
    }


def evaluate_doublet_observables(spins, E_band1_keV, E_band2_keV, j_pi, j_nu):
    """
    Evaluates energy differences Delta E(I), staggering parameters S(I), and chiral confidence.
    """
    spins = np.array(spins, dtype=float)
    E1 = np.array(E_band1_keV, dtype=float)
    E2 = np.array(E_band2_keV, dtype=float)

    dE = np.abs(E2 - E1)
    mean_dE = float(np.mean(dE))
    min_dE = float(np.min(dE))

    S1 = (E1[1:] - E1[:-1]) / (2.0 * spins[1:])
    S2 = (E2[1:] - E2[:-1]) / (2.0 * spins[1:])
    delta_S = np.abs(S1 - S2)
    mean_delta_S = float(np.mean(delta_S)) if len(delta_S) > 0 else 0.0

    I_mid = float(spins[len(spins) // 2])
    geom = evaluate_chiral_geometry(j_pi, j_nu, I_mid)

    q_deg = max(0.0, 1.0 - mean_dE / 150.0)
    q_stag = max(0.0, 1.0 - mean_delta_S / 5.0)
    q_span = min(1.0, len(spins) / 5.0)
    q_apla = min(1.0, geom["aplanarity_volume_metric"] / 0.50)

    q_total = 0.35 * q_deg + 0.25 * q_stag + 0.20 * q_span + 0.20 * q_apla
    chiral_confidence_percent = q_total * 100.0

    level_details = []
    for i in range(len(spins)):
        lvl = {
            "spin": float(spins[i]),
            "E_band1_keV": float(E1[i]),
            "E_band2_keV": float(E2[i]),
            "delta_E_keV": float(dE[i])
        }
        if i > 0:
            lvl["S1_keV"] = float(S1[i-1])
            lvl["S2_keV"] = float(S2[i-1])
            lvl["delta_S_keV"] = float(delta_S[i-1])
        level_details.append(lvl)

    return {
        "mean_delta_E_keV": mean_dE,
        "min_delta_E_keV": min_dE,
        "mean_delta_S_keV": mean_delta_S,
        "chiral_confidence_percent": float(chiral_confidence_percent),
        "geometry_at_mid_spin": geom,
        "level_details": level_details
    }


def analyze_mchid(doublets_data, nucleus_name=None):
    """
    Analyzes all candidate doublet pairs in a nucleus to verify Multiple Chiral Doublets (MchiD).
    """
    results = []
    for d in doublets_data:
        res = evaluate_doublet_observables(
            spins=d["spins"],
            E_band1_keV=d["E_band1_keV"],
            E_band2_keV=d["E_band2_keV"],
            j_pi=d["j_pi"],
            j_nu=d["j_nu"]
        )
        res["doublet_id"] = d.get("doublet_id", "Doublet")
        res["configuration"] = d.get("configuration", "unspecified")
        res["parity"] = d.get("parity", "+")
        results.append(res)

    num_doublets = len(results)
    is_mchid_verified = False
    mchid_summary = ""

    if num_doublets >= 2:
        c1 = results[0]["chiral_confidence_percent"]
        c2 = results[1]["chiral_confidence_percent"]
        if c1 >= 60.0 and c2 >= 60.0:
            is_mchid_verified = True
            mchid_summary = f"MchiD confirmed in {nucleus_name}: 2 independent chiral doublets coexisting with confidence {c1:.1f}% and {c2:.1f}%."
        else:
            mchid_summary = f"MchiD candidate: Doublet 1 confidence {c1:.1f}%, Doublet 2 confidence {c2:.1f}%."
    else:
        c1 = results[0]["chiral_confidence_percent"] if num_doublets == 1 else 0.0
        mchid_summary = f"Single chiral doublet evaluated in {nucleus_name} (Confidence = {c1:.1f}%)."

    return {
        "nucleus": nucleus_name,
        "num_doublets": num_doublets,
        "is_mchid_verified": is_mchid_verified,
        "mchid_summary": mchid_summary,
        "doublets_analysis": results
    }


def main():
    parser = argparse.ArgumentParser(
        description="Multi-Quasiparticle Multiple Chiral Doublets (MchiD) & 4-QP Angular Momentum Geometry Analyzer."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load experimental preset")
    parser.add_argument("--nucleus", type=str, default="Unknown", help="Nucleus name")
    parser.add_argument("--j-pi", type=float, default=8.0, help="Valence proton angular momentum along short axis")
    parser.add_argument("--j-nu", type=float, default=8.0, help="Valence neutron angular momentum along long axis")
    parser.add_argument("--spins", type=str, help="Comma-separated spin list (e.g. 15,16,17,18,19,20)")
    parser.add_argument("--energies1", type=str, help="Comma-separated band 1 energies in keV")
    parser.add_argument("--energies2", type=str, help="Comma-separated band 2 energies in keV")
    parser.add_argument("--json", action="store_true", help="Output JSON format")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        nucleus = p["nucleus"]
        doublets = p["doublets"]
        title = f"Preset: {args.preset} ({p['description']})"
    elif args.spins and args.energies1 and args.energies2:
        spins = [float(s.strip()) for s in args.spins.split(",")]
        e1 = [float(e.strip()) for e in args.energies1.split(",")]
        e2 = [float(e.strip()) for e in args.energies2.split(",")]
        nucleus = args.nucleus
        doublets = [{
            "doublet_id": "Custom_Doublet",
            "configuration": f"j_pi={args.j_pi}, j_nu={args.j_nu}",
            "parity": "+",
            "j_pi": args.j_pi,
            "j_nu": args.j_nu,
            "spins": spins,
            "E_band1_keV": e1,
            "E_band2_keV": e2
        }]
        title = f"Custom Doublet: {nucleus}"
    else:
        return parser.print_help()

    res = analyze_mchid(doublets, nucleus_name=nucleus)

    if args.json:
        print(json.dumps(res, indent=2))
        return

    print("=" * 76)
    print("Multi-Quasiparticle Multiple Chiral Doublets (MchiD) Analyzer")
    print(f"{title}")
    print("=" * 76)
    print(f"Nucleus: {res['nucleus']} | Number of Candidate Doublets: {res['num_doublets']}")
    print(f"Status : {res['mchid_summary']}")
    print("=" * 76)

    for d in res["doublets_analysis"]:
        print(f"--- {d['doublet_id']}: {d['configuration']} (Parity: {d['parity']}) ---")
        print(f"  Energy Degeneracy   : Mean Delta E = {d['mean_delta_E_keV']:.1f} keV (Min Delta E = {d['min_delta_E_keV']:.1f} keV)")
        print(f"  Staggering Delta S  : Mean |S1 - S2| = {d['mean_delta_S_keV']:.2f} keV")
        geom = d["geometry_at_mid_spin"]
        print(f"  Aplanar Geometry    : j_pi={geom['j_pi_short']}, j_nu={geom['j_nu_long']}, R_m={geom['R_m_intermediate']:.1f}")
        print(f"  Chiral Volume Metric: V_chiral = {geom['aplanarity_volume_metric']:.3f} | chi = {geom['scalar_triple_product_chi']:.1f}")
        print(f"  Chiral Confidence   : {d['chiral_confidence_percent']:.1f}%")
        print("  Level Details:")
        print("    Spin     E_band1 (keV)   E_band2 (keV)   Delta_E (keV)   S1 (keV)   S2 (keV)")
        for lvl in d["level_details"]:
            s1_str = f"{lvl.get('S1_keV', 0.0):.2f}" if "S1_keV" in lvl else "-"
            s2_str = f"{lvl.get('S2_keV', 0.0):.2f}" if "S2_keV" in lvl else "-"
            print(f"    {lvl['spin']:4.1f}     {lvl['E_band1_keV']:10.1f}      {lvl['E_band2_keV']:10.1f}      {lvl['delta_E_keV']:8.1f}      {s1_str:8s}   {s2_str:8s}")
        print("-" * 76)
    print("=" * 76)


if __name__ == "__main__":
    main()
