"""Exact Laurent-polynomial identities in arbitrary stretch scales, no nuclear input."""
import json
from pathlib import Path

# Monomial exponents are (dx,dy,dz,X,Y,Z); coefficients are Gaussian integers.
# Negative d exponents occur only in physical angular-momentum generators.
ZERO = (0,)*6
def add(*polys):
    out = {}
    for poly in polys:
        for powers, coefficient in poly.items():
            out[powers] = out.get(powers, 0) + coefficient
    return {p:c for p,c in out.items() if c}
def scale(poly, coefficient):
    return {p:c*coefficient for p,c in poly.items() if c*coefficient}
def mul(a, b):
    out = {}
    for p,c in a.items():
        for q,e in b.items():
            powers = tuple(x+y for x,y in zip(p,q))
            out[powers] = out.get(powers, 0) + c*e
    return {p:c for p,c in out.items() if c}
def var(index, exponent=1):
    powers = list(ZERO); powers[index] = exponent
    return {tuple(powers):1}
def diff(poly, index):
    out = {}
    for p,c in poly.items():
        if p[index]:
            q=list(p); q[index]-=1; out[tuple(q)]=c*p[index]
    return out
def same(a,b):
    assert not add(a,scale(b,-1))
def component(X,Y,Z):
    return {
        0:add(scale(mul(Z,Z),2),scale(mul(X,X),-1),scale(mul(Y,Y),-1)),
        1:scale(mul(Z,add(X,scale(Y,1j))),-1),
        -1:mul(Z,add(X,scale(Y,-1j))),
        2:mul(add(X,scale(Y,1j)),add(X,scale(Y,1j))),
        -2:mul(add(X,scale(Y,-1j)),add(X,scale(Y,-1j)))
    }
def L(poly, i):
    j,k=((1,2),(2,0),(0,1))[i]
    first=mul(mul(mul(var(j),var(k,-1)),var(3+j)),diff(poly,3+k))
    second=mul(mul(mul(var(k),var(j,-1)),var(3+k)),diff(poly,3+j))
    return scale(add(first,scale(second,-1)),-1j)
def ladder(poly, direction):
    return add(L(poly,0),scale(L(poly,1),direction*1j))

d=[var(i) for i in range(3)]; X,Y,Z=[var(i) for i in range(3,6)]
q=component(*(mul(d[i],v) for i,v in enumerate((X,Y,Z))))
t=component(X,Y,Z)
for m in range(-2,3):
    same(L(q[m],2),scale(q[m],m))
    # Normalization ratios for q0=A*T0, q±1=B*T±1, q±2=C*T±2.
    plus={-2:4,-1:1,0:6,1:1,2:0}[m]
    minus={-2:0,-1:1,0:6,1:1,2:4}[m]
    same(ladder(q[m],1),scale(q.get(m+1,{}),plus))
    same(ladder(q[m],-1),scale(q.get(m-1,{}),minus))
ax,ay,az=[mul(v,v) for v in d]
r2=add(mul(X,X),mul(Y,Y),mul(Z,Z))
D=add(mul(X,X),scale(mul(Y,Y),-1))
same(scale(q[0],6),add(mul(add(scale(az,4),ax,ay),t[0]),
                       mul(scale(add(ay,scale(ax,-1)),3),D),
                       mul(scale(add(scale(az,2),scale(ax,-1),scale(ay,-1)),2),r2)))
for m in (1,-1):
    same(scale(q[m],2),mul(d[2],add(mul(add(d[0],d[1]),t[m]),
                                      scale(mul(add(d[0],scale(d[1],-1)),t[-m]),-1))))
for m in (2,-2):
    same(scale(q[m],12),add(
        mul(scale(add(ax,ay,scale(mul(d[0],d[1]),2)),3),t[m]),
        mul(scale(add(ax,ay,scale(mul(d[0],d[1]),-2)),3),t[-m]),
        mul(scale(add(ax,scale(ay,-1)),-2),t[0]),
        mul(scale(add(ax,scale(ay,-1)),4),r2)))
result={
    'method':'exact Gaussian-integer Laurent-polynomial coefficient cancellation in arbitrary positive dx,dy,dz; no sampled scale or nuclear parameter',
    'physical_L_tensor_commutators':'verified for all five components, including zero ladder endpoints',
    'six_function_dictionary':'verified for all five components; includes common r_t^2 function with component-dependent coefficients',
    'not_verified':'historical Ref23 conventions, actual oscillator radial/basis matrices, charge/length units in GAMPN or Ce predictions',
    'scope':'coordinate identities only; hbar divided out of generators',
}
here=Path(__file__).resolve().parent
(here/'identity-check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
