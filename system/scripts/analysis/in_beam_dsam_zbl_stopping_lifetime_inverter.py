#!/usr/bin/env python3
"""
In-Beam DSAM Stopping Power Lifetime & Quadrupole Moment Inverter.

Physical Principle & Methodological Foundations:
In heavy-ion in-beam gamma-ray spectroscopy, the Doppler Shift Attenuation Method (DSAM)
determines short nuclear state lifetimes (0.02 ps <= tau <= 2.0 ps) of high-spin rotational
and wobbling states.

Compound nucleus recoils enter a stopping medium (target backing, e.g. Au, Pb, Cu, Ta)
with initial recoil velocity beta_0 = v_0 / c ~ 0.015 - 0.040.
While slowing down, the recoil emits gamma-rays with Doppler-shifted energy:
  E_gamma(theta, t) = E_0 * [1 + (v(t) / c) * cos(theta)]
The experimentally measured centroid Doppler shift factor is:
  F(tau) = <v * cos(phi)> / v_0 = int_0^{t_stop} P(t) * (v(t) / v_0) * <cos(phi)>(t) dt
where P(t) is the decay probability distribution of the state.

1. Electronic and Nuclear Stopping:
   - Electronic Stopping S_e = - (dE/dx)_e:
     At low-to-medium velocities (v < v_0 * Z_1^(2/3)), electronic stopping is dominated by
     velocity-proportional drag S_e = k_e * sqrt(E), with shell oscillation modulations
     characterized by Ziegler, Biersack & Littmark (ZBL 1985 / SRIM).
   - Nuclear Stopping S_n = - (dE/dx)_n:
     At very low energies, screened Coulomb collisions dominate energy loss and direction deflections.

2. Nuclear Multiple Scattering (Blaugrund Theory):
   Elastic nuclear scattering deflects the ion velocity vector away from the initial beam axis:
     <cos(phi)>(t) = exp( - (1 / 2) * C_B * (M_stopper / M_recoil) * int_0^t (S_n(t') * v(t') / E(t')) dt' )
   where C_B ~ 0.5 - 1.0 is the Blaugrund deflection parameter and the integrand (S_n * v / E) dt'
   is strictly dimensionless.

3. Side-Feeding Temporal Delay (Bateman Population Convolution):
   In in-beam reactions, a discrete state is fed by a quasicontinuum cascade.
   Modeling the side-feeding as an effective single-cascade delay with time constant tau_sf:
     dP/dt = (1 / tau_sf) * exp(-t / tau_sf) - P(t) / tau_level
   The state population decay profile is the exact Bateman convolution:
     P(t) = (1 / (tau_level - tau_sf)) * [ exp(-t / tau_level) - exp(-t / tau_sf) ]   (tau_level != tau_sf)
     P(t) = (t / tau_level^2) * exp(-t / tau_level)                                    (tau_level == tau_sf)
   When tau_sf = 0, P(t) recovers the prompt exponential decay (1 / tau) * exp(-t / tau).
   Delayed side-feeding shifts decays toward later times when recoils are slower, reducing the
   observed F factor. The intrinsic level lifetime tau_level is inverted by matching the convoluted F.

4. Electromagnetic Transition Rates:
   From Bohr & Mottelson, "Nuclear Structure" Vol. I, p. 382, Eq. (3-28):
     T(E2) = (4 * pi / (75 * hbar * (hbar * c)^5)) * E_gamma^5 * B(E2)
           = 8.50845e12 * (E_gamma_MeV^5) * B(E2)[e^2 b^2]   (in s^-1)
   The intrinsic quadrupole moment Q_0 is obtained via the rotational projection:
     B(E2; I -> I-2) = (5 / (16 * pi)) * e^2 * Q_0^2 * <I 0 2 0 | I-2 0>^2

Textbook & Literature References:
- Wu Zhihua, 《原子核物理实验方法》 (3rd Ed.), Ch. 15, §15.3 (pp. 435-450)
- Lu Xiting, 《原子核物理》 (Revised Ed.), Ch. 6, §6.4
- A. E. Blaugrund, Nucl. Phys. 88, 501 (1966)
- J. F. Ziegler, J. P. Biersack, U. Littmark, "The Stopping and Range of Ions in Solids" (Pergamon 1985)
- Bohr & Mottelson, "Nuclear Structure", Vol. I, p. 382
- P. J. Nolan & J. F. Sharpey-Schafer, Rep. Prog. Phys. 42, 1 (1979)
"""

