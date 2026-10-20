#!/usr/bin/env python3
"""Literal L74 table replay and independent net-count variance derivation."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def merit(q,p,eff,s1,s2):
    a=q*p
    bracket=((1-a)*(1+2/s1)+(1+a)*(1+2/s2))
    return eff*q*q/((1-a*a)*bracket)


def main():
    path=RUN/'logan1974-table-contract.json'
    c=json.loads(path.read_text())
    conv=c['models']['conventional'];plan=c['models']['planar']
    base=merit(conv['Q'],1,conv['epsilon_arbitrary_units'],conv['S1'],conv['S2'])
    rows=[]
    for i,p in enumerate(c['P_values']):
        values={}
        for name,m in c['models'].items():
            value=merit(m['Q'],p,m['epsilon_arbitrary_units'],m['S1'],m['S2'])/base
            values[name]={'normalized_M':value,'printed_M':c['printed_Table2'][name][i],
                          'replayed_minus_printed':value-c['printed_Table2'][name][i]}
        rows.append({'P':p,'models':values})
    old_base=merit(conv['Q'],1,conv['epsilon_arbitrary_units'],13,13)
    old_ratio=merit(plan['Q'],1,plan['epsilon_arbitrary_units'],plan['S1'],plan['S2'])/old_base
    n1,n2,lam,a,s1,s2=sp.symbols('n1 n2 lambda a s1 s2',positive=True)
    asym=(n1-n2)/(n1+n2)
    gradient=[sp.diff(asym,n1),sp.diff(asym,n2)]
    var=gradient[0]**2*n1*(1+2/s1)+gradient[1]**2*n2*(1+2/s2)
    derived=sp.factor(var.subs({n1:lam*(1+a),n2:lam*(1-a)}))
    quoted=(1-a*a)/(4*lam)*((1-a)*(1+2/s1)+(1+a)*(1+2/s2))
    assert sp.simplify(derived-quoted)==0
    # Net-count noise depends on the estimator of the peak background.
    eta1,eta2=sp.symbols('eta1 eta2',nonnegative=True)
    generalized=gradient[0]**2*n1*(1+(1+eta1)/s1)+gradient[1]**2*n2*(1+(1+eta2)/s2)
    assert sp.simplify(generalized.subs({eta1:1,eta2:1})-var)==0
    result={'at':datetime.now(timezone.utc).isoformat(),
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'contract_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'Table1_S13_variant_planar_ratio_atP1':old_ratio,
            'actual_Table2_replays':rows,
            'backgroundfree_limit_source_M':'epsilon*Q^2/[2*(1-Q^2*P^2)]',
            'small_asymmetry_backgroundfree_limit_source_M':'epsilon*Q^2/2',
            'source_time_t_per_orientation':'t>x^2/(4*I*P^2*M); total elapsed=2*t',
            'generalized_background_estimator_variance':str(generalized),
            'VarN_Nplus2B_reproduces_original_Eq2_symbolically':True,
            'not_any_peakfit_background_is_independent_PoissonB':True,
            'old_OCR_S13_not_tuned_as_actual_input':True,
            'small_Table2_nonclosures_preserved':True,
            'no_absolute_efficiency_or_new_detector_ranking_CI':True,'ok':True}
    (RUN/'logan1974-table-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
