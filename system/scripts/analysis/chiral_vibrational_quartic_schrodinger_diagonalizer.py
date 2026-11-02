#!/usr/bin/env python3
"""
chiral_vibrational_quartic_schrodinger_diagonalizer.py
======================================================
Large-Amplitude Chiral Collective Motion (LACM) Quartic Double-Well Potential
Numerical 1D Schrödinger Equation Diagonalizer & Tunneling Energy Splitting Engine.

Physics Formulation:
--------------------
1. One-Dimensional Collective Chiral Hamiltonian:
   Based on "Chirality and Wobbling in Atomic Nuclei" (CRC Press 2025) Chapter 2 (PDF pp. 43–80),
   Chapter 10 (PDF pp. 222–238), S. Mukhopadhyay et al. (Phys. Rev. Lett. 99, 172501, 2007),
   and Q. B. Chen et al. (Phys. Rev. C 96, 051303(R), 2017):
   In triaxial nuclei with aplanar chiral rotation, the collective orientation along the out-of-plane
   azimuth phi in [-pi/2, pi/2] is governed by the collective Hamiltonian:
     H = - [ hbar^2 / (2 * B_phi) ] * (d^2 / d phi^2) + V(phi)
   where B_phi is the collective mass parameter for out-of-plane chiral motion.

2. Non-Harmonic Quartic Potential Parameterization:
   The effective orientation energy profile is expanded as:
     V(phi) = 0.5 * c_2 * phi^2 + 0.25 * c_4 * phi^4
   - When c_2 > 0: Single-well harmonic/anharmonic vibrator (Chiral Vibration, large splitting);
   - When c_2 < 0, c_4 > 0: Symmetric double-well potential with minima at:
       +/- phi_0 = +/- sqrt( - c_2 / c_4 )
       Barrier height: V_B = c_2^2 / (4 * c_4).

3. Finite-Difference Numerical Diagonalization:
   Discretizing on a spatial grid phi_i in [-phi_max, phi_max] with step Delta_phi:
     H_ii = [ hbar^2 / (B_phi * Delta_phi^2) ] + V(phi_i)
     H_{i, i+1} = H_{i+1, i} = - [ hbar^2 / (2 * B_phi * Delta_phi^2) ]
   Diagonalizing this tridiagonal Hermitian matrix yields exact quantum energy levels E_n and
   wavefunctions Psi_n(phi):
     - Ground state E_0: Symmetric wave function (positive parity, Band 1);
     - First excited state E_1: Antisymmetric wave function (negative parity, Band 2);
     - Exact chiral tunneling splitting: Delta E_chir = E_1 - E_0;
     - Two-phonon chiral excitation: E_2 - E_0;
     - Anharmonicity ratio: R_21 = (E_2 - E_0) / (E_1 - E_0).

4. Transition Dipole Matrix Elements:
   The dipole transition operator between symmetric and antisymmetric partner states is:
     M_01 = <Psi_0 | sin(phi) | Psi_1> = sum_i Psi_0(phi_i) * sin(phi_i) * Psi_1(phi_i) * Delta_phi.
"""

import sys
import json
import math
import argparse
import numpy as np
from scipy.linalg import eigh_tridiagonal


PRESETS = {
    "135Nd_chiral_vibration": {
        "description": "135Nd soft-potential chiral vibration (Mukhopadhyay 2007, shallow barrier ~170 keV)",
        "nucleus": "135Nd",
        "c2_MeV": -3.50,
        "c4_MeV": 18.00,
        "B_phi_hbar2_per_MeV": 12.0,
        "phi_max_rad": 1.10,
        "n_grid": 300
    },
    "134Pr_static_chiral_rotation": {
        "description": "134Pr deep double-well static chirality (Tonev 2006, barrier ~640 keV)",
        "nucleus": "134Pr",
        "c2_MeV": -8.00,
        "c4_MeV": 25.00,
        "B_phi_hbar2_per_MeV": 16.0,
        "phi_max_rad": 1.20,
        "n_grid": 300
    },
    "harmonic_vibrator_limit": {
        "description": "Pure single-well harmonic vibrator limit (c2 > 0, c4 = 0)",
        "nucleus": "Harmonic-Ref",
        "c2_MeV": 6.00,
        "c4_MeV": 0.00,
        "B_phi_hbar2_per_MeV": 10.0,
        "phi_max_rad": 1.00,
        "n_grid": 300
    }
}


