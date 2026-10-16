#!/usr/bin/env python3
"""129Ba printed-summary audit in an explicit maximum-alignment reference.

Reference population and covariance models are chosen. This is not a raw
experimental refit or proof of the original coefficient correction layer.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial import polynomial as poly

from day16_se21_m3_reference import population, forms, direct
from day16_st99_table_replay import quoted


def evaluate(matrix: np.ndarray, delta: float) -> float:
    vector=np.array([1.,delta])
    return float(vector@matrix@vector/(1+delta*delta))


def root_equation(matrix: np.ndarray, observed: float) -> list:
    c=np.array([matrix[0,0]-observed,2*matrix[0,1],matrix[1,1]-observed])
    result=[]
    for root in poly.polyroots(c):
        if abs(root.imag)<1e-10:
            value=float(root.real)
            assert abs(evaluate(matrix,value)-observed)<1e-12
            result.append(value)
    return result


def score_candidates(matrices: list[np.ndarray], means: np.ndarray,
                     sigmas: np.ndarray, rho: float) -> dict:
    residual=[]
    for mat,mean in zip(matrices,means):
        residual.append(np.array([mat[0,0]-mean,2*mat[0,1],mat[1,1]-mean]))
    cov=np.outer(sigmas,sigmas)*np.array([[1,rho],[rho,1]])
    assert min(np.linalg.eigvalsh(cov))>0
    precision=np.linalg.inv(cov)
    numerator=np.zeros(5)
    for i in range(2):
        for j in range(2):numerator+=precision[i,j]*np.convolve(residual[i],residual[j])
    derivative=poly.polysub(np.convolve(poly.polyder(numerator),[1,0,1]),
                            np.r_[0,4*numerator])
    derivative=poly.polytrim(derivative,tol=1e-10)
    candidates=[]
    for root in poly.polyroots(derivative):
        if abs(root.imag)<1e-8:
            d=float(root.real);diff=np.array([evaluate(m,d) for m in matrices])-means
            score=float(diff@precision@diff)
            assert abs(score-poly.polyval(d,numerator)/(1+d*d)**2)<1e-9
            candidates.append({"delta":d,"score":score,"A2_A4":[evaluate(m,d) for m in matrices],
                               "radiative_E2_fraction":d*d/(1+d*d)})
    pure_res=np.array([m[1,1] for m in matrices])-means
    pure_score=float(pure_res@precision@pure_res)
    best=min(candidates,key=lambda x:x["score"])
    return {"chosen_rho":rho,"covariance":cov.tolist(),"stationary_points":sorted(candidates,key=lambda x:x["delta"]),
            "pureE2_limit_score":pure_score,"best_stationary_point":best,
            "global_best_is_finite":best["score"]<pure_score,
            "not_actual_experimental_confidence":True}


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args();cfg=json.loads(args.input.read_text());root=Path(__file__).resolve().parents[2]
    for source in cfg["sources"]:
        assert hashlib.sha256((root/source["raw"]).read_bytes()).hexdigest()==source["sha256"]
    tr=cfg["transition"];ti,tf=tr["twice_Ji"],tr["twice_Jf"]
    components=tuple(tuple(x) for x in tr["components"]);pop=population(ti,0.)
    assert np.count_nonzero(pop)==2
    mats=forms(ti,tf,components,pop)
    controls=[]
    for delta in (-2.,-.33,0.,1.):
        a=np.array([1.,delta]);projected,norm=direct(ti,tf,components,pop,a,12)
        alternate,_=direct(ti,tf,components,pop,a,16)
        difference=max(abs(evaluate(mats[k],delta)-projected[k]) for k in (0,2,4))
        quad=max(abs(projected[k]-alternate[k]) for k in (0,2,4))
        assert difference<2e-12 and quad<2e-12
        controls.append({"delta_chosen":delta,"F_projection_max_difference":difference,
                         "quadrature12_vs16":quad,"integrated_channel_error":float(max(abs(norm-1)))})
    inputs=[quoted(cfg["printed_observations"][key]) for key in ("A22","A44")]
    means=np.array([x[0] for x in inputs]);sigmas=np.array([x[1] for x in inputs])
    equations=[]
    for rank,(mean,sigma) in zip((2,4),inputs):
        equations.append({"rank":rank,"central":root_equation(mats[rank],mean),
                          "mean_minus_sigma":root_equation(mats[rank],mean-sigma),
                          "mean_plus_sigma":root_equation(mats[rank],mean+sigma)})
    scores=[score_candidates([mats[2],mats[4]],means,sigmas,rho)
            for rho in cfg["analysis"]["chosen_covariance_rhos"]]
    fractions=[]
    for label,values in [("new_author_delta",cfg["literature_summary"]["2024authors_new_delta"]),
                         ("old_angular_delta",cfg["literature_summary"]["historical_angular_delta"]),
                         ("old_polar_delta",cfg["literature_summary"]["historical_polar_delta"])]:
        d,sd=values
        fractions.append({"label":label,"delta":d,"quoted_sigma_delta":sd,
                          "radiative_E2_fraction":d*d/(1+d*d),
                          "local_sigma_fraction":abs(2*d/(1+d*d)**2)*sd,
                          "literal_delta_endpoint_fractions":[x*x/(1+x*x) for x in [d-sd,d+sd]]})
    old=cfg["literature_summary"]["old_1978_adopted_delta"]
    out={"identity":cfg["identity"],"input_sha256":hashlib.sha256(args.input.read_bytes()).hexdigest(),
         "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         "reference_population":pop.tolist(),"reference_forms":{str(k):v.tolist() for k,v in mats.items()},
         "controls":controls,"single_coefficient_equations":equations,"chosen_covariance_scores":scores,
         "old_adopted_interval_reference_predictions":[{"delta":d,"A2":evaluate(mats[2],d),
                "A4":evaluate(mats[4],d),"E2_fraction":d*d/(1+d*d)} for d in old],
         "literature_fraction_conversions":fractions,
         "printed_P_value_sigma":list(quoted(cfg["printed_observations"]["physical_P"])),
         "P_fit_performed":False,
         "boundary":"Maximum-alignment reference and chosen correlations only. OriginalA22/A44correctionlayer/convention/Cov notverifiedfromGizon1978body. Noactualpopulationfit, experimentalCI, correctedP, absoluteB orwobblingassignment."}
    args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"roots":equations,"chosen_score_minima":[{"rho":s["chosen_rho"],"best":s["best_stationary_point"]} for s in scores],"fractions":fractions,"controls":controls},ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
