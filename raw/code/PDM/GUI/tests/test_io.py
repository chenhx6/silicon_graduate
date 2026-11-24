from dataclasses import replace
import json

import numpy as np
import pytest

from multipolepdm.cli import forward_calibration
from multipolepdm.contracts import GridSpec, Transition
from multipolepdm.io.input import (
    example_data,
    export_example,
    job_from_dict,
    load_jobs,
    save_input,
)
from multipolepdm.io.export import export_result, load_result
from multipolepdm.jobs.workers import compute_job


@pytest.mark.parametrize("mode", ["P_ADO", "P_DCO", "PDCO"])
def test_json_and_result_roundtrip(tmp_path, mode):
    job = replace(
        job_from_dict(example_data(mode)), grid=GridSpec(xi_points=101, sigma_points=51)
    )
    path = tmp_path / "input.json"
    save_input(job, path)
    assert load_jobs(path) == (job,)
    result, summary = compute_job(job)
    export_result(result, summary, tmp_path / "result")
    restored = load_result(tmp_path / "result")
    assert restored.job == job
    np.testing.assert_array_equal(restored.parameter_density, result.parameter_density)
    assert (
        json.loads((tmp_path / "result/manifest.json").read_text())["status"] == "saved"
    )


def test_examples_outside_source_cwd(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    export_example("batch", "batch.json")
    jobs = load_jobs("batch.json")
    assert tuple(j.mode for j in jobs) == ("P_ADO", "P_DCO", "PDCO")


def test_no_unknown_observables():
    data = example_data()
    data["observations"]["R_DCO"] = data["observations"].pop("R_ADO")
    with pytest.raises(ValueError):
        job_from_dict(data)


def test_pure_e2_forward_not_fake_pdf(tmp_path):
    job = replace(
        job_from_dict(example_data()),
        target=Transition(4, 2, ("E2",)),
        grid=GridSpec(xi_points=11, sigma_points=31),
    )
    response = forward_calibration(job, tmp_path)
    assert response.polarization.shape == (31, 1)
    assert (tmp_path / "forward_calibration.csv").exists()
    with pytest.raises(ValueError, match="pure one-component"):
        compute_job(job)
