"""Frozen, one-factor operator sensitivity on five fixed odd-Ba Hamiltonians.

Writes only beside this driver. Existing modules and inputs are read-only.
No Hamiltonian fit, coupling ablation, full RME/pair export, or source replay.
"""

import os
import sys

sys.dont_write_bytecode = True
for _name in (
    "OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
    "BLIS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS",
):
    os.environ[_name] = "1"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

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
CONTRACT = OUT / "operator-sensitivity-contract.json"
FROZEN_CONTRACT_SHA = "688386441deb562b19f7dc5df8b3abeb522976fd9daebf367a4781ca2e53de1e"
sys.path.insert(0, str(ROOT / "system/scripts/analysis"))

import numpy as np
import scipy
from single_j_ibfm import (
    IBFMParameters, IBFMKernel, CoreParameters, BosonCore,
    calibrate_core_e2, transition_rme,
)
from paired_single_j_em import clebsch_gordan
from quadrupole_scalar_invariants import (
    ReducedQuadrupole, direct_from_spectrum, reduced_table_from_spectrum,
    reduced_invariants, j_plus_two_proxy,
)


def utc():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def json_sha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def array_sha(a):
    return hashlib.sha256(np.ascontiguousarray(a).tobytes()).hexdigest()


def csr_sha(a):
    digest = hashlib.sha256()
    digest.update(str(a.shape).encode())
    for field in (a.data, a.indices, a.indptr):
        digest.update(np.ascontiguousarray(field).tobytes())
    return digest.hexdigest()


def write_new(name, data):
    with (OUT / name).open("x", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, ensure_ascii=False, allow_nan=False)
        handle.write("\n")


def native_blas_threads():
    libraries = sorted({
        line.split()[-1]
        for line in Path("/proc/self/maps").read_text().splitlines()
        if "openblas" in line.lower() and ".so" in line and line.split()[-1].startswith("/")
    })
    found = []
    for name in libraries:
        lib = ctypes.CDLL(name)
        for symbol in (
            "scipy_openblas_get_num_threads64_", "scipy_openblas_get_num_threads",
            "openblas_get_num_threads64_", "openblas_get_num_threads",
        ):
            try:
                func = getattr(lib, symbol)
            except AttributeError:
                continue
            func.argtypes = []
            func.restype = ctypes.c_int
            threads = int(func())
            if threads != 1:
                raise RuntimeError(f"BLAS is not single-threaded: {name}: {threads}")
            found.append({"library": name, "query_symbol": symbol, "threads": threads})
            break
        else:
            raise RuntimeError(f"Cannot verify loaded OpenBLAS thread count: {name}")
    if not found:
        raise RuntimeError("No loaded OpenBLAS found for direct thread verification.")
    return found


def calibration_numeric_projection(data):
    rows = []
    for row in data["selected_rows"]:
        value = row["selected_strength"]
        rows.append({
            "core_A": row["A"],
            "B_down_e2b2": value["B_down_e2b2"],
            "B_up_e2b2": value["B_up_e2b2"],
            "B_down_margin_e2b2": value["B_down_margin_e2b2"],
        })
    return sorted(rows, key=lambda row: row["core_A"])


def lowest(solution, two_j):
    indices = solution.indices_for_J(two_j)
    if not len(indices):
        raise ValueError(f"No state with two_J={two_j}")
    order = indices[np.argsort(solution.energies[indices], kind="stable")]
    return int(order[0]), (
        float(solution.energies[order[1]] - solution.energies[order[0]])
        if len(order) > 1 else None
    )


def angle(ratio):
    if ratio is None:
        return None, "undefined_zero_quadratic"
    if not math.isfinite(ratio):
        raise ValueError("Nonfinite raw ratio.")
    if abs(ratio) > 1:
        return None, "outside_rigid_domain"
    return math.degrees(math.acos(ratio)) / 3, "within_rigid_domain"


def close(actual, expected, tolerance, name):
    error = abs(actual - expected)
    if error > tolerance["absolute"] + tolerance["relative"] * abs(expected):
        raise ValueError(f"{name}: {actual} versus {expected}; difference {error}")
    return error


def direction(left, right, metric, comparison):
    if left is None or right is None:
        return None
    tolerance = comparison["numeric_direction_rtol"] * max(abs(left), abs(right), 1e-15)
    if "angle" in metric:
        tolerance = max(tolerance, comparison["angle_direction_atol_degrees"])
    delta = right - left
    return 1 if delta > tolerance else -1 if delta < -tolerance else 0


