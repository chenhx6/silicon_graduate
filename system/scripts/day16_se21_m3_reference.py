#!/usr/bin/env python3
"""Bounded single-gamma reference model; no experimental delta/sigma fit.

Nuclear angular momenta and projections use doubled integers. The independent
source-F and RB photon-amplitude routes are checked before any interpretation.
This does not extend the earlier integer-only gamma-gamma response to 135Pr.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
import math
from math import factorial as fact
from pathlib import Path

import numpy as np

from day14_unobserved_feeding_transfer import cg_squared, tensor
from day16_pdco_ambiguity_preview import small_d


def phase(n: int) -> int:
    return -1 if n % 2 else 1


@lru_cache(None)
def cg2(a: int, b: int, c: int, ma: int, mb: int, mc: int) -> float:
    if (ma + mb != mc or abs(ma) > a or abs(mb) > b or abs(mc) > c
            or not abs(a - b) <= c <= a + b
            or any(x % 2 for x in [a + ma, b + mb, c + mc, a + b + c])):
        return 0.
    aa, bb, cc = (a + b - c) // 2, (a - ma) // 2, (b + mb) // 2
    dd, ee = (c - b + ma) // 2, (c - a - mb) // 2
    pref = F((c + 1) * fact(aa) * fact((a - b + c) // 2)
             * fact((-a + b + c) // 2), fact((a + b + c) // 2 + 1))
    for n in [(a + ma) // 2, (a - ma) // 2, (b + mb) // 2,
              (b - mb) // 2, (c + mc) // 2, (c - mc) // 2]:
        pref *= fact(n)
    total = sum((F(phase(z), fact(z) * fact(aa - z) * fact(bb - z)
                   * fact(cc - z) * fact(dd + z) * fact(ee + z))
                 for z in range(max(0, -dd, -ee), min(aa, bb, cc) + 1)), F(0))
    value = math.sqrt(float(pref)) * float(total)
    assert abs(value * value - float(cg_squared(a, b, c, ma, mb, mc))) < 2e-14
    return value


def triangle(a: int, b: int, c: int) -> F:
    if (a + b + c) % 2 or not abs(a - b) <= c <= a + b:
        return F(0)
    return F(fact((a + b - c) // 2) * fact((a - b + c) // 2)
             * fact((-a + b + c) // 2), fact((a + b + c) // 2 + 1))


@lru_cache(None)
def sixj2(a: int, b: int, c: int, d: int, e: int, f: int) -> float:
    pref = triangle(a, b, c) * triangle(a, e, f) * triangle(d, b, f) * triangle(d, e, c)
    if not pref:
        return 0.
    lower = [(a + b + c) // 2, (a + e + f) // 2,
             (d + b + f) // 2, (d + e + c) // 2]
    upper = [(a + b + d + e) // 2, (a + c + d + f) // 2,
             (b + c + e + f) // 2]
    total = F(0)
    for z in range(max(lower), min(upper) + 1):
        denominator = math.prod(fact(z - n) for n in lower) * math.prod(
            fact(n - z) for n in upper)
        total += F(phase(z) * fact(z + 1), denominator)
    return math.sqrt(float(pref)) * float(total)


def native_f(ti: int, tf: int, rank: int, ell: int, ellp: int) -> float:
    # SE21 Eq2.43 / DA74 Eq8; W(abcd;ef)=(-1)^(a+b+c+d){a b e; d c f}.
    cg = cg2(2 * ell, 2 * ellp, 2 * rank, 2, -2, 0)
    if cg == 0:
        return 0.
    racah = phase(ti + ell + ellp) * sixj2(ti, ti, 2 * rank, 2 * ellp, 2 * ell, tf)
    return (phase((tf - ti) // 2 - 1) * math.sqrt(
        (2 * ell + 1) * (2 * ellp + 1) * (ti + 1)) * cg * racah)


def population(ti: int, width_ratio: float) -> np.ndarray:
    m = np.arange(-ti, ti + 1, 2, dtype=float) / 2
    if width_ratio == 0:
        p = (abs(m) == min(abs(m))).astype(float)
    else:
        width = width_ratio * ti / 2
        p = np.exp(-(m * m - min(m * m)) / (2 * width * width))
    return p / p.sum()


def forms(ti: int, tf: int, components: tuple, pop: np.ndarray) -> dict[int, np.ndarray]:
    result = {}
    for rank in range(0, 2 * max(x[1] for x in components) + 1, 2):
        v, pref = tensor(ti, rank)
        rho = float(np.dot(np.array(v, dtype=float), pop)) * math.sqrt(float(pref))
        result[rank] = rho * np.array([
            [native_f(ti, tf, rank, a[1], b[1]) for b in components] for a in components])
        assert np.max(abs(result[rank] - result[rank].T)) < 2e-13
    assert np.max(abs(result[0] - np.eye(len(components)))) < 2e-13
    return result


@lru_cache(None)
def photon(ti: int, tf: int, kind: str, ell: int, theta: float, helicity: int) -> np.ndarray:
    assert ti % 2 == tf % 2
    op = np.zeros((tf + 1, ti + 1))
    for row, mf in enumerate(range(-tf, tf + 1, 2)):
        for col, mi in enumerate(range(-ti, ti + 1, 2)):
            mu = (mi - mf) // 2
            if abs(mu) <= ell:
                op[row, col] = (
                    math.sqrt((2 * ell + 1) / (8 * math.pi))
                    * cg2(tf, 2 * ell, ti, mf, 2 * mu, mi)
                    * small_d(ell, mu, helicity, theta)
                    * (helicity if kind == "M" else 1))
    return op


def direct(ti: int, tf: int, components: tuple, pop: np.ndarray,
           native: np.ndarray, order: int = 12) -> tuple[dict[int, float], np.ndarray]:
    native = native / np.linalg.norm(native)
    # KS/native versus RB: the common spin factor cancels; retain (-1)^L per component.
    rb = np.array([phase(x[1]) * a for x, a in zip(components, native)])
    x, weights = np.polynomial.legendre.leggauss(order)
    intensity, diagonal_integral = [], np.zeros(ti + 1)
    for c, w in zip(x, weights):
        theta = float(np.arccos(c))
        diagonal = np.zeros(ti + 1)
        for q in (-1, 1):
            op = sum(a * photon(ti, tf, kind, ell, theta, q)
                     for (kind, ell), a in zip(components, rb))
            diagonal += np.sum(op * op, axis=0)
        intensity.append(float(diagonal @ pop))
        diagonal_integral += 2 * math.pi * w * diagonal
    intensity = np.array(intensity)
    norm = weights @ intensity
    assert np.max(abs(diagonal_integral - 1)) < 3e-12
    coeff = {rank: float((2 * rank + 1) * (
        weights @ (intensity * np.polynomial.legendre.legval(x, [0] * rank + [1]))) / norm)
             for rank in range(0, 2 * max(x[1] for x in components) + 1, 2)}
    return coeff, diagonal_integral


def evaluate(matrix: np.ndarray, delta: float) -> float:
    v = np.array([1., delta]) / math.sqrt(1 + delta * delta)
    return float(v @ matrix @ v)


def point_value(ti: int, tf: int, components: tuple, pop: np.ndarray,
                native: np.ndarray, theta: float) -> float:
    native = native / np.linalg.norm(native)
    rb = np.array([phase(c[1]) * a for c, a in zip(components, native)])
    return float(sum(np.sum(sum(a * photon(ti, tf, kind, ell, theta, q)
                               for (kind, ell), a in zip(components, rb)) ** 2, axis=0) @ pop
                     for q in (-1, 1)))


def interval_image(matrix: np.ndarray, lo: float, hi: float) -> dict:
    a, b, c = matrix[0, 0], matrix[0, 1], matrix[1, 1]
    points = [lo, hi]
    if abs(b) > 1e-14:
        points += [float(z.real) for z in np.roots([-b, c - a, b])
                   if abs(z.imag) < 1e-12 and lo <= z.real <= hi]
    elif abs(c - a) > 1e-14 and lo <= 0 <= hi:
        points.append(0.)
    values = [evaluate(matrix, p) for p in points]
    return {"range": [min(values), max(values)], "candidate_deltas": points,
            "kind": "Literal parameter-span image, not a confidence interval"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    cfg = json.loads(args.input.read_text())
    system = cfg["system"]
    ti, tf = system["Ji_twice"], system["Jf_twice"]
    components = tuple((c["type"], c["L"]) for c in system["components"])
    pop = population(ti, float(system["sigma_over_J"]))
    matrices = forms(ti, tf, components, pop)
    # Primary pure-reference and D/Q negative-column controls before M3 use.
    complete = forms(ti, tf, components, population(ti, 0.))
    assert abs(complete[2][0, 0] - 65 / 161) < 2e-13
    assert abs(complete[4][0, 0] + 26 / 161) < 2e-13
    dq_parts = (("M", 1), ("E", 2))
    dq_pop = population(12, .4)
    dq = forms(12, 10, dq_parts, dq_pop)
    dq_values = [evaluate(dq[k], -.5) for k in (2, 4)]
    assert abs(dq_values[0] + .66825) <= 5e-6
    assert abs(dq_values[1] - .02811) <= 5e-6
    comparisons = []
    for a, b, parts, p, deltas in [(12, 10, dq_parts, dq_pop, [-.5, .5]),
                                  (ti, tf, components, pop, [0., -.04, .04, -.06])]:
        f = forms(a, b, parts, p)
        for delta in deltas:
            measured, _ = direct(a, b, parts, p, np.array([1., delta]))
            convergence, _ = direct(a, b, parts, p, np.array([1., delta]), order=16)
            expected = {k: evaluate(f[k], delta) for k in f}
            error = max(abs(measured[k] - expected[k]) for k in f)
            quad = max(abs(measured[k] - convergence[k]) for k in f)
            comparisons.append({"spin_twice": [a, b], "delta_native": delta,
                                "max_F_vs_direct_error": error, "quadrature12_vs16": quad})
            assert error < 5e-12 and quad < 5e-12
    uniform = forms(ti, tf, components, np.ones(ti + 1) / (ti + 1))
    assert all(np.max(abs(m)) < 2e-13 for k, m in uniform.items() if k > 0)
    uniform_direct, _ = direct(ti, tf, components, np.ones(ti + 1) / (ti + 1),
                              np.array([1., -.04]))
    assert max(abs(x) for k, x in uniform_direct.items() if k > 0) < 5e-12
    pure_m3, _ = direct(ti, tf, components, pop, np.array([0., 1.]))
    assert max(abs(pure_m3[k] - matrices[k][1, 1]) for k in matrices) < 5e-12
    mirror = abs(point_value(ti, tf, components, pop, np.array([1., -.04]), .37)
                 - point_value(ti, tf, components, pop, np.array([1., -.04]), math.pi - .37))
    assert mirror < 5e-12
    true_alpha = np.array([matrices[k][0, 0] / complete[k][0, 0] for k in (2, 4)])
    true_dual = float(7 - 10 * true_alpha[0] + 3 * true_alpha[1])
    assert true_dual >= -1e-12
    angles = np.deg2rad([float(x) for x in cfg["seven_angle_design"]["degrees"]])
    cosines = np.cos(angles)
    design = np.array([[np.polynomial.legendre.legval(c, [0] * k + [1])
                        for k in (0, 2, 4)] for c in cosines])
    full_design = np.array([[np.polynomial.legendre.legval(c, [0] * k + [1])
                             for k in (0, 2, 4, 6)] for c in cosines])
    results = []
    for source in cfg["source_configurations"]:
        delta = float(source["delta_central"])
        coeff = {k: evaluate(m, delta) for k, m in matrices.items()}
        y = full_design @ np.array([coeff[k] for k in (0, 2, 4, 6)])
        beta = np.linalg.lstsq(design, y, rcond=None)[0]
        full = np.linalg.lstsq(full_design, y, rcond=None)[0]
        assert np.max(abs(full - [coeff[k] for k in (0, 2, 4, 6)])) < 2e-13
        assert beta[0] > 0
        apparent = np.array([coeff[k] / complete[k][0, 0] for k in (2, 4)])
        opposite_apparent = np.array([evaluate(matrices[k], -delta) / complete[k][0, 0]
                                      for k in (2, 4)])
        transform = np.diag([1., -1.])
        v = np.array([1., delta]) / math.sqrt(1 + delta * delta)
        for k, matrix in matrices.items():
            assert abs(float((transform @ v) @ (transform @ matrix @ transform)
                             @ (transform @ v)) - coeff[k]) < 2e-13
        results.append({
            "source_configuration": source["identity"], "delta_native": delta,
            "M3_radiative_fraction": delta * delta / (1 + delta * delta),
            "forward_normalized_coefficients": {str(k): v for k, v in coeff.items()},
            "opposite_sign_A4": evaluate(matrices[4], -delta),
            "opposite_sign_identity": "Physical phase control at fixed operators; not a KS/RB coordinate rewrite or measured value",
            "apparent_alpha_if_reference_falsely_treated_as_pureE2": apparent.tolist(),
            "apparent_positive_P_dual": float(7 - 10 * apparent[0] + 3 * apparent[1]),
            "chosen_opposite_phase_apparent_alpha": opposite_apparent.tolist(),
            "chosen_opposite_phase_apparent_dual": float(
                7 - 10 * opposite_apparent[0] + 3 * opposite_apparent[1]),
            "literal_delta_span_images": {str(k): interval_image(
                m, float(source["literal_delta_low"]), float(source["literal_delta_high"]))
                for k, m in matrices.items() if k > 0},
            "equal_weight_point_design_only": {
                "fitted_scale": float(beta[0]), "truncated_A2_A4": (beta[1:] / beta[0]).tolist(),
                "shift_from_full_moments": (beta[1:] / beta[0]
                                            - np.array([coeff[2], coeff[4]])).tolist(),
                "design_condition_number": float(np.linalg.cond(design)),
                "actual_experimental_covariance_used": False}
        })
    assert results[0]["chosen_opposite_phase_apparent_dual"] < 0
    result = {
        "data_identity": cfg["data_identity"], "kind": cfg["kind"],
        "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "convention": cfg["convention"], "source_F_matrices": {str(k): m.tolist() for k, m in matrices.items()},
        "independent_route_controls": comparisons, "primary_DQ_control": dq_values,
        "physical_limits": {"uniform_direct_isotropic": True, "pure_M3_limit_matched": True,
                            "mirror_absolute_error": mirror, "true_nuclear_alpha": true_alpha.tolist(),
                            "true_nuclear_positive_P_dual": true_dual,
                            "coordinate_change_preserves_observable": True},
        "configurations": results, "source_summaries_kept_separate": cfg["separate_source_summaries"],
        "stop_contract": cfg["stop_contract"], "boundaries": cfg["boundaries"],
    }
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"identity": result["data_identity"], "controls": comparisons,
                      "configurations": results}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
