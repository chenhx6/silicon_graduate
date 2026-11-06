#!/usr/bin/env python3
"""
Parameterized fixed-frequency shape-coexistence Routhian demonstration.

A polynomial background and user-specified Gaussian valleys define E0(beta,gamma).
Numerically u=hbar*omega is in MeV and J_tilde=J_x/hbar^2 is in
MeV^-1, so the rotational Routhian term is -0.5*J_tilde*u^2. It is a
fixed-frequency Routhian after a simple rotor Legendre transform, not
fixed-I total energy. A crossing in that surface alone does not establish
a first-order quantum shape transition, wobbling, chirality or an observed
nuclear minimum. No Nilsson spectrum, Strutinsky smoothing or HFB is solved.

The valley coordinates, deformation-dependent inertia and isotope-named
presets are illustrative inputs. Their particular coefficients and nuclear
assignments have not been derived from Bohr--Mottelson or independently
validated against experiment. The existing synthetic_model_benchmark labels
apply to the complete calculation. Legacy field names are retained for callers.
"""

import sys
import json
import argparse
import numpy as np
from scipy.optimize import minimize

PRESETS = {
    "130Ba_triaxial_oblate_coexistence": {
        "nucleus": "130Ba (synthetic benchmark)",
        "description": "130Ba (Z=56, N=74) triaxial-oblate shape coexistence driving high-spin wobbling",
        "data_kind": "synthetic_model_benchmark",
        "C2": 15.0,  # MeV
        "C3": -8.0,  # MeV
        "C4": 25.0,  # MeV
        "J0": 34.0,  # MeV^-1 hbar^2
        "beta0": 0.20,
        "shell_minima": [
            {"name": "Triaxial-Min", "beta": 0.24, "gamma_deg": 24.0, "depth_MeV": -2.6, "w_beta": 0.08, "w_gamma_deg": 12.0},
            {"name": "Oblate-Min",   "beta": 0.17, "gamma_deg": 58.0, "depth_MeV": -2.8, "w_beta": 0.07, "w_gamma_deg": 10.0}
        ],
        "eval_frequencies_MeV": [0.0, 0.15, 0.25, 0.35, 0.45]
    },
    "76Kr_prolate_oblate_coexistence": {
        "nucleus": "76Kr (synthetic benchmark)",
        "description": "76Kr (Z=36, N=40) classic large-amplitude prolate-oblate shape coexistence",
        "data_kind": "synthetic_model_benchmark",
        "C2": 12.0,
        "C3": -10.0,
        "C4": 22.0,
        "J0": 22.0,
        "beta0": 0.22,
        "shell_minima": [
            {"name": "Prolate-Min", "beta": 0.35, "gamma_deg": 6.0,  "depth_MeV": -3.2, "w_beta": 0.10, "w_gamma_deg": 15.0},
            {"name": "Oblate-Min",  "beta": 0.20, "gamma_deg": 56.0, "depth_MeV": -3.4, "w_beta": 0.08, "w_gamma_deg": 12.0}
        ],
        "eval_frequencies_MeV": [0.0, 0.15, 0.25, 0.35, 0.45]
    },
    "186Pb_triple_shape_coexistence": {
        "nucleus": "186Pb (synthetic benchmark)",
        "description": "186Pb (Z=82, N=104) exotic shape coexistence (oblate ground state, prolate/triaxial intruder)",
        "data_kind": "synthetic_model_benchmark",
        "C2": 25.0,
        "C3": -12.0,
        "C4": 40.0,
        "J0": 48.0,
        "beta0": 0.20,
        "shell_minima": [
            {"name": "Triaxial/Prolate", "beta": 0.28, "gamma_deg": 15.0, "depth_MeV": -3.6, "w_beta": 0.08, "w_gamma_deg": 12.0},
            {"name": "Oblate-Min",       "beta": 0.17, "gamma_deg": 56.0, "depth_MeV": -3.8, "w_beta": 0.07, "w_gamma_deg": 10.0}
        ],
        "eval_frequencies_MeV": [0.0, 0.12, 0.22, 0.32, 0.42]
    }
}


