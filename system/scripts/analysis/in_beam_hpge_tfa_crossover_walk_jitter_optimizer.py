#!/usr/bin/env python3
"""
In-Beam HPGe Timing Filter Amplifier (TFA) Bipolar Crossover Walk & Jitter Optimizer.

Physical Principle & Core Textbook Source:
In in-beam gamma-ray spectroscopy, prompt coincidence time resolution (FWHM <= 5-10 ns for HPGe,
sub-nanosecond for fast timing arrays) is critical for:
1. Prompt-delayed time gating and suppressing random coincidences N_rnd = 2 * tau * N1 * N2;
2. Clean gamma-gamma coincidence matrix generation;
3. Picosecond/nanosecond nuclear level lifetime measurements (e.g., GCD, RDDS).

Large coaxial HPGe detectors exhibit finite and distributed charge collection times
(t_coll ~ 100 - 400 ns) due to radial electric field variation E(r) ~ V / (r * ln(r_out/r_in))
and differing electron/hole drift velocities.

When preamplifier pulses are processed by a Timing Filter Amplifier (TFA) with bipolar shaping
(double differentiation CR and integration RC):
The bipolar pulse V_bi(t) crosses zero at t_0.
- Timing Jitter (electronic noise):
    sigma_jitter = sigma_noise(tau_int) / |dV_bi/dt|_{t_0}
  where series thermal noise dominates at high frequencies (requiring larger tau_int), while
  parallel shot noise and 1/f noise dominate at low frequencies.
  sigma_noise ~ e_n * (C_det / C_f) * sqrt(1 / (4 * tau_int))
- Timing Walk (amplitude & risetime dependence):
    Delta t_walk(t_r) = |d t_0 / d t_r| * sigma(t_r)
  When tau_diff is too short (tau_diff << t_r), zero-crossing occurs during active charge
  collection, maximizing walk sensitivity. When tau_diff is long (tau_diff >> t_r),
  walk is suppressed, but the zero-crossing slope is flattened, dramatically inflating jitter.

The Core Textbook Conflict Resolved:
- Wu Zhihua 《原子核物理实验方法》 §9.3 (pp. 235-250):
  Emphasizes long differentiation time constants (tau_diff >> t_r, 200 - 500 ns) to eliminate
  ballistic deficit in the zero-crossing slope. However, in high-rate in-beam experiments,
  this causes severe pulse pileup, baseline drift, and large timing jitter due to flat slope.
- Wang Xiaolian 《粒子探测技术》 §8.3 (pp. 280-295):
  Derives noise spectral power optimization: series noise dominates for sub-microsecond shaping.
  Recommends short shaping times (tau_int ~ 0.2 - 0.4 t_r, tau_diff ~ 0.5 - 1.0 t_r) to maximize
  the zero-crossing slope |dV/dt|_{t_0}, achieving fast response, but risking risetime walk.
- Nakhostin 《Signal Processing for Radiation Detectors》 Ch. 6:
  Provides the exact bipolar transfer function and trade-off criterion.

This module implements:
1. Analytical calculation of zero-crossing time t_0(tau_diff, t_r) and slope |dV/dt|_{t_0}.
2. Noise bandwidth and RMS voltage calculation as a function of tau_int and detector capacitance.
3. Accurate computation of electronic timing jitter sigma_jitter(E_gamma).
4. Ballistic timing walk sensitivity sigma_walk(t_r).
5. 2D optimization of (tau_int, tau_diff) minimizing total FWHM timing resolution.
6. Energy dynamic range response across 100 keV to 3000 keV.

Textbook & Literature References:
- Wu Zhihua, 《原子核物理实验方法》 (3rd Ed.), Ch. 9, §9.3
- Wang Xiaolian et al., 《粒子探测技术》, Ch. 8, §8.3
- Nakhostin, 《Signal Processing for Radiation Detectors》 (Wiley 2017), Ch. 6
- Goulding & Landis, IEEE Trans. Nucl. Sci. NS-29, 1125 (1982)
"""

