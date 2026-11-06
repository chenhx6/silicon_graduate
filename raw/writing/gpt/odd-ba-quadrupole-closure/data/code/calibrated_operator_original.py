"""All-branch central E2 calibration and withheld 135Ba prediction.

Two explicit stages keep the analytic calibration independent of the holdout.
Writes only beside this file. Existing modules, inputs and contracts are read-only.
"""

import os
import sys

sys.dont_write_bytecode = True
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
             "BLIS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_key] = "1"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

import argparse
from datetime import datetime, timezone
import csv
import ctypes
import hashlib
import json
import math
from pathlib import Path
import time
import traceback

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
CONTRACT = OUT / "calibrated-operator-contract.json"
CONTRACT_SHA = "5d49a9ceda150dea250e80eceb1389fdc6b96f6af4307ca2c6c8c2aabb75b6ff"
sys.path.insert(0, str(ROOT / "system/scripts/analysis"))

import numpy as np
import scipy
from single_j_ibfm import IBFMParameters, IBFMKernel, CoreParameters, BosonCore, transition_rme, calibrate_core_e2
from paired_single_j_em import clebsch_gordan
from quadrupole_scalar_invariants import (
    ReducedQuadrupole, direct_from_spectrum, reduced_table_from_spectrum,
    reduced_invariants, j_plus_two_proxy,
)


def utc():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def array_sha(value):
    return hashlib.sha256(np.ascontiguousarray(value).tobytes()).hexdigest()


def csr_sha(value):
    h = hashlib.sha256(str(value.shape).encode())
    for array in (value.data, value.indices, value.indptr):
        h.update(np.ascontiguousarray(array).tobytes())
    return h.hexdigest()


def write_new(name, value):
    with (OUT/name).open("x", encoding="utf-8") as f:
        json.dump(value, f, indent=2, ensure_ascii=False, allow_nan=False)
        f.write("\n")


def verify_inputs(c):
    assert sha(CONTRACT) == CONTRACT_SHA, "Frozen contract changed."
    for item in c["input_files"] + c["read_only_modules"]:
        if sha(ROOT/item["path"]) != item["sha256"]:
            raise RuntimeError(f"Read-only input changed: {item['path']}")


def blas_threads():
    paths = sorted({line.split()[-1] for line in Path("/proc/self/maps").read_text().splitlines()
                    if "openblas" in line.lower() and ".so" in line and line.split()[-1].startswith("/")})
    found = []
    for path in paths:
        lib = ctypes.CDLL(path)
        for name in ("scipy_openblas_get_num_threads64_", "scipy_openblas_get_num_threads",
                     "openblas_get_num_threads64_", "openblas_get_num_threads"):
            try:
                f = getattr(lib, name)
            except AttributeError:
                continue
            f.argtypes = []
            f.restype = ctypes.c_int
            n = int(f())
            if n != 1:
                raise RuntimeError(f"Non-single-thread BLAS: {path}: {n}")
            found.append({"library": path, "query": name, "threads": n})
            break
        else:
            raise RuntimeError(f"Cannot verify thread count: {path}")
    if not found:
        raise RuntimeError("No BLAS thread count verified.")
    return found


def real(value, name):
    value = complex(value)
    if not math.isfinite(value.real) or not math.isfinite(value.imag):
        raise ValueError(f"Nonfinite {name}")
    if abs(value.imag) > 1e-12 + 1e-10*abs(value.real):
        raise ValueError(f"{name} is not real in the fixed eigenvector convention.")
    return float(value.real)


def check(value, expected, c, name):
    error = abs(value-expected)
    n = c["numerics"]
    if error > n["replay_atol"] + n["replay_rtol"]*abs(expected):
        raise ValueError(f"{name}: {value} vs {expected}; abs error {error}")
    return error


def lowest(s, two_J):
    ix = s.indices_for_J(two_J)
    ix = ix[np.argsort(s.energies[ix], kind="stable")]
    if not len(ix):
        raise ValueError("Requested spin missing.")
    if len(ix) > 1 and s.energies[ix[1]]-s.energies[ix[0]] <= 1e-10:
        raise ValueError("Unresolved lowest-state same-spin degeneracy.")
    return int(ix[0])


