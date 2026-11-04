#!/usr/bin/env python3
"""
triaxial_wobbling_tip_chiral_analyzer.py
========================================
Triaxial Rotor Harmonic Wobbling, Tilted Precession (TiP) vs Phonon Classifier &
Chiral Doublet Electromagnetic Staggering Analysis Suite.

Physics & Formulation:
----------------------
1. Triaxial Rotor & Moments of Inertia:
   Principal axes are ordered by convention:
     - s-axis (short, axis 1)
     - m-axis (intermediate, axis 2)
     - l-axis (long, axis 3)
   For collective rotation, the intermediate axis has the largest moment of inertia:
     J_m > J_s > J_l  =>  A_m < A_s < A_l  (where A_i = hbar^2 / (2 * J_i))
   The asymmetry parameter kappa (Frauendorf 2025, Eq. 2.2):
     kappa = (2*A_s - A_m - A_l) / (A_m - A_l),  A_m <= A_s <= A_l.
     Its numerical endpoints depend on the adopted axis and gamma convention;
     the scalar alone is not a shape classification.

2. Transverse Wobbling (TW) vs Longitudinal Wobbling (LW):
   - Particle j aligned with short s-axis (Frauendorf 2025, Eqs. 2.20 - 2.21):
     Effective s-axis rotational parameter:
       A_bar_s(I) = A_s * (1 - j / I)
     Transverse wobbling frequency:
       hbar * omega_TW(I) = 2 * I * sqrt[ (A_m - A_bar_s(I)) * (A_l - A_bar_s(I)) ]
     Critical softening spin where TW mode breaks down (omega_TW -> 0):
       I_c = j * J_m / (J_m - J_s)
     Signature: d(hbar*omega_TW)/dI < 0 (wobbling frequency decreases with increasing spin I).
   - Particle j aligned with intermediate m-axis (Longitudinal Wobbling, LW):
     Signature: d(hbar*omega_LW)/dI > 0 (frequency increases with spin I).

3. Lawrie Tilted Precession (TiP) vs Vibrational Wobbling Classifier:
   Based on E. A. Lawrie, in *Chirality and Wobbling in Atomic Nuclei* (CRC 2025), Ch. 6, Table 6.1:
   - Excitation energy scaling at constant spin I:
       Wobbling Phonon: E_exc(I, n_w) proportional to n_w (linear phonon harmonicity)
       Tilted Precession: E_exc(I, m) proportional to m^2 (quadratic 3D angular momentum tilt)
   - Even-even sum rule:
       Delta_sum = E(2_g^+) + E(2_gamma^+) - E(3_gamma^+)
       If Delta_sum > 0 => Vibrational (wobbling phonon)
       If Delta_sum == 0 => Rotational (TiP)
   - Delta n or Delta m > 1 selection rule:
       B(E2; n_w=2 -> n_w=0) == 0 (forbidden for harmonic wobbling phonon)
       B(E2; m=2 -> m=0) > 0 (allowed collective rotational transition for TiP)

4. Chiral Doublet Selection Rules & Staggering:
   Based on J. Meng & Y. P. Wang, Ch. 3; E. Grodner, Ch. 7:
   - Chiral energy splitting: Delta_E(I) = |E_band1(I) - E_band2(I)|
   - Signature staggering parameter: S(I) = [ E(I) - E(I-1) ] / (2*I)
   - Intra-band B(M1)/B(E2) odd-even staggering:
       Delta_S_M1E2(I) = R(I) - 0.5 * [ R(I+1) + R(I-1) ]
       where R(I) = B(M1; I -> I-1) / B(E2; I -> I-2)
   - Chiral Aplanarity Volume Metric:
       V_chiral = j_p * j_n * sqrt( max(0, I*(I+1) - j_p^2 - j_n^2) )

References:
  - C. M. Petrache (Ed.), *Chirality and Wobbling in Atomic Nuclei*, CRC Press (2025).
  - S. Frauendorf, Ch. 2 (pp. 43-80); J. Meng & Y. P. Wang, Ch. 3 (pp. 81-93).
  - E. A. Lawrie, Ch. 6 (pp. 127-155); E. Grodner, Ch. 7 (pp. 156-166).
  - K. Nomura, Ch. 11 (pp. 239-255); J. A. Sheikh et al., Ch. 12 (pp. 256-274).
  - A. Bohr and B. R. Mottelson, *Nuclear Structure*, Vol. II, §4-5.
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_triaxial_rotor_moi_parameters(
    J_m: float,
    J_s: float,
    J_l: float
) -> Dict[str, Any]:
    """
    Calculates rotational parameters A_i = hbar^2 / (2*J_i) and Ray's asymmetry parameter kappa.
    Requires J_m >= J_s >= J_l > 0.
    """
    if J_m <= 0.0 or J_s <= 0.0 or J_l <= 0.0:
        raise ValueError("Moments of inertia must be strictly positive.")
    if not (J_m >= J_s >= J_l):
        raise ValueError(f"Inertia ordering violation: expected J_m >= J_s >= J_l, got ({J_m}, {J_s}, {J_l})")

    # Rotational parameters in keV (assuming J in hbar^2/MeV => A in keV)
    A_m_keV = 1000.0 / (2.0 * J_m)
    A_s_keV = 1000.0 / (2.0 * J_s)
    A_l_keV = 1000.0 / (2.0 * J_l)

    # Ray's asymmetry parameter. Its shape interpretation remains convention-
    # dependent and is intentionally not inferred from the scalar alone.
    diff = A_m_keV - A_l_keV
    if abs(diff) < 1e-12:
        kappa = 0.0
    else:
        kappa = (2.0 * A_s_keV - A_m_keV - A_l_keV) / diff

    # Separatrix energy coefficient: E_sep(I) = I*(I+1) / (2*J_s)
    separatrix_coeff_keV = A_s_keV

    return {
        "J_m": J_m,
        "J_s": J_s,
        "J_l": J_l,
        "A_m_keV": round(A_m_keV, 3),
        "A_s_keV": round(A_s_keV, 3),
        "A_l_keV": round(A_l_keV, 3),
        "asymmetry_parameter_kappa": round(kappa, 4),
        "separatrix_rotational_parameter_keV": round(separatrix_coeff_keV, 3)
    }


def calculate_transverse_wobbling_spectrum(
    J_m: float,
    J_s: float,
    J_l: float,
    j_single: float,
    spins: List[float]
) -> Dict[str, Any]:
    """
    Calculates Transverse Wobbling (TW) frequencies hbar*omega_TW(I) and detects critical spin I_c.
    Based on Frauendorf & Dönau (2014) / Frauendorf in Petrache (2025) Ch. 2, Eqs. (2.20)-(2.21).
    """
    if J_m <= J_s:
        raise ValueError("Transverse wobbling requires J_m > J_s for intermediate-axis collective dominance.")
    if j_single <= 0.0:
        raise ValueError("Single-particle angular momentum j must be positive.")

    A_m = 1.0 / (2.0 * J_m) # MeV
    A_s = 1.0 / (2.0 * J_s)
    A_l = 1.0 / (2.0 * J_l)

    # Critical spin I_c where A_m - A_bar_s = 0: I_c = j * J_m / (J_m - J_s)
    I_c = j_single * J_m / (J_m - J_s)

    results = []
    freqs = []
    valid_spins = []

    for I in spins:
        if I < j_single:
            status = "unphysical_spin_below_j"
            omega_keV = None
        elif abs(I - I_c) <= 1.0e-12:
            status = "critical_softening"
            omega_keV = None
        elif I > I_c:
            status = "above_critical_spin_requires_full_model"
            omega_keV = None
        else:
            A_bar_s = A_s * (1.0 - j_single / I)
            term1 = A_m - A_bar_s
            term2 = A_l - A_bar_s
            arg = term1 * term2
            if arg > 0.0:
                omega_MeV = 2.0 * I * math.sqrt(arg)
                omega_keV = omega_MeV * 1000.0
                status = "stable_harmonic_tw"
                freqs.append(omega_keV)
                valid_spins.append(I)
            else:
                status = "complex_frequency_instability"
                omega_keV = None

        results.append({
            "spin_I": I,
            "hbar_omega_TW_keV": round(omega_keV, 2) if omega_keV is not None else None,
            "status": status
        })

    # Slope check d(omega)/dI
    if len(freqs) >= 2:
        slope = (freqs[-1] - freqs[0]) / (valid_spins[-1] - valid_spins[0])
        slope_classification = (
            "negative_local_or_window_slope"
            if slope < 0
            else "positive_local_or_window_slope"
        )
    else:
        slope = None
        slope_classification = "Insufficient points"

    return {
        "critical_spin_Ic": round(I_c, 3),
        "single_particle_j": j_single,
        "wobbling_slope_keV_per_hbar": round(slope, 3) if slope is not None else None,
        "slope_descriptor": slope_classification,
        "mode_identification": None,
        "mode_confirmed": None,
        "boundary": (
            "A harmonic-model slope descriptor only; a non-monotonic curve, "
            "TiP branch, or experimental wobbling identity is not inferred."
        ),
        "spectrum": results
    }


def classify_tip_vs_phonon_wobbling(
    n_or_m_indices: List[int],
    energies_keV: List[float],
    E_2g_keV: Optional[float] = None,
    E_2gamma_keV: Optional[float] = None,
    E_3gamma_keV: Optional[float] = None,
    B_E2_delta2_Wu: Optional[float] = None
) -> Dict[str, Any]:
    """
    Classifies an excited band sequence as Vibrational Wobbling vs Rotational Tilted Precession (TiP)
    using Elena Lawrie's diagnostic framework (Petrache 2025, Ch. 6, Table 6.1).
    """
    if len(n_or_m_indices) != len(energies_keV) or len(n_or_m_indices) < 2:
        raise ValueError("Must provide at least 2 points of (index, energy).")

    # 1. Linear vs Quadratic Fit
    # Fit E = c1 * k (linear) vs E = c2 * k^2 (quadratic)
    sum_k = sum(n_or_m_indices)
    sum_k2 = sum(k ** 2 for k in n_or_m_indices)
    sum_k4 = sum(k ** 4 for k in n_or_m_indices)
    sum_kE = sum(k * E for k, E in zip(n_or_m_indices, energies_keV))
    sum_k2E = sum((k ** 2) * E for k, E in zip(n_or_m_indices, energies_keV))

    c1_lin = sum_kE / sum_k2 if sum_k2 > 0 else 0.0
    c2_quad = sum_k2E / sum_k4 if sum_k4 > 0 else 0.0

    res_lin = sum((E - c1_lin * k) ** 2 for k, E in zip(n_or_m_indices, energies_keV))
    res_quad = sum((E - c2_quad * (k ** 2)) ** 2 for k, E in zip(n_or_m_indices, energies_keV))

    scaling_favors = (
        "linear_model_residual_smaller"
        if res_lin <= res_quad
        else "quadratic_model_residual_smaller"
    )

    # 2. Even-even sum rule: Delta_sum = E(2_g^+) + E(2_gamma^+) - E(3_gamma^+)
    sum_rule_eval = None
    if E_2g_keV is not None and E_2gamma_keV is not None and E_3gamma_keV is not None:
        delta_sum = E_2g_keV + E_2gamma_keV - E_3gamma_keV
        if delta_sum > 0.0:
            sr_diag = f"sum_rule_positive_screening (Delta_sum = {delta_sum:.1f} keV)"
        else:
            sr_diag = f"sum_rule_nonpositive_screening (Delta_sum = {delta_sum:.1f} keV)"
        sum_rule_eval = {
            "delta_sum_keV": round(delta_sum, 2),
            "diagnosis": sr_diag
        }

    # 3. Delta k > 1 Selection Rule
    selection_rule_eval = None
    if B_E2_delta2_Wu is not None:
        sel_diag = (
            "delta_n_or_delta_m_selection_screening_only "
            f"(input={B_E2_delta2_Wu:.2f} W.u.)"
        )
        selection_rule_eval = {
            "B_E2_Delta_n_or_delta_m_2_Wu": B_E2_delta2_Wu,
            "diagnosis": sel_diag
        }

    return {
        "linear_fit_residual_sq": round(res_lin, 2),
        "quadratic_fit_residual_sq": round(res_quad, 2),
        "energy_scaling_diagnosis": scaling_favors,
        "sum_rule_test": sum_rule_eval,
        "selection_rule_test": selection_rule_eval,
        "mode_verdict": None,
        "evidence_level": "conditional-observable-screen",
        "boundary": (
            "Residuals, sum rules and selection-rule inputs are reported as "
            "conditional diagnostics; they do not confirm TiP or wobbling."
        ),
    }


def calculate_lawrie_tip_wobbling_metrics(
    *,
    E_2g_keV: float,
    E_2gamma_keV: float,
    E_3gamma_keV: float,
    B_E2_2gamma_to_2g: Optional[float] = None,
    B_E2_2g_to_0g: Optional[float] = None,
    B_E2_3gamma_to_2gamma: Optional[float] = None,
    B_E2_delta2: Optional[float] = None,
    A_s_MeV: Optional[float] = None,
    A_i_MeV: Optional[float] = None,
    A_l_MeV: Optional[float] = None,
    spin_I: Optional[float] = None,
    phonon_n: int = 1,
) -> Dict[str, Any]:
    """Return Lawrie Ch. 6 TiP/wobbling observables without auto-confirmation.

    The source distinguishes rotational tilted precession (TiP) from
    vibrational wobbling through energy additivity, relative excitation
    energies, and several B(E2) ratios.  This function reports those
    observables and reference expectations; it deliberately does not collapse
    them into a nuclear-mode verdict.
    """
    energies = (float(E_2g_keV), float(E_2gamma_keV), float(E_3gamma_keV))
    if not all(math.isfinite(value) for value in energies):
        raise ValueError("All level energies must be finite.")
    delta_sum = energies[0] + energies[1] - energies[2]

    ratios: Dict[str, Optional[float]] = {
        "R_2gamma_2g": None,
        "R_3gamma_2gamma": None,
    }
    for name, value in (
        ("B_E2_2gamma_to_2g", B_E2_2gamma_to_2g),
        ("B_E2_2g_to_0g", B_E2_2g_to_0g),
        ("B_E2_3gamma_to_2gamma", B_E2_3gamma_to_2gamma),
        ("B_E2_delta2", B_E2_delta2),
    ):
        if value is not None and (not math.isfinite(float(value)) or float(value) < 0.0):
            raise ValueError(f"{name} must be finite and non-negative.")
    if B_E2_2g_to_0g is not None:
        denominator = float(B_E2_2g_to_0g)
        if denominator <= 0.0:
            raise ValueError("B_E2_2g_to_0g must be positive when ratios are requested.")
        if B_E2_2gamma_to_2g is not None:
            ratios["R_2gamma_2g"] = float(B_E2_2gamma_to_2g) / denominator
        if B_E2_3gamma_to_2gamma is not None:
            ratios["R_3gamma_2gamma"] = float(B_E2_3gamma_to_2gamma) / denominator

    harmonicity = None
    if any(value is not None for value in (A_s_MeV, A_i_MeV, A_l_MeV, spin_I)):
        if any(value is None for value in (A_s_MeV, A_i_MeV, A_l_MeV, spin_I)):
            raise ValueError("A_s, A_i, A_l and spin_I must be supplied together.")
        A_s = float(A_s_MeV)
        A_i = float(A_i_MeV)
        A_l = float(A_l_MeV)
        spin = float(spin_I)
        if min(A_s, A_i, A_l, spin) <= 0.0:
            raise ValueError("Rotational constants and spin must be positive.")
        denominator = 2.0 * spin * math.sqrt((A_s - A_i) * (A_l - A_i))
        if denominator <= 0.0:
            raise ValueError("Harmonic wobbling condition requires A_i < A_s and A_i < A_l.")
        numerator = (2.0 * int(phonon_n) + 1.0) * (A_s + A_l - 2.0 * A_i)
        harmonicity = {
            "f_n_I": numerator / denominator,
            "n": int(phonon_n),
            "spin_I": spin,
            "high_spin_harmonic_limit": "f(n,I) << 1",
        }

    return {
        "delta_sum_keV": delta_sum,
        "energy_reference": {
            "tip": "E(3_gamma) = E(2_g) + E(2_gamma), so delta_sum = 0",
            "wobbling": "E(3_gamma) < E(2_g) + E(2_gamma), so delta_sum > 0",
        },
        "B_E2_ratios": ratios,
        "B_E2_delta2": B_E2_delta2,
        "reference_expectations": {
            "R_2gamma_2g_tip": "approximately 0.4-1.4 for gamma around 20-30 degrees",
            "R_2gamma_2g_wobbling": 0.0,
            "R_3gamma_2gamma_tip": 1.78,
            "R_3gamma_2gamma_wobbling": 1.0,
            "delta_n_ge_2_wobbling": "forbidden in ideal harmonic phonon limit",
            "delta_m_ge_2_tip": "allowed in general; gamma=30 degrees adds zeros for selected branches",
        },
        "harmonicity_parameter": harmonicity,
        "mode_verdict": None,
        "boundary": (
            "Observable comparison card from Lawrie Ch. 6. "
            "Requires level identity, branching/efficiency corrections and "
            "competing TiP, gamma-vibration, signature-partner and configuration-mixing tests."
        ),
    }


def analyze_chiral_doublet_staggering(
    spins: List[float],
    energies_band1_keV: List[float],
    energies_band2_keV: List[float],
    bm1_be2_band1: Optional[List[float]] = None,
    j_p: float = 5.5,
    j_n: float = 5.5
) -> Dict[str, Any]:
    """
    Analyzes chiral doublet energy splitting Delta_E(I), signature staggering S(I),
    intra-band B(M1)/B(E2) odd-even staggering and aplanarity volume metric.
    """
    if len(spins) != len(energies_band1_keV) or len(spins) != len(energies_band2_keV):
        raise ValueError("Spins and energy lists must have equal lengths.")

    records = []
    for i, I in enumerate(spins):
        e1 = energies_band1_keV[i]
        e2 = energies_band2_keV[i]
        delta_E = abs(e2 - e1)

        # Signature staggering S(I) = (E(I) - E(I-1)) / (2*I)
        s1 = (e1 - energies_band1_keV[i-1]) / (2.0 * I) if i > 0 else None
        s2 = (e2 - energies_band2_keV[i-1]) / (2.0 * I) if i > 0 else None

        # Aplanarity volume V_chiral = j_p * j_n * R_core
        r_sq = I * (I + 1.0) - j_p ** 2 - j_n ** 2
        r_core = math.sqrt(max(0.0, r_sq))
        v_chiral = j_p * j_n * r_core

        rec = {
            "spin_I": I,
            "E_band1_keV": e1,
            "E_band2_keV": e2,
            "energy_splitting_DeltaE_keV": round(delta_E, 2),
            "S_band1": round(s1, 3) if s1 is not None else None,
            "S_band2": round(s2, 3) if s2 is not None else None,
            "ideal_orthogonal_tripod_proxy": round(v_chiral, 2),
            "chiral_aplanarity_volume": round(v_chiral, 2)
        }

        if bm1_be2_band1 is not None and i < len(bm1_be2_band1):
            rec["B_M1_over_B_E2"] = bm1_be2_band1[i]

        records.append(rec)

    # Calculate M1/E2 staggering if available
    staggering_vals = []
    if bm1_be2_band1 is not None and len(bm1_be2_band1) >= 3:
        for i in range(1, len(bm1_be2_band1) - 1):
            r_curr = bm1_be2_band1[i]
            r_prev = bm1_be2_band1[i-1]
            r_next = bm1_be2_band1[i+1]
            if r_curr is not None and r_prev is not None and r_next is not None:
                stag = r_curr - 0.5 * (r_prev + r_next)
                staggering_vals.append(round(stag, 3))
            else:
                staggering_vals.append(None)

    # Average energy splitting in chiral plateau
    avg_splitting = sum(r["energy_splitting_DeltaE_keV"] for r in records) / len(records)

    return {
        "mean_energy_splitting_keV": round(avg_splitting, 2),
        "chiral_conundrum_status": "energy_splitting_screening_only",
        "m1_e2_staggering_profile": staggering_vals if staggering_vals else None,
        "band_levels": records,
        "mode_confirmed": None,
        "evidence_level": "conditional-observable-screen",
        "boundary": (
            "The ideal orthogonal-tripod quantity is a geometry proxy. "
            "Energy splitting alone does not confirm chiral doublets."
        )
    }


def format_text_report(
    moi_res: Dict[str, Any],
    tw_res: Optional[Dict[str, Any]] = None,
    tip_res: Optional[Dict[str, Any]] = None,
    chiral_res: Optional[Dict[str, Any]] = None
) -> str:
    lines = [
        "=" * 76,
        "   TRIAXIAL ROTOR WOBBLING, TiP CLASSIFIER & CHIRAL SELECTION RULES SUITE",
        "   Based on C. M. Petrache (Ed.), Chirality and Wobbling in Atomic Nuclei (2025)",
        "=" * 76,
        " TRIAXIAL MOMENTS OF INERTIA & ROTOR CHARACTERISTICS:",
        f"   Moments of Inertia (m, s, l): ({moi_res['J_m']}, {moi_res['J_s']}, {moi_res['J_l']}) hbar^2/MeV",
        f"   Rotational Parameters A_i   : (A_m={moi_res['A_m_keV']:.2f}, A_s={moi_res['A_s_keV']:.2f}, A_l={moi_res['A_l_keV']:.2f}) keV",
        f"   Ray's Asymmetry Parameter   : kappa = {moi_res['asymmetry_parameter_kappa']:.4f} (0 = maximal triaxiality)",
        f"   Separatrix Parameter        : {moi_res['separatrix_rotational_parameter_keV']:.2f} keV",
        "-" * 76,
    ]

    if tw_res is not None:
        lines.extend([
            f" TRANSVERSE WOBBLING (TW) SPECTRUM & STABILITY (Particle j = {tw_res['single_particle_j']}):",
            f"   Critical Softening Spin I_c : {tw_res['critical_spin_Ic']:.2f} hbar",
            f"   Frequency Slope d(omega)/dI : {tw_res['wobbling_slope_keV_per_hbar']} keV/hbar",
            f"   Mode Identification         : {tw_res['mode_identification']}",
            "   Calculated Wobbling Frequencies:",
        ])
        for r in tw_res["spectrum"]:
            val_str = f"{r['hbar_omega_TW_keV']:.1f} keV" if r["hbar_omega_TW_keV"] is not None else "None"
            lines.append(f"     I = {r['spin_I']:4.1f} hbar : hbar*omega_TW = {val_str:<12} [{r['status']}]")
        lines.append("-" * 76)

    if tip_res is not None:
        lines.extend([
            " LAWRIE TILTED PRECESSION (TiP) vs WOBBLING PHONON DIAGNOSTICS (Ch. 6 Table 6.1):",
            f"   Linear Fit Residual Sq (E ~ n_w) : {tip_res['linear_fit_residual_sq']:.2f}",
            f"   Quadratic Fit Residual Sq (E ~ m^2): {tip_res['quadratic_fit_residual_sq']:.2f}",
            f"   Energy Scaling Conclusion       : {tip_res['energy_scaling_diagnosis']}",
        ])
        if tip_res["sum_rule_test"] is not None:
            sr = tip_res["sum_rule_test"]
            lines.append(f"   Even-Even Sum Rule Test         : {sr['diagnosis']}")
        if tip_res["selection_rule_test"] is not None:
            sel = tip_res["selection_rule_test"]
            lines.append(f"   Delta_k = 2 Transition Test     : {sel['diagnosis']}")
        lines.append("-" * 76)

    if chiral_res is not None:
        lines.extend([
            " CHIRAL DOUBLET BANDS & ELECTROMAGNETIC STAGGERING PROFILE:",
            f"   Mean Chiral Splitting Delta_E   : {chiral_res['mean_energy_splitting_keV']:.2f} keV",
            f"   Chiral State Status             : {chiral_res['chiral_conundrum_status']}",
            "   Doublet Level Comparison Table:",
            "     Spin I     E(Band 1)     E(Band 2)    Delta_E       S(Band 1)     V_chiral",
        ])
        for r in chiral_res["band_levels"]:
            s_str = f"{r['S_band1']:.3f}" if r["S_band1"] is not None else "  ---  "
            lines.append(f"     {r['spin_I']:4.1f}   {r['E_band1_keV']:9.1f}   {r['E_band2_keV']:9.1f}   {r['energy_splitting_DeltaE_keV']:8.1f}   {s_str:<10}   {r['chiral_aplanarity_volume']:8.1f}")
        lines.append("-" * 76)

    lines.extend([
        " Methodological & Diagnostic Guidelines:",
        "   - TW signature: d(hbar*omega)/dI < 0 and inter-band Delta_I=1 transition has dominant E2.",
        "   - If inter-band transition is dominated by M1 (delta ~ 0), wobbling is ruled out (Nomura IBFM Ch. 11).",
        "   - Chiral doublets require same parity, Delta_I=1 twin bands, Delta_E -> 0, and B(M1)/B(E2) odd-even staggering.",
        "=" * 76
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Triaxial Rotor Wobbling, TiP Classifier & Chiral Doublet Analyzer"
    )
    parser.add_argument("--preset", type=str, default="163Lu",
                        choices=["163Lu", "135Pr", "192Os", "128Cs", "134Pr", "custom"],
                        help="Benchmark preset: 163Lu, 135Pr, 192Os, 128Cs, 134Pr")
    parser.add_argument("--Jm", type=float, default=64.0, help="Intermediate axis MOI in hbar^2/MeV")
    parser.add_argument("--Js", type=float, default=56.0, help="Short axis MOI in hbar^2/MeV")
    parser.add_argument("--Jl", type=float, default=13.0, help="Long axis MOI in hbar^2/MeV")
    parser.add_argument("--j-single", type=float, default=6.5, help="Single particle angular momentum j")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")

    args = parser.parse_args()

    Jm_val = args.Jm
    Js_val = args.Js
    Jl_val = args.Jl
    j_val = args.j_single
    tw_res = None
    tip_res = None
    chiral_res = None

    if args.preset == "163Lu":
        # Frauendorf & Donau (2014) / Petrache (2025) Ch. 2, p. 53
        Jm_val, Js_val, Jl_val = 64.0, 56.0, 13.0
        j_val = 6.5 # i13/2
        spins = [9.5, 11.5, 13.5, 15.5, 17.5, 19.5, 21.5, 25.5, 30.5, 35.5]
        tw_res = calculate_transverse_wobbling_spectrum(Jm_val, Js_val, Jl_val, j_val, spins)
    elif args.preset == "135Pr":
        # Frauendorf (2014) / Petrache (2025) Ch. 2 & Ch. 11
        Jm_val, Js_val, Jl_val = 21.0, 13.0, 4.0
        j_val = 5.5 # h11/2
        spins = [6.5, 8.5, 10.5, 12.5, 14.5]
        tw_res = calculate_transverse_wobbling_spectrum(Jm_val, Js_val, Jl_val, j_val, spins)
    elif args.preset == "192Os":
        # Elena Lawrie Ch. 6, Fig. 6.10 TiP benchmark
        Jm_val, Js_val, Jl_val = 30.0, 18.0, 6.0
        # Testing k=1, 2 gamma bands at I=4
        tip_res = classify_tip_vs_phonon_wobbling(
            n_or_m_indices=[1, 2],
            energies_keV=[867.0, 1980.0],
            E_2g_keV=205.8,
            E_2gamma_keV=489.1,
            E_3gamma_keV=690.5, # Delta_sum = 205.8 + 489.1 - 690.5 = 4.4 keV ~ 0 (TiP!)
            B_E2_delta2_Wu=15.0 # Allowed Delta_k=2 transition in 192Os
        )
    elif args.preset == "128Cs":
        # E. Grodner Ch. 7, p. 156 / J. Meng Ch. 3
        Jm_val, Js_val, Jl_val = 35.0, 25.0, 10.0
        spins = [9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0]
        e_b1 = [0.0, 235.0, 520.0, 856.0, 1245.0, 1680.0, 2160.0]
        e_b2 = [280.0, 450.0, 680.0, 960.0, 1310.0, 1720.0, 2190.0] # Splitting diminishes towards 30 keV
        bm1_be2 = [0.45, 0.85, 0.38, 0.92, 0.40, 0.88, 0.42] # Staggering
        chiral_res = analyze_chiral_doublet_staggering(spins, e_b1, e_b2, bm1_be2, j_p=5.5, j_n=5.5)
    elif args.preset == "134Pr":
        # Famous Chiral Conundrum (Petrache 1996, Tonev 2006)
        Jm_val, Js_val, Jl_val = 32.0, 20.0, 8.0
        spins = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0]
        e_b1 = [0.0, 285.0, 620.0, 1010.0, 1450.0, 1940.0]
        e_b2 = [350.0, 580.0, 840.0, 1160.0, 1540.0, 1990.0]
        chiral_res = analyze_chiral_doublet_staggering(spins, e_b1, e_b2, j_p=5.5, j_n=5.5)
    else:
        spins = [9.5, 11.5, 13.5, 15.5, 17.5]
        tw_res = calculate_transverse_wobbling_spectrum(Jm_val, Js_val, Jl_val, j_val, spins)

    moi_res = calculate_triaxial_rotor_moi_parameters(Jm_val, Js_val, Jl_val)

    if args.json:
        out = {"moments_of_inertia": moi_res}
        if tw_res is not None:
            out["transverse_wobbling"] = tw_res
        if tip_res is not None:
            out["tip_classifier"] = tip_res
        if chiral_res is not None:
            out["chiral_doublets"] = chiral_res
        print(json.dumps(out, indent=2))
    else:
        print(format_text_report(moi_res, tw_res, tip_res, chiral_res))


if __name__ == "__main__":
    main()
