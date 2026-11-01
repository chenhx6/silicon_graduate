#!/usr/bin/env python3
"""
Oslo Method Analyzer: Nuclear Level Density (NLD) & Gamma-Ray Strength Function (gSF).

Based on:
  - A. Schiller et al., Nucl. Instrum. Methods Phys. Res. A 447, 498 (2000) (Oslo Method extraction & Lie group invariance)
  - M. Guttormsen et al., Phys. Scr. T32, 54 (1990) (Subtractive iteration for primary gamma matrix)
  - D. M. Brink, Doctoral thesis, Oxford (1955) & P. Axel, Phys. Rev. 126, 671 (1962) (Brink-Axel hypothesis)
  - A. C. Larsen et al., Phys. Rev. C 83, 034315 (2011) & PRC 108, 025804 (2023) (NLD & gSF normalization protocol)

Features:
  1. Computes total level density at neutron separation energy rho(S_n) from s-wave resonance spacing D_0.
  2. Verifies the continuous 3-parameter Lie group transformation invariance of the primary gamma matrix.
  3. Calibrates raw NLD and transmission coefficient using low-energy discrete levels and high-energy D_0 anchor.
  4. Converts transmission coefficient T(E_gamma) to absolute Gamma-Ray Strength Function f(E_gamma) = T / (2*pi*E_gamma^3).
  5. Diagnoses Upbend / Low-Energy Enhancement (LEE) in dipole photon strength as E_gamma -> 0.
"""

import numpy as np


def calculate_rho_at_sn(D0_eV, I_target, S_n_MeV, A):
    """
    Compute total nuclear level density at neutron separation energy S_n:
    rho(S_n) in MeV^-1 from experimental s-wave resonance spacing D_0 (in eV).
    """
    if D0_eV <= 0:
        raise ValueError("Resonance spacing D_0 must be strictly positive.")

    # Spin cutoff parameter sigma(S_n)
    # Standard parametrization: sigma^2 approx 0.0146 * A^(5/3) * sqrt(U / a)
    a_param = float(A) / 9.0
    u_energy = max(0.5, float(S_n_MeV) - 1.0)
    sigma_sq = max(1.0, 0.0146 * (A ** (5.0 / 3.0)) * np.sqrt(u_energy / a_param))

    i_t = float(I_target)
    if abs(i_t) < 1e-5:
        # Target spin 0 -> s-wave captured into J = 1/2
        # g(J=1/2) = (1 / sigma^2) * exp(-1 / (8 * sigma^2))
        g_spin_sum = (1.0 / sigma_sq) * np.exp(-1.0 / (8.0 * sigma_sq))
    else:
        # Target spin > 0 -> s-wave captured into J1 = I_t - 1/2 and J2 = I_t + 1/2
        j1 = i_t - 0.5
        j2 = i_t + 0.5
        g1 = ((2.0 * j1 + 1.0) / (2.0 * sigma_sq)) * np.exp(-((j1 + 0.5) ** 2) / (2.0 * sigma_sq))
        g2 = ((2.0 * j2 + 1.0) / (2.0 * sigma_sq)) * np.exp(-((j2 + 0.5) ** 2) / (2.0 * sigma_sq))
        g_spin_sum = g1 + g2

    # D_0 is in eV -> convert to MeV (1 MeV = 10^6 eV)
    # rho(S_n) = 1 / ( (D_0 * 10^-6 MeV) * g_spin_sum )
    d0_MeV = D0_eV * 1e-6
    rho_Sn_MeV_inv = 1.0 / (d0_MeV * g_spin_sum)

    return {
        "D0_eV": float(D0_eV),
        "I_target": float(I_target),
        "S_n_MeV": float(S_n_MeV),
        "A": int(A),
        "spin_cutoff_sigma": float(np.sqrt(sigma_sq)),
        "spin_distribution_sum": float(g_spin_sum),
        "rho_Sn_MeV_inv": float(rho_Sn_MeV_inv)
    }


