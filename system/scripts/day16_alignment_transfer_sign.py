#!/usr/bin/env python3
"""Exact rank-two transfer conditions under a fully unobserved emission.

CG/6j and polynomial certificates are model checks, not measured feeding or
alignment in Rh99. A directional-gate control deliberately changes the object.
"""
from __future__ import annotations
import argparse
from datetime import datetime
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path
from zoneinfo import ZoneInfo
import numpy as np
import sympy as s
from sympy.physics.wigner import clebsch_gordan, wigner_6j
from day16_co60_conditional_stokes import operators


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def moment(J, m):
    return 3*m*m-J*(J+1)


def projection(Ji,Jf,j):
    Ii=Ji*(Ji+1);Af=Jf*(Jf+1);x=(Ii+Af-j*(j+1))/2
    return s.factor((3*x*x-s.Rational(3,2)*x-Ii*Af)/(2*Ii*Ii-s.Rational(3,2)*Ii))


@lru_cache(None)
def cg(Jf,j,Ji,mf,q,mi):
    return clebsch_gordan(Jf,j,Ji,mf,q,mi)


def map_and_checks(Ji,Jf,j):
    mi=[-Ji+i for i in range(int(2*Ji)+1)]
    mf=[-Jf+i for i in range(int(2*Jf)+1)]
    T=s.zeros(len(mf),len(mi))
    for row,m in enumerate(mf):
        for col,M in enumerate(mi):
            q=M-m
            if abs(q)<=j:T[row,col]=cg(Jf,j,Ji,m,q,M)**2
    assert all(s.simplify(sum(T[:,k])-1)==0 for k in range(T.cols))
    assert all(x>=0 for x in T)
    uniform=T*s.ones(T.cols,1)/T.cols
    assert all(s.simplify(x-1/s.Integer(T.rows))==0 for x in uniform)
    vi=s.Matrix([moment(Ji,M) for M in mi]).T
    vf=s.Matrix([moment(Jf,m) for m in mf]).T
    if Ji<s.Integer(1):
        assert all(s.simplify(x)==0 for x in vf*T)
        return {'Ji':str(Ji),'Jf':str(Jf),'j':str(j),'rank2_parent_absent_child_moment_zero':True}
    c=projection(Ji,Jf,j)
    assert all(s.simplify(x)==0 for x in vf*T-c*vi),(Ji,Jf,j,c)
    if Jf>=1:
        a=lambda J:s.sqrt(5/(J*(J+1)*(2*J-1)*(2*J+3)))
        exact_U=s.simplify(c*a(Jf)/a(Ji))
        W=s.simplify(wigner_6j(Jf,Jf,2,Ji,Ji,j)/wigner_6j(Jf,Jf,0,Ji,Ji,j))
        assert s.simplify(exact_U-W)==0,(Ji,Jf,j,exact_U,W)
        normalized=s.factor(c*Ji*(2*Ji-1)/(Jf*(2*Jf-1)))
    else:exact_U=normalized=s.Integer(0)
    return {'Ji':str(Ji),'Jf':str(Jf),'j':str(j),'mu2_transfer_c':str(c),
        'statistical_tensor_U2':str(exact_U),'u2_transfer':str(normalized),
        'column_stochastic_isotropic_and_every_parent_m_exact':True,
        'independent_6j_match':True,'sign':int(s.sign(c))}


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--contract',required=True,type=Path)
    ap.add_argument('--output',required=True,type=Path)
    a=ap.parse_args();cfg=json.loads(a.contract.read_text());r=a.contract.parent
    assert cfg['identity']=='D66-UNOBSERVED-RANK2-TRANSFER-01'
    root=Path(__file__).resolve().parents[2]
    assert sha(root/cfg['raw'])==cfg['raw_sha256']
    assert sha(root/cfg['source'])==cfg['old_human_source_sha256']
    old=json.loads((r/'rh99-1117-feasibility-contract.json').read_text())
    for p,h in old['fixed_helper_hashes'].items():assert sha(root/p)==h
    # Exact positive-coefficient polynomials, covering all real s>=0 in a
    # domain stronger than just the allowed integer/half-integer spin grid.
    x=s.symbols('s',nonnegative=True);certificates=[]
    for L in [1,2]:
        for n in range(-L,L+1):
            Jf=s.Rational(5,2)+max(0,-n)+x;Ji=Jf+n
            Ii=Ji*(Ji+1);Af=Jf*(Jf+1);z=(Ii+Af-L*(L+1))/2
            N=s.Poly(s.expand(3*z*z-s.Rational(3,2)*z-Ii*Af),x)
            co=N.all_coeffs();assert all(t>0 for t in co),(L,n,N)
            den=s.Poly(s.expand(2*Ii*Ii-s.Rational(3,2)*Ii),x)
            assert all(t>0 for t in den.all_coeffs())
            row=map_and_checks(Ji.subs(x,0),Jf.subs(x,0),s.Integer(L))
            certificates.append({'L':L,'Ji_minus_Jf':n,'Jf_substitution':str(Jf),
                'positive_numerator_polynomial':str(N.as_expr()),
                'positive_denominator_polynomial':str(den.as_expr()),
                'all_coefficients_strictly_positive':True,'boundary_CG_check':row})
    assert len(certificates)==8
    actual=[map_and_checks(s.Rational(25,2),s.Rational(23,2),s.Integer(1)),
            map_and_checks(s.Rational(27,2),s.Rational(23,2),s.Integer(2))]
    particle_domain=[]
    for j2 in range(1,7):
        j=s.Rational(j2,2);Jf=s.Rational(23,2)
        for step in range(j2+1):
            Ji=Jf-j+step
            row=map_and_checks(Ji,Jf,j);assert row['sign']>0
            particle_domain.append(row)
    counter=[map_and_checks(s.Integer(1),s.Integer(1),s.Integer(1)),
             map_and_checks(s.Integer(2),s.Integer(2),s.Integer(2)),
             map_and_checks(s.Rational(23,2),s.Rational(23,2),s.Integer(11))]
    assert all(t['sign']<0 for t in counter)
    nulls=[map_and_checks(s.Integer(0),s.Integer(1),s.Integer(1)),
           map_and_checks(s.Rational(1,2),s.Rational(3,2),s.Integer(1))]
    # This direction-conditioned channel is distinct from the full trace.
    # Isotropic input has u2=0; observing a photon along beam can create u2>0.
    Ji2,Jf2=25,23;parent=np.eye(Ji2+1)/(Ji2+1);Jf=Jf2/2
    child_m=np.arange(-Jf,Jf+1);gates=[]
    for theta in [0.,math.pi/2]:
        op=operators(Ji2,Jf2,(("M",1,1.),),theta,0.,'native')
        rho=np.einsum('ari,ij,asj->rs',op,parent,op.conj());rho/=np.trace(rho)
        assert np.linalg.eigvalsh(rho).min()>-1e-12
        mu=float(np.dot(3*child_m**2-Jf*(Jf+1),np.diag(rho).real))
        gates.append({'theta_deg':math.degrees(theta),'mu2_child':mu,
            'u2_child':mu/(2*Jf*(2*Jf-1)),
            'full_direction_trace_child_u2':0.,'parent_isotropic_u2':0.,
            'normalized_density_min_eigenvalue':float(np.linalg.eigvalsh(rho).min())})
    assert gates[0]['u2_child']>1e-5 and gates[1]['u2_child']<0
    result={'at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),
        'script_sha256':sha(Path(__file__)),'contract_sha256':sha(a.contract),
        'raw_and_old_human_source_and_helpers_unchanged':True,
        'projection_formula':cfg['derived_projection_candidate'],
        'all_real_highspin_lowL_certificates':certificates,
        'actual_Rh99_spinpath_models':actual,
        'Jf23half_emittedj_half_to3_all27paths':particle_domain,
        'legal_signflip_counterexamples':counter,'no_rank2_parent_controls':nulls,
        'direction_gate_failure_control':gates,
        'scope':{'single_fulltrace_rotationally_covariant':True,
            'no_Gaussian_or_actual_feeding_weights':True,
            'no_newexperimental_u2_delta_parity_or_confidence':True,
            'not_a_global_theorem_for_all_reaction_particles_or_gates':True}}
    a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['actual_Rh99_spinpath_models','legal_signflip_counterexamples','direction_gate_failure_control','scope']},ensure_ascii=False,indent=2))
    print('positive domain certificates',len(certificates),'finite particle paths',len(particle_domain))


if __name__=='__main__':main()
