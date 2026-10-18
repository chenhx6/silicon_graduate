#!/usr/bin/env python3
"""JT74 Fig2's spin path: exact coefficients and a conditional nonregular limit.

This is a source-motivated theoretical calculation, not sampled or refitted
experimental data. No covariance, Q, counts or isotope identity is invented.
"""
from __future__ import annotations

import argparse
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path
from statistics import NormalDist

import numpy as np
from scipy.integrate import quad
import sympy as sp
from sympy.physics.wigner import clebsch_gordan, wigner_d_small

from day16_d96_eq4_erratum_audit import direct_operators


@lru_cache(None)
def sympy_rotation(ell: int, theta: sp.Expr) -> sp.Matrix:
    # SymPy's d-small argument is opposite the frozen photon helper's exponent.
    return wigner_d_small(ell, -theta)


def symbolic_rates(theta: sp.Expr, delta: sp.Symbol, u: sp.Symbol) -> tuple:
    """Return 4pi I and 4pi(I_parallel-I_perpendicular) at phi=0."""
    intensity, difference = 0, 0
    for mi, population in [(0, 1-u), (-1, u/2), (1, u/2)]:
        for mf in range(-2, 3):
            mu = mi - mf
            helicity = {}
            for h in [-1, 1]:
                value = 0
                for ell, amp in [(1, 1), (2, delta)]:
                    if abs(mu) <= ell:
                        cg = clebsch_gordan(2, ell, 3, mf, mu, mi)
                        d = sympy_rotation(ell, theta)[ell-mu, ell-h]
                        # Explicit D96-native mapping: M1 -> -h, E2 -> 1.
                        value += (-h if ell == 1 else 1) * amp * sp.sqrt(2*ell+1) * cg * d
                helicity[h] = value
            intensity += population * (helicity[1]**2 + helicity[-1]**2) / 2
            difference -= population * helicity[1] * helicity[-1]
    return (sp.simplify(sp.expand(intensity) / (1+delta**2)),
            sp.simplify(sp.expand(difference) / (1+delta**2)))