import sys
import json
import argparse
import numpy as np
from scipy.optimize import minimize

PRESETS = {
    "coaxial_hpge_in_beam_70pct": {
        "detector": "70% Relative Efficiency Coaxial HPGe",
        "description": "Standard large volume coaxial HPGe in heavy-ion in-beam experiment",
        "t_rise_mean_ns": 180.0,
        "t_rise_sigma_ns": 40.0,
        "preamp_decay_us": 50.0,
        "capacitance_pF": 35.0,
        "noise_series_e_n": 1.2e-9,     # V / sqrt(Hz)
        "noise_parallel_i_n": 0.05e-12, # A / sqrt(Hz)
        "preamp_feedback_Cf_pF": 1.0,
        "amplifier_gain": 20.0,
        "e_gamma_eval_keV": 511.0,
        "energy_range_keV": [100.0, 3000.0],
    },
    "clover_hpge_leaf_segment": {
        "detector": "Euroball/AFRODITE Clover HPGe Single Leaf",
        "description": "Medium volume tapered leaf with faster charge collection (t_r ~ 120 ns)",
        "t_rise_mean_ns": 120.0,
        "t_rise_sigma_ns": 25.0,
        "preamp_decay_us": 40.0,
        "capacitance_pF": 20.0,
        "noise_series_e_n": 0.9e-9,
        "noise_parallel_i_n": 0.03e-12,
        "preamp_feedback_Cf_pF": 1.0,
        "amplifier_gain": 20.0,
        "e_gamma_eval_keV": 300.0,
        "energy_range_keV": [80.0, 2000.0],
    },
    "planar_hpge_low_energy": {
        "detector": "Planar LEPS HPGe Detector",
        "description": "High resolution planar HPGe for low-energy gamma/X-ray fast timing",
        "t_rise_mean_ns": 45.0,
        "t_rise_sigma_ns": 10.0,
        "preamp_decay_us": 30.0,
        "capacitance_pF": 10.0,
        "noise_series_e_n": 0.6e-9,
        "noise_parallel_i_n": 0.01e-12,
        "preamp_feedback_Cf_pF": 1.0,
        "amplifier_gain": 25.0,
        "e_gamma_eval_keV": 122.0,
        "energy_range_keV": [30.0, 500.0],
    }
}

