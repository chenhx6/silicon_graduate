#!/usr/bin/env python3
"""Independent Racah/Fock and exact two-state controls; Python stdlib only."""
from fractions import Fraction as F
from math import factorial, sqrt, exp, isclose
from pathlib import Path
import json
import hashlib
import sys


def fact(x):
    x = F(x)
    if x.denominator != 1 or x < 0:
        raise ValueError(f'factorial argument {x}')
    return factorial(x.numerator)


def phase(n):
    n = F(n)
    assert n.denominator == 1
    return (-1) ** n.numerator


def tri(a,b,c):
    return F(fact(a+b-c)*fact(a-b+c)*fact(-a+b+c),fact(a+b+c+1))


def w3(a,b,c,x,y,z):
    if x+y+z != 0 or any(abs(m)>j for j,m in [(a,x),(b,y),(c,z)]): return 0.0
    pref = phase(a-b-z)*sqrt(float(tri(a,b,c))*fact(a+x)*fact(a-x)*fact(b+y)*fact(b-y)*fact(c+z)*fact(c-z))
    low=max(0,int(b-c-x),int(a-c+y))
    high=min(int(a+b-c),int(a-x),int(b+y))
    s=sum((F((-1)**k, fact(k)*fact(a+b-c-k)*fact(a-x-k)*fact(b+y-k)*fact(c-b+x+k)*fact(c-a-y+k)) for k in range(low,high+1)), F(0))
    return pref*float(s)


def w6_parts(a,b,c,d,e,f):
    """Exact 6j = rational_coefficient * sqrt(rational_radicand)."""
    radical=tri(a,b,c)*tri(a,e,f)*tri(d,b,f)*tri(d,e,c)
    low=max(int(a+b+c),int(a+e+f),int(d+b+f),int(d+e+c))
    high=min(int(a+b+d+e),int(a+c+d+f),int(b+c+e+f))
    total=F(0)
    for k in range(low,high+1):
        denom=(fact(k-a-b-c)*fact(k-a-e-f)*fact(k-d-b-f)*fact(k-d-e-c)*fact(a+b+d+e-k)*fact(a+c+d+f-k)*fact(b+c+e+f-k))
        total += F((-1)**k*fact(k+1),denom)
    return total,radical


def create(mask,i):
    if mask & (1<<i): return None
    return mask | (1<<i), (-1)**((mask & ((1<<i)-1)).bit_count())


def annihilate(mask,i):
    if not mask & (1<<i): return None
    return mask ^ (1<<i), (-1)**((mask & ((1<<i)-1)).bit_count())


def normalize(s):
    norm=sqrt(sum(x*x for x in s.values()))
    assert norm>1e-12
    return {m:x/norm for m,x in s.items() if abs(x)>1e-13}


def coupled_two(j,J,M):
    size=int(2*j+1); out={}
    for i in range(size):
        mi=-j+i
        for k in range(size):
            mk=-j+k
            if mi+mk != M: continue
            cg=phase(M)*sqrt(2*J+1)*w3(j,j,F(J),mi,mk,F(-M))
            first=create(0,k)
            second=create(first[0],i) if first else None
            if second:
                mask,sign=second
                out[mask]=out.get(mask,0)+cg*first[1]*sign/sqrt(2)
    return normalize(out)


