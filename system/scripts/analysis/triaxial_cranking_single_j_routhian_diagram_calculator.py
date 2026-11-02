#!/usr/bin/env python3
"""
triaxial_cranking_single_j_routhian_diagram_calculator.py
=========================================================
High-j Single-Shell Triaxial Cranking Hamiltonian Diagonalizer, Routhians e'(omega, gamma),
Signature alpha = +/- 1/2 Classification & Signature Inversion Engine.

Physics & Formulation:
----------------------
1. The High-j Triaxial Single-Particle Hamiltonian:
   In high-spin deformed and triaxial nuclei, intruder orbitals with large angular momentum j
   (e.g. h_11/2 in A ~ 130, i_13/2 in rare earths) dominate the Coriolis alignment.
   The triaxial deformed single-particle Hamiltonian in a single-j shell is parameterized as
   (Frauendorf & Meng 1997; Frauendorf in Petrache 2025 CRC Press Ch. 2, Eq. 2.13):
     h_sp(gamma) = [ kappa / (j * (j + 1)) ] * [ (3 * j_z^2 - j * (j + 1)) * cos(gamma) +
                                                sqrt(3) * (j_x^2 - j_y^2) * sin(gamma) ]
   where:
     - kappa is the quadrupole coupling parameter (~ 2.5 - 4.0 MeV);
     - gamma is the triaxiality parameter (Copenhagen / Lund convention):
         gamma = 0 deg   : Axially symmetric prolate (lengthened along z)
         gamma = -30 deg : Maximally triaxial (intermediate axis collective rotation)
         gamma = -60 deg : Axially symmetric oblate (flattened along z)

2. Cranking Term & Rotating Frame:
   Cranking rotation with rotational frequency omega about the x-axis adds the Coriolis term:
     h_crank(gamma, omega) = h_sp(gamma) - omega * j_x
   In the basis of magnetic substates |j, m> (m = -j, -j+1, ..., +j, dimension 2j+1):
     - j_z is diagonal: <j, m| j_z |j, m> = m
     - j_x = 0.5 * (j_+ + j_-) connects Delta_m = +/- 1 states
     - (j_x^2 - j_y^2) = 0.5 * (j_+^2 + j_-^2) connects Delta_m = +/- 2 states

3. Signature Symmetry alpha = +/- 1/2:
   The cranking Hamiltonian commutes with the signature operator R_x(pi) = exp(-i * pi * j_x):
     [ h_crank, R_x(pi) ] == 0
   Its eigenvalues are r = exp(-i * pi * alpha) = -i (favored, alpha = +1/2) and +i (unfavored, alpha = -1/2).
   Diagonalization of the (2j+1) x (2j+1) Hermitian matrix yields 2j+1 real eigenvalues (Routhians e'_nu):
     h_crank |nu> = e'_nu |nu>

4. Quasiparticle Alignment & Signature Inversion:
   - Aligned angular momentum: i_x = <nu| j_x |nu> = - d(e'_nu) / domega
   - Signature splitting: Delta_e'(omega) = e'(alpha = -1/2) - e'(alpha = +1/2)
   - Signature Inversion: In triaxial nuclei, at low frequencies, Delta_e' can become negative
     (unfavored signature anomalously lower than favored signature), crossing zero to restore
     normal ordering at the inversion frequency omega_inv!

References:
  - S. Frauendorf, in *Chirality and Wobbling in Atomic Nuclei* (CRC Press 2025), Ch. 2, Eq. (2.13).
  - S. Frauendorf and J. Meng, Nucl. Phys. A 617, 131 (1997).
  - R. Bengtsson and I. Ragnarsson, Nucl. Phys. A 436, 14 (1985).
  - A. Bohr and B. R. Mottelson, *Nuclear Structure*, Vol. II, §4-3.
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple
import numpy as np


def _construct_single_j_matrices(j: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Constructs Jx, Jy, Jz, and Rx(pi) matrices in |j, m> basis."""
    m_vals = np.arange(-j, j + 1.0, 1.0)
    dim = len(m_vals)

    Jz = np.diag(m_vals)
    J_plus = np.zeros((dim, dim))
    J_minus = np.zeros((dim, dim))

    for idx, m in enumerate(m_vals):
        if idx + 1 < dim:
            val = math.sqrt(j * (j + 1.0) - m * (m + 1.0))
            J_plus[idx + 1, idx] = val
            J_minus[idx, idx + 1] = val

    Jx = 0.5 * (J_plus + J_minus)
    Jy = -0.5j * (J_plus - J_minus)

    # Rx(pi) = exp(-i * pi * Jx)
    # Using scipy.linalg.expm
    from scipy.linalg import expm
    Rx_pi = expm(-1j * math.pi * Jx)

    return Jx, Jy, Jz, Rx_pi