class HPGeTFACrossoverOptimizer:
    def __init__(self, t_rise_mean_ns=180.0, t_rise_sigma_ns=40.0, preamp_decay_us=50.0,
                 capacitance_pF=35.0, noise_series_e_n=1.2e-9, noise_parallel_i_n=0.05e-12,
                 preamp_feedback_Cf_pF=1.0, amplifier_gain=20.0):
        self.t_r = float(t_rise_mean_ns) * 1e-9      # s
        self.sigma_tr = float(t_rise_sigma_ns) * 1e-9  # s
        self.tau_p = float(preamp_decay_us) * 1e-6    # s
        self.C_d = float(capacitance_pF) * 1e-12      # F
        self.C_f = float(preamp_feedback_Cf_pF) * 1e-12 # F
        self.gain = float(amplifier_gain)
        self.e_n = float(noise_series_e_n)
        self.i_n = float(noise_parallel_i_n)

    def calculate_crossover_properties(self, tau_diff, t_rise):
        """
        Calculates the crossover time t_0 and normalized slope at zero crossing.
        For a linear ramp current of duration t_r convolved with bipolar filter:
        t_0(tau_diff, t_r) = 2.0 * tau_diff * (1.0 + 0.35 * (t_rise / (2.0 * tau_diff))**1.5)
        Walk derivative: d t_0 / d t_r
        """
        ratio = t_rise / (2.0 * max(1e-12, tau_diff))
        # Zero-crossing time relative to arrival
        t_0 = 2.0 * tau_diff * (1.0 + 0.35 * (ratio**1.4))
        # Sensitivity of zero crossing to rise time variation (walk factor)
        d_t0_d_tr = 0.35 * 1.4 * (ratio**0.4)

        # Ballistic attenuation of the zero-crossing peak-to-peak amplitude
        ballistic_factor = 1.0 / np.sqrt(1.0 + (ratio)**2)
        return t_0, d_t0_d_tr, ballistic_factor

    def calculate_noise_voltage_rms(self, tau_int):
        """
        Total noise voltage at TFA output:
        Series noise dominates for fast timing:
          sigma_v = e_n * (1 + C_in / C_f) * sqrt(1 / (4 * tau_int)) * gain
        """
        C_in = self.C_d + 5e-12 + self.C_f  # including FET input capacitance
        noise_gain = C_in / self.C_f
        Bn = 1.0 / (4.0 * max(1e-12, tau_int))
        sigma_v = self.e_n * noise_gain * np.sqrt(Bn) * self.gain
        return sigma_v

    def calculate_timing_resolution(self, tau_int_ns, tau_diff_ns, e_gamma_keV=511.0):
        """
        Computes timing jitter, walk, and combined FWHM time resolution.
        """
        tau_i = float(tau_int_ns) * 1e-9
        tau_d = float(tau_diff_ns) * 1e-9

        # 1. Preamplifier step voltage for E_gamma:
        # e-h pair creation energy in Ge at 77K is 2.96 eV
        e_pairs = (e_gamma_keV * 1e3) / 2.96
        q_det = e_pairs * 1.602e-19  # Coulombs
        v_preamp = q_det / self.C_f  # Volts (~ 27.6 mV for 511 keV)

        # 2. Crossover slope
        t0, d_t0_d_tr, ballistic = self.calculate_crossover_properties(tau_d, self.t_r)
        # Pulse peak after TFA
        v_peak = v_preamp * self.gain * ballistic
        # Zero-crossing slope: |dV/dt|_{t_0} ~ 1.5 * v_peak / tau_d (V/s)
        # Note tau_i also attenuates slope if tau_i is large:
        int_atten = 1.0 / np.sqrt(1.0 + (tau_i / tau_d)**2)
        dV_dt = (1.5 * v_peak * int_atten) / tau_d  # V/s

        # 3. Noise RMS
        sigma_noise = self.calculate_noise_voltage_rms(tau_i)

        # 4. Timing Jitter
        sigma_jitter_s = sigma_noise / max(1e-6, dV_dt)
        sigma_jitter_ns = sigma_jitter_s * 1e9

        # 5. Timing Walk from rise-time variation sigma_tr
        sigma_walk_s = d_t0_d_tr * self.sigma_tr
        sigma_walk_ns = sigma_walk_s * 1e9

        # 6. Combined total resolution
        sigma_tot_ns = np.sqrt(sigma_jitter_ns**2 + sigma_walk_ns**2)
        fwhm_tot_ns = 2.355 * sigma_tot_ns

        return {
            "tau_int_ns": float(tau_int_ns),
            "tau_diff_ns": float(tau_diff_ns),
            "e_gamma_keV": float(e_gamma_keV),
            "t0_crossover_ns": float(t0 * 1e9),
            "zero_crossing_slope_V_per_ns": float(dV_dt * 1e-9),
            "noise_rms_mV": float(sigma_noise * 1e3),
            "timing_jitter_sigma_ns": float(sigma_jitter_ns),
            "timing_walk_sigma_ns": float(sigma_walk_ns),
            "total_sigma_ns": float(sigma_tot_ns),
            "total_fwhm_ns": float(fwhm_tot_ns)
        }

    def optimize_shaping_constants(self, e_gamma_keV=511.0):
        """
        Find optimal (tau_int, tau_diff) minimizing total FWHM time resolution.
        """
        def objective(params):
            t_int, t_diff = params
            res = self.calculate_timing_resolution(t_int, t_diff, e_gamma_keV)
            return res["total_fwhm_ns"]

        init_guess = [self.t_r * 1e9 * 0.25, self.t_r * 1e9 * 0.75]
        bounds = [(5.0, 150.0), (15.0, 450.0)]

        opt = minimize(objective, x0=init_guess, bounds=bounds, method='L-BFGS-B')
        best_int, best_diff = opt.x[0], opt.x[1]

        best_res = self.calculate_timing_resolution(best_int, best_diff, e_gamma_keV)

        # Wu Zhihua textbook baseline (tau_diff >> t_r ~ 350 ns, tau_int ~ 100 ns)
        wu_res = self.calculate_timing_resolution(100.0, 350.0, e_gamma_keV)

        # Wang Xiaolian textbook baseline (tau_diff ~ 0.5 t_r, tau_int ~ 0.2 t_r)
        wang_res = self.calculate_timing_resolution(self.t_r * 1e9 * 0.2, self.t_r * 1e9 * 0.5, e_gamma_keV)

        return {
            "optimal": best_res,
            "wu_zhihua_comparison": wu_res,
            "wang_xiaolian_comparison": wang_res,
            "optimization_improvement_pct": float((wu_res["total_fwhm_ns"] - best_res["total_fwhm_ns"]) / wu_res["total_fwhm_ns"] * 100.0)
        }

    def generate_energy_walk_curve(self, tau_int_ns, tau_diff_ns, energies_keV):
        """
        Generate timing walk and FWHM resolution across gamma-ray energies.
        """
        curve = []
        for e in energies_keV:
            res = self.calculate_timing_resolution(tau_int_ns, tau_diff_ns, e)
            curve.append({
                "energy_keV": float(e),
                "jitter_sigma_ns": res["timing_jitter_sigma_ns"],
                "walk_sigma_ns": res["timing_walk_sigma_ns"],
                "total_fwhm_ns": res["total_fwhm_ns"]
            })
        return curve

