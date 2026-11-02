#!/usr/bin/env python3
"""
triaxial_hexadecapole_deformation_wobbling_modifier.py
======================================================
Triaxial Nuclear Hexadecapole (beta_4, gamma_4) Deformation Perturbation Engine,
Principal Moments of Inertia Renormalization & Wobbling Frequency Modifier.

Physics Formulation:
--------------------
1. Quadrupole-Hexadecapole Triaxial Nuclear Shape Expansion:
   Based on A. Bohr & B. R. Mottelson "Nuclear Structure" Vol. II §4-2 & §4-5,
   "Chirality and Wobbling in Atomic Nuclei" (CRC Press 2025) Ch. 2 & Ch. 10,
   D. L. Hendrie (Phys. Rev. Lett. 31, 478, 1973), and J. Dudek et al. (Phys. Rev. C 26, 1712, 1982):
   At high angular momentum, centrifugal forces drive higher-order multipole distortions,
   predominantly hexadecapole deformation (lambda = 4).
   The nuclear surface is expanded as:
     R(theta, phi) = R_0 * [ 1 + alpha_20 * Y_20 + alpha_22 * (Y_22 + Y_2,-2) + alpha_40 * Y_40 + alpha_42 * (Y_42 + Y_4,-2) + alpha_44 * (Y_44 + Y_4,-4) ]
   where (beta_2, gamma) parameterize quadrupole deformation and (beta_4, gamma_4) parameterize
   hexadecapole deformation.

2. Renormalization of Principal Moments of Inertia J_k:
   In the hydrodynamic and microscopic cranking formulations, hexadecapole coupling alters the
   effective mass distribution and nuclear radius along each principal axis (k = 1, 2, 3 -> s, m, l):
     J_k(beta_2, gamma, beta_4) = J_k^(0)(beta_2, gamma) * [ 1 + kappa_4 * beta_4 * cos(gamma - 2*pi*k/3) + kappa_44 * beta_4^2 ]
   where:
     - J_k^(0) = 4 * B_core * beta_2^2 * sin^2(gamma - 2*pi*k/3) is the pure quadrupole Davydov inertia;
     - kappa_4 ~ 1.85 is the quadrupole-hexadecapole geometric cross-coupling parameter;
     - Intermediate axis (k = 2) corresponds to the largest collective moment of inertia J_m.

3. Perturbation on Wobbling Frequency hbar*omega_w:
   For intermediate-axis collective rotation with aligned quasiparticle j_align:
     hbar * omega_w = omega_rot * sqrt( [ (J_m - J_s) * (J_m - J_l) ] / [ J_s * J_l ] )
   - Positive beta_4 > 0 (common in rare-earth superdeformed nuclei like 163Lu):
     Increases J_m relative to J_s, enhancing wobbling mode stability;
   - Negative beta_4 < 0 (found in A ~ 130 transitional nuclei like 135Pr):
     Reduces J_m asymmetry, accelerating the drop of wobbling frequency towards instability or TiP.
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "163Lu_TSD_positive_beta4": {
        "description": "163Lu TSD band with positive hexadecapole deformation (beta2=0.39, gamma=20, beta4=+0.025)",
        "nucleus": "163Lu",
        "beta2": 0.39,
        "gamma_deg": 20.0,
        "beta4": 0.025,
        "J_base_hbar2_per_MeV": 65.0,
        "j_aligned_hbar": 6.5,
        "spin_I": 35.5
    },
    "135Pr_triaxial_negative_beta4": {
        "description": "135Pr wobbler with negative hexadecapole deformation (beta2=0.17, gamma=-26, beta4=-0.015)",
        "nucleus": "135Pr",
        "beta2": 0.17,
        "gamma_deg": -26.0,
        "beta4": -0.015,
        "J_base_hbar2_per_MeV": 22.0,
        "j_aligned_hbar": 5.5,
        "spin_I": 17.5
    },
    "pure_quadrupole_limit": {
        "description": "Pure quadrupole reference (beta4 = 0.0, exact Bohr-Mottelson limit)",
        "nucleus": "Quadrupole-Ref",
        "beta2": 0.25,
        "gamma_deg": 22.0,
        "beta4": 0.0,
        "J_base_hbar2_per_MeV": 30.0,
        "j_aligned_hbar": 5.5,
        "spin_I": 19.5
    }
}


def calculate_hexadecapole_modified_moi(beta2, gamma_deg, beta4, J_base, kappa_4=1.85, kappa_44=0.60):
    """
    Calculates principal moments of inertia [J_s, J_m, J_l] with hexadecapole beta_4 correction.
    """
    gamma_rad = math.radians(abs(gamma_deg))

    # Pure quadrupole Hydrodynamic MOI: sin^2(gamma - 2*pi*k / 3)
    # Axis 1: short (s), Axis 2: intermediate (m), Axis 3: long (l)
    angles = [gamma_rad - 2.0 * math.pi / 3.0, gamma_rad - 4.0 * math.pi / 3.0, gamma_rad]

    J_unperturbed = []
    J_modified = []

    for k_idx, ang in enumerate(angles):
        sin_sq = (math.sin(ang))**2
        J_0 = J_base * sin_sq
        # Hexadecapole perturbation factor
        corr_factor = 1.0 + kappa_4 * beta4 * math.cos(ang) + kappa_44 * (beta4**2)
        J_mod = J_0 * max(0.05, corr_factor)

        J_unperturbed.append(float(J_0))
        J_modified.append(float(J_mod))

    # For gamma in (0, 60 deg), axis 1 (index 0) has sin^2(gamma - 120 deg) which is largest -> J_m
    # Axis 2 (index 1) -> J_s, Axis 3 (index 2) -> J_l
    J_m_0, J_s_0, J_l_0 = J_unperturbed[0], J_unperturbed[1], J_unperturbed[2]
    J_m_mod, J_s_mod, J_l_mod = J_modified[0], J_modified[1], J_modified[2]

    return {
        "unperturbed_MOI": {"J_s": J_s_0, "J_m": J_m_0, "J_l": J_l_0},
        "modified_MOI": {"J_s": J_s_mod, "J_m": J_m_mod, "J_l": J_l_mod},
        "J_m_enhancement_pct": float(((J_m_mod - J_m_0) / max(1e-4, J_m_0)) * 100.0)
    }


def calculate_wobbling_frequency_with_beta4(moi_dict, spin_I, j_aligned):
    """
    Evaluates wobbling frequency hbar*omega_w for both unperturbed and modified MOI.
    """
    def _calc_wob(J_s, J_m, J_l):
        if J_m <= J_s or J_m <= J_l or J_s <= 0 or J_l <= 0:
            return 0.0
        omega_rot = (spin_I - j_aligned) / J_m  # MeV
        wob_factor = math.sqrt(((J_m - J_s) * (J_m - J_l)) / (J_s * J_l))
        hw_keV = omega_rot * wob_factor * 1000.0  # keV
        return float(hw_keV)

    u = moi_dict["unperturbed_MOI"]
    m = moi_dict["modified_MOI"]

    hw_0 = _calc_wob(u["J_s"], u["J_m"], u["J_l"])
    hw_mod = _calc_wob(m["J_s"], m["J_m"], m["J_l"])

    delta_hw = hw_mod - hw_0
    pct_shift = (delta_hw / max(1.0, hw_0)) * 100.0 if hw_0 > 0 else 0.0

    return {
        "spin_I": float(spin_I),
        "j_aligned_hbar": float(j_aligned),
        "wobbling_freq_unperturbed_keV": float(hw_0),
        "wobbling_freq_modified_keV": float(hw_mod),
        "delta_wobbling_freq_keV": float(delta_hw),
        "fractional_shift_pct": float(pct_shift)
    }


def run_hexadecapole_wobbling_analysis(nucleus, beta2, gamma_deg, beta4, J_base, j_aligned, spin_I):
    """
    Complete execution pipeline for hexadecapole wobbling modification analysis.
    """
    moi_res = calculate_hexadecapole_modified_moi(beta2, gamma_deg, beta4, J_base)
    wob_res = calculate_wobbling_frequency_with_beta4(moi_res, spin_I, j_aligned)

    return {
        "nucleus": nucleus,
        "deformations": {
            "beta2": float(beta2),
            "gamma_deg": float(gamma_deg),
            "beta4": float(beta4)
        },
        "moi_analysis": moi_res,
        "wobbling_modification": wob_res
    }


def format_text_report(res, title="Triaxial Hexadecapole Wobbling Modifier"):
    nuc = res["nucleus"]
    d = res["deformations"]
    m = res["moi_analysis"]
    w = res["wobbling_modification"]

    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Nucleus: {nuc} | Deformations: beta2 = {d['beta2']:.3f}, gamma = {d['gamma_deg']:.1f} deg, beta4 = {d['beta4']:+.4f}")
    lines.append("=" * 76)
    lines.append("Principal Moments of Inertia [J_s, J_m, J_l] (hbar^2/MeV):")
    u = m["unperturbed_MOI"]
    mod = m["modified_MOI"]
    lines.append(f"  Pure Quadrupole (beta4 = 0)     : J_s = {u['J_s']:6.2f}, J_m = {u['J_m']:6.2f}, J_l = {u['J_l']:6.2f}")
    lines.append(f"  Hexadecapole Corrected (beta4)  : J_s = {mod['J_s']:6.2f}, J_m = {mod['J_m']:6.2f}, J_l = {mod['J_l']:6.2f}")
    lines.append(f"  Intermediate Axis (J_m) Shift   : {m['J_m_enhancement_pct']:+5.2f}%")
    lines.append("-" * 76)
    lines.append("Wobbling Excitation Frequency Perturbation (at spin I = {:.1f} hbar):".format(w["spin_I"]))
    lines.append(f"  Unperturbed Frequency hbar*omega_0 : {w['wobbling_freq_unperturbed_keV']:7.1f} keV")
    lines.append(f"  Modified Frequency hbar*omega_w    : {w['wobbling_freq_modified_keV']:7.1f} keV")
    lines.append(f"  Frequency Shift Delta(hbar*omega)  : {w['delta_wobbling_freq_keV']:+7.1f} keV ({w['fractional_shift_pct']:+5.2f}%)")
    lines.append("-" * 76)
    if d['beta4'] > 0:
        effect_str = "Positive beta4 enhances intermediate-axis dominance and stabilizes transverse wobbling."
    elif d['beta4'] < 0:
        effect_str = "Negative beta4 reduces MOI asymmetry, accelerating frequency decline towards TiP."
    else:
        effect_str = "Exact zero hexadecapole limit: strictly reproduces Bohr-Mottelson quadrupole rotor."
    lines.append(f"Physical Impact: {effect_str}")
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Triaxial Nuclear Hexadecapole Wobbling Modifier."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load benchmark preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        nucleus = p["nucleus"]
        b2 = p["beta2"]
        gamma = p["gamma_deg"]
        b4 = p["beta4"]
        jbase = p["J_base_hbar2_per_MeV"]
        jalign = p["j_aligned_hbar"]
        spin_I = p["spin_I"]
        title = f"Preset: {args.preset} ({p['description']})"
    else:
        return parser.print_help()

    res = run_hexadecapole_wobbling_analysis(
        nucleus=nucleus,
        beta2=b2,
        gamma_deg=gamma,
        beta4=b4,
        J_base=jbase,
        j_aligned=jalign,
        spin_I=spin_I
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
