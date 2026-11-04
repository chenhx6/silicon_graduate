#!/usr/bin/env python3
"""
Odd-A Transverse vs. Longitudinal Wobbling Stability Boundary & Bifurcation Solver.

Physical Principle & Formalism:
In odd-A triaxially deformed nuclei, a high-j valence quasiparticle couples to a triaxial
rotor core. Following the Lund convention for the triaxiality parameter gamma in (0, 60 deg),
the principal axes of the intrinsic density and inertia distributions are:
  - Axis 1 = Short axis (s)
  - Axis 2 = Intermediate / Medium axis (m)
  - Axis 3 = Long axis (l)

The moments of inertia obey the fundamental ordering:
  J_m > J_s > J_l    (i.e. A_m < A_s < A_l where A_k = 1 / (2 * J_k))
such that collective core rotation preferentially takes place around the intermediate axis (m).

1. Transverse Wobbling (TW) [Frauendorf & Donau, PRC 89, 014322 (2014)]:
   The valence quasiparticle aligns along the short axis (s), perpendicular to the collective
   rotation axis (m).
   Under the Harmonic Frozen Alignment (HFA) approximation [Frauendorf 2025, Ch. 2, Eq. (2.20)]:
     hbar * omega_w_TW = 2 * I * sqrt( (A_m - A_s_bar(I)) * (A_l - A_s_bar(I)) )
   where the effective rotational parameter A_s_bar is attenuated by particle alignment:
     A_s_bar(I) = A_s * (1 - j_eff / I)
   Expressed directly in terms of moments of inertia:
     hbar * omega_w_TW = sqrt( [ I / J_m - (I - j_eff) / J_s ] * [ I / J_l - (I - j_eff) / J_s ] )

   Because J_m > J_s > J_l, the second factor [ I / J_l - (I - j_eff) / J_s ] is strictly positive
   for all I >= j_eff.
   The first factor [ I / J_m - (I - j_eff) / J_s ] starts positive at I = j_eff, but decreases
   monotonically as spin I increases, causing the wobbling excitation energy to DECREASE with spin:
     d(hbar * omega_w_TW) / dI < 0   (Characteristic signature of Transverse Wobbling)

   Critical Instability & Bifurcation to Tilted Precession (TiP):
   The first factor reaches zero at the critical spin I_c:
     I_c = j_eff / (1 - J_s / J_m)
   At I = I_c, the harmonic TW mode softens to zero frequency (omega_w -> 0).
   For I > I_c, the harmonic mode becomes dynamically unstable (omega_w^2 < 0), and the
   classical precession orbit bifurcates into the flip mode (FM) or tilted precession (TiP),
   eventually approaching longitudinal wobbling (LW) at very high spins.

   Nuclear Inertia Paradigms:
   - Hydrodynamic (Irrotational) Flow [Bohr-Mottelson Vol. II, Eq. (6B-17)]:
     J_m = J_0 * sin^2(gamma - 120 deg), J_s = J_0 * sin^2(gamma + 120 deg), J_l = J_0 * sin^2(gamma).
     At gamma ~ 20-26 deg, J_s / J_m ~ 0.30 - 0.38, yielding a very low I_c ~ 8 - 9 hbar.
     Pure hydrodynamic inertia thus predicts premature instability at the band head for 135Pr (j=11/2).
   - Rigid-Body / Pairing-Quenched (CAP) Inertia:
     Pairing correlations are quenched with spin, raising J_s / J_m to ~ 0.60 - 0.75.
     This expands I_c to 14 - 22 hbar, stabilizing harmonic TW across the experimentally observed band!

2. Longitudinal Wobbling (LW):
   The high-j quasiparticle aligns along the intermediate axis (m), parallel to core rotation.
     hbar * omega_w_LW = sqrt( [ I / J_s - (I - j_eff) / J_m ] * [ I / J_l - (I - j_eff) / J_m ] )
   Both factors are strictly positive and increase with spin:
     d(hbar * omega_w_LW) / dI > 0   (Signature of Longitudinal Wobbling, e.g. 187Au)

3. Electromagnetic Transition Signature:
   Within the harmonic approximation well below I_c:
     B(E2_out) / B(E2_in) approx (1 / I) * (1 / (J_m * omega_w)) * [1 + sqrt(J_s / J_l)]^2 / 2
   which scales inversely with spin I.

Textbook & Literature References:
- Bohr & Mottelson, "Nuclear Structure", Vol. II, §4-5e (pp. 190-193), App. 6B (Eq. 6B-17)
- C. M. Petrache (Ed.), "Chirality and Wobbling in Atomic Nuclei" (CRC Press 2025):
  * Ch. 2: S. Frauendorf, "Wobbling motion in triaxial nuclei", pp. 24-61 (Eqs. 2.20-2.21)
  * Ch. 5: S. Guo & B. F. Lv, "Recent experimental results on chirality and wobbling", pp. 91-107
  * Ch. 6: E. A. Lawrie, "Tilted precession and wobbling in triaxial nuclei", pp. 108-136
- Frauendorf & Donau, Phys. Rev. C 89, 014322 (2014)
- Tanabe & Sugawara-Tanabe, Phys. Rev. C 95, 064315 (2017)
- Sensharma et al., Phys. Rev. Lett. 124, 052501 (2020)
- Lv et al., Phys. Rev. Lett. 128, 242501 (2022) [Evidence against wobbling in 135Pr]
"""

