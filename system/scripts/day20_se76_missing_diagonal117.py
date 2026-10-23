#!/usr/bin/env python3
"""Conditional first-three-2+ TableII sensitivity, not a GOSIA reanalysis.

Only literal central signed RMEs. Unmeasured d33 stays a free symbolic argument;
all higher 2+ states are outside this declared finite projection. No fit CI.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from day19_evidence_repair_audit import signed_cg


def component_contractions(a, d):
    states = [(0,0,0)]+[(n,2,m) for n in range(1,4) for m in range(-2,3)]
    reduced = np.zeros((4,4))
    reduced[0,1:] = reduced[1:,0] = a
    reduced[1:,1:] = d
    ts = {}
    for mu in range(-2,3):
        t = np.zeros((16,16))
        for f,(nf,jf,mf) in enumerate(states):
            for i,(ni,ji,mi) in enumerate(states):
                t[f,i] = signed_cg(ji,2,jf,mi,mu,mf)*reduced[nf,ni]/math.sqrt(2*jf+1)
        ts[mu] = t
    q2 = sum((-1.)**mu*(t@ts[-mu])[0,0] for mu,t in ts.items())
    scalar = 0.
    for mu in range(-2,3):
        for nu in range(-2,3):
            k = mu+nu
            if abs(k) <= 2:
                scalar += signed_cg(2,2,2,mu,nu,k)*signed_cg(2,2,0,k,-k,0)*(ts[mu]@ts[nu]@ts[-k])[0,0]
    q3 = -math.sqrt(35/2)*scalar
    hermitian_error = max(np.max(abs(t.T-(-1.)**mu*ts[-mu])) for mu,t in ts.items())
    return float(q2),float(q3),float(hermitian_error)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--inputs',type=Path,required=True)
    p.add_argument('--source-pdf',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    args = p.parse_args()
    if args.output.exists():raise SystemExit('Refusing overwrite')
    inputs = json.loads(args.inputs.read_text())
    pdfhash = hashlib.sha256(args.source_pdf.read_bytes()).hexdigest()
    assert pdfhash == inputs['source_pdf_sha256']
    assert inputs['D_2plus'][2][2] is None
    d = [[F(x) if x is not None else F(0) for x in row] for row in inputs['D_2plus']]
    assert all(d[i][j]==d[j][i] for i in range(3) for j in range(3))
    checks,rows = [],{}
    def check(name,error,tol=3e-13):
        checks.append({'name':name,'absolute_error':float(error),'tolerance':tol})
        if abs(error)>tol:raise AssertionError(name)
    for label in ['a0_1','a0_2']:
        a = [F(x) for x in inputs[label]]
        q2 = sum(x*x for x in a)
        quadratic = sum(a[i]*d[i][j]*a[j] for i in range(3) for j in range(3))
        coeff = a[2]**2
        q3intercept = -math.sqrt(7/10)*float(quadratic)
        q3slope = -math.sqrt(7/10)*float(coeff)
        dn = np.array(d,dtype=float);an = np.array(a,dtype=float)
        c2,c3,he = component_contractions(an,dn)
        check(label+' spherical Hermiticity',he)
        check(label+' q2 tensor versus RME sum',c2-float(q2))
        check(label+' q3 tensor versus quadratic',c3-q3intercept)
        # d33=1 here is a polynomial evaluation point, not an assumed physical value.
        d1=dn.copy();d1[2,2]=1.
        _,q31,_ = component_contractions(an,d1)
        check(label+' free-d33 affine coefficient',q31-c3-q3slope)
        phase=np.diag([1.,-1.,1.])
        pc2,pc3,_=component_contractions(phase@an,phase@dn@phase)
        check(label+' whole-multiplet rephase invariance',max(abs(pc2-c2),abs(pc3-c3)))
        rows[label]={'q2_eb2':float(q2),'q2_exact':str(q2),
                     'a3_squared_eb2':str(coeff),
                     'q3_intercept_at_d33zero_eb3':q3intercept,
                     'q3_derivative_per_d33_eb2':q3slope,
                     'R_intercept_at_d33zero':q3intercept/float(q2)**1.5,
                     'R_derivative_per_d33_inverse_eb':q3slope/float(q2)**1.5,
                     'meaning':'conditional three-state affine expression; intercept is not adopted true value'}
    raw_ratio=F(inputs['a0_2'][2])**2/F(inputs['a0_1'][2])**2
    check('literal squared-coupling ratio exact',float(raw_ratio-F(17689,100)),0.)
    # Source B-up/down direction changes initial spin denominator; do not expand
    # rounding residual to claim actual extraction closure.
    rme=F(inputs['a0_1'][0]);bup=rme*rme*10000;bdown=bup/5
    result={'checkpoint':'117','kind':'literal-source conditional unknown-diagonal sensitivity',
            'source':'HE19-D20-3/4, PDF6/printed5TableII, integerI0 Eq2/3',
            'q3_formula':'-sqrt(7/10) * a.T D a; D33 remains free',
            'rows':rows,'raw_cubic_sensitivity_ratio':str(raw_ratio),
            'normalized_R_sensitivity_ratio':rows['a0_2']['R_derivative_per_d33_inverse_eb']/rows['a0_1']['R_derivative_per_d33_inverse_eb'],
            'direction_contract':{'Bup_from_printed_rme_e2fm4':float(bup),
                                  'Bdown_from_same_rme_e2fm4':float(bdown),
                                  'printed_Bup':4190,'printed_Bdown':838,
                                  'literal_rounding_residuals':[float(bup-4190),float(bdown-838)],
                                  'not_scientific_validation':'No errors or actual producer reconstructed; printed values retained'},
            'controls_executed':len(checks),'checks':checks,'scientific_certification':False,
            'boundaries':['No numerical bound/prior imposed on missing d33',
                          'Small coefficient is not a universal negligible-error guarantee without d33 bound',
                          'No propagation of marginal errors, no actual Cov/fitCI',
                          'No high2+ strength closure, no Fig6 fit reproduced',
                          'Matrix tensor projected model is not microscopic CI producer'],
            'input_sha256':hashlib.sha256(args.inputs.read_bytes()).hexdigest(),
            'source_pdf_sha256':pdfhash,
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'controls':len(checks),'rows':rows,'raw_ratio':str(raw_ratio),
                      'R_sensitivity_ratio':result['normalized_R_sensitivity_ratio'],
                      'scientific_certification':False}))


if __name__=='__main__':main()
