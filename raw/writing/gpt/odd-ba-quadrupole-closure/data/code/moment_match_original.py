#!/usr/bin/env python3
"""Two-stage signed-Qs matching, followed by frozen-root scalar diagnostics."""
import os

THREAD_KEYS = (
    "OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
    "BLIS_NUM_THREADS", "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS",
)
for _key in THREAD_KEYS:
    os.environ[_key] = "1"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

import argparse
import csv
from dataclasses import replace
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import sys
import time

import numpy as np
from scipy.optimize import brentq

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
sys.path.insert(0, str(ROOT / "system/scripts/analysis"))
from single_j_ibfm import (
    IBFMParameters, IBFMKernel, CoreParameters, BosonCore, transition_rme,
)
from paired_single_j_em import clebsch_gordan
from run_controls import real, scalar_summary, proxy_summary


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(name, data):
    with (OUT / name).open("x", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, allow_nan=False)
        handle.write("\n")


def write_csv(name, records):
    with (OUT / name).open("x", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)


def load_protocol():
    path = OUT / "moment-match-protocol.json"
    protocol = json.loads(path.read_text())
    for collection in ("input_sha256", "preserved_existing_output_sha256"):
        for rel, expected in protocol[collection].items():
            if sha(ROOT / rel) != expected:
                raise RuntimeError(f"Frozen input changed: {rel}")
    return protocol


def solve(gamma, protocol, two_M):
    params = replace(
        IBFMParameters(**protocol["parameters_at_primary"]), Gamma0=float(gamma)
    )
    kernel = IBFMKernel(params)
    sol = kernel.solve(two_M=two_M)
    em = protocol["electromagnetic_operator"]
    operator = kernel.e2(em["eB_parent_reference"], em["eF_eb"], em["chi_E2"])
    same = sol.indices_for_J(11)
    assert len(same) > 1
    return kernel, sol, operator, same


QS_FACTOR = math.sqrt(16 * math.pi / 5)
RME_TO_QS = QS_FACTOR * clebsch_gordan(11, 11, 4, 0, 11, 11) / math.sqrt(12)


