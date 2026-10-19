#!/usr/bin/env python3
"""Conservative numerical parameter-cell audit after the D66 finite grid.

Negative cells require an independently checkable nonnegative dual separator.
Budgets and boundary cells stay undecided. This is not experimental spin fitting
or a formally verified exact-real-arithmetic theorem.
"""
from __future__ import annotations
import argparse
from datetime import datetime
from functools import lru_cache
import hashlib
import heapq
import json
import math
from pathlib import Path
import time
from zoneinfo import ZoneInfo
import numpy as np
from scipy.optimize import linprog
import sympy as s
from sympy.physics.wigner import clebsch_gordan,wigner_6j
from day16_diamond1966_three_ad_feasibility import kernel,coefficients,witness


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


@lru_cache(None)
def exact_coefficients(Ji2,Jf2,nodes):
    J,F=s.Rational(Ji2,2),s.Rational(Jf2,2);n=(Ji2+1)//2
    def fk(L,Lp,k):
        if k>L+Lp or abs(J-F)>L or abs(J-F)>Lp:return s.Integer(0)
        return s.simplify((-1)**(J+F-1)*s.sqrt((2*L+1)*(2*Lp+1)*(2*J+1))*
            clebsch_gordan(L,Lp,k,1,-1,0)*wigner_6j(L,Lp,k,J,J,F))
    out={};old=kernel(Ji2,Jf2,nodes);maximum=0.;sign=0
    for k in [2,4]:
        b=[s.simplify(s.sqrt(2*J+1)*(-1)**i*clebsch_gordan(J,J,k,J-i,-J+i,0)) for i in range(n)]
        arr=np.array([[float(s.N(z*fk(L,Lp,k),45)) for z in b] for L,Lp in [(1,1),(2,2),(1,2)]])
        if k==2 and np.max(abs(arr[2]))>1e-14:
            plus=np.max(abs(arr[2]-old[k][2]));minus=np.max(abs(-arr[2]-old[k][2]))
            sign=1 if plus<minus else -1
        if sign:arr[2]*=sign
        maximum=max(maximum,float(np.max(abs(arr-old[k]))));out[k]=arr
    assert maximum<3e-12,(Ji2,Jf2,maximum)
    return out,maximum,sign


def trig_bounds(K,lo,hi,pad):
    low=2*math.radians(lo);high=2*math.radians(hi)
    offset=(K[0]+K[1])/2;co=(K[0]-K[1])/2;si=K[2]
    lower=[];upper=[]
    for a,b,c in zip(offset,co,si):
        points=[a+b*math.cos(low)+c*math.sin(low),a+b*math.cos(high)+c*math.sin(high)]
        phase=math.atan2(c,b)
        for integer in range(-3,4):
            angle=phase+integer*math.pi
            if low-1e-15<=angle<=high+1e-15:points.append(a+b*math.cos(angle)+c*math.sin(angle))
        lower.append(min(points)-pad);upper.append(max(points)+pad)
    lower=np.array(lower);upper=np.array(upper)
    for beta in [lo,(lo+hi)/2,hi]:
        rad=math.radians(2*beta);v=offset+co*math.cos(rad)+si*math.sin(rad)
        assert np.all(v>=lower) and np.all(v<=upper)
    return lower,upper


