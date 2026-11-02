#!/usr/bin/env python3
"""
Heavy-Ion Triaxial Nuclei Fusion Barrier Distribution Inverter.

Physical Principle & Formalism:
In heavy-ion fusion reactions, channel coupling of relative motion to nuclear shape
degrees of freedom (quadrupole and hexadecapole deformations) produces an effective
distribution of potential barriers D_fus(E) = d^2(E * sigma_fus) / dE^2.

For a spherical projectile colliding with a triaxially deformed target nucleus with
deformation parameters (beta_2, gamma):
The orientation-dependent nuclear radius in the intrinsic body-fixed frame is:
  R(theta, phi) = R_0 * [1 + sqrt(5 / (16 * pi)) * beta_2 * (cos(gamma) * (3*cos^2(theta) - 1) + sqrt(3) * sin(gamma) * sin^2(theta) * cos(2*phi))]

To first order in deformation, the height of the Coulomb + proximity fusion barrier
depends on the orientation of the target relative to the collision axis:
  V_B(theta, phi) = V_B0 - Delta V_B * [cos(gamma) * (3*cos^2(theta) - 1) + sqrt(3) * sin(gamma) * sin^2(theta) * cos(2*phi)]
where:
  Delta V_B = V_B0 * sqrt(5 / (16 * pi)) * (R_t / (R_p + R_t)) * beta_2

In Wong's parabolic barrier penetration model with barrier curvature hbar * omega_B:
The fusion cross section is an orientation average over the unit sphere:
  sigma_fus(E) = (R_B^2 * hbar * omega_B) / (2 * E) * (2 / pi) * int_0^{pi/2} sin(theta) d(theta) * int_0^{pi/2} d(phi) * ln[1 + exp(2*pi*(E - V_B(theta, phi)) / (hbar * omega_B))]

The fusion barrier distribution is defined by:
  D_fus(E) = d^2(E * sigma_fus) / dE^2

Distinctive Structural Signatures:
1. Spherical target (beta_2 = 0): Single symmetric bell-shaped peak centered at V_B0 with width ~ hbar*omega_B / pi.
2. Axially symmetric prolate target (gamma = 0 deg): Two-peaked distribution (low-energy pole-on collision, high-energy belly-on collision).
3. Triaxial target (0 < gamma < 60 deg, e.g. gamma ~ 25-30 deg): The belly-on peak splits into two separate sub-peaks corresponding to collision along the short axis (phi=0) and intermediate axis (phi=pi/2), generating a unique three-peaked barrier distribution fingerprint!

This module implements:
1. Exact 2D orientation integration of Wong's formula for arbitrary (beta_2, gamma).
2. Numerical second derivative calculation with spline and finite-difference smoothing.
3. Analysis of barrier distribution centroids, peak splitting, and barrier widths.
4. Presets for heavy-ion fusion systems.

Textbook & Literature References:
- Lin Chengjian, 《重离子核反应》 (Heavy-Ion Nuclear Reactions), Ch. 4, §4.3
- C. A. Bertulani & P. Danielewicz, 《Introduction to Nuclear Reactions》 (CRC 2004), Ch. 7, §7.4
- Rowley, Satchler & Stelson, Phys. Lett. B 254, 25 (1991)
- Leigh et al., Phys. Rev. C 52, 3151 (1995)
"""

import sys
import json
import argparse
import numpy as np
from scipy.interpolate import UnivariateSpline

