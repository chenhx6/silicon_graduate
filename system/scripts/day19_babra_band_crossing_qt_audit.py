#!/usr/bin/env python3
"""Quantitative audit of Babra 2019 Table I: 136Sm band-crossing Qt evolution.

Audits the pre-crossing (8+, 10+, 12+) vs post-crossing (14+, 16+, 18+) transition quadrupole
moments, evaluates the -10.3% drop in Qt (z = -2.45 sigma) and -19.5% drop in B(E2),
proves stopping-power scale invariance, and models two-band mixing vs side-feeding alternatives.
Uses only the Python standard library. Requires --output PATH.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path


def weighted_mean(values, sigmas):
    weights = [1.0 / (s ** 2) for s in sigmas]
    w_sum = sum(weights)
    mean_val = sum(w * v for w, v in zip(weights, values)) / w_sum
    sig_val = 1.0 / math.sqrt(w_sum)
    return mean_val, sig_val


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Path for output JSON")
    args = parser.parse_args()

    checks = []
    def check(name, condition):
        checks.append({"name": name, "passed": bool(condition)})
        if not condition:
            raise AssertionError(f"Check failed: {name}")

    # 1. Babra 2019 Table I data for 136Sm
    table1 = [
        {"spin": "8+",  "I": 8,  "E_gamma_keV": 576, "tau_ps": 1.23, "sig_tau": 0.08, "qt_eb": 5.66, "sig_qt_plus": 0.19, "sig_qt_minus": 0.19, "mean_sig_qt": 0.19},
        {"spin": "10+", "I": 10, "E_gamma_keV": 614, "tau_ps": 0.89, "sig_tau": 0.25, "qt_eb": 5.59, "sig_qt_plus": 0.78, "sig_qt_minus": 0.79, "mean_sig_qt": 0.785},
        {"spin": "12+", "I": 12, "E_gamma_keV": 676, "tau_ps": 0.52, "sig_tau": 0.04, "qt_eb": 5.70, "sig_qt_plus": 0.21, "sig_qt_minus": 0.20, "mean_sig_qt": 0.205},
        {"spin": "14+", "I": 14, "E_gamma_keV": 735, "tau_ps": 0.38, "sig_tau": 0.05, "qt_eb": 5.38, "sig_qt_plus": 0.34, "sig_qt_minus": 0.33, "mean_sig_qt": 0.335},
        {"spin": "16+", "I": 16, "E_gamma_keV": 774, "tau_ps": 0.36, "sig_tau": 0.05, "qt_eb": 4.85, "sig_qt_plus": 0.34, "sig_qt_minus": 0.32, "mean_sig_qt": 0.330},
        {"spin": "18+", "I": 18, "E_gamma_keV": 841, "tau_ps": 0.22, "sig_tau": 0.03, "qt_eb": 5.05, "sig_qt_plus": 0.37, "sig_qt_minus": 0.33, "mean_sig_qt": 0.350},
    ]

    check("Table I contains 6 finite fitted states", len(table1) == 6)

    # 2. Pre-crossing (8+, 10+, 12+) vs Post-crossing (14+, 16+, 18+)
    pre_states = table1[:3]
    post_states = table1[3:]

    pre_qt_vals = [s["qt_eb"] for s in pre_states]
    pre_sig_vals = [s["mean_sig_qt"] for s in pre_states]
    mean_pre, sig_pre = weighted_mean(pre_qt_vals, pre_sig_vals)

    post_qt_vals = [s["qt_eb"] for s in post_states]
    post_sig_vals = [s["mean_sig_qt"] for s in post_states]
    mean_post, sig_post = weighted_mean(post_qt_vals, post_sig_vals)

    diff_qt = mean_post - mean_pre
    sig_diff = math.sqrt(sig_pre ** 2 + sig_post ** 2)
    z_diff = diff_qt / sig_diff
    pct_drop_qt = (diff_qt / mean_pre) * 100.0
    pct_drop_be2 = ((mean_post ** 2 / mean_pre ** 2) - 1.0) * 100.0

    check("Pre-crossing mean Qt is ~ 5.68 eb", math.isclose(mean_pre, 5.676, abs_tol=0.01))
    check("Post-crossing mean Qt is ~ 5.09 eb", math.isclose(mean_post, 5.092, abs_tol=0.01))
    check("Qt drop across crossing is -0.584 +- 0.239 eb (-10.3%)",
          math.isclose(diff_qt, -0.584, abs_tol=0.01))
    check("Significance of crossing Qt drop is z = -2.45 sigma (p ~ 0.014)",
          math.isclose(z_diff, -2.45, abs_tol=0.05))
    check("Collective B(E2) drops by ~ -19.5%", math.isclose(pct_drop_be2, -19.51, abs_tol=0.5))

    # 3. Weighted linear regression across all 6 states
    spins = [s["I"] for s in table1]
    all_qts = [s["qt_eb"] for s in table1]
    all_sigs = [s["mean_sig_qt"] for s in table1]
    all_weights = [1.0 / (s ** 2) for s in all_sigs]

    w_sum = sum(all_weights)
    x_bar = sum(w * x for w, x in zip(all_weights, spins)) / w_sum
    y_bar = sum(w * y for w, y in zip(all_weights, all_qts)) / w_sum
    sxx = sum(w * ((x - x_bar) ** 2) for w, x in zip(all_weights, spins))
    sxy = sum(w * (x - x_bar) * (y - y_bar) for w, x, y in zip(all_weights, spins, all_qts))

    slope = sxy / sxx
    sig_slope = 1.0 / math.sqrt(sxx)
    z_slope = slope / sig_slope

    check("Weighted linear regression slope is negative (-0.0716 eb/hbar)",
          math.isclose(slope, -0.0716, abs_tol=0.005))
    check("Known-variance Gaussian significance z is -2.18 sigma",
          math.isclose(z_slope, -2.179, abs_tol=0.02))

    # 4. Stopping power scale invariance proof
    # If stopping power is scaled by factor S_factor = 1.15 (+15%):
    # In DSAM, tau_scale = 1 / 1.15, so Qt_scale = sqrt(1.15)
    s_factor = 1.15
    qt_scale = math.sqrt(s_factor)

    scaled_qts = [q * qt_scale for q in all_qts]
    scaled_sigs = [s * qt_scale for s in all_sigs]
    scaled_weights = [1.0 / (s ** 2) for s in scaled_sigs]

    w_sum_sc = sum(scaled_weights)
    x_bar_sc = sum(w * x for w, x in zip(scaled_weights, spins)) / w_sum_sc
    y_bar_sc = sum(w * y for w, y in zip(scaled_weights, scaled_qts)) / w_sum_sc
    sxx_sc = sum(w * ((x - x_bar_sc) ** 2) for w, x in zip(scaled_weights, spins))
    sxy_sc = sum(w * (x - x_bar_sc) * (y - y_bar_sc) for w, x, y in zip(scaled_weights, spins, scaled_qts))

    slope_sc = sxy_sc / sxx_sc
    sig_slope_sc = 1.0 / math.sqrt(sxx_sc)
    z_slope_sc = slope_sc / sig_slope_sc

    check("Stopping scale scales slope by exactly sqrt(1.15)",
          math.isclose(slope_sc, slope * qt_scale, rel_tol=1e-12))
    check("Standardized z-statistic is strictly invariant under uniform stopping scaling",
          math.isclose(z_slope_sc, z_slope, rel_tol=1e-12))

    # 5. Two-band mixing model at crossing (12+ -> 14+)
    # Ground band Q0_g = 5.68 eb, S-band Q0_s = 5.20 eb
    # At I=12, mixing is 50-50: alpha12 = 1/sqrt(2), beta12 = 1/sqrt(2)
    # At I=14, S-band dominates: beta14 = 0.90, alpha14 = sqrt(1 - 0.90^2) = 0.4359
    # Transition matrix element: <14|E2|12> = alpha14*alpha12*Q0_g + beta14*beta12*Q0_s
    alpha12, beta12 = 1.0 / math.sqrt(2.0), 1.0 / math.sqrt(2.0)
    beta14 = 0.90
    alpha14 = math.sqrt(1.0 - beta14 ** 2)
    q_eff_mixing_14_12 = alpha14 * alpha12 * mean_pre + beta14 * beta12 * 5.20

    check("Two-band mixing naturally yields intermediate Qt = 5.06 eb, matching observed 5.38(34) eb",
          abs(q_eff_mixing_14_12 - 5.38) < 0.35)

    result = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Babra 2019 Table I 136Sm band-crossing Qt evolution and stopping invariance audit",
        "pre_crossing_group_8_10_12": {
            "mean_qt_eb": mean_pre,
            "sig_mean_qt_eb": sig_pre,
            "states": pre_states,
        },
        "post_crossing_group_14_16_18": {
            "mean_qt_eb": mean_post,
            "sig_mean_qt_eb": sig_post,
            "states": post_states,
        },
        "crossing_evolution_statistics": {
            "diff_qt_eb": diff_qt,
            "sig_diff_eb": sig_diff,
            "z_significance": z_diff,
            "p_value_two_tailed": 2.0 * (1.0 - 0.5 * (1.0 + math.erf(abs(z_diff) / math.sqrt(2.0)))),
            "percentage_drop_qt": pct_drop_qt,
            "percentage_drop_be2": pct_drop_be2,
            "conclusion": "Qt drops by -10.3% (z = -2.45 sigma, p = 0.014) across the crossing, corresponding to a -19.5% reduction in B(E2)",
        },
        "weighted_linear_regression": {
            "slope_eb_per_hbar": slope,
            "sig_slope_eb_per_hbar": sig_slope,
            "gaussian_z": z_slope,
            "scale_invariance_verified": True,
            "insight": "Uniform stopping power errors change absolute Qt scale but cannot fake or erase the negative slope",
        },
        "competing_interpretations_matrix": {
            "hypothesis_1_shape_evolution": "Babra model: core changes from gamma-soft (beta2 ~ 0.30, gamma ~ 0 deg) to stable triaxial (beta2 ~ 0.22, gamma ~ -25 deg)",
            "hypothesis_2_two_band_mixing": f"Wave function mixing between ground band and S-band depresses effective E2 matrix element to {q_eff_mixing_14_12:.2f} eb without static shape change",
            "hypothesis_3_side_feeding_bias": "8+ gated from above (0% side-feeding), 14+-18+ gated from below (25% side-feeding); slow feeding could simulate apparent lifetime elongation",
        },
        "checks": checks,
        "check_count": len(checks),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"Babra band-crossing audit completed: {len(checks)} checks passed.")
    print(f"Pre-crossing Qt: {mean_pre:.3f} +- {sig_pre:.3f} eb vs Post-crossing Qt: {mean_post:.3f} +- {sig_post:.3f} eb")
    print(f"Qt drop: {diff_qt:.3f} +- {sig_diff:.3f} eb (-{abs(pct_drop_qt):.2f}%, z = {z_diff:.2f} sigma)")
    print(f"Stopping scale invariance verified: z = {z_slope:.3f} is strictly conserved.")


if __name__ == "__main__":
    main()
