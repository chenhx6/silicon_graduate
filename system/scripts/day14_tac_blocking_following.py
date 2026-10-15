#!/usr/bin/env python3
"""Conditional replay of the published 2015 O1/O2 blocking expression.

All U/V matrices below are chosen real canonical controls, not nuclear inputs.
The author's actual phase/tie/zero-norm conventions and code are unavailable.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import pymupdf

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02"
TEMP = ROOT / "tmp/day14-20261014/tac2015"
SHA = "ce3c7672420b07e9bbe7d7a869049771c5cef9aa64f4dffce5dfd18bcb0b3c21"
TOL = 1e-12  # Declared analysis tolerance; not the author's implementation.


def canonical(u: np.ndarray, v: np.ndarray) -> bool:
    return bool(np.allclose(u.T@u + v.T@v, np.eye(u.shape[1]), atol=TOL)
                and np.allclose(u.T@v + v.T@u, 0, atol=TOL))


def density(u: np.ndarray, v: np.ndarray, blocked: int | None = None) -> np.ndarray:
    rho = v @ v.T
    if blocked is not None:
        rho = rho + np.outer(u[:,blocked], u[:,blocked]) - np.outer(v[:,blocked], v[:,blocked])
    return rho


def pairing(u: np.ndarray, v: np.ndarray, blocked: int | None = None) -> np.ndarray:
    kappa = v @ u.T
    if blocked is not None:
        kappa = kappa + np.outer(u[:,blocked], v[:,blocked]) - np.outer(v[:,blocked], u[:,blocked])
    return kappa


def normalized_components(u: np.ndarray, v: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    # Real controls only: this is the literal transpose norm on source PDF p.5.
    nu, nv = np.sqrt(np.sum(u*u, axis=0)), np.sqrt(np.sum(v*v, axis=0))
    if np.any(nu <= TOL) or np.any(nv <= TOL):
        raise ValueError("separate U/V normalization undefined at a zero component; source branch unspecified")
    return u/nu, v/nv


def decisions(o1: np.ndarray, o2: np.ndarray, old_blocked: list[bool]) -> list[dict]:
    results = []
    for row1, row2 in zip(o1, o2):
        best1, best2 = float(max(row1)), float(max(row2))
        k1 = np.flatnonzero(np.isclose(row1, best1, atol=TOL, rtol=0)).tolist()
        k2 = np.flatnonzero(np.isclose(row2, best2, atol=TOL, rtol=0)).tolist()
        if math.isclose(best1, best2, abs_tol=TOL):
            branch, values = "O1/O2 tie: source handling unspecified", None
        elif best1 > best2:
            branch, values = "O1: inherit", sorted(set(old_blocked[j] for j in k1))
        else:
            branch, values = "O2: invert", sorted(set(not old_blocked[j] for j in k2))
        results.append({"O1_max":best1,"O2_max":best2,"O1_max_indices":k1,"O2_max_indices":k2,
                        "branch":branch,"possible_blocking":values,
                        "unique_blocking":values[0] if values is not None and len(values)==1 else None})
    return results


def follow(u: np.ndarray, v: np.ndarray, previous_u: np.ndarray, previous_v: np.ndarray,
           old_blocked: list[bool], *, absolute_control: bool = False) -> dict:
    cu, cv = normalized_components(u, v)
    pu, pv = normalized_components(previous_u, previous_v)
    o1, o2 = cu.T@pu + cv.T@pv, cu.T@pv + cv.T@pu
    if absolute_control:
        o1, o2 = abs(o1), abs(o2)
    return {"score_policy":"declared absolute-score control, not attributed to source" if absolute_control else "literal signed source expression",
            "O1":o1.tolist(),"O2":o2.tolist(),"decisions":decisions(o1,o2,old_blocked)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=RUN / "tac2015-blocking-following.json")
    args = parser.parse_args()
    checks: dict[str,bool] = {}

    def check(name: str, value: object) -> None:
        checks[name] = bool(value)

    manifest = json.loads((TEMP/"manifest.json").read_text())
    pdf = Path(manifest["results"][0]["file"]).resolve()
    data = pdf.read_bytes()
    check("input_within_wiki", pdf.is_relative_to(ROOT))
    check("actual_PDF_identity", data.startswith(b"%PDF") and hashlib.sha256(data).hexdigest()==SHA)
    doc = pymupdf.open(pdf)
    text = [p.get_text() for p in doc]
    check("thirteen_pages", len(doc)==13)
    check("exact_arxiv_and_title", "1506.08340v2" in text[0] and "pairing correlations" in text[0] and "spin" in text[0])
    check("blocking_rule_location", all(s in text[4] for s in ["O1", "O2", "largest overlap", "blocked", "unblocked"]))
    check("source_norm_UV_location", all(s in text[4] for s in ["normalized wave functions", "Uk", "Vk"]))

    u0, v0 = math.sqrt(.7), math.sqrt(.3)
    u = u0*np.eye(2)
    v = v0*np.array([[0.,-1.],[1.,0.]])
    blocked = [True,False]
    check("chosen_canonical_Bogoliubov", canonical(u,v))
    j = np.array([[0.,-1.],[1.,0.]])
    h = (u0**2-v0**2)*np.eye(2)
    delta = -2*u0*v0*j
    bdg = np.block([[h,delta],[-delta,-h]])  # Chosen real, degenerate E=1 limit.
    w_positive = np.vstack([u,v])
    check("chosen_BdG_degenerate_positive_eigenbasis", np.allclose(bdg,bdg.T)
          and np.allclose(np.linalg.eigvalsh(bdg),[-1,-1,1,1])
          and np.allclose(bdg@w_positive,w_positive))
    check("chosen_density_eigenvalues", np.allclose(np.linalg.eigvalsh(density(u,v)), [.3,.3]))
    check("chosen_pairing_tensor_antisymmetric", np.allclose(v@u.T, -(v@u.T).T))
    check("chosen_blocked_generalized_density", np.allclose(density(u,v,0), [[1,0],[0,0]]) and np.allclose(pairing(u,v,0),0))

    cases: dict[str,dict] = {}
    cases["same"] = follow(u,v,u,v,blocked)
    check("same_inherits_all_flags", [x["unique_blocking"] for x in cases["same"]["decisions"]]==blocked)
    check("same_O1_diagonal_two", np.allclose(cases["same"]["O1"], 2*np.eye(2)))
    check("same_O2_zero", np.allclose(cases["same"]["O2"], 0))

    signs = np.diag([-1.,1.])
    us, vs = u@signs, v@signs
    check("sign_change_still_canonical", canonical(us,vs))
    check("sign_change_same_density", np.allclose(density(us,vs),density(u,v)))
    check("sign_change_same_pairing_tensor", np.allclose(vs@us.T,v@u.T))
    check("sign_change_same_blocked_generalized_density", np.allclose(density(us,vs,0),density(u,v,0)) and np.allclose(pairing(us,vs,0),pairing(u,v,0)))
    cases["sign_literal"] = follow(us,vs,u,v,blocked)
    cases["sign_absolute_control"] = follow(us,vs,u,v,blocked,absolute_control=True)
    check("literal_sign_control_needs_policy", cases["sign_literal"]["decisions"][0]["unique_blocking"] is None)
    check("declared_absolute_control_restores_sign_invariance", [x["unique_blocking"] for x in cases["sign_absolute_control"]["decisions"]]==blocked)

    uh, vh = u.copy(), v.copy()
    uh[:,0], vh[:,0] = v[:,0], u[:,0]
    check("particle_hole_swap_canonical", canonical(uh,vh))
    cases["particle_hole_swap"] = follow(uh,vh,u,v,blocked)
    check("particle_hole_uses_O2", cases["particle_hole_swap"]["decisions"][0]["branch"]=="O2: invert")
    check("particle_hole_inverts_blocking", cases["particle_hole_swap"]["decisions"][0]["unique_blocking"] is False)
    check("particle_hole_reference_change_same_blocked_generalized_density", np.allclose(density(uh,vh),density(u,v,0)) and np.allclose(pairing(uh,vh),pairing(u,v,0)))

    for degrees in [10,45,80]:
        if degrees==45:
            rotation = np.array([[1.,-1.],[1.,1.]])/math.sqrt(2)
        else:
            angle = math.radians(degrees)
            rotation = np.array([[math.cos(angle),-math.sin(angle)],[math.sin(angle),math.cos(angle)]])
        ur, vr = u@rotation, v@rotation
        check(f"rotation_{degrees}_canonical_eigenbasis", canonical(ur,vr) and np.allclose(bdg@np.vstack([ur,vr]),np.vstack([ur,vr])))
        check(f"rotation_{degrees}_vacuum_density_unchanged", np.allclose(density(ur,vr),density(u,v)))
        check(f"rotation_{degrees}_pairing_tensor_unchanged", np.allclose(vr@ur.T,v@u.T))
        cases[f"rotation_{degrees}_literal"] = follow(ur,vr,u,v,blocked)
        cases[f"rotation_{degrees}_absolute_control"] = follow(ur,vr,u,v,blocked,absolute_control=True)
    check("small_step_follows", [x["unique_blocking"] for x in cases["rotation_10_literal"]["decisions"]]==blocked)
    check("fortyfive_best_previous_tie", len(cases["rotation_45_literal"]["decisions"][0]["O1_max_indices"])==2)
    check("fortyfive_blocking_not_unique", cases["rotation_45_literal"]["decisions"][0]["possible_blocking"]==[False,True])
    check("absolute_score_does_not_resolve_fortyfive", all(x["unique_blocking"] is None for x in cases["rotation_45_absolute_control"]["decisions"]))
    check("large_step_literal_maps_both_to_previous_one", all(x["O1_max_indices"]==[1] for x in cases["rotation_80_literal"]["decisions"]))
    check("large_step_literal_block_count_changes_in_control", [x["unique_blocking"] for x in cases["rotation_80_literal"]["decisions"]]==[False,False])
    check("declared_absolute_large_step_control", [x["unique_blocking"] for x in cases["rotation_80_absolute_control"]["decisions"]]==[False,True])

    # Demonstrate why an unrecorded first-argmax tie rule is not source evidence.
    row = np.array(cases["rotation_45_literal"]["O1"])[0]
    first = blocked[int(np.argmax(row))]
    reordered = [blocked[1],blocked[0]][int(np.argmax(row[::-1]))]
    check("chosen_first_argmax_order_sensitive", first != reordered)
    zero_boundary = None
    check("zero_pairing_control_canonical", canonical(np.eye(2),np.zeros((2,2))))
    try:
        follow(np.eye(2),np.zeros((2,2)),u,v,blocked)
    except ValueError as exc:
        zero_boundary = str(exc)
    check("zero_component_declared_boundary", zero_boundary is not None)

    out={"kind":"literal published overlap rule under chosen real canonical matrices, not an RHB run or author-code verdict",
         "source":{"doi":"10.1103/PhysRevC.92.034319","arxiv":"1506.08340v2","pdf":str(pdf.relative_to(ROOT)),"sha256":SHA,"locator":"PDF p.5 O1/O2 blocking paragraph","raw_archived":False},
         "chosen_parameters":{"u_squared":.7,"v_squared":.3,"initial_blocked":blocked,"analysis_tolerance":TOL,"U":u.tolist(),"V":v.tolist(),
                              "BdG":bdg.tolist(),"positive_energy":1,"actual_rotating_nuclear_spectrum":False},
         "cases":cases,"chosen_first_argmax_tie_control":{"before_reordering":first,"after_reordering":reordered,"attributed_to_source":False},
         "zero_component_boundary":zero_boundary,
         "missing_actual_conventions":["phase/gauge alignment or magnitude convention","equal O1/O2 and equal maxima handling","zero norm policy and no-pairing branch","actual lambda/omega step sizes and tracking log","previous/current blocked inventories and density convergence"],
         "interpretation":"conditions needed to replay the public expression; actual implementation may specify all of them; no Pr136 spectator or blocking inferred",
         "checks":checks,"check_count":len(checks),"passed":all(checks.values())}
    args.output.resolve().relative_to(ROOT)
    args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"output":str(args.output.relative_to(ROOT)),"checks":len(checks),"passed":out["passed"],"failed":[k for k,v in checks.items() if not v]},ensure_ascii=False))
    return 0 if out["passed"] else 1


if __name__=="__main__":
    raise SystemExit(main())
