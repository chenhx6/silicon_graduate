#!/usr/bin/env python3
"""Source-parameter audit of RZ17's probability-measure and tail boundaries.

The declared joint Gaussian pushforward is a separate statistical construction
from the unspecified RooFit convolution implementation. Neither is a fresh
experimental determination of the 251Fm mixing ratio.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import brentq
from scipy.special import ndtr
from scipy.integrate import quad


class Pushforward:
    def __init__(self, cfg: dict, order: int, theory_errors: bool = True):
        source = cfg["source_case"]
        self.e, self.se = source["alpha_exp"]
        m1, s1 = source["alpha1"]
        m2, s2 = source["alpha2"]
        if not theory_errors:
            s1 = s2 = 0.0
            order = 1
        nodes, weights = np.polynomial.hermite.hermgauss(order)
        a1, a2 = m1 + math.sqrt(2) * s1 * nodes, m2 + math.sqrt(2) * s2 * nodes
        self.a1, self.a2 = np.meshgrid(a1, a2, indexing="ij")
        self.w = np.outer(weights, weights) / math.pi
        assert np.all(self.a1 > self.a2) and np.all(self.a2 > 0)
        self.difference = self.a1 - self.a2
        self.upper_cdf = ndtr((self.a1 - self.e) / self.se)
        self.lower_cdf = ndtr((self.a2 - self.e) / self.se)
        self.z = float(np.sum(self.w * (self.upper_cdf - self.lower_cdf)))

    def gaussian(self, x):
        return np.exp(-0.5 * ((x - self.e) / self.se)**2) / (self.se * math.sqrt(2 * math.pi))

    def alpha(self, delta: float):
        return self.a2 + self.difference / (1 + delta * delta)

    def cdf(self, delta: float) -> float:
        cdf = float(np.sum(self.w * (self.upper_cdf - ndtr((self.alpha(delta) - self.e) / self.se))) / self.z)
        return cdf

    def pdf(self, delta: float) -> float:
        jacobian = 2 * delta * self.difference / (1 + delta * delta)**2
        return float(np.sum(self.w * self.gaussian(self.alpha(delta)) * jacobian) / self.z)

    def quantile(self, probability: float) -> float:
        assert 0 < probability < 1
        theta = brentq(lambda t: self.cdf(math.tan(t)) - probability, 0.0,
                       math.pi / 2 - 1e-9, xtol=1e-13)
        return math.tan(theta)

    def moment(self, exponent: int, order: int, cutoff: float | None = None) -> float:
        xs, ws = np.polynomial.legendre.leggauss(order)
        end = math.pi / 2 if cutoff is None else math.atan(cutoff)
        ts = (xs + 1) * end / 2
        result = 0.0
        for t, weight in zip(ts, ws):
            sn, cs = math.sin(t), math.cos(t)
            alpha = self.a1 * cs * cs + self.a2 * sn * sn
            # p(delta)d(delta)=G(alpha)*2(A1-A2)sin(t)cos(t)dt.
            power_weight = sn**(exponent + 1) * cs**(1 - exponent)
            result += weight * float(np.sum(self.w * self.gaussian(alpha)
                                            * 2 * self.difference * power_weight))
        return float(result * end / (2 * self.z))

    def tail_coefficient(self) -> float:
        # lim_delta->infinity delta^3 p(delta).
        return float(np.sum(self.w * self.gaussian(self.a2) * 2 * self.difference) / self.z)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.input.read_text())
    assert cfg["identity"] == "DAY16-RZ17-PDF-MEASURE-01"
    source, design = cfg["source_case"], cfg["numeric_design"]
    m1, s1 = source["alpha1"]
    m2, s2 = source["alpha2"]
    e, se = source["alpha_exp"]
    central = math.sqrt((m1 - e) / (e - m2))
    convergence = []
    for h in design["gauss_hermite_orders"]:
        p = Pushforward(cfg, h)
        for n in design["gauss_legendre_theta_orders"]:
            convergence.append({"Hermite_order": h, "Legendre_order": n,
                                "physical_domain_probability": p.z,
                                "conditional_mean_abs_delta": p.moment(1, n),
                                "normalization_check": p.moment(0, n)})
    p = Pushforward(cfg, max(design["gauss_hermite_orders"]))
    fixed = Pushforward(cfg, 1, theory_errors=False)
    mean = p.moment(1, max(design["gauss_legendre_theta_orders"]))
    fixed_mean = fixed.moment(1, max(design["gauss_legendre_theta_orders"]))
    fm = p.cdf(mean)
    author_style_interval = [p.quantile(fm - 0.34), p.quantile(fm + 0.34)]
    equal_tail_interval = [p.quantile(0.16), p.quantile(0.84)]
    nodes, weights = np.polynomial.hermite.hermgauss(40)
    w = weights / math.sqrt(math.pi)
    partial1 = np.sqrt((m1 + math.sqrt(2) * s1 * nodes - e) / (e - m2))
    partial2 = np.sqrt((m1 - e) / (e - (m2 + math.sqrt(2) * s2 * nodes)))
    p1_mean, p2_mean = float(w @ partial1), float(w @ partial2)
    sum_mean = p1_mean + p2_mean + fixed_mean
    # Two-parameter uncertainty band of source Eq17, no extra exp uncertainty
    # is added into it; the intersections use the exp margin separately.
    def band(theta: float, sign: int) -> float:
        sn2, cs2 = math.sin(theta)**2, math.cos(theta)**2
        return m1 * cs2 + m2 * sn2 + sign * math.hypot(s1 * cs2, s2 * sn2)
    lower = math.tan(brentq(lambda t: band(t, -1) - (e + se), 0.0, math.pi / 2))
    upper = math.tan(brentq(lambda t: band(t, +1) - (e - se), 0.0, math.pi / 2))
    graphical_probability = p.cdf(upper) - p.cdf(lower)
    reported_bounds = [source["published_mean"][0] + source["published_mean"][1],
                       source["published_mean"][0] + source["published_mean"][2]]
    reported_bounds_probability = p.cdf(reported_bounds[1]) - p.cdf(reported_bounds[0])
    reported_mean_cdf = p.cdf(source["published_mean"][0])
    tail = p.tail_coefficient()
    # Independent change of variables: X=A1-E, Y=E-A2, q=X/Y.
    # Independent original alphas still give Cov(X,Y)=-Var(E).
    mean_xy = np.array([m1 - e, e - m2])
    covariance_xy = np.array([[s1*s1 + se*se, -se*se],
                              [-se*se, se*se + s2*s2]])
    precision_xy = np.linalg.inv(covariance_xy)
    det_xy = float(np.linalg.det(covariance_xy))

    def gaussian_ratio_pdf(delta: float) -> float:
        ray = np.array([delta*delta, 1.0])
        aa = float(ray @ precision_xy @ ray)
        bb = float(ray @ precision_xy @ mean_xy)
        cc = float(mean_xy @ precision_xy @ mean_xy)
        integral = (math.exp(-cc/2) / aa
                    + bb/aa * math.sqrt(2*math.pi/aa)
                    * math.exp(-(cc-bb*bb/aa)/2) * float(ndtr(bb/math.sqrt(aa))))
        return 2*delta * integral / (2*math.pi*math.sqrt(det_xy)*p.z)

    ratio_comparison = []
    for delta in [0.01, 0.1, 0.3, 0.8, 1.0, 2.0, 10.0, 100.0]:
        exact, gh = gaussian_ratio_pdf(delta), p.pdf(delta)
        ratio_comparison.append({"delta": delta, "joint_bivariate_ratio_pdf": exact,
                                 "theory_GH_pushforward_pdf": gh,
                                 "absolute_difference": abs(exact-gh)})
    assert max(x["absolute_difference"] for x in ratio_comparison) < 1e-10
    cutoffs = []
    for cutoff in design["delta_cutoffs"]:
        cutoffs.append({"maximum_delta": cutoff, "probability_below_cutoff": p.cdf(cutoff),
                        "first_moment_partial_not_renormalized": p.moment(1, 640, cutoff),
                        "second_moment_partial_not_renormalized": p.moment(2, 640, cutoff),
                        "flat_delta_likelihood_integral_to_cutoff": quad(
                            lambda value: float(fixed.gaussian(fixed.alpha(value))[0, 0]),
                            0.0, cutoff, points=[x for x in [central, 2, 5, 10, 30, 100, 300]
                                                  if x < cutoff], epsabs=1e-10)[0]})
    # A flat-delta prior multiplies a likelihood that tends to a strictly
    # positive constant. Its normalization on [0,infinity) does not exist.
    likelihood_tail = math.exp(-0.5 * ((m2 - e) / se)**2) / (se * math.sqrt(2 * math.pi))
    rng = np.random.default_rng(design["seed"])
    a1 = rng.normal(m1, s1, design["MC_draws"])
    a2 = rng.normal(m2, s2, design["MC_draws"])
    exp = rng.normal(e, se, design["MC_draws"])
    keep = (a1 > exp) & (exp > a2) & (a2 > 0)
    samples = np.sqrt((a1[keep] - exp[keep]) / (exp[keep] - a2[keep]))
    observed_acceptance = float(keep.mean())
    mc_error = math.sqrt(p.z * (1 - p.z) / design["MC_draws"])
    mc_quantiles = np.quantile(samples, [0.16, 0.5, 0.84])
    mc_mean = float(samples.mean())
    mc_mean_error_estimate = float(samples.std(ddof=1) / math.sqrt(len(samples)))
    assert abs(observed_acceptance - p.z) < 5 * mc_error
    assert max(abs(mc_quantiles[[0, 2]] - np.array(equal_tail_interval))) < 0.01
    assert abs(p.moment(0, 320) - 1) < 1e-12
    assert abs(mean - convergence[-2]["conditional_mean_abs_delta"]) < 1e-10
    assert sum_mean - mean > 1.0
    assert all(p.pdf(x) > 0 for x in [0.1, 1.0, 10.0, 100.0])
    result = {
        "identity": cfg["identity"],
        "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "arithmetic_inverse_abs_delta": central,
        "joint_Gaussian_physical_domain_probability": p.z,
        "joint_pushforward_conditional_mean_abs_delta": mean,
        "joint_cdf_at_mean": fm,
        "joint_34percent_each_side_mean_interval": author_style_interval,
        "joint_equal_tailed_16_84_interval": equal_tail_interval,
        "source_graphical_Eq17_intersections": [lower, upper],
        "source_graphical_interval_probability_under_declared_joint": graphical_probability,
        "source_analytical_printed_bounds": reported_bounds,
        "source_analytical_printed_bounds_probability_under_declared_joint": reported_bounds_probability,
        "probability_left_right_of_reported_mean_within_printed_bounds": [
            reported_mean_cdf - p.cdf(reported_bounds[0]),
            p.cdf(reported_bounds[1]) - reported_mean_cdf],
        "partialPDF_means_P1_P2_Pexp": [p1_mean, p2_mean, fixed_mean],
        "ordinary_convolution_mean_of_positive_partials": sum_mean,
        "ordinary_convolution_shift_required_to_match_joint_mean": sum_mean - mean,
        "zero_theory_error_control": {"Pexp_mean": fixed_mean,
            "joint_minus_Pexp_mean": mean - fixed_mean,
            "ordinary_convolution_zero_theory_error_mean": 2 * central + fixed_mean,
            "meaning": "delta-like P1 and P2 at positive delta0 add two shifts under an ordinary convolution, rather than acting as zero-centered error kernels."},
        "tail": {"lim_delta_cubed_Pdelta": tail,
            "asymptotic_density": "P(delta) ~ tail_coefficient/delta^3",
            "mean_finite": True, "second_moment_finite": False,
            "logarithmic_second_moment_growth_per_log_cutoff": tail,
            "flat_delta_Gaussian_likelihood_limit_at_infinity": likelihood_tail,
            "flat_delta_prior_posterior_proper_without_cutoff": False},
        "independent_bivariate_ratio_check": {
            "X_Y_means": mean_xy.tolist(), "X_Y_covariance": covariance_xy.tolist(),
            "correlation_X_Y": float(covariance_xy[0, 1] / math.sqrt(
                covariance_xy[0, 0]*covariance_xy[1, 1])),
            "identity": "p(delta)=2delta/Z * integral_0^infinity y f_XY(delta^2*y,y)dy; shared measured E gives Cov(X,Y)=-sigma_E^2.",
            "alpha2_positive_boundary": "Gaussian P(alpha2<0) is below1e-700 for this frozen example; the bivariate reduction does not impose this negligible extra cut.",
            "samples": ratio_comparison},
        "cutoff_checks": cutoffs, "quadrature_convergence": convergence,
        "Monte_Carlo": {"seed": design["seed"], "draws": design["MC_draws"] ,
            "accepted": int(keep.sum()), "physical_fraction": observed_acceptance,
            "physical_fraction_standard_error": mc_error,
            "quantiles_16_50_84": mc_quantiles.tolist(), "sample_mean": mc_mean,
            "naive_sample_mean_standard_error_not_a_finite_variance_guarantee": mc_mean_error_estimate},
        "all_internal_checks_passed": True, "new_measured_delta": False,
        "source_RooFit_recipe_recovered": False,
        "boundary": "The printed Eq14 symbol does not specify centering, support shifts, FFT range or RooFit recipe. Literal ordinary convolution fails this mean invariant; direct joint Gaussian pushforward is an explicitly defined alternative, not an assertion about unpublished author code or true experimental coverage."}
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    print(json.dumps({k: result[k] for k in result if k not in ["quadrature_convergence", "cutoff_checks"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
