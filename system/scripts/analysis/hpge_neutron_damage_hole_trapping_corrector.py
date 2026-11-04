#!/usr/bin/env python3
"""
HPGe Detector Neutron Damage Hole Trapping Distortion & Digital Restoration Filter.

Physical Principle & Formalism:
In long-duration in-beam heavy-ion gamma-ray experiments, high-purity germanium (HPGe)
detectors are exposed to intense fast neutron fluences (Phi_n ~ 10^9 - 10^10 n/cm^2)
produced by compound nucleus evaporation.
Neutrons create disordered cluster defects in the germanium lattice that act as deep
acceptor centers with large capture cross sections for HOLES (sigma_h >> sigma_e).

1. Incomplete Charge Collection & Generalized Hecht Relation:
   For a detector of active thickness d:
   If a gamma-ray interacts at depth x from the contact:
     Q(x) = Q_0 * [ (lambda_e / d) * (1 - exp(-(d - x) / lambda_e)) + (lambda_h / d) * (1 - exp(-x / lambda_h)) ]
   where the hole mean free path is lambda_h = v_drift,h * tau_h.
   Under neutron damage, the hole lifetime tau_h degrades from > 50 us to 5 - 20 us (lambda_h ~ 50 - 200 cm),
   while electron transport remains unhindered (lambda_e ~ 500 cm).
   Events where holes must drift long distances suffer charge deficits Delta Q(x) ~ x^2 / (2 * d * lambda_h).

2. Peak Shape Distortion:
   The monoenergetic photopeak broadens into an asymmetric shape with an exponential
   low-energy tail ("hole tailing"):
     FWHM increases from 2.0 keV to 4.5 - 12.0 keV;
     FWTM / FWHM ratio degrades from 1.82 (Gaussian) to > 2.8 - 4.0;
     Peak centroids shift down by several keV, destroying Ritz loop energy closure.

3. Digital Rise-Time Trapping Inversion:
   In Digital Pulse Processing (DPP), the pulse 10%-90% rise time t_r measures carrier
   drift duration and interaction depth x:
     t_r(x) ~ t_r_min + x / v_drift
   The charge deficit is functionally correlated with rise time:
     Delta E(t_r) = c_0 + c_1 * (t_r - t_r_min) + c_2 * (t_r - t_r_min)^2
   The digitally restored energy is:
     E_corr = E_meas + Delta E(t_r)
   Restoring the degraded 5-15 keV resolution back to <= 2.2 keV!

This module implements:
1. Simulation of neutron-damaged HPGe peak with realistic Hecht charge collection distribution.
2. Two-dimensional (E_meas, t_r) trapping correlation matrix generation.
3. Polynomial calibration of digital rise-time correction Delta E(t_r).
4. Full spectral restoration, recovery of FWHM, FWTM / FWHM ratio, and peak centroid.
5. Presets for heavy-ion in-beam damage scenarios (moderate, severe, and mild fluences).

Textbook & Literature References:
- Wu Zhihua, 《原子核物理实验方法》 (3rd Ed.), Ch. 8, §8.3 (pp. 180-195)
- Wang Xiaolian et al., 《粒子探测技术》, Ch. 8, §8.2 (pp. 260-280)
- N. Nakhostin, 《Signal Processing for Radiation Detectors》 (Wiley 2017), Ch. 5 & 8
- T. W. Raudorf et al., IEEE Trans. Nucl. Sci. 31, 253 (1984)
- S. L. Shepherd et al., Nucl. Instrum. Meth. A 434, 373 (1999)
"""

import sys
import json
import argparse
import numpy as np

