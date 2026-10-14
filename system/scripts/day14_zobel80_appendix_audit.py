#!/usr/bin/env python3
"""Primary-transcription and conditional statistical controls for Zobel1980.

This audits the supplied p231 print against ratio propagation and the
Gaussian density of Eq.A4. It does not recover experimental covariance,
correct a published dataset, or attest an official erratum.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

from day14_angular_coefficient_conventions import (
    normalized_coefficients, ratio_jacobian)


def gaussian_joint_threshold(probability):
    return -2 * math.log1p(-probability)


def sign_mismatched_ellipse_coverage(rho, threshold, n=512):
    # Whiten the ACTUAL chosen covariance. The wrong-sign ellipse then
    # has eigenvalues (1+rho)/(1-rho) and its reciprocal. Conditional on
    # standard-normal polar angle, the squared radius is chi-square2.
    points, weights = leggauss(n)
    phi = math.pi * (points + 1)
    lam = (1 + rho) / (1 - rho)
    u = lam * np.cos(phi)**2 + np.sin(phi)**2 / lam
    return float(weights @ (-np.expm1(-threshold / (2 * u))) / 2)


def audit(fixture):
    checks = {}

    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            raise AssertionError(name)

    check("actual_source_covariance_kept_unknown", fixture["rho_source"] is None)
    c = np.array([40 / 91, -216 / 1001])
    al = np.array([fixture["alpha2"], fixture["alpha4"]])
    ae = np.array([fixture["a2"], fixture["a4"]])
    sa = np.array([fixture["sigma_a2"], fixture["sigma_a4"]])
    sal = np.array([fixture["sigma_alpha2"], fixture["sigma_alpha4"]])
    check("source_table_central_columns_match_c_to_printed_rounding",
          np.max(abs(ae - c * al)) < .0005)
    check("source_table_error_columns_match_absolute_c_to_printed_rounding",
          np.max(abs(sa - abs(c) * sal)) < .0005)
    check("literal_A3_negative_c_requires_absolute_error_convention",
          (sa / c)[1] < 0 < (sa / abs(c))[1])

    beta = np.array([1000., 300., -100.])
    cb = np.array([[100., 30., -10.], [30., 25., 2.], [-10., 2., 16.]])
    check("chosen_full_beta_covariance_positive_definite",
          np.linalg.eigvalsh(cb).min() > 0)
    a = normalized_coefficients(beta)
    j = ratio_jacobian(beta)
    ca = j @ cb @ j.T
    rho0 = cb[0, 1:] / np.sqrt(cb[0, 0] * np.diag(cb)[1:])
    relative0 = math.sqrt(cb[0, 0]) / beta[0]
    relativek = np.sqrt(np.diag(cb)[1:]) / beta[1:]
    correct = a*a * (relative0**2 + relativek**2 -
                     2 * rho0 * relative0 * relativek)
    literal_A2 = a*a * (relative0**2 + relativek**2 - 2 * rho0)
    check("ratio_variance_formula_equals_matrix_Jacobian",
          np.allclose(correct, np.diag(ca), atol=1e-15))
    check("literal_A2_has_negative_variance_in_positive_covariance_control",
          literal_A2[0] < 0 < correct[0])
    independent = cb.copy()
    independent[0, 1:] = independent[1:, 0] = 0
    no_correlation = j @ independent @ j.T
    literal_at_zero_rho = a*a * (relative0**2 + relativek**2)
    check("zero_b0_correlation_control_restores_A2_agreement",
          np.allclose(literal_at_zero_rho, np.diag(no_correlation)))
    zero_mean = beta.copy()
    zero_mean[1] = 0
    zero_cov = ratio_jacobian(zero_mean) @ cb @ ratio_jacobian(zero_mean).T
    check("zero_mean_coefficient_has_finite_Jacobian_uncertainty",
          np.isclose(zero_cov[0, 0], cb[1, 1] / beta[0]**2))

    # A6 coefficients represent HALF the Mahalanobis quadratic if its
    # cross coefficient is -D*cov. The supplied scan instead prints +D*cov.
    sigma = np.array([.03, .06])
    rho = .6
    cov = np.outer(sigma, sigma) * np.array([[1, rho], [rho, 1]])
    determinant = np.linalg.det(cov)
    half_matrix = np.array([[cov[1, 1], -cov[0, 1]],
                            [-cov[0, 1], cov[0, 0]]]) / (2 * determinant)
    literal_matrix = half_matrix.copy()
    literal_matrix[0, 1] *= -1
    literal_matrix[1, 0] *= -1
    check("correct_A6_polynomial_equals_half_inverse_covariance",
          np.allclose(half_matrix, np.linalg.inv(cov) / 2))
    residual = np.array([.03, .06])
    h = float(residual @ np.linalg.solve(cov, residual))
    literal_half = float(residual @ literal_matrix @ residual)
    check("literal_A6_cross_sign_differs_from_A4_density",
          not np.isclose(literal_half, h / 2))
    check("literal_A6_equivalent_to_opposite_correlation", np.allclose(
        literal_matrix, np.linalg.inv(np.diag([1, -1]) @ cov @
                                     np.diag([1, -1])) / 2))
    diagonal = np.diag(sigma*sigma)
    check("zero_correlation_A6_sign_control_is_identical", np.allclose(
        np.diag(np.diag(half_matrix)) * (1-rho*rho),
        np.linalg.inv(diagonal) / 2))

    probability = .68
    q68 = gaussian_joint_threshold(probability)
    half_radius = -math.log1p(-probability)
    check("A5_half_radius_matches_consistent_A6",
          np.isclose(q68 / 2, half_radius))
    check("correct_joint_contour_has_target_Gaussian_content",
          np.isclose(-math.expm1(-q68 / 2), probability))
    factor2_failure = -math.expm1(-half_radius / 2)
    check("half_radius_used_as_full_Q_has_wrong_content",
          abs(factor2_failure - probability) > .2)
    one_radius_content = -math.expm1(-.5)
    independent_rectangle_content = math.erf(1/math.sqrt(2))**2
    check("unit_Mahalanobis_contour_is_not_joint68percent",
          abs(one_radius_content - probability) > .2)
    check("independent_plusminus1sigma_rectangle_is_not_joint68percent",
          abs(independent_rectangle_content - probability) > .2)
    wrong_coverage = sign_mismatched_ellipse_coverage(rho, q68)
    wrong_high = sign_mismatched_ellipse_coverage(rho, q68, 1024)
    check("polar_quadrature_converges_for_wrong_sign_ellipse",
          np.isclose(wrong_coverage, wrong_high, atol=1e-12))
    check("wrong_cross_sign_changes_joint_content_under_actual_covariance",
          abs(wrong_coverage - probability) > .05)

    # Ellipse/rectangle area comparison is not an inclusion theorem.
    area_ratios = {str(p): math.pi * q68 * math.sqrt(1-p*p) / 4
                   for p in [0., .6, .95]}
    check("joint68_ellipse_need_not_have_larger_area_than_errorbar_rectangle",
          area_ratios["0.0"] > 1 and area_ratios["0.95"] < 1)
    opposite_rectangle_corner = np.array([sigma[0], -sigma[1]])
    check("an_errorbar_rectangle_corner_can_lie_outside_joint68_ellipse",
          opposite_rectangle_corner @ np.linalg.solve(
              cov, opposite_rectangle_corner) > q68)
    ellipse_projection_point = math.sqrt(q68) * cov[:, 0] / sigma[0]
    check("joint68_ellipse_can_extend_outside_errorbar_rectangle",
          np.isclose(ellipse_projection_point @ np.linalg.solve(
              cov, ellipse_projection_point), q68) and
          ellipse_projection_point[0] > sigma[0])
    return {
        "kind": "L2 primary appendix transcription versus mathematical controls",
        "source_row": fixture,
        "chosen_beta_control": {
            "beta": beta.tolist(), "covariance": cb.tolist(),
            "normalized_a": a.tolist(), "normalized_covariance": ca.tolist(),
            "correct_ratio_variances": correct.tolist(),
            "literal_printed_A2_variances": literal_A2.tolist()},
        "chosen_ellipse_control": {
            "sigma": sigma.tolist(), "rho": rho, "covariance": cov.tolist(),
            "A4_Q_at_chosen_residual": h,
            "literal_A6_polynomial_at_same_residual": literal_half,
            "correct_A6_polynomial_at_same_residual": h/2,
            "joint_probability": probability, "full_Q_threshold": q68,
            "A5_half_radius_squared": half_radius,
            "wrong_sign_ellipse_actual_content": wrong_coverage,
            "wrong_sign_ellipse_content_1024_nodes": wrong_high,
            "half_radius_used_as_full_Q_content": factor2_failure,
            "unit_Q_contour_content": one_radius_content,
            "independent_1sigma_rectangle_content": independent_rectangle_content,
            "ellipse_over_rectangle_area_for_chosen_rhos": area_ratios},
        "boundaries": [
            "The supplied primary print is transcribed literally; no official erratum is attested.",
            "General covariance/ellipse statement Z80-12 remains supported; exact formulas require this self-audit.",
            "A5 is consistent with a HALF-Mahalanobis radius when the quadratic coefficients and cross sign are matched.",
            "All beta/covariance/rho/residual/coverage controls are chosen, not the experimental covariance or ALY significance.",
            "Source data selection is a matched single transition; no full17row hypothesis test is claimed.",
            "Published rounded a/error columns corroborate the variable/sign convention, not independent sampling.",
            "Day15 remains a partial uncredited preview; formal DAY14 score remains21/24."],
        "checks": checks, "checks_passed": len(checks)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = audit(json.loads(args.fixture.read_text()))
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"checks_passed": result["checks_passed"],
                      "all_checks_true": all(result["checks"].values()),
                      "output": str(args.output)}))


if __name__ == "__main__":
    main()