import sys
import json
import argparse
import numpy as np

PRESETS = {
    "135Pr_transverse_rigid_stable": {
        "nucleus": "135Pr (synthetic model demonstration)",
        "description": "Prototype transverse wobbling with rigid/pairing-quenched inertia (stable up to I_c ~ 14.4 hbar)",
        "data_kind": "synthetic_model_benchmark",
        "wobbling_mode": "TW",
        "inertia_model": "rigid",
        "j_quasiparticle": 5.5,
        "k_coriolis_attenuation": 1.0,
        "gamma_deg": 26.0,
        "moi_m": 21.0,
        "moi_i": 21.0,
        "moi_s": 13.0,
        "moi_l": 4.0,
        "eval_spins": [8.5, 10.5, 12.5]
    },
    "135Pr_transverse_hydro_unstable": {
        "nucleus": "135Pr (synthetic hydro demonstration)",
        "description": "Transverse wobbling with hydrodynamic irrotational inertia (exhibits low-spin instability at I_c ~ 8.0 hbar)",
        "data_kind": "synthetic_model_benchmark",
        "wobbling_mode": "TW",
        "inertia_model": "hydrodynamic",
        "j_quasiparticle": 5.5,
        "k_coriolis_attenuation": 1.0,
        "gamma_deg": 26.0,
        "moi_m": 21.0,
        "moi_i": 21.0,
        "eval_spins": [8.5, 10.5, 12.5]
    },
    "105Pd_transverse_odd_neutron": {
        "nucleus": "105Pd (synthetic model demonstration)",
        "description": "Odd-neutron transverse wobbling candidate in A~100 region (nu h11/2 quasiparticle)",
        "data_kind": "synthetic_model_benchmark",
        "wobbling_mode": "TW",
        "inertia_model": "rigid",
        "j_quasiparticle": 5.5,
        "k_coriolis_attenuation": 0.85,
        "gamma_deg": 20.0,
        "moi_m": 32.0,
        "moi_i": 32.0,
        "moi_s": 22.0,
        "moi_l": 7.0,
        "eval_spins": [8.5, 10.5, 12.5, 14.5]
    },
    "187Au_longitudinal_wobbling": {
        "nucleus": "187Au (synthetic model demonstration)",
        "description": "Longitudinal wobbling candidate in A~190 region (pi h9/2 along intermediate axis)",
        "data_kind": "synthetic_model_benchmark",
        "wobbling_mode": "LW",
        "inertia_model": "rigid",
        "j_quasiparticle": 4.5,
        "k_coriolis_attenuation": 1.0,
        "gamma_deg": 20.0,
        "moi_m": 45.0,
        "moi_i": 45.0,
        "moi_s": 28.0,
        "moi_l": 10.0,
        "eval_spins": [11.5, 13.5, 15.5, 17.5]
    }
}