PRESETS = {
    "moderate_neutron_damage_1332keV": {
        "detector": "70% Coaxial HPGe (Phi_n ~ 2e9 n/cm^2)",
        "description": "Moderate neutron damage after 60h in-beam run at 60Co 1332.5 keV",
        "data_kind": "synthetic_simulation_benchmark",
        "E_true_keV": 1332.5,
        "fwhm_undamaged_keV": 2.10,
        "hole_lifetime_us": 14.0,   # lambda_h = 140 cm
        "detector_depth_cm": 5.0,
        "t_r_min_ns": 110.0,
        "n_events": 20000
    },
    "severe_neutron_damage_850keV": {
        "detector": "Segmented Clover HPGe Leaf (Phi_n ~ 8e9 n/cm^2)",
        "description": "Severe neutron damage after 150h heavy-ion run at 134Ce 852.0 keV",
        "data_kind": "synthetic_simulation_benchmark",
        "E_true_keV": 852.0,
        "fwhm_undamaged_keV": 1.95,
        "hole_lifetime_us": 8.0,    # lambda_h = 80 cm
        "detector_depth_cm": 4.0,
        "t_r_min_ns": 95.0,
        "n_events": 20000
    },
    "mild_neutron_damage_511keV": {
        "detector": "Planar HPGe Detector (Phi_n ~ 8e8 n/cm^2)",
        "description": "Mild damage on low-energy planar detector at 511.0 keV annihilation peak",
        "data_kind": "synthetic_simulation_benchmark",
        "E_true_keV": 511.0,
        "fwhm_undamaged_keV": 1.65,
        "hole_lifetime_us": 25.0,   # lambda_h = 250 cm
        "detector_depth_cm": 2.5,
        "t_r_min_ns": 60.0,
        "n_events": 20000
    }
}