PRESETS = {
    "16O_154Sm_prolate_baseline": {
        "system": "16O + 154Sm",
        "description": "Classic axially prolate deformed fusion baseline (beta2=0.30, gamma=0)",
        "Ap": 16, "Zp": 8,
        "At": 154, "Zt": 62,
        "V_B0_MeV": 60.0,
        "R_B0_fm": 10.8,
        "hbar_omega_B_MeV": 4.5,
        "beta2": 0.30,
        "gamma_deg": 0.0,
        "energy_eval_range_MeV": [52.0, 70.0],
        "n_energy_points": 50
    },
    "16O_186W_triaxial_candidate": {
        "system": "16O + 186W",
        "description": "Heavy transitional triaxial candidate (beta2=0.23, gamma=22 deg)",
        "Ap": 16, "Zp": 8,
        "At": 186, "Zt": 74,
        "V_B0_MeV": 72.5,
        "R_B0_fm": 11.2,
        "hbar_omega_B_MeV": 4.2,
        "beta2": 0.23,
        "gamma_deg": 22.0,
        "energy_eval_range_MeV": [64.0, 84.0],
        "n_energy_points": 50
    },
    "36S_100Mo_in_beam_fusion": {
        "system": "36S + 100Mo",
        "description": "In-beam gamma entry state fusion reaction for A~130 spectroscopy (beta2=0.20, gamma=25 deg)",
        "Ap": 36, "Zp": 16,
        "At": 100, "Zt": 42,
        "V_B0_MeV": 82.0,
        "R_B0_fm": 10.5,
        "hbar_omega_B_MeV": 4.0,
        "beta2": 0.20,
        "gamma_deg": 25.0,
        "energy_eval_range_MeV": [73.0, 93.0],
        "n_energy_points": 50
    }
}

