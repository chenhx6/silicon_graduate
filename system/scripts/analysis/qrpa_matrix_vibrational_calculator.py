#!/usr/bin/env python3
"""
Quasiparticle Random-Phase Approximation (QRPA) & pnQRPA Matrix Calculator.

Based on:
  - P. Ring & P. Schuck, The Nuclear Many-Body Problem, Ch. 8 (RPA & QRPA formalism)
  - J. Suhonen, From Nucleons to Nucleus, Ch. 18-19 (QRPA, pnQRPA & double beta decay)
  - P. Vogel & M. R. Zirnbauer, Phys. Rev. Lett. 57, 3148 (1986) (Suppression of 2nu beta beta by g_pp)
  - O. Civitarese, A. Faessler, T. Tomoda, Phys. Lett. B 194, 11 (1987) (pnQRPA matrix elements)

Features:
  1. Constructs and diagonalizes non-Hermitian QRPA supermatrix [[A, B], [-B, -A]].
  2. Normalizes eigenvectors to Bose metric X^2 - Y^2 = 1 and extracts forward/backward amplitudes.
  3. Evaluates collective transition enhancement factors (X + Y)^2 beyond Tamm-Dancoff (QTDA).
  4. Scans proton-neutron particle-particle strength g_pp sensitivity and zero-crossing in double beta decay.
  5. Diagnoses QRPA vacuum stability via positive-definiteness of (A - B) and (A + B) Hessian matrices.
"""

import numpy as np


def solve_qrpa_eigenvalues_and_amplitudes(matrix_A, matrix_B):
    """
    Solve the non-Hermitian QRPA eigenvalue problem:
      [[A, B], [-B, -A]] * [X, Y]^T = omega * [X, Y]^T.
    Returns sorted positive physical eigenvalues omega_nu, normalized (X, Y) vectors,
    and collective transition enhancement factors.
    """
    a_mat = np.array(matrix_A, dtype=float)
    b_mat = np.array(matrix_B, dtype=float)

    if a_mat.shape != b_mat.shape:
        raise ValueError("Matrices A and B must have identical square shapes.")
    if a_mat.shape[0] != a_mat.shape[1]:
        raise ValueError("Matrix A must be square.")

    n_dim = a_mat.shape[0]

    # Construct QRPA supermatrix
    m_super = np.block([[a_mat, b_mat], [-b_mat, -a_mat]])
    eigenvalues, eigenvectors = np.linalg.eig(m_super)

    # Sort and filter positive real eigenvalues
    modes = []
    # Identify pairs: for each positive eigenvalue
    for idx in range(len(eigenvalues)):
        val = eigenvalues[idx]
        if val.real > 1e-4 and abs(val.imag) < 1e-3:
            vec = eigenvectors[:, idx].real
            x_vec = vec[:n_dim]
            y_vec = vec[n_dim:]

            # Metric norm: sum(X_i^2 - Y_i^2)
            norm = np.dot(x_vec, x_vec) - np.dot(y_vec, y_vec)
            if norm > 1e-6:
                scale = 1.0 / np.sqrt(norm)
                x_norm = x_vec * scale
                y_norm = y_vec * scale

                # Collective enhancement factor (sum_i (X_i + Y_i))^2
                enhancement = float(np.sum(x_norm + y_norm) ** 2)

                modes.append({
                    "omega_MeV": float(val.real),
                    "X_amplitudes": x_norm.tolist(),
                    "Y_amplitudes": y_norm.tolist(),
                    "sum_Y_squared": float(np.sum(y_norm ** 2)),
                    "coherent_enhancement_factor": enhancement
                })

    # Sort ascending by energy
    modes = sorted(modes, key=lambda m: m["omega_MeV"])

    # Stability check: both A-B and A+B must be positive definite
    eig_diff = np.linalg.eigvalsh(a_mat - b_mat)
    eig_sum  = np.linalg.eigvalsh(a_mat + b_mat)
    is_stable = bool(np.all(eig_diff > 0) and np.all(eig_sum > 0))

    return {
        "dimension": n_dim,
        "is_stable_vacuum": is_stable,
        "modes_found": len(modes),
        "modes": modes
    }


