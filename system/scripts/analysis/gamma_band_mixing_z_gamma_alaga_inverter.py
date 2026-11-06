#!/usr/bin/env python3
"""Conditional Mikhailov strength inversion, BM-II §4-4, Eqs.4-230–4-235.

Legacy z_gamma in this module means a2, not BM z2 or epsilon2.
B=2 M1**2 C**2 (1+a2*Delta)**2. A strength ratio loses amplitude sign;
all real branches are returned. Neither h2 nor a mechanism is identifiable.
"""
import argparse
import json
import math


def calculate_alaga_cg_coefficient(I_gamma: int, I_g: int) -> float:
    """Condon–Shortley <I_gamma,2;2,-2|I_g,0>, integer spins.

    Racah factorial sum; no approximate high-spin fallback. The even-even
    K=0 ground band has only even spins (odd final spins return zero).
    """
    if any(isinstance(x, bool) or not isinstance(x, int) or x < 0
           for x in (I_gamma, I_g)) or I_gamma < 2:
        raise ValueError("Require integer I_gamma >= 2 and I_g >= 0")
    j, J = I_gamma, I_g
    if J % 2 or not abs(j - 2) <= J <= j + 2:
        return 0.0
    f = math.factorial
    pref = math.sqrt((2*J+1)*f(J+j-2)*f(J-j+2)*f(j+2-J)/f(j+J+3))
    pref *= math.sqrt(f(J)**2*f(j-2)*f(j+2)*f(4))
    terms = []
    for k in range(j + 3):
        ds = (k, j+2-J-k, j-2-k, 0-k, J-2+2+k, J-j+2+k)
        if min(ds) >= 0:
            terms.append((-1)**k / math.prod(f(d) for d in ds))
    return pref * math.fsum(terms)


def mikhailov_branch(a2: float, amplitude_sign: int) -> dict:
    """Map a finite a2 to BM z2 and the second module's legacy t.

    None marks an infinite coordinate, never a missing physical branch.
    """
    return {
        "amplitude_sign": amplitude_sign,
        "a2": a2,
        "bm_z2": None if 1-4*a2 == 0 else 2*a2/(1-4*a2),
        "bm_z2_coordinate": "infinite" if 1-4*a2 == 0 else "finite",
        "legacy_rostovsky_z_gamma": None if 1-2*a2 == 0 else 2*a2/(1-2*a2),
        "legacy_rostovsky_coordinate": "infinite" if 1-2*a2 == 0 else "finite",
        "predicted_B_E2_4g_to_2g_ratio": 0.05*(1+14*a2)**2,
        "epsilon2": None,
        "h2_keV": None,
        "validity": "algebraic candidate; weak-mixing validity requires independent evidence",
    }


def invert_z_gamma_from_branching(
    R_exp_B_E2: float, E_2gamma_keV: float = 821.1,
    E_2g_keV: float = 79.8, I_gamma: int = 2
) -> dict:
    """Invert B(2_gamma->0_g)/B(2_gamma->2_g), not a photon ratio.

    Legacy scalar keys select the +sqrt branch by convention only. h2 keys
    are retained as JSON null: epsilon2 and intrinsic moments are missing.
    """
    if I_gamma != 2:
        raise ValueError("This ratio inversion is defined only for I_gamma=2")
    if not math.isfinite(R_exp_B_E2) or R_exp_B_E2 < 0:
        raise ValueError("Branching ratio must be finite and nonnegative")
    if not all(math.isfinite(e) and e >= 0 for e in (E_2gamma_keV, E_2g_keV)):
        raise ValueError("Energies must be finite and nonnegative (keV)")
    q = math.sqrt(R_exp_B_E2 / 0.7)
    signs = (1,) if q == 0 else (1, -1)
    branches = [mikhailov_branch((1-s*q)/6, s) for s in signs]
    primary = branches[0]
    return {
        "I_gamma": I_gamma,
        "experimental_B_E2_ratio": R_exp_B_E2,
        "unperturbed_Alaga_ratio": 0.7,
        "alaga_deviation_pct": (R_exp_B_E2/0.7-1)*100,
        "inverted_z_gamma": primary["a2"],
        "parameter_convention": "legacy z_gamma = BM a2 (dimensionless), not BM z2 or epsilon2",
        "branches": branches,
        "branch_selection": "legacy scalar uses +sqrt; no physical branch selected",
        "rotational_vibrational_h2_keV": None,
        "gamma_ground_band_energy_gap_keV": E_2gamma_keV-E_2g_keV,
        "predicted_B_E2_4g_to_2g_ratio": primary["predicted_B_E2_4g_to_2g_ratio"],
        "structural_classification": "Undetermined from one strength ratio",
        "coupling_boundary": "h2=epsilon2*DeltaE; epsilon2 is not determined by a2 alone",
        "preset_provenance": "Legacy numerical examples are unverified fixtures, not experimental evidence",
    }


def format_text_report(inv_res: dict) -> str:
    lines = ["Mikhailov conditional strength inversion (BM-II §4-4)",
             inv_res["parameter_convention"], inv_res["branch_selection"]]
    for b in inv_res["branches"]:
        lines.append(f"sign={b['amplitude_sign']:+d}: a2={b['a2']:.8g}, BM z2={b['bm_z2']}, "
                     f"B(2_gamma->4_g)/B(2_gamma->2_g)={b['predicted_B_E2_4g_to_2g_ratio']:.8g}")
    lines.extend(["h2 (keV), epsilon2 and structure: undetermined.", inv_res["preset_provenance"]])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ratio", type=float, default=0.540)
    parser.add_argument("--E-gamma-bandhead", type=float, default=821.1)
    parser.add_argument("--E-ground-2plus", type=float, default=79.8)
    fixtures = {"168Er_gamma_band": (0.540,821.1,79.8),
                "166Er_gamma_band": (0.525,785.9,80.6),
                "154Sm_gamma_band": (0.450,1440.0,82.0),
                "130Ba_gamma_soft": (0.320,908.1,357.4)}
    parser.add_argument("--preset", choices=list(fixtures), default=None,
                        help="Unverified legacy numerical fixture")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    r,e,e0 = fixtures[args.preset] if args.preset else (args.ratio,args.E_gamma_bandhead,args.E_ground_2plus)
    res = invert_z_gamma_from_branching(r,e,e0)
    print(json.dumps(res, indent=2, allow_nan=False) if args.json else format_text_report(res))


if __name__ == "__main__":
    main()
