#!/usr/bin/env python3
"""Deterministic validation checks for the local P-ADO manuscript outputs."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).parents[1]
profile = json.loads((ROOT / "analysis" / "results" / "alignment-profile.json").read_text())
coverage = json.loads((ROOT / "analysis" / "results" / "coverage.json").read_text())

fits = profile["fits_at_rho_center"]
assert set(fits) == {"shared", "family", "energy", "mixture"}
assert abs(fits["shared"]["params"][0] - 0.280145995) < 1e-6
assert abs(fits["mixture"]["params"][2] - 0.530370441) < 1e-6
assert fits["shared"]["aic"] < fits["family"]["aic"]
assert fits["shared"]["aic"] < fits["energy"]["aic"]
assert fits["shared"]["aic"] < fits["mixture"]["aic"]
assert len(profile["rho_profile"]) == 17 * 4
assert coverage["n_toys"] == 1000
assert 0.0 < coverage["empirical_fraction_max_d2_leq_q95"] < 1.0
assert coverage["max_d2_quantiles"]["0.95"] > coverage["threshold_q95_2d"]
print("P-ADO manuscript output validation passed.")
