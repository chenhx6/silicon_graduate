#!/usr/bin/env python3
"""Inclusive vs anti-alpha diagnostics in the already-read MI07 selection."""
from datetime import datetime, timezone
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def main():
    path=RUN/'sega-singles-selection-contract.json';c=json.loads(path.read_text())
    raw=c['downscale']*c['approx_singles_per_detector'];tag=c['approx_coincidences_per_detector']
    frac=tag/raw;odds=frac/(1-frac);exclusive_frac=tag/(raw+tag)
    pp,f=sp.symbols('p f',real=True);anti=-f*pp/(1-f)
    assert sp.simplify(f*pp+(1-f)*anti)==0
    q,at,aa=sp.symbols('Q a_tag a_anti',real=True)
    # Count asymmetry transform when a' / a = (1+a_anti)/(1-a_anti).
    expression=sp.simplify(((1+at)-(1+aa)/(1-aa)*(1-at))/
                           ((1+at)+(1+aa)/(1-aa)*(1-at)))
    assert sp.simplify(expression-(at-aa)/(1-at*aa))==0
    scale=c['source_Q_for_conditional_scale'];ageom=c['a_reference']
    abound=scale*odds
    delta_bound=ageom*2*abound/(1-abound)
    calibration_bias=[]
    for target_p in [-1.,0.,1.]:
        tag_a=scale*target_p;anti_a=-odds*tag_a
        measured=(tag_a-anti_a)/(1-tag_a*anti_a)
        calibration_bias.append({'design_tag_P':target_p,'complement_a':anti_a,
             'A_using_complement_as_null':measured,
             'relative_Q_shift_if_nonzero_P':None if target_p==0 else measured/(scale*target_p)-1})
    # If the photopeak tag fraction is reused without matching response, only
    # class capacities can be bounded; fractions alone do not specify Stokes.
    x,y=c['rounded_photopeak_class_fractions']['perp'],c['rounded_photopeak_class_fractions']['parallel']
    capacity=[]
    vertices=[(0.,0.),(min(frac,x),0.),(0.,min(frac,y))]
    if frac<=x and frac<=y:
        # Here all allocations may lie in either class, so the three vertices
        # cover the allowed z_perp,z_parallel simplex.
        pass
    else:
        raise AssertionError('Update capacity vertices for this parameter domain')
    for zx,zy in vertices:
        relative_null_ratio=(1-zx/x)/(1-zy/y)
        capacity.append({'removed_perp_fraction_of_fullpeak':zx,
                         'removed_parallel_fraction_of_fullpeak':zy,
                         'a_anti_over_a_inclusive':relative_null_ratio})
    capacity_range=[min(x['a_anti_over_a_inclusive'] for x in capacity),
                    max(x['a_anti_over_a_inclusive'] for x in capacity)]
    result={'at':datetime.now(timezone.utc).isoformat(),
       'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'contract_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
       'headline_count_interpretations':{'unscaled_singles':raw,'tag':tag,
          'inclusive_tag_fraction':frac,'inclusive_complement_odds':odds,
          'if_singles_exclusive_tag_fraction':exclusive_frac,
          'if_singles_exclusive_complement_odds':tag/raw},
       'matched_response_scalar_Q_design':{'P_complement_absolute_bound':odds,
          'count_asymmetry_complement_bound_Q_0_14':abound,
          'absolute_a_bias_bound_at_source_a':delta_bound,'quoted_a_sigma':c['quoted_a_sigma'],
          'tag_P_control_rows':calibration_bias,'actual_response_not_attested':True},
       'counts_only_class_capacity_controls':capacity,
       'counts_only_relative_a_ratio_range_not_actual_bias':capacity_range,
       'exact_complement_and_count_ratio_transform_controls':True,
       'headline_f_does_not_attest_polarimetry_selection':True,
       'no_original_sorter_or_Q_correction_or_CI_inferred':True,'ok':True}
    (RUN/'sega-singles-selection-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['headline_count_interpretations','matched_response_scalar_Q_design',
       'counts_only_relative_a_ratio_range_not_actual_bias']},indent=2))


if __name__=='__main__':
    main()