def necessary_constraints(Ji2,transitions,box,mode,cfg,base):
    A=[];b=[]
    for (line,Jf2),(lo,hi) in zip(transitions,box):
        K,_,_=exact_coefficients(Ji2,Jf2,base['quadrature_nodes'])
        for rank in [2,4]:
            lower,upper=trig_bounds(K[rank],lo,hi,cfg['outer_coefficient_padding'])
            mean,error=base['observations'][line]['a'+str(rank)]
            A += [lower,-upper];b += [mean+error,-mean+error]
    if mode=='extra_lowm_u2nonpositive':
        J=Ji2/2;m=np.array([J-i for i in range((Ji2+1)//2)])
        A.append((3*m*m-J*(J+1))/(2*J*(2*J-1)));b.append(0.)
    return np.array(A),np.array(b)


def separator(A,b,cfg):
    m,n=A.shape
    constraints=np.column_stack(((-A+b[:,None]).T,np.ones(n)))
    fit=linprog(np.r_[np.zeros(m),-1.],A_ub=constraints,b_ub=np.zeros(n),
        A_eq=np.array([np.r_[np.ones(m),0.]]),b_eq=[1.],bounds=[(0,None)]*m+[(None,None)],
        method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
    if not fit.success:return None
    lam=fit.x[:m]
    if np.min(lam)<0:return None
    margin=float(np.min(lam@A)-lam@b)
    if margin>cfg['certificate_min_margin']:
        assert abs(sum(lam)-1)<1e-7
        return {'lambda':lam.tolist(),'verified_min_vertex_minus_bound':margin}
    return None


def audit(Ji2,transitions,mode,cfg,base,stop_at,deadline):
    initial=[[-90.,-90.] if abs(Ji2-jf)==4 else [-90.,90.] for _,jf in transitions]
    heap=[(-max(hi-lo for lo,hi in initial),'',initial)]
    cert=[];unresolved=[];processed=0
    while heap:
        if time.monotonic()>stop_at or datetime.now(ZoneInfo('Asia/Shanghai'))>=deadline:
            unresolved += [{'path':path,'box':box,'reason':'time-budget-or-original-deadline'} for _,path,box in heap]
            heap=[];break
        if processed>=cfg['max_cells_per_problem']:
            unresolved += [{'path':path,'box':box,'reason':'cell-budget'} for _,path,box in heap]
            heap=[];break
        _,path,box=heapq.heappop(heap);processed+=1
        A,b=necessary_constraints(Ji2,transitions,box,mode,cfg,base)
        sep=separator(A,b,cfg)
        if sep is not None:cert.append({'path':path,'box':box,**sep});continue
        centre=[(lo+hi)/2 for lo,hi in box]
        obs=[(line,coefficients(Ji2,jf,beta,base['quadrature_nodes'])) for (line,jf),beta in zip(transitions,centre)]
        point=witness(Ji2,obs,mode,base)
        if point is not None:
            return {'status':'new-strict-positive-point','betas_native_deg':centre,
                'witness':point,'processed_cells':processed,'negative_cells_before_point':len(cert),
                'all_parameter_exclusion_claimed':False}
        widths=[hi-lo for lo,hi in box];axis=int(np.argmax(widths))
        if widths[axis]<=cfg['min_beta_width_deg']:
            unresolved.append({'path':path,'box':box,'reason':'min-width-no-strict-point-or-separator'});continue
        lo,hi=box[axis];mid=(lo+hi)/2
        for bit,endpoints in [('0',[lo,mid]),('1',[mid,hi])]:
            child=[list(x) for x in box];child[axis]=endpoints
            heapq.heappush(heap,(-max(h-l for l,h in child),path+bit,child))
    status='numerically-separated-all-cells' if not unresolved else 'undecided-cells-retained'
    return {'status':status,'processed_cells':processed,'initial_box':initial,
        'negative_cells':cert,'undecided_cells':unresolved,
        'numerical_outerbounds_not_formal_exact_arithmetic':True}


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--contract',required=True,type=Path);p.add_argument('--output',required=True,type=Path);args=p.parse_args()
    c=json.loads(args.contract.read_text());assert c['identity']=='D66-POSTGRID-CONSERVATIVE-CONTINUOUS-DOMAIN-01'
    root=Path(__file__).resolve().parents[2];r=args.contract.parent
    assert sha(r/c['base_contract'])==c['base_contract_sha256'] and sha(r/c['grid_result'])==c['grid_result_sha256']
    base=json.loads((r/c['base_contract']).read_text());grid=json.loads((r/c['grid_result']).read_text())
    assert sha(root/base['source'])==base['source_current_sha256'] and sha(root/base['raw'])==base['raw_sha256']
    for path,h in base['fixed_helpers'].items():assert sha(root/path)==h
    start=time.monotonic();stop_at=start+c['total_runtime_budget_seconds'];deadline=datetime.fromisoformat(c['hard_stop_original'])
    result={'at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),'script_sha256':sha(Path(__file__)),
        'contract_sha256':sha(args.contract),'source_and_input_hashes_unchanged':True,
        'middle_audits':{},'sequence_audits':[],'coefficient_crosschecks':[]}
    for Ji2,Jf2 in grid['nineteen_sequences']:
        _,err,phase=exact_coefficients(Ji2,Jf2,base['quadrature_nodes'])
        result['coefficient_crosschecks'].append({'Ji2':Ji2,'Jf2':Jf2,'max_error':err,
            'native_cross_sign_relative_to_Racah_F12':phase,'not_a_map_to_D66_author_delta':True})
    def save():args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    for key,old in grid['middle_level_witnesses'].items():
        Ji2,mode=key.split(':',1)
        z={'status':'existing-grid-strict-point'} if old is not None else audit(int(Ji2),[('370',9)],mode,c,base,stop_at,deadline)
        result['middle_audits'][key]=z;save();print('middle',key,z['status'],z.get('processed_cells',0),flush=True)
    for old in grid['sameparent_results']:
        top,mid,mode=old['top_spin2'],old['middle_spin2'],old['population_mode'];middle=result['middle_audits'][old['middle_witness_key']]
        if old['strict_upper_witness'] is not None:z={'status':'existing-grid-strict-point'}
        elif middle['status']=='numerically-separated-all-cells':z={'status':'numerically-excluded-by-middle','middle_key':old['middle_witness_key']}
        else:z=audit(top,[('331',mid),('701',9)],mode,c,base,stop_at,deadline)
        result['sequence_audits'].append({'top_spin2':top,'middle_spin2':mid,'population_mode':mode,
            'middle_status':middle['status'],'upper_domain':z})
        save();print('sequence',top,mid,mode,z['status'],z.get('processed_cells',0),flush=True)
    result['elapsed_seconds']=time.monotonic()-start
    result['scope']={'only_declared_point_positive_population_marginal_domain':True,
        'no_new_experimental_spin_delta_or_CI':True,'undecided_not_excluded':True,
        'floating_padding_and_margin_assumptions_explicit':True,'no_new_source_or_daycard':True}
    save();print('finished bounded audit',round(result['elapsed_seconds'],3),flush=True)


if __name__=='__main__':main()
