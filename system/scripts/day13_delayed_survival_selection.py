#!/usr/bin/env python3
"""Day13 proper flight survival and stopped-delayed-gate selection toy.

Path760cm and velocity2.9-4cm/ns are LS23 scales. Uniform velocities, instant
stopping and unit photon/detector probability are self-chosen. Window100ns-
200us is chosen from a capability scale, not an actual executed gate. Decay
does not remove the isotope ion; the probability tracks isomer survival only.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss


C_CM_NS=29.9792458


def probability(velocity,tau,low,high,length=760.):
    velocity=np.asarray(velocity);beta=velocity/C_CM_NS
    gamma=1/np.sqrt(1-beta*beta)
    lab_flight=length/velocity
    survival=np.exp(-lab_flight/(gamma*tau))
    conditional_gate=math.exp(-low/tau)-math.exp(-high/tau)
    return survival,survival*conditional_gate,lab_flight/gamma


def calculate():
    velocity_low,velocity_high=2.9,4.;gate_low,gate_high=100.,200000.
    source_half_ns=28100.;source_tau=source_half_ns/math.log(2)
    rng=np.random.default_rng(131025);samples=500000
    velocities=rng.uniform(velocity_low,velocity_high,samples)
    nodes,weights=leggauss(128);vquad=(velocity_low+velocity_high)/2+(velocity_high-velocity_low)/2*nodes
    normalized_weights=weights/2
    rows=[];max_MC=0.
    for tau in (100.,1000.,source_tau,1e6):
        surv,selected,properflight=probability(vquad,tau,gate_low,gate_high)
        mean_survival=float(normalized_weights@surv);total=float(normalized_weights@selected)
        conditional_mean_v=float(normalized_weights@(vquad*selected)/total)
        short_v=probability(velocity_low,tau,gate_low,gate_high)[0]
        fast_v=probability(velocity_high,tau,gate_low,gate_high)[0]
        _,_,flight_mc=probability(velocities,tau,gate_low,gate_high)
        lifetime=rng.exponential(tau,samples)
        survivors=lifetime>flight_mc
        # Memoryless residual proper waiting after instant stopping.
        residual=lifetime-flight_mc
        accepted=survivors&(residual>=gate_low)&(residual<=gate_high)
        mc=float(np.mean(accepted));max_MC=max(max_MC,abs(mc-total))
        mean_velocity_MC=float(np.mean(velocities[accepted]))
        assert abs(mc-total)<.002 and abs(mean_velocity_MC-conditional_mean_v)<.006
        rows.append({'chosen_proper_tau_ns':tau,
                     'tau_kind':'source_half28100ns_divided_by_ln2' if tau==source_tau else 'self-chosen mean lifetime',
                     'mean_isomer_survival_to_FP':mean_survival,
                     'stopped_window_fraction_given_survival':math.exp(-gate_low/tau)-math.exp(-gate_high/tau),
                     'total_ideal_delayed_selection_probability':total,'MC_delayed_probability':mc,
                     'prior_uniform_mean_v_cm_per_ns':(velocity_low+velocity_high)/2,
                     'conditional_delayed_mean_v_cm_per_ns':conditional_mean_v,
                     'MC_conditional_delayed_mean_v_cm_per_ns':mean_velocity_MC,
                     'survival_fast_over_slow_ratio':float(fast_v/short_v)})
    # Independent gate/no-flight limits; replace the finite window with full
    # positive time support to recover survival alone.
    surv,full,_=probability(vquad,1000.,0.,math.inf)
    assert np.max(np.abs(surv-full))==0
    zero_surv,zero_gate,_=probability(vquad,1000.,gate_low,gate_high,length=0)
    assert np.max(np.abs(zero_surv-1))==0
    assert np.max(np.abs(zero_gate-(math.exp(-gate_low/1000)-math.exp(-gate_high/1000))))<1e-15
    assert rows[0]['conditional_delayed_mean_v_cm_per_ns']>3.5
    assert abs(source_tau*math.log(2)-source_half_ns)<1e-9
    return {'schema_version':1,'kind':'synthetic flight-survival/stopped-delayed-gate selection model; no actual intensity fit',
            'parameters':{'path_cm':760.,'uniform_velocity_cm_per_ns':[velocity_low,velocity_high],
                          'chosen_stopped_delay_window_ns':[gate_low,gate_high],
                          '132Te_source_half_life_ns':source_half_ns,'132Te_corresponding_mean_tau_ns':source_tau,
                          'instant_stop':True,'photon_branch_and_detector_efficiency':1.,'samples':samples},
            'rows':rows,'verification':{'analytic_velocity_integral_and_MC_probability_max_difference':max_MC,
                                      'conditional_velocity_MC_passed':True,'mean_half_conversion_passed':True,
                                      'full_delay_window_recovers_survival_limit_passed':True,
                                      'zero_flight_recovers_stopped_gate_limit_passed':True,'passed':True},
            'boundaries':['Isomer decay does not destroy the isotope ion, so survival is not a particle detection efficiency.',
                          'Actual production/velocity/angle distributions, branch/ICC and delay response are absent.',
                          'A missing delayed peak requires survival/gate/efficiency sensitivity before it falsifies an isomer.',
                          'Quoted LS23 capability range is not proof of this chosen gate being used in the original experiment.'],
            'numpy_version':np.__version__}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=calculate()
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(a.output),'verification':r['verification'],'rows':r['rows']}))


if __name__=='__main__':
    main()
