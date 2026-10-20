#!/usr/bin/env python3
"""VT74 exact rank coefficients vs independent Eq9/22 helicity amplitudes."""
from datetime import datetime, timezone
from functools import lru_cache
import hashlib
import json
from pathlib import Path

import sympy as sp
from sympy.physics.wigner import clebsch_gordan as cg, racah, wigner_d_small

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'
D=sp.Symbol('d',real=True)


@lru_cache(None)
def prefactor(ji,jf,ell,other,rank):
    if not abs(ell-other)<=rank<=ell+other:
        return sp.S.Zero
    return ((-1)**(1+ji-jf+other-ell-rank)
            *sp.sqrt((2*ji+1)*(2*ell+1)*(2*other+1))
            *racah(ji,ji,ell,other,rank,jf))


def coefficient(ji,jf,ell,other,rank,polarized=False):
    pref=prefactor(ji,jf,ell,other,rank)
    if polarized:
        return (sp.S.Zero if rank<2 else -pref
                *sp.sqrt(sp.factorial(rank-2)/sp.factorial(rank+2))
                *cg(ell,other,rank,1,1,2))
    return pref*cg(ell,other,rank,1,-1,0)


@lru_cache(None)
def rotation(ell,theta):
    return wigner_d_small(ell,theta)


def evaluate(case,theta):
    ji,jf=sp.Rational(case['Ji2'],2),sp.Rational(case['Jf2'],2)
    pop=list(map(sp.Rational,case['population']))
    assert len(pop)==2*ji+1 and sum(pop)==1 and min(pop)>=0
    parts=[(kind,ell,sp.sympify(a,locals={'d':D})) for kind,ell,a in case['multipoles']]
    norm=sum(a*a for _,_,a in parts)
    rank_i=rank_s=sp.S.Zero
    for rank in range(0,int(2*ji)+1,2):
        b=sum((-1)**(ji-mi)*sp.sqrt(2*ji+1)*cg(ji,ji,rank,mi,-mi,0)*p
              for mi,p in zip([(-case['Ji2']+2*i)/sp.S(2) for i in range(len(pop))],pop))
        rr=hh=sp.S.Zero
        for kind,ell,a in parts:
            for otherkind,other,amp in parts:
                rr+=a*amp*coefficient(ji,jf,ell,other,rank)
                hh+=a*amp*(-1)**(otherkind=='M')*coefficient(ji,jf,ell,other,rank,True)
        rank_i+=b*rr*sp.legendre(rank,sp.cos(theta))/norm
        if rank>=2:
            rank_s+=b*hh*sp.assoc_legendre(rank,2,sp.cos(theta))/norm
    helicities={}
    for h in [-1,1]:
        op=sp.zeros(case['Jf2']+1,case['Ji2']+1)
        for i in range(case['Jf2']+1):
            mf=(-case['Jf2']+2*i)/sp.S(2)
            for j in range(case['Ji2']+1):
                mi=(-case['Ji2']+2*j)/sp.S(2);mu=mi-mf
                for kind,ell,a in parts:
                    if abs(mu)<=ell:
                        op[i,j]+=sp.sqrt(2*ell+1)*a*h**(kind=='M')*cg(jf,ell,ji,mf,mu,mi)*rotation(ell,theta)[ell-int(mu),ell-h]
        helicities[h]=op
    x=(-helicities[1]+helicities[-1])/sp.sqrt(2)
    y=-sp.I*(helicities[1]+helicities[-1])/sp.sqrt(2)
    ix=sum(x[i,j]*sp.conjugate(x[i,j])*pop[j] for i in range(x.rows) for j in range(x.cols))
    iy=sum(y[i,j]*sp.conjugate(y[i,j])*pop[j] for i in range(y.rows) for j in range(y.cols))
    direct_i,direct_s=sp.simplify((ix+iy)/(2*norm)),sp.simplify((ix-iy)/(2*norm))
    assert sp.simplify(rank_i-direct_i)==0,(case['id'],theta,'I')
    assert sp.simplify(rank_s-direct_s)==0,(case['id'],theta,'S')
    return direct_i,direct_s


