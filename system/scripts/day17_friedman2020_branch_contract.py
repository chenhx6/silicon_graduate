#!/usr/bin/env python3
"""Audit printed GADGET intensity roles and conditional covariance, not an event fit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    cp=RUN/'friedman2020-exercise-contract.json';c=json.loads(cp.read_text())
    assert c['identity']=='FR20-GAS-PROTON-NORMALIZATION-01'
    assert sha(ROOT/c['pdf'])==c['pdf_sha256']
    mean=sum(c['ratios'])/2
    st=c['stat_scales'][0];sy=c['shared_systematic_scale']
    assert c['stat_scales'][0]==c['stat_scales'][1]
    combination=[{'declared_stat_correlation':rho,'combined_center':mean,
                  'conditional_scale':math.sqrt(st*st*(1+rho)/2+sy*sy)} for rho in [0,.5,1]]
    i=mean*c['I866_absolute_percent']
    si=math.hypot(c['reported_combined_scale']*c['I866_absolute_percent'],
                  mean*c['I866_scale_percent'])
    p=c['I204_reported_percent'];sp=c['I204_scale_percent'];g=c['betaGamma_percent'];sg=c['betaGamma_scale_percent']
    total=p+g;bp=p/total;dp=g/total**2;dg=-p/total**2
    sbp=math.hypot(dp*sp,dg*sg)
    rate=lambda tau,branch:(2*c['J_fixed']+1)/14*c['hbar_meV_fs']/tau*branch*(1-branch)
    central=rate(c['tau_fixed_fs'],c['Bp_reported'])
    tau_endpoint=rate(c['tau_upper_endpoint_fs'],c['Bp_reported'])
    legacy_gamma=(6.63+1.53)*.433
    eff={str(e):v for e,v in c['efficiencies']}
    # raw ratio = corrected ratio * eps_low/eps_reference, if otherwise matched.
    raw_control=c['reported_combined_ratio']*eff['204']/eff['866']
    checks={'combined_ratio_center_matches_printed':abs(mean-c['reported_combined_ratio'])<1e-15,
            'independent_stat_shared_sys_scale_rounds_to_0p004':round(combination[0]['conditional_scale'],3)==.004,
            'daughter_fraction_near_reported':abs(bp-c['Bp_reported'])<5e-5,
            'omega_center_near_printed_0p24':abs(central-.24)<.005,
            'fullstatcorrelation_changes_combinedscale':combination[-1]['conditional_scale']>combination[0]['conditional_scale'],
            'old_thesis_printed_gamma_sum_not_equal_new_adopted':abs(legacy_gamma-g)>.1}
    out={'at':datetime.now(timezone.utc).isoformat(),'script_sha256':sha(Path(__file__)),
         'contract_sha256':sha(cp),'conditional_ratio_combination':combination,
         'absolute_beta_proton':{'from_rounded_ratio_and_old_reference_percent':i,
             'conditional_independent_scale_percent':si,'reported_percent':p,
             'nominal_center_residual_percent':i-p},
         'daughter_branch':{'from_reported_absolute_inputs':bp,'conditional_independent_scale':sbp,
             'gradient_per_percent':[dp,dg],
             'variance_with_unknown_covariance':'dp^2 Var(p)+dg^2 Var(g)+2dp dg Cov(p,g)',
             'no_full_Cov_or_CI_recovered':True},
         'conditional_rate':{'fixed_tau_J_reported_Bp_meV':central,
              'at_tau_upper_endpoint_fixed_Bp_meV':tau_endpoint,
              'endpoint_is_not_original_joint_CL_lowerlimit':True},
         'efficiency_raw_ratio_control':{'corrected_ratio':c['reported_combined_ratio'],
              'implied_raw_ratio_if_matched':raw_control,'no_new_efficiency_measured':True},
         'old_thesis_gamma_denominator_boundary':{'old_Fig5p7_two_gamma_sum_absolute_percent':legacy_gamma,
              'F20_adopted_gamma_through_state_percent':g,
              'boundary':'different printed source/inventory; original gamma references needed, not forced closure'},
         'checks':checks,'no_new_experimental_branch_tau_spin_or_CI':True,'ok':all(checks.values())}
    (RUN/'friedman2020-exercise-result.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(out,ensure_ascii=False,indent=2))
    return 0 if out['ok'] else 1


if __name__=='__main__':
    raise SystemExit(main())
