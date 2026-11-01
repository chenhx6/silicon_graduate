#!/usr/bin/env python3
"""
Halo Nuclei Breakup Dynamics, Momentum Distribution & Cluster E1 Sum Rule Calculator.

Based on:
  - I. Tanihata et al., Phys. Rev. Lett. 55, 2676 (1985) (Discovery of neutron halo in 11Li)
  - P. G. Hansen & B. Jonson, Europhys. Lett. 4, 409 (1987) (Yukawa wave function & Lorentzian-squared momentum distribution)
  - A. S. Goldhaber, Phys. Lett. B 53, 306 (1974) (Statistical Fermi motion in fragmentation)
  - C. A. Bertulani & P. Danielewicz, Introduction to Nuclear Reactions, Ch. 11 (Breakup of halo nuclei)
  - K. Heyde, Basic Ideas in Nuclear Physics, Ch. 15 (Weakly bound quantum systems and exotic nuclei)

Features:
  1. Computes Hansen-Jonson longitudinal momentum distribution FWHM from valence nucleon binding energy S_n/S_2n.
  2. Inverts experimental narrow momentum distribution FWHM to extract valence nucleon binding energy S_n.
  3. Evaluates Goldhaber statistical model momentum width for normal compact core fragment Fermi motion.
  4. Diagnoses halo formation by comparing experimental narrow width vs normal Fermi motion baseline.
  5. Computes cluster Thomas-Reiche-Kuhn (TRK) soft E1 dipole sum rule for core vs halo relative oscillation.
  6. Estimates projectile root-mean-square matter radius R_rms from high-energy reaction cross section sigma_R.
"""

import numpy as np

HBAR_C_MEV_FM = 197.3269804  # MeV * fm
AMU_MEV = 931.49410242       # MeV / c^2


def calculate_hansen_jonson_fwhm(S_n_keV, A_core=9.0, A_halo=2.0):
    """
    Compute theoretical FWHM of longitudinal momentum distribution from separation energy S_n.
    For an asymptotic Yukawa wave function psi(r) ~ exp(-kappa * r)/r,
    the momentum distribution is Lorentzian-squared: dsigma/dp_z ~ 1 / (p_z^2 + alpha^2)^2,
    where alpha = hbar * kappa = sqrt(2 * mu * S_n).
    FWHM = 2 * sqrt(sqrt(2) - 1) * alpha approx 1.2871885 * alpha.
    """
    if S_n_keV <= 0:
        raise ValueError("Separation energy S_n must be strictly positive.")

    # Reduced mass in amu
    mu_amu = (A_core * A_halo) / (A_core + A_halo)
    mu_MeV = mu_amu * AMU_MEV
    S_n_MeV = S_n_keV / 1000.0

    alpha_MeV_c = np.sqrt(2.0 * mu_MeV * S_n_MeV)
    factor = 2.0 * np.sqrt(np.sqrt(2.0) - 1.0)
    fwhm_MeV_c = factor * alpha_MeV_c
    decay_length_fm = HBAR_C_MEV_FM / alpha_MeV_c

    return {
        "S_n_keV": float(S_n_keV),
        "A_core": float(A_core),
        "A_halo": float(A_halo),
        "mu_amu": float(mu_amu),
        "alpha_MeV_c": float(alpha_MeV_c),
        "fwhm_MeV_c": float(fwhm_MeV_c),
        "decay_length_fm": float(decay_length_fm)
    }


def invert_separation_energy_from_fwhm(fwhm_MeV_c, A_core=9.0, A_halo=2.0):
    """
    Inverse problem: extract valence nucleon separation energy S_n (in keV)
    from measured narrow momentum distribution FWHM (in MeV/c).
    """
    if fwhm_MeV_c <= 0:
        raise ValueError("FWHM must be strictly positive.")

    mu_amu = (A_core * A_halo) / (A_core + A_halo)
    mu_MeV = mu_amu * AMU_MEV

    factor = 2.0 * np.sqrt(np.sqrt(2.0) - 1.0)
    alpha_MeV_c = fwhm_MeV_c / factor
    S_n_MeV = (alpha_MeV_c ** 2) / (2.0 * mu_MeV)
    S_n_keV = S_n_MeV * 1000.0
    decay_length_fm = HBAR_C_MEV_FM / alpha_MeV_c

    return {
        "measured_fwhm_MeV_c": float(fwhm_MeV_c),
        "A_core": float(A_core),
        "A_halo": float(A_halo),
        "extracted_S_n_keV": float(S_n_keV),
        "alpha_MeV_c": float(alpha_MeV_c),
        "decay_length_fm": float(decay_length_fm)
    }


