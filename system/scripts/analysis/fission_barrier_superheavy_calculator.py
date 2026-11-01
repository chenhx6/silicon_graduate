#!/usr/bin/env python3
"""
Nuclear Fission Barriers, Strutinsky Shell Correction & Superheavy Element Synthesis Calculator.

Based on:
  - N. Bohr & J. A. Wheeler, Phys. Rev. 56, 426 (1939) (Mechanism of nuclear fission)
  - V. M. Strutinsky, Nucl. Phys. A 95, 420 (1967) (Shell corrections & double-humped barriers)
  - R. Vandenbosch & J. R. Huizenga, Nuclear Fission (1973) (Statistical Gamma_n / Gamma_f ratio)
  - C. A. Bertulani & P. Danielewicz, Introduction to Nuclear Reactions, Ch. 5 (Fusion and Fission)
  - Yu. Ts. Oganessian & V. K. Utyonkov, Rep. Prog. Phys. 78, 036301 (2015) (Superheavy elements)

Features:
  1. Calculates liquid drop model fissility parameter x = (Z^2/A) / (Z^2/A)_crit and macroscopic LDM fission barrier.
  2. Evaluates Hill-Wheeler quantum transmission probability across parabolic fission barrier.
  3. Computes Vandenbosch-Huizenga Gamma_n / Gamma_f statistical branching ratio with shell thermal damping.
  4. Models multi-step neutron evaporation survival probability P_surv = prod(Gamma_n / (Gamma_n + Gamma_f)).
  5. Estimates superheavy element residue cross section sigma_ER = sigma_cap * P_CN * P_surv (in pb / fb / nb).
"""

import numpy as np


def calculate_liquid_drop_fissility(Z, A):
    """
    Calculate macroscopic liquid drop model (LDM) fissility parameter x and barrier height.
    x = (Z^2 / A) / (Z^2 / A)_crit,
    where (Z^2 / A)_crit = 50.883 * [1 - 1.7826 * ((N - Z)/A)^2].
    """
    N = A - Z
    asym = (N - Z) / float(A)
    asym_sq = asym ** 2

    crit_limit = 50.883 * (1.0 - 1.7826 * asym_sq)
    z2_a = (float(Z) ** 2) / float(A)
    x = z2_a / crit_limit

    # Surface energy constant E_s0
    e_s0 = 17.9439 * (1.0 - 1.7826 * asym_sq) * (A ** (2.0 / 3.0))

    if x < 0.675:
        f_x = 0.38 * ((1.0 - x) ** 3)
    elif x < 1.0:
        f_x = 0.83 * ((1.0 - x) ** 3)
    else:
        f_x = 0.0

    b_f_ldm_MeV = e_s0 * f_x

    return {
        "Z": int(Z),
        "A": int(A),
        "N": int(N),
        "asymmetry": float(asym),
        "Z2_over_A": float(z2_a),
        "Z2_over_A_crit": float(crit_limit),
        "fissility_x": float(x),
        "surface_energy_E_s0_MeV": float(e_s0),
        "liquid_drop_barrier_MeV": float(b_f_ldm_MeV)
    }


def calculate_hill_wheeler_penetration(E_excitation_MeV, V_barrier_MeV, hbar_omega_MeV=0.7):
    """
    Calculate Hill-Wheeler transmission coefficient across parabolic barrier:
    T(E) = 1 / [1 + exp(2 * pi * (V - E) / (hbar * omega))].
    """
    diff = float(V_barrier_MeV - E_excitation_MeV)
    exponent = 2.0 * np.pi * diff / float(hbar_omega_MeV)
    # Prevent numerical overflow
    if exponent > 60.0:
        prob = 0.0
    elif exponent < -60.0:
        prob = 1.0
    else:
        prob = 1.0 / (1.0 + np.exp(exponent))

    return {
        "E_excitation_MeV": float(E_excitation_MeV),
        "V_barrier_MeV": float(V_barrier_MeV),
        "hbar_omega_MeV": float(hbar_omega_MeV),
        "transmission_probability": float(prob)
    }


