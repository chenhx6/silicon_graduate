"""Check provenance/anchor arithmetic and locate the one failed control.

Reads only the declared model inputs and continuation products. Writes the
verification receipt here; does not refit or alter the acceptance thresholds.
"""
import sys
sys.dont_write_bytecode = True

import csv
import json

import run_continuation as r
import run_adaptive_refinement as adaptive

np = r.np


def main():
    result = json.loads((r.OUT / "refined-results.json").read_text())
    assert r.sha(r.OUT / "run_continuation.py") == result["runner_sha256"]
    assert r.sha(r.OUT / "run_adaptive_refinement.py") == result["adaptive_runner_sha256"]
    assert r.sha(r.OUT / "results.json") == result["uniform_results_sha256"]
    for path, digest in result["input_sha256"].items():
        assert r.sha(r.ROOT / path) == digest, path
    with (r.OUT / "refined-state-results.csv").open(newline="") as handle:
        table = list(csv.DictReader(handle))
    assert len(table) == 30
    parent_errors = {}
    arithmetic_errors = {}
    failures = []
    for case in result["cases"]:
        parent = json.loads((r.ROOT / case["parameter_source"]).read_text())
        parent_fit = (parent["best"] if case["source_selector"] == "best" else
                      next(x for x in parent["starts"]
                           if x["start"] == case["source_selector"]))
        parent_rows = {row["level_id"]: row for row in parent_fit["energy_comparison"]}
        parent_errors[case["case_id"]] = max(
            abs(row["t0_relative_energy_keV"]
                - parent_rows[row["level_id"]]["model_relative_energy_keV"])
            for row in case["state_results"])
        assert parent_errors[case["case_id"]] < 1e-7
        anchor = next(row for row in case["state_results"]
                      if row["level_id"] == case["energy_reference_level"])
        assert anchor["level_id"] == "129Ba_Ex278p81keV"
        assert anchor["twice_I"] == 11 and anchor["model_ordinal_assumed"] == 0
        assert anchor["relative_shift_vs_mapped_anchor_keV"] == 0
        assert anchor["t1_Ex_at_fixed_anchor_keV"] == 278.81
        arithmetic_errors[case["case_id"]] = max(
            abs(row["relative_shift_vs_mapped_anchor_keV"]
                - (row["absolute_shift_keV"] - anchor["absolute_shift_keV"]))
            for row in case["state_results"])
        assert arithmetic_errors[case["case_id"]] < 1e-8
        for row in case["state_results"]:
            tab = next(x for x in table if x["case_id"] == case["case_id"]
                       and x["level_id"] == row["level_id"])
            assert tab["status"] == row["status"]
            for key in ("t0_energy_MeV", "t1_energy_MeV",
                        "relative_shift_vs_mapped_anchor_keV", "t1_BCS_plus_weight"):
                assert float(tab[key]) == row[key]
            assert row["t0_full_index"] == row["t1_full_index"]
        for spin in case["spin_results"]:
            assert spin["forward_diagnostics"]["local_tracking_checks_pass"]
            assert spin["reverse_check"]["pass"]
            assert spin["zero_coupling_check"]["pass"]
            if not spin["reference_shift_check"]["pass"]:
                failures.append({"case_id": case["case_id"], "two_I": spin["two_I"],
                                 "control": "common-reference-shift BCS+ weight tolerance"})
    # Re-evaluate only the failed control to preserve its actual location.
    located = []
    for failure in failures:
        case = next(c for c in result["cases"] if c["case_id"] == failure["case_id"])
        spin = next(s for s in case["spin_results"] if s["two_I"] == failure["two_I"])
        path = json.loads((
            r.OUT / case["case_id"] / f"I{spin['two_I']}-adaptive-final.json").read_text())
        system = r.nambu.build_nambu(spin["two_I"], adaptive.parameters(case))
        seeds, _ = r.seed_vectors(system, spin["ordinals"])
        shifted = r.track(system, spin["ordinals"], np.asarray(path["t"]), seeds,
                          shift=r.POLICY["reference_shift_control_MeV"])
        difference = abs(shifted["arrays"]["weight"] - np.asarray(path["weight"]))
        point, column = np.unravel_index(np.argmax(difference), difference.shape)
        at_t = float(path["t"][point])
        matrix = r.nambu.hamiltonian_at(system, at_t)
        shifted_matrix = matrix + 100 * np.eye(len(matrix))
        matrix_rounding = float(np.linalg.norm(shifted_matrix - 100 * np.eye(len(matrix))
                                              - matrix, 2))
        located.append({
            **failure, "t": at_t, "selected_ordinal": spin["ordinals"][column],
            "full_index": path["indices"][point][column],
            "maximum_weight_change": float(difference[point, column]),
            "prespecified_weight_tolerance": r.POLICY["weight_refinement_tolerance"],
            "unshifted_weight": path["weight"][point][column],
            "shifted_weight": float(shifted["arrays"]["weight"][point, column]),
            "selected_complement_gap_here_MeV": path["gap_complement"][point][column],
            "shifted_eigen_residual_here_MeV":
                float(shifted["arrays"]["residual"][point, column]),
            "matrix_shift_then_subtract_rounding_norm_MeV": matrix_rounding,
            "endpoint_weight_errors_by_selected_ordinal": difference[-1].tolist(),
            "endpoint_energy_errors_MeV": (
                shifted["arrays"]["energy"][-1] - np.asarray(path["energy"][-1])).tolist(),
            "interpretation": (
                "Fixed-rank forward/reverse paths pass. The full-path weight "
                "invariance control fails its declared tolerance; retain the "
                "joint spin-sector failure. Endpoint agreement alone does not "
                "override that failure."
            ),
        })
    receipt = {
        "input_and_runner_hashes_match": True,
        "CSV_matches_consolidated_JSON": True,
        "parent_t0_relative_energy_max_difference_keV": parent_errors,
        "anchor_relative_shift_arithmetic_max_error_keV": arithmetic_errors,
        "forward_local_and_reverse_checks_all_pass": True,
        "zero_coupling_checks_all_pass": True,
        "control_failures": located,
        "fully_accepted_state_count": sum(
            row["status"] == "converged-mathematical-continuation"
            for c in result["cases"] for row in c["state_results"]),
        "total_state_references": len(table),
        "verification_runner_sha256": r.sha(__file__),
        "refined_results_sha256": r.sha(r.OUT / "refined-results.json"),
    }
    r.write_json(r.OUT / "verification.json", receipt)
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
