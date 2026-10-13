#!/usr/bin/env python3
"""Day13 two-distance Doppler-position design, under explicit Gaussian assumptions.

This uses a declared model W(R)^2=B^2+(k*p/R)^2, not the literal unsquared
Eq.(4.4) printed in arXiv:0812.0091v1. W and B are energy FWHM in keV,
p is one projected position FWHM in mm, R is the actual source-to-first-point
distance in mm, k is the angular sensitivity in keV/radian at the chosen angle.
Recoil/intrinsic baseline, p and k must transfer across geometries. All parameter
choices and Gaussian width-measurement covariances below are synthetic.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def width(distance, baseline, k, position):
    return np.sqrt(baseline**2 + (k * position / np.asarray(distance))**2)


def reconstruct(close, far, rc, rf, k):
    return (np.asarray(close)**2 - np.asarray(far)**2) / (k*k * (rc**-2-rf**-2))


def calculate():
    k, p_true, baseline = 70., 5., 3.
    rc, rf = 150., 235.
    wc, wf = map(float, width(np.array([rc, rf]), baseline, k, p_true))
    inferred2 = float(reconstruct(wc, wf, rc, rf, k))
    assert abs(inferred2-p_true**2) < 1e-12
    assert np.linalg.matrix_rank(np.array([[1.,rc**-2],[1.,rf**-2]])) == 2
    # The p uncertainty is linearised around an interior p>0 solution.
    denom = k*k * (rc**-2-rf**-2)
    jacobian_p = np.array([wc,-wf])/(denom*p_true)
    rng = np.random.default_rng(131015)
    errors = []
    for rho in (-.8,0.,.8):
        sigma_width = .02
        cov = sigma_width**2*np.array([[1.,rho],[rho,1.]])
        perturbations = rng.multivariate_normal([wc,wf],cov,size=250000)
        reconstructed2 = reconstruct(perturbations[:,0],perturbations[:,1],rc,rf,k)
        valid = reconstructed2 > 0
        assert np.mean(valid) > .999
        sigma = math.sqrt(float(jacobian_p@cov@jacobian_p))
        mc_sigma = float(np.std(np.sqrt(reconstructed2[valid])))
        assert abs(mc_sigma/sigma-1) < .01
        errors.append({"rho_width_errors":rho,"width_sigma_keV":sigma_width,
                       "position_sigma_linear_mm":sigma,"position_sigma_MC_mm":mc_sigma,
                       "fraction_negative_p2":float(np.mean(~valid))})
    # The front-face distance is not necessarily the first-interaction distance.
    front_c,front_f,depth = 40.,140.,30.
    depth_wc,depth_wf=map(float,width(np.array([front_c+depth,front_f+depth]),baseline,k,p_true))
    wrong_p=math.sqrt(float(reconstruct(depth_wc,depth_wf,front_c,front_f,k)))
    correct_p=math.sqrt(float(reconstruct(depth_wc,depth_wf,front_c+depth,front_f+depth,k)))
    assert abs(correct_p-p_true)<1e-12 and wrong_p<.65*p_true
    # Two points fit even a non-transferring baseline. A held-out third
    # geometry provides a failure check of the common-baseline model.
    changed_close=float(width(rc,3.3,k,p_true))
    changed_far=wf
    fitted_p2=float(reconstruct(changed_close,changed_far,rc,rf,k))
    fitted_baseline2=changed_far**2-k*k*fitted_p2/rf**2
    third=200.
    predicted_third=math.sqrt(fitted_baseline2+k*k*fitted_p2/third**2)
    actual_third=float(width(third,baseline,k,p_true))
    assert abs(predicted_third-actual_third)>.05
    # Near distances have low leverage: the physical constraint must be
    # reported, not silently replaced with p=0 after clipping a noisy p^2.
    near_c,near_f=220.,235.
    near_wc,near_wf=map(float,width(np.array([near_c,near_f]),baseline,k,p_true))
    noisy=rng.normal([near_wc,near_wf],.05,size=(250000,2))
    near_p2=reconstruct(noisy[:,0],noisy[:,1],near_c,near_f,k)
    negative_fraction=float(np.mean(near_p2<0))
    assert negative_fraction>.1
    # Finite differences verify the interior propagation Jacobian.
    numeric=[]
    for j in (0,1):
        plus=np.array([wc,wf]);minus=plus.copy();step=1e-5
        plus[j]+=step;minus[j]-=step
        numeric.append((math.sqrt(float(reconstruct(*plus,rc,rf,k)))-
                        math.sqrt(float(reconstruct(*minus,rc,rf,k))))/(2*step))
    max_jac_error=float(np.max(np.abs(np.array(numeric)-jacobian_p)))
    assert max_jac_error<1e-7
    return {"schema_version":1,"kind":"synthetic two-distance design and counterexamples; no source refit",
            "formula_boundary":"own squared-variance derivation; literal source Eq4.4 is preserved and not executed",
            "ideal_model":{"k_keV_per_radian":k,"position_FWHM_mm":p_true,"baseline_FWHM_keV":baseline,
                           "distances_mm":[rc,rf],"widths_FWHM_keV":[wc,wf],
                           "reconstructed_position_FWHM_mm":math.sqrt(inferred2)},
            "width_covariance_examples":errors,
            "first_point_distance_counterexample":{"front_distances_mm":[front_c,front_f],
                                                   "self_chosen_depth_mm":depth,
                                                   "wrong_front_distance_inference_mm":wrong_p,
                                                   "correct_first_point_inference_mm":correct_p},
            "non_transferring_baseline_counterexample":{"close_baseline_FWHM_keV":3.3,
                                                      "far_and_heldout_baseline_FWHM_keV":3.,
                                                      "two_point_fitted_position_FWHM_mm":math.sqrt(fitted_p2),
                                                      "heldout_distance_mm":third,"heldout_predicted_FWHM_keV":predicted_third,
                                                      "heldout_actual_FWHM_keV":actual_third},
            "small_leverage_example":{"distances_mm":[near_c,near_f],"width_sigma_keV":.05,
                                      "negative_position_variance_fraction":negative_fraction,
                                      "boundary":"Gaussian measurement toy; do not clip negative estimates into a claimed p=0 measurement"},
            "verification":{"ideal_reconstruction_passed":True,"width_Jacobian_finite_difference_max_error":max_jac_error,
                            "covariance_MC_passed":True,"first_point_geometry_counterexample_passed":True,
                            "heldout_geometry_counterexample_passed":True,"physical_boundary_checked":True,"passed":True},
            "numpy_version":np.__version__}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=calculate();args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(args.output),'verification':result['verification'],
                     'first_point':result['first_point_distance_counterexample'],
                     'small_leverage':result['small_leverage_example']}))


if __name__=='__main__':
    main()
