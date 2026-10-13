#!/usr/bin/env python3
"""Day13 conditional magnetic-rigidity velocity and PID-branch exercise.

Use the AS21 mass-number constant3.107 in beta*gamma=Brho*q/(3.107*A).
The source's unlabelled .2% resolutions are not silently Gaussian sigmas:
this fixture explicitly chooses both fractional design sigmas=.002 and a
7m path. No actual ion PID confusion matrix or data is fitted.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


C_MM_NS=299.792458
RIGIDITY_CONSTANT=3.107


def beta_from_rigidity(rigidity,a,q):
    x=np.asarray(rigidity)*q/(RIGIDITY_CONSTANT*a)
    return x/np.sqrt(1+x*x)


def flight(length,rigidity,a,q):
    return np.asarray(length)/(C_MM_NS*beta_from_rigidity(rigidity,a,q))


def calculate():
    a,q,beta0,length=20.,8.,.126,7000.
    gamma0=1/math.sqrt(1-beta0*beta0)
    rigidity=RIGIDITY_CONSTANT*a/q*beta0*gamma0
    assert abs(float(beta_from_rigidity(rigidity,a,q))-beta0)<1e-12
    derivative=beta0*(1-beta0*beta0)/rigidity
    step=1e-6
    finite=float((beta_from_rigidity(rigidity+step,a,q)-beta_from_rigidity(rigidity-step,a,q))/(2*step))
    assert abs(finite-derivative)<1e-9
    true_flight=float(flight(length,rigidity,a,q))
    jacobian=np.array([true_flight/length,-true_flight*(1-beta0*beta0)/rigidity])
    rng=np.random.default_rng(131022);samples=250000;covariance_cases=[];max_relative=0.
    design_sigmas=np.array([.002*length,.002*rigidity])
    for rho in (-.8,0.,.8):
        cov=np.outer(design_sigmas,design_sigmas)*np.array([[1.,rho],[rho,1.]])
        linear_sigma=math.sqrt(float(jacobian@cov@jacobian))
        perturbed=rng.multivariate_normal([length,rigidity],cov,size=samples)
        simulated=flight(perturbed[:,0],perturbed[:,1],a,q)
        mc_sigma=float(np.std(simulated));relative=abs(mc_sigma/linear_sigma-1);max_relative=max(max_relative,relative)
        covariance_cases.append({'rho_path_rigidity':rho,'linear_flight_sigma_ns':linear_sigma,
                                 'MC_flight_sigma_ns':mc_sigma,'relative_difference':relative,
                                 'boundary':'both design sigmas=.002 relative are explicitly chosen, not known source sigma conventions'})
    # Conditional branches under otherwise identical Brho. All chosen charge
    # states satisfy q<=Z=8, but known reaction/energy constraints can reject
    # some mass alternatives; no occurrence probabilities are assigned.
    rest_gamma=1673.;angles=(35.,90.,145.);branches=[]
    for assumed_a,assumed_q in ((20.,8.),(19.,8.),(21.,8.),(20.,7.)):
        beta=float(beta_from_rigidity(rigidity,assumed_a,assumed_q))
        gamma=1/math.sqrt(1-beta*beta)
        residuals=[]
        for theta in angles:
            cosine=math.cos(math.radians(theta))
            lab=rest_gamma/(gamma0*(1-beta0*cosine))
            corrected=lab*gamma*(1-beta*cosine)
            residuals.append({'lab_photon_angle_deg':theta,'corrected_gamma_residual_keV':corrected-rest_gamma})
        branches.append({'assumed_A':assumed_a,'assumed_q':assumed_q,'conditional_beta':beta,
                         'flight_ns_for_same_path':float(flight(length,rigidity,assumed_a,assumed_q)),
                         'gamma_residuals':residuals,'boundary':'hypothetical label branch, not actual source misidentification'})
    assert max(abs(x['corrected_gamma_residual_keV']) for x in branches[0]['gamma_residuals'])<1e-9
    assert max(abs(x['corrected_gamma_residual_keV']) for x in branches[3]['gamma_residuals'])>10
    assert max_relative<.008
    return {'schema_version':1,'kind':'synthetic fixed-integer rigidity/path covariance and alternate-PID fixture',
            'parameters':{'true_A':a,'true_q':q,'true_beta':beta0,'self_chosen_path_mm':length,
                          'computed_Brho_Tm':rigidity,'true_flight_ns':true_flight,'rest_gamma_keV_source_inspired_scale':rest_gamma,
                          'source_resolution_convention':'AS21 .2% is not explicitly sigma/FWHM; chosen design sigmas=.002 in this fixture'},
            'rigidity_relative_beta_sensitivity':1-beta0*beta0,
            'flight_path_rigidity_covariance_cases':covariance_cases,'alternate_integer_PID_branches':branches,
            'verification':{'rigidity_beta_derivative_FD_error':abs(finite-derivative),
                            'covariance_MC_max_relative_difference':max_relative,
                            'correct_PID_energy_inverse_passed':True,
                            'wrong_integer_branch_counterexamples_passed':True,'passed':True},
            'boundaries':['No actual target path, ion-mass precision, energy loss, stage correction or calibration is supplied.',
                          'Integer labels reduce uncertainty conditional on a correct assignment; they do not independently validate the assignment.',
                          'Independent two-body reaction constraints or known gamma lines can reject alternate branches.',
                          'Actual inferred light TOF also needs measured time-difference and its clock/walk covariance.'],
            'numpy_version':np.__version__}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=calculate()
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(a.output),'verification':r['verification'],
                     'flight_sigmas_ns':[c['linear_flight_sigma_ns'] for c in r['flight_path_rigidity_covariance_cases']],
                     'beta_branches':[c['conditional_beta'] for c in r['alternate_integer_PID_branches']]}))


if __name__=='__main__':
    main()
