#!/usr/bin/env python3
"""Exact EW69/TW70 intensity-ratio versus bounded-degree convention bridge."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def main():
    a2,a4=sp.symbols('a2 a4',real=True)
    d=1-a2/2+sp.Rational(3,8)*a4
    n=sp.Rational(3,2)*a2+sp.Rational(5,8)*a4
    degree=n/d
    ratio=(1+a2+a4)/(1-2*a2-a4/4)
    assert sp.factor(ratio-(1+degree)/(1-degree))==0
    assert sp.factor((ratio-1)/(ratio+1)-degree)==0
    assert sp.factor((1+a2+a4)/d-(1+degree))==0
    source=RUN/'ewan1969-calibration-contract.json'
    data=json.loads(source.read_text())
    rows=[]
    for eg,a,s2,b,s4,q,sq in data['Ru_rows'][:3]:
        rp=float(ratio.subs({a2:a,a4:b}))
        pp=float(degree.subs({a2:a,a4:b}))
        inverted=(rp-1)/(rp+1)
        assert abs(pp-inverted)<1e-14
        rows.append({'Egamma_MeV':eg,'EW69_literal_expression':rp,
                     'mapped_bounded_degree':inverted,'TW70_pureE2_degree':pp})
    result={'at':datetime.now(timezone.utc).isoformat(),
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
            'exact_symbolic_bridge':'r_EW=(1+p)/(1-p); p=(r_EW-1)/(r_EW+1)',
            'AD_zero_over_90_bridge':'W(0)/W(90)=1+p for the same normalized pure-E2 point coefficients',
            'domain':'D=W90 nonzero; ratio poles handled as limits; pure E2 axisymmetric full final-state trace',
            'rows':rows,
            'endpoints':{'p0_r':1,'p_plus1_r':'positive infinity','p_minus1_r':0},
            'prior_literal_formula_failure_interpretation_withdrawn':True,
            'source_author_intent_not_proven_from_algebra':True,
            'no_official_erratum_or_new_experimental_P_Q_CI':True,'ok':True}
    (RUN/'polarization-ratio-degree-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
