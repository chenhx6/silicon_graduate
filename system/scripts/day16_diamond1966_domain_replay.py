#!/usr/bin/env python3
"""Independent high-precision replay of D66 numerical cell separators.

Rebuilds Racah coefficients and extrema without importing the interval or dual
solver. Checks dyadic coverage exactly and constructs interior point controls.
"""
from __future__ import annotations
import argparse
from datetime import datetime
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from pathlib import Path
from zoneinfo import ZoneInfo
import mpmath as mp
import numpy as np
from scipy.optimize import linprog
import sympy as s
from sympy.physics.wigner import clebsch_gordan,wigner_6j
from day16_diamond1966_three_ad_feasibility import coefficients


def sha(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()


def number(x):return mp.mpf(str(x))


@lru_cache(None)
def angular_coefficients(Ji2,Jf2,k,phase):
    Ji,Jf=s.Rational(Ji2,2),s.Rational(Jf2,2)
    tensor=[s.sqrt(2*Ji+1)*(-1)**i*clebsch_gordan(Ji,Ji,k,Ji-i,-Ji+i,0) for i in range((Ji2+1)//2)]
    out=[]
    for L,Lp in [(1,1),(2,2),(1,2)]:
        if abs(Ji-Jf)>L or abs(Ji-Jf)>Lp or k>L+Lp:factor=s.Integer(0)
        else:factor=(-1)**(Ji+Jf-1)*s.sqrt((2*L+1)*(2*Lp+1)*(2*Ji+1))*clebsch_gordan(L,Lp,k,1,-1,0)*wigner_6j(L,Lp,k,Ji,Ji,Jf)
        if L!=Lp:factor*=phase
        out.append([mp.mpf(str(s.N(z*factor,95))) for z in tensor])
    return out


def extrema(coef,lo,hi):
    a=(coef[0]+coef[1])/2;b=(coef[0]-coef[1])/2;c=coef[2]
    lo=mp.radians(2*number(lo));hi=mp.radians(2*number(hi))
    vals=[a+b*mp.cos(lo)+c*mp.sin(lo),a+b*mp.cos(hi)+c*mp.sin(hi)]
    phase=mp.atan2(c,b);R=mp.sqrt(b*b+c*c)
    # Independent amplitude representation for the critical values.
    for k in range(-3,4):
        peak=phase+2*k*mp.pi;trough=peak+mp.pi
        if lo<=peak<=hi:vals.append(a+R)
        if lo<=trough<=hi:vals.append(a-R)
    return min(vals),max(vals)


def bounds(Ji2,transitions,box,mode,base,phase_map):
    A=[];b=[]
    for (line,Jf2),(lo,hi) in zip(transitions,box):
        phase=phase_map[(Ji2,Jf2)]
        for k in [2,4]:
            C=angular_coefficients(Ji2,Jf2,k,phase)
            intervals=[extrema([C[j][i] for j in range(3)],lo,hi) for i in range(len(C[0]))]
            mean,err=map(number,base['observations'][line]['a'+str(k)])
            A += [[x[0] for x in intervals],[-x[1] for x in intervals]];b += [mean+err,-mean+err]
    if mode=='extra_lowm_u2nonpositive':
        J=mp.mpf(Ji2)/2
        A.append([(3*(J-i)**2-J*(J+1))/(2*J*(2*J-1)) for i in range((Ji2+1)//2)]);b.append(mp.mpf(0))
    return A,b


def verify_partition(initial,cells):
    paths=sorted(x['path'] for x in cells)
    assert len(set(paths))==len(paths)
    assert all(not b.startswith(a) for a,b in zip(paths,paths[1:]))
    assert sum((Fraction(1,2**len(p)) for p in paths),Fraction(0))==1
    for cell in cells:
        box=[list(v) for v in initial]
        for bit in cell['path']:
            widths=[hi-lo for lo,hi in box];axis=int(np.argmax(widths));lo,hi=box[axis];mid=(lo+hi)/2
            box[axis]=[lo,mid] if bit=='0' else [mid,hi]
        assert box==cell['box']


def point_values(Ji2,transitions,betas,q,base,phase_map):
    q=list(map(number,q));rows={}
    for (line,Jf2),beta in zip(transitions,betas):
        phase=phase_map[(Ji2,Jf2)];angle=mp.radians(number(beta));c=mp.cos(angle);sine=mp.sin(angle)
        rows[line]={}
        for k in [2,4]:
            C=angular_coefficients(Ji2,Jf2,k,phase)
            v=[C[0][i]*c*c+C[1][i]*sine*sine+2*C[2][i]*c*sine for i in range(len(q))]
            val=sum(x*y for x,y in zip(v,q));mean,err=map(number,base['observations'][line]['a'+str(k)])
            assert mean-err-mp.mpf('1e-10')<=val<=mean+err+mp.mpf('1e-10')
            rows[line]['a'+str(k)]=float(val)
    assert min(q)>0 and abs(sum(q)-1)<mp.mpf('1e-10')
    return rows


def interior(Ji2,transitions,betas,old,base,phase_map):
    floor=old['minimum_pair_probability']/2;n=len(old['q_pair']);A=[];b=[]
    for (line,Jf2),beta in zip(transitions,betas):
        vec=coefficients(Ji2,Jf2,beta,base['quadrature_nodes'])
        for k in [2,4]:
            mean,err=base['observations'][line]['a'+str(k)]
            A += [np.r_[vec[k],err],np.r_[-vec[k],err]];b += [mean+err,-mean+err]
    fit=linprog(np.r_[np.zeros(n),-1.],A_ub=A,b_ub=b,A_eq=[np.r_[np.ones(n),0]],b_eq=[1],
        bounds=[(floor,None)]*n+[(0,1)],method='highs')
    if not fit.success:return {'interior_slack_found':False,'old_witness_retained':True}
    eta=float(fit.x[-1]);q=fit.x[:-1];values=point_values(Ji2,transitions,betas,q,base,phase_map)
    return {'interior_slack_found':eta>1e-7,'fraction_of_quoted_box_halfwidth':eta,
        'pair_probability_floor':floor,'q_pair':q.tolist(),'minimum_pair_probability':float(min(q)),
        'betas_native_deg':betas,'observations_high_precision':values}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--contract',required=True,type=Path);p.add_argument('--output',required=True,type=Path);a=p.parse_args()
    cfg=json.loads(a.contract.read_text());assert cfg['identity']=='D66-DOMAIN-INDEPENDENT-CERTIFICATE-REPLAY-01';r=a.contract.parent
    assert sha(r/cfg['domain_contract'])==cfg['domain_contract_sha256'] and sha(r/cfg['domain_result'])==cfg['domain_result_sha256']
    dc=json.loads((r/cfg['domain_contract']).read_text());z=json.loads((r/cfg['domain_result']).read_text());base=json.loads((r/dc['base_contract']).read_text());grid=json.loads((r/dc['grid_result']).read_text());mp.mp.dps=cfg['precision_decimal_digits']
    phases={(x['Ji2'],x['Jf2']):x['native_cross_sign_relative_to_Racah_F12'] for x in z['coefficient_crosschecks']}
    checked=[];min_margin=mp.inf
    def negative(label,Ji2,transitions,mode,problem):
        nonlocal min_margin
        cells=problem['negative_cells'];verify_partition(problem['initial_box'],cells)
        for cell in cells:
            A,b=bounds(Ji2,transitions,cell['box'],mode,base,phases);lam=list(map(number,cell['lambda']));assert min(lam)>=0
            lhs=[sum(lam[j]*A[j][i] for j in range(len(lam))) for i in range(len(A[0]))]
            gap=min(lhs)-sum(x*y for x,y in zip(lam,b));assert gap>number(dc['certificate_min_margin'])
            assert gap>=number(cell['verified_min_vertex_minus_bound'])-mp.mpf('1e-12')
            min_margin=min(min_margin,gap)
        checked.append({'label':label,'covered_negative_cells':len(cells),'exact_Kraft_sum':1,'MP80_duals_passed':True})
    for key,problem in z['middle_audits'].items():
        if problem['status']=='numerically-separated-all-cells':
            Ji,mode=key.split(':',1);negative('middle:'+key,int(Ji),[('370',9)],mode,problem)
    newpoints=[];counts={}
    for row in z['sequence_audits']:
        top,mid,mode=row['top_spin2'],row['middle_spin2'],row['population_mode'];problem=row['upper_domain'];state=problem['status']
        if state=='numerically-separated-all-cells':negative(f'{top}/{mid}:{mode}',top,[('331',mid),('701',9)],mode,problem)
        elif state=='numerically-excluded-by-middle':assert z['middle_audits'][problem['middle_key']]['status']=='numerically-separated-all-cells'
        elif state=='new-strict-positive-point':
            original=problem['witness'];beta=problem['betas_native_deg']
            values=point_values(top,[('331',mid),('701',9)],beta,original['q_pair'],base,phases)
            mw=grid['middle_level_witnesses'][str(mid)+':'+mode];assert mw is not None
            newpoints.append({'top_spin2':top,'middle_spin2':mid,'mode':mode,
                'original_newpoint_MP80_observations':values,
                'upper_interior':interior(top,[('331',mid),('701',9)],beta,original,base,phases),
                'middle_interior':interior(mid,[('370',9)],[mw['beta_native_deg']],mw,base,phases)})
        counts.setdefault(mode,{});counts[mode][state]=counts[mode].get(state,0)+1
    assert len(newpoints)==1
    result={'at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),'script_sha256':sha(Path(__file__)),
        'contract_sha256':sha(a.contract),'precision_decimal_digits':mp.mp.dps,
        'negative_partition_and_dual_replays':checked,'minimum_MP80_separator_gap':str(min_margin),
        'new_strict_points':newpoints,'classification_status_counts':counts,
        'no_undecided_cells_in_this_bounded_result':all('undecided' not in x for q in counts.values() for x in q),
        'scope':{'announced_numerical_outerbounds_not_formal_exact_real_proof':True,
            'source_point_marginal_domain_not_experimental_spin_assignment':True,
            'no_original_author_five_count_or_actual_jointCI_reconstructed':True}}
    a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
