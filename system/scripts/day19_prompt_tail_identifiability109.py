#!/usr/bin/env python3
"""Positive prompt-tail aliases for an unlabeled symmetric timing model.

This writes only the requested artifact. Inputs are synthetic; no original
events, experimental lifetime fit, covariance or confidence interval is used.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


def gaussian(t: float, sigma: float) -> float:
    return math.exp(-t*t/(2*sigma*sigma))/(math.sqrt(2*math.pi)*sigma)


def normal_laplace(t: float, sigma: float, tau: float) -> float:
    """Gaussian convolved with exp(-|t|/tau)/(2tau), evaluated analytically."""
    if tau == 0:
        return gaussian(t, sigma)
    # Parameters below keep the exp/erfc products well within float range.
    first = math.exp(-t/tau) * math.erfc((sigma/tau-t/sigma)/math.sqrt(2))
    second = math.exp(t/tau) * math.erfc((sigma/tau+t/sigma)/math.sqrt(2))
    return math.exp(sigma*sigma/(2*tau*tau))*(first+second)/(4*tau)


def simpson(function, low: float, high: float, count: int) -> float:
    assert count % 2 == 0
    h=(high-low)/count
    return h/3*(function(low)+function(high)
                +4*sum(function(low+i*h) for i in range(1,count,2))
                +2*sum(function(low+i*h) for i in range(2,count,2)))


def alias_weight(tau_original: float, tau_alternate: float) -> float:
    if not 0 <= tau_alternate <= tau_original or tau_original <= 0:
        raise ValueError("Declared positive-mixture construction needs 0<=tau2<=tau1")
    return (tau_alternate/tau_original)**2


def calculate() -> dict:
    sigma,tau1,tau2=80.0,20.0,10.0
    weight=alias_weight(tau1,tau2)

    def alternate_prompt(t):
        return weight*gaussian(t,sigma)+(1-weight)*normal_laplace(t,sigma,tau1)

    def alternate_observed(t,count):
        # Integrate the second decay kernel in time, independently of the
        # characteristic-function proof or closed original observed density.
        return simpson(lambda z: alternate_prompt(t-z)*math.exp(-abs(z)/tau2)/(2*tau2),
                       -400,400,count)

    pointwise=[]
    for t in [-320.,-160.,-80.,0.,80.,160.,320.]:
        reference=normal_laplace(t,sigma,tau1)
        coarse=alternate_observed(t,1600)
        fine=alternate_observed(t,3200)
        pointwise.append(dict(t_ps=t,original_density_per_ps=reference,
                              alternate_coarse_per_ps=coarse,
                              alternate_fine_per_ps=fine,
                              relative_error=(fine-reference)/reference,
                              refinement_change_per_ps=fine-coarse))
    max_error=max(abs(p["relative_error"]) for p in pointwise)
    assert max_error < 2e-7, max_error

    # Frequency-space proof checked at independent frequencies, including zero.
    characteristic=[]
    for k in [0.,.002,.01,.025,.05,.1]:
        original=math.exp(-sigma*sigma*k*k/2)/(1+tau1*tau1*k*k)
        alternate=(math.exp(-sigma*sigma*k*k/2)
                   *(weight+(1-weight)/(1+tau1*tau1*k*k))
                   /(1+tau2*tau2*k*k))
        characteristic.append(dict(k_per_ps=k,original=original,alternate=alternate))
        assert math.isclose(original,alternate,rel_tol=1e-13,abs_tol=1e-16)

    norm_original=simpson(lambda t:normal_laplace(t,sigma,tau1),-1200,1200,9600)
    norm_alternate_prompt=simpson(alternate_prompt,-1200,1200,9600)
    assert abs(norm_original-1)<1e-10 and abs(norm_alternate_prompt-1)<1e-10
    var_original=sigma*sigma+2*tau1*tau1
    var_prompt_alternate=sigma*sigma+(1-weight)*2*tau1*tau1
    var_observed_alternate=var_prompt_alternate+2*tau2*tau2
    assert var_observed_alternate==var_original

    windows=[]
    for halfwidth in [40.,80.,160.,320.]:
        acceptance=simpson(lambda t:normal_laplace(t,sigma,tau1),
                           -halfwidth,halfwidth,1600)
        # Identical full densities imply identical restricted distributions;
        # no "independent alternate window fit" is claimed here.
        windows.append(dict(halfwidth_ps=halfwidth,common_acceptance=acceptance,
                            invariant_reason="same full density, so same deterministic ROI"))
    try:
        alias_weight(10,20)
    except ValueError:
        invalid_mixture_rejected=True
    else:
        raise AssertionError("Invalid positive-mixture direction was accepted")
    return {
        "scope":"Synthetic unlabeled equal-weight +/- exponential timing; no background, drift or real-event fit",
        "inputs":{"gaussian_sigma_ps":sigma,"tau_original_ps":tau1,
                  "tau_alternate_ps":tau2,"alternate_prompt_delta_weight":weight},
        "kernel_definition":"L_tau(t)=exp(-abs(t)/tau)/(2tau); its CF=1/(1+tau^2 k^2)",
        "exact_identity":"G*L_tau1 = [G*(a delta+(1-a)L_tau1)]*L_tau2, a=tau2^2/tau1^2",
        "assumptions":["equal-weight causal +/- mixture due to lost branch-role labels",
                       "unknown allowed prompt family includes the alternate positive tail mixture",
                       "complete normalized spectra before deterministic ROI"],
        "pointwise_time_quadrature":pointwise,
        "max_relative_error_time_quadrature":max_error,
        "characteristic_function_values":characteristic,
        "normalizations":{"original_observed":norm_original,
                          "alternate_prompt":norm_alternate_prompt},
        "variance_ps2":{"original_prompt":sigma*sigma,
                        "alternate_prompt":var_prompt_alternate,
                        "common_observed":var_original},
        "finite_windows":windows,
        "invalid_positive_mixture_direction_rejected":invalid_mixture_rejected,
        "conclusion":"Even full spectrum is nonidentifying over this allowed prompt family. More counts or identical ROI scans cannot separate the two constructed cases.",
        "needed_companions":["independently matched full-energy prompt response, including tails and time-scale uncertainty",
                             "verified feeder/decay role tagging or another constraint excluding the alternate prompt family"],
        "not_claimed":["actual LaBr3 response has these tails","all fast timing is nonidentifying",
                       "new experimental lifetime/fit/CI","numerical agreement certifies a source's scientific interpretation"]
    }


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    result=calculate()
    result["script_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({key:result[key] for key in
                     ["inputs","max_relative_error_time_quadrature","variance_ps2","finite_windows"]}))


if __name__=="__main__":
    main()
