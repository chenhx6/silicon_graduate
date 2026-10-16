#!/usr/bin/env python3
"""Typed transition identity, selected-graph paths and conditional RI bound.

Printed transition endpoints are inputs, not a fresh level-scheme fit. Graph
nonreachability is scoped to the selected edges, not experimental absence.
"""
from __future__ import annotations

import argparse
from decimal import Decimal as D
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02"


def paths(rows, start, finish, seen=()):
    if start == finish:
        return [seen]
    return [path for row in rows if row["parent_keV"] == start and row["id"] not in seen
            for path in paths(rows, row["daughter_keV"], finish, seen+(row["id"],))]


def joined(rows, sequence):
    by_id = {r["id"]:r for r in rows}
    return all(by_id[a]["daughter_keV"] == by_id[b]["parent_keV"]
               for a,b in zip(sequence,sequence[1:]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=RUN / "ding128i-lowenergy-typed-audit.json")
    args = parser.parse_args()
    p = RUN / "ding128i-lowenergy-typed-input.json"
    data = json.loads(p.read_text())
    checks = {}
    def check(name, value):
        checks[name] = bool(value)
        if not value:
            raise AssertionError(name)
    for role in ["thesis_source","paper_source"]:
        check(role+"_hash", hashlib.sha256((ROOT/data[role]["path"]).read_bytes()).hexdigest() == data[role]["sha256"])
    rows = data["rows"]
    by_id = {r["id"]:r for r in rows}
    energy_ids = {}
    for r in rows:
        energy_ids.setdefault(r["E_gamma_keV"],[]).append(r["id"])
    check("typed_IDs_unique_with_duplicate_energy", len(by_id)==9 and energy_ids["102.2"] == ["t102a","t102b"])
    check("energy_only_key_would_drop_transition", len({r["E_gamma_keV"]:r for r in rows}) == len(rows)-1)
    seq = ["t101","t764","t411","t102a"]
    check("source_four_step_chain_endpoint_join", joined(rows,seq))
    check("other102_cannot_replace_last_edge", not joined(rows,seq[:-1]+["t102b"]))
    chain_sum = sum((D(by_id[k]["E_gamma_keV"]) for k in seq),D(0))
    check("four_step_source_energy_sum", chain_sum == D("1379.2")
          == D(by_id[seq[0]]["parent_keV"])-D(by_id[seq[-1]]["daughter_keV"]))
    short = ["t101","t764"]
    check("866_crossover_matches_parallel_sum", joined(rows,short)
          and sum(D(by_id[k]["E_gamma_keV"]) for k in short)==D("866.0"))
    below756 = paths(rows,"285.2","183.0") + paths(rows,"285.2","167.4")
    check("selected_graph_756_daughter_has_two_terminal_branches", below756==[("t102a",),("t117",)])
    check("selected_graph_no_102b_path_from285", all("t102b" not in q for q in below756))
    check("same_parent102a_and117_exclusive_in_selected_graph", by_id["t102a"]["parent_keV"]==by_id["t117"]["parent_keV"]
          and by_id["t102a"]["daughter_keV"]!=by_id["t117"]["daughter_keV"])
    check("graph_nonreachability_not_experimental_absence", data["graph_completeness_claimed"] is False)
    conversions = {x["transition_id"]:x for x in data["conversion"]}
    check("ICC_attached_to_specific_rows", set(conversions)=={"t102a","t101"} and data["t102b_conversion"] is None)
    check("ICC_gate_and_purity_condition_retained", conversions["t102a"]["gates"]=="866.0"
          and conversions["t102a"]["conditioning"]=="117.8 assumed pure E2")
    strong, weak_min = F(563),F(79)
    fmin = weak_min/(strong+weak_min)
    check("conditional_fraction_lower_endpoint", fmin==F(79,642))
    check("lower_bound_not_weak_value_measurement", by_id["t102b"]["I_gamma_literal"]==">=79")
    required_for14 = strong*F(14,100)/(1-F(14,100))
    check("paper_rough14_compatible_with_fixedcenter_lower_bound", required_for14>=weak_min)
    check("no_actual_fraction_or_joint_cov_inferred", data["actual_component_fraction"] is None
          and data["actual_covariance"] is None and data["actual_net_counts"] is None)
    residuals = {r["id"]:D(r["E_gamma_keV"])-(D(r["parent_keV"])-D(r["daughter_keV"])) for r in rows}
    check("source_selected_energy_residuals_literal", residuals["t345"]==D("-.1")
          and all(v==0 for k,v in residuals.items() if k!="t345"))
    result = dict(kind="typed source graph/field contract, not experimental reconstruction or fraction fit",
                  checks=checks,check_count=len(checks),passed=all(checks.values()),inputs=data,
                  energy_to_typed_IDs=energy_ids,four_step_chain=seq,chain_sum_keV=chain_sum,
                  selected_graph_paths_below_756_daughter=below756,
                  central_energy_residuals_keV=residuals,
                  conditional_two_photon_component_fraction_lower_endpoint=fmin,
                  weak_component_RI_required_if_fraction14_and_strong563=required_for14,
                  blended_conversion_symbolic="(563*alpha_102a + W*alpha_102b)/(563+W), W>=79 only under declared intensity contract",
                  actual_alpha_102b=None,actual_component_fraction=None,
                  input_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
                  limitations=["source endpoint graph is an input, not independently fitted from raw coincidences",
                               "selected graph is not complete; missing path is not an experimental upper limit",
                               "photon fraction bound conditions on common scale and fixed strongcenter; not CL",
                               "quoted global error ranges and approximate10/14percent do not define a joint version-comparison test",
                               "no calibrated digitization of thesis Fig6.5 axis and no unknown ICC imputed",
                               "2010paper/theses treated as dependent acquisition, not independent replications"])
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2,default=str)+"\n")
    print(json.dumps({k:result[k] for k in ["kind","check_count","passed","four_step_chain","conditional_two_photon_component_fraction_lower_endpoint"]},default=str))


if __name__ == "__main__":
    main()
