"""Bounded diagnostic-threshold audit; never tune against literature or truth."""

import argparse
from dataclasses import replace
import hashlib
import json
from pathlib import Path
import sys
from time import perf_counter

import numpy as np


def run(output):
    root = Path(__file__).resolve().parents[2]
    sys.path.insert(0, str(root / "GUI/src"))
    import multipolepdm
    from multipolepdm.contracts import GridSpec, Measurement
    from multipolepdm.io.input import example_data, job_from_dict, job_to_dict
    from multipolepdm.models import registry
    from multipolepdm.pdm import mapping

    output.mkdir(parents=True, exist_ok=True)
    constants = [
        (mapping, "_NEAR_SINGULAR", [1e-14, 1e-12, 1e-10], "warning only"),
        (mapping, "_SIGMA_EPS_MULTIPLIER", [32, 64, 128], "resolvability check"),
        (
            registry,
            "RESPONSE_ROUNDOFF_TOLERANCE",
            [1e-13, 1e-12, 1e-11],
            "physical response roundoff",
        ),
    ]
    rows, inputs = [], []
    start = perf_counter()
    for mode in ("P_ADO", "P_DCO", "PDCO"):
        base = job_from_dict(example_data(mode))
        base = replace(
            base,
            grid=GridSpec(
                xi_min_rad=np.deg2rad(-89.9),
                xi_max_rad=np.deg2rad(89.9),
                xi_points=361,
                sigma_points=101,
            ),
        )
        for delta in (-0.1, 1.0, -10.0):
            truth = registry.evaluate_response(
                base,
                np.array([np.arctan(delta)]),
                np.array([0.3 * base.reference_spin]),
            )
            p, r = float(truth.polarization[0, 0]), float(truth.angular_ratio[0, 0])
            pe, re = max(0.1075, 0.8 * abs(p)), 0.1 * abs(r)
            job = replace(
                base,
                polarization=Measurement(p, pe, pe),
                angular_ratio=Measurement(r, re, re),
            )
            response = registry.evaluate_response(job)
            baseline = mapping.map_density(job, response)
            inputs.append(
                {
                    "delta_truth": delta,
                    "sigma_over_i_truth": 0.3,
                    "job": job_to_dict(job),
                }
            )
            for module, name, values, purpose in constants:
                original = getattr(module, name)
                try:
                    for value in values:
                        setattr(module, name, value)
                        changed_response = registry.evaluate_response(job)
                        changed = mapping.map_density(job, changed_response)
                        equal = np.array_equal
                        rows.append(
                            {
                                "mode": mode,
                                "delta": delta,
                                "parameter": name,
                                "value": value,
                                "purpose": purpose,
                                "response_mask_equal": equal(
                                    response.valid, changed_response.valid
                                ),
                                "P_equal": equal(
                                    response.polarization,
                                    changed_response.polarization,
                                    equal_nan=True,
                                ),
                                "R_equal": equal(
                                    response.angular_ratio,
                                    changed_response.angular_ratio,
                                    equal_nan=True,
                                ),
                                "jacobian_equal": equal(
                                    baseline.jacobian, changed.jacobian, equal_nan=True
                                ),
                                "pdf_equal": equal(
                                    baseline.parameter_density,
                                    changed.parameter_density,
                                ),
                                "max_pdf_difference": float(
                                    np.max(
                                        np.abs(
                                            baseline.parameter_density
                                            - changed.parameter_density
                                        )
                                    )
                                ),
                                "warning_count": len(changed.warnings),
                            }
                        )
                finally:
                    setattr(module, name, original)
    input_bytes = (json.dumps(inputs, indent=2) + "\n").encode()
    (output / "inputs.json").write_bytes(input_bytes)
    result = {
        "package_version": multipolepdm.__version__,
        "input_sha256": hashlib.sha256(input_bytes).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds": perf_counter() - start,
        "cases": len(inputs),
        "scope": "Nine finite-response synthetic controls on a bounded361x101 grid; not universal threshold optimality. Warning/resolvability thresholds are not probability truncation parameters.",
        "all_pdfs_equal": all(row["pdf_equal"] for row in rows),
        "rows": rows,
    }
    (output / "results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "rows"}, indent=2))
    if not result["all_pdfs_equal"]:
        raise RuntimeError("Threshold changes affected a control PDF; inspect results.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "benchmarks/numeric_policy_v0_1_1",
    )
    run(parser.parse_args().output)