def root_phase():
    started = now()
    protocol = load_protocol()
    rule = protocol["root_design"]
    cache, history = {}, []

    def moment(gamma):
        gamma = float(gamma)
        if gamma not in cache:
            begin = time.perf_counter()
            _, sol, op, same = solve(gamma, protocol, 11)
            i = int(same[0])
            vector = sol.vectors[:, i]
            qs = QS_FACTOR * real(np.vdot(vector, op.block(sol.basis) @ vector))
            row = {
                "evaluation": len(cache),
                "Gamma0_MeV": gamma,
                "Qs_direct_stretched_eb": qs,
                "same_J_ordinal": 0,
                "state_index_in_MJ_block": i,
                "energy_MeV": float(sol.energies[i]),
                "same_J_gap_MeV": float(sol.energies[same[1]] - sol.energies[i]),
            }
            cache[gamma] = row
            history.append(row)
            print(json.dumps({"stage": "Qs_only", **row,
                              "seconds": time.perf_counter() - begin}), flush=True)
        return cache[gamma]["Qs_direct_stretched_eb"]

    grid = rule["existing_grid_for_initial_brackets"]
    grid_values = [moment(g) for g in grid]
    assert abs(grid_values[-1] - protocol["primary_reference"]["Qs_eb"]) < 1e-10
    solutions, unavailable = [], []
    for target in protocol["targets"]:
        wanted = target["Qs_eb"]
        grid_roots = [g for g, q in zip(grid, grid_values) if q == wanted]
        brackets = [
            (a, b) for a, b, qa, qb in
            zip(grid, grid[1:], grid_values, grid_values[1:])
            if (qa - wanted) * (qb - wanted) < 0
        ]
        candidates = []
        for g in grid_roots:
            candidates.append((g, [g, g], 0, 0, []))
        for a, b in brackets:
            calls = []

            def residual(gamma):
                value = moment(gamma) - wanted
                calls.append({"Gamma0_MeV": float(gamma), "residual_eb": value})
                return value

            value, status = brentq(
                residual, a, b, xtol=rule["xtol_Gamma0_MeV"],
                rtol=rule["rtol"], maxiter=rule["maxiter"], full_output=True,
            )
            assert status.converged
            candidates.append(
                (float(value), [a, b], status.iterations, status.function_calls, calls)
            )
        if not candidates:
            unavailable.append({"target": target, "reason": "No existing-grid sign bracket"})
        for ordinal, (gamma, bracket, iterations, calls, trace) in enumerate(candidates):
            qs = moment(gamma)
            assert abs(qs - wanted) < rule["Qs_match_absolute_tolerance_eb"]
            lower = max(grid[0], gamma - 1e-8)
            upper = min(grid[-1], gamma + 1e-8)
            certificate = [
                {"Gamma0_MeV": g, "residual_eb": moment(g) - wanted}
                for g in (lower, upper)
            ]
            assert certificate[0]["residual_eb"] * certificate[1]["residual_eb"] <= 0
            solutions.append({
                "case_id": f"{target['id']}_root{ordinal}",
                "target": target,
                "root_ordinal_among_detected_brackets": ordinal,
                "Gamma0_MeV": gamma,
                "Qs_direct_stretched_eb": qs,
                "Qs_residual_eb": qs - wanted,
                "initial_bracket_MeV": bracket,
                "root_certificate": certificate,
                "iterations": int(iterations),
                "function_calls": int(calls),
                "root_function_trace": trace,
                "stretched_state": cache[gamma],
            })
    ordered = sorted(cache.values(), key=lambda row: row["Gamma0_MeV"])
    monotone = all(
        b["Qs_direct_stretched_eb"] > a["Qs_direct_stretched_eb"]
        for a, b in zip(ordered, ordered[1:])
    )
    load_protocol()
    result = {
        "schema": "135Ba-signed-moment-roots-v1",
        "started_at_utc": started, "completed_before_new_proxies_at_utc": now(),
        "protocol_sha256": sha(OUT / "moment-match-protocol.json"),
        "driver_sha256": sha(Path(__file__)),
        "algorithm": rule,
        "grid_Qs": [cache[float(g)] for g in grid],
        "solutions": solutions, "unavailable_targets": unavailable,
        "unique_Qs_evaluations": len(cache),
        "Qs_evaluation_history": history,
        "sampled_Qs_strictly_increasing": monotone,
        "minimum_sampled_same_J_gap_MeV": min(r["same_J_gap_MeV"] for r in history),
        "no_new_proxy_computed_in_this_phase": True,
        "thread_environment": {key: os.environ[key] for key in THREAD_KEYS},
        "uniqueness_boundary": rule["uniqueness_boundary"],
    }
    write_json("moment-match-roots.json", result)
    print("ROOTS_FROZEN", json.dumps([
        {"case_id": s["case_id"], "Gamma0": s["Gamma0_MeV"],
         "Qs": s["Qs_direct_stretched_eb"]} for s in solutions
    ]), flush=True)


def overlap(left_sol, right_sol):
    assert np.array_equal(left_sol.basis.full_indices, right_sol.basis.full_indices)
    left = left_sol.vectors[:, left_sol.indices_for_J(11)]
    right = right_sol.vectors[:, right_sol.indices_for_J(11)]
    forward = abs(right.conj().T @ left[:, 0]) ** 2
    backward = abs(left.conj().T @ right[:, 0]) ** 2
    return {
        "lowest_to_lowest_fidelity": float(forward[0]),
        "left_lowest_best_right_same_J_ordinal": int(np.argmax(forward)),
        "right_lowest_best_left_same_J_ordinal": int(np.argmax(backward)),
        "left_lowest_best_right_fidelity": float(np.max(forward)),
        "right_lowest_best_left_fidelity": float(np.max(backward)),
        "left_lowest_second_largest_right_fidelity": float(np.sort(forward)[-2]),
    }