import sys
import json
import argparse
import numpy as np
from scipy.optimize import brentq
from scipy.interpolate import interp1d

PRESETS = {
    "130Ba_8plus_in_Au_backing": {
        "recoil_nucleus": "130Ba (synthetic benchmark)",
        "description": "130Ba 8+ state DSAM lifetime benchmark in gold (Au) backing (E_gamma = 712.5 keV)",
        "data_kind": "synthetic_model_benchmark",
        "Ar": 130, "Zr": 56,
        "As": 197, "Zs": 79,  # Au stopper
        "stopper_density_g_cm3": 19.32,
        "beta_0": 0.022,       # v_0 / c
        "E_gamma_keV": 712.5,
        "spin_initial": 8.0,
        "F_experimental": 0.62,
        "F_uncertainty": 0.04,
        "side_feeding_tau_ps": 0.05
    },
    "134Ce_12plus_in_Pb_backing": {
        "recoil_nucleus": "134Ce (synthetic benchmark)",
        "description": "134Ce 12+ high-spin state in lead (Pb) backing (E_gamma = 852.0 keV)",
        "data_kind": "synthetic_model_benchmark",
        "Ar": 134, "Zr": 58,
        "As": 208, "Zs": 82,  # Pb stopper
        "stopper_density_g_cm3": 11.34,
        "beta_0": 0.025,
        "E_gamma_keV": 852.0,
        "spin_initial": 12.0,
        "F_experimental": 0.78,
        "F_uncertainty": 0.03,
        "side_feeding_tau_ps": 0.03
    },
    "164Yb_14plus_in_Cu_backing": {
        "recoil_nucleus": "164Yb (synthetic benchmark)",
        "description": "164Yb 14+ yrast band crossing state in copper (Cu) backing (E_gamma = 628.0 keV)",
        "data_kind": "synthetic_model_benchmark",
        "Ar": 164, "Zr": 70,
        "As": 63, "Zs": 29,   # Cu stopper
        "stopper_density_g_cm3": 8.96,
        "beta_0": 0.018,
        "E_gamma_keV": 628.0,
        "spin_initial": 14.0,
        "F_experimental": 0.45,
        "F_uncertainty": 0.05,
        "side_feeding_tau_ps": 0.08
    }
}