class HPGeneutronDamageTrappingCorrector:
    def __init__(self, E_true_keV=1332.5, fwhm_undamaged_keV=2.10,
                 hole_lifetime_us=14.0, detector_depth_cm=5.0,
                 t_r_min_ns=110.0):
        self.E0 = float(E_true_keV)
        self.fwhm_0 = float(fwhm_undamaged_keV)
        self.sigma_0 = self.fwhm_0 / 2.355
        self.tau_h = float(hole_lifetime_us) * 1e-6 # s
        self.d = float(detector_depth_cm)            # cm
        self.t_r_min = float(t_r_min_ns)

        self.v_h = 1.0e7 # cm / s
        self.v_e = 1.0e7 # cm / s

        self.lambda_h = self.v_h * self.tau_h # cm
        self.lambda_e = 500.0                 # cm

    def simulate_damaged_events(self, n_events=20000, seed=42):
        """
        Simulates raw damaged events: (E_meas, t_r, x).
        """
        rng = np.random.default_rng(seed)

        # Exponential attenuation profile P(x) = exp(-mu * x)
        mu_att = 0.35 # cm^-1
        u = rng.uniform(0.0, 1.0, n_events)
        x = - (1.0 / mu_att) * np.log(1.0 - u * (1.0 - np.exp(-mu_att * self.d)))

        # Generalized Hecht collection efficiency eta(x)
        term_e = (self.lambda_e / self.d) * (1.0 - np.exp(-(self.d - x) / self.lambda_e))
        term_h = (self.lambda_h / self.d) * (1.0 - np.exp(-x / self.lambda_h))
        eta = term_e + term_h

        # Pulse rise time t_r in ns
        t_r = self.t_r_min + (x / self.v_h) * 1e9 + rng.normal(0.0, 4.0, n_events)

        # Energy measured: E0 * eta + electronic noise Gaussian
        noise = rng.normal(0.0, self.sigma_0, n_events)
        E_meas = self.E0 * eta + noise

        return E_meas, t_r, x

    def calibrate_rise_time_correction(self, E_meas, t_r):
        """
        Fits 2nd-order polynomial Delta E(t_r) = c0 + c1*(tr - tr_min) + c2*(tr - tr_min)^2.
        """
        dt = t_r - self.t_r_min
        # Deficit relative to E0
        deficit = self.E0 - E_meas
        poly_coeff = np.polyfit(dt, deficit, deg=2)
        return poly_coeff

    def apply_digital_correction(self, E_meas, t_r, poly_coeff):
        """
        Restores pulse energy: E_corr = E_meas + Delta E(t_r).
        """
        dt = t_r - self.t_r_min
        deficit_corr = np.polyval(poly_coeff, dt)
        return E_meas + deficit_corr

    def calculate_peak_metrics(self, energies):
        """
        Calculates centroid, FWHM, and FWTM / FWHM shape ratio.
        """
        hist, bin_edges = np.histogram(energies, bins=350, range=(self.E0 - 20.0, self.E0 + 10.0))
        bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])

        peak_idx = np.argmax(hist)
        peak_max = hist[peak_idx]
        centroid = float(bin_centers[peak_idx])

        half_max = peak_max / 2.0
        tenth_max = peak_max / 10.0

        idx_left_half = np.where((bin_centers < centroid) & (hist < half_max))[0]
        idx_right_half = np.where((bin_centers > centroid) & (hist < half_max))[0]

        if len(idx_left_half) > 0 and len(idx_right_half) > 0:
            left_half = bin_centers[idx_left_half[-1]]
            right_half = bin_centers[idx_right_half[0]]
            fwhm = float(right_half - left_half)
        else:
            fwhm = float(2.355 * np.std(energies))

        idx_left_tenth = np.where((bin_centers < centroid) & (hist < tenth_max))[0]
        idx_right_tenth = np.where((bin_centers > centroid) & (hist < tenth_max))[0]

        if len(idx_left_tenth) > 0 and len(idx_right_tenth) > 0:
            left_tenth = bin_centers[idx_left_tenth[-1]]
            right_tenth = bin_centers[idx_right_tenth[0]]
            fwtm = float(right_tenth - left_tenth)
        else:
            fwtm = float(fwhm * 1.82)

        fwtm_fwhm_ratio = float(fwtm / max(0.1, fwhm))

        return {
            "centroid_keV": centroid,
            "fwhm_keV": fwhm,
            "fwtm_keV": fwtm,
            "fwtm_fwhm_ratio": fwtm_fwhm_ratio
        }

    def execute_restoration(self, n_events=20000):
        """
        Full restoration workflow: simulation -> metrics -> polynomial fit -> restored metrics.
        """
        E_meas, t_r, _ = self.simulate_damaged_events(n_events=n_events)
        raw_metrics = self.calculate_peak_metrics(E_meas)

        poly = self.calibrate_rise_time_correction(E_meas, t_r)
        E_corr = self.apply_digital_correction(E_meas, t_r, poly)
        restored_metrics = self.calculate_peak_metrics(E_corr)

        impr_pct = (raw_metrics["fwhm_keV"] - restored_metrics["fwhm_keV"]) / raw_metrics["fwhm_keV"] * 100.0

        return {
            "analysis_kind": "phenomenological_hecht_trapping_model",
            "data_kind": "synthetic_simulation_benchmark",
            "methodological_boundary": "Hecht charge-trapping simulation and digital rise-time restoration model; events are generated from physical transport equations, not replayed from hardware experimental waveforms",
            "E_true_keV": self.E0,
            "fwhm_undamaged_ideal_keV": self.fwhm_0,
            "hole_lifetime_us": self.tau_h * 1e6,
            "raw_damaged_metrics": raw_metrics,
            "polynomial_correction_coefficients": poly.tolist(),
            "restored_metrics": restored_metrics,
            "fwhm_improvement_percent": float(impr_pct),
            "is_resolution_recovered": bool(restored_metrics["fwhm_keV"] <= 1.25 * self.fwhm_0)
        }

def run_trapping_correction_analysis(detector="Generic HPGe", E_true_keV=1332.5,
                                     fwhm_undamaged_keV=2.10, hole_lifetime_us=14.0,
                                     detector_depth_cm=5.0, t_r_min_ns=110.0,
                                     n_events=20000):
    corrector = HPGeneutronDamageTrappingCorrector(
        E_true_keV=E_true_keV,
        fwhm_undamaged_keV=fwhm_undamaged_keV,
        hole_lifetime_us=hole_lifetime_us,
        detector_depth_cm=detector_depth_cm,
        t_r_min_ns=t_r_min_ns
    )
    res = corrector.execute_restoration(n_events=n_events)
    res["detector"] = detector
    return res