class OddAWobblingStabilitySolver:
    def __init__(self, wobbling_mode="TW", inertia_model="rigid", j_qp=5.5,
                 k_att=1.0, gamma_deg=26.0, moi_m=21.0, moi_s=None, moi_l=None,
                 moi_i=None):
        self.mode = wobbling_mode.upper()
        self.inertia_model = inertia_model.lower()
        self.j = float(j_qp)
        self.k_att = float(k_att)
        self.j_eff = self.j * self.k_att
        self.gamma_deg = float(gamma_deg)
        self.gamma = np.radians(gamma_deg)

        # Handle legacy alias moi_i for moi_m
        effective_moi_m = moi_m if moi_i is None else moi_i

        # Determine relative moments of inertia: J_m, J_s, J_l
        # Following Bohr-Mottelson App. 6B / Frauendorf 2025:
        # J_m (intermediate) > J_s (short) > J_l (long)
        if moi_s is not None and moi_l is not None:
            self.moi_m = float(effective_moi_m)
            self.moi_s = float(moi_s)
            self.moi_l = float(moi_l)
        elif self.inertia_model == "hydrodynamic":
            # Bohr-Mottelson Eq. (6B-17): J_k = 4*B*beta^2 * sin^2(gamma - 2*pi*k / 3)
            # For 0 < gamma < 60 deg:
            # Intermediate axis (m): sin^2(gamma - 120 deg) -> largest (maximum at gamma=30 deg)
            # Short axis (s): sin^2(gamma + 120 deg) -> middle
            # Long axis (l): sin^2(gamma) -> smallest
            jm_hydro = np.sin(self.gamma - 2.0 * np.pi / 3.0)**2
            js_hydro = np.sin(self.gamma + 2.0 * np.pi / 3.0)**2
            jl_hydro = np.sin(self.gamma)**2
            scale = float(effective_moi_m) / max(1e-6, jm_hydro)
            self.moi_m = float(effective_moi_m)
            self.moi_s = scale * js_hydro
            self.moi_l = scale * jl_hydro
        else: # "rigid" or empirical quenched
            # When explicit values not provided, use typical pairing-quenched ratios J_s/J_m ~ 0.65, J_l/J_m ~ 0.20
            self.moi_m = float(effective_moi_m)
            self.moi_s = 0.65 * self.moi_m
            self.moi_l = 0.20 * self.moi_m

        # Legacy alias for backward compatibility
        self.moi_i = self.moi_m

        # Critical spin for Transverse Wobbling instability:
        # I_c = j_eff / (1 - J_s / J_m)  [Frauendorf 2025, Eq. 2.21]
        ratio_s_m = self.moi_s / self.moi_m
        denom = 1.0 - ratio_s_m
        if denom > 1e-4:
            self.I_crit = self.j_eff / denom
        else:
            self.I_crit = 999.0

        self.omega_crit = self.I_crit / self.moi_m
        self.R_crit = np.sqrt(max(0.0, self.I_crit**2 - self.j_eff**2))

    def calculate_wobbling_frequency(self, spin):
        """
        Calculate rotational frequency and wobbling excitation energy for a single spin I.
        """
        I = float(spin)
        if I < self.j_eff:
            return {
                "spin": I,
                "omega_rot_MeV": 0.0,
                "hbar_omega_w_MeV": 0.0,
                "is_stable": False,
                "stability_status": "spin_below_aligned_particle",
                "BE2_out_in_ratio": 0.0
            }

        if self.mode == "TW":
            # Transverse Wobbling:
            # term1 = I / J_m - (I - j_eff) / J_s
            # term2 = I / J_l - (I - j_eff) / J_s
            omega_rot = I / self.moi_m
            term1 = I / self.moi_m - (I - self.j_eff) / self.moi_s
            term2 = I / self.moi_l - (I - self.j_eff) / self.moi_s

            prod = term1 * term2
            if prod > 0.0 and term1 > 0.0 and term2 > 0.0:
                hbar_omega_w = float(np.sqrt(prod))
                is_stable = True
                stability_status = "stable_harmonic"
            elif abs(prod) <= 1.0e-14:
                hbar_omega_w = 0.0
                is_stable = False
                stability_status = "critical_softening"
            else:
                hbar_omega_w = 0.0
                is_stable = False
                stability_status = "HFA_unstable_requires_full_model"

            # B(E2_out)/B(E2_in) transition probability ratio:
            # Scales as (1 / I) * [1 / (J_m * omega_w)] * [1 + sqrt(J_s / J_l)]^2 / 2
            if is_stable and hbar_omega_w > 1e-3:
                geo_factor = 0.5 * (1.0 + np.sqrt(self.moi_s / self.moi_l))**2
                be2_ratio = float((1.0 / (I * self.moi_m * hbar_omega_w)) * geo_factor)
            else:
                be2_ratio = 0.0

        else: # "LW"
            # Longitudinal Wobbling:
            omega_rot = I / self.moi_m
            term1 = I / self.moi_s - (I - self.j_eff) / self.moi_m
            term2 = I / self.moi_l - (I - self.j_eff) / self.moi_m

            prod = term1 * term2
            if prod > 0.0 and term1 > 0.0 and term2 > 0.0:
                hbar_omega_w = float(np.sqrt(prod))
                is_stable = True
                stability_status = "stable_harmonic"
            elif abs(prod) <= 1.0e-14:
                hbar_omega_w = 0.0
                is_stable = False
                stability_status = "critical_softening"
            else:
                hbar_omega_w = 0.0
                is_stable = False
                stability_status = "HFA_unstable_requires_full_model"

            if is_stable and hbar_omega_w > 1e-3:
                geo_factor = 0.5 * (1.0 + np.sqrt(self.moi_m / self.moi_l))**2
                be2_ratio = float((1.0 / (I * self.moi_s * hbar_omega_w)) * geo_factor)
            else:
                be2_ratio = 0.0

        return {
            "spin": I,
            "omega_rot_MeV": float(omega_rot),
            "omega_rot_definition": "I / J_m (total-spin cranking proxy; not a separately inferred core frequency)",
            "hbar_omega_w_MeV": float(hbar_omega_w),
            "is_stable": is_stable,
            "stability_status": stability_status,
            "BE2_out_in_ratio": float(be2_ratio)
        }

    def evaluate_spin_series(self, spins):
        """
        Evaluate full spin trajectory, frequency slope, and stability diagnostics.
        """
        results = [self.calculate_wobbling_frequency(s) for s in spins]

        # Calculate slope d(hbar * omega_w) / dI for stable points
        valid_pts = [r for r in results if r["is_stable"]]
        if len(valid_pts) >= 2:
            sp_arr = np.array([p["spin"] for p in valid_pts])
            om_arr = np.array([p["hbar_omega_w_MeV"] for p in valid_pts])
            slope = float(np.polyfit(sp_arr, om_arr, 1)[0])
        else:
            slope = 0.0

        all_stable = (len(valid_pts) == len(results)) and len(results) > 0

        if self.mode == "TW":
            if all_stable and slope < 0.0:
                diag_str = "Harmonic TW model stable across evaluated spins; d(omega_w)/dI < 0"
            elif any(r["stability_status"] == "critical_softening" for r in results):
                diag_str = (
                    f"Frozen-alignment HFA reaches softening near I_c = "
                    f"{self.I_crit:.1f} hbar; full model required"
                )
            elif any(not r["is_stable"] for r in results):
                diag_str = (
                    f"Frozen-alignment HFA is unstable above its boundary near "
                    f"I_c = {self.I_crit:.1f} hbar; full QTR/TAC treatment required"
                )
            else:
                diag_str = "Anomalous TW slope in model"
        else:
            if all_stable and slope > 0.0:
                diag_str = "Harmonic LW model stable across evaluated spins; d(omega_w)/dI > 0"
            else:
                diag_str = "Anomalous LW slope in model"

        return {
            "analysis_kind": "quantitative_model_descriptors_only",
            "data_kind": "synthetic_model_benchmark",
            "wobbling_mode": self.mode,
            "inertia_model": self.inertia_model,
            "j_qp": self.j,
            "k_coriolis_attenuation": self.k_att,
            "j_eff": self.j_eff,
            "gamma_deg": self.gamma_deg,
            "moments_of_inertia": {
                "moi_m": float(self.moi_m),
                "moi_s": float(self.moi_s),
                "moi_l": float(self.moi_l),
                "moi_i": float(self.moi_m)  # legacy compatibility alias
            },
            "critical_spin_I_crit": float(self.I_crit),
            "critical_frequency_omega_crit_MeV": float(self.omega_crit),
            "frequency_slope_dOmega_dI": slope,
            "is_harmonic_stable": all_stable,
            "mode_confirmed": None,  # Model calculations do not confirm physical modes in real nuclei
            "diagnosis": diag_str,
            "spin_trajectory": results,
            "scientific_context": {
                "TW_hallmark": "d(hbar*omega_w)/dI < 0 and collective inter-band E2 enhancement B(E2_out)/B(E2_in) ~ 1/I",
                "LW_hallmark": "d(hbar*omega_w)/dI > 0 with dominant E2 inter-band transitions",
                "bifurcation_boundary": (
                    f"TW HFA softens to omega_w=0 at I_c = {self.I_crit:.1f} hbar; "
                    "the post-softening branch is not identified by this solver"
                ),
                "controversy_status": "Empirical identification requires mixing ratio delta, linear polarization P_gamma, and lifetime tau; model slope alone does not establish nature of band."
            }
        }


