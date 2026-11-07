#!/usr/bin/env python3
"""Exact rational-square Racah CG check; Condon-Shortley, integer j only."""
from fractions import Fraction
from math import factorial, prod, sqrt

def cg(j1, j2, j, m1, m2, m):
    assert m1 + m2 == m and abs(j1-j2) <= j <= j1+j2
    assert abs(m1)<=j1 and abs(m2)<=j2 and abs(m)<=j
    f = factorial
    pref = Fraction((2*j+1)*f(j+j1-j2)*f(j-j1+j2)*f(j1+j2-j),f(j1+j2+j+1))
    pref *= prod(f(x) for x in (j+m,j-m,j1-m1,j1+m1,j2-m2,j2+m2))
    total = Fraction(0)
    for k in range(j1+j2+j+2):
        terms=(k,j1+j2-j-k,j1-m1-k,j2+m2-k,j-j2+m1+k,j-j1-m2+k)
        if min(terms)>=0:
            total += Fraction((-1)**k,prod(f(x) for x in terms))
    return (-1 if total<0 else 1), pref*total*total

for j1 in (2,4):
    for m in (-1,0,1):
        sign, square = cg(j1,3,1,0,m,m)
        print(f'C({j1} 0, 3 {m} | 1 {m}): sign={sign:+d} square={square} value={sign*sqrt(float(square)):.12f}')
assert [cg(2,3,1,0,m,m) for m in (-1,0,1)] == [(1,Fraction(6,35)),(1,Fraction(9,35)),(1,Fraction(6,35))]
assert [cg(4,3,1,0,m,m) for m in (-1,0,1)] == [(1,Fraction(1,14)),(-1,Fraction(4,21)),(1,Fraction(1,14))]
print('PASS: exact squared coefficients, signs, K symmetry; no nuclear spectrum calculated')
