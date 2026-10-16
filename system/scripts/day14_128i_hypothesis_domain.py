#!/usr/bin/env python3
"""Necessary spin sets under explicit restricted and expanded hypotheses.

No angular response, delta, likelihood or experimental reassignment is fitted.
The upper/anchor spins and cross-source line identity are conditioned inputs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from day14_ding128i_local_evidence import radiative_allowed

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/"outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02"


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output",type=Path,default=RUN/"128i-hypothesis-domain-audit.json")
    args=p.parse_args()
    ipath=RUN/"128i-hypothesis-domain-input.json"
    data=json.loads(ipath.read_text())
    checks={}
    def check(name,condition):
        checks[name]=bool(condition)
        if not condition:
            raise AssertionError(name)
    for name in ["source_primary","capture_object","reaction_object"]:
        v=data[name]
        check(name+"_hash",hashlib.sha256((ROOT/v["path"]).read_bytes()).hexdigest()==v["sha256"])
    upper,anchor=data["upper_spin_given"],data["anchor_spin_given"]
    universe=range(0,upper+anchor+3)
    restricted={j for j in universe if (j==anchor and radiative_allowed(j,anchor,1))
                or (abs(j-anchor)==2 and radiative_allowed(j,anchor,2))}
    expanded={j for j in universe if radiative_allowed(j,anchor,1)}
    companion=lambda j:radiative_allowed(upper,j,1) and radiative_allowed(upper,anchor,1)
    trend=lambda j:anchor<=j<=upper
    restricted_comp={j for j in restricted if companion(j)}
    expanded_comp={j for j in expanded if companion(j)}
    restricted_trend={j for j in restricted_comp if trend(j)}
    expanded_trend={j for j in expanded_comp if trend(j)}
    stretched255={j for j in expanded_trend if abs(upper-j)==1}
    check("original_restricted_domain_reproduced",restricted=={4,6,8} and restricted_comp=={6,8} and restricted_trend=={6})
    check("M1_component_gives_historical_allowedset",expanded=={5,6,7}==set(data["capture_allowed_set_if_anchor6"]))
    check("expanded_M1_family_with_two_dipoles",expanded_comp=={6,7})
    check("nondecreasing_reaction_trend_not_unique_in_expanded_family",expanded_trend=={6,7})
    check("adding_255_stretched_is_extra_constraint",stretched255=={6} and stretched255!=expanded_trend)
    check("J7_counterexample_obeys_all_generic_triangles",radiative_allowed(7,6,1) and radiative_allowed(7,7,1))
    check("M1_and_E2_components_both_allowed_for_expanded_survivors",all(radiative_allowed(j,anchor,1) and radiative_allowed(j,anchor,2) for j in expanded_comp))
    check("derived_historical_allowedset_not_extra_independent_measurement",expanded_comp & set(data["capture_allowed_set_if_anchor6"])==expanded_comp)
    check("lineidentity_and_anchors_are_conditions",data["crosssource58_identity_is_explicit_condition"] is True)
    check("no_unmeasured_delta_response_or_reassignment",data["actual_delta58"] is None and data["actual_delta255"] is None
          and data["actual_population_response_covariance"] is None and not data["source_spin6_reassigned"])
    result=dict(kind="conditional necessary-spin-set hypothesis-domain audit; no actual ADO fit",
                checks=checks,check_count=len(checks),passed=all(checks.values()),inputs=data,
                spin_sets=dict(restricted58=sorted(restricted),restricted_plus_generic_companions=sorted(restricted_comp),
                               restricted_plus_trend=sorted(restricted_trend),
                               M1_present_family=sorted(expanded),expanded_plus_generic_companions=sorted(expanded_comp),
                               expanded_plus_trend=sorted(expanded_trend),
                               expanded_plus_additional_stretched255=sorted(stretched255)),
                new_experimental_spin_assignment=None,actual_angular_likelihood_comparison=None,
                input_sha256=hashlib.sha256(ipath.read_bytes()).hexdigest(),
                helper_sha256=hashlib.sha256((ROOT/"system/scripts/day14_ding128i_local_evidence.py").read_bytes()).hexdigest(),
                limitations=["given upper7/anchor6 and matched58capture identity are conditioned inputs",
                             "M1 presence is a limited family, not an exhaustive all-multipole or lineidentity search",
                             "general mixedDeltaI1 warning does not show actual58 or255 is mixed",
                             "survivingJ7 is a kinematic counterexample, not a demonstrated angular-data fit",
                             "stretched255 must be independently constrained, not proved circularly from the desiredJ6",
                             "parent/finalEx identification alone does not measure spin; actual response and jointCov missing"])
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({k:result[k] for k in ["kind","check_count","passed","spin_sets"]}))


if __name__=="__main__":
    main()