def traced_rate(population: np.ndarray, parts: tuple, theta: float, psi: float | None) -> float:
    return float(sum(np.sum(np.abs(op)**2 * population[None, :]).real
                     for op in direct_operators(3, 2, parts, theta, 0.0, psi)))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.input.read_text())
    assert cfg["identity"] == "JT74-FIG2-3TO2-NONREGULAR-PROFILE-01"
    for file, expected in cfg["helper_hashes"].items():
        assert hashlib.sha256(Path(file).read_bytes()).hexdigest() == expected
    delta, u, u0 = sp.symbols("delta u u0", real=True)
    q = sp.symbols("Q", positive=True)
    angles = [sp.Integer(0), sp.pi/4, sp.pi/2]
    rates = [symbolic_rates(theta, delta, u) for theta in angles]
    design = sp.Matrix([[1, sp.legendre(2, sp.cos(t)), sp.legendre(4, sp.cos(t))] for t in angles])
    coefficients = (design.inv() @ sp.Matrix([r[0] for r in rates])).applyfunc(sp.simplify)
    assert coefficients[0] == 1
    a2, a4 = coefficients[1], coefficients[2]
    h90 = rates[-1][1]
    w90 = sp.simplify(1-a2/2+3*a4/8)
    p90 = sp.factor(h90 / w90)
    assert sp.simplify(a4 - (6-5*u)*delta**2/(7*(1+delta**2))) == 0
    # Independent source pure-E2 identity, no calibration point fitted to it.
    pure_e2_p = sp.simplify(sp.limit(p90, delta, sp.oo))
    pure_e2_a2, pure_e2_a4 = [sp.limit(v, delta, sp.oo) for v in [a2, a4]]
    assert sp.simplify(pure_e2_p - (12*pure_e2_a2+5*pure_e2_a4)/(8-4*pure_e2_a2+3*pure_e2_a4)) == 0
    j_ad = sp.Matrix([a2, a4]).jacobian([delta, u]).subs(delta, 0).applyfunc(sp.simplify)
    j_pol = sp.Matrix([a2, a4, p90]).jacobian([delta, u]).subs(delta, 0).applyfunc(sp.simplify)
    j_known_q = sp.Matrix([a2, a4, q*p90]).jacobian([delta, u]).subs(delta, 0)
    j_unknown_q = sp.Matrix([a2, a4, q*p90]).jacobian([delta, u, q]).subs(delta, 0)
    j_with_q_calibration = sp.Matrix([a2, a4, q*p90, q]).jacobian([delta, u, q]).subs(delta, 0)
    assert j_ad.rank() == 1 and j_pol.rank() == 2
    assert j_known_q.rank() == 2 and j_known_q.subs(q, 0).rank() == 1
    assert j_unknown_q.rank() == 2
    assert j_with_q_calibration.rank() == 3
    determinant = sp.factor(sp.Matrix([a2, p90]).jacobian([delta, u]).subs(delta, 0).det())

    # For fixed delta the mean is exactly affine in u. Profiling a known
    # positive-definite Gaussian covariance can therefore be done analytically.
    mean = sp.Matrix([a2, a4])
    base = mean.subs(u, 0)
    tangent = mean.diff(u)
    true_mean = mean.subs({delta: 0, u: u0})
    residual = true_mean-base
    determinant_residual = sp.factor(tangent[0]*residual[1]-tangent[1]*residual[0])
    s11, s12, s22 = sp.symbols("Sigma22 Sigma24 Sigma44", real=True)
    profile_denominator = tangent[1]**2*s11 - 2*tangent[0]*tangent[1]*s12 + tangent[0]**2*s22
    leading_det = sp.simplify(sp.limit(determinant_residual/delta**2, delta, 0))
    leading_profile = sp.factor(leading_det**2/profile_denominator.subs(delta, 0))
    assert sp.simplify(leading_profile-(6-5*u0)**2/(49*s22)) == 0

    f_a2 = sp.lambdify((delta, u), a2, "numpy")
    f_a4 = sp.lambdify((delta, u), a4, "numpy")
    f_h = sp.lambdify((delta, u), h90, "numpy")
    f_base = sp.lambdify(delta, base, "numpy")
    f_tangent = sp.lambdify(delta, tangent, "numpy")
    trace_errors, polarization_errors = [], []
    for pop_u in [0.0, *cfg["interior_checks_u"], 1.0]:
        population = np.zeros(7)
        population[3] = 1-pop_u
        population[2] = population[4] = pop_u/2
        assert min(population) >= 0 and abs(sum(population)-1) < 1e-14
        for mixing in [-2.0, -1.0, 0.0, .2, 1.0, 2.0]:
            parts = (("M", 1, 1.0), ("E", 2, mixing))
            for angle in np.linspace(0, math.pi, 17):
                intensity = traced_rate(population, parts, float(angle), None) * 4*math.pi
                predicted = 1 + f_a2(mixing, pop_u)*float(sp.legendre(2, math.cos(angle))) + f_a4(mixing, pop_u)*float(sp.legendre(4, math.cos(angle)))
                trace_errors.append(abs(intensity-predicted))
                assert intensity >= -1e-13
            para = traced_rate(population, parts, math.pi/2, 0.0)
            perp = traced_rate(population, parts, math.pi/2, math.pi/2)
            polarization_errors.append(abs((para-perp)*4*math.pi-f_h(mixing, pop_u)))
    assert max(trace_errors) < 2e-12 and max(polarization_errors) < 2e-12
    # Failure control: complete isotropy removes this single-photon information.
    isotropic_error = 0.0
    for mixing in [-1.0, 0.0, 1.0]:
        parts = (("M", 1, 1.0), ("E", 2, mixing))
        for angle in [0.0, math.pi/4, math.pi/2]:
            isotropic_error = max(isotropic_error, abs(4*math.pi*traced_rate(np.ones(7)/7, parts, angle, None)-1))
        para = traced_rate(np.ones(7)/7, parts, math.pi/2, 0.0)
        perp = traced_rate(np.ones(7)/7, parts, math.pi/2, math.pi/2)
        isotropic_error = max(isotropic_error, abs(para-perp))
    assert isotropic_error < 2e-12

    power_checks = []
    for true_u in cfg["interior_checks_u"]:
        center = np.array([f_a2(0.0, true_u), 0.0])
        expected_leading = ((6-5*true_u)/7)**2
        for step in cfg["small_delta_checks"]:
            for sign in [-1, 1]:
                mixing = sign*step
                b = np.asarray(f_base(mixing), float).ravel()
                v = np.asarray(f_tangent(mixing), float).ravel()
                # Identity covariance is a unit-norm numerical control, not a
                # measured covariance or synthetic experiment.
                fitted_u = float(np.dot(v, center-b)/np.dot(v, v))
                assert 0 < fitted_u < 1
                centered_profile = float(np.sum((center-b-fitted_u*v)**2))
                scaled = centered_profile/mixing**4
                power_checks.append({"u0": true_u, "delta": mixing, "profiled_u": fitted_u,
                                     "centered_unit_norm_profile": centered_profile,
                                     "profile_over_delta4": scaled,
                                     "expected_limit": expected_leading})
                if step == cfg["small_delta_checks"][-1]:
                    assert abs(scaled/expected_leading-1) < 1e-3

    # Conditional known-Sigma, interior-u, high-statistics limit only. After
    # profiling a2's mean, the rank-four direction has lambda=delta^2>=0.
    # For Z~N(0,1), LR=max(Z,0)^2, including an atom of probability1/2 at0.
    coverage_plus_one = NormalDist().cdf(1.0)
    critical_68 = NormalDist().inv_cdf(.68)**2
    integrated_coverage, _ = quad(lambda z: math.exp(-z*z/2)/math.sqrt(2*math.pi),
                                 -np.inf, 1.0, epsabs=1e-13)
    assert abs(integrated_coverage-coverage_plus_one) < 1e-13
    output = {"identity": cfg["identity"],
              "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "helper_hashes": cfg["helper_hashes"], "sympy_version": sp.__version__,
              "symbolic": {"a0": "1", "a2": str(sp.factor(a2)), "a4": str(sp.factor(a4)),
                           "H90": str(sp.factor(h90)), "P90": str(p90),
                           "J_a2_a4_at_delta0": str(j_ad),
                           "det_J_a2_P_at_delta0": str(determinant),
                           "profile_leading_S_over_delta4": str(leading_profile)},
              "ranks_at_pure_M1": {"a2_a4_unknown_u": 1, "a2_a4_P_known_response": 2,
                                    "a2_a4_A_known_nonzero_Q": 2, "a2_a4_A_known_Qzero": 1,
                                    "a2_a4_A_free_Q_three_parameters": 2,
                                    "a2_a4_A_plus_independent_Qcal_three_parameters": 3},
              "trace_vs_independent_symbolic_max_error": max(trace_errors),
              "polarization_numerator_max_error": max(polarization_errors),
              "isotropic_failure_control_max_error": isotropic_error,
              "centered_profile_power_checks": power_checks,
              "conditional_nonregular_limit": {"LR_distribution": "0.5 pointmass0 + 0.5 chi2_1; LR=max(Z,0)^2",
                                                "coverage_if_critical_increment_1": coverage_plus_one,
                                                "local_critical_increment_for_68percent": critical_68,
                                                "unconstrained_u_delta_scale": "N^(-1/4) if harmonic errors scale N^(-1/2)",
                                                "scope": "Known positive-definite Sigma, interior u0, pure M1 and specified density family; not a general DCO confidence calibration or source-author result."},
              "assumptions": cfg["statistical_assumptions"],
              "phase_boundary": "JT74's signed-delta operator convention was not authenticated; coordinate sign reversal leaves these rank/order/coverage statements invariant.",
              "day_index": 16, "partial_day_indices": [17], "formal_day17_credit": False,
              "experimental_data_created_or_refit": False, "all_internal_checks_passed": True}
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2, allow_nan=False)+"\n")
    print(json.dumps({"output": str(args.output), "symbolic": output["symbolic"],
                      "ranks": output["ranks_at_pure_M1"], "trace_max_error": max(trace_errors),
                      "conditional_nonregular_limit": output["conditional_nonregular_limit"],
                      "all_internal_checks_passed": True}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
