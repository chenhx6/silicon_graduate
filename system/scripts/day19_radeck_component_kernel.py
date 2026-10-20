#!/usr/bin/env python3
"""Conditional Radeck component average; does not reproduce the experimental fit."""
import argparse
import hashlib
import json
import math
from pathlib import Path


def shifted(a,g,tau,t):
    if t==0:
        return 1.0
    return a+(1-a)*(-math.expm1(-(g+1/tau)*t))/((1+g*tau)*(-math.expm1(-t/tau)))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--contract',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    q=p.parse_args();d=json.loads(q.contract.read_text())
    sha=hashlib.sha256(Path(d['raw_file']).read_bytes()).hexdigest()
    if sha!=d['raw_sha256']:raise ValueError('raw hash differs')
    tau=d['tau_ps'];v=d['velocity_um_per_ps'];rows=[]
    for k,ak,gk in d['parameters']:
        for t in [0,.25,1,5,10,20,100]:
            us=ak+(1-ak)*math.exp(-gk*t);sh=shifted(ak,gk,tau,t)
            rows.append({'rank':k,'physical_time_ps':t,'unshifted_G':us,'shifted_conditional_G':sh,'SH_minus_US':sh-us})
        for r in [x for x in rows if x['rank']==k]:
            if not (ak-1e-14<=r['unshifted_G']<=r['shifted_conditional_G']+1e-14<=1+1e-13):
                raise ValueError('monotone component average failed')
    # Literal d-d0 convention only; this cannot decide authors actual coordinate producer.
    t_literal=(3-d['printed_d0_um'])/v
    p_literal=-math.expm1(-t_literal/tau)
    result={'scope':d['scope'],'contract_sha256':hashlib.sha256(q.contract.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'raw_sha256':sha,'conditional_formula':'SH=alpha+(1-alpha)*(1-exp(-(Gamma+1/tau)t))/((1+Gamma*tau)*(1-exp(-t/tau))); t>=0 and frozenalignment in stopper',
        'rows':rows,'source_parameter_asymptotes':[{'rank':k,'G_US_infinity':a,'G_SH_infinity':a+(1-a)/(1+g*tau),'C_from_g047_ps':.47/g,'C_from_g041_ps':.41/g} for k,a,g in d['parameters']],
        'literal_printing_control':{'d_um':3,'printed_positive_d0_um':d['printed_d0_um'],'P_from_literal_Eq9_at_a1':p_literal,'not_actual_job_or_erratum':True},
        'zero_absolute_time_d3_control':{'time_ps':3/v,'G2_US':d['parameters'][0][1]+(1-d['parameters'][0][1])*math.exp(-d['parameters'][0][2]*3/v),'not_actual_shortest_distance_alignment_or_efficiency_bias':True},
        'actual_Acoul_or_fitCov_recovered':False,'no_new_tau_or_g_or_CI':True}
    q.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['source_parameter_asymptotes','literal_printing_control','zero_absolute_time_d3_control']},ensure_ascii=False))


if __name__=='__main__':main()
