#!/usr/bin/env python3
"""
in_beam_prompt_delayed_time_gating_random_subtractor.py
========================================================
In-Beam Multi-Detector Array Prompt-Delayed Coincidence Time Gating,
Accidental (Random) Background Difference Subtraction & Isomer Isolation Engine.

Physics Formulation:
--------------------
1. Time-Difference Coincidence Spectrum in Pulsed Beam Experiments:
   Based on 吴治华《原子核物理实验方法》第 9 章 §9.4 (pp. 245–255), 第 10 章 §10.2 (pp. 250–260),
   汪晓莲《粒子探测技术》第 8 章 §8.3, and 朱永生《实验物理中的概率和统计》第 4 章:
   In accelerator-based in-beam gamma spectroscopy, the ion beam exhibits a periodic micro-structure
   (RF period T_RF ~ 40 - 100 ns).
   The relative time-difference histogram between two detectors Delta t = t_1 - t_2 contains:
     a. Prompt Coincidence Peak: Genuine cascade gamma-rays emitted from short-lived states
        (tau < 1 - 2 ns), with instrumental Gaussian width FWHM ~ 5 - 12 ns;
     b. Delayed Isomer Tail: Exponential decay tail from nanosecond-to-microsecond isomeric states;
     c. Accidental (Random) Coincidence Floor: Events from uncorrelated nuclear reactions produced
        by separate beam bunches, forming a periodic flat baseline spanning each RF bucket.

2. Time Gating & Normalized Difference Subtraction:
   Let W_prompt = [t_p1, t_p2] be the prompt coincidence time gate of width Delta T_prompt.
   Let W_rand = [t_r1, t_r2] be one or more pure random background time gates of total width Delta T_rand.
   The normalization scaling factor is:
     f_norm = Delta T_prompt / Delta T_rand
   The net genuine prompt coincidence spectrum is:
     S_true(E) = S_prompt(E) - f_norm * S_rand(E)
   The variance in each channel is strictly propagated from Poisson statistics:
     sigma^2_true(E) = S_prompt(E) + f_norm^2 * S_rand(E).

3. Delayed Isomer Gating:
   By setting a delayed time gate W_delayed = [t_prompt_end + 3*sigma_t, t_delayed_end], the prompt
   in-beam flash (accounting for > 95% of total spectrum counts) is completely rejected.
   Subtracting the normalized random window leaves purely the delayed gamma transitions de-exciting
   the isomer, enhancing the peak-to-background ratio of isomeric lines by up to 20 - 50 times!
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "in_beam_134Ce_prompt_random_subtraction": {
        "description": "134Ce in-beam prompt-random coincidence subtraction (T_RF = 50 ns, 409 & 638 keV)",
        "nucleus": "134Ce",
        "beam_rf_period_ns": 50.0,
        "prompt_window_ns": {"t_start": -4.0, "t_stop": 8.0},
        "random_window_ns": {"t_start": 25.0, "t_stop": 75.0},
        "peaks": [
            {"energy_keV": 409.0, "prompt_counts": 14200, "random_counts": 6400},
            {"energy_keV": 638.0, "prompt_counts": 11800, "random_counts": 5100},
            {"energy_keV": 814.0, "prompt_counts": 5400, "random_counts": 2900}
        ]
    },
    "181Ta_nanosecond_isomer_delayed_gating": {
        "description": "181Ta 6.05 ns isomer delayed gating isolating 133 & 482 keV depopulating lines",
        "nucleus": "181Ta",
        "beam_rf_period_ns": 80.0,
        "prompt_window_ns": {"t_start": -3.0, "t_stop": 6.0},
        "random_window_ns": {"t_start": 50.0, "t_stop": 110.0},
        "delayed_window_ns": {"t_start": 10.0, "t_stop": 45.0},
        "peaks": [
            {"energy_keV": 133.0, "prompt_counts": 4500, "delayed_counts": 8800, "random_counts": 2400},
            {"energy_keV": 482.0, "prompt_counts": 3800, "delayed_counts": 7900, "random_counts": 2100},
            {"energy_keV": 346.0, "prompt_counts": 9200, "delayed_counts": 250, "random_counts": 1800}
        ]
    },
    "high_rate_random_dominated_benchmark": {
        "description": "High rate experiment where random coincidences dominate (P/R ~ 0.8)",
        "nucleus": "High-Rate-Test",
        "beam_rf_period_ns": 40.0,
        "prompt_window_ns": {"t_start": -5.0, "t_stop": 5.0},
        "random_window_ns": {"t_start": 15.0, "t_stop": 55.0},
        "peaks": [
            {"energy_keV": 511.0, "prompt_counts": 25000, "random_counts": 78000},
            {"energy_keV": 1000.0, "prompt_counts": 12000, "random_counts": 28000}
        ]
    }
}


def calculate_window_width(win_dict):
    """Calculates width of a time window in ns."""
    return float(win_dict["t_stop"] - win_dict["t_start"])


def perform_random_subtraction(peaks, prompt_win, rand_win):
    """
    Performs normalized random coincidence subtraction for prompt peaks.
    """
    dt_prompt = calculate_window_width(prompt_win)
    dt_rand = calculate_window_width(rand_win)
    f_norm = dt_prompt / max(1e-4, dt_rand)

    results = []
    for p in peaks:
        E = p["energy_keV"]
        N_p = float(p["prompt_counts"])
        N_r = float(p["random_counts"])

        N_net = N_p - f_norm * N_r
        var_net = N_p + (f_norm**2) * N_r
        sigma_net = math.sqrt(max(0.0, var_net))

        rel_err = (sigma_net / max(1.0, abs(N_net))) * 100.0 if N_net > 0 else 0.0
        significance_Z = N_net / max(1e-3, sigma_net) if N_net > 0 else 0.0
        pt_to_bkg = N_net / max(1.0, f_norm * N_r)

        results.append({
            "energy_keV": float(E),
            "prompt_raw_counts": N_p,
            "random_scaled_counts": float(f_norm * N_r),
            "net_true_counts": float(N_net),
            "sigma_net_counts": float(sigma_net),
            "relative_error_pct": float(rel_err),
            "significance_Z": float(significance_Z),
            "signal_to_random_ratio": float(pt_to_bkg)
        })

    return {
        "time_windows": {
            "prompt_width_ns": dt_prompt,
            "random_width_ns": dt_rand,
            "normalization_factor_f": float(f_norm)
        },
        "subtracted_peaks": results
    }


def perform_delayed_isomer_analysis(peaks, delayed_win, rand_win):
    """
    Performs normalized random subtraction for delayed isomer transitions.
    """
    dt_del = calculate_window_width(delayed_win)
    dt_rand = calculate_window_width(rand_win)
    f_del = dt_del / max(1e-4, dt_rand)

    results = []
    for p in peaks:
        E = p["energy_keV"]
        N_d = float(p.get("delayed_counts", 0.0))
        N_r = float(p["random_counts"])

        N_net_del = N_d - f_del * N_r
        var_del = N_d + (f_del**2) * N_r
        sigma_del = math.sqrt(max(0.0, var_del))

        is_isomer_line = bool(N_net_del > 500.0 and (N_net_del / max(1.0, sigma_del)) > 5.0)

        results.append({
            "energy_keV": float(E),
            "delayed_raw_counts": N_d,
            "random_scaled_counts": float(f_del * N_r),
            "net_delayed_counts": float(N_net_del),
            "sigma_delayed_counts": float(sigma_del),
            "is_isomeric_transition": is_isomer_line
        })

    return {
        "delayed_window_width_ns": dt_del,
        "delayed_normalization_factor": float(f_del),
        "delayed_peaks": results
    }


def run_prompt_delayed_analysis(peaks, prompt_win, rand_win, delayed_win=None, nucleus="Nucleus"):
    """
    Complete execution pipeline for prompt-delayed gating and random subtraction.
    """
    prompt_res = perform_random_subtraction(peaks, prompt_win, rand_win)
    delayed_res = None
    if delayed_win is not None:
        delayed_res = perform_delayed_isomer_analysis(peaks, delayed_win, rand_win)

    return {
        "nucleus": nucleus,
        "prompt_analysis": prompt_res,
        "delayed_analysis": delayed_res
    }


def format_text_report(res, title="In-Beam Prompt-Delayed Gating & Random Subtractor"):
    nuc = res["nucleus"]
    pr = res["prompt_analysis"]
    tw = pr["time_windows"]
    peaks = pr["subtracted_peaks"]

    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Nucleus: {nuc} | Prompt Window = {tw['prompt_width_ns']:.1f} ns | Random Window = {tw['random_width_ns']:.1f} ns (f = {tw['normalization_factor_f']:.4f})")
    lines.append("=" * 76)
    lines.append("Prompt-Gated Random Background Subtraction Results:")
    lines.append("  E_gamma (keV)   Prompt Raw   Random Scaled     Net True Counts       Rel Err (%)    S/R Ratio")
    for p in peaks:
        lines.append(f"    {p['energy_keV']:7.1f}        {p['prompt_raw_counts']:8.0f}       {p['random_scaled_counts']:8.1f}     {p['net_true_counts']:8.1f} +- {p['sigma_net_counts']:5.1f}     {p['relative_error_pct']:5.2f}%       {p['signal_to_random_ratio']:5.2f}")
    lines.append("-" * 76)

    if res["delayed_analysis"] is not None:
        da = res["delayed_analysis"]
        lines.append(f"Delayed Isomer Gating Analysis (Delayed Window = {da['delayed_window_width_ns']:.1f} ns, f = {da['delayed_normalization_factor']:.4f}):")
        lines.append("  E_gamma (keV)   Delayed Raw   Random Scaled   Net Delayed Counts   Isomer Assignment")
        for dp in da["delayed_peaks"]:
            tag = "YES (Isomer Line)" if dp["is_isomeric_transition"] else "NO (Prompt / Continuum)"
            lines.append(f"    {dp['energy_keV']:7.1f}        {dp['delayed_raw_counts']:8.0f}       {dp['random_scaled_counts']:8.1f}    {dp['net_delayed_counts']:8.1f} +- {dp['sigma_delayed_counts']:5.1f}   {tag}")
        lines.append("-" * 76)

    lines.append("Methodology Note: Accidental background subtraction eliminates systematic false peaks")
    lines.append("and restores true branching intensity balance across pulsed-beam RF cycles.")
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="In-Beam Prompt-Delayed Gating & Random Background Subtractor."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load experimental preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        nucleus = p["nucleus"]
        p_win = p["prompt_window_ns"]
        r_win = p["random_window_ns"]
        d_win = p.get("delayed_window_ns", None)
        peaks = p["peaks"]
        title = f"Preset: {args.preset} ({p['description']})"
    else:
        return parser.print_help()

    res = run_prompt_delayed_analysis(
        peaks=peaks,
        prompt_win=p_win,
        rand_win=r_win,
        delayed_win=d_win,
        nucleus=nucleus
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
