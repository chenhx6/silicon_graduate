#!/usr/bin/env python3
"""
feldman_cousins_unified_confidence_interval_calculator.py
=========================================================
Feldman-Cousins Unified Confidence Intervals with Physical Boundaries for Poisson &
Gaussian Observables in Nuclear and Particle Physics.

Physics & Statistical Formulation:
----------------------------------
1. Physical Boundary Constraint & Classical Neyman Dilemma:
   In counting experiments (e.g., rare decay, search for faint wobbling/chiral transitions,
   or dark matter/neutrino mass), the unknown signal parameter is bounded physically:
     mu >= 0
   When the observed count n is smaller than expected background b (downward fluctuation, n < b):
   - Classical central Neyman intervals yield negative signal mu < 0 or empty sets (null intervals).
   - "Flip-flopping" between reporting upper limits (when n ~ b) and two-sided intervals (when n >> b)
     causes severe undercoverage (true coverage probability drops well below the nominal CL).

2. Feldman-Cousins Likelihood Ratio Ordering (Unified Method):
   Feldman and Cousins (Phys. Rev. D 57, 3873, 1998) and Zhu Yongsheng (Ch. 11, 2006)
   resolve this by ordering the acceptance region using the generalized likelihood ratio:
     R(n | mu) = P(n | mu + b) / P(n | mu_best + b)
   where mu_best is the physically constrained Maximum Likelihood Estimator (MLE):
     mu_best = max(0, n - b)

3. Poisson Acceptance Interval & Confidence Belt:
   For a given mu >= 0 and known background b >= 0:
     P(n | mu + b) = (mu + b)^n * exp(-(mu + b)) / n!
   The ratio R(n | mu) is evaluated for all n = 0, 1, 2, ...
   Values of n are ranked in descending order of R(n | mu).
   Probabilities P(n | mu + b) are summed along the rank order until:
     sum_r P(n_r | mu + b) >= CL  (e.g., CL = 0.6827, 0.90, 0.95, 0.99)
   The accepted set of n forms the horizontal slice [n_lo(mu), n_hi(mu)] of the confidence belt.
   For an experimental observation n_obs, the confidence interval [mu_lo, mu_hi] is the union
   of all mu whose acceptance intervals contain n_obs:
     mu in [mu_lo, mu_hi]  <=>  n_obs in [n_lo(mu), n_hi(mu)]

4. Properties of the Unified Method:
   - Guaranteed exact coverage: Coverage probability is strictly >= nominal CL for all mu >= 0.
   - Smooth automatic transition:
       When n_obs <= b, mu_lo = 0.0 (reports upper limit without flip-flopping).
       When n_obs >> b, mu_lo > 0.0 (reports two-sided confidence interval).
   - Completely eliminates unphysical negative signal estimates and empty sets.

References:
  - G. J. Feldman and R. D. Cousins, Phys. Rev. D 57, 3873 (1998).
  - 朱永生, 《实验物理中的概率和统计（第二版）》, 科学出版社 (2006), 第11章 (小信号测量的区间估计, 印刷 pp. 370–383 / PDF pp. 386–399).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def _poisson_pmf(n: int, mean: float) -> float:
    """Calculates Poisson probability P(n | mean)."""
    if mean < 0.0 or n < 0:
        return 0.0
    if mean == 0.0:
        return 1.0 if n == 0 else 0.0
    try:
        return math.exp(float(n) * math.log(mean) - mean - math.lgamma(n + 1))
    except OverflowError:
        return 0.0


def calculate_poisson_fc_interval(
    n_obs: int,
    background: float,
    cl: float = 0.90,
    mu_max: float = 40.0,
    mu_step: float = 0.005,
    n_scan_max: int = 80
) -> Dict[str, Any]:
    """
    Computes exact Feldman-Cousins unified confidence interval [mu_lo, mu_hi]
    for Poisson process with known background b and observed count n_obs.
    """
    if n_obs < 0:
        raise ValueError("Observed counts n_obs must be a nonnegative integer.")
    if background < 0.0:
        raise ValueError("Background b must be nonnegative.")
    if not (0.0 < cl < 1.0):
        raise ValueError("Confidence level CL must be between 0 and 1.")

    in_belt_mu = []
    n_steps = int(round(mu_max / mu_step)) + 1

    for step_idx in range(n_steps):
        mu = step_idx * mu_step
        total_mean = mu + background

        # Calculate likelihood ratios for n = 0, 1, ..., n_scan_max
        r_list = []
        for n in range(n_scan_max):
            mu_best = max(0.0, float(n) - background)
            denom_mean = mu_best + background
            p_num = _poisson_pmf(n, total_mean)
            p_den = _poisson_pmf(n, denom_mean)
            ratio = (p_num / p_den) if p_den > 0.0 else 0.0
            r_list.append((ratio, n, p_num))

        # Sort descending by likelihood ratio
        r_list.sort(key=lambda item: item[0], reverse=True)

        # Accumulate until sum of probabilities reaches or exceeds CL
        cum_prob = 0.0
        accepted_n = set()
        for ratio, n, p in r_list:
            accepted_n.add(n)
            cum_prob += p
            if cum_prob >= cl - 1e-12:
                break

        if n_obs in accepted_n:
            in_belt_mu.append(mu)

    if not in_belt_mu:
        # Fallback if mu_max was too small
        mu_lo = max(0.0, float(n_obs) - background)
        mu_hi = mu_lo + 3.0 * math.sqrt(max(1.0, float(n_obs)))
        interval_type = "approximation_scan_exhausted"
    else:
        mu_lo = min(in_belt_mu)
        mu_hi = max(in_belt_mu)
        # If mu_lo is at the boundary (close to 0), snap to 0.0
        if mu_lo <= mu_step:
            mu_lo = 0.0
            interval_type = f"Upper Limit (at {int(round(cl*100))}% CL)"
        else:
            interval_type = f"Two-Sided Interval (at {int(round(cl*100))}% CL)"

    # Classical naive estimator and Poisson significance
    mu_mle_unconstrained = float(n_obs) - background
    mu_mle_physical = max(0.0, mu_mle_unconstrained)

    return {
        "n_obs": n_obs,
        "background_b": background,
        "confidence_level": cl,
        "mu_mle_unconstrained": round(mu_mle_unconstrained, 3),
        "mu_mle_physical": round(mu_mle_physical, 3),
        "fc_interval_lower": round(mu_lo, 3),
        "fc_interval_upper": round(mu_hi, 3),
        "interval_classification": interval_type,
        "is_upper_limit": (mu_lo == 0.0)
    }


def calculate_gaussian_fc_interval(
    x_obs: float,
    sigma: float = 1.0,
    cl: float = 0.90
) -> Dict[str, Any]:
    """
    Computes Feldman-Cousins unified confidence interval for Gaussian observable x ~ N(mu, sigma)
    with physical boundary mu >= 0 (Zhu Yongsheng §11.2.2, pp. 378-380; Feldman-Cousins 1998 Table X).
    """
    if sigma <= 0.0:
        raise ValueError("Gaussian standard deviation sigma must be positive.")
    if not (0.0 < cl < 1.0):
        raise ValueError("Confidence level CL must be between 0 and 1.")

    from scipy.optimize import brentq
    from scipy.special import ndtr, ndtri

    x_norm = x_obs / sigma
    z_two_sided = float(ndtri(0.5 + 0.5 * cl))
    z_one_sided = float(ndtri(cl))

    def _get_x1_x2(mu_val: float) -> Tuple[float, float]:
        if mu_val >= z_two_sided:
            return mu_val - z_two_sided, mu_val + z_two_sided
        if mu_val <= 1e-7:
            return -1e10, z_one_sided

        def eq_diff(x2):
            diff = x2 - mu_val
            x1 = 0.5 * mu_val - (diff ** 2) / (2.0 * mu_val)
            return ndtr(x2 - mu_val) - ndtr(x1 - mu_val) - cl

        x2_sol = float(brentq(eq_diff, mu_val, mu_val + z_two_sided + 2.0))
        x1_sol = 0.5 * mu_val - ((x2_sol - mu_val) ** 2) / (2.0 * mu_val)
        return x1_sol, x2_sol

    # Find mu_lo and mu_hi intersecting x_norm
    if x_norm <= z_one_sided:
        mu_lo = 0.0
    else:
        def eq_lo(mu_val):
            _, x2 = _get_x1_x2(mu_val)
            return x2 - x_norm
        mu_lo = float(brentq(eq_lo, 0.0, max(0.1, x_norm)))

    if x_norm < 0.0:
        def eq_hi(mu_val):
            x1, _ = _get_x1_x2(mu_val)
            return x1 - x_norm
        mu_hi = float(brentq(eq_hi, 0.001, z_two_sided))
    else:
        mu_hi = x_norm + z_two_sided

    return {
        "x_obs": x_obs,
        "sigma": sigma,
        "confidence_level": cl,
        "mu_fc_lower": round(mu_lo * sigma, 3),
        "mu_fc_upper": round(mu_hi * sigma, 3),
        "is_upper_limit": (mu_lo == 0.0),
        "classification": "Upper Limit" if mu_lo == 0.0 else "Two-Sided Interval"
    }


def format_text_report(poisson_res: Dict[str, Any], gauss_res: Optional[Dict[str, Any]] = None) -> str:
    lines = [
        "=" * 76,
        "   FELDMAN-COUSINS UNIFIED CONFIDENCE INTERVAL CALCULATOR",
        "   Based on Feldman & Cousins (1998) & Zhu Yongsheng Ch. 11 (2006)",
        "=" * 76,
        " POISSON COUNTING EXPERIMENT WITH PHYSICAL BOUNDARY (mu >= 0):",
        f"   Observed Counts n_obs       : {poisson_res['n_obs']}",
        f"   Expected Background b       : {poisson_res['background_b']:.3f}",
        f"   Confidence Level (CL)       : {int(round(poisson_res['confidence_level'] * 100))}%",
        f"   Unconstrained MLE (n - b)   : {poisson_res['mu_mle_unconstrained']:.3f}",
        f"   Physical MLE max(0, n - b)  : {poisson_res['mu_mle_physical']:.3f}",
        "-" * 76,
        f" FELDMAN-COUSINS UNIFIED INTERVAL [{int(round(poisson_res['confidence_level'] * 100))}% CL]:",
        f"   Signal Interval [mu_lo, mu_hi]: [{poisson_res['fc_interval_lower']:.3f}, {poisson_res['fc_interval_upper']:.3f}]",
        f"   Interval Classification     : {poisson_res['interval_classification']}",
        "-" * 76,
        " Methodological Significance:",
        "   - Eliminates classical Neyman empty sets and unphysical negative signal boundaries.",
        "   - Guarantees exact coverage without 'flip-flopping' between upper limit and two-sided.",
        "   - Automatically reports Upper Limit when n_obs <= b, and Two-Sided when n_obs > b.",
    ]

    if gauss_res is not None:
        lines.extend([
            "-" * 76,
            " GAUSSIAN OBSERVABLE WITH BOUNDARY CONSTRAINT (x ~ N(mu, sigma), mu >= 0):",
            f"   Observed Value x_obs        : {gauss_res['x_obs']:.3f} (sigma = {gauss_res['sigma']:.3f})",
            f"   Feldman-Cousins Interval    : [{gauss_res['mu_fc_lower']:.3f}, {gauss_res['mu_fc_upper']:.3f}] ({gauss_res['classification']})",
        ])

    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Feldman-Cousins Unified Confidence Interval Calculator"
    )
    parser.add_argument("--n-obs", "-n", type=int, default=0, help="Observed count n_obs (default: 0)")
    parser.add_argument("--background", "-b", type=float, default=3.0, help="Expected background b (default: 3.0)")
    parser.add_argument("--cl", type=float, default=0.90, help="Confidence Level CL (default: 0.90 for 90%% CL)")
    parser.add_argument("--preset", type=str, default=None,
                        choices=["rare_decay_0", "faint_peak_2", "significant_6", "gaussian_neg"],
                        help="Benchmark preset")
    parser.add_argument("--gaussian-x", type=float, default=None, help="Evaluate Gaussian observable x")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")

    args = parser.parse_args()

    n_val = args.n_obs
    b_val = args.background
    cl_val = args.cl
    gx_val = args.gaussian_x

    if args.preset == "rare_decay_0":
        n_val, b_val, cl_val = 0, 3.0, 0.90
    elif args.preset == "faint_peak_2":
        n_val, b_val, cl_val = 2, 3.0, 0.90
    elif args.preset == "significant_6":
        n_val, b_val, cl_val = 6, 3.0, 0.90
    elif args.preset == "gaussian_neg":
        n_val, b_val, cl_val = 0, 3.0, 0.90
        gx_val = -1.5

    p_res = calculate_poisson_fc_interval(n_obs=n_val, background=b_val, cl=cl_val)
    g_res = None
    if gx_val is not None:
        g_res = calculate_gaussian_fc_interval(x_obs=gx_val, sigma=1.0, cl=cl_val)

    if args.json:
        out = {"poisson_feldman_cousins": p_res}
        if g_res is not None:
            out["gaussian_feldman_cousins"] = g_res
        print(json.dumps(out, indent=2))
    else:
        print(format_text_report(p_res, g_res))


if __name__ == "__main__":
    main()
