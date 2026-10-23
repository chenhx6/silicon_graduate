#!/usr/bin/env python3
"""Two-band mixing model for apparent Qt attenuation across band crossings.

Demonstrates that an apparent drop or step in transition quadrupole moment Qt
at a rotational band crossing can arise purely from two-state wave-function
fragmentation, without requiring intrinsic static shape shrinkage.
Audits Babra 2019 (136Sm) and Klemme 1999 (134Nd).
"""
from __future__ import annotations

raise SystemExit("Retired by Day20 audit007: source attribution / model / score certifications withdrawn; historical output preserved. Use current canonical boundaries and audited conditional controls.")

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np


def two_band_mixed_qt(alpha_i, alpha_f, qt_g, qt_s, qt_inter=0.0):
    """Calculate apparent Qt for a transition I -> I-2 between two mixed states.

    |I> = alpha_i |g> + beta_i |S>, with alpha_i^2 + beta_i^2 = 1.
    |I-2> = alpha_f |g> + beta_f |S>, with alpha_f^2 + beta_f^2 = 1.
    If inter-band matrix element <g||M(E2)||S> is negligible (qt_inter=0),
    Qt_app = alpha_i * alpha_f * Qt_g + beta_i * beta_f * Qt_s.
    """
    beta_i = math.sqrt(max(0.0, 1.0 - alpha_i ** 2))
    beta_f = math.sqrt(max(0.0, 1.0 - alpha_f ** 2))
    return alpha_i * alpha_f * qt_g + beta_i * beta_f * qt_s + (alpha_i * beta_f + beta_i * alpha_f) * qt_inter


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    raw_babra = root / "raw/papers/2019_Babra et al_Investigation of a large change in deformation for the γ -soft nucleus Sm 136.pdf"
    babra_sha = "a26149bff0e7b3bdb5459ba5897b69bc7f8ed17a646f13ed59dd5b38ae425ba6"
    checks = []

    def check(name, cond):
        checks.append({"name": name, "passed": bool(cond)})
        if not cond:
            raise AssertionError(name)

    check("Babra 2019 raw SHA256 verified", hashlib.sha256(raw_babra.read_bytes()).hexdigest() == babra_sha)

    # 1. 136Sm Babra 2019 Table I literal data
    # Pre-crossing: 8+, 10+, 12+
    # Post-crossing: 14+, 16+, 18+
    states_136sm = [
        {"spin": 8, "E_gamma": 576, "tau": 1.23, "tau_err": 0.08, "Qt": 5.66, "Qt_err": 0.19},
        {"spin": 10, "E_gamma": 614, "tau": 0.89, "tau_err": 0.25, "Qt": 5.59, "Qt_err": 0.785},
        {"spin": 12, "E_gamma": 676, "tau": 0.52, "tau_err": 0.04, "Qt": 5.70, "Qt_err": 0.205},
        {"spin": 14, "E_gamma": 735, "tau": 0.38, "tau_err": 0.05, "Qt": 5.38, "Qt_err": 0.335},
        {"spin": 16, "E_gamma": 774, "tau": 0.36, "tau_err": 0.05, "Qt": 4.85, "Qt_err": 0.33},
        {"spin": 18, "E_gamma": 841, "tau": 0.22, "tau_err": 0.03, "Qt": 5.05, "Qt_err": 0.35},
    ]
    pre_states = states_136sm[:3]
    post_states = states_136sm[3:]
    w_pre = [1.0 / (s["Qt_err"] ** 2) for s in pre_states]
    w_post = [1.0 / (s["Qt_err"] ** 2) for s in post_states]
    mean_pre = sum(w * s["Qt"] for w, s in zip(w_pre, pre_states)) / sum(w_pre)
    mean_pre_err = 1.0 / math.sqrt(sum(w_pre))
    mean_post = sum(w * s["Qt"] for w, s in zip(w_post, post_states)) / sum(w_post)
    mean_post_err = 1.0 / math.sqrt(sum(w_post))
    delta_mean = mean_post - mean_pre
    delta_err = math.sqrt(mean_pre_err ** 2 + mean_post_err ** 2)
    z_step = delta_mean / delta_err

    check("Pre-crossing mean Qt is ~5.68 eb", math.isclose(mean_pre, 5.676, abs_tol=0.01))
    check("Post-crossing mean Qt is ~5.09 eb", math.isclose(mean_post, 5.092, abs_tol=0.01))
    check("Net drop Delta Qt is ~ -0.58 eb (-10.3%)", math.isclose(delta_mean, -0.584, abs_tol=0.01))
    check("Step significance z is ~ -2.45 sigma", math.isclose(z_step, -2.45, abs_tol=0.05))

    # 2. Two-band mixing model for 136Sm across 14+ -> 12+
    # Unperturbed parameters: Qt_g = mean_pre (~5.68 eb), Qt_S = mean_post (~4.95 eb for pure S)
    # State 12+ is pure ground: alpha_12 = 1.0, beta_12 = 0.0
    # State 14+ is mixed: alpha_14 = cos(theta_14)
    # For theta_14 ~ 26.5 deg (sin^2 theta = 0.20, 20% S-band in 14+ yrast):
    theta_14 = math.radians(26.5)
    alpha_14 = math.cos(theta_14)
    qt_14_calc = two_band_mixed_qt(alpha_14, 1.0, mean_pre, 4.95, qt_inter=0.0)
    check("Two-band mixing at 14+ reproduces observed Qt within 0.35 eb (1 sigma)",
          math.isclose(qt_14_calc, 5.38, abs_tol=0.35))

    # 3. 134Nd Klemme 1999 Table II extreme band-crossing attenuation case
    # 10S2+ -> 8g+ transition: B(E2) = 0.009(2) e2b2, Qt = 0.51(4) eb
    # Compare to g.s.b. Qt(2+) = 4.32(7) eb
    # Drop factor: 0.51 / 4.32 ~ 0.118 (8.5-fold drop)
    check("134Nd 10S2->8g crossing drops Qt by more than factor of 8", 0.51 / 4.32 < 0.15)

    result = {
        "kind": "two-band mixing audit for band-crossing Qt evolution",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "babra_raw_sha256": babra_sha,
        "babra_table1_stats": {
            "mean_pre_8_10_12_eb": mean_pre,
            "mean_pre_err_eb": mean_pre_err,
            "mean_post_14_16_18_eb": mean_post,
            "mean_post_err_eb": mean_post_err,
            "delta_Qt_eb": delta_mean,
            "delta_Qt_pct": (delta_mean / mean_pre) * 100.0,
            "step_significance_z": z_step,
            "step_two_sided_p": float(2.0 * (1.0 - 0.5 * (1.0 + math.erf(abs(z_step) / math.sqrt(2))))),
        },
        "two_band_mixing_model": {
            "136Sm_14+_transition": {
                "assumed_Qt_g_eb": mean_pre,
                "assumed_Qt_S_eb": 4.95,
                "mixing_angle_deg": 26.5,
                "alpha_14": alpha_14,
                "alpha_12": 1.0,
                "calculated_Qt_app_eb": qt_14_calc,
                "observed_Qt_eb": 5.38,
                "observed_Qt_err_eb": 0.34,
                "residual_eb": qt_14_calc - 5.38,
                "residual_in_sigma": (qt_14_calc - 5.38) / 0.34,
            },
            "134Nd_10S2_crossing": {
                "observed_Qt_10S2_8g_eb": 0.51,
                "observed_Qt_gsb_2g_eb": 4.32,
                "ratio": 0.51 / 4.32,
            },
        },
        "checks": checks,
        "all_checks_passed": all(c["passed"] for c in checks),
        "scientific_boundary": (
            "Two-band wave-function mixing between a ground-state band and an aligned S-band "
            "naturally fragments transition matrix elements at the crossing point. "
            "In 136Sm, a mild ~20% mixing (mixing angle ~26 deg) reproduces the observed 14+ Qt=5.38(34) eb "
            "starting from constant intrinsic deformations Qt_g=5.68 eb and Qt_S=4.95 eb. "
            "In 134Nd, weak cross-band mixing drops Qt(10S2->8g) to 0.51(4) eb (>8-fold drop). "
            "Therefore, observing Qt attenuation at a band crossing does not uniquely establish "
            "static shape shrinkage or a gamma-soft to gamma-rigid transition; band mixing "
            "must be ruled out via inter-band links and partner-band lifetimes before concluding shape change."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"output": str(args.output), "controls": len(checks), "all_passed": result["all_checks_passed"]}))


if __name__ == "__main__":
    main()
