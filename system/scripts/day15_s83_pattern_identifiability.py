#!/usr/bin/env python3
"""Bound H/V overlap from S83 aggregate constraints in a chosen Boolean model.

These are statistical event-mask witnesses, not photon-transport simulations or
reconstructions of the original electronic routing/covariance.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


def rotate(mask: int, k: int) -> int:
    return ((mask<<k)|(mask>>(8-k)))&255 if k else mask


def features(mask: int) -> np.ndarray:
    n=mask.bit_count()
    quads=[bool(mask&(3<<(2*q))) for q in range(4)]
    vertical=(quads[3] and quads[2]) or (quads[0] and quads[1])
    horizontal=(quads[3] and quads[0]) or (quads[2] and quads[1])
    bits=[i for i in range(8) if mask&(1<<i)]
    adjacent=n==2 and (bits[1]-bits[0] in (1,7))
    return np.array([n==1,n==2,n==3,n>=4,adjacent,
                     horizontal,vertical,horizontal and vertical],dtype=float)


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args()
    cfg=json.loads(args.input.read_text())
    s=cfg["source_nominal_constraints"]
    extra=cfg["chosen_extra_constraints"]
    target=np.array([s["p_n1"],s["p_n2"],s["p_n3"],s["p_n_ge4"],
                     s["p_n2"]*s["p_adjacent_given_n2"],extra["p_H"],extra["p_V"]])
    models=[]
    for symmetric in (False,True):
        groups=[]
        seen=set()
        for mask in range(1,256):
            if mask in seen:
                continue
            group=sorted({rotate(mask,k) for k in range(8)}) if symmetric else [mask]
            groups.append(group)
            seen.update(group)
        matrix=np.array([np.mean([features(m) for m in group],axis=0) for group in groups]).T
        witnesses=[]
        for direction in (1,-1):
            fit=linprog(direction*matrix[7],A_eq=matrix[:7],b_eq=target,
                        bounds=(0,None),method="highs")
            item={"optimization":"min_overlap" if direction==1 else "max_overlap",
                  "status":int(fit.status),"message":fit.message,"feasible":bool(fit.success)}
            if fit.success:
                prob=np.zeros(256)
                for weight,group in zip(fit.x,groups):
                    for mask in group:
                        prob[mask]+=weight/len(group)
                full=np.array([features(m) if m else np.zeros(8) for m in range(256)]).T
                residual=float(max(abs(full[:7]@prob-target)))
                assert residual<2e-10 and min(prob)>-2e-10 and abs(prob.sum()-1)<2e-10
                dual=np.array(fit.eqlin.marginals)
                dual_violation=float(max(np.maximum(matrix[:7].T@dual-direction*matrix[7],0)))
                dual_gap=abs(float(target@dual)-fit.fun)
                assert dual_violation<2e-10 and dual_gap<2e-10
                overlap=float(full[7]@prob)
                assert abs(extra["p_H"]-extra["p_V"])<1e-14
                mean=extra["p_H"]
                variance_coefficient=(mean-overlap)/(2*mean**2)
                if symmetric:
                    assert max(abs(prob[m]-prob[rotate(m,1)]) for m in range(1,256))<2e-10
                item.update({"p_HV":overlap,"fixedN_covariance_per_event":overlap-mean**2,
                             "Poisson_covariance_per_mean_event_yield":overlap,
                             "local_VarA_times_event_yield_known_a1":variance_coefficient,
                             "naive_independent_Poisson_VarA_times_yield":1/(2*mean),
                             "constraint_max_abs_residual":residual,
                             "dual_certificate":dual.tolist(),"dual_max_violation":dual_violation,
                             "primal_dual_gap":dual_gap,
                             "nonzero_event_masks":[{"mask_hex":f"{m:02x}","fired_sectors":[i+1 for i in range(8) if m&(1<<i)],
                                                       "probability":float(prob[m])}
                                                      for m in range(1,256) if prob[m]>1e-12]})
            witnesses.append(item)
        models.append({"full_cyclic_symmetry":symmetric,"witnesses":witnesses})
    out={"identity":cfg["identity"],"input_sha256":hashlib.sha256(args.input.read_bytes()).hexdigest(),
         "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         "target_constraints":target.tolist(),"models":models,
         "boundary":"All routing and selectedH/Vmeans are chosen. Published multiplicity ratios are nominal. Statistical mask distributions need not be realizable detector transport; they demonstrate aggregate insufficiency, not actual hardware overlap/Cov or polarization precision."}
    args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"models":[{"symmetry":m["full_cyclic_symmetry"],
                                 "bounds":[{k:x.get(k) for k in ["optimization","feasible","p_HV","constraint_max_abs_residual","local_VarA_times_event_yield_known_a1"]}
                                           for x in m["witnesses"]]} for m in models]},ensure_ascii=False,indent=2))
    assert all(x["feasible"] for m in models for x in m["witnesses"])
    assert all(m["witnesses"][1]["p_HV"]-m["witnesses"][0]["p_HV"]>1e-3 for m in models)


if __name__=="__main__":
    main()
