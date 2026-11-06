"""Resolve only failed uniform-grid intervals; preserve the first run verbatim.

This bounded supplement uses the same assignment, embeddings and tolerances.
It writes consolidated results beside the original uniform-grid audit. No fit.
"""
import sys
sys.dont_write_bytecode = True

import copy
import csv
import io
import json
import time

import run_continuation as r

np = r.np
OUT = r.OUT
ADAPTIVE = {
    "trigger": "only spins unresolved by the declared 33/129/513/2049 uniform grids",
    "maximum_iterations": 18,
    "maximum_nodes_per_spin": 16385,
    "minimum_allowed_interval": 2.0 ** -32,
    "refinement_rule": (
        "bisect intervals failing the same gap bound, overlap, projector, "
        "assignment margin or fixed-rank tests; if none fail but refinement "
        "comparison does, bisect every interval for an independent nested check"
    ),
    "acceptance": "unchanged tolerances, plus reverse and reference-shift controls",
}


def compare(coarse, fine):
    """Compare arbitrary nested grids; the endpoints may follow other branches."""
    ci = np.searchsorted(fine["nodes"], coarse["nodes"])
    if np.any(ci >= len(fine["nodes"])) or not np.array_equal(
        fine["nodes"][ci], coarse["nodes"]
    ):
        raise ValueError("non-nested path comparison")
    cv, fv = coarse["vectors"], fine["vectors"][ci]
    fidelity = np.clip(abs(np.einsum("tij,tij->tj", cv.conj(), fv)) ** 2, 0, 1)
    projectors = [
        float(np.clip(np.linalg.svd(x.conj().T @ y, compute_uv=False).min() ** 2, 0, 1))
        for x, y in zip(cv, fv)
    ]
    a, b = coarse["arrays"], fine["arrays"]
    energy = float(np.max(abs(a["energy"] - b["energy"][ci])))
    weight = float(np.max(abs(a["weight"] - b["weight"][ci])))
    gap0 = coarse["summary"]["minimum_sampled_selected_complement_gap_MeV"]
    gap1 = fine["summary"]["minimum_sampled_selected_complement_gap_MeV"]
    gap_tolerance = max(
        r.POLICY["minimum_gap_absolute_refinement_tolerance_MeV"],
        r.POLICY["minimum_gap_relative_refinement_tolerance"] * abs(gap1),
    )
    gap_stable = abs(gap0 - gap1) <= gap_tolerance
    indices = bool(np.array_equal(a["indices"], b["indices"][ci]))
    passed = (
        indices and energy <= r.POLICY["energy_refinement_tolerance_MeV"]
        and weight <= r.POLICY["weight_refinement_tolerance"]
        and float(fidelity.min()) >= 1 - r.POLICY["fidelity_refinement_tolerance"]
        and min(projectors) >= 1 - r.POLICY["fidelity_refinement_tolerance"]
        and gap_stable
    )
    return {
        "coarse_nodes": len(coarse["nodes"]), "fine_nodes": len(fine["nodes"]),
        "same_labels_at_common_nodes": indices,
        "max_energy_change_MeV": energy, "max_plus_weight_change": weight,
        "minimum_individual_fidelity_at_common_nodes": float(fidelity.min()),
        "minimum_projector_fidelity_at_common_nodes": min(projectors),
        "sampled_minimum_gap_change_MeV": gap1 - gap0,
        "sampled_minimum_gap_stable": gap_stable, "pass": bool(passed),
    }


def failing_intervals(path):
    a = path["arrays"]
    dt = np.diff(path["nodes"])
    gaps = a["gap_all"].min(axis=1)
    bound = (np.minimum(gaps[:-1], gaps[1:])
             - path["summary"]["K_norm_MeV"] * dt
             - 2 * r.POLICY["eigen_residual_tolerance_MeV"])
    bad = bound <= r.POLICY["energy_degeneracy_tolerance_MeV"]
    bad |= a["overlap"][1:].min(axis=1) < r.POLICY["minimum_step_overlap_squared"]
    bad |= a["projector_min_singular_squared"][1:] < (
        r.POLICY["minimum_step_projector_singular_value_squared"])
    bad |= a["assignment_margin"][1:] <= r.POLICY["assignment_score_tie_tolerance"]
    bad |= np.any(a["indices"][1:] != a["indices"][:-1], axis=1)
    return np.flatnonzero(bad)


