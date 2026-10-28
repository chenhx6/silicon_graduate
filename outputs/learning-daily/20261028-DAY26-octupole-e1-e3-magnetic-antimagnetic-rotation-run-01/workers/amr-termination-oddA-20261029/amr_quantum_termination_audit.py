#!/usr/bin/env python3
"""Finite-j algebra, not a Cd Hamiltonian or EDF calculation. Standard library only."""
from fractions import Fraction as F
from math import factorial,sqrt
from itertools import combinations
from pathlib import Path
import json,csv,hashlib
OUT=Path(__file__).resolve().parent

def fac(x):
    x=F(x)
    if x.denominator!=1 or x<0: raise ValueError(x)
    return factorial(int(x))

def phase(x):return (-1)**int(x)

def threej(a,b,c,x,y,z):
    a,b,c,x,y,z=map(F,(a,b,c,x,y,z))
    if x+y+z or any(abs(m)>j for m,j in [(x,a),(y,b),(z,c)]) or c<abs(a-b) or c>a+b:return 0.0
    try:
        delta=F(fac(a+b-c)*fac(a-b+c)*fac(-a+b+c),fac(a+b+c+1))
        pref=phase(a-b-z)*sqrt(float(delta*fac(a+x)*fac(a-x)*fac(b+y)*fac(b-y)*fac(c+z)*fac(c-z)))
        result=F(0)
        for k in range(int(a+b+c)+2):
            args=[k,a+b-c-k,a-x-k,b+y-k,c-b+x+k,c-a-y+k]
            if min(args)<0:continue
            den=1
            for arg in args:den*=fac(arg)
            result+=F(phase(k),den)
        return pref*float(result)
    except ValueError:return 0.0

def cg(a,x,b,y,c,z):return phase(F(a)-F(b)+F(z))*sqrt(2*float(c)+1)*threej(a,b,c,x,y,-F(z))

def pair_state(j,J,M):
    ms=[-j+i for i in range(int(2*j)+1)]
    return { (1<<i)|(1<<k):sqrt(2)*cg(j,ms[i],j,ms[k],J,M) for i,k in combinations(range(len(ms)),2) if ms[i]+ms[k]==M}

def annihilate(mask,i):
    if not mask>>i&1:return None,0
    return mask^(1<<i),phase((mask&((1<<i)-1)).bit_count())

def create(mask,i):
    if mask>>i&1:return None,0
    return mask|(1<<i),phase((mask&((1<<i)-1)).bit_count())

def pair_norm(j,J):
    ms=[-j+i for i in range(int(2*j)+1)];amp=0.
    for mask,a in pair_state(j,J,J).items():
        for i,m in enumerate(ms):
            if m<=0:continue
            k=ms.index(-m);k1,s1=annihilate(mask,i)
            if k1 is None:continue
            k2,s2=annihilate(k1,k)
            if k2==0:amp+=a*phase(j-m)*s1*s2
    return amp*amp

def single_q(j,mf,mi,q):return cg(j,mi,2,q,j,mf)/sqrt(2*float(j)+1)

def pair_me(j,Jf,Mf,Ji,Mi,q):
    initial=pair_state(j,Ji,Mi);final=pair_state(j,Jf,Mf)
    ms=[-j+i for i in range(int(2*j)+1)];value=0.
    for mask,a in initial.items():
        for i,mi in enumerate(ms):
            k1,s1=annihilate(mask,i)
            if k1 is None:continue
            for k,mf in enumerate(ms):
                if mf!=mi+q:continue
                k2,s2=create(k1,k)
                if k2 in final:value+=final[k2]*a*s1*s2*single_q(j,mf,mi,q)
    return value

records=[]
for j in [F(9,2),F(11,2)]:
    ms=[-j+i for i in range(int(2*j)+1)]
    counts={}
    for a,b in combinations(ms,2):counts[a+b]=counts.get(a+b,0)+1
    mult={str(J):counts.get(F(J),0)-counts.get(F(J+1),0) for J in range(int(2*j)+1)}
    mult={J:n for J,n in mult.items() if n}
    allowed=list(map(int,mult));Jmax=max(allowed)
    me=pair_me(j,Jmax-2,Jmax-2,Jmax,Jmax,-2)
    B=me**2*(2*(Jmax-2)+1)/((2*Jmax+1)*cg(Jmax,Jmax,2,-2,Jmax-2,Jmax-2)**2)
    records.append(dict(j=str(j),slater_dimension=len(ms)*(len(ms)-1)//2,allowed_J_multiplicities=mult,Jmax=Jmax,paired_J0_SdagS=pair_norm(j,0),aligned_SdagS=pair_norm(j,Jmax),endpoint_E2_B_single_reduced_q_squared=B,endpoint_E2_matrix_element=me))
    assert abs(pair_norm(j,0)-(float(j)+.5))<1e-12
    assert abs(pair_norm(j,Jmax))<1e-12
    assert all(J%2==0 for J in allowed)
    assert abs(sum(pair_state(j,Jmax,Jmax).values())**2-1)<1e-12
# Four-qp fixed Jp=8,Jn=10, exact coupled I=18->16, proton E2 only.
j=F(9,2)
pme=pair_me(j,8,6,8,8,-2)
fullme=cg(8,6,10,10,16,16)*pme
B18=fullme**2*33/(37*cg(18,18,2,-2,16,16)**2)
assert B18>0
rows=[]
for mass,data in [('106Cd',[(18,.15,.01,False),(20,.14,.02,False),(22,.07,.01,False),(24,.05,.01,False),(26,.07,None,True)]),('108Cd',[(16,.15,.01,False),(18,.14,.01,False),(20,.09,.01,False),(22,.03,None,True)]),('110Cd',[(16,.14,.01,False),(18,.12,.02,False),(20,.11,.02,False),(22,.09,.03,False),(24,.06,.02,False)])]:
    for I,B,dB,effective in data:rows.append(dict(nucleus=mass,I=I,BE2=B,sigma=dB,effective_lifetime=effective,unit='e^2 b^2',provenance='Roy2011 p324 Table1; 106/108 reused earlier measurements'))
with (OUT/'cd_BE2_reinspection.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
results=dict(scope='exact finite-single-j algebra; no full-Cd eigenstates, no EDF reproduction',pair_sectors=records,four_qp={'frozen_configuration':'pi(g9/2)^-2 x nu(h11/2)^2; other particles frozen to J0','exact_max_spin':18,'classical_max_spin':20,'classical_with_quantum_neutron_pair':19,'I18_to_I16_E2_B_proton_single_reduced_q_squared':B18,'endpoint_transition_nonzero':True},oddA={'Rz_pi_half_integer_eigenvalues':['+i','-i'],'transverse_expectation_zero_condition':'state or density invariant under Rz(pi), including the blocked odd orbital','antiunitary_Ry_pi_T_constraint':'only mu_y=0; mu_x is not forced to zero','not_proven':'no exclusive AMR or all-interband-M1 selection rule'},ratios={'106Cd_non_effective_24over18':.05/.15,'108Cd_non_effective_20over16':.09/.15,'108Cd_effective_22over16':.03/.15,'110Cd_24over16':.06/.14},finite_pairing_toy={'H':'-G Sdag S - omega Jz, n=2 single-j only','g9/2_Omega':5,'aligned_J':8,'crossing_omega_over_G':5/8,'is_Cd_prediction':False})
(OUT/'quantum_termination_audit.json').write_text(json.dumps(results,ensure_ascii=False,indent=2));print(json.dumps(results,ensure_ascii=False,indent=2))