def calculate_goldhaber_width(A_projectile, A_fragment, sigma_0_MeV_c=90.0):
    """
    Compute normal core fragment momentum distribution width from Goldhaber statistical model:
    sigma^2 = sigma_0^2 * [A_F * (A_P - A_F) / (A_P - 1)].
    FWHM_Goldhaber = 2 * sqrt(2 * ln(2)) * sigma approx 2.35482 * sigma.
    """
    if A_fragment >= A_projectile:
        raise ValueError("Fragment mass A_fragment must be strictly less than projectile mass A_projectile.")

    var = (sigma_0_MeV_c ** 2) * (A_fragment * (A_projectile - A_fragment)) / (A_projectile - 1.0)
    sigma_MeV_c = np.sqrt(var)
    fwhm_goldhaber_MeV_c = 2.0 * np.sqrt(2.0 * np.log(2.0)) * sigma_MeV_c

    return {
        "A_projectile": float(A_projectile),
        "A_fragment": float(A_fragment),
        "sigma_0_MeV_c": float(sigma_0_MeV_c),
        "sigma_Goldhaber_MeV_c": float(sigma_MeV_c),
        "fwhm_Goldhaber_MeV_c": float(fwhm_goldhaber_MeV_c)
    }


def diagnose_halo_signature(measured_fwhm_MeV_c, goldhaber_fwhm_MeV_c):
    """
    Diagnose whether measured fragment momentum width signifies an extended spatial halo.
    """
    ratio = measured_fwhm_MeV_c / goldhaber_fwhm_MeV_c
    if ratio < 0.45:
        diagnosis = "Prominent Halo Signature: Extreme spatial wave function extension (Quantum Tunneling)"
        is_halo = True
    elif ratio < 0.70:
        diagnosis = "Moderate Halo / Neutron Skin Candidate: Weakly bound surface valence nucleons"
        is_halo = True
    else:
        diagnosis = "Standard Nuclear Core Motion: Consistent with normal Fermi momentum distribution"
        is_halo = False

    return {
        "measured_fwhm_MeV_c": float(measured_fwhm_MeV_c),
        "goldhaber_fwhm_MeV_c": float(goldhaber_fwhm_MeV_c),
        "width_ratio_to_goldhaber": float(ratio),
        "is_halo_signature": is_halo,
        "diagnosis": diagnosis
    }


def calculate_cluster_soft_e1_sum_rule(Z_core, A_core, Z_halo, A_halo, r_rms_halo_fm=5.0):
    """
    Calculate cluster Thomas-Reiche-Kuhn (TRK) non-energy-weighted dipole sum rule:
    S_cluster(E1) = (9 / (4 * pi)) * e^2 * [ (Z_core * A_halo - Z_halo * A_core) / A_tot ]^2 * <r^2>.
    """
    A_tot = A_core + A_halo
    e_eff = (Z_core * A_halo - Z_halo * A_core) / A_tot
    # B(E1) sum in e^2 fm^2
    b_e1_cluster = (9.0 / (4.0 * np.pi)) * (e_eff ** 2) * (r_rms_halo_fm ** 2)

    return {
        "Z_core": int(Z_core),
        "A_core": float(A_core),
        "Z_halo": int(Z_halo),
        "A_halo": float(A_halo),
        "A_total": float(A_tot),
        "e_eff": float(e_eff),
        "r_rms_halo_fm": float(r_rms_halo_fm),
        "B_E1_cluster_sum_e2_fm2": float(b_e1_cluster)
    }


def estimate_matter_radius_from_reaction_cross_section(sigma_R_mb, A_p, A_t=12.0):
    """
    Invert high-energy reaction cross section sigma_R (e.g. on 12C target at ~800 MeV/u)
    to estimate root-mean-square matter radius R_rms(P) using optical geometric limit:
    sigma_R approx pi * [ R_int(P) + R_int(T) ]^2.
    """
    # 1 mb = 0.1 fm^2 -> sigma_R in fm^2 is sigma_R_mb / 10.0
    sigma_R_fm2 = sigma_R_mb / 10.0
    r_total_int_fm = np.sqrt(sigma_R_fm2 / np.pi)

    # Standard interaction radius of target (e.g. 12C): R_int(12C) approx 2.61 fm
    r_int_target = 0.95 * (A_t ** (1.0 / 3.0)) + 0.45
    r_int_proj = r_total_int_fm - r_int_target

    # Convert interaction radius to approximate RMS matter radius: R_rms approx R_int * 0.90
    r_rms_proj = r_int_proj * 0.90
    r_rms_normal_core = 0.95 * (A_p ** (1.0 / 3.0))

    halo_expansion_percent = ((r_rms_proj - r_rms_normal_core) / r_rms_normal_core) * 100.0

    return {
        "sigma_R_mb": float(sigma_R_mb),
        "A_projectile": float(A_p),
        "A_target": float(A_t),
        "R_int_projectile_fm": float(r_int_proj),
        "R_rms_projectile_fm": float(r_rms_proj),
        "R_rms_normal_reference_fm": float(r_rms_normal_core),
        "relative_radius_expansion_percent": float(halo_expansion_percent)
    }
