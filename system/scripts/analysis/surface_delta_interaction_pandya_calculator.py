#!/usr/bin/env python3
"""
Surface Delta Interaction (SDI), Two-Body Residual Matrix Elements & Pandya Transformation Calculator.

Based on:
  - S. P. Pandya, Phys. Rev. 103, 956 (1956) (Interaction of nucleons in unfilled shells)
  - I. M. Green & S. A. Moszkowski, Phys. Rev. 139, B790 (1965) (Surface Delta Interaction)
  - J. Suhonen, From Nucleons to Nucleus, Ch. 8 (Two-body interactions & SDI)
  - P. J. Brussaard & P. W. M. Glaudemans, Shell-Model Applications in Nuclear Spectroscopy, Ch. 4

Features:
  1. Computes analytical Clebsch-Gordan coefficients and Wigner 6j symbols via exact Racah algebra.
  2. Evaluates two-body residual matrix elements for the Surface Delta Interaction (SDI).
  3. Generates the single-j shell pairing spectrum, verifying E(J=0) = - V_0 * (j + 1/2).
  4. Executes the Pandya transformation from particle-particle (pp) to particle-hole (ph) matrix elements.
  5. Verifies the unitary involution property P^2 = Identity to machine precision.
  6. Benchmarks the classic 42Sc (pp) versus 40K / 48Sc (ph) dual spectrum reversal.
"""

import math
import numpy as np


def triangle_delta(a, b, c):
    """
    Triangle coefficient Delta(a, b, c) for angular momentum coupling.
    """
    if (a + b < c) or (a + c < b) or (b + c < a):
        return 0.0
    # Must be integer or half-integer satisfying perimeter
    num = math.factorial(int(round(a + b - c))) * math.factorial(int(round(a - b + c))) * math.factorial(int(round(-a + b + c)))
    den = math.factorial(int(round(a + b + c + 1)))
    return math.sqrt(num / den)


def calculate_wigner_6j(j1, j2, j3, j4, j5, j6):
    """
    Exact Racah formula for Wigner 6j symbol:
      { j1 j2 j3 }
      { j4 j5 j6 }.
    """
    d1 = triangle_delta(j1, j2, j3)
    d2 = triangle_delta(j1, j5, j6)
    d3 = triangle_delta(j4, j2, j6)
    d4 = triangle_delta(j4, j5, j3)
    if d1 == 0 or d2 == 0 or d3 == 0 or d4 == 0:
        return 0.0

    k_min = max(int(round(j1 + j2 + j3)), int(round(j1 + j5 + j6)), int(round(j4 + j2 + j6)), int(round(j4 + j5 + j3)))
    k_max = min(int(round(j1 + j2 + j4 + j5)), int(round(j2 + j3 + j5 + j6)), int(round(j3 + j1 + j6 + j4)))

    sum_val = 0.0
    for k in range(k_min, k_max + 1):
        num = ((-1) ** k) * math.factorial(k + 1)
        den = (math.factorial(int(round(k - j1 - j2 - j3))) *
               math.factorial(int(round(k - j1 - j5 - j6))) *
               math.factorial(int(round(k - j4 - j2 - j6))) *
               math.factorial(int(round(k - j4 - j5 - j3))) *
               math.factorial(int(round(j1 + j2 + j4 + j5 - k))) *
               math.factorial(int(round(j2 + j3 + j5 + j6 - k))) *
               math.factorial(int(round(j3 + j1 + j6 + j4 - k))))
        sum_val += num / den

    return float(d1 * d2 * d3 * d4 * sum_val)


def calculate_clebsch_gordan(j1, m1, j2, m2, j3, m3):
    """
    Exact algebraic formula for Clebsch-Gordan coefficient <j1 m1 j2 m2 | j3 m3>.
    """
    if abs(m1 + m2 - m3) > 1e-4:
        return 0.0
    if abs(m1) > j1 or abs(m2) > j2 or abs(m3) > j3:
        return 0.0
    d = triangle_delta(j1, j2, j3)
    if d == 0:
        return 0.0

    pre = math.sqrt(2.0 * j3 + 1.0) * d
    pre *= math.sqrt(math.factorial(int(round(j1 + m1))) * math.factorial(int(round(j1 - m1))) *
                     math.factorial(int(round(j2 + m2))) * math.factorial(int(round(j2 - m2))) *
                     math.factorial(int(round(j3 + m3))) * math.factorial(int(round(j3 - m3))))

    k_min = max(0, int(round(j2 - m1 - j3)), int(round(j1 + m2 - j3)))
    k_max = min(int(round(j1 + j2 - j3)), int(round(j1 - m1)), int(round(j2 + m2)))

    sum_k = 0.0
    for k in range(k_min, k_max + 1):
        den = (math.factorial(k) *
               math.factorial(int(round(j1 + j2 - j3 - k))) *
               math.factorial(int(round(j1 - m1 - k))) *
               math.factorial(int(round(j2 + m2 - k))) *
               math.factorial(int(round(j3 - j2 + m1 + k))) *
               math.factorial(int(round(j3 - j1 - m2 + k))))
        sum_k += ((-1) ** k) / den

    return float(pre * sum_k)


