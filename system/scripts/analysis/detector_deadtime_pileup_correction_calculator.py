#!/usr/bin/env python3
"""Ideal constant-dead-time models for stationary Poisson arrivals.

Nonparalyzable means nonextendable: m = n / (1 + n*tau).
Paralyzable means extendable: m = n * exp(-n*tau).
Here n is the input pulse rate and m the accepted rate, not a source activity.

The historical ``hybrid`` API retains q/(1 + q*tau_N), q=n*exp(-n*tau_P),
as a Poissonized approximation only. An actual upstream dead-time filter does
not produce a Poisson process, so this is not an exact cascade formula.
The pileup diagnostic assumes an isolation window of total duration 2*T_p;
it does not predict a full-energy peak rate or combine losses from all stages.

Local evidence and audit locators:
  knowledge/concepts/reconciliation-of-detector-dead-time-and-pulse-pileup.md
  Wu, Experimental Methods, printed pp. 23-25 (PDF pp. 31-33).
  Nakhostin, local Chinese translation, PDF/printed pp. 215-218.
"""

import math
import json
import argparse
from decimal import Decimal, localcontext
from typing import Dict, Any


def _finite(value, name):
    try:
        value = float(value)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError(f"{name} must be finite") from exc
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")
    return value


def _nonnegative(value, name):
    value = _finite(value, name)
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")
    return value


def _bisect_increasing(function, lower, upper, tol, max_iter):
    for _ in range(max_iter):
        middle = lower + (upper - lower) / 2
        if middle == lower or middle == upper:
            return middle
        residual = function(middle)
        if residual == 0 or upper - lower <= tol * abs(middle):
            return middle
        if residual < 0:
            lower = middle
        else:
            upper = middle
    raise RuntimeError("Lambert W bisection did not converge")


def _branch_loss(displacement):
    # s - log(1+s) loses precision close to the double root s=0.
    if abs(displacement) < 0.01:
        return math.fsum((-displacement) ** k / k for k in range(2, 18))
    return displacement - math.log1p(displacement)


def _negative_w_displacement(target, branch, tol, max_iter):
    if branch == 0:
        return _bisect_increasing(
            lambda s: target - _branch_loss(s), -0.9, 0.0, tol, max_iter)
    return _bisect_increasing(
        lambda s: _branch_loss(s) - target, 0.0, max(1.0, 2 * (target + 1)),
        tol, max_iter)


def lambert_w_eval(x: float, branch: int = 0, tol: float = 1e-13, max_iter: int = 100) -> float:
    """Real W_0 or W_-1 using monotone brackets, without SciPy.

    W_-1(0) has no finite real value and raises ValueError. The binary64
    representation of -1/e is treated as the shared endpoint W=-1.
    tol bounds bracket width relative to the root (displacement near -1),
    rather than an absolute residual that can falsely accept tiny arguments.
    """
    x = _finite(x, "x")
    tol = _finite(tol, "tol")
    if branch not in (0, -1):
        raise ValueError("Only branch 0 and -1 are supported")
    if tol <= 0 or not isinstance(max_iter, int) or max_iter <= 0:
        raise ValueError("tol and integer max_iter must be positive")
    endpoint = -1 / math.e
    if x < endpoint or (branch == -1 and x >= 0):
        raise ValueError("x is outside the selected real Lambert W branch")
    if x == endpoint:
        return -1.0
    if x == 0:
        return 0.0
    if x > 0:
        if x < 1:
            return _bisect_increasing(
                lambda w: w * math.exp(w) - x, x / (1 + x), x, tol, max_iter)
        log_x = math.log(x)
        return _bisect_increasing(
            lambda w: w + math.log(w) - log_x,
            0.5, max(1.0, log_x + 1), tol, max_iter)

    q = -x
    if branch == 0 and q < 0.25:
        root = _bisect_increasing(
            lambda r: r * math.exp(-r) - q, q, min(1.0, math.e * q),
            tol, max_iter)
        return -root
    if q > 0.35:
        # log(q)+1 rounds away the distance from the branch point.
        with localcontext() as context:
            context.prec = 60
            target = float(-Decimal.from_float(q).ln() - 1)
    else:
        target = -math.log(q) - 1
    displacement = _negative_w_displacement(target, branch, tol, max_iter)
    return -(1 + displacement)


def _nonparalyzable(rate, tau):
    exposure = rate * tau
    if math.isinf(exposure):
        return 1 / tau, 0.0, 1.0
    live = 1 / (1 + exposure)
    return rate * live, live, exposure * live


