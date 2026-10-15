#!/usr/bin/env python3
"""Audit original band/fit roles, a model estimate and channel-specific F scale.

The numerical controls do not reconstruct state lifetimes or a fit likelihood.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=RUN / "petrache1998-reference-audit.json")
    args = parser.parse_args()
    data = json.loads((RUN / "petrache1998-table-I-input.json").read_text())
    proof = json.loads((RUN / "petrache1998-pdf-verification-working.json").read_text())
    checks = {}

    def check(name, result):
        checks[name] = bool(result)
        if not result:
            raise AssertionError(name)

    check("original_hash_matches_existing_source", hashlib.sha256((ROOT / proof["path"]).read_bytes()).hexdigest() == data["source_sha256"])
    rows = data["rows"]
    current = [r for r in rows if not r["fit_role"].startswith("external_")]
    check("eight_source_rows_five_current_physical_bands", len(rows) == 8 and len({r["band_id"] for r in current}) == 5)
    variants = [r for r in current if r["band_id"] == "134Nd:Band3"]
    check("one_Band3_has_three_alternative_or_segment_rows", len(variants) == 3 and len({r["band_id"] for r in variants}) == 1)
    panels = data["figure2_panels"]
    check("six_panels_five_bands_not_six_independent_samples", len(panels) == 6 and len({r["band_id"] for r in panels}) == 5)
    check("external_Ce132_not_reassigned_to_current_data", rows[-1]["band_id"] == "132Ce:yrastHD" and rows[-1] not in current)
    check("unreported_cells_preserved", rows[4]["Q0_the_eb"] is None and rows[7]["Qsf_eb"] is None)
    a = data["footnote_a"]
    low0, low1 = map(lambda x: Fraction(str(x)), a["reported_lower_endpoints"])
    low = (low0 + low1) / 2
    two = Fraction(str(a["reported_two_intruder_reference"]))
    fraction = Fraction(str(a["assumed_contribution_fraction"]))
    estimate = low + fraction * (two - low)
    check("footnote_lower_average_exact", low == Fraction("5.45"))
    check("footnote_6p07_is_exact_conditional_midpoint", estimate == Fraction("6.07") == (low + two) / 2)
    check("estimated_row_not_direct_computed_configuration", a["one_intruder_positive_parity_not_calculated"] and rows[3]["model_role"].startswith("footnote_a_"))
    conflicts = data["literal_conflicts"]
    check("prose_table_feeding_conflict_not_resolved", conflicts["135Nd_Qsf_table"] != conflicts["135Nd_Qsf_prose"] and conflicts["conflict_resolution"] is None)
    v = data["velocity_source"]
    beta_nd = v["beta_Nd"]
    beta_ce = v["beta_Ce_alpha3n_MC_corrected"]
    factor = beta_ce / beta_nd
    check("borrowing_Nd_velocity_lowers_Ce_F", 0 < factor < 1)
    # F = mean decay velocity / initial velocity. This changes only its
    # normalization, not a fitted lifetime without a slowing/feeding model.
    chosen_f = 0.45
    check("F_rescaling_exact_in_stated_definition", math.isclose((beta_ce * chosen_f) / beta_nd, chosen_f * factor))
    chosen_ftop = 0.9
    beta_hat = beta_ce * chosen_ftop
    check("forcing_observed_top_to_one_biases_beta", math.isclose(beta_hat / beta_ce, chosen_ftop) and math.isclose(beta_ce * chosen_f / beta_hat, chosen_f / chosen_ftop))
    angular = []
    for angle in [36, 60, 72, 90, 108, 120, 144]:
        relative_shift = (beta_nd - beta_ce) * math.cos(math.radians(angle))
        angular.append({"angle_deg": angle, "delta_E_per_MeV_keV_if_F1": relative_shift * 1000})
    check("first_order_angle_checks", abs(angular[3]["delta_E_per_MeV_keV_if_F1"]) < 1e-12 and math.isclose(angular[0]["delta_E_per_MeV_keV_if_F1"], -angular[-1]["delta_E_per_MeV_keV_if_F1"]))
    check("nominal_channels_balance_not_measured_purity", (28 + 110 - 4, 14 + 46) == (134, 60) and (28 + 110 - 3, 14 + 46) == (135, 60) and (28 + 110 - 4 - 3, 14 + 46 - 2) == (131, 58))
    check("no_unavailable_tau_or_covariance_inferred", data["actual_state_lifetimes"] is None and data["chi2_grid"] is None and v["actual_covariance"] is None)
    output = {
        "source": {"doi": data["source_doi"], "sha256": data["source_sha256"], "locator": data["locator"]},
        "table_rows": rows,
        "source_counts": {"table_rows": 8, "current_physical_bands": 5, "external_bands": 1, "figure_panels": 6, "new_independent_measurements_in_this_run": 0},
        "footnote_a": {"lower_average_exact": str(low), "two_intruder_input": str(two), "assumed_fraction": str(fraction), "estimated_Q0_eb": float(estimate), "sensitivity_dQ0_dfraction_eb": float(two - low), "role": "author conditional estimate; no calculated one-intruder configuration or assigned sigma"},
        "channel_velocity": {"beta_Nd": beta_nd, "beta_Ce": beta_ce, "Ce_F_scale_if_wrong_Nd_beta": factor, "relative_F_percent_change": 100 * (factor - 1), "actual_Q0_or_tau_bias": None, "first_order_angles": angular},
        "chosen_top_normalization_control": {"chosen_true_Ftop": chosen_ftop, "chosen_true_other_F": chosen_f, "beta_hat_over_beta": chosen_ftop, "F_other_after_forcing_top_one": chosen_f / chosen_ftop, "scope": "declared definition control; no source Ftop or measured beta uncertainty"},
        "source_reference": {"Petrache_original_Ce131_Q0_eb": "7.3(4)", "Clark1996_quoted_Ce131_Q0_eb": "7.4(3)", "Matev2007_reference39": "Clark PRL76,3510(1996), not Petrache1998", "Clark_original_body_read": False},
        "literal_conflicts": conflicts,
        "missing_inputs": ["raw gated centroids and common covariance", "actual slowing/feeding inputs and likelihood", "explicit band/transition and Q0-to-Qt geometry manifest", "Clark original acquisition/band crosswalk"],
        "checks": checks,
        "check_count": len(checks),
        "passed": all(checks.values()),
    }
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"checks": len(checks), "passed": output["passed"], "source_counts": output["source_counts"], "footnote_Q0": float(estimate), "wrong_channel_F_factor": factor, "actual_tau_reconstructed": False}))


if __name__ == "__main__":
    main()