def build(c, odd_A):
    params = c["kernel_parameters_by_odd_A"][str(odd_A)]
    k = IBFMKernel(IBFMParameters(**params))
    s = k.solve(two_M=1)
    i = lowest(s, 11)
    b = BosonCore(CoreParameters(params["n_b"], params["eps_d"], params["kappa"], params["chi"]))
    bs = b.solve(two_M=0)
    return k, s, i, b, bs, lowest(bs, 0), lowest(bs, 4)


def static_qs(s, op, i):
    tj = int(s.two_J[i])
    rme = transition_rme(s, op, i, i)
    scale = math.sqrt(16*math.pi/5)*clebsch_gordan(tj, tj, 4, 0, tj, tj)/math.sqrt(tj+1)
    return real(scale*rme, "spectroscopic Qs")


def fingerprint(k, s, i):
    return {"state_index": i, "state_energy_MeV": float(s.energies[i]),
            "state_vector_sha256": array_sha(s.vectors[:, i]),
            "Hamiltonian_csr_sha256": csr_sha(k.hamiltonian),
            "dimension_full": k.dimension, "dimension_M_half": s.basis.dimension,
            "solver_diagnostics": dict(s.diagnostics)}


def calibration_stage(c):
    start, clock = utc(), time.perf_counter()
    threads = blas_threads()
    k, s, i, core, cs, c0, c2 = build(c, 137)
    unit0, unit1 = core.e2(1, 0), core.e2(1, 1)
    a = real(transition_rme(cs, unit0, c0, c2), "a")
    b = real(transition_rme(cs, unit1, c0, c2), "a+b")-a
    cc = static_qs(cs, unit0, c2)
    d = static_qs(cs, unit1, c2)-cc
    u = static_qs(s, k.e2(1, 0, 0), i)
    v = static_qs(s, k.e2(1, 0, 1), i)-u
    w = static_qs(s, k.e2(0, 1, 0), i)
    Bup = c["core_calibrations"]["136"]["B_up_e2b2"]
    g = math.sqrt(Bup)
    coefficients = {"a_transition": a, "b_transition": b, "c_core_Qs": cc, "d_core_Qs": d,
                    "u_odd137_boson_Qs": u, "v_odd137_boson_Qs": v, "w_odd137_fermion_Qs": w,
                    "Bup136": Bup, "sqrt_Bup136": g,
                    "calibration_pole_chi": -a/b if b else None,
                    "core_Qs_limit_chi_positive_infinity": g*d/abs(b) if b else None,
                    "core_Qs_limit_chi_negative_infinity": -g*d/abs(b) if b else None,
                    "ad_minus_bc": a*d-b*cc}
    # Replay affine matrix elements away from 0 and 1 before using them.
    for chi in (-0.85, 0.35, 2.0):
        op = core.e2(1, chi)
        check(real(transition_rme(cs, op, c0, c2), "T(chi)"), a+b*chi, c, "linear transition")
        check(static_qs(cs, op, c2), cc+d*chi, c, "linear core Qs")
        check(static_qs(s, k.e2(1, 0, chi), i), u+v*chi, c, "linear odd137 boson Qs")
    primary_eB = g/abs(a+0.35*b)
    ref137 = next(r for r in c["reference_primary"] if r["odd_A"] == 137)
    check(primary_eB, ref137["eB"], c, "primary eB136")
    baseline_core_Qs = primary_eB*(cc+0.35*d)
    if abs(baseline_core_Qs-c["reference_primary_core136_Qs_rounded_eb"]) > 1e-7:
        raise ValueError("Primary core Qs failed rounded source-card replay.")
    check(primary_eB*(u+0.35*v)+0.125*w, ref137["Qs_eb"], c, "primary Qs137")

    candidates, roots, warnings = [], [], []
    for target in c["core_136_moment_targets"]:
        t = target["target_Qs_eb"]
        for sign in c["analytic_contract"]["sign_branches"]:
            denom = g*d-t*sign*b
            numer = t*sign*a-g*cc
            scale = max(abs(g*d), abs(t*b), 1e-300)
            record = {"target_id": target["id"], "target_Qs136_eb": t,
                      "algebra_sign_s": sign, "linear_coefficient": denom, "linear_RHS": numer,
                      "source_provenance": target["provenance"],
                      "near_degenerate_linear_coefficient": abs(denom) <= c["numerics"]["near_singular_relative_threshold"]*scale}
            if denom == 0:
                record["status"] = "continuum_on_sign_interval" if numer == 0 else "no_root_on_sign_branch"
                candidates.append(record)
                warnings.append(record)
                continue
            chi = numer/denom
            record["candidate_chi_E"] = chi
            if not math.isfinite(chi):
                record["status"] = "nonfinite_candidate"
                candidates.append(record)
                warnings.append(record)
                continue
            transition = a+b*chi
            record["unit_transition_RME"] = transition
            if transition == 0:
                record["status"] = "zero_calibration_denominator"
                candidates.append(record)
                warnings.append(record)
                continue
            record["near_calibration_pole"] = abs(transition) <= c["numerics"]["near_singular_relative_threshold"]*max(abs(a), abs(b*chi), 1e-300)
            if sign*transition <= 0:
                record["status"] = "extraneous_wrong_absolute_value_branch"
                candidates.append(record)
                continue
            eB = g/abs(transition)
            fitted_core = eB*(cc+d*chi)
            check(fitted_core, t, c, "unsquared core moment equation")
            if w == 0:
                residual = c["Q137_calibration"]["target_Qs_eb"]-eB*(u+v*chi)
                record["status"] = "eF_underdetermined_continuum" if residual == 0 else "eF_fit_impossible_zero_response"
                candidates.append(record)
                warnings.append(record)
                continue
            eF = (c["Q137_calibration"]["target_Qs_eb"]-eB*(u+v*chi))/w
            if not math.isfinite(eB) or not math.isfinite(eF):
                record["status"] = "nonfinite_charge"
                candidates.append(record)
                warnings.append(record)
                continue
            root_id = f"{target['id']}_s{'plus' if sign > 0 else 'minus'}"
            measured_core = static_qs(cs, core.e2(eB, chi), c2)
            measured_137 = static_qs(s, k.e2(eB, eF, chi), i)
            eB_replay = calibrate_core_e2(core, cs, c0, c2, chi_prime=chi, target_B_0_to_2=Bup)
            check(eB_replay.eB, eB, c, "positive core strength recalibration")
            root = {
                "root_id": root_id, "target_id": target["id"], "target_Qs136_eb": t,
                "source_provenance": target["provenance"], "algebra_sign_s": sign,
                "chi_E": chi, "eB136_eb": eB, "eF_eb": eF, "unit_transition_RME": transition,
                "charge_positive_eF": eF > 0, "charge_nonnegative_eF": eF >= 0,
                "source_parameter_interval_known": False,
                "near_calibration_pole": record["near_calibration_pole"],
                "near_degenerate_linear_coefficient": record["near_degenerate_linear_coefficient"],
                "Qs136_replayed_eb": measured_core, "Qs137_replayed_eb": measured_137,
                "Qs136_abs_residual": check(measured_core, t, c, "core target replay"),
                "Qs137_abs_residual": check(measured_137, c["Q137_calibration"]["target_Qs_eb"], c, "odd137 target replay"),
                "core_Qs_derivative_per_chi": g*sign*(a*d-b*cc)/(transition*transition),
                "fermion_Qs_derivative_per_eF": w,
                "condition": "each Q136 alternative paired conditionally with the same averaged Bup=.407; no joint covariance fit",
            }
            roots.append(root)
            record.update(status="accepted_finite_real_root", root_id=root_id, eB136_eb=eB, eF_eb=eF)
            candidates.append(record)
            if record["near_calibration_pole"] or record["near_degenerate_linear_coefficient"]:
                warnings.append({"root_id": root_id, "condition": "near-singular calibration"})
            if eF <= 0:
                warnings.append({"root_id": root_id, "condition": "algebraic solution violates an additional positive-eF assumption; retained"})
            print(f"Q136={t:+.2f}, s={sign:+d}: chiE={chi:.12g}, eB136={eB:.12g}, eF={eF:.12g}; positive_eF={eF>0}", flush=True)
    result = {
        "schema": "all-real-central-moment-calibration-branches/1", "contract_sha256": CONTRACT_SHA,
        "coefficients": coefficients, "candidate_count": len(candidates), "accepted_root_count": len(roots),
        "candidates": candidates, "roots": roots, "warnings": warnings,
        "baseline_core136_Qs_eb": baseline_core_Qs, "baseline_eB136_eb": primary_eB,
        "odd137_fingerprint": fingerprint(k, s, i),
        "core136_indices": {"initial_0plus": c0, "final_2plus": c2},
        "core136_fingerprint": {"Hamiltonian_csr_sha256": csr_sha(core.hamiltonian),
                               "initial_vector_sha256": array_sha(cs.vectors[:, c0]),
                               "final_vector_sha256": array_sha(cs.vectors[:, c2])},
        "135_state_Qs_or_proxy_evaluated_during_calibration": False,
        "no_roots_discarded_for_negative_eF": True,
    }
    verify_inputs(c)
    write_new("linear-calibration.json", result)
    write_new("calibration-run.json", {
        "status": "completed", "started_at_utc": start, "finished_at_utc": utc(),
        "elapsed_seconds": time.perf_counter()-clock, "native_BLAS": threads,
        "driver_sha256": sha(__file__), "contract_sha256": CONTRACT_SHA,
        "linear_calibration_sha256": sha(OUT/"linear-calibration.json"),
        "accepted_roots": len(roots), "inputs_and_modules_unchanged": True,
    })
    print(f"Calibration enumerated {len(candidates)} sign candidates; {len(roots)} finite roots; warnings={len(warnings)}. No holdout used.", flush=True)


