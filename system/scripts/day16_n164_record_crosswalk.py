#!/usr/bin/env python3
"""Read fixed-column selected ENSDF records without inventing blank values.

This audits three already acquired evaluated objects, not the original event
experiments. It keeps record labels, uncertainties, comments and theory/experiment
coefficient fields distinct, and never assigns a new spin or missing branch.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation
import hashlib
import json
import math
from pathlib import Path
import re


def number(value: str, uncertainty: str = "") -> dict:
    raw=value.strip();u=uncertainty.strip()
    obj={"raw":raw,"uncertainty_raw":u,"value":None,"sigma":None}
    if not raw:
        return obj
    try:
        x=Decimal(raw);obj["value"]=float(x)
        if u.isdigit():obj["sigma"]=float(Decimal(u)*Decimal(10)**x.as_tuple().exponent)
    except InvalidOperation:
        pass
    return obj


def read_object(path: Path) -> dict:
    lines=path.read_text().splitlines()
    band_keys=set(re.findall(r" CL BAND\(([A-Za-z])\)","\n".join(lines)))
    levels=[];current=None;gamma=None
    for index,text in enumerate(lines,1):
        if not text.startswith("164YB"):
            continue
        s=text.ljust(80)
        if s[5:9]=="  L ":
            current={"line":index,"record":text,"energy":number(s[9:19],s[19:21]),
                     "Jpi":s[21:39].strip(),"time_raw":s[39:49].strip(),
                     "time_uncertainty_raw":s[49:55].strip(),
                     "comment_flag":s[76:77],
                     "band_flag":s[76:77] if s[76:77] in band_keys else None,
                     "continuation":[],"gammas":[]}
            levels.append(current);gamma=None
        elif s[5:9]=="  G ":
            assert current is not None
            gamma={"line":index,"record":text,"energy":number(s[9:19],s[19:21]),
                   "RI":number(s[21:29],s[29:31]),"multipolarity":s[31:41].strip(),
                   "mixing_ratio":number(s[41:49],s[49:55]),"CC":number(s[55:62],s[62:64]),
                   "continuation":[]}
            current["gammas"].append(gamma)
        elif current is not None:
            if gamma is not None and s[7:8]=="G":gamma["continuation"].append({"line":index,"text":text})
            elif s[7:8]=="L":current["continuation"].append({"line":index,"text":text})
    return {"header":lines[1],"line_count":len(lines),"levels":levels}


def unique(items: list[dict], value: float) -> dict:
    found=[x for x in items if x["energy"]["value"] is not None
           and abs(x["energy"]["value"]-value)<1e-7]
    assert len(found)==1,(value,len(found))
    return found[0]


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args();cfg=json.loads(args.input.read_text())
    root=Path(__file__).resolve().parents[2]
    selected={};reference={}
    for inp in cfg["inputs"]:
        path=root/inp["path"];assert hashlib.sha256(path.read_bytes()).hexdigest()==inp["sha256"]
        name=inp["label"];sel=cfg["selectors"][name];data=read_object(path)
        assert sel["header"] in data["header"]
        by_spin={}
        for spin in cfg["reference_ground_spins"]:
            found=[x for x in data["levels"] if x["band_flag"]==sel["groundband_flag"]
                   and x["Jpi"]==spin]
            assert len(found)==1,(name,spin,[(x["Jpi"],x["band_flag"]) for x in data["levels"][:5]])
            by_spin[spin]=found[0]
        targets={};nearby=[]
        for short,spin in [("490","14+"),("647","10+")]:
            parent=unique(data["levels"],sel["parent"+short+"_Ex"])
            g=unique(parent["gammas"],sel["gamma"+short]);daughter=by_spin[spin]
            residual=parent["energy"]["value"]-daughter["energy"]["value"]-g["energy"]["value"]
            targets[short]={"parent":parent,"selected_gamma_line":g["line"],
                            "daughter_groundband":{k:daughter[k] for k in ["line","record","energy","Jpi","band_flag"]},
                            "literal_energy_residual_keV":residual,
                            "residual_not_a_chi_square":True}
        width=cfg["nearby_search_halfwidth_keV"]
        for level in data["levels"]:
            for g in level["gammas"]:
                e=g["energy"]["value"]
                if e is not None and (abs(e-490)<=width or abs(e-647)<=width):
                    nearby.append({"parent_Ex":level["energy"]["value"],"parent_Jpi":level["Jpi"],
                                   "parent_band":level["band_flag"],"gamma_line":g["line"],
                                   "gamma_energy":e,"multipolarity":g["multipolarity"]})
        selected[name]={"record":inp["record"],"raw":inp["path"],"sha256":inp["sha256"],
                        "header":data["header"],"targets":targets,"nearby_energy_candidates":nearby}
        reference[name]={spin:{"energy":x["energy"],"line":x["line"],"Jpi":x["Jpi"]}
                         for spin,x in by_spin.items()}
    shifts=[]
    for spin in cfg["reference_ground_spins"]:
        a=reference["adopted"][spin]["energy"]["value"]
        b=reference["sm16o"][spin]["energy"]["value"]
        shifts.append({"spin":spin,"adopted":a,"sm16o":b,"adopted_minus_sm16o_keV":a-b})
    parent=selected["adopted"]["targets"]["490"]["parent"]
    t=parent["time_raw"].split();assert len(t)==2 and t[1]=="PS",t
    time=number(t[0],parent["time_uncertainty_raw"])
    half=time["value"];sigma=time["sigma"]
    angle=cfg["published_ST99_alternative"]["arctan_delta_deg"]
    delta=math.tan(math.radians(angle))
    fractions={"M1":1/(1+delta*delta),"E2":delta*delta/(1+delta*delta)}
    g490=unique(parent["gammas"],489.8);g302=unique(parent["gammas"],302.3)
    r_ad=g302["RI"]["value"]/g490["RI"]["value"]
    rp=selected["sm16o"]["targets"]["490"]["parent"]
    r_reaction=unique(rp["gammas"],302.3)["RI"]["value"]/unique(rp["gammas"],489.8)["RI"]["value"]
    assert g302["CC"]["value"] is None and g490["CC"]["value"] is not None
    experiment490=[x for x in g490["continuation"] if "EKC" in x["text"]]
    r647=selected["sm16o"]["targets"]["647"]["parent"]
    g647=unique(r647["gammas"],647.4)
    experiment647=[x for x in g647["continuation"] if "EKC" in x["text"]]
    assert not experiment490 and len(experiment647)==1
    out={"identity":cfg["identity"],"input_sha256":hashlib.sha256(args.input.read_bytes()).hexdigest(),
         "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         "selected_objects":selected,"ground_reference_crosswalk":reference,"evaluated_energy_shifts":shifts,
         "time_conversion":{"ENSDF_T_half_ps":half,"sigma_T_half_ps":sigma,
                            "mean_tau_ps":half/math.log(2),"sigma_mean_tau_ps":sigma/math.log(2),
                            "total_decay_rate_per_second":math.log(2)/(half*1e-12),
                            "local_sigma_decay_rate_per_second":math.log(2)*sigma/(half*half*1e-12),
                            "primary_fit_definition_verified":False},
         "radiative_component_hypothesis":{"arctan_delta_deg":angle,"delta":delta,"fractions":fractions,
                                            "meaning":"ST99alternativecomponentfractions, not observedbranch/totaldecay or newfit"},
         "RI_normalization":{"adopted_I302_over_I490":r_ad,"reaction_I302_over_I490":r_reaction,
                             "same_primary_intensity_lineage_not_independent":True,"Cov_available":False},
         "ICC_identity":{"G489_CC_theoretical":g490["CC"],"G302_CC_unknown":g302["CC"],
                         "G489_EKC_in_selected_adopted_block":experiment490,
                         "G647_experimental_EKC_limit_line":experiment647,
                         "G647_mixing_M2_over_E1_not_E2_over_M1":g647["mixing_ratio"]},
         "readiness":"Evaluatedsummaryreadinessonly. Nooriginalcount/feeding/response/Cov or unknown302ICC. NoabsoluteB, uniqueJpi, directlifetimefit, measured489ICC or newexperiment claimed."}
    args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({k:v for k,v in out.items() if k not in ["selected_objects","ground_reference_crosswalk"]},ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
