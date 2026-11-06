#!/usr/bin/env python3
"""Exploratory comparison of full scalar E2 moments and a restricted prescription.

No new Hamiltonian fit is performed. This is a model/definition diagnostic,
not a measurement of intrinsic shape or a novelty claim.
"""
from dataclasses import replace
import hashlib
import json
import math
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT/"system/scripts/analysis"))
from single_j_ibfm import (
    IBFMParameters, CoreParameters, IBFMKernel, BosonCore,
)
from paired_single_j_em import clebsch_gordan as cg

OUT = Path(__file__).resolve().parent
CASE = ROOT/"outputs/l4/20261105-ba129-controlled-pairing/ibfm-case-v1/prediction.json"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def gamma_coordinate(ratio):
    # Only remove numerical overshoot at an exact boundary; never hide a
    # material domain violation with an unconditional clamp.
    if abs(ratio) > 1 + 1e-12:
        return None
    return math.degrees(math.acos(max(-1., min(1., ratio))))/3


def moments(solution, operator, state):
    if operator.rank != 2 or solution.model_key != operator.model_key:
        raise ValueError("matching rank-2 tensor required")
    psi = np.zeros(solution.basis.full_dimension, dtype=complex)
    psi[solution.basis.full_indices] = solution.vectors[:, state]
    v = {q: operator.components[q] @ psi for q in range(-2, 3)}
    q2 = float(sum(np.vdot(z, z).real for z in v.values()))
    cubic = 0j
    for m in range(-2, 3):
        for n in range(-2, 3):
            p = -m-n
            if abs(p) <= 2:
                cubic += ((-1.)**n * cg(4, 2*m, 4, 2*n, 4, 2*(m+n))
                          * np.vdot(v[-m], operator.components[n] @ v[p]))
    if abs(cubic.imag) > 1e-10*max(1., abs(cubic)):
        raise ValueError("cubic scalar is not real at numerical tolerance")
    q3 = -math.sqrt(7/2)*float(cubic.real)
    ratio = q3/q2**1.5 if q2 > 0 else None
    return {"q2_scalar": q2, "q3_scalar_signed": q3,
            "ratio_signed": ratio,
            "gamma_rigid_equivalent_signed_deg": gamma_coordinate(ratio) if ratio is not None else None,
            "gamma_folded_deg": gamma_coordinate(abs(ratio)) if ratio is not None else None,
            "cubic_imaginary_residual": float(cubic.imag)}


def channel_closure(solution, operator, state):
    ji, m = int(solution.two_J[state]), int(solution.basis.two_M)
    component = solution.vectors.conj().T @ (
        operator.block(solution.basis) @ solution.vectors[:, state])
    result = {}
    for jf in range(max(0, ji-4), ji+5, 2):
        indices = solution.indices_for_J(jf)
        if not len(indices) or ji+jf < 4:
            continue
        coefficient = cg(ji, m, 4, 0, jf, m)/math.sqrt(jf+1)
        if coefficient == 0:
            raise ValueError("this M component does not resolve a permitted channel")
        u = component[indices]/coefficient
        result[str(jf)] = {"state_count": len(indices),
                           "q2_contribution": float(np.vdot(u, u).real/(ji+1))}
    return result


def restricted(solution, operator, state, count):
    ji, m = int(solution.two_J[state]), int(solution.basis.two_M)
    jp = ji+4
    indices = solution.indices_for_J(jp)
    if count is not None:
        indices = indices[:count]
    if not len(indices):
        raise ValueError("no J+2 intermediate state")
    t = operator.block(solution.basis)
    vectors = solution.vectors[:, indices]
    factor_up = cg(ji, m, 4, 0, jp, m)/math.sqrt(jp+1)
    factor_same = cg(jp, m, 4, 0, jp, m)/math.sqrt(jp+1)
    if factor_up == 0 or factor_same == 0:
        raise ValueError("zero component CG in restricted prescription")
    u = vectors.conj().T @ (t @ solution.vectors[:, state])/factor_up
    target_rme = vectors.conj().T @ (t @ vectors)/factor_same
    q2 = float(np.vdot(u, u).real)
    chain = np.vdot(u, target_rme @ u)
    if abs(chain.imag) > 1e-10*max(1, abs(chain)):
        raise ValueError("restricted cubic chain is not real")
    q3 = math.sqrt(7/10)*abs(chain)
    z = float(q3/q2**1.5)
    band_cg = cg(jp, ji, 4, 0, ji, ji)
    beta_scale = math.sqrt(q2/((jp+1)*band_cg**2))
    return {"count_requested": count, "states_used": len(indices), "two_Jprime": jp,
            "q2_raw_restricted": q2, "q2_with_scalar_normalization": q2/(ji+1),
            "q3_raw_restricted_abs": float(q3), "gamma_argument": z,
            "gamma_proxy_deg": gamma_coordinate(z), "beta_proxy_without_radius_prefactor": beta_scale}


