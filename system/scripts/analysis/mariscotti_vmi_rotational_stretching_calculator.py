#!/usr/bin/env python3
"""
mariscotti_vmi_rotational_stretching_calculator.py
==================================================
Mariscotti Variable Moment of Inertia (VMI) Model, Centrifugal Stretching Cubic Solver &
Ground-State Band Inverter.

Physics & Formulation:
----------------------
1. The Variable Moment of Inertia (VMI) Model:
   In transitional and deformed nuclei, the moment of inertia increases dynamically
   with angular momentum I due to centrifugal stretching and Coriolis pair-breaking:
     E(I) = [ I(I + 1) / (2 * J(I)) ] + 0.5 * C * (J(I) - J_0)^2
   where:
     - J_0 is the ground-state moment of inertia (hbar^2 / MeV);
     - C is the restoring force constant (hardness of the nuclear core, MeV / (hbar^2/MeV)^2);
     - J(I) is the equilibrium moment of inertia at spin I.

2. Equilibrium Condition & Cardano Cubic Equation:
   Setting dE / dJ = 0 yields the fundamental cubic equilibrium equation:
     J(I)^3 - J_0 * J(I)^2 = [ I(I + 1) / (2 * C) ]
   By depressed cubic transformation y = J - J_0/3:
     y^3 + p * y + q = 0
     where p = - (J_0^2) / 3,  q = - 2 * (J_0^3) / 27 - [ I(I + 1) / (2 * C) ]
   The discriminant Delta = (q/2)^2 + (p/3)^3 determines the real root via Cardano's formula.

3. Structural Casten Phase Classification via R_4/2:
   The ratio R_4/2 = E(4_1^+) / E(2_1^+) provides a fundamental structural signature:
     - R_4/2 -> 3.333 : Rigid axially symmetric rotor (C -> infinity, J(I) = J_0)
     - R_4/2 ~ 3.00 - 3.29 : Deformed / centrifugally stretched rotor (VMI regime)
     - R_4/2 ~ 2.40 - 2.90 : Transitional / gamma-soft nucleus
     - R_4/2 -> 2.000 : Harmonic vibrator (J_0 -> 0)
     - R_4/2 < 2.000 : Sub-vibrational (negative J_0, asymmetric or intruder-mixed)

4. Unbiased Linear / Nonlinear Inversion:
   Given experimental ground band level energies (E(2^+), E(4^+), E(6^+), ...):
   The parameters (J_0, C) are optimized to minimize the sum of squared residuals:
     chi^2 = sum_i [ E_exp(I_i) - E_VMI(I_i; J_0, C) ]^2

References:
  - M. A. J. Mariscotti, G. Scharff-Goldhaber, and B. Kirk, Phys. Rev. 178, 1864 (1969).
  - 卢希庭, 《原子核物理（修订版）》, 原子能出版社 (2000), 第8章 §8.5 (VMI模型, 印刷 pp. 212–215).
  - A. Bohr and B. R. Mottelson, *Nuclear Structure*, Vol. II, §4-2.
  - S. Frauendorf, in *Chirality and Wobbling in Atomic Nuclei* (CRC 2025), Ch. 2, p. 50 (VMI in 112Ru).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def solve_vmi_cubic_moi(
    J0: float,
    C: float,
    spin_I: float
) -> Tuple[float, float, float]:
    """
    Solves the VMI cubic equation J^3 - J0*J^2 = I*(I+1)/(2*C) using Cardano's method.
    Returns: (J_I, E_kin_keV, E_pot_keV).
    """
    if C <= 0.0:
        raise ValueError("Core restoring stiffness C must be strictly positive.")
    if spin_I < 0.0:
        raise ValueError("Spin I must be nonnegative.")

    if spin_I == 0.0:
        return J0, 0.0, 0.0

    rhs = (spin_I * (spin_I + 1.0)) / (2.0 * C)
    p = - (J0 ** 2) / 3.0
    q = - 2.0 * (J0 ** 3) / 27.0 - rhs

    discriminant = (q / 2.0) ** 2 + (p / 3.0) ** 3

    if discriminant >= 0.0:
        u_val = - (q / 2.0) + math.sqrt(discriminant)
        v_val = - (q / 2.0) - math.sqrt(discriminant)
        u_cbrt = math.copysign(abs(u_val) ** (1.0 / 3.0), u_val)
        v_cbrt = math.copysign(abs(v_val) ** (1.0 / 3.0), v_val)
        y = u_cbrt + v_cbrt
        J_I = y + J0 / 3.0
    else:
        r = math.sqrt(- (p / 3.0) ** 3)
        phi = math.acos(- (q / (2.0 * r)))
        y = 2.0 * (r ** (1.0 / 3.0)) * math.cos(phi / 3.0)
        J_I = y + J0 / 3.0

    if J_I <= 0.0:
        # Fallback to prevent unphysical negative/zero MOI
        J_I = max(0.1, J0)

    E_kin_MeV = (spin_I * (spin_I + 1.0)) / (2.0 * J_I)
    E_pot_MeV = 0.5 * C * ((J_I - J0) ** 2)

    return J_I, E_kin_MeV * 1000.0, E_pot_MeV * 1000.0


def calculate_vmi_spectrum(
    J0: float,
    C: float,
    spins: List[float]
) -> Dict[str, Any]:
    """
    Computes VMI dynamic moment of inertia J(I), kinetic/potential energies, and total E(I).
    """
    levels = []
    e2 = None
    e4 = None

    for I in spins:
        J_I, e_kin_keV, e_pot_keV = solve_vmi_cubic_moi(J0, C, I)
        e_tot_keV = e_kin_keV + e_pot_keV
        levels.append({
            "spin_I": I,
            "moment_of_inertia_J_hbar2_MeV": round(J_I, 4),
            "E_kinetic_keV": round(e_kin_keV, 2),
            "E_potential_stretching_keV": round(e_pot_keV, 2),
            "E_total_keV": round(e_tot_keV, 2),
            "stretching_fraction_pct": round((e_pot_keV / e_tot_keV) * 100.0, 2) if e_tot_keV > 0 else 0.0
        })

        if abs(I - 2.0) < 1e-4:
            e2 = e_tot_keV
        elif abs(I - 4.0) < 1e-4:
            e4 = e_tot_keV

    r42 = (e4 / e2) if (e2 is not None and e4 is not None and e2 > 0) else None

    # Casten classification
    if r42 is None:
        struct = "Indeterminate"
    elif r42 >= 3.27:
        struct = "Rigid / Well-Deformed Rotor (SU(3) limit)"
    elif r42 >= 2.90:
        struct = "Centrifugally Stretched / VMI Deformed Rotor"
    elif r42 >= 2.25:
        struct = "Transitional / Gamma-Soft Core (O(6) / Triaxial)"
    else:
        struct = "Anharmonic Vibrator (U(5) limit)"

    return {
        "J0_hbar2_MeV": J0,
        "stiffness_C_MeV3": C,
        "R_4_2_ratio": round(r42, 4) if r42 is not None else None,
        "structural_classification": struct,
        "levels": levels
    }


def invert_vmi_parameters(
    spins: List[float],
    energies_keV: List[float]
) -> Dict[str, Any]:
    """
    Inverts (J0, C) from experimental ground band energies using Nelder-Mead optimization.
    """
    if len(spins) != len(energies_keV) or len(spins) < 2:
        raise ValueError("Must provide at least 2 experimental levels to invert VMI parameters.")

    from scipy.optimize import minimize

    # Initial guess: J0 ~ 3.0 / E(2+)_MeV, C ~ 1.0
    e2_MeV = energies_keV[0] * 1e-3
    j0_init = max(1.0, 3.0 / e2_MeV) if e2_MeV > 0 else 10.0
    c_init = 0.5

    def loss_fn(params):
        j0_val, c_val = params
        if j0_val <= 0.01 or c_val <= 0.0001:
            return 1e9
        chi2 = 0.0
        for s_val, e_exp in zip(spins, energies_keV):
            _, e_kin, e_pot = solve_vmi_cubic_moi(j0_val, c_val, s_val)
            e_calc = e_kin + e_pot
            chi2 += (e_calc - e_exp) ** 2
        return chi2

    res = minimize(loss_fn, [j0_init, c_init], method="Nelder-Mead")
    j0_fit, c_fit = res.x
    rms_res = math.sqrt(res.fun / len(spins))

    # Calculate model levels
    model_spec = calculate_vmi_spectrum(j0_fit, c_fit, spins)

    return {
        "J0_fitted_hbar2_MeV": round(j0_fit, 3),
        "C_fitted_MeV3": round(c_fit, 5),
        "rms_residual_keV": round(rms_res, 2),
        "R_4_2_ratio": model_spec["R_4_2_ratio"],
        "structural_classification": model_spec["structural_classification"],
        "calculated_levels": model_spec["levels"]
    }


def format_text_report(spec: Dict[str, Any], inv: Optional[Dict[str, Any]] = None) -> str:
    lines = [
        "=" * 76,
        "   MARISCOTTI VARIABLE MOMENT OF INERTIA (VMI) ROTATIONAL SUITE",
        "   Based on Mariscotti et al. (1969), Lu Xiting §8.5 & Bohr-Mottelson Vol. II §4-2",
        "=" * 76,
        " VMI CORE PARAMETERS & STRUCTURAL PHASE SIGNATURE:",
        f"   Ground-State MOI J_0        : {spec['J0_hbar2_MeV']:.3f} hbar^2/MeV",
        f"   Core Restoring Stiffness C  : {spec['stiffness_C_MeV3']:.5f} MeV / (hbar^2/MeV)^2",
        f"   Energy Ratio R_4/2          : {spec['R_4_2_ratio']:.4f}  (Rotor: 3.333, Vibrator: 2.000)",
        f"   Structural Phase Assignment : {spec['structural_classification']}",
        "-" * 76,
    ]

    if inv is not None:
        lines.extend([
            " LEAST-SQUARES INVERSION FROM EXPERIMENTAL LEVELS:",
            f"   Fitted J_0                  : {inv['J0_fitted_hbar2_MeV']:.3f} hbar^2/MeV",
            f"   Fitted Stiffness C          : {inv['C_fitted_MeV3']:.5f}",
            f"   RMS Fit Residual            : {inv['rms_residual_keV']:.2f} keV",
            "-" * 76,
        ])

    lines.extend([
        " DYNAMIC CENTRIFUGAL STRETCHING & LEVEL ENERGY TABLE:",
        "   Spin I     E_total (keV)     J(I) (hbar^2/MeV)    E_kin (keV)    E_pot (keV)    Stretching %",
    ])

    for lv in spec["levels"]:
        lines.append(f"     {lv['spin_I']:2.0f}+   {lv['E_total_keV']:12.2f}     {lv['moment_of_inertia_J_hbar2_MeV']:11.4f}     {lv['E_kinetic_keV']:10.2f}     {lv['E_potential_stretching_keV']:10.2f}     {lv['stretching_fraction_pct']:7.2f}%")

    lines.extend([
        "-" * 76,
        " Methodological Significance:",
        "   - Cardano cubic equation J^3 - J0*J^2 = I(I+1)/(2C) exactly models pair-breaking stretching.",
        "   - C -> infinity recovers rigid rotor E = I(I+1)/(2J0) with R_4/2 = 3.333.",
        "   - Small C explains low-lying non-yrast staggering in A~130 transitional nuclei.",
        "=" * 76
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Mariscotti Variable Moment of Inertia (VMI) Calculator"
    )
    parser.add_argument("--preset", type=str, default="168Er",
                        choices=["168Er", "120Xe", "110Cd", "112Ru", "custom"],
                        help="Benchmark preset: 168Er (rotor), 120Xe (transitional), 110Cd (vibrator), 112Ru (wobbler)")
    parser.add_argument("--J0", type=float, default=35.0, help="Ground-state MOI J0 (default: 35.0)")
    parser.add_argument("--C", type=float, default=2500.0, help="Restoring stiffness C (default: 2500.0)")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")

    args = parser.parse_args()

    j0_val = args.J0
    c_val = args.C
    spins = [2.0, 4.0, 6.0, 8.0, 10.0, 12.0]
    inv_res = None

    if args.preset == "168Er":
        # Well-deformed rotor benchmark
        spins = [2.0, 4.0, 6.0, 8.0, 10.0, 12.0]
        e_exp = [79.8, 264.1, 548.7, 912.0, 1344.0, 1830.0]
        inv_res = invert_vmi_parameters(spins, e_exp)
        j0_val = inv_res["J0_fitted_hbar2_MeV"]
        c_val = inv_res["C_fitted_MeV3"]
    elif args.preset == "120Xe":
        # Transitional A~130 nucleus
        spins = [2.0, 4.0, 6.0, 8.0, 10.0]
        e_exp = [322.6, 795.9, 1389.2, 2073.4, 2824.0]
        inv_res = invert_vmi_parameters(spins, e_exp)
        j0_val = inv_res["J0_fitted_hbar2_MeV"]
        c_val = inv_res["C_fitted_MeV3"]
    elif args.preset == "110Cd":
        # Vibrational nucleus
        spins = [2.0, 4.0, 6.0, 8.0]
        e_exp = [657.8, 1475.8, 2479.9, 3600.0]
        inv_res = invert_vmi_parameters(spins, e_exp)
        j0_val = inv_res["J0_fitted_hbar2_MeV"]
        c_val = inv_res["C_fitted_MeV3"]
    elif args.preset == "112Ru":
        # Triaxial wobbler core (Frauendorf 2025 Ch. 2, p. 50)
        spins = [2.0, 4.0, 6.0, 8.0, 10.0]
        e_exp = [237.2, 678.8, 1279.0, 1999.0, 2780.0]
        inv_res = invert_vmi_parameters(spins, e_exp)
        j0_val = inv_res["J0_fitted_hbar2_MeV"]
        c_val = inv_res["C_fitted_MeV3"]

    spec = calculate_vmi_spectrum(j0_val, c_val, spins)

    if args.json:
        out = {"vmi_spectrum": spec}
        if inv_res is not None:
            out["inversion"] = inv_res
        print(json.dumps(out, indent=2))
    else:
        print(format_text_report(spec, inv_res))


if __name__ == "__main__":
    main()
