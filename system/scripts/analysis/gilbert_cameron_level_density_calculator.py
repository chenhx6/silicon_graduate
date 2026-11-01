#!/usr/bin/env python3
"""
gilbert_cameron_level_density_calculator.py
===========================================
Composite Gilbert-Cameron Nuclear Level Density Calculator with Ignatyuk
Shell Damping Parameterization.

Theory & Formulation:
---------------------
1. Shell Damping of Level Density Parameter (Ignatyuk 1975 / RIPL-2):
   a(U, Z, A) = a_tilde(A) * [1 + delta_W(Z, A) * (1 - exp(-gamma * U)) / U]
   where:
     a_tilde(A) = alpha * A + beta * A^(2/3)   (alpha=0.07224 MeV^-1, beta=0.1794 MeV^-1)
     delta_W(Z, A) = Ground-state shell correction energy (M_exp - M_LDM) [MeV]
     gamma = Shell damping factor ~ 0.054 - 0.0615 MeV^-1
     U = E - Delta (effective excitation energy)

2. Pairing Energy Shift (Delta):
   Delta = 12 / sqrt(A) * (delta_n + delta_p)
   where delta_n, delta_p = 1 for even, 0 for odd.
   Even-even: Delta ~ 24 / sqrt(A)
   Odd-A:     Delta ~ 12 / sqrt(A)
   Odd-odd:   Delta = 0

3. High-Energy Regime (U > U_x): Back-Shifted Fermi Gas (BSFG):
   rho_BSFG(U) = [sqrt(pi) / 12] * exp(2*sqrt(a*U)) / (a^(1/4) * U^(5/4)) * [1 / (sqrt(2*pi)*sigma)]
   Spin cut-off parameter:
   sigma^2(U) = 0.01389 * A^(5/3) * sqrt(U / a(U))

4. Low-Energy Regime (E <= E_x = U_x + Delta): Constant Temperature (CT):
   rho_CT(E) = (1 / T_0) * exp((E - E_0) / T_0)

5. Matching Conditions at E_x:
   rho_CT(E_x) = rho_BSFG(U_x)
   d/dE [ln rho_CT] = d/dE [ln rho_BSFG] = 1 / T_0
   yielding:
     1 / T_0 = sqrt(a/U_x) - 5 / (4 * U_x) + (U_x / a)^(1/2) * (da/dU)
     E_0 = E_x - T_0 * ln(T_0 * rho_BSFG(U_x))

6. Spin and Parity Distribution:
   rho(E, J, pi) = 0.5 * rho(E) * [(2J + 1) / (2 * sigma^2)] * exp(-(J + 0.5)^2 / (2 * sigma^2))

7. S-Wave Neutron Resonance Spacing D_0:
   For target nucleus with ground state spin I_0:
   If I_0 = 0: D_0 = 1 / rho(S_n, J=1/2)
   If I_0 > 0: D_0 = 1 / [rho(S_n, J=I_0 - 1/2) + rho(S_n, J=I_0 + 1/2)]

References:
  - A. Gilbert and A. G. W. Cameron, Can. J. Phys. 43, 1446 (1965).
  - A. V. Ignatyuk et al., Sov. J. Nucl. Phys. 21, 255 (1975).
  - IAEA-TECDOC-1035 / RIPL Handbook (1998 / 2006).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, Optional, Tuple, List


def weizsaecker_liquid_drop_mass(Z: int, A: int) -> float:
    """
    Computes smooth liquid-drop binding energy (in MeV) via Myers-Swiatecki / Bethe-Weizsaecker:
    B_LDM(Z, A) = a_v*A - a_s*A^(2/3) - a_c*Z*(Z-1)*A^(-1/3) - a_sym*(A - 2Z)^2/A
    """
    if A <= 0 or Z <= 0 or Z > A:
        return 0.0
    N = A - Z
    a_v = 15.67
    a_s = 17.23
    a_c = 0.714
    a_sym = 23.28

    vol = a_v * A
    surf = a_s * (A ** (2.0 / 3.0))
    coul = a_c * Z * (Z - 1.0) / (A ** (1.0 / 3.0))
    sym = a_sym * ((A - 2.0 * Z) ** 2) / A

    return vol - surf - coul - sym


def empirical_shell_correction(Z: int, A: int) -> float:
    """
    Empirical shell correction energy delta_W (MeV).
    Negative for magic nuclei (stronger binding than LDM), positive for mid-shell deformed.
    Uses Myers-Swiatecki closed-shell approximation:
    Magic numbers: 8, 20, 28, 50, 82, 126
    """
    magic_n = [2, 8, 20, 28, 50, 82, 126, 184]
    magic_z = [2, 8, 20, 28, 50, 82, 114]

    N = A - Z
    # Distance to nearest magic
    dist_z = min(abs(Z - m) for m in magic_z)
    dist_n = min(abs(N - m) for m in magic_n)

    # Maximum shell depression at double magic (e.g. Pb-208 ~ -12 MeV, Sn-132 ~ -11 MeV, Ca-40 ~ -8 MeV)
    w_z = -5.5 * math.exp(-0.15 * (dist_z ** 1.8))
    w_n = -6.5 * math.exp(-0.15 * (dist_n ** 1.8))

    # Deformed mid-shell slight positive correction (+1.5 to +3.0 MeV)
    def_mid = 2.2 * math.sin(math.pi * dist_z / 20.0) * math.sin(math.pi * dist_n / 25.0) if dist_z > 3 and dist_n > 3 else 0.0

    return round(w_z + w_n + def_mid, 3)


def calculate_pairing_shift(Z: int, A: int) -> float:
    """
    Computes pairing shift Delta (MeV) from standard Gilbert-Cameron parameterization:
    Even-even: 24 / sqrt(A)
    Odd-A:     12 / sqrt(A)
    Odd-odd:   0.0
    """
    if A <= 0:
        return 0.0
    n_even = ((A - Z) % 2 == 0)
    z_even = (Z % 2 == 0)

    if z_even and n_even:
        return 24.0 / math.sqrt(A)
    elif (not z_even) and (not n_even):
        return 0.0
    else:
        return 12.0 / math.sqrt(A)


def asymptotic_level_density_param(A: int, alpha: float = 0.07224, beta: float = 0.1794) -> float:
    """
    Asymptotic level density parameter a_tilde (MeV^-1).
    RIPL-2 default: alpha = 0.07224 MeV^-1, beta = 0.1794 MeV^-1
    a_tilde = alpha * A + beta * A^(2/3)
    """
    return alpha * A + beta * (A ** (2.0 / 3.0))


def ignatyuk_a_parameter(U: float, A: int, delta_W: float, a_tilde: float, gamma: float = 0.054) -> Tuple[float, float]:
    """
    Computes energy-dependent level density parameter a(U) and its derivative da/dU.
    a(U) = a_tilde * [1 + delta_W * (1 - exp(-gamma * U)) / U]
    Returns (a, da_dU).
    """
    if U <= 1e-4:
        # Limit as U -> 0: (1 - exp(-gamma*U))/U -> gamma
        a_val = a_tilde * (1.0 + delta_W * gamma)
        da_dU = -0.5 * a_tilde * delta_W * (gamma ** 2)
        return max(a_val, 0.5), da_dU

    exp_term = math.exp(-gamma * U)
    f_u = (1.0 - exp_term) / U
    a_val = a_tilde * (1.0 + delta_W * f_u)

    # Derivative of f(U): (gamma*exp(-gamma*U)*U - (1 - exp(-gamma*U))) / U^2
    df_dU = (gamma * exp_term * U - (1.0 - exp_term)) / (U ** 2)
    da_dU = a_tilde * delta_W * df_dU

    return max(a_val, 0.5), da_dU


def spin_cutoff_factor(U: float, A: int, a_val: float) -> float:
    """
    Spin cut-off parameter sigma^2:
    sigma^2 = 0.01389 * A^(5/3) * sqrt(U / a)
    With lower bound to avoid divergence.
    """
    eff_U = max(U, 0.1)
    s2 = 0.01389 * (A ** (5.0 / 3.0)) * math.sqrt(eff_U / max(a_val, 0.5))
    return max(s2, 1.0)


def bsfg_total_density(U: float, A: int, a_val: float) -> float:
    """
    Total Back-Shifted Fermi Gas level density rho_BSFG(U) in MeV^-1:
    rho(U) = [sqrt(pi) / 12] * exp(2*sqrt(a*U)) / (a^(1/4) * U^(5/4)) * [1 / (sqrt(2*pi)*sigma)]
    """
    eff_U = max(U, 0.05)
    s2 = spin_cutoff_factor(eff_U, A, a_val)
    sigma = math.sqrt(s2)

    sqrt_au = math.sqrt(a_val * eff_U)
    # Prevent overflow
    if 2.0 * sqrt_au > 700.0:
        exponent = 700.0
    else:
        exponent = 2.0 * sqrt_au

    denom = 12.0 * (a_val ** 0.25) * (eff_U ** 1.25) * math.sqrt(2.0 * math.pi) * sigma
    if denom <= 0:
        denom = 1e-6
    rho = (math.sqrt(math.pi) * math.exp(exponent)) / denom
    return rho


def solve_gilbert_cameron_matching(
    Z: int,
    A: int,
    delta_W: Optional[float] = None,
    gamma: float = 0.054,
    delta_pair: Optional[float] = None,
    a_tilde: Optional[float] = None
) -> Dict[str, float]:
    """
    Determines the matching energy U_x, nuclear temperature T_0, and backshift E_0
    for seamless tangency between Constant-Temperature (low-E) and Fermi Gas (high-E).
    """
    if delta_W is None:
        delta_W = empirical_shell_correction(Z, A)
    if delta_pair is None:
        delta_pair = calculate_pairing_shift(Z, A)
    if a_tilde is None:
        a_tilde = asymptotic_level_density_param(A)

    # Standard initial guess for U_x: U_x = 2.5 + 150.0 / A MeV (Gilbert-Cameron)
    U_x_guess = 2.5 + 150.0 / A

    # We evaluate at U_x_guess
    U_x = max(U_x_guess, 1.5)
    a_x, da_dU_x = ignatyuk_a_parameter(U_x, A, delta_W, a_tilde, gamma)

    # 1/T_0 = d/dU [ln rho_BSFG]
    inv_T0 = math.sqrt(a_x / U_x) - 1.5 / U_x
    if inv_T0 <= 0.05:
        inv_T0 = 0.05
    T_0 = 1.0 / inv_T0

    E_x = U_x + delta_pair
    rho_x = bsfg_total_density(U_x, A, a_x)

    # E_0 from matching: rho_CT(E_x) = (1/T_0) * exp((E_x - E_0)/T_0) = rho_x
    arg = max(T_0 * rho_x, 1e-12)
    E_0 = E_x - T_0 * math.log(arg)

    return {
        "U_x": round(U_x, 4),
        "E_x": round(E_x, 4),
        "T_0": round(T_0, 4),
        "E_0": round(E_0, 4),
        "rho_at_match": round(rho_x, 4),
        "a_tilde": round(a_tilde, 4),
        "a_at_match": round(a_x, 4),
        "delta_W": round(delta_W, 4),
        "delta_pair": round(delta_pair, 4)
    }


def compute_level_density(
    E: float,
    Z: int,
    A: int,
    J: Optional[float] = None,
    parity: Optional[int] = None,
    delta_W: Optional[float] = None,
    gamma: float = 0.054,
    match_params: Optional[Dict[str, float]] = None
) -> Dict[str, Any]:
    """
    Computes total and spin/parity-dependent level density at excitation energy E (MeV).
    """
    if match_params is None:
        match_params = solve_gilbert_cameron_matching(Z, A, delta_W, gamma)

    E_x = match_params["E_x"]
    T_0 = match_params["T_0"]
    E_0 = match_params["E_0"]
    delta_pair = match_params["delta_pair"]
    a_tilde = match_params["a_tilde"]
    dW = match_params["delta_W"]

    regime = "Constant_Temperature" if E <= E_x else "Back_Shifted_Fermi_Gas"

    if E <= E_x:
        # Constant temperature regime
        exponent = (E - E_0) / T_0
        if exponent > 700.0:
            exponent = 700.0
        rho_tot = (1.0 / T_0) * math.exp(exponent)
        eff_U = max(E - delta_pair, 0.1)
        a_curr, _ = ignatyuk_a_parameter(eff_U, A, dW, a_tilde, gamma)
        local_temp = T_0
    else:
        # Fermi gas regime
        eff_U = E - delta_pair
        a_curr, _ = ignatyuk_a_parameter(eff_U, A, dW, a_tilde, gamma)
        rho_tot = bsfg_total_density(eff_U, A, a_curr)
        local_temp = math.sqrt(eff_U / a_curr)

    s2 = spin_cutoff_factor(max(E - delta_pair, 0.1), A, a_curr)

    res = {
        "E_MeV": round(E, 4),
        "regime": regime,
        "rho_total_MeV_inv": rho_tot,
        "a_parameter_MeV_inv": round(a_curr, 4),
        "spin_cutoff_sigma2": round(s2, 3),
        "nuclear_temperature_MeV": round(local_temp, 4),
    }

    if J is not None:
        f_J = ((2.0 * J + 1.0) / (2.0 * s2)) * math.exp(-((J + 0.5) ** 2) / (2.0 * s2))
        rho_J = rho_tot * f_J
        if parity is not None:
            rho_J_pi = 0.5 * rho_J
            res["J"] = J
            res["parity"] = parity
            res["spin_distribution_f_J"] = round(f_J, 6)
            res["rho_J_pi_MeV_inv"] = rho_J_pi
            res["rho_J_MeV_inv"] = rho_J
        else:
            res["J"] = J
            res["spin_distribution_f_J"] = round(f_J, 6)
            res["rho_J_MeV_inv"] = rho_J

    return res


def calculate_s_wave_resonance_spacing(
    S_n: float,
    Z: int,
    A: int,
    target_I0: float = 0.0,
    delta_W: Optional[float] = None,
    gamma: float = 0.054
) -> Dict[str, Any]:
    """
    Computes average s-wave neutron resonance spacing D_0 (in eV) at neutron separation energy S_n.
    Target spin I_0:
      If I_0 = 0: compound states are J = 1/2+ (or 1/2-)
      If I_0 > 0: compound states are J_1 = I_0 - 1/2 and J_2 = I_0 + 1/2
    """
    match_params = solve_gilbert_cameron_matching(Z, A, delta_W, gamma)

    if target_I0 == 0.0:
        eval_res = compute_level_density(S_n, Z, A, J=0.5, parity=1, match_params=match_params)
        rho_res = eval_res["rho_J_pi_MeV_inv"]
    else:
        j1 = abs(target_I0 - 0.5)
        j2 = target_I0 + 0.5
        eval_1 = compute_level_density(S_n, Z, A, J=j1, parity=1, match_params=match_params)
        eval_2 = compute_level_density(S_n, Z, A, J=j2, parity=1, match_params=match_params)
        rho_res = eval_1["rho_J_pi_MeV_inv"] + eval_2["rho_J_pi_MeV_inv"]

    if rho_res > 0:
        D_0_eV = (1.0 / rho_res) * 1e6
    else:
        D_0_eV = float("inf")

    return {
        "compound_nucleus": f"Z={Z}, A={A}",
        "neutron_separation_energy_S_n_MeV": S_n,
        "target_ground_state_spin": target_I0,
        "resonant_density_MeV_inv": round(rho_res, 4),
        "average_s_wave_spacing_D_0_eV": round(D_0_eV, 2),
        "matching_params": match_params
    }


def cumulative_level_count(
    E_max: float,
    Z: int,
    A: int,
    num_steps: int = 100,
    delta_W: Optional[float] = None
) -> List[Dict[str, float]]:
    """
    Integrates level density from 0 to E_max to compute cumulative number of levels N(E) = int_0^E rho(E') dE'.
    Useful for comparing against discrete levels from ENSDF / RIPL.
    """
    match_params = solve_gilbert_cameron_matching(Z, A, delta_W)
    dE = E_max / float(num_steps)

    cum_levels = []
    current_N = 0.0
    prev_rho = 0.0

    for i in range(num_steps + 1):
        E = i * dE
        res = compute_level_density(E, Z, A, match_params=match_params)
        rho = res["rho_total_MeV_inv"]

        if i > 0:
            current_N += 0.5 * (prev_rho + rho) * dE

        cum_levels.append({
            "E_MeV": round(E, 3),
            "rho_total": round(rho, 3),
            "N_cumulative": round(current_N, 2)
        })
        prev_rho = rho

    return cum_levels


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   GILBERT-CAMERON LEVEL DENSITY WITH IGNATYUK SHELL DAMPING")
    lines.append("=" * 72)
    lines.append(f" Nucleus: Z = {summary.get('Z')}, A = {summary.get('A')}")
    lines.append(f" Pairing Shift Delta: {summary.get('pairing_shift_MeV'):.3f} MeV")
    lines.append(f" Ground-State Shell Correction delta_W: {summary.get('shell_correction_delta_W_MeV'):.3f} MeV")
    lines.append(f" Asymptotic Level Density Parameter a_tilde: {summary.get('asymptotic_a_MeV_inv'):.3f} MeV^-1")
    lines.append("-" * 72)
    lines.append(" MATCHING CHARACTERISTICS (CT <-> BSFG):")
    lines.append(f"   Matching Excitation Energy E_x : {summary.get('E_x_MeV'):.3f} MeV (U_x = {summary.get('U_x_MeV'):.3f} MeV)")
    lines.append(f"   Constant Temperature T_0        : {summary.get('T_0_MeV'):.3f} MeV")
    lines.append(f"   Energy Shift E_0               : {summary.get('E_0_MeV'):.3f} MeV")
    lines.append(f"   Level Density at Match Point   : {summary.get('rho_match_MeV_inv'):.2e} MeV^-1")
    lines.append("-" * 72)

    if "evaluated_energy" in summary:
        ev = summary["evaluated_energy"]
        lines.append(f" EVALUATION AT E = {ev['E_MeV']} MeV:")
        lines.append(f"   Regime                         : {ev['regime']}")
        lines.append(f"   Effective Level Density Param a: {ev['a_parameter_MeV_inv']:.3f} MeV^-1")
        lines.append(f"   Spin Cutoff Factor sigma^2     : {ev['spin_cutoff_sigma2']:.2f}")
        lines.append(f"   Total Level Density rho(E)     : {ev['rho_total_MeV_inv']:.3e} MeV^-1")
        if "rho_J_MeV_inv" in ev:
            lines.append(f"   Partial Density rho(E, J={ev['J']}) : {ev['rho_J_MeV_inv']:.3e} MeV^-1")
        if "rho_J_pi_MeV_inv" in ev:
            lines.append(f"   Parity Density rho(E, J={ev['J']}, pi) : {ev['rho_J_pi_MeV_inv']:.3e} MeV^-1")
        lines.append("-" * 72)

    if "resonance_spacing_D0" in summary:
        d0 = summary["resonance_spacing_D0"]
        lines.append(f" NEUTRON RESONANCE SPACING AT S_n = {d0['neutron_separation_energy_S_n_MeV']} MeV:")
        lines.append(f"   Target Spin I_0                : {d0['target_ground_state_spin']}")
        lines.append(f"   Compound Resonant State Density: {d0['resonant_density_MeV_inv']:.3e} MeV^-1")
        lines.append(f"   Predicted Average D_0          : {d0['average_s_wave_spacing_D_0_eV']:.2f} eV")
        lines.append("-" * 72)

    lines.append(" Physical Significance:")
    lines.append("   - Ignatyuk damping ensures shell effects melt at high excitation U.")
    lines.append("   - Constant-temperature formula models discrete state clustering at low E.")
    lines.append("   - Crucial input for Hauser-Feshbach, PACE4, CASCADE, and Oslo method.")
    lines.append("=" * 72)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Gilbert-Cameron Composite Level Density Calculator with Ignatyuk Shell Damping."
    )
    parser.add_argument("-Z", "--protons", type=int, required=True, help="Proton number Z")
    parser.add_argument("-A", "--mass", type=int, required=True, help="Mass number A")
    parser.add_argument("-E", "--energy", type=float, default=8.0, help="Excitation energy E in MeV (default: 8.0)")
    parser.add_argument("-J", "--spin", type=float, default=None, help="Spin J for spin-dependent density")
    parser.add_argument("-p", "--parity", type=int, default=None, choices=[1, -1], help="Parity (+1 or -1)")
    parser.add_argument("--sn", type=float, default=None, help="Neutron separation energy S_n in MeV for D_0 calculation")
    parser.add_argument("--target-spin", type=float, default=0.0, help="Target ground state spin I_0 (default: 0.0)")
    parser.add_argument("--delta-w", type=float, default=None, help="Shell correction delta_W in MeV (default: empirical)")
    parser.add_argument("--gamma", type=float, default=0.054, help="Ignatyuk damping factor gamma in MeV^-1 (default: 0.054)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    match = solve_gilbert_cameron_matching(args.protons, args.mass, args.delta_w, args.gamma)
    eval_res = compute_level_density(args.energy, args.protons, args.mass, args.spin, args.parity, match_params=match)

    summary = {
        "Z": args.protons,
        "A": args.mass,
        "pairing_shift_MeV": match["delta_pair"],
        "shell_correction_delta_W_MeV": match["delta_W"],
        "asymptotic_a_MeV_inv": match["a_tilde"],
        "E_x_MeV": match["E_x"],
        "U_x_MeV": match["U_x"],
        "T_0_MeV": match["T_0"],
        "E_0_MeV": match["E_0"],
        "rho_match_MeV_inv": match["rho_at_match"],
        "evaluated_energy": eval_res
    }

    if args.sn is not None:
        d0_res = calculate_s_wave_resonance_spacing(
            args.sn, args.protons, args.mass, args.target_spin, args.delta_w, args.gamma
        )
        summary["resonance_spacing_D0"] = d0_res

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