def low_energies(sol, protocol):
    zero = sol.energies[sol.indices_for_J(11)[0]]
    panel = {}
    for two_j in protocol["energy_panel"]["two_J"]:
        members = sol.indices_for_J(two_j)
        for rank in protocol["energy_panel"]["same_J_ordinals"]:
            if rank < len(members):
                panel[(two_j, rank)] = float(sol.energies[members[rank]] - zero)
    global_lowest = []
    for i in range(min(8, len(sol.energies))):
        two_j = int(sol.two_J[i])
        rank = int(np.flatnonzero(sol.indices_for_J(two_j) == i)[0])
        global_lowest.append({
            "energy_order_index": i, "two_J": two_j, "same_J_ordinal": rank,
            "relative_to_lowest_11half_MeV": float(sol.energies[i] - zero),
        })
    return panel, global_lowest


def diagnostic_phase():
    from quadrupole_scalar_invariants import (
        direct_from_spectrum, reduced_table_from_spectrum, reduced_invariants,
    )

    started = now()
    protocol = load_protocol()
    roots_path = OUT / "moment-match-roots.json"
    roots = json.loads(roots_path.read_text())
    assert roots["protocol_sha256"] == sha(OUT / "moment-match-protocol.json")
    assert roots["driver_sha256"] == sha(Path(__file__))
    assert roots["completed_before_new_proxies_at_utc"] < started
    em = protocol["electromagnetic_operator"]
    core = BosonCore(CoreParameters(**protocol["frozen_even_core"]))
    cs = core.solve()
    cg = int(cs.indices_for_J(0)[0])
    ground = np.zeros(core.bosons.dimension, complex)
    ground[cs.basis.full_indices] = cs.vectors[:, cg]
    rv, rvec = np.linalg.eigh(core.bosons.L2.toarray())
    angular = (np.sqrt(np.maximum(0, 1 + 4 * rv)) - 1) / 2
    rlabels = np.rint(angular).astype(int)
    assert np.max(abs(angular - rlabels)) < 1e-10

    previous = json.loads((OUT / "gamma-path.json").read_text())
    baseline = next(
        c for c in json.loads((OUT / "controls.json").read_text())["cases"]
        if c["label"] == "common_t1"
    )
    known, replay = {}, []
    for gamma in protocol["root_design"]["existing_grid_for_initial_brackets"]:
        _, sol, op, same = solve(gamma, protocol, 1)
        known[gamma] = sol
        i = int(same[0])
        qs = RME_TO_QS * real(transition_rme(sol, op, i, i))
        old = min(previous["points"], key=lambda row: abs(row["Gamma0"] - gamma))
        qs_grid = next(x for x in roots["grid_Qs"] if x["Gamma0_MeV"] == gamma)
        gap_delta = float(sol.energies[same[1]] - sol.energies[i]) - old["same_J_gap_MeV"]
        qs_delta = qs - qs_grid["Qs_direct_stretched_eb"]
        energy_delta = float(sol.energies[i]) - qs_grid["energy_MeV"]
        assert abs(gap_delta) < 1e-10
        assert abs(qs_delta) < 1e-10
        assert abs(energy_delta) < 1e-10
        replay.append({
            "Gamma0_MeV": gamma, "Qs_RME_eb": qs,
            "Qs_RME_minus_stretched_eb": qs_delta,
            "same_J_gap_minus_existing_MeV": gap_delta,
            "Mhalf_minus_MJ_energy_MeV": energy_delta,
            "purpose": "Recover vectors/energies only; no new proxy or complete invariants on known grid",
        })
    reference_panel, reference_lowest = low_energies(known[0.6], protocol)
    energy_rows = [
        {"case_id": "primary_Gamma0.6", "target_Qs_eb": None, "Gamma0_MeV": 0.6,
         "two_J": j, "same_J_ordinal": rank,
         "relative_to_lowest_11half_MeV": energy,
         "primary_relative_energy_MeV": energy, "shift_from_primary_MeV": 0.0}
        for (j, rank), energy in reference_panel.items()
    ]
    cases, matched = [], {}
    for root in roots["solutions"]:
        gamma = root["Gamma0_MeV"]
        kernel, sol, op, same = solve(gamma, protocol, 1)
        matched[root["case_id"]] = (gamma, sol)
        i = int(same[0])
        label = "135Ba fixed-Lambda,A signed-static-moment conditional match"
        table = reduced_table_from_spectrum(sol, op, representation_label=label)
        closure = reduced_invariants(table, i)
        assert closure.complete and not closure.missing_entries
        assert table.representation.dimension == kernel.dimension
        direct = direct_from_spectrum(sol, op, i, representation_label=label)
        delta2 = closure.invariants.q2 - direct.q2
        delta3 = closure.invariants.q3 - direct.q3
        assert max(abs(delta2), abs(delta3)) < 1e-9
        rme = real(table.rme[i, i])
        qs = RME_TO_QS * rme
        qs_difference = qs - root["Qs_direct_stretched_eb"]
        assert abs(qs_difference) < 1e-10
        assert abs(qs - root["target"]["Qs_eb"]) < 1e-9
        energy_difference = float(sol.energies[i]) - root["stretched_state"]["energy_MeV"]
        assert abs(energy_difference) < 1e-10
        static = rme * rme / 12
        static_from_qs = (qs / RME_TO_QS) ** 2 / 12
        assert abs(static - static_from_qs) < 1e-12
        proxies = [proxy_summary(table, i, n) for n in (5, None)]
        for proxy in proxies:
            proxy["fraction_of_full_q2"] = proxy["q2_scalar_contribution_e2b2"] / direct.q2
        psi = np.zeros(kernel.dimension, complex)
        psi[sol.basis.full_indices] = sol.vectors[:, i]
        product = psi.reshape(core.bosons.dimension, 12)
        coefficients = rvec.conj().T @ product
        probs = {
            str(r): float(np.sum(abs(coefficients[rlabels == r]) ** 2))
            for r in sorted(set(rlabels))
        }
        assert abs(sum(probs.values()) - 1) < 1e-10
        sectors = [
            {"two_Ja": int(a), "two_Jb": int(b), "q3_e3b3": real(value)}
            for (a, b), value in sorted(closure.cubic_by_two_J_pair.items())
        ]
        positive = sum(s["q3_e3b3"] for s in sectors if s["q3_e3b3"] > 0)
        negative = sum(s["q3_e3b3"] for s in sectors if s["q3_e3b3"] < 0)
        assert abs(positive + negative - direct.q3) < 1e-10
        ilabel = table.multiplets[i].label
        touches = {0: 0.0, 1: 0.0, 2: 0.0}
        for (a, b), value in closure.cubic_by_state_pair.items():
            touches[int(a == ilabel) + int(b == ilabel)] += real(value)
        assert abs(sum(touches.values()) - direct.q3) < 1e-10
        lower = max(g for g in known if g <= gamma)
        upper = min(g for g in known if g >= gamma)
        left_overlap = overlap(known[lower], sol)
        right_overlap = overlap(sol, known[upper])
        panel, lowest = low_energies(sol, protocol)
        shifts = []
        for (j, rank), energy in panel.items():
            shift = energy - reference_panel[(j, rank)]
            shifts.append(shift)
            energy_rows.append({
                "case_id": root["case_id"], "target_Qs_eb": root["target"]["Qs_eb"],
                "Gamma0_MeV": gamma, "two_J": j, "same_J_ordinal": rank,
                "relative_to_lowest_11half_MeV": energy,
                "primary_relative_energy_MeV": reference_panel[(j, rank)],
                "shift_from_primary_MeV": shift,
            })
        same_q2 = closure.quadratic_by_two_J[11]
        result = {
            "case_id": root["case_id"], "target": root["target"],
            "Gamma0_MeV": gamma, "Lambda0": 1.0, "A0": -0.9,
            "Qs": {
                "direct_stretched_eb": root["Qs_direct_stretched_eb"],
                "from_RME_eb": qs, "RME_minus_stretched_eb": qs_difference,
                "match_residual_eb": qs - root["target"]["Qs_eb"],
                "diagonal_RME_eb": rme, "RME_to_Qs_factor": RME_TO_QS,
            },
            "state": {
                "two_J": 11, "same_J_ordinal": 0, "state_index": i,
                "energy_MeV": float(sol.energies[i]),
                "relative_to_lowest_negative_parity_MeV": float(sol.energies[i] - sol.energies[0]),
                "same_J_next_gap_MeV": float(sol.energies[same[1]] - sol.energies[i]),
                "Mhalf_minus_MJ_energy_MeV": energy_difference,
            },
            "full_direct": scalar_summary(direct),
            "full_6j": {"q2_e2b2": closure.invariants.q2, "q3_e3b3": closure.invariants.q3},
            "closure": {
                "complete": closure.complete, "required_missing_count": len(closure.missing_entries),
                "delta_q2": delta2, "delta_q3": delta3,
                "reciprocity_residual": closure.reciprocity_residual,
                "full_dimension": kernel.dimension, "Mhalf_registry_multiplets": len(table.multiplets),
            },
            "proxy5": proxies[0], "proxy_all": proxies[1],
            "same_J": {
                "static_q2_e2b2": static, "static_from_matched_Qs_e2b2": static_from_qs,
                "other_same_J_q2_e2b2": float(same_q2 - static),
                "static_fraction": float(static / direct.q2),
                "other_same_J_fraction": float((same_q2 - static) / direct.q2),
                "boundary": "Static term follows algebraically from matched Qs; not independent evidence.",
            },
            "quadratic_by_spin": [
                {"two_J": int(j), "q2_e2b2": float(value),
                 "fraction": float(value / direct.q2)}
                for j, value in sorted(closure.quadratic_by_two_J.items())
            ],
            "signed_cubic_spin_pairs": sectors,
            "cubic": {
                "positive_spin_pair_sum_e3b3": positive,
                "negative_spin_pair_sum_e3b3": negative,
                "spin_pair_cancellation_fraction": 1 - abs(direct.q3) / (positive - negative),
                "Jplus2_Jplus2_e3b3": real(closure.cubic_by_two_J_pair[(15, 15)]),
                "initial_triple_e3b3": touches[2],
                "one_initial_intermediate_e3b3": touches[1],
                "no_initial_intermediate_e3b3": touches[0],
            },
            "core": {
                "P_R": probs, "P_ground_R0": float(np.sum(abs(ground.conj() @ product) ** 2)),
                "n_d_expectation": real(np.vdot(product, core.bosons.n_d @ product)),
            },
            "adjacent_known_path": {
                "lower_Gamma0_MeV": lower, "upper_Gamma0_MeV": upper,
                "lower_to_match": left_overlap, "match_to_upper": right_overlap,
            },
            "low_negative_parity_spectrum": {
                "reference": "lowest11/2- in this Hamiltonian; not physical nuclear ground state",
                "lowest_eight": lowest,
                "fixed_panel_csv": "moment-match-energies.csv",
                "max_absolute_shift_from_primary_MeV": max(abs(x) for x in shifts),
                "minimum_shift_MeV": min(shifts), "maximum_shift_MeV": max(shifts),
            },
        }
        cases.append(result)
        print(json.dumps({
            "stage": "frozen_root_diagnostics", "case_id": result["case_id"],
            "Gamma0": gamma, "Qs": qs, "full_ratio": direct.raw_ratio,
            "proxy5": proxies[0]["raw_ratio"], "proxy_all": proxies[1]["raw_ratio"],
            "full_folded_angle": result["full_direct"]["folded_angle_deg"],
            "proxy_all_angle": proxies[1]["angle_deg"],
            "same_J_gap": result["state"]["same_J_next_gap_MeV"],
        }), flush=True)
    combined = [
        (g, f"known_Gamma{g:g}", sol) for g, sol in known.items()
    ] + [(g, label, sol) for label, (g, sol) in matched.items()]
    combined.sort(key=lambda item: item[0])
    adjacent = [
        {"left": a[1], "right": b[1], "left_Gamma0": a[0], "right_Gamma0": b[0],
         **overlap(a[2], b[2])} for a, b in zip(combined, combined[1:])
    ]
    load_protocol()
    result = {
        "schema": "135Ba-conditional-static-moment-diagnostics-v1",
        "started_after_roots_frozen_at_utc": started, "finished_at_utc": now(),
        "protocol_sha256": sha(OUT / "moment-match-protocol.json"),
        "roots_sha256": sha(roots_path), "driver_sha256": sha(Path(__file__)),
        "fixed_E2": em, "fixed_core": protocol["frozen_even_core"],
        "source": protocol["adopted_source"],
        "primary_reference": {
            **protocol["primary_reference"],
            "full_direct": baseline["full_direct"],
            "proxy5": baseline["proxy5"], "proxy_all": baseline["proxy_all"],
            "same_J": baseline["same_J"], "lowest_eight": reference_lowest,
            "source": "Existing common_t1 scalars reused; only Qs/energies/vectors replayed",
        },
        "known_grid_replay": replay, "cases": cases,
        "combined_known_and_matched_adjacent_overlaps": adjacent,
        "thread_environment": {key: os.environ[key] for key in THREAD_KEYS},
        "threadpool_runtime_independent_query": "unavailable; no package installation",
        "boundaries": protocol["decision_boundaries"],
    }
    write_json("moment-match-results.json", result)
    write_csv("moment-match-energies.csv", energy_rows)
    summary = []
    for c in cases:
        summary.append({
            "case_id": c["case_id"], "target_Qs_eb": c["target"]["Qs_eb"],
            "Gamma0_MeV": c["Gamma0_MeV"], "Qs_RME_eb": c["Qs"]["from_RME_eb"],
            "q2_e2b2": c["full_direct"]["q2_e2b2"], "q3_e3b3": c["full_direct"]["q3_e3b3"],
            "full_signed_ratio": c["full_direct"]["signed_ratio"],
            "full_folded_angle_deg": c["full_direct"]["folded_angle_deg"],
            "proxy5_raw_ratio": c["proxy5"]["raw_ratio"],
            "proxy5_angle_deg": c["proxy5"]["angle_deg"],
            "proxy_all_raw_ratio": c["proxy_all"]["raw_ratio"],
            "proxy_all_angle_deg": c["proxy_all"]["angle_deg"],
            "proxy_all_status": c["proxy_all"]["angle_status"],
            "folded_full_minus_proxy_all_deg":
                c["full_direct"]["folded_angle_deg"] - c["proxy_all"]["angle_deg"]
                if c["proxy_all"]["angle_deg"] is not None else None,
            "static_q2_fraction": c["same_J"]["static_fraction"],
            "other_sameJ_q2_fraction": c["same_J"]["other_same_J_fraction"],
            "Jplus2_q2_fraction": c["proxy_all"]["fraction_of_full_q2"],
            "P_core_R0": c["core"]["P_R"]["0"], "P_core_R2": c["core"]["P_R"]["2"],
            "nd": c["core"]["n_d_expectation"],
            "sameJ_gap_MeV": c["state"]["same_J_next_gap_MeV"],
            "fidelity_to_lower_known": c["adjacent_known_path"]["lower_to_match"]["lowest_to_lowest_fidelity"],
            "fidelity_to_upper_known": c["adjacent_known_path"]["match_to_upper"]["lowest_to_lowest_fidelity"],
            "q3_positive": c["cubic"]["positive_spin_pair_sum_e3b3"],
            "q3_negative": c["cubic"]["negative_spin_pair_sum_e3b3"],
            "max_panel_energy_shift_MeV":
                c["low_negative_parity_spectrum"]["max_absolute_shift_from_primary_MeV"],
        })
    write_csv("moment-match-summary.csv", summary)
    print("DIAGNOSTICS_COMPLETE", len(cases), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase", choices=("roots", "diagnostics"))
    args = parser.parse_args()
    if args.phase == "roots":
        root_phase()
    else:
        diagnostic_phase()