def parameters(case):
    p = case["parameters"]
    return r.PairedRotorParameters(
        p["two_j"], p["C_MeV"], p["gamma_deg"], tuple(p["inertias_hbar2_per_MeV"]),
        p["lambda_F_MeV"], p["Delta_MeV"],
    )


def refine_spin(case, original_spin):
    two_I = original_spin["two_I"]
    ordinals = original_spin["ordinals"]
    system = r.nambu.build_nambu(two_I, parameters(case))
    seeds, seed_error = r.seed_vectors(system, ordinals)
    nodes = np.linspace(0, 1, original_spin["final_grid_nodes"])
    previous = None
    history = []
    converged = False
    stop_reason = "iteration-cap"
    for iteration in range(ADAPTIVE["maximum_iterations"]):
        latest = r.track(system, ordinals, nodes, seeds)
        comparison = compare(previous, latest) if previous is not None else None
        bad = failing_intervals(latest)
        history.append({
            "iteration": iteration, "nodes": len(nodes),
            "minimum_dt": float(np.diff(nodes).min()),
            "number_of_failing_intervals": len(bad),
            "diagnostics": latest["summary"],
            "comparison_to_previous": comparison,
        })
        r.write_json(
            OUT / case["case_id"] / f"I{two_I}-adaptive-{iteration:02d}.json",
            {"case_id": case["case_id"], "two_I": two_I, "ordinals": ordinals,
             **r.serial_path(latest)},
        )
        d = latest["summary"]
        print(
            f"{case['case_id']} I={two_I}/2 adaptive={iteration} nodes={len(nodes)} "
            f"bad_intervals={len(bad)} overlap={d['minimum_selected_step_overlap_squared']:.9f} "
            f"gap={1000*d['minimum_sampled_selected_complement_gap_MeV']:.9f}keV "
            f"bound={1000*d['minimum_interval_selected_complement_gap_bound_MeV']:.9f}keV "
            f"issues={len(d['issues'])}", flush=True,
        )
        if comparison and comparison["pass"] and d["local_tracking_checks_pass"]:
            converged = True
            stop_reason = "declared-local-and-refinement-checks-passed"
            break
        if not len(bad):
            bad = np.arange(len(nodes) - 1)
        if len(nodes) + len(bad) > ADAPTIVE["maximum_nodes_per_spin"]:
            stop_reason = "node-cap"
            break
        if np.min(np.diff(nodes)[bad]) <= ADAPTIVE["minimum_allowed_interval"]:
            stop_reason = "minimum-interval-cap-or-degeneracy"
            break
        previous = latest
        nodes = np.sort(np.concatenate((nodes, (nodes[bad] + nodes[bad + 1]) / 2)))
    reverse = r.track(system, ordinals, latest["nodes"][::-1], latest["vectors"][-1])
    reversed_path = {
        "nodes": reverse["nodes"][::-1],
        "arrays": {k: v[::-1] for k, v in reverse["arrays"].items()},
        "vectors": reverse["vectors"][::-1], "summary": reverse["summary"],
    }
    reverse_comparison = compare(latest, reversed_path)
    seed_fidelity = np.clip(abs(np.einsum(
        "ij,ij->j", seeds.conj(), reverse["vectors"][-1])) ** 2, 0, 1)
    reverse_check = {
        "comparison": reverse_comparison,
        "return_seed_fidelities": seed_fidelity.tolist(),
        "diagnostics": reverse["summary"],
        "pass": bool(reverse_comparison["pass"]
                     and seed_fidelity.min() >= 1 - r.POLICY["fidelity_refinement_tolerance"]
                     and reverse["summary"]["local_tracking_checks_pass"]),
    }
    r.write_json(OUT / case["case_id"] / f"I{two_I}-adaptive-reverse.json",
                 {**r.serial_path(reverse), "check": reverse_check})
    shifted = r.track(
        system, ordinals, latest["nodes"], seeds,
        shift=r.POLICY["reference_shift_control_MeV"],
    )
    shift_comparison = compare(latest, shifted)
    shift_check = {
        "common_shift_MeV": r.POLICY["reference_shift_control_MeV"],
        "comparison": shift_comparison,
        "pass": bool(shift_comparison["pass"]
                     and shifted["summary"]["local_tracking_checks_pass"]),
    }
    a = latest["arrays"]
    original_vectors = system.embedding @ latest["vectors"][-1]
    original_residual = np.linalg.norm(
        system.endpoint_product_MeV @ original_vectors
        - original_vectors * a["energy"][-1], axis=0,
    )
    accepted = (converged and reverse_check["pass"] and shift_check["pass"]
                and original_spin["zero_coupling_check"]["pass"]
                and original_residual.max() < r.POLICY["eigen_residual_tolerance_MeV"])
    result = copy.deepcopy(original_spin)
    result.update({
        "uniform_grid_status": original_spin["status"],
        "initial_embedding_error": seed_error,
        "adaptive_refinement_history": history, "adaptive_stop_reason": stop_reason,
        "final_grid_nodes": len(latest["nodes"]), "final_grid_kind": "locally-refined",
        "minimum_dt": float(np.diff(latest["nodes"]).min()),
        "forward_diagnostics": latest["summary"],
        "reverse_check": reverse_check, "reference_shift_check": shift_check,
        "endpoint_original_product_residuals_MeV": original_residual.tolist(),
        "status": ("converged-mathematical-continuation" if accepted else
                   "unresolved-continuation-candidates-not-certified"),
    })
    r.write_json(OUT / case["case_id"] / f"I{two_I}-adaptive-final.json",
                 {**r.serial_path(latest), "check": result})
    np.savez_compressed(
        OUT / case["case_id"] / f"I{two_I}-adaptive-selected-endpoints.npz",
        seeds_BCS_coordinates=seeds, endpoint_BCS_coordinates=latest["vectors"][-1],
        endpoint_original_product_coordinates=original_vectors,
    )
    for row in case["state_results"]:
        if row["twice_I"] != two_I:
            continue
        column = ordinals.index(row["model_ordinal_assumed"])
        row.update({
            "status": result["status"], "final_grid_nodes": len(latest["nodes"]),
            "t1_energy_MeV": float(a["energy"][-1, column]),
            "absolute_shift_keV": float(
                1000 * (a["energy"][-1, column] - row["t0_energy_MeV"])),
            "t0_full_index": int(a["indices"][0, column]),
            "t1_full_index": int(a["indices"][-1, column]),
            "t1_BCS_plus_weight": float(a["weight"][-1, column]),
            "minimum_BCS_plus_weight_along_path": float(a["weight"][:, column].min()),
            "minimum_step_overlap_squared": float(a["overlap"][:, column].min()),
            "minimum_selected_complement_gap_keV": float(
                1000 * a["gap_complement"][:, column].min()),
            "minimum_all_other_gap_keV": float(1000 * a["gap_all"][:, column].min()),
        })
    return result


