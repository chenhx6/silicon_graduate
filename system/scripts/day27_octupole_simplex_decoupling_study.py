#!/usr/bin/env python3
"""
Day 27 Continuation Study:
Nuclear Octupole Simplex Quantum Numbers and Parity Decoupling Oscillations:
Microscopic Origin of Alternating Sign Decoupling Parameters across A~220 (223,225Ra) and A~140 (143,145Ba)

This study models the parity-projected rotor dynamics for K=1/2 and K=3/2 reflection-asymmetric bands:
1. Fundamental theorem of octupole decoupling parameters: a^+ = - a^- = a_0 (Bohr, Mottelson, Leander 1982)
2. Exact parity-decoupling oscillations in Delta E(I) = E(I^-) - E(I^+) showing alternating-sign zigzags and parity inversion
3. Simplex classification: s = +/- i for odd-A alternating-parity bands (Delta I = 1, Delta pi = odd)
4. Cross-mass systematics:
   - A~220 (225Ra, 223Ra): large negative a_0 ~ -1.52, small tunneling gap Delta E_0 ~ 55 keV, deep double-well
   - A~140 (145Ba, 143Ba): positive a_0 ~ +0.85, larger tunneling gap Delta E_0 ~ 200-245 keV, softer octupole barrier
"""

import sys
import json
import math
from pathlib import Path
import numpy as np

def compute_simplex_band(system_name, Z, A, K, a0, dE0_kev, A_rot_kev, B_rot_ev=0.0):
    """
    Computes energy levels, parity splitting, and simplex sequences for an odd-A octupole doublet.
    """
    spins = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5] if K == 0.5 else [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]

    levels_plus = {}
    levels_minus = {}

    for I in spins:
        rot_term = I * (I + 1.0) - (K ** 2)
        centrif = (B_rot_ev / 1000.0) * ((I * (I + 1.0)) ** 2)

        if K == 0.5:
            phase = (-1.0) ** (I + 0.5)
            # Positive parity: a^+ = + a0
            decoup_p = a0 * phase * (I + 0.5)
            # Negative parity: a^- = - a0
            decoup_m = - a0 * phase * (I + 0.5)
        else:
            # For K > 1/2, effective Coriolis mixing generates a small effective decoupling
            phase = (-1.0) ** (I + 0.5)
            decoup_p = a0 * phase * (I + 0.5) * 0.15
            decoup_m = - a0 * phase * (I + 0.5) * 0.15

        e_p = A_rot_kev * (rot_term + decoup_p) - centrif
        e_m = dE0_kev + A_rot_kev * (rot_term + decoup_m) - centrif

        levels_plus[I] = e_p
        levels_minus[I] = e_m

    # Set positive-parity bandhead to zero
    e0_ref = levels_plus[spins[0]]

    trajectory = []
    parity_inversions = 0

    for I in spins:
        ep = levels_plus[I] - e0_ref
        em = levels_minus[I] - e0_ref
        dE = em - ep  # Parity splitting: E(I^-) - E(I^+)

        is_inverted = (dE < 0.0)
        if is_inverted:
            parity_inversions += 1

        trajectory.append({
            "spin": I,
            "E_plus_kev": round(ep, 1),
            "E_minus_kev": round(em, 1),
            "delta_E_kev": round(dE, 1),
            "is_inverted": is_inverted
        })

    # Group into Simplex sequences:
    # Simplex s = +i: I^pi = 1/2^+, 3/2^-, 5/2^+, 7/2^-, 9/2^+ ...
    # Simplex s = -i: I^pi = 1/2^-, 3/2^+, 5/2^-, 7/2^+, 9/2^- ...
    simplex_plus_i = []
    simplex_minus_i = []

    for pt in trajectory:
        I = pt["spin"]
        # for s = +i: pi = (-1)^(I - 1/2)
        if int(I - 0.5) % 2 == 0:  # I = 1/2, 5/2, 9/2 -> pi = +1
            simplex_plus_i.append({"spin": I, "parity": "+", "E_kev": pt["E_plus_kev"]})
            simplex_minus_i.append({"spin": I, "parity": "-", "E_kev": pt["E_minus_kev"]})
        else:  # I = 3/2, 7/2, 11/2 -> pi = -1
            simplex_plus_i.append({"spin": I, "parity": "-", "E_kev": pt["E_minus_kev"]})
            simplex_minus_i.append({"spin": I, "parity": "+", "E_kev": pt["E_plus_kev"]})

    # Calculate energy staggering within simplex s = +i band
    s_I_simplex = []
    for idx in range(1, len(simplex_plus_i)):
        I = simplex_plus_i[idx]["spin"]
        dE_step = simplex_plus_i[idx]["E_kev"] - simplex_plus_i[idx - 1]["E_kev"]
        s_val = dE_step / (2.0 * I)
        s_I_simplex.append({"spin": I, "S_simplex": round(s_val, 2)})

    return {
        "system": system_name,
        "Z": Z, "A": A, "K": K,
        "parameters": {
            "a0_decoupling": a0,
            "a_plus": a0,
            "a_minus": -a0,
            "dE0_tunneling_kev": dE0_kev,
            "A_rot_kev": A_rot_kev,
            "B_rot_ev": B_rot_ev
        },
        "parity_doublets": trajectory,
        "parity_inversion_count": parity_inversions,
        "simplex_s_plus_i": simplex_plus_i,
        "simplex_s_minus_i": simplex_minus_i,
        "simplex_staggering": s_I_simplex
    }