def add_pair(s,j):
    size=int(2*j+1); out={}
    for mask,amp in s.items():
        for i in range(size//2,size):
            m=-j+i; k=size-1-i
            first=create(mask,k)
            second=create(first[0],i) if first else None
            if second:
                dest,sign=second
                out[dest]=out.get(dest,0)+amp*phase(j-m)*first[1]*sign
    return normalize(out)


def one_body_overlap(sf,si,j,k,q):
    size=int(2*j+1); total=0.0
    for mask,amp in si.items():
        for col in range(size):
            rem=annihilate(mask,col)
            if rem is None: continue
            row=col+q
            if not 0<=row<size: continue
            added=create(rem[0],row)
            if added is None: continue
            m=-j+row; mp=-j+col
            element=phase(j-m)*w3(j,F(k),j,-m,F(q),mp)
            total += sf.get(added[0],0.0)*amp*rem[1]*added[1]*element
    return total


def rme(sf,si,j,k,Ji,Mi,Jf,Mf):
    q=Mf-Mi
    angular=phase(Jf-Mf)*w3(F(Jf),F(k),F(Ji),F(-Mf),F(q),F(Mi))
    assert abs(angular)>1e-12
    return one_body_overlap(sf,si,j,k,q)/angular


def main():
    j=F(11,2); Ji=10; Jf=8
    si=coupled_two(j,Ji,Ji); sf=coupled_two(j,Jf,Jf)
    six_i=add_pair(add_pair(si,j),j); six_f=add_pair(add_pair(sf,j),j)
    r2=rme(sf,si,j,3,Ji,Ji,Jf,Jf)
    r6=rme(six_f,six_i,j,3,Ji,Ji,Jf,Jf)
    e2_2=rme(sf,si,j,2,Ji,Ji,Jf,Jf)
    e2_6=rme(six_f,six_i,j,2,Ji,Ji,Jf,Jf)
    # Angular-allowed M1 between distinct J values: 10 -> 9 is absent in the
    # two-identical-particle j=11/2 spectrum, so test J=10 -> J=10 diagonal;
    # J=10 -> J=8 violates angular triangle for rank 1. Operator identity is analytic.
    c,rad=w6_parts(j,F(Jf),j,F(Ji),j,F(3))
    sixj=float(c)*sqrt(float(rad))
    analytic_magnitude=2*sqrt((2*Jf+1)*(2*Ji+1))*abs(sixj)
    assert abs(sixj)>1e-12 and abs(r6)>1e-12
    assert isclose(r2,r6,rel_tol=1e-11,abs_tol=1e-11)
    assert isclose(abs(r2),analytic_magnitude,rel_tol=1e-11,abs_tol=1e-11)
    assert abs(e2_2)>1e-12 and abs(e2_6)<1e-11
    assert 3>=abs(Ji-Jf) and 3<=Ji+Jf and (-1)**(3+1)==1
    # Exact singular counterexample and one-way repeated-root example.
    a,b,d1,d2=map(F,(0,0,1,0)); s=(F(1),F(0))
    det=a*d2+b*d1+d1*d2
    assert det==0
    for c0 in map(F,(0,1,7)):
        n=(F(1),c0)
        assert (-(a+d1)*n[0]+b*n[1]+s[0],a*n[0]-(b+d2)*n[1]+s[1])==(0,0)
    a,b,d1,d2=map(F,(0,1,2,1))
    disc=(a-b+d1-d2)**2+4*a*b
    assert disc==0
    # A=-2I+K with K^2=0, K !=0; e^(At)=e^-2t(I+tK).
    K=((F(0),F(1)),(F(0),F(0)))
    assert K[0][1] and all(sum(K[i][h]*K[h][k] for h in range(2))==0 for i in range(2) for k in range(2))
    # Test first-order root coefficients through exact coefficients of the
    # characteristic polynomial, and the equal-loss fraction derivative.
    checks=[]
    for aa,bb,dd1,dd2 in [(2,3,5,7),(1,0,4,9),(0,2,3,8)]:
        aa,bb,dd1,dd2=map(F,(aa,bb,dd1,dd2)); rate=aa+bb
        slow=-(bb*dd1+aa*dd2)/rate
        fast=-(aa*dd1+bb*dd2)/rate
        assert rate*slow+aa*dd2+bb*dd1==0
        assert -rate*(fast+dd1+dd2)+aa*dd2+bb*dd1==0
        n1,n2,D=F(7),F(11),F(4)
        n1dot=-(aa+D)*n1+bb*n2
        n2dot=aa*n1-(bb+D)*n2
        f=n2/(n1+n2)
        fdot=(n2dot*(n1+n2)-n2*(n1dot+n2dot))/(n1+n2)**2
        assert fdot==aa-rate*f
        checks.append({'a':str(aa),'b':str(bb),'d1':str(dd1),'d2':str(dd2),'slow_first_order':str(slow),'fast_first_order':str(fast),'equal_loss_fraction_derivative':str(fdot)})
    times=[0.0,0.5,1.0,2.0]
    traj=[{'t':t,'N1':t*exp(-2*t),'N2':exp(-2*t),'total':(1+t)*exp(-2*t)} for t in times]
    assert all(traj[i]['total']>=traj[i+1]['total'] for i in range(len(traj)-1))
    result={'status':'pass','method':'factorial Racah 3j and exact rational-radical 6j; independently construct antisymmetric two-particle CG states, apply two normalized J=0 pair creators, and evaluate one-body matrices in bitmask Fock basis; floating arithmetic for Fock amplitudes',
      'm3':{'j':'11/2','omega':6,'n_reference':2,'n_half_filled':6,'seniority':2,'Ji':10,'Jf':8,'operator_rank':3,'one_particle_reduced_matrix_element':1,'convention':'<Jf Mf|T(k,q)|Ji Mi> = (-1)^(Jf-Mf) (Jf k Ji; -Mf q Mi) <Jf||T(k)||Ji>', 'six_j_layout':'{11/2 8 11/2; 10 11/2 3}','six_j_rational_coefficient':str(c),'six_j_radicand':str(rad),'six_j_value':sixj,'rme_n2':r2,'rme_n6':r6,'absolute_rme_from_6j':analytic_magnitude,'rme_squared_exact':str(4*(2*Jf+1)*(2*Ji+1)*c*c*rad),'rme_ratio':r6/r2,'e2_rme_n2_control':e2_2,'e2_rme_n6_control':e2_6,'J_pair_state_components':[len(si),len(sf),len(six_i),len(six_f)],'physical_boundary':'same parity; energy ordering and physical one-particle M3 RME assumed, no actual nucleus or rate'},
      'singular_stationary':{'a':0,'b':0,'D1':1,'D2':0,'S':[1,0],'det':str(det),'family':'(1,c), c>=0'},
      'jordan':{'a':0,'b':1,'D1':2,'D2':1,'discriminant':str(disc),'A':[[-2,1],[0,-2]],'propagator':'exp(-2t)[[1,t],[0,1]]','initial':[0,1],'trajectory':traj},
      'first_order_roots_and_equal_loss_checks':checks,
      'claim_scope':'finite controls validate examples, not a physical decay measurement'}
    root = Path(__file__).resolve().parents[2]
    result['provenance'] = {'control': str(Path(__file__).relative_to(root)), 'control_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'python': sys.version.split()[0], 'source': 'Jain2021 actualPDF52/55/56, Eqs3.11/3.12/3.22; mathematical counterexamples independently constructed'}
    output = root / 'outputs/l4/20261114-A130-m3-open-network-controls/results.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__=='__main__': main()
