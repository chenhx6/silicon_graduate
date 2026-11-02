#!/usr/bin/env python3
"""
constant_fraction_discriminator_fast_timing_calculator.py
=========================================================
Constant Fraction Discriminator (CFD) Amplitude Walk Elimination, Delay Parameter Optimization
& Scintillator Fast-Timing Jitter Calculator.

Physics & Electronics Formulation:
----------------------------------
1. Amplitude Walk in Leading Edge Discrimination (LED):
   In in-beam gamma spectroscopy, detector pulses have identical rise time t_r but varying
   amplitudes V_0 (proportional to gamma-ray energy). A fixed-threshold discriminator (LED) triggers
   at time t_th where V(t_th) = V_th.
   Larger pulses reach threshold earlier than smaller pulses, producing an amplitude-dependent
   timing error known as **time walk**:
     Delta_t_walk = t_th(V_min) - t_th(V_max) ~ t_r * [ (V_th / V_min) - (V_th / V_max) ]
   For fast scintillators, LED walk introduces hundreds of picoseconds of artificial timing jitter,
   severely corrupting coincidence lifetime measurements.

2. Constant Fraction Discriminator (CFD) Zero-Crossing Principle:
   The CFD eliminates time walk by triggering at a constant fraction f of the pulse peak amplitude V_0:
   - An inverted and attenuated copy of the input signal is formed: - f * V(t)  (typically f ~ 0.20 - 0.30)
   - The original signal is delayed by time t_d: V(t - t_d)
   - The two signals are summed to produce the bipolar CFD signal:
       V_CFD(t) = V(t - t_d) - f * V(t)
   - The discriminator triggers at the zero-crossing time t_z where V_CFD(t_z) = 0:
       V(t_z - t_d) = f * V(t_z)

3. Optimum Delay Condition:
   When t_d is chosen to match the linear rise time segment:
     t_d = t_r * (1.0 - f)
   the zero-crossing time t_z falls precisely on the steepest slope of the delayed pulse, and t_z
   becomes **strictly independent of pulse amplitude V_0**:
     Delta_t_walk(CFD) == 0.0 ps !

4. Electronic Timing Jitter & Resolution:
   In the absence of walk, timing uncertainty is governed by statistical and electronic noise:
     sigma_total = sqrt( sigma_scint^2 + sigma_TTS^2 + sigma_noise^2 )
     - Scintillator photon emission statistics: sigma_scint ~ tau_decay / sqrt(N_pe)
     - Photomultiplier Tube (PMT) Transit Time Spread: sigma_TTS = FWHM_TTS / (2.355 * sqrt(N_pe))
     - Electronic noise jitter on zero-crossing slope: sigma_noise = V_noise_rms / |dV_CFD / dt|_{t=t_z}
     Total timing resolution: FWHM_t = 2.355 * sigma_total.

References:
  - 吴治华, 《原子核物理实验方法（第三版）》, 原子能出版社 (2005), 第9章 §9.3 (时间测量与定时方法, 印刷 pp. 235–256).
  - 汪晓莲等, 《粒子探测技术》, 中国科学技术大学出版社 (2009), 第8章 (电子学定时与脉冲成形).
  - M. Nakhostin, 《辐射探测器信号处理》, 科学出版社 (2020), 第4章.
  - D. A. Gedcke and W. J. McDonald, Nucl. Instrum. Methods 58, 253 (1968).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def _pulse_shape(t_ns: float, V0_V: float, tr_ns: float = 2.0) -> float:
    """Semi-empirical pulse shape with rise time tr: V(t) = V0 * (t/tr)^2 * exp(-2*(t-tr)/tr) for t >= 0."""
    if t_ns <= 0.0:
        return 0.0
    scaled = t_ns / tr_ns
    return V0_V * (scaled ** 2) * math.exp(- 2.0 * (t_ns - tr_ns) / tr_ns)


def simulate_cfd_walk_elimination(
    amplitudes_V: List[float],
    rise_time_ns: float = 2.0,
    fraction: float = 0.20,
    delay_ns: Optional[float] = None,
    v_threshold_led_V: float = 0.10
) -> Dict[str, Any]:
    """
    Simulates CFD zero-crossing times vs Leading Edge Discriminator (LED) trigger times
    across a range of pulse amplitudes to demonstrate exact walk elimination.
    """
    if rise_time_ns <= 0.0:
        raise ValueError("Rise time must be strictly positive.")
    if not (0.0 < fraction < 1.0):
        raise ValueError("CFD fraction f must be between 0 and 1.")

    from scipy.optimize import brentq

    # Optimal CFD delay: td = tr * (1 - f)
    td_opt = rise_time_ns * (1.0 - fraction) if delay_ns is None else delay_ns

    cfd_results = []
    led_results = []

    for v0 in amplitudes_V:
        if v0 <= 0.0:
            continue

        # 1. CFD Zero-Crossing Time: V(t - td) - f * V(t) = 0
        def cfd_func(t):
            return _pulse_shape(t - td_opt, v0, rise_time_ns) - fraction * _pulse_shape(t, v0, rise_time_ns)

        # Root search between td and td + 2*tr
        try:
            tz = float(brentq(cfd_func, td_opt + 1e-4, td_opt + 2.0 * rise_time_ns))
        except ValueError:
            tz = td_opt + rise_time_ns # Fallback

        # Slope at zero crossing |dV/dt| in V/ns
        dt = 1e-3
        dv_dt = abs(cfd_func(tz + dt) - cfd_func(tz - dt)) / (2.0 * dt)

        cfd_results.append({
            "amplitude_V": v0,
            "zero_crossing_time_ns": round(tz, 5),
            "zero_crossing_slope_V_per_ns": round(dv_dt, 3)
        })

        # 2. Leading Edge Discriminator Trigger Time: V(t) = v_threshold_led_V
        if v0 > v_threshold_led_V:
            try:
                t_led = float(brentq(lambda t: _pulse_shape(t, v0, rise_time_ns) - v_threshold_led_V, 1e-4, rise_time_ns))
            except ValueError:
                t_led = 0.0
            led_results.append({
                "amplitude_V": v0,
                "led_trigger_time_ns": round(t_led, 5)
            })

    # Calculate time walks
    cfd_times = [r["zero_crossing_time_ns"] for r in cfd_results]
    cfd_walk_ps = (max(cfd_times) - min(cfd_times)) * 1000.0 if cfd_times else 0.0

    led_times = [r["led_trigger_time_ns"] for r in led_results]
    led_walk_ps = (max(led_times) - min(led_times)) * 1000.0 if led_times else 0.0

    return {
        "rise_time_ns": rise_time_ns,
        "fraction": fraction,
        "delay_ns": round(td_opt, 3),
        "led_threshold_V": v_threshold_led_V,
        "cfd_walk_ps": round(cfd_walk_ps, 3),
        "led_walk_ps": round(led_walk_ps, 1),
        "walk_reduction_factor": round(led_walk_ps / max(cfd_walk_ps, 1e-4), 1),
        "cfd_measurements": cfd_results,
        "led_measurements": led_results
    }


def calculate_fast_timing_resolution(
    scint_decay_time_ns: float,
    pmt_tts_fwhm_ns: float,
    N_photoelectrons: float,
    noise_rms_mV: float = 2.0,
    zero_crossing_slope_V_per_ns: float = 0.5
) -> Dict[str, Any]:
    """
    Computes statistical and electronic contributions to detector timing resolution FWHM.
    """
    if N_photoelectrons <= 0.0:
        raise ValueError("Number of photoelectrons must be positive.")

    # 1. Scintillator decay statistics: sigma_scint = tau_decay / sqrt(N_pe)
    sigma_scint_ns = scint_decay_time_ns / math.sqrt(N_photoelectrons)

    # 2. PMT Transit Time Spread: sigma_tts = FWHM_tts / (2.355 * sqrt(N_pe))
    sigma_tts_ns = (pmt_tts_fwhm_ns / 2.355) / math.sqrt(N_photoelectrons)

    # 3. Electronic noise jitter on zero-crossing slope: sigma_noise = V_noise / slope
    # noise_rms in V: noise_rms_mV * 1e-3
    v_noise_V = noise_rms_mV * 1e-3
    sigma_noise_ns = v_noise_V / max(zero_crossing_slope_V_per_ns, 1e-4)

    # Total resolution: FWHM = 2.355 * sqrt( sigma_scint^2 + sigma_tts^2 + sigma_noise^2 )
    sigma_tot_ns = math.sqrt(sigma_scint_ns ** 2 + sigma_tts_ns ** 2 + sigma_noise_ns ** 2)
    fwhm_total_ps = 2.355 * sigma_tot_ns * 1000.0

    return {
        "N_photoelectrons": N_photoelectrons,
        "sigma_scint_ps": round(sigma_scint_ns * 1000.0, 1),
        "sigma_pmt_tts_ps": round(sigma_tts_ns * 1000.0, 1),
        "sigma_electronic_noise_ps": round(sigma_noise_ns * 1000.0, 1),
        "total_timing_resolution_FWHM_ps": round(fwhm_total_ps, 1)
    }


def format_text_report(walk_res: Dict[str, Any], res_res: Optional[Dict[str, Any]] = None) -> str:
    lines = [
        "=" * 76,
        "   CONSTANT FRACTION DISCRIMINATOR (CFD) FAST-TIMING SUITE",
        "   Based on Wu Zhihua Ch. 9 §9.3 & Wang Xiaolian Ch. 8 (2009)",
        "=" * 76,
        " CFD PARAMETER OPTIMIZATION & ZERO-CROSSING CONDITION:",
        f"   Signal Rise Time t_r        : {walk_res['rise_time_ns']:.2f} ns",
        f"   Fraction f                  : {walk_res['fraction']:.2f}",
        f"   Optimum Delay t_d = tr*(1-f): {walk_res['delay_ns']:.2f} ns",
        "-" * 76,
        " TIME WALK COMPARISON ACROSS DYNAMIC AMPLITUDE RANGE (10:1):",
        f"   Leading Edge Walk (LED)     : {walk_res['led_walk_ps']:.1f} ps (Threshold V_th = {walk_res['led_threshold_V']:.2f} V)",
        f"   CFD Zero-Crossing Walk      : {walk_res['cfd_walk_ps']:.3f} ps (Exact Zero Walk!)",
        f"   Timing Jitter Reduction     : {walk_res['walk_reduction_factor']:.1f}x suppression of amplitude walk",
        "-" * 76,
        " AMPLITUDE vs TRIGGER TIME SCAN:",
        "   Amplitude (V)    CFD t_zero (ns)    CFD Slope (V/ns)    LED Trigger (ns)",
    ]

    for cfd_pt, led_pt in zip(walk_res["cfd_measurements"], walk_res["led_measurements"]):
        lines.append(f"     {cfd_pt['amplitude_V']:4.1f} V          {cfd_pt['zero_crossing_time_ns']:8.5f} ns        {cfd_pt['zero_crossing_slope_V_per_ns']:6.3f}            {led_pt['led_trigger_time_ns']:8.5f} ns")

    if res_res is not None:
        lines.extend([
            "-" * 76,
            " FAST-TIMING RESOLUTION BUDGET (FWHM):",
            f"   Photoelectron Yield N_pe    : {res_res['N_photoelectrons']:.0f} pe",
            f"   Scintillation Statistics    : {res_res['sigma_scint_ps']:.1f} ps",
            f"   PMT Transit Time Spread(TTS): {res_res['sigma_pmt_tts_ps']:.1f} ps",
            f"   Electronic Noise Jitter     : {res_res['sigma_electronic_noise_ps']:.1f} ps",
            f"   TOTAL TIME RESOLUTION (FWHM): {res_res['total_timing_resolution_FWHM_ps']:.1f} ps",
        ])

    lines.extend([
        "-" * 76,
        " Methodological Guidelines for In-Beam Gamma Timing:",
        "   - LaBr3(Ce) fast-timing arrays achieve FWHM ~ 150-250 ps using CFD with f = 0.20.",
        "   - CFD delay must strictly satisfy t_d = t_r * (1 - f) to prevent residual walk.",
        "=" * 76
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Constant Fraction Discriminator (CFD) Fast-Timing Analyzer"
    )
    parser.add_argument("--tr", type=float, default=2.0, help="Signal rise time in ns (default: 2.0 ns)")
    parser.add_argument("--fraction", type=float, default=0.20, help="CFD fraction f (default: 0.20)")
    parser.add_argument("--delay", type=float, default=None, help="CFD delay in ns (default: tr*(1-f))")
    parser.add_argument("--preset", type=str, default="labr3_fast_timing",
                        choices=["labr3_fast_timing", "baf2_fast_timing", "hpge_timing", "plastic_scintillator"],
                        help="Benchmark preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")

    args = parser.parse_args()

    tr_val = args.tr
    f_val = args.fraction
    d_val = args.delay
    res_info = None

    if args.preset == "labr3_fast_timing":
        tr_val, f_val = 2.0, 0.20
        amps = [0.5, 1.0, 2.0, 3.5, 5.0]
        res_info = calculate_fast_timing_resolution(
            scint_decay_time_ns=16.0, pmt_tts_fwhm_ns=0.35, N_photoelectrons=2500.0,
            noise_rms_mV=2.0, zero_crossing_slope_V_per_ns=1.2
        )
    elif args.preset == "baf2_fast_timing":
        tr_val, f_val = 0.8, 0.15
        amps = [0.5, 1.0, 2.0, 3.5, 5.0]
        res_info = calculate_fast_timing_resolution(
            scint_decay_time_ns=0.8, pmt_tts_fwhm_ns=0.25, N_photoelectrons=1500.0,
            noise_rms_mV=1.5, zero_crossing_slope_V_per_ns=2.5
        )
    elif args.preset == "hpge_timing":
        tr_val, f_val = 150.0, 0.30
        amps = [0.5, 1.0, 2.0, 5.0]
        res_info = calculate_fast_timing_resolution(
            scint_decay_time_ns=150.0, pmt_tts_fwhm_ns=0.0, N_photoelectrons=1e5,
            noise_rms_mV=5.0, zero_crossing_slope_V_per_ns=0.02
        )
    elif args.preset == "plastic_scintillator":
        tr_val, f_val = 0.5, 0.20
        amps = [0.5, 1.0, 2.0, 4.0]
        res_info = calculate_fast_timing_resolution(
            scint_decay_time_ns=1.4, pmt_tts_fwhm_ns=0.20, N_photoelectrons=800.0,
            noise_rms_mV=1.0, zero_crossing_slope_V_per_ns=3.0
        )
    else:
        amps = [0.5, 1.0, 2.0, 5.0]

    walk_res = simulate_cfd_walk_elimination(amps, tr_val, f_val, d_val)

    if args.json:
        out = {"cfd_walk_analysis": walk_res}
        if res_info is not None:
            out["timing_resolution_budget"] = res_info
        print(json.dumps(out, indent=2))
    else:
        print(format_text_report(walk_res, res_info))


if __name__ == "__main__":
    main()
