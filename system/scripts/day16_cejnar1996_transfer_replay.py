#!/usr/bin/env python3
"""Replay Cejnar1996 Fig1 model paths and audit the signed Eq6 domain.

The source's model sequences are not experimental populations. Gaussian
moment inversions use exact polynomial root counts and do not fit any delta.
"""
from __future__ import annotations
import argparse
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
from zoneinfo import ZoneInfo
import numpy as np
import sympy as s
from sympy.physics.wigner import clebsch_gordan, wigner_6j
from day16_alignment_transfer_sign import cg


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def states(J):
    return [-J+i for i in range(int(2*J)+1)]


def Bvector(J,k):
    return s.Matrix([s.simplify(s.sqrt(2*J+1)*(-1)**(J-m)*
        clebsch_gordan(J,J,k,m,-m,0)) for m in states(J)])


def transition(Ji,Jf,j):
    T=s.zeros(int(2*Jf)+1,int(2*Ji)+1)
    for a,m in enumerate(states(Jf)):
        for b,M in enumerate(states(Ji)):
            if abs(M-m)<=j:T[a,b]=cg(Jf,j,Ji,m,M-m,M)**2
    assert all(s.simplify(sum(T[:,k])-1)==0 for k in range(T.cols))
    assert all(x>=0 for x in T)
    assert all(s.simplify(x-1/s.Integer(T.rows))==0 for x in T*s.ones(T.cols,1)/T.cols)
    return T


def U(Ji,Jf,j,k):
    return s.simplify((-1)**(Ji+Jf+j+k)*s.sqrt((2*Ji+1)*(2*Jf+1))*
        wigner_6j(Ji,Ji,k,Jf,Jf,j))


