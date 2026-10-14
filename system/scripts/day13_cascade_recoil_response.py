#!/usr/bin/env python3
"""Synthetic cascade-recoil response breaking an ideal common-kernel identity.

Constant parent flight; isotropic upper and lower photons; mass proxies;
parent-reference correction omits the first photon recoil. Chosen Gaussian
resolution, gap and population. No actual source spectrum or lifetime fit.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss


MU_KEV=931494.10242
E0_KEV=2396.1
SIGMA_KEV=2.0
FEED_FRACTION=0.5


def boost(k,b):
    b=np.asarray(b,dtype=float)
    b2=float(b@b)
    if b2==0:
        return np.asarray(k,dtype=float).copy()
    g=1/math.sqrt(1-b2)
    dot=float(b@k[1:])
    return np.r_[g*(k[0]+dot),k[1:]+(g*g/(g+1)*dot+g*k[0])*b]


def recoil(a,gap):
    lower=a*MU_KEV
    upper=lower+gap
    photon=gap*(2*lower+gap)/(2*upper)
    daughter_energy=upper-photon
    speed=photon/daughter_energy
    gamma=daughter_energy/lower
    assert abs((daughter_energy**2-photon**2)/lower**2-1)<1e-14
    assert abs(daughter_energy+photon-upper)<1e-8
    return lower,upper,photon,daughter_energy,speed,gamma


def calculate():
    nodes,quadw=leggauss(192)
    grid=np.linspace(E0_KEV-20,E0_KEV+20,2001)
    g0=np.exp(-0.5*((grid-E0_KEV)/SIGMA_KEV)**2)/(math.sqrt(2*math.pi)*SIGMA_KEV)
    cases=[]
    for a,gap in [(20,100.),(20,1000.),(20,3000.),(130,1000.)]:
        mass,upper,k,daughter,u,gamma=recoil(a,gap)
        d=gamma*(1-u*nodes)
        weights=quadw/2/d**2
        normalization=float(weights.sum())
        assert abs(normalization-1)<1e-13
        centers=E0_KEV/d
        mean_quad=float(weights@centers)
        var_quad=float(weights@((centers-mean_quad)**2))
        mean=E0_KEV*gamma
        variance=(E0_KEV*gamma*u)**2/3
        assert abs(mean_quad-mean)<1e-9 and abs(var_quad/variance-1)<1e-8
        gaussian=np.exp(-0.5*((grid[:,None]-centers)/SIGMA_KEV)**2)
        fed=gaussian@weights/(math.sqrt(2*math.pi)*SIGMA_KEV)
        p=(1-FEED_FRACTION)*g0+FEED_FRACTION*fed
        mu=(1-FEED_FRACTION)*E0_KEV+FEED_FRACTION*mean
        var=SIGMA_KEV**2+FEED_FRACTION*variance
        var+=FEED_FRACTION*(1-FEED_FRACTION)*(mean-E0_KEV)**2
        fitted_g=np.exp(-0.5*((grid-mu)/math.sqrt(var))**2)/math.sqrt(2*math.pi*var)
        norm_error=abs(float(np.trapezoid(p,grid))-1)
        fixed_kl=float(np.trapezoid(p*(np.log(np.maximum(p,1e-300))-np.log(np.maximum(g0,1e-300))),grid))
        profile_kl=float(np.trapezoid(p*(np.log(np.maximum(p,1e-300))-np.log(np.maximum(fitted_g,1e-300))),grid))
        assert norm_error<1e-10 and fixed_kl>=-1e-13 and profile_kl>=-1e-13
        assert profile_kl <= fixed_kl+1e-13
        cases.append(dict(chosen_mass_number=a,chosen_level_gap_keV=gap,
                          upper_mass_keV=upper,lower_mass_keV=mass,
                          emitted_feeder_photon_keV=k,recoil_speed_in_parent_frame=u,
                          feeder_recoil_only_sigma_keV=math.sqrt(variance),
                          feeder_target_mean_in_parent_keV=mean,
                          mixed_Gaussian_convolved_sigma_keV=math.sqrt(var),
                          mixed_centroid_keV=mu,
                          fixed_response_KL_per_photon=max(0.,fixed_kl),
                          fitted_mean_sigma_KL_per_photon=max(0.,profile_kl),
                          profiled_KL_resolution_note='values below1e-12 are not numerically resolved physical significance',
                          expected2N_KL_fixed_response_for_chosen_N10000=2e4*max(0.,fixed_kl),
                          normalization_error=norm_error))

    # Independent two boosts at one lab direction, with an arbitrary first photon.
    mass,upper,k,daughter,u,gamma=recoil(20,1000.)
    n_feed=np.array([0.3,0.4,math.sqrt(0.75)])
    v_recoil=-u*n_feed
    parent_beta=0.1
    lab_angle=math.radians(150.)
    cos=math.cos(lab_angle)
    gp=1/math.sqrt(1-parent_beta**2)
    dp=gp*(1-parent_beta*cos)
    n_parent=np.array([math.sin(lab_angle)/dp,0,(cos-parent_beta)/(1-parent_beta*cos)])
    assert abs(n_parent@n_parent-1)<1e-14
    dr=gamma*(1-v_recoil@n_parent)
    photon_parent=np.r_[E0_KEV/dr,E0_KEV/dr*n_parent]
    photon_lower=boost(photon_parent,-v_recoil)
    photon_lab=boost(photon_parent,[0,0,parent_beta])
    assert abs(photon_lower[0]-E0_KEV)<1e-9
    assert abs(photon_lab[0]*dp-photon_parent[0])<1e-9
    assert abs(photon_lab[3]/photon_lab[0]-cos)<1e-13
    assert np.linalg.norm(daughter*v_recoil+k*n_feed)<1e-9
    energy_sum=daughter+k
    assert abs(energy_sum-upper)<1e-8
    # Independently sample first-photon orientations and apply angular importance weights.
    rng=np.random.default_rng(131423)
    cs=rng.uniform(-1,1,600000)
    ds=gamma*(1-u*cs)
    measured=E0_KEV/ds
    w=1/ds**2
    mean_mc=float(w@measured/w.sum())
    var_mc=float(w@((measured-mean_mc)**2)/w.sum())
    expected_mean=E0_KEV*gamma
    expected_var=(E0_KEV*gamma*u)**2/3
    se=math.sqrt(expected_var/len(cs))
    assert abs(mean_mc-expected_mean)<5*se and abs(var_mc/expected_var-1)<0.01
    assert recoil(20,0.)[-2]==0 and recoil(20,0.)[-1]==1
    assert recoil(200000000,1000.)[-2] < 1e-11
    assert np.max(np.abs(boost(photon_parent,[0,0,0])-photon_parent))==0
    return dict(schema_version=1,kind='synthetic cascade-recoil/response identifiability check',
                chosen_parameters=dict(target_rest_photon_keV=E0_KEV,corrected_Gaussian_sigma_keV=SIGMA_KEV,
                                       feed_fraction=FEED_FRACTION,constant_flight=True,
                                       isotropic_feeder_and_target_photons=True),
                cases=cases,
                frame_check=dict(parent_beta=parent_beta,chosen_lab_angle_deg=150,
                                 upper_photon_direction_in_parent=n_feed.tolist(),
                                 lower_frame_target_energy_keV=float(photon_lower[0]),
                                 parent_frame_target_energy_keV=float(photon_parent[0]),
                                 measured_lab_target_energy_keV=float(photon_lab[0]),
                                 parent_reference_corrected_target_keV=float(photon_lab[0]*dp)),
                independent_MC=dict(repetitions=len(cs),analytic_mean_keV=expected_mean,
                                    MC_mean_keV=mean_mc,mean_SE_keV=se,
                                    analytic_variance_keV2=expected_var,MC_variance_keV2=var_mc),
                verification=dict(two_body_mass_shell_and_energy_momentum_passed=True,
                                  scalar_aberration_and_nested_fourvector_passed=True,
                                  angular_normalization_and_moments_quad_passed=True,
                                  independent_angular_MC_passed=True,
                                  zero_gap_large_mass_and_zero_boost_limits_passed=True,
                                  energy_profile_and_KL_checks_passed=True,all_passed=True),
                boundaries=['This is chosen constant flight, not a slowed foil/cascade lifetime refit.',
                            'Parent-reference correction deliberately ignores the upper photon kick; a measured lower-emission vector is a different reference.',
                            'Mass proxies and gap/energy/response/fractions are not source state assignments.',
                            'Real cascade correlations, polarization/alignment, transport, tagging and response covariance may change the signature.',
                            'Expected2N*KL is exact-model design information, not an experimental p-value or confidence.',
                            'Profiled KL below1e-12 has a stated numerical boundary; no precision significance claim.'])


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    r=calculate()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(args.output),'verification':r['verification'],'cases':r['cases']}))


if __name__=='__main__':
    main()