def _attenuated_rate(rate, exposure):
    fraction = math.exp(-exposure)
    if fraction or rate == 0 or math.isinf(exposure):
        return rate * fraction
    # exp(-exposure) can underflow although rate*exp(-exposure) is representable.
    return math.exp(math.log(rate) - exposure)


def calculate_deadtime_models(
    true_rate: float,
    tau_nonpar: float,
    tau_par: float,
    tau_hybrid_p: float,
    tau_hybrid_n: float,
    peaking_time: float
) -> Dict[str, Any]:
    """
    Calculate ideal pulse acceptance and a separately reported pileup diagnostic.

    All inputs must be finite and nonnegative, with times in seconds.
    At zero input, live/acceptance fractions use their continuous limit of 1.
    The hybrid live_time_fraction key is retained as an acceptance fraction;
    it is not a calibrated instrument wall-clock live time.
    """
    n = _nonnegative(true_rate, "true_rate")
    tau_nonpar = _nonnegative(tau_nonpar, "tau_nonpar")
    tau_par = _nonnegative(tau_par, "tau_par")
    tau_hybrid_p = _nonnegative(tau_hybrid_p, "tau_hybrid_p")
    tau_hybrid_n = _nonnegative(tau_hybrid_n, "tau_hybrid_n")
    peaking_time = _nonnegative(peaking_time, "peaking_time")

    m_np, livetime_np, loss_np = _nonparalyzable(n, tau_nonpar)
    p_exposure = n * tau_par
    livetime_p = math.exp(-p_exposure)
    m_p = _attenuated_rate(n, p_exposure)
    m_p_max = (1 / math.e) / tau_par if tau_par > 0 else None
    n_crit_p = 1 / tau_par if tau_par > 0 else None
    is_saturated_par = p_exposure > 1

    hybrid_exposure = n * tau_hybrid_p
    exp_p = math.exp(-hybrid_exposure)
    upstream_rate = _attenuated_rate(n, hybrid_exposure)
    m_hybrid, downstream_live, downstream_loss = _nonparalyzable(upstream_rate, tau_hybrid_n)
    livetime_hybrid = exp_p * downstream_live
    loss_hybrid = -math.expm1(-hybrid_exposure) + exp_p * downstream_loss

    isolation_exposure = 2 * (n * peaking_time)
    pileup_prob = -math.expm1(-isolation_exposure)
    clean_peak_rate = _attenuated_rate(n, isolation_exposure)

    return {
        "true_rate_cps": n,
        "non_paralyzable": {
            "tau_sec": tau_nonpar,
            "observed_rate_cps": m_np,
            "fractional_loss": loss_np,
            "live_time_fraction": livetime_np
        },
        "paralyzable": {
            "tau_sec": tau_par,
            "observed_rate_cps": m_p,
            "max_possible_rate_cps": m_p_max,
            "critical_true_rate_cps": n_crit_p,
            "saturation_status": "unbounded-identity" if tau_par == 0 else ("saturated" if is_saturated_par else "unsaturated"),
            "fractional_loss": -math.expm1(-p_exposure),
            "live_time_fraction": livetime_p,
            "is_in_saturated_regime": is_saturated_par
        },
        "hybrid": {
            "model_status": "poissonized-cascade-approximation",
            "assumptions": "Stationary Poisson input; downstream input re-Poissonized at q=n*exp(-n*tau_P).",
            "live_time_fraction_interpretation": "Approximate input-pulse acceptance, not measured wall-clock live time.",
            "tau_paralyzable_sec": tau_hybrid_p,
            "tau_nonparalyzable_sec": tau_hybrid_n,
            "observed_rate_cps": m_hybrid,
            "fractional_loss": loss_hybrid,
            "live_time_fraction": livetime_hybrid
        },
        "pileup_diagnostics": {
            "model_status": "ideal-Poisson-isolation-window",
            "assumptions": "No other input pulses in a window of total duration 2*peaking_time.",
            "clean_peak_rate_interpretation": "Isolated input pulses only; full-energy efficiency and DAQ losses excluded.",
            "peaking_time_sec": peaking_time,
            "pileup_loss_fraction": pileup_prob,
            "clean_peak_rate_cps": clean_peak_rate
        }
    }


