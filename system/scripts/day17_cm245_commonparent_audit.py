#!/usr/bin/env python3
"""Necessary pure-E1 common-parent AD relation; marginal errors, not a CI."""
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path

import sympy as sp
from sympy.physics.wigner import clebsch_gordan as cg, racah

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def main():
    path=RUN/'cm245-commonparent-contract.json';c=json.loads(path.read_text());ji=sp.Rational(c['source_Ji2'],2)
    rr=[]
    for branch in c['branches']:
        jf=sp.Rational(branch['Jf2'],2)
        val=sp.simplify((-1)**(1+ji-jf-2)*sp.sqrt((2*ji+1)*9)*cg(1,1,2,1,-1,0)*racah(ji,ji,1,1,2,jf))
        rr.append(val)
    ratio=sp.simplify(rr[0]/rr[1]);assert ratio==sp.Rational(-16,11)
    a,sa=c['branches'][0]['a2'];b,sb=c['branches'][1]['a2'];r=float(ratio)
    residual=a-r*b;terms=[sa,abs(r)*sb]
    sigma=math.hypot(*terms);smin,smax=abs(terms[0]-terms[1]),sum(terms)
    boxes=[]
    for multiplier in [1,2]:
        first=[sp.Rational(str(a))-multiplier*sp.Rational(str(sa)),sp.Rational(str(a))+multiplier*sp.Rational(str(sa))]
        second=[sp.Rational(str(b))-multiplier*sp.Rational(str(sb)),sp.Rational(str(b))+multiplier*sp.Rational(str(sb))]
        required=sorted(ratio*x for x in second)
        low,high=max(first[0],required[0]),min(first[1],required[1]);feasible=bool(low<=high)
        boxes.append({'sigma_multiple_marginal_not_jointCI':multiplier,'intersection_exists':feasible,
                      'a333_intersection':list(map(str,[low,high])) if feasible else None})
    assert not boxes[0]['intersection_exists'] and boxes[1]['intersection_exists']
    weights=[]
    for m2 in range(1,c['source_Ji2']+1,2):
        m=sp.Rational(m2,2)
        b2=sp.simplify((-1)**(ji-m)*sp.sqrt(2*ji+1)*cg(ji,ji,2,m,-m,0))
        weights.append({'folded_abs_m':str(m),'B2':str(b2),'a2_333':str(sp.simplify(b2*rr[0])),
                        'a2_388':str(sp.simplify(b2*rr[1]))})
    result={'at':datetime.now(timezone.utc).isoformat(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'contract_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'pureE1_rank2_coefficients':list(map(str,rr)),'a333_over_a388_exact':str(ratio),
        'rank2_folded_vertex_controls':weights,
        'printed_a2_summary':{'a333':a,'a388':b,'necessary_relation_residual':residual,
           'conditional_sigma_residual_if_independent':sigma,
           'local_sigma_residual_range_unknown_correlation':[smin,smax],
           'absolute_standardized_residual_if_independent':abs(residual)/sigma,
           'no_covariance_hypothesis_test_claimed':True},
        'marginal_boxes':boxes,'exact_rank_and_box_controls':True,
        'same_parent_necessary_relation_not_unconditional_Q_rejection':True,
        'no_actual_P_Q_delta_CI_or_mixing_sign_inferred':True,'ok':True}
    (RUN/'cm245-commonparent-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'ratio':str(ratio),'summary':result['printed_a2_summary'],'boxes':boxes},indent=2))


if __name__=='__main__':
    main()
