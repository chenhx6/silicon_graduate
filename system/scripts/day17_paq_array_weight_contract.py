#!/usr/bin/env python3
"""Exact conditional response algebra for pooling polarimeters; no experiment fit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

import sympy as s

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rat(value):
    return s.Rational(value)


def encoded(value):
    value = s.factor(value)
    return {"exact": str(value), "decimal": float(value)}


def main():
    inp = RUN / "array-weight-input.json"
    config = json.loads(inp.read_text())
    checks = []

    def check(name, difference):
        difference = s.factor(difference)
        checks.append({"name": name, "passed": difference == 0, "exact_residual": str(difference)})

    p, w, a1, a2, q1, q2 = s.symbols("P w a1 a2 q1 q2", real=True)
    abar = w*a1 + (1-w)*a2
    qbar = w*q1 + (1-w)*q2
    aqbar = w*a1*q1 + (1-w)*a2*q2
    cov = aqbar - abar*qbar
    k = qbar + cov/(2*abar)
    lam = -cov/(2*abar)
    raw_perp = w*(1+q1*p)+(1-w)*(1+q2*p)
    raw_parallel = w*a1*(1-q1*p)+(1-w)*a2*(1-q2*p)
    raw_A = (abar*raw_perp-raw_parallel)/(abar*raw_perp+raw_parallel)
    response_A = k*p/(1+lam*p)
    check("clover direct summed counts equal Mobius response", raw_A-response_A)
    check("common a restores linear response", (raw_A-qbar*p).subs(a2,a1))
    check("common Q restores linear response", (raw_A-q1*p).subs(q2,q1))
    check("matched pooled null zero does not certify linear response", raw_A.subs(p,0))
    pr = s.symbols("Pr", real=True)
    calibrated = pr * response_A / response_A.subs(p,pr)
    check("clover one-reference bias exact", calibrated-p*(1+lam*pr)/(1+lam*p))

    c0u, c0t, dt, eta_u = s.symbols("c0u c0t dt etaU", positive=True)
    eta_from_u = (1-c0u)/c0u
    pooled_SG = ((1+eta_u)*(c0t+dt*p)-1)/s.sqrt(eta_u)
    intercept = ((1+eta_u)*c0t-1)/s.sqrt(eta_u)
    slope = (1+eta_u)*dt/s.sqrt(eta_u)
    check("SG98 direct sum gives affine response", pooled_SG-intercept-slope*p)
    check("SG98 matched unpolarized fraction gives zero offset", intercept.subs({eta_u:eta_from_u,c0t:c0u}))

    results = {}
    probes = list(map(rat,config["physical_polarization_probe_points"]))
    for kind in ("clover","sg98"):
        data=config[kind]; wr=list(map(rat,data["reference_weights"])); wt=list(map(rat,data["target_weights"])); qs=list(map(rat,data["Q"])); pref=rat(data["reference_P"]);pt=rat(data["target_P"])
        check(kind+" reference weights normalized",sum(wr)-1);check(kind+" target weights normalized",sum(wt)-1)
        if kind=="clover":
            aa=list(map(rat,data["a"])); hu=sum(ww*av for ww,av in zip(wr,aa))
            def yields(weights,P):
                return [(weights[j]*(1+qs[j]*P),weights[j]*aa[j]*(1-qs[j]*P)) for j in range(2)]
            def pooled(weights,P):
                ys=yields(weights,P);x=sum(z[0] for z in ys);y=sum(z[1] for z in ys);return (hu*x-y)/(hu*x+y)
            cv=sum(wr[j]*aa[j]*qs[j] for j in range(2))-hu*sum(wr[j]*qs[j] for j in range(2))
            local_k=sum(wr[j]*qs[j] for j in range(2))+cv/(2*hu);local_lam=-cv/(2*hu)
            results[kind]={"pooled_null_geometry":encoded(hu),"cov_a_Q_perpendicular_basis":encoded(cv),"matching_response_k":encoded(local_k),"matching_response_lambda":encoded(local_lam)}
        else:
            etas=list(map(rat,data["eta"])); c0=sum(wr[j]/(1+etas[j]) for j in range(2));hu=(1-c0)/c0
            def yields(weights,P):
                return [(weights[j]*(1+s.sqrt(etas[j])*qs[j]*P)/(1+etas[j]), weights[j]*(etas[j]-s.sqrt(etas[j])*qs[j]*P)/(1+etas[j])) for j in range(2)]
            def pooled(weights,P):
                ys=yields(weights,P);C=sum(z[0] for z in ys);S=sum(z[1] for z in ys);return (hu*C-S)/(s.sqrt(hu)*(C+S))
            qeff=s.diff(pooled(wr,p),p)
            results[kind]={"pooled_null_geometry":encoded(hu),"arithmetic_eta_not_the_same":encoded(sum(wr[j]*etas[j] for j in range(2))),"matching_response_Qeff":encoded(qeff)}
        ar=pooled(wr,pref);qcal=ar/pref
        results[kind].update({"reference_A":encoded(ar),"one_reference_Q":encoded(qcal),"matched_target_P_estimate":encoded(pooled(wr,pt)/qcal),"mismatched_target_P_estimate":encoded(pooled(wt,pt)/qcal),"mismatched_unpolarized_A":encoded(pooled(wt,s.Integer(0))),"mismatched_unpolarized_apparent_P":encoded(pooled(wt,s.Integer(0))/qcal)})
        rows=[]
        for P in probes:
            ys=yields(wt,P)
            assert all(z>=0 for pair in ys for z in pair)
            perA=[]
            for j,(first,second) in enumerate(ys):
                if kind=="clover":v=(aa[j]*first-second)/(aa[j]*first+second)
                else:v=(etas[j]*first-second)/(s.sqrt(etas[j])*(first+second))
                check(kind+" perdetector correction at P="+str(P)+" detector="+str(j),v-qs[j]*P);perA.append(v)
            recovered=sum(wt[j]*perA[j] for j in range(2))/sum(wt[j]*qs[j] for j in range(2))
            check(kind+" explicit perdetector matched estimator recovers P="+str(P),recovered-P)
            rows.append({"P":encoded(P),"pooled_A":encoded(pooled(wt,P)),"one_reference_apparent_P":encoded(pooled(wt,P)/qcal),"perdetector_P":encoded(recovered)})
        results[kind]["probe_rows"]=rows

    bounds={k:rat(v) for k,v in config["conditional_ST99_bounds"].items() if k!="note"}
    beta=(bounds['a_max']-bounds['a_min'])*(bounds['Q_max']-bounds['Q_min'])/(8*bounds['pooled_a_min'])
    worst_bias=2*beta/(1-beta)
    null_positive=(bounds['pooled_a_max']-bounds['a_min'])/(bounds['pooled_a_max']+bounds['a_min'])
    null_negative=(bounds['pooled_a_min']-bounds['a_max'])/(bounds['pooled_a_min']+bounds['a_max'])
    provenance=[]
    for src in config['sources']:
        text=(ROOT/src['path']).read_text();raw=ROOT/re.search(r'^raw_file: "(.+)"',text,re.M).group(1);assert sha(raw)==src['raw_sha256'];provenance.append({**src,'actual_hash_match':True})
    failed=[c['name'] for c in checks if not c['passed']]
    out={'run_id':config['run_id'],'input_kind':config['input_kind'],'generated_at':datetime.now(timezone.utc).isoformat(),'input_sha256':sha(inp),'script_sha256':sha(Path(__file__)),'sympy_version':s.__version__,'source_provenance':provenance,'symbolic_results':{'clover_response':str(response_A),'clover_cov':str(s.factor(cov)),'SG98_affine_response':str(pooled_SG)},'design_results':results,'conditional_ST99_bounds':{'lambda_abs_upper':encoded(beta),'matching_weights_single_reference_P_absolute_bias_upper':encoded(worst_bias),'mismatched_weights_null_A_positive_upper':encoded(null_positive),'mismatched_weights_null_A_negative_lower':encoded(null_negative),'not_experimental_error_budget':True},'checks':checks,'failed_checks':failed,'ok':not failed}
    (RUN/'array-weight-result.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'ok':out['ok'],'failed_checks':failed,'results':{kind:{k:v for k,v in value.items() if k!='probe_rows'} for kind,value in results.items()},'bounds':out['conditional_ST99_bounds']},ensure_ascii=False,indent=2))
    return 0 if out['ok'] else 1


if __name__=='__main__':
    raise SystemExit(main())