def low_spin_control(case):
    """I=1/2 is a control only, not an extra mapped/physical level."""
    system = r.nambu.build_nambu(1, parameters(case))
    d = system.sector_dimension
    gap = float(np.linalg.eigvalsh(system.Hplus_MeV)[0]
                - np.linalg.eigvalsh(system.Hminus_MeV)[-1])
    if gap <= r.POLICY["energy_degeneracy_tolerance_MeV"]:
        return {"two_I": 1, "ordered_block_gap_MeV": gap, "applicable": False}
    ordinals = list(range(d))
    seeds, _ = r.seed_vectors(system, ordinals)
    # Test the complete plus projector; do not label its internal high states.
    previous = seeds
    projector_steps = []
    cross_gaps = []
    initial_projector_fidelity = None
    for t in np.linspace(0, 1, 129):
        e, v = np.linalg.eigh(r.nambu.hamiltonian_at(system, float(t)))
        columns, _ = r.assignment(abs(previous.conj().T @ v) ** 2)
        selected = v[:, columns]
        if set(columns) != set(range(d, 2 * d)):
            raise RuntimeError("ordered low-spin upper-d projector disagrees")
        fidelity = float(np.clip(
            np.linalg.svd(previous.conj().T @ selected, compute_uv=False).min() ** 2, 0, 1))
        if initial_projector_fidelity is None:
            initial_projector_fidelity = fidelity
        projector_steps.append(fidelity)
        cross_gaps.append(float(e[d] - e[d - 1]))
        previous = selected
    return {
        "two_I": 1, "purpose": "ordered-gap low-spin subspace control only",
        "applicable": True, "ordered_block_gap_MeV": gap,
        "upper_d_set_agrees_at_all_129_nodes": True,
        "initial_full_plus_projector_fidelity": initial_projector_fidelity,
        "minimum_upper_d_projector_step_fidelity": min(projector_steps),
        "minimum_upper_lower_spectral_gap_MeV": min(cross_gaps),
    }


