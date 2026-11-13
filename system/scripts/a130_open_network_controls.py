#!/usr/bin/env python3
"""Algebra controls for the declared two-cluster model, not a nuclear fit."""

import json

import sympy as sp


def main() -> None:
    a, b, dg, dm, r = sp.symbols("a b D_g D_m r", nonnegative=True)
    f, population = sp.symbols("f N", positive=True)
    pg, pm = sp.symbols("P_g P_m", nonnegative=True)
    generator = sp.Matrix([[-a - dg, b], [a, -b - dm]])
    expected_polynomial = r**2 - (a + b + dg + dm) * r + a * dm + b * dg + dg * dm
    characteristic_ok = sp.expand((generator + r * sp.eye(2)).det() - expected_polynomial) == 0
    state = sp.Matrix([(1 - f) * population, f * population])
    derivative = generator * state + sp.Matrix([pg, pm])
    total_derivative = sp.simplify(sum(derivative))
    fraction_derivative = sp.simplify((derivative[1] - f * total_derivative) / population)
    expected_fraction = a - (a + b) * f - (dm - dg) * f * (1 - f) + (pm - f * (pg + pm)) / population
    fraction_ok = sp.simplify(fraction_derivative - expected_fraction) == 0
    equal_loss_ok = sp.simplify(
        fraction_derivative.subs({dm: dg, pg: 0, pm: 0}) - (a - (a + b) * f)
    ) == 0

    # A fixed open stationary trajectory conserves its population by balanced
    # feeding and removal. This does not assert conservation for all initial states.
    open_generator = generator.subs({a: 2, b: 3, dg: 5, dm: 7})
    open_state = sp.Matrix([3, 2])
    open_source = sp.Matrix([15, 14])
    stationary_residual = open_generator * open_state + open_source

    # Entry distributions here are finite probability examples only. The
    # conditional weights are not calculated reaction cross sections.
    weights = [sp.Rational(1, 4), sp.Rational(3, 4)]
    branching = [sp.Rational(1, 10), sp.Rational(9, 10)]
    conditional_feed = sum(w * branch for w, branch in zip(weights, branching))
    tf, window, tau, time = sp.symbols("t_f Delta_t tau t", positive=True)
    acceptance = sp.exp(-tf / tau) * (1 - sp.exp(-window / tau))
    integrated_density = sp.integrate(sp.exp(-time / tau) / tau, (time, tf, tf + window))
    window_ok = sp.simplify(acceptance - integrated_density) == 0
    checks = {
        "characteristic_polynomial_identity": characteristic_ok,
        "normalized_fraction_equation_identity": fraction_ok,
        "equal_common_loss_cancels_from_fraction_equation": equal_loss_ok,
        "open_stationary_balance_residual_zero": stationary_residual == sp.zeros(2, 1),
        "conditional_feeding_example": str(conditional_feed),
        "window_integral_identity": window_ok,
        "zero_window_acceptance": str(sp.limit(acceptance, window, 0)),
        "infinite_window_acceptance": str(sp.limit(acceptance, window, sp.oo)),
        "infinite_lifetime_acceptance": str(sp.limit(acceptance, tau, sp.oo)),
    }
    assert characteristic_ok and fraction_ok and equal_loss_ok and window_ok
    assert stationary_residual == sp.zeros(2, 1)
    assert conditional_feed == sp.Rational(7, 10)
    assert sp.limit(acceptance, window, 0) == 0
    assert sp.limit(acceptance, tau, sp.oo) == 0
    print(json.dumps({
        "kind": "symbolic algebra and declared probability controls only",
        "sympy_version": sp.__version__,
        "checks": checks,
        "limits": [
            "No fitted rates, reaction yields, detector parameters or stellar trajectories.",
            "The open balance example concerns one stationary trajectory, not every initial population.",
            "The window formula assumes one constant laboratory-frame lifetime and a fixed flight time.",
            "The entry weights are illustrative normalized probabilities, not an evaporation calculation.",
        ],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