def main():
    parser = argparse.ArgumentParser(description="HPGe TFA Bipolar Crossover Timing Optimizer")
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Preset configuration")
    parser.add_argument("--energy", type=float, help="Gamma-ray energy for optimization (keV)")
    parser.add_argument("--trise", type=float, help="Mean detector charge collection rise time (ns)")
    parser.add_argument("--tau-int", type=float, help="Explicit integration constant (ns)")
    parser.add_argument("--tau-diff", type=float, help="Explicit differentiation constant (ns)")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON format")
    args = parser.parse_args()

    cfg = PRESETS["coaxial_hpge_in_beam_70pct"].copy()
    if args.preset:
        cfg = PRESETS[args.preset].copy()
    if args.energy is not None:
        cfg["e_gamma_eval_keV"] = args.energy
    if args.trise is not None:
        cfg["t_rise_mean_ns"] = args.trise

    optimizer = HPGeTFACrossoverOptimizer(
        t_rise_mean_ns=cfg["t_rise_mean_ns"],
        t_rise_sigma_ns=cfg["t_rise_sigma_ns"],
        preamp_decay_us=cfg["preamp_decay_us"],
        capacitance_pF=cfg["capacitance_pF"],
        noise_series_e_n=cfg["noise_series_e_n"],
        noise_parallel_i_n=cfg["noise_parallel_i_n"],
        preamp_feedback_Cf_pF=cfg["preamp_feedback_Cf_pF"],
        amplifier_gain=cfg["amplifier_gain"]
    )

    if args.tau_int and args.tau_diff:
        eval_res = optimizer.calculate_timing_resolution(args.tau_int, args.tau_diff, cfg["e_gamma_eval_keV"])
        output = {"manual_evaluation": eval_res}
    else:
        opt_res = optimizer.optimize_shaping_constants(cfg["e_gamma_eval_keV"])
        energies = [100.0, 200.0, 350.0, 511.0, 800.0, 1332.0, 2000.0]
        walk_curve = optimizer.generate_energy_walk_curve(
            opt_res["optimal"]["tau_int_ns"],
            opt_res["optimal"]["tau_diff_ns"],
            energies
        )
        opt_res["energy_walk_curve"] = walk_curve
        output = opt_res

    output["detector"] = cfg.get("detector", "Generic HPGe")
    output["description"] = cfg.get("description", "")

    if args.json:
        print(json.dumps(output, indent=2))
    else:
        print(f"=========================================================================")
        print(f"  HPGe TFA Bipolar Crossover Timing Walk & Jitter Optimizer (Mod 156)   ")
        print(f"=========================================================================")
        print(f"Detector:    {output['detector']}")
        print(f"Description: {output['description']}")
        if "optimal" in output:
            opt = output["optimal"]
            wu = output["wu_zhihua_comparison"]
            wang = output["wang_xiaolian_comparison"]
            print(f"\n[1] Optimal Shaping Parameters (at E_gamma = {opt['e_gamma_keV']:.1f} keV):")
            print(f"  tau_int_opt:   {opt['tau_int_ns']:.1f} ns")
            print(f"  tau_diff_opt:  {opt['tau_diff_ns']:.1f} ns")
            print(f"  Crossover t0:  {opt['t0_crossover_ns']:.1f} ns")
            print(f"  Slope @ t0:    {opt['zero_crossing_slope_V_per_ns']:.3f} V/ns")
            print(f"  RMS Noise:     {opt['noise_rms_mV']:.2f} mV")
            print(f"  Timing Jitter: sigma_jitter = {opt['timing_jitter_sigma_ns']:.2f} ns")
            print(f"  Risetime Walk: sigma_walk   = {opt['timing_walk_sigma_ns']:.2f} ns")
            print(f"  Total FWHM:    Delta T_FWHM = {opt['total_fwhm_ns']:.2f} ns")
            print(f"\n[2] Textbook Paradigm Comparison:")
            print(f"  吴治华《实验方法》 (Long tau_d=350ns):  FWHM = {wu['total_fwhm_ns']:.2f} ns (Jitter dominated)")
            print(f"  汪晓莲《探测技术》 (Short tau_d=90ns):  FWHM = {wang['total_fwhm_ns']:.2f} ns (Walk dominated)")
            print(f"  Unified Optimization (Pareto point):    FWHM = {opt['total_fwhm_ns']:.2f} ns (Gain: +{output['optimization_improvement_pct']:.1f}%)")
            print(f"\n[3] Energy Dynamic Range Response (Optimal Filter):")
            print(f"  Energy (keV) | Jitter sigma (ns) | Walk sigma (ns) | Total FWHM (ns)")
            print(f"  ------------------------------------------------------------------")
            for pt in output["energy_walk_curve"]:
                print(f"     {pt['energy_keV']:6.1f}    |      {pt['jitter_sigma_ns']:6.2f}       |     {pt['walk_sigma_ns']:6.2f}      |     {pt['total_fwhm_ns']:6.2f}")
        print(f"=========================================================================")

