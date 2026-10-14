#!/usr/bin/env python3
"""Angular information about photon order in chosen pure-E2 cascades.

No 193Bi spin, population, photon count or covariance is fitted. A maximal
coupling proof is compared with a separate total-J^2/ladder construction.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

from day14_conditional_angular_response import direction,rotation_columns


def raising(spin):
    m=np.arange(spin,-spin-1,-1);a=np.zeros((len(m),len(m)))
    for col,x in enumerate(m):
        if x<spin:a[col-1,col]=np.sqrt(spin*(spin+1)-x*(x+1))
    return m,a


def coupling(j_lower,rank,j_upper):
    """CG coefficients from total J^2, fixed highest M, and total lowering."""
    lo,a=raising(j_lower);mu,b=raising(rank)
    plus=np.kron(a,np.eye(len(mu)))+np.kron(np.eye(len(lo)),b)
    minus=plus.T;m=(lo[:,None]+mu).ravel()
    j2=minus@plus+np.diag(m*(m+1))
    selected=np.flatnonzero(np.isclose(m,j_upper))
    values,vectors=np.linalg.eigh(j2[np.ix_(selected,selected)])
    eigen_index=np.argmin(abs(values-j_upper*(j_upper+1)))
    if abs(values[eigen_index]-j_upper*(j_upper+1))>1e-10:raise ValueError('triangle fails')
    state=np.zeros(len(m));state[selected]=vectors[:,eigen_index]
    if state[selected[0]]<0:state=-state
    rows=[]
    for step in range(round(2*j_upper)+1):
        rows.append(state.reshape(len(lo),len(mu)).copy())
        current=j_upper-step
        if step<round(2*j_upper):state=minus@state/np.sqrt((j_upper+current)*(j_upper-current+1))
    return np.array(rows)


def maximal_coupling(j_lower,rank):
    upper=j_lower+rank;mi=np.arange(upper,-upper-1,-1);mf=np.arange(j_lower,-j_lower-1,-1);mu=np.arange(rank,-rank-1,-1)
    result=np.zeros((len(mi),len(mf),len(mu)))
    for i,x in enumerate(mi):
        for f,y in enumerate(mf):
            q=x-y
            if abs(q)<=rank:
                result[i,f,round(rank-q)]=math.sqrt(math.comb(round(2*j_lower),round(j_lower+y))*math.comb(2*rank,round(rank+q))/math.comb(round(2*upper),round(upper+x)))
    return result


def amplitude(c1,c2,n1,n2,rank=2):
    first=np.einsum('imk,kq->imq',c1,rotation_columns(rank,n1))*np.sqrt((2*rank+1)/2)
    second=np.einsum('mfk,ks->mfs',c2,rotation_columns(rank,n2))*np.sqrt((2*rank+1)/2)
    return np.einsum('imq,mfs->ifqs',first,second)


def intensity(s,rho):
    flat=s.reshape(len(rho),-1)
    return float(np.einsum('ij,ia,ja->',rho,flat,flat.conj()).real)


def audit():
    checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    points=[direction(np.deg2rad(t),p) for t,p in [(32,0),(90,0),(157.6,.8),(75.5,-.3)]]
    rng=np.random.default_rng(1405);results=[]
    for spins in [(9.5,7.5,5.5),(9.5,8.5,6.5)]:
        ji,jm,jf=spins;c1=coupling(jm,2,ji);c2=coupling(jf,2,jm)
        check(f'{spins}_CG_rows_normalized',np.allclose(np.sum(c1*c1,axis=(1,2)),1) and np.allclose(np.sum(c2*c2,axis=(1,2)),1))
        m=np.arange(ji,-ji-1,-1);p=np.exp(-m*m/(2*(.3*ji)**2));p/=p.sum()
        psi=rng.normal(size=len(m))+1j*rng.normal(size=len(m));psi/=np.linalg.norm(psi)
        states={'random':np.eye(len(m))/len(m),'chosen_Gaussian_sigma_J_point3':np.diag(p),'chosen_coherent_state':np.outer(psi,psi.conj())}
        for name,rho in states.items():
            check(f'{spins}_{name}_rho_PSD_trace_one',np.linalg.eigvalsh(rho).min()>-1e-13 and np.isclose(np.trace(rho),1))
        swaps=[];physical=[]
        for a in points:
            for b in points:
                s=amplitude(c1,c2,a,b);rev=amplitude(c1,c2,b,a)
                swaps.append(float(np.max(abs(s-rev.swapaxes(-1,-2)))))
                physical.append({name:abs(intensity(s,rho)-intensity(rev,rho)) for name,rho in states.items()})
                check(f'{spins}_positive_intensities_{len(physical)}',all(intensity(s,rho)>-1e-13 for rho in states.values()))
        errors={name:max(v[name] for v in physical) for name in states}
        check(f'{spins}_random_intensity_exchange_symmetry',errors['random']<1e-12)
        # The real normalized feeding density from the first unobserved gamma.
        middle=np.einsum('i,imk,ink->mn',p,c1,c1)
        random_middle=np.einsum('i,imk,ink->mn',np.ones(len(m))/len(m),c1,c1)
        check(f'{spins}_feeding_density_PSD_trace_one',np.linalg.eigvalsh(middle).min()>-1e-13 and np.isclose(np.trace(middle),1))
        check(f'{spins}_random_feeding_is_random',np.allclose(random_middle,np.eye(len(middle))/len(middle)))
        if jm==jf+2 and ji==jm+2:
            check('maximal_binomial_and_J2_ladder_independent_agreement',np.allclose(c1,maximal_coupling(jm,2),atol=1e-13) and np.allclose(c2,maximal_coupling(jf,2),atol=1e-13))
            check('stretched_full_amplitude_exchange_symmetry',max(swaps)<1e-12)
            check('stretched_even_coherent_initial_does_not_rescue_angular_order',max(errors.values())<1e-12)
        else:
            check('nonstretched_amplitudes_need_not_be_exchange_symmetric',max(swaps)>.01)
            check('nonstretched_chosen_alignment_can_break_intensity_symmetry',errors['chosen_Gaussian_sigma_J_point3']>1e-4)
        a,b=points[2:];s,rev=amplitude(c1,c2,a,b),amplitude(c1,c2,b,a)
        mj=np.arange(jm,-jm-1,-1);gauss_mid=np.exp(-mj*mj/(2*(.3*jm)**2));gauss_mid/=gauss_mid.sum()
        results.append({'chosen_spins':spins,'full_amplitude_swap_max_error':max(swaps),'intensity_swap_max_errors':errors,
                        'chosen_point_pair':[{'theta_deg':157.6,'phi_rad':.8},{'theta_deg':75.5,'phi_rad':-.3}],'point_intensities':{name:{'first_at_a_second_at_b':intensity(s,rho),'first_at_b_second_at_a':intensity(rev,rho)} for name,rho in states.items()},
                        'exact_unobserved_feeding_middle_population':middle.diagonal().tolist(),'separately_assumed_sigma_over_J_point3_middle_population':gauss_mid.tolist(),'middle_population_L1_distance':float(np.sum(abs(middle.diagonal()-gauss_mid)))})
    return {'kind':'L2 angular-order identifiability; selected static pure-E2 spin cascades',
            'source_locators':['HE15-9 / Table I footnote f: unresolved order','RB67-3 / printed326 PDF21 Eq3.73: random initial condition','RB67-11 / printed316 PDF11 Eq3.24: CG/helicity amplitudes'],
            'results':results,'checks':checks,'checks_passed':sum(checks.values()),
            'boundaries':['No actual weak-line spin/parity assignment, population, counts or covariance is supplied.','Random-initial intensity symmetry follows rotational covariance for the static cascade, not the0-L-0specialcase alone.','Two equal-rank pure stretched downward transitions have a stronger full-amplitude swap symmetry in this no-intermediate-evolution model.','Chosen alignment does not break that maximal-coupling symmetry; nonstretched control can break intensity symmetry.','Known same-rank electromagnetic type, definite parity, fixed energy modes, complete final-spin trace and a common instrument are assumptions.','Unobserved feeding population is computed from the first transition; independently imposing the same sigma/J at each level is another input.','Intermediate interactions/time evolution, mixed or different multipoles, branches, independent levels and time tags require separate analysis.','Day14 continues; Day15 preview remains uncredited.']}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();args.output.resolve().relative_to(Path(__file__).resolve().parents[2]);result=audit()
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'checks_passed':result['checks_passed'],'results':result['results']},ensure_ascii=False))


if __name__=='__main__':main()
