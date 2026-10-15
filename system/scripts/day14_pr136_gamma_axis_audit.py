#!/usr/bin/env python3
"""Read actual Pr136 model beta/gamma and audit a declared tensor convention.

The normalized tensor and irrotational inertia law are explicit mathematical
controls. They do not identify the author's signed rotation-frame mapping.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import subprocess
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import numpy as np

from day14_pr136_configuration_ledger import actual_table_rows

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02"


@dataclass(frozen=True)
class Q3:
    """Exact a + b*sqrt(3); sufficient for the declared polynomial identities."""
    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    @staticmethod
    def value(x):
        return x if isinstance(x,Q3) else Q3(Fraction(x))

    def __add__(self, other):
        y=self.value(other)
        return Q3(self.a+y.a,self.b+y.b)

    __radd__=__add__

    def __neg__(self):
        return Q3(-self.a,-self.b)

    def __sub__(self, other):
        return self+-self.value(other)

    def __rsub__(self, other):
        return self.value(other)+-self

    def __mul__(self, other):
        y=self.value(other)
        return Q3(self.a*y.a+3*self.b*y.b,self.a*y.b+self.b*y.a)

    __rmul__=__mul__

    def __truediv__(self, rational):
        return Q3(self.a/Fraction(rational),self.b/Fraction(rational))

    def __pow__(self, n):
        out=Q3(Fraction(1))
        for _ in range(n): out=out*self
        return out


def exact_q(c, s):
    c,s=Q3.value(c),Q3.value(s)
    root3=Q3(Fraction(0),Fraction(1))
    return ((-c-root3*s)/2,(-c+root3*s)/2,c)


def tensor(beta: float, degrees: float) -> np.ndarray:
    gamma = math.radians(degrees)
    return np.diag(beta*np.cos(gamma+np.array([2*math.pi/3,-2*math.pi/3,0])))


def inertia(q: np.ndarray) -> np.ndarray:
    x,y,z = np.diag(q)
    return np.diag([(y-z)**2/3,(z-x)**2/3,(x-y)**2/3])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=RUN/"pr136-gamma-axis-audit.json")
    args = parser.parse_args()
    checks: dict[str,bool] = {}

    def check(name: str, condition: object) -> None:
        checks[name] = bool(condition)

    source = ROOT/"knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md"
    st = source.read_text()
    raw = ROOT/re.search(r'^raw_file: "(.*)"$',st,re.M)[1]
    sha = re.search(r'^raw_sha256: (\w+)',st,re.M)[1]
    check("actual_accepted_PDF_hash", hashlib.sha256(raw.read_bytes()).hexdigest()==sha)
    pages = subprocess.check_output(["pdftotext","-layout",str(raw),"-"],text=True).split("\f")
    rows = actual_table_rows(pages[14])
    check("actual_ten_table_rows", len(rows)==10)
    check("actual_alternative_scenario_marker", "An alternative scenario is shape coexistence" in pages[11])
    check("actual_rotation_axes_and_irrotational_assumption", all(x in pages[11] for x in ["medium axis","short axis","irrotational"]))
    check("actual_Fig16_axis_marker", "FIG. 16." in pages[14] and "increasing direction" in pages[14])

    # Each difference below is polynomial of degree <=3 in each c,s. Exact
    # equality on four distinct c values times four s values certifies it by
    # polynomial unisolvence over Q(sqrt(3)); c^2+s^2=1 is applied afterward.
    identities={k:True for k in ["traceless","quadratic","cubic","sign_axis_swap","plus120_cycle","inertia_trig","inertia_trace"]}
    root3=Q3(Fraction(0),Fraction(1))
    for cv in [-1,0,1,2]:
        for sv in [-1,0,1,2]:
            c,s=Q3.value(cv),Q3.value(sv)
            qx,qy,qz=exact_q(c,s)
            js=((qy-qz)**2/3,(qz-qx)**2/3,(qx-qy)**2/3)
            expected_j=((-s+root3*c)**2/4,(-s-root3*c)**2/4,s*s)
            identities["traceless"] &= qx+qy+qz==Q3()
            identities["quadratic"] &= qx**2+qy**2+qz**2==Fraction(3,2)*(c*c+s*s)
            identities["cubic"] &= qx**3+qy**3+qz**3==Fraction(3,4)*c*(c*c-3*s*s)
            identities["sign_axis_swap"] &= exact_q(c,-s)==(qy,qx,qz)
            identities["plus120_cycle"] &= exact_q((-c-root3*s)/2,(root3*c-s)/2)==(qy,qz,qx)
            identities["inertia_trig"] &= js==expected_j
            identities["inertia_trace"] &= sum(js)==Fraction(3,2)*(c*c+s*s)
    for key,value in identities.items():check("exact_polynomial_"+key,value)
    swap=np.array([[0,1,0],[1,0,0],[0,0,-1]],dtype=int)
    cycle=np.array([[0,1,0],[0,0,1],[1,0,0]],dtype=int)
    def det3(m):
        return sum(int(m[0,j])*(int(m[1,(j+1)%3])*int(m[2,(j+2)%3])-int(m[1,(j+2)%3])*int(m[2,(j+1)%3])) for j in range(3))
    check("sign_swap_proper_rotation", det3(swap)==1 and np.array_equal(swap.T@swap,np.eye(3,dtype=int)))
    check("cycle_proper_rotation", det3(cycle)==1 and np.array_equal(cycle.T@cycle,np.eye(3,dtype=int)))

    known = {"ConfigD1":(.18,22),"ConfigD2":(.20,27),"ConfigD3":(.17,23),"ConfigD4":(.17,35),
             "ConfigD6":(.19,39),"ConfigQ1":(.24,17),"ConfigQ1*":(.24,14),"ConfigQ2":(.22,17),
             "ConfigQ2*":(.22,17),"ConfigQ3Q4":(.16,26)}
    result_rows = []
    sr = np.array(swap,dtype=float)
    cr = np.array(cycle,dtype=float)
    for row in rows:
        values = re.findall(r"[-+]?\d+(?:\.\d+)?",row["deformation_literal"])
        if len(values)!=2:
            raise ValueError("deformation needs visual inspection: "+row["deformation_literal"])
        b,g = map(float,values)
        check("actual_beta_gamma_"+row["name"], (b,g)==known[row["name"]])
        q, qm, qc = tensor(b,g),tensor(b,-g),tensor(b,g+120)
        check("tensor_invariants_"+row["name"], np.isclose(np.trace(q@q),1.5*b*b)
              and np.isclose(np.trace(q@q@q),.75*b**3*math.cos(math.radians(3*g))))
        check("proper_axis_equivalences_"+row["name"], np.allclose(qm,sr@q@sr.T) and np.allclose(qc,cr@q@cr.T))
        result_rows.append({"configuration":row["name"],"source_deformation_literal":row["deformation_literal"],
                            "beta":b,"gamma_degrees":g,"chosen_tensor_diagonal":np.diag(q).tolist(),
                            "quadratic":float(np.trace(q@q)),"cubic":float(np.trace(q@q@q)),
                            "normalized_cubic_cos3gamma":math.cos(math.radians(3*g)),
                            "kind":"deterministic chosen normal-form transform of rounded model parameters; not experimental invariant"})

    qp,qm = tensor(1,20),tensor(1,-20)  # Chosen values, not a source re-signing.
    jp,jm = inertia(qp),inertia(qm)
    axis = np.array([1.,0.,0.])
    rotated_axis = sr@axis
    fixed_plus,fixed_minus = float(axis@jp@axis),float(axis@jm@axis)
    together = float(rotated_axis@jm@rotated_axis)
    check("chosen_same_unordered_shape", np.allclose(np.linalg.eigvalsh(qp),np.linalg.eigvalsh(qm)))
    check("chosen_inertia_axis_equivariance", np.allclose(jm,sr@jp@sr.T))
    check("chosen_fixed_axis_differs", not np.isclose(fixed_plus,fixed_minus))
    check("chosen_simultaneous_axis_rotation_invariant", np.isclose(fixed_plus,together))
    check("chosen_hydrodynamic_inertia_nonnegative", min(np.diag(jp))>=0 and min(np.diag(jm))>=0)
    check("axial_normal_form_limits", np.allclose(np.sort(np.diag(tensor(1,0))),[-.5,-.5,1])
          and np.allclose(np.sort(np.diag(tensor(1,60))),[-1,.5,.5]))
    result={"kind":"actual beta/gamma extraction plus symbolic declared quadrupole/irrotational control; no nuclear model rerun",
            "source":{"path":str(source.relative_to(ROOT)),"raw":str(raw.relative_to(ROOT)),"sha256":sha,
                      "locators":["PDF p.12 alternate D4/D6 paragraph","PDF p.15 TableII","PDF p.15 Fig16"]},
            "chosen_convention":{"axes":"(x,y,z)","qz":"beta cos(gamma)","qx":"beta cos(gamma+120deg)","qy":"beta cos(gamma-120deg)",
                                 "inertia":"Jx=(qy-qz)^2/3 and cyclic; arbitrary common scale, assumed irrotational law",
                                 "author_frame_attested":False,"experimental_invariants":False},
            "symbolic_results":{"TrQ2":"3 beta^2/2","TrQ3":"3 beta^3 cos(3 gamma)/4",
                                "sign_rotation":swap.tolist(),"plus120_cycle":cycle.tolist(),
                                "proof":"exact Q(sqrt3) polynomial identities, degree<=3 in each variable, checked on a 4x4 distinct rational grid; unisolvence",
                                "CAS_dependency":False},
            "actual_model_rows":result_rows,
            "chosen_axis_counterexample":{"beta":1,"gamma_plus":20,"gamma_minus":-20,"fixed_axis":[1,0,0],
                                          "same_sorted_shape":np.linalg.eigvalsh(qp).tolist(),"J_fixed_plus":fixed_plus,
                                          "J_fixed_minus":fixed_minus,"J_simultaneously_rotated":together,
                                          "ratio_fixed_minus_over_plus":fixed_minus/fixed_plus,
                                          "source_D4_reassigned_minus35":False},
            "missing_actual_inputs":["signed rotation-frame gamma/axis mapping for each actual TAC state","numeric alternative-scenario solution and code",
                                     "partner/branch resolved electromagnetic and independent shape observables","experimental response/covariance"],
            "checks":checks,"check_count":len(checks),"passed":all(checks.values())}
    args.output.resolve().relative_to(ROOT)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"checks":len(checks),"passed":result["passed"],"failed":[k for k,v in checks.items() if not v],
                      "fixed_axis_J_plus":fixed_plus,"fixed_axis_J_minus":fixed_minus,"simultaneous":together},ensure_ascii=False))
    return 0 if result["passed"] else 1


if __name__=="__main__":
    raise SystemExit(main())
