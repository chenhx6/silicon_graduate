#!/usr/bin/env python3
"""Day13 ideal fixed-detector arrival-time/energy kinematics.

Constant beta along +z, isotropic rest emission, exponential proper lifetime,
an infinitesimal planar detector facing the nominal source, and known prompt
flight reference are declared. No actual clock response or lifetime is fitted.
The time-jitter convolution is self-chosen and independent, not SY14 timing.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.laguerre import laggauss
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import ndtr


C_MM_PS=.299792458


def state(t,beta,radius,theta_deg):
    gamma=1/math.sqrt(1-beta*beta);cos0=math.cos(math.radians(theta_deg))
    distance_z=beta*gamma*C_MM_PS*np.asarray(t)
    path=np.sqrt(radius*radius+distance_z*distance_z-2*radius*distance_z*cos0)
    cos_true=(radius*cos0-distance_z)/path
    arrival=gamma*np.asarray(t)+(path-radius)/C_MM_PS
    slope=gamma*(1-beta*cos_true)
    projection=np.maximum(0.,(radius-distance_z*cos0)/path)
    detection=(1-beta*beta)/(1-beta*cos_true)**2*projection*radius**2/path**2
    return arrival,slope,detection


def conditional(beta,radius,angle,tau,gate,jitter,order):
    nodes,weights=laggauss(order);time=nodes*tau
    arrival,slope,detected=state(time,beta,radius,angle)
    weighted=weights*detected;norm=float(np.sum(weighted))
    mean=float(np.sum(weighted*arrival)/norm)
    if jitter>0:
        selected=float(np.sum(weighted*ndtr((gate-arrival)/jitter))/norm)
    else:
        # Exact monotonic time mapping sets the upper integration boundary;
        # avoid approximating an abrupt gate by a Gaussian quadrature step.
        cut=brentq(lambda t:float(state(t,beta,radius,angle)[0])-gate,0.,10*gate+100*tau)
        selected=quad(lambda t:math.exp(-t/tau)*float(state(t,beta,radius,angle)[2])/tau,
                      0.,cut,epsabs=1e-11)[0]/norm
    return mean,selected,norm


def calculate():
    rows=[];max_quad=0.;max_slope_error=0.;max_MC=0.;max_energy_slope_error=0.
    rng=np.random.default_rng(131020);samples=400000;tau,gate=10.,10.
    times=rng.exponential(tau,samples)
    for beta,radius in ((.07,235.),(.3,150.),(.5,150.)):
        for angle in (35.,90.,145.):
            gamma=1/math.sqrt(1-beta*beta);d0=gamma*(1-beta*math.cos(math.radians(angle)))
            mean48,p48,norm48=conditional(beta,radius,angle,tau,gate,0.,48)
            mean96,p96,norm96=conditional(beta,radius,angle,tau,gate,0.,96)
            jitter_mean,jitter_p,_=conditional(beta,radius,angle,tau,gate,1000.,96)
            max_quad=max(max_quad,abs(mean48-mean96),abs(p48-p96),abs(norm48-norm96))
            arrival,slope,detected=state(times,beta,radius,angle)
            mc_mean=float(np.sum(detected*arrival)/np.sum(detected))
            mc_gate=float(np.sum(detected*(arrival<gate))/np.sum(detected))
            max_MC=max(max_MC,abs(mc_mean/mean96-1),abs(mc_gate-p96))
            for t in (0.,1.,10.,50.):
                step=1e-3
                # Symmetric derivative of the mathematical path map includes
                # small negative t around zero, not physical negative decays.
                num=(state(t+step,beta,radius,angle)[0]-state(t-step,beta,radius,angle)[0])/(2*step)
                expected=state(t,beta,radius,angle)[1]
                max_slope_error=max(max_slope_error,abs(float(num-expected)))
                # Independent route: transform a rest-frame photon whose
                # direction aberrates into the instantaneous lab line of sight.
                displacement=beta*gamma*C_MM_PS*t
                cosine0=math.cos(math.radians(angle))
                path=math.sqrt(radius**2+displacement**2-2*radius*displacement*cosine0)
                cosine_lab=(radius*cosine0-displacement)/path
                cosine_rest=(cosine_lab-beta)/(1-beta*cosine_lab)
                energy_lab=gamma*1000*(1+beta*cosine_rest)
                energy_slope_error=abs(float(energy_lab*num)-1000)
                max_energy_slope_error=max(max_energy_slope_error,energy_slope_error)
                assert energy_slope_error<1e-7
            far_mean,far_gate,_=conditional(beta,1e6,angle,tau,gate,0.,96)
            far_pred_mean=d0*tau;far_pred_gate=1-math.exp(-gate/(d0*tau))
            assert abs(far_mean-far_pred_mean)<1e-4 and abs(far_gate-far_pred_gate)<1e-5
            rows.append({'beta':beta,'first_point_radius_mm':radius,'nominal_angle_deg':angle,
                         'proper_tau_ps':tau,'lab_emission_tau_ps':gamma*tau,
                         'far_arrival_scale_D':d0,'far_arrival_mean_ps':far_pred_mean,
                         'exact_detected_arrival_mean_ps':mean96,'MC_detected_arrival_mean_ps':mc_mean,
                         'ideal_arrival_gate_ps':gate,'far_ideal_gate_fraction':far_pred_gate,
                         'exact_detected_ideal_gate_fraction':p96,'MC_detected_ideal_gate_fraction':mc_gate,
                         'self_chosen_1000ps_Gaussian_jitter_gate_fraction':jitter_p,
                         'relative_detector_weight_integral':norm96})
    static_mean,static_gate,_=conditional(0.,150.,90.,tau,gate,0.,96)
    assert abs(static_mean-tau)<1e-10 and abs(static_gate-(1-math.exp(-gate/tau)))<1e-10
    assert max_quad<1e-7 and max_slope_error<1e-7 and max_MC<.008
    return {'schema_version':1,'kind':'synthetic retarded-time/energy fixed-detector model; no timing measurement',
            'rows':rows,'verification':{'quadrature48_96_max_absolute_difference':max_quad,
                                      'arrival_derivative_finite_difference_max_error':max_slope_error,
                                      'boosted_photon_times_numeric_arrival_slope_max_error_keV':max_energy_slope_error,
                                      'energy_times_proper_to_arrival_derivative_equals_rest_energy':True,
                                      'far_detector_linear_time_gate_limit_passed':True,
                                      'static_emission_arrival_limit_passed':True,
                                      'detected_moment_and_gate_MC_max_difference':max_MC,'passed':True},
            'boundaries':['Arrival time subtracts the known prompt photon flight reference, not a measured nuclear lifetime.',
                          'Jitter1000ps is self-chosen, not an actual instrument timing value.',
                          'Real start/flightpath/walk/jitter/particle gates, stopping and feeding require a separate packet.',
                          'These ideal picosecond fractions do not establish resolvable lifetime information for SY14 ns TOF.'],
            'numpy_version':np.__version__}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=calculate()
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(a.output),'verification':r['verification'],
                     'beta0_3_rows':[x for x in r['rows'] if x['beta']==.3]}))


if __name__=='__main__':
    main()