def calculate_wigner_3j(j1, j2, j3, m1, m2, m3):
    """Calculate a Wigner 3j symbol through the exact CG implementation."""
    if abs(m1 + m2 + m3) > 1e-8:
        return 0.0
    if abs(m3) > j3:
        return 0.0
    # <j1 m1 j2 m2 | j3, -m3>
    cg = calculate_clebsch_gordan(j1, m1, j2, m2, j3, -m3)
    exponent = int(round(j1 - j2 + m3))
    return float(((-1) ** exponent) * cg / math.sqrt(2.0 * j3 + 1.0))


def calculate_sdi_matrix_element(ja, jb, jc, jd, J, la, lb, lc, ld, V0_MeV=1.0):
    """
    Compute Surface Delta Interaction (SDI) two-body matrix element:
      < (ja jb) J | V_SDI | (jc jd) J >.

    This is the like-nucleon schematic SDI of Suhonen Eqs. (8.66) and
    (8.70), where ``V0_MeV`` is the fitted A_T strength.  It retains the
    coupled-state normalizers, parity factors, exchange phase and the two
    Wigner-3j factors.  It does not include orbital-dependent radial
    amplitudes or the separate proton-neutron T=0/T=1 expression of Eq. (8.68).
    """
    parity_factor = 1.0 + ((-1) ** int(round(la + lb + lc + ld)))
    angular_parity_factor = 1.0 + ((-1) ** int(round(lc + ld + J)))
    if abs(parity_factor * angular_parity_factor) < 1e-4:
        return 0.0

    w3j1 = calculate_wigner_3j(ja, jb, J, 0.5, -0.5, 0.0)
    w3j2 = calculate_wigner_3j(jc, jd, J, 0.5, -0.5, 0.0)

    same_ab = abs(ja - jb) < 1e-4 and la == lb
    same_cd = abs(jc - jd) < 1e-4 and lc == ld
    if (same_ab and int(round(J)) % 2 == 1) or (same_cd and int(round(J)) % 2 == 1):
        return 0.0
    norm_ab = math.sqrt(
        (1.0 + (1.0 if same_ab else 0.0) * ((-1) ** int(round(J))))
        / (1.0 + (1.0 if same_ab else 0.0))
    )
    norm_cd = math.sqrt(
        (1.0 + (1.0 if same_cd else 0.0) * ((-1) ** int(round(J))))
        / (1.0 + (1.0 if same_cd else 0.0))
    )

    # The public V0 interface is normalized so the single-j benchmark remains
    # E(J=0) = -V0*(j + 1/2), as used by the existing API. The fitted A_T in
    # Suhonen Eq. (8.70) absorbs convention factors that are explicit here.
    k_abcd = -float(V0_MeV) / 8.0
    phase = (-1) ** int(round(la + lc + jb + jd))
    geom = math.sqrt(
        (2.0 * ja + 1.0) * (2.0 * jb + 1.0)
        * (2.0 * jc + 1.0) * (2.0 * jd + 1.0)
    )

    return float(
        -k_abcd
        * norm_ab
        * norm_cd
        * phase
        * parity_factor
        * angular_parity_factor
        * geom
        * w3j1
        * w3j2
    )


