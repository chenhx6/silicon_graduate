#!/usr/bin/env python3
"""
Multi-Nucleon Transfer (MNT), Deep Inelastic Collisions (DIC) & N=126 Factory Calculator.

Based on:
  - V. V. Volkov, Phys. Rep. 44, 93 (1978) (Deep inelastic transfer reactions review)
  - J. Wilczynski, Phys. Lett. B 47, 484 (1973) (Wilczynski plot & energy loss vs angle)
  - V. I. Zagrebaev & W. Greiner, Phys. Rev. Lett. 101, 122701 (2008) (MNT production of heavy neutron-rich nuclei)
  - V. I. Zagrebaev & W. Greiner, Phys. Rev. C 83, 044618 (2011) (136Xe + 208Pb MNT dynamics)
  - C. A. Bertulani & P. Danielewicz, Introduction to Nuclear Reactions, Ch. 8-9

Features:
  1. Computes Wilczynski energy dissipation, entrance/exit Coulomb barriers, and maximum kinetic energy loss TKEL_max.
  2. Evaluates the driving potential V_dr(Z, N) on the potential energy surface governing nucleon drift.
  3. Models ultrafast charge equilibration (N/Z equilibration) towards the bottom of the potential valley.
  4. Calculates thermal excitation energy partition between primary fragments and post-collision neutron evaporation.
  5. Estimates MNT production cross sections for exotic heavy neutron-rich nuclei (e.g. around N=126).
"""

import numpy as np

# Physical constants
E2_CONST_MEV_FM = 1.439965  # e^2 in MeV * fm


def calculate_liquid_drop_binding_energy(Z, N):
    """
    Compute Bethe-Weizsacker liquid drop binding energy B(Z, N) in MeV.
    B = a_v*A - a_s*A^(2/3) - a_c*Z^2/A^(1/3) - a_sym*(N-Z)^2/A.
    """
    z_f = float(Z)
    n_f = float(N)
    a_f = z_f + n_f
    if a_f <= 0:
        return 0.0

    a_v = 15.67
    a_s = 17.23
    a_c = 0.714
    a_sym = 23.285

    b_val = (a_v * a_f -
             a_s * (a_f ** (2.0 / 3.0)) -
             a_c * (z_f ** 2) / (a_f ** (1.0 / 3.0)) -
             a_sym * ((n_f - z_f) ** 2) / a_f)
    return b_val


def calculate_wilczynski_energy_loss_and_orbiting(Elab_MeV_u, Ap, Zp, At, Zt, d_scission_fm=2.5):
    """
    Calculate Wilczynski plot energy dissipation kinematics:
      E_lab = Elab_MeV_u * Ap
      E_cm = E_lab * At / (Ap + At)
      V_coul = Zp * Zt * e^2 / (Rp + Rt)
      V_exit = Zp * Zt * e^2 / (Rp + Rt + d_scission)
      TKEL_max = E_cm - V_exit.
    """
    if Elab_MeV_u <= 0:
        raise ValueError("Beam energy must be strictly positive.")

    e_lab = float(Elab_MeV_u) * float(Ap)
    e_cm = e_lab * (float(At) / (float(Ap) + float(At)))

    rp = 1.2 * (float(Ap) ** (1.0 / 3.0))
    rt = 1.2 * (float(At) ** (1.0 / 3.0))
    r_contact = rp + rt
    r_sciss = r_contact + float(d_scission_fm)

    v_coul = (E2_CONST_MEV_FM * float(Zp) * float(Zt)) / r_contact
    v_exit = (E2_CONST_MEV_FM * float(Zp) * float(Zt)) / r_sciss

    tkel_max = max(0.0, e_cm - v_exit)
    energy_above_barrier = e_cm - v_coul

    # Grazing angular momentum
    # mu in amu
    mu_amu = (float(Ap) * float(At)) / (float(Ap) + float(At))
    if energy_above_barrier > 0:
        # L_graz approx 0.2199 * R_contact * sqrt(mu * (Ecm - V_coul))
        l_graz = 0.2199 * r_contact * np.sqrt(mu_amu * energy_above_barrier)
    else:
        l_graz = 0.0

    return {
        "E_lab_MeV": float(e_lab),
        "E_cm_MeV": float(e_cm),
        "R_contact_fm": float(r_contact),
        "R_scission_fm": float(r_sciss),
        "V_Coul_contact_MeV": float(v_coul),
        "V_exit_barrier_MeV": float(v_exit),
        "energy_above_barrier_MeV": float(energy_above_barrier),
        "L_grazing_hbar": float(l_graz),
        "TKEL_max_MeV": float(tkel_max)
    }


def calculate_charge_equilibration(Ap, Zp, At, Zt):
    """
    Model fast N/Z charge equilibration in the dinuclear system:
    (N/Z)_system = (Np + Nt) / (Zp + Zt).
    For a given fragment mass A1, equilibrated charge Z1_eq = A1 / [1 + (N/Z)_sys].
    """
    zp = float(Zp)
    np_n = float(Ap) - zp
    zt = float(Zt)
    nt_n = float(At) - zt

    nz_sys = (np_n + nt_n) / (zp + zt)
    nz_proj = np_n / zp
    nz_targ = nt_n / zt

    # Equilibrated charge for projectile-like fragment of mass Ap
    z1_eq_proj = float(Ap) / (1.0 + nz_sys)
    z2_eq_targ = float(At) / (1.0 + nz_sys)

    return {
        "N_over_Z_projectile": float(nz_proj),
        "N_over_Z_target": float(nz_targ),
        "N_over_Z_system_equilibrated": float(nz_sys),
        "Z1_equilibrated_for_Ap": float(z1_eq_proj),
        "Z2_equilibrated_for_At": float(z2_eq_targ)
    }


