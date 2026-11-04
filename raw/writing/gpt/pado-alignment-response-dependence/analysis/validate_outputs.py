#!/usr/bin/env python3
"""Deterministic validation checks for the local P-ADO manuscript outputs."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).parents[1]
profile = json.loads((ROOT / "analysis" / "results" / "alignment-profile.json").read_text())
coverage = json.loads((ROOT / "analysis" / "results" / "coverage.json").read_text())
coverage_grid = json.loads((ROOT / "analysis" / "results" / "coverage-grid.json").read_text())
profile_coverage = json.loads((ROOT / "analysis" / "results" / "profile-coverage.json").read_text())

fits = profile["fits_at_rho_center"]
assert set(fits) == {"shared", "family", "energy", "mixture"}
assert abs(fits["shared"]["params"][0] - 0.280145995) < 1e-6
assert abs(fits["mixture"]["params"][2] - 0.530370441) < 1e-6
assert fits["shared"]["aic"] < fits["family"]["aic"]
assert fits["shared"]["aic"] < fits["energy"]["aic"]
assert fits["shared"]["aic"] < fits["mixture"]["aic"]
assert len(profile["rho_profile"]) == 81 * 4
assert coverage["n_toys"] == 1000
assert 0.0 < coverage["empirical_fraction_max_d2_leq_q95"] < 1.0
assert coverage["max_d2_quantiles"]["0.95"] > coverage["threshold_q95_2d"]
assert len(coverage_grid["matched_covariance"]) == 35
assert len(coverage_grid["rho_misspecified_to_zero"]) == 35
assert coverage["empirical_fraction_mc_se"] > 0.0
assert profile_coverage["n_toys_per_true_rho"] == 300
assert profile_coverage["observed_profiled_max_d2"] > 20.0
assert all(
    profile_coverage["profiled_max_d2_quantiles"][str(rho)]["0.95"]
    < profile_coverage["observed_profiled_max_d2"]
    for rho in profile_coverage["true_rho_values"]
)
matched = [x["coverage_at_q95_2d"] for x in coverage_grid["matched_covariance"]]
misspecified = [x["coverage_at_q95_2d"] for x in coverage_grid["rho_misspecified_to_zero"]]
assert min(matched) > 0.60
assert min(misspecified) < 0.56
print("P-ADO manuscript output validation passed.")
