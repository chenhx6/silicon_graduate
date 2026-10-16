#!/usr/bin/env python3
"""Conditional rank4 same-parent reference check; no actual delta extraction."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar

from day16_se21_m3_reference import native_f, population, forms, direct, triangle
from day16_st99_table_replay import quoted


def exact_sixj_square(a: int,b: int,c: int,d: int,e: int,f: int) -> tuple:
    pref=triangle(a,b,c)*triangle(a,e,f)*triangle(d,b,f)*triangle(d,e,c)
    low=[(a+b+c)//2,(a+e+f)//2,(d+b+f)//2,(d+e+c)//2]
    high=[(a+b+d+e)//2,(a+c+d+f)//2,(b+c+e+f)//2]
    total=Fraction(0)
    for z in range(max(low),min(high)+1):
        den=math.prod(math.factorial(z-x) for x in low)*math.prod(math.factorial(x-z) for x in high)
        total+=Fraction((-1)**z*math.factorial(z+1),den)
    return pref*total*total,(-1 if total<0 else 1)


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args();cfg=json.loads(args.input.read_text());root=Path(__file__).resolve().parents[2]
    assert hashlib.sha256((root/cfg["source_raw"]).read_bytes()).hexdigest()==cfg["source_sha256"]
    ti=cfg["parent"]["twice_J"];tf=cfg["target"]["twice_Jf"];rf=cfg["reference"]["twice_Jf"]
    f_target=native_f(ti,tf,4,2,2);f_ref=native_f(ti,rf,4,2,2)
    assert native_f(ti,tf,4,1,1)==0 and native_f(ti,tf,4,1,2)==0
    ratio=f_target/f_ref;assert ratio<0
    st2,sign_t=exact_sixj_square(ti,ti,8,4,4,tf)
    sr2,sign_r=exact_sixj_square(ti,ti,8,4,4,rf)
    square_ratio=st2/sr2
    n,d=math.isqrt(square_ratio.numerator),math.isqrt(square_ratio.denominator)
    assert n*n==square_ratio.numerator and d*d==square_ratio.denominator
    exact_ratio=Fraction((-1)**((tf-rf)//2)*sign_t*sign_r*n,d)
    assert abs(float(exact_ratio)-ratio)<1e-14
    # Distinct fixed populations serve only to verify cancellation/forward algebra.
    errors=[]
    for width in (0.,.2,.4):
        pop=population(ti,width)
        target=forms(ti,tf,(("M",1),("E",2)),pop)
        ref=forms(ti,rf,(("E",2),),pop)
        for delta in (-2.,.5):
            v=np.array([1.,delta])/math.sqrt(1+delta*delta)
            a=float(v@target[4]@v)
            predicted=float(ref[4][0,0])*ratio*delta*delta/(1+delta*delta)
            errors.append(abs(a-predicted));assert abs(a-predicted)<1e-12
        projected,_=direct(ti,rf,(("E",2),),pop,np.array([1.]),12)
        errors.append(abs(projected[4]-ref[4][0,0]));assert errors[-1]<2e-12
    t,st=quoted(cfg["target"]["A4"]);r,sr=quoted(cfg["reference"]["A4"])
    bmax=-ratio*cfg["geometry"]["chosen_s4_for_nominalbounds"]
    def profile(b: float) -> tuple[float,float,float]:
        ref_true=(r/sr**2-b*t/st**2)/(1/sr**2+b*b/st**2)
        target_true=-b*ref_true
        score=(r-ref_true)**2/sr**2+(t-target_true)**2/st**2
        return score,ref_true,target_true
    fit=minimize_scalar(lambda x:profile(x)[0],bounds=(0,bmax),method="bounded",
                        options={"xatol":1e-13})
    assert fit.success
    candidates=[(b,profile(b)) for b in [0.,float(fit.x),bmax]]
    best=min(candidates,key=lambda x:x[1][0])
    intervals=[]
    for n in (1,2):
        rlo,rhi=r-n*sr,r+n*sr;tlo,thi=t-n*st,t+n*st
        # Image over all b in[0,bmax] and the independent reference interval.
        image=[0.,-bmax*rlo,-bmax*rhi]
        lo,hi=min(image),max(image)
        intervals.append({"nominal_error_multiplier":n,"reference_interval":[rlo,rhi],
                          "target_interval":[tlo,thi],"target_image_under_ratio":[lo,hi],
                          "overlap":max(lo,tlo)<=min(hi,thi),"not_joint_confidence":True})
    out={"identity":cfg["identity"],"input_sha256":hashlib.sha256(args.input.read_bytes()).hexdigest(),
         "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         "F4_target_pureE2":f_target,"F4_reference_pureE2":f_ref,
         "F4_ratio":ratio,"exact_ratio_fraction":str(exact_ratio),
         "exact_sixj_squared_ratio_certificate":str(square_ratio),
         "max_forward_cancellation_or_projection_error":max(errors),
         "necessary_relation":"A4target=ratio*s4*fE2*A4reference, fE2in[0,1]. Forpositivegeometryratio, nonzeroA4valuesmusthaveoppositesigns. Noactualdataerrorverdict.",
         "literal_interval_controls":intervals,
         "chosen_diagonal_profile":{"s4":1.,"b_range":[0,bmax],
              "minimum_diagnostic_score":best[1][0],"b_at_min":best[0],
              "reference_true_at_diagnostic_min":best[1][1],
              "target_true_at_diagnostic_min":best[1][2],
              "not_actual_delta_fit_or_formal_test":True},
         "boundary":"Necessary shared-density/pureE2-reference/coefficient-layer/positiveQratio model only. Actualgate/postselection, finiteacceptance, highermultipoles, originalproducer/correctionlayer andCov remain unknown. NoGaussianalignment requirement, actualdelta/CI ormodeclassification."}
    args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(out,ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