def verify_oslo_lie_transformation_invariance(rho_raw, trans_raw, Ex_bins, Eg_bins, A_factor=1.5, alpha_slope=0.25, B_factor=2.0):
    """
    Verify the 3-parameter continuous Lie group transformation:
      rho_tilde(E_f) = A * exp(alpha * E_f) * rho(E_f)
      T_tilde(E_g)   = B * exp(alpha * E_g) * T(E_g)
    leaves the row-normalized primary gamma matrix P(E_x, E_g) strictly invariant.
    """
    Ex = np.array(Ex_bins, dtype=float)
    Eg = np.array(Eg_bins, dtype=float)
    r = np.array(rho_raw, dtype=float)
    t = np.array(trans_raw, dtype=float)

    n_ex = len(Ex)
    n_eg = len(Eg)

    # Build primary matrix P_raw(i, j) = r(E_f) * t(E_g) where E_f = Ex[i] - Eg[j]
    P_orig = np.zeros((n_ex, n_eg), dtype=float)
    P_trans = np.zeros((n_ex, n_eg), dtype=float)

    for i in range(n_ex):
        for j in range(n_eg):
            if Ex[i] >= Eg[j]:
                ef = Ex[i] - Eg[j]
                # Linear interpolation for rho
                r_val = np.interp(ef, Ex, r)
                t_val = t[j]
                P_orig[i, j] = r_val * t_val

                r_tilde = A_factor * np.exp(alpha_slope * ef) * r_val
                t_tilde = B_factor * np.exp(alpha_slope * Eg[j]) * t_val
                P_trans[i, j] = r_tilde * t_tilde

    # Row normalize both matrices
    row_sum_orig = np.sum(P_orig, axis=1, keepdims=True)
    row_sum_orig[row_sum_orig == 0] = 1.0
    P_norm_orig = P_orig / row_sum_orig

    row_sum_trans = np.sum(P_trans, axis=1, keepdims=True)
    row_sum_trans[row_sum_trans == 0] = 1.0
    P_norm_trans = P_trans / row_sum_trans

    max_abs_diff = float(np.max(np.abs(P_norm_orig - P_norm_trans)))
    is_strictly_invariant = max_abs_diff < 1e-10

    return {
        "A_factor": float(A_factor),
        "alpha_slope": float(alpha_slope),
        "B_factor": float(B_factor),
        "max_absolute_difference": max_abs_diff,
        "is_strictly_invariant": is_strictly_invariant
    }


