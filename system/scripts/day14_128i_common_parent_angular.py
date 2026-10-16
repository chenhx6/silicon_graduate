#!/usr/bin/env python3
"""Pure-L1 common-parent angular constraint with declared point/gate conditions.

CG weights and photon transversality construct radiation coefficients directly.
No unobserved-U propagation is used as a selected-gamma response. No data fit.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from math import cos, radians
from pathlib import Path

from day14_unobserved_feeding_transfer import cg_squared

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/"outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02"


def coefficients(ti,tf):
    out=[]
    probabilities=[]
    for mi in range(-ti,ti+1,2):
        probs={q:F(0) for q in [-2,0,2]}
        for mf in range(-tf,tf+1,2):
            q=mi-mf
            c=cg_squared(tf,2,ti,mf,q,mi)
            if c:
                probs[q]+=c
        probabilities.append(probs)
        # Normalized transverse pure-L1 angular functions:
        # q0: 1-P2; q+-1: 1+P2/2. No phase convention issue for a pure L.
        out.append(-probs[0]+(probs[-2]+probs[2])/2)
    return out,probabilities


def p2(x):
    return (3*x*x-1)/2


def ratio(a,s,l):
    return (1+a*s)/(1+a*l)


def inverse_ratio(r,s,l):
    return (r-1)/(s-r*l)


def mixture(ti,w,tm):
    return [(1-w)/F(ti+1)+(w if m==tm==0 else w/2 if tm and abs(m)==tm else 0)
            for m in range(-ti,ti+1,2)]


def moment(v,p):
    return sum((a*b for a,b in zip(v,p)),F(0))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output",type=Path,default=RUN/"128i-common-parent-angular-audit.json")
    args=p.parse_args()
    ipath=RUN/"128i-common-parent-angular-input.json"
    data=json.loads(ipath.read_text())
    checks={}
    def check(name,condition):
        checks[name]=bool(condition)
        if not condition:
            raise AssertionError(name)
    for name in ["source_primary","source_reaction"]:
        v=data[name]
        check(name+"_hash",hashlib.sha256((ROOT/v["path"]).read_bytes()).hexdigest()==v["sha256"])
    ti=data["parent_spin_twice"]
    v6,k6=coefficients(ti,data["daughter_anchor_twice"])
    v7,k7=coefficients(ti,data["daughter_counterexample_twice"])
    for name,k,v in [("7to6",k6,v6),("7to7",k7,v7)]:
        check(name+"_positive_normalized_CG_emission_weights",all(min(q.values())>=0 and sum(q.values())==1 for q in k))
        check(name+"_unoriented_radiation_isotropic",sum(v)==0)
        check(name+"_positive_angular_functions_at_declared_points",all(1+a*p2(x)>=0 for a in v for x in [F(-1),F(-1,2),F(0),F(1,2),F(1)]))
    scale=F(-13,8)
    check("all_Mi_exact_opposite_coefficient_relation",all(b==scale*a for a,b in zip(v6,v7)))
    check("m0_complete_alignment_coefficients",v6[ti//2]==F(-4,13) and v7[ti//2]==F(1,2))
    check("positive_population_ranges",min(v6)==F(-4,13) and max(v6)==F(1,2)
          and min(v7)==F(-13,16) and max(v7)==F(1,2))
    s,l=p2(cos(radians(37))),p2(cos(radians(90)))
    check("backward37_symmetric_even_rank",abs(s-p2(cos(radians(143))))<1e-15)
    check("ratio_positive_denominators_and_monotonicity",s>l and all(1+float(a)*l>0 for a in v6+v7))
    r314,r255=float(data["source_R314_center"]),float(data["source_R255_center"])
    a314,a255=inverse_ratio(r314,s,l),inverse_ratio(r255,s,l)
    check("inverse_ratio_roundtrip",abs(ratio(a314,s,l)-r314)<1e-14 and abs(ratio(a255,s,l)-r255)<1e-14)
    check("printed_centers_violate_opposite_sign_necessary_condition",(r314-1)*(r255-1)>0)
    check("same_sequence_also_not_exact_central_equality",r314!=r255)
    w=F(data["chosen_m0_plus_uniform_weight"])
    common=mixture(ti,w,0)
    other=mixture(ti,w,ti)
    check("chosen_parent_densities_strictly_positive_normalized",min(common)>0 and min(other)>0 and sum(common)==sum(other)==1)
    aa,bb=moment(v6,common),moment(v7,common)
    check("nonzero_common_density_witness_coefficients",aa==F(-2,65) and bb==F(1,20))
    common_r314,common_r255=ratio(float(aa),s,l),ratio(float(bb),s,l)
    check("chosen_H7_pair_inside_quoted_marginal_box",abs(common_r314-r314)<float(data["source_R314_quoted_halfwidth"])
          and abs(common_r255-r255)<float(data["source_R255_quoted_halfwidth"]))
    check("chosen_H6_pair_inside_same_marginal_box",abs(common_r314-r314)<float(data["source_R314_quoted_halfwidth"])
          and abs(common_r314-r255)<float(data["source_R255_quoted_halfwidth"]))
    check("common_density_opposite_ratio_signs",(common_r314-1)*(common_r255-1)<0)
    different_a255=moment(v7,other)
    different_r255=ratio(float(different_a255),s,l)
    check("different_postselection_breaks_necessary_sign_relation",(common_r314-1)*(different_r255-1)>0 and different_a255!=scale*aa)
    check("no_actual_gate_delta_Cov_or_full_three_line_fit",all(data[k] is None for k in ["actual_perline_gate_ids","actual_mixing_ratios","actual_detector_response","actual_covariance","actual58_parent_distribution"])
          and data["full_three_line_fit"] is False and data["spin_reassignment"] is None)
    result=dict(kind="conditional common-parent pureL1 radiation constraint, no actual angular fit",
                checks=checks,check_count=len(checks),passed=all(checks.values()),inputs=data,
                point_geometry=dict(P2S=s,P2L=l),exact_coefficient_scale=str(scale),
                radiation_a2_by_parent_Mi=dict(J7to6=v6,J7to7=v7),
                complete_alignment_a2=dict(J7to6="-4/13",J7to7="1/2"),
                printed_center_control=dict(a314=a314,a255=a255,H7_a255_if_314_center= float(scale)*a314,
                                            H7_R255_if_314_center=ratio(float(scale)*a314,s,l),
                                            H6_exact_center_equality=False,actual_hypothesis_exclusion=False),
                chosen_positive_parent_density=common,
                marginal_box_witness=dict(a314=str(aa),a255_H7=str(bb),R314=common_r314,R255_H7=common_r255,
                                          R255_H6=common_r314,confidence_interpretation=None,full_three_line_fit=False),
                chosen_different_postselection=dict(other_density=other,a255=str(different_a255),R255=different_r255,
                                                   actual_gate_effect_claimed=False),
                actual_angular_likelihood_comparison=None,new_spin_assignment=None,
                input_sha256=hashlib.sha256(ipath.read_bytes()).hexdigest(),
                CG_helper_sha256=hashlib.sha256((ROOT/"system/scripts/day14_unobserved_feeding_transfer.py").read_bytes()).hexdigest(),
                limitations=["pureL1/delta0 and point37/90/f_ADO1 are explicit mathematical baseline, not measured conditions",
                             "same parent level does not guarantee same postselected population for different gates",
                             "quoted marginal halfwidth box is not a joint likelihood or confidence region",
                             "E2 mixing/rank4/interference, geometry and energy-dependent response can change the constraint",
                             "58line from the other parent is not modeled; witness not complete feeding or three-line fit",
                             "sign/central mismatch is not an actual experimental exclusion or preferred spin"])
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2,default=str)+"\n")
    print(json.dumps({k:result[k] for k in ["kind","check_count","passed","exact_coefficient_scale","printed_center_control","marginal_box_witness","chosen_different_postselection"]},default=str))


if __name__=="__main__":
    main()
