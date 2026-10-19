#!/usr/bin/env python3
"""Finish the existing D66 companion check over full native beta domains.

Tests sign feasibility only in four declared spin/population cases, with the
same AD marginal box. These are numerical model statements, not measured P.
"""
from __future__ import annotations
import argparse
from datetime import datetime
import hashlib
import heapq
import json
import math
from pathlib import Path
import time
from zoneinfo import ZoneInfo
import numpy as np
from scipy.optimize import linprog
from day16_diamond1966_three_ad_feasibility import kernel,coefficients
from day16_diamond1966_polarization_companion import at90,weight
from day16_diamond1966_continuous_domain import necessary_constraints,trig_bounds,separator,exact_coefficients


def sha(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()


def Q_components(top,jf,base):
    K,_,_=exact_coefficients(top,jf,base['quadrature_nodes'])
    expected=np.array([1.5*K[2][0],1.5*K[2][1]+.625*K[4][1],-.5*K[2][2]])
    assert np.max(abs(expected-at90(top,jf)[:,1,:]))<1e-12
    return expected


def point(top,mid,mode,betas,sign,c,base):
    n=(top+1)//2;A=[];b=[];vectors={}
    for line,jf,beta in [('331',mid,betas[0]),('701',9,betas[1])]:
        vectors[line]=coefficients(top,jf,beta,base['quadrature_nodes'])
        for k in [2,4]:
            mean,err=base['observations'][line]['a'+str(k)];v=vectors[line][k]
            A += [v,-v];b += [mean+err,-mean+err]
    J=top/2;m=np.array([J-i for i in range(n)]);u2=(3*m*m-J*(J+1))/(2*J*(2*J-1))
    if mode=='extra_lowm_u2nonpositive':A.append(u2);b.append(0.)
    mixed=weight(betas[1])@at90(top,9)[:,1,:]
    sg=1. if sign=='P701_nonpositive' else -1.
    A.append(sg*mixed);b.append(0.)
    fit=linprog(sg*mixed,A_ub=A,b_ub=b,A_eq=[np.ones(n)],b_eq=[1.],
        bounds=[(c['strict_q_floor'],None)]*n,method='highs')
    if not fit.success:return None
    q=fit.x;I=1-.5*(vectors['701'][2]@q)+.375*(vectors['701'][4]@q);P=float(mixed@q/I)
    if sg*P>=-100*c['certificate_min_margin']:return None
    residual=max(abs(q.sum()-1),max(0.,float(np.max(np.array(A)@q-np.array(b)))))
    assert residual<1e-8 and min(q)>=c['strict_q_floor']-1e-12 and abs(P)<=1+1e-12
    return {'q_pair':q.tolist(),'minimum_pair_probability':float(min(q)),
        'u2_population':float(u2@q),'betas_native_deg':betas,'P701':P,
        'observations':{line:{'a'+str(k):float(v[k]@q) for k in [2,4]} for line,v in vectors.items()},
        'max_constraint_residual':residual,'strict_sign_threshold':100*c['certificate_min_margin']}


def audit(top,mid,mode,sign,c,base,stop_at,deadline):
    initial=[[-90.,-90.] if abs(top-mid)==4 else [-90.,90.],[-90.,-90.] if abs(top-9)==4 else [-90.,90.]]
    heap=[(-max(b-a for a,b in initial),'',initial)];cert=[];undecided=[];processed=0
    legacy={'outer_coefficient_padding':c['outer_padding'],'certificate_min_margin':c['certificate_min_margin']}
    qcomp=Q_components(top,9,base)
    while heap:
        if time.monotonic()>stop_at or datetime.now(ZoneInfo('Asia/Shanghai'))>=deadline or processed>=c['max_cells_per_case']:
            undecided += [{'path':p,'box':b,'reason':'time/deadline/cellbudget'} for _,p,b in heap];break
        _,path,box=heapq.heappop(heap);processed+=1
        A,b=necessary_constraints(top,[('331',mid),('701',9)],box,mode,legacy,base)
        lo,hi=trig_bounds(qcomp,*box[1],c['outer_padding'])
        extra=lo if sign=='P701_nonpositive' else -hi
        A=np.vstack([A,extra]);b=np.r_[b,0.];sep=separator(A,b,legacy)
        if sep is not None:cert.append({'path':path,'box':box,**sep});continue
        centre=[(lo+hi)/2 for lo,hi in box];w=point(top,mid,mode,centre,sign,c,base)
        if w is not None:return {'status':'strict-nonzero-sign-witness','witness':w,'processed_cells':processed}
        widths=[hi-lo for lo,hi in box];axis=int(np.argmax(widths))
        if widths[axis]<=c['min_beta_width_deg']:
            undecided.append({'path':path,'box':box,'reason':'minimumwidth/possibleboundary'});continue
        lo,hi=box[axis];middle=(lo+hi)/2
        for bit,span in [('0',[lo,middle]),('1',[middle,hi])]:
            child=[list(x) for x in box];child[axis]=span
            heapq.heappush(heap,(-max(b-a for a,b in child),path+bit,child))
    return {'status':'numerically-separated-all-cells' if not undecided else 'undecided-cells-retained',
        'initial_box':initial,'negative_cells':cert,'undecided_cells':undecided,'processed_cells':processed}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--contract',required=True,type=Path);p.add_argument('--output',required=True,type=Path);a=p.parse_args();c=json.loads(a.contract.read_text());assert c['identity']=='D66-CURRENT-FULLBETA-P701-SIGN-DOMAIN-01';r=a.contract.parent
    for key in ['base_contract','fixed_projection_result','previous_domain_result']:assert sha(r/c[key])==c[key+'_sha256']
    base=json.loads((r/c['base_contract']).read_text());fixed=json.loads((r/c['fixed_projection_result']).read_text());start=time.monotonic();stop_at=start+c['total_runtime_budget_seconds'];deadline=datetime.fromisoformat(c['hard_deadline'])
    result={'at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),'script_sha256':sha(Path(__file__)),
        'contract_sha256':sha(a.contract),'all_frozen_inputs_unchanged':True,'results':[]}
    for item in c['cases']:
        for sign in c['polarization_sign_constraints']:
            z=audit(item['top2'],item['mid2'],item['mode'],sign,c,base,stop_at,deadline)
            result['results'].append({**item,'sign_constraint':sign,'audit':z});a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
            print('Psign',item['top2'],item['mid2'],sign,z['status'],z['processed_cells'],
                z.get('witness',{}).get('P701'),flush=True)
    defects=[]
    for case in fixed['cases']:
        top,mid=case['top_spin2'],case['middle_spin2'];beta=case['beta701_native_deg']
        # Use the exact population stored at the fixed projection endpoint to
        # check the interference identity independently at a physical point.
        q=np.array(case['individual_fixed_beta_P_projections']['701']['endpoint_witnesses'][0]['q_pair'])
        K=kernel(top,9,base['quadrature_nodes']);W=weight(beta);intA2=float(W[2]*(K[2][2]@q))
        A2=float(W@K[2]@q);A4=float(W@K[4]@q);I=1-.5*A2+.375*A4;Q=float(W@at90(top,9)[:,1,:]@q)
        difference=Q-(1.5*A2+.625*A4)
        assert abs(difference+2*intA2)<1e-12
        defects.append({'top2':top,'mid2':mid,'beta701':beta,'E2_fraction':float(W[1]),
            'A2_interference_contribution':intA2,'Q90_minus_pureformula':difference,
            'equals_minus2_A2interference':True})
    result.update(elapsed_seconds=time.monotonic()-start,interference_identity_controls=defects,
        independent_pureE2_sign_bound={'Q90_lower_from_sourcebox':1.5*(.26-.04)+.625*(-.03-.04),
            'applies_top13half_to_bottom9half_pureE2':True,'not_instrument_Q':True},
        scope={'same_native_M1E2_family_only':True,'not_experimental_P_or_spin_or_profileCI':True,
            'unknown_EMduality_alternatives_remain':True,'no_new_source_or_card':True})
    a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print('finished',result['elapsed_seconds'],flush=True)


if __name__=='__main__':main()
