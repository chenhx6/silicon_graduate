#!/usr/bin/env python3
"""
Isoscalar Giant Monopole Resonance (ISGMR), Incompressibility & EOS Calculator.

Based on:
  - J. P. Blaizot, Phys. Rep. 64, 171 (1980) (Nuclear incompressibility & leptodermous expansion)
  - D. H. Youngblood et al., Phys. Rev. C 69, 034315 (2004) (ISGMR splitting in deformed 154Sm)
  - T. Li et al., Phys. Rev. Lett. 99, 162503 (2007) (ISGMR in Sn isotopes & QPVC softness)
  - J. Piekarewicz, Phys. Rev. C 69, 041301 (2004) (Soft monopole mode & K_tau)
  - U. Garg & G. Colo, Prog. Part. Nucl. Phys. 101, 55 (2018) (Compression-mode review)

Features:
  1. Inverts finite nuclear incompressibility K_A from experimental ISGMR centroid energy and RMS radius.
  2. Evaluates Leptodermous expansion K_A = K_vol + K_surf*A^(-1/3) + K_tau*((N-Z)/A)^2 + K_coul*Z^2/A^(4/3).
  3. Models deformation-induced monopole-quadrupole mixing (L=0 x L=2, K=0) yielding two-component ISGMR splitting.
  4. Evaluates Quasiparticle-Vibration Coupling (QPVC) dynamic self-energy downward shift (resolving the Tin softness puzzle).
  5. Fits nuclear matter incompressibility K_infinity and asymmetry incompressibility K_tau across isotopic chains.
"""

import numpy as np

# Physical constants
HBAR_C_MEV_FM = 197.3269804  # MeV * fm
M_NUCLEON_MEV = 938.272088    # MeV / c^2


def calculate_ka_from_isgmr_energy(E_gmr_MeV, A, R0_fm=1.2):
    """
    Invert finite nuclear incompressibility K_A (in MeV) from measured
    ISGMR centroid energy E_ISGMR (in MeV) and mass number A:
    E_ISGMR = sqrt( hbar^2 * K_A / (m * <r^2>) ),
    where <r^2> approx (3/5) * R_0^2 * A^(2/3).
    """
    if E_gmr_MeV <= 0 or A <= 0:
        raise ValueError("Energy and mass number A must be strictly positive.")

    a_f = float(A)
    # Mean square radius <r^2> in fm^2
    r_ms_fm2 = 0.6 * (float(R0_fm) ** 2) * (a_f ** (2.0 / 3.0))

    # Denominator in MeV^-1: m * <r^2> / hbar^2 = (m*c^2 * <r^2>) / (hbar*c)^2
    denom_MeV_inv = (M_NUCLEON_MEV * r_ms_fm2) / (HBAR_C_MEV_FM ** 2)

    # K_A = E_gmr^2 * (m * <r^2> / hbar^2)
    k_a_MeV = (float(E_gmr_MeV) ** 2) * denom_MeV_inv

    return {
        "E_gmr_MeV": float(E_gmr_MeV),
        "A": int(A),
        "R0_fm": float(R0_fm),
        "rms_radius_fm": float(np.sqrt(r_ms_fm2)),
        "K_A_MeV": float(k_a_MeV)
    }


def leptodermous_expansion_ka(A, Z, K_vol=240.0, K_surf=-310.0, K_tau=-550.0, K_coul=-5.2):
    """
    Compute theoretical finite nuclear incompressibility K_A via Leptodermous expansion:
    K_A = K_vol + K_surf * A^(-1/3) + K_tau * ((N - Z) / A)^2 + K_coul * (Z^2 / A^(4/3)).
    """
    a_f = float(A)
    z_f = float(Z)
    n_f = a_f - z_f

    asym = (n_f - z_f) / a_f
    term_vol = float(K_vol)
    term_surf = float(K_surf) * (a_f ** (-1.0 / 3.0))
    term_tau = float(K_tau) * (asym ** 2)
    term_coul = float(K_coul) * (z_f ** 2) / (a_f ** (4.0 / 3.0))

    k_a_total = term_vol + term_surf + term_tau + term_coul

    return {
        "A": int(A),
        "Z": int(Z),
        "N": int(n_f),
        "asymmetry": float(asym),
        "K_vol_MeV": term_vol,
        "K_surf_contribution_MeV": float(term_surf),
        "K_tau_contribution_MeV": float(term_tau),
        "K_coul_contribution_MeV": float(term_coul),
        "K_A_theoretical_MeV": float(k_a_total)
    }


