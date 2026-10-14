#!/usr/bin/env python3
"""Read selected fixed-column ENSDF records without replacing source assignments."""
from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation
import hashlib
import json
from pathlib import Path
import re

import numpy as np


def number(text):
    try:
        return float(text.strip()) if text.strip() else None
    except ValueError:
        return None


def uncertainty(value, digits):
    if not re.fullmatch(r"\d+", digits.strip()):
        return None
    try:
        return float(Decimal(digits.strip()) * Decimal(10) ** Decimal(value.strip()).as_tuple().exponent)
    except InvalidOperation:
        return None


def records(path):
    lines = path.read_text().splitlines()
    levels, gammas = [], []
    current_level, current_gamma = None, None
    for line_number, raw in enumerate(lines, 1):
        line = raw.ljust(80)
        if line[:5] != "193BI":
            continue
        if line[5:7] == "  " and line[7] == "L":
            current_level = {"line":line_number,"energy_expression":line[9:19].strip(),
                             "energy_keV":number(line[9:19]),
                             "energy_uncertainty_keV":uncertainty(line[9:19],line[19:21]),
                             "Jpi":line[21:39].strip(),"half_life_text":line[39:49].strip(),
                             "half_life_uncertainty_digits":line[49:55].strip(),"raw":raw,"comments":[]}
            levels.append(current_level)
            current_gamma = None
        elif line[5:7] == "  " and line[7] == "G":
            current_gamma = {"line":line_number,"energy_expression":line[9:19].strip(),
                             "energy_keV":number(line[9:19]),
                             "energy_uncertainty_keV":uncertainty(line[9:19],line[19:21]),
                             "RI":number(line[21:29]),"RI_uncertainty":uncertainty(line[21:29],line[29:31]),
                             "multipolarity":line[31:41].strip(),"mixing_ratio_text":line[41:49].strip(),
                             "CC":number(line[55:62]),"parent":current_level,"raw":raw,"comments":[]}
            gammas.append(current_gamma)
        elif line[7] == "G" and current_gamma is not None:
            current_gamma["comments"].append({"line":line_number,"text":raw})
        elif line[7] == "L" and current_level is not None:
            current_level["comments"].append({"line":line_number,"text":raw})
    return lines, levels, gammas