def diagonalize_chiral_schrodinger(c2_MeV, c4_MeV, B_phi, phi_max_rad=1.15, n_grid=300):
    """
    Discretizes and diagonalizes 1D collective chiral Hamiltonian.
    Returns lowest eigenvalues, wavefunctions, and matrix elements.
    """
    phi_arr = np.linspace(-phi_max_rad, phi_max_rad, n_grid)
    d_phi = phi_arr[1] - phi_arr[0]

    # Potential energy: V(phi) = 0.5 * c2 * phi^2 + 0.25 * c4 * phi^4 (in MeV)
    V_pot = 0.5 * c2_MeV * (phi_arr**2) + 0.25 * c4_MeV * (phi_arr**4)

    # Kinetic energy prefactor: hbar^2 / (2 * B_phi) in MeV (with hbar = 1)
    # d^2/dphi^2 prefactor: t_kin = 1.0 / (2.0 * B_phi * d_phi^2)
    t_kin = 1.0 / (2.0 * B_phi * (d_phi**2))

    diag = 2.0 * t_kin + V_pot
    off_diag = -t_kin * np.ones(n_grid - 1)

    # Diagonalize lowest 6 states
    evals, evecs = eigh_tridiagonal(diag, off_diag, select="i", select_range=(0, 5))

    # Normalize wavefunctions: sum |psi|^2 * d_phi = 1.0
    for k in range(len(evals)):
        norm = math.sqrt(np.sum((evecs[:, k]**2) * d_phi))
        if norm > 0:
            evecs[:, k] /= norm

    # Energy levels in keV relative to ground state
    E0_MeV = evals[0]
    E_rel_keV = [(e - E0_MeV) * 1000.0 for e in evals]

    delta_E_chir_keV = E_rel_keV[1]  # E1 - E0
    delta_E_2phonon_keV = E_rel_keV[2]  # E2 - E0
    r21_ratio = delta_E_2phonon_keV / max(1e-4, delta_E_chir_keV)

    # Potential barrier and minimum
    if c2_MeV < 0 and c4_MeV > 0:
        phi_0 = math.sqrt(-c2_MeV / c4_MeV)
        barrier_keV = ((c2_MeV**2) / (4.0 * c4_MeV)) * 1000.0
    else:
        phi_0 = 0.0
        barrier_keV = 0.0

    # Dipole matrix element <0 | sin(phi) | 1>
    sin_phi = np.sin(phi_arr)
    M_01 = float(np.sum(evecs[:, 0] * sin_phi * evecs[:, 1] * d_phi))

    # Right-well localization fraction of ground state: int_0^infty |psi_0|^2 dphi
    idx_zero = n_grid // 2
    p_right = float(np.sum((evecs[idx_zero:, 0]**2) * d_phi))

    return {
        "eigenvalues_rel_keV": [float(e) for e in E_rel_keV],
        "chiral_splitting_keV": float(delta_E_chir_keV),
        "two_phonon_excitation_keV": float(delta_E_2phonon_keV),
        "anharmonic_ratio_R21": float(r21_ratio),
        "barrier_height_keV": float(barrier_keV),
        "equilibrium_phi0_deg": float(math.degrees(phi_0)),
        "dipole_matrix_element_M01": float(abs(M_01)),
        "right_half_probability": float(p_right),
        "is_double_well": bool(c2_MeV < 0.0 and c4_MeV > 0.0)
    }