def calibrate_oslo_nld_and_gsf(Ex_grid, rho_raw, Eg_grid, trans_raw,
                              E_low_anchor_MeV, N_disc_low,
                              Sn_MeV, rho_Sn_MeV_inv,
                              gamma_gamma_total_meV=100.0, D0_eV=100.0):
    """
    Execute the Oslo normalization protocol to determine A, alpha, and B:
      1. Match low-energy discrete count: int_0^E_low A * exp(alpha * E) * rho_raw(E) dE = N_disc.
      2. Match high-energy rho(S_n): A * exp(alpha * S_n) * rho_raw(S_n) = rho_Sn.
      3. Scale T(E_g) by B to normalize total radiation width <Gamma_gamma>.
    """
    Ex = np.array(Ex_grid, dtype=float)
    Eg = np.array(Eg_grid, dtype=float)
    r_raw = np.array(rho_raw, dtype=float)
    t_raw = np.array(trans_raw, dtype=float)

    rho_raw_Sn = float(np.interp(Sn_MeV, Ex, r_raw))
    idx_low = np.where(Ex <= E_low_anchor_MeV)[0]

    # Binary search for slope alpha in range [-2.0, 2.0]
    best_alpha = 0.0
    best_A = 1.0
    min_diff = 1e9

    for alpha in np.linspace(-1.5, 1.5, 301):
        # A from Sn anchor: A = rho_Sn / [exp(alpha * Sn) * rho_raw(Sn)]
        a_val = rho_Sn_MeV_inv / (np.exp(alpha * Sn_MeV) * rho_raw_Sn)
        # Low energy integral
        integrand = a_val * np.exp(alpha * Ex[idx_low]) * r_raw[idx_low]
        integ_val = np.trapz(integrand, Ex[idx_low])
        diff = abs(integ_val - N_disc_low)
        if diff < min_diff:
            min_diff = diff
            best_alpha = alpha
            best_A = a_val

    # Calibrated NLD
    rho_calibrated = best_A * np.exp(best_alpha * Ex) * r_raw

    # Calibrate T(E_gamma) scale B using average radiation width <Gamma_gamma>
    # <Gamma_gamma0> = (D0 / 2pi) * sum int E_g^3 * f(E_g) * rho(Sn - Eg) dEg
    # T_calibrated = B * exp(best_alpha * Eg) * t_raw
    t_shape = np.exp(best_alpha * Eg) * t_raw
    # Integral approximation: sum T_shape * rho(Sn - Eg)
    integrand_t = []
    for g_val, t_val in zip(Eg, t_shape):
        if g_val <= Sn_MeV:
            ef = Sn_MeV - g_val
            r_val = float(np.interp(ef, Ex, rho_calibrated))
            integrand_t.append(t_val * r_val)
        else:
            integrand_t.append(0.0)

    integ_width_raw = np.trapz(integrand_t, Eg)
    # B factor
    # Gamma_gamma in eV is gamma_gamma_total_meV * 1e-3
    gamma_ev = gamma_gamma_total_meV * 1e-3
    # B * integ_width_raw * (D0 / (2pi)) = gamma_ev
    if integ_width_raw > 1e-5:
        best_B = (2.0 * np.pi * gamma_ev) / (D0_eV * integ_width_raw)
    else:
        best_B = 1.0

    t_calibrated = best_B * t_shape

    # Gamma-ray strength function f(E_gamma) = T(E_gamma) / (2 * pi * E_gamma^3) in MeV^-3
    gsf_MeV_inv3 = []
    for g_val, t_val in zip(Eg, t_calibrated):
        if g_val > 0.05:
            gsf_val = t_val / (2.0 * np.pi * (g_val ** 3))
        else:
            gsf_val = 0.0
        gsf_MeV_inv3.append(gsf_val)
    gsf_MeV_inv3 = np.array(gsf_MeV_inv3, dtype=float)

    return {
        "alpha_slope": float(best_alpha),
        "A_factor": float(best_A),
        "B_factor": float(best_B),
        "rho_calibrated": rho_calibrated.tolist(),
        "t_calibrated": t_calibrated.tolist(),
        "gsf_MeV_inv3": gsf_MeV_inv3.tolist(),
        "rho_Sn_actual": float(np.interp(Sn_MeV, Ex, rho_calibrated))
    }


def diagnose_low_energy_enhancement(Eg_grid, gsf_values, E_threshold_MeV=2.5):
    """
    Diagnose whether Gamma-Ray Strength Function exhibits an Upbend / Low-Energy Enhancement (LEE)
    as E_gamma -> 0 below E_threshold_MeV.
    """
    Eg = np.array(Eg_grid, dtype=float)
    f = np.array(gsf_values, dtype=float)

    # Filter to 0.5 MeV <= Eg <= E_threshold_MeV
    idx = np.where((Eg >= 0.5) & (Eg <= E_threshold_MeV))[0]
    if len(idx) < 3:
        return {"has_lee": False, "diagnosis": "Insufficient data points in low-energy region."}

    eg_sub = Eg[idx]
    f_sub = f[idx]

    # Linear fit of log(f) vs Eg to test if df/dEg < 0
    slope, intercept = np.polyfit(eg_sub, np.log(np.maximum(1e-15, f_sub)), 1)
    min_val = np.min(f_sub)
    start_val = f_sub[0]

    enhancement_ratio = start_val / max(1e-15, min_val)

    if slope < -0.3 and enhancement_ratio > 1.8:
        has_lee = True
        diagnosis = (f"Distinct Low-Energy Enhancement (Upbend) observed: slope={slope:.2f}, "
                     f"enhancement ratio={enhancement_ratio:.2f}x. Likely M1 shears / quasiparticle transitions.")
    else:
        has_lee = False
        diagnosis = (f"Standard Brink-Axel / Lorentzian tail behavior: slope={slope:.2f}, "
                     f"enhancement ratio={enhancement_ratio:.2f}x. No significant upbend.")

    return {
        "has_lee": has_lee,
        "slope_log_f": float(slope),
        "enhancement_ratio": float(enhancement_ratio),
        "diagnosis": diagnosis
    }