def calculate_gamma_n_over_gamma_f(E_star_MeV, B_n_MeV, B_f_nominal_MeV, A, B_f_ldm_MeV=0.5, a_n=None, a_f_over_a_n=1.05, E_D_MeV=18.5):
    """
    Calculate Vandenbosch-Huizenga statistical branching ratio Gamma_n / Gamma_f
    incorporating thermal damping of the microscopic shell correction.
    B_f(E*) = B_f_ldm + (B_f_nominal - B_f_ldm) * exp(-E* / E_D).
    """
    if a_n is None:
        a_n = float(A) / 9.5
    a_f = a_n * float(a_f_over_a_n)

    # Thermal damping of shell correction
    damping_factor = np.exp(-float(E_star_MeV) / float(E_D_MeV))
    b_f_eff = float(B_f_ldm_MeV) + (float(B_f_nominal_MeV) - float(B_f_ldm_MeV)) * damping_factor
    b_f_eff = max(0.1, b_f_eff)

    u_n = max(0.01, float(E_star_MeV - B_n_MeV))
    u_f = max(0.01, float(E_star_MeV - b_f_eff))

    temp = np.sqrt(E_star_MeV / a_n)
    # Pre-exponential factor C approx 0.14 * A^(2/3) * sqrt(T) / (2 * sqrt(pi * a_f))
    c_pre = 0.14 * (A ** (2.0 / 3.0)) * np.sqrt(max(0.1, temp)) / (2.0 * np.sqrt(np.pi * a_f))

    exp_arg = 2.0 * (np.sqrt(a_n * u_n) - np.sqrt(a_f * u_f))
    exp_arg = min(50.0, max(-50.0, exp_arg))
    ratio = c_pre * np.exp(exp_arg)

    # Survival fraction in this single step: P_1 = Gamma_n / (Gamma_n + Gamma_f)
    p_survival_step = ratio / (1.0 + ratio)

    return {
        "E_star_MeV": float(E_star_MeV),
        "B_n_MeV": float(B_n_MeV),
        "B_f_nominal_MeV": float(B_f_nominal_MeV),
        "B_f_effective_MeV": float(b_f_eff),
        "shell_damping_factor": float(damping_factor),
        "a_n": float(a_n),
        "a_f": float(a_f),
        "gamma_n_over_gamma_f": float(ratio),
        "survival_fraction_step": float(p_survival_step)
    }


def estimate_superheavy_cross_section(sigma_cap_mb, P_cn, E_star_initial_MeV, B_n_list_MeV, B_f_list_MeV, A_compound, B_f_ldm_MeV=0.5, xn=3):
    """
    Estimate superheavy evaporation residue cross section:
    sigma_ER = sigma_cap * P_CN * P_surv,
    where P_surv = prod_{i=1}^{xn} [Gamma_n / (Gamma_n + Gamma_f)]_i.
    """
    e_star = float(E_star_initial_MeV)
    p_surv_total = 1.0
    steps = []

    for step_idx in range(xn):
        b_n = B_n_list_MeV[step_idx] if step_idx < len(B_n_list_MeV) else B_n_list_MeV[-1]
        b_f = B_f_list_MeV[step_idx] if step_idx < len(B_f_list_MeV) else B_f_list_MeV[-1]
        a_curr = A_compound - step_idx

        branch = calculate_gamma_n_over_gamma_f(e_star, b_n, b_f, a_curr, B_f_ldm_MeV=B_f_ldm_MeV)
        p_step = branch["survival_fraction_step"]
        p_surv_total *= p_step

        steps.append({
            "step": step_idx + 1,
            "E_star_MeV": e_star,
            "B_n_MeV": b_n,
            "B_f_eff_MeV": branch["B_f_effective_MeV"],
            "gamma_n_over_gamma_f": branch["gamma_n_over_gamma_f"],
            "step_survival": p_step
        })
        # After emitting a neutron, excitation energy drops by B_n + average kinetic energy (2*T)
        temp = np.sqrt(e_star / (a_curr / 9.5))
        e_star = max(1.0, e_star - b_n - 2.0 * temp)

    # sigma_cap in mb, sigma_ER in mb
    sigma_er_mb = float(sigma_cap_mb) * float(P_cn) * p_surv_total
    # Convert to picobarns (1 mb = 10^9 pb)
    sigma_er_pb = sigma_er_mb * 1e9

    return {
        "sigma_cap_mb": float(sigma_cap_mb),
        "P_cn": float(P_cn),
        "xn_channels": int(xn),
        "P_surv_total": float(p_surv_total),
        "sigma_ER_mb": float(sigma_er_mb),
        "sigma_ER_pb": float(sigma_er_pb),
        "step_details": steps
    }