def run_chiral_schrodinger_analysis(nucleus, c2_MeV, c4_MeV, B_phi, phi_max_rad=1.15, n_grid=300):
    """
    Complete execution pipeline for chiral Schrödinger equation diagonalization.
    """
    diag_res = diagonalize_chiral_schrodinger(c2_MeV, c4_MeV, B_phi, phi_max_rad, n_grid)
    return {
        "nucleus": nucleus,
        "parameters": {
            "c2_MeV": float(c2_MeV),
            "c4_MeV": float(c4_MeV),
            "B_phi_hbar2_per_MeV": float(B_phi),
            "phi_max_deg": float(math.degrees(phi_max_rad)),
            "n_grid_points": int(n_grid)
        },
        "schrodinger_results": diag_res
    }


def format_text_report(res, title="Chiral Quartic Double-Well Schrödinger Diagonalizer"):
    nuc = res["nucleus"]
    p = res["parameters"]
    sr = res["schrodinger_results"]
    evals = sr["eigenvalues_rel_keV"]

    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Nucleus: {nuc} | Potential: c2 = {p['c2_MeV']:.2f} MeV, c4 = {p['c4_MeV']:.2f} MeV | Mass B_phi = {p['B_phi_hbar2_per_MeV']:.1f} hbar^2/MeV")
    lines.append("=" * 76)
    lines.append("Potential Landscape Topology:")
    if sr["is_double_well"]:
        lines.append(f"  Double-Well Minima Positions    : +- {sr['equilibrium_phi0_deg']:.1f} deg (Aplanar left/right enantiomers)")
        lines.append(f"  Central Barrier Height V_B      : {sr['barrier_height_keV']:.1f} keV (Separating left/right chiral wells)")
    else:
        lines.append("  Single-Well Potential Minimum   : phi = 0.0 deg (Planar harmonic/anharmonic vibrator)")
    lines.append("-" * 76)
    lines.append("Numerical Energy Eigenstates (relative to ground state E_0):")
    lines.append(f"  E_0 (Ground State, Band 1)      :    0.0 keV  [Symmetric, Even Parity]")
    lines.append(f"  E_1 (1st Excited, Band 2)       : {evals[1]:6.1f} keV  [Antisymmetric, Odd Parity, Delta E_chir = {sr['chiral_splitting_keV']:.1f} keV]")
    lines.append(f"  E_2 (2nd Excited, Two-Phonon)   : {evals[2]:6.1f} keV  [Two-phonon collective vibration]")
    lines.append(f"  E_3 (3rd Excited State)         : {evals[3]:6.1f} keV")
    lines.append("-" * 76)
    lines.append("Quantum Dynamics & Selection Metrics:")
    lines.append(f"  Chiral Tunneling Energy Splitting: Delta E = {sr['chiral_splitting_keV']:.1f} keV ({'Static Chiral Rotation (< 70 keV)' if sr['chiral_splitting_keV'] < 70.0 else 'Chiral Vibration (> 150 keV)'})")
    lines.append(f"  Anharmonicity Ratio R_21        : R_21 = {sr['anharmonic_ratio_R21']:.2f} (Harmonic limit = 2.00, Tunneling doublet >> 2.0)")
    lines.append(f"  Interband Dipole Matrix Element : M_01 = <0|sin(phi)|1> = {sr['dipole_matrix_element_M01']:.4f}")
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Chiral Quartic Double-Well Schrödinger Equation Diagonalizer."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load benchmark preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        nucleus = p["nucleus"]
        c2 = p["c2_MeV"]
        c4 = p["c4_MeV"]
        B_phi = p["B_phi_hbar2_per_MeV"]
        phi_max = p.get("phi_max_rad", 1.15)
        ngrid = p.get("n_grid", 300)
        title = f"Preset: {args.preset} ({p['description']})"
    else:
        return parser.print_help()

    res = run_chiral_schrodinger_analysis(
        nucleus=nucleus,
        c2_MeV=c2,
        c4_MeV=c4,
        B_phi=B_phi,
        phi_max_rad=phi_max,
        n_grid=ngrid
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