def angle(ratio):
    if ratio is None:
        return None, "undefined_zero_quadratic"
    if abs(ratio) > 1:
        return None, "outside_rigid_domain"
    return math.degrees(math.acos(ratio))/3, "within_rigid_domain"


def prediction_stage(c):
    start, clock = utc(), time.perf_counter()
    threads = blas_threads()
    calibration_path = OUT/"linear-calibration.json"
    fitted = json.loads(calibration_path.read_text())
    prior = json.loads((OUT/"calibration-run.json").read_text())
    if sha(calibration_path) != prior["linear_calibration_sha256"]:
        raise ValueError("Calibrated branches changed before prediction.")
    if not fitted["roots"]:
        raise ValueError("No finite identified calibration roots to predict.")
    settings = [{"root_id": "primary_reference", "chi_E": 0.35, "eF_eb": 0.125,
                 "target_Qs136_eb": None, "algebra_sign_s": None}] + fitted["roots"]
    rows, models = [], []
    validation = {"max_q2_closure_abs": 0., "max_q3_closure_abs": 0., "max_137_calibration_Qs_abs": 0.,
                  "max_core_Bup_abs": 0., "max_primary_replay_abs": 0.}
    options = {"rtol": c["numerics"]["module_rtol"], "atol": c["numerics"]["module_atol"], "angle_tolerance": 0.}
    for odd_A in [135,137]:
        k, s, i, core, cs, c0, c2 = build(c, odd_A)
        fp = fingerprint(k,s,i)
        if odd_A == 137:
            for key in ["state_vector_sha256","Hamiltonian_csr_sha256"]:
                if fp[key] != fitted["odd137_fingerprint"][key]:
                    raise ValueError("137 calibration and prediction state/H changed.")
        order = np.argsort(s.energies, kind="stable")
        ordered_i = int(np.flatnonzero(order == i)[0])
        core_A = odd_A-1
        Bup = c["core_calibrations"][str(core_A)]["B_up_e2b2"]
        target0 = real(transition_rme(cs,core.e2(1,0),c0,c2), "core transition intercept")
        target1 = real(transition_rme(cs,core.e2(1,1),c0,c2), "core transition at chi1")-target0
        fp["core_A"] = core_A
        fp["core_calibration_transition_coefficients"] = {"a":target0,"b":target1,"pole":-target0/target1 if target1 else None}
        models.append({"odd_A":odd_A,**fp})
        ref = next(r for r in c["reference_primary"] if r["odd_A"] == odd_A)
        beta_prefactor = 100*4*math.pi/(3*56*(1.2*odd_A**(1/3))**2)
        for setting in settings:
            chi, ef = setting["chi_E"],setting["eF_eb"]
            row={"odd_A":odd_A,"root_id":setting["root_id"],"target_Qs136_eb":setting["target_Qs136_eb"],
                 "algebra_sign_s":setting["algebra_sign_s"],"chi_E":chi,"eF_eb":ef,"charge_positive_eF":ef>0}
            den=target0+target1*chi
            if den == 0:
                row["prediction_status"]="zero_core_calibration_denominator"
                rows.append(row)
                print(f"{odd_A} {setting['root_id']}: zero core calibration denominator; branch retained, prediction unavailable.",flush=True)
                continue
            cal=calibrate_core_e2(core,cs,c0,c2,chi_prime=chi,target_B_0_to_2=Bup)
            eB=cal.eB
            measured_B=abs(transition_rme(cs,core.e2(eB,chi),c0,c2))**2
            validation["max_core_Bup_abs"]=max(validation["max_core_Bup_abs"],check(measured_B,Bup,c,"Bup replay"))
            if odd_A==137 and setting["root_id"]!="primary_reference":
                check(eB,setting["eB136_eb"],c,"eB137 uses same calibrated core136")
            op=k.e2(eB,ef,chi)
            qs=static_qs(s,op,i)
            qs_b=static_qs(s,k.e2(eB,0,chi),i)
            qs_f=static_qs(s,k.e2(0,ef,chi),i)
            check(qs,qs_b+qs_f,c,"Qs boson+fermion linear decomposition")
            direct=direct_from_spectrum(s,op,i,representation_label=f"{odd_A}Ba frozen model",**options)
            rt=reduced_table_from_spectrum(s,op,representation_label=f"{odd_A}Ba frozen model",
                                           rtol=options["rtol"],atol=options["atol"])
            table=ReducedQuadrupole(rt.representation,tuple(rt.multiplets[x] for x in order),
                                    rt.rme[np.ix_(order,order)],rt.complete,rt.unresolved)
            closure=reduced_invariants(table,ordered_i,**options)
            if not closure.complete or closure.invariants is None:
                raise ValueError("Incomplete required closure.")
            dq2=check(closure.invariants.q2,direct.q2,c,"q2 direct vs reduced")
            dq3=check(closure.invariants.q3,direct.q3,c,"q3 direct vs reduced")
            validation["max_q2_closure_abs"]=max(validation["max_q2_closure_abs"],dq2)
            validation["max_q3_closure_abs"]=max(validation["max_q3_closure_abs"],dq3)
            row.update(prediction_status="finite",eB_eb=eB,core_Bup_target=Bup,Qs_eb=qs,
                       Qs_boson_eb=qs_b,Qs_fermion_eb=qs_f,full_q2=direct.q2,
                       full_signed_q3=direct.q3,full_signed_ratio=direct.raw_ratio,
                       full_signed_angle=direct.rigid_equivalent_angle_deg,
                       full_folded_angle=angle(abs(direct.raw_ratio))[0],full_angle_status=direct.angle_status,
                       full_beta=beta_prefactor*math.sqrt(direct.q2),q2_closure_abs=dq2,q3_closure_abs=dq3)
            cg=clebsch_gordan(15,11,4,0,11,11)
            for label,n in [("n5",5),("all",None)]:
                p=j_plus_two_proxy(table,ordered_i,max_states=n,**options)
                row.update({f"{label}_states":len(p.selected_labels),
                            f"{label}_q2_raw":p.quadratic_strength_sum,
                            f"{label}_q2_contribution":p.quadratic_closure_contribution,
                            f"{label}_fraction_full_q2":p.quadratic_closure_contribution/direct.q2,
                            f"{label}_signed_chain":p.cubic_chain.real,
                            f"{label}_q3_absolute_scaled":p.scaled_absolute_chain,
                            f"{label}_raw_ratio":p.raw_proxy_ratio,f"{label}_angle":p.proxy_angle_deg,
                            f"{label}_angle_status":p.angle_status,
                            f"{label}_beta":beta_prefactor*math.sqrt(p.quadratic_strength_sum/16/cg**2)})
            row["n5_fraction_all_Jplus2_q2"]=row["n5_q2_contribution"]/row["all_q2_contribution"]
            if odd_A==137 and setting["root_id"]!="primary_reference":
                validation["max_137_calibration_Qs_abs"]=max(validation["max_137_calibration_Qs_abs"],check(qs,0.78,c,"137 fitted moment"))
            if setting["root_id"]=="primary_reference":
                for key,val in [("Qs_eb",ref["Qs_eb"]),("eB_eb",ref["eB"]),
                                ("full_q2",ref["full"]["q2_e2b2"]),("full_signed_q3",ref["full"]["q3_e3b3"]),
                                ("n5_raw_ratio",ref["proxy_n5_ratio"]),("all_raw_ratio",ref["proxy_all_ratio"])]:
                    validation["max_primary_replay_abs"]=max(validation["max_primary_replay_abs"],check(row[key],val,c,"primary reference"))
            if odd_A==135:
                for test in c["Q135_out_of_calibration_tests"]:
                    name,t,margin=test["id"],test["target_Qs_eb"],test["quoted_margin_eb"]
                    row[f"holdout_{name}_signed_residual_eb"]=qs-t
                    row[f"holdout_{name}_abs_error_improvement_eb"]=abs(ref["Qs_eb"]-t)-abs(qs-t)
                    row[f"holdout_{name}_inside_quoted_margin"]=abs(qs-t)<=margin
            rows.append(row)
            print(f"{odd_A} {setting['root_id']}: Qs={qs:.10g}; eF={ef:.10g}; full c={direct.raw_ratio:.9g}; proxy5/all={row['n5_raw_ratio']:.9g}/{row['all_raw_ratio']:.9g}",flush=True)
        if csr_sha(k.hamiltonian)!=fp["Hamiltonian_csr_sha256"] or array_sha(s.vectors[:,i])!=fp["state_vector_sha256"]:
            raise ValueError("Hamiltonian or state changed across calibrated operators.")
    verify_inputs(c)
    result={"schema":"moment-calibrated-E2-holdout-predictions/1","contract_sha256":CONTRACT_SHA,
            "linear_calibration_sha256":sha(calibration_path),"models":models,"rows":rows,
            "validation":validation,"all_finite_roots_evaluated_without_holdout_selection":True,
            "positive_eF_is_a_classification_not_an_exclusion":True,
            "all_target_pairs_are_conditional_at_fixed_Bup":True,"no_uncertainty_posterior":True,
            "no_published_operator_reproduction_claim":True,"no_state_pair_JSON":True}
    write_new("predictions.json",result)
    columns=list(dict.fromkeys(k for r in rows for k in r))
    with (OUT/"predictions.csv").open("x",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=columns);writer.writeheader();writer.writerows(rows)
    write_new("prediction-run.json",{"status":"completed","started_at_utc":start,"finished_at_utc":utc(),
              "elapsed_seconds":time.perf_counter()-clock,"contract_sha256":CONTRACT_SHA,
              "driver_sha256":sha(__file__),"native_BLAS":threads,"validation":validation,
              "predictions_sha256":sha(OUT/"predictions.json"),"csv_sha256":sha(OUT/"predictions.csv"),
              "input_and_module_hashes_unchanged":True,"python":sys.version.split()[0],
              "numpy":np.__version__,"scipy":scipy.__version__,"no_commit":True})


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--stage",choices=["calibrate","predict"],required=True)
    args=parser.parse_args()
    try:
        c=json.loads(CONTRACT.read_text());verify_inputs(c)
        calibration_stage(c) if args.stage=="calibrate" else prediction_stage(c)
    except Exception:
        write_new(f"failure-{time.time_ns()}.json",{"stage":args.stage,"at_utc":utc(),"traceback":traceback.format_exc(),
                                                 "driver_sha256":sha(__file__),"contract_sha256":sha(CONTRACT)})
        raise