def invert_observed_rate(
    observed_rate: float,
    tau_nonpar: float,
    tau_par: float
) -> Dict[str, Any]:
    """
    Inverts measured count rate m to find true rate n under non-paralyzable
    and paralyzable assumptions, demonstrating the critical dual-root pitfall.
    """
    m = _nonnegative(observed_rate, "observed_rate")
    tau_nonpar = _nonnegative(tau_nonpar, "tau_nonpar")
    tau_par = _nonnegative(tau_par, "tau_par")

    if tau_nonpar > 0 and (m >= 1 / tau_nonpar or m * tau_nonpar >= 1):
        n_np = None
        np_valid = False
        np_status = "asymptotic-limit-exceeded"
    else:
        n_np = m / (1.0 - m * tau_nonpar)
        np_valid = True
        np_status = "unique-real-root"

    m_max = (1 / math.e) / tau_par if tau_par > 0 else None
    if tau_par == 0:
        p_valid, root1, root2, root_status = True, m, None, "identity-no-deadtime"
    elif m == 0:
        p_valid, root1, root2, root_status = True, 0.0, None, "unique-finite-zero-root"
    elif m_max is not None and m > m_max:
        p_valid = False
        root1 = None
        root2 = None
        root_status = "outside-model-range"
    elif m_max is not None and m == m_max:
        p_valid, root1, root2, root_status = True, 1 / tau_par, 1 / tau_par, "coalesced"
    else:
        p_valid = True
        q = min(m * tau_par, 1 / math.e)
        if q == 0:
            # Preserve the low root when m*tau underflows, and solve the
            # upper branch in log space rather than treating it as m=0.
            root1 = m
            target = -math.log(m) - math.log(tau_par) - 1
            root2 = (1 + _negative_w_displacement(target, -1, 1e-13, 100)) / tau_par
        else:
            w0 = lambert_w_eval(-q, branch=0)
            root1 = m * math.exp(-w0)
            root2 = -lambert_w_eval(-q, branch=-1) / tau_par
        root_status = "two-real-roots"

    return {
        "observed_rate_cps": m,
        "non_paralyzable_inversion": {
            "tau_sec": tau_nonpar,
            "true_rate_cps": n_np,
            "is_physically_admissible": np_valid,
            "inversion_status": np_status
        },
        "paralyzable_dual_root_inversion": {
            "tau_sec": tau_par,
            "max_observable_rate_cps": m_max,
            "is_physically_admissible": p_valid,
            "root_status": root_status,
            "root1_unsaturated_cps": root1,
            "root2_paralyzed_cps": root2,
            "dual_root_discrepancy_ratio": (root2 / root1) if (root1 and root2 and root1 > 0) else None
        }
    }


