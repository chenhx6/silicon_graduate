#!/usr/bin/env python3
"""Exact chosen-cone response controls for unobserved feeding and positivity.

This is a mathematical design, not a reconstruction of detector dimensions,
efficiency, response or feeding fractions in the Ionescu experiment.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
from math import comb, factorial
from pathlib import Path

from day14_feeding_fraction_moment_bound import geometry
from day14_unobserved_feeding_transfer import kernel, tensor

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02"


def legendre_average(k, c):
    """Uniform solid-angle cone average of P_k(cos(beta)), including point limit."""
    c = F(c)
    if c == 1:
        return F(1)
    return sum((F((-1)**s * factorial(2*k-2*s),
                  2**k * factorial(s) * factorial(k-s) * factorial(k-2*s))
                * (1-c**(k-2*s+1))/((k-2*s+1)*(1-c))
                for s in range(k//2+1)), F(0))


@lru_cache(None)
def half_angle_moment(p, q, c):
    """Average cos(beta/2)^(2p) sin(beta/2)^(2q), exact rational c."""
    if c == 1:
        return F(q == 0)
    a = (1+c)/2
    return sum(((-1)**i * comb(q, i) * (1-a**(p+i+1))/F(p+i+1)
                for i in range(q+1)), F(0))/(1-a)


@lru_cache(None)
def rotation_kernel(tj, c):
    """R[m',m]=average |d^J(m',m;beta)|^2; all spin args doubled.

    A spin-J state is the normalized symmetric product of N=2J spin halves.
    Expand (c_h u+s_h d)^a(-s_h u+c_h d)^(N-a), square the
    coefficient of u^b d^(N-b), then integrate each even-power monomial.
    An azimuthal average dephases the output; input is diagonal.
    """
    c = F(c)
    if not -1 <= c <= 1:
        raise ValueError("cone cosine must be in [-1,1]")
    n = tj
    out = []
    for b in range(n+1):
        row = []
        for a in range(n+1):
            terms = [(t, F((-1)**(b-t)*comb(a, t)*comb(n-a, b-t)))
                     for t in range(max(0, b-(n-a)), min(a, b)+1)]
            value = F(0)
            for t, h in terms:
                for u, g in terms:
                    p, q = n-a-b+t+u, a+b-t-u
                    assert p >= 0 and q >= 0
                    value += h*g*half_angle_moment(p, q, c)
            row.append(F(comb(n, a), comb(n, b))*value)
        out.append(row)
    return out


def matvec(a, x):
    return [sum((p*q for p, q in zip(row, x)), F(0)) for row in a]


def matmul(a, b):
    return [[sum((p*q for p, q in zip(row, col)), F(0))
             for col in zip(*b)] for row in a]


def pair_population(tj, tm):
    if tm not in range(tj % 2, tj+1, 2):
        raise ValueError("invalid magnetic projection")
    return [F(m == tm) if tm == 0 else F(abs(m) == tm, 2)
            for m in range(-tj, tj+1, 2)]


def moments(tj, population):
    return [sum((v*p for v, p in zip(tensor(tj, k)[0], population)), F(0))
            for k in [2, 4]]


def hull_faces(points):
    def cross(a, b, c):
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    def chain(seq):
        out = []
        for p in seq:
            while len(out) >= 2 and cross(out[-2], out[-1], p) <= 0:
                out.pop()
            out.append(p)
        return out
    pts = sorted(set(tuple(p) for p in points))
    h = chain(pts)[:-1]+chain(pts[::-1])[:-1]
    if len(h) < 3:
        raise ValueError("two-dimensional moment domain required")
    faces = []
    for a, b in zip(h, h[1:]+h[:1]):
        normal = (b[1]-a[1], a[0]-b[0])
        faces.append((normal, sum((x*y for x, y in zip(normal, a)), F(0))))
    return faces


def sharp_bound(target, feed, points):
    candidates = [F(1)]
    for a, b in hull_faces(points):
        n = b-sum((x*y for x, y in zip(a, target)), F(0))
        d = b-sum((x*y for x, y in zip(a, feed)), F(0))
        if n < 0 or d < 0:
            raise ValueError("moments must start inside declared domain")
        if d:
            candidates.append(n/d)
    return min(candidates)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=RUN / "finite-geometry-feeding-audit.json")
    args = parser.parse_args()
    inputs_path = RUN / "finite-geometry-design-input.json"
    data = json.loads(inputs_path.read_text())
    c = F(data["cone_cosine"])
    ti, tf = data["parent_spin_twice"], data["child_spin_twice"]
    checks = {}
    def check(name, value):
        checks[name] = bool(value)
        if not value:
            raise AssertionError(name)
    q = [legendre_average(k, c) for k in [2, 4]]
    check("Q2_closed_form", q[0] == c*(1+c)/2)
    check("Q4_closed_form", q[1] == c*(1+c)*(7*c*c-3)/8)
    check("independent_spin_half_transition_probabilities", rotation_kernel(1, c) ==
          [[(3+c)/4, (1-c)/4], [(1-c)/4, (3+c)/4]])
    check("independent_spin_one_M0_projection_integral", rotation_kernel(2, c)[1][1]
          == (1+c+c*c)/3)
    summaries = []
    for tj in [4, tf, ti]:
        for aperture in [F(1), c, F(0), F(-1)]:
            r = rotation_kernel(tj, aperture)
            check(f"positive_unital_stochastic_J{tj}_c{aperture}",
                  min(x for row in r for x in row) >= 0
                  and all(sum(col) == 1 for col in zip(*r))
                  and all(sum(row) == 1 for row in r))
            for rank in [0, 2, 4]:
                v, _ = tensor(tj, rank)
                check(f"rank{rank}_eigenvalue_J{tj}_c{aperture}",
                      all(sum((v[row]*r[row][col] for row in range(tj+1)), F(0))
                          == legendre_average(rank, aperture)*v[col]
                          for col in range(tj+1)))
            if aperture == -1:
                check(f"sphere_is_uniform_J{tj}",
                      all(x == F(1, tj+1) for row in r for x in row))
            summaries.append(dict(spin_twice=tj, cone_cosine=str(aperture),
                                  Q2=str(legendre_average(2, aperture)),
                                  Q4=str(legendre_average(4, aperture))))
    k = kernel(ti, tf, data["multipole"])
    ri, rf = rotation_kernel(ti, c), rotation_kernel(tf, c)
    check("same_cone_commutes_with_unobserved_feeding", matmul(rf, k) == matmul(k, ri))
    check("point_limit_identity", rotation_kernel(4, F(1)) ==
          [[F(i == j) for j in range(5)] for i in range(5)])
    parent = pair_population(ti, data["chosen_parent_abs_m_twice"])
    feed = matvec(k, parent)
    rest = pair_population(tf, data["chosen_remainder_abs_m_twice"])
    w = F(data["chosen_weight"])
    target = [w*f+(1-w)*s for f, s in zip(feed, rest)]
    check("chosen_populations_positive_normalized", all(min(p) >= 0 and sum(p) == 1
          for p in [parent, feed, rest, target]))
    f, t = moments(tf, feed), moments(tf, target)
    points = [p[:2] for p in geometry(tf)["points"]]
    folded_points = [[q[i]*p[i] for i in range(2)] for p in points]
    ff, ft = [q[i]*f[i] for i in range(2)], [q[i]*t[i] for i in range(2)]
    check("population_and_moment_convolution_agree", moments(tf, matvec(rf, target)) == ft)
    raw_bound = sharp_bound(t, f, points)
    folded_bound = sharp_bound(ft, ff, folded_points)
    conservative_bound = sharp_bound(ft, ff, points)
    check("chosen_boundary_remainder_attains_raw_bound", raw_bound == w)
    check("invertible_common_fold_with_folded_domain_preserves_bound", folded_bound == raw_bound)
    check("using_original_domain_after_fold_is_strictly_weaker_in_chosen_case", conservative_bound > folded_bound)
    # Actual design has weight one: parent point response, child cone response.
    different_target = matvec(rf, feed)
    wrong_bound = sharp_bound(moments(tf, different_target), f, points)
    check("different_kernels_do_not_commute", matmul(rf, k) != k)
    check("wrong_common_point_response_excludes_true_weight_one", wrong_bound < 1)
    check("correct_different_response_exactly_matches_weight_one", different_target == matvec(rf, matvec(k, parent)))
    check("isotropic_reference_cannot_distinguish_cones", all(legendre_average(0, a) == 1
          for a in [F(1), c, F(0), F(-1)]))
    check("hemisphere_discards_selected_even_ranks", legendre_average(2, F(0)) == legendre_average(4, F(0)) == 0)
    check("no_actual_response_or_fraction_inferred", data["actual_IO81_response"] is None
          and data["actual_IO81_feeding_fraction"] is None and data["actual_covariance"] is None)
    output = dict(kind="chosen-cone mathematical control, not experiment reanalysis",
                  inputs=data, checks=checks, check_count=len(checks), passed=all(checks.values()),
                  cone_Q=dict(Q0="1", Q2=str(q[0]), Q4=str(q[1])), kernel_summary=summaries,
                  chosen_parent_population=parent, chosen_feed_population=feed,
                  chosen_target_population=target, selected_moments=dict(feed=f, target=t),
                  bounds=dict(original=raw_bound, common_fold_with_folded_domain=folded_bound,
                              common_fold_but_original_domain=conservative_bound,
                              different_kernels_wrong_common_model=wrong_bound,
                              actual_chosen_different_kernel_weight="1"),
                  input_sha256=hashlib.sha256(inputs_path.read_bytes()).hexdigest(),
                  dependencies={p:hashlib.sha256((ROOT/"system/scripts"/p).read_bytes()).hexdigest()
                                for p in ["day14_unobserved_feeding_transfer.py", "day14_feeding_fraction_moment_bound.py"]},
                  limitations=["axisymmetric positive normalized single-gamma kernel; aligned q0 input",
                               "rotation averaging is a mathematical representation, not nuclear evolution",
                               "unobserved radiative feeding, no direction/polarization/gamma-gamma gate",
                               "equivalent sharp bound requires known invertible Q and folded allowed domain",
                               "no actual dimensions, energy response, weights, ICC, fit, covariance or CL"])
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2, default=str)+"\n")
    print(json.dumps({key:output[key] for key in ["kind", "check_count", "passed", "cone_Q", "bounds"]}, default=str))


if __name__ == "__main__":
    main()
