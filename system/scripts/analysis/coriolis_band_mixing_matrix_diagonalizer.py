#!/usr/bin/env python3
"""
coriolis_band_mixing_matrix_diagonalizer.py
===========================================
Odd-A Deformed Nuclei Multi-Band Coriolis Matrix Diagonalizer,
Signature Splitting / Inversion & Decoupling Parameter Engine.

Physics Formulation:
--------------------
1. Deformed Rotor-Particle Coupling Hamiltonian:
   Based on A. Bohr & B. R. Mottelson "Nuclear Structure" Vol. II §4-3 (pp. 158–175),
   卢希庭《原子核物理（修订版）》第 8 章 §8.6, and A. K. Kerman (1956):
   The total Hamiltonian for an odd nucleon coupled to a deformed core:
     H = H_0 + H_rot + H_Coriolis
   where rotational kinetic energy is:
     H_rot = A_rot * [ I(I+1) - K^2 ]  (with A_rot = hbar^2 / (2*J))
   and the Coriolis interaction is:
     H_Coriolis = -A_rot * [ I_+ * j_- + I_- * j_+ ]

2. Matrix Elements in the Deformed Strong-Coupling Basis |I, M, K, j>:
   - Diagonal matrix elements:
     <I, K | H | I, K> = eps_K + A_rot * [ I(I+1) - K^2 ]
                         + delta_{K, 1/2} * a * A_rot * (-1)^(I + 1/2) * (I + 1/2)
     where a is the decoupling parameter for the K = 1/2 band.
   - Off-diagonal Coriolis matrix elements (Delta K = +- 1):
     <I, K+1 | H | I, K> = -A_rot * sqrt( (I - K) * (I + K + 1) ) * <K+1 | j_+ | K>
   For single-j shell approximation:
     <K+1 | j_+ | K> = sqrt( j(j+1) - K(K+1) ).

3. Tridiagonal Hamiltonian Diagonalization:
   For each total spin I, a basis of allowed K-components (K <= I) is constructed.
   Exact algebraic diagonalization yields perturbed eigenenergies E_i(I)
   and mixed wavefunctions:
     |Psi_i(I)> = sum_K c_{i, K}(I) |I, K>.

4. Signature Staggering Parameter S(I):
   S(I) = [ E(I) - E(I-1) ] / (2*I)
   Coriolis band mixing produces characteristic signature staggering between
   favored (alpha_f) and unfavored (alpha_u) signature branches.
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "159Dy_neutron_i13_2": {
        "description": "159Dy neutron i13/2 band mixing (K = 1/2+, 3/2+, 5/2+, 7/2+)",
        "nucleus": "159Dy",
        "A_mass": 159,
        "A_rot_keV": 12.0,
        "j_valence": 6.5,
        "a_decouple": 0.85,
        "K_values": [0.5, 1.5, 2.5, 3.5],
        "eps_keV": [0.0, 180.0, 390.0, 680.0],
        "spins": [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]
    },
    "135Pr_proton_h11_2": {
        "description": "135Pr proton h11/2 band mixing (K = 1/2-, 3/2-, 5/2-)",
        "nucleus": "135Pr",
        "A_mass": 135,
        "A_rot_keV": 14.5,
        "j_valence": 5.5,
        "a_decouple": -3.20,
        "K_values": [0.5, 1.5, 2.5],
        "eps_keV": [0.0, 150.0, 380.0],
        "spins": [2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5]
    },
    "169Tm_proton_1_2plus": {
        "description": "169Tm proton 1/2+[411] decoupling & Coriolis mixing (K=1/2, 3/2)",
        "nucleus": "169Tm",
        "A_mass": 169,
        "A_rot_keV": 12.4,
        "j_valence": 2.5,
        "a_decouple": -0.77,
        "K_values": [0.5, 1.5],
        "eps_keV": [0.0, 330.0],
        "spins": [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
    }
}


def construct_coriolis_matrix(I_spin, K_list, eps_list, A_rot_keV, j_val, a_decouple=0.0):
    """
    Constructs the Coriolis Hamiltonian matrix in the basis of K <= I.
    """
    basis = []
    for idx, k in enumerate(K_list):
        if k <= I_spin:
            basis.append((idx, k, eps_list[idx]))

    dim = len(basis)
    if dim == 0:
        return np.zeros((0, 0)), []

    H = np.zeros((dim, dim))
    for i in range(dim):
        idx_orig, K, eps_k = basis[i]
        # Diagonal term
        diag = eps_k + A_rot_keV * (I_spin * (I_spin + 1.0) - K**2)
        if abs(K - 0.5) < 1e-4:
            phase = (-1.0)**int(round(I_spin + 0.5))
            diag += a_decouple * A_rot_keV * phase * (I_spin + 0.5)
        H[i, i] = diag

        # Off-diagonal Coriolis term to K+1
        if i + 1 < dim:
            idx_next, K_next, _ = basis[i + 1]
            if abs(K_next - (K + 1.0)) < 1e-4:
                # Matrix element of j_+
                j_plus_sq = j_val * (j_val + 1.0) - K * (K + 1.0)
                if j_plus_sq > 0:
                    j_plus = math.sqrt(j_plus_sq)
                    me = -A_rot_keV * math.sqrt((I_spin - K) * (I_spin + K + 1.0)) * j_plus
                    H[i, i + 1] = me
                    H[i + 1, i] = me

    return H, basis


def diagonalize_coriolis_mixing(I_list, K_list, eps_list, A_rot_keV, j_val, a_decouple=0.0):
    """
    Diagonalizes the Coriolis matrix for a sequence of spins I.
    """
    level_results = []
    for I in I_list:
        H, basis = construct_coriolis_matrix(I, K_list, eps_list, A_rot_keV, j_val, a_decouple)
        if len(basis) == 0:
            continue
        evals, evecs = np.linalg.eigh(H)
        # Lowest bandhead eigenstate
        e_yrast = float(evals[0])
        wavefn = {f"K={basis[m][1]:.1f}": float(evecs[m, 0]) for m in range(len(basis))}

        # All eigenvalues
        all_evals = [float(ev) for ev in evals]

        level_results.append({
            "spin_I": float(I),
            "E_yrast_keV": e_yrast,
            "all_eigenvalues_keV": all_evals,
            "wavefunction_amplitudes": wavefn
        })

    # Calculate staggering parameter S(I) = [E(I) - E(I-1)] / (2*I)
    for i in range(1, len(level_results)):
        I_curr = level_results[i]["spin_I"]
        dE = level_results[i]["E_yrast_keV"] - level_results[i - 1]["E_yrast_keV"]
        S_val = dE / (2.0 * I_curr)
        level_results[i]["staggering_S_keV"] = float(S_val)

    return level_results


def run_coriolis_analysis(A_mass, spins, K_values, eps_keV, A_rot_keV, j_val, a_decouple=0.0):
    """
    Complete execution pipeline for Coriolis band mixing.
    """
    levels = diagonalize_coriolis_mixing(spins, K_values, eps_keV, A_rot_keV, j_val, a_decouple)
    # Ground state normalization (shift lowest to 0.0)
    if levels:
        min_E = min([lv["E_yrast_keV"] for lv in levels])
        for lv in levels:
            lv["E_excitation_keV"] = float(lv["E_yrast_keV"] - min_E)

    return {
        "A_mass": A_mass,
        "A_rot_keV": float(A_rot_keV),
        "j_valence": float(j_val),
        "decoupling_parameter_a": float(a_decouple),
        "K_channels": [float(k) for k in K_values],
        "levels": levels
    }


def format_text_report(res, title="Coriolis Band Mixing & Signature Splitting Engine"):
    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Nucleus: A = {res['A_mass']}, Rotational Const A_rot = {res['A_rot_keV']:.2f} keV, j = {res['j_valence']:.1f}, Decoupling a = {res['decoupling_parameter_a']:+.2f}")
    lines.append("=" * 76)
    lines.append("Energy Levels & Wavefunction Amplitudes |Psi(I)> = sum c_K |I, K>:")
    lines.append("   Spin I     E_yrast (keV)   E_ex (keV)   S(I) (keV)   Dominant Wavefunction Amplitudes")
    for lv in res["levels"]:
        s_str = f"{lv.get('staggering_S_keV', 0.0):8.2f}" if "staggering_S_keV" in lv else "       -"
        wf_parts = [f"{k}:{v:+.3f}" for k, v in lv["wavefunction_amplitudes"].items()]
        wf_str = ", ".join(wf_parts)
        lines.append(
            f"    {lv['spin_I']:4.1f}      {lv['E_yrast_keV']:10.1f}   {lv['E_excitation_keV']:10.1f}   {s_str}   {wf_str}"
        )
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Odd-A Deformed Nuclei Coriolis Band Mixing & Signature Splitting Diagonalizer."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load experimental preset")
    parser.add_argument("--mass-a", type=int, help="Mass number A")
    parser.add_argument("--arot", type=float, default=13.0, help="Rotational parameter hbar^2/(2*J) in keV")
    parser.add_argument("--jval", type=float, default=5.5, help="Valence orbital angular momentum j")
    parser.add_argument("--adecouple", type=float, default=0.0, help="K=1/2 decoupling parameter a")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        A_mass = p["A_mass"]
        spins = p["spins"]
        K_values = p["K_values"]
        eps_keV = p["eps_keV"]
        A_rot_keV = p["A_rot_keV"]
        j_val = p["j_valence"]
        a_decouple = p["a_decouple"]
        title = f"Preset: {args.preset} ({p['description']})"
    elif args.mass_a:
        A_mass = args.mass_a
        spins = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
        K_values = [0.5, 1.5, 2.5]
        eps_keV = [0.0, 160.0, 380.0]
        A_rot_keV = args.arot
        j_val = args.jval
        a_decouple = args.adecouple
        title = "Custom User Input"
    else:
        return parser.print_help()

    res = run_coriolis_analysis(
        A_mass=A_mass,
        spins=spins,
        K_values=K_values,
        eps_keV=eps_keV,
        A_rot_keV=A_rot_keV,
        j_val=j_val,
        a_decouple=a_decouple
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
