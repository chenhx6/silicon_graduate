#!/usr/bin/env python3
"""Conditional magnitude-box sensitivity of the Cm245 common-parent ratio."""
from datetime import datetime, timezone
from functools import lru_cache
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp
from sympy.physics.wigner import clebsch_gordan as cg, racah

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'
D=sp.Symbol('d',real=True)


@lru_cache(None)
def radiation(jf2,ell,other,k):
    ji,jf=sp.Rational(9,2),sp.Rational(jf2,2)
    if not abs(ell-other)<=k<=ell+other:
        return sp.S.Zero
    return sp.simplify((-1)**(1+ji-jf+other-ell-k)
      *sp.sqrt((2*ji+1)*(2*ell+1)*(2*other+1))*cg(ell,other,k,1,-1,0)*racah(ji,ji,ell,other,k,jf))


def extrema(expr,low,high):
    numerator=sp.fraction(sp.cancel(sp.diff(expr,D)))[0]
    roots=sp.solve(numerator,D)
    points=[low,high]+[x for x in roots if x.is_real and bool(low<x<high)]
    values=[sp.simplify(expr.subs(D,x)) for x in points]
    return min(values),max(values),list(map(str,points))


def main():
    path=RUN/'cm245-mixing-companion-contract.json';c=json.loads(path.read_text());branches=[]
    for branch in c['branches']:
        jf2=branch['Jf2']
        rr=sp.factor((radiation(jf2,1,1,2)+2*D*radiation(jf2,1,2,2)+D**2*radiation(jf2,2,2,2))/(1+D**2))
        r4=sp.factor(D**2*radiation(jf2,2,2,4)/(1+D**2))
        lo,hi=map(sp.Rational,branch['delta_abs_marginal_interval']);intervals=[]
        for sign in [-1,1]:
            low,high=(-hi,-lo) if sign<0 else (lo,hi)
            a,b,pts=extrema(rr,low,high)
            assert (b<0 if branch['label']=='333' else a>0)
            intervals.append({'sign':sign,'delta_box':[str(low),str(high)],
                              'rank2_range_exact':[str(a),str(b)],'rank2_range_float':[float(a),float(b)],
                              'extremum_points_exact':pts,'private_bounds':(a,b)})
        branches.append({'label':branch['label'],'rank2_formula':str(rr),'rank4_formula':str(r4),'intervals':intervals})
    boxes=[]
    for multiple in [0,1,2]:
        raw=[]
        for branch in c['branches']:
            center,sigma=map(sp.Rational,[branch['a2_central'],branch['a2_sigma']])
            raw.append([center-multiple*sigma,center+multiple*sigma])
        vals=[x/y for x,y in itertools.product(*raw)]
        boxes.append({'multiple_marginals_not_CI':multiple,'ratio_range_exact':[str(min(vals)),str(max(vals))],
                      'private_bounds':(min(vals),max(vals))})
    comparisons=[]
    for first,second in itertools.product(branches[0]['intervals'],branches[1]['intervals']):
        values=[a/b for a,b in itertools.product(first['private_bounds'],second['private_bounds'])]
        low,high=min(values),max(values)
        intersections=[]
        for target in boxes:
            tl,th=target['private_bounds'];exists=bool(max(tl,low)<=min(th,high))
            intersections.append({'a2_box_multiple':target['multiple_marginals_not_CI'],'intersection':exists})
        comparisons.append({'delta333_sign':first['sign'],'delta388_sign':second['sign'],
                            'ratio_range_exact':[str(low),str(high)],'ratio_range_float':[float(low),float(high)],
                            'summary_box_checks':intersections})
    for branch in branches:
        for interval in branch['intervals']:
            del interval['private_bounds']
    for target in boxes:
        del target['private_bounds']
    no_witness=not any(t['intersection'] for row in comparisons for t in row['summary_box_checks'])
    result={'at':datetime.now(timezone.utc).isoformat(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'contract_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'branch_response_formulas_and_exact_extrema':branches,'a2_summary_ratio_boxes':boxes,
        'four_sign_magnitude_box_comparisons':comparisons,
        'no_matching_witness_in_declared_boxes':no_witness,
        'exact_stationary_and_endpoint_extrema_checked':True,
        'no_primary_phase_assignment_or_experimental_rejection':True,
        'no_posthoc_box_expansion_or_Q_recalibration':True,'ok':True}
    (RUN/'cm245-mixing-companion-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'ratio_ranges':[x['ratio_range_float'] for x in comparisons],
                      'all_declared_sign_boxes_no_witness':no_witness,'a2boxes':boxes},indent=2))


if __name__=='__main__':
    main()