def _sdi_like_from_k(
    ja, jb, jc, jd, J, la, lb, lc, ld, k_abcd
):
    """Evaluate Eq. (8.66) for a supplied radial K_abcd coefficient."""
    parity_factor = 1.0 + ((-1) ** int(round(la + lb + lc + ld)))
    angular_parity_factor = 1.0 + ((-1) ** int(round(lc + ld + J)))
    if abs(parity_factor * angular_parity_factor) < 1e-4:
        return 0.0

    same_ab = abs(ja - jb) < 1e-4 and la == lb
    same_cd = abs(jc - jd) < 1e-4 and lc == ld
    j_phase = int(round(J))
    if (same_ab and j_phase % 2 == 1) or (same_cd and j_phase % 2 == 1):
        return 0.0
    norm_ab = math.sqrt(
        (1.0 + (1.0 if same_ab else 0.0) * ((-1) ** j_phase))
        / (1.0 + (1.0 if same_ab else 0.0))
    )
    norm_cd = math.sqrt(
        (1.0 + (1.0 if same_cd else 0.0) * ((-1) ** j_phase))
        / (1.0 + (1.0 if same_cd else 0.0))
    )
    w3j1 = calculate_wigner_3j(ja, jb, J, 0.5, -0.5, 0.0)
    w3j2 = calculate_wigner_3j(jc, jd, J, 0.5, -0.5, 0.0)
    phase = (-1) ** int(round(la + lc + jb + jd))
    geom = math.sqrt(
        (2.0 * ja + 1.0) * (2.0 * jb + 1.0)
        * (2.0 * jc + 1.0) * (2.0 * jd + 1.0)
    )
    return float(
        -float(k_abcd)
        * norm_ab
        * norm_cd
        * phase
        * parity_factor
        * angular_parity_factor
        * geom
        * w3j1
        * w3j2
    )


def calculate_sdi_matrix_element_from_radial_k(
    ja, jb, jc, jd, J, la, lb, lc, ld, k_abcd_MeV
):
    """Evaluate the like-nucleon SDI matrix element for a supplied K_abcd.

    Suhonen Eq. (8.62) defines ``K_abcd`` from the interaction strength and
    surface radial amplitudes.  This entry point keeps that coefficient
    explicit, while the legacy ``calculate_sdi_matrix_element`` uses the
    single-j public V0 normalization.
    """
    return _sdi_like_from_k(
        ja, jb, jc, jd, J, la, lb, lc, ld, k_abcd_MeV
    )


def calculate_sdi_isospin_matrix_element(
    ja, jb, jc, jd, J, la, lb, lc, ld, T, A_T_MeV=1.0
):
    """Evaluate the schematic isospin SDI of Suhonen Eq. (8.68)/(8.70).

    ``A_T_MeV`` is the simplified constant-strength parameter for T=0 or 1.
    The implementation uses the same convention as the public single-j
    baseline, so the 0d-1s table values can be used as regression anchors.
    """
    if int(T) not in (0, 1):
        raise ValueError("T must be 0 or 1 for the schematic SDI.")
    same_ab = abs(ja - jb) < 1e-4 and la == lb
    same_cd = abs(jc - jd) < 1e-4 and lc == ld
    jt = int(round(J + T))
    norm_ab = math.sqrt(
        (1.0 - (1.0 if same_ab else 0.0) * ((-1) ** jt))
        / (1.0 + (1.0 if same_ab else 0.0))
    )
    norm_cd = math.sqrt(
        (1.0 - (1.0 if same_cd else 0.0) * ((-1) ** jt))
        / (1.0 + (1.0 if same_cd else 0.0))
    )
    if norm_ab == 0.0 or norm_cd == 0.0:
        return 0.0

    parity_factor = 1.0 + ((-1) ** int(round(la + lb + lc + ld)))
    if abs(parity_factor) < 1e-4:
        return 0.0
    plus_ab = calculate_wigner_3j(ja, jb, J, 0.5, 0.5, -1.0)
    plus_cd = calculate_wigner_3j(jc, jd, J, 0.5, 0.5, -1.0)
    minus_ab = calculate_wigner_3j(ja, jb, J, 0.5, -0.5, 0.0)
    minus_cd = calculate_wigner_3j(jc, jd, J, 0.5, -0.5, 0.0)
    exchange_phase = (-1) ** int(round(la + lc + jb + jd))
    bracket = (
        (1.0 + (-1) ** int(T)) * plus_ab * plus_cd
        - exchange_phase
        * (1.0 - (-1) ** int(round(lc + ld + J + T)))
        * minus_ab
        * minus_cd
    )
    geom = math.sqrt(
        (2.0 * ja + 1.0) * (2.0 * jb + 1.0)
        * (2.0 * jc + 1.0) * (2.0 * jd + 1.0)
    )
    # Convention matched to the public single-j A_T benchmark.
    k_abcd = -float(A_T_MeV) / 8.0
    return float(k_abcd * norm_ab * norm_cd * parity_factor * geom * bracket)


