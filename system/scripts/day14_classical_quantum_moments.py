#!/usr/bin/env python3
"""Symbolic trace-moment derivation of the finite-spin quartic correction.

All algebra is polynomial over exact Fractions. This is our interpretation of
printed formulas, not a reading of Morinaga/Yamazaki1976 or the author's code.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
from itertools import zip_longest
import json
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02"


def poly(p):
    p = list(map(F, p))
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def add(a, b):
    return poly(x+y for x,y in zip_longest(a, b, fillvalue=F(0)))


def scale(a, c):
    return poly(x*c for x in a)


def sub(a, b):
    return add(a, scale(b, -1))


def mul(a, b):
    out = [F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] += x*y
    return poly(out)


def power(a, n):
    out = poly([1])
    for _ in range(n):
        out = mul(out, a)
    return out


def compose(a, b):
    out = poly([0])
    for i,x in enumerate(a):
        out = add(out, scale(power(b, i), x))
    return out


def at(a, x):
    return sum((v*x**i for i,v in enumerate(a)), F(0))


def faulhaber(p):
    """Sum k^p for k=0,...,N, as a polynomial in N."""
    if p == 0:
        return poly([1, 1])
    bernoulli = [F(1), F(-1, 2), F(1, 6), F(0), F(-1, 30),
                 F(0), F(1, 42), F(0), F(-1, 30)]
    out = [F(0)]*(p+2)
    for j in range(p+1):
        out[p+1-j] += F((-1)**j*comb(p+1, j), p+1)*bernoulli[j]
    return poly(out)


def shifted_spin_power_sum(p):
    # m=k-N/2 for k=0,...,N and N=2J; covers integer/half-integer spin.
    out = poly([0])
    for q in range(p+1):
        out = add(out, scale(mul(poly([0]*(p-q)+[1]), faulhaber(q)),
                             comb(p,q)*F(-1,2)**(p-q)))
    return out


def quartic_norm(m, a, b):
    return add(sub(add(sub(m[8], scale(mul(a,m[6]),2)),
                       mul(add(mul(a,a),scale(b,2)),m[4])),
                   scale(mul(mul(a,b),m[2]),2)),mul(b,b))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=RUN / "classical-quantum-moment-audit.json")
    args = parser.parse_args()
    ipath = RUN / "classical-quantum-moment-input.json"
    data = json.loads(ipath.read_text())
    checks = {}
    def check(name, value):
        checks[name] = bool(value)
        if not value:
            raise AssertionError(name)
    check("publisher_source_hash", hashlib.sha256((ROOT/data["publisher_pdf"]["path"]).read_bytes()).hexdigest() == data["publisher_pdf"]["sha256"])
    legendre = {int(k):poly(v) for k,v in data["source_legendre_coefficients"].items()}
    q = {k:scale(v, 1/v[0]) for k,v in legendre.items()}
    check("classical_P2_reference_identity", q[2] == poly([1,0,-3]))
    check("classical_P4_reference_identity", q[4] == poly([1,0,-10,0,F(35,3)]))
    check("continuous_isotropic_normalized_P2_P4_zero", all(sum((c/F(i+1) for i,c in enumerate(v) if i%2==0),F(0)) == 0 for v in q.values()))
    S = poly([0,1])
    S_of_N = poly([0,F(1,2),F(1,4)])
    quantum = {2:poly([0,F(1,3)]),4:poly([0,F(-1,15),F(1,5)]),
               6:poly([0,F(1,21),F(-1,7),F(1,7)]),
               8:poly([0,F(-1,15),F(1,5),F(-2,9),F(1,9)])}
    classical = {p:scale(power(S,p//2), F(1,p+1)) for p in [2,4,6,8]}
    for p in [2,4,6,8]:
        target = mul(poly([1,1]),compose(quantum[p],S_of_N))
        check(f"trace_power_{p}_Faulhaber_all_integer_N", shifted_spin_power_sum(p) == target)
    aq,bq = poly([F(-5,7),F(6,7)]),poly([0,F(-6,35),F(3,35)])
    ac,bc = poly([0,F(6,7)]),poly([0,0,F(3,35)])
    for name,m,a,b in [("quantum",quantum,aq,bq),("classical",classical,ac,bc)]:
        check(name+"_quartic_orthogonal_to_one", add(sub(m[4],mul(a,m[2])),b) == poly([0]))
        check(name+"_quartic_orthogonal_to_m_squared", add(sub(m[6],mul(a,m[4])),mul(b,m[2])) == poly([0]))
    check("quantum_T4_correction_m_squared_coefficient", scale(sub(ac,aq),35) == poly([25]))
    check("quantum_T4_correction_constant", scale(sub(bq,bc),35) == scale(S,-6))
    det = sub(quantum[4],mul(quantum[2],quantum[2]))
    check("lower_moment_Gram_determinant", det == scale(mul(S,poly([-3,4])),F(1,45)))
    nq,nc = quartic_norm(quantum,aq,bq),quartic_norm(classical,ac,bc)
    factor = scale(mul(mul(S,poly([-2,1])),mul(poly([-3,4]),poly([-15,4]))), F(4,11025))
    check("quantum_quartic_norm_factorization", nq == factor)
    check("absent_rank_4_trace_norm_zero", all(at(nq,j*(j+1)) == 0 for j in [F(0),F(1,2),F(1),F(3,2)]))
    check("rank_4_exists_at_J2", at(nq,F(6)) == F(2016,1225))
    check("classical_quartic_norm", nc == scale(power(S,4),F(64,11025)))
    check("quantum_norm_leading_classical_limit", nq[-1] == nc[-1])
    raw_numerator = add(sub(power(S,2),scale(mul(S,quantum[2]),10)),scale(quantum[4],F(35,3)))
    check("printed_q4_uniform_residual_from_trace_moments", raw_numerator == scale(S,F(-7,9)))
    check("no_book_author_or_experimental_attribution", not data["Ref39_body_read"] and not data["author_attribution_verified"] and data["actual_sigma_delta_fit"] is None)
    result = dict(kind="our symbolic classical-vector versus quantum trace-moment interpretation",
                  checks=checks,check_count=len(checks),passed=all(checks.values()),inputs=data,
                  coefficient_order="ascending powers of S, except normalized Legendre arrays use z",
                  quantum_trace_moments=quantum,classical_projection_moments=classical,
                  normalized_Legendre=q,quantum_quartic_a=aq,quantum_quartic_b=bq,
                  classical_quartic_a=ac,classical_quartic_b=bc,
                  lower_Gram_determinant=det,quantum_monic_quartic_norm=nq,
                  classical_monic_quartic_norm=nc,
                  rank4_norm_factorization="4*S*(S-2)*(4*S-3)*(4*S-15)/11025",
                  input_sha256=hashlib.sha256(ipath.read_bytes()).hexdigest(),
                  literal_sha256=hashlib.sha256((RUN/data["literal_record"]).read_bytes()).hexdigest(),
                  limitations=["exact algebra interprets formula shape; does not attribute an argument to the unread textbook",
                               "continuum orientation model and quantum magnetic-substate trace are distinct measures",
                               "no author code, experimental populations, sigma/delta fit or confidence interval",
                               "low-spin zero norm is a rank boundary, not a usable normalization"])
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2,default=str)+"\n")
    print(json.dumps({k:result[k] for k in ["kind","check_count","passed","quantum_quartic_a","quantum_quartic_b","rank4_norm_factorization"]},default=str))


if __name__ == "__main__":
    main()
