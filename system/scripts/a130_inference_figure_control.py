#!/usr/bin/env python3
"""Check the actual plotted profiles against their declared mathematical meaning.

This executes the producer and inspects its plotted arrays. It tests the two
synthetic minima, the actual local curvature, and the Gaussian likelihood ratio
with a physical boundary. It does not test frequentist coverage.
"""
import datetime
import hashlib
import json
import os
from pathlib import Path
import runpy

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    root = Path(__file__).resolve().parents[2]
    os.chdir(root)
    producer = Path("system/scripts/a130_inference_profile_figure.py")
    captured = []
    original_close = plt.close

    def capture_close(*args, **kwargs):
        if args and hasattr(args[0], "axes") and len(args[0].axes) == 2:
            captured.append([
                [(line.get_xdata().copy(), line.get_ydata().copy())
                 for line in ax.lines]
                for ax in args[0].axes
            ])
        return original_close(*args, **kwargs)

    plt.close = capture_close
    try:
        runpy.run_path(str(producer), run_name="__main__")
    finally:
        plt.close = original_close

    left, right = captured[-1]
    x, y = left[0]
    minima = np.where((y[1:-1] < y[:-2]) & (y[1:-1] < y[2:]))[0] + 1
    fitted_polynomial = np.polyfit(x, y, 4)
    half_hessian = 0.5 * np.polyval(np.polyder(fitted_polynomial, 2), 20.0)
    px, py = left[1]
    curvature_error = float(np.max(np.abs(py - half_hessian * (px - 20.0)**2)))
    rx, ry = right[1]
    likelihood_ratio = np.exp(-0.5 * (rx + 0.6)**2) / np.exp(-0.5 * 0.6**2)
    ratio_error = float(np.max(np.abs(ry + 2.0 * np.log(likelihood_ratio))))
    checks = {
        "two_local_minima": len(minima) == 2,
        "minima_at_declared_positions": (
            len(minima) == 2 and np.allclose(x[minima], [-40.0, 20.0])
        ),
        "local_parabola_matches_actual_hessian": curvature_error < 1e-8,
        "physical_domain_includes_boundary": rx[0] == 0 and np.min(rx) >= 0,
        "same_gaussian_likelihood_reference": (
            ratio_error < 1e-12 and abs(ry[0]) < 1e-15
        ),
        "finite_nonnegative_physical_profile": (
            np.isfinite(ry).all() and np.min(ry) >= 0
        ),
    }
    result = {
        "observed_machine_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "producer": str(producer),
        "producer_sha256": hashlib.sha256(producer.read_bytes()).hexdigest(),
        "control": str(Path(__file__).relative_to(root)),
        "minima_degrees": x[minima].tolist(),
        "profile_values_at_minima": y[minima].tolist(),
        "local_parabola_max_error_vs_fitted_quartic_hessian": curvature_error,
        "physical_profile_max_error_vs_gaussian_log_ratio": ratio_error,
        "checks": {key: bool(value) for key, value in checks.items()},
        "passed": all(checks.values()),
        "boundary": (
            "Synthetic quartic profile and specified Gaussian observation only; "
            "no nuclear-response fit or Feldman-Cousins coverage construction."
        ),
    }
    output = Path("outputs/l4/20261114-A130-inference-figure-controls/results.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"passed": result["passed"], "output": str(output)}))
    if not result["passed"]:
        raise AssertionError("Inference figure control failed; inspect its JSON.")


if __name__ == "__main__":
    main()