def run_wobbling_stability_analysis(nucleus="Generic", wobbling_mode="TW", inertia_model="rigid",
                                    j_qp=5.5, k_att=1.0, gamma_deg=26.0, moi_m=21.0,
                                    moi_s=None, moi_l=None, moi_i=None, eval_spins=None):
    if eval_spins is None:
        eval_spins = [8.5, 10.5, 12.5]
    effective_moi_m = moi_m if moi_i is None else moi_i
    solver = OddAWobblingStabilitySolver(
        wobbling_mode=wobbling_mode, inertia_model=inertia_model,
        j_qp=j_qp, k_att=k_att, gamma_deg=gamma_deg, moi_m=effective_moi_m,
        moi_s=moi_s, moi_l=moi_l
    )
    res = solver.evaluate_spin_series(eval_spins)
    res["nucleus"] = nucleus
    return res


def format_text_report(output, title="Odd-A Wobbling Stability & Bifurcation Analysis"):
    lines = []
    lines.append("=" * 78)
    lines.append(f"  {title}")
    lines.append("=" * 78)
    lines.append(f"Nucleus: {output.get('nucleus', 'Generic')} | Mode: {output['wobbling_mode']} | Inertia Model: {output['inertia_model'].upper()}")
    lines.append(f"j = {output['j_qp']:.1f} hbar (k_att = {output['k_coriolis_attenuation']:.2f}, j_eff = {output['j_eff']:.2f} hbar), gamma = {output['gamma_deg']:.1f} deg")
    moi = output["moments_of_inertia"]
    lines.append(f"Moments of Inertia: J_m = {moi['moi_m']:.1f}, J_s = {moi['moi_s']:.1f}, J_l = {moi['moi_l']:.1f} hbar^2/MeV")
    lines.append("\n[1] Dynamic Stability Boundaries (Frozen Alignment Harmonic Approximation):")
    lines.append(f"  Critical Bifurcation Spin:        I_c        = {output['critical_spin_I_crit']:.2f} hbar")
    lines.append(f"  Critical Core Frequency:          omega_c    = {output['critical_frequency_omega_crit_MeV']:.3f} MeV/hbar")
    lines.append(f"  Wobbling Frequency Slope:         d(omega)/dI= {output['frequency_slope_dOmega_dI']:+.4f} MeV/hbar")
    lines.append(f"  Model Diagnostic Status:          {output['diagnosis']}")
    lines.append(f"  Mode Confirmation Status:         UNASSESSED (Model descriptor only; requires delta, P_gamma, tau)")
    lines.append("\n[2] Spin Evolution Trajectory:")
    lines.append("   Spin I (hbar)    omega_rot (MeV)    hbar*omega_w (MeV)    B(E2_out)/B(E2_in)    Stability")
    lines.append("   ---------------------------------------------------------------------------------")
    for pt in output["spin_trajectory"]:
        stab_str = pt.get("stability_status", "unknown")
        lines.append(f"       {pt['spin']:4.1f}             {pt['omega_rot_MeV']:6.3f}             {pt['hbar_omega_w_MeV']:6.3f}                {pt['BE2_out_in_ratio']:6.3f}          {stab_str}")
    lines.append("-" * 78)
    lines.append("Evidence Boundary Note:")
    lines.append("  In this frozen-alignment parameterization, TW can soften at I_c = j_eff / (1 - J_s/J_m); the post-softening branch is unresolved here.")
    lines.append("  Competing interpretations (e.g. 135Pr: TW vs SP vs TiP vs IBFM gamma-vibration) remain open.")
    lines.append("=" * 78)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Odd-A Wobbling Stability & Bifurcation Solver")
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Preset configuration")
    parser.add_argument("--mode", choices=["TW", "LW"], help="Wobbling mode (TW or LW)")
    parser.add_argument("--inertia", choices=["rigid", "hydrodynamic"], help="Inertia model")
    parser.add_argument("--spin", type=float, help="Single spin to evaluate")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON format")
    args = parser.parse_args()

    cfg = PRESETS["135Pr_transverse_rigid_stable"].copy()
    if args.preset:
        cfg = PRESETS[args.preset].copy()
    if args.mode:
        cfg["wobbling_mode"] = args.mode
    if args.inertia:
        cfg["inertia_model"] = args.inertia

    if args.spin:
        spins = [args.spin]
    else:
        spins = cfg.get("eval_spins", [8.5, 10.5, 12.5])

    res = run_wobbling_stability_analysis(
        nucleus=cfg.get("nucleus", "Generic"),
        wobbling_mode=cfg["wobbling_mode"],
        inertia_model=cfg.get("inertia_model", "rigid"),
        j_qp=cfg["j_quasiparticle"],
        k_att=cfg.get("k_coriolis_attenuation", 1.0),
        gamma_deg=cfg["gamma_deg"],
        moi_m=cfg.get("moi_m", cfg.get("moi_i", 21.0)),
        moi_s=cfg.get("moi_s", None),
        moi_l=cfg.get("moi_l", None),
        eval_spins=spins
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=f"Preset: {args.preset or '135Pr_transverse_rigid_stable'} ({cfg['description']})"))


if __name__ == "__main__":
    main()