class InBeamDSAMZBLInverter:
    def __init__(self, Ar=130, Zr=56, As=197, Zs=79, density_g_cm3=19.32, beta_0=0.022):
        self.Ar = float(Ar)
        self.Zr = float(Zr)
        self.As = float(As)
        self.Zs = float(Zs)
        self.rho = float(density_g_cm3)  # g / cm^3
        self.beta_0 = float(beta_0)
        self.c_cm_s = 2.99792458e10       # cm / s
        self.u_MeV = 931.494             # MeV / u
        self.v_0 = self.beta_0 * self.c_cm_s

        self.M_recoil_MeV = self.Ar * self.u_MeV
        E_init = self.E_init_MeV()

        # Electronic and nuclear stopping parameters (scaled to density and effective charges):
        k_scale = 850.0 * (self.rho / 19.32) * (self.Zr * self.Zs / 4424.0) * np.sqrt(130.0 / self.Ar)
        self.k_e = float(k_scale * 19.5)  # MeV / cm / sqrt(MeV)
        self.k_n = float(k_scale * 28.0)  # MeV / cm
        self.b_n = 0.35 / (E_init / 30.0)

    def E_init_MeV(self):
        return 0.5 * self.M_recoil_MeV * (self.beta_0**2)

    def stopping_powers(self, E_MeV):
        """
        Calculate electronic stopping S_e and nuclear stopping S_n in MeV / cm.
        """
        if E_MeV <= 1e-5:
            return 1e-4, 1e-4
        S_e = self.k_e * np.sqrt(max(1e-5, E_MeV))
        S_n = self.k_n / (1.0 + self.b_n * E_MeV)
        return float(S_e), float(S_n)

    def integrate_slowing_down(self, dt_fs=2.0, max_time_ps=5.0):
        """
        Integrates recoil trajectory dE/dt = - (S_e + S_n) * v.
        Returns:
          times_ps: array of time steps in ps
          v_over_v0: array of fractional velocity v(t) / v_0
          cos_phi: array of Blaugrund nuclear multiple scattering angular factor <cos(phi)>(t)
        """
        E = self.E_init_MeV()
        t = 0.0
        dt_s = dt_fs * 1e-15

        times_ps = [0.0]
        v_over_v0 = [1.0]
        cos_phi = [1.0]
        integral_sn_over_e = 0.0
        mass_ratio = self.As / self.Ar

        while t < max_time_ps * 1e-12 and E > 0.02 * self.E_init_MeV():
            v = np.sqrt(2.0 * E / self.M_recoil_MeV) * self.c_cm_s
            S_e, S_n = self.stopping_powers(E)

            dE = (S_e + S_n) * v * dt_s  # MeV loss
            E = max(1e-4, E - dE)
            t += dt_s

            v_new = np.sqrt(2.0 * E / self.M_recoil_MeV) * self.c_cm_s

            # Dimensionless Blaugrund integral: (S_n * v / E) dt is dimensionless
            integral_sn_over_e += (S_n * v / max(1e-4, E)) * dt_s
            blaugrund_factor = np.exp(-0.25 * mass_ratio * integral_sn_over_e)

            times_ps.append(t * 1e12)
            v_over_v0.append(v_new / self.v_0)
            cos_phi.append(float(np.clip(blaugrund_factor, 0.05, 1.0)))

        return np.array(times_ps), np.array(v_over_v0), np.array(cos_phi)

    def calculate_F_tau(self, tau_level_ps, times_ps=None, v_over_v0=None, cos_phi=None, tau_sf_ps=0.0):
        """
        Calculates theoretical F(tau) for a given level lifetime and side-feeding delay.
        Uses exact Bateman population convolution.
        """
        if times_ps is None:
            times_ps, v_over_v0, cos_phi = self.integrate_slowing_down()

        if tau_level_ps <= 1e-4:
            return 1.0

        t_ps = times_ps
        t_lvl = float(tau_level_ps)
        t_sf = float(tau_sf_ps)

        if t_sf <= 1e-4:
            P = np.exp(-t_ps / t_lvl) / t_lvl
        else:
            if abs(t_lvl - t_sf) < 1e-4:
                P = (t_ps / (t_lvl**2)) * np.exp(-t_ps / t_lvl)
            else:
                P = (np.exp(-t_ps / t_lvl) - np.exp(-t_ps / t_sf)) / (t_lvl - t_sf)

        integrand = v_over_v0 * cos_phi * P
        trap = getattr(np, "trapezoid", getattr(np, "trapz", None))
        F = trap(integrand, t_ps)
        return float(np.clip(F, 0.01, 0.99))

    def generate_attenuation_curve(self, tau_grid_ps=None, tau_sf_ps=0.0):
        """
        Generates reference F(tau) attenuation curve across 0.02 ps to 4.0 ps.
        """
        if tau_grid_ps is None:
            tau_grid_ps = np.logspace(-1.7, 0.6, 60)
        times_ps, v_ratio, cos_phi = self.integrate_slowing_down()
        F_values = [self.calculate_F_tau(tau, times_ps, v_ratio, cos_phi, tau_sf_ps) for tau in tau_grid_ps]
        return tau_grid_ps, np.array(F_values)

    def invert_lifetime(self, F_exp, F_err=0.04, tau_sf_ps=0.0):
        """
        Inverts nuclear state lifetime tau from experimental F_exp +/- F_err.
        Inverts both prompt raw lifetime tau_raw (assuming tau_sf=0) and intrinsic level lifetime tau_level
        (accounting for side-feeding convolution).
        """
        times_ps, v_ratio, cos_phi = self.integrate_slowing_down()

        # Invert prompt raw lifetime (tau_sf = 0)
        def f_raw_root(tau):
            return self.calculate_F_tau(tau, times_ps, v_ratio, cos_phi, 0.0) - F_exp

        try:
            tau_raw = float(brentq(f_raw_root, 0.005, 5.0))
        except ValueError:
            tau_grid, F_grid = self.generate_attenuation_curve(tau_sf_ps=0.0)
            interp = interp1d(F_grid[::-1], tau_grid[::-1], kind='linear', fill_value='extrapolate')
            tau_raw = float(interp(F_exp))

        # Invert intrinsic level lifetime with side-feeding convolution
        if tau_sf_ps <= 1e-4:
            tau_level = tau_raw
            def f_err_high(t):
                return self.calculate_F_tau(t, times_ps, v_ratio, cos_phi, 0.0) - (F_exp + F_err)
            def f_err_low(t):
                return self.calculate_F_tau(t, times_ps, v_ratio, cos_phi, 0.0) - (F_exp - F_err)
        else:
            def f_level_root(tau):
                return self.calculate_F_tau(tau, times_ps, v_ratio, cos_phi, tau_sf_ps) - F_exp
            try:
                tau_level = float(brentq(f_level_root, 0.005, 5.0))
            except ValueError:
                tau_level = max(0.005, tau_raw - float(tau_sf_ps))

            def f_err_high(t):
                return self.calculate_F_tau(t, times_ps, v_ratio, cos_phi, tau_sf_ps) - (F_exp + F_err)
            def f_err_low(t):
                return self.calculate_F_tau(t, times_ps, v_ratio, cos_phi, tau_sf_ps) - (F_exp - F_err)

        try:
            t_min = float(brentq(f_err_high, 0.005, 5.0))
        except ValueError:
            t_min = max(0.005, tau_level * 0.8)

        try:
            t_max = float(brentq(f_err_low, 0.005, 5.0))
        except ValueError:
            t_max = tau_level * 1.25

        sigma_tau = 0.5 * abs(t_max - t_min)

        return {
            "analysis_kind": "quantitative_dsam_inversion",
            "data_kind": "synthetic_model_benchmark",
            "F_experimental": float(F_exp),
            "F_uncertainty": float(F_err),
            "side_feeding_tau_ps": float(tau_sf_ps),
            "tau_raw_ps": tau_raw,
            "tau_level_ps": tau_level,
            "sigma_tau_ps": sigma_tau,
            "tau_level_fs": tau_level * 1000.0,
            "sigma_tau_fs": sigma_tau * 1000.0,
            "side_feeding_model": "Bateman convolution cascade: P(t) = (e^(-t/tau_lvl) - e^(-t/tau_sf))/(tau_lvl - tau_sf)"
        }

    def calculate_transition_properties(self, tau_level_ps, E_gamma_keV, spin_I):
        """
        Calculates B(E2; I -> I-2) in e^2 b^2 and intrinsic quadrupole moment Q_0 in e*b.
        From Bohr & Mottelson Vol. I p. 382:
          T(E2) = 8.50845e12 * (E_gamma_MeV^5) * B(E2)
        """
        tau_s = tau_level_ps * 1e-12
        E_gamma_MeV = E_gamma_keV * 1e-3
        I = float(spin_I)

        lambda_trans = 1.0 / tau_s
        be2 = lambda_trans / (8.50845e12 * (E_gamma_MeV**5))

        # Clebsch-Gordan squared <I 0 2 0 | I-2 0>^2 = 3*I*(I-1) / (2*(2I-1)*(2I+1))
        cg_squared = (3.0 * I * (I - 1.0)) / (2.0 * (2.0 * I - 1.0) * (2.0 * I + 1.0))
        q0_squared = be2 / ((5.0 / (16.0 * np.pi)) * cg_squared)
        Q_0 = np.sqrt(max(0.0, q0_squared))  # e * b

        # Weisskopf unit in e^2 * b^2: B_sp(E2) = 5.94e-6 * A^(4/3)
        b_sp = 5.94e-6 * (self.Ar**(4.0 / 3.0))
        be2_wu = be2 / b_sp

        return {
            "E_gamma_keV": float(E_gamma_keV),
            "spin_initial": I,
            "B_E2_e2b2": float(be2),
            "B_E2_W_u": float(be2_wu),
            "intrinsic_quadrupole_moment_Q0_eb": float(Q_0),
            "rotational_projection_cg2": float(cg_squared)
        }