def calculate_single_j_sdi_spectrum(j_val, l_val, V0_MeV=1.0):
    """
    Calculate single-j shell SDI two-body pairing spectrum for identical nucleons:
      J = 0, 2, 4, ..., 2j - 1.
    Verifies that E(J=0) = - V0 * (j + 1/2).
    """
    jf = float(j_val)
    lf = int(l_val)
    v0 = float(V0_MeV)

    max_J = int(round(2.0 * jf - 1.0))
    spins = [J for J in range(0, max_J + 1, 2)]

    results = []
    e0_expected = - v0 * (jf + 0.5)

    for J in spins:
        val = calculate_sdi_matrix_element(jf, jf, jf, jf, J, lf, lf, lf, lf, V0_MeV=v0)
        results.append({
            "J": J,
            "V_SDI_MeV": val
        })

    e0_actual = results[0]["V_SDI_MeV"]
    is_exact_pairing_energy = abs(e0_actual - e0_expected) < 1e-5

    return {
        "j": jf,
        "l": lf,
        "V0_MeV": v0,
        "E_J0_actual_MeV": e0_actual,
        "E_J0_expected_MeV": e0_expected,
        "is_exact_pairing_energy": is_exact_pairing_energy,
        "spectrum": results
    }


def perform_pandya_transformation(j1, j2, matrix_elements_dict, direction="pp_to_ph"):
    """
    Execute the Pandya Transformation between particle-particle (pp) and particle-hole (ph):
      < j1 j2^-1; J | V | j1 j2^-1; J > = - sum_{J'} (2*J' + 1) * { j1 j2 J; j1 j2 J' } * < j1 j2; J' | V | j1 j2; J' >.
    Direction can be 'pp_to_ph' or 'ph_to_pp'.
    Verifies P^2 = Identity (involution).
    """
    j1_f = float(j1)
    j2_f = float(j2)

    min_J = int(round(abs(j1_f - j2_f)))
    max_J = int(round(j1_f + j2_f))
    spins = list(range(min_J, max_J + 1))
    n_spins = len(spins)

    # Build Pandya transformation matrix P_{J, J'}
    p_mat = np.zeros((n_spins, n_spins), dtype=float)
    for i, J in enumerate(spins):
        for k, Jprime in enumerate(spins):
            w6 = calculate_wigner_6j(j1_f, j2_f, J, j1_f, j2_f, Jprime)
            p_mat[i, k] = - (2.0 * Jprime + 1.0) * w6

    # Verify involution P^2 = I
    p2 = np.dot(p_mat, p_mat)
    max_involution_dev = float(np.max(np.abs(p2 - np.eye(n_spins))))
    is_involution = max_involution_dev < 1e-12

    # Vector of inputs
    v_in = np.zeros(n_spins, dtype=float)
    for i, J in enumerate(spins):
        v_in[i] = matrix_elements_dict.get(J, matrix_elements_dict.get(str(J), 0.0))

    # Output vector
    v_out = np.dot(p_mat, v_in)

    res_dict = {int(spins[i]): float(v_out[i]) for i in range(n_spins)}

    return {
        "j1": j1_f,
        "j2": j2_f,
        "direction": direction,
        "is_unitary_involution_P2_eq_I": is_involution,
        "max_P2_deviation": max_involution_dev,
        "transformed_spectrum": res_dict
    }


def benchmark_sc42_k40_pandya():
    """
    Classic textbook benchmark: 42Sc (pp in 1f7/2^2) vs 40K / 48Sc (ph in 1f7/2 1f7/2^-1).
    Empirical 42Sc excitation energies (in keV):
      J=0 (0), J=1 (611), J=2 (1586), J=3 (1490), J=4 (2815), J=5 (1510), J=6 (3190), J=7 (616).
    """
    j_f72 = 3.5
    # Empirical 42Sc two-body interaction energies (relative to J=0 ground state, in keV)
    sc42_pp = {
        0: -3200.0,
        1: -2589.0,
        2: -1614.0,
        3: -1710.0,
        4: -385.0,
        5: -1690.0,
        6: -10.0,
        7: -2584.0
    }

    res_ph = perform_pandya_transformation(j_f72, j_f72, sc42_pp, direction="pp_to_ph")

    # In 40K / 48Sc, lowest energy state is J=4- or J=3-, J=0 is excited high!
    ph_energies = res_ph["transformed_spectrum"]
    ground_state_ph_spin = min(ph_energies, key=ph_energies.get)

    return {
        "j": 3.5,
        "benchmark": "42Sc(pp) to 48Sc/40K(ph)",
        "ground_state_pp_spin": 0,
        "ground_state_ph_spin": int(ground_state_ph_spin),
        "P2_verified": res_ph["is_unitary_involution_P2_eq_I"],
        "ph_spectrum_keV": ph_energies
    }
