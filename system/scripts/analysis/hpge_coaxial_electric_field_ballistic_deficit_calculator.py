#!/usr/bin/env python3
"""
hpge_coaxial_electric_field_ballistic_deficit_calculator.py
===========================================================
HPGe Coaxial Detector Electric Field, Depletion Voltage, Shockley-Ramo Pulse Formation,
Ballistic Deficit & P-Type vs N-Type Fast-Neutron Radiation Hardness Reconciler.

Physics & Engineering Formulation:
----------------------------------
1. Coaxial Geometry & Depletion Voltage:
   High-purity Germanium (HPGe) at 77 K (liquid nitrogen) has relative permittivity eps_r = 16.0.
   For true coaxial geometry with inner radius r_1 and outer radius r_2:
   Poisson's equation for net space charge density rho = e * |N_A - N_D|:
     (1/r) d/dr [ r * dV/dr ] = -rho / eps
   The depletion voltage V_dep required to fully deplete the crystal from r_1 to r_2:
     V_dep = [ e * |N_A - N_D| / (2 * eps) ] * [ r_2^2 * ln(r_2 / r_1) - 0.5 * (r_2^2 - r_1^2) ]
   Operational bias V_bias must satisfy V_bias >= V_dep (typically 1.3 - 2.0 * V_dep) to ensure
   electric field E(r) >= 1000 V/cm (10^5 V/m) throughout the volume for carrier velocity saturation.

2. Electric Field Distribution:
   Under full depletion (V_bias >= V_dep):
     E(r) = -dV/dr = [ V_bias - (rho / (4 * eps)) * (r_2^2 - r_1^2) ] / [ r * ln(r_2 / r_1) ] + [ rho / (2 * eps) ] * r
   - In P-type HPGe (uncompensated acceptors N_A > N_D, negative space charge):
     E(r) is highest at the inner contact r_1 and decreases outwards.
   - In N-type HPGe (reverse electrode, positive donor space charge):
     E(r) distribution is inverted.

3. Shockley-Ramo Theorem & Charge Collection Time:
   The instantaneous current induced on the collection electrode by drifting charge q is:
     i(t) = q * v(r(t)) * E_w(r(t))
   where the weighting field for true coaxial geometry is:
     E_w(r) = 1 / [ r * ln(r_2 / r_1) ]
   Under saturated carrier drift (v_s ~ 10^7 cm/s = 10^5 m/s at 77 K):
   For gamma interaction at radius r_0:
     Electron drift time: t_e(r_0) = |r_0 - r_anode| / v_s
     Hole drift time    : t_h(r_0) = |r_cathode - r_0| / v_s
     Total collection time: t_c(r_0) = max(t_e(r_0), t_h(r_0))
     Maximum collection time: t_c_max = (r_2 - r_1) / v_s (typically 200 - 400 ns)

4. Ballistic Deficit:
   Dispersion in charge collection time delta_t_c causes output pulse peak attenuation:
   - For analog CR-(RC)^n / semi-Gaussian shaper with peaking time tau:
       Deficit_Gaussian ~ (1 / 12) * (t_c / tau)^2
   - For digital trapezoidal filter (Jordanov algorithm / Pixie-16) with flat-top T_flat:
       If T_flat >= t_c_max : Deficit_digital = 0.0 (exact zero ballistic deficit!)
       If T_flat < t_c_max  : Deficit_digital ~ (t_c_max - T_flat) / (T_rise + T_flat)

5. P-Type vs N-Type Neutron Radiation Hardness (Wu Zhihua vs Wang Xiaolian):
   Fast neutron irradiation (E_n > 1 MeV) produces vacancy cluster defects acting as hole traps.
   - P-type coaxial: Gamma interactions predominantly occur near the outer radius r_2. Holes must
     drift all the way inwards across (r_2 - r_1) to the central core => severe hole trapping,
     asymmetric low-energy tailing, and resolution degradation at fluence Phi_n >= 10^9 n/cm^2.
   - N-type coaxial (reverse electrode): Outer contact is cathode. Holes created near outer surface
     only drift a short distance delta_r << (r_2 - r_1) => hole trapping is minimized =>
     N-type detectors withstand Phi_n ~ 1 - 2 * 10^10 n/cm^2 (10 - 20x higher tolerance).

References:
  - 吴治华, 《原子核物理实验方法（第三版）》, 原子能出版社 (2005), 第5章 (半导体探测器, 印刷 pp. 135–150).
  - 汪晓莲等, 《粒子探测技术》, 中国科学技术大学出版社 (2009), 第5章 (半导体探测器, 印刷 pp. 180–225).
  - M. Nakhostin (吴鸿毅译), 《辐射探测器信号处理》, 科学出版社 (2020), 第1章 (感应电荷与Shockley-Ramo定理) & 第4章 (脉冲成形与弹道亏损).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_coaxial_depletion_and_field(
    r1_mm: float,
    r2_mm: float,
    N_net_cm3: float = 3.0e9,
    V_bias_V: float = 4000.0,
    detector_type: str = "p_type"
) -> Dict[str, Any]:
    """
    Calculates depletion voltage V_dep, overbias ratio, and electric field E(r) distribution.
    """
    if r1_mm <= 0.0 or r2_mm <= r1_mm:
        raise ValueError("Radii must satisfy 0 < r1 < r2.")
    if N_net_cm3 <= 0.0:
        raise ValueError("Net impurity concentration N_net must be positive.")
    if V_bias_V <= 0.0:
        raise ValueError("Bias voltage V_bias must be positive.")

    r1_m = r1_mm * 1e-3
    r2_m = r2_mm * 1e-3
    eps_r = 16.0 # Germanium at 77 K
    eps_0 = 8.854187817e-12 # F/m
    eps = eps_r * eps_0
    q_e = 1.602176634e-19 # C

    # Space charge density rho in C/m^3
    N_net_m3 = N_net_cm3 * 1e6
    rho = q_e * N_net_m3

    # Depletion voltage: V_dep = [ rho / (2*eps) ] * [ r2^2 * ln(r2/r1) - 0.5 * (r2^2 - r1^2) ]
    geom_factor = (r2_m ** 2) * math.log(r2_m / r1_m) - 0.5 * (r2_m ** 2 - r1_m ** 2)
    V_dep = (rho / (2.0 * eps)) * geom_factor

    overbias_ratio = V_bias_V / V_dep if V_dep > 0 else float("inf")
    is_fully_depleted = (V_bias_V >= V_dep)

    # Electric field calculation at inner contact, outer contact, and mid-radius
    # E(r) = [ V_bias - (rho / (4*eps))*(r2^2 - r1^2) ] / [ r * ln(r2/r1) ] + [ rho / (2*eps) ] * r
    const_term = (V_bias_V - (rho / (4.0 * eps)) * (r2_m ** 2 - r1_m ** 2)) / math.log(r2_m / r1_m)

    def calc_E(r_m):
        E_val = (const_term / r_m) + (rho / (2.0 * eps)) * r_m
        return E_val # V/m

    E_r1_V_cm = calc_E(r1_m) * 1e-2 # V/cm
    E_r2_V_cm = calc_E(r2_m) * 1e-2
    r_mid_m = 0.5 * (r1_m + r2_m)
    E_mid_V_cm = calc_E(r_mid_m) * 1e-2

    # Velocity saturation threshold ~ 1000 V/cm (10^5 V/m)
    E_min_V_cm = min(E_r1_V_cm, E_r2_V_cm, E_mid_V_cm)
    velocity_saturated = (E_min_V_cm >= 1000.0)

    return {
        "inner_radius_r1_mm": r1_mm,
        "outer_radius_r2_mm": r2_mm,
        "detector_type": detector_type,
        "net_impurity_N_cm3": N_net_cm3,
        "bias_voltage_V": V_bias_V,
        "depletion_voltage_V": round(V_dep, 1),
        "overbias_ratio": round(overbias_ratio, 2),
        "is_fully_depleted": is_fully_depleted,
        "E_inner_contact_V_per_cm": round(E_r1_V_cm, 1),
        "E_outer_contact_V_per_cm": round(E_r2_V_cm, 1),
        "E_midpoint_V_per_cm": round(E_mid_V_cm, 1),
        "is_velocity_saturated": velocity_saturated
    }


def calculate_shockley_ramo_collection(
    r0_mm: float,
    r1_mm: float = 5.0,
    r2_mm: float = 35.0,
    detector_type: str = "p_type"
) -> Dict[str, Any]:
    """
    Calculates carrier drift times and total charge collection time using Shockley-Ramo theorem.
    """
    if not (r1_mm < r0_mm < r2_mm):
        raise ValueError(f"Interaction radius r0 must be within crystal active volume ({r1_mm}, {r2_mm}).")

    vs_m_s = 1.0e5 # Saturated drift velocity at 77 K: 1.0e7 cm/s = 1.0e5 m/s

    r0_m = r0_mm * 1e-3
    r1_m = r1_mm * 1e-3
    r2_m = r2_mm * 1e-3

    if detector_type == "p_type":
        # Electrons drift to inner contact r1; holes drift to outer contact r2
        dist_e = r0_m - r1_m
        dist_h = r2_m - r0_m
    else:
        # N-type (reverse electrode): electrons drift to r2; holes drift to r1
        dist_e = r2_m - r0_m
        dist_h = r0_m - r1_m

    t_e_ns = (dist_e / vs_m_s) * 1e9
    t_h_ns = (dist_h / vs_m_s) * 1e9
    t_c_ns = max(t_e_ns, t_h_ns)
    t_c_max_ns = ((r2_m - r1_m) / vs_m_s) * 1e9

    # Weighting field at r0: E_w(r0) = 1 / [ r0 * ln(r2/r1) ]
    E_w_mm1 = 1.0 / (r0_mm * math.log(r2_mm / r1_mm))

    return {
        "interaction_radius_r0_mm": r0_mm,
        "electron_drift_distance_mm": round(dist_e * 1e3, 2),
        "hole_drift_distance_mm": round(dist_h * 1e3, 2),
        "electron_drift_time_ns": round(t_e_ns, 1),
        "hole_drift_time_ns": round(t_h_ns, 1),
        "total_collection_time_ns": round(t_c_ns, 1),
        "max_possible_collection_time_ns": round(t_c_max_ns, 1),
        "weighting_field_mm1": round(E_w_mm1, 4)
    }


def calculate_coaxial_ballistic_deficit(
    tc_ns: float,
    shaper_type: str = "trapezoidal",
    tau_gaussian_ns: float = 2000.0,
    rise_time_ns: float = 4000.0,
    flat_top_ns: float = 800.0
) -> Dict[str, Any]:
    """
    Calculates pulse height ballistic deficit for analog Gaussian vs digital trapezoidal filter.
    """
    if tc_ns <= 0.0:
        raise ValueError("Collection time must be positive.")

    # 1. Analog Gaussian / CR-(RC)^4: Deficit ~ (1/12) * (t_c / tau)^2
    deficit_gaussian_pct = (1.0 / 12.0) * ((tc_ns / tau_gaussian_ns) ** 2) * 100.0

    # 2. Digital Trapezoidal Filter:
    # If flat_top >= tc, the shaped pulse reaches full flat plateau without deficit!
    if flat_top_ns >= tc_ns:
        deficit_trapezoidal_pct = 0.0
        trap_status = "Exact Zero Deficit (Flat-top >= collection time)"
    else:
        # Insufficient flat-top introduces ballistic deficit
        deficit_trapezoidal_pct = ((tc_ns - flat_top_ns) / (rise_time_ns + flat_top_ns)) * 100.0
        trap_status = "Finite Deficit (Flat-top < collection time)"

    return {
        "charge_collection_time_ns": tc_ns,
        "gaussian_peaking_time_ns": tau_gaussian_ns,
        "gaussian_ballistic_deficit_pct": round(deficit_gaussian_pct, 4),
        "trapezoidal_flat_top_ns": flat_top_ns,
        "trapezoidal_rise_time_ns": rise_time_ns,
        "trapezoidal_ballistic_deficit_pct": round(deficit_trapezoidal_pct, 4),
        "trapezoidal_immunity_status": trap_status
    }


def reconcile_neutron_damage_p_vs_n(
    fast_neutron_fluence_n_cm2: float
) -> Dict[str, Any]:
    """
    Reconciles P-type vs N-type HPGe fast neutron damage, hole trapping and annealing thresholds.
    Based on Wu Zhihua Ch. 5 vs Wang Xiaolian Ch. 5.
    """
    if fast_neutron_fluence_n_cm2 < 0.0:
        raise ValueError("Neutron fluence must be nonnegative.")

    # P-type: hole collection travels full crystal diameter; resolution degrades above 10^9 n/cm^2
    if fast_neutron_fluence_n_cm2 < 1.0e8:
        p_status = "Normal (No observable degradation)"
        p_tailing = "Symmetric peak"
    elif fast_neutron_fluence_n_cm2 < 1.0e9:
        p_status = "Mild Trapping (Slight FWHM degradation, manageable with baseline restoration)"
        p_tailing = "Minor low-energy shoulder"
    elif fast_neutron_fluence_n_cm2 < 5.0e9:
        p_status = "Severe Degradation (Substantial peak broadening, thermal annealing required)"
        p_tailing = "Prominent low-energy tailing"
    else:
        p_status = "Detector Crippled (Severe hole trapping, completely loss of spectroscopic quality)"
        p_tailing = "Extreme asymmetric tail"

    # N-type: holes collected at outer contact; survives 10-20x higher fluence
    if fast_neutron_fluence_n_cm2 < 1.0e9:
        n_status = "Normal (No observable degradation)"
        n_tailing = "Symmetric peak"
    elif fast_neutron_fluence_n_cm2 < 1.0e10:
        n_status = "Good / Mild (Negligible resolution loss due to short hole collection path)"
        n_tailing = "Negligible tailing"
    elif fast_neutron_fluence_n_cm2 < 3.0e10:
        n_status = "Moderate Degradation (Thermal annealing required at 100-120 deg C)"
        n_tailing = "Moderate low-energy shoulder"
    else:
        n_status = "Severe Degradation (Requires extended thermal annealing cycle)"
        n_tailing = "Asymmetric tail"

    return {
        "neutron_fluence_n_cm2": fast_neutron_fluence_n_cm2,
        "p_type_coaxial_status": p_status,
        "p_type_peak_shape": p_tailing,
        "n_type_reverse_coaxial_status": n_status,
        "n_type_peak_shape": n_tailing,
        "neutron_hardness_advantage": "N-type (reverse electrode) has 10-20x higher fast-neutron tolerance because holes only travel short distances near the outer entrance window."
    }


def format_text_report(
    dep_res: Dict[str, Any],
    ramo_res: Optional[Dict[str, Any]] = None,
    bal_res: Optional[Dict[str, Any]] = None,
    neu_res: Optional[Dict[str, Any]] = None
) -> str:
    lines = [
        "=" * 76,
        "   HPGe COAXIAL ELECTRIC FIELD, PULSE FORMATION & BALLISTIC DEFICIT SUITE",
        "   Based on Wu Zhihua Ch. 5, Wang Xiaolian Ch. 5 & Nakhostin Ch. 1, 4 (2020)",
        "=" * 76,
        " COAXIAL GEOMETRY & FULL DEPLETION STATUS:",
        f"   Geometry Radii (r1, r2)     : ({dep_res['inner_radius_r1_mm']:.1f}, {dep_res['outer_radius_r2_mm']:.1f}) mm",
        f"   Net Impurity |N_A - N_D|    : {dep_res['net_impurity_N_cm3']:.2e} cm^-3",
        f"   Depletion Voltage V_dep     : {dep_res['depletion_voltage_V']:.1f} V",
        f"   Operational Bias V_bias     : {dep_res['bias_voltage_V']:.1f} V (Overbias Ratio: {dep_res['overbias_ratio']:.2f})",
        f"   Full Depletion Reached      : {dep_res['is_fully_depleted']}",
        "-" * 76,
        " ELECTRIC FIELD AT OPERATIONAL BIAS (77 K):",
        f"   E at Inner Contact (r1)     : {dep_res['E_inner_contact_V_per_cm']:.1f} V/cm",
        f"   E at Midpoint               : {dep_res['E_midpoint_V_per_cm']:.1f} V/cm",
        f"   E at Outer Contact (r2)     : {dep_res['E_outer_contact_V_per_cm']:.1f} V/cm",
        f"   Carrier Drift Saturation    : {dep_res['is_velocity_saturated']} (E >= 1000 V/cm throughout active volume)",
    ]

    if ramo_res is not None:
        lines.extend([
            "-" * 76,
            f" SHOCKLEY-RAMO CHARGE COLLECTION (Interaction at r0 = {ramo_res['interaction_radius_r0_mm']:.1f} mm):",
            f"   Electron Drift Time t_e     : {ramo_res['electron_drift_time_ns']:.1f} ns (distance: {ramo_res['electron_drift_distance_mm']:.1f} mm)",
            f"   Hole Drift Time t_h         : {ramo_res['hole_drift_time_ns']:.1f} ns (distance: {ramo_res['hole_drift_distance_mm']:.1f} mm)",
            f"   Total Collection Time t_c   : {ramo_res['total_collection_time_ns']:.1f} ns",
            f"   Max Possible Collection Time: {ramo_res['max_possible_collection_time_ns']:.1f} ns",
            f"   Weighting Field E_w(r0)     : {ramo_res['weighting_field_mm1']:.4f} mm^-1",
        ])

    if bal_res is not None:
        lines.extend([
            "-" * 76,
            " BALLISTIC DEFICIT COMPARISON (Collection Time t_c = {:.1f} ns):".format(bal_res['charge_collection_time_ns']),
            f"   Analog Gaussian (tau = {bal_res['gaussian_peaking_time_ns']:.0f} ns) : Deficit = {bal_res['gaussian_ballistic_deficit_pct']:.4f}%",
            f"   Digital Trapezoidal (Flat-top = {bal_res['trapezoidal_flat_top_ns']:.0f} ns): Deficit = {bal_res['trapezoidal_ballistic_deficit_pct']:.4f}% [{bal_res['trapezoidal_immunity_status']}]",
        ])

    if neu_res is not None:
        lines.extend([
            "-" * 76,
            f" FAST NEUTRON RADIATION DAMAGE RECONCILER (Fluence = {neu_res['neutron_fluence_n_cm2']:.1e} n/cm^2):",
            f"   P-Type Coaxial Status       : {neu_res['p_type_coaxial_status']} ({neu_res['p_type_peak_shape']})",
            f"   N-Type Reverse Coaxial Status: {neu_res['n_type_reverse_coaxial_status']} ({neu_res['n_type_peak_shape']})",
            f"   Physical Mechanism          : {neu_res['neutron_hardness_advantage']}",
        ])

    lines.extend([
        "-" * 76,
        " Methodological & Experimental Guidelines:",
        "   - Digital trapezoidal filters with Flat-top >= t_c_max completely eliminate ballistic deficit.",
        "   - For in-beam heavy-ion experiments with high neutron backgrounds, N-type HPGe is mandatory.",
        "=" * 76
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="HPGe Coaxial Electric Field, Pulse Formation & Ballistic Deficit Calculator"
    )
    parser.add_argument("--r1", type=float, default=5.0, help="Inner core radius in mm (default: 5.0 mm)")
    parser.add_argument("--r2", type=float, default=35.0, help="Outer radius in mm (default: 35.0 mm)")
    parser.add_argument("--net-impurity", type=float, default=3.0e9, help="Net impurity |N_A - N_D| in cm^-3 (default: 3.0e9)")
    parser.add_argument("--v-bias", type=float, default=4000.0, help="Operational bias voltage in Volts (default: 4000 V)")
    parser.add_argument("--r0", type=float, default=25.0, help="Interaction radius in mm (default: 25.0 mm)")
    parser.add_argument("--neutron-fluence", type=float, default=2.0e9, help="Fast neutron fluence in n/cm^2 (default: 2.0e9)")
    parser.add_argument("--preset", type=str, default="standard_coaxial_ptype",
                        choices=["standard_coaxial_ptype", "reverse_electrode_ntype", "large_clover_leaf"],
                        help="Benchmark preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")

    args = parser.parse_args()

    r1_val = args.r1
    r2_val = args.r2
    n_imp = args.net_impurity
    v_bias = args.v_bias
    r0_val = args.r0
    fluence = args.neutron_fluence
    det_type = "p_type"

    if args.preset == "standard_coaxial_ptype":
        r1_val, r2_val, n_imp, v_bias, det_type = 5.0, 35.0, 3.0e9, 4000.0, "p_type"
        r0_val = 25.0
    elif args.preset == "reverse_electrode_ntype":
        r1_val, r2_val, n_imp, v_bias, det_type = 5.0, 35.0, 3.0e9, 4000.0, "n_type"
        r0_val = 25.0
    elif args.preset == "large_clover_leaf":
        r1_val, r2_val, n_imp, v_bias, det_type = 4.0, 25.0, 2.5e9, 3000.0, "n_type"
        r0_val = 18.0

    dep_res = calculate_coaxial_depletion_and_field(r1_val, r2_val, n_imp, v_bias, det_type)
    ramo_res = calculate_shockley_ramo_collection(r0_val, r1_val, r2_val, det_type)
    bal_res = calculate_coaxial_ballistic_deficit(ramo_res["total_collection_time_ns"])
    neu_res = reconcile_neutron_damage_p_vs_n(fluence)

    if args.json:
        out = {
            "depletion_and_field": dep_res,
            "shockley_ramo": ramo_res,
            "ballistic_deficit": bal_res,
            "neutron_damage_reconciliation": neu_res
        }
        print(json.dumps(out, indent=2))
    else:
        print(format_text_report(dep_res, ramo_res, bal_res, neu_res))


if __name__ == "__main__":
    main()
