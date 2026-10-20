#!/usr/bin/env python3
"""BA72 actual Ge table, shared numerator/denominator and partial error scope."""
import hashlib
import json
import math
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def main():
    path=RUN/'bass1972-Ge-contract.json';c=json.loads(path.read_text())
    pmap={r[0]:r for r in c['P_rows']}
    out=[];groups=defaultdict(list)
    for e,eth,n,sn,r,sr in c['Ge_rows']:
        pp=pmap[e];p,spol=pp[3:]
        f=n/100;response=r/100;q=response*p
        f0,f90=f*(1+q),f*(1-q)
        assert 0<f0<1 and 0<f90<1
        assert abs((f0-f90)/(f0+f90)-q)<1e-14
        odds0,odds90=f0/(1-f0),f90/(1-f90)
        aq_odds=(odds0-odds90)/(odds0+odds90)
        assert abs(aq_odds-q/(1-f+f*q*q))<1e-14
        merit=response*math.sqrt(f)
        groups[e].append((merit,eth))
        out.append({'Egamma_MeV':e,'Eth_keV':eth,'Nbar_fraction':f,'R':response,
                    'Q_count_fraction_source':q,'algebraic_f0':f0,'algebraic_f90':f90,
                    'wrong_C_over_anti_odds_asymmetry':aq_odds,
                    'source_relative_merit_RsqrtNbar':merit,
                    'conditional_sigmaR_from_P_only_excluded_in_source':response*spol/p,
                    'quoted_stat_sigmaR':sr/100,
                    'no_actual_counts_or_full_covariance_reconstructed':True})
    cal=[]
    for e,a2,a4,p,spol in c['P_rows']:
        point=(1.5*a2+.625*a4)/(1-a2/2+3*a4/8)
        cal.append({'Egamma_MeV':e,'reported_P':p,'pointP_from_source_central_coefficients':point})
    cc,aa=sp.symbols('C A',positive=True)
    frac=cc/(cc+aa)
    var=sp.diff(frac,cc)**2*cc+sp.diff(frac,aa)**2*aa
    assert sp.simplify(var-frac*(1-frac)/(cc+aa))==0
    result={'at':datetime.now(timezone.utc).isoformat(),
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'contract_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'actual_Ge_rows':out,'Table1_point_P_controls':cal,
            'largest_printed_central_merit_threshold_within_each_energy_only':{
                str(e):max(v)[1] for e,v in groups.items()},
            'symbolic_primitive_count_variance':'Var(C/(C+A))=f(1-f)/(C+A) for independent primitive Poisson C,A',
            'wrong_denominator_odds_relation':'Qodds=q/(1-fbar+fbar*q^2), q=R*P',
            'source_fraction_vs_odds_and_variance_controls':True,
            'partial_error_budget_exclusion_not_claimed_as_source_error':True,
            'no_actual_fullSigma_threshold_CI_or_new_P_R':True,'ok':True}
    (RUN/'bass1972-Ge-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='actual_Ge_rows'},indent=2))


if __name__=='__main__':
    main()
