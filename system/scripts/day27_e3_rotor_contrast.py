#!/usr/bin/env python3
"""Conditional E3 rotor contrasts from Butler2020; no experimental likelihood."""

import argparse
import fractions
import json
import math
from datetime import datetime, timezone
from pathlib import Path


def clebsch_gordan_exact_zero_zero(j1, j2, j):
    """Exact (j1 0 j2 0 | j 0) for integer angular momenta."""
    if (j1 + j2 + j) % 2 != 0:
        return 0.0, fractions.Fraction(0, 1)
    g = (j1 + j2 + j) // 2
    if not (abs(j1 - j2) <= j <= j1 + j2):
        return 0.0, fractions.Fraction(0, 1)
    # Racah formula for zero z-projections:
    numerator = math.factorial(2 * g - 2 * j1) * math.factorial(2 * g - 2 * j2) * math.factorial(2 * g - 2 * j)
    denominator = math.factorial(2 * g + 1)
    prefactor = fractions.Fraction(numerator, denominator)
    factors = fractions.Fraction(math.factorial(g), (math.factorial(g - j1) * math.factorial(g - j2) * math.factorial(g - j)))
    sign = (-1) ** (g - j)
    exact_squared = prefactor * (factors ** 2) * (2 * j + 1)
    return sign * math.sqrt(float(exact_squared)), exact_squared


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    cg, cg_squared = clebsch_gordan_exact_zero_zero(2, 3, 3)
    ratio_squared = 5 * cg_squared
    if ratio_squared != fractions.Fraction(4, 3):
        raise AssertionError("K=0 E3 angular coefficient convention mismatch")
    rotor_ratio = -math.sqrt(4.0 / 3.0)
    data = [
        {
            "nucleus": "222Ra",
            "m03": 1.13,
            "m03_error": 0.09,
            "m23": -0.9,
            "m23_error_low": 0.5,
            "m23_error_high": 0.5,
            "m23_starred": False,
        },
        {
            "nucleus": "228Ra",
            "m03": 0.87,
            "m03_error": 0.15,
            "m23": -0.06,
            "m23_error_low": 0.16,
            "m23_error_high": 0.23,
            "m23_starred": True,
        },
    ]
    rows = []
    for row in data:
        predicted = rotor_ratio * row["m03"]
        contrast = row["m23"] - predicted
        lower = (
            row["m23"]
            - row["m23_error_low"]
            - rotor_ratio * (row["m03"] - row["m03_error"])
        )
        upper = (
            row["m23"]
            + row["m23_error_high"]
            - rotor_ratio * (row["m03"] + row["m03_error"])
        )
        if not lower <= contrast <= upper:
            raise AssertionError("Central contrast outside endpoint box")
        rows.append(
            {
                **row,
                "rotor_prediction_m23": predicted,
                "central_m23_over_m03": row["m23"] / row["m03"],
                "contrast_m23_minus_rotor_prediction": contrast,
                "printed_input_endpoint_box": [lower, upper],
                "box_contains_zero": lower <= 0 <= upper,
                "source_locator": "Butler2020 PRL PDF p3 Table I, 0+||E3||3- and 2+||E3||3-",
                "units": "e b^(3/2)",
            }
        )
    variance_control = []
    sigma_a, sigma_b = 0.5, abs(rotor_ratio) * 0.09
    for correlation in (-1, 0, 1):
        # D=M23-r*M03; this is hypothetical Gaussian covariance algebra.
        covariance = correlation * 0.5 * 0.09
        variance = (
            0.5**2 + rotor_ratio**2 * 0.09**2 - 2 * rotor_ratio * covariance
        )
        variance_control.append(
            {
                "assumed_correlation": correlation,
                "conditional_sigma_contrast": math.sqrt(max(0, variance)),
            }
        )
    low = abs(sigma_a - sigma_b)
    high = sigma_a + sigma_b
    if not math.isclose(
        min(x["conditional_sigma_contrast"] for x in variance_control),
        low,
        abs_tol=1e-12,
    ) or not math.isclose(
        max(x["conditional_sigma_contrast"] for x in variance_control),
        high,
        abs_tol=1e-12,
    ):
        raise AssertionError("Covariance endpoint control failed")
    result = {
        "schema_version": 1,
        "observed_at": datetime.now(timezone.utc).isoformat(),
        "status": "conditional-published-table-contrast",
        "source": "knowledge/sources/butler-2020-222-228ra-octupole-evolution.md",
        "rotor_ratio_exact": "-sqrt(4/3)",
        "rotor_ratio_float": rotor_ratio,
        "normalization": "K=0, single Q3, common adopted state-phase convention",
        "data": rows,
        "gaussian_covariance_control_222Ra_only": variance_control,
        "boundary": [
            "Input endpoint boxes are not simultaneous confidence regions.",
            "Quoted errors include chi-square and systematic contributions.",
            "228Ra M23 is a coupled/starred parameter; no independence assumed.",
            "No likelihood ratio, posterior odds, or experimental significance computed.",
            "No full closure sum or fourth octupole moment reconstructed.",
            "A phase convention must be fixed consistently with the E2/E3 network.",
        ],
    }
    output = args.output_dir / "e3-rotor-contrast.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
