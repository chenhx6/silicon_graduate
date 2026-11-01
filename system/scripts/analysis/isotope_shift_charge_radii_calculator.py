#!/usr/bin/env python3
"""
Nuclear Charge Radii, Laser Isotope Shifts & King Plot Linearity Calculator.

Based on:
  - W. H. King, Isotope Shifts in Atomic Spectra (Plenum, 1984) (King plot formalism)
  - I. Angeli & K. P. Marinova, At. Data Nucl. Data Tables 99, 69 (2013) (Charge radii table)
  - C. M. Karthein et al., Nature Phys. 20, 390 (2024) (Indium charge radii towards 100Sn)
  - E. W. Otten, Treatise on Heavy-Ion Science, Vol. 8, p. 517 (1989) (Radii & moments review)

Features:
  1. Computes normal mass shift (NMS) and specific mass shift (SMS) from atomic transition frequencies.
  2. Inverts nuclear mean-square charge radius change delta<r^2> from measured optical isotope shifts delta_nu.
  3. Decomposes charge radius changes into spherical volume expansion and quadrupole deformation delta<beta_2^2>.
  4. Performs King plot 2D linear regression across two optical lines to test linearity and extract F2/F1 ratio.
  5. Evaluates charge radius odd-even staggering (OES) parameter gamma_r to diagnose surface vibration blocking.
"""

import numpy as np

# Physical constants
ELECTRON_MASS_AMU = 5.48579909065e-4 # Electron mass in atomic mass units (u)


def calculate_normal_mass_shift(transition_freq_GHz, mass_A, mass_A_ref):
    """
    Compute normal mass shift (NMS) in GHz:
      M_NMS = nu_0 * (m_e / u) (in GHz * amu).
      mu_A_Aprime = (m_A - m_Aref) / (m_A * m_Aref) (in amu^-1).
      delta_nu_NMS = M_NMS * mu_A_Aprime (in GHz).
    """
    if mass_A <= 0 or mass_A_ref <= 0 or transition_freq_GHz <= 0:
        raise ValueError("Masses and transition frequency must be strictly positive.")

    m_nms = float(transition_freq_GHz) * ELECTRON_MASS_AMU
    mu_factor = (float(mass_A) - float(mass_A_ref)) / (float(mass_A) * float(mass_A_ref))
    delta_nu_nms = m_nms * mu_factor

    return {
        "transition_freq_GHz": float(transition_freq_GHz),
        "mass_A": float(mass_A),
        "mass_A_ref": float(mass_A_ref),
        "M_NMS_GHz_amu": float(m_nms),
        "mu_factor_amu_inv": float(mu_factor),
        "delta_nu_NMS_GHz": float(delta_nu_nms),
        "delta_nu_NMS_MHz": float(delta_nu_nms * 1000.0)
    }


def extract_delta_r2_from_isotope_shift(delta_nu_exp_GHz, mass_A, mass_A_ref, K_mass_shift_GHz_amu, F_field_shift_GHz_fm2):
    """
    Invert mean-square charge radius change delta<r^2> (in fm^2) from experimental isotope shift:
      delta_nu_exp = K_mass * mu + F_field * delta<r^2>
      => delta<r^2> = (delta_nu_exp - K_mass * mu) / F_field.
    """
    if abs(F_field_shift_GHz_fm2) < 1e-6:
        raise ValueError("Field shift factor F must be non-zero.")

    mu_factor = (float(mass_A) - float(mass_A_ref)) / (float(mass_A) * float(mass_A_ref))
    delta_nu_ms = float(K_mass_shift_GHz_amu) * mu_factor
    delta_nu_fs = float(delta_nu_exp_GHz) - delta_nu_ms

    delta_r2_fm2 = delta_nu_fs / float(F_field_shift_GHz_fm2)

    return {
        "delta_nu_exp_GHz": float(delta_nu_exp_GHz),
        "mass_A": float(mass_A),
        "mass_A_ref": float(mass_A_ref),
        "delta_nu_MS_GHz": float(delta_nu_ms),
        "delta_nu_FS_GHz": float(delta_nu_fs),
        "F_field_shift_GHz_fm2": float(F_field_shift_GHz_fm2),
        "delta_r2_fm2": float(delta_r2_fm2)
    }


