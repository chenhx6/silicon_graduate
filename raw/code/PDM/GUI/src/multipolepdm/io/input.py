"""JSON-only input, shared by the GUI, CLI and notebooks."""

import json
from dataclasses import asdict
from importlib import resources
from pathlib import Path

from multipolepdm.contracts import (
    Geometry,
    GridSpec,
    JobRequest,
    Measurement,
    OutputSpec,
    Transition,
)
from multipolepdm.physics.detectors import DetectorDirection, DetectorGroup


def _transition(data):
    return Transition(**data)


def _geometry(data):
    values = dict(data)
    for name in (
        "ratio_group_a",
        "ratio_group_b",
        "polarization_group",
        "polarization_gate_group",
    ):
        group = values.get(name)
        if group is not None:
            if set(group) - {"directions", "normalization"}:
                raise ValueError(f"Unknown detector group fields in {name}.")
            values[name] = DetectorGroup(
                tuple(DetectorDirection(**row) for row in group["directions"]),
                normalization=group.get("normalization", "mean"),
            )
    return Geometry(**values)


def job_from_dict(data):
    allowed = {
        "mode",
        "label",
        "target",
        "gate",
        "target_first",
        "intermediates",
        "observations",
        "geometry",
        "grid",
        "output",
    }
    unknown = set(data) - allowed
    if unknown:
        raise ValueError(f"Unknown input fields: {', '.join(sorted(unknown))}")
    mode = data["mode"]
    ratio = "R_ADO" if mode == "P_ADO" else "R_DCO"
    observations = data["observations"]
    if set(observations) != {"P", ratio}:
        raise ValueError(f"{mode} requires observations P and {ratio}.")
    return JobRequest(
        mode=mode,
        target=_transition(data["target"]),
        polarization=Measurement(**observations["P"]),
        angular_ratio=Measurement(**observations[ratio]),
        label=str(data.get("label", "Transition")),
        gate=_transition(data["gate"]) if data.get("gate") is not None else None,
        target_first=data.get("target_first", True),
        intermediates=tuple(_transition(t) for t in data.get("intermediates", [])),
        geometry=_geometry(data.get("geometry", {})),
        grid=GridSpec(**data.get("grid", {})),
        output=OutputSpec(**data.get("output", {})),
    )


def job_to_dict(job):
    data = {
        "mode": job.mode,
        "label": job.label,
        "target": asdict(job.target),
        "observations": {
            "P": asdict(job.polarization),
            job.ratio_name: asdict(job.angular_ratio),
        },
        "geometry": asdict(job.geometry),
        "grid": asdict(job.grid),
        "output": asdict(job.output),
    }
    data["target"].pop("delta")
    if job.mode != "P_ADO":
        data.update(
            gate=asdict(job.gate),
            target_first=job.target_first,
            intermediates=[asdict(t) for t in job.intermediates],
        )
    return data


def load_jobs(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(data, dict) and set(data) == {"jobs"}:
        records = data["jobs"]
        if not isinstance(records, list) or not records:
            raise ValueError("Batch jobs must be a nonempty array.")
    else:
        records = [data]
    return tuple(job_from_dict(record) for record in records)


def save_input(job, path):
    Path(path).write_text(
        json.dumps(job_to_dict(job), indent=2, allow_nan=False) + "\n", encoding="utf-8"
    )


def example_data(mode="P_ADO"):
    name = {
        "P_ADO": "example.json",
        "P_DCO": "example_P_DCO.json",
        "PDCO": "example_PDCO.json",
        "batch": "example_batch.json",
    }[mode]
    return json.loads(
        resources.files("multipolepdm")
        .joinpath("examples", name)
        .read_text(encoding="utf-8")
    )


def export_example(mode, path):
    Path(path).write_text(
        json.dumps(example_data(mode), indent=2) + "\n", encoding="utf-8"
    )