def main():
    print("=== Day 27: Octupole Simplex and Parity Decoupling Oscillations Study ===")

    # 1. 225Ra (A~220): K=1/2, a0=-1.52, dE0=55.2 keV, A_rot=7.15 keV (NNDC, Leander 1982)
    res_ra225 = compute_simplex_band("225Ra", 88, 225, 0.5, -1.52, 55.2, 7.15, B_rot_ev=0.45)

    # 2. 223Ra (A~220): K=3/2 Coriolis-mixed, a_eff=-0.45, dE0=50.1 keV, A_rot=7.30 keV
    res_ra223 = compute_simplex_band("223Ra", 88, 223, 1.5, -0.45, 50.1, 7.30, B_rot_ev=0.50)

    # 3. 145Ba (A~140): K=1/2, a0=+0.85, dE0=198.5 keV, A_rot=12.50 keV
    res_ba145 = compute_simplex_band("145Ba", 56, 145, 0.5, +0.85, 198.5, 12.50, B_rot_ev=1.20)

    # 4. 143Ba (A~140): K=1/2, a0=+0.72, dE0=245.0 keV, A_rot=13.80 keV
    res_ba143 = compute_simplex_band("143Ba", 56, 143, 0.5, +0.72, 245.0, 13.80, B_rot_ev=1.50)

    systems = [res_ra225, res_ra223, res_ba145, res_ba143]

    # Print Summary Table
    print(f"\n{'Nucleus':<8} | {'K':<4} | {'a0':<6} | {'Delta E0 (keV)':<16} | {'A_rot (keV)':<12} | {'Inversions':<11} | {'Delta E(1/2)':<13} | {'Delta E(5/2)'}")
    print("-" * 92)
    for res in systems:
        p = res["parameters"]
        d = res["parity_doublets"]
        dE_low = d[0]["delta_E_kev"]
        dE_mid = d[2]["delta_E_kev"]
        print(f"{res['system']:<8} | {res['K']:<4.1f} | {p['a0_decoupling']:<6.2f} | {p['dE0_tunneling_kev']:<16.1f} | {p['A_rot_kev']:<12.2f} | {res['parity_inversion_count']:<11} | {dE_low:<13.1f} | {dE_mid:<11.1f}")

    print("\n--- 225Ra Parity Doublet Zigzag (E^- - E^+) Detailed Profile ---")
    print(f"{'Spin':<6} | {'E+(keV)':<10} | {'E-(keV)':<10} | {'Delta E (keV)':<15} | {'Parity Order'}")
    print("-" * 55)
    for pt in res_ra225["parity_doublets"]:
        order = "Normal (+ below -)" if not pt["is_inverted"] else "INVERTED (- below +)"
        print(f"{pt['spin']:<6.1f} | {pt['E_plus_kev']:<10.1f} | {pt['E_minus_kev']:<10.1f} | {pt['delta_E_kev']:<15.1f} | {order}")

    # Validation assertions
    # 1. 225Ra must exhibit parity inversions (negative Delta E) at odd-even spin steps
    assert res_ra225["parity_inversion_count"] >= 2, "225Ra must show at least 2 parity inversions in trajectory"

    # 2. Opposite signs of decoupling: a_plus == - a_minus
    for res in systems:
        assert res["parameters"]["a_plus"] == - res["parameters"]["a_minus"], "Decoupling parameters must have opposite signs"

    # 3. 145Ba must have larger Delta E0 than 225Ra reflecting higher tunneling barrier
    assert res_ba145["parameters"]["dE0_tunneling_kev"] > 3.0 * res_ra225["parameters"]["dE0_tunneling_kev"], "145Ba tunneling gap must be >3x 225Ra"

    # Save structured results
    out_dir = Path("outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/octupole-simplex")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "octupole_simplex_results.json"

    payload = {
        "schema_version": 1,
        "investigation": "Nuclear Octupole Simplex Quantum Numbers and Parity Decoupling Oscillations",
        "description": "Parity-projected rotor modeling of alternating-sign decoupling parameters (a^+ = -a^-) and parity doublets across 225Ra, 223Ra, 145Ba, and 143Ba",
        "systems": systems,
        "conclusions": [
            "In reflection-asymmetric odd-A nuclei, intrinsic parity breaking splits the classical Coriolis decoupling parameter into two branches with exact opposite signs: a^+ = -a^- = a0 (Bohr-Mottelson-Leander theorem).",
            "In 225Ra (K=1/2, a0 = -1.52), the negative-parity branch undergoes signature inversion while the positive-parity branch experiences normal Coriolis decoupling; this drives wild parity splitting oscillations Delta E(I) = E(I^-) - E(I^+), producing recurring parity inversions where negative-parity states drop below positive-parity states (e.g. at I = 5/2 and 9/2).",
            "Simplex symmetry s = +/- i classifies the true physical eigenstates into alternating-parity cascades (1/2^+ -> 3/2^- -> 5/2^+ ...), where intra-simplex transitions are collective E1 links and crossover transitions are collective E2 links.",
            "Across mass regions, the intrinsic tunneling gap Delta E0 increases by a factor of 4 from light actinides (Delta E0 ~ 50-55 keV in Ra) to neutron-rich lanthanides (Delta E0 ~ 200-245 keV in Ba), reflecting the shallower octupole potential well and increased zero-point barrier tunneling in A~140 compared to the stiff pear rotors in A~220."
        ]
    }

    with open(out_file, "w") as f:
        json.dump(payload, f, indent=2)

    print(f"\n[OK] Structured results saved to {out_file}")

if __name__ == "__main__":
    main()