def assess(solution, operator, state):
    full = moments(solution, operator, state)
    channels = channel_closure(solution, operator, state)
    closure = sum(c["q2_contribution"] for c in channels.values())
    if abs(closure-full["q2_scalar"]) > 2e-10*max(1, full["q2_scalar"]):
        raise ValueError("all-spin RME quadratic closure failed")
    proxies = [restricted(solution, operator, state, n) for n in (1, 5, None)]
    for r in proxies:
        r["retained_fraction_of_full_q2"] = r["q2_with_scalar_normalization"]/full["q2_scalar"]
        r["beta_proxy_over_full_invariant_scale"] = (
            r["beta_proxy_without_radius_prefactor"]/math.sqrt(full["q2_scalar"]))
    return {"state_index": int(state), "two_J": int(solution.two_J[state]),
            "full_moments": full, "quadratic_spin_channels": channels,
            "quadratic_RME_closure_error": closure-full["q2_scalar"],
            "restricted_prescriptions": proxies}


def axial_controls():
    rows = []
    for ji in (0, 1, 3, 5, 7, 9, 11, 13):
        jp, k = ji+4, ji
        up = math.sqrt(ji+1)*cg(ji, k, 4, 0, jp, k)
        diagonal = math.sqrt(jp+1)*cg(jp, k, 4, 0, jp, k)
        z = math.sqrt(.7)*abs(diagonal/up)
        rows.append({"two_J": ji, "K_equals_J": True, "intrinsic_gamma_deg": 0.,
                     "restricted_argument": z, "restricted_gamma_deg": gamma_coordinate(z)})
    # Intrinsic c-number normalization of the FULL cubic scalar.
    for gamma in (0, 10, 30, 40, 60):
        q = {0: math.cos(math.radians(gamma)),
             2: math.sin(math.radians(gamma))/math.sqrt(2),
             -2: math.sin(math.radians(gamma))/math.sqrt(2), 1: 0., -1: 0.}
        cubic = sum((-1.)**(m+n)*cg(4, 2*m, 4, 2*n, 4, 2*(m+n))*q[m]*q[n]*q[-m-n]
                    for m in range(-2,3) for n in range(-2,3) if abs(m+n)<=2)
        assert abs(-math.sqrt(7/2)*cubic-math.cos(3*math.radians(gamma))) < 1e-13
    return rows


def main():
    locked = {p: digest(p) for p in (
        CASE, Path(__file__), ROOT/"system/scripts/analysis/single_j_ibfm.py",
        ROOT/"system/scripts/analysis/paired_single_j_em.py")}
    old = json.loads(CASE.read_text())
    params = IBFMParameters(**old["parameters"])
    core = BosonCore(CoreParameters(params.n_b, params.eps_d, params.kappa, params.chi))
    cs = core.solve()
    eB, eF, chiE = (old["core_calibration"][k] for k in ("eB", "eF_eb", "chi_E2"))
    cstate = int(cs.indices_for_J(0)[0])
    core_result = assess(cs, core.e2(eB, chiE), cstate)
    odd = IBFMKernel(params)
    os = odd.solve()
    state = int(os.indices_for_J(11)[0])
    odd_result = assess(os, odd.e2(eB, eF, chiE), state)
    ms = odd.solve(two_M=3)
    mstate = int(ms.indices_for_J(11)[0])
    other_M = moments(ms, odd.e2(eB, eF, chiE), mstate)
    for key in ("q2_scalar", "q3_scalar_signed"):
        assert abs(other_M[key]-odd_result["full_moments"][key]) < 1e-10
    spectator = IBFMKernel(replace(params, Gamma0=0., Lambda0=0., A0=0.))
    ss = spectator.solve()
    sstate = int(ss.indices_for_J(11)[0])
    spectator_result = assess(ss, spectator.e2(eB, 0., chiE), sstate)
    for key in ("q2_scalar", "q3_scalar_signed"):
        assert abs(spectator_result["full_moments"][key]-core_result["full_moments"][key]) < 1e-10
    for p, h in locked.items():
        if digest(p) != h:
            raise RuntimeError(f"input changed during probe: {p}")
    result = {"scope": __doc__, "input_sha256": {str(p.relative_to(ROOT)): h for p,h in locked.items()},
              "core_128_J0": core_result, "odd_129_J11half": odd_result,
              "spectator_J11half_core_operator_only": spectator_result,
              "odd_other_M_full_moments": other_M,
              "axial_K_equals_J_controls": axial_controls(),
              "boundary": "Full moments are rotation scalars; a rigid-equivalent gamma remains conditional on operator and fluctuation assumptions. Restricted prescription is a defined proxy. No journal readiness or novelty claim."}
    out = OUT/"probe-v1.json"
    if out.exists():
        raise FileExistsError(out)
    out.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")
    for label, r in [("core", core_result), ("odd", odd_result), ("spectator", spectator_result)]:
        print(label, json.dumps({"full": r["full_moments"], "restricted5": r["restricted_prescriptions"][1],
                                  "restricted_all": r["restricted_prescriptions"][2]}))


if __name__ == "__main__":
    main()
