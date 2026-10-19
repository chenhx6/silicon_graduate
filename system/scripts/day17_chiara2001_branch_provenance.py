#!/usr/bin/env python3
"""Printed parent-level photon inventories and lifetime coverage, not a new fit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def forward(case, intensity_set, only_rate_columns=False):
    selected=[x for x in case['transitions'] if not only_rate_columns or x['in_rate_table']]
    total=sum(x['intensities'][intensity_set] for x in selected)
    result=[]
    for x in selected:
        fraction=x['intensities'][intensity_set]/total
        row={'transition':x['id'],'energy_keV':x['E_keV'],'visible_photon_share':fraction,
             'conditional_partial_tau_ps':case['tau_ps']/fraction}
        if x['rate_control_kind'] in ['M1','E2']:
            kind=x['rate_control_kind'];power=3 if kind=='M1' else 5
            coeff=.0569 if kind=='M1' else .0816
            value=coeff*fraction/(case['tau_ps']*(x['E_keV']/1000)**power)
            row.update(kind=kind,conditional_B=value,units='muN^2' if kind=='M1' else 'e^2 b^2')
            if x.get('reported_B') is not None:
                row['reported_B']=x['reported_B']
                row['conditional_over_reported_minus_one']=value/x['reported_B']-1
        result.append(row)
    return {'parent':case['parent'],'intensity_set':intensity_set,
            'only_rate_table_columns':only_rate_columns,'visible_photon_sum':total,'rows':result,
            'boundary':'visible photon normalization, alpha=0 and dipole delta=0; not original IC/complete inventory/Cov or experimental B/CI'}


def main():
    cp=RUN/'chiara2001-branch-contract.json';c=json.loads(cp.read_text())
    assert sha(ROOT/c['pdf'])==c['pdf_sha256']
    rows=[]
    for case in c['parents']:
        rows.append(forward(case,case['author_input_set']))
        if any(not x['in_rate_table'] for x in case['transitions']):
            rows.append(forward(case,case['author_input_set'],True))
        if case.get('counter_input_set'):
            rows.append(forward(case,case['counter_input_set']))
    thin=next(x for x in rows if x['parent']=='110In:band3:(19+)' and x['intensity_set']=='thin')
    backed=next(x for x in rows if x['parent']==thin['parent'] and x['intensity_set']=='backed')
    e2=lambda x:next(v['conditional_B'] for v in x['rows'] if v.get('kind')=='E2')
    ratio=e2(backed)/e2(thin)
    measured=[{**x,'hbar_omega_MeV':x['E_keV']/2000} for x in c['AMR_fitted']]
    observed=[{**x,'hbar_omega_MeV':x['E_keV']/2000,'lifetime_or_B_not_measured_here':True}
              for x in c['AMR_observed_higher']]
    high=max(x['hbar_omega_MeV'] for x in measured)
    assert high<c['predicted_decline_omega_MeV']
    out={'at':datetime.now(timezone.utc).isoformat(),'script_sha256':sha(Path(__file__)),
         'contract_sha256':sha(cp),'photon_only_forward_controls':rows,
         'counter_input_E2_backed_over_thin':ratio,
         'conditional_Qt_backed_over_thin_at_fixed_same_geometry':math.sqrt(ratio),
         'AMR_lifetime_covered_points':measured,'AMR_observed_but_not_lifetime_measured_points':observed,
         'largest_lifetime_covered_omega_MeV':high,
         'author_predicted_decline_above_omega_MeV':c['predicted_decline_omega_MeV'],
         'observed_candidates_above_decline_threshold':[x for x in observed if x['hbar_omega_MeV']>c['predicted_decline_omega_MeV']],
         'no_IC_delta_covariance_or_branch_tuned_to_match':True,
         'no_Qt_geometry_identification_from_method_citation':True,
         'no_new_experimental_lifetime_strength_shape_or_CI':True,'ok':True}
    (RUN/'chiara2001-branch-result.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(out,ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
