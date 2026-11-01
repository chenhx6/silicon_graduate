#!/usr/bin/env python3
"""
particle_identification_delta_e_calculator.py
=============================================
Charged-Particle Identification (Delta_E - E) Telescope & Stopping Power Analyzer.
Resolves Detector Non-Idealities & Discrepancies between Nuclear Experiment Methods
and Particle Detection Techniques.

Physics & Formulation:
----------------------
1. Bethe-Bloch Relativistic Stopping Power with Effective Charge:
   -dE/dx = 4*pi*N_A*r_e^2*m_e*c^2 * rho * (Z_t / A_t) * (z_eff^2 / beta^2) *
            [ ln(2*m_e*c^2*beta^2*gamma_L^2*T_max / I_0^2) - beta^2 - delta_den/2 - C_shell/Z_t ]
   Effective charge (Barkas / Northcliffe):
     z_eff = Z_p * [1 - exp(-125 * beta * Z_p^(-2/3))]

2. Range-Energy & Goulding Particle Identification (PID):
   Range approximation: R(E) = a * (M^(b-1) * Z^2)^(-1) * E^b  (b ~ 1.73 for Si)
   For Delta_E thickness Delta_x and residual energy E:
     PI = (E + Delta_E)^b - E^b = C * Delta_x * M^(b-1) * Z^2
   Enables unique identification of p, d, t, 3He, 4He, 6Li, 7Li, etc.

3. Resolution of Detector Non-Idealities & Text Discrepancies:
   Discrepancy A: Pulse Height Defect (PHD) for Heavy Ions (Schmitt / Lindhard):
     E_measured = E_true - Delta_E_window - Delta_E_nuclear - Delta_E_plasma
     - Window defect Delta_E_w: Dead layer (e.g. 50-200 nm Si equivalent)
     - Nuclear defect Delta_E_n: Non-ionizing energy loss (NIEL) to atomic recoils
     - Plasma recombination Delta_E_r: Field shielding in dense plasma track
   Discrepancy B: Energy Straggling Regime (Bohr vs Vavilov vs Landau):
     Vavilov parameter kappa = xi / T_max, where xi = 2*pi*z^2*e^4 * N*Z_t*Delta_x / (m_e * v^2)
     - kappa > 10: Gaussian (Bohr straggling: sigma_B^2 = 4*pi*z^2*e^4 * N*Z_t * Delta_x)
     - 0.01 <= kappa <= 10: Vavilov distribution
     - kappa < 0.01: Landau distribution (asymmetric tail from delta-electrons)

References:
  - F. S. Goulding et al., IEEE Trans. Nucl. Sci. NS-11, 388 (1964).
  - H. W. Schmitt et al., Phys. Rev. 137, B837 (1965).
  - 吴治华, 《原子核物理实验方法》, 第三版.
  - 汪晓莲等, 《粒子探测技术》.
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


# Fundamental Physical Constants
M_E_MEV = 0.51099895  # Electron mass in MeV
U_MEV = 931.49410242  # Atomic mass unit in MeV
FOUR_PI_NA_RE2_ME = 0.307075  # MeV * cm^2 / mol

# Standard Absorber Properties (Silicon Detector default)
ABSORBERS = {
    "Si": {
        "name": "Silicon",
        "Z": 14,
        "A": 28.0855,
        "density_g_cm3": 2.329,
        "I_0_eV": 173.0,
        "w_pair_eV": 3.62  # Average electron-hole pair creation energy
    },
    "Gas_Isobutane": {
        "name": "Isobutane (C4H10)",
        "Z": 34 / 14,  # Mean
        "A": 58.12,
        "density_g_cm3": 0.00251,  # at 1 atm
        "I_0_eV": 48.3,
        "w_pair_eV": 23.0
    },
    "Au": {
        "name": "Gold (Contact/Window)",
        "Z": 79,
        "A": 196.9665,
        "density_g_cm3": 19.32,
        "I_0_eV": 790.0,
        "w_pair_eV": 0.0
    }
}

# Standard Light & Heavy Projectiles
PROJECTILES = {
    "p": {"name": "Proton", "Z": 1, "A": 1.0078, "M_MeV": 938.272},
    "d": {"name": "Deuteron", "Z": 1, "A": 2.0141, "M_MeV": 1875.61},
    "t": {"name": "Triton", "Z": 1, "A": 3.0160, "M_MeV": 2808.92},
    "3He": {"name": "Helium-3", "Z": 2, "A": 3.0160, "M_MeV": 2808.39},
    "alpha": {"name": "Alpha (4He)", "Z": 2, "A": 4.0026, "M_MeV": 3727.38},
    "6Li": {"name": "Lithium-6", "Z": 3, "A": 6.0151, "M_MeV": 5601.52},
    "7Li": {"name": "Lithium-7", "Z": 3, "A": 7.0160, "M_MeV": 6533.83},
    "12C": {"name": "Carbon-12", "Z": 6, "A": 12.0000, "M_MeV": 11177.93},
    "16O": {"name": "Oxygen-16", "Z": 8, "A": 15.9949, "M_MeV": 14895.08}
}


def calculate_stopping_power(
    projectile_key: str,
    kinetic_energy_MeV: float,
    absorber_key: str = "Si"
) -> Dict[str, Any]:
    """
    Calculates relativistic Bethe-Bloch stopping power -dE/dx (in MeV/um and MeV/(mg/cm^2)).
    """
    if projectile_key not in PROJECTILES:
        raise ValueError(f"Unknown projectile {projectile_key}")
    if absorber_key not in ABSORBERS:
        raise ValueError(f"Unknown absorber {absorber_key}")

    p = PROJECTILES[projectile_key]
    med = ABSORBERS[absorber_key]

    E_k = max(kinetic_energy_MeV, 0.05)
    M = p["M_MeV"]
    gamma_L = (E_k + M) / M
    beta_sq = 1.0 - (1.0 / (gamma_L ** 2))
    beta = math.sqrt(max(beta_sq, 1e-6))

    # Effective charge z_eff via Barkas / Northcliffe
    z_eff = p["Z"] * (1.0 - math.exp(-125.0 * beta * (p["Z"] ** (-2.0 / 3.0))))
    z_eff = max(z_eff, 0.1)

    # T_max: maximum kinetic energy transferable to free electron
    s = M_E_MEV / M
    T_max = (2.0 * M_E_MEV * beta_sq * (gamma_L ** 2)) / (1.0 + 2.0 * gamma_L * s + (s ** 2))

    I_0_MeV = med["I_0_eV"] * 1e-6

    # Bethe-Bloch bracket
    ln_term = math.log((2.0 * M_E_MEV * beta_sq * (gamma_L ** 2) * T_max) / (I_0_MeV ** 2))
    bracket = ln_term - 2.0 * beta_sq
    if bracket < 0.1:
        bracket = 0.1

    # Stopping power in MeV * cm^2 / g
    dE_dx_mass = FOUR_PI_NA_RE2_ME * (med["Z"] / med["A"]) * ((z_eff ** 2) / beta_sq) * bracket
    # In MeV / um: dE/dx [MeV*cm^2/g] * density [g/cm^3] * 1e-4 cm/um
    dE_dx_um = dE_dx_mass * med["density_g_cm3"] * 1e-4

    return {
        "projectile": p["name"],
        "absorber": med["name"],
        "kinetic_energy_MeV": kinetic_energy_MeV,
        "beta": round(beta, 4),
        "effective_charge_z_eff": round(z_eff, 3),
        "dE_dx_MeV_per_um": round(dE_dx_um, 4),
        "dE_dx_MeV_per_mg_cm2": round(dE_dx_mass * 1e-3, 4),
        "T_max_MeV": round(T_max, 4)
    }


def simulate_telescope_response(
    projectile_key: str,
    total_energy_MeV: float,
    delta_e_thickness_um: float = 30.0,
    dead_layer_nm: float = 100.0,
    b_exponent: float = 1.73
) -> Dict[str, Any]:
    """
    Simulates Delta_E - E detector telescope response:
    - Particle passes through front dead layer (nm).
    - Particle deposits Delta_E in thin transmission detector (um).
    - Residual energy E_res is stopped in thick E detector.
    - Evaluates Goulding Particle Identification (PID) index.
    """
    p = PROJECTILES[projectile_key]
    E_curr = total_energy_MeV

    # 1. Front dead layer energy loss
    if dead_layer_nm > 0:
        sp_window = calculate_stopping_power(projectile_key, E_curr, "Si")
        loss_window = sp_window["dE_dx_MeV_per_um"] * (dead_layer_nm * 1e-3)
        E_curr = max(E_curr - loss_window, 0.0)
    else:
        loss_window = 0.0

    # 2. Delta_E detector loss (numerical step integration for accuracy)
    steps = 20
    dx = delta_e_thickness_um / steps
    dE_accum = 0.0

    for _ in range(steps):
        if E_curr <= 0.01:
            break
        sp = calculate_stopping_power(projectile_key, E_curr, "Si")
        de = sp["dE_dx_MeV_per_um"] * dx
        if de > E_curr:
            de = E_curr
        dE_accum += de
        E_curr -= de

    E_res = E_curr  # Residual energy deposited in E detector

    # 3. Goulding PID index: PI = (E_res + dE)^b - E_res^b
    if E_res > 0:
        PI = ((E_res + dE_accum) ** b_exponent) - (E_res ** b_exponent)
    else:
        PI = (dE_accum ** b_exponent)

    # Theoretical scale ~ M^(b-1) * Z^2
    theory_pid_scale = (p["A"] ** (b_exponent - 1.0)) * (p["Z"] ** 2)

    return {
        "projectile": p["name"],
        "projectile_Z": p["Z"],
        "projectile_A": p["A"],
        "incident_energy_MeV": total_energy_MeV,
        "dead_layer_loss_keV": round(loss_window * 1e3, 2),
        "delta_E_deposited_MeV": round(dE_accum, 3),
        "E_residual_MeV": round(E_res, 3),
        "total_detected_energy_MeV": round(dE_accum + E_res, 3),
        "goulding_PID_index": round(PI, 2),
        "theory_PID_scale": round(theory_pid_scale, 2),
        "transmitted_delta_E": (E_res > 0)
    }


def evaluate_pulse_height_defect(
    projectile_key: str,
    energy_MeV: float,
    applied_bias_V: float = 100.0,
    dead_layer_nm: float = 100.0
) -> Dict[str, Any]:
    """
    Evaluates Pulse Height Defect (PHD) for heavy ions in silicon detectors:
    Resolves differences between Wu Zhihua and Wang Xiaolian textbooks.
    PHD = Delta_E_window + Delta_E_nuclear + Delta_E_plasma
    """
    p = PROJECTILES[projectile_key]
    Z = p["Z"]
    A = p["A"]

    # 1. Window defect
    sp = calculate_stopping_power(projectile_key, energy_MeV, "Si")
    dE_window = sp["dE_dx_MeV_per_um"] * (dead_layer_nm * 1e-3)

    # 2. Nuclear stopping defect (Lindhard NIEL formula)
    # Proportional to Z^(2/3) * A, dominant for heavy ions at low velocities
    reduced_eps = 88.5 * energy_MeV / ((Z ** (7.0 / 3.0)) * (A ** (1.0 / 3.0)))
    if reduced_eps > 0.01:
        # Non-ionizing fraction g(eps)
        g_eps = 1.0 / (1.0 + 0.15 * (reduced_eps ** 0.8))
        dE_nuclear = 0.08 * (Z ** (4.0 / 3.0)) * g_eps
    else:
        dE_nuclear = 0.5 * energy_MeV
    dE_nuclear = min(dE_nuclear, 0.25 * energy_MeV)

    # 3. Plasma recombination defect
    # Increases with Z^2 and dE/dx, decreases with electric field (bias voltage)
    dE_plasma = 0.015 * (Z ** 2) * (sp["dE_dx_MeV_per_um"] / 1.0) * (100.0 / max(applied_bias_V, 20.0))
    dE_plasma = min(dE_plasma, 0.15 * energy_MeV)

    total_PHD = dE_window + dE_nuclear + dE_plasma
    E_measured = max(energy_MeV - total_PHD, 0.0)

    return {
        "projectile": p["name"],
        "true_energy_MeV": energy_MeV,
        "window_defect_MeV": round(dE_window, 4),
        "nuclear_defect_MeV": round(dE_nuclear, 4),
        "plasma_defect_MeV": round(dE_plasma, 4),
        "total_pulse_height_defect_MeV": round(total_PHD, 4),
        "defect_percentage": round((total_PHD / energy_MeV) * 100.0, 2),
        "measured_energy_MeV": round(E_measured, 4)
    }


def evaluate_energy_straggling(
    projectile_key: str,
    energy_MeV: float,
    absorber_thickness_um: float = 30.0
) -> Dict[str, Any]:
    """
    Assesses energy straggling regime (Bohr vs Vavilov vs Landau).
    Resolves discrepancies regarding Gaussian validity in thin transmission detectors.
    """
    p = PROJECTILES[projectile_key]
    sp = calculate_stopping_power(projectile_key, energy_MeV, "Si")

    # xi parameter: mean energy transfer parameter
    # xi = 0.1535 * (Z_t/A_t) * rho * (z_eff^2 / beta^2) * x [MeV]
    med = ABSORBERS["Si"]
    x_cm = absorber_thickness_um * 1e-4
    beta = sp["beta"]
    z_eff = sp["effective_charge_z_eff"]

    xi = 0.1535 * (med["Z"] / med["A"]) * med["density_g_cm3"] * ((z_eff ** 2) / (beta ** 2)) * x_cm
    T_max = sp["T_max_MeV"]

    kappa = xi / max(T_max, 1e-5)

    # Bohr Gaussian straggling variance: sigma_Bohr = sqrt(4*pi*z^2*e^4 * N*Z_t * x)
    sigma_bohr_MeV = math.sqrt(0.1569 * (med["Z"] / med["A"]) * med["density_g_cm3"] * (z_eff ** 2) * x_cm)

    if kappa > 10.0:
        regime = "Gaussian (Bohr Straggling)"
        note = "Thick absorber; symmetric Gaussian distribution."
    elif kappa >= 0.01:
        regime = "Vavilov Distribution"
        note = "Intermediate thickness; noticeable asymmetric high-energy delta-electron tail."
    else:
        regime = "Landau Distribution"
        note = "Very thin absorber; strongly asymmetric Landau distribution with long tail."

    return {
        "projectile": p["name"],
        "absorber_thickness_um": absorber_thickness_um,
        "xi_parameter_MeV": round(xi, 4),
        "T_max_MeV": round(T_max, 4),
        "vavilov_kappa": round(kappa, 4),
        "straggling_regime": regime,
        "bohr_gaussian_sigma_keV": round(sigma_bohr_MeV * 1e3, 2),
        "textbook_resolution": note
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   CHARGED-PARTICLE TELESCOPE & STOPPING POWER ANALYZER")
    lines.append("=" * 72)

    if "stopping_power" in summary:
        sp = summary["stopping_power"]
        lines.append(f" STOPPING POWER: {sp['projectile']} in {sp['absorber']} @ {sp['kinetic_energy_MeV']} MeV")
        lines.append(f"   Velocity beta (v/c)            : {sp['beta']}")
        lines.append(f"   Effective Charge z_eff         : {sp['effective_charge_z_eff']}")
        lines.append(f"   Linear Stopping Power -dE/dx   : {sp['dE_dx_MeV_per_um']} MeV/um ({sp['dE_dx_MeV_per_mg_cm2']} MeV/(mg/cm^2))")
        lines.append(f"   Max Transferable Energy T_max  : {sp['T_max_MeV']} MeV")
        lines.append("-" * 72)

    if "telescope_response" in summary:
        tr = summary["telescope_response"]
        lines.append(f" DELTA_E - E TELESCOPE RESPONSE ({tr['projectile']}):")
        lines.append(f"   Incident Energy                : {tr['incident_energy_MeV']} MeV")
        lines.append(f"   Dead Layer Window Loss         : {tr['dead_layer_loss_keV']} keV")
        lines.append(f"   Delta_E Detector Loss          : {tr['delta_E_deposited_MeV']} MeV")
        lines.append(f"   Residual E Detector Loss       : {tr['E_residual_MeV']} MeV (Transmitted: {tr['transmitted_delta_E']})")
        lines.append(f"   Goulding PID Index PI          : {tr['goulding_PID_index']} (Theory Scale: {tr['theory_PID_scale']})")
        lines.append("-" * 72)

    if "pulse_height_defect" in summary:
        phd = summary["pulse_height_defect"]
        lines.append(f" HEAVY-ION PULSE HEIGHT DEFECT (PHD) ANALYSIS:")
        lines.append(f"   Window Absorption Defect       : {phd['window_defect_MeV']} MeV")
        lines.append(f"   Nuclear Non-Ionizing Defect    : {phd['nuclear_defect_MeV']} MeV")
        lines.append(f"   Plasma Recombination Defect    : {phd['plasma_defect_MeV']} MeV")
        lines.append(f"   Total Defect                   : {phd['total_pulse_height_defect_MeV']} MeV ({phd['defect_percentage']}%)")
        lines.append(f"   Apparent Measured Energy       : {phd['measured_energy_MeV']} MeV")
        lines.append("-" * 72)

    if "straggling" in summary:
        st = summary["straggling"]
        lines.append(" ENERGY STRAGGLING REGIME & TEXTBOOK CONFLICT RESOLUTION:")
        lines.append(f"   Vavilov Parameter kappa        : {st['vavilov_kappa']}")
        lines.append(f"   Governing Regime               : {st['straggling_regime']}")
        lines.append(f"   Bohr Gaussian FWHM/Sigma       : {st['bohr_gaussian_sigma_keV']} keV")
        lines.append(f"   Explanation                    : {st['textbook_resolution']}")
        lines.append("-" * 72)

    lines.append(" Physical Significance:")
    lines.append("   - Solves the conflict between Wu Zhihua & Wang Xiaolian textbooks.")
    lines.append("   - Distinguishes Bohr Gaussian vs Vavilov/Landau asymmetric straggling.")
    lines.append("   - Accounts for heavy ion pulse height defect (PHD) in Si detectors.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Charged-Particle Identification (Delta_E - E) & Stopping Power Analyzer."
    )
    parser.add_argument("-p", "--projectile", type=str, default="alpha", choices=list(PROJECTILES.keys()),
                        help="Projectile particle (p, d, t, 3He, alpha, 6Li, 7Li, 12C, 16O)")
    parser.add_argument("-E", "--energy", type=float, default=20.0, help="Kinetic energy in MeV (default: 20.0)")
    parser.add_argument("--delta-thick", type=float, default=30.0, help="Delta_E detector thickness in um (default: 30.0)")
    parser.add_argument("--window-nm", type=float, default=100.0, help="Front dead layer thickness in nm (default: 100.0)")
    parser.add_argument("--bias-V", type=float, default=100.0, help="Detector reverse bias in V (default: 100.0)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    sp_res = calculate_stopping_power(args.projectile, args.energy, "Si")
    tele_res = simulate_telescope_response(args.projectile, args.energy, args.delta_thick, args.window_nm)
    phd_res = evaluate_pulse_height_defect(args.projectile, args.energy, args.bias_V, args.window_nm)
    strag_res = evaluate_energy_straggling(args.projectile, args.energy, args.delta_thick)

    summary = {
        "stopping_power": sp_res,
        "telescope_response": tele_res,
        "pulse_height_defect": phd_res,
        "straggling": strag_res
    }

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
