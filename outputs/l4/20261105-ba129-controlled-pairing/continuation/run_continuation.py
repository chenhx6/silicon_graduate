"""Bounded fixed-parameter continuation of ten predeclared Hplus labels.

Writes only beside this runner. Uses the supplied Nambu module without
modifying it. No fit, physical-state certification, EM or transfer forecast.
"""
import sys
sys.dont_write_bytecode = True

import csv
import hashlib
import io
import json
import os
import platform
import time
from dataclasses import asdict
from pathlib import Path

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
import numpy as np
import scipy
from scipy.optimize import linear_sum_assignment

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
sys.path.insert(0, str(ROOT / "system/scripts/analysis"))
import paired_single_j_nambu as nambu
from paired_single_j_rotor import PairedRotorParameters

PRIOR = "outputs/l4/20261105-ba129-model-readiness/"
SPECS = [
    ("C60_best", PRIOR + "model-fit-C60/energy-calibration.json", "best"),
    ("C120_start0", PRIOR + "model-fit-free-inertias-C120/energy-calibration.json", 0),
    ("C120_start1", PRIOR + "model-fit-free-inertias-C120/energy-calibration.json", 1),
]
POLICY = {
    "interpretation": "mathematical Hplus-connected references; not certified physical states",
    "parameter_changes_or_refitting": False,
    "seed_rule": "original-product Xplus times the predeclared Hplus eigenvector, then Xdagger",
    "assignment": "rectangular maximum sum of squared overlaps, one selected label per column",
    "tracked_objects": "only the one/two mapped states at each spin, not arbitrarily labelled high states",
    "grids": [33, 129, 513, 2049],
    "minimum_grids": 2,
    "minimum_step_overlap_squared": 0.995,
    "minimum_step_projector_singular_value_squared": 0.995,
    "assignment_score_tie_tolerance": 1e-8,
    "energy_degeneracy_tolerance_MeV": 1e-9,
    "energy_refinement_tolerance_MeV": 1e-8,
    "weight_refinement_tolerance": 1e-8,
    "fidelity_refinement_tolerance": 1e-8,
    "minimum_gap_relative_refinement_tolerance": 0.02,
    "minimum_gap_absolute_refinement_tolerance_MeV": 1e-5,
    "eigen_residual_tolerance_MeV": 1e-10,
    "gap_interval_bound": (
        "min(endpoint selected gap)-norm(K)*dt-2*residual_tolerance; "
        "valid for fixed energy-rank labels and the linear Hermitian path"
    ),
    "reference_shift_control_MeV": 100.0,
    "zero_coupling_control": "evaluate hamiltonian_at(system,0) along a five-point dummy path",
    "failure_policy": (
        "Refine on rank jumps, small overlaps, ties, unbounded intervening gaps, "
        "or unconverged common-grid diagnostics. At cap retain unresolved status "
        "and tentative candidates; do not call them unique continued labels."
    ),
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")


def assignment(overlap):
    """One-to-one row assignment and gap to the best different assignment."""
    rows, columns = linear_sum_assignment(overlap, maximize=True)
    if not np.array_equal(rows, np.arange(overlap.shape[0])):
        raise RuntimeError("not every selected label was assigned")
    best = float(overlap[rows, columns].sum())
    second = -np.inf
    for row, column in zip(rows, columns):
        alternative = overlap.copy()
        alternative[row, column] = -1e6
        rr, cc = linear_sum_assignment(alternative, maximize=True)
        second = max(second, float(alternative[rr, cc].sum()))
    return columns, best - second


def seed_vectors(system, ordinals):
    reference = system.reference_plus
    original = system.positive_embedding @ reference.eigenvectors[:, ordinals]
    seed = system.embedding.conj().T @ original
    error = max(
        float(np.max(abs(system.embedding @ seed - original))),
        float(np.max(abs(seed[system.sector_dimension:]))),
        float(np.max(abs(seed.conj().T @ seed - np.eye(len(ordinals))))),
    )
    if error > 1e-10:
        raise RuntimeError("actual embedding did not reproduce the intended plus seeds")
    return seed, error


def track(system, ordinals, nodes, initial, shift=0.0, coupling_scale=1.0):
    """Track only mapped labels. Complement states need no individual labels."""
    previous = initial
    size, count = initial.shape
    d = system.sector_dimension
    k_norm = float(np.linalg.norm(system.K_MeV, 2)) * coupling_scale
    ordered_gap = float(
        np.linalg.eigvalsh(system.Hplus_MeV)[0]
        - np.linalg.eigvalsh(system.Hminus_MeV)[-1]
    )
    arrays = {key: [] for key in (
        "energy", "indices", "weight", "overlap", "gap_complement", "gap_all",
        "projector_min_singular_squared", "assignment_margin", "residual",
    )}
    vectors = []
    issues = []
    ordered_matches = []
    for step, t in enumerate(nodes):
        h = nambu.hamiltonian_at(system, float(t) * coupling_scale)
        if shift:
            h = h + shift * np.eye(size)
        energies, eigenvectors = np.linalg.eigh(h)
        overlaps = np.clip(abs(previous.conj().T @ eigenvectors) ** 2, 0.0, 1.0)
        columns, margin = assignment(overlaps)
        selected = eigenvectors[:, columns]
        chosen = overlaps[np.arange(count), columns]
        singular = np.linalg.svd(previous.conj().T @ selected, compute_uv=False)
        projector_overlap = float(np.clip(singular.min() ** 2, 0.0, 1.0))
        # Rephase for a continuous representation, without changing projectors.
        phase = np.einsum("ij,ij->j", previous.conj(), selected)
        selected = selected * np.exp(-1j * np.angle(phase))[None, :]
        selected_energy = energies[columns]
        complement = np.ones(size, bool)
        complement[columns] = False
        gap_complement = np.min(
            abs(selected_energy[:, None] - energies[None, complement]), axis=1
        )
        distances = abs(selected_energy[:, None] - energies[None, :])
        distances[np.arange(count), columns] = np.inf
        gap_all = distances.min(axis=1)
        residual = np.linalg.norm(h @ selected - selected * selected_energy, axis=0)
        weight = np.sum(abs(selected[:d]) ** 2, axis=0)
        if margin <= POLICY["assignment_score_tie_tolerance"]:
            issues.append({"kind": "assignment_tie", "step": step, "t": float(t),
                           "margin": margin})
        if float(gap_complement.min()) <= POLICY["energy_degeneracy_tolerance_MeV"]:
            issues.append({"kind": "selected_complement_degeneracy", "step": step,
                           "t": float(t)})
        elif float(gap_all.min()) <= POLICY["energy_degeneracy_tolerance_MeV"]:
            issues.append({"kind": "internal_selected_degeneracy_individual_labels_unresolved",
                           "step": step, "t": float(t)})
        if float(residual.max()) > POLICY["eigen_residual_tolerance_MeV"]:
            issues.append({"kind": "selected_eigen_residual", "step": step, "t": float(t)})
        if step and not np.array_equal(columns, arrays["indices"][-1]):
            issues.append({
                "kind": "energy_rank_jump_or_crossing_requires_resolution",
                "step": step, "t": float(t),
                "from": arrays["indices"][-1].tolist(), "to": columns.tolist(),
            })
        if ordered_gap > POLICY["energy_degeneracy_tolerance_MeV"]:
            ordered_matches.append(bool(np.array_equal(columns, d + np.array(ordinals))))
        for key, value in (
            ("energy", selected_energy - shift), ("indices", columns),
            ("weight", weight), ("overlap", chosen),
            ("gap_complement", gap_complement), ("gap_all", gap_all),
            ("projector_min_singular_squared", projector_overlap),
            ("assignment_margin", margin), ("residual", residual),
        ):
            arrays[key].append(value)
        vectors.append(selected)
        previous = selected
    arrays = {key: np.asarray(value) for key, value in arrays.items()}
    gaps = arrays["gap_complement"].min(axis=1)
    gaps_all = arrays["gap_all"].min(axis=1)
    dt = np.abs(np.diff(nodes))
    safety = 2 * POLICY["eigen_residual_tolerance_MeV"]
    bound = np.minimum(gaps[:-1], gaps[1:]) - k_norm * dt - safety
    individual_bound = np.minimum(gaps_all[:-1], gaps_all[1:]) - k_norm * dt - safety
    rank_stable = bool(np.all(arrays["indices"] == arrays["indices"][0]))
    summary = {
        "minimum_selected_step_overlap_squared": float(arrays["overlap"].min()),
        "minimum_selected_projector_step_singular_squared": float(
            arrays["projector_min_singular_squared"].min()),
        "minimum_assignment_margin": float(arrays["assignment_margin"].min()),
        "minimum_sampled_selected_complement_gap_MeV": float(gaps.min()),
        "minimum_sampled_selected_all_other_gap_MeV": float(gaps_all.min()),
        "minimum_interval_selected_complement_gap_bound_MeV": float(bound.min()),
        "minimum_interval_individual_gap_bound_MeV": float(individual_bound.min()),
        "gap_bounds_applicable_to_fixed_rank_labels": rank_stable,
        "energy_rank_labels_stable": rank_stable,
        "ordered_block_gap_at_t0_MeV": ordered_gap,
        "ordered_upper_d_check_applicable": bool(ordered_matches),
        "ordered_upper_d_agrees": all(ordered_matches) if ordered_matches else None,
        "maximum_selected_residual_MeV": float(arrays["residual"].max()),
        "K_norm_MeV": k_norm,
        "issues": issues,
    }
    local_ok = (
        not issues and rank_stable
        and summary["minimum_selected_step_overlap_squared"]
            >= POLICY["minimum_step_overlap_squared"]
        and summary["minimum_selected_projector_step_singular_squared"]
            >= POLICY["minimum_step_projector_singular_value_squared"]
        and bound.min() > POLICY["energy_degeneracy_tolerance_MeV"]
        and individual_bound.min() > POLICY["energy_degeneracy_tolerance_MeV"]
        and (not ordered_matches or all(ordered_matches))
    )
    summary["local_tracking_checks_pass"] = bool(local_ok)
    return {"nodes": np.asarray(nodes), "arrays": arrays, "vectors": np.asarray(vectors),
            "summary": summary}


def compare_paths(coarse, fine):
    ratio = (len(fine["nodes"]) - 1) // (len(coarse["nodes"]) - 1)
    if ratio * (len(coarse["nodes"]) - 1) + 1 != len(fine["nodes"]):
        raise ValueError("comparison requires nested uniform grids")
    fv = fine["vectors"][::ratio]
    cv = coarse["vectors"]
    fidelity = np.clip(abs(np.einsum("tij,tij->tj", cv.conj(), fv)) ** 2, 0, 1)
    projectors = [
        float(np.clip(np.linalg.svd(x.conj().T @ y, compute_uv=False).min() ** 2, 0, 1))
        for x, y in zip(cv, fv)
    ]
    a, b = coarse["arrays"], fine["arrays"]
    energy = float(np.max(abs(a["energy"] - b["energy"][::ratio])))
    weight = float(np.max(abs(a["weight"] - b["weight"][::ratio])))
    gap0 = coarse["summary"]["minimum_sampled_selected_complement_gap_MeV"]
    gap1 = fine["summary"]["minimum_sampled_selected_complement_gap_MeV"]
    gap_tolerance = max(
        POLICY["minimum_gap_absolute_refinement_tolerance_MeV"],
        POLICY["minimum_gap_relative_refinement_tolerance"] * abs(gap1),
    )
    gap_stable = abs(gap0 - gap1) <= gap_tolerance
    indices = bool(np.array_equal(a["indices"], b["indices"][::ratio]))
    passed = (
        indices and energy <= POLICY["energy_refinement_tolerance_MeV"]
        and weight <= POLICY["weight_refinement_tolerance"]
        and float(fidelity.min()) >= 1 - POLICY["fidelity_refinement_tolerance"]
        and min(projectors) >= 1 - POLICY["fidelity_refinement_tolerance"]
        and gap_stable
    )
    return {
        "coarse_nodes": len(coarse["nodes"]), "fine_nodes": len(fine["nodes"]),
        "same_labels_at_common_nodes": indices,
        "max_energy_change_MeV": energy, "max_plus_weight_change": weight,
        "minimum_individual_fidelity_at_common_nodes": float(fidelity.min()),
        "minimum_projector_fidelity_at_common_nodes": min(projectors),
        "sampled_minimum_gap_change_MeV": gap1 - gap0,
        "sampled_minimum_gap_stable": gap_stable,
        "pass": bool(passed),
    }


def serial_path(path):
    return {
        "t": path["nodes"].tolist(), "summary": path["summary"],
        **{key: value.tolist() for key, value in path["arrays"].items()},
    }


def main():
    started = time.time()
    modules = [
        ROOT / "system/scripts/analysis/paired_single_j_nambu.py",
        ROOT / "system/scripts/analysis/paired_single_j_rotor.py",
    ]
    input_hashes = {str(p.relative_to(ROOT)): sha(p) for p in modules}
    write_json(OUT / "continuation-contract.json", POLICY)
    results = []
    all_rows = []
    reference_mapping = None
    for case_id, relative, selector in SPECS:
        source = ROOT / relative
        input_hashes[relative] = sha(source)
        fit = json.loads(source.read_text())
        chosen = fit["best"] if selector == "best" else next(
            x for x in fit["starts"] if x["start"] == selector)
        contract_path = ROOT / fit["contract"]
        input_hashes[fit["contract"]] = sha(contract_path)
        if input_hashes[fit["contract"]] != fit["contract_sha256"]:
            raise RuntimeError("parent contract hash mismatch")
        if fit["model_sha256"] != input_hashes[str(modules[1].relative_to(ROOT))]:
            raise RuntimeError("frozen rotor hash mismatch")
        contract = json.loads(contract_path.read_text())
        mapping = contract["energy_data"]
        identity = [(x["level_id"], x["twice_I"], x["model_ordinal_assumed"],
                     x["energy_keV"]) for x in mapping]
        recorded = [(x["level_id"], x["twice_I"], x["model_ordinal_assumed"],
                     x["energy_keV"]) for x in chosen["energy_comparison"]]
        if identity != recorded or len(mapping) != 10:
            raise RuntimeError("predeclared state mapping changed")
        if reference_mapping is None:
            reference_mapping = identity
        elif identity != reference_mapping:
            raise RuntimeError("three minima do not share the same ten-state mapping")
        par = chosen["model_parameters"]
        params = PairedRotorParameters(
            par["two_j"], par["C_MeV"], par["gamma_deg"],
            tuple(par["inertias_hbar2_per_MeV"]),
            par["lambda_F_MeV"], par["Delta_MeV"],
        )
        if any(chosen["active_bound_mask"]):
            raise RuntimeError("a requested minimum has an active optimizer bound")
        case = {
            "case_id": case_id, "parameter_source": relative,
            "parameter_source_sha256": input_hashes[relative],
            "source_selector": selector,
            "parent_start": chosen["start"],
            "parent_RMS_keV_excluding_anchor_not_refitted":
                chosen["RMS_residual_keV_excluding_anchor"],
            "active_bound_mask": chosen["active_bound_mask"],
            "parameters": asdict(params),
            "energy_reference_level": contract["energy_reference_level"],
            "predeclared_mapping": mapping,
            "spin_results": [],
        }
        for two_I in sorted({row["twice_I"] for row in mapping}):
            rows = sorted(
                (row for row in mapping if row["twice_I"] == two_I),
                key=lambda row: row["model_ordinal_assumed"],
            )
            ordinals = [row["model_ordinal_assumed"] for row in rows]
            system = nambu.build_nambu(two_I, params)
            seeds, seed_error = seed_vectors(system, ordinals)
            build_errors = {
                key: float(getattr(system, key)) for key in (
                    "unitarity_error", "direct_transform_error_MeV",
                    "D2_leakage_MeV", "positive_reference_error_MeV",
                    "hermiticity_error_MeV",
                )
            }
            if max(build_errors.values()) > 1e-9:
                raise RuntimeError("Nambu build/embedding checks failed")
            history = []
            previous = None
            converged = False
            latest = None
            for nodes in POLICY["grids"]:
                latest = track(system, ordinals, np.linspace(0, 1, nodes), seeds)
                comparison = compare_paths(previous, latest) if previous is not None else None
                history.append({
                    "nodes": nodes, "diagnostics": latest["summary"],
                    "comparison_to_previous_grid": comparison,
                })
                write_json(
                    OUT / case_id / f"I{two_I}-grid{nodes}.json",
                    {"case_id": case_id, "two_I": two_I, "ordinals": ordinals,
                     "level_ids": [x["level_id"] for x in rows], **serial_path(latest)},
                )
                print(
                    f"{case_id} I={two_I}/2 grid={nodes} "
                    f"overlap={latest['summary']['minimum_selected_step_overlap_squared']:.8f} "
                    f"gap={1000*latest['summary']['minimum_sampled_selected_complement_gap_MeV']:.6f}keV "
                    f"bound={1000*latest['summary']['minimum_interval_selected_complement_gap_bound_MeV']:.6f}keV "
                    f"issues={len(latest['summary']['issues'])}", flush=True,
                )
                if (comparison and comparison["pass"]
                        and latest["summary"]["local_tracking_checks_pass"]):
                    converged = True
                    break
                previous = latest
            # Reverse matching is independently evaluated on the same refined nodes.
            reverse = track(system, ordinals, latest["nodes"][::-1], latest["vectors"][-1])
            reversed_path = {
                "nodes": reverse["nodes"][::-1],
                "arrays": {k: v[::-1] for k, v in reverse["arrays"].items()},
                "vectors": reverse["vectors"][::-1], "summary": reverse["summary"],
            }
            reverse_comparison = compare_paths(latest, reversed_path)
            reverse_seed_fidelity = np.clip(abs(np.einsum(
                "ij,ij->j", seeds.conj(), reverse["vectors"][-1])) ** 2, 0, 1)
            reverse_check = {
                "comparison": reverse_comparison,
                "return_seed_fidelities": reverse_seed_fidelity.tolist(),
                "diagnostics": reverse["summary"],
                "pass": bool(reverse_comparison["pass"]
                             and reverse_seed_fidelity.min() >= 1 - POLICY["fidelity_refinement_tolerance"]
                             and reverse["summary"]["local_tracking_checks_pass"]),
            }
            write_json(OUT / case_id / f"I{two_I}-reverse.json",
                       {**serial_path(reverse), "check": reverse_check})
            shifted = track(
                system, ordinals, latest["nodes"], seeds,
                shift=POLICY["reference_shift_control_MeV"],
            )
            shift_comparison = compare_paths(latest, shifted)
            shift_check = {
                "common_shift_MeV": POLICY["reference_shift_control_MeV"],
                "comparison": shift_comparison,
                "pass": bool(shift_comparison["pass"]
                             and shifted["summary"]["local_tracking_checks_pass"]),
            }
            zero = track(system, ordinals, np.linspace(0, 1, 5), seeds, coupling_scale=0)
            zero_energy_error = float(np.max(abs(
                zero["arrays"]["energy"] - system.reference_plus.eigenvalues_MeV[ordinals]
            )))
            zero_weight_error = float(np.max(abs(zero["arrays"]["weight"] - 1)))
            zero_fidelity = float(np.clip(abs(np.einsum(
                "ij,ij->j", seeds.conj(), zero["vectors"][-1])) ** 2, 0, 1).min())
            zero_check = {
                "maximum_energy_error_MeV": zero_energy_error,
                "maximum_plus_weight_error": zero_weight_error,
                "minimum_seed_fidelity": zero_fidelity,
                "pass": bool(zero_energy_error < POLICY["energy_refinement_tolerance_MeV"]
                             and zero_weight_error < POLICY["weight_refinement_tolerance"]
                             and zero_fidelity > 1 - POLICY["fidelity_refinement_tolerance"]
                             and zero["summary"]["local_tracking_checks_pass"]),
            }
            accepted = converged and reverse_check["pass"] and shift_check["pass"] and zero_check["pass"]
            spin_result = {
                "two_I": two_I, "ordinals": ordinals,
                "sector_dimension": system.sector_dimension,
                "initial_embedding_error": seed_error,
                "build_errors": build_errors,
                "grids_attempted": history,
                "final_grid_nodes": len(latest["nodes"]),
                "forward_diagnostics": latest["summary"],
                "reverse_check": reverse_check, "reference_shift_check": shift_check,
                "zero_coupling_check": zero_check,
                "status": "converged-mathematical-continuation" if accepted else
                          "unresolved-continuation-candidates-not-certified",
            }
            case["spin_results"].append(spin_result)
            np.savez_compressed(
                OUT / case_id / f"I{two_I}-selected-endpoints.npz",
                seeds_BCS_coordinates=seeds,
                endpoint_BCS_coordinates=latest["vectors"][-1],
                endpoint_original_product_coordinates=system.embedding @ latest["vectors"][-1],
            )
            for column, mapped in enumerate(rows):
                a = latest["arrays"]
                record = {
                    "case_id": case_id, **mapped,
                    "status": spin_result["status"],
                    "final_grid_nodes": len(latest["nodes"]),
                    "t0_energy_MeV": float(system.reference_plus.eigenvalues_MeV[ordinals[column]]),
                    "t1_energy_MeV": float(a["energy"][-1, column]),
                    "absolute_shift_keV": float(
                        1000 * (a["energy"][-1, column]
                                - system.reference_plus.eigenvalues_MeV[ordinals[column]])),
                    "t0_full_index": int(a["indices"][0, column]),
                    "t1_full_index": int(a["indices"][-1, column]),
                    "t1_BCS_plus_weight": float(a["weight"][-1, column]),
                    "minimum_BCS_plus_weight_along_path": float(a["weight"][:, column].min()),
                    "minimum_step_overlap_squared": float(a["overlap"][:, column].min()),
                    "minimum_selected_complement_gap_keV": float(
                        1000 * a["gap_complement"][:, column].min()),
                    "minimum_all_other_gap_keV": float(1000 * a["gap_all"][:, column].min()),
                }
                all_rows.append(record)
            write_json(OUT / case_id / "progress.json", case)
        local_rows = [row for row in all_rows if row["case_id"] == case_id]
        anchor = next(row for row in local_rows
                      if row["level_id"] == case["energy_reference_level"])
        for row in local_rows:
            row["t0_relative_energy_keV"] = 1000 * (row["t0_energy_MeV"] - anchor["t0_energy_MeV"])
            row["t1_relative_energy_keV"] = 1000 * (row["t1_energy_MeV"] - anchor["t1_energy_MeV"])
            row["relative_shift_vs_mapped_anchor_keV"] = (
                row["t1_relative_energy_keV"] - row["t0_relative_energy_keV"])
            row["t1_Ex_at_fixed_anchor_keV"] = anchor["energy_keV"] + row["t1_relative_energy_keV"]
            row["relative_shift_status"] = (
                "converged-mathematical-reference"
                if row["status"] == anchor["status"] == "converged-mathematical-continuation"
                else "tentative-because-state-or-anchor-unresolved"
            )
        case["anchor_absolute_shift_keV"] = anchor["absolute_shift_keV"]
        case["state_results"] = local_rows
        case["all_ten_states_converged"] = all(
            row["status"] == "converged-mathematical-continuation" for row in local_rows)
        write_json(OUT / case_id / "result.json", case)
        results.append(case)
    changed = [path for path, before in input_hashes.items() if sha(ROOT / path) != before]
    result = {
        "scope": POLICY["interpretation"], "policy": POLICY,
        "runner_sha256": sha(__file__), "input_sha256": input_hashes,
        "inputs_changed_during_run": changed,
        "runtime": {"python": platform.python_version(), "numpy": np.__version__,
                    "scipy": scipy.__version__, "elapsed_seconds": time.time() - started},
        "cases": results,
        "all_cases_converged_under_declared_checks": bool(
            not changed and all(case["all_ten_states_converged"] for case in results)),
        "boundaries": [
            "No refit, physical-state certification, original-code certification, EM or transfer prediction.",
            "Three minima have no active bounds, but originate from finite declared fitting bounds.",
            "Tracking labels remain those of the predeclared t0 Hplus states.",
            "The source's physical-particle/hole versus BCS-sign issue remains explicit and unresolved.",
        ],
    }
    write_json(OUT / "results.json", result)
    fields = [
        "case_id", "level_id", "twice_I", "model_ordinal_assumed", "status",
        "final_grid_nodes", "t0_full_index", "t1_full_index",
        "t0_energy_MeV", "t1_energy_MeV", "absolute_shift_keV",
        "t0_relative_energy_keV", "t1_relative_energy_keV",
        "relative_shift_vs_mapped_anchor_keV", "t1_Ex_at_fixed_anchor_keV",
        "t1_BCS_plus_weight", "minimum_BCS_plus_weight_along_path",
        "minimum_step_overlap_squared", "minimum_selected_complement_gap_keV",
        "minimum_all_other_gap_keV", "relative_shift_status",
    ]
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(all_rows)
    (OUT / "state-results.csv").write_text(buffer.getvalue())
    print(f"COMPLETE: all_cases_converged={result['all_cases_converged_under_declared_checks']} "
          f"elapsed={time.time()-started:.2f}s changed_inputs={changed}", flush=True)


if __name__ == "__main__":
    main()
