"""Batch calculation and exact pure-multipole forward calibration."""

import argparse
from dataclasses import replace
import json
from pathlib import Path

import numpy as np

from multipolepdm.contracts import OutputSpec
from multipolepdm.io.export import export_result, result_directory
from multipolepdm.io.input import (
    example_data,
    export_example,
    job_from_dict,
    job_to_dict,
    load_jobs,
)
from multipolepdm.jobs.workers import compute_job
from multipolepdm.models.registry import evaluate_response


def forward_calibration(job, directory):
    """A pure transition supplies a response curve, not a fabricated delta PDF."""
    if len(job.target.multipoles) != 1:
        raise ValueError("Forward calibration requires a single target multipole.")
    if job.reference_spin == 0:
        sigma = np.array([1.0])
    else:
        _, sigma = job.grid.axes(job.reference_spin)
    r = evaluate_response(job, np.array([0.0]), sigma)
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    np.savetxt(
        directory / "forward_calibration.csv",
        np.column_stack(
            (sigma, r.polarization[:, 0], r.angular_ratio[:, 0], r.valid[:, 0])
        ),
        delimiter=",",
        header=f"source_sigma,polarization_P,{job.ratio_name},response_defined",
        comments="",
    )
    (directory / "forward_calibration.json").write_text(
        json.dumps(
            {
                "input": job_to_dict(job),
                "observations_used_for_inference": False,
                "undefined_points": int(np.count_nonzero(~r.valid)),
                "target_multipole": job.target.multipoles[0],
                "reference_spin": job.reference_spin,
                "sigma_meaning": "irrelevant for I_ref=0"
                if job.reference_spin == 0
                else "Gaussian width at reference state",
                "density_status": "No delta PDF: a pure target has no mixing degree of freedom.",
                "response_metadata": r.metadata,
            },
            indent=2,
        )
        + "\n"
    )
    return r


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="PDM: measured polarization and angular ratios to parameter densities."
    )
    parser.add_argument("input", nargs="?", help="Single-job or batch JSON file")
    parser.add_argument("--example", choices=["P_ADO", "P_DCO", "PDCO", "batch"])
    parser.add_argument("--export-example", metavar="PATH")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--full-csv", action="store_true")
    parser.add_argument(
        "--forward",
        action="store_true",
        help="Pure-target forward calibration only (no parameter PDF)",
    )
    args = parser.parse_args(argv)
    if args.export_example:
        export_example(args.example or "P_ADO", args.export_example)
        return 0
    if args.input:
        jobs = load_jobs(args.input)
    elif args.example:
        data = example_data(args.example)
        jobs = (
            tuple(job_from_dict(d) for d in data["jobs"])
            if args.example == "batch"
            else (job_from_dict(data),)
        )
    else:
        parser.error("Provide an input JSON file or --example MODE.")
    errors = 0
    for job in jobs:
        if args.output_dir is not None or args.full_csv:
            job = replace(
                job,
                output=OutputSpec(
                    str(args.output_dir or job.output.directory),
                    args.full_csv or job.output.full_csv,
                ),
            )
        try:
            directory = result_directory(job)
            if args.forward:
                forward_calibration(job, directory)
            else:
                result, summary = compute_job(job)
                print(
                    f"{job.label}: calculation ready; saving to {directory}", flush=True
                )
                export_result(result, summary, directory)
                from multipolepdm.plotting.overview import make_preview
                from matplotlib import pyplot as plt

                preview = make_preview(result, summary)
                preview.figure.savefig(directory / "overview.pdf")
                plt.close(preview.figure)
            print(f"OK: {directory}", flush=True)
        except Exception as exc:
            print(f"FAILED {job.label}: {exc}", flush=True)
            errors += 1
    return int(errors > 0)


if __name__ == "__main__":
    raise SystemExit(main())
