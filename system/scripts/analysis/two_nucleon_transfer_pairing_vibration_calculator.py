#!/usr/bin/env python3
"""
Two-Nucleon Transfer Reactions, Pairing Vibrations & Nuclear Josephson Effect Calculator.

Based on:
  - D. R. Bes & R. A. Broglia, Nucl. Phys. 80, 289 (1966) (Pairing vibrations in gauge space)
  - A. Bohr & B. R. Mottelson, Nuclear Structure Vol. II, Ch. 6 (Pairing Vibrations & (t,p)/(p,t))
  - M. Cavallaro et al., Nature Commun. 10, 167 (2019) (Giant Pairing Vibration discovery)
  - W. von Oertzen & A. Vitturi, Rep. Prog. Phys. 64, 1247 (2001) (Nuclear Josephson supercurrent)

Features:
  1. Computes BCS coherent pair transfer enhancement factor sigma_BCS / sigma_sp.
  2. Calculates pair addition (hw+) and pair removal (hw-) phonon energies and the (1,1) double-phonon 0+ state in closed-shell nuclei.
  3. Evaluates kinematic Q-matching and optimum Q_opt for light-ion (p,t) vs heavy-ion (18O, 16O) transfer.
  4. Models the Nuclear Josephson multi-pair tunneling enhancement ratio P_2pair / (P_1pair)^2.
"""

import numpy as np


def calculate_bcs_transfer_enhancement(valence_orbitals_j_v2):
    """
    Compute BCS coherent pair transfer cross section enhancement:
      Coherent amplitude: A_coh = sum_j sqrt(j + 1/2) * u_j * v_j.
      Incoherent rate:    sigma_incoh = sum_j (j + 1/2) * u_j^2 * v_j^2.
      sigma_coh = |A_coh|^2.
      Enhancement factor = sigma_coh / sigma_incoh.
    Input format: list of tuples [(j, v_j^2), ...]
    """
    if len(valence_orbitals_j_v2) == 0:
        raise ValueError("Must provide at least one valence orbital.")

    a_coh = 0.0
    sigma_incoh = 0.0
    details = []

    for j_val, v2_val in valence_orbitals_j_v2:
        j_f = float(j_val)
        v2 = min(1.0, max(0.0, float(v2_val)))
        u2 = 1.0 - v2
        u = np.sqrt(u2)
        v = np.sqrt(v2)
        deg = j_f + 0.5

        term_coh = np.sqrt(deg) * u * v
        term_incoh = deg * u2 * v2

        a_coh += term_coh
        sigma_incoh += term_incoh

        details.append({
            "j": j_f,
            "degeneracy": deg,
            "v_squared": v2,
            "u_squared": u2,
            "uv_amplitude": float(u * v)
        })

    sigma_coh = a_coh ** 2
    if sigma_incoh > 1e-6:
        enhancement = sigma_coh / sigma_incoh
    else:
        enhancement = 1.0

    return {
        "coherent_amplitude_A": float(a_coh),
        "sigma_coherent": float(sigma_coh),
        "sigma_incoherent": float(sigma_incoh),
        "enhancement_factor": float(enhancement),
        "orbitals_count": len(valence_orbitals_j_v2),
        "details": details
    }


def calculate_pairing_vibration_energies(S2n_A_plus_2_MeV, S2n_A_MeV):
    """
    Compute pair addition (hw+) and pair removal (hw-) phonon energies
    around a doubly closed-shell core A:
      S2n(A+2) is the two-neutron separation energy of nucleus A+2 (pair addition).
      S2n(A)   is the two-neutron separation energy of nucleus A   (pair removal).
      2*lambda_F = 0.5 * [ S2n(A+2) + S2n(A) ].
      hw_+ = 2*lambda_F - S2n(A+2).
      hw_- = S2n(A) - 2*lambda_F.
      E_x(1, 1) = hw_+ + hw_-.
    """
    s2n_add = float(S2n_A_plus_2_MeV)
    s2n_rem = float(S2n_A_MeV)

    if s2n_rem <= s2n_add:
        # In normal shell closures, S2n drops across the gap: S2n(A) > S2n(A+2)
        pass

    two_lambda = 0.5 * (s2n_add + s2n_rem)
    hw_plus = two_lambda - s2n_add
    hw_minus = s2n_rem - two_lambda
    ex_double_phonon = hw_plus + hw_minus

    return {
        "S2n_A_plus_2_MeV": s2n_add,
        "S2n_A_MeV": s2n_rem,
        "two_lambda_Fermi_MeV": float(two_lambda),
        "hw_plus_addition_phonon_MeV": float(hw_plus),
        "hw_minus_removal_phonon_MeV": float(hw_minus),
        "Ex_double_phonon_1_1_MeV": float(ex_double_phonon)
    }


def evaluate_kinematic_q_matching(E_lab_MeV, Q_actual_MeV, Z_proj, A_proj, Z_targ, A_targ, Z_ejec, A_ejec):
    """
    Evaluate kinematic Q-matching for charged-particle transfer:
    Q_opt approx [ (Z_ejec * Z_res) / (Z_proj * Z_targ) - 1 ] * E_cm.
    """
    e_lab = float(E_lab_MeV)
    ap = float(A_proj)
    at = float(A_targ)
    ae = float(A_ejec)
    ar = ap + at - ae

    zp = float(Z_proj)
    zt = float(Z_targ)
    ze = float(Z_ejec)
    zr = zp + zt - ze

    # E_cm
    e_cm = e_lab * (at / (ap + at))

    # Coulomb factor ratio
    coul_ratio = (ze * zr) / (zp * zt)
    q_opt = (coul_ratio - 1.0) * e_cm
    q_diff = float(Q_actual_MeV) - q_opt

    if abs(q_diff) < 2.0:
        match_status = "Optimal kinematic Q-matching (High direct cross section)"
    elif abs(q_diff) < 5.0:
        match_status = "Moderate Q-matching (Observable cross section)"
    else:
        match_status = "Severe Q-mismatch (Coulomb barrier suppressed transfer)"

    return {
        "E_lab_MeV": e_lab,
        "E_cm_MeV": float(e_cm),
        "Q_actual_MeV": float(Q_actual_MeV),
        "Q_optimal_MeV": float(q_opt),
        "Q_mismatch_MeV": float(q_diff),
        "matching_status": match_status
    }


def calculate_josephson_transfer_probability(P_1pair, n_pairs=2, enhancement_factor=15.0):
    """
    Model the Nuclear Josephson multi-pair tunneling enhancement:
    Uncorrelated transfer: P_uncorr = (P_1pair)^n.
    Superfluid Josephson:  P_Josephson = enhancement_factor * (P_1pair)^n.
    """
    p1 = float(P_1pair)
    n = int(n_pairs)
    enh = float(enhancement_factor)

    p_uncorr = p1 ** n
    p_josephson = min(1.0, enh * p_uncorr)

    return {
        "P_1pair": p1,
        "n_pairs": n,
        "P_uncorrelated": float(p_uncorr),
        "P_Josephson": float(p_josephson),
        "enhancement_factor": enh,
        "supercurrent_signature": enh >= 5.0
    }
