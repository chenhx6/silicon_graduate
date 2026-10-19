#!/usr/bin/env python3
"""Printed Table I and conditional controls; no new experimental rates or CI."""
import hashlib
import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def main():
    p=RUN/'jenkins2004-exercise-contract.json';c=json.loads(p.read_text())
    assert c['identity']=='J04-PRINTED-ENERGY-THRESHOLD-STRENGTH-01'
    assert hashlib.sha256((ROOT/c['source_pdf']).read_bytes()).hexdigest()==c['source_sha256']
    f=c['lab_factor_massnumber'];rows=[]
    for row in c['parents']:
        calculated=f*(row['Ex']-c['Qp_keV'])
        assert abs(calculated-row['Ep'])<=.05
        rows.append(dict(row,Ep_massnumber_NR_keV=calculated,
                         central_residual_keV=calculated-row['Ep'],
                         sigma_if_Ex_and_Q_independent=f*math.hypot(row['sigma_Ex'],c['Qp_sigma_keV'])))
    common=f*f*c['Qp_sigma_keV']**2
    statistical=(2*c['J']+1)/((2*c['Jp']+1)*(2*c['Jtarget']+1))
    width_meV=c['hbar_eV_s']/(c['tau_fs']*1e-15)*1000
    k=c['adopted_omega_gamma_meV']/(statistical*width_meV)
    assert 0<k<.25
    roots=[(1-math.sqrt(1-4*k))/2,(1+math.sqrt(1-4*k))/2]
    assert all(abs(b*(1-b)-k)<1e-14 for b in roots)
    visible=sum(x['percent']/100 for x in c['branches_7769'] if x['Eg_keV']>=c['ideal_threshold_keV'])
    result={'identity':c['identity'],'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'contract_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
            'parent_rows':rows,'common_Q_only_covariance_component_keV2':common,
            'common_Q_scope':'f^2 sigmaQ^2 11^T if Q independent of Ex; notactualjointSigma',
            'actual_sigma_Ep_closure_claimed':False,
            'tau_width_conditional':{'tau_fs':c['tau_fs'],'total_width_meV':width_meV,
                                     'local_scale_if_tau_scale_is_SD_meV':width_meV*c['tau_quoted_scale_fs']/c['tau_fs']},
            'adopted_rate_plus_new_tau_conditional_Bp_roots':roots,
            'Bp_roots_are_not_a_measurement_or_CI':True,
            'threshold_inventory_design':{'visible_fraction':visible,'total_over_visible':1/visible,
                                          'not_original_efficiency_or_4meVlimit_replay':True},
            'strength_table_footnote_preserved':'omega_gamma1.8(.7) adoptedAngulo, notnewtauderivation',
            'new_experimental_fit_or_95percent_interval':False,'ok':True}
    (RUN/'jenkins2004-exercise-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
