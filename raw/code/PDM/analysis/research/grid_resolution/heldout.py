"""Freeze and check six held-out cases against the original reference grid."""

import argparse
import math
import os
from pathlib import Path
import sys
from time import perf_counter

import numpy as np

from study import (
    HERE, MODES, PACKAGE, ROOT, SCRATCH, build_job, compare, csv_rows, digest,
    dump, evaluate_response, flatten_result, frozen, inventory, load,
    observation, run_group,
)


INPUTS = HERE / "heldout_inputs.json"
PRIMARY_INPUTS = HERE / "frozen_inputs.json"
PRIMARY_RESULTS = HERE / "results.json"
SELECTED = "a0.1_s0.005"
DELTAS = (-0.5, 5.0)


def freeze():
    primary = frozen(PRIMARY_INPUTS)
    primary_results = load(PRIMARY_RESULTS)
    assert primary_results["input_sha256"] == digest(PRIMARY_INPUTS)
    assert primary_results["fastest_converged"]["id"] == SELECTED
    assert inventory(PACKAGE.rglob("*.py"), PACKAGE) == primary["source_package_sha256"]
    assert not set(DELTAS) & {case["truth_delta"] for case in primary["cases"]}
    floor = primary["polarization_error_floor"]
    cases = []
    for mode in MODES:
        original = next(case for case in primary["cases"] if case["mode"] == mode)
        xi = np.arctan(DELTAS)
        response = evaluate_response(build_job(original), xi, np.array([original["truth_sigma"]]))
        assert response.valid.all()
        for index, delta in enumerate(DELTAS):
            polar = float(response.polarization[0, index])
            ratio = float(response.angular_ratio[0, index])
            cases.append({
                **original,
                "id": f"{mode}_{delta:+g}",
                "truth_delta": delta,
                "truth_angle_deg": math.degrees(xi[index]),
                "polarization": observation(polar, max(floor, 0.8 * abs(polar))),
                "polarization_floor_applied": floor >= 0.8 * abs(polar),
                "ratio": observation(ratio, 0.10 * ratio),
            })
    assert any(case["polarization_floor_applied"] for case in cases)
    dump(INPUTS, {
        **primary,
        "primary_inputs_sha256": digest(PRIMARY_INPUTS),
        "primary_results_sha256": digest(PRIMARY_RESULTS),
        "heldout_script_sha256": digest(Path(__file__)),
        "selected_grid": SELECTED,
        "grids": [grid for grid in primary["grids"] if grid["id"] in (SELECTED, primary["reference"])],
        "cases": cases,
    }, exclusive=True)
    INPUTS.with_suffix(".sha256").write_text(f"{digest(INPUTS)}  {INPUTS.name}\n", encoding="ascii")
    print(f"Frozen {len(cases)} cases. SHA-256 {digest(INPUTS)}")


def s_truth_in_hdi(result, truth):
    return any(component["lower"] <= truth <= component["upper"]
               for component in result["s"]["hdi_components"])


def run():
    config = frozen(INPUTS)
    assert digest(PRIMARY_INPUTS) == config["primary_inputs_sha256"]
    assert digest(PRIMARY_RESULTS) == config["primary_results_sha256"]
    assert digest(Path(__file__)) == config["heldout_script_sha256"]
    source_hashes = inventory(PACKAGE.rglob("*.py"), PACKAGE)
    assert source_hashes == config["source_package_sha256"]
    assert all(digest(ROOT / path) == checksum for path, checksum in config["empirical_sha256"].items())

    start = perf_counter()
    scratch = SCRATCH / "heldout"
    scratch.mkdir(parents=True, exist_ok=True)
    cases = {case["id"]: case for case in config["cases"]}
    selected, reference = config["selected_grid"], config["reference"]
    case_results, comparison_rows = [], []
    for mode in MODES:
        prefixes = {grid: scratch / f"{grid}_{mode}" for grid in (selected, reference)}
        for grid, prefix in prefixes.items():
            run_group(config, grid, mode, prefix)
        sample_group, ref_group = [
            load(prefix.parent / f"{prefix.name}.json") for prefix in prefixes.values()
        ]
        sample_prefix, ref_prefix = prefixes.values()
        with (
            np.load(sample_prefix.parent / f"{sample_prefix.name}.npz") as sample_pdf,
            np.load(ref_prefix.parent / f"{ref_prefix.name}.npz") as ref_pdf,
        ):
            for sample, ref in zip(sample_group["rows"], ref_group["rows"], strict=True):
                assert sample["case_id"] == ref["case_id"]
                case = cases[sample["case_id"]]
                comparison = compare(sample, ref, sample_pdf, ref_pdf, config["comparison_tolerances"])
                for row in (sample, ref):
                    row["truth_in_s_hdi"] = s_truth_in_hdi(row, case["truth_s"])
                comparison_rows.append(flatten_result({
                    **comparison,
                    "truth_delta": case["truth_delta"], "truth_s": case["truth_s"],
                    "P0": case["polarization"]["value"], "P_error": case["polarization"]["err_plus"],
                    "P_floor_applied": case["polarization_floor_applied"],
                    "R0": case["ratio"]["value"], "R_error": case["ratio"]["err_plus"],
                    "selected_truth_in_angle_hdi": sample["truth_in_angle_hdi"],
                    "reference_truth_in_angle_hdi": ref["truth_in_angle_hdi"],
                    "selected_truth_in_s_hdi": sample["truth_in_s_hdi"],
                    "reference_truth_in_s_hdi": ref["truth_in_s_hdi"],
                    "selected_edge_flags": sample["edge_flags"],
                    "reference_edge_flags": ref["edge_flags"],
                }))
                case_results.append({
                    "input": case, "selected": sample, "reference": ref, "comparison": comparison,
                })
    assert {row["case_id"] for row in comparison_rows} == set(cases)
    assert inventory(PACKAGE.rglob("*.py"), PACKAGE) == source_hashes
    summary = {
        "converged_count": sum(row["converged"] for row in comparison_rows),
        "case_count": len(comparison_rows),
        "failed_cases": [row["case_id"] for row in comparison_rows if not row["converged"]],
        "floor_active_count": sum(row["P_floor_applied"] for row in comparison_rows),
        "selected_truth_in_angle_hdi_count": sum(row["selected_truth_in_angle_hdi"] for row in comparison_rows),
        "reference_truth_in_angle_hdi_count": sum(row["reference_truth_in_angle_hdi"] for row in comparison_rows),
    }
    dump(HERE / "heldout.json", {
        "input_sha256": digest(INPUTS),
        "primary_results_sha256": config["primary_results_sha256"],
        "selected_grid": selected,
        "reference_grid": reference,
        "comparison_tolerances": config["comparison_tolerances"],
        "summary": summary,
        "cases": case_results,
        "run_wall_seconds": perf_counter() - start,
    })
    csv_rows(HERE / "heldout.csv", comparison_rows)
    print(summary)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("freeze", "run"))
    args = parser.parse_args()
    if os.environ.get("OPENBLAS_NUM_THREADS") != "1" or not sys.dont_write_bytecode:
        parser.error("Run with OPENBLAS_NUM_THREADS=1 and python -B.")
    if args.command == "freeze":
        freeze()
    else:
        run()


if __name__ == "__main__":
    main()