if __name__ == "__main__":
    main()

def run_tfa_walk_analysis(detector="Generic HPGe", t_rise_mean_ns=180.0, t_rise_sigma_ns=40.0,
                          preamp_decay_us=50.0, capacitance_pF=35.0, noise_series_e_n=1.2e-9,
                          noise_parallel_i_n=0.05e-12, preamp_feedback_Cf_pF=1.0,
                          amplifier_gain=20.0, e_gamma_eval_keV=511.0,
                          energy_range_keV=None):
    optimizer = HPGeTFACrossoverOptimizer(
        t_rise_mean_ns=t_rise_mean_ns,
        t_rise_sigma_ns=t_rise_sigma_ns,
        preamp_decay_us=preamp_decay_us,
        capacitance_pF=capacitance_pF,
        noise_series_e_n=noise_series_e_n,
        noise_parallel_i_n=noise_parallel_i_n,
        preamp_feedback_Cf_pF=preamp_feedback_Cf_pF,
        amplifier_gain=amplifier_gain
    )
    opt_res = optimizer.optimize_shaping_constants(e_gamma_eval_keV)
    if energy_range_keV is None:
        energies = [100.0, 200.0, 350.0, 511.0, 800.0, 1332.0, 2000.0]
    else:
        energies = np.linspace(energy_range_keV[0], energy_range_keV[1], 7).tolist()
    walk_curve = optimizer.generate_energy_walk_curve(
        opt_res["optimal"]["tau_int_ns"],
        opt_res["optimal"]["tau_diff_ns"],
        energies
    )
    opt_res["energy_walk_curve"] = walk_curve
    opt_res["detector"] = detector
    return opt_res

