#!/usr/bin/env python3
"""Read 128I source-specific ENSDF fields and retain primary topology conflicts.

No energy-nearest matching across objects or new experimental assignment.
Fixed-column parent binding is checked against NNDC's rendered gamma table.
"""
from __future__ import annotations

import argparse
from decimal import Decimal as D, InvalidOperation
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02"


def value(x):
    try:
        return D(x.strip()) if x.strip() else None
    except InvalidOperation:
        return None


def parse(path):
    lines = path.read_text().splitlines()
    levels, gammas = [], []
    level = gamma = None
    for n,raw in enumerate(lines,1):
        s = raw.ljust(80)
        if s[:5].strip().upper() != "128I":
            continue
        if s[5:7] == "  " and s[7] == "L":
            level = dict(line=n,E=s[9:19].strip(),DE=s[19:21].strip(),Jpi=s[21:39].strip(),
                         half_life=s[39:49].strip(),Dhalf=s[49:55].strip(),raw=raw,comments=[])
            levels.append(level)
            gamma = None
        elif s[5:7] == "  " and s[7] == "G":
            gamma = dict(line=n,E=s[9:19].strip(),DE=s[19:21].strip(),RI=s[21:29].strip(),
                         DRI_or_limit=s[29:31].strip(),multipolarity=s[31:41].strip(),
                         mixing_ratio=s[41:49].strip(),CC=s[55:62].strip(),
                         parent_E=level["E"] if level else None,raw=raw,comments=[])
            gammas.append(gamma)
        elif s[7] == "G" and gamma is not None:
            gamma["comments"].append(dict(line=n,text=raw))
        elif s[7] == "L" and level is not None:
            level["comments"].append(dict(line=n,text=raw))
    return dict(lines=lines,levels=levels,gammas=gammas)


