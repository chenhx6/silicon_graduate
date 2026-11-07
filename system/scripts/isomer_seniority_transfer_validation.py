#!/usr/bin/env python3
"""Exact single-j seniority check. Energies and E2 strength are dimensionless.

Slater bits ordered m=-j,...,+j; operators act right to left. Coupled pair
A_JM = sum_{a<b} sqrt(2) <j a,j b|JM> c_b c_a. H=-A00†A00
+epsilon sum_M A2M†A2M. E2 has single-particle reduced matrix element 1.
No experimental inputs or fitted parameters. Run: python3 SCRIPT --output FILE
"""
import argparse
import hashlib
import itertools
import json
import math
import platform
from functools import lru_cache
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import null_space

TWOJ = 11
MS = tuple(range(-TWOJ, TWOJ + 1, 2))
OM = 6

def fac(x):
    if x < 0 or int(x) != x:
        raise ValueError(x)
    return math.factorial(int(x))

def phase(n):
    return -1 if n % 2 else 1

@lru_cache(None)
def w3j(a, b, c, x, y, z):
    """Wigner 3j, all integer arguments are twice physical quantum numbers."""
    if x+y+z or abs(x)>a or abs(y)>b or abs(z)>c or c>a+b or c<abs(a-b):
        return 0.0
    if any(t % 2 for t in (a+b+c, a+x, b+y, c+z)):
        return 0.0
    ab_c=(a+b-c)//2; ac_b=(a+c-b)//2; bc_a=(b+c-a)//2
    d=fac(ab_c)*fac(ac_b)*fac(bc_a)/fac((a+b+c)//2+1)
    f=fac((a+x)//2)*fac((a-x)//2)*fac((b+y)//2)*fac((b-y)//2)*fac((c+z)//2)*fac((c-z)//2)
    zmin=max(0, (b-c-x)//2, (a-c+y)//2)
    zmax=min(ab_c, (a-x)//2, (b+y)//2)
    terms=[]
    for k in range(zmin,zmax+1):
        den=fac(k)*fac(ab_c-k)*fac((a-x)//2-k)*fac((b+y)//2-k)*fac((c-b+x)//2+k)*fac((c-a-y)//2+k)
        terms.append(phase(k)/den)
    return phase((a-b-z)//2)*math.sqrt(d*f)*math.fsum(terms)

def cg_pair(m1,m2,J,M):
    return phase((m1+m2)//2)*math.sqrt(2*J+1)*w3j(TWOJ,TWOJ,2*J,m1,m2,-2*M)

@lru_cache(None)
def basis(n, two_m):
    return tuple(sum(1<<i for i in comb) for comb in itertools.combinations(range(12),n) if sum(MS[i] for i in comb)==two_m)

def annihilate(s,i):
    if not s>>i & 1: return None
    return s ^ (1<<i), phase((s & ((1<<i)-1)).bit_count())

def create(s,i):
    if s>>i & 1: return None
    return s | (1<<i), phase((s & ((1<<i)-1)).bit_count())

def pair(n,two_m,J,M):
    src=basis(n,two_m); dst=basis(n-2,two_m-2*M); ix={s:i for i,s in enumerate(dst)}
    out=np.zeros((len(dst),len(src)))
    for a in range(12):
        for b in range(a+1,12):
            if MS[a]+MS[b]!=2*M: continue
            val=math.sqrt(2)*cg_pair(MS[a],MS[b],J,M)
            if abs(val)<1e-15: continue
            for k,s in enumerate(src):
                r=annihilate(s,a)
                if r is None: continue
                u=annihilate(r[0],b)
                if u is not None: out[ix[u[0]],k]+=val*r[1]*u[1]
    return out

def onebody(n,two_m,q,kind):
    src=basis(n,two_m); dst=basis(n,two_m+2*q); ix={s:i for i,s in enumerate(dst)}
    out=np.zeros((len(dst),len(src)))
    for b,mb in enumerate(MS):
        ma=mb+2*q
        if ma not in MS: continue
        a=MS.index(ma)
        if kind=='jplus':
            val=math.sqrt((TWOJ/2-mb/2)*(TWOJ/2+mb/2+1))
        else:
            val=phase((TWOJ-ma)//2)*w3j(TWOJ,4,TWOJ,-ma,2*q,mb)
        for k,s in enumerate(src):
            r=annihilate(s,b)
            if r is None: continue
            u=create(r[0],a)
            if u is not None: out[ix[u[0]],k]+=val*r[1]*u[1]
    return out

def conjugation(n,two_m):
    """Particle-hole conjugation C c†_m C^-1=(-1)^(j-m)c_-m."""
    src=basis(n,two_m); dst=basis(12-n,two_m); ix={s:i for i,s in enumerate(dst)}
    out=np.zeros((len(dst),len(src)))
    for k,s in enumerate(src):
        state=(1<<12)-1; sign=1
        for i in reversed([i for i in range(12) if s>>i & 1]):
            a=MS.index(-MS[i]); state,t=annihilate(state,a)
            sign*=t*phase((TWOJ-MS[i])//2)
        out[ix[state],k]=sign
    return out

def ham(n,J,eps):
    m=2*J; a=pair(n,m,0,0); h=-a.T@a
    for k in range(-2,3):
        a=pair(n,m,2,k); h+=eps*(a.T@a)
    return h

def solve(n,J,eps,reference=None):
    jplus=onebody(n,2*J,1,'jplus')
    z=null_space(jplus) if jplus.shape[0] else np.eye(jplus.shape[1])
    h=ham(n,J,eps); energies,vec=np.linalg.eigh(z.T@h@z); states=z@vec
    if reference is None:
        target=-((n-2)/2)*(OM-(n+2)/2+1)/OM
        k=int(np.argmin(abs(energies-target)))
        assert abs(energies[k]-target)<1e-9,(n,J,energies,target)
    else:
        k=int(np.argmax(abs(states.T@reference)))
    v=states[:,k]; residual=float(np.linalg.norm(h@v-energies[k]*v))
    highest=float(np.linalg.norm(jplus@v))
    assert residual<1e-9 and highest<1e-9
    return v,float(energies[k]), residual, highest, float(abs(v@reference)**2 if reference is not None else 1),len(energies)

def strength(n,vi,vf):
    # lower highest |10,10> to |10,8>, retain Condon-Shortley convention
    v=vi.copy()
    for m in (10,9):
        v=onebody(n,2*(m-1),1,'jplus').T@v/math.sqrt((10+m)*(10-m+1))
    assert abs(np.linalg.norm(v)-1)<1e-10
    amp=float(vf@onebody(n,16,0,'q')@v)
    w=w3j(16,4,20,-16,0,16)
    B=amp*amp/(21*w*w)
    # Independent tensor component q=-1 and M_i=9; same reduced matrix element.
    v9=onebody(n,18,1,'jplus').T@vi/math.sqrt(20)
    alt=float(vf@onebody(n,18,-1,'q')@v9)
    walt=w3j(16,4,20,-16,-2,18)
    assert abs(B-alt*alt/(21*walt*walt))<1e-12
    return B,amp

def midshell_opposite_signature_control(vi, b2):
    """Project the E2 image onto the complete J=8, v=4 pairing eigenspace."""
    n=6
    h=ham(n,8,0.0)
    jp=onebody(n,16,1,'jplus')
    z=null_space(jp)
    energies,vec=np.linalg.eigh(z.T@h@z)
    # The exact normalized-pairing eigenvalue for v=4 is -1/3.
    v4_energy=-((n-4)/2)*(OM-(n+4)/2+1)/OM
    v4=z@vec[:,np.isclose(energies,v4_energy,rtol=0,atol=1e-10)]
    assert v4.shape[1]==3
    assert np.linalg.norm(conjugation(n,16)@v4-v4)<1e-10
    initial_h=ham(n,10,0.0)
    initial_energy=float(vi@initial_h@vi)
    initial_residual=float(np.linalg.norm(initial_h@vi-initial_energy*vi))
    assert abs(initial_energy+1)<1e-10 and initial_residual<1e-10
    v8=vi.copy()
    for m in (10,9):
        v8=onebody(n,2*(m-1),1,'jplus').T@v8/math.sqrt((10+m)*(10-m+1))
    image=onebody(n,16,0,'q')@v8
    doorway=v4@(v4.T@image)
    norm=float(np.linalg.norm(doorway))
    assert norm>1e-8
    doorway/=norm
    energy=float(doorway@h@doorway)
    residual=float(np.linalg.norm(h@doorway-energy*doorway))
    highest=float(np.linalg.norm(jp@doorway))
    parity_i=float(vi@conjugation(n,20)@vi)
    parity_f=float(doorway@conjugation(n,16)@doorway)
    assert abs(energy-v4_energy)<1e-10 and residual<1e-10 and highest<1e-10
    assert abs(parity_i+1)<1e-10 and abs(parity_f-1)<1e-10
    B,amp=strength(n,vi,doorway)
    total=math.fsum(strength(n,vi,v4[:,k])[0] for k in range(v4.shape[1]))
    assert B>1e-8 and abs(B-total)<1e-12
    rotation,_=np.linalg.qr(np.array([[1.,2.,3.],[2.,-1.,1.],[1.,1.,-1.]]))
    v4_rotated=v4@rotation
    rotated_total=math.fsum(strength(n,vi,v4_rotated[:,k])[0] for k in range(v4.shape[1]))
    assert abs(rotated_total-total)<1e-12
    return {
        'n':n,'epsilon':0.0,'initial_J':10,'initial_seniority':2,
        'initial_pairing_energy':initial_energy,'initial_eigen_residual':initial_residual,
        'initial_particle_hole_signature':parity_i,
        'final_J':8,'final_seniority':4,'final_pairing_energy':energy,
        'final_particle_hole_signature':parity_f,'final_eigenspace_dimension':v4.shape[1],
        'final_state':'normalized projection of Q20|10,8> onto the full J=8 v=4 eigenspace',
        'selection_scope':'doorway depends on E2 operator; individual eigenvectors within the degenerate v=4 space are not unique',
        'energy_order':'final state is above initial state; strength is an upward E2 transition, not a radiative decay branch',
        'strength':B,'strength_ratio_to_unperturbed_n2':B/b2,
        'sum_strength_to_v4_eigenspace':total,'sum_after_eigenspace_rotation':rotated_total,
        'amplitude_M8_q0':amp,
        'final_eigen_residual':residual,'final_highest_weight_norm':highest
    }

def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--output',type=Path,required=True); args=parser.parse_args()
    assert abs(w3j(11,11,0,11,-11,0)-1/math.sqrt(12))<1e-14
    # Coupled-pair orthonormality / full two-body J=0 and J=2 eigenvalues.
    assert abs(float((pair(2,0,0,0)@pair(2,0,0,0).T)[0,0])-1)<1e-12
    for m in range(-2,3):
        p=pair(2,2*m,2,m); assert abs(float((p@p.T)[0,0])-1)<1e-12
    assert abs(w3j(0,4,4,0,0,0)-1/math.sqrt(5))<1e-14
    # One-body reduced matrix element 1: sum_m'q |<j m'|T2q|j m>|^2=1/(2j+1) per initial m.
    for mb in MS:
        s=sum((phase((TWOJ-ma)//2)*w3j(TWOJ,4,TWOJ,-ma,2*q,mb))**2 for q in range(-2,3) for ma in MS if ma==mb+2*q)
        assert abs(s-1/12)<1e-13
    base={}; rows=[]
    for n in (2,4,6,8,10):
        vi,*_=solve(n,10,0); vf,*_=solve(n,8,0); base[n]=(vi,vf)
    b2=strength(2,*base[2])[0]
    # Rotational scalar commutator between neighboring M sectors, independently of J projection.
    checks=[]
    for n in (2,4,6,8,10):
        p=onebody(n,16,1,'jplus')
        comm=float(np.linalg.norm(ham(n,9,0.037)@p-p@ham(n,8,0.037)))
        assert comm<1e-10
        checks.append({'n':n,'rotational_commutator_norm':comm})
    for eps in (0.0,0.001,0.01,0.05):
        for n in (2,4,6,8,10):
            vi,ei,ri,hi,oi,di=solve(n,10,eps,base[n][0]); vf,ef,rf,hf,of,df=solve(n,8,eps,base[n][1]); B,amp=strength(n,vi,vf)
            # arbitrary independent eigenvector phases cannot affect observable
            bp,_=strength(n,-vi,vf); assert abs(bp-B)<1e-13
            # Explicitly reverse and independently rephase every M=8 Slater basis vector.
            v8=vi.copy()
            for mm in (10,9):
                v8=onebody(n,2*(mm-1),1,'jplus').T@v8/math.sqrt((10+mm)*(10-mm+1))
            perm=np.arange(len(v8)-1,-1,-1)
            signs=np.array([phase((state & 0x555).bit_count()) for state in basis(n,16)])[perm]
            qp=onebody(n,16,0,'q')[np.ix_(perm,perm)]*signs[:,None]*signs[None,:]
            ap=float((vf[perm]*signs)@qp@(v8[perm]*signs))
            assert abs(ap-amp)<1e-12
            ph={}
            if n==6:
                ci=conjugation(n,20); cf=conjugation(n,16); q=onebody(n,16,0,'q')
                assert np.linalg.norm(ci.T@ci-np.eye(len(ci)))<1e-12
                assert np.linalg.norm(cf.T@q@cf+q)<1e-12
                assert np.linalg.norm(ci.T@ham(n,10,eps)@ci-ham(n,10,eps))<1e-10
                assert np.linalg.norm(cf.T@ham(n,8,eps)@cf-ham(n,8,eps))<1e-10
                ph={'particle_hole_J10':float(vi@ci@vi),'particle_hole_J8':float(vf@cf@vf)}
                assert abs(abs(ph['particle_hole_J10'])-1)<1e-10 and abs(ph['particle_hole_J10']-ph['particle_hole_J8'])<1e-10
            rows.append({**ph,'n':n,'epsilon':eps,'strength':B,'ratio_to_unperturbed_n2':B/b2,'amplitude_M8_q0':amp,'energy_J10':ei,'energy_J8':ef,'overlap_J10':oi,'overlap_J8':of,'dimension_J10':di,'dimension_J8':df,'max_residual':max(ri,rf),'max_highest_weight_norm':max(hi,hf)})
    expected=[1,.25,0,.25,1]; observed=[r['ratio_to_unperturbed_n2'] for r in rows if r['epsilon']==0.0]
    assert np.allclose(observed,expected,atol=2e-12,rtol=2e-12),(observed,expected)
    # Independent n=2 endpoint must have same wavefunctions for any scalar two-body perturbation.
    assert max(abs(r['ratio_to_unperturbed_n2']-1) for r in rows if r['n']==2)<1e-12
    negative_control=midshell_opposite_signature_control(base[6][0],b2)
    result={'model':'12 single-particle m substates; identical fermions; H=-A00†A00+epsilon Σ_M A2M†A2M; reduced <j||Q2||j>=1','units':'dimensionless E2 strength and pairing-energy units','seed':None,'numpy':np.__version__,'scipy':scipy.__version__,'python':platform.python_version(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'b2_unperturbed':b2,'rows':rows,'opposite_signature_negative_control':negative_control,'checks':checks,'assertions':'3j reference signs, pair norm, single-particle tensor sum, H-Jplus commutator, eigen residuals, highest weights, Wigner-Eckart q=0 and -1, eigenvector sign, rephased and reordered Slater basis, particle-hole operator symmetry, n=2 scalar control, seniority analytical ratios, nonzero n=6 v=2 to opposite-signature v=4 E2 doorway and complete degenerate-subspace sum'}
    args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'b2':b2,'pure_ratios':observed,'n6_perturbation':[(r['epsilon'],r['ratio_to_unperturbed_n2'],r['overlap_J10'],r['overlap_J8']) for r in rows if r['n']==6],'opposite_signature_negative_control':negative_control,'max_commutator':max(x['rotational_commutator_norm'] for x in checks)},indent=2))

if __name__=='__main__': main()
