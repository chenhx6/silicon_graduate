#!/usr/bin/env python3
"""
in_beam_pulser_injection_live_time_corrector.py
==============================================
In-Beam High-Count-Rate Pulser Injection Live-Time Clock & Cascaded Pileup/ADC
Dead-Time Loss Compensation Suite.

Physics Formulation:
--------------------
1. Cascaded Dead Time in High-Rate Nuclear Spectroscopy:
   Based on 吴治华《原子核物理实验方法》第 8 章 §8.4 (pp. 210–225), 汪晓莲《粒子探测技术》第 8 章 §8.2,
   朱永生《实验物理中的概率和统计》第 4 章, and E. De Filippo et al. (NIM A 438, 397, 1999):
   In high-intensity in-beam experiments (detector event rates 20 - 80 kHz), event loss occurs
   through three distinct cascaded stages:
     a. Preamplifier and shaper pulse pileup rejection (paralyzable fast loss);
     b. Main amplifier and ADC conversion time (non-paralyzable Wilkinson or pipeline loss);
     c. DAQ event-builder buffer queueing and disk writing dead time.

2. Precision Pulser Injection Method:
   A periodic pulse generator injects precision charge pulses of stable frequency f_pulser into
   the preamplifier test input throughout the measurement run time T_real.
   The total injected pulses are:
     N_injected = f_pulser * T_real.
   In the final calibrated energy spectrum, the recorded pulser peak area is N_recorded.
   The true overall Live-Time Fraction is:
     LT = N_recorded / N_injected.
   The binomial variance of the live-time fraction is:
     sigma_LT = sqrt[ LT * (1 - LT) / N_injected ].

3. Absolute Peak Area Correction & Compound Error Propagation:
   For any physical gamma transition with observed peak area A_meas +- sigma_A_meas:
     A_true = A_meas / LT.
   The exact compound variance (combining Poisson counting of the peak with binomial sampling
   of the pulser live-time monitor) is:
     (sigma_A_true / A_true)^2 = (sigma_A_meas / A_meas)^2 + (sigma_LT / LT)^2.

4. Critical Discrepancy: Pulser vs Hardware Gated Clock (LTC):
   Standard hardware live-time clocks (LTC) monitor only ADC/DAQ busy logic gates, being completely
   blind to fast analog pileup rejection in the preamplifier/shaper.
   The unmonitored analog pileup loss fraction is:
     f_pileup = (LT_hardware - LT_pulser) / LT_hardware.
   Ignoring this discrepancy systematically underestimates cross sections and absolute transition
   rates by 5% - 20%!
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "in_beam_high_rate_clover_130Ba": {
        "description": "High-rate (45 kHz) in-beam 130Ba run with 50 Hz pulser (reveals 8.1% pileup loss)",
        "experiment": "130Ba high-spin in-beam fusion",
        "real_time_s": 7200.0,
        "pulser_frequency_Hz": 50.0,
        "pulser_recorded_counts": 278640,
        "hardware_clock_live_time": 0.842,
        "physical_peaks": [
            {"energy_keV": 328.0, "measured_area": 84500.0, "sigma_area": 320.0},
            {"energy_keV": 455.0, "measured_area": 42100.0, "sigma_area": 230.0},
            {"energy_keV": 638.0, "measured_area": 29800.0, "sigma_area": 195.0}
        ]
    },
    "moderate_rate_germanium_array": {
        "description": "Moderate-rate (12 kHz) in-beam run with 100 Hz pulser (LT ~ 0.925)",
        "experiment": "Medium-spin spectroscopy run",
        "real_time_s": 3600.0,
        "pulser_frequency_Hz": 100.0,
        "pulser_recorded_counts": 333000,
        "hardware_clock_live_time": 0.945,
        "physical_peaks": [
            {"energy_keV": 511.0, "measured_area": 65000.0, "sigma_area": 280.0},
            {"energy_keV": 1173.2, "measured_area": 34000.0, "sigma_area": 200.0}
        ]
    },
    "pure_low_rate_calibration": {
        "description": "Low-rate (1.5 kHz) radioactive source calibration (LT ~ 0.988)",
        "experiment": "152Eu source efficiency calibration",
        "real_time_s": 1800.0,
        "pulser_frequency_Hz": 20.0,
        "pulser_recorded_counts": 35568,
        "hardware_clock_live_time": 0.991,
        "physical_peaks": [
            {"energy_keV": 344.3, "measured_area": 18500.0, "sigma_area": 140.0},
            {"energy_keV": 1408.0, "measured_area": 4200.0, "sigma_area": 70.0}
        ]
    }
}


def calculate_pulser_live_time(real_time_s, pulser_freq_Hz, recorded_counts):
    """
    Calculates pulser-based live-time fraction and binomial uncertainty.
    """
    n_inj = real_time_s * pulser_freq_Hz
    n_rec = float(recorded_counts)

    if n_inj <= 0:
        return {"live_time_fraction": 1.0, "sigma_live_time": 0.0, "dead_time_pct": 0.0}

    lt = min(1.0, max(0.0, n_rec / float(n_inj)))
    # Binomial variance: Var(p) = p*(1-p) / N
    var_lt = (lt * (1.0 - lt)) / float(n_inj)
    sig_lt = math.sqrt(max(0.0, var_lt))
    dead_time_pct = (1.0 - lt) * 100.0

    return {
        "pulses_injected": float(n_inj),
        "pulses_recorded": float(n_rec),
        "live_time_fraction": float(lt),
        "sigma_live_time": float(sig_lt),
        "dead_time_pct": float(dead_time_pct)
    }


def correct_peaks(peaks, lt_info):
    """
    Applies live-time correction to physical gamma peaks with compound error propagation.
    """
    lt = lt_info["live_time_fraction"]
    sig_lt = lt_info["sigma_live_time"]

    corrected = []
    for p in peaks:
        E = p["energy_keV"]
        A_meas = float(p["measured_area"])
        sig_meas = float(p["sigma_area"])

        A_true = A_meas / max(1e-6, lt)
        # Compound variance
        rel_meas_sq = (sig_meas / max(1.0, A_meas))**2
        rel_lt_sq = (sig_lt / max(1e-6, lt))**2
        sig_true = A_true * math.sqrt(rel_meas_sq + rel_lt_sq)

        correction_factor = 1.0 / max(1e-6, lt)

        corrected.append({
            "energy_keV": float(E),
            "measured_area": A_meas,
            "sigma_measured_area": sig_meas,
            "true_area": float(A_true),
            "sigma_true_area": float(sig_true),
            "correction_multiplier": float(correction_factor),
            "relative_error_pct": float((sig_true / max(1.0, A_true)) * 100.0)
        })
    return corrected


def diagnose_hardware_clock_bias(lt_pulser, lt_hardware):
    """
    Evaluates the unmonitored analog pileup loss hidden from hardware busy clock.
    """
    if lt_hardware <= 0.0:
        return {"unmonitored_pileup_loss_pct": 0.0, "hardware_clock_bias_severity": "UNKNOWN"}

    pileup_loss = max(0.0, (lt_hardware - lt_pulser) / float(lt_hardware))
    pileup_pct = pileup_loss * 100.0

    if pileup_pct > 6.0:
        sev = "HIGH_ANALOG_PILEUP_LOSS (LTC invalid)"
    elif pileup_pct > 2.0:
        sev = "MODERATE_PILEUP_LOSS"
    else:
        sev = "NEGLIGIBLE_PILEUP_LOSS (LTC consistent)"

    return {
        "hardware_live_time": float(lt_hardware),
        "pulser_live_time": float(lt_pulser),
        "unmonitored_pileup_loss_pct": float(pileup_pct),
        "hardware_clock_bias_severity": sev
    }


def run_pulser_live_time_analysis(experiment, real_time_s, pulser_freq_Hz, recorded_counts,
                                  hardware_lt, physical_peaks):
    """
    Complete execution pipeline for pulser injection live-time analysis.
    """
    lt_info = calculate_pulser_live_time(real_time_s, pulser_freq_Hz, recorded_counts)
    corr_peaks = correct_peaks(physical_peaks, lt_info)
    bias_info = diagnose_hardware_clock_bias(lt_info["live_time_fraction"], hardware_lt)

    return {
        "experiment": experiment,
        "run_time_s": float(real_time_s),
        "live_time_metrics": lt_info,
        "hardware_clock_comparison": bias_info,
        "corrected_peaks": corr_peaks
    }


def format_text_report(res, title="In-Beam Pulser Injection Live-Time Loss Corrector"):
    exp = res["experiment"]
    lt = res["live_time_metrics"]
    hw = res["hardware_clock_comparison"]
    peaks = res["corrected_peaks"]

    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Experiment: {exp} | Run Time = {res['run_time_s']:.1f} s")
    lines.append("=" * 76)
    lines.append("Precision Pulser Live-Time Measurement:")
    lines.append(f"  Injected Pulser Events          : {lt['pulses_injected']:.0f} pulses")
    lines.append(f"  Recorded Pulser Peak Counts     : {lt['pulses_recorded']:.0f} pulses")
    lines.append(f"  Effective Live-Time Fraction LT : {lt['live_time_fraction']:.4f} +- {lt['sigma_live_time']:.5f} ({lt['live_time_fraction']*100.0:.2f}%)")
    lines.append(f"  Total Dead-Time Count Loss      : {lt['dead_time_pct']:.2f}% (Cascaded pileup + ADC + DAQ)")
    lines.append("-" * 76)
    lines.append("Hardware Gated Clock (LTC) vs Pulser Comparison:")
    lines.append(f"  Hardware Clock Live-Time (LTC)  : {hw['hardware_live_time']*100.0:.2f}% (Blind to analog pileup)")
    lines.append(f"  Unmonitored Preamp Pileup Loss  : {hw['unmonitored_pileup_loss_pct']:.2f}%")
    lines.append(f"  LTC Clock Bias Assessment       : {hw['hardware_clock_bias_severity']}")
    lines.append("-" * 76)
    lines.append("Absolute Physical Gamma Peak Area Corrections:")
    lines.append("  E_gamma (keV)   Observed Area       Corrected True Area   Multiplier   Rel Err (%)")
    for p in peaks:
        lines.append(f"    {p['energy_keV']:7.1f}        {p['measured_area']:8.1f} +- {p['sigma_measured_area']:4.1f}     {p['true_area']:9.1f} +- {p['sigma_true_area']:5.1f}     x{p['correction_multiplier']:.3f}       {p['relative_error_pct']:4.2f}%")
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="In-Beam Pulser Injection Live-Time Loss Corrector."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load experimental preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        exp = p["experiment"]
        t_real = p["real_time_s"]
        f_p = p["pulser_frequency_Hz"]
        n_rec = p["pulser_recorded_counts"]
        hw_lt = p["hardware_clock_live_time"]
        peaks = p["physical_peaks"]
        title = f"Preset: {args.preset} ({p['description']})"
    else:
        return parser.print_help()

    res = run_pulser_live_time_analysis(
        experiment=exp,
        real_time_s=t_real,
        pulser_freq_Hz=f_p,
        recorded_counts=n_rec,
        hardware_lt=hw_lt,
        physical_peaks=peaks
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