class CrankedShapeCoexistencePESEngine:
    def __init__(self, C2=15.0, C3=-8.0, C4=25.0, J0=34.0, beta0=0.20, shell_minima=None):
        self.C2 = float(C2)
        self.C3 = float(C3)
        self.C4 = float(C4)
        self.J0 = float(J0)
        self.beta0 = float(beta0)
        self.shell_minima = shell_minima or []

    def potential_routhian(self, beta, gamma_rad, omega_MeV):
        """
        Evaluates total collective Routhian E_total(beta, gamma, omega) in MeV.
        beta >= 0.01, 0 <= gamma <= pi/3.
        """
        b = max(0.01, float(beta))
        g = float(gamma_rad)

        # Macroscopic liquid-drop energy:
        E_ldm = self.C2 * (b**2) + self.C3 * (b**3) * np.cos(3.0 * g) + self.C4 * (b**4)

        # Microscopic shell correction:
        delta_U = 0.0
        for sm in self.shell_minima:
            b_k = sm["beta"]
            g_k = np.radians(sm["gamma_deg"])
            depth = sm["depth_MeV"]
            w_b = sm.get("w_beta", 0.08)
            w_g = np.radians(sm.get("w_gamma_deg", 12.0))
            gauss = depth * np.exp(-0.5 * ((b - b_k) / w_b)**2 - 0.5 * ((g - g_k) / w_g)**2)
            delta_U += gauss

        # Deformation-dependent moment of inertia J_x along the intermediate axis:
        def_factor = (b / self.beta0)**1.5
        axis_factor = 1.0 - 0.5 * np.cos(g - 4.0 * np.pi / 3.0)
        J_x = self.J0 * def_factor * axis_factor

        E_rot = - 0.5 * J_x * (omega_MeV**2)

        return float(E_ldm + delta_U + E_rot)

    def find_coexisting_minima(self, omega_MeV=0.0):
        """
        Locates the two primary coexisting shape minima (Min 1: triaxial/prolate, Min 2: oblate)
        and the intervening barrier along the minimum energy path.
        """
        # Minimum 1: Triaxial / Prolate minimum (gamma ~ 0-35 deg)
        res1 = minimize(lambda p: self.potential_routhian(p[0], p[1], omega_MeV),
                        x0=[0.24, np.radians(22.0)],
                        bounds=[(0.08, 0.55), (0.0, np.radians(35.0))],
                        method='L-BFGS-B')

        # Minimum 2: Oblate minimum (gamma ~ 45-60 deg)
        res2 = minimize(lambda p: self.potential_routhian(p[0], p[1], omega_MeV),
                        x0=[0.17, np.radians(57.0)],
                        bounds=[(0.08, 0.55), (np.radians(45.0), np.radians(60.0))],
                        method='L-BFGS-B')

        v1 = float(res1.fun)
        v2 = float(res2.fun)

        # 1D ridge path between Min 1 and Min 2 to locate the true saddle barrier:
        b1, g1 = res1.x[0], res1.x[1]
        b2, g2 = res2.x[0], res2.x[1]

        s_vals = np.linspace(0.0, 1.0, 60)
        b_path = (1.0 - s_vals) * b1 + s_vals * b2
        g_path = (1.0 - s_vals) * g1 + s_vals * g2
        v_path = [self.potential_routhian(b, g, omega_MeV) for b, g in zip(b_path, g_path)]

        idx_max = int(np.argmax(v_path))
        v_sad = float(v_path[idx_max])
        b_sad = float(b_path[idx_max])
        g_sad = float(g_path[idx_max])

        barrier1 = max(0.0, v_sad - v1)
        barrier2 = max(0.0, v_sad - v2)

        return {
            "omega_MeV": float(omega_MeV),
            "minimum_1": {
                "name": "Triaxial/Prolate",
                "beta": float(res1.x[0]),
                "gamma_deg": float(np.degrees(res1.x[1])),
                "energy_MeV": v1
            },
            "minimum_2": {
                "name": "Oblate",
                "beta": float(res2.x[0]),
                "gamma_deg": float(np.degrees(res2.x[1])),
                "energy_MeV": v2
            },
            "saddle_point": {
                "beta": b_sad,
                "gamma_deg": float(np.degrees(g_sad)),
                "energy_MeV": v_sad
            },
            "energy_difference_E2_minus_E1_MeV": float(v2 - v1),
            "barrier_height_from_min1_MeV": float(barrier1),
            "barrier_height_from_min2_MeV": float(barrier2),
            "yrast_shape": "Triaxial/Prolate" if v1 < v2 else "Oblate"
        }

    def evaluate_frequency_evolution(self, frequencies_MeV):
        """
        Traces the shape coexistence minima across cranking frequencies and detects shape crossing.
        """
        evol = [self.find_coexisting_minima(om) for om in frequencies_MeV]

        # Check for shape crossing: sign change in (v2 - v1)
        diffs = [pt["energy_difference_E2_minus_E1_MeV"] for pt in evol]
        omega_cross = None
        for i in range(len(diffs) - 1):
            if diffs[i] * diffs[i+1] <= 0:
                w1, w2 = frequencies_MeV[i], frequencies_MeV[i+1]
                d1, d2 = diffs[i], diffs[i+1]
                if abs(d2 - d1) > 1e-6:
                    omega_cross = float(w1 - d1 * (w2 - w1) / (d2 - d1))
                else:
                    omega_cross = float(w1)
                break

        return {
            "analysis_kind": "phenomenological_pes_model",
            "data_kind": "synthetic_model_benchmark",
            "frequency_evolution": evol,
            "critical_crossing_frequency_omega_cross_MeV": omega_cross,
            "has_shape_transition": bool(omega_cross is not None),
            "methodological_boundary": "Phenomenological 2D collective PES; does not replace microscopic HFB/CDFT calculations"
        }


