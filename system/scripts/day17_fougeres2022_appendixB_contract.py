#!/usr/bin/env python3
"""Actual calibration tables and conditional activity/parameter covariance audit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    cp = RUN / 'fougeres2022-thesis-B-exercise-contract.json'
    c = json.loads(cp.read_text())
    assert sha(ROOT/c['pdf']) == c['pdf_sha256']
    strips = json.loads((ROOT/c['strip_table']).read_text())['rows']
    assert len(strips) == 64
    counts = {k:sum(x['status']==k for x in strips) for k in ['numeric','missing','ambiguous-literal']}
    assert counts == {'numeric':62,'missing':1,'ambiguous-literal':1}
    activities = []
    for role, lam in [('if_printed_value_is_mean',1/c['printed_tau_s']),
                       ('if_printed_value_is_half',math.log(2)/c['printed_tau_s'])]:
        a = c['initial_activity_per_s']*math.exp(-lam*c['source_age_s'])
        decays = a*(-math.expm1(-lam*c['counting_time_s']))/lam
        activities.append({'role':role,'decay_constant_per_s':lam,'activity_at_start_per_s':a,
                           'expected_decays_during_run_conditional':decays,
                           'boundary':'conditional role arithmetic, not inferred original job normalization'})
    predictions = []
    for q, strip in [(2,1),(1,1)]:
        row = next(x for x in strips if x['quadrant']==q and x['strip']==strip)
        b, sb = row['offset_keV_and_quoted_error']
        m, sm = row['gain_keV_per_au_and_quoted_error']
        for e in c['alpha_reference_energies_keV']:
            a = (e-b)/m
            predictions.append({'quadrant':q,'strip':strip,'reference_E_keV':e,'implied_raw_amplitude_au':a,
                                'conditional_parameter_scale_min_keV':abs(sb-abs(a)*sm),
                                'conditional_parameter_scale_max_keV':sb+abs(a)*sm,
                                'conditional_rho_zero_scale_keV':math.hypot(sb,a*sm),
                                'boundary':'fixed raw amplitude, quoted marginal scales as variance inputs; actual covariance/CL unknown, not detector width'})
    resolution = [{**x,'FWHM_using_author_factor_keV':x['sigma_keV']*2.35,
                   'nominal_centroid_relative_to_rounded_reference_percent':100*(x['centroid_keV']-x['reference_keV'])/x['reference_keV']}
                  for x in c['TableB1']]
    out = {'at':datetime.now(timezone.utc).isoformat(),'script_sha256':sha(Path(__file__)),
           'contract_sha256':sha(cp),'strip_status_counts':counts,
           'incomplete_or_ambiguous_strips':[x for x in strips if x['status']!='numeric'],
           'TableB1_resolution_crosschecks':resolution,'activity_role_controls':activities,
           'half_role_over_mean_role_activity_ratio':activities[1]['activity_at_start_per_s']/activities[0]['activity_at_start_per_s'],
           'actual_parameter_covariance_controls':predictions,
           'shared_calibration_cross_event_covariance':'Var(b)+A_i*A_j*Var(m)+(A_i+A_j)*Cov(b,m), for fixed raw amplitudes',
           'no_missing_calibration_imputed':True,
           'source_coreE_is_not_the_same_observable_as_TrackE_efficiency':True,
           'no_new_experimental_efficiency_tau_branch_or_CI':True,'ok':True}
    (RUN/'fougeres2022-thesis-B-exercise-result.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(out,ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
