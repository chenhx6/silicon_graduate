#!/usr/bin/env python3
"""Literal 128I local-energy checks and conditional spin-set enumeration.

Source ADO interpretation is an input, not a universal ratio threshold or a
likelihood here. Surviving sets are selection-rule compatibility, not evidence
for an alternative experimental spin assignment.
"""
from __future__ import annotations

import argparse
from decimal import Decimal as D
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02"


def radiative_allowed(ji, jf, multipole):
    return multipole >= 1 and abs(ji-jf) <= multipole <= ji+jf


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path, default=RUN / "ding128i-local-evidence-audit.json")
    args = p.parse_args()
    ipath = RUN / "ding128i-local-evidence-input.json"
    data = json.loads(ipath.read_text())
    checks = {}
    def check(name, value):
        checks[name] = bool(value)
        if not value:
            raise AssertionError(name)
    check("source_hash", hashlib.sha256((ROOT/data["source"]["path"]).read_bytes()).hexdigest() == data["source"]["sha256"])
    nodes = {n["id"]:n for n in data["nodes"]}
    residuals = []
    for r in data["rows"]:
        delta = D(nodes[r["parent"]]["E_keV"])-D(nodes[r["daughter"]]["E_keV"])
        residuals.append(dict(id=r["id"], transition=r["parent"]+"->"+r["daughter"],
                              E_gamma_keV=r["E_gamma_keV"], level_difference_keV=delta,
                              gamma_minus_level_difference_keV=D(r["E_gamma_keV"])-delta,
                              R_ADO_literal=r["R_ADO_literal"], source=r["source"]))
    check("literal_energy_residuals_retained", [x["gamma_minus_level_difference_keV"] for x in residuals] == [D(0), D("-.3"), D("-.1")])
    triangle = D("255.6")+D("58.5")-D("314.3")
    check("triangle_central_residual_not_silently_zeroed", triangle == D("-.2"))
    # Energy uncertainties are not per-row sigmas; these are only range arithmetic.
    possible_triangle_sum_halfwidth = [3*D(v) for v in data["energy_uncertainty_range_keV"]]
    check("central_triangle_below_even_smallest_sum_halfwidth", abs(triangle) <= min(possible_triangle_sum_halfwidth))
    check("figure_table_label_difference_preserved", data["figure_node_labels_keV"] == {"L226":"226.0","L482":"481.7"})
    anchor, feeder = data["anchor_J_given"], data["common_feeder_J_given"]
    h0 = {j for j in range(0,15) if j-anchor == 0 and radiative_allowed(j,anchor,1)}
    h2 = {j for j in range(0,15) if abs(j-anchor) == 2 and radiative_allowed(j,anchor,2)}
    triangle_only = {j for j in h0|h2 if radiative_allowed(feeder,j,1) and radiative_allowed(feeder,anchor,1)}
    check("H0_H2_declared_sets", h0 == {6} and h2 == {4,8})
    check("dipole_companions_allow_both_J6_and_J8", triangle_only == {6,8})
    # There is no exact selection rule requiring spin to fall with energy.
    check("J7_to_J8_dipole_allowed_while_energy_falls", radiative_allowed(7,8,1))
    reaction_prior = {j for j in triangle_only if feeder >= j >= anchor}
    historical_prior = triangle_only & set(data["historical_prior_J_values"])
    check("explicit_nondecreasing_excitation_spin_prior_selects6", reaction_prior == {6})
    check("separate_historical_prior_selects6", historical_prior == {6})
    check("historical_primary_not_newly_verified", data["historical_primary_ref_bodies_checked"] is False)
    check("all_adopted_spins_and_parities_tentative", all(n["tentative"] for n in nodes.values()))
    check("daughter_isomer_lifetime_not_parent_lifetime", nodes["L167"]["half_life_ns"] == "175"
          and nodes["L226"]["half_life_ns"] is None and nodes["L482"]["half_life_ns"] is None)
    check("no_ratio_threshold_or_likelihood_used", all(r["R_ADO_literal"] for r in data["rows"])
          and data["actual_angular_response"] is None and data["actual_joint_covariance"] is None)
    check("relative_intensity_not_branch_probability", "866.0-keV = 100" in data["relative_intensity_reference"])
    check("no_raw_counts_or_actual_spin_inferred", data["actual_net_gate_counts"] is None
          and data["true_spin_inferred_by_this_task"] is None)
    result = dict(kind="published local scheme plus conditional selection-rule compatibility audit",
                  checks=checks,check_count=len(checks),passed=all(checks.values()),inputs=data,
                  central_energy_crosscheck=residuals,triangle_residual_keV=triangle,
                  sum_three_possible_energy_halfwidth_range_keV=possible_triangle_sum_halfwidth,
                  no_chi2_or_confidence_from_ranges=True,
                  spin_sets=dict(H0=sorted(h0),H2_before_companions=sorted(h2),
                                 exact_triangles_with_given_parent7_anchor6=sorted(triangle_only),
                                 plus_source_reaction_spin_trend=sorted(reaction_prior),
                                 plus_historical_5_6_7_prior=sorted(historical_prior)),
                  input_sha256=hashlib.sha256(ipath.read_bytes()).hexdigest(),
                  new_experimental_assignment=None,
                  limitations=["given feeder7/anchor6 and source dipole interpretation remain conditioned inputs",
                               "candidate J8 is compatibility counterexample, not evidence or a proposed reassignment",
                               "reaction spin trend is a physical prior, not an exact selection rule",
                               "historical reference bodies, raw component spectra, timing and covariance not recovered",
                               "range-only energy/intensity errors do not define a likelihood or CI",
                               "daughter isomer lifetime cannot supply the two parents' transition rates"])
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2,default=str)+"\n")
    print(json.dumps({k:result[k] for k in ["kind","check_count","passed","triangle_residual_keV","spin_sets"]},default=str))


if __name__ == "__main__":
    main()