def all_gaussian_moment_roots(J,p,k):
    assert J==int(J) # r**m^2 is a polynomial for this source's final J=5.
    ms=states(J);B=Bvector(J,k);b0=B[ms.index(s.Integer(0))]
    target=s.simplify((B.T*p)[0]/b0)
    r=s.symbols('r');poly=s.Poly(sum(s.simplify(B[i]/b0-target)*r**int(m*m)
        for i,m in enumerate(ms)),r,domain=s.QQ)
    count=int(poly.count_roots(0,1));intervals=poly.intervals(eps=s.Rational(1,10**20))
    roots=[]
    for (lo,hi),multiplicity in intervals:
        if lo>=0 and hi<=1:
            rr=(lo+hi)/2
            assert 0<rr<1
            sigma=s.sqrt(-1/(2*s.log(rr))).evalf(55)
            val=float(sigma);mm=np.array([float(m) for m in ms]);w=np.exp(-mm**2/(2*val**2));q=w/w.sum()
            actual=np.array([float(z) for z in p]);Bnp=np.array([float(z) for z in B])
            assert abs(Bnp@q-float((B.T*p)[0]))<1e-12
            roots.append({'r_interval':[str(lo),str(hi)],'multiplicity':multiplicity,
                'sigma':val,'B_target_exact':str(s.simplify((B.T*p)[0])),
                'total_variation_distance_to_exact_path':float(np.sum(abs(q-actual))/2),
                'gaussian_p_m':q.tolist()})
    assert sum(x['multiplicity'] for x in roots)==count
    return {'rank':k,'polynomial_in_r':str(poly.as_expr()),
        'r_definition':'exp(-1/(2sigma²)) with integer m, final J=5',
        'exact_physical_root_count_by_Sturm':count,'roots':roots,
        'not_an_experimental_width_fit_or_confidence_interval':True}


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--contract',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args();c=json.loads(a.contract.read_text());root=Path(__file__).resolve().parents[2]
    assert c['identity']=='C96-U-RANGE-AND-FIG1-REPLAY-01'
    assert sha(root/c['raw'])==c['raw_sha256']
    assert hashlib.sha256((root/c['source']).read_bytes()[:c['source_prefix_bytes']]).hexdigest()==c['source_prefix_sha256']
    base=json.loads((a.contract.parent/'alignment-transfer-result.json').read_text())
    assert sha(root/'system/scripts/day16_alignment_transfer_sign.py')==base['script_sha256']
    paths=[]
    for sequence in c['sequences']:
        Ji=s.Rational(sequence['initial_J2'],2);m0=s.Rational(sequence['initial_m']);p=s.zeros(int(2*Ji)+1,1);p[states(Ji).index(m0)]=1
        records=[]
        for step in sequence['steps']:
            Jf=s.Rational(step['Jf2'],2);j=s.Rational(step['j2'],2);T=transition(Ji,Jf,j);out=T*p;Uk={}
            for k in c['rank_parameters']:
                bi,bf=Bvector(Ji,k),Bvector(Jf,k);u=U(Ji,Jf,j,k)
                assert s.simplify(sum(bi.multiply_elementwise(bi))/(2*Ji+1)-1)==0
                assert s.simplify(sum(bf.multiply_elementwise(bf))/(2*Jf+1)-1)==0
                assert all(s.simplify(v)==0 for v in bf.T*T-u*bi.T)
                assert abs(u)<=1
                # Uniform parent/daughter marginals make U the correlation
                # of two unit-variance B_k functions, yielding |U|<=1.
                corr=s.simplify((bf.T*T*bi)[0]/(2*Ji+1))
                assert s.simplify(corr-u)==0
                assert s.simplify((bf.T*out)[0]-u*(bi.T*p)[0])==0
                Uk[str(k)]=str(u)
            records.append({'Ji':str(Ji),'Jf':str(Jf),'j':str(j),'signed_Uk':Uk,
                'B2_after_exact':str(s.simplify((Bvector(Jf,2).T*out)[0])),
                'B4_after_exact':str(s.simplify((Bvector(Jf,4).T*out)[0]))})
            p=out;Ji=Jf
        inversions=[all_gaussian_moment_roots(Ji,p,k) for k in [2,4]]
        paths.append({'name':sequence['name'],'steps':records,
            'final_J':str(Ji),'m_values':[str(m) for m in states(Ji)],
            'exact_final_p_m':[str(s.simplify(z)) for z in p],
            'exact_Bk':{str(k):str(s.simplify((Bvector(Ji,k).T*p)[0])) for k in c['rank_parameters']},
            'gaussian_moment_inversions':inversions,
            'source_author_model_not_experimental_population':True})
    exceptions=[]
    for Ji,Jf,j,k in [(s.Integer(1),s.Integer(1),s.Integer(1),2),
                      (s.Integer(2),s.Integer(2),s.Integer(2),2),
                      (s.Rational(23,2),s.Rational(23,2),s.Integer(11),2),
                      (s.Rational(5,2),s.Rational(5,2),s.Integer(2),4)]:
        u=U(Ji,Jf,j,k);assert u<0
        exceptions.append({'Ji':str(Ji),'Jf':str(Jf),'j':str(j),'rank':k,
            'Eq6_exact_U':str(u),'literal_0to1_not_general_identity':True})
    # Signed flow example drawn from the J5 dipole tail in the source figure.
    start=s.simplify(Bvector(s.Integer(5),2)[5]);u=U(s.Integer(5),s.Integer(5),s.Integer(1),2)
    assert start<0 and 0<u<1 and u*start>start and abs(u*start)<abs(start)
    output={'at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),
        'script_sha256':sha(Path(__file__)),'contract_sha256':sha(a.contract),
        'original_pdf_and_old_human_prefix_unchanged':True,'Eq6_signed_counterexamples':exceptions,
        'source_Fig1_paths':paths,'signed_flow_vs_magnitude':{'unit_feeding_normalization_only':True,
            'B2_in':str(start),'U2':str(u),'B2_out':str(s.simplify(u*start)),
            'signed_out_greater_than_signed_in':True,'magnitude_out_smaller_than_magnitude_in':True},
        'CauchySchwarz_absU_bound_verified':True,
        'scope':{'not_AvalancheII_producer_or_112Cd_data_replay':True,
            'not_a_new_delta_or_experimental_sigma':True,
            'original_source_literal_positive_range_preserved_as_source_statement':True,
            'physical_subset_or_code_paths_not_proven_wrong':True,
            'higher_rank_transfer_does_not_follow_from_rank2_sign_theorem':True}}
    a.output.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'counterexamples':exceptions,'path_summaries':[{'name':p['name'],'p_m':p['exact_final_p_m'],
        'B2':p['exact_Bk']['2'],'B4':p['exact_Bk']['4'],
        'Gaussian_sigma_roots':[[z['sigma'] for z in q['roots']] for q in p['gaussian_moment_inversions']]} for p in paths],
        'signedflow':output['signed_flow_vs_magnitude']},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
