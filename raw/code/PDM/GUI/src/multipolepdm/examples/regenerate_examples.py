"""Regenerate packaged observations with the production response evaluator.

Run from the GUI project with PYTHONPATH=src python
src/multipolepdm/examples/regenerate_examples.py. No random noise is added.
"""

import json
from dataclasses import asdict
from math import atan
from pathlib import Path

import numpy as np

from multipolepdm.grid import recommend_grid
from multipolepdm.io.input import input_help, job_from_dict
from multipolepdm.models.registry import evaluate_response


def make_example(mode):
    def group(theta):
        return {
            "directions": [{"theta_deg": theta, "weight": 1.0}],
            "normalization": "mean",
        }

    grid = asdict(recommend_grid(5))
    # Step-defined scans need no legacy point-count hints.
    grid.pop("xi_points")
    grid.pop("sigma_points")
    ratio_name = "R_ADO" if mode == "P_ADO" else "R_DCO"
    data = {
        "_help": input_help(mode),
        "mode": mode,
        "label": f"Synthetic {mode}: delta=0.5, sigma/I=0.3",
        "target": {"spin_initial": 5.0, "spin_final": 4.0, "multipoles": ["M1", "E2"]},
        "observations": {
            "P": {"value": 0.0, "err_minus": 0.1075, "err_plus": 0.1075},
            ratio_name: {"value": 1.0, "err_minus": 0.1, "err_plus": 0.1},
        },
        "geometry": {
            "select_azimuth": False,
            "ratio_group_a": group(26),
            "ratio_group_b": group(90),
            "polarization_group": group(90),
        },
        "grid": grid,
        "output": {"directory": "pdm-results", "full_csv": False},
    }
    if mode != "P_ADO":
        data.update(
            gate={
                "spin_initial": 4.0,
                "spin_final": 2.0,
                "multipoles": ["E2"],
                "delta": 0.0,
            },
            target_first=True,
            intermediates=[],
        )
    if mode == "PDCO":
        data["geometry"]["polarization_gate_group"] = group(90)
    job = job_from_dict(data)
    response = evaluate_response(
        job, np.array([atan(0.5)]), np.array([0.30 * job.reference_spin])
    )
    if not response.valid[0, 0]:
        raise ValueError(f"Undefined injected response for {mode}")
    p, r = float(response.polarization[0, 0]), float(response.angular_ratio[0, 0])
    for name, value, err in (
        ("P", p, max(0.1075, 0.8 * abs(p))),
        (ratio_name, r, 0.1 * abs(r)),
    ):
        data["observations"][name] = {
            "value": value,
            "err_minus": err,
            "err_plus": err,
        }
    return data


def main():
    directory = Path(__file__).resolve().parent
    names = {
        "P_ADO": "example.json",
        "P_DCO": "example_P_DCO.json",
        "PDCO": "example_PDCO.json",
    }
    jobs = [make_example(mode) for mode in names]
    batch = {
        "_help": {
            "format": "严格 JSON。根层仅 jobs 与可选 _help 对象；每个任务也可有顶层 _help 对象。说明完全不参与计算，其它未知字段报错。",
            "jobs": "非空独立任务数组；每项使用自己的 mode、目标、门、观测、几何及网格，不能从批量根层继承计算参数。",
        },
        "jobs": jobs,
    }
    for name, data in [*zip(names.values(), jobs), ("example_batch.json", batch)]:
        (directory / name).write_text(
            json.dumps(data, indent=2, ensure_ascii=False, allow_nan=False) + "\n",
            encoding="utf-8",
        )
    for job in jobs:
        print(job["mode"], json.dumps(job["observations"], allow_nan=False))


if __name__ == "__main__":
    main()