def compare(rows, contract):
    lookup = {(r["setting"], r["odd_A"]): r for r in rows}
    policy = contract["predeclared_comparisons"]
    metrics, intervals = policy["metrics"], policy["chain_intervals"]
    settings = [s["id"] for s in contract["settings"]]
    primary = {r["odd_A"]: r for r in rows if r["setting"] == "primary"}
    trend_reversals, domain_changes, cubic_sign_changes = [], [], []
    full_selected = []
    trend_signatures = {}
    pair_metrics = [
        ("full_q2", "n5_q2_contribution"), ("full_q2", "all_q2_contribution"),
        ("full_beta", "n5_beta"), ("full_beta", "all_beta"),
        ("full_folded_angle", "n5_angle"), ("full_folded_angle", "all_angle"),
    ]
    for setting in settings:
        trend_signatures[setting] = {}
        for metric in metrics:
            signatures = []
            for a, b in intervals:
                sign_now = direction(lookup[setting, a][metric], lookup[setting, b][metric], metric, policy)
                sign_base = direction(primary[a][metric], primary[b][metric], metric, policy)
                signatures.append(sign_now)
                if setting != "primary" and sign_now in (-1, 1) and sign_base in (-1, 1) and sign_now != sign_base:
                    trend_reversals.append({
                        "setting": setting, "metric": metric, "interval": [a, b],
                        "primary_direction": sign_base, "control_direction": sign_now,
                    })
            trend_signatures[setting][metric] = signatures
        for a, b in intervals:
            for full, selected in pair_metrics:
                full_sign = direction(lookup[setting, a][full], lookup[setting, b][full], full, policy)
                selected_sign = direction(lookup[setting, a][selected], lookup[setting, b][selected], selected, policy)
                base_full = direction(primary[a][full], primary[b][full], full, policy)
                base_selected = direction(primary[a][selected], primary[b][selected], selected, policy)
                if full_sign in (-1, 1) and selected_sign in (-1, 1) and full_sign != selected_sign:
                    full_selected.append({
                        "setting": setting, "interval": [a, b],
                        "full_metric": full, "selected_metric": selected,
                        "full_direction": full_sign, "selected_direction": selected_sign,
                        "also_disagree_in_primary": base_full in (-1, 1) and base_selected in (-1, 1) and base_full != base_selected,
                    })
        for case in contract["cases"]:
            a = case["odd_A"]
            row, base = lookup[setting, a], primary[a]
            for prefix in ("full", "n5", "all"):
                field = f"{prefix}_angle_status"
                if row[field] != base[field]:
                    domain_changes.append({
                        "setting": setting, "odd_A": a, "quantity": prefix,
                        "primary_status": base[field], "control_status": row[field],
                        "primary_raw_ratio": base[f"{prefix}_ratio"],
                        "control_raw_ratio": row[f"{prefix}_ratio"],
                    })
            if row["full_signed_q3"] * base["full_signed_q3"] < 0:
                cubic_sign_changes.append({
                    "setting": setting, "odd_A": a,
                    "primary_q3": base["full_signed_q3"], "control_q3": row["full_signed_q3"],
                })
    margin_possibilities = []
    for a, b in intervals:
        for metric in metrics:
            primary_sign = direction(primary[a][metric], primary[b][metric], metric, policy)
            possible = []
            for endpoint_a in ("B_down_lower", "B_down_upper"):
                for endpoint_b in ("B_down_lower", "B_down_upper"):
                    sign_now = direction(
                        lookup[endpoint_a, a][metric], lookup[endpoint_b, b][metric], metric, policy
                    )
                    if sign_now in (-1, 1) and primary_sign in (-1, 1) and sign_now != primary_sign:
                        possible.append([endpoint_a, endpoint_b])
            if possible:
                margin_possibilities.append({
                    "interval": [a, b], "metric": metric,
                    "primary_direction": primary_sign, "reversing_endpoint_combinations": possible,
                    "boundary": "deterministic quoted-margin corner; no covariance or probability inferred",
                })
    return {
        "interval_order": intervals,
        "direction_legend": {"1": "increase", "-1": "decrease", "0": "within_declared_tolerance", "null": "undefined_angle"},
        "trend_signatures": trend_signatures,
        "trend_reversals_relative_to_primary": trend_reversals,
        "full_versus_selected_trend_disagreements": full_selected,
        "angle_domain_changes_relative_to_primary": domain_changes,
        "full_signed_q3_sign_changes": cubic_sign_changes,
        "calibration_margin_reversal_possibilities": margin_possibilities,
        "domain_survival_is_not_required_for_full_vs_selected_distinction": True,
    }


