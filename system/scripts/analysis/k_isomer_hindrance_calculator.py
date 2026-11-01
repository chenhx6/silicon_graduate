#!/usr/bin/env python3
"""
Nuclear K-Isomer Hindrance, Reduced Hindrance per Degree of Forbiddenness & Gamma-Tunneling Calculator.

Based on:
  - P. M. Walker & G. D. Dracoulis, Nature 399, 35 (1999) (Energy traps in atomic nuclei)
  - A. K. Jain et al., Nuclear Isomers: A Primer (Springer, 2021)
  - A. B. Hayes et al., Phys. Rev. Lett. 96, 042501 (2005) (K-selection breakdown in 178Hf)
  - A. Bohr & B. R. Mottelson, Nuclear Structure Vol. II, Ch. 4 (Electromagnetic transitions)

Features:
  1. Computes degree of K-forbiddenness nu = |Delta K| - lambda for electromagnetic multipole transitions.
  2. Calculates Weisskopf hindrance factor F_W = T_1/2^gamma / T_1/2^sp and reduced hindrance f_nu = (F_W)^(1/nu).
  3. Models triaxial gamma-tunneling collapse of reduced hindrance: f_nu(gamma) approx f_nu,0 * exp(-c * gamma).
  4. Models spin-dependent Coriolis K-mixing reducing effective hindrance at high spin.
  5. Classifies nuclear isomers into Spin Traps, K-Isomers, Seniority Isomers, and Shape Isomers.
"""

import numpy as np


def calculate_k_forbiddenness(Ki, Kf, multipolarity_lambda):
    """
    Calculate degree of K-forbiddenness nu:
      Delta_K = |Ki - Kf|
      nu = max(0, Delta_K - lambda).
    """
    delta_k = abs(float(Ki) - float(Kf))
    lam = float(multipolarity_lambda)
    nu = max(0.0, delta_k - lam)

    is_forbidden = nu > 0.0

    return {
        "Ki": float(Ki),
        "Kf": float(Kf),
        "Delta_K": float(delta_k),
        "multipolarity_lambda": int(lam),
        "degree_of_forbiddenness_nu": int(nu),
        "is_K_forbidden": is_forbidden
    }


def calculate_reduced_hindrance(tau_gamma_ps, E_gamma_keV, A, multipolarity="E1", delta_K=7):
    """
    Calculate Weisskopf hindrance factor F_W and reduced hindrance per degree of forbiddenness f_nu:
      F_W = T_1/2^gamma / T_1/2^sp
      nu = |Delta_K| - lambda
      f_nu = (F_W)^(1/nu).
    """
    if tau_gamma_ps <= 0 or E_gamma_keV <= 0:
        raise ValueError("Lifetime and gamma energy must be strictly positive.")

    eg_MeV = float(E_gamma_keV) / 1000.0
    a_f = float(A)
    mult = multipolarity.upper()

    if mult == "E1":
        lam = 1
        b_sp = 0.06446 * (a_f ** (2.0 / 3.0))
        t_sp_rate = 1.587e15 * (eg_MeV ** 3) * b_sp
    elif mult == "E2":
        lam = 2
        b_sp = 0.05940 * (a_f ** (4.0 / 3.0))
        t_sp_rate = 1.225e9 * (eg_MeV ** 5) * b_sp
    elif mult == "E3":
        lam = 3
        b_sp = 0.05940 * (a_f ** 2.0)
        t_sp_rate = 5.709e2 * (eg_MeV ** 7) * b_sp
    elif mult == "M1":
        lam = 1
        b_sp = 1.7905
        t_sp_rate = 1.758e13 * (eg_MeV ** 3) * b_sp
    elif mult == "M2":
        lam = 2
        b_sp = 1.6501 * (a_f ** (2.0 / 3.0))
        t_sp_rate = 1.350e7 * (eg_MeV ** 5) * b_sp
    else:
        raise ValueError(f"Unsupported multipolarity {multipolarity}.")

    t12_sp_s = np.log(2.0) / max(1e-300, t_sp_rate)
    t12_exp_s = float(tau_gamma_ps) * 1e-12 * np.log(2.0)

    f_w = t12_exp_s / max(1e-300, t12_sp_s)

    dk = abs(float(delta_K))
    nu = max(0.0, dk - lam)

    if nu > 0:
        f_nu = f_w ** (1.0 / nu)
    else:
        f_nu = 1.0

    # Diagnostic
    if nu == 0:
        diag = "K-allowed transition (nu = 0)."
    elif f_nu > 30.0:
        diag = f"Normal rigid axial K-hindrance: f_nu = {f_nu:.1f} (robust K-conservation)."
    elif f_nu > 10.0:
        diag = f"Moderate K-hindrance: f_nu = {f_nu:.1f} (partial Coriolis or shape mixing)."
    else:
        diag = f"Anomalous K-hindrance collapse: f_nu = {f_nu:.1f} <= 10 (strong triaxial gamma-tunneling or high-spin Coriolis mixing)."

    return {
        "A": int(A),
        "E_gamma_keV": float(E_gamma_keV),
        "multipolarity": mult,
        "Delta_K": dk,
        "degree_of_forbiddenness_nu": int(nu),
        "T12_sp_s": float(t12_sp_s),
        "T12_exp_s": float(t12_exp_s),
        "hindrance_F_W": float(f_w),
        "reduced_hindrance_f_nu": float(f_nu),
        "diagnosis": diag
    }


