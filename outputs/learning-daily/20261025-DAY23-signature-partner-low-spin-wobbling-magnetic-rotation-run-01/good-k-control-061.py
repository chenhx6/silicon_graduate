"""Exact good-K control. No experimental fit or new measured quantities."""
from fractions import Fraction as F
from math import factorial as fac
import json
from pathlib import Path


def cg_squared(j1, j2, j3, m1, m2, m3):
    a, b, c = j1+j2-j3, j1-j2+j3, -j1+j2+j3
    triangle = F(fac(a)*fac(b)*fac(c), fac(j1+j2+j3+1))
    product = fac(j1+m1)*fac(j1-m1)*fac(j2+m2)*fac(j2-m2)*fac(j3+m3)*fac(j3-m3)
    total = F(0)
    for z in range(j1+j2+j3+1):
        args = [z, a-z, j1-m1-z, j2+m2-z, j3-j2+m1+z, j3-j1-m2+z]
        if min(args) < 0:
            continue
        denominator = 1
        for value in args:
            denominator *= fac(value)
        total += F((-1)**z, denominator)
    return (2*j3+1)*triangle*product*total*total


rows = []
for spin in [10, 12, 16, 20]:
    k = 8
    cg1 = cg_squared(spin, 2, spin-1, k, 0, k)
    cg2 = cg_squared(spin, 2, spin-2, k, 0, k)
    analytic = F(2*k*k*(2*spin-1), (spin+1)*((spin-1)**2-k*k))
    assert cg1/cg2 == analytic
    rows.append(dict(I=spin, K=k, cg1_squared_exact=str(cg1),
                     cg2_squared_exact=str(cg2), ratio_exact=str(cg1/cg2),
                     ratio=float(cg1/cg2), analytic_agrees_exactly=True))
result = dict(scope="goodK fixed intrinsic Q analytic control; not t-band fit, not S1prime to S1 definition",
              method="independent standard-library factorial Wigner3j sum, exact Fraction arithmetic",
              rows=rows, source_motivation="Petrache2019 p245 paragraphs around Fig5; model exercise only",
              new_measurement=False, failed_optional_route="sympy unavailable; no installation attempted")
Path(__file__).with_name("cg-benchmark.json").write_text(json.dumps(result, indent=2)+"\n")
