#!/usr/bin/env python3
"""Finish DAY13 long-control applicability: vertex and parent/daughter frame.

Reuses previously verified displacement/recoil relationships at the selected
control scales. Isolates each omitted effect; does not add them as an actual
calibration prediction or reproduce the source's transport/estimator.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.laguerre import laggauss
from scipy.optimize import brentq

import day13_doppler_displaced_vertex as vertex
import day13_photon_recoil_width as recoil
import day13_long_control_velocity_estimator as control


def displaced_mode(e0, tau, angle, radius=150.0, order=96):
    nodes, weights=laggauss(order)
    beta=control.TRUE_BETA_EXIT
    gamma=1/math.sqrt(1-beta**2)
    theta=math.radians(angle)
    nominal_cosine=math.cos(theta)
    travel=beta*gamma*vertex.C_MM_PER_PS*tau*nodes
    distance=np.sqrt(radius**2+travel**2-2*radius*travel*nominal_cosine)
    cosine=(radius*nominal_cosine-travel)/distance
    actual_d=(1-beta*cosine)*gamma
    reference_d=(1-beta*nominal_cosine)*gamma
    residual=e0*(reference_d/actual_d-1)
    projected_area=np.maximum(0,(radius-travel*nominal_cosine)/distance)
    detected=weights/actual_d**2*projected_area*radius**2/distance**2
    detected/=detected.sum()
    # Work in residual coordinates, avoiding a large-E absolute tolerance.
    sigma=control.LAB_GAUSSIAN_SIGMA_KEV*reference_d
    def density(value):
        g=np.exp(-.5*((value-residual)/sigma)**2)
        return float(detected @ g)/(math.sqrt(2*math.pi)*sigma)
    def score(value):
        offset=value-residual
        g=np.exp(-.5*(offset/sigma)**2)
        return float(detected @ (-offset*g/sigma**2))/(math.sqrt(2*math.pi)*sigma)
    mode=brentq(score,-3*sigma,3*sigma,xtol=1e-12)
    assert abs(score(mode))<1e-10
    assert density(mode)>=max(density(x)for x in np.linspace(-3*sigma,3*sigma,601))-1e-10
    assert np.max(np.abs((e0/actual_d)*actual_d-e0))<1e-10
    return float(detected @ residual),mode


def calculate():
    geometry=[]
    mode_order_error=mean_order_error=0.0
    for e0,tau in control.CONTROLS:
        angle=150.0
        prior=vertex.moments(control.TRUE_BETA_EXIT,150.0,angle,tau,order=96)
        mean,mode=displaced_mode(e0,tau,angle,order=96)
        alternate_mean,alternate_mode=displaced_mode(e0,tau,angle,order=128)
        expected=prior['mean_residual_detected_keV']*e0/1000
        assert abs(mean-expected)<1e-10
        mean_order_error=max(mean_order_error,abs(mean-alternate_mean))
        mode_order_error=max(mode_order_error,abs(mode-alternate_mode))
        geometry.append(dict(control_rest_gamma_keV=e0,context_tau_ps=tau,
                             chosen_parent_late_beta=control.TRUE_BETA_EXIT,
                             chosen_point_radius_mm=150.0,nominal_angle_deg=angle,
                             unconditional_mean_lab_travel_mm=prior['mean_flight_mm_unconditional'],
                             wrong_target_vertex_corrected_mean_residual_keV=mean,
                             wrong_target_vertex_corrected_mode_residual_keV=mode,
                             correctly_known_vertex_signal_residual_keV=0.0))
    assert mean_order_error<1e-8 and mode_order_error<1e-8
    assert abs(vertex.moments(0,150,150,12.4)['mean_residual_detected_keV'])<1e-12
    assert abs(vertex.moments(.09,1e12,150,12.4)['mean_residual_detected_keV'])<1e-7

    frames=[]
    conservation_error=frame_inverse_error=0.0
    for a,e0 in ((19,1375.80),(13,3853.170)):
        mf=a*recoil.U_MEV
        energy=e0/1000
        # Given parent-rest photon energy, solve the mass gap stably.
        gap=energy+energy**2/(math.hypot(mf,energy)+mf)
        mi=mf+gap
        daughter_rest_energy=mi-energy
        difference_keV=1000*energy*gap/mf
        for beta in (0.0,.09,.126):
            for theta_deg in (0.0,90.0,180.0):
                theta=math.radians(theta_deg)
                photon_p=energy*np.array([math.sin(theta),0,math.cos(theta)])
                ep,pp=recoil.boost_z(mi,np.zeros(3),beta)
                eg,pg=recoil.boost_z(energy,photon_p,beta)
                ef,pf=recoil.boost_z(daughter_rest_energy,-photon_p,beta)
                conservation_error=max(conservation_error,abs(ep-eg-ef),float(np.max(np.abs(pp-pg-pf))))
                parent_corrected=(eg-beta*pg[2])/math.sqrt(1-beta**2)
                daughter_corrected=(ef*eg-pf@pg)/mf
                frame_inverse_error=max(frame_inverse_error,abs(parent_corrected-energy),
                                        abs(daughter_corrected-energy*mi/mf))
        frames.append(dict(chosen_mass_proxy_A=a,context_parent_rest_photon_keV=e0,
                           daughter_ground_mass_proxy_MeV=mf,implied_mass_gap_keV=gap*1000,
                           daughter_frame_minus_parent_frame_keV=difference_keV))
    assert conservation_error<1e-9 and frame_inverse_error<1e-9
    return dict(schema_version=1,kind='dependent calibration applicability audit; no new experimental inputs',
                independent_evidence=False,
                displaced_vertex_controls=geometry,parent_daughter_frame_controls=frames,
                verification=dict(geometry_mean_quad96_128_difference_keV=mean_order_error,
                                  geometry_mode_quad96_128_difference_keV=mode_order_error,
                                  source_frame_fourmomentum_max_residual_MeV=conservation_error,
                                  frame_inverse_max_error_MeV=frame_inverse_error,
                                  known_vertex_zero_signal_error_passed=True,
                                  static_and_far_detector_limits_passed=True,all_passed=True),
                dependencies={name:hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest()
                              for name,module in [('vertex_script',vertex),('recoil_script',recoil),('control_script',control)]},
                boundaries=['Constant late-parentbeta/no-stopping displacement fixture isolates geometry; it is not the full preceding finite-history fixture.',
                            'Point planar detectorR150mm and true-relative direction are chosen, not CM21 geometry or PSA/vertex data.',
                            'Frame fixture is an ideal free single-gamma decay with mass-number proxy, not an actual VAMOS delayed/transported residue.',
                            'Displacement, recoil, finite history and source-fit objective are not combined into a real calibration correction.',
                            'Prior fixed-angle mean/mode comparison is conditional on its geometry/reference assumptions.',
                            'Actual production treatment of these effects is unknown; no source pipeline error is claimed.'])


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    result=calculate()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__=='__main__':
    main()
