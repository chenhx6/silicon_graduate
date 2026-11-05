#!/usr/bin/env python3
"""
Nuclear Band Termination, Transition Quadrupole Moment Collapse & CNS Alignment Calculator.

Based on:
  - T. Bengtsson & I. Ragnarsson, Nucl. Phys. A 436, 14 (1985) (Cranked Nilsson-Strutinsky formalism)
  - A. V. Afanasjev et al., Phys. Rep. 322, 1 (1999) (Termination of rotational bands review)
  - R. Wadsworth et al., Phys. Rev. Lett. 80, 1174 (1998) (Experimental Qt collapse in 109Sb)
  - S. Frauendorf, Rev. Mod. Phys. 73, 463 (2001) (Spontaneous symmetry breaking in rotating nuclei)

Features:
  1. Calculates exact maximal valence-space aligned angular momentum I_max from orbital configurations.
  2. Models the collapse of transition quadrupole moment Q_t(I) -> 0 along triaxial trajectory gamma -> 60 deg.
  3. Computes rigid rotor energy subtraction E - E_RR to identify the characteristic band termination downward cusp.
  4. Evaluates dynamic moment of inertia J^(2) to detect centrifugal steep dive at termination.
  5. Diagnoses smooth band termination against backbending and conventional crossing alternatives.
"""

import numpy as np


def calculate_valence_maximum_spin(valence_orbitals_protons, valence_orbitals_neutrons):
    """
    Calculate the theoretical maximum aligned angular momentum I_max from a set of valence orbitals.
    Each orbital is defined as a tuple: (j, occupation_number).
    Max aligned projection for n nucleons in orbital j is the sum of highest m_j:
      m_max = sum_{k=0}^{n-1} (j - k).
    """
    def sum_orbital_max(orbitals):
        total_m = 0.0
        for j_val, occ in orbitals:
            j_f = float(j_val)
            occ_n = int(occ)
            max_occ = int(2 * j_f + 1)
            if occ_n > max_occ:
                raise ValueError(f"Occupation {occ_n} exceeds maximum allowed {max_occ} for j={j_val}")
            for k in range(occ_n):
                total_m += (j_f - k)
        return total_m

    i_max_p = sum_orbital_max(valence_orbitals_protons)
    i_max_n = sum_orbital_max(valence_orbitals_neutrons)
    total_i_max = i_max_p + i_max_n

    return {
        "I_max_protons": float(i_max_p),
        "I_max_neutrons": float(i_max_n),
        "I_max_total": float(total_i_max)
    }


def model_transition_quadrupole_collapse(spins, Q0_eb, I_start, I_term):
    """
    Model the smooth collapse of transition quadrupole moment Q_t(I) and B(E2; I -> I-2)
    as the nuclear shape evolves along the triaxial path gamma: 0 deg (prolate) -> 60 deg (oblate).
    Q_t(I) = Q_0 * [cos(gamma(I) + 30 deg) / cos(30 deg)].
    B(E2; I -> I-2) = (5 / 16pi) * e^2 * Q_t(I)^2 * <I 0 2 0 | I-2 0>^2.
    """
    sp = np.array(spins, dtype=float)
    i_s = float(I_start)
    i_t = float(I_term)

    if i_t <= i_s:
        raise ValueError("Termination spin I_term must be strictly greater than start spin I_start.")

    results = []
    cos30 = np.cos(np.radians(30.0))

    for spin in sp:
        # Interpolate gamma angle from 0 to 60 deg
        frac = min(1.0, max(0.0, (spin - i_s) / (i_t - i_s)))
        gamma_deg = 60.0 * frac

        # Q_t formula
        cos_term = np.cos(np.radians(gamma_deg + 30.0))
        q_t = float(Q0_eb * (cos_term / cos30))
        q_t = max(0.0, q_t)

        # Clebsch-Gordan squared: <I 0 2 0 | I-2 0>^2 = 3*I*(I-1) / [2*(2I-1)*(2I+1)]
        if spin >= 2.0:
            cg_sq = (3.0 * spin * (spin - 1.0)) / (2.0 * (2.0 * spin - 1.0) * (2.0 * spin + 1.0))
            b_e2 = (5.0 / (16.0 * np.pi)) * (q_t ** 2) * cg_sq
        else:
            b_e2 = 0.0

        results.append({
            "spin": float(spin),
            "gamma_deg": float(gamma_deg),
            "Q_t_eb": float(q_t),
            "B_E2_e2b2": float(b_e2)
        })

    q_initial = results[0]["Q_t_eb"]
    q_final = results[-1]["Q_t_eb"]
    drop_percent = ((q_initial - q_final) / max(1e-5, q_initial)) * 100.0

    return {
        "I_start": i_s,
        "I_term": i_t,
        "Q0_eb": float(Q0_eb),
        "Q_t_drop_percent": float(drop_percent),
        "trajectory": results
    }


