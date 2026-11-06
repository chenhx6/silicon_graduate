#!/usr/bin/env python3
"""Prospectively specified 135Ba coupling interventions; fixed core/E2 operator."""
import os
for _variable in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
                  "BLIS_NUM_THREADS", "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_variable] = "1"

from dataclasses import asdict, replace
from datetime import datetime, timezone
import csv
import hashlib
import json
import math
from pathlib import Path
import sys
import time

import numpy as np
from scipy import sparse

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "system/scripts/analysis"))
from single_j_ibfm import IBFMParameters, CoreParameters, BosonCore, IBFMKernel, calibrate_core_e2
from quadrupole_scalar_invariants import (
    direct_from_spectrum, reduced_table_from_spectrum, reduced_invariants,
    j_plus_two_proxy,
)


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def real(z):
    z = complex(z)
    if abs(z.imag) > 1e-10 * max(1, abs(z)):
        raise ValueError("Unexpected complex residual in a real diagnostic")
    return float(z.real)


def angle(ratio, folded=False):
    value = abs(ratio) if folded else ratio
    if abs(value) > 1 + 1e-12:
        return None
    return math.degrees(math.acos(max(-1., min(1., value)))) / 3


def scalar_summary(s):
    return {
        "q2_e2b2": s.q2, "q3_e3b3": s.q3, "signed_ratio": s.raw_ratio,
        "signed_angle_deg": s.rigid_equivalent_angle_deg,
        "folded_angle_deg": angle(s.raw_ratio, True) if s.raw_ratio is not None else None,
        "angle_status": s.angle_status,
    }


def proxy_summary(table, i, count):
    proxy = j_plus_two_proxy(table, i, max_states=count)
    js = table.multiplets[i].two_J
    members = [j for j, m in enumerate(table.multiplets) if m.two_J == js + 4]
    if count is not None:
        members = members[:count]
    u = table.rme[members, i]
    middle = table.rme[np.ix_(members, members)]
    terms = u[:, None].conj() * middle * u[None, :]
    diagonal = real(np.trace(terms))
    return {
        "n": count, "states_used": len(members),
        "strength_raw_e2b2": proxy.quadratic_strength_sum,
        "q2_scalar_contribution_e2b2": proxy.quadratic_closure_contribution,
        "chain_signed_e3b3": real(proxy.cubic_chain),
        "chain_middle_diagonal_e3b3": diagonal,
        "chain_middle_offdiagonal_e3b3": real(proxy.cubic_chain) - diagonal,
        "chain_sum_positive_terms_e3b3": float(np.sum(terms.real[terms.real > 0])),
        "chain_sum_negative_terms_e3b3": float(np.sum(terms.real[terms.real < 0])),
        "raw_ratio": proxy.raw_proxy_ratio,
        "angle_deg": proxy.proxy_angle_deg,
        "angle_status": proxy.angle_status,
    }


def write_csv(path, records):
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)