def main():
    started, clock = utc(), time.perf_counter()
    if sha(CONTRACT) != FROZEN_CONTRACT_SHA:
        raise ValueError("Frozen contract hash changed.")
    for name in ("results.json", "operator-results.csv", "run.json"):
        if (OUT / name).exists():
            raise FileExistsError(f"Output already exists: {name}")
    contract = json.loads(CONTRACT.read_text())
    for entry in contract["read_only_modules"]:
        if sha(ROOT / entry["path"]) != entry["sha256"]:
            raise ValueError(f"Module changed since contract: {entry['path']}")
    if sha(ROOT / contract["inputs"]["chain"]["path"]) != contract["inputs"]["chain"]["sha256"]:
        raise ValueError("Chain contract changed.")
    cal_path = ROOT / contract["inputs"]["calibration"]["path"]
    calibration_data = json.loads(cal_path.read_text())
    if json_sha(calibration_numeric_projection(calibration_data)) != contract["inputs"]["calibration"]["selected_numeric_projection_sha256"]:
        raise ValueError("Selected calibration numbers changed.")
    native_threads = native_blas_threads()
    print(f"Contract {FROZEN_CONTRACT_SHA}; native BLAS threads verified as one.", flush=True)
    settings = contract["settings"]
    calibration = {r["core_A"]: r for r in contract["selected_core_calibrations"]}
    expected = {r["odd_A"]: r for r in contract["primary_reference"]}
    accept = contract["numerical_acceptance"]
    options = {"rtol": accept["module_rtol"], "atol": accept["module_atol"], "angle_tolerance": 0.0}
    closure_tolerance = {
        "relative": accept["closure_relative_tolerance"], "absolute": accept["closure_absolute_tolerance"]
    }
    primary_tolerance = {
        "relative": accept["primary_reference_relative_tolerance"], "absolute": accept["primary_reference_absolute_tolerance"]
    }
    rows, cases = [], []
    validation = {"max_q2_closure_abs": 0.0, "max_q3_closure_abs": 0.0,
                  "max_primary_reference_abs_difference": 0.0, "max_calibration_abs_difference": 0.0}
    cg_beta = clebsch_gordan(15, 11, 4, 0, 11, 11)

    for case in contract["cases"]:
        case_clock = time.perf_counter()
        a = case["odd_A"]
        params = IBFMParameters(**contract["kernel_parameters_by_odd_A"][str(a)])
        kernel = IBFMKernel(params)
        solution = kernel.solve(two_M=1)
        state_index, state_gap = lowest(solution, 11)
        if state_gap is not None and state_gap <= 1e-10:
            raise ValueError("Lowest J=11/2 state has unresolved same-J degeneracy.")
        h_hash = csr_sha(kernel.hamiltonian)
        state_hash = array_sha(solution.vectors[:, state_index])
        energy_order = np.argsort(solution.energies, kind="stable")
        ordered_initial = int(np.flatnonzero(energy_order == state_index)[0])
        core = BosonCore(CoreParameters(case["n_b"], case["eps_d"], case["kappa"], case["chi"]))
        core_solution = core.solve(two_M=0)
        core0, core0_gap = lowest(core_solution, 0)
        core2, core2_gap = lowest(core_solution, 4)
        if min(x for x in (core0_gap, core2_gap) if x is not None) <= 1e-10:
            raise ValueError("Core calibration level has unresolved same-J degeneracy.")
        selected = calibration[case["core_A"]]
        radius = 1.2 * a**(1/3)
        beta_prefactor = 100 * 4 * math.pi / (3 * case["Z"] * radius**2)
        meta = {
            "odd_A": a, "core_A": case["core_A"], "parameters": contract["kernel_parameters_by_odd_A"][str(a)],
            "full_dimension": solution.basis.full_dimension, "M_half_dimension": solution.basis.dimension,
            "state_index": state_index, "state_two_J": 11, "state_energy_MeV": float(solution.energies[state_index]),
            "next_same_J_gap_MeV": state_gap, "hamiltonian_csr_sha256": h_hash, "state_vector_sha256": state_hash,
            "core_initial_index": core0, "core_final_index": core2,
            "core_calibration_energy_MeV": float(core_solution.energies[core2] - core_solution.energies[core0]),
            "solver_diagnostics": dict(solution.diagnostics),
            "core_solver_diagnostics": dict(core_solution.diagnostics),
        }
        print(f"{a}Ba: fixed H solved; full dimension {kernel.dimension}, M=1/2 dimension {solution.basis.dimension}.", flush=True)

        for setting in settings:
            tag = setting["id"]
            chi = {"primary_0.35": 0.35, "zero": 0.0, "hamiltonian_chi": case["chi"]}[setting["chi_E"]]
            eF = setting["eF_eb"]
            target_down = selected["B_down_e2b2"] + setting["B_margin_direction"] * selected["B_down_margin_e2b2"]
            target_up = 5 * target_down
            calibrated = calibrate_core_e2(core, core_solution, core0, core2,
                                           chi_prime=chi, target_B_0_to_2=target_up, sign=1)
            check_up = abs(transition_rme(core_solution, core.e2(calibrated.eB, chi), core0, core2))**2
            calibration_error = close(check_up, target_up, primary_tolerance, f"{a}:{tag}:Bup")
            validation["max_calibration_abs_difference"] = max(validation["max_calibration_abs_difference"], calibration_error)
            op = kernel.e2(calibrated.eB, eF, chi)
            direct = direct_from_spectrum(solution, op, state_index,
                                           representation_label=f"{a}Ba frozen sd-boson x h11/2 space", **options)
            raw_table = reduced_table_from_spectrum(
                solution, op, representation_label=f"{a}Ba frozen sd-boson x h11/2 space",
                rtol=accept["module_rtol"], atol=accept["module_atol"],
            )
            table = ReducedQuadrupole(
                raw_table.representation, tuple(raw_table.multiplets[i] for i in energy_order),
                raw_table.rme[np.ix_(energy_order, energy_order)],
                raw_table.complete, raw_table.unresolved,
            )
            closure = reduced_invariants(table, ordered_initial, **options)
            if not closure.complete or closure.invariants is None:
                raise ValueError(f"{a}:{tag}: incomplete reduced closure")
            eq2 = close(closure.invariants.q2, direct.q2, closure_tolerance, f"{a}:{tag}:q2")
            eq3 = close(closure.invariants.q3, direct.q3, closure_tolerance, f"{a}:{tag}:q3")
            validation["max_q2_closure_abs"] = max(validation["max_q2_closure_abs"], eq2)
            validation["max_q3_closure_abs"] = max(validation["max_q3_closure_abs"], eq3)
            full_folded, _ = angle(abs(direct.raw_ratio) if direct.raw_ratio is not None else None)
            row = {
                "odd_A": a, "core_A": case["core_A"], "setting": tag,
                "chi_E": chi, "eF_eb": eF, "eB_eb": calibrated.eB,
                "B_down_target_e2b2": target_down, "B_up_target_e2b2": target_up,
                "unit_core_Bup": calibrated.unit_B_0_to_2,
                "full_q2": direct.q2, "full_signed_q3": direct.q3,
                "full_ratio": direct.raw_ratio, "full_signed_angle": direct.rigid_equivalent_angle_deg,
                "full_folded_angle": full_folded, "full_angle_status": direct.angle_status,
                "full_beta": beta_prefactor*math.sqrt(direct.q2),
                "q2_closure_abs_difference": eq2, "q3_closure_abs_difference": eq3,
                "reciprocity_residual": closure.reciprocity_residual,
                "q2_imaginary_residual": abs(direct.q2_complex.imag),
                "q3_imaginary_residual": abs(direct.q3_complex.imag),
                "spherical_hermiticity_residual": direct.diagnostics["spherical_hermiticity_residual"],
                "state_norm_residual": direct.diagnostics["state_norm_residual"],
                "q2_by_two_J": {str(j): float(value) for j, value in closure.quadratic_by_two_J.items()},
            }
            for prefix, max_states in [("n5", 5), ("all", None)]:
                proxy = j_plus_two_proxy(table, ordered_initial, max_states=max_states, **options)
                row.update({
                    f"{prefix}_states": len(proxy.selected_labels),
                    f"{prefix}_q2_raw": proxy.quadratic_strength_sum,
                    f"{prefix}_q2_contribution": proxy.quadratic_closure_contribution,
                    f"{prefix}_fraction_full_q2": proxy.quadratic_closure_contribution/direct.q2,
                    f"{prefix}_signed_chain": proxy.cubic_chain.real,
                    f"{prefix}_q3_absolute_scaled": proxy.scaled_absolute_chain,
                    f"{prefix}_ratio": proxy.raw_proxy_ratio,
                    f"{prefix}_angle": proxy.proxy_angle_deg,
                    f"{prefix}_angle_status": proxy.angle_status,
                    f"{prefix}_beta": beta_prefactor*math.sqrt(proxy.quadratic_strength_sum/16/cg_beta**2),
                })
            row["n5_fraction_all_Jplus2_q2"] = row["n5_q2_contribution"]/row["all_q2_contribution"]
            if tag == "primary":
                ref = expected[a]
                for field, target in [
                    ("eB_eb", ref["eB"]), ("full_q2", ref["full"]["q2_e2b2"]),
                    ("full_signed_q3", ref["full"]["q3_e3b3"]),
                    ("full_ratio", ref["full"]["signed_ratio"]),
                    ("n5_ratio", ref["n5"]["raw_proxy_ratio"]),
                    ("all_ratio", ref["all"]["raw_proxy_ratio"]),
                    ("n5_q2_raw", ref["n5"]["quadratic_strength_sum_e2b2"]),
                    ("all_q2_raw", ref["all"]["quadratic_strength_sum_e2b2"]),
                ]:
                    error = close(row[field], target, primary_tolerance, f"{a}:primary:{field}")
                    validation["max_primary_reference_abs_difference"] = max(validation["max_primary_reference_abs_difference"], error)
            rows.append(row)
            print(f"{a}Ba {tag}: eB={calibrated.eB:.10g}, full ratio={direct.raw_ratio:.9g}, n5={row['n5_ratio']:.9g}, all={row['all_ratio']:.9g}; {row['n5_angle_status']}/{row['all_angle_status']}", flush=True)

        if csr_sha(kernel.hamiltonian) != h_hash or array_sha(solution.vectors[:, state_index]) != state_hash:
            raise RuntimeError("Fixed Hamiltonian or state changed across operator controls.")
        meta["unchanged_across_seven_operator_controls"] = True
        meta["elapsed_seconds"] = time.perf_counter() - case_clock
        cases.append(meta)

    if len(rows) != contract["expected_rows"]:
        raise RuntimeError("Incomplete operator grid.")
    module_after = []
    for entry in contract["read_only_modules"]:
        current = sha(ROOT/entry["path"])
        if current != entry["sha256"]:
            raise RuntimeError(f"Module changed during run: {entry['path']}")
        module_after.append({"path": entry["path"], "sha256": current, "unchanged": True})
    cal_after = json.loads(cal_path.read_text())
    if json_sha(calibration_numeric_projection(cal_after)) != contract["inputs"]["calibration"]["selected_numeric_projection_sha256"]:
        raise RuntimeError("Selected calibration numbers changed during the run.")
    comparisons = compare(rows, contract)
    payload = {
        "schema": "odd-Ba-fixed-H-operator-sensitivity-results/1",
        "contract_sha256": FROZEN_CONTRACT_SHA,
        "evidence_class": "finite-model operator sensitivity; not posterior or source-figure reproduction",
        "units": {"q2": "e^2 b^2", "q3": "e^3 b^3", "eB_eF": "e b", "angle": "degree", "beta": "dimensionless; b converted to 100 fm^2"},
        "cases": cases, "rows": rows, "validation": validation, "comparisons": comparisons,
        "interpretation": contract["interpretation"],
    }
    write_new("results.json", payload)
    columns = [k for k in rows[0] if k != "q2_by_two_J"]
    with (OUT/"operator-results.csv").open("x", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    write_new("run.json", {
        "schema": "operator-control-run/1", "status": "completed",
        "started_at_utc": started, "finished_at_utc": utc(),
        "elapsed_seconds": time.perf_counter()-clock,
        "contract_sha256": FROZEN_CONTRACT_SHA, "driver_sha256": sha(__file__),
        "rows": len(rows), "native_blas": native_threads,
        "environment": {"python": sys.version.split()[0], "numpy": np.__version__, "scipy": scipy.__version__,
                        "thread_env": contract["runtime"]["environment"]},
        "calibration_sha256_at_freeze": contract["inputs"]["calibration"]["sha256_at_freeze"],
        "calibration_sha256_at_finish": sha(cal_path),
        "selected_numeric_calibrations_unchanged": True,
        "read_only_modules": module_after, "validation": validation,
        "results_sha256": sha(OUT/"results.json"), "csv_sha256": sha(OUT/"operator-results.csv"),
        "no_full_pair_JSON": True, "no_fit_to_discrepancy": True,
        "no_get_paper_PLAN_or_other_session_work": True, "no_commit": True,
    })
    print("Completed 35 rows; fixed states, calibration replay and direct/reduced closure checks passed.", flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        failure = {"time_utc": utc(), "driver_sha256": sha(__file__),
                   "contract_sha256": sha(CONTRACT), "traceback": traceback.format_exc()}
        filename = f"failure-{time.time_ns()}.json"
        write_new(filename, failure)
        raise