def calculate_rigid_rotor_subtraction(spins, energies_keV, A, J_factor=0.015):
    """
    Compute rigid rotor subtraction: E_diff(I) = E(I) - (hbar^2 / 2J_RR) * I(I + 1),
    where hbar^2 / 2J_RR approx A^(-5/3) / J_factor (in MeV).
    A characteristic downward cusp in E - E_RR marks the band termination state.
    """
    sp = np.array(spins, dtype=float)
    en_MeV = np.array(energies_keV, dtype=float) / 1000.0

    h2_2j = (float(A) ** (-5.0 / 3.0)) / float(J_factor)

    e_diff = en_MeV - h2_2j * sp * (sp + 1.0)
    min_idx = int(np.argmin(e_diff))
    cusp_spin = float(sp[min_idx])
    cusp_energy_diff = float(e_diff[min_idx])

    return {
        "A": int(A),
        "h2_over_2J_RR_MeV": float(h2_2j),
        "spins": sp.tolist(),
        "E_minus_E_RR_MeV": e_diff.tolist(),
        "cusp_spin": cusp_spin,
        "cusp_min_E_diff_MeV": cusp_energy_diff
    }


def calculate_dynamic_moment_of_inertia_j2(spins, energies_keV):
    """
    Calculate dynamic moment of inertia J^(2) = 4 / [E_gamma(I+2) - E_gamma(I)].
    At band termination, Delta E_gamma widens dramatically, causing J^(2) to plunge steeply.
    """
    sp = np.array(spins, dtype=float)
    en = np.array(energies_keV, dtype=float) / 1000.0 # MeV

    # First calculate transition energies E_gamma(I -> I-2)
    e_gamma = []
    sp_mid = []
    for i in range(1, len(sp)):
        dI = sp[i] - sp[i-1]
        if abs(dI - 2.0) < 0.1: # Delta I = 2 cascade
            eg = en[i] - en[i-1]
            e_gamma.append(eg)
            sp_mid.append(sp[i])

    # Now calculate J^(2) = 4 / (E_gamma[i+1] - E_gamma[i])
    j2_res = []
    for i in range(len(e_gamma) - 1):
        deg = e_gamma[i+1] - e_gamma[i]
        if abs(deg) > 1e-5:
            j2 = 4.0 / deg # hbar^2 / MeV
        else:
            j2 = float("inf")
        j2_res.append({
            "spin": float(sp_mid[i+1]),
            "E_gamma_MeV": float(e_gamma[i+1]),
            "Delta_E_gamma_MeV": float(deg),
            "J2_hbar2_MeV": float(j2)
        })

    return j2_res


def diagnose_smooth_band_termination(q_drop_percent=None, j2_steep_dive=None, e_diff_cusp_found=None):
    """
    Diagnose whether an observed high-spin sequence corresponds to smooth band termination.
    """
    criteria_met = 0
    reasons = []

    if q_drop_percent is not None:
        if q_drop_percent >= 75.0:
            criteria_met += 1
            reasons.append(f"Transition quadrupole moment collapsed by {q_drop_percent:.1f}% (Qt -> 0)")
        elif q_drop_percent >= 50.0:
            criteria_met += 0.5
            reasons.append(f"Substantial Qt loss ({q_drop_percent:.1f}%)")

    if j2_steep_dive is True:
        criteria_met += 1
        reasons.append("Dynamic moment of inertia J^(2) dives steeply towards zero")

    if e_diff_cusp_found is True:
        criteria_met += 1
        reasons.append("Pronounced minimum cusp observed in E - E_RR trajectory")

    if criteria_met >= 2.0:
        diagnosis = (
            "Smooth-band-termination screening pass: the supplied Qt, J^(2), "
            "and energy-cusp descriptors are jointly compatible with a "
            "terminating-rotation interpretation; absolute lifetime/Qt and "
            "configuration evidence are still required."
        )
        is_termination = True
    elif criteria_met >= 1.0:
        diagnosis = "Candidate Terminating Sequence: Partial alignment indicators present; requires absolute lifetime/Qt measurement."
        is_termination = True
    else:
        diagnosis = "Standard Rotational Band: Collectivity sustained; no evidence of impending valence exhaustion."
        is_termination = False

    return {
        "criteria_score": float(criteria_met),
        "is_band_termination": is_termination,
        "diagnosis": diagnosis,
        "supporting_reasons": reasons
    }
