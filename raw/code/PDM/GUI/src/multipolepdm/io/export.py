"""Portable output snapshots; large text export is optional and streamed."""

from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
from importlib.metadata import version
import json
from pathlib import Path
import re
import uuid
import sys

import numpy as np

from multipolepdm import __version__
from multipolepdm.contracts import (
    HDISegment,
    Interval,
    MappingResult,
    MarginalSummary,
    ResponseGrid,
    Summary,
)
from multipolepdm.io.input import job_from_dict, job_to_dict
from multipolepdm.pdm.observations import observation_mesh
from multipolepdm.pdm.statistics import DEFAULT_INTERVAL_MASS, summarize_density

RESULT_SCHEMA = "multipolepdm-result-v2"
LEGACY_RESULT_SCHEMA = "multipolepdm-result-v1"


def reserve_result_directory(job):
    label = re.sub(r"[^A-Za-z0-9_.-]+", "-", job.label).strip(".-")[:60] or "transition"
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
    return Path(job.output.directory) / f"{stamp}-{label}-{uuid.uuid4().hex[:10]}"


def result_directory(job):
    path = reserve_result_directory(job).expanduser()
    path.mkdir(parents=True, exist_ok=False)
    return path


def _jsonable(value):
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    raise TypeError(type(value).__name__)


def export_result(
    result, summary, directory, cancelled=lambda: False, progress=lambda value: None
):
    """Write the snapshot and return the terminal status recorded on disk."""
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    r = result.response
    package_root = Path(__file__).resolve().parents[1]
    code_digest = hashlib.sha256()
    for source in sorted(package_root.rglob("*.py")):
        code_digest.update(source.relative_to(package_root).as_posix().encode())
        code_digest.update(source.read_bytes())
    manifest = {
        "schema": RESULT_SCHEMA,
        "version": __version__,
        "implementation_sha256": code_digest.hexdigest(),
        "runtime": {
            "python": sys.version.split()[0],
            **{
                name: version(name)
                for name in ("numpy", "scipy", "sympy", "matplotlib")
            },
        },
        "status": "saving",
        "input": job_to_dict(result.job),
        "response_metadata": r.metadata,
        "normalization": result.normalization,
        "warnings": list(result.warnings),
        "reference_spin": r.reference_spin,
        "ratio_name": r.ratio_name,
        "invalid_response_nodes": int(r.valid.size - np.count_nonzero(r.valid)),
        "units": {
            "xi_rad": "rad",
            "sigma": "hbar units",
            "sigma_over_i": "dimensionless",
        },
        "grid_interpretation": "Pointwise density samples on the native xi/sigma grid, not histogram heights. For probability use parameter_node_probability or native trapezoidal weights. Coarse tan(xi) resampling is not mass preserving; use marginal_delta.csv for the refined delta PDF.",
        "independent_observation_errors": True,
        "summary_interpretation": {
            "default_interval_mass": DEFAULT_INTERVAL_MASS,
            "delta_statistics": "tan of angle estimates; HDI modes, mass and threshold are evaluated in arctan_delta (rad)",
            "delta_mean": "tan of the angle mean; guides are null when their angle is outside the scan or crosses a tan singularity",
            "sigma_statistics": "evaluated in sigma_over_i",
        },
    }

    def record(status, error=None):
        manifest["status"] = status
        if error is not None:
            manifest["error"] = str(error)
        (directory / "manifest.json").write_text(
            json.dumps(manifest, indent=2, allow_nan=False) + "\n", encoding="utf-8"
        )

    record("saving")
    try:
        if cancelled():
            record("cancelled")
            return "cancelled"
        observed_p, observed_ratio, observed_pdf = observation_mesh(
            result.job.polarization, result.job.angular_ratio
        )
        np.savez_compressed(
            directory / "density.npz",
            xi_rad=r.xi_rad,
            sigma=r.sigma,
            polarization=r.polarization,
            angular_ratio=r.angular_ratio,
            valid=r.valid,
            observation_density=result.observation_density,
            jacobian=result.jacobian,
            parameter_density=result.parameter_density,
            observed_p=observed_p,
            observed_ratio=observed_ratio,
            observed_pdf=observed_pdf,
        )
        summary_data = asdict(summary)
        marginals = (
            ("arctan_delta", summary.arctan_delta),
            ("delta", summary.delta),
            ("sigma_over_i", summary.sigma_over_i),
        )
        for name, marginal in marginals:
            for serialized, interval in zip(summary_data[name]["intervals"], marginal.intervals):
                serialized["hdi"] = interval.hdi
        (directory / "summary.json").write_text(
            json.dumps(summary_data, default=_jsonable, indent=2, allow_nan=False)
            + "\n",
            encoding="utf-8",
        )
        for name, marginal in marginals:
            np.savetxt(
                directory / f"marginal_{name}.csv",
                np.column_stack((marginal.coordinate, marginal.density)),
                delimiter=",",
                header=f"{name},probability_density_per_{name}",
                comments="",
            )
        progress(25)
        if cancelled():
            record("cancelled")
            return "cancelled"
        if result.job.output.full_csv:
            ratio_mesh, p_mesh = np.meshgrid(observed_ratio, observed_p)
            np.savetxt(
                directory / "observation_density.csv",
                np.column_stack(
                    (ratio_mesh.ravel(), p_mesh.ravel(), observed_pdf.ravel())
                ),
                delimiter=",",
                header=f"{r.ratio_name},polarization_P,observation_density",
                comments="",
            )
            with (directory / "parameter_density.csv").open(
                "w", encoding="utf-8"
            ) as stream:
                stream.write(
                    f"mixing_angle_xi_rad,mixing_ratio_delta,alignment_sigma,alignment_sigma_over_i,polarization_P,{r.ratio_name},observation_density,jacobian_abs_xi_sigma,parameter_density_per_rad_sigma,parameter_density_per_delta_sigma,parameter_density_per_rad_sigma_over_i,native_quadrature_weight,parameter_node_probability\n"
                )

                def weights(axis):
                    widths = np.diff(axis)
                    return np.concatenate(
                        (
                            [widths[0] / 2],
                            (widths[:-1] + widths[1:]) / 2,
                            [widths[-1] / 2],
                        )
                    )

                wx, ws = weights(r.xi_rad), weights(r.sigma)
                for n, sigma in enumerate(r.sigma):
                    if cancelled():
                        break
                    delta = np.tan(r.xi_rad)
                    weight = wx * ws[n]
                    columns = (
                        r.xi_rad,
                        delta,
                        np.full(delta.shape, sigma),
                        np.full(delta.shape, sigma / r.reference_spin),
                        r.polarization[n],
                        r.angular_ratio[n],
                        result.observation_density[n],
                        result.jacobian[n],
                        result.parameter_density[n],
                        result.parameter_density[n] / (1 + delta**2),
                        r.reference_spin * result.parameter_density[n],
                        weight,
                        result.parameter_density[n] * weight,
                    )
                    np.savetxt(
                        stream, np.column_stack(columns), delimiter=",", fmt="%.12g"
                    )
                    progress(25 + 74 * (n + 1) / len(r.sigma))
        if cancelled():
            record("cancelled")
            return "cancelled"
        record("saved")
    except Exception as exc:
        record("save_failed", exc)
        raise
    progress(100)
    return "saved"


