#!/usr/bin/env python3
"""Finite-dimensional control, not a RAT-PRM calculation."""
import itertools
import json
from pathlib import Path
import numpy as np


def kron(*xs):
    out = np.array([[1.0 + 0j]])
    for x in xs:
        out = np.kron(out, x)
    return out


def spin(j):
    m = np.arange(j, -j-1, -1)
    n = len(m)
    plus = np.zeros((n, n), complex)
    for col in range(1, n):
        plus[col-1, col] = np.sqrt(j*(j+1)-m[col]*(m[col]+1))
    minus = plus.T.conj()
    return (plus+minus)/2, (plus-minus)/(2j), np.diag(m)


def run(j):
    a = spin(j)
    n = len(a[0]); eye = np.eye(n); x = np.array([[0,1],[1,0]]); z = np.diag([1.,-1.]); sh = np.eye(2)
    # Rotation exp(-i*pi*Jy) computed using its Hermitian eigendecomposition.
    eigenvalues, v = np.linalg.eigh(a[1])
    ry = (v * np.exp(-1j*np.pi*eigenvalues)) @ v.conj().T
    u = kron(ry, ry, ry)
    p = kron(x, eye, eye, eye)
    r = kron(x, ry, ry, ry)
    t = kron(sh, u)
    c = t @ r.conj()
    pc = p @ c
    ops = [[kron(sh, *(a[k] if i == pos else eye for i in range(3))) for k in range(3)] for pos in range(3)]
    chi = sum((1 if perm in [(0,1,2),(1,2,0),(2,0,1)] else -1)*ops[0][perm[0]]@ops[1][perm[1]]@ops[2][perm[2]] for perm in itertools.permutations(range(3)))
    beta = kron(z, eye, eye, eye)
    unit = np.eye(len(beta))
    def norm(a): return float(np.max(np.abs(a)))
    def tr(u,o,anti=False): return u @ (o.conj() if anti else o) @ u.conj().T
    checks = {}
    for name,U,anti,bsgn,jsigns,csgn in [
        ('P',p,False,-1,(1,1,1),1),('T',t,True,1,(-1,-1,-1),-1),
        ('Ry_pi',r,False,-1,(-1,1,-1),1),('C',c,True,-1,(1,-1,1),-1),
        ('PC',pc,True,1,(1,-1,1),-1)]:
        checks[name] = max([norm(tr(U,beta,anti)-bsgn*beta),norm(tr(U,chi,anti)-csgn*chi)] + [norm(tr(U,ops[i][k],anti)-jsigns[k]*ops[i][k]) for i in range(3) for k in range(3)])
    expected = -1 if j == .5 else 1
    checks.update(T_squared=norm(t@t.conj()-expected*unit), R_squared=norm(r@r-expected*unit), C_squared=norm(c@c.conj()-unit), P_commutes_C=norm(p@c-c@p.conj()))
    return checks


def main():
    checks={str(j):run(j) for j in (.5,1.)}
    # Compare a beta30 polynomial and the y-type real rank-3 harmonic at one nonzero point.
    def f30(x,y,z): return z*(2*z*z-3*x*x-3*y*y)
    def f3y(x,y,z): return y*(4*z*z-x*x-y*y)
    point=(1.,2.,3.); rotated=(-point[0],point[1],-point[2])
    sample={'point':point,'Ry_point':rotated,'f30_before_after':[f30(*point),f30(*rotated)],'f3y_before_after':[f3y(*point),f3y(*rotated)]}
    passed=all(v < 1e-12 for vals in checks.values() for v in vals.values()) and sample['f30_before_after'][1] == -sample['f30_before_after'][0] and sample['f3y_before_after'][1] == sample['f3y_before_after'][0]
    result={'kind':'finite spin/parity representation and rank-3 harmonic counterexample; not nuclear model fit','max_abs_residuals':checks,'real_harmonic_control':sample,'tolerance':1e-12,'passed':passed}
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    if not passed: raise SystemExit(1)

if __name__ == '__main__': main()
