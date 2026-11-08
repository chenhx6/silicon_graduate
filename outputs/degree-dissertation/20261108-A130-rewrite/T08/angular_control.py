#!/usr/bin/env python3
"""T08: algebraic toy controls only; no nuclear matrix elements or data.
Uses SymPy Wigner 3j/6j and CG coefficients, with exact arithmetic.
Convention <a ma|T_kq|b mb>=(-1)^(a-ma) (a k b;-ma q mb)<a||T||b>.
Run: python3 angular_control.py (SymPy required).
"""
from sympy import S, simplify, sqrt
from sympy.physics.wigner import wigner_3j, wigner_6j, clebsch_gordan

def ms(j):
    return [-j+n for n in range(int(2*j)+1)]

def we(a, ma, k, q, b, mb):
    return (-1)**(a-ma)*wigner_3j(a,k,b,-ma,q,mb)

def direct2(s,r):
    total=S.Zero
    for mr in ms(r):
        for u in range(-2,3):
            total+=clebsch_gordan(2,2,0,u,-u,0)*we(s,s,2,u,r,mr)*we(r,mr,2,-u,s,s)
    return simplify(total)

def direct3(s,r,t):
    total=S.Zero
    for mr in ms(r):
        for mt in ms(t):
            for u in range(-2,3):
                for v in range(-2,3):
                    k=u+v
                    if abs(k)>2:
                        continue
                    total+=clebsch_gordan(2,2,2,u,v,k)*clebsch_gordan(2,2,0,k,-k,0)*we(s,s,2,u,r,mr)*we(r,mr,2,v,t,mt)*we(t,mt,2,-k,s,s)
    return simplify(total)

def candidates(s):
    return [r for r in ms(s+2) if r>=0 and (2*r)%2==(2*s)%2 and abs(s-r)<=2<=s+r]

two=three=0
for s in [S(0),S(1)/2,S(1),S(3)/2,S(2),S(5)/2]:
    for r in candidates(s):
        # Coefficient of R_sr R_rs, before Hermitian conjugation.
        expected2=(-1)**(s-r)/(sqrt(5)*(2*s+1))
        assert simplify(direct2(s,r)-expected2)==0,(s,r)
        # Correct 6j form of coefficient of |R_sr|^2.
        six2=(-1)**(s+r)*wigner_6j(2,2,0,s,s,r)/sqrt(2*s+1)
        assert simplify(six2-1/(sqrt(5)*(2*s+1)))==0,(s,r)
        two+=1
        for t in candidates(s):
            if not abs(r-t)<=2<=r+t:
                continue
            expected3=(-1)**(2*s)*wigner_6j(2,2,2,s,r,t)/(2*s+1)
            assert simplify(direct3(s,r,t)-expected3)==0,(s,r,t)
            three+=1
print('PASS q2 channels:',two,'q3 channels:',three,'for I=0,1/2,1,3/2,2,5/2')
print('I=0,r=t=2: exact coefficient =',direct3(S(0),S(2),S(2)),'draft coefficient =',1/(5*sqrt(5)))
print('I=1,r=1: correct |R|^2 coefficient =',1/(3*sqrt(5)),'draft =',-1/(3*sqrt(5)))
print('I=3/2,r=3/2: draft (-1)^r is non-real under ordinary complex exponent convention')
# Positive commuting-coordinate toy: Q equally 1 or 2, gamma=0 in both points.
a=S(5)/2; b=S(9)/2
print('two-point coordinate toy ratio =',simplify(b/(a**S('3/2'))),'> 1; E[cos 3gamma]=1')

# Same toy: actual cos(3 gamma) is identically one, so its exact variance is zero.
va=S(9)/4; vb=S(49)/4; covariance=S(21)/4
linear_variance=simplify(vb/a**3+S(9)/4*b**2*va/a**5-3*b*covariance/a**4)
assert linear_variance==S(121)/6250
print('two-point toy exact Var(cos)=0; linearized variance =',linear_variance)
