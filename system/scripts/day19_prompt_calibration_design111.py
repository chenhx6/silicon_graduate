#!/usr/bin/env python3
"""Moment-calibration planning in a declared symmetric timing toy model.

Independent Gaussian prompt, signed exponential wait, known zero mean, complete
time support, no background/feeding/drift. This is no experimental fit or CI.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import statistics
from pathlib import Path


def variance_of_squared_signal(sigma: float, tau: float) -> float:
    return 2*sigma**4+8*sigma*sigma*tau*tau+20*tau**4


def monte_carlo(sigma: float, tau: float, count: int, repetitions: int,
                seed: int) -> dict:
    rng=random.Random(seed)
    estimates=[]
    for _ in range(repetitions):
        signal_sum=0.
        prompt_sum=0.
        for _ in range(count):
            sign=1 if rng.random() < .5 else -1
            signal=rng.gauss(0,sigma)+sign*rng.expovariate(1/tau)
            prompt=rng.gauss(0,sigma)
            signal_sum+=signal*signal
            prompt_sum+=prompt*prompt
        estimates.append((signal_sum-prompt_sum)/(2*count))
    mean=statistics.mean(estimates)
    variance=statistics.variance(estimates)
    expected=(variance_of_squared_signal(sigma,tau)+2*sigma**4)/(4*count)
    mean_se=math.sqrt(expected/repetitions)
    # Sampling checks have a declared Monte Carlo tolerance; they do not
    # certify the applicability of this toy model to any detector.
    assert abs(variance/expected-1)<.12, (variance,expected)
    assert abs(mean-tau*tau)<4*mean_se, (mean,tau*tau,mean_se)
    return dict(count_signal=count,count_prompt=count,repetitions=repetitions,
                seed=seed,Q_true_ps2=tau*tau,mean_Q_ps2=mean,
                variance_Q_empirical_ps4=variance,
                variance_Q_analytic_ps4=expected,
                variance_ratio=variance/expected,
                MC_mean_standard_error_ps2=mean_se,
                negative_Q_fraction=sum(q<0 for q in estimates)/repetitions,
                boundary_handling="negative Q retained; no clipping or Gaussian tau CI reported")


def calculate() -> dict:
    sigma=80.
    cases=[]
    for tau,seed in [(20.,201110),(5.,501110)]:
        a=variance_of_squared_signal(sigma,tau)
        b=2*sigma**4
        # Var(Qhat)=(A/N+B/N0)/4; local Var(tauhat)=.../(16tau²).
        planning=[]
        for target_sigma_tau in [1.,.5]:
            count=math.ceil((a+b)/(16*tau*tau*target_sigma_tau**2))
            planning.append(dict(target_local_sigma_tau_ps=target_sigma_tau,
                                 equal_N_each_spectrum=count,
                                 convention="asymptotic delta-method, away from tau=0, independent complete samples"))
        mismatch=[]
        true_second_moment=sigma*sigma+2*tau*tau
        for assumed_sigma in [78.,80.,82.]:
            q=(true_second_moment-assumed_sigma**2)/2
            mismatch.append(dict(assumed_prompt_sigma_ps=assumed_sigma,
                                 inferred_Q_ps2=q,
                                 inferred_tau_ps=math.sqrt(q) if q>=0 else None,
                                 interpretation="deterministic mismatch, no assigned probability/CI"))
        cases.append(dict(tau_true_ps=tau,variance_of_signal_squared_ps4=a,
                          variance_of_prompt_squared_ps4=b,
                          derivative_tau_wrt_prompt_sigma=-sigma/(2*tau),
                          variance_planning=planning,
                          optimal_count_ratio_N_over_N0=math.sqrt(a/b),
                          prompt_sigma_mismatch=mismatch,
                          MC=monte_carlo(sigma,tau,1000,2000,seed)))
    return dict(scope="Synthetic calibration allocation, not original events or experimental precision",
                prompt_sigma_ps=sigma,
                observable="Qhat=(mean(signal_t²)-mean(prompt_t²))/2 estimates tau²",
                moment_derivation={
                    "M2_signal":"sigma²+2tau²",
                    "M4_signal":"3sigma^4+12sigma²tau²+24tau^4",
                    "Var_signal_t_squared":"2sigma^4+8sigma²tau²+20tau^4",
                    "Var_Q_general":"[Var(M2signal)+Var(M2prompt)-2Cov(M2signal,M2prompt)]/4",
                    "Var_Q_independent":"[A/N+B/N0]/4",
                    "local_Var_tau":"Var_Q/(4tau²), valid away from zero boundary",
                    "optimal_detected_count_allocation":"N/N0=sqrt(A/B); not automatically beamtime allocation"},
                cases=cases,
                limitations=["requires matched prompt mean/variance and complete or correctly modeled time acceptance",
                             "finite ROI, nonGaussian prompt, background or feeding change required moments",
                             "Gaussian prompt assumed only for stated planning/MC formulas; real prompt fourth moment must be measured or modeled",
                             "shared events/reference invalidate zero covariance assumption",
                             "unknown calibration transfer mismatch cannot be removed by more target events",
                             "counts are detected samples; no efficiency/beamtime supplied"],
                conclusion="Matched prompt moments can break the constructed alias. Calibration precision and boundary behavior must be included; a moment deficit may be negative at finite N.")


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    result=calculate()
    result["script_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"cases":[{"tau":c["tau_true_ps"],"planning":c["variance_planning"],
                               "MC_variance_ratio":c["MC"]["variance_ratio"],
                               "negative_Q_fraction":c["MC"]["negative_Q_fraction"],
                               "mismatch":c["prompt_sigma_mismatch"]} for c in result["cases"]]}))


if __name__=="__main__":
    main()
