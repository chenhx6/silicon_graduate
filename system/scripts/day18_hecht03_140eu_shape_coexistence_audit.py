#!/usr/bin/env python3
"""Conditional high-spin E2 tensor exercise. No paper fit or experimental CI.

Previous result/contract-043 are superseded and never overwritten.
Tensor axes and gamma convention below define THIS design, not paper axes.
"""
import hashlib
import json
import math
from pathlib import Path
import pymupdf

RUN = Path("outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01")
RAW = Path("raw/papers/2003_Hecht et al_Evidence for chiral symmetry breaking in Eu 140.pdf")
RAW_HASH = "5ee92742d8e78a8ccc1a37058bee711d99fadcaf38023a710af186a4fe497463"

def eigenvalues(beta, gamma_deg):
    """Traceless dimensionless quadrupole tensor amplitude proportional to beta."""
    gamma = math.radians(gamma_deg)
    return [beta * math.cos(gamma - 2 * math.pi * k / 3) for k in range(3)]

def anisotropy(q, n):
    """Squared difference of transverse tensor eigenvalues for unit rotation axis n.

    Equal to 2 tr(Q^2) - 4 n.Q^2.n + (n.Q.n)^2 for traceless Q.
    The 2*omega radiation power is proportional to this quantity.
    """
    assert math.isclose(sum(x*x for x in n), 1, abs_tol=1e-12)
    return 2*sum(x*x for x in q) - 4*sum(x*x*y*y for x,y in zip(q,n)) + sum(x*y*y for x,y in zip(q,n))**2

def audit():
    checks = []
    def check(name, condition):
        checks.append({"name": name, "passed": bool(condition)})
        assert condition, name
    check("raw hash unchanged", hashlib.sha256(RAW.read_bytes()).hexdigest() == RAW_HASH)
    with pymupdf.open(RAW) as doc:
        check("14 pages", len(doc) == 14)
        conclusion = doc[12].get_text()
        check("conclusion requests lifetime experiments", "Lifetime ex-" in conclusion and "periments are required" in conclusion)
        check("conclusion compares large jump and smooth increase", "large jump" in conclusion and "smooth increase" in conclusion)
    qa, qb = eigenvalues(.20, -26), eigenvalues(.16, 28)
    radial = (.20/.16)**2
    check("radial only ratio", math.isclose(radial, 1.5625))
    axes = [[1.,0.,0.], [0.,1.,0.], [0.,0.,1.]]
    rows = []
    for k,n in enumerate(axes):
        a,b = anisotropy(qa,n), anisotropy(qb,n)
        i,j = [v for v in range(3) if v != k]
        check(f"axis {k} tensor identity", math.isclose(a,(qa[i]-qa[j])**2, abs_tol=1e-14))
        ratio = a/b
        analytic = radial*math.sin(math.radians(-26)-2*math.pi*k/3)**2/math.sin(math.radians(28)-2*math.pi*k/3)**2
        check(f"axis {k} sine identity", math.isclose(ratio,analytic,rel_tol=1e-12))
        rows.append({"defined_axis":k, "conditional_BE2_ratio":ratio})
    check("beta ratio does not determine BE2 ratio", rows[1]["conditional_BE2_ratio"] < 1 < rows[2]["conditional_BE2_ratio"])
    qax = eigenvalues(1,0)
    check("axial symmetry axis zero", abs(anisotropy(qax,axes[0])) < 1e-12)
    check("axial perpendicular amplitude 9/4", math.isclose(anisotropy(qax,axes[1]),2.25))
    n = [math.sqrt(.2),math.sqrt(.3),math.sqrt(.5)]
    check("simultaneous permutation invariant", math.isclose(anisotropy(qa,n),anisotropy(qa[1:]+qa[:1],n[1:]+n[:1]),abs_tol=1e-14))
    check("zero deformation", anisotropy([0.,0.,0.],n)==0)
    # Constructive different-shape/equal-strength witness. These are free axes,
    # not a claim that either axis solves a TAC/PRM Hamiltonian.
    target = anisotropy(qa,axes[1])
    def response(angle):
        return anisotropy(qb,[0.,math.cos(angle),math.sin(angle)])
    lo,hi = 0., math.pi/2
    check("equal strength bracket", (response(lo)-target)*(response(hi)-target)<0)
    for _ in range(80):
        mid = (lo+hi)/2
        if (response(lo)-target)*(response(mid)-target) <= 0: hi = mid
        else: lo = mid
    angle = (lo+hi)/2
    check("different shape equal strength witness", math.isclose(response(angle),target,rel_tol=1e-12))
    result = {
        "schema_version":1,
        "kind":"conditional-high-spin-tensor-design-not-experimental-fit",
        "source":{"path":str(RAW),"sha256":RAW_HASH,"locator":"PDF p.13 parameters and Conclusion; Fig.9 p.9"},
        "supersedes":["hecht03-140eu-shape-result-043.json","hecht03-140eu-shape-contract-043.json"],
        "parameters":{"beta_a":.20,"gamma_a_deg":-26,"beta_b":.16,"gamma_b_deg":28},
        "radial_only_ratio":radial,
        "same_defined_principal_axis_controls":rows,
        "equal_strength_witness":{"n_a":axes[1],"n_b":[0.,math.cos(angle),math.sin(angle)],"angle_in_defined_1_2_plane_deg":math.degrees(angle),"ratio":target/response(angle)},
        "checks":checks,"valid":all(x["passed"] for x in checks),
        "readiness":{"actual_axis":"not certified","finite_spin_wavefunctions":"not supplied","paper_strength_or_CI_reproduction":False,"independent_experiment":False}
    }
    path = RUN/"hecht03-geometry-correction-result-045.json"
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"valid":result["valid"],"checks":len(checks),"principal_controls":rows,"equal_strength_angle_deg":math.degrees(angle),"output":str(path)}))

if __name__ == "__main__":
    audit()