def unique(rows, **fields):
    found = [r for r in rows if all(r[k]==v for k,v in fields.items())]
    if len(found) != 1:
        raise ValueError((fields,len(found)))
    return found[0]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,default=RUN/"nndc128i-crosswalk-audit.json")
    args = parser.parse_args()
    ipath = RUN/"nndc128i-crosswalk-input.json"
    data = json.loads(ipath.read_text())
    checks = {}
    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            raise AssertionError(name)
    obj = {}
    for name,item in data["objects"].items():
        p = ROOT/item["path"]
        check(name+"_object_hash",hashlib.sha256(p.read_bytes()).hexdigest()==item["sha256"])
        obj[name] = parse(p)
        check(name+"_version_cutoff",any("15NDS" in s and "201510" in s for s in obj[name]["lines"])
              and any("CUT=28-Feb-2015" in s for s in obj[name]["lines"]))
    check("independent_rendered_PDF_hash",hashlib.sha256((ROOT/data["rendered_reaction_pdf"]["path"]).read_bytes()).hexdigest()==data["rendered_reaction_pdf"]["sha256"])
    a,r,c = obj["adopted"],obj["li7-reaction"],obj["thermal-secondary"]
    r102 = unique(r["gammas"],E="102.2")
    r15 = unique(r["gammas"],E="15.6")
    check("reaction102_parent_and_limit",r102["parent_E"]=="269.57" and r102["RI"]=="632" and r102["DRI_or_limit"]=="LE")
    check("reaction102_total_theoreticalCC_vs_experimentalECC",r102["CC"]=="0.703"
          and any("ECC=0.60 7" in s["text"] for s in r102["comments"]))
    check("reaction285_has15_6_and117_8_not102",{g["E"] for g in r["gammas"] if g["parent_E"]=="285.19"}=={"15.6","117.8"})
    check("adopted285_has_same_topology",{g["E"] for g in a["gammas"] if g["parent_E"]=="285.24"}=={"15.6","117.8"})
    check("adopted183_is_level_without_outgoing_gamma_record",unique(a["levels"],E="183.0")["Jpi"]=="(7-)"
          and not any(g["parent_E"]=="183.0" for g in a["gammas"]))
    check("two_low_spins_not_promoted_to_unique_values",all(unique(a["levels"],E=e)["Jpi"]=="(5,6,7)-" for e in ["226.102","269.712"]))
    cap102 = unique(c["gammas"],E="102.344")
    check("captureK_shell_experiment_not_totalICC",cap102["parent_E"]=="269.711" and cap102["CC"]=="0.700"
          and any("EKC=0.55 11" in s["text"] for s in cap102["comments"]))
    check("capture_normalization_is_different",any("Relative to I(133.61|g)=46.9" in s for s in c["lines"])
          and any(s.startswith("128I   N 1.06") for s in c["lines"]))
    r101 = unique(r["gammas"],E="101.3")
    a101 = unique(a["gammas"],E="101.3")
    check("adopted_and_reactionRI_scale_not_directly_equal",r101["RI"]=="146" and a101["RI"]=="100")
    check("source_explicit_evaluator_uncertainty_assignment",all(any(q in s for s in r["lines"]) for q in ["Evaluator assigns", "I|g>50", "I|g=20-50", "I|g<20"]))
    for eg,de,ri,dri in [("101.3","1","146","7"),("345.4","3","45","7"),("255.6","5","4","1")]:
        g=unique(r["gammas"],E=eg)
        check("evaluator_error_class_"+eg,g["DE"]==de and g["RI"]==ri and g["DRI_or_limit"]==dri)
    isomer = unique(a["levels"],E="167.368")
    daughter = unique(a["levels"],E="137.851")
    g29 = unique(a["gammas"],E="29.512")
    check("isomer_tau_identity_and_units",isomer["half_life"]=="175 NS" and isomer["Dhalf"]=="15"
          and daughter["half_life"]=="0.845 US" and g29["parent_E"]=="167.368" and g29["multipolarity"]=="(E2)")
    check("large_conversion_is_theoretical_field",g29["CC"]=="175.0")
    pri=json.loads((RUN/data["primary_thesis_input"]).read_text())
    p102a=unique(pri["rows"],id="t102a")
    p102b=unique(pri["rows"],id="t102b")
    check("same_energy_different_parent_explicitly_retained",p102a["parent_keV"]=="285.2" and p102b["parent_keV"]=="269.6"
          and r102["parent_E"]=="269.57")
    endpoint_sum_primary=D("285.2")-D("167.4")
    endpoint_sum_evaluated=D("285.19")-D("167.367")
    check("rounded_energy_sums_do_not_resolve_node_order",D("102.2")+D("15.6")==D("117.8")==endpoint_sum_primary
          and abs(endpoint_sum_evaluated-D("117.8"))<D(".1"))
    refs=json.loads((RUN/data["refs_object"]).read_text())["text"]
    check("2012Di14_exact_primary_identified_not_read","10.1103/PhysRevC.86.034302" in refs and not data["2012Di14_body_read"])
    check("literal2012Wa27_reference_identity_boundary","2012Wa27" in "\n".join(r["lines"])
          and "Total Routhian surface calculations of octupole properties in neutron-deficient U isotopes" in refs)
    check("2009_secondary_metadata_beam_boundary","E=25, 28, 32 MeV" in "\n".join(r["lines"])
          and "E=25, 28, 42 MeV" in refs and not data["2009_body_read"])
    check("no_actual_refit_or_topology_adjudication",not data["primary_topology_adjudicated"] and not data["actual_event_refit"] and data["full_covariance"] is None)
    selected = {}
    for name,energies in {"adopted":["137.851","167.368","183.0","226.102","269.712","285.24","1562.27"],
                          "li7-reaction":["167.367","182.99","226.0","269.57","285.19","1562.21"],
                          "thermal-secondary":["137.850","167.367","226.101","269.711"]}.items():
        selected[name] = dict(levels=[unique(obj[name]["levels"],E=e) for e in energies],
                              gammas=[g for g in obj[name]["gammas"] if g["parent_E"] in energies])
    result=dict(kind="selected evaluated ENSDF records with preserved primary topology/field conflict",
                checks=checks,check_count=len(checks),passed=all(checks.values()),inputs=data,
                selected_source_records=selected,
                primary_102a=p102a,primary_102b=p102b,evaluated_reaction_102=r102,evaluated15=r15,
                parent_difference_not_rounding=True,
                energy_sums=dict(primary_285_to167=endpoint_sum_primary,evaluation_285_to167=endpoint_sum_evaluated,
                                 reported_gamma_15plus102=D("117.8")),
                topology_choice=None,actual_full_covariance=None,
                input_sha256=hashlib.sha256(ipath.read_bytes()).hexdigest(),
                thesis_input_sha256=hashlib.sha256((RUN/data["primary_thesis_input"]).read_bytes()).hexdigest(),
                references_sha256=hashlib.sha256((RUN/data["refs_object"]).read_bytes()).hexdigest(),
                limitations=["evaluation reuses Tsukuba sources, not a new independent measurement",
                             "raw text and rendered PDF are two representations of the same evaluated data",
                             "no attribution of cause until original2012Di14/errata/data verified",
                             "theory CC, experimental totalECC and K-shellEKC are different quantities",
                             "evaluator-added perrowerrors do not restore actual covariance or selection likelihood",
                             "lowlevel half-life/decay belongs to that parent, not higher cascade parents"])
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2,default=str)+"\n")
    print(json.dumps({k:result[k] for k in ["kind","check_count","passed","parent_difference_not_rounding","energy_sums"]},default=str))


if __name__=="__main__":
    main()