def run_dsam_zbl_analysis(recoil_nucleus="Generic", Ar=130, Zr=56, As=197, Zs=79,
                          density_g_cm3=19.32, beta_0=0.022, E_gamma_keV=712.5,
                          spin_initial=8.0, F_experimental=0.62, F_uncertainty=0.04,
                          side_feeding_tau_ps=0.05):
    inverter = InBeamDSAMZBLInverter(
        Ar=Ar, Zr=Zr, As=As, Zs=Zs,
        density_g_cm3=density_g_cm3, beta_0=beta_0
    )
    lifetime_res = inverter.invert_lifetime(F_experimental, F_uncertainty, side_feeding_tau_ps)
    trans_res = inverter.calculate_transition_properties(lifetime_res["tau_level_ps"], E_gamma_keV, spin_initial)

    return {
        "analysis_kind": "quantitative_dsam_inversion",
        "data_kind": "synthetic_model_benchmark",
        "recoil_nucleus": recoil_nucleus,
        "Ar": Ar, "Zr": Zr,
        "As": As, "Zs": Zs,
        "stopper_density_g_cm3": density_g_cm3,
        "beta_0": beta_0,
        "lifetime_analysis": lifetime_res,
        "transition_properties": trans_res
    }


def format_text_report(output, title="In-Beam DSAM Lifetime & Transition Inversion"):
    lt = output["lifetime_analysis"]
    tp = output["transition_properties"]
    lines = []
    lines.append("=" * 78)
    lines.append(f"  {title}")
    lines.append("=" * 78)
    lines.append(f"Recoil: {output['recoil_nucleus']} (A={output['Ar']}, Z={output['Zr']}) | Stopper: A={output['As']}, Z={output['Zs']}")
    lines.append(f"Initial Velocity: beta_0 = {output['beta_0']:.4f} (v_0/c) | Stopper Density: {output['stopper_density_g_cm3']:.2f} g/cm^3")
    lines.append("\n[1] Doppler Shift Attenuation Factor Inversion:")
    lines.append(f"  Experimental F(tau):              {lt['F_experimental']:.3f} +/- {lt['F_uncertainty']:.3f}")
    lines.append(f"  Side-Feeding Cascade Delay:       tau_sf     = {lt['side_feeding_tau_ps']:.3f} ps")
    lines.append(f"  Uncorrected Prompt Lifetime:      tau_raw    = {lt['tau_raw_ps']:.3f} ps ({lt['tau_raw_ps']*1000.0:.1f} fs)")
    lines.append(f"  Inverted Intrinsic Level Lifetime: tau_level  = {lt['tau_level_ps']:.3f} +/- {lt['sigma_tau_ps']:.3f} ps")
    lines.append(f"                                              = {lt['tau_level_fs']:.1f} +/- {lt['sigma_tau_fs']:.1f} fs")
    lines.append("\n[2] Transition Probability & Deformation:")
    lines.append(f"  E_gamma:                          {tp['E_gamma_keV']:.1f} keV (I_i = {tp['spin_initial']:.1f} -> I_f = {tp['spin_initial']-2.0:.1f})")
    lines.append(f"  B(E2; I -> I-2):                  {tp['B_E2_e2b2']:.4f} e^2 b^2 ({tp['B_E2_W_u']:.1f} W.u.)")
    lines.append(f"  Intrinsic Quadrupole Moment Q_0:  {tp['intrinsic_quadrupole_moment_Q0_eb']:.2f} e*b")
    lines.append("-" * 78)
    lines.append("Methodology & Evidence Boundary:")
    lines.append("  Side-feeding is evaluated using Bateman population convolution; nuclear scattering")
    lines.append("  is computed via Blaugrund angular deflection <cos(phi)>(t).")
    lines.append("  Stopping power parameters are scaled to target backing density.")
    lines.append("=" * 78)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="In-Beam DSAM Stopping Lifetime Inverter")
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Preset configuration")
    parser.add_argument("--f-exp", type=float, help="Experimental F(tau) factor")
    parser.add_argument("--f-err", type=float, default=0.04, help="Uncertainty on F(tau)")
    parser.add_argument("--tau-sf", type=float, help="Side-feeding delay time in ps")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON format")
    args = parser.parse_args()

    cfg = PRESETS["130Ba_8plus_in_Au_backing"].copy()
    if args.preset:
        cfg = PRESETS[args.preset].copy()
    if args.f_exp is not None:
        cfg["F_experimental"] = args.f_exp
    if args.f_err is not None:
        cfg["F_uncertainty"] = args.f_err
    if args.tau_sf is not None:
        cfg["side_feeding_tau_ps"] = args.tau_sf

    res = run_dsam_zbl_analysis(
        recoil_nucleus=cfg.get("recoil_nucleus", "Generic"),
        Ar=cfg["Ar"], Zr=cfg["Zr"],
        As=cfg["As"], Zs=cfg["Zs"],
        density_g_cm3=cfg["stopper_density_g_cm3"],
        beta_0=cfg["beta_0"],
        E_gamma_keV=cfg["E_gamma_keV"],
        spin_initial=cfg["spin_initial"],
        F_experimental=cfg["F_experimental"],
        F_uncertainty=cfg["F_uncertainty"],
        side_feeding_tau_ps=cfg.get("side_feeding_tau_ps", 0.0)
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=f"Preset: {args.preset or '130Ba_8plus_in_Au_backing'} ({cfg['description']})"))


if __name__ == "__main__":
    main()