def main():
    path=RUN/'vaillancourt1974-response-contract.json';contract=json.loads(path.read_text())
    angles=[sp.sympify(t) for t in contract['angles']]
    rows=[]
    for case in contract['cases']:
        for theta in angles:
            ii,ss=evaluate(case,theta)
            rows.append({'case':case['id'],'theta':str(theta),'I':str(ii),'S':str(ss)})
    limit_controls=[]
    for case in contract['cases']:
        flipped=dict(case)
        flipped['multipoles']=[['M' if kind=='E' else 'E',ell,a] for kind,ell,a in case['multipoles']]
        for theta in [sp.pi/6,sp.pi/2]:
            ii,ss=evaluate(case,theta)
            fi,fs=evaluate(flipped,theta)
            assert sp.simplify(fi-ii)==0 and sp.simplify(fs+ss)==0
        unoriented=dict(case)
        unoriented['population']=[str(sp.Rational(1,case['Ji2']+1))]*(case['Ji2']+1)
        ui,us=evaluate(unoriented,sp.pi/3)
        assert sp.simplify(ui-1)==0 and sp.simplify(us)==0
        limit_controls.append({'case':case['id'],'all_EM_flip_I_same_S_opposite':True,
                               'unoriented_I1_S0':True})
    truncated=dict(contract['cases'][1])
    truncated['multipoles']=[list(p) for p in truncated['multipoles']]
    truncated['multipoles'][2][2]='0'
    two=dict(truncated);two['multipoles']=two['multipoles'][:2]
    for theta in angles:
        ii,ss=evaluate(truncated,theta);ti,ts=evaluate(two,theta)
        assert sp.simplify(ii-ti)==0 and sp.simplify(ss-ts)==0
    i0,s0=evaluate(contract['cases'][0],sp.S.Zero)
    i90,s90=evaluate(contract['cases'][0],sp.pi/2)
    roots=sp.solve(sp.together(i0-i90),D)
    iso=[]
    for root in roots:
        for theta in angles:
            ii,ss=evaluate(contract['cases'][0],theta)
            assert sp.simplify(ii.subs(D,root)-1)==0
            iso.append({'delta':str(root),'theta':str(theta),'I':'1','S':str(sp.simplify(ss.subs(D,root)))})
    zero=[]
    for ell in range(1,contract['zero_CG_grid_Lmax']+1):
        for other in range(1,contract['zero_CG_grid_Lmax']+1):
            for rank in range(2,ell+other+1,2):
                if cg(ell,other,rank,1,-1,0)==0 and cg(ell,other,rank,1,1,2)!=0:
                    zero.append([ell,other,rank,str(cg(ell,other,rank,1,1,2))])
    selected=coefficient(sp.S(3),sp.S(2),3,5,6,True)
    assert coefficient(sp.S(3),sp.S(2),3,5,6)==0 and selected!=0
    p,r=sp.symbols('p r',positive=True)
    nn=(p*r+1)/(p+r)
    assert sp.simplify((nn-1)/(nn+1)-(p-1)/(p+1)*(r-1)/(r+1))==0
    result={'at':datetime.now(timezone.utc).isoformat(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'contract_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'rank_and_Eq9_amplitude_rows':rows,'isotropic_AD_nonzero_P_controls':iso,
        'EM_and_unoriented_controls':limit_controls,'third_multipole_zero_limit':True,
        'isotropic_AD_roots':list(map(str,roots)),
        'zero_CG_nonzero_polarized_CG':zero,
        'selected_J3_to_J2_L3_L5_K6_finite_R_times_K':str(selected),
        'Eq53_56_ratio_to_boundedP_and_countA_exact':True,
        'exact_rank_vs_direct_amplitude_controls':True,
        'zeroCG_product_and_isotropic_AD_P_controls':True,
        'no_actual_35Cl_37Ar_fit_or_original_producer_Q_CI':True,'ok':True}
    (RUN/'vaillancourt1974-response-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print('rows',len(rows),'isotropic roots',list(map(str,roots)),'zero CG',zero,'finite',selected,'OK')


if __name__=='__main__':
    main()
