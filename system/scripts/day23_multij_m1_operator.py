#!/usr/bin/env python3
"""Exact l x spin-1/2 angular M1 component; no nuclear mixing or physical g."""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day23_prm_basis_rotor import clebsch_gordan, spin_matrices


def spherical(axes):
    x, y, z = axes
    return [ (x-1j*y)/math.sqrt(2), z, -(x+1j*y)/math.sqrt(2) ]


def calculate(ell):
    if ell < 1 or int(ell) != ell:
        raise ValueError("Integer l>=1 required for both spin-orbit partners")
    uncoupled = [(ml, ms/2) for ml in range(-ell, ell+1) for ms in [-1, 1]]
    coupled = [(two_j, m/2) for two_j in [2*ell-1, 2*ell+1]
               for m in range(-two_j, two_j+1, 2)]
    u = np.array([[clebsch_gordan(ell, ml, .5, ms, two_j/2, mj)
                   for two_j, mj in coupled] for ml, ms in uncoupled])
    ls = [np.kron(op, np.eye(2)) for op in spin_matrices(2*ell)]
    ss = [np.kron(np.eye(2*ell+1), op) for op in spin_matrices(1)]
    lc = [u.T@op@u for op in ls]
    sc = [u.T@op@u for op in ss]
    jc = [a+b for a, b in zip(lc, sc)]
    nminus, dimension = 2*ell, len(coupled)
    slices = {"minus": slice(0, nminus), "plus": slice(nminus, dimension)}
    closure = sum(op.T.conj()@op for op in spherical(sc))
    expected_j = []
    for axis in range(3):
        expected = np.zeros((dimension, dimension), complex)
        expected[slices["minus"], slices["minus"]] = spin_matrices(2*ell-1)[axis]
        expected[slices["plus"], slices["plus"]] = spin_matrices(2*ell+1)[axis]
        expected_j.append(expected)
    error = lambda a: float(np.max(abs(a)))
    details = {"CG_unitarity_error": error(u.T@u-np.eye(dimension)),
               "total_j_directsum_error": max(error(a-b) for a,b in zip(jc,expected_j)),
               "spin_complete_closure_error_hbar2": error(closure-.75*np.eye(dimension)),
               "orbital_Casimir_error_hbar2": error(sum(op@op for op in lc)-ell*(ell+1)*np.eye(dimension)),
               "offdiagonal_total_j_error": max(error(op[slices["minus"],slices["plus"]]) for op in jc)}
    strengths = {}
    for initial in ["plus", "minus"]:
        for final in ["plus", "minus"]:
            si, sf = slices[initial], slices[final]
            ni = (2*ell+2) if initial == "plus" else 2*ell
            strengths[f"{initial}_to_{final}"] = float(sum(
                np.linalg.norm(op[sf,si])**2 for op in spherical(sc))/ni)
    projection_error = 0.0
    for name, sign in [("plus",1),("minus",-1)]:
        sl = slices[name]
        projection_error = max(projection_error,max(error(
            s[sl,sl]-sign/(2*ell+1)*j[sl,sl]) for s,j in zip(sc,jc)))
    details["diagonal_spin_projection_error"] = projection_error
    controls = {"complete_CG_basis_unitary": details["CG_unitarity_error"] < 1e-12,
                "l_plus_s_directsum_j_generator": details["total_j_directsum_error"] < 1e-12,
                "total_j_has_no_cross_irrep_matrix": details["offdiagonal_total_j_error"] < 1e-12,
                "spin_Casimir_closure": details["spin_complete_closure_error_hbar2"] < 1e-12,
                "orbital_Casimir_closure": details["orbital_Casimir_error_hbar2"] < 1e-12,
                "diagonal_Lande_projection": projection_error < 1e-12,
                "spinflip_plus_minus_analytic": math.isclose(strengths["plus_to_minus"],ell/(2*ell+1),abs_tol=1e-13),
                "spinflip_minus_plus_analytic": math.isclose(strengths["minus_to_plus"],(ell+1)/(2*ell+1),abs_tol=1e-13),
                "reverse_detailed_balance": math.isclose((2*ell+2)*strengths["plus_to_minus"],2*ell*strengths["minus_to_plus"],abs_tol=1e-13),
                "spin_tensor_nonzero_between_partners": strengths["plus_to_minus"] > 0,
                "each_initial_irrep_spin_sum_three_quarters": all(math.isclose(
                    sum(strengths[f"{initial}_to_{final}"] for final in ["minus","plus"]),.75,abs_tol=1e-13)
                    for initial in ["minus","plus"])}
    return {"l":ell,"s":.5,"j_minus":ell-.5,"j_plus":ell+.5,"dimension":dimension,
            "normalized_spin_tensor_B_hbar2":strengths,"control_details":details,
            "controls":{k:bool(v) for k,v in controls.items()},"all_controls_pass":all(controls.values())}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,required=True)
    a=parser.parse_args()
    rows=[calculate(ell) for ell in [1,5]]
    result={"status":"exact-angular-operator-component","hbar":1,
            "source_premise":"H02-D23-003 Eq9; full orbital/spin magnetic tensor before single-j projection",
            "symbolic_cross_j_operator":"<jminus|mu_intr|jplus> = (gs-gl)<jminus|s|jplus>; <jminus|j|jplus>=0",
            "symbolic_diagonal_g":"gj_plus=gl+(gs-gl)/(2l+1); gj_minus=gl-(gs-gl)/(2l+1). No numerical gl/gs/gR chosen.",
            "normalized_cross_strength":"B_M1(jplus->jminus) / [(3/(4pi))*(gs-gl)^2*muN^2] = l/(2l+1) for this pure angular component only",
            "results":rows,"all_controls_pass":all(r['all_controls_pass'] for r in rows),
            "implementation_sha256":{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [
                Path(__file__),Path(__file__).with_name('day23_prm_basis_rotor.py')]},
            "limitations":["No nuclear rotor coupling, radial/BCS amplitudes, state configuration weights, response, actual BM1, delta or lifetime calculated.",
                           "l=5 h11/2/h9/2 basis is an angular component, not an observed Pr/Au state or transition.",
                           "Spin closure includes all diagonal and reverse/upward matrix elements, not gamma branch completeness.",
                           "This proves common single-j scale cancellation is conditional, not that it necessarily fails numerically in an h-dominant actual QTR state.",
                           "No original QTR producer or new experiment is certified; missing mixing amplitudes prevent transfer of this component to a nuclear prediction."]}
    a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({"all_controls_pass":result['all_controls_pass'],"checks":sum(len(r['controls']) for r in rows),
                      "results":rows},ensure_ascii=False))
    return 0 if result['all_controls_pass'] else 1


if __name__=='__main__':
    raise SystemExit(main())
