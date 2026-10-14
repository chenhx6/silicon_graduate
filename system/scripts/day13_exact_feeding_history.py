#!/usr/bin/env python3
"""Exact synthetic feeding/target-lifetime ambiguity in proper emission time.

For tau_lower < tau_effective, a direct fraction tau_lower/tau_effective
and feeder fraction 1-that, with tau_upper=tau_effective, reproduce exactly
one exponential with tau_effective. Common transport and target-gamma
response cannot distinguish the models when feeder tags/recoil are omitted.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.stats import ks_2samp

from day13_entry_gate_feeding_design import (
    kernel, fed_density, E0_KEV, BETA_IN, BETA_EXIT,
    T_EXIT_PS, SIGMA_KEV, ANGLES_DEG,
)


def mixed_time_density(t, tau_eff, tau_low):
    direct = tau_low/tau_eff
    return direct*np.exp(-t/tau_low)/tau_low + (1-direct)*fed_density(t,tau_low,tau_eff)


def photon_density(grid, tau_low, f, tau_upper, angle):
    ratios, weights, _ = kernel(tau_low, f, angle, tau3=tau_upper, order=192)
    gaussian = np.exp(-0.5*((grid[:,None]-E0_KEV*ratios)/SIGMA_KEV)**2)
    return gaussian@weights/(math.sqrt(2*math.pi)*SIGMA_KEV)


def calculate():
    tau_eff, tau_low = 0.12, 0.06
    direct, feed = tau_low/tau_eff, 1-tau_low/tau_eff
    t = np.linspace(0,2.0,10001)
    simple = np.exp(-t/tau_eff)/tau_eff
    mixed = mixed_time_density(t,tau_eff,tau_low)
    time_error = float(np.max(np.abs(simple-mixed)))
    assert time_error < 1e-12
    norm = quad(lambda x:float(mixed_time_density(x,tau_eff,tau_low)),0,np.inf)[0]
    assert abs(norm-1)<1e-10
    laplace = []
    for rate in (0.0, 0.5, 1.0, 5.0, 10.0, 100.0):
        single = 1/(1+rate*tau_eff)
        mixture = (direct+feed/(1+rate*tau_eff))/(1+rate*tau_low)
        assert abs(single-mixture)<1e-15
        laplace.append(dict(rate_per_ps=rate,single=single,mixture=mixture))
    # General ratio and endpoint limits in the Laplace representation.
    for ratio in (0.0,0.001,0.1,0.5,0.9,1.0):
        lower = ratio*tau_eff
        for rate in (0.0,1.0,10.0,100.0):
            assert abs((ratio+(1-ratio)/(1+rate*tau_eff))/(1+rate*lower)
                       -1/(1+rate*tau_eff)) < 1e-15
    mean = tau_low+feed*tau_eff
    variance = tau_low**2+feed*(2-feed)*tau_eff**2
    assert abs(mean-tau_eff)<1e-15 and abs(variance-tau_eff**2)<1e-15

    grid = np.linspace(E0_KEV-180,E0_KEV+25,1641)
    energy_error = 0.0
    normalization_error = 0.0
    for angle in ANGLES_DEG:
        p = photon_density(grid,tau_eff,0.0,tau_eff,angle)
        q = photon_density(grid,tau_low,feed,tau_eff,angle)
        energy_error=max(energy_error,float(np.max(np.abs(p-q))))
        normalization_error=max(normalization_error,abs(float(np.trapezoid(p,grid))-1))
    assert energy_error<1e-12 and normalization_error<1e-9
    rng=np.random.default_rng(131421)
    n=600000
    t_simple=rng.exponential(tau_eff,n)
    fed=rng.random(n)<feed
    t_mixed=rng.exponential(tau_low,n)+fed*rng.exponential(tau_eff,n)
    ks=ks_2samp(t_simple,t_mixed)
    assert ks.statistic<0.005
    for times in (t_simple,t_mixed):
        assert abs(times.mean()-tau_eff)<5*tau_eff/math.sqrt(n)
    photon_moments=[]
    for angle in ANGLES_DEG:
        cosine=math.cos(math.radians(angle))
        d_exit=(1-BETA_EXIT*cosine)/math.sqrt(1-BETA_EXIT**2)
        values=[]
        for times in (t_simple,t_mixed):
            beta=np.where(times<T_EXIT_PS,
                          BETA_IN+(BETA_EXIT-BETA_IN)*times/T_EXIT_PS,BETA_EXIT)
            d=(1-beta*cosine)/np.sqrt(1-beta*beta)
            energy=E0_KEV*d_exit/d+rng.normal(0,SIGMA_KEV,n)
            w=1/d**2
            mu=float(w@energy/w.sum())
            se=float(np.sqrt(np.sum(w*w*(energy-mu)**2))/w.sum())
            values.append(dict(mean_keV=mu,mean_SE_keV=se))
        assert abs(values[0]['mean_keV']-values[1]['mean_keV']) < 5*math.hypot(
            values[0]['mean_SE_keV'],values[1]['mean_SE_keV'])
        photon_moments.append(dict(angle_deg=angle,single=values[0],feeding=values[1]))
    return dict(schema_version=1,kind='synthetic exact propertime/feeding ambiguity',
                chosen_parameters=dict(effective_tau_ps=tau_eff,target_tau_ps=tau_low,
                                       feeder_tau_ps=tau_eff,direct_entry_fraction=direct,
                                       feeder_entry_fraction=feed,
                                       beta_in=BETA_IN,beta_exit=BETA_EXIT,
                                       common_slowing_duration_ps=T_EXIT_PS,
                                       target_gamma_keV=E0_KEV,Gaussian_sigma_keV=SIGMA_KEV,
                                       point_angles_deg=list(ANGLES_DEG)),
                moment_identity=dict(single_mean_ps=tau_eff,mixed_mean_ps=mean,
                                     single_variance_ps2=tau_eff**2,mixed_variance_ps2=variance),
                laplace_checks=laplace,
                independent_MC=dict(repetitions=n,proper_time_KS_statistic=float(ks.statistic),
                                    proper_time_KS_pvalue=float(ks.pvalue),
                                    single_time_mean_ps=float(t_simple.mean()),
                                    mixed_time_mean_ps=float(t_mixed.mean()),photon_moments=photon_moments),
                companion_observation=dict(denominator="pre-angular-selection parent population with unit4pi target acceptance",
                                           chosen_feeder_gamma_tag_efficiency=0.25,
                                           predicted_tag_fraction_in_feeding_model=feed*0.25,
                                           predicted_tag_fraction_in_direct_only_model=0.0),
                verification=dict(full_time_density_max_error=time_error,
                                  probability_normalization_error=abs(norm-1),
                                  Laplace_general_ratio_and_endpoint_checks_passed=True,
                                  first_two_moments_identity_passed=True,
                                  energy_density_three_angle_max_error=energy_error,
                                  photon_profile_normalization_max_error=normalization_error,
                                  independent_time_MC_KS_passed=True,
                                  independent_weighted_photon_MC_passed=True,
                                  all_passed=True),
                boundaries=['Exact only within independent exponential waits, chosen branching/entry fractions and common transport.',
                            'Upper-photon recoil, state-dependent transport/alignment, cascade angular correlations, feeder observation and entry selection are omitted.',
                            'Selfchosen120/60fs does not infer the actual150/70fs experiment feeding or unknown upper lifetime.',
                            'Known54fs feeder in ZA23 is not the120fs feeder required by this counterexample.',
                            'KS is a simulation consistency check, not an experimental p-value or validation of source feeding assumptions.',
                            'Feeder gamma/particle excitation gates or known entry history can break or exclude this model.'])


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    result=calculate()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(args.output),'verification':result['verification'],
                      'parameters':result['chosen_parameters'],'MC':result['independent_MC']}))


if __name__=='__main__':
    main()
