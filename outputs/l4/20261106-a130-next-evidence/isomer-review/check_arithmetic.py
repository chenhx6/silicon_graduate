"""Interpretation audit of frozen isomer results; no model imports or reruns."""
import sys
sys.dont_write_bytecode=True
from collections import defaultdict
from datetime import datetime,timezone
import hashlib
import json
import math
from pathlib import Path

ROOT=Path("/workspace/wiki")
BENCH=ROOT/"outputs/l4/20261106-a130-next-evidence/isomer-benchmark"
OUT=Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def relative(a,b):
    return abs(a-b)/max(abs(a),abs(b),1e-300)


def main():
    names=[
        "protocol.json","results.json","energy-mapping-frozen.json",
        "decay-width-protocol.json","decay-width-results.json",
        "predictions.csv","decay-width-summary.csv",
        "run_benchmark.py","run_decay_widths.py",
    ]
    hashes={str((BENCH/n).relative_to(ROOT)):sha(BENCH/n) for n in names}
    p=json.loads((BENCH/"protocol.json").read_text())
    r=json.loads((BENCH/"results.json").read_text())
    mapping=json.loads((BENCH/"energy-mapping-frozen.json").read_text())
    wp=json.loads((BENCH/"decay-width-protocol.json").read_text())
    w=json.loads((BENCH/"decay-width-results.json").read_text())
    assert r["protocol_sha256"]==sha(BENCH/"protocol.json")
    assert r["producer_sha256"]==sha(BENCH/"run_benchmark.py")
    assert r["energy_mapping_record_sha256"]==sha(BENCH/"energy-mapping-frozen.json")
    assert w["protocol_sha256"]==sha(BENCH/"decay-width-protocol.json")
    assert w["producer_sha256"]==sha(BENCH/"run_decay_widths.py")
    assert wp["base_protocol_sha256"]==r["protocol_sha256"]
    assert wp["base_results_sha256"]==sha(BENCH/"results.json")
    obs=r["experimental"]
    unit_fm4=(1/(4*math.pi))*(3/5)**2*(1.2*obs["A"]**(1/3))**4
    unit_b2=unit_fm4/10000
    assert relative(unit_b2,r["Weisskopf_unit_down_e2b2"])<1e-12
    b_errors=[];rev_errors=[]
    for row in r["rows"]:
        b=row["signed_RME_eb"]**2/(obs["initial_two_J"]+1)
        b_errors.append(relative(b,row["Bdown_e2b2"]))
        assert relative(row["Bdown_e2b2"]/unit_b2,row["Bdown_Wu"])<1e-12
        rev_errors.append(abs(row["Bup_reverse_e2b2"]/row["Bdown_e2b2"]-20/16))
    C=wp["rate_coefficient"]["value"]
    groups=defaultdict(list);rate_errors=[]
    for branch in w["branches"]:
        assert branch["photon_model_MeV"]>0
        assert abs(branch["final_two_J"]-19)<=4
        b=branch["signed_RME_eb"]**2/20
        assert relative(b,branch["Bdown_e2b2"])<1e-12
        rate=C*branch["photon_model_MeV"]**5*b
        alternate=(C/10000)*branch["photon_model_MeV"]**5*(b*10000)
        alternate_keV=(C/1e15)*(1000*branch["photon_model_MeV"])**5*b
        assert relative(rate,alternate)<1e-12 and relative(rate,alternate_keV)<1e-12
        rate_errors.append(relative(rate,branch["E2_gamma_rate_s_inverse"]))
        groups[(branch["operator"],branch["initial_ordinal"])].append(branch)
    summary={(row["operator"],row["initial_ordinal"]):row for row in w["rows"]}
    for key,branches in groups.items():
        row=summary[key]
        rate=sum(x["E2_gamma_rate_s_inverse"] for x in branches)
        assert len(branches)==row["open_E2_branch_count"]
        assert relative(rate,row["sum_E2_gamma_rate_s_inverse"])<1e-12
        assert abs(sum(x["conditional_E2_only_radiative_fraction"] for x in branches)-1)<1e-12
        bound_ns=math.log(2)*1e9/rate
        assert relative(bound_ns,row["model_scheme_half_life_upper_bound_ns"])<1e-12
    operators=sorted({row["operator"] for row in w["rows"]})
    assert len(operators)==7 and len(w["rows"])==14 and len(r["rows"])==28
    selected=[
        ("primary","19half_1_to_15half_1"),
        ("primary","19half_1_to_15half_2"),
        ("Q136_plus_007_splus","19half_1_to_15half_2"),
        ("Q136_plus_007_splus","19half_1_to_15half_1"),
    ]
    comparisons=[]
    for op,pair in selected:
        row=next(x for x in r["rows"] if x["operator"]==op and x["pair"]==pair)
        branch=next(x for x in groups[(op,row["parent_ordinal"])]
                    if x["final_two_J"]==15 and x["final_ordinal"]==row["daughter_ordinal"])
        eratio=row["photon_model_MeV"]/(obs["photon_energy_keV"]/1000)
        bratio=row["Bdown_Wu"]/obs["Bdown_Wu"]
        comparisons.append({
            "operator":op,"pair":pair,"model_Egamma_keV":1000*row["photon_model_MeV"],
            "model_Bdown_Wu":row["Bdown_Wu"],"B_ratio_to_observed":bratio,
            "Egamma_ratio_to_observed":eratio,"Egamma_fifth_power_factor":eratio**5,
            "gamma_rate_ratio_to_same_experiment_derived_selected_gamma_rate":bratio*eratio**5,
            "model_selected_branch_gamma_rate_s_inverse":branch["E2_gamma_rate_s_inverse"],
            "conditional_fraction_of_model_E2_gamma_sum":branch["conditional_E2_only_radiative_fraction"],
            "parent_model_upper_half_life_ns":
                summary[(op,row["parent_ordinal"])]["model_scheme_half_life_upper_bound_ns"],
        })
    near=next(x for x in comparisons if x["operator"]=="Q136_plus_007_splus"
              and x["pair"]=="19half_1_to_15half_2")
    maximum=max(w["rows"],key=lambda x:x["model_scheme_half_life_upper_bound_ns"])
    record={
        "checked_at_actual_utc":datetime.now(timezone.utc).isoformat(),
        "scope":"Frozen artifact provenance and arithmetic only; no kernel, fit, source reconstruction or model rerun.",
        "input_sha256":hashes,
        "unit_checks":{
            "one_downward_E2_Wu_e2fm4":unit_fm4,"one_downward_E2_Wu_e2b2":unit_b2,
            "RME_initial_denominator":20,"reverse_RME_denominator":16,
            "reverse_up_B_over_down_B":20/16,
            "declared_rate_C_MeV_e2b2":C,"equivalent_C_MeV_e2fm4":C/10000,
            "equivalent_C_keV_e2b2":C/1e15,
            "half_life_ns_formula":"ln(2)*1e9 / sum_gamma_rates_s_inverse",
            "rate_constant_boundary":"Numerical value follows the frozen declared convention; no atomic ICC or observed total lifetime was reconstructed.",
        },
        "counts":{"strength_rows":len(r["rows"]),"distinct_operators":len(operators),
                  "parent_ordinals":[0,1],"width_rows":len(w["rows"]),"stored_open_branches":len(w["branches"])},
        "maximum_B_relative_error":max(b_errors),
        "maximum_reciprocity_ratio_error":max(rev_errors),
        "maximum_branch_rate_relative_error":max(rate_errors),
        "all_group_sums_half_lives_fractions_and_unit_rescalings_match":True,
        "energy_mapping":mapping,
        "selected_comparisons":comparisons,
        "conditional_selected_B_check":{
            "B_Wu":near["model_Bdown_Wu"],"quoted_interval_Wu":[obs["Bdown_Wu"]-obs["Bdown_quoted_margin_Wu"],obs["Bdown_Wu"]+obs["Bdown_quoted_margin_Wu"]],
            "inside_quoted_interval":False,
            "difference_in_units_of_quoted_margin":
                (near["model_Bdown_Wu"]-obs["Bdown_Wu"])/obs["Bdown_quoted_margin_Wu"],
            "not_a_p_value_or_complete_uncertainty_comparison":True,
        },
        "largest_model_scheme_upper_half_life_row":maximum,
        "observational_dependence":"Quoted B(E2) and 589ns half-life arise from the same experiment; not two independent residuals.",
        "q3_scope":"For initial J=11/2, both intermediate spins in the cubic loop are 7/2 through 15/2. The 19/2-to-15/2 element is outside that loop.",
        "Planck_source_replay":"Pending per parent instruction; no fidelity conclusion is drawn.",
    }
    changed=[n for n,h in hashes.items() if sha(ROOT/n)!=h]
    assert not changed,changed
    record["frozen_benchmark_files_changed_during_review"]=changed
    with (OUT/"arithmetic-checks.json").open("x") as f:
        f.write(json.dumps(record,ensure_ascii=False,indent=2)+"\n")
    for x in comparisons:print(json.dumps(x,indent=2))
    print("NEAR",record["conditional_selected_B_check"])
    print("MAXIMUM_BOUND",maximum)


if __name__=="__main__":
    main()
