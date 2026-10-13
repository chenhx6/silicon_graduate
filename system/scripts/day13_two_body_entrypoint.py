#!/usr/bin/env python3
"""Day13 exact synthetic binary reaction and cascade-stage fixture.

Mbeam=19u, deuteron/proton rest masses, and a self-chosen ground-state Q5.4MeV
define consistent synthetic heavy masses. BeamT152MeV and excitation scales
1.673/3.570MeV are inspired by AS21 but are not an actual19O/20O mass model.
No Au backing, target loss, beam spot, response or measured dataset is included.
All gamma four-vectors obey free two-body mass shells. A forced wrong entry
mass is an illustrative hypothesis, not an accusation about source analysis.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import brentq


U_MEV=931.49410242
MB=19*U_MEV
MD=1875.61294257
MP=938.27208816
CHOSEN_Q=5.4
MH_GROUND=MB+MD-MP-CHOSEN_Q


def invariant_mass(p4):
    return np.sqrt(p4[...,0]**2-np.sum(p4[...,1:]**2,axis=-1))


def initial(beam_t):
    beam_t=np.asarray(beam_t);energy=MB+beam_t+MD
    momentum=np.sqrt(beam_t*(beam_t+2*MB))
    return np.stack((energy,np.zeros_like(beam_t),np.zeros_like(beam_t),momentum),axis=-1)


def light(t,theta,phi):
    t,theta,phi=np.broadcast_arrays(t,theta,phi)
    momentum=np.sqrt(t*(t+2*MP))
    return np.stack((MP+t,momentum*np.sin(theta)*np.cos(phi),momentum*np.sin(theta)*np.sin(phi),momentum*np.cos(theta)),axis=-1)


def heavy(inputs):
    x=np.asarray(inputs)
    return initial(x[...,0])-light(x[...,1],x[...,2],x[...,3])


def light_solution(beam_t,excitation,theta,phi=0.):
    pi=initial(beam_t);target_mass=MH_GROUND+excitation
    # Rearranged invariant equation avoids subtracting two nearly equal
    # large invariant masses repeatedly inside the root search.
    s=float(pi[0]**2-pi[3]**2)
    constant=(s+MP*MP-target_mass*target_mass)/2
    residual=lambda p:pi[0]*math.hypot(MP,p)-pi[3]*p*math.cos(theta)-constant
    momentum=brentq(residual,0.,2000.,xtol=1e-10)
    t=momentum*momentum/(math.hypot(MP,momentum)+MP)
    x=np.array([beam_t,t,theta,phi]);ph=heavy(x)
    assert abs(float(invariant_mass(ph))-target_mass)<1e-8
    return x,ph


def emit_gamma(parent,final_mass,lab_direction):
    mi=float(invariant_mass(parent));rest=(mi-final_mass)*(mi+final_mass)/(2*mi)
    beta=parent[1:]/parent[0];gamma=parent[0]/mi
    lab_energy=rest/(gamma*(1-float(beta@lab_direction)))
    photon=np.concatenate(([lab_energy],lab_energy*lab_direction))
    daughter=parent-photon
    assert abs(float(invariant_mass(daughter))-final_mass)<1e-8
    return photon,daughter,rest


def inverse_energy(photon,parent):
    mass=float(invariant_mass(parent));beta=parent[1:]/parent[0]
    return parent[0]/mass*(photon[0]-float(beta@photon[1:]))


def calculate():
    beam_t=152.;low_ex,high_ex=1.673,3.570
    gamma_direction=np.array([math.sin(math.radians(145)),0.,math.cos(math.radians(145))])
    cases=[];max_conservation=0.
    for theta_deg in (120.,150.,170.):
        x,parent=light_solution(beam_t,low_ex,math.radians(theta_deg))
        photon,terminal,rest=emit_gamma(parent,MH_GROUND,gamma_direction)
        recovered=inverse_energy(photon,parent)
        beam_velocity=initial(beam_t)[3]/(MB+beam_t)
        beam_corrected=1/math.sqrt(1-beam_velocity*beam_velocity)*(photon[0]-beam_velocity*photon[3])
        max_conservation=max(max_conservation,float(np.max(np.abs(initial(beam_t)-light(x[1],x[2],x[3])-photon-terminal))))
        assert abs(recovered-rest)<1e-10
        cases.append({'self_chosen_light_angle_deg':theta_deg,'predicted_light_T_MeV':float(x[1]),
                      'reconstructed_entry_excitation_MeV':float(invariant_mass(parent)-MH_GROUND),
                      'true_postreaction_beta_vector':(parent[1:]/parent[0]).tolist(),
                      'true_direct_rest_gamma_MeV':rest,'photon_lab_MeV':float(photon[0]),
                      'nominal_beam_velocity_correction_residual_keV':(beam_corrected-rest)*1000})
    # Shared input-error fixture at theta150. These sigmas are deliberately
    # chosen and independent, not inferred from AS21 resolution labels.
    x,parent=light_solution(beam_t,low_ex,math.radians(150.))
    photon,_,rest=emit_gamma(parent,MH_GROUND,gamma_direction)
    sigmas=np.array([.1,.01,math.radians(.1),math.radians(.1)])
    covariance=np.diag(sigmas**2);jacobian=[]
    for i in range(4):
        step=1e-4 if i<2 else 1e-5;plus=x.copy();minus=x.copy();plus[i]+=step;minus[i]-=step
        jacobian.append((inverse_energy(photon,heavy(plus))-inverse_energy(photon,heavy(minus)))/(2*step))
    jacobian=np.array(jacobian);sigma_gamma=math.sqrt(float(jacobian@covariance@jacobian))*1000
    rng=np.random.default_rng(131023);draws=rng.multivariate_normal(x,covariance,size=250000)
    hp=heavy(draws);hm=invariant_mass(hp);b=hp[:,1:]/hp[:,0,None]
    corrected=hp[:,0]/hm*(photon[0]-b@photon[1:])
    mc_sigma=float(np.std(corrected))*1000
    assert abs(mc_sigma/sigma_gamma-1)<.01
    # High entry emits an unobserved feeding gamma before the observed lower
    # gamma. Exact gamma recoil is retained rather than forcing a common beta.
    hx,entry=light_solution(beam_t,high_ex,math.radians(150.))
    feeding,low_parent,feeding_rest=emit_gamma(entry,MH_GROUND+low_ex,np.array([0.,1.,0.]))
    observed,terminal,low_rest=emit_gamma(low_parent,MH_GROUND,gamma_direction)
    assert abs(inverse_energy(observed,low_parent)-low_rest)<1e-10
    prefeed_residual=(inverse_energy(observed,entry)-low_rest)*1000
    # Force the low mass to be the reaction entry despite this feeding path.
    # This can be made algebraically consistent by changing beam energy.
    # The missing-mass curve is not monotonic over [0,beam_t]. For this
    # backward-light fixture d(MH^2)/dT=2[(Md-El)+p_l cos(theta)/beta_beam],
    # so its analytic minimum separates two root brackets. A single endpoint
    # sign check missed both roots in the initial attempt; preserve both here.
    light_momentum=math.sqrt(hx[1]*(hx[1]+2*MP))
    minimum_beam_beta=-light_momentum*math.cos(hx[2])/(MD-(MP+hx[1]))
    assert 0<minimum_beam_beta<1
    minimum_beam_t=MB*(1/math.sqrt(1-minimum_beam_beta**2)-1)
    constraint=lambda t:float(invariant_mass(initial(t)-light(hx[1],hx[2],hx[3])))-(MH_GROUND+low_ex)
    assert constraint(0)>0 and constraint(minimum_beam_t)<0 and constraint(beam_t)>0
    forced_hypotheses=[]
    for left,right in ((0.,minimum_beam_t),(minimum_beam_t,beam_t)):
        forced_beam=brentq(constraint,left,right)
        forced_entry=initial(forced_beam)-light(hx[1],hx[2],hx[3])
        wrong_residual=(inverse_energy(observed,forced_entry)-low_rest)*1000
        assert abs(float(invariant_mass(forced_entry))-(MH_GROUND+low_ex))<1e-8
        assert abs(forced_beam-beam_t)>10 and abs(wrong_residual)>10
        forced_hypotheses.append({'forced_beam_T_MeV':forced_beam,
                                  'forced_entry_gamma_residual_keV':wrong_residual})
    assert np.max(np.abs(entry-feeding-observed-terminal))<1e-8
    return {'schema_version':1,'kind':'synthetic exact binary-reaction and feeding-stage exercise; no source refit',
            'mass_parameters_MeV':{'beam_19u':MB,'deuteron':MD,'proton':MP,'self_chosen_Q':CHOSEN_Q,'synthetic_heavy_ground':MH_GROUND},
            'direct_entry_cases':cases,
            'self_chosen_input_covariance_fixture':{'input_order':['beam_T_MeV','light_T_MeV','theta_rad','phi_rad'],
                                                     'sigmas':sigmas.tolist(),'gamma_Jacobian_MeV_per_input_unit':jacobian.tolist(),
                                                     'predicted_rest_gamma_sigma_keV':sigma_gamma,'MC_rest_gamma_sigma_keV':mc_sigma,
                                                     'boundary':'no target loss/beamspot/PSA history; does not explain measured7.1keV width'},
            'feeding_entry_counterexample':{'true_entry_excitation_MeV':high_ex,'lower_emitting_excitation_MeV':low_ex,
                                             'feeding_rest_gamma_MeV':feeding_rest,'observed_lower_rest_gamma_MeV':low_rest,
                                             'using_prefeeding_reaction_vector_residual_keV':prefeed_residual,
                                             'forced_wrong_entry_solutions':forced_hypotheses,'actual_self_chosen_beam_T_MeV':beam_t,
                                             'mass_constraint_curve_minimum_beam_T_MeV':minimum_beam_t,
                                             'boundary':'synthetic path; knownbeam/missingmass/observedfeeding can reject this forced entry hypothesis'},
            'verification':{'binary_and_gamma_mass_shells_passed':True,'staged_four_momentum_conservation_passed':True,
                            'max_direct_four_momentum_residual_MeV':max_conservation,
                            'correct_emitter_inverse_passed':True,'self_chosen_covariance_MC_passed':True,
                            'both_global_wrong_entry_roots_retained':True,
                            'wrong_entry_hypothesis_counterexample_passed':True,'passed':True},
            'boundaries':['19u/Q5.4 defines a consistent synthetic reaction, not actual isotope masses.',
                          'A known lower gamma does not by itself identify the reaction entry or all prior feeding.',
                          'Raw channels/beam/target/backing/particle/PSA/response/covariance are required for a real analysis.',
                          'No actual source branch, lifetime, strength or misidentified reaction is asserted.'],
            'numpy_version':np.__version__}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=calculate()
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(a.output),'verification':r['verification'],
                     'feeding_counterexample':r['feeding_entry_counterexample'],
                     'covariance':r['self_chosen_input_covariance_fixture']}))


if __name__=='__main__':
    main()
