#!/usr/bin/env python3
"""
mwpc_drift_chamber_field_avalanche_simulator.py
===============================================
Multiwire Proportional Chamber (MWPC) & Drift Chamber Conformal Electrostatic Field,
Townsend Avalanche Gas Gain & Electron Drift Space-Time Calibration Simulator.

Physics Formulation:
--------------------
1. MWPC Conformal Mapping & Potential Field Distribution:
   Based on 汪晓莲等《粒子探测技术》第 3 章 (pp. 58–105), 吴治华《原子核物理实验方法》第 4 章,
   and F. Sauli (CERN 77-09, 1977):
   For an array of parallel anode wires along y=0 with pitch s and wire radius r0,
   centered between two planar cathode planes at y = +L and y = -L:
   Cathodes are grounded (V=0) and anode wires are biased to +V0.
   The charge per unit length q on each wire is given by:
     q / (2*pi*eps0) = V0 / [ (pi * L / s) - ln(2*pi * r0 / s) ]
   The analytical 2D potential at any point (x, y) is:
     V(x, y) = V0 - [ q / (4*pi*eps0) ] * [ (2*pi * L / s) - ln( 4 * ( sin(pi*x/s)^2 + sinh(pi*y/s)^2 ) ) ]

2. Asymptotic Fields (Near-Wire Avalanche vs Uniform Drift Region):
   - Near-wire region (r << s):
     E(r) = [ q / (2*pi*eps0) ] * (1 / r)
     Field at the anode surface: E(r0) ~ 10^5 - 10^6 V/cm, initiating electron avalanche.
   - Drift region (y >= s / 2):
     The field becomes nearly uniform:
     E_drift = [ q / (2*eps0*s) ] = (pi / s) * [ q / (2*pi*eps0) ]

3. First Townsend Ionization Coefficient & Gas Gain M:
   Townsend ionization coefficient:
     alpha(E) = A * P * exp( -B * P / E )
   For standard P-10 gas (90% Ar + 10% CH4 at P = 760 Torr):
     A ~ 14.0 cm^-1 * Torr^-1, B ~ 180.0 V / (cm * Torr).
   Gas avalanche multiplication factor:
     M = exp( integral_{r0}^{r_crit} alpha(E(r)) dr )
   In standard proportional operation: M ~ 10^4 - 10^6.

4. Drift Chamber Space-Time Relation x(t) & Diffusion Broadening:
   Under saturated drift velocity (v_d ~ 5.0 cm/us = 50 um/ns in typical drift gases):
     t_drift(x) = x / v_d
   Position resolution limit from thermal diffusion:
     sigma_x = sqrt( 2 * D * t_drift ) = sqrt( 2 * D * x / v_d )
     (where diffusion constant D ~ 100 - 200 um^2 / ns).
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "standard_mwpc_p10": {
        "description": "Standard MWPC with P-10 gas (s=2mm, L=5mm, r0=10um, V0=2600V)",
        "detector_type": "MWPC",
        "pitch_s_mm": 2.0,
        "gap_L_mm": 5.0,
        "wire_r0_um": 10.0,
        "voltage_V0": 2600.0,
        "gas_pressure_Torr": 760.0,
        "townsend_A": 14.0,
        "townsend_B": 180.0,
        "drift_velocity_cm_us": 5.0,
        "diffusion_D_um2_ns": 120.0
    },
    "high_gain_isobutane_mwpc": {
        "description": "High-gain MWPC with Ar-Isobutane mixture (s=2mm, L=6mm, r0=12.5um, V0=3200V)",
        "detector_type": "MWPC-Isobutane",
        "pitch_s_mm": 2.0,
        "gap_L_mm": 6.0,
        "wire_r0_um": 12.5,
        "voltage_V0": 3200.0,
        "gas_pressure_Torr": 760.0,
        "townsend_A": 16.5,
        "townsend_B": 195.0,
        "drift_velocity_cm_us": 5.2,
        "diffusion_D_um2_ns": 90.0
    },
    "drift_chamber_large_gap": {
        "description": "Large gap drift chamber cell (s=10mm, L=20mm, r0=20um, V0=3500V)",
        "detector_type": "Drift-Chamber",
        "pitch_s_mm": 10.0,
        "gap_L_mm": 20.0,
        "wire_r0_um": 20.0,
        "voltage_V0": 3500.0,
        "gas_pressure_Torr": 760.0,
        "townsend_A": 14.0,
        "townsend_B": 180.0,
        "drift_velocity_cm_us": 5.0,
        "diffusion_D_um2_ns": 150.0
    }
}


def calculate_electrostatic_field(pitch_s_mm, gap_L_mm, wire_r0_um, voltage_V0):
    """
    Calculates charge density, anode surface field, and uniform drift field.
    """
    s = pitch_s_mm * 1e-3  # m
    L = gap_L_mm * 1e-3    # m
    r0 = wire_r0_um * 1e-6 # m

    # Capacitance denominator
    term = (math.pi * L / s) - math.log(2.0 * math.pi * r0 / s)
    q_factor = voltage_V0 / term  # q / (2*pi*eps0) in Volts

    # Field at anode surface E(r0) in V/m
    E_surface_Vm = q_factor / r0
    E_surface_Vcm = E_surface_Vm / 100.0

    # Uniform drift field in the gap E_drift in V/m
    E_drift_Vm = (math.pi / s) * q_factor
    E_drift_Vcm = E_drift_Vm / 100.0

    return {
        "q_factor_V": float(q_factor),
        "E_surface_V_cm": float(E_surface_Vcm),
        "E_drift_V_cm": float(E_drift_Vcm),
        "capacitance_term": float(term)
    }


def calculate_townsend_gas_gain(q_factor_V, wire_r0_um, pressure_Torr, townsend_A, townsend_B, r_max_mm=0.5):
    """
    Integrates Townsend ionization coefficient alpha(E) from wire surface outward.
    """
    r0_cm = wire_r0_um * 1e-4  # cm
    r_max_cm = r_max_mm * 0.1  # cm

    # Radial integration grid
    r_pts = np.linspace(r0_cm, r_max_cm, 500)
    dr_cm = r_pts[1] - r_pts[0]

    # E(r) in V/cm: E(r) = (q_factor_V / r_meters) / 100 = q_factor_V / (r_cm)
    E_field_Vcm = q_factor_V / r_pts

    # alpha(E) = A * P * exp( -B * P / E )
    exponent = - (townsend_B * pressure_Torr) / np.maximum(1.0, E_field_Vcm)
    alpha = townsend_A * pressure_Torr * np.exp(np.clip(exponent, -50.0, 0.0))

    # Critical radius where avalanche starts (alpha > 1 cm^-1)
    active_indices = np.where(alpha > 1.0)[0]
    if len(active_indices) > 0:
        r_crit_um = float(r_pts[active_indices[-1]] * 1e4)
    else:
        r_crit_um = float(wire_r0_um)

    integral_alpha = float(np.sum(alpha) * dr_cm)
    gas_gain = float(math.exp(min(40.0, integral_alpha)))

    return {
        "avalanche_radius_rcrit_um": r_crit_um,
        "integrated_alpha": integral_alpha,
        "gas_gain_M": gas_gain
    }


def calculate_drift_space_time_relation(gap_L_mm, drift_velocity_cm_us, diffusion_D_um2_ns, n_steps=20):
    """
    Generates the space-time calibration grid: x -> t_drift -> diffusion spatial resolution sigma_x.
    """
    # v_d in mm / ns: 1 cm/us = 10 mm / 1000 ns = 0.01 mm/ns
    vd_mm_ns = drift_velocity_cm_us * 0.01

    x_vals_mm = np.linspace(0.5, gap_L_mm, n_steps)
    trajectory = []

    for x in x_vals_mm:
        t_ns = x / vd_mm_ns
        # sigma_x = sqrt(2 * D * t) in um
        sigma_um = math.sqrt(2.0 * diffusion_D_um2_ns * t_ns)
        trajectory.append({
            "drift_distance_mm": float(x),
            "drift_time_ns": float(t_ns),
            "diffusion_width_sigma_um": float(sigma_um)
        })

    return trajectory


def run_mwpc_simulation(pitch_s_mm, gap_L_mm, wire_r0_um, voltage_V0,
                        pressure_Torr=760.0, townsend_A=14.0, townsend_B=180.0,
                        drift_velocity_cm_us=5.0, diffusion_D_um2_ns=120.0):
    """
    Full MWPC and drift chamber simulation.
    """
    field = calculate_electrostatic_field(pitch_s_mm, gap_L_mm, wire_r0_um, voltage_V0)
    avalanche = calculate_townsend_gas_gain(
        field["q_factor_V"], wire_r0_um, pressure_Torr, townsend_A, townsend_B
    )
    drift = calculate_drift_space_time_relation(gap_L_mm, drift_velocity_cm_us, diffusion_D_um2_ns)

    return {
        "geometry": {
            "pitch_s_mm": float(pitch_s_mm),
            "gap_L_mm": float(gap_L_mm),
            "wire_r0_um": float(wire_r0_um),
            "voltage_V0": float(voltage_V0),
            "gas_pressure_Torr": float(pressure_Torr)
        },
        "electrostatic_field": field,
        "avalanche_gain": avalanche,
        "drift_trajectory": drift
    }


def format_text_report(res, title="MWPC & Drift Chamber Field & Avalanche Simulator"):
    geo = res["geometry"]
    fld = res["electrostatic_field"]
    ava = res["avalanche_gain"]

    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Geometry: Pitch s = {geo['pitch_s_mm']:.1f} mm, Gap L = {geo['gap_L_mm']:.1f} mm, Radius r0 = {geo['wire_r0_um']:.1f} um, Bias V0 = {geo['voltage_V0']:.0f} V")
    lines.append("=" * 76)
    lines.append(f"  Anode Wire Surface Field E(r0)  : {fld['E_surface_V_cm']:.2e} V/cm ({fld['E_surface_V_cm']/1e3:.1f} kV/cm)")
    lines.append(f"  Uniform Drift Field E_drift     : {fld['E_drift_V_cm']:.1f} V/cm")
    lines.append(f"  Effective Avalanche Boundary rc : {ava['avalanche_radius_rcrit_um']:.1f} um (from wire center)")
    lines.append(f"  Integrated Townsend Ionization  : int alpha dr = {ava['integrated_alpha']:.2f}")
    lines.append(f"  Total Gas Avalanche Gain M      : {ava['gas_gain_M']:.2e}")
    lines.append("-" * 76)
    lines.append("Drift Chamber Space-Time Calibration Samples:")
    lines.append("   Drift Distance x (mm)     Drift Time t (ns)     Diffusion Sigma_x (um)")
    for idx, pt in enumerate(res["drift_trajectory"]):
        if idx % max(1, len(res["drift_trajectory"]) // 6) == 0 or idx == len(res["drift_trajectory"]) - 1:
            lines.append(
                f"          {pt['drift_distance_mm']:6.2f}               {pt['drift_time_ns']:8.1f}               {pt['diffusion_width_sigma_um']:8.1f}"
            )
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="MWPC & Drift Chamber Field, Townsend Avalanche & Space-Time Simulator."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load experimental preset")
    parser.add_argument("--pitch-s", type=float, default=2.0, help="Anode wire pitch in mm")
    parser.add_argument("--gap-L", type=float, default=5.0, help="Cathode-anode gap in mm")
    parser.add_argument("--wire-r0", type=float, default=10.0, help="Anode wire radius in um")
    parser.add_argument("--voltage", type=float, default=2600.0, help="Anode high voltage in V")
    parser.add_argument("--pressure", type=float, default=760.0, help="Gas pressure in Torr")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        pitch_s = p["pitch_s_mm"]
        gap_L = p["gap_L_mm"]
        wire_r0 = p["wire_r0_um"]
        voltage = p["voltage_V0"]
        pressure = p.get("gas_pressure_Torr", 760.0)
        A = p.get("townsend_A", 14.0)
        B = p.get("townsend_B", 180.0)
        vd = p.get("drift_velocity_cm_us", 5.0)
        D = p.get("diffusion_D_um2_ns", 120.0)
        title = f"Preset: {args.preset} ({p['description']})"
    else:
        pitch_s = args.pitch_s
        gap_L = args.gap_L
        wire_r0 = args.wire_r0
        voltage = args.voltage
        pressure = args.pressure
        A = 14.0
        B = 180.0
        vd = 5.0
        D = 120.0
        title = "Custom User Input"

    res = run_mwpc_simulation(
        pitch_s_mm=pitch_s,
        gap_L_mm=gap_L,
        wire_r0_um=wire_r0,
        voltage_V0=voltage,
        pressure_Torr=pressure,
        townsend_A=A,
        townsend_B=B,
        drift_velocity_cm_us=vd,
        diffusion_D_um2_ns=D
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