def solve_analytic_single_mode_qrpa(A_val, B_val):
    """
    Solve single-mode analytic QRPA equation:
      omega = sqrt(A^2 - B^2)
      X = sqrt( (A + omega) / (2 * omega) )
      Y = - sign(B) * sqrt( (A - omega) / (2 * omega) )
      (X + Y)^2 = (A - B) / omega = sqrt( (A - B) / (A + B) ).
    """
    a = float(A_val)
    b = float(B_val)

    if a <= abs(b):
        raise ValueError(f"Instability condition: A ({a}) must be strictly greater than |B| ({abs(b)}).")

    omega = np.sqrt(a ** 2 - b ** 2)
    x = np.sqrt((a + omega) / (2.0 * omega))
    y = - np.sign(b) * np.sqrt((a - omega) / (2.0 * omega))
    enhancement = (x + y) ** 2

    return {
        "A": a,
        "B": b,
        "omega_MeV": float(omega),
        "X": float(x),
        "Y": float(y),
        "Y_squared": float(y ** 2),
        "X_squared_minus_Y_squared": float(x ** 2 - y ** 2),
        "coherent_enhancement": float(enhancement)
    }


def scan_pnqrpa_gpp_sensitivity(E_unpert_MeV=4.0, g_ph=1.0, g_pp_range=(0.0, 1.2), n_points=25):
    """
    Scan proton-neutron particle-particle strength g_pp sensitivity on 1+ state energy
    and double beta decay matrix element suppression (Vogel-Zirnbauer mechanism).
    """
    e0 = float(E_unpert_MeV)
    gph = float(g_ph)
    gpp_arr = np.linspace(g_pp_range[0], g_pp_range[1], int(n_points))

    chi_ph = 0.5
    chi_pp = 0.6

    results = []
    zero_crossing_gpp = None

    for gpp in gpp_arr:
        # A increases with g_ph, decreases with g_pp
        a_val = e0 + 2.0 * chi_ph * gph - 2.0 * chi_pp * gpp
        b_val = 2.0 * chi_ph * gph + 2.0 * chi_pp * gpp

        radicand = a_val ** 2 - b_val ** 2
        if radicand > 0:
            omega = np.sqrt(radicand)
            is_stable = True
        else:
            omega = 0.0
            is_stable = False

        # 2nu beta beta matrix element: proportional to (1 - g_pp / g_pp_crit)
        m2nu = max(-1.0, 1.0 - (gpp / 0.95))
        if zero_crossing_gpp is None and m2nu <= 0:
            zero_crossing_gpp = float(gpp)

        results.append({
            "g_pp": float(gpp),
            "omega_MeV": float(omega),
            "A_val": float(a_val),
            "B_val": float(b_val),
            "M_2nu_relative": float(m2nu),
            "is_stable": is_stable
        })

    return {
        "E_unperturbed_MeV": e0,
        "g_ph": gph,
        "zero_crossing_gpp": zero_crossing_gpp,
        "scan_data": results
    }


def diagnose_qrpa_stability(matrix_A, matrix_B):
    """
    Diagnose the stability of the QRPA vacuum by inspecting the eigenvalues of
    the Hessian submatrices (A - B) and (A + B).
    """
    a_mat = np.array(matrix_A, dtype=float)
    b_mat = np.array(matrix_B, dtype=float)

    eig_diff = np.linalg.eigvalsh(a_mat - b_mat)
    eig_sum  = np.linalg.eigvalsh(a_mat + b_mat)

    min_diff = float(np.min(eig_diff))
    min_sum  = float(np.min(eig_sum))

    if min_diff > 0 and min_sum > 0:
        is_stable = True
        diag = "QRPA vacuum is stable (Hessian matrix is strictly positive definite)."
    elif abs(min_diff) < 1e-4 or abs(min_sum) < 1e-4:
        is_stable = False
        diag = "Marginal stability: Goldstone zero-mode present (spontaneous symmetry breaking threshold)."
    else:
        is_stable = False
        diag = "QRPA collapse / instability: Imaginary eigenvalues indicate spontaneous symmetry breaking in ground state."

    return {
        "is_stable": is_stable,
        "min_eigenvalue_A_minus_B": min_diff,
        "min_eigenvalue_A_plus_B": min_sum,
        "diagnosis": diag
    }
