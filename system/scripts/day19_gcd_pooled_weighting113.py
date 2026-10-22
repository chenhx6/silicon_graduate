#!/usr/bin/env python3
"""Weighting and alignment conditions for pooled-pair timing arrays.

This writes only the declared design output. Inputs are synthetic; no EXILL or
FATIMA experimental events, fit covariance or confidence interval is used.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import statistics
from pathlib import Path


def pooled_centroid(centers: list[float], weights: list[float]) -> float:
    total=sum(weights)
    assert total > 0 and len(centers) == len(weights)
    return sum(c*w for c,w in zip(centers,weights))/total


def delta_c_pooled(stop_centers: list[float], stop_weights: list[float],
                   start_centers: list[float], start_weights: list[float]) -> float:
    return pooled_centroid(stop_centers,stop_weights)-pooled_centroid(start_centers,start_weights)


def simulate_mc(pairs: list[dict], stop_weights: list[float],
                start_weights: list[float], repetitions: int,
                events_per_pair: int, seed: int) -> dict:
    rng=random.Random(seed)
    estimates=[]
    k=len(pairs)
    for _ in range(repetitions):
        stops=[]
        starts=[]
        for p in pairs:
            sigma=p["sigma_ps"]
            # stop branch: center = T0 + PRD/2 + tau
            center_stop=p["t0_ps"]+p["prd_ps"]/2+p["tau_ps"]
            # start branch: center = T0 - PRD/2 - tau
            center_start=p["t0_ps"]-p["prd_ps"]/2-p["tau_ps"]
            stop_samples=[rng.gauss(center_stop,sigma) for _ in range(events_per_pair)]
            start_samples=[rng.gauss(center_start,sigma) for _ in range(events_per_pair)]
            stops.append(statistics.mean(stop_samples))
            starts.append(statistics.mean(start_samples))
        estimates.append(delta_c_pooled(stops,stop_weights,starts,start_weights))
    empirical_mean=statistics.mean(estimates)
    empirical_var=statistics.variance(estimates)
    # Analytic variance: sum(w_i^2 sigma_i^2 / n_i) / (sum w_i)^2 for both branches
    w_stop_tot=sum(stop_weights)
    w_start_tot=sum(start_weights)
    var_stop=sum((w/w_stop_tot)**2 * (p["sigma_ps"]**2/events_per_pair)
                 for w,p in zip(stop_weights,pairs))
    var_start=sum((w/w_start_tot)**2 * (p["sigma_ps"]**2/events_per_pair)
                  for w,p in zip(start_weights,pairs))
    expected_var=var_stop+var_start
    assert abs(empirical_var/expected_var-1)<.12
    return dict(repetitions=repetitions,events_per_pair=events_per_pair,
                empirical_mean=empirical_mean,empirical_var=empirical_var,
                expected_var=expected_var,variance_ratio=empirical_var/expected_var)


def calculate() -> dict:
    tau_true=20.0
    # Two accepted pairs with different alignment and individual zero-time responses
    pA=dict(pair="pA",t0_ps=-30.0,prd_ps=-20.0,tau_ps=tau_true,sigma_ps=120.0)
    pB=dict(pair="pB",t0_ps=30.0,prd_ps=40.0,tau_ps=tau_true,sigma_ps=140.0)
    pairs=[pA,pB]
    shifts=[30.0,-30.0]  # constant shift to bring t0 to 0

    stop_raw=[p["t0_ps"]+p["prd_ps"]/2+tau_true for p in pairs]
    start_raw=[p["t0_ps"]-p["prd_ps"]/2-tau_true for p in pairs]
    stop_aligned=[c+s for c,s in zip(stop_raw,shifts)]
    start_aligned=[c+s for c,s in zip(start_raw,shifts)]

    cases=[]
    # Case 1: unweighted scalar mean / equal-weight pool (matches Eq 11 form)
    w_equal=[0.5,0.5]
    dc1_raw=delta_c_pooled(stop_raw,w_equal,start_raw,w_equal)
    dc1_aligned=delta_c_pooled(stop_aligned,w_equal,start_aligned,w_equal)
    mean_prd_equal=pooled_centroid([p["prd_ps"] for p in pairs],w_equal)
    tau1_raw=(dc1_raw-mean_prd_equal)/2
    tau1_aligned=(dc1_aligned-mean_prd_equal)/2
    cases.append(dict(name="equal_weight_unweighted_form",
                      weights_stop=w_equal,weights_start=w_equal,
                      mean_prd=mean_prd_equal,
                      delta_c_raw=dc1_raw,delta_c_aligned=dc1_aligned,
                      alignment_invariant=math.isclose(dc1_raw,dc1_aligned),
                      inferred_tau_raw=tau1_raw,inferred_tau_aligned=tau1_aligned))

    # Case 2: unequal sample weights, but symmetric between roles: w_stop = w_start = [0.8, 0.2]
    w_symm=[0.8,0.2]
    dc2_raw=delta_c_pooled(stop_raw,w_symm,start_raw,w_symm)
    dc2_aligned=delta_c_pooled(stop_aligned,w_symm,start_aligned,w_symm)
    mean_prd_symm=pooled_centroid([p["prd_ps"] for p in pairs],w_symm)
    tau2_using_symm_prd=(dc2_raw-mean_prd_symm)/2
    tau2_using_equal_prd=(dc2_raw-mean_prd_equal)/2
    cases.append(dict(name="role_symmetric_unequal_weights",
                      weights_stop=w_symm,weights_start=w_symm,
                      mean_prd_matched=mean_prd_symm,mean_prd_unweighted=mean_prd_equal,
                      delta_c_raw=dc2_raw,delta_c_aligned=dc2_aligned,
                      alignment_invariant=math.isclose(dc2_raw,dc2_aligned),
                      tau_with_matched_prd=tau2_using_symm_prd,
                      tau_bias_if_using_unweighted_prd=tau2_using_equal_prd-tau_true))

    # Case 3: asymmetric weights between roles: w_stop=[0.8,0.2], w_start=[0.2,0.8]
    w_stop_asymm=[0.8,0.2]
    w_start_asymm=[0.2,0.8]
    dc3_raw=delta_c_pooled(stop_raw,w_stop_asymm,start_raw,w_start_asymm)
    dc3_aligned=delta_c_pooled(stop_aligned,w_stop_asymm,start_aligned,w_start_asymm)
    cases.append(dict(name="role_asymmetric_weights",
                      weights_stop=w_stop_asymm,weights_start=w_start_asymm,
                      delta_c_raw=dc3_raw,delta_c_aligned=dc3_aligned,
                      alignment_invariant=math.isclose(dc3_raw,dc3_aligned),
                      raw_minus_aligned_ps=dc3_raw-dc3_aligned,
                      reason="t0 shifts do not cancel when start and stop pools use different pair weights"))

    mc_results=simulate_mc(pairs,w_equal,w_equal,1200,150,seed=1132015)
    return dict(
        scope="Synthetic 2-pair timing array; tests alignment and weighting assumptions of pooled GCD",
        declared_model={
            "pair_stop_center":"T0_i + PRD_i/2 + tau",
            "pair_start_center":"T0_i - PRD_i/2 - tau",
            "pair_DeltaC":"PRD_i + 2tau (cancels T0_i and its shift)",
            "pool_DeltaC":"sum(w+_i C+_i)/sum(w+_i) - sum(w-_i C-_i)/sum(w-_i)",
            "mean_PRD_matched":"sum(w_i PRD_i)/sum(w_i) when w+=w-=w"
        },
        inputs=dict(tau_true_ps=tau_true,pairs=pairs,shifts=shifts),
        cases=cases,
        mc_simulation=mc_results,
        conclusions=[
            "Constant alignment shifts cancel strictly if each pair has its own DeltaC or if w+_i == w-_i",
            "If calibrator and target cascades have different relative pair yields, mean PRD must use matched weights",
            "A simple superposition of raw counts equals the unweighted Eq 11 only when all pair event counts are equal",
            "None of these controls implies actual EXILL&FATIMA data violated these conditions; it defines the audit boundary"
        ]
    )


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    result=calculate()
    result["script_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({k:result[k] for k in ["inputs","cases","mc_simulation"]}))


if __name__=="__main__":
    main()