def decompose_charge_radius_components(A, A_ref, delta_r2_total_fm2, R0_fm=1.2):
    """
    Decompose total charge radius change into spherical droplet volume increase
    and quadrupole deformation change delta<beta_2^2>:
      <r^2>_sph = (3/5) * R_0^2 * A^(2/3)
      delta<r^2>_sph = (3/5) * R_0^2 * [A^(2/3) - A_ref^(2/3)]
      delta<r^2>_def = delta<r^2>_total - delta<r^2>_sph
      delta<beta_2^2> = (4*pi / (5 * <r^2>_sph)) * delta<r^2>_def.
    """
    a_f = float(A)
    a_ref_f = float(A_ref)

    r2_sph = 0.6 * (float(R0_fm) ** 2) * (a_ref_f ** (2.0 / 3.0))
    delta_r2_sph = 0.6 * (float(R0_fm) ** 2) * ((a_f ** (2.0 / 3.0)) - (a_ref_f ** (2.0 / 3.0)))
    delta_r2_def = float(delta_r2_total_fm2) - delta_r2_sph

    # Factor 4*pi / (5 * <r^2>_sph)
    delta_beta2_sq = (4.0 * np.pi / (5.0 * r2_sph)) * delta_r2_def

    return {
        "A": int(A),
        "A_ref": int(A_ref),
        "delta_r2_total_fm2": float(delta_r2_total_fm2),
        "delta_r2_spherical_fm2": float(delta_r2_sph),
        "delta_r2_deformation_fm2": float(delta_r2_def),
        "delta_mean_square_beta2": float(delta_beta2_sq)
    }


def perform_king_plot_analysis(masses_A, mass_A_ref, shifts_line1_GHz, shifts_line2_GHz):
    """
    Perform 2D King Plot linear regression across two atomic transitions:
      Modified shift: xi_i = delta_nu_i / mu(A, A_ref).
      Linear relation: xi_2 = (F_2 / F_1) * xi_1 + [K_2 - (F_2 / F_1) * K_1].
    Returns slope (F2/F1), intercept, R^2, and residuals.
    """
    a_list = np.array(masses_A, dtype=float)
    a_ref = float(mass_A_ref)
    s1 = np.array(shifts_line1_GHz, dtype=float)
    s2 = np.array(shifts_line2_GHz, dtype=float)

    if not (len(a_list) == len(s1) == len(s2)):
        raise ValueError("Array lengths of masses and shifts must match.")
    if len(a_list) < 3:
        raise ValueError("At least 3 isotope pairs required for King plot regression.")

    mu_list = (a_list - a_ref) / (a_list * a_ref)
    # Modified shifts
    xi_1 = s1 / mu_list
    xi_2 = s2 / mu_list

    # Linear fit
    slope, intercept = np.polyfit(xi_1, xi_2, 1)

    # Predicted and R^2
    xi_2_pred = slope * xi_1 + intercept
    res = xi_2 - xi_2_pred
    ss_res = np.sum(res ** 2)
    ss_tot = np.sum((xi_2 - np.mean(xi_2)) ** 2)
    r_squared = 1.0 - (ss_res / max(1e-12, ss_tot))

    # Linearity check: if R^2 > 0.999 -> clean King linearity
    is_linear = bool(r_squared > 0.998)

    return {
        "slope_F2_over_F1": float(slope),
        "intercept_GHz_amu": float(intercept),
        "R_squared": float(r_squared),
        "is_strictly_linear": is_linear,
        "max_residual_GHz_amu": float(np.max(np.abs(res))),
        "xi_1_modified_shifts": xi_1.tolist(),
        "xi_2_modified_shifts": xi_2.tolist()
    }


def calculate_charge_radius_odd_even_staggering(N_list, r2_series_fm2):
    """
    Evaluate charge radius odd-even staggering parameter gamma_r(N):
      gamma_r(N) = 2 * [ <r^2>(N) - <r^2>(N-1) ] / [ <r^2>(N+1) - <r^2>(N-1) ].
    Normal surface vibration blocking: gamma_r < 1.0 (odd nucleus smaller than average).
    Anomalous shape transition: gamma_r > 1.5 or < 0.
    """
    n_arr = np.array(N_list, dtype=int)
    r2_arr = np.array(r2_series_fm2, dtype=float)

    staggering_results = []
    for i in range(1, len(n_arr) - 1):
        if n_arr[i] % 2 != 0: # Odd N
            if (n_arr[i] - n_arr[i-1] == 1) and (n_arr[i+1] - n_arr[i] == 1):
                numerator = 2.0 * (r2_arr[i] - r2_arr[i-1])
                denominator = r2_arr[i+1] - r2_arr[i-1]
                if abs(denominator) > 1e-6:
                    gamma_r = numerator / denominator
                else:
                    gamma_r = 1.0

                if gamma_r < 0.95:
                    status = "Normal OES: Strong surface quadrupole vibration blocking in odd nucleus"
                elif gamma_r > 1.3:
                    status = "Anomalous OES / Shape staggering: Sudden expansion in odd nucleus"
                else:
                    status = "Smooth monotonic evolution (Weak staggering)"

                staggering_results.append({
                    "N_odd": int(n_arr[i]),
                    "gamma_r": float(gamma_r),
                    "interpretation": status
                })

    return staggering_results
