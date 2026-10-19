#!/usr/bin/env python3
"""Printed input and conditional method checks; no original data/fit recovery."""
import hashlib
import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def main():
    p=RUN/'kirsebom2016-exercise-contract.json'
    c=json.loads(p.read_text())
    assert c['identity']=='K16-PRINTED-INPUT-AND-CONDITIONAL-EXERCISE-01'
    assert hashlib.sha256((ROOT/c['source_pdf']).read_bytes()).hexdigest()==c['source_sha256']
    A,dc,cp=c['swelling_A'],c['quoted_A_scale'],c['peak_c']
    density=[{'A':a,'density_relative_to_unswollen_Au':1/(1+a*cp),
              'r_mass_He3_over_Au_for_zero_net_change':197*a/3}
             for a in [A-dc,A,A+dc]]
    statistical_factor=lambda J:(2*J+1)/((2*c['Jp']+1)*(2*c['JNa']+1))
    width_meV=c['hbar_eV_s']/(c['tau_upper_fs']*1e-15)*1000
    bp=c['Bp_intro_printed']
    strength=statistical_factor(c['J'])*width_meV*bp*(1-bp)
    strength_alt=statistical_factor(c['J_alternative'])*width_meV*bp*(1-bp)
    assert abs(strength_alt/strength-.75)<1e-12
    clocks=[{'beta':b,'gamma_squared':1/(1-b*b),
             'printed_integral_over_proper_time_integral':1/(1-b*b)}
            for b in c['beta_source_range']]
    solid=lambda deg:2*math.pi*(1-math.cos(math.radians(deg)))
    geometry_ratio=solid(16)*solid(16)/(solid(8)*solid(32))
    delta_beta=.32e-3/c['A_recoil']*c['shorttime_stopping_MeV_um']
    shift=delta_beta*c['gamma_transition_approx_keV']
    fwhm=3.3*7.8**.52
    finite=[x for x in c['tableII'] if 'tau_fs' in x]
    limits=[x for x in c['tableII'] if 'tau_upper_fs' in x]
    assert len(finite)==4 and len(limits)==9
    result={'identity':c['identity'],'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'contract_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
            'tableII_printed_rows':c['tableII'],'finite_count':len(finite),'limit_count':len(limits),
            'swelling_density_only_controls':density,
            'complete_stopping_ratio_formula':'[1+(3/197)*c*r_mass]/[1+A*c]',
            'Bp_relative_printed_scales':{'intro':c['Bp_intro_printed_scale']/bp,
                                          'conclusion':c['Bp_conclusion_scale']/bp},
            'fixed_central_Bp_strength_at_tau12':{'J':c['J'],'omega_gamma_meV':strength,
                'J_alternative':c['J_alternative'],'omega_gamma_alternative_meV':strength_alt,
                'new_95percent_joint_CI':False},
            'constant_beta_clock_comparison':clocks,
            'ideal_cone_solid_angle_product_Fig21_modified_over_original':geometry_ratio,
            'one_fs_shorttime_approx':{'delta_beta':delta_beta,'gamma_shift_keV_approx':shift},
            'intrinsic_resolution_7p8_MeV':{'FWHM_keV':fwhm,'relative_FWHM':fwhm/7800},
            'original_fit_or_covariance_recovered':False,'paper_code_equivalence_claimed':False,'ok':True}
    (RUN/'kirsebom2016-exercise-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='tableII_printed_rows'},indent=2))


if __name__=='__main__':
    main()
