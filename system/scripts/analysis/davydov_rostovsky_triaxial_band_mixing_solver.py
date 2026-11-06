#!/usr/bin/env python3
"""Legacy rostovsky interface for conditional Mikhailov strength inversion.

This is not a Davydov–Rostovsky Hamiltonian solver. Its legacy parameter t
obeys R=.7*((1-2*t)/(1+t))**2: a2=t/[2(1+t)], BM z2=t/(1-t).
The historical attribution and h2/softness interpretation are withdrawn.
BM-II §4-4, Eqs.4-230–4-235 supplies the strength contract only.
"""
import json
import math
import argparse
from gamma_band_mixing_z_gamma_alaga_inverter import invert_z_gamma_from_branching


PRESETS = {
    "152Sm_classic_transitional_nucleus": {
        "description": "Unverified legacy 152Sm numerical fixture",
        "nucleus": "152Sm",
        "E_2g_keV": 121.78,
        "E_4g_keV": 366.5,
        "E_2gamma_keV": 1085.87,
        "E_0beta_keV": 684.7,
        "exp_be2_gamma_ratio": 0.540
    },
    "130Ba_gamma_soft_triaxial": {
        "description": "Unverified legacy 130Ba numerical fixture (R = 0.485)",
        "nucleus": "130Ba",
        "E_2g_keV": 357.2,
        "E_4g_keV": 908.1,
        "E_2gamma_keV": 1187.5,
        "E_0beta_keV": 890.0,
        "exp_be2_gamma_ratio": 0.485
    },
    "rigid_rotor_zero_mixing_limit": {
        "description": "Zero-a2 algebraic reference (no mechanism identification) (R_exp = 0.700, z_gamma = 0)",
        "nucleus": "Rigid-Rotor-Ref",
        "E_2g_keV": 100.0,
        "E_4g_keV": 333.3,
        "E_2gamma_keV": 1200.0,
        "E_0beta_keV": 1500.0,
        "exp_be2_gamma_ratio": 0.700
    }
}



def invert_gamma_mixing_parameter(exp_ratio):
    """Legacy scalar t on +sqrt branch; all branches are in calculate_*.

    t is dimensionless, not BM z2, epsilon2, or a wavefunction amplitude.
    """
    res = invert_z_gamma_from_branching(exp_ratio)
    return res["branches"][0]["legacy_rostovsky_z_gamma"]


def calculate_davydov_rostovsky_parameters(E_2g, E_2gamma, E_0beta, exp_ratio):
    """Compatibility API; no unique coupling or softness is inferred."""
    if not math.isfinite(E_0beta) or E_0beta <= 0:
        raise ValueError("E_0beta must be finite and positive (keV)")
    res = invert_z_gamma_from_branching(exp_ratio, E_2gamma, E_2g)
    primary = res["branches"][0]
    return {
        "alaga_unperturbed_ratio": 0.7,
        "experimental_ratio": exp_ratio,
        "alaga_suppression_pct": -res["alaga_deviation_pct"],
        "z_gamma_mixing_parameter": primary["legacy_rostovsky_z_gamma"],
        "parameter_convention": "legacy t = 2*a2/(1-2*a2); BM z2=t/(1-t)",
        "bm_a2": primary["a2"],
        "bm_z2": primary["bm_z2"],
        "branches": res["branches"],
        "branch_selection": res["branch_selection"],
        "coupling_matrix_element_h2_keV": None,
        "non_adiabatic_softness_mu": None,
        "legacy_energy_ratio_fourth_root": (E_2g/E_0beta)**0.25,
        "predicted_ratio_2gamma_to_4g_vs_2g": primary["predicted_B_E2_4g_to_2g_ratio"],
        "interpretation_boundary": "No unique mechanism, h2 or softness from one ratio; energy fourth root is only a numerical proxy",
        "preset_provenance": res["preset_provenance"],
    }


def run_davydov_rostovsky_analysis(nucleus, E_2g, E_4g, E_2gamma, E_0beta, exp_ratio):
    if not math.isfinite(E_4g) or E_4g < 0:
        raise ValueError("E_4g must be finite and nonnegative (keV)")
    return {
        "nucleus": nucleus,
        "experimental_energies_keV": {"E_2g": E_2g, "E_4g": E_4g,
                                      "E_2gamma": E_2gamma, "E_0beta": E_0beta},
        "energy_provenance": "Supplied values; legacy presets are unverified fixtures",
        "mixing_results": calculate_davydov_rostovsky_parameters(E_2g,E_2gamma,E_0beta,exp_ratio),
    }


def format_text_report(res, title="Legacy rostovsky Mikhailov strength interface"):
    m = res["mixing_results"]
    lines = [title, f"Input label: {res['nucleus']}", m["parameter_convention"], m["branch_selection"]]
    for b in m["branches"]:
        lines.append(f"sign={b['amplitude_sign']:+d}: t={b['legacy_rostovsky_z_gamma']} "
                     f"({b['legacy_rostovsky_coordinate']}), a2={b['a2']:.8g}, "
                     f"B(2_gamma->4_g)/B(2_gamma->2_g)={b['predicted_B_E2_4g_to_2g_ratio']:.8g}")
    lines.extend([m["interpretation_boundary"], m["preset_provenance"]])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preset", choices=list(PRESETS))
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if not args.preset:
        return parser.print_help()
    p = PRESETS[args.preset]
    res = run_davydov_rostovsky_analysis(p["nucleus"],p["E_2g_keV"],p["E_4g_keV"],
                                        p["E_2gamma_keV"],p["E_0beta_keV"],p["exp_be2_gamma_ratio"])
    print(json.dumps(res, indent=2, allow_nan=False) if args.json else format_text_report(res))


if __name__ == "__main__":
    main()
