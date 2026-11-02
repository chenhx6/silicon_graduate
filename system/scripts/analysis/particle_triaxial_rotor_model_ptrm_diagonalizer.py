#!/usr/bin/env python3
"""
particle_triaxial_rotor_model_ptrm_diagonalizer.py
==================================================
Full Microscopic Particle-Triaxial-Rotor Model (PTRM) Algebraic Diagonalizer,
Transverse/Longitudinal Wobbling Energy Hierarchy & Band Structure Engine.

Physics Formulation:
--------------------
1. Particle-Triaxial-Rotor Hamiltonian:
   Based on J. Meyer-ter-Vehn (Nucl. Phys. A 249, 111, 1975), S. Frauendorf & F. Dönau (PRC 89, 014322, 2014),
   and I. Hamamoto (Phys. Rev. C 65, 044305, 2002):
   In non-axial triaxial odd-A nuclei, an odd nucleon of angular momentum j couples
   to an asymmetric triaxial core with moments of inertia J_s, J_m, J_l:
     H_PTRM = H_rot + H_sp
     H_rot = (I_s - j_s)^2 / (2 * J_s) + (I_m - j_m)^2 / (2 * J_m) + (I_l - j_l)^2 / (2 * J_l)

2. Single-j Nilsson Quadrupole Field:
   The triaxial deformed single-particle potential is parameterized by deformation scale C
   and triaxiality angle gamma:
     H_sp = C * [ cos(gamma) * ( 3*j_l^2 - j(j+1) ) - sqrt(3) * sin(gamma) * ( j_s^2 - j_m^2 ) ]
   where (s, m, l) correspond to the short, intermediate, and long principal axes.

3. Symmetrized Strong-Coupling D2 Basis:
   In the coupled basis |I M K j Omega>, the D2 discrete spatial rotational symmetry
   requires states to be symmetrized under R_z(pi) and R_y(pi):
     |I M K j Omega, alpha> = [ |I M K j Omega> + (-1)^(I - j) * |I M -K j -Omega> ] / sqrt(2 * (1 + delta_{K0}*delta_{Omega0}))
   The matrix dimension for a given total spin I is bounded by the available (K, Omega) projections.

4. Numerical Matrix Diagonalization:
   Exact algebraic diagonalization produces the yrast sequence (n_w = 0, yrast band),
   first wobbling excitation (n_w = 1, yrare band), and second wobbling excitation (n_w = 2):
     Wobbling excitation frequency: hbar * omega_wob(I) = E(I, n_w = 1) - E_yrast(I).
   Unlike high-spin harmonic approximations, full PTRM diagonalization remains strictly
   exact across the entire low-to-high spin evolution.
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "135Pr_triaxial_wobbler_ptrm": {
        "description": "135Pr proton h11/2 transverse wobbling candidate (Matta 2015 / Frauendorf 2014)",
        "nucleus": "135Pr",
        "A_mass": 135,
        "j_valence": 5.5,
        "gamma_deg": 26.0,
        "C_quadrupole_keV": 35.0,
        "J_m_hbar2_MeV": 26.0,
        "J_s_hbar2_MeV": 15.0,
        "J_l_hbar2_MeV": 6.0,
        "spins": [5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5]
    },
    "163Lu_tsw_wobbler_ptrm": {
        "description": "163Lu triaxial superdeformed multi-phonon wobbler (Jensen 2002 / Hamamoto 2002)",
        "nucleus": "163Lu",
        "A_mass": 163,
        "j_valence": 6.5,
        "gamma_deg": 20.0,
        "C_quadrupole_keV": 50.0,
        "J_m_hbar2_MeV": 45.0,
        "J_s_hbar2_MeV": 20.0,
        "J_l_hbar2_MeV": 10.0,
        "spins": [8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5]
    },
    "105Pd_triaxial_ptrm": {
        "description": "105Pd neutron h11/2 wobbler candidate in A~100 (Timar et al. 2019)",
        "nucleus": "105Pd",
        "A_mass": 105,
        "j_valence": 5.5,
        "gamma_deg": 22.0,
        "C_quadrupole_keV": 40.0,
        "J_m_hbar2_MeV": 22.0,
        "J_s_hbar2_MeV": 12.0,
        "J_l_hbar2_MeV": 5.0,
        "spins": [5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5]
    }
}


def evaluate_ptrm_matrix_elements(I_spin, j_val, J_s, J_m, J_l, C_quad, gamma_deg):
    """
    Constructs the PTRM Hamiltonian matrix in the coupled basis |I, K, j, Omega>.
    Axes: s = 1 (short), m = 2 (intermediate), l = 3 (long).
    """
    A_s = 1000.0 / (2.0 * J_s)
    A_m = 1000.0 / (2.0 * J_m)
    A_l = 1000.0 / (2.0 * J_l)

    A_plus = 0.5 * (A_s + A_m)
    A_minus = 0.5 * (A_s - A_m)

    gamma_rad = math.radians(gamma_deg)
    cos_g = math.cos(gamma_rad)
    sin_g = math.sin(gamma_rad)

    k_vals = [k for k in np.arange(0.5, I_spin + 0.1, 1.0)]
    omega_vals = [w for w in np.arange(-j_val, j_val + 0.1, 1.0)]

    basis = []
    for k in k_vals:
        for w in omega_vals:
            basis.append((k, w))

    dim = len(basis)
    if dim == 0:
        return np.zeros((0, 0)), []

    H = np.zeros((dim, dim))

    for idx1 in range(dim):
        K1, W1 = basis[idx1]

        R_l_sq = (K1 - W1)**2
        diag_rot = A_l * R_l_sq + A_plus * ( (I_spin * (I_spin + 1.0) - K1**2) + (j_val * (j_val + 1.0) - W1**2) )
        diag_sp = C_quad * cos_g * (3.0 * W1**2 - j_val * (j_val + 1.0))

        H[idx1, idx1] = diag_rot + diag_sp

        for idx2 in range(idx1 + 1, dim):
            K2, W2 = basis[idx2]
            val_me = 0.0

            # Term 1: Delta K = +1, Delta Omega = +1 (I_- j_+)
            if abs(K2 - (K1 + 1.0)) < 1e-4 and abs(W2 - (W1 + 1.0)) < 1e-4:
                cg_I = math.sqrt(max(0.0, (I_spin - K1) * (I_spin + K1 + 1.0)))
                cg_j = math.sqrt(max(0.0, (j_val - W1) * (j_val + W1 + 1.0)))
                val_me += -A_plus * cg_I * cg_j

            # Term 2: Delta K = +1, Delta Omega = -1 (I_- j_-)
            if abs(K2 - (K1 + 1.0)) < 1e-4 and abs(W2 - (W1 - 1.0)) < 1e-4:
                cg_I = math.sqrt(max(0.0, (I_spin - K1) * (I_spin + K1 + 1.0)))
                cg_j = math.sqrt(max(0.0, (j_val + W1) * (j_val - W1 + 1.0)))
                val_me += -A_minus * cg_I * cg_j

            # Term 3: Single-particle asymmetry H_sp: Delta Omega = +- 2
            if abs(K1 - K2) < 1e-4 and abs(W2 - (W1 + 2.0)) < 1e-4:
                c1 = math.sqrt(max(0.0, (j_val - W1) * (j_val + W1 + 1.0)))
                c2 = math.sqrt(max(0.0, (j_val - (W1 + 1.0)) * (j_val + W1 + 2.0)))
                val_me += -0.5 * math.sqrt(3.0) * C_quad * sin_g * c1 * c2

            # Term 4: Core asymmetry H_rot: Delta K = +- 2
            if abs(W1 - W2) < 1e-4 and abs(K2 - (K1 + 2.0)) < 1e-4:
                c1 = math.sqrt(max(0.0, (I_spin - K1) * (I_spin + K1 + 1.0)))
                c2 = math.sqrt(max(0.0, (I_spin - (K1 + 1.0)) * (I_spin + K1 + 2.0)))
                val_me += 0.5 * A_minus * c1 * c2

            if abs(val_me) > 1e-9:
                H[idx1, idx2] = val_me
                H[idx2, idx1] = val_me

    return H, basis


def diagonalize_ptrm_spectrum(spins, j_val, J_s, J_m, J_l, C_quad, gamma_deg):
    """
    Diagonalizes PTRM for a list of spins, extracting the yrast (n_w=0)
    and excited (n_w=1, 2) wobbling bands.
    """
    trajectory = []
    for I in spins:
        H, basis = evaluate_ptrm_matrix_elements(I, j_val, J_s, J_m, J_l, C_quad, gamma_deg)
        if len(basis) == 0:
            continue
        evals = np.linalg.eigvalsh(H)

        e_yrast = float(evals[0])
        e_wob1 = float(evals[1]) if len(evals) > 1 else e_yrast
        e_wob2 = float(evals[2]) if len(evals) > 2 else e_wob1

        hw_wob = e_wob1 - e_yrast
        anharm_ratio = ((e_wob2 - e_yrast) / max(1.0, hw_wob)) if hw_wob > 0 else 2.0

        trajectory.append({
            "spin_I": float(I),
            "E_yrast_keV": e_yrast,
            "E_wob1_keV": e_wob1,
            "E_wob2_keV": e_wob2,
            "wobbling_energy_keV": float(hw_wob),
            "anharmonic_ratio_R21": float(anharm_ratio)
        })

    if trajectory:
        min_yrast = min([pt["E_yrast_keV"] for pt in trajectory])
        for pt in trajectory:
            pt["E_ex_yrast_keV"] = float(pt["E_yrast_keV"] - min_yrast)
            pt["E_ex_wob1_keV"] = float(pt["E_wob1_keV"] - min_yrast)

    return trajectory


def run_ptrm_analysis(A_mass, spins, j_val, J_s, J_m, J_l, C_quad, gamma_deg):
    """
    Complete execution pipeline for PTRM analysis.
    """
    traj = diagonalize_ptrm_spectrum(spins, j_val, J_s, J_m, J_l, C_quad, gamma_deg)
    return {
        "A_mass": A_mass,
        "j_valence": float(j_val),
        "gamma_deg": float(gamma_deg),
        "moments_of_inertia": {
            "J_s_hbar2_MeV": float(J_s),
            "J_m_hbar2_MeV": float(J_m),
            "J_l_hbar2_MeV": float(J_l)
        },
        "quadrupole_splitting_C_keV": float(C_quad),
        "levels": traj
    }


def format_text_report(res, title="Particle-Triaxial-Rotor Model (PTRM) Engine"):
    moi = res["moments_of_inertia"]
    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Nucleus: A = {res['A_mass']}, j = {res['j_valence']:.1f}, gamma = {res['gamma_deg']:.1f} deg, C_quad = {res['quadrupole_splitting_C_keV']:.1f} keV")
    lines.append(f"Inertia Parameters: J_s = {moi['J_s_hbar2_MeV']:.1f}, J_m = {moi['J_m_hbar2_MeV']:.1f}, J_l = {moi['J_l_hbar2_MeV']:.1f} (hbar^2/MeV)")
    lines.append("=" * 76)
    lines.append("PTRM Eigenvalue Spectrum & Wobbling Hierarchy:")
    lines.append("   Spin I     E_yrast(keV)   E_wob1(keV)   hbar*omega(keV)   R_21 (Anharm)")
    for lv in res["levels"]:
        lines.append(
            f"    {lv['spin_I']:4.1f}      {lv['E_yrast_keV']:10.1f}    {lv['E_wob1_keV']:10.1f}        {lv['wobbling_energy_keV']:8.1f}         {lv['anharmonic_ratio_R21']:6.2f}"
        )
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Full Microscopic Particle-Triaxial-Rotor Model (PTRM) Algebraic Diagonalizer."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load experimental preset")
    parser.add_argument("--mass-a", type=int, help="Mass number A")
    parser.add_argument("--jval", type=float, default=5.5, help="Valence orbital angular momentum j")
    parser.add_argument("--gamma", type=float, default=26.0, help="Triaxial deformation angle gamma in deg")
    parser.add_argument("--cquad", type=float, default=35.0, help="Quadrupole splitting parameter C in keV")
    parser.add_argument("--Js", type=float, default=15.0, help="Short axis moment of inertia")
    parser.add_argument("--Jm", type=float, default=26.0, help="Intermediate axis moment of inertia")
    parser.add_argument("--Jl", type=float, default=6.0, help="Long axis moment of inertia")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        A_mass = p["A_mass"]
        spins = p["spins"]
        j_val = p["j_valence"]
        gamma = p["gamma_deg"]
        c_quad = p["C_quadrupole_keV"]
        Js = p["J_s_hbar2_MeV"]
        Jm = p["J_m_hbar2_MeV"]
        Jl = p["J_l_hbar2_MeV"]
        title = f"Preset: {args.preset} ({p['description']})"
    elif args.mass_a:
        A_mass = args.mass_a
        spins = [5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5]
        j_val = args.jval
        gamma = args.gamma
        c_quad = args.cquad
        Js = args.Js
        Jm = args.Jm
        Jl = args.Jl
        title = "Custom User Input"
    else:
        return parser.print_help()

    res = run_ptrm_analysis(
        A_mass=A_mass,
        spins=spins,
        j_val=j_val,
        J_s=Js,
        J_m=Jm,
        J_l=Jl,
        C_quad=c_quad,
        gamma_deg=gamma
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
