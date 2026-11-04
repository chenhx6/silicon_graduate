#!/usr/bin/env python3
"""Independent finite-J response-map checks for the P-ADO analysis.

The benchmark is a replay of a published attenuation-table row, not a new
measurement.  The check is kept separate from the fit so that a numerical
change in the response map cannot silently pass through the paper outputs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from profile_alignment_models import alpha_prediction


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).parents[1]
        / "analysis"
        / "results"
        / "response-map-validation.json",
    )
    args = parser.parse_args()

    # Der Mateosian & Sunyar, ADNDT 13, 391--406 (1974), Table II,
    # J=23/2 and sigma/J=0.2: alpha2=0.894266 and alpha4=0.689096.
    # The source locator is carried into the output for paper review.
    expected = np.asarray([0.894266, 0.689096])
    observed = np.asarray(alpha_prediction(23 / 2, 0.2))
    delta = observed - expected
    tolerance = 5e-7

    checks = [
        {
            "id": "DA74-6",
            "description": "finite-J Gaussian attenuation-table replay",
            "spin_j": 23 / 2,
            "r": 0.2,
            "expected_alpha2_alpha4": expected.tolist(),
            "calculated_alpha2_alpha4": observed.tolist(),
            "absolute_difference": np.abs(delta).tolist(),
            "tolerance": tolerance,
            "source": "knowledge/sources/der-mateosian-sunyar-1974-attenuation-coefficients.md",
            "locator": "DA74-6; printed p.400 / PDF p.10, Table II, J=23/2, sigma/J=0.2",
            "passed": bool(np.all(np.abs(delta) < tolerance)),
        },
        {
            "id": "finite-J-limit",
            "description": "narrow-width complete-alignment limit",
            "spin_j": 13 / 2,
            "r": 0.02,
            "expected_alpha2_alpha4": [1.0, 1.0],
            "calculated_alpha2_alpha4": list(alpha_prediction(13 / 2, 0.02)),
            "tolerance": 1e-12,
            "source": "local analytical limit",
            "locator": "Gaussian population concentrated at the minimum |m| substate under the declared normalization",
            "passed": bool(np.allclose(alpha_prediction(13 / 2, 0.02), [1.0, 1.0], atol=1e-12)),
        },
    ]
    if not all(check["passed"] for check in checks):
        raise SystemExit("response-map validation failed")

    payload = {
        "schema_version": 1,
        "analysis_script": str(Path(__file__)),
        "analysis_script_sha256": sha256_file(Path(__file__)),
        "response_implementation": "profile_alignment_models.alpha_prediction",
        "checks": checks,
        "interpretation_boundary": [
            "The external-table replay checks the finite-J Gaussian attenuation convention.",
            "It does not validate the Zobel detector response, event counts, covariance, or feeding history.",
            "The local narrow-width check is a mathematical limit, not an experimental result.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "checks": len(checks)}, indent=2))


if __name__ == "__main__":
    main()
