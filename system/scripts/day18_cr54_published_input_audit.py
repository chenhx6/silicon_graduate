#!/usr/bin/env python3
"""Audit fresh 54Cr published inputs; no reconstruction of original DSAM fits."""
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--contract", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    d = json.loads(a.contract.read_text())
    checks, rows = [], []

    def check(name, condition, **values):
        checks.append({"name": name, "passed": bool(condition), **values})

    for i, x in enumerate(d["F_rows"]):
        den = Fraction(x["Eg_MeV"]) * Fraction(x["delta_beta_cos_times1000"])
        f = Fraction(x["shift_keV"]) / den
        df = Fraction(x["shift_SD_keV"]) / den
        residual = float(f - Fraction(x["printed_F"]))
        sd_residual = float(df - Fraction(x["printed_F_SD"]))
        rows.append({**x, "F_from_printed_centers": float(f),
                     "F_sd_fixed_denominator_only": float(df),
                     "F_center_residual": residual,
                     "F_sd_residual": sd_residual})
        check(f"row_{i}_{x['medium']}_F_units_arithmetic", abs(residual) < 0.001,
              center_residual=residual)
    check("unclipped_F_above_one_is_preserved",
          any(float(r["printed_F"]) > 1 for r in rows))
    means = []
    for medium in ("Ta", "Mo"):
        pair = [x for x in d["F_rows"] if x["medium"] == medium and x["Ex_MeV"] == "3.160"]
        weights = [1 / float(x["printed_F_SD"]) ** 2 for x in pair]
        mean = sum(w * float(x["printed_F"]) for w, x in zip(weights, pair)) / sum(weights)
        sd = 1 / sum(weights) ** 0.5
        means.append({"medium": medium, "conditional_independent_weighted_F": mean,
                      "conditional_sd": sd,
                      "not_certification_of_original_estimator_or_covariance": True})
        target = 0.332 if medium == "Ta" else 0.381
        check(f"two_line_conditional_mean_{medium}", abs(mean - target) < 0.001,
              mean=mean, sd=sd)
    tau = []
    for x in d["tau_rows"]:
        old = Fraction(x["old_Ta_tau_ps"])
        new_ta = Fraction(x["new_Ta_tau_ps"])
        new_adopted = Fraction(x["new_adopted_tau_ps"])
        tau.append({**x, "newTa_over_oldTa": float(new_ta / old),
                    "newAdopted_over_oldTa": float(new_adopted / old),
                    "fixed_branch_strength_multiplier_Ta": float(old / new_ta)})
    spread = max(x["newTa_over_oldTa"] for x in tau) / min(x["newTa_over_oldTa"] for x in tau)
    check("printed_ta_changes_are_not_one_exact_common_multiplier", spread > 1.02,
          extrema_ratio=spread)
    # Exact radiative M1/E2 fraction at fixed absolute photon probability.
    sm = Fraction(d["model_dependent_mixing"]["source_delta_SM"])
    f0 = sm ** 2 / (1 + sm ** 2)
    mixing = []
    for delta in map(Fraction, d["model_dependent_mixing"]["self_chosen_delta_controls"]):
        f = delta ** 2 / (1 + delta ** 2)
        ratio = f / f0
        mixing.append({"delta": float(delta), "E2_fraction": float(f),
                       "B_ratio_fixed_absolute_photon_chart": float(ratio),
                       "conditional_B_from_printed88_e2fm4": 88 * float(ratio)})
    check("delta_sign_not_identified_by_component_rate", f0 == (-sm) ** 2 / (1 + (-sm) ** 2))
    check("model_delta_double_control", abs(mixing[1]["B_ratio_fixed_absolute_photon_chart"] - 401/101) < 1e-14)
    pure = []
    for x in d["illustrative_pure_E2_controls"]:
        b = 1e4 * 0.0816202120 / (float(x["tau_ps"]) * float(x["Eg_MeV"]) ** 5)
        pure.append({**x, "conditional_pgamma1_E2_e2fm4": b,
                     "descriptive_center_difference_percent": 100 * (b / float(x["source_B"]) - 1),
                     "does_not_certify_inventory": True})
    mass = d["oscillator_comparison"]["A"]
    w1 = 45 / mass ** (1/3) - 25 / mass ** (2/3)
    w2 = 41 / mass ** (1/3)
    oscillator = {"omega_author_MeV": w1, "omega_alternative_MeV": w2,
                  "conditional_B_alternative_over_author": (w1 / w2) ** 2,
                  "not_original_shell_model_replay": True}
    check("oscillator_radial_scaling_direction", (w1 / w2) ** 2 < 1)
    output = {"scope": d["scope"], "contract_sha256": hashlib.sha256(a.contract.read_bytes()).hexdigest(),
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "F_rows": rows, "max_F_center_residual": max(abs(x["F_center_residual"]) for x in rows),
              "conditional_two_line_means": means, "tau_comparison_roles": tau,
              "Ta_multiplier_spread": spread, "model_delta_sensitivity": mixing,
              "conditional_pure_E2": pure, "oscillator_radial_scaling": oscillator,
              "checks": checks, "checks_passed": sum(x["passed"] for x in checks),
              "checks_total": len(checks), "all_passed": all(x["passed"] for x in checks)}
    a.output.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"all_passed": output["all_passed"], "checks": len(checks),
                      "max_F_center_residual": output["max_F_center_residual"],
                      "Ta_multiplier_spread": spread, "mixing_controls": mixing,
                      "oscillator": oscillator}))
    if not output["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