def format_text_report(fwd: Dict[str, Any], inv: Dict[str, Any]) -> str:
    lines = [
        "=" * 74,
        "   DETECTOR DEAD TIME, PULSE PILE-UP & COUNTING LOSS ANALYZER",
        "   Ideal stationary-Poisson models and conditional approximations",
        "=" * 74,
        f" FORWARD THROUGHPUT AT TRUE RATE n = {fwd['true_rate_cps']:.1f} cps:",
        f"   1. Non-Paralyzable / Nonextendable (tau = {fwd['non_paralyzable']['tau_sec']*1e6:.2f} us):",
        f"      Observed Rate m_NP   : {fwd['non_paralyzable']['observed_rate_cps']:.1f} cps",
        f"      Live Time Fraction   : {fwd['non_paralyzable']['live_time_fraction']*100:.2f}%",
        f"      Counting Loss        : {fwd['non_paralyzable']['fractional_loss']*100:.2f}%",
        "",
        f"   2. Paralyzable / Extendable (tau = {fwd['paralyzable']['tau_sec']*1e6:.2f} us):",
        f"      Observed Rate m_P    : {fwd['paralyzable']['observed_rate_cps']:.1f} cps",
        f"      Max Observable Rate  : {('{:.1f} cps (at n_crit = {:.1f})'.format(fwd['paralyzable']['max_possible_rate_cps'], fwd['paralyzable']['critical_true_rate_cps'])) if fwd['paralyzable']['max_possible_rate_cps'] is not None else 'Unbounded (tau=0)'}",
        f"      Live Time Fraction   : {fwd['paralyzable']['live_time_fraction']*100:.2f}%",
        f"      Regime Status        : {'PARALYZED SATURATION! (Rate decreases)' if fwd['paralyzable']['is_in_saturated_regime'] else 'Normal unsaturated operation'}",
        "",
        "   3. Hybrid Poissonized Cascade APPROXIMATION (tau_P then tau_N):",
        f"      tau_P = {fwd['hybrid']['tau_paralyzable_sec']*1e6:.2f} us, tau_N = {fwd['hybrid']['tau_nonparalyzable_sec']*1e6:.2f} us",
        f"      Observed Rate m_Hyb  : {fwd['hybrid']['observed_rate_cps']:.1f} cps (Acceptance: {fwd['hybrid']['live_time_fraction']*100:.2f}%)",
        "",
        f"   4. Assumed Isolation Window 2*T_p (T_p = {fwd['pileup_diagnostics']['peaking_time_sec']*1e6:.2f} us):",
        f"      Fractional Pile-up   : {fwd['pileup_diagnostics']['pileup_loss_fraction']*100:.2f}%",
        f"      Isolated Input Rate : {fwd['pileup_diagnostics']['clean_peak_rate_cps']:.1f} cps",
        "-" * 74,
        f" EXPERIMENTAL INVERSION FROM OBSERVED RATE m = {inv['observed_rate_cps']:.1f} cps:",
        f"   Non-Paralyzable Inversion n_NP: {('{:.1f} cps'.format(inv['non_paralyzable_inversion']['true_rate_cps'])) if inv['non_paralyzable_inversion']['true_rate_cps'] is not None else 'Over range (m * tau >= 1.0)'}",
        f"   Paralyzable DUAL ROOTS:",
    ]

    p_inv = inv['paralyzable_dual_root_inversion']
    if p_inv['is_physically_admissible']:
        r1 = p_inv['root1_unsaturated_cps']
        r2 = p_inv['root2_paralyzed_cps']
        ratio = p_inv['dual_root_discrepancy_ratio']
        lines.extend([
            f"      Root 1 (Unsaturated) : {r1:.1f} cps",
            f"      Root 2 (Paralyzed)   : {f'{r2:.1f} cps' if r2 is not None else 'No second finite root'}",
            f"      Discrepancy Ratio    : {f'{ratio:.2f}x' if ratio is not None else 'Not applicable'}",
            f"      Root Status          : {p_inv['root_status']}"
        ])
    else:
        rate_str = '{:.1f}'.format(p_inv['max_observable_rate_cps']) if p_inv['max_observable_rate_cps'] is not None else 'None'
        lines.append(f"      EXCEEDS MAX OBSERVABLE RATE ({rate_str} cps)!")

    lines.extend([
        "-" * 74,
        " Physical & Methodological Synthesis:",
        "   - Select a dead-time model from measured system behavior and timing logic.",
        "   - Positive rates below the paralyzable maximum have two model roots.",
        "   - Near the maximum, inversion is ill-conditioned; use independent rate data.",
        "   - The hybrid approximation ignores inter-arrival correlations after stage 1.",
        "   - Isolation, energy-peak efficiency, and DAQ acceptance are distinct.",
        "   - A flat top can reduce ballistic deficit; it does not remove all losses.",
        "=" * 74
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Detector Dead Time, Pile-up & Counting Loss Reconciler"
    )
    parser.add_argument("--true-rate", "-n", type=float, default=25000.0,
                        help="True event rate (cps)")
    parser.add_argument("--obs-rate", "-m", type=float, default=20000.0,
                        help="Observed event rate for inversion (cps)")
    parser.add_argument("--tau-np", type=float, default=10.0,
                        help="Non-paralyzable dead time in microseconds (default: 10.0 us)")
    parser.add_argument("--tau-p", type=float, default=10.0,
                        help="Paralyzable dead time in microseconds (default: 10.0 us)")
    parser.add_argument("--tp", type=float, default=4.0,
                        help="Peaking time in microseconds (default: 4.0 us)")
    parser.add_argument("--json", action="store_true",
                        help="Output pure JSON")

    args = parser.parse_args()

    tau_np_sec = args.tau_np * 1e-6
    tau_p_sec = args.tau_p * 1e-6
    tp_sec = args.tp * 1e-6

    try:
        # Validate before unit conversion so a tiny negative time cannot
        # silently underflow to negative zero.
        for name in ("true_rate", "obs_rate", "tau_np", "tau_p", "tp"):
            _nonnegative(getattr(args, name), name)
        fwd = calculate_deadtime_models(
            true_rate=args.true_rate,
            tau_nonpar=tau_np_sec,
            tau_par=tau_p_sec,
            tau_hybrid_p=tau_p_sec * 0.5,
            tau_hybrid_n=tau_np_sec * 0.5,
            peaking_time=tp_sec
        )
        inv = invert_observed_rate(
            observed_rate=args.obs_rate,
            tau_nonpar=tau_np_sec,
            tau_par=tau_p_sec
        )
    except ValueError as exc:
        parser.error(str(exc))

    if args.json:
        print(json.dumps({"forward": fwd, "inversion": inv}, indent=2, allow_nan=False))
    else:
        print(format_text_report(fwd, inv))


if __name__ == "__main__":
    main()