def main():
    started = now()
    protocol_path = OUT / "protocol.json"
    protocol = json.loads(protocol_path.read_text())
    for name, value in protocol["input_sha256"].items():
        if digest(ROOT / name) != value:
            raise RuntimeError(f"Frozen input changed before run: {name}")
    primary_file = ROOT / "outputs/l4/20261105-ba129-controlled-pairing/shape-closure-v1/study.json"
    parent = next(r for r in json.loads(primary_file.read_text())["cases"]
                  if r["case"]["odd_A"] == 135)
    p0 = IBFMParameters(**protocol["parameters_at_t1"])
    core = BosonCore(CoreParameters(**protocol["frozen_even_core"]))
    cs = core.solve()
    ci, cf = (int(cs.indices_for_J(j)[0]) for j in (0, 4))
    em = protocol["electromagnetic_operator"]
    calibration = calibrate_core_e2(core, cs, ci, cf, chi_prime=em["chi_E2"],
                                    target_B_0_to_2=em["core_target_Bup_e2b2"], sign=1)
    assert abs(calibration.eB - em["eB_parent_reference"]) < 1e-13
    core_scalar = direct_from_spectrum(cs, core.e2(calibration.eB, em["chi_E2"]), ci,
                                      representation_label="fixed 134Ba sd core N_B=5")
    # Complete boson R projectors, including all projections and radial states.
    evals, rvec = np.linalg.eigh(core.bosons.L2.toarray())
    angular = (np.sqrt(np.maximum(0, 1 + 4 * evals)) - 1) / 2
    rlabels = np.rint(angular).astype(int)
    assert np.max(abs(angular - rlabels)) < 1e-10
    core_ground = np.zeros(core.bosons.dimension, complex)
    core_ground[cs.basis.full_indices] = cs.vectors[:, ci]
    collected, cache = {}, {}

    def evaluate(label, params, kind, t=None, removed=None):
        begun = time.perf_counter()
        kernel = IBFMKernel(params)
        spectrum = kernel.solve(two_M=1)
        jindices = spectrum.indices_for_J(11)
        i = int(jindices[0])
        operator = kernel.e2(calibration.eB, em["eF_eb"], em["chi_E2"])
        direct = direct_from_spectrum(spectrum, operator, i,
                                      representation_label="135Ba complete sd^5 x h11/2 space")
        table = reduced_table_from_spectrum(
            spectrum, operator, representation_label="135Ba complete sd^5 x h11/2 space")
        closure = reduced_invariants(table, i)
        if not closure.complete:
            raise RuntimeError("Incomplete required closure")
        dq2, dq3 = closure.invariants.q2 - direct.q2, closure.invariants.q3 - direct.q3
        assert abs(dq2) < 1e-9 * max(1, direct.q2)
        assert abs(dq3) < 1e-9 * max(1, abs(direct.q3))
        proxy5, proxy_all = (proxy_summary(table, i, n) for n in (5, None))
        for proxy in (proxy5, proxy_all):
            proxy["fraction_of_full_q2"] = proxy["q2_scalar_contribution_e2b2"] / direct.q2
        static = abs(table.rme[i, i])**2 / 12
        same_j = closure.quadratic_by_two_J[11]
        q2_channels = [
            {"two_J": int(j), "q2_e2b2": float(v), "fraction": float(v / direct.q2)}
            for j, v in sorted(closure.quadratic_by_two_J.items())
        ]
        sectors = [
            {"two_Ja": int(a), "two_Jb": int(b), "q3_e3b3": real(v)}
            for (a, b), v in sorted(closure.cubic_by_two_J_pair.items())
        ]
        positive = sum(x["q3_e3b3"] for x in sectors if x["q3_e3b3"] > 0)
        negative = sum(x["q3_e3b3"] for x in sectors if x["q3_e3b3"] < 0)
        plus_sector = real(closure.cubic_by_two_J_pair[(15, 15)])
        by_touches = {0: 0., 1: 0., 2: 0.}
        diag_cubic, offdiag_cubic, state_abs_sum = 0., 0., 0.
        ilabel = table.multiplets[i].label
        for (a, b), value in closure.cubic_by_state_pair.items():
            value = real(value)
            by_touches[int(a == ilabel) + int(b == ilabel)] += value
            if a == b:
                diag_cubic += value
            else:
                offdiag_cubic += value
            state_abs_sum += abs(value)
        psi = np.zeros(kernel.dimension, complex)
        psi[spectrum.basis.full_indices] = spectrum.vectors[:, i]
        product = psi.reshape(core.bosons.dimension, p0.two_j + 1)
        coefficients = rvec.conj().T @ product
        probs = {str(r): float(np.sum(abs(coefficients[rlabels == r, :])**2))
                 for r in sorted(set(rlabels))}
        assert abs(sum(probs.values()) - 1) < 1e-10
        nd = real(np.vdot(product, core.bosons.n_d @ product))
        component_energy = {name: real(np.vdot(psi, term @ psi))
                            for name, term in kernel.components.items()}
        assert abs(sum(component_energy.values()) - spectrum.energies[i]) < 1e-9
        spectrum_diag = {k: float(v) for k, v in spectrum.diagnostics.items()
                         if isinstance(v, (int, float, np.integer, np.floating))}
        result = {
            "label": label, "control_kind": kind, "t": t, "removed_term": removed,
            "couplings": {k: getattr(params, k) for k in ("Gamma0", "Lambda0", "A0")},
            "state": {
                "two_J": 11, "same_J_ordinal": 0, "state_index": i,
                "energy_MeV": float(spectrum.energies[i]),
                "relative_to_global_lowest_MeV": float(spectrum.energies[i] - spectrum.energies[0]),
                "same_J_next_gap_MeV": float(spectrum.energies[jindices[1]] - spectrum.energies[i]),
            },
            "full_direct": scalar_summary(direct),
            "full_6j": {"q2_e2b2": closure.invariants.q2, "q3_e3b3": closure.invariants.q3},
            "closure": {"complete": closure.complete, "delta_q2": dq2, "delta_q3": dq3,
                        "reciprocity_residual": closure.reciprocity_residual,
                        "required_missing_count": len(closure.missing_entries)},
            "proxy5": proxy5, "proxy_all": proxy_all,
            "quadratic_channels": q2_channels,
            "same_J": {
                "static_diagonal_RME_eb": real(table.rme[i, i]),
                "static_q2_e2b2": float(static), "other_same_J_q2_e2b2": float(same_j - static),
                "static_fraction": float(static / direct.q2),
                "other_same_J_fraction": float((same_j - static) / direct.q2),
            },
            "signed_cubic_spin_pairs": sectors,
            "cubic": {
                "positive_spin_pair_sum_e3b3": positive, "negative_spin_pair_sum_e3b3": negative,
                "spin_pair_abs_sum_e3b3": positive - negative,
                "spin_pair_cancellation_fraction": 1 - abs(direct.q3) / (positive - negative),
                "Jplus2_Jplus2_e3b3": plus_sector, "all_other_spin_pairs_e3b3": direct.q3 - plus_sector,
                "initial_triple_e3b3": by_touches[2],
                "one_initial_intermediate_e3b3": by_touches[1],
                "no_initial_intermediate_e3b3": by_touches[0],
                "middle_diagonal_e3b3": diag_cubic, "middle_offdiagonal_e3b3": offdiag_cubic,
                "state_pair_abs_sum_e3b3": state_abs_sum,
                "state_pair_boundary": "Aggregates only; individual terms not serialized. Degenerate-subspace rotations can alter state-pair partitions; full spin-pair sums are the primary diagnostic.",
            },
            "core": {
                "P_R": probs,
                "P_ground_R0": float(np.sum(abs(core_ground.conj() @ product)**2)),
                "n_d_expectation": nd,
                "effective_n_d_coefficient_eps_plus_A0_MeV": params.eps_d + params.A0,
                "R0_boundary": "R=0 includes excited core 0+ states; P(R0) alone is not a causal argument.",
            },
            "Hamiltonian_term_expectations_MeV": component_energy,
            "spectrum_checks": spectrum_diag,
            "elapsed_seconds": time.perf_counter() - begun,
        }
        assert abs(positive + negative - direct.q3) < 1e-10
        assert abs(sum(by_touches.values()) - direct.q3) < 1e-10
        assert abs(diag_cubic + offdiag_cubic - direct.q3) < 1e-10
        collected[label] = result
        cache[label] = (spectrum.vectors[:, jindices], int(i), jindices)
        print(json.dumps({
            "label": label, "q2": direct.q2, "full_ratio": direct.raw_ratio,
            "proxy5_ratio": proxy5["raw_ratio"], "proxy_all_ratio": proxy_all["raw_ratio"],
            "P_R0": probs["0"], "gap": result["state"]["same_J_next_gap_MeV"],
            "seconds": result["elapsed_seconds"],
        }), flush=True)
        return result

    # Frozen base grid; no use of control results to choose physical parameters.
    grid_labels = []
    for t in protocol["design"]["common_scale_t"]:
        params = replace(p0, Gamma0=t * p0.Gamma0, Lambda0=t * p0.Lambda0, A0=t * p0.A0)
        label = f"common_t{t:g}"
        grid_labels.append(label)
        evaluate(label, params, "common_scale", float(t))
    baseline = collected["common_t1"]
    expected = parent["primary"]
    comparisons = {
        "q2": baseline["full_direct"]["q2_e2b2"] - expected["full"]["q2_e2b2"],
        "q3": baseline["full_direct"]["q3_e3b3"] - expected["full"]["q3_e3b3"],
        "signed_ratio": baseline["full_direct"]["signed_ratio"] - expected["full"]["signed_ratio"],
        "static_fraction": baseline["same_J"]["static_fraction"] - expected["same_spin"]["static_fraction_of_full_q2"],
        "other_same_J_fraction": baseline["same_J"]["other_same_J_fraction"] - expected["same_spin"]["other_same_spin_fraction_of_full_q2"],
    }
    parent_n5 = next(x for x in expected["restricted"] if x["max_states"] == 5)
    parent_all = next(x for x in expected["restricted"] if x["max_states"] is None)
    comparisons.update({
        "proxy5_raw_ratio": baseline["proxy5"]["raw_ratio"] - parent_n5["raw_proxy_ratio"],
        "proxy_all_raw_ratio": baseline["proxy_all"]["raw_ratio"] - parent_all["raw_proxy_ratio"],
        "q3_positive_sectors": baseline["cubic"]["positive_spin_pair_sum_e3b3"]
        - expected["cubic_cancellation"]["sum_positive_spin_pairs_e3b3"],
        "q3_negative_sectors": baseline["cubic"]["negative_spin_pair_sum_e3b3"]
        - expected["cubic_cancellation"]["sum_negative_spin_pairs_e3b3"],
    })
    assert max(abs(v) for v in comparisons.values()) < 1e-9
    for term in protocol["design"]["single_term_removals_at_t1"]:
        evaluate("remove_" + term, replace(p0, **{term: 0.}), "single_term_removal", 1., term)

    def overlap(left, right):
        lv, _, _ = cache[left]
        rv, _, _ = cache[right]
        values = abs(rv.conj().T @ lv[:, 0])**2
        return {
            "left": left, "right": right, "lowest_to_lowest_fidelity": float(values[0]),
            "left_lowest_best_match_right_same_J_ordinal": int(np.argmax(values)),
            "best_match_fidelity": float(np.max(values)),
        }

    candidates = []
    for left, right in zip(grid_labels, grid_labels[1:]):
        l, r = collected[left], collected[right]
        ov = overlap(left, right)
        change = abs(r["proxy_all"]["raw_ratio"] - l["proxy_all"]["raw_ratio"])
        conditions = {
            "argument_jump": change >= .15,
            "low_adjacent_fidelity": ov["lowest_to_lowest_fidelity"] < .85,
            "small_same_J_gap": min(l["state"]["same_J_next_gap_MeV"], r["state"]["same_J_next_gap_MeV"]) < .10,
            "domain_status_change": l["proxy_all"]["angle_status"] != r["proxy_all"]["angle_status"],
        }
        if any(conditions.values()):
            candidates.append({"left": left, "right": right, "argument_jump": change,
                               "conditions": conditions, "overlap": ov})
    refinement = {"triggered_intervals": candidates, "chosen": None, "new_t": []}
    if candidates:
        chosen = max(candidates, key=lambda c: c["argument_jump"])
        lo, hi = (collected[chosen[k]]["t"] for k in ("left", "right"))
        refinement["chosen"] = chosen
        for f in (.25, .5, .75):
            t = lo + f * (hi - lo)
            refinement["new_t"].append(t)
            params = replace(p0, Gamma0=t * p0.Gamma0, Lambda0=t * p0.Lambda0, A0=t * p0.A0)
            label = f"common_t{t:g}"
            grid_labels.append(label)
            evaluate(label, params, "common_scale_refinement", t)
    grid_labels.sort(key=lambda label: collected[label]["t"])
    adjacent = [overlap(l, r) for l, r in zip(grid_labels, grid_labels[1:])]
    for label, result in collected.items():
        result["overlap_to_t1"] = overlap("common_t1", label)
    for name, value in protocol["input_sha256"].items():
        if digest(ROOT / name) != value:
            raise RuntimeError(f"Frozen input changed during run: {name}")
    try:
        from threadpoolctl import threadpool_info
        threads = threadpool_info()
        assert all(x["num_threads"] == 1 for x in threads)
    except ImportError:
        threads = {"unavailable": True, "thread_environment": "all relevant variables set to1 before import"}
    ordered = [collected[k] for k in grid_labels] + [
        collected["remove_" + term] for term in protocol["design"]["single_term_removals_at_t1"]]
    result = {
        "schema": "135Ba-coupling-sensitivity-results-v1", "started_at_utc": started,
        "finished_at_utc": now(), "protocol_sha256": digest(protocol_path),
        "driver_sha256": digest(Path(__file__)), "input_sha256": protocol["input_sha256"],
        "primary_parameters": asdict(p0), "calibration": asdict(calibration),
        "E2_fixed": {"eF_eb": em["eF_eb"], "chi_E2": em["chi_E2"]},
        "fixed_core_full": scalar_summary(core_scalar),
        "basis": {"full_dimension": 3024, "M_half_dimension": cache["common_t1"][0].shape[0]},
        "parent_endpoint_differences": comparisons,
        "refinement": refinement, "adjacent_grid_overlaps": adjacent,
        "cases": ordered, "threadpools": threads,
        "boundary": "Causal sensitivity inside the fixed finite model. No fit, parameter uncertainty, intrinsic-shape measurement, published-figure replay or novelty claim. Raw out-of-domain proxy arguments are not clipped.",
    }
    with (OUT / "controls.json").open("x") as f:
        json.dump(result, f, indent=2, allow_nan=False)
        f.write("\n")
    summary = []
    for r in ordered:
        summary.append({
            "label": r["label"], "kind": r["control_kind"], "t": r["t"],
            "Gamma0": r["couplings"]["Gamma0"], "Lambda0": r["couplings"]["Lambda0"], "A0": r["couplings"]["A0"],
            "q2_e2b2": r["full_direct"]["q2_e2b2"], "q3_e3b3": r["full_direct"]["q3_e3b3"],
            "full_signed_ratio": r["full_direct"]["signed_ratio"],
            "full_folded_angle_deg": r["full_direct"]["folded_angle_deg"],
            "proxy5_raw_ratio": r["proxy5"]["raw_ratio"], "proxy5_angle_deg": r["proxy5"]["angle_deg"],
            "proxy_all_raw_ratio": r["proxy_all"]["raw_ratio"], "proxy_all_angle_deg": r["proxy_all"]["angle_deg"],
            "proxy_all_status": r["proxy_all"]["angle_status"],
            "q2_Jplus2_fraction": r["proxy_all"]["fraction_of_full_q2"],
            "q2_static_fraction": r["same_J"]["static_fraction"],
            "q2_other_sameJ_fraction": r["same_J"]["other_same_J_fraction"],
            "P_core_R0": r["core"]["P_R"]["0"], "P_core_R2": r["core"]["P_R"]["2"],
            "nd": r["core"]["n_d_expectation"], "sameJ_gap_MeV": r["state"]["same_J_next_gap_MeV"],
            "overlap_with_t1_lowest": r["overlap_to_t1"]["lowest_to_lowest_fidelity"],
            "q3_positive_sectors": r["cubic"]["positive_spin_pair_sum_e3b3"],
            "q3_negative_sectors": r["cubic"]["negative_spin_pair_sum_e3b3"],
            "q3_initial_triple": r["cubic"]["initial_triple_e3b3"],
            "q3_plus_plus": r["cubic"]["Jplus2_Jplus2_e3b3"],
            "q3_other_sectors": r["cubic"]["all_other_spin_pairs_e3b3"],
        })
    write_csv(OUT / "summary.csv", summary)
    write_csv(OUT / "cubic-spin-sectors.csv", [
        {"case": r["label"], **s} for r in ordered for s in r["signed_cubic_spin_pairs"]])
    print("COMPLETE", json.dumps({"cases": len(ordered), "refinement": refinement["new_t"],
                                  "endpoint_differences": comparisons}), flush=True)


if __name__ == "__main__":
    main()