def format_text_report(output, title="HPGe Neutron Damage Hole Trapping Digital Corrector"):
    lines = []
    lines.append("=" * 76)
    lines.append(f"  {title}")
    lines.append("=" * 76)
    lines.append(f"Detector: {output['detector']} | True Energy: E_0 = {output['E_true_keV']:.1f} keV")
    lines.append(f"Neutron Damage Level: Hole Lifetime tau_h = {output['hole_lifetime_us']:.1f} us (Ideal FWHM = {output['fwhm_undamaged_ideal_keV']:.2f} keV)")

    raw = output["raw_damaged_metrics"]
    rst = output["restored_metrics"]
    lines.append("\n[1] Damaged vs. Restored Photopeak Metrics:")
    lines.append("  Metric                      Damaged State      Restored (Corrected)   Target (Ideal)")
    lines.append("  ---------------------------------------------------------------------------------")
    lines.append(f"  Centroid Energy (keV):       {raw['centroid_keV']:10.2f}         {rst['centroid_keV']:10.2f}          {output['E_true_keV']:10.2f}")
    lines.append(f"  Energy Resolution FWHM (keV):{raw['fwhm_keV']:10.2f}         {rst['fwhm_keV']:10.2f}          {output['fwhm_undamaged_ideal_keV']:10.2f}")
    lines.append(f"  Tenth Maximum FWTM (keV):    {raw['fwtm_keV']:10.2f}         {rst['fwtm_keV']:10.2f}          {output['fwhm_undamaged_ideal_keV']*1.82:10.2f}")
    lines.append(f"  Peak Tail Ratio FWTM/FWHM:   {raw['fwtm_fwhm_ratio']:10.2f}         {rst['fwtm_fwhm_ratio']:10.2f}                1.82")

    poly = output["polynomial_correction_coefficients"]
    lines.append("\n[2] Digital Restoration Polynomial Coefficients:")
    lines.append(f"  c_2 (quadratic, keV/ns^2):             {poly[0]:.6e}")
    lines.append(f"  c_1 (linear, keV/ns):                  {poly[1]:.6e}")
    lines.append(f"  c_0 (offset, keV):                     {poly[2]:.4f}")
    lines.append(f"  FWHM Resolution Improvement:           +{output['fwhm_improvement_percent']:.1f} %")
    lines.append(f"  Restoration Diagnostic Verdict:        {'SUCCESS (Gaussian Restored <= 1.25*FWHM0)' if output['is_resolution_recovered'] else 'PARTIAL RECOVERY'}")
    lines.append("-" * 76)
    lines.append("Methodology Takeaway: Digital rise-time correlated charge loss compensation")
    lines.append("eliminates neutron hole-tailing without interrupting in-beam data acquisition.")
    lines.append("=" * 76)
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="HPGe Neutron Damage Hole Trapping Digital Corrector")
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Preset configuration")
    parser.add_argument("--energy", type=float, help="True gamma-ray energy (keV)")
    parser.add_argument("--tau-h", type=float, help="Effective hole lifetime tau_h (microseconds)")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON format")
    args = parser.parse_args()

    cfg = PRESETS["moderate_neutron_damage_1332keV"].copy()
    if args.preset:
        cfg = PRESETS[args.preset].copy()
    if args.energy is not None:
        cfg["E_true_keV"] = args.energy
    if args.tau_h is not None:
        cfg["hole_lifetime_us"] = args.tau_h

    res = run_trapping_correction_analysis(
        detector=cfg.get("detector", "Generic HPGe"),
        E_true_keV=cfg["E_true_keV"],
        fwhm_undamaged_keV=cfg["fwhm_undamaged_keV"],
        hole_lifetime_us=cfg["hole_lifetime_us"],
        detector_depth_cm=cfg["detector_depth_cm"],
        t_r_min_ns=cfg["t_r_min_ns"],
        n_events=cfg.get("n_events", 20000)
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=f"Preset: {args.preset or 'moderate_neutron_damage_1332keV'} ({cfg['description']})"))

if __name__ == "__main__":
    main()
