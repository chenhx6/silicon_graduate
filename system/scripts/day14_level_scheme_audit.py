#!/usr/bin/env python3
"""Audit a published 193Bi subgraph, with explicitly conditional covariances.

This is an L2 table exercise, not an event-level fit or an ENSDF evaluation.
The fixture keeps fitting errors separate from the caption's extra error.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.stats import chi2


def audit(data: dict) -> dict:
    checks: dict[str, bool] = {}

    def check(name: str, predicate: bool) -> None:
        checks[name] = bool(predicate)
        if not predicate:
            raise AssertionError(name)

    rows = data["transitions"]
    n = len(data["levels"])
    incidence = np.zeros((len(rows), n))
    for i, row in enumerate(rows):
        incidence[i, row["parent"]] = 1
        incidence[i, row["daughter"]] = -1
    y = np.array([r["energy_keV"] for r in rows])
    fit_error = np.array([r["fitting_error_keV"] for r in rows])
    # Independent cycle basis, not three independent statistical tests.
    cycles = np.array([[1, 1, 0, 0, -1, 0, 0],
                       [0, 1, 1, 0, 0, -1, 0],
                       [0, 0, 1, 1, 0, 0, -1]], dtype=float)
    check("incidence_rank_n_minus_one", np.linalg.matrix_rank(incidence) == n - 1)
    check("unanchored_offset_is_null", np.allclose(incidence @ np.ones(n), 0))
    check("cycles_close_for_any_level_vector", np.allclose(cycles @ incidence, 0))
    check("independent_cycle_basis", np.linalg.matrix_rank(cycles) == len(rows) - n + 1)
    design = incidence[:, 1:]
    closure = cycles @ y

    def fit(covariance: np.ndarray) -> dict:
        precision = np.linalg.inv(covariance)
        level_cov = np.linalg.inv(design.T @ precision @ design)
        delta = level_cov @ design.T @ precision @ y
        predicted = design @ delta
        residual = y - predicted
        chi = float(residual @ precision @ residual)
        cycle_cov = cycles @ covariance @ cycles.T
        cycle_chi = float(closure @ np.linalg.solve(cycle_cov, closure))
        check("gls_equals_cycle_chi_" + str(len(checks)), np.isclose(chi, cycle_chi, atol=1e-8))
        check("gls_normal_equations_" + str(len(checks)), np.allclose(design.T @ precision @ residual, 0, atol=1e-8))
        # Whitened least squares provides a separate numerical route.
        white = np.linalg.cholesky(covariance)
        direct = np.linalg.lstsq(np.linalg.solve(white, design), np.linalg.solve(white, y), rcond=None)[0]
        check("whitened_lstsq_agrees_" + str(len(checks)), np.allclose(direct, delta, atol=1e-8))
        return {"levels_relative_to_anchor_keV": [0.0, *delta.tolist()],
                "conditional_level_covariance_keV2": level_cov.tolist(),
                "residual_keV": residual.tolist(), "chi2": chi,
                "dof": len(rows) - n + 1, "conditional_p_value": float(chi2.sf(chi, len(rows) - n + 1)),
                "cycle_covariance_keV2": cycle_cov.tolist()}

    diagonal_fit = np.diag(fit_error ** 2)
    # The quadrature rule and independence are our assumptions, not a supplied Sigma.
    diagonal_added = diagonal_fit + data["caption_extra_error_keV"] ** 2 * np.eye(len(rows))
    cases = {"fitting_error_only_independent": fit(diagonal_fit),
             "caption_extra_quadrature_independent": fit(diagonal_added)}
    # A shared energy offset survives two-photon minus one-photon closure.
    common_offset = data["counterfactual_common_offset_sigma_keV"]
    offset_cov = diagonal_added + common_offset ** 2 * np.ones((len(rows), len(rows)))
    cases["declared_common_offset_counterfactual"] = fit(offset_cov)
    check("common_offset_survives_cycles", np.array_equal(cycles @ np.ones(len(rows)), np.ones(3)))
    # A common gain on physically consistent gaps cancels in cycle space.
    physical_gaps = design @ np.array(cases["caption_extra_quadrature_independent"]["levels_relative_to_anchor_keV"][1:])
    gain_cov = diagonal_added + data["counterfactual_gain_sigma"] ** 2 * np.outer(physical_gaps, physical_gaps)
    cases["declared_common_gain_counterfactual"] = fit(gain_cov)
    check("consistent_common_gain_cancels_cycles", np.allclose(cycles @ physical_gaps, 0, atol=1e-10))
    check("common_gain_preserves_cycle_covariance", np.allclose(cycles @ gain_cov @ cycles.T, cycles @ diagonal_added @ cycles.T, atol=1e-10))
    check("shared_edges_correlate_closures", (cycles @ diagonal_added @ cycles.T)[0, 1] > 0)

    # An unpenalized offset illustrates a different model and two remaining contrasts.
    augmented = np.column_stack((design, np.ones(len(rows))))
    precision = np.linalg.inv(diagonal_added)
    augmented_cov = np.linalg.inv(augmented.T @ precision @ augmented)
    augmented_fit = augmented_cov @ augmented.T @ precision @ y
    augmented_residual = y - augmented @ augmented_fit
    augmented_chi = float(augmented_residual @ precision @ augmented_residual)
    check("offset_design_rank", np.linalg.matrix_rank(augmented) == n)
    check("floating_offset_cannot_worsen_fit", augmented_chi <= cases["caption_extra_quadrature_independent"]["chi2"] + 1e-10)

    corrupted = y.copy()
    corrupted[4] += data["deliberate_corruption_keV"]
    corrupted_closure = cycles @ corrupted
    corrupt_chi = float(corrupted_closure @ np.linalg.solve(cycles @ diagonal_added @ cycles.T, corrupted_closure))
    check("deliberate_bad_crossover_detected", corrupt_chi > cases["caption_extra_quadrature_independent"]["chi2"] + 10)
    # Changing labels/order of rows must not alter the graph fit.
    order = np.array([6, 2, 5, 1, 4, 0, 3])
    shuffled = np.linalg.lstsq(design[order], y[order], rcond=None)[0]
    check("row_permutation_preserves_equal_weight_fit", np.allclose(shuffled, np.array(cases["caption_extra_quadrature_independent"]["levels_relative_to_anchor_keV"][1:])))

    pair = data["unresolved_doublet_keV"]
    anchor = data["doublet_lower_anchor_keV"]
    alternatives = [{"first_from_top_keV": pair[1], "second_keV": pair[0],
                     "intermediate_keV": anchor + pair[0], "upper_keV": anchor + sum(pair)},
                    {"first_from_top_keV": pair[0], "second_keV": pair[1],
                     "intermediate_keV": anchor + pair[1], "upper_keV": anchor + sum(pair)}]
    check("doublet_orders_same_upper_level", alternatives[0]["upper_keV"] == alternatives[1]["upper_keV"])
    check("doublet_orders_change_intermediate", np.isclose(alternatives[1]["intermediate_keV"] - alternatives[0]["intermediate_keV"], 0.6))
    # The thirteen-line floating SD chain has no absolute-energy anchor.
    sd = np.zeros((13, 14))
    for i in range(13):
        sd[i, i + 1] = 1
        sd[i, i] = -1
    check("sd_chain_rank_13_of_14", np.linalg.matrix_rank(sd) == 13)
    check("sd_unknown_X_is_null", np.array_equal(sd @ np.ones(14), np.zeros(13)))

    # Source-specific normalization matters even before extracting P=A/Q.
    polarization = []
    a0, a1 = data["polarization_normalization_coefficients"]
    for row in rows:
        asymmetry = row["IPDCO"]
        a = a0 + a1 * row["energy_keV"]
        ratio = (1 + asymmetry) / (a * (1 - asymmetry))
        recovered = (a * ratio - 1) / (a * ratio + 1)
        without_a = (ratio - 1) / (ratio + 1)
        check("polarization_inverse_" + row["id"], np.isclose(recovered, asymmetry))
        polarization.append({"transition": row["id"], "a": a,
                             "conditional_Nperp_over_Nparallel": ratio,
                             "reported_A": asymmetry, "counterfactual_A_without_a": without_a})
    # Same-parent photon ratios; not total branches and not absolute B values.
    intensity_ratios = []
    for mother in [2, 3, 4]:
        rs = [r for r in rows if r["parent"] == mother]
        m1 = next(r for r in rs if r["assigned_multipolarity"] == "M1")
        e2 = next(r for r in rs if r["assigned_multipolarity"] == "E2")
        intensity_ratios.append({"parent_level_index": mother, "lines": [m1["id"], e2["id"]],
                                 "relative_photon_intensity_ratio": m1["relative_intensity"] / e2["relative_intensity"],
                                 "absolute_B_available": False, "ICC_and_delta_available": False})
    return {"analysis_kind": "L2 published-table consistency exercise",
            "source_sha256": data["raw_sha256"], "transition_count": len(rows),
            "incidence_rank": int(np.linalg.matrix_rank(incidence)), "cycle_count": len(cycles),
            "cycle_residual_keV": closure.tolist(), "covariance_cases": cases,
            "floating_offset_model": {"offset_keV": float(augmented_fit[-1]), "offset_conditional_sigma_keV": float(np.sqrt(augmented_cov[-1, -1])), "chi2": augmented_chi, "dof": 2},
            "intentional_corruption_control": {"shift_keV": data["deliberate_corruption_keV"], "chi2": corrupt_chi},
            "doublet_order_alternatives": alternatives, "sd_chain_absolute_energy_identifiable": False,
            "polarization_normalization_counterfactual": polarization,
            "same_parent_intensity_ratios": intensity_ratios,
            "checks": checks, "checks_passed": sum(checks.values()),
            "boundaries": data["boundaries"]}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    for path in (args.fixture, args.output):
        path.resolve().relative_to(root)
    data = json.loads(args.fixture.read_text(encoding="utf-8"))
    raw = root / data["raw_file"]
    if hashlib.sha256(raw.read_bytes()).hexdigest() != data["raw_sha256"]:
        raise ValueError("raw identity mismatch; do not use the fixture")
    result = audit(data)
    result["fixture_sha256"] = hashlib.sha256(args.fixture.read_bytes()).hexdigest()
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"checks_passed": result["checks_passed"], "closure_keV": result["cycle_residual_keV"],
                      "conditional_chi2": {k: v["chi2"] for k, v in result["covariance_cases"].items()},
                      "floating_offset": result["floating_offset_model"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
