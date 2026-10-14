#!/usr/bin/env python3
"""Conditional coefficient-convention worksheet, not a new experimental fit.

Z83-1 defines Aexp = alpha * Amax. Z83-11 supplies published alpha
marginals; the actual covariance is absent (Z83-12). Amax below is a
task-derived pure-E2 point-response coefficient; rho is deliberately chosen.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from numpy.polynomial import legendre

from day14_angular_fit_covariance_design import maximum_coefficients


def normalized_coefficients(beta):
    beta = np.asarray(beta, dtype=float)
    return beta[1:] / beta[0]


def ratio_jacobian(beta):
    f = beta[0]
    a = normalized_coefficients(beta)
    return np.array([[-a[0] / f, 1 / f, 0],
                     [-a[1] / f, 0, 1 / f]])


def audit():
    checks = {}

    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            raise AssertionError(name)

    c = maximum_coefficients()
    check("pure_E2_CG_maximum_matches_exact_fractions",
          np.allclose(c, [40 / 91, -216 / 1001], atol=1e-13))
    alpha = np.array([.973, .803])
    sigma = np.array([.037, .090])
    a = c * alpha
    check("published_alpha_requires_conversion_not_relabeling",
          not np.allclose(alpha, a))
    check("different_signs_despite_positive_alpha", a[0] > 0 > a[1])
    transformed_sigmas = abs(c) * sigma

    # This covariance has the published marginal errors and a CHOSEN rho.
    rho = .6
    calpha = np.outer(sigma, sigma) * np.array([[1, rho], [rho, 1]])
    d = np.diag(c)
    ca = d @ calpha @ d
    check("chosen_alpha_and_transformed_A_covariances_positive_definite",
          np.linalg.eigvalsh(calpha).min() > 0 and
          np.linalg.eigvalsh(ca).min() > 0)
    check("marginal_error_transformation", np.allclose(
        np.sqrt(np.diag(ca)), transformed_sigmas))
    rho_a = ca[0, 1] / np.sqrt(ca[0, 0] * ca[1, 1])
    check("correlation_sign_flip", np.isclose(rho_a, -rho))
    check("covariance_inverse_transform", np.allclose(
        np.linalg.solve(d, np.linalg.solve(d, ca.T).T), calpha))

    # A separate chosen comparison point: invariance tests a coordinate
    # change, not a Gaussian hypothesis or source significance.
    comparison = np.array([.90, .72])
    residual = alpha - comparison
    residual_a = d @ residual
    distance_alpha = float(residual @ np.linalg.solve(calpha, residual))
    distance_a = float(residual_a @ np.linalg.solve(ca, residual_a))
    check("Mahalanobis_distance_is_coordinate_invariant",
          np.isclose(distance_alpha, distance_a, atol=1e-13))
    check("covariance_determinant_transform",
          np.isclose(np.linalg.det(ca), np.linalg.det(d)**2 *
                     np.linalg.det(calpha), atol=1e-16))

    # Chosen full beta covariance tests normalization including fitted F.
    f = 1200.
    beta = np.r_[f, f * a]
    factor = np.array([[10., 0., 0.], [2., 8., 0.], [-3., 1., 7.]])
    cbeta = factor @ factor.T
    j = ratio_jacobian(beta)
    finite_difference = []
    for k in range(3):
        hi, lo = beta.copy(), beta.copy()
        hi[k] += .001
        lo[k] -= .001
        finite_difference.append((normalized_coefficients(hi) -
                                  normalized_coefficients(lo)) / .002)
    check("normalization_Jacobian_matches_finite_difference",
          np.allclose(j, np.array(finite_difference).T, atol=1e-12))
    check("global_scale_direction_is_null", np.allclose(j @ beta, 0))
    normalized_cov = j @ cbeta @ j.T
    truncated_cov = cbeta[1:, 1:] / f**2
    check("omitting_F_terms_changes_uncertainty",
          not np.allclose(normalized_cov, truncated_cov, atol=1e-12))
    check("normalization_invariant_to_joint_units_change", np.allclose(
        ratio_jacobian(7 * beta) @ (49 * cbeta) @
        ratio_jacobian(7 * beta).T, normalized_cov))

    # A semantic failure need not break the normalization/positivity checks.
    x, weights = legendre.leggauss(128)
    p = legendre.legvander(x, 4)[:, [2, 4]]
    w_correct = 1 + p @ a
    w_wrong = 1 + p @ alpha
    check("both_forms_have_unit_spherical_mean",
          np.isclose(weights @ w_correct / 2, 1) and
          np.isclose(weights @ w_wrong / 2, 1))
    # For even P2/P4, extremize the exact quartic in z=x*x on [0,1].
    def exact_minimum(coefficients):
        a2, a4 = coefficients
        quadratic = 35 * a4 / 8
        linear = 3 * a2 / 2 - 30 * a4 / 8
        constant = 1 - a2 / 2 + 3 * a4 / 8
        zs = [0., 1.]
        if quadratic != 0:
            vertex = -linear / (2 * quadratic)
            if 0 < vertex < 1:
                zs.append(vertex)
        return min(quadratic * z*z + linear * z + constant for z in zs)
    check("both_forms_can_be_nonnegative_on_full_interval",
          exact_minimum(a) > 0 and exact_minimum(alpha) > 0)
    angles = np.array([0., 90.])
    directions = legendre.legvander(np.cos(np.deg2rad(angles)), 4)[:, [2, 4]]
    check("semantic_error_changes_angular_prediction",
          np.max(abs(directions @ (a - alpha))) > .5)

    # If c is uncertain, fixed-D propagation is incomplete. A wholly
    # chosen independent c-error control demonstrates the additional term.
    cc = np.diag([.01**2, .02**2])
    with_c_error = ca + np.diag(alpha) @ cc @ np.diag(alpha)
    check("uncertain_maximum_requires_extra_covariance_terms",
          np.trace(with_c_error) > np.trace(ca))
    return {
        "kind": "L2 conditional convention transformation; no new source fit",
        "source_locators": ["Z83-1", "Z83-11", "Z83-12"],
        "published_alpha": alpha.tolist(),
        "published_statistical_marginal_errors": sigma.tolist(),
        "actual_source_rho": None,
        "task_pure_E2_maximum_coefficients": c.tolist(),
        "conditional_normalized_Aexp": a.tolist(),
        "conditional_Aexp_marginal_errors": transformed_sigmas.tolist(),
        "chosen_coordinate_control": {
            "rho_alpha_chosen": rho,
            "alpha_covariance_chosen": calpha.tolist(),
            "Aexp_covariance_transformed": ca.tolist(),
            "rho_Aexp_transformed": float(rho_a),
            "comparison_point_chosen": comparison.tolist(),
            "Mahalanobis_squared_alpha": distance_alpha,
            "Mahalanobis_squared_Aexp": distance_a},
        "chosen_normalization_control": {
            "F_chosen": f, "beta_chosen": beta.tolist(),
            "beta_covariance_chosen": cbeta.tolist(),
            "full_normalized_covariance": normalized_cov.tolist(),
            "omitted_F_covariance_counterfactual": truncated_cov.tolist()},
        "semantic_counterexample": {
            "angles_degrees": angles.tolist(),
            "conditional_correct_W": (1 + directions @ a).tolist(),
            "mistaken_alpha_as_A_W": (1 + directions @ alpha).tolist(),
            "correct_minimum_full_domain": exact_minimum(a),
            "mistaken_minimum_full_domain": exact_minimum(alpha)},
        "boundaries": [
            "Amax is task-derived for 13/2 to 9/2 pure E2 and point response, not a new measured table column.",
            "The published alpha marginal errors do not identify source rho or a joint confidence region.",
            "Chosen rho, comparison point, beta covariance and maximum-coefficient errors are not source measurements.",
            "If delta/spin/acceptance is uncertain, its nuisance and cross covariance must be retained.",
            "A detector attenuation coefficient and nuclear alpha are different factors; a general coincidence gate may require full joint response.",
            "Day15 remains an uncredited preview; formal DAY14 score and original deadline are unchanged."],
        "checks": checks, "checks_passed": len(checks)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = audit()
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"checks_passed": result["checks_passed"],
                      "all_checks_true": all(result["checks"].values()),
                      "output": str(args.output)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
