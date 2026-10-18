#!/usr/bin/env python3
"""Uncredited Day17 preview within Day16: SG98's actual table and covariance.

Raw peak areas are fitted summaries, not independent Poisson events. Printed
rounding compatibility is diagnostic and is not a confidence or data-error claim.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np


def asymmetry(c: float,s: float,eta: float) -> float:
    if min(c,s,eta)<=0:raise ValueError('Positive confined/shared yields and eta required')
    return (eta*c-s)/(math.sqrt(eta)*(c+s))


def gradients(c: float,s: float,eta: float) -> np.ndarray:
    n=c+s;se=math.sqrt(eta)
    return np.array([(eta+1)*s/(se*n*n),-(eta+1)*c/(se*n*n),
                     (eta*c+s)/(2*eta**1.5*n)])


def main() -> int:
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True);a=p.parse_args();cfg=json.loads(a.input.read_text())
    assert cfg['identity']=='DAY16-UNCredited-D17-SG98-TABLE3-01'
    rows=[];derivative_errors=[]
    for row in cfg['Table3']:
        c,sc=row['C'];s,ss=row['S'];eta,se=row['eta'];central=asymmetry(c,s,eta);g=gradients(c,s,eta)
        for i,x in enumerate([c,s,eta]):
            step=abs(x)*1e-5;v=np.array([c,s,eta],float);v[i]+=step
            plus=asymmetry(*v);v[i]-=2*step;minus=asymmetry(*v)
            derivative_errors.append(abs((plus-minus)/(2*step)-g[i]))
        # These are sensitivity diagnostics, not the actual (unknown) full Sigma.
        peak_only=math.hypot(g[0]*sc,g[1]*ss)
        poisson=math.sqrt(g[0]**2*c+g[1]**2*s)
        formula17=math.sqrt(c*s*(eta+1)**2/(eta*(c+s)**3))
        assert abs(poisson-formula17)<1e-14
        eta_scale=abs(g[2]*se)
        boxes=[]
        for signs in itertools.product([-1,1],repeat=3):
            boxes.append(asymmetry(c+signs[0]*.5,s+signs[1]*.5,eta+signs[2]*.0005))
        lo,hi=min(boxes),max(boxes);pr=row['A_printed'][0]
        matches=max(lo,pr-.0005)<=min(hi,pr+.0005)
        # Per-energy eta matching can be an independent systematic condition.
        eta_needed=((-pr*(c+s)+math.sqrt(pr**2*(c+s)**2+4*c*s))/(2*s))**-2
        # Solve C t^2 - A N t - S=0 for t=sqrt(eta), independently.
        t=(pr*(c+s)+math.sqrt(pr**2*(c+s)**2+4*c*s))/(2*c)
        assert abs(eta_needed-t*t)<1e-13
        rows.append({**row,'A_recomputed':central,'A_minus_printed':central-pr,
                     'derivatives_C_S_eta':g.tolist(),
                     'quoted_peak_error_independent_C_S_diagnostic':peak_only,
                     'eta_quoted_error_sensitivity':eta_scale,
                     'peak_plus_eta_independent_diagnostic':math.hypot(peak_only,eta_scale),
                     'Poisson_area_diagnostic':poisson,
                     'quoted_fit_error_over_sqrtarea':{'C':sc/math.sqrt(c),'S':ss/math.sqrt(s)},
                     'printing_box_A_image':[lo,hi],
                     'printing_boxes_overlap':matches,
                     'eta_needed_for_exact_printed_A':t*t,
                     'eta_needed_is_not_independent_calibration':True,
                     'source_A_over_P_implied_Q_not_new_calibration':pr/row['P_printed'][0]})
    assert max(derivative_errors)<1e-7
    calibrations=[]
    for row in cfg['Table1']:
        pa,pe=row['P'];aa,ae=row['A'];q,qe=row['Q']
        assert pa>0
        # A/P is an identity; rounded central differences are not independent Q data.
        calibrations.append({**row,'central_A_over_P':aa/pa,
                             'local_Q_error_if_A_P_independent':math.hypot(ae/pa,aa*pe/pa**2),
                             'not_independent_measurements':True})
    # Exact conditional binomial identity for a declared model, no toy counts.
    # A=((eta+1)pC-1)/sqrteta. Var(A|n)=
    # [1+(eta-1)A/sqrteta-A^2]/n, reducing to 1/n near A=0.
    identity_errors=[]
    for eta,physa in [(.105,0.),(.163,.041),(.13,-.007)]:
        pc=(1+math.sqrt(eta)*physa)/(1+eta);assert 0<pc<1
        lhs=(eta+1)**2/eta*pc*(1-pc)
        rhs=1+(eta-1)/math.sqrt(eta)*physa-physa**2
        identity_errors.append(abs(lhs-rhs))
    assert max(identity_errors)<1e-13
    result={'identity':cfg['identity'],'input_sha256':hashlib.sha256(a.input.read_bytes()).hexdigest(),
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'table3_replay':rows,'table1_identity_checks':calibrations,
            'printing_closure_failures_keV':[r['E_keV'] for r in rows if not r['printing_boxes_overlap']],
            'derivative_max_absolute_error':max(derivative_errors),
            'binomial_identity_max_error':max(identity_errors),
            'full_covariance_relation':'P=A(C,S,eta)/Q; VarP=gP^T Sigma(C,S,eta,Q) gP. In particular keep C-S covariance and A-Q covariance from common calibration.',
            'error_origin_boundary':'Source Table3 errors derive from peak-fit parameters; adding eta and Q as independent terms is only a diagnostic, not reconstruction of the reported full error budget.',
            'all_internal_checks_passed':True,'all_printed_rows_reproduced':all(r['printing_boxes_overlap'] for r in rows),
            'day_index':16,'uncredited_preview_day':17,'formal_Day17_credit':False}
    a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'output':str(a.output),'printing_closure_failures_keV':result['printing_closure_failures_keV'],
                      'rows':[{k:r[k] for k in ['E_keV','A_recomputed','A_minus_printed','quoted_peak_error_independent_C_S_diagnostic','eta_quoted_error_sensitivity','Poisson_area_diagnostic','printing_boxes_overlap','eta_needed_for_exact_printed_A']} for r in rows],
                      'internal_checks_passed':True,'all_printed_rows_reproduced':result['all_printed_rows_reproduced']},ensure_ascii=False));return 0


if __name__=='__main__':raise SystemExit(main())
