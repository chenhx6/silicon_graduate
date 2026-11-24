#!/usr/bin/env python3
"""Reproduce declared literature scenarios; never use reported delta as input."""

import argparse
import csv
from dataclasses import replace
import hashlib
import json
from pathlib import Path
import sys
from time import perf_counter

from run_literature_cases import (code_provenance, compare_resolution, refined_grid, run_grouped,
                                  select_package, summarize_arrays)


def write_json(path, data):
    path.write_text(json.dumps(data, indent=2, allow_nan=False) + "\n")


def run(input_dir, output):
    import numpy as np
    from scipy.integrate import trapezoid

    import multipolepdm
    from multipolepdm.io.input import job_from_dict, job_to_dict
    from multipolepdm.jobs.workers import compute_job
    from multipolepdm.models.registry import evaluate_response

    output.mkdir(parents=True, exist_ok=True)
    manifest = json.loads((input_dir / "scenarios.json").read_text())
    rows = []
    for declaration in manifest["batches"]:
        path = input_dir / declaration["file"]
        if hashlib.sha256(path.read_bytes()).hexdigest() != declaration["sha256"]:
            raise ValueError(f"Frozen input hash changed: {path}")
        for number, doc in enumerate(json.loads(path.read_text())["jobs"], 1):
            job = job_from_dict(doc)
            row = {
                "case_id": f"{path.stem}_{number:02d}",
                "label": job.label,
                "mode": job.mode,
                "input": job_to_dict(job),
                "source_declaration": declaration,
            }
            stamp = perf_counter()
            try:
                if len(job.target.multipoles) == 1:
                    _, sigma = job.grid.axes(job.reference_spin)
                    response = evaluate_response(job, np.array([0.0]), sigma)
                    p, ratio, valid = (response.polarization[:, 0],
                                       response.angular_ratio[:, 0], response.valid[:, 0])
                    def distance(values, measurement):
                        difference = values - measurement.value
                        return np.abs(difference) / np.where(
                            difference < 0, measurement.err_minus, measurement.err_plus)
                    boxes = np.maximum(distance(p, job.polarization),
                                       distance(ratio, job.angular_ratio))
                    row.update(
                        kind="pure_forward", no_delta_pdf=True,
                        sigma_over_i_grid=(sigma / job.reference_spin).tolist(),
                        polarization=np.where(valid, p, None).tolist(),
                        angular_ratio=np.where(valid, ratio, None).tolist(),
                        response_defined=valid.tolist(),
                        minimum_joint_error_box_scale=float(boxes[valid].min()),
                    )
                else:
                    result, summary = compute_job(job)
                    row.update(kind="mixed_inverse",
                               **summarize_arrays(result, summary, np, trapezoid))
                    # The first declared mixed case per batch has a resolution control.
                    if number == 1:
                        fine, fine_summary = compute_job(replace(
                            job, grid=refined_grid(job.grid)))
                        refined = summarize_arrays(fine, fine_summary, np, trapezoid)
                        row["refinement"] = compare_resolution(row, refined)
                row["status"] = "success"
            except Exception as exc:
                row.update(status="failed", error=f"{type(exc).__name__}: {exc}")
            row["elapsed_seconds"] = perf_counter() - stamp
            rows.append(row)
            print(row["case_id"], row["label"], row["status"], flush=True)
    write_json(output / "results.json", {
        "scope": "Declared point or ideal-ring models, not exact array replays. Alternatives reuse observations and are not independent experiments.",
        "reported_delta_used_in_inference": False,
        "provenance": code_provenance(multipolepdm), "cases": rows,
    })
    with (output / "results.csv").open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["case_id", "label", "mode", "kind", "status", "delta_median",
                         "sigma_over_i_median", "minimum_joint_error_box_scale"])
        for row in rows:
            writer.writerow([row["case_id"], row["label"], row["mode"], row.get("kind"),
                             row["status"], row.get("delta", {}).get("median"),
                             row.get("sigma_over_i", {}).get("median"),
                             row.get("minimum_joint_error_box_scale", row.get(
                                 "observation_compatibility", {}).get("minimum_joint_error_box_scale"))])
    return int(any(row["status"] != "success" for row in rows))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path(__file__).resolve().parents[1] / "cases/followup")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--project-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--save-grids", action="store_true")
    args = parser.parse_args()
    sys.dont_write_bytecode = True
    if (args.input / "snapshot.json").is_file():
        package = select_package(args.project_root)
        output = args.output or args.input.parent / "results_v0_1_1"
        raise SystemExit(run_grouped(args.input, output, package, "followup",
                                     save_grids=args.save_grids, entrypoint=Path(__file__)))
    output = args.output or Path(__file__).resolve().parents[1] / "cases/followup/results"
    raise SystemExit(run(args.input, output))
