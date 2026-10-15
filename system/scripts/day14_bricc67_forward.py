#!/usr/bin/env python3
"""Offline replay of captured BrIccFO inputs and the conditional 67Ga ledger.

No network queries or writes to raw are performed. Captured provider tables
are theoretical data. The evaluation's blank CC fields stay unchanged.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

from day14_ensdf_crosswalk import uncertainty
from day14_ensdf67_strength_crosswalk import conditional_strength


def audit(snapshot, source):
    checks = {}

    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            raise AssertionError(name)

    inputs = snapshot["model_inputs"]
    for row in inputs:
        name = row["case"]
        check(name+"_model_Z_version", row["Z"] == 31 and
              row["model"] == "BrIccFO" and
              row["version"] == "BrIccS v2.3 (9-Dec-2011)")
        tot = [r for r in row["all_printed_rows"] if r and r[0] == "Tot"]
        check(name+"_one_captured_Tot", len(tot) == 1)
        check(name+"_numeric_and_error_replay", float(tot[0][2]) ==
              row["coefficients"]["Tot"]["value"] and
              uncertainty(tot[0][2],tot[0][3][1:-1]) ==
              row["coefficients"]["Tot"]["quoted_error"])
        check(name+"_K_not_total", row["coefficients"]["Tot"]["value"] >
              row["coefficients"]["K"]["value"] > 0)
    coefficient = {r["case"]:r["coefficients"]["Tot"]["value"] for r in inputs}
    check("four_captured_theory_values", coefficient == {
        "168p8-M1":.0175,"168p8-E2":.0976,
        "958p01-E2":.000358,"958p01-M3":.001513})
    ratio = source["independent_marginal_approximation"]["photon_ratio"]
    T = source["half_life_input_ps"]
    E = source["selected_source_records"]["adopted"]["strong958"]["energy_keV"]/1000
    controls = []
    for delta in [0.,.01,.02]:
        strong = (coefficient["958p01-E2"]+delta*delta*
                  coefficient["958p01-M3"])/(1+delta*delta)
        for mode, weak in [("M1",coefficient["168p8-M1"]),
                           ("E2",coefficient["168p8-E2"])]:
            value = conditional_strength(E,T,ratio,strong,weak,delta,
                                         complete_inventory_assumed=True)
            p1 = 1/value["rate_ledger_denominator"]
            p2 = ratio*p1
            check(f'd{delta}_{mode}_complete_chosen_ledger', math.isclose(
                p1*(1+strong)+p2*(1+weak),1))
            check(f'd{delta}_{mode}_atomic_correction_direction', value[
                "B_E2_WU"] < conditional_strength(E,T,ratio,0.,0.,delta,
                complete_inventory_assumed=True)["B_E2_WU"])
            controls.append(dict(delta_chosen_not_a_hard_bound=delta,
                                 weak_gamma_lowrank_hypothesis=mode,
                                 strong_CC_eff_model=strong,weak_CC_model=weak,
                                 photon_probability958_conditional=p1,
                                 total_branch168_conditional=p2*(1+weak),
                                 relative_to_zeroIC_delta0=value["B_E2_WU"]/source[
                                     "conditional_two_observed_gamma_zeroIC"]["B_E2_WU"]-1,
                                 **value))
    pure = [r for r in controls if r["delta_chosen_not_a_hard_bound"] == 0]
    check("lowrank_weak_mode_range_small", max(r["B_E2_WU"] for r in pure)-
          min(r["B_E2_WU"] for r in pure) < .002)
    check("lowrank_ICC_below_chosen55p67_threshold", max(
        coefficient["168p8-M1"],coefficient["168p8-E2"]) < source[
            "chosen_ccweak_for10percent_change"])
    hypothetical_ratio = ratio*(E/.1688)**5
    check("weak_photon_can_have_larger_conditional_E2_strength",
          hypothetical_ratio > 10)
    result = dict(snapshot)
    result.update(forward_controls=controls,
                  conditional_both_pureE2_Bweak_over_Bstrong=hypothetical_ratio,
                  checks=checks,checks_passed=len(checks),
                  replay_kind="captured provider-table offline replay, not experimental fit")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot",type=Path,required=True)
    parser.add_argument("--source-data",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args = parser.parse_args()
    result = audit(json.loads(args.snapshot.read_text()),
                   json.loads(args.source_data.read_text()))
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(dict(checks_passed=result["checks_passed"],
                          all_checks_true=all(result["checks"].values()),
                          output=str(args.output))))


if __name__ == "__main__":
    main()