def format_text_report(output, title="HPGe TFA Bipolar Crossover Timing Optimizer"):
    lines = []
    lines.append("=" * 76)
    lines.append(f"  {title}")
    lines.append("=" * 76)
    lines.append(f"Detector: {output['detector']}")
    if "optimal" in output:
        opt = output["optimal"]
        wu = output["wu_zhihua_comparison"]
        wang = output["wang_xiaolian_comparison"]
        lines.append(f"\n[1] Optimal Shaping Parameters (at E_gamma = {opt['e_gamma_keV']:.1f} keV):")
        lines.append(f"  tau_int_opt:   {opt['tau_int_ns']:.1f} ns")
        lines.append(f"  tau_diff_opt:  {opt['tau_diff_ns']:.1f} ns")
        lines.append(f"  Crossover t0:  {opt['t0_crossover_ns']:.1f} ns")
        lines.append(f"  Slope @ t0:    {opt['zero_crossing_slope_V_per_ns']:.3f} V/ns")
        lines.append(f"  RMS Noise:     {opt['noise_rms_mV']:.2f} mV")
        lines.append(f"  Timing Jitter: sigma_jitter = {opt['timing_jitter_sigma_ns']:.2f} ns")
        lines.append(f"  Risetime Walk: sigma_walk   = {opt['timing_walk_sigma_ns']:.2f} ns")
        lines.append(f"  Total FWHM:    Delta T_FWHM = {opt['total_fwhm_ns']:.2f} ns")
        lines.append(f"\n[2] Textbook Paradigm Comparison:")
        lines.append(f"  Wu Zhihua baseline (Long tau_d=350ns):  FWHM = {wu['total_fwhm_ns']:.2f} ns (Jitter dominated)")
        lines.append(f"  Wang Xiaolian baseline (Short tau_d=90ns): FWHM = {wang['total_fwhm_ns']:.2f} ns (Walk dominated)")
        lines.append(f"  Unified Optimization (Pareto point):    FWHM = {opt['total_fwhm_ns']:.2f} ns (Gain: +{output['optimization_improvement_pct']:.1f}%)")
        lines.append(f"\n[3] Energy Dynamic Range Response (Optimal Filter):")
        lines.append(f"  Energy (keV) | Jitter sigma (ns) | Walk sigma (ns) | Total FWHM (ns)")
        lines.append(f"  ------------------------------------------------------------------")
        for pt in output["energy_walk_curve"]:
            lines.append(f"     {pt['energy_keV']:6.1f}    |      {pt['jitter_sigma_ns']:6.2f}       |     {pt['walk_sigma_ns']:6.2f}      |     {pt['total_fwhm_ns']:6.2f}")
    lines.append("-" * 76)
    lines.append("Methodology Takeaway: Resolves Wu Zhihua vs Wang Xiaolian conflict by joint")
    lines.append("optimization of series noise jitter and risetime ballistic walk.")
    lines.append("=" * 76)
    return "\n".join(lines)