def diagonalize_triaxial_cranked_high_j(
    j_orbital: float,
    gamma_deg: float = -30.0,
    omega_MeV: float = 0.20,
    kappa_MeV: float = 3.0
) -> Dict[str, Any]:
    """
    Diagonalizes the single-j triaxial cranking Hamiltonian h_crank(gamma, omega).
    Returns sorted Routhians, signature labels, alignments <jx>, and expectation values <jz^2>, <jy^2>.
    """
    if j_orbital <= 0.5 or int(round(2.0 * j_orbital)) % 2 == 0:
        raise ValueError("j_orbital must be half-integer >= 1.5 (e.g. 5.5 for h11/2).")

    Jx, Jy, Jz, Rx_pi = _construct_single_j_matrices(j_orbital)
    dim = len(Jx)

    gamma_rad = math.radians(gamma_deg)

    # Triaxial Nilsson term
    j_fac = j_orbital * (j_orbital + 1.0)
    term1 = (3.0 * (Jz @ Jz) - j_fac * np.eye(dim)) * math.cos(gamma_rad)
    term2 = math.sqrt(3.0) * (Jx @ Jx - Jy @ Jy) * math.sin(gamma_rad)
    h_nilsson = (kappa_MeV / j_fac) * (term1 + term2)

    # Cranking term - omega * Jx
    h_crank = h_nilsson - omega_MeV * Jx

    # Diagonalize Hermitian matrix
    eigvals, eigvecs = np.linalg.eigh(h_crank)

    levels = []
    favored_levels = []
    unfavored_levels = []

    for i in range(dim):
        v = eigvecs[:, i]
        e_val = float(eigvals[i])

        # Signature eigenvalue r = <v| Rx(pi) |v>
        rx_val = complex(np.vdot(v, Rx_pi @ v))
        # r = exp(-i * pi * alpha) = -i for alpha = +1/2, +i for alpha = -1/2
        if rx_val.imag < 0:
            alpha = "+1/2"
            favored_levels.append((e_val, i))
        else:
            alpha = "-1/2"
            unfavored_levels.append((e_val, i))

        jx_exp = float(np.vdot(v, Jx @ v).real)
        jy2_exp = float(np.vdot(v, Jy @ Jy @ v).real)
        jz2_exp = float(np.vdot(v, Jz @ Jz @ v).real)

        levels.append({
            "level_index": i + 1,
            "Routhian_e_MeV": round(e_val, 4),
            "signature_alpha": alpha,
            "alignment_jx_hbar": round(jx_exp, 2),
            "exp_jz2": round(jz2_exp, 2),
            "exp_jy2": round(jy2_exp, 2)
        })

    # Signature splitting for the lowest pair
    sig_split_keV = None
    if favored_levels and unfavored_levels:
        # Lowest favored and lowest unfavored
        e_fav = favored_levels[0][0]
        e_unfav = unfavored_levels[0][0]
        sig_split_keV = (e_unfav - e_fav) * 1000.0

    return {
        "j_orbital": j_orbital,
        "gamma_deg": gamma_deg,
        "omega_MeV": omega_MeV,
        "kappa_MeV": kappa_MeV,
        "lowest_signature_splitting_keV": round(sig_split_keV, 1) if sig_split_keV is not None else None,
        "is_signature_inverted": (sig_split_keV is not None and sig_split_keV < 0.0),
        "levels": levels
    }


def scan_routhian_frequency_trajectory(
    j_orbital: float,
    gamma_deg: float = -30.0,
    kappa_MeV: float = 3.0,
    omega_max_MeV: float = 0.40,
    omega_step_MeV: float = 0.04
) -> List[Dict[str, Any]]:
    """Scans the Routhians across rotational frequencies to track alignment and signature splitting."""
    omegas = [round(i * omega_step_MeV, 3) for i in range(int(round(omega_max_MeV / omega_step_MeV)) + 1)]
    traj = []
    for w in omegas:
        res = diagonalize_triaxial_cranked_high_j(j_orbital, gamma_deg=gamma_deg, omega_MeV=w, kappa_MeV=kappa_MeV)
        traj.append({
            "omega_MeV": w,
            "lowest_routhian_MeV": res["levels"][0]["Routhian_e_MeV"],
            "lowest_alignment_jx": res["levels"][0]["alignment_jx_hbar"],
            "signature_splitting_keV": res["lowest_signature_splitting_keV"],
            "is_inverted": res["is_signature_inverted"]
        })
    return traj