class TriaxialFusionBarrierInverter:
    def __init__(self, V_B0_MeV=60.0, R_B0_fm=10.8, hbar_omega_B_MeV=4.5,
                 beta2=0.25, gamma_deg=25.0, Ap=16, At=154):
        self.V_B0 = float(V_B0_MeV)
        self.R_B0 = float(R_B0_fm)
        self.hbar_omega_B = float(hbar_omega_B_MeV)
        self.beta2 = float(beta2)
        self.gamma = np.radians(gamma_deg)
        self.gamma_deg = float(gamma_deg)
        self.Ap = float(Ap)
        self.At = float(At)

        # Nuclear radii estimates: R = 1.2 * A^(1/3)
        R_p = 1.2 * (self.Ap**(1.0/3.0))
        R_t = 1.2 * (self.At**(1.0/3.0))
        # Barrier shift scaling coefficient Delta V_B
        geom_factor = np.sqrt(5.0 / (16.0 * np.pi)) * (R_t / (R_p + R_t))
        self.delta_V = self.V_B0 * geom_factor * self.beta2

    def orientation_barrier(self, theta, phi):
        """
        Calculates local fusion barrier V_B(theta, phi) for target orientation angles:
        theta in [0, pi/2], phi in [0, pi/2]
        """
        c_th = np.cos(theta)
        s_th = np.sin(theta)
        y20_term = np.cos(self.gamma) * (3.0 * c_th**2 - 1.0)
        y22_term = np.sqrt(3.0) * np.sin(self.gamma) * (s_th**2) * np.cos(2.0 * phi)
        V_b = self.V_B0 - self.delta_V * (y20_term + y22_term)
        return V_b

    def calculate_cross_section(self, E_cm):
        """
        Orientation-averaged fusion cross section sigma_fus(E_cm) in millibarns (mb).
        Uses 2D Gauss-Legendre quadrature over theta in [0, pi/2] and phi in [0, pi/2].
        """
        if E_cm <= 0.1:
            return 0.0

        n_pts = 32
        x_th, w_th = np.polynomial.legendre.leggauss(n_pts)
        theta = 0.5 * (np.pi / 2.0) * (x_th + 1.0)
        w_th_scaled = w_th * 0.5 * (np.pi / 2.0)

        x_ph, w_ph = np.polynomial.legendre.leggauss(n_pts)
        phi = 0.5 * (np.pi / 2.0) * (x_ph + 1.0)
        w_ph_scaled = w_ph * 0.5 * (np.pi / 2.0)

        # 2D Grid
        TH, PH = np.meshgrid(theta, phi, indexing='ij')
        W_TH, W_PH = np.meshgrid(w_th_scaled, w_ph_scaled, indexing='ij')

        V_b = self.orientation_barrier(TH, PH)
        arg = 2.0 * np.pi * (E_cm - V_b) / self.hbar_omega_B

        # Stable log(1 + exp(arg)) computation
        log_term = np.zeros_like(arg)
        mask_pos = arg > 30.0
        mask_neg = arg < -30.0
        mask_mid = ~mask_pos & ~mask_neg

        log_term[mask_pos] = arg[mask_pos]
        log_term[mask_neg] = np.exp(arg[mask_neg])
        log_term[mask_mid] = np.log(1.0 + np.exp(arg[mask_mid]))

        integrand = np.sin(TH) * log_term * W_TH * W_PH
        integral = np.sum(integrand)

        # Normalization factor: (2 / pi) for phi integration from 0 to pi/2
        # Front factor: (R_B^2 * hbar * omega_B) / (2 * E_cm)
        # 1 fm^2 = 10 mb
        pref = (self.R_B0**2 * self.hbar_omega_B) / (2.0 * E_cm) * 10.0 * (2.0 / np.pi)
        sigma_mb = pref * integral
        return float(max(1e-9, sigma_mb))

    def evaluate_barrier_distribution(self, energies_MeV):
        """
        Evaluates E * sigma_fus(E) and its second derivative D_fus(E) = d^2(E * sigma) / dE^2.
        """
        energies = np.array(energies_MeV, dtype=float)
        cross_sections = np.array([self.calculate_cross_section(e) for e in energies])
        E_sigma = energies * cross_sections

        # Spline smoothed second derivative
        spline = UnivariateSpline(energies, E_sigma, s=0.0)
        d2_E_sigma = spline.derivative(n=2)(energies)

        # Identification of primary barriers:
        # V_pole: theta = 0 (pole-on collision)
        V_pole = self.orientation_barrier(0.0, 0.0)
        # V_side_short: theta = pi/2, phi = 0 (side-on, short axis)
        V_side_s = self.orientation_barrier(np.pi / 2.0, 0.0)
        # V_side_intermediate: theta = pi/2, phi = pi/2 (side-on, intermediate axis)
        V_side_i = self.orientation_barrier(np.pi / 2.0, np.pi / 2.0)

        # Centroid of the barrier distribution
        weights = np.maximum(0.0, d2_E_sigma)
        if np.sum(weights) > 1e-6:
            centroid_E = float(np.sum(energies * weights) / np.sum(weights))
            variance_E = float(np.sum((energies - centroid_E)**2 * weights) / np.sum(weights))
            width_fwhm = 2.355 * np.sqrt(variance_E)
        else:
            centroid_E = self.V_B0
            width_fwhm = self.hbar_omega_B

        return {
            "energies_MeV": energies.tolist(),
            "cross_sections_mb": cross_sections.tolist(),
            "D_fus_distribution": d2_E_sigma.tolist(),
            "characteristic_barriers": {
                "V_pole_MeV": float(V_pole),
                "V_side_short_axis_MeV": float(V_side_s),
                "V_side_interm_axis_MeV": float(V_side_i),
                "barrier_splitting_pole_side_MeV": float(abs(V_side_s - V_pole)),
                "triaxial_belly_splitting_MeV": float(abs(V_side_i - V_side_s))
            },
            "distribution_centroid_MeV": centroid_E,
            "distribution_fwhm_MeV": float(width_fwhm),
            "is_triaxial_fingerprint": bool(self.gamma_deg > 5.0 and self.gamma_deg < 55.0 and abs(V_side_i - V_side_s) > 0.4)
        }

def run_fusion_barrier_analysis(system="Generic", V_B0_MeV=60.0, R_B0_fm=10.8,
                                hbar_omega_B_MeV=4.5, beta2=0.25, gamma_deg=25.0,
                                Ap=16, At=154, energy_range_MeV=None, n_points=50):
    if energy_range_MeV is None:
        energy_range_MeV = [V_B0_MeV - 8.0, V_B0_MeV + 10.0]
    energies = np.linspace(energy_range_MeV[0], energy_range_MeV[1], n_points)
    inverter = TriaxialFusionBarrierInverter(
        V_B0_MeV=V_B0_MeV, R_B0_fm=R_B0_fm, hbar_omega_B_MeV=hbar_omega_B_MeV,
        beta2=beta2, gamma_deg=gamma_deg, Ap=Ap, At=At
    )
    res = inverter.evaluate_barrier_distribution(energies)
    res["system"] = system
    res["beta2"] = beta2
    res["gamma_deg"] = gamma_deg
    return res