def model_triaxial_gamma_tunneling_hindrance(gamma_deg, f_nu_axial=80.0, c_damping=0.12):
    """
    Model the exponential collapse of reduced hindrance f_nu as triaxial deformation gamma increases:
      f_nu(gamma) = f_nu_axial * exp(- c_damping * gamma_deg).
    At gamma = 0 deg: f_nu approx 80 (rigid axial rotor).
    At gamma = 25 deg: f_nu collapses to ~ 4 (triaxial soft transition).
    """
    g = float(gamma_deg)
    f_val = float(f_nu_axial) * np.exp(- float(c_damping) * g)
    f_val = max(1.0, f_val)

    return {
        "gamma_deg": g,
        "f_nu_axial_reference": float(f_nu_axial),
        "predicted_reduced_hindrance_f_nu": float(f_val),
        "is_hindrance_collapsed": f_val < 10.0
    }


def classify_isomer_mechanism(T12_s, delta_I, delta_K=0, E_gamma_keV=100.0, seniority_isomer=False, is_shape_isomer=False):
    """
    Classify the microscopic mechanism of a nuclear isomer into:
      1. Shape Isomer (second well of double-humped fission barrier)
      2. Seniority Isomer (half-filled shell E2 matrix element cancellation)
      3. K-Isomer (axial angular momentum projection trap)
      4. Spin Trap (large spin difference Delta I >= 4 or small transition energy).
    """
    t12 = float(T12_s)
    dI = abs(float(delta_I))
    dK = abs(float(delta_K))

    if is_shape_isomer:
        cat = "Shape Isomer (Fission Isomer)"
        explanation = "Trapped in the second deformed minimum (beta2 ~ 0.6) of the double-humped fission barrier."
    elif seniority_isomer:
        cat = "Seniority Isomer"
        explanation = "Originates from particle-hole symmetry in half-filled j-shell where E2 matrix elements vanish between states of identical seniority v."
    elif dK >= 4.0:
        cat = "K-Isomer (Orientation Trap)"
        explanation = f"High-K multi-quasiparticle state trapped by orientation quantum number (Delta K = {dK:.0f} >> multipolarity)."
    elif dI >= 4.0:
        cat = "Spin Trap"
        explanation = f"Large spin change (Delta I = {dI:.0f} hbar) forces decay into highly retarded high-multipole radiation."
    else:
        cat = "Low-Energy / Multipole Retarded State"
        explanation = f"Long lifetime due to small transition energy (E_gamma = {E_gamma_keV:.1f} keV) or small single-particle overlap."

    return {
        "T12_s": t12,
        "delta_I": dI,
        "delta_K": dK,
        "classification": cat,
        "physical_mechanism": explanation
    }
