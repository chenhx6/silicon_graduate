#!/usr/bin/env python3
"""Printed-centre dependency exercise; no experimental likelihood or CI fit."""
import argparse
import json
from pathlib import Path

import numpy as np


def observables(delta, photon_ratio, eout, ein):
    k = photon_ratio * (ein / eout) ** 5
    c = 0.697 * eout ** 2
    return np.array([delta, k * delta ** 2 / (1 + delta ** 2),
                     c * k / (1 + delta ** 2)])


def exercise():
    # Lv2022 main Table1 / SI Table1: 813.2 and 726.0 share a parent.
    delta, photon_ratio, eout, ein = -0.37, 6.4 / 3.7, 0.8132, 0.7260
    y = observables(delta, photon_ratio, eout, ein)
    k = photon_ratio * (ein / eout) ** 5
    c = 0.697 * eout ** 2
    jac = np.array([[1, 0],
                    [2 * delta * k / (1 + delta ** 2) ** 2,
                     delta ** 2 / (1 + delta ** 2)],
                    [-2 * c * delta * k / (1 + delta ** 2) ** 2,
                     c / (1 + delta ** 2)]])
    # Inputs here are (delta,K); this is an algebraic null direction,
    # independent of any choice of actual experimental covariance.
    normal = np.array([-2 * delta * y[2], c, -delta ** 2])
    fd = np.column_stack([
        (observables(delta + 1e-6, photon_ratio, eout, ein)
         - observables(delta - 1e-6, photon_ratio, eout, ein)) / 2e-6,
        (observables(delta, photon_ratio + 1e-6, eout, ein)
         - observables(delta, photon_ratio - 1e-6, eout, ein)) / 2e-6
        / (ein / eout) ** 5])
    controls = {
        "analytic_jacobian_matches_finite_difference": bool(np.max(abs(fd-jac)) < 1e-8),
        "two_inputs_rank_two": int(np.linalg.matrix_rank(jac)) == 2,
        "constraint_normal_annihilates_jacobian": bool(np.max(abs(normal @ jac)) < 1e-12),
        "sign_flip_keeps_strength_ratios": bool(np.allclose(
            y[1:], observables(-delta, photon_ratio, eout, ein)[1:])),
        "pure_M1_zero_E2_component": bool(observables(0, photon_ratio, eout, ein)[1] == 0),
        "doubling_photon_branch_doubles_both_strength_ratios": bool(np.allclose(
            2 * y[1:], observables(delta, 2 * photon_ratio, eout, ein)[1:])),
    }
    return {
        "scope": "Conditional printed-centre algebra; pure E2 photon denominator; energies MeV. No raw counts, response, experimental Cov, CI, mode verdict or beam time inferred.",
        "source": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
        "locators": ["L22-D22-R095-2", "L22-D22-002"],
        "inputs": {"delta": delta, "photon_ratio": photon_ratio,
                   "eout_MeV": eout, "ein_MeV": ein},
        "output_order": ["delta", "rE2", "rM1_muN2_per_e2b2"],
        "values": y.tolist(), "K": k, "c": c,
        "jacobian_input_order": ["delta", "K"],
        "jacobian": jac.tolist(), "rank": int(np.linalg.matrix_rank(jac)),
        "constraint": "c*rE2-delta^2*rM1=0",
        "constraint_residual": float(c*y[1]-delta**2*y[2]),
        "controls": controls, "all_controls_pass": all(controls.values()),
        "limitations": ["Printed values are rounded; no significance assigned to their differences.",
                        "The value 0.697 depends on electromagnetic units/conventions.",
                        "This analytic rank concerns transformed summaries, not the rank of unavailable experimental event data.",
                        "Covariance singularity is only first-order for the local propagated 3-vector, not a claim that every nonlinear sample covariance is singular."]}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    result = exercise()
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"all_controls_pass": result["all_controls_pass"],
                      "values": result["values"], "rank": result["rank"]}))
    return 0 if result["all_controls_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
