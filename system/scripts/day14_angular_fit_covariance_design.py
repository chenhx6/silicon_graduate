#!/usr/bin/env python3
"""Chosen angular-fit covariance models with the published 67Ga geometry.

No GF fit, observed angular counts, efficiencies or actual correlation is
recovered. Positive diagonal variances are design examples, not measurements.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from numpy.polynomial import legendre
from scipy.optimize import minimize

from day14_shared_polarization_limits import stretched_weights,e2_gradient_kernel


def maximum_coefficients():
    x,w=legendre.leggauss(32)
    p=(stretched_weights(6.5,.5)+stretched_weights(6.5,-.5))/2
    values=sum(v*e2_gradient_kernel(q,np.arccos(x))[0] for q,v in zip(range(-2,3),p))
    fitted=legendre.legfit(x,values,4)
    integrated=np.array([(2*k+1)/2*np.dot(w,values*legendre.Legendre.basis(k)(x)) for k in range(5)])
    if not np.allclose(fitted,integrated,atol=1e-13):raise AssertionError('independent coefficient routes')
    return fitted[[2,4]]


def design(angles):
    return legendre.legvander(np.cos(np.deg2rad(angles)),4)[:,[0,2,4]]


def normalized_alpha(beta,maximum):
    return beta[1:]/beta[0]/maximum


def jacobian(beta,maximum):
    f=beta[0];a=normalized_alpha(beta,maximum)
    return np.array([[-a[0]/f,1/(f*maximum[0]),0],[-a[1]/f,0,1/(f*maximum[1])]])


def covariance(x,v,beta,maximum):
    vinv=np.linalg.inv(v);c=np.linalg.inv(x.T@vinv@x);j=jacobian(beta,maximum)
    return c,j@c@j.T


def correlation(c):
    return float(c[0,1]/np.sqrt(c[0,0]*c[1,1]))


def two_variance_examples(x,beta,maximum):
    target=np.array([.037,.090]);ratio=(target[1]/target[0])**2
    def current(z):
        variances=np.exp(np.r_[0,z]);_,c=covariance(x,np.diag(variances),beta,maximum)
        return variances,c
    def constraint(z):
        _,c=current(z);return np.log(c[1,1]/c[0,0]/ratio)
    rows=[]
    for sign in [1,-1]:
        result=minimize(lambda z:sign*correlation(current(z)[1]),np.zeros(5),method='SLSQP',
                        bounds=[(-2,2)]*5,constraints={'type':'eq','fun':constraint},
                        options={'ftol':1e-12,'maxiter':300})
        if not result.success or abs(constraint(result.x))>1e-9:raise AssertionError('chosen family search failed')
        var,c=current(result.x);scale=target[0]**2/c[0,0];var*=scale
        cb,ca=covariance(x,np.diag(var),beta,maximum)
        rows.append({'angle_variances_chosen':var.tolist(),'alpha_covariance_chosen':ca.tolist(),
                     'marginal_sigmas':np.sqrt(np.diag(ca)).tolist(),'rho':correlation(ca),
                     'optimizer_success':bool(result.success),'not_a_global_bound_or_source_fit':True})
    return rows


def audit():
    checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    maximum=maximum_coefficients();check('CG_kernel_legendre_and_integrated_coefficients',np.allclose(maximum,[40/91,-216/1001]))
    # This published fit point is used only as the local linearization point.
    # It is also held fixed for the C-geometry comparison, not a C-data refit.
    alpha0=np.array([.973,.803]);beta=np.r_[1,alpha0*maximum];j=jacobian(beta,maximum)
    fd=[]
    for i in range(3):
        h=1e-6;hi=beta.copy();lo=beta.copy();hi[i]+=h;lo[i]-=h
        fd.append((normalized_alpha(hi,maximum)-normalized_alpha(lo,maximum))/(2*h))
    check('normalization_Jacobian_finite_difference',np.allclose(j,np.array(fd).T,rtol=1e-9))
    check('global_multiplicative_direction_cancels_first_order',np.allclose(j@beta,0,atol=1e-14))
    geometry={'C_simultaneous':[0,57,90,158],
              'alpha_two_runs':[61,105,146.5,43,87,128.5]}
    results=[]
    for name,angles in geometry.items():
        x=design(angles);y=x@beta;v=np.eye(len(angles));cb,ca=covariance(x,v,beta,maximum)
        check(name+'_rank_three_and_positive_mean_intensities',np.linalg.matrix_rank(x)==3 and np.all(y>0))
        check(name+'_PSD_parameter_covariances',np.linalg.eigvalsh(cb).min()>0 and np.linalg.eigvalsh(ca).min()>0)
        q,r=np.linalg.qr(x);qr_cov=np.linalg.inv(r)@np.linalg.inv(r).T
        check(name+'_QR_and_normal_matrix_covariances_agree',np.allclose(cb,qr_cov))
        # A second parameterization fits (F,alpha2,alpha4) directly.
        tangent=np.c_[y/beta[0],x[:,1:]*maximum*beta[0]]
        fisher=tangent.T@tangent
        direct=np.linalg.inv(fisher)[1:,1:]
        schur=fisher[1:,1:]-np.outer(fisher[1:,0],fisher[0,1:])/fisher[0,0]
        check(name+'_Jacobian_Fisher_and_profiled_Schur_agree',np.allclose(ca,direct) and np.allclose(ca,np.linalg.inv(schur)))
        _,scaled=covariance(x,7*v,beta,maximum)
        check(name+'_noise_scale_covariance_and_rho',np.allclose(scaled,7*ca) and np.isclose(correlation(scaled),correlation(ca)))
        global_v=v+.03**2*np.outer(y,y);c_global,a_global=covariance(x,global_v,beta,maximum)
        check(name+'_global_mode_parameter_propagation',np.allclose(c_global,cb+.03**2*np.outer(beta,beta)))
        check(name+'_global_mode_cancels_normalized_alpha',np.allclose(a_global,ca))
        # Fixing F and removing its covariance is a different design assumption.
        fixed_cov=np.linalg.inv((x[:,1:]*maximum).T@(x[:,1:]*maximum))
        check(name+'_known_F_is_not_normalized_unknown_F',np.max(abs(fixed_cov-ca))>.01)
        results.append({'geometry':name,'angles_deg':angles,'chosen_equal_absolute_variance_rho':correlation(ca),
                        'chosen_sigma4_over_sigma2':float(np.sqrt(ca[1,1]/ca[0,0])),
                        'unknown_F_alpha_covariance_unit_noise':ca.tolist(),'known_F_alpha_covariance_unit_noise':fixed_cov.tolist()})
    check('same_mean_geometries_can_give_opposite_rho',results[0]['chosen_equal_absolute_variance_rho']>0 and results[1]['chosen_equal_absolute_variance_rho']<0)
    x=design(geometry['alpha_two_runs']);examples=two_variance_examples(x,beta,maximum)
    for i,row in enumerate(examples):
        check(f'family{i}_positive_variances_and_covariance',np.min(row['angle_variances_chosen'])>0 and np.linalg.eigvalsh(row['alpha_covariance_chosen']).min()>0)
        check(f'family{i}_same_target_marginal_sigmas',np.allclose(row['marginal_sigmas'],[.037,.09],atol=1e-10))
    check('same_marginals_do_not_identify_rho',abs(examples[0]['rho']-examples[1]['rho'])>.3)
    # Structured run-monitor example uses a declared separate-mode covariance.
    v=np.diag(examples[1]['angle_variances_chosen']);y=x@beta;u=y.copy();u[3:]=0
    _,before=covariance(x,v,beta,maximum);_,with_run=covariance(x,v+.02**2*np.outer(u,u),beta,maximum)
    check('one_run_monitor_mode_changes_normalized_covariance',np.max(abs(with_run-before))>1e-5)
    return {'kind':'L2 chosen angular-fit covariance design with source geometry; not actual GF covariance',
            'source_locators':['Z83-12 / printed393 statistical dependence','printed390 Sec2 detector geometry','Z83-11 / Table1 marginal errors'],
            'local_linearization_point':{'from_published_alpha11p3_fit':alpha0.tolist(),'held_same_for_geometry_comparison':True,'F_chosen':1,'pureE2_maximum_coefficients_task_derived':maximum.tolist()},
            'geometry_equal_variance_controls':results,'same_marginals_positive_variance_examples':examples,
            'separate_run_monitor_control':{'chosen_relative_monitor_sigma':.02,'before_alpha_covariance':before.tolist(),'after_alpha_covariance':with_run.tolist()},
            'checks':checks,'checks_passed':sum(checks.values()),
            'boundaries':['No observed angle counts, relative efficiencies, background model, monitor counts or GF covariance is supplied.','The3parameter model is beta0+beta2P2+beta4P4; normalized alpha includes an uncertain fitted beta0.','The published alpha point is a linearization point, not a generated true nuclear population or a C-measurement point.','The positive variance examples merely reproduce two numerical marginal errors; no actual source variances or certified rho bounds are inferred.','Global multiplicative-mode cancellation is first order for normalized coefficients; angle/run-specific modes can remain.','A different fit parameterization or fixed F is a different covariance problem.','Day14 remains active; Day15 preview stays uncredited.']}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    args.output.resolve().relative_to(Path(__file__).resolve().parents[2]);r=audit();args.output.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:r[k] for k in ['checks_passed','geometry_equal_variance_controls','same_marginals_positive_variance_examples','separate_run_monitor_control']},ensure_ascii=False))


if __name__=='__main__':main()