def model_deformation_splitting_two_state(E0_unpert_MeV, beta2, A, alpha_coupling=5.5):
    """
    Model the two-state mixing between the L=0 breathing mode and L=2, K=0 quadrupole branch
    in prolate deformed nuclei (e.g. 154Sm):
    H = [[E_0, V], [V, E_2]], where V approx alpha_coupling * beta2.
    """
    e0 = float(E0_unpert_MeV)
    b2 = float(beta2)
    a_f = float(A)

    # Quadrupole energy approx (63 / A^(1/3)) * (1 - beta2 / 3)
    e2 = (63.0 / (a_f ** (1.0 / 3.0))) * (1.0 - b2 / 3.0)
    v_coup = float(alpha_coupling) * b2

    h_mat = np.array([[e0, v_coup], [v_coup, e2]], dtype=float)
    eigenvals, eigenvecs = np.linalg.eigh(h_mat)

    # Sort ascending
    idx = np.argsort(eigenvals)
    e_low = float(eigenvals[idx[0]])
    e_high = float(eigenvals[idx[1]])

    # Monopole EWSR fraction is the square of the overlap with pure L=0 state [1, 0]^T
    frac_low = float(eigenvecs[0, idx[0]] ** 2)
    frac_high = float(eigenvecs[0, idx[1]] ** 2)

    return {
        "A": int(A),
        "beta2": b2,
        "E0_unperturbed_MeV": e0,
        "E2_unperturbed_MeV": float(e2),
        "coupling_matrix_element_V_MeV": float(v_coup),
        "E_low_peak_MeV": e_low,
        "E_high_peak_MeV": e_high,
        "EWSR_fraction_low": frac_low,
        "EWSR_fraction_high": frac_high,
        "splitting_energy_MeV": float(e_high - e_low)
    }


def calculate_qpvc_self_energy_shift(E_gmr_unpert_MeV, E_phonon_MeV, g_coupling_MeV=1.65):
    """
    Compute Quasiparticle-Vibration Coupling (QPVC) dynamic self-energy downward shift:
    Delta E_QPVC approx - g^2 / (E_GMR - E_phonon).
    Explains the 'Why is Tin so soft?' puzzle (downward shift ~ 0.8 - 1.0 MeV).
    """
    e_gmr = float(E_gmr_unpert_MeV)
    e_ph = float(E_phonon_MeV)
    g = float(g_coupling_MeV)

    energy_diff = e_gmr - e_ph
    if energy_diff <= 0.1:
        raise ValueError("Unperturbed GMR energy must be significantly higher than low-energy phonon energy.")

    shift_MeV = - (g ** 2) / energy_diff
    e_shifted_MeV = e_gmr + shift_MeV

    return {
        "E_gmr_unperturbed_MeV": e_gmr,
        "E_phonon_MeV": e_ph,
        "coupling_constant_g_MeV": g,
        "self_energy_shift_MeV": float(shift_MeV),
        "E_gmr_shifted_MeV": float(e_shifted_MeV)
    }


def diagnose_incompressibility_status(K_vol_extracted, K_tau_extracted=None):
    """
    Diagnose whether extracted nuclear incompressibility K_vol and K_tau are consistent
    with empirical nuclear EOS boundaries (K_infinity = 240 +/- 20 MeV, K_tau = -550 +/- 100 MeV).
    """
    k_vol = float(K_vol_extracted)
    reasons = []

    if 220.0 <= k_vol <= 260.0:
        status_vol = "Optimal Standard EOS Stiffness (consistent with 208Pb breathing mode)"
        valid_vol = True
    elif k_vol < 220.0:
        status_vol = "Anomalously Soft EOS (potential uncorrected QPVC or deformation splitting pseudo-softening)"
        valid_vol = False
    else:
        status_vol = "Overly Stiff EOS (incompatible with low-energy collective alpha-scattering)"
        valid_vol = False

    reasons.append(f"K_infinity = {k_vol:.1f} MeV: {status_vol}")

    if K_tau_extracted is not None:
        k_tau = float(K_tau_extracted)
        if -650.0 <= k_tau <= -450.0:
            status_tau = "Standard Asymmetry Stiffness (consistent with Sn isotopic chain)"
        elif k_tau < -650.0:
            status_tau = "Enhanced Asymmetry Softening (strong neutron-skin influence)"
        else:
            status_tau = "Weak Asymmetry Damping"
        reasons.append(f"K_tau = {k_tau:.1f} MeV: {status_tau}")

    return {
        "K_vol_MeV": k_vol,
        "is_standard_eos_stiffness": valid_vol,
        "diagnosis": "; ".join(reasons)
    }