def run_shape_coexistence_pes_analysis(nucleus="Generic", C2=15.0, C3=-8.0, C4=25.0,
                                       J0=34.0, beta0=0.20, shell_minima=None,
                                       frequencies_MeV=None):
    if frequencies_MeV is None:
        frequencies_MeV = [0.0, 0.15, 0.25, 0.35, 0.45]
    engine = CrankedShapeCoexistencePESEngine(
        C2=C2, C3=C3, C4=C4, J0=J0, beta0=beta0, shell_minima=shell_minima
    )
    res = engine.evaluate_frequency_evolution(frequencies_MeV)
    res["nucleus"] = nucleus
    return res


def format_text_report(output, title="Cranked Triaxial Shape Coexistence PES Engine"):
    lines = []
    lines.append("=" * 78)
    lines.append(f"  {title}")
    lines.append("=" * 78)
    lines.append(f"Nucleus: {output.get('nucleus', 'Generic')} | Model Type: 2D Phenomenological PES")
    cross_str = f"{output['critical_crossing_frequency_omega_cross_MeV']:.3f} MeV/hbar" if output['has_shape_transition'] else "None (Single Yrast Shape across range)"
    lines.append(
        "Shape Crossing Status:        "
        f"{'Model crossing detected in the evaluated range' if output['has_shape_transition'] else 'No crossing in evaluated range'}"
    )
    lines.append(f"Critical Crossing Frequency:  omega_cross = {cross_str}")
    lines.append("\n[1] Dynamic Evolution of Coexisting Minima vs. Cranking Frequency:")
    lines.append("  omega (MeV)   Min 1 (Triax/Prol)       Min 2 (Oblate)         Delta E (MeV)  Yrast State")
    lines.append("  -----------------------------------------------------------------------------------------")
    for pt in output["frequency_evolution"]:
        m1 = pt["minimum_1"]
        m2 = pt["minimum_2"]
        diff = pt["energy_difference_E2_minus_E1_MeV"]
        yrast = pt["yrast_shape"]
        lines.append(f"     {pt['omega_MeV']:4.2f}       b={m1['beta']:.2f}, g={m1['gamma_deg']:4.1f} deg     b={m2['beta']:.2f}, g={m2['gamma_deg']:4.1f} deg      {diff:+6.3f}     {yrast}")
    lines.append("-" * 78)
    lines.append("Methodology & Evidence Boundary:")
    lines.append("  Rotational Coriolis energy -0.5*J_x*omega^2 preferentially lowers the triaxial")
    lines.append("  minimum because intermediate-axis rotation has the maximal collective moment of inertia.")
    lines.append(
        "  This illustrates a spin-dependent minimum crossing in the supplied "
        "phenomenological PES; it does not demonstrate a nucleus-specific "
        "spin-stabilized triaxiality mechanism."
    )
    lines.append("==============================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Cranked Shape Coexistence PES Engine")
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Preset configuration")
    parser.add_argument("--omega", type=float, help="Single cranking frequency to evaluate (MeV)")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON format")
    args = parser.parse_args()

    cfg = PRESETS["130Ba_triaxial_oblate_coexistence"].copy()
    if args.preset:
        cfg = PRESETS[args.preset].copy()

    if args.omega is not None:
        freqs = [args.omega]
    else:
        freqs = cfg.get("eval_frequencies_MeV", [0.0, 0.15, 0.25, 0.35, 0.45])

    res = run_shape_coexistence_pes_analysis(
        nucleus=cfg.get("nucleus", "Generic"),
        C2=cfg["C2"], C3=cfg["C3"], C4=cfg["C4"],
        J0=cfg["J0"],
        beta0=cfg.get("beta0", 0.20),
        shell_minima=cfg.get("shell_minima"),
        frequencies_MeV=freqs
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=f"Preset: {args.preset or '130Ba_triaxial_oblate_coexistence'} ({cfg['description']})"))


if __name__ == "__main__":
    main()
