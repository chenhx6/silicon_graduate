#!/usr/bin/env python3
"""Source-conditioned support equivalence and a declared Gaussian tag design.

No experimental topology, likelihood or detector performance is inferred.
The primary level at183 is not assigned an invented observed decay.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from math import log, sqrt
from pathlib import Path
from statistics import NormalDist

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02"


def all_paths(edges):
    starts = sorted({e["p"] for e in edges})
    def descend(node, visited=(), chain=()):
        if node in visited:
            raise ValueError("source-selected decay graph must be acyclic")
        outgoing = [e for e in edges if e["p"] == node]
        if not outgoing:
            return [chain]
        return [p for e in outgoing for p in descend(e["d"],visited+(node,),chain+(e["id"],))]
    return [path for start in starts for path in descend(start)]


def supports(edges,gates,groups):
    byid={e["id"]:e for e in edges}
    paths=all_paths(edges)
    return {gate:sorted({byid[k]["group"] for p in paths if gate in p
                         for k in p if k!=gate and byid[k]["group"] in groups}) for gate in gates}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output",type=Path,default=RUN/"128i-discriminating-design-audit.json")
    args=p.parse_args()
    ipath=RUN/"128i-discriminating-design-input.json"
    data=json.loads(ipath.read_text())
    checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:
            raise AssertionError(name)
    for name,src in data["sources"].items():
        check(name+"_hash",hashlib.sha256((ROOT/src["path"]).read_bytes()).hexdigest()==src["sha256"])
    primary=data["common_upper_skeleton_assumed_sourcecompatible"]+data["primary_edges"]
    evaluated=data["common_upper_skeleton_assumed_sourcecompatible"]+data["evaluated_edges"]
    s1=supports(primary,data["gates"],data["coarse_target_groups"])
    s2=supports(evaluated,data["gates"],data["coarse_target_groups"])
    expected={"t756":["102"],"t764":["101","102"],"t117":["101"]}
    check("primary_coarse_support",s1==expected)
    check("evaluated_coarse_support",s2==expected)
    check("source_topologies_differ_despite_support_equality",data["primary_edges"]!=data["evaluated_edges"])
    check("primary183_decay_not_invented",not any(e["p"]=="A" for e in primary))
    check("15_discarding_is_declared_projection_not_detector_fact",data["invisible15_projection_is_our_condition"]
          and not data["actual_detector15_response_known"])
    check("support_not_actual_likelihood_equivalence",not data["actual_gate_intensities_or_likelihood_matched"])
    delta=float(data["state_tag_separation_keV"])
    target=float(data["chosen_class_error_target"])
    z=NormalDist().inv_cdf(1-target)
    sigma_max=delta/(2*z)
    fwhm_max=2*sqrt(2*log(2))*sigma_max
    error=NormalDist().cdf(-delta/(2*sigma_max))
    check("Gaussian_tag_class_error_target",abs(error-target)<1e-14)
    check("broader_tag_cannot_meet_same_target",NormalDist().cdf(-delta/(4*sigma_max))>target)
    check("zero_separation_has_no_tag_discrimination",NormalDist().cdf(0)==.5)
    check("Gaussian_FWHM_conversion",abs(fwhm_max/sigma_max-2.3548200450309493)<1e-14)
    check("no_actual_tag_or_covariance_claim",data["actual_state_tag_resolution_keV"] is None
          and data["actual_calibration_bias_bound_keV"] is None
          and data["actual_full_response_covariance"] is None)
    result=dict(kind="source-conditioned coarse supports plus declared independent-state-tag specification",
                checks=checks,check_count=len(checks),passed=all(checks.values()),inputs=data,
                primary_support=s1,evaluated_support=s2,
                source_path_sets=dict(primary=all_paths(primary),evaluated=all_paths(evaluated)),
                tag_design=dict(separation_keV=delta,per_class_error_target=target,z=z,
                                sigma_max_keV=sigma_max,FWHM_max_keV=fwhm_max,calculated_error=error,
                                with_known_bias_budget="sigma <= (Delta/2-bmax)/z, requiring0<=bmax<Delta/2",
                                observed_detector_performance=None),
                full_likelihood_equivalence_claimed=False,topology_choice=None,
                input_sha256=hashlib.sha256(ipath.read_bytes()).hexdigest(),
                limitations=["support equality only for declared selected graphs and coarse observation; not actual data likelihood",
                             "same102 group and hidden15.6 are analysis conditions, not proved detector limitations",
                             "a positive15.6 coincidence alone still needs order/endpoint; primaryfurtherdecay is unknown",
                             "source lowenergy ICC without parenttag cannot uniquely label sameE/samemultipole parent",
                             "Gaussian state-tag requirement is not existing gamma-detector resolution or experimental CI",
                             "actual tag implementation, tails, priors, calibration, efficiency and covariance are missing"])
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({k:result[k] for k in ["kind","check_count","passed","primary_support","evaluated_support","tag_design"]}))


if __name__=="__main__":
    main()
