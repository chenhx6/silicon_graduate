#!/usr/bin/env python3
"""
pulse_shape_discrimination_psd_calculator.py
============================================
Fast Neutron vs Gamma Scintillation Pulse Shape Discrimination (PSD),
Charge Comparison (CCM), Zero-Crossing (ZCM) & Figure of Merit (FOM) Analyzer.

Physics & Formulation:
----------------------
1. Scintillation Decay Mechanism:
   I(t) = I_0 * [ (1 - f_slow) * (1 / tau_fast) * exp(-t / tau_fast) +
                  f_slow * (1 / tau_slow) * exp(-t / tau_slow) ]
   where:
     tau_fast ~ 3.2 ns (prompt fluorescence from singlet states S1).
     tau_slow ~ 270 ns (delayed fluorescence from triplet-triplet annihilation T1 + T1).
   High dE/dx particles (fast neutrons via recoil protons): f_slow ~ 0.25 - 0.35.
   Low dE/dx particles (gamma-rays via Compton electrons): f_slow ~ 0.10 - 0.15.

2. Charge Comparison Method (CCM):
   Dual-gate integration:
     Q_total = integral_{0}^{t_long} I(t) dt
     Q_tail  = integral_{t_gate}^{t_long} I(t) dt
     PSD_parameter = Q_tail / Q_total

3. Zero-Crossing Method (ZCM):
   Bipolar shaping: CR-(RC)^2 filter transfer.
   Zero-crossing time t_zc is delayed for neutrons relative to gamma rays:
     Delta_t_zc = t_zc(neutron) - t_zc(gamma) ~ 15 - 35 ns.

4. Figure of Merit (FOM):
   FOM = S / (FWHM_n + FWHM_gamma) = |mu_n - mu_gamma| / [2.355 * (sigma_n + sigma_gamma)]
   - FOM < 1.0: Poor separation, cross-contamination.
   - FOM >= 1.27: 3-sigma separation (clean discrimination).
   - FOM >= 1.5: Excellent discrimination.
   FOM scales with light output: FOM(E) ~ FOM_0 * sqrt(E_MeVee).

References:
  - G. F. Knoll, Radiation Detection and Measurement, 4th ed., Wiley (2010).
  - 吴治华, 《原子核物理实验方法》, 第三版.
  - 汪晓莲等, 《粒子探测技术》.
  - R. A. Winyard et al., Nucl. Instrum. Methods 95, 141 (1971).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_charge_comparison_psd(
    f_slow_gamma: float = 0.12,
    f_slow_neutron: float = 0.28,
    tau_fast_ns: float = 3.2,
    tau_slow_ns: float = 270.0,
    t_tail_gate_ns: float = 30.0,
    t_long_gate_ns: float = 400.0
) -> Dict[str, Any]:
    """
    Computes theoretical Q_tail / Q_total ratio for gamma and neutron pulses.
    """
    def integrate_fraction(f_slow: float) -> Tuple[float, float, float]:
        f_fast = 1.0 - f_slow
        # Total charge integral 0 to t_long
        q_fast_tot = f_fast * (1.0 - math.exp(-t_long_gate_ns / tau_fast_ns))
        q_slow_tot = f_slow * (1.0 - math.exp(-t_long_gate_ns / tau_slow_ns))
        q_total = q_fast_tot + q_slow_tot

        # Tail charge integral t_tail to t_long
        q_fast_tail = f_fast * (math.exp(-t_tail_gate_ns / tau_fast_ns) - math.exp(-t_long_gate_ns / tau_fast_ns))
        q_slow_tail = f_slow * (math.exp(-t_tail_gate_ns / tau_slow_ns) - math.exp(-t_long_gate_ns / tau_slow_ns))
        q_tail = max(q_fast_tail + q_slow_tail, 0.0)

        psd_ratio = q_tail / max(q_total, 1e-6)
        return q_total, q_tail, psd_ratio

    _, _, psd_gamma = integrate_fraction(f_slow_gamma)
    _, _, psd_neutron = integrate_fraction(f_slow_neutron)

    separation = psd_neutron - psd_gamma

    return {
        "tau_fast_ns": tau_fast_ns,
        "tau_slow_ns": tau_slow_ns,
        "t_tail_gate_ns": t_tail_gate_ns,
        "t_long_gate_ns": t_long_gate_ns,
        "psd_ratio_gamma": round(psd_gamma, 4),
        "psd_ratio_neutron": round(psd_neutron, 4),
        "psd_centroid_separation": round(separation, 4)
    }


def calculate_figure_of_merit(
    mu_gamma: float = 0.15,
    sigma_gamma: float = 0.020,
    mu_neutron: float = 0.32,
    sigma_neutron: float = 0.028,
    energy_MeVee: float = 1.0
) -> Dict[str, Any]:
    """
    Computes Figure of Merit (FOM):
    FOM = |mu_n - mu_gamma| / [2.355 * (sigma_n + sigma_gamma)]
    """
    fwhm_gamma = 2.355 * sigma_gamma
    fwhm_neutron = 2.355 * sigma_neutron
    separation = abs(mu_neutron - mu_gamma)

    denom = fwhm_gamma + fwhm_neutron
    fom = separation / max(denom, 1e-6)

    # Energy scaling: FOM(E) ~ FOM * sqrt(E / 1.0)
    fom_scaled = fom * math.sqrt(max(energy_MeVee, 0.05))

    if fom_scaled < 1.0:
        verdict = "Poor_Separation (FOM < 1.0, significant n-gamma misidentification)"
    elif fom_scaled < 1.27:
        verdict = "Acceptable_Separation (1.0 <= FOM < 1.27, partial overlap)"
    elif fom_scaled < 1.5:
        verdict = "Clean_3Sigma_Separation (1.27 <= FOM < 1.5, in-beam spectroscopy grade)"
    else:
        verdict = "Excellent_Separation (FOM >= 1.5, pristine neutron tagging)"

    return {
        "energy_deposited_MeVee": energy_MeVee,
        "gamma_centroid_mu": mu_gamma,
        "gamma_fwhm": round(fwhm_gamma, 4),
        "neutron_centroid_mu": mu_neutron,
        "neutron_fwhm": round(fwhm_neutron, 4),
        "peak_separation": round(separation, 4),
        "fom_at_1MeVee": round(fom, 3),
        "fom_at_current_energy": round(fom_scaled, 3),
        "separation_verdict": verdict
    }


def simulate_zero_crossing_timing(
    tau_fast_ns: float = 3.2,
    tau_slow_ns: float = 270.0,
    f_slow_gamma: float = 0.12,
    f_slow_neutron: float = 0.28,
    shaping_time_ns: float = 40.0
) -> Dict[str, Any]:
    """
    Models zero-crossing time shift in CR-(RC)^2 bipolar shaping network.
    """
    # Analytical approximation for zero-crossing time:
    # t_zc ~ 2 * tau_shaping + C * (f_slow * tau_slow)
    t_zc_gamma = 2.0 * shaping_time_ns + 0.15 * f_slow_gamma * tau_slow_ns
    t_zc_neutron = 2.0 * shaping_time_ns + 0.15 * f_slow_neutron * tau_slow_ns
    delta_t_ns = t_zc_neutron - t_zc_gamma

    return {
        "bipolar_shaping_time_ns": shaping_time_ns,
        "zero_crossing_gamma_ns": round(t_zc_gamma, 2),
        "zero_crossing_neutron_ns": round(t_zc_neutron, 2),
        "zero_crossing_time_difference_ns": round(delta_t_ns, 2)
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   SCINTILLATOR PULSE SHAPE DISCRIMINATION (PSD) ANALYZER")
    lines.append("=" * 72)

    ccm = summary["charge_comparison"]
    lines.append(" DUAL-GATE CHARGE COMPARISON METHOD (CCM):")
    lines.append(f"   Fast Decay tau_fast            : {ccm['tau_fast_ns']} ns")
    lines.append(f"   Slow Decay tau_slow            : {ccm['tau_slow_ns']} ns")
    lines.append(f"   Tail Gate Window               : {ccm['t_tail_gate_ns']} ns to {ccm['t_long_gate_ns']} ns")
    lines.append(f"   Gamma PSD Ratio (Q_tail/Q_tot) : {ccm['psd_ratio_gamma']}")
    lines.append(f"   Neutron PSD Ratio (Q_tail/Q_tot): {ccm['psd_ratio_neutron']}")
    lines.append(f"   Centroid Separation Delta_PSD  : {ccm['psd_centroid_separation']}")
    lines.append("-" * 72)

    fom = summary["figure_of_merit"]
    lines.append(f" FIGURE OF MERIT (FOM) AUDIT (E = {fom['energy_deposited_MeVee']} MeVee):")
    lines.append(f"   Gamma Peak FWHM                : {fom['gamma_fwhm']}")
    lines.append(f"   Neutron Peak FWHM              : {fom['neutron_fwhm']}")
    lines.append(f"   Figure of Merit (FOM)          : {fom['fom_at_current_energy']}")
    lines.append(f"   Discrimination Quality         : {fom['separation_verdict']}")
    lines.append("-" * 72)

    zc = summary["zero_crossing"]
    lines.append(" ZERO-CROSSING METHOD (ZCM) BIPOLAR SHAPING:")
    lines.append(f"   Gamma Zero-Crossing Time       : {zc['zero_crossing_gamma_ns']} ns")
    lines.append(f"   Neutron Zero-Crossing Time     : {zc['zero_crossing_neutron_ns']} ns")
    lines.append(f"   Time Separation Delta_t_zc     : {zc['zero_crossing_time_difference_ns']} ns")
    lines.append("-" * 72)
    lines.append(" Physical Significance:")
    lines.append("   - Triplet-triplet delayed fluorescence drives high neutron tail charge.")
    lines.append("   - FOM >= 1.27 guarantees 3-sigma pure neutron tagging for in-beam arrays.")
    lines.append("   - Essential for (HI, xn) neutron wall and liquid scintillator filter arrays.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Scintillator Pulse Shape Discrimination (PSD) Analyzer."
    )
    parser.add_argument("--f-slow-g", type=float, default=0.12, help="Slow component fraction for gamma (default: 0.12)")
    parser.add_argument("--f-slow-n", type=float, default=0.28, help="Slow component fraction for neutron (default: 0.28)")
    parser.add_argument("--tau-fast", type=float, default=3.2, help="Fast decay time in ns (default: 3.2)")
    parser.add_argument("--tau-slow", type=float, default=270.0, help="Slow decay time in ns (default: 270.0)")
    parser.add_argument("--t-tail", type=float, default=30.0, help="Tail gate start time in ns (default: 30.0)")
    parser.add_argument("--t-long", type=float, default=400.0, help="Total gate length in ns (default: 400.0)")
    parser.add_argument("-E", "--energy-mevee", type=float, default=1.0, help="Electron equivalent energy in MeVee (default: 1.0)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    ccm_res = calculate_charge_comparison_psd(
        args.f_slow_g, args.f_slow_n, args.tau_fast, args.tau_slow, args.t_tail, args.t_long
    )
    fom_res = calculate_figure_of_merit(
        ccm_res["psd_ratio_gamma"], 0.020, ccm_res["psd_ratio_neutron"], 0.028, args.energy_mevee
    )
    zc_res = simulate_zero_crossing_timing(
        args.tau_fast, args.tau_slow, args.f_slow_g, args.f_slow_n
    )

    summary = {
        "charge_comparison": ccm_res,
        "figure_of_merit": fom_res,
        "zero_crossing": zc_res
    }

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