def main():
    started = time.time()
    baseline_path = OUT / "results.json"
    baseline = json.loads(baseline_path.read_text())
    if r.sha(OUT / "run_continuation.py") != baseline["runner_sha256"]:
        raise RuntimeError("uniform runner changed")
    hashes = baseline["input_sha256"]
    if any(r.sha(r.ROOT / p) != digest for p, digest in hashes.items()):
        raise RuntimeError("a frozen input changed since the uniform run")
    result = copy.deepcopy(baseline)
    result["uniform_results_sha256"] = r.sha(baseline_path)
    result["adaptive_policy"] = ADAPTIVE
    r.write_json(OUT / "adaptive-contract.json", ADAPTIVE)
    for case in result["cases"]:
        case["low_spin_ordered_gap_control"] = low_spin_control(case)
        for index, spin in enumerate(case["spin_results"]):
            if spin["status"] != "converged-mathematical-continuation":
                case["spin_results"][index] = refine_spin(case, spin)
        anchor = next(row for row in case["state_results"]
                      if row["level_id"] == case["energy_reference_level"])
        for row in case["state_results"]:
            row["t0_relative_energy_keV"] = 1000 * (row["t0_energy_MeV"] - anchor["t0_energy_MeV"])
            row["t1_relative_energy_keV"] = 1000 * (row["t1_energy_MeV"] - anchor["t1_energy_MeV"])
            row["relative_shift_vs_mapped_anchor_keV"] = (
                row["t1_relative_energy_keV"] - row["t0_relative_energy_keV"])
            row["t1_Ex_at_fixed_anchor_keV"] = anchor["energy_keV"] + row["t1_relative_energy_keV"]
            row["relative_shift_status"] = (
                "converged-mathematical-reference"
                if row["status"] == anchor["status"] == "converged-mathematical-continuation"
                else "tentative-because-state-or-anchor-unresolved")
        case["all_ten_states_converged"] = all(
            row["status"] == "converged-mathematical-continuation"
            for row in case["state_results"])
        r.write_json(OUT / case["case_id"] / "refined-result.json", case)
    changed = [p for p, digest in hashes.items() if r.sha(r.ROOT / p) != digest]
    result["inputs_changed_during_adaptive_run"] = changed
    result["adaptive_runner_sha256"] = r.sha(__file__)
    result["adaptive_elapsed_seconds"] = time.time() - started
    result["all_cases_converged_under_declared_checks"] = bool(
        not changed and all(c["all_ten_states_converged"] for c in result["cases"]))
    r.write_json(OUT / "refined-results.json", result)
    fields = next(csv.reader(io.StringIO((OUT / "state-results.csv").read_text())))
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, extrasaction="ignore")
    writer.writeheader()
    for case in result["cases"]:
        writer.writerows(case["state_results"])
    (OUT / "refined-state-results.csv").write_text(buffer.getvalue())
    print(
        f"COMPLETE adaptive: all_cases_converged="
        f"{result['all_cases_converged_under_declared_checks']} "
        f"elapsed={time.time()-started:.2f}s changed_inputs={changed}", flush=True)


if __name__ == "__main__":
    main()
