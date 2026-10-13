#!/usr/bin/env python3
"""Day13 known-selection likelihood toy; no in-beam spectrum or beta fit.

Residual x in keV is drawn from an explicitly chosen Gaussian parent. A
fixed laboratory residual gate selects the observed sample. Conditional
likelihood needs its parameter-dependent normalization Z(mu,sigma); known
N_generated and binomial selection provide additional acceptance information.
Actual tracking response, backgrounds, mixtures, gain, stopping and detector
efficiency are absent. A data-dependent gate would need its own definition.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import quad
from scipy.optimize import minimize
from scipy.special import log_ndtr, logsumexp, ndtr


def acceptance(mu: float, sigma: float, low: float, high: float) -> float:
    return float(ndtr((high-mu)/sigma)-ndtr((low-mu)/sigma))


def log_acceptance(mu: float, sigma: float, low: float, high: float) -> float:
    a,b=(low-mu)/sigma,(high-mu)/sigma
    # Stable subtraction of two normal CDFs; use survival tails for a>0.
    log_large,log_small=(log_ndtr(-a),log_ndtr(-b)) if a>0 else (log_ndtr(b),log_ndtr(a))
    return float(log_large+math.log(-math.expm1(float(log_small-log_large))))


def truncated_nll(par: np.ndarray, n: int, total: float, square_total: float,
                  low: float, high: float, generated: int | None = None) -> float:
    mu,log_sigma=map(float,par);sigma=math.exp(log_sigma)
    logz=log_acceptance(mu,sigma,low,high)
    quadratic=(square_total-2*mu*total+n*mu*mu)/(2*sigma*sigma)
    conditional=n*(log_sigma+.5*math.log(2*math.pi)+logz)+quadratic
    if generated is None:
        return conditional
    # Add the binomial selected/unselected likelihood. The selected n log Z
    # cancels the conditional normalization, as it must for known trials.
    # P(outside)=Phi(a)+Phi(-b); this remains finite even when Z rounds to 1.
    log_not_z=float(logsumexp([log_ndtr((low-mu)/sigma),log_ndtr((mu-high)/sigma)]))
    return conditional-n*logz-(generated-n)*log_not_z


def fit(selected: np.ndarray, low: float, high: float, generated: int | None = None) -> dict:
    n=len(selected);total=float(np.sum(selected));square=float(selected@selected)
    best=None
    for start in ((float(np.mean(selected)),math.log(float(np.std(selected)))),(0.,math.log(3.)),(1.,math.log(2.))):
        res=minimize(truncated_nll,np.array(start),args=(n,total,square,low,high,generated),
                     method='L-BFGS-B',bounds=((-8.,8.),(math.log(.1),math.log(10.))),
                     options={'ftol':1e-13,'gtol':1e-6,'maxiter':2000})
        if np.isfinite(res.fun) and (best is None or res.fun<best.fun):best=res
    assert best is not None and best.success
    return {'mu_keV':float(best.x[0]),'sigma_keV':math.exp(float(best.x[1])),
            'nll':float(best.fun),'optimization_success':bool(best.success)}


def calculate() -> dict:
    rng=np.random.default_rng(131016)
    true_mu,true_sigma,low,high=1.2,2.,-2.,2.
    generated=1000000
    data=rng.normal(true_mu,true_sigma,generated)
    chosen=data[(data>low)&(data<high)]
    z=acceptance(true_mu,true_sigma,low,high)
    conditional=fit(chosen,low,high)
    trials=fit(chosen,low,high,generated)
    naive={'mu_keV':float(np.mean(chosen)),'sigma_keV':float(np.std(chosen))}
    normalization=quad(lambda x: math.exp(-.5*((x-true_mu)/true_sigma)**2)
                        /(true_sigma*math.sqrt(2*math.pi)*z),low,high,epsabs=1e-11)[0]
    analytic_selected_mu=quad(lambda x: x*math.exp(-.5*((x-true_mu)/true_sigma)**2)
                              /(true_sigma*math.sqrt(2*math.pi)*z),low,high,epsabs=1e-11)[0]
    assert abs(normalization-1)<1e-10
    assert abs(analytic_selected_mu-naive['mu_keV'])<.01
    assert abs(len(chosen)/generated-z)<.002
    assert abs(conditional['mu_keV']-true_mu)<.06 and abs(conditional['sigma_keV']-true_sigma)<.06
    assert abs(trials['mu_keV']-true_mu)<.03 and abs(trials['sigma_keV']-true_sigma)<.03
    assert naive['sigma_keV']<.6*true_sigma and naive['mu_keV']<.5*true_mu
    # Count rate alone does not identify N0, detector efficiency and Z.
    # The following pairs give the same expected selected count.
    count_equivalence=[]
    expected=len(chosen)
    for mu,sigma,eff in ((1.2,2.,1.),(0.,2.,.8),(1.2,3.,.6)):
        gate_z=acceptance(mu,sigma,low,high)
        n0=expected/(eff*gate_z)
        count_equivalence.append({'parent_mu_keV':mu,'parent_sigma_keV':sigma,
                                  'detector_efficiency':eff,'gate_fraction':gate_z,
                                  'required_incident_yield':n0,'same_expected_gate_count':n0*eff*gate_z})
    # With known Z and known N_generated, the selected count supplies real
    # information. This is absent if N_generated and efficiency are unknown.
    predicted_selected_naive=generated*acceptance(naive['mu_keV'],naive['sigma_keV'],low,high)
    assert predicted_selected_naive>len(chosen)*1.3
    # Remove selection: the conditional likelihood equals ordinary Gaussian.
    huge_low,huge_high=-100.,100.
    plain=truncated_nll(np.array([true_mu,math.log(true_sigma)]),len(data),float(np.sum(data)),float(data@data),huge_low,huge_high)
    expected_plain=len(data)*(math.log(true_sigma)+.5*math.log(2*math.pi))+float(np.sum((data-true_mu)**2))/(2*true_sigma**2)
    assert abs(plain-expected_plain)/len(data)<1e-10
    return {'schema_version':1,'kind':'synthetic fixed-gate likelihood; no measured beta or yield',
            'parent_model':{'mu_keV':true_mu,'sigma_keV':true_sigma,'gate_keV':[low,high],'generated':generated},
            'selected':{'n':len(chosen),'fraction':len(chosen)/generated,'analytic_fraction':z,
                        'analytic_conditional_mu_keV':analytic_selected_mu},
            'naive_untruncated_fit':naive,'conditional_truncated_fit':conditional,
            'known_trials_and_conditional_fit':trials,
            'naive_predicted_selected_if_trials_known':predicted_selected_naive,
            'count_only_equivalent_parameter_sets':count_equivalence,
            'boundaries':['Generated count is known only in this synthetic exercise.',
                          'Real global fitting needs selection and response identity; a conditional shape alone is not an absolute rate measurement.',
                          'Actual FOM/particle/time/energy gates may be coupled and require a multivariate acceptance.',
                          'Held-out events share calibration/systematics; they do not alone prove independent validation.'],
            'verification':{'normalization_error':abs(normalization-1),
                            'analytic_selected_mean_MC_passed':True,'parameter_recovery_passed':True,
                            'wide_gate_Gaussian_limit_passed':True,'count_identifiability_boundary_passed':True,'passed':True},
            'dependencies':{'numpy':np.__version__,'scipy':scipy.__version__}}


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    r=calculate();a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(a.output),'verification':r['verification'],'naive':r['naive_untruncated_fit'],
                      'conditional':r['conditional_truncated_fit'],'known_trials':r['known_trials_and_conditional_fit']}))


if __name__=='__main__':
    main()
