#!/usr/bin/env python3
"""
digital_psd_charge_comparison_optimizer.py
==========================================
Digital Pulse Shape Discrimination (PSD), Dual-Gate Charge Comparison Method (CCM),
Optimal Gate Width Optimization & Fast-Neutron/Gamma Figure-of-Merit (FOM) Engine.

Physics Formulation:
--------------------
1. Organic Scintillation Double Exponential Decay:
   Based on Nakhostin《辐射探测器信号处理》第 4 章 (pp. 110–145), 汪晓莲等《粒子探测技术》第 4, 8 章,
   and G. F. Knoll (Radiation Detection and Measurement, 4th ed., Ch. 8, 15):
   In organic scintillators (e.g. BC-501A, EJ-301, Stilbene), the light emission pulse v(t)
   is characterized by a fast rise time tau_rise and two fluorescence decay components:
     v(t) = V0 * [ 1.0 - exp(-t / tau_rise) ] * [ (1 - f_slow) * exp(-t / tau_fast) + f_slow * exp(-t / tau_slow) ]
   where:
     tau_rise ~ 1.0 - 2.0 ns (finite PMT and scintillation transit response)
     tau_fast ~ 3.0 - 5.0 ns (direct singlet de-excitation)
     tau_slow ~ 200 - 300 ns (delayed triplet-triplet annihilation de-excitation)

2. dE/dx Ionization Density & Slow Component Fraction:
   - Gamma-ray interactions (Compton electrons, low dE/dx): f_slow ~ 0.08 - 0.15;
   - Fast-neutron interactions (recoil protons, high dE/dx): f_slow ~ 0.28 - 0.38.
   The higher ionization density of recoil protons strongly favors delayed triplet states,
   producing significantly higher tail charge.

3. Digital Charge Comparison Method (CCM):
   For digitized pulse samples v_i at sampling period dt:
     Total charge: Q_long = sum_{i=0}^{N_long} v_i * dt  (e.g. T_long ~ 300 - 500 ns)
     Short charge: Q_short = sum_{i=0}^{N_short} v_i * dt (e.g. T_short ~ 15 - 40 ns)
     Tail charge:  Q_tail = Q_long - Q_short
   Definition of PSD parameter:
     PSD = Q_tail / Q_long = 1.0 - (Q_short / Q_long)

4. Optimal Short-Gate Width Search:
   The optimal short-gate integration time T_short is determined by maximizing
   the peak separation distance between the neutron and gamma PSD distributions:
     Delta_PSD(T_short) = PSD_n(T_short) - PSD_g(T_short)

5. Figure of Merit (FOM) & Energy Threshold Systematics:
   The separation quality is evaluated by the Figure of Merit:
     FOM = |mu_n - mu_g| / ( FWHM_n + FWHM_g ) = |mu_n - mu_g| / [ 2.355 * (sigma_n + sigma_g) ]
   - FOM < 1.0: Poor discrimination, severe peak overlap and contamination;
   - FOM >= 1.27: Standard 3-sigma separation (neutron contamination <= 0.3%);
   - FOM >= 1.50: Excellent, high-purity clean separation.
   Energy dependence follows photoelectron Poisson statistics:
     sigma(E_ee) = sigma_0 * sqrt( E_0 / E_ee )
     FOM(E_ee) = FOM_0 * sqrt( E_ee / E_0 ).
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "EJ301_fast_neutron_psd": {
        "description": "EJ-301 / BC-501A liquid scintillator benchmark (Knoll / Nakhostin 2017)",
        "scintillator": "EJ-301",
        "tau_rise_ns": 1.5,
        "tau_fast_ns": 3.2,
        "tau_slow_ns": 270.0,
        "f_slow_gamma": 0.12,
        "f_slow_neutron": 0.32,
        "T_long_ns": 350.0,
        "sampling_dt_ns": 0.5,
        "base_energy_keVee": 500.0,
        "base_fom": 1.45
    },
    "Stilbene_crystal_psd": {
        "description": "Organic Stilbene crystal (high light yield, sharp PSD separation)",
        "scintillator": "Stilbene",
        "tau_rise_ns": 1.2,
        "tau_fast_ns": 4.5,
        "tau_slow_ns": 220.0,
        "f_slow_gamma": 0.08,
        "f_slow_neutron": 0.35,
        "T_long_ns": 300.0,
        "sampling_dt_ns": 0.5,
        "base_energy_keVee": 500.0,
        "base_fom": 1.75
    },
    "Low_energy_threshold_psd": {
        "description": "EJ-301 at low light output (100 keVee threshold, Poisson broadened)",
        "scintillator": "EJ-301 (Low-E)",
        "tau_rise_ns": 1.5,
        "tau_fast_ns": 3.2,
        "tau_slow_ns": 270.0,
        "f_slow_gamma": 0.12,
        "f_slow_neutron": 0.32,
        "T_long_ns": 350.0,
        "sampling_dt_ns": 0.5,
        "base_energy_keVee": 100.0,
        "base_fom": 0.95
    }
}


def synthesize_scintillation_pulse(t_arr_ns, tau_rise, tau_fast, tau_slow, f_slow, amplitude=1.0):
    """
    Generates the analytical double-exponential scintillation pulse with finite rise time.
    """
    rise = 1.0 - np.exp(-t_arr_ns / max(1e-4, tau_rise))
    decay = (1.0 - f_slow) * np.exp(-t_arr_ns / max(1e-4, tau_fast)) + f_slow * np.exp(-t_arr_ns / max(1e-4, tau_slow))
    pulse = amplitude * rise * decay
    return np.maximum(0.0, pulse)


def compute_ccm_psd(pulse, dt_ns, t_short_ns, t_long_ns):
    """
    Computes Q_short, Q_long, Q_tail and PSD = Q_tail / Q_long.
    """
    idx_s = max(1, min(len(pulse), int(t_short_ns / dt_ns)))
    idx_l = max(idx_s + 1, min(len(pulse), int(t_long_ns / dt_ns)))

    q_short = float(np.sum(pulse[:idx_s]) * dt_ns)
    q_long = float(np.sum(pulse[:idx_l]) * dt_ns)
    q_tail = float(max(0.0, q_long - q_short))

    psd = (q_tail / q_long) if q_long > 0 else 0.0
    return {
        "Q_short": q_short,
        "Q_long": q_long,
        "Q_tail": q_tail,
        "PSD": float(psd)
    }


def optimize_gate_widths(tau_rise_ns, tau_fast_ns, tau_slow_ns, f_slow_g, f_slow_n,
                         dt_ns=0.5, t_long_ns=350.0, t_short_min=5.0, t_short_max=60.0):
    """
    Scans short-gate integration time T_short to maximize PSD separation distance.
    """
    t_arr = np.arange(0.0, max(500.0, t_long_ns + 50.0), dt_ns)
    p_g = synthesize_scintillation_pulse(t_arr, tau_rise_ns, tau_fast_ns, tau_slow_ns, f_slow_g)
    p_n = synthesize_scintillation_pulse(t_arr, tau_rise_ns, tau_fast_ns, tau_slow_ns, f_slow_n)

    t_short_scan = np.linspace(t_short_min, t_short_max, 56)
    scan_results = []

    for ts in t_short_scan:
        res_g = compute_ccm_psd(p_g, dt_ns, ts, t_long_ns)
        res_n = compute_ccm_psd(p_n, dt_ns, ts, t_long_ns)
        delta_psd = res_n["PSD"] - res_g["PSD"]
        scan_results.append({
            "T_short_ns": float(ts),
            "PSD_gamma": float(res_g["PSD"]),
            "PSD_neutron": float(res_n["PSD"]),
            "delta_PSD": float(delta_psd)
        })

    # Find maximum separation
    best_entry = max(scan_results, key=lambda x: x["delta_PSD"])
    return {
        "optimal_T_short_ns": best_entry["T_short_ns"],
        "max_delta_PSD": best_entry["delta_PSD"],
        "optimal_PSD_gamma": best_entry["PSD_gamma"],
        "optimal_PSD_neutron": best_entry["PSD_neutron"],
        "scan_profile": scan_results
    }


def evaluate_fom_energy_dependence(base_energy_keVee, base_fom, energy_list_keVee):
    """
    Evaluates the degradation of FOM at lower energies according to Poisson photoelectron statistics:
      FOM(E) = base_fom * sqrt(E / base_energy).
    """
    res = []
    for e in energy_list_keVee:
        fom_e = base_fom * math.sqrt(max(1.0, e) / max(1.0, base_energy_keVee))
        # Quality classification
        if fom_e >= 1.50:
            qual = "excellent_pure_separation"
        elif fom_e >= 1.27:
            qual = "good_3sigma_standard"
        elif fom_e >= 1.00:
            qual = "moderate_partial_leakage"
        else:
            qual = "poor_severe_overlap"

        res.append({
            "energy_keVee": float(e),
            "FOM": float(fom_e),
            "separation_quality": qual
        })
    return res


def run_psd_analysis(scintillator, tau_rise_ns, tau_fast_ns, tau_slow_ns, f_slow_g, f_slow_n,
                     T_long_ns=350.0, dt_ns=0.5, base_energy_keVee=500.0, base_fom=1.45):
    """
    Full PSD pipeline.
    """
    opt_res = optimize_gate_widths(
        tau_rise_ns=tau_rise_ns,
        tau_fast_ns=tau_fast_ns,
        tau_slow_ns=tau_slow_ns,
        f_slow_g=f_slow_g,
        f_slow_n=f_slow_n,
        dt_ns=dt_ns,
        t_long_ns=T_long_ns
    )

    energies = [100.0, 200.0, 300.0, 500.0, 800.0, 1200.0]
    fom_energy = evaluate_fom_energy_dependence(base_energy_keVee, base_fom, energies)

    return {
        "scintillator": scintillator,
        "decay_parameters": {
            "tau_rise_ns": float(tau_rise_ns),
            "tau_fast_ns": float(tau_fast_ns),
            "tau_slow_ns": float(tau_slow_ns),
            "f_slow_gamma": float(f_slow_g),
            "f_slow_neutron": float(f_slow_n)
        },
        "gate_parameters": {
            "T_long_ns": float(T_long_ns),
            "sampling_dt_ns": float(dt_ns),
            "optimal_T_short_ns": opt_res["optimal_T_short_ns"]
        },
        "optimal_psd_separation": {
            "max_delta_PSD": opt_res["max_delta_PSD"],
            "PSD_gamma": opt_res["optimal_PSD_gamma"],
            "PSD_neutron": opt_res["optimal_PSD_neutron"]
        },
        "fom_at_reference_energy": {
            "reference_energy_keVee": float(base_energy_keVee),
            "FOM": float(base_fom)
        },
        "energy_dependence_fom": fom_energy
    }


def format_text_report(res, title="Digital PSD & Charge Comparison Method Engine"):
    dp = res["decay_parameters"]
    gp = res["gate_parameters"]
    psd = res["optimal_psd_separation"]
    fom_ref = res["fom_at_reference_energy"]

    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Scintillator: {res['scintillator']}")
    lines.append("=" * 76)
    lines.append(f"  Rise Time (tau_rise)            : {dp['tau_rise_ns']:.2f} ns")
    lines.append(f"  Fast Decay Component (tau_fast) : {dp['tau_fast_ns']:.2f} ns")
    lines.append(f"  Slow Decay Component (tau_slow) : {dp['tau_slow_ns']:.1f} ns")
    lines.append(f"  Slow Component Fraction (Gamma) : {dp['f_slow_gamma']*100.0:.1f}%")
    lines.append(f"  Slow Component Fraction (Neutron): {dp['f_slow_neutron']*100.0:.1f}%")
    lines.append("-" * 76)
    lines.append("Charge Comparison Method (CCM) Gate Optimization:")
    lines.append(f"  Total Integration Window T_long : {gp['T_long_ns']:.1f} ns")
    lines.append(f"  Optimal Short Gate T_short      : {gp['optimal_T_short_ns']:.1f} ns")
    lines.append(f"  Gamma Peak Centroid PSD_g       : {psd['PSD_gamma']:.4f}")
    lines.append(f"  Neutron Peak Centroid PSD_n     : {psd['PSD_neutron']:.4f}")
    lines.append(f"  Maximum Peak Separation Delta_PSD: {psd['max_delta_PSD']:.4f}")
    lines.append(f"  Reference Energy & FOM          : {fom_ref['FOM']:.2f} at {fom_ref['reference_energy_keVee']:.0f} keVee")
    lines.append("-" * 76)
    lines.append("Energy Threshold & FOM Systematics (Poisson Light Yield Model):")
    lines.append("   Energy (keVee)       FOM            Quality Classification")
    for e_pt in res["energy_dependence_fom"]:
        lines.append(f"     {e_pt['energy_keVee']:7.1f}          {e_pt['FOM']:5.2f}          {e_pt['separation_quality']}")
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Digital Pulse Shape Discrimination (PSD), CCM Gate Optimization & Neutron/Gamma FOM Engine."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load experimental preset")
    parser.add_argument("--scintillator", type=str, default="Organic-Scintillator", help="Scintillator type")
    parser.add_argument("--tau-fast", type=float, default=3.2, help="Fast decay time in ns")
    parser.add_argument("--tau-slow", type=float, default=270.0, help="Slow decay time in ns")
    parser.add_argument("--f-slow-g", type=float, default=0.12, help="Slow fraction for gamma")
    parser.add_argument("--f-slow-n", type=float, default=0.32, help="Slow fraction for neutron")
    parser.add_argument("--t-long", type=float, default=350.0, help="Long integration gate in ns")
    parser.add_argument("--energy-kevee", type=float, default=500.0, help="Reference energy in keVee")
    parser.add_argument("--base-fom", type=float, default=1.45, help="FOM at reference energy")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        scintillator = p["scintillator"]
        tau_rise = p.get("tau_rise_ns", 1.5)
        tau_fast = p["tau_fast_ns"]
        tau_slow = p["tau_slow_ns"]
        f_slow_g = p["f_slow_gamma"]
        f_slow_n = p["f_slow_neutron"]
        t_long = p.get("T_long_ns", 350.0)
        dt = p.get("sampling_dt_ns", 0.5)
        base_energy = p.get("base_energy_keVee", 500.0)
        base_fom = p.get("base_fom", 1.45)
        title = f"Preset: {args.preset} ({p['description']})"
    else:
        scintillator = args.scintillator
        tau_rise = 1.5
        tau_fast = args.tau_fast
        tau_slow = args.tau_slow
        f_slow_g = args.f_slow_g
        f_slow_n = args.f_slow_n
        t_long = args.t_long
        dt = 0.5
        base_energy = args.energy_kevee
        base_fom = args.base_fom
        title = "Custom User Input"

    res = run_psd_analysis(
        scintillator=scintillator,
        tau_rise_ns=tau_rise,
        tau_fast_ns=tau_fast,
        tau_slow_ns=tau_slow,
        f_slow_g=f_slow_g,
        f_slow_n=f_slow_n,
        T_long_ns=t_long,
        dt_ns=dt,
        base_energy_keVee=base_energy,
        base_fom=base_fom
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