def calculate_driving_potential(Z1, N1, Z_proj, N_proj, Z_targ, N_targ, d_sep_fm=2.5):
    """
    Compute dinuclear driving potential V_dr(Z1, N1) on the potential energy surface:
    V_dr = - [B(Z1, N1) + B(Z2, N2)] + V_Coul(Z1, Z2) - ( -[B(Zp, Np) + B(Zt, Nt)] + V_Coul_0 ).
    """
    z_tot = int(Z_proj + Z_targ)
    n_tot = int(N_proj + N_targ)

    z1_val = int(Z1)
    n1_val = int(N1)
    z2_val = z_tot - z1_val
    n2_val = n_tot - n1_val

    a1 = z1_val + n1_val
    a2 = z2_val + n2_val
    a_proj = Z_proj + N_proj
    a_targ = Z_targ + N_targ

    # Binding energies
    b1 = calculate_liquid_drop_binding_energy(z1_val, n1_val)
    b2 = calculate_liquid_drop_binding_energy(z2_val, n2_val)
    bp = calculate_liquid_drop_binding_energy(Z_proj, N_proj)
    bt = calculate_liquid_drop_binding_energy(Z_targ, N_targ)

    r_touch = 1.2 * ((a1 ** (1.0 / 3.0)) + (a2 ** (1.0 / 3.0))) + float(d_sep_fm)
    r_touch0 = 1.2 * ((a_proj ** (1.0 / 3.0)) + (a_targ ** (1.0 / 3.0))) + float(d_sep_fm)

    v_coul = (E2_CONST_MEV_FM * z1_val * z2_val) / r_touch
    v_coul0 = (E2_CONST_MEV_FM * Z_proj * Z_targ) / r_touch0

    v_dr = (- (b1 + b2) + v_coul) - (- (bp + bt) + v_coul0)

    return {
        "Z1": z1_val,
        "N1": n1_val,
        "A1": a1,
        "Z2": z2_val,
        "N2": n2_val,
        "A2": a2,
        "V_driving_potential_MeV": float(v_dr)
    }


def calculate_fragment_thermal_excitation_and_evaporation(TKEL_MeV, A1_prim, Z1_prim, A2_prim, Z2_prim, Bn1_MeV=7.0, Bn2_MeV=6.5):
    """
    Model thermal partition of total kinetic energy loss (TKEL) between primary fragments:
      E1* = TKEL * A1 / (A1 + A2)
      E2* = TKEL * A2 / (A1 + A2)
    and predict average number of evaporated neutrons:
      <xn1> approx E1* / (Bn1 + 2*T1).
    """
    tkel = float(TKEL_MeV)
    a1 = float(A1_prim)
    a2 = float(A2_prim)
    a_tot = a1 + a2

    e1_star = tkel * (a1 / a_tot)
    e2_star = tkel * (a2 / a_tot)

    # Nuclear temperature T = sqrt(E* / a_level) with a_level = A / 9.5
    t1 = np.sqrt(max(0.1, e1_star) / (a1 / 9.5))
    t2 = np.sqrt(max(0.1, e2_star) / (a2 / 9.5))

    # Evaporated neutrons
    xn1 = e1_star / (float(Bn1_MeV) + 2.0 * t1)
    xn2 = e2_star / (float(Bn2_MeV) + 2.0 * t2)

    a1_cold = a1 - xn1
    a2_cold = a2 - xn2

    return {
        "TKEL_MeV": tkel,
        "E1_star_MeV": float(e1_star),
        "E2_star_MeV": float(e2_star),
        "T1_temperature_MeV": float(t1),
        "T2_temperature_MeV": float(t2),
        "neutrons_evaporated_frag1": float(xn1),
        "neutrons_evaporated_frag2": float(xn2),
        "A1_cold_residue": float(a1_cold),
        "A2_cold_residue": float(a2_cold)
    }


def predict_mnt_cross_section(sigma_dic_mb, delta_Z, delta_N, TKEL_MeV=80.0):
    """
    Estimate multi-nucleon transfer cross section sigma_MNT (in microbarns/millibarns):
    Gaussian distribution in delta_Z and delta_N with variance sigma_A^2 propto TKEL.
    """
    dz = float(delta_Z)
    dn = float(delta_N)
    da = dz + dn

    # Mass variance increases with TKEL: sigma_A^2 approx 0.15 * TKEL
    var_a = max(1.0, 0.15 * float(TKEL_MeV))
    prob_a = np.exp(- (da ** 2) / (2.0 * var_a)) / np.sqrt(2.0 * np.pi * var_a)

    # Charge variance
    var_z = max(0.5, 0.05 * float(TKEL_MeV))
    prob_z = np.exp(- (dz ** 2) / (2.0 * var_z)) / np.sqrt(2.0 * np.pi * var_z)

    prob_total = prob_a * prob_z
    sigma_mnt_mb = float(sigma_dic_mb) * prob_total
    sigma_mnt_microbarn = sigma_mnt_mb * 1000.0

    return {
        "sigma_dic_mb": float(sigma_dic_mb),
        "delta_Z": int(dz),
        "delta_N": int(dn),
        "delta_A": int(da),
        "mass_variance_sigma_A2": float(var_a),
        "transfer_probability": float(prob_total),
        "sigma_MNT_mb": float(sigma_mnt_mb),
        "sigma_MNT_microbarn": float(sigma_mnt_microbarn)
    }
