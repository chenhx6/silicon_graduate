#!/usr/bin/env python3
"""Day13 Cartesian energy/velocity/vertex/first-point error propagation.

Inputs are (E_lab[keV], beta_x/y/z, vertex_x/y/z[mm], firstIP_x/y/z[mm]).
The full 10x10 covariance is self-chosen, not measured source covariance.
Common coordinate-origin and rotation invariances differ from physical target
or detector displacements; the latter need not cancel.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def corrected(x):
    x=np.asarray(x);e=x[...,0];b=x[...,1:4];r=x[...,7:10]-x[...,4:7]
    n=r/np.linalg.norm(r,axis=-1)[...,None]
    gamma=1/np.sqrt(1-np.sum(b*b,axis=-1))
    return e*gamma*(1-np.sum(b*n,axis=-1))


def jacobian(x):
    e=x[0];b=x[1:4];r=x[7:10]-x[4:7];distance=np.linalg.norm(r);n=r/distance
    gamma=1/math.sqrt(1-float(b@b));bn=float(b@n)
    db=e*(gamma**3*b*(1-bn)-gamma*n)
    dr=-e*gamma*(b-float(b@n)*n)/distance
    return np.concatenate(([gamma*(1-bn)],db,-dr,dr))


def calculate():
    rng=np.random.default_rng(131018);samples=250000;theta=math.radians(35);radius=235.
    sigmas=np.array([1.,.0005,.0005,.002,.3,.3,.3,2.12,2.12,2.12])
    covariance=np.diag(sigmas**2)
    covariance[3,4]=covariance[4,3]=-.6*sigmas[3]*sigmas[4]
    assert np.linalg.eigvalsh(covariance).min()>0
    cases=[];max_derivative_error=0.;max_MC_difference=0.
    for beta in (0.,.07,.3):
        e=1000*math.sqrt(1-beta*beta)/(1-beta*math.cos(theta))
        x=np.array([e,0.,0.,beta,0.,0.,0.,radius*math.sin(theta),0.,radius*math.cos(theta)])
        j=jacobian(x);finite=[]
        for i in range(10):
            step=1e-7 if 1<=i<=3 else 1e-3
            plus=x.copy();minus=x.copy();plus[i]+=step;minus[i]-=step
            finite.append((corrected(plus)-corrected(minus))/(2*step))
        derivative_error=float(np.max(np.abs(np.array(finite)-j)))
        max_derivative_error=max(max_derivative_error,derivative_error)
        sigma=math.sqrt(float(j@covariance@j))
        perturbed=rng.multivariate_normal(x,covariance,size=samples)
        energies=corrected(perturbed);mc_sigma=float(np.std(energies));relative=abs(mc_sigma/sigma-1)
        max_MC_difference=max(max_MC_difference,relative)
        # Origin shift is the same vector added to vertex and first-IP.
        translation=np.array([20.,-30.,50.]);same_frame=x.copy();same_frame[4:7]+=translation;same_frame[7:10]+=translation
        assert abs(corrected(same_frame)-corrected(x))<1e-10
        origin_cov=np.zeros((10,10));common=np.zeros((10,3));common[4:7,:]=np.eye(3);common[7:10,:]=np.eye(3)
        origin_cov=10**2*common@common.T
        common_change=float(j@origin_cov@j)
        independent_wrong=10**2*float(j[4:]@j[4:])
        assert abs(common_change)<1e-10
        # A physical target displacement changes vertex alone and is not a
        # coordinate-origin change; show a declared 1-mm transverse shift.
        physical=x.copy();physical[4]+=1.
        physical_residual=float(corrected(physical)-corrected(x))
        angle=.6;rotation=np.array([[math.cos(angle),-math.sin(angle),0.],[math.sin(angle),math.cos(angle),0.],[0.,0.,1.]])
        rotated=x.copy();rotated[1:4]=rotation@x[1:4];rotated[4:7]=rotation@x[4:7];rotated[7:10]=rotation@x[7:10]
        assert abs(corrected(rotated)-corrected(x))<1e-10
        n=(x[7:10]-x[4:7])/radius
        assert abs(float(j[7:10]@n))<1e-12
        # At nonzero beta, scalar coordinates beta/theta give the same
        # longitudinal speed derivative as the Cartesian z derivative.
        gamma=1/math.sqrt(1-beta*beta)
        scalar_db=e*gamma**3*(beta-math.cos(theta))
        assert abs(scalar_db-j[3])<1e-10
        if beta==0.:assert np.max(np.abs(j[4:10]))==0. and physical_residual==0.
        cases.append({'beta':beta,'lab_energy_keV':e,'corrected_keV':float(corrected(x)),
                      'Jacobian_keV_per_input_unit':j.tolist(),'linear_sigma_keV':sigma,
                      'MC_sigma_keV':mc_sigma,'MC_mean_bias_keV':float(np.mean(energies)-1000),
                      'MC_sigma_relative_difference':relative,
                      'common_origin_uncertainty_added_variance_keV2':common_change,
                      'wrong_independent_origin_added_variance_keV2':independent_wrong,
                      'physical_1mm_transverse_target_shift_keV':physical_residual})
    assert max_derivative_error<5e-6 and max_MC_difference<.01
    return {'schema_version':1,'kind':'synthetic Cartesian input/error exercise; no measured event reconstruction',
            'input_order':['E_lab_keV','beta_x','beta_y','beta_z','vertex_x_mm','vertex_y_mm','vertex_z_mm','first_x_mm','first_y_mm','first_z_mm'],
            'chosen_covariance':covariance.tolist(),'geometry':{'photon_theta_deg':35,'source_firstIP_distance_mm':radius},
            'cases':cases,'verification':{'finite_difference_max_absolute_error':max_derivative_error,
                                         'scalar_longitudinal_derivative_match':True,'radial_position_derivative_zero':True,
                                         'common_coordinate_translation_and_rotation_invariant':True,
                                         'physical_target_shift_distinguished':True,'static_limit_regular':True,
                                         'MC_sigma_max_relative_difference':max_MC_difference,'passed':True},
            'boundaries':['Coordinate frame changes cancel only when represented consistently for all inputs.',
                          'Physical relative target/detector movements are different and usually do not cancel.',
                          'If theta is derived from beta and positions, do not propagate its same errors again independently.',
                          'All covariance values here are self-chosen; actual particle/PSA shared uncertainty is absent.'],
            'numpy_version':np.__version__}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=calculate()
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(a.output),'verification':r['verification'],
                     'sigmas_keV':[c['linear_sigma_keV'] for c in r['cases']]}))


if __name__=='__main__':
    main()
