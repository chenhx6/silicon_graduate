#!/usr/bin/env python3
"""
hpge_pulse_processing_pole_zero_calculator.py
=============================================
High-Rate HPGe Digital Pulse Processing, Pole-Zero Cancellation (PZC) &
Ballistic Deficit (BD) Simulator.

Physics & Formulation:
----------------------
1. Preamplifier Pulse Response:
   V_preamp(t) = V_0 * [1 - exp(-t / t_rise)] * exp(-t / tau_decay)
   tau_decay = R_f * C_f (typically 40 - 100 us).
   Charge collection time t_c in coaxial HPGe: typically 100 - 600 ns.

2. Pole-Zero Cancellation (PZC) in Digital Domain:
   Without PZC, CR differentiation leaves a long undershoot tail with time constant tau_decay.
   Discrete PZC filter (Jordanov recursive algorithm):
     p[n] = x[n] + (1 / M_pz) * sum_{k=0}^n x[k]
   where M_pz = 1 / [exp(T_s / tau_decay) - 1] ~ tau_decay / T_s.
   - Perfect match (tau_PZ == tau_decay): prompt return to baseline.
   - Under-compensation (tau_PZ < tau_decay): negative undershoot, high-rate count loss.
   - Over-compensation (tau_PZ > tau_decay): secondary positive tail, false triggers.

3. Ballistic Deficit (BD) in Coaxial HPGe Crystals:
   Because charge collection time t_c depends on interaction position (electron/hole drift),
   shaping without an adequate flat top causes amplitude depletion:
   - If t_flat >= t_c: Ballistic Deficit is exactly ZERO!
   - If t_flat < t_c:
       Relative Deficit = (1 / 12) * [(t_c - t_flat) / t_rise]^2
   Variation in t_c creates photopeak tailing and degrades FWHM resolution.

4. High-Rate Pileup & Dead Time Modeling:
   - Non-paralyzable dead time: Fraction_dead = R * tau_pulse / (1 + R * tau_pulse)
   - Paralyzable dead time: Fraction_dead = 1 - exp(-R * tau_pulse)
   - Peak pile-up probability: P_pileup = 1 - exp(-2 * R * tau_shaping)

References:
  - V. T. Jordanov and G. F. Knoll, Nucl. Instrum. Methods A 345, 337 (1994).
  - G. F. Knoll, Radiation Detection and Measurement, Wiley (2010).
  - 吴治华, 《原子核物理实验方法》, 第三版.
  - 汪晓莲等, 《粒子探测技术》.
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_ballistic_deficit(
    charge_collection_time_ns: float = 350.0,
    trapezoid_rise_time_ns: float = 2000.0,
    trapezoid_flat_top_ns: float = 800.0
) -> Dict[str, Any]:
    """
    Computes ballistic deficit for a trapezoidal filter:
    - If flat_top >= collection_time: BD = 0.
    - If flat_top < collection_time: BD = (1/12) * ((t_c - t_flat)/t_rise)^2.
    """
    t_c = charge_collection_time_ns
    t_r = trapezoid_rise_time_ns
    t_f = trapezoid_flat_top_ns

    if t_f >= t_c:
        deficit_fraction = 0.0
        status = "Zero_Ballistic_Deficit (Flat top fully covers charge collection time)"
    else:
        dt = t_c - t_f
        deficit_fraction = (1.0 / 12.0) * ((dt / t_r) ** 2)
        status = f"Deficit_Active (Flat top insufficient by {dt:.1f} ns)"

    fwhm_degradation_keV = deficit_fraction * 1332.5  # evaluated on Co-60 1332 keV peak

    return {
        "charge_collection_time_ns": t_c,
        "trapezoid_rise_time_ns": t_r,
        "trapezoid_flat_top_ns": t_f,
        "ballistic_deficit_fraction": round(deficit_fraction, 6),
        "ballistic_deficit_percent": round(deficit_fraction * 100.0, 4),
        "estimated_peak_shift_1332keV_keV": round(deficit_fraction * 1332.5, 3),
        "status": status
    }


def simulate_pole_zero_compensation(
    tau_preamp_us: float = 50.0,
    tau_pz_setting_us: float = 50.0,
    sampling_rate_mhz: float = 100.0,
    pulse_length_us: float = 20.0
) -> Dict[str, Any]:
    """
    Evaluates Pole-Zero Cancellation (PZC) quality:
    - Perfect cancellation: tau_pz == tau_preamp
    - Under-compensation: tau_pz < tau_preamp (undershoot)
    - Over-compensation: tau_pz > tau_preamp (overshoot)
    """
    dt_us = 1.0 / sampling_rate_mhz
    n_points = int(pulse_length_us / dt_us)

    # Preamp pulse: V(t) = exp(-t / tau_preamp)
    # Pole-Zero Jordanov recursive filter: y[n] = x[n] - x[n-1] + (dt / tau_pz) * x[n]
    m_ratio = tau_pz_setting_us / tau_preamp_us

    if abs(m_ratio - 1.0) < 0.01:
        quality = "Perfect_Cancellation (Baseline restored cleanly)"
        tail_residual = 0.0
    elif m_ratio < 1.0:
        quality = f"Under_Compensated (Negative undershoot, tail deficit = {(1.0 - m_ratio)*100:.1f}%)"
        tail_residual = round((m_ratio - 1.0), 4)
    else:
        quality = f"Over_Compensated (Positive tail bump, tail excess = {(m_ratio - 1.0)*100:.1f}%)"
        tail_residual = round((m_ratio - 1.0), 4)

    return {
        "tau_preamp_us": tau_preamp_us,
        "tau_pz_setting_us": tau_pz_setting_us,
        "ratio_PZ_over_preamp": round(m_ratio, 4),
        "residual_tail_fraction": tail_residual,
        "cancellation_verdict": quality
    }


def calculate_high_rate_pileup(
    input_count_rate_cps: float = 50000.0,
    trapezoid_rise_time_us: float = 2.0,
    trapezoid_flat_top_us: float = 0.8
) -> Dict[str, Any]:
    """
    Computes dead time, pile-up probability, and throughput rate:
    Total shaped pulse duration: tau_pulse = 2 * t_rise + t_flat.
    """
    tau_pulse_us = 2.0 * trapezoid_rise_time_us + trapezoid_flat_top_us
    tau_pulse_s = tau_pulse_us * 1e-6
    R = input_count_rate_cps

    # Non-paralyzable throughput: R_out = R / (1 + R * tau)
    out_non_paralyzable = R / (1.0 + R * tau_pulse_s)
    dead_time_non_par = (R * tau_pulse_s) / (1.0 + R * tau_pulse_s)

    # Paralyzable throughput: R_out = R * exp(-R * tau)
    out_paralyzable = R * math.exp(-R * tau_pulse_s)
    dead_time_par = 1.0 - math.exp(-R * tau_pulse_s)

    # Peak pile-up probability (two pulses arriving within shaping inspection time)
    p_pileup = 1.0 - math.exp(-2.0 * R * (trapezoid_rise_time_us * 1e-6))

    return {
        "input_rate_cps": R,
        "pulse_total_duration_us": round(tau_pulse_us, 2),
        "non_paralyzable_throughput_cps": round(out_non_paralyzable, 1),
        "non_paralyzable_dead_time_percent": round(dead_time_non_par * 100.0, 2),
        "paralyzable_throughput_cps": round(out_paralyzable, 1),
        "paralyzable_dead_time_percent": round(dead_time_par * 100.0, 2),
        "pileup_loss_probability_percent": round(p_pileup * 100.0, 2)
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   HPGe DIGITAL PULSE PROCESSING, PZC & BALLISTIC DEFICIT ANALYZER")
    lines.append("=" * 72)

    if "ballistic_deficit" in summary:
        bd = summary["ballistic_deficit"]
        lines.append(" BALLISTIC DEFICIT (BD) ASSESSMENT:")
        lines.append(f"   Charge Collection Time t_c     : {bd['charge_collection_time_ns']} ns")
        lines.append(f"   Trapezoid Rise Time t_r        : {bd['trapezoid_rise_time_ns']} ns")
        lines.append(f"   Trapezoid Flat-Top t_flat      : {bd['trapezoid_flat_top_ns']} ns")
        lines.append(f"   Deficit Fraction               : {bd['ballistic_deficit_percent']}%")
        lines.append(f"   Peak Shift on 1332 keV         : {bd['estimated_peak_shift_1332keV_keV']} keV")
        lines.append(f"   Status                         : {bd['status']}")
        lines.append("-" * 72)

    if "pole_zero" in summary:
        pz = summary["pole_zero"]
        lines.append(" POLE-ZERO CANCELLATION (PZC) INTEGRITY:")
        lines.append(f"   Preamplifier Decay Time tau    : {pz['tau_preamp_us']} us")
        lines.append(f"   Digitizer PZ Setting tau_pz    : {pz['tau_pz_setting_us']} us")
        lines.append(f"   Ratio PZ / Preamp              : {pz['ratio_PZ_over_preamp']}")
        lines.append(f"   Verdict                        : {pz['cancellation_verdict']}")
        lines.append("-" * 72)

    if "pileup" in summary:
        pu = summary["pileup"]
        lines.append(" HIGH-RATE THROUGHPUT & PILE-UP EVALUATION:")
        lines.append(f"   Input Event Rate               : {pu['input_rate_cps']} cps ({pu['input_rate_cps']/1e3:.1f} kcps)")
        lines.append(f"   Shaped Pulse Duration          : {pu['pulse_total_duration_us']} us")
        lines.append(f"   Non-Paralyzable Throughput     : {pu['non_paralyzable_throughput_cps']} cps (Dead: {pu['non_paralyzable_dead_time_percent']}%)")
        lines.append(f"   Paralyzable Throughput         : {pu['paralyzable_throughput_cps']} cps (Dead: {pu['paralyzable_dead_time_percent']}%)")
        lines.append(f"   Pile-up Coincidence Loss       : {pu['pileup_loss_probability_percent']}%")
        lines.append("-" * 72)

    lines.append(" Physical Significance:")
    lines.append("   - Solves resolution degradation in high-rate in-beam experiments.")
    lines.append("   - Ensure t_flat >= max(t_c) to eliminate asymmetric peak tailing.")
    lines.append("   - Exact PZC tuning eliminates baseline undershoot and false thresholds.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="HPGe Digital Pulse Processing, Pole-Zero & Ballistic Deficit Analyzer."
    )
    parser.add_argument("--tc-ns", type=float, default=350.0, help="Charge collection time in ns (default: 350.0)")
    parser.add_argument("--trise-ns", type=float, default=2000.0, help="Trapezoid rise time in ns (default: 2000.0)")
    parser.add_argument("--tflat-ns", type=float, default=800.0, help="Trapezoid flat-top in ns (default: 800.0)")
    parser.add_argument("--tau-preamp", type=float, default=50.0, help="Preamplifier decay time in us (default: 50.0)")
    parser.add_argument("--tau-pz", type=float, default=50.0, help="Digitizer PZ time constant in us (default: 50.0)")
    parser.add_argument("--rate-cps", type=float, default=50000.0, help="Input count rate in cps (default: 50000.0)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    bd_res = calculate_ballistic_deficit(args.tc_ns, args.trise_ns, args.tflat_ns)
    pz_res = simulate_pole_zero_compensation(args.tau_preamp, args.tau_pz)
    pu_res = calculate_high_rate_pileup(args.rate_cps, args.trise_ns * 1e-3, args.tflat_ns * 1e-3)

    summary = {
        "ballistic_deficit": bd_res,
        "pole_zero": pz_res,
        "pileup": pu_res
    }

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