def audit(adopted, reaction, fixture):
    checks = {}
    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            raise AssertionError(name)
    aa, al, ag = records(adopted)
    rr, rl, rg = records(reaction)
    check("adopted_object_identity", "ADOPTED LEVELS, GAMMAS" in aa[1])
    check("reaction_object_identity", "165HO(32S,4NG)" in rr[1] and "2015HE27" in rr[1])
    check("adopted_2019_half_life_revision", any("17-Jul-2019" in s for s in aa))
    check("reaction_2017_cutoff", any("CUT=31-Mar-2017" in s for s in rr))
    check("evaluation_explicit_quadrature", any("0.3 keV added in quadrature" in s for s in rr))
    check("evaluation_explicit_LS_anchor", any("305 keV level holding" in s for s in rr))
    # A numeric energy matcher is used only for these source-identified seven lines.
    def match(gs, energy):
        result = [g for g in gs if g["energy_keV"] is not None and abs(g["energy_keV"]-energy)<1e-7]
        if len(result) != 1:
            raise ValueError((energy,"not a unique gamma identity",len(result)))
        return result[0]
    crosswalk = []
    for row in fixture["transitions"]:
        ga, gr = match(ag,row["energy_keV"]),match(rg,row["energy_keV"])
        check("same_energy_"+row["id"], ga["energy_keV"]==gr["energy_keV"]==row["energy_keV"])
        check("reported_gamma_error_point3_"+row["id"], ga["energy_uncertainty_keV"]==gr["energy_uncertainty_keV"]==.3)
        check("reaction_intensity_scale_"+row["id"], np.isclose(gr["RI"],.1*row["relative_intensity"]))
        check("reaction_intensity_error_scale_"+row["id"], np.isclose(gr["RI_uncertainty"],.1*row["intensity_error"]))
        check("selected_multipolarity_retained_"+row["id"], ga["multipolarity"]==gr["multipolarity"]==row["assigned_multipolarity"])
        check("selected_CC_is_present_"+row["id"], ga["CC"] is not None and ga["CC"]>0)
        check("no_higher_parent_tau_in_selected_record_"+row["id"], not ga["parent"]["half_life_text"])
        crosswalk.append({"paper_line_id":row["id"],"paper_parent_rounded_keV":fixture["levels"][row["parent"]]["rounded_keV"],
                          "adopted":ga,"reaction":gr,
                          "parentage_from_selected_source":True,"not_independent_measurements":True})
    selected_level_energies = [605.53,928.93,1228.13,1555.30,1875.1]
    selected_levels = []
    for energy in selected_level_energies:
        ls=[x for x in al if x["energy_keV"] is not None and abs(x["energy_keV"]-energy)<1e-7]
        check("unique_level_"+str(energy),len(ls)==1)
        selected_levels.extend(ls)
    bandhead=selected_levels[0]
    check("bandhead_half_life_not_mean_lifetime",bandhead["half_life_text"]=="153 NS")
    check("bandhead_original_reference_present",any("2004Ni06" in x["text"] for x in bandhead["comments"]))
    # Preserve the float coordinate X; do not quietly substitute a zero level.
    sd=[x for x in al if "X" in x["energy_expression"]]
    check("fourteen_floating_SD_levels",len(sd)==14)
    check("SD_numeric_conversion_is_blocked",all(x["energy_keV"] is None for x in sd))
    candidate=match(rg,1836.0)
    check("candidate_link_remains_unplaced",candidate["parent"] is None)
    q_lines=[]
    for energy in [393.4,394.0]:
        g=match(rg,energy)
        check("doublet_only_Q_"+str(energy),g["multipolarity"]=="Q")
        check("negative_POL_conflict_documented_"+str(energy),any("consistent with (E2)" in s["text"] for s in g["comments"]))
        check("doublet_order_not_established_"+str(energy),any("not established" in s["text"] for s in g["comments"]))
        q_lines.append(g)
    weak=match(rg,352.3)
    check("weak352_multipolarity_left_blank",weak["multipolarity"]=="")
    check("weak352_table_figure_discrepancy_documented",any("inconsistent with (15/2-)" in x["text"] for x in weak["comments"]))
    # These are conditional fractions for the two reported pure-M1/pure-E2 channels.
    branching=[]
    for m1energy,e2energy in [(299.2,622.4),(327.4,626.2),(319.8,646.9)]:
        m,e=match(ag,m1energy),match(ag,e2energy)
        total=m["RI"]*(1+m["CC"])+e["RI"]*(1+e["CC"])
        fractions={"M1_photon":m["RI"]/total,"E2_photon":e["RI"]/total,
                   "M1_conversion":m["RI"]*m["CC"]/total,"E2_conversion":e["RI"]*e["CC"]/total}
        check("four_channels_normalized_"+str(m1energy),np.isclose(sum(fractions.values()),1))
        total_m1=fractions["M1_photon"]+fractions["M1_conversion"]
        photon_only_ratio=m["RI"]/(m["RI"]+e["RI"])
        check("photon_fraction_not_total_branch_"+str(m1energy),total_m1>photon_only_ratio>fractions["M1_photon"])
        branching.append({"parent_keV":m["parent"]["energy_keV"],"M1_gamma_keV":m1energy,"E2_gamma_keV":e2energy,
                          "pure_multipole_theoretical_CC":[m["CC"],e["CC"]],"two_observed_channel_conditional_fractions":fractions,
                          "conditional_total_M1_branch":total_m1,"photon_only_normalized_M1_ratio":photon_only_ratio,
                          "not_a_measured_complete_branch":True,"parent_lifetime_available_in_selected_records":False})
    return {"kind":"selected evaluated ENSDF crosswalk; not event refit",
            "objects":{"adopted":{"lines":len(aa),"sha256":hashlib.sha256(adopted.read_bytes()).hexdigest()},
                       "reaction":{"lines":len(rr),"sha256":hashlib.sha256(reaction.read_bytes()).hexdigest()}},
            "selected_levels":selected_levels,"seven_line_crosswalk":crosswalk,"doublet":q_lines,"weak352":weak,
            "SD_energy_expressions":[x["energy_expression"] for x in sd],"unplaced_candidate_1836":candidate,
            "conditional_ICC_branch_exercise":branching,"checks":checks,"checks_passed":sum(checks.values()),
            "boundary":"NDS reuses2015He27 and quotes2004Ni06; record precision/CC/LS energies are evaluated or calculated, not independent new experiment. No complete calibration covariance, weak-line polarity resolution, parent lifetime or unseen-branch completeness was inferred."}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--adopted",type=Path,required=True)
    p.add_argument("--reaction",type=Path,required=True)
    p.add_argument("--fixture",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    a=p.parse_args()
    root=Path(__file__).resolve().parents[2]
    for path in [a.adopted,a.reaction,a.fixture,a.output]:path.resolve().relative_to(root)
    result=audit(a.adopted,a.reaction,json.loads(a.fixture.read_text()))
    a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"checks_passed":result["checks_passed"],"levels":[(x["energy_expression"],x["energy_uncertainty_keV"]) for x in result["selected_levels"]],"ICC_branch_exercise":result["conditional_ICC_branch_exercise"]},ensure_ascii=False))


if __name__=="__main__":main()