def load_result(directory, allow_partial=False):
    directory = Path(directory)
    meta = json.loads((directory / "manifest.json").read_text(encoding="utf-8"))
    if meta["schema"] not in (RESULT_SCHEMA, LEGACY_RESULT_SCHEMA):
        raise ValueError("Unsupported output schema.")
    if meta["status"] != "saved" and not allow_partial:
        raise ValueError(
            "Output is not fully saved. Use allow_partial=True only to recover a complete snapshot knowingly."
        )
    with np.load(directory / "density.npz", allow_pickle=False) as data:
        r = ResponseGrid(
            data["xi_rad"],
            data["sigma"],
            data["polarization"],
            data["angular_ratio"],
            data["valid"],
            meta["reference_spin"],
            meta["ratio_name"],
            meta["response_metadata"],
        )
        return MappingResult(
            job_from_dict(meta["input"]),
            r,
            data["observation_density"],
            data["jacobian"],
            data["parameter_density"],
            meta["normalization"],
            tuple(meta["warnings"]),
        )


def load_snapshot(directory):
    directory = Path(directory)
    result = load_result(directory)
    summary = json.loads((directory / "summary.json").read_text(encoding="utf-8"))
    if "arctan_delta" not in summary:
        return result, summarize_density(result)

    def marginal(name):
        entry = summary[name]
        intervals = tuple(
            Interval(
                interval["mass"],
                tuple(interval["eti"]),
                tuple(
                    HDISegment(
                        tuple(segment["bounds"]),
                        segment["mass"],
                        tuple(tuple(band) for band in segment["mode_ranges"]),
                    )
                    for segment in interval["hdi_segments"]
                ),
                interval["hdi_threshold"],
            )
            for interval in entry["intervals"]
        )
        return MarginalSummary(
            np.asarray(entry["coordinate"], dtype=float),
            np.asarray(entry["density"], dtype=float),
            entry["median"],
            entry["mode"],
            intervals,
            entry["coordinate_name"],
            entry["evaluation_coordinate"],
            entry["mean"],
            entry["std"],
            tuple(entry["mean_bounds"]),
            tuple(tuple(flags) for flags in entry["mean_bound_flags"]),
        )

    return result, Summary(
        delta=marginal("delta"),
        sigma_over_i=marginal("sigma_over_i"),
        arctan_delta=marginal("arctan_delta"),
    )
