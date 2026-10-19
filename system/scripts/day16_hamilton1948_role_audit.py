#!/usr/bin/env python3
"""Hamilton1948 exact 16-case role audit; no isotope counts or delta fitting."""
from __future__ import annotations
import argparse
from datetime import datetime
import hashlib
import itertools
import json
from pathlib import Path
from zoneinfo import ZoneInfo
import sympy as sp
from sympy.physics.wigner import wigner_6j


def sha(path:Path)->str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main()->None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--contract',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args();cfg=json.loads(args.contract.read_text())
    assert cfg['identity']=='HAM48-PHOTON-ROLE-WEIGHT-01'
    root=Path(__file__).resolve().parents[2]
    raw=root/'raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1948_Hamilton_Polarization and Direction of Propagation of Successive Quanta.pdf'
    assert sha(raw)==cfg['source_sha256']
    a,b,t=sp.symbols('alpha2 alpha4 cos_theta_squared',real=True)
    wf,wl=sp.symbols('alphaAB alphaBC',positive=True)
    def intensity(kind:str,bb:sp.Expr)->tuple:
        if kind[1]=='1':
            f=3/(3+a);values=(f*(1+a*(2*t-1)),f*(1+a))
        else:
            f=15/(15+5*a+3*bb)
            values=(f*(1+a+bb-2*bb*t*(1-t)),f*(1+(a+bb)*(2*t-1)))
        return values if kind[0]=='E' else values[::-1]
    rows=[];derived={}
    expected_independent={('E1','E1'),('M1','M1'),('E2','E2'),('M2','M2'),
        ('E1','M2'),('M2','E1'),('M1','E2'),('E2','M1')}
    for first,last in itertools.product(cfg['multipoles'],repeat=2):
        bb=b if first[1]==last[1]=='2' else sp.Integer(0)
        ftheta,fphi=intensity(first,bb);ltheta,lphi=intensity(last,bb)
        Itheta=sp.factor((wf*ftheta+wl*ltheta)/(wf+wl))
        Iphi=sp.factor((wf*fphi+wl*lphi)/(wf+wl))
        total=sp.factor(Itheta+Iphi)
        W=1+a*t+bb*t*t
        k=30/(15+5*a+3*bb) if first[1]==last[1]=='2' else 6/(3+a)
        assert sp.simplify(total-k*W)==0,(first,last)
        pol=sp.factor((Itheta-Iphi)/total)
        independent=sp.simplify(sp.diff(pol,wf))==0
        assert independent==((first,last) in expected_independent)
        assert sp.simplify((Itheta-Iphi).subs(t,1))==0
        if not independent:assert sp.simplify(pol.subs(wf,wl))==0
        derived[(first,last)]=(Itheta,Iphi,pol,bb)
        rows.append({'first':first,'last':last,'polarization_theta':str(Itheta),
            'polarization_phi':str(Iphi),'P_plane':str(pol),
            'rank4_available_in_formula':bool(bb!=0),
            'role_weights_cancel_from_polarization':bool(independent),
            'equal_weights_P_if_dependent':0 if not independent else None,
            'normalized_sum_over_W':str(k)})
    maximum_symbolic_errors=[]
    for (first,last),(it,ip,pol,bb) in derived.items():
        jt,jp,_,_=derived[(last,first)]
        assert sp.simplify(jt.subs({wf:wl,wl:wf},simultaneous=True)-it)==0
        assert sp.simplify(jp.subs({wf:wl,wl:wf},simultaneous=True)-ip)==0
        swap=lambda kind:('M' if kind[0]=='E' else 'E')+kind[1]
        mt,mp,_,_=derived[(swap(first),swap(last))]
        assert sp.simplify(mt-ip)==0 and sp.simplify(mp-it)==0
    qtheta,qphi=intensity('E2',b)
    wrong_qphi=15/(15+5*a+3*b)*(1+(a+b)*t)
    wrong_residual=sp.factor(qtheta+wrong_qphi-30/(15+5*a+3*b)*(1+a*t+b*t*t))
    assert wrong_residual!=0
    # A rank-four analyzer coefficient is not guaranteed solely by E2,E2.
    # The allowed pure-E2 path Ji=2 -> J=1 -> Jf=2 has max density rank 2.
    rank4=wigner_6j(2,2,4,1,1,2)
    assert rank4==0
    # Coefficients are physical angular functions, not arbitrary data.
    result={'at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),
        'script_sha256':sha(Path(__file__)),'contract_sha256':sha(args.contract),
        'source_sha256':sha(raw),'rows':rows,
        'exact_control_summary':{'sixteen_sequences':len(rows),
            'weight_independent_cases':sum(x['role_weights_cancel_from_polarization'] for x in rows),
            'weight_dependent_cases':sum(not x['role_weights_cancel_from_polarization'] for x in rows),
            'equal_weight_washout_dependent_cases':8,'collinear_nulls':16,
            'role_exchange_with_weight_exchange':16,'global_EM_dual_swaps_fields':16,
            'all_normalized_sums_recover_source_W':True},
        'wrong_OCR_control':{'wrong_use':'qphi cos(theta)^2 instead of cos(2theta)',
            'sum_minus_correct_W':str(wrong_residual),'failure_observed_symbolically':True,
            'not_source_erratum':True},
        'rank4_classifier_boundary':{'declaration':'allowed pureE2 path2→1→2',
            'max_intermediate_density_rank':2,'F4_geometric_6j':str(rank4),
            'all_pure_QQ_have_nonzero_alpha4_not_guaranteed':True,
            'claim_kind':'selection-rule inference; not experimental band or state assignment'},
        'scope':{'original_shapes_replayed':True,'any_new_toy_counts_or_delta_fit':False,
            'actual_array_phi_response_or_joint_cov_recovered':False,
            'mixed_transition_amplitude_phase_bridge_established':False}}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'controls':result['exact_control_summary'],
        'OCR_failure':result['wrong_OCR_control'],'rank4':result['rank4_classifier_boundary']},ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
