#!/usr/bin/env python3
"""Old Garg2015 table calibration response; not the unobserved2019 correction."""
from __future__ import annotations
import argparse
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
from zoneinfo import ZoneInfo
import sympy as sp


def sha(path:Path)->str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main()->None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--contract',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args();cfg=json.loads(args.contract.read_text());assert cfg['identity']=='GARG15-ORIGINAL-CALIBRATION-IDENTITY-01'
    root=Path(__file__).resolve().parents[2]
    raw=root/'raw/papers/gpt/high-spin-20260920/纲图/2015_Garg et al_Negative-parity high-spin states and a possible magnetic rotation band in Pr 76.pdf'
    assert sha(raw)==cfg['source_sha256']
    a,rho,lam=sp.symbols('a rho lambda',positive=True)
    d,old=sp.symbols('Delta a0',real=True)
    delta=(a-rho)/(a+rho)
    rho0=old*(1-d)/(1+d)
    transform=sp.factor(delta.subs({rho:rho0,a:lam*old}))
    assert sp.simplify(transform.subs(lam,1)-d)==0
    assert sp.simplify(transform.subs(lam,(1-d)/(1+d)))==0
    derivative=sp.simplify(a*sp.diff(delta,a))
    assert sp.simplify(derivative.subs(rho,rho0).subs(a,old)-(1-d*d)/2)==0
    rows=[];cal=cfg['a0_reported_approx'];sca=cfg['sigma_a0_reported']
    for z in cfg['rows_original2015']:
        x=dict(z,final_level_central_keV=z['Ei_keV']-z['E_keV'])
        if z['Delta2015'] is not None:
            value=z['Delta2015'];assert abs(value)<1
            ratio=cal*(1-value)/(1+value)
            threshold=(1-value)/(1+value)
            grad=(1-value*value)/(2*cal)
            x.update(Nparallel_over_Nperp_if_single_a0=ratio,
                signzero_a_if_original_central_counts_fixed=ratio,
                signzero_lambda_if_counts_fixed=threshold,
                derivative_wrt_a0_fixedcounts=grad,
                sigma_Delta_from_common_a0_only=grad*sca)
        rows.append(x)
    two=[x for x in rows if x['E_keV'] in [747.5,813.3]]
    m1=[x for x in rows if x['E_keV'] in [325.1,332.9,410.8,424.,429.7,498.5]]
    lower=max(x['signzero_lambda_if_counts_fixed'] for x in two)
    upper=min(x['signzero_lambda_if_counts_fixed'] for x in m1)
    assert lower>upper
    grads=[x['derivative_wrt_a0_fixedcounts'] for x in rows if x['Delta2015'] is not None]
    covariance=[[i*j*sca**2 for j in grads] for i in grads]
    # No covariance is inferred from whether source labels say M1 or E2;
    # those labels depend on the same data and are not independent constraints.
    result={'at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),
        'script_sha256':sha(Path(__file__)),'contract_sha256':sha(args.contract),
        'source_sha256':sha(raw),'calibration_transform_fixedcounts':str(transform),
        'dDelta_dln_a':str(derivative),'original_table_rows':rows,
        'single_global_scale_central_sign_test':{
            'lower_lambda_for_both747_813_positive':lower,
            'upper_lambda_to_keep_all_six_source_M1_negative':upper,
            'central_interval_nonempty':lower<upper,
            'counterexample_excludes_only':'Onecommonconstant a0scale with identicaloldcountledger, centralvalues and claimedpreservedsigns',
            'not_excluded':'energy/gatedependent a(E), background/peakresorting, uncertaintyintervals, differentcampaigns or actualerratum'},
        'conditional_common_a_covariance':{'dimension':len(grads),'matrix':covariance,
            'not_recovered_total_covariance':True,
            'not_added_to_quoted_errors':True,
            'sigma_a_point06_interpretation_is_conditional':True},
        'transition_aliases':[{'E_Garg':747.5,'same_path':'17/2−→15/2−','Matta_alias':747.0,'Lv_alias':747.3},
            {'E_Garg':813.3,'same_path':'21/2−→19/2−','Matta_alias':812.8,'Lv_alias':813.2}],
        'scope':{'original2015_not_latest2019':True,
            'original_netcounts_Q_response_aEproducer_recovered':False,
            'new_delta_fit_or_wobbling_ranking':False,
            'all_source_assignments_are_independent_validation':False}}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'transform':str(transform),'14oldrows':len(rows),
        '747_813_signzeros':[(x['E_keV'],x['signzero_a_if_original_central_counts_fixed'],x['sigma_Delta_from_common_a0_only']) for x in two],
        'one_global_scale_centraltest':result['single_global_scale_central_sign_test']},ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