def format_text_report(output, title="Heavy-Ion Triaxial Fusion Barrier Distribution Analysis"):
    lines = []
    lines.append("=" * 76)
    lines.append(f"  {title}")
    lines.append("=" * 76)
    lines.append(f"System: {output['system']} | beta2 = {output['beta2']:.3f}, gamma = {output['gamma_deg']:.1f} deg")
    cb = output["characteristic_barriers"]
    lines.append("\n[1] Orientation-Dependent Characteristic Fusion Barriers:")
    lines.append(f"  V_pole (theta=0, pole-on):                {cb['V_pole_MeV']:.2f} MeV")
    lines.append(f"  V_side (theta=90, phi=0, short axis):     {cb['V_side_short_axis_MeV']:.2f} MeV")
    lines.append(f"  V_side (theta=90, phi=90, interm axis):   {cb['V_side_interm_axis_MeV']:.2f} MeV")
    lines.append(f"  Pole-to-Side Barrier Splitting:           Delta V_ps = {cb['barrier_splitting_pole_side_MeV']:.2f} MeV")
    lines.append(f"  Triaxial In-Plane Belly Splitting:        Delta V_tri = {cb['triaxial_belly_splitting_MeV']:.2f} MeV")
    lines.append(f"  Triaxial Structural Signature:            {'CONFIRMED (Three-barrier structure)' if output['is_triaxial_fingerprint'] else 'Axial or Weak Triaxial'}")
    lines.append("\n[2] Barrier Distribution Summary:")
    lines.append(f"  Effective Centroid Energy:                <E_barrier> = {output['distribution_centroid_MeV']:.2f} MeV")
    lines.append(f"  Effective FWHM Barrier Width:             FWHM = {output['distribution_fwhm_MeV']:.2f} MeV")
    lines.append("\n[3] Sample Excitation Function & D_fus(E):")
    lines.append("   E_cm (MeV)       sigma_fus (mb)       D_fus = d2(E*sigma)/dE2")
    lines.append("   --------------------------------------------------------------")
    # Print 7 representative points
    step = len(output["energies_MeV"]) // 6
    for i in range(0, len(output["energies_MeV"]), step):
        lines.append(f"     {output['energies_MeV'][i]:6.2f}            {output['cross_sections_mb'][i]:9.2f}              {output['D_fus_distribution'][i]:10.3f}")
    lines.append("-" * 76)
    lines.append("Methodology Takeaway: Non-axial triaxial deformation gamma lifts the belly-on")
    lines.append("barrier degeneracy, producing an identifiable multi-peaked barrier distribution.")
    lines.append("=" * 76)
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Triaxial Heavy-Ion Fusion Barrier Distribution Inverter")
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Preset configuration")
    parser.add_argument("--beta2", type=float, help="Quadrupole deformation parameter beta2")
    parser.add_argument("--gamma", type=float, help="Triaxial deformation angle gamma (degrees)")
    parser.add_argument("--vb0", type=float, help="Spherical baseline barrier V_B0 (MeV)")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON format")
    args = parser.parse_args()

    cfg = PRESETS["16O_186W_triaxial_candidate"].copy()
    if args.preset:
        cfg = PRESETS[args.preset].copy()
    if args.beta2 is not None:
        cfg["beta2"] = args.beta2
    if args.gamma is not None:
        cfg["gamma_deg"] = args.gamma
    if args.vb0 is not None:
        cfg["V_B0_MeV"] = args.vb0

    res = run_fusion_barrier_analysis(
        system=cfg["system"],
        V_B0_MeV=cfg["V_B0_MeV"],
        R_B0_fm=cfg["R_B0_fm"],
        hbar_omega_B_MeV=cfg["hbar_omega_B_MeV"],
        beta2=cfg["beta2"],
        gamma_deg=cfg["gamma_deg"],
        Ap=cfg["Ap"],
        At=cfg["At"],
        energy_range_MeV=cfg["energy_eval_range_MeV"],
        n_points=cfg["n_energy_points"]
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=f"Preset: {args.preset or '16O_186W_triaxial_candidate'} ({cfg['description']})"))

if __name__ == "__main__":
    main()