def format_text_report(diag: Dict[str, Any], traj: Optional[List[Dict[str, Any]]] = None) -> str:
    lines = [
        "=" * 76,
        "   HIGH-j TRIAXIAL CRANKING SINGLE-PARTICLE ROUTHIAN SUITE",
        "   Based on Frauendorf in Petrache (2025) Ch. 2 & Frauendorf-Meng (1997)",
        "=" * 76,
        f" CONFIGURATION: Single j = {diag['j_orbital']} Shell (Dimension: {len(diag['levels'])})",
        f"   Triaxiality Parameter gamma : {diag['gamma_deg']:.1f} deg",
        f"   Rotational Frequency omega  : {diag['omega_MeV']:.3f} MeV  (hbar*omega)",
        f"   Quadrupole Strength kappa   : {diag['kappa_MeV']:.2f} MeV",
        f"   Lowest Signature Splitting  : {diag['lowest_signature_splitting_keV']} keV  [Inverted: {diag['is_signature_inverted']}]",
        "-" * 76,
        " SINGLE-PARTICLE ROUTHIAN SPECTRUM & OPERATOR EXPECTATION VALUES:",
        "   Idx     Routhian e' (MeV)    Signature    <j_x> (hbar)    <j_z^2>     <j_y^2>",
    ]

    for lv in diag["levels"]:
        lines.append(f"    {lv['level_index']:2d}        {lv['Routhian_e_MeV']:8.4f}          {lv['signature_alpha']:<8}     {lv['alignment_jx_hbar']:5.2f}       {lv['exp_jz2']:6.2f}      {lv['exp_jy2']:6.2f}")

    if traj is not None:
        lines.extend([
            "-" * 76,
            " FREQUENCY TRAJECTORY SCAN (omega = 0 to omega_max):",
            "   omega (MeV)    Lowest e' (MeV)    <j_x> (hbar)    Splitting (keV)    Inverted?",
        ])
        for pt in traj:
            inv_str = "YES (Inverted)" if pt["is_inverted"] else "Normal"
            lines.append(f"     {pt['omega_MeV']:5.3f}          {pt['lowest_routhian_MeV']:8.4f}         {pt['lowest_alignment_jx']:5.2f}         {pt['signature_splitting_keV']:9.1f}        {inv_str}")
        lines.append("-" * 76)

    lines.extend([
        " Methodological Significance for Wobbling and Chirality:",
        "   - At gamma = -30 deg, particle j aligns along short s-axis (<jx> ~ j), forming the TW mode.",
        "   - Signature splitting Delta_e' = e'(alpha=-1/2) - e'(alpha=+1/2) governs signature inversion.",
        "   - In chiral nuclei, partner bands have identical single-particle Routhian structures.",
        "=" * 76
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="High-j Triaxial Cranking Routhian Diagonalizer"
    )
    parser.add_argument("--j-orbital", type=float, default=5.5, help="Single-j orbital (default: 5.5 for h11/2)")
    parser.add_argument("--gamma", type=float, default=-30.0, help="Triaxiality gamma in deg (default: -30.0 deg)")
    parser.add_argument("--omega", type=float, default=0.20, help="Cranking frequency in MeV (default: 0.20)")
    parser.add_argument("--kappa", type=float, default=3.0, help="Quadrupole coupling strength in MeV (default: 3.0)")
    parser.add_argument("--preset", type=str, default="h11/2_triaxial_chiral",
                        choices=["h11/2_triaxial_chiral", "h11/2_prolate", "h11/2_oblate", "i13/2_rare_earth"],
                        help="Benchmark preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")

    args = parser.parse_args()

    j_val = args.j_orbital
    gam_val = args.gamma
    w_val = args.omega
    kap_val = args.kappa

    if args.preset == "h11/2_triaxial_chiral":
        j_val, gam_val, w_val, kap_val = 5.5, -30.0, 0.20, 3.0
    elif args.preset == "h11/2_prolate":
        j_val, gam_val, w_val, kap_val = 5.5, 0.0, 0.20, 3.0
    elif args.preset == "h11/2_oblate":
        j_val, gam_val, w_val, kap_val = 5.5, -60.0, 0.20, 3.0
    elif args.preset == "i13/2_rare_earth":
        j_val, gam_val, w_val, kap_val = 6.5, -20.0, 0.25, 3.5

    diag_res = diagonalize_triaxial_cranked_high_j(j_val, gamma_deg=gam_val, omega_MeV=w_val, kappa_MeV=kap_val)
    traj_res = scan_routhian_frequency_trajectory(j_val, gamma_deg=gam_val, kappa_MeV=kap_val)

    if args.json:
        out = {"diagonalization": diag_res, "frequency_scan": traj_res}
        print(json.dumps(out, indent=2))
    else:
        print(format_text_report(diag_res, traj_res))


if __name__ == "__main__":
    main()
