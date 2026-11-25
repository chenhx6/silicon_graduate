"""Documentation metadata must not change the physical job or its calculation."""

import json
from copy import deepcopy
from dataclasses import replace
from math import atan, radians

import numpy as np
import pytest
from multipolepdm.cli import main
from multipolepdm.contracts import GridSpec, OutputSpec
from multipolepdm.grid import recommend_grid
from multipolepdm.io.input import (
    example_data,
    job_from_dict,
    job_to_dict,
    load_jobs,
    save_input,
)
from multipolepdm.jobs.workers import compute_job
from multipolepdm.models.registry import evaluate_response

MODES = ("P_ADO", "P_DCO", "PDCO")


@pytest.mark.parametrize("mode", MODES)
def test_help_does_not_change_physical_input_or_computation(mode):
    plain = example_data(mode)
    plain.pop("_help", None)
    documented = deepcopy(plain)
    documented["_help"] = {"mode": "explanatory text", "nested": {"delta": 999}}
    before = deepcopy(documented)
    a, b = job_from_dict(plain), job_from_dict(documented)
    assert a == b
    assert job_to_dict(a) == job_to_dict(b)
    assert documented == before
    grid = GridSpec(xi_points=41, sigma_points=21)
    result_a, summary_a = compute_job(replace(a, grid=grid))
    result_b, summary_b = compute_job(replace(b, grid=grid))
    for name in ("polarization", "angular_ratio", "valid"):
        np.testing.assert_array_equal(
            getattr(result_a.response, name), getattr(result_b.response, name)
        )
    np.testing.assert_array_equal(
        result_a.parameter_density, result_b.parameter_density
    )
    np.testing.assert_array_equal(
        summary_a.delta_pdf.density, summary_b.delta_pdf.density
    )


@pytest.mark.parametrize("mode", MODES)
def test_legacy_scalar_geometry_json_remains_loadable(tmp_path, mode):
    data = example_data(mode)
    data.pop("_help", None)
    data["geometry"] = {"theta_a_deg": 125, "theta_b_deg": 90, "theta_p_deg": 90}
    data["grid"] = {"xi_points": 41, "sigma_points": 21}
    path = tmp_path / "old.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    assert load_jobs(path) == (job_from_dict(data),)


@pytest.mark.parametrize(
    "path",
    [
        (),
        ("target",),
        ("gate",),
        ("observations", "P"),
        ("geometry",),
        ("grid",),
        ("output",),
        ("geometry", "ratio_group_a"),
        ("geometry", "ratio_group_a", "directions", 0),
    ],
)
@pytest.mark.parametrize("field", ["misspelled_computation", "_help"])
def test_unknown_fields_are_still_strict(path, field):
    data = example_data("PDCO")
    data.pop("_help", None)
    node = data
    for key in path:
        node = node[key]
    node[field] = {}
    if not path and field == "_help":
        assert job_from_dict(data)
    else:
        with pytest.raises((TypeError, ValueError)):
            job_from_dict(data)


@pytest.mark.parametrize("help_value", [None, "comment", [], 1, True])
def test_help_must_be_an_object(tmp_path, help_value):
    data = example_data()
    data["_help"] = help_value
    with pytest.raises(ValueError, match="_help.*object"):
        job_from_dict(data)
    path = tmp_path / "batch.json"
    path.write_text(json.dumps({"_help": help_value, "jobs": [example_data()]}))
    with pytest.raises(ValueError, match="_help.*object"):
        load_jobs(path)


@pytest.mark.parametrize("root_help", [False, True])
@pytest.mark.parametrize("job_help", [False, True])
def test_batch_help_at_root_and_each_job(tmp_path, root_help, job_help):
    data = example_data("batch")
    data.pop("_help", None)
    if root_help:
        data["_help"] = {"jobs": "Independent physical inputs"}
    for job in data["jobs"]:
        job.pop("_help", None)
        if job_help:
            job["_help"] = {"mode": job["mode"]}
    path = tmp_path / "batch.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    jobs = load_jobs(path)
    assert tuple(j.mode for j in jobs) == MODES
    assert jobs == tuple(job_from_dict(example_data(mode)) for mode in MODES)


@pytest.mark.parametrize("jobs", [[], {}, None, "jobs"])
def test_batch_requires_nonempty_array(tmp_path, jobs):
    path = tmp_path / "batch.json"
    path.write_text(json.dumps({"_help": {}, "jobs": jobs}))
    with pytest.raises(ValueError, match="nonempty array"):
        load_jobs(path)


def test_batch_unknown_root_and_task_fields_fail(tmp_path):
    data = example_data("batch")
    path = tmp_path / "batch.json"
    for node in (data, data["jobs"][0]):
        node["typo"] = 123
        path.write_text(json.dumps(data))
        with pytest.raises(ValueError, match="Unknown.*typo"):
            load_jobs(path)
        del node["typo"]


@pytest.mark.parametrize(
    "text",
    [
        '{"_help": {"number": NaN}, "jobs": []}',
        '{"_help": {"number": Infinity}, "jobs": []}',
        '{"_help": {"number": -Infinity}, "jobs": []}',
        '{"_help": {}, "jobs": [],}',
        '{/* comment */ "jobs": []}',
        '{"jobs": [], "jobs": []}',
    ],
)
def test_nonstandard_json_is_rejected(tmp_path, text):
    path = tmp_path / "bad.json"
    path.write_text(text)
    with pytest.raises(ValueError, match="Invalid JSON numeric|Expecting|Duplicate"):
        load_jobs(path)


@pytest.mark.parametrize("mode", MODES)
def test_gui_save_input_exports_help_and_roundtrips(tmp_path, mode):
    job = job_from_dict(example_data(mode))
    path = tmp_path / "gui-export.json"
    save_input(job, path)
    data = json.loads(path.read_text())
    assert isinstance(data["_help"], dict)
    assert "delta" not in data["target"]
    assert load_jobs(path) == (job,)
    assert "_help" not in job_to_dict(job)


@pytest.mark.parametrize("mode", MODES)
def test_real_gui_save_json_contains_help(qtbot, tmp_path, monkeypatch, mode):
    from multipolepdm.gui.window import MainWindow
    from PySide6.QtWidgets import QFileDialog

    window = MainWindow()
    qtbot.addWidget(window)
    window.mode.setCurrentText(mode)
    window.load_example()
    expected = window.read_job()
    path = tmp_path / "gui-input.json"
    monkeypatch.setattr(QFileDialog, "getSaveFileName", lambda *a: (str(path), "JSON"))
    window.save_json()
    assert isinstance(json.loads(path.read_text())["_help"], dict)
    assert load_jobs(path) == (expected,)
    window.close()


@pytest.mark.parametrize("mode", (*MODES, "batch"))
@pytest.mark.parametrize("include_help", [False, True])
def test_real_gui_imports_documented_or_plain_json(
    qtbot, tmp_path, monkeypatch, mode, include_help
):
    from multipolepdm.gui.window import MainWindow

    data = example_data(mode)
    if not include_help:
        data.pop("_help", None)
        for record in data.get("jobs", []):
            record.pop("_help", None)
    path = tmp_path / "input.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    window = MainWindow()
    qtbot.addWidget(window)
    window.file_mode.setChecked(True)
    window.file_path.setText(str(path))
    window.output_path.setText(str(tmp_path))
    # Inspect the real file-to-queue path before asynchronous submission.
    monkeypatch.setattr(window, "submit_pending", lambda: None)
    window.calculate()
    expected = tuple(
        replace(job, output=OutputSpec(str(tmp_path), False)) for job in load_jobs(path)
    )
    assert tuple(window.pending_jobs) == expected
    window.pending_jobs.clear()
    window.close()


@pytest.mark.parametrize("mode", (*MODES, "batch"))
def test_cli_export_example_includes_help(tmp_path, mode):
    path = tmp_path / "cli-export.json"
    assert main(["--example", mode, "--export-example", str(path)]) == 0
    data = json.loads(path.read_text())
    assert isinstance(data["_help"], dict)
    assert len(load_jobs(path)) == (3 if mode == "batch" else 1)


def test_cli_computes_documented_batch_example(tmp_path, monkeypatch):
    from multipolepdm import cli

    data = example_data("batch")
    for job in data["jobs"]:
        job["grid"] = {"xi_points": 41, "sigma_points": 21}
    monkeypatch.setattr(cli, "example_data", lambda mode: data)
    assert main(["--example", "batch", "--output-dir", str(tmp_path)]) == 0
    manifests = list(tmp_path.glob("*/manifest.json"))
    assert len(manifests) == 3
    for path in manifests:
        record = json.loads(path.read_text())
        assert record["status"] == "saved"
        assert "_help" not in record["input"]


@pytest.mark.parametrize("reference_spin", [5.0, 5.5])
@pytest.mark.parametrize("empty_grid", [False, True])
def test_omitted_or_empty_grid_uses_shared_recommendation(reference_spin, empty_grid):
    data = example_data()
    data.pop("grid")
    if empty_grid:
        data["grid"] = {}
    data["target"]["spin_initial"] = reference_spin
    data["target"]["spin_final"] = reference_spin - 1
    job = job_from_dict(data)
    assert job.grid == recommend_grid(reference_spin)


@pytest.mark.parametrize("empty_grid", [False, True])
def test_upstream_gate_is_common_source_for_recommended_grid(empty_grid):
    data = example_data("PDCO")
    data.pop("grid")
    if empty_grid:
        data["grid"] = {}
    data["target_first"] = False
    data["gate"]["spin_initial"] = 7
    data["gate"]["spin_final"] = 5
    job = job_from_dict(data)
    assert job.reference_spin == 7
    assert job.grid == recommend_grid(7)
    assert job.grid.sigma_step == pytest.approx(0.005 * 7)


def test_zero_spin_forward_input_does_not_request_a_sigma_scan():
    data = example_data()
    data.pop("grid")
    data["target"] = {"spin_initial": 0, "spin_final": 1, "multipoles": ["M1"]}
    job = job_from_dict(data)
    assert job.reference_spin == 0
    assert job.grid == GridSpec()


@pytest.mark.parametrize("mode", MODES)
def test_injection_label_is_not_a_computational_input(mode):
    job = job_from_dict(example_data(mode))
    other = replace(job, label="Synthetic delta=-999, sigma/I=999")
    xi, sigma = np.array([-0.5, 0.5]), np.array([0.5, 1.5])
    a, b = evaluate_response(job, xi, sigma), evaluate_response(other, xi, sigma)
    np.testing.assert_array_equal(a.polarization, b.polarization)
    np.testing.assert_array_equal(a.angular_ratio, b.angular_ratio)


def test_explicit_old_grid_and_display_units_do_not_reinterpret_numbers():
    data = example_data()
    data["grid"] = {
        "xi_min_rad": -1.2,
        "xi_max_rad": 1.3,
        "xi_points": 41,
        "sigma_min": 0.3,
        "sigma_max": 4.5,
        "sigma_points": 21,
        "xi_input_unit": "deg",
        "sigma_input_unit": "sigma/I",
    }
    a = job_from_dict(data)
    assert a.grid == GridSpec(**data["grid"])
    data["grid"].update(xi_input_unit="rad", sigma_input_unit="sigma")
    b = job_from_dict(data)
    for x, y in zip(a.grid.axes(a.reference_spin), b.grid.axes(b.reference_spin)):
        np.testing.assert_array_equal(x, y)


@pytest.mark.parametrize("mode", MODES)
def test_example_centers_are_formal_response_at_documented_injection(mode):
    data = example_data(mode)
    assert "delta" not in data["target"]
    assert data["target"]["spin_initial"] == 5
    assert data["target"]["spin_final"] == 4
    assert data["target"]["multipoles"] == ["M1", "E2"]
    geometry = data["geometry"]
    for name, theta in (
        ("ratio_group_a", 26),
        ("ratio_group_b", 90),
        ("polarization_group", 90),
    ):
        assert geometry[name]["directions"] == [{"theta_deg": theta, "weight": 1.0}]
    if mode != "P_ADO":
        assert data["gate"] == {
            "spin_initial": 4.0,
            "spin_final": 2.0,
            "multipoles": ["E2"],
            "delta": 0.0,
        }
        assert data["target_first"] is True
    if mode == "PDCO":
        assert geometry["polarization_gate_group"]["directions"] == [
            {"theta_deg": 90, "weight": 1.0}
        ]
    job = job_from_dict(data)
    response = evaluate_response(
        job, np.array([atan(0.5)]), np.array([0.30 * job.reference_spin])
    )
    assert response.valid[0, 0]
    p, r = response.polarization[0, 0], response.angular_ratio[0, 0]
    assert data["observations"]["P"]["value"] == pytest.approx(p, abs=1e-14)
    assert data["observations"][job.ratio_name]["value"] == pytest.approx(r, abs=1e-14)
    for name, err in (("P", max(0.1075, 0.8 * abs(p))), (job.ratio_name, 0.1 * abs(r))):
        assert data["observations"][name]["err_minus"] == pytest.approx(err)
        assert data["observations"][name]["err_plus"] == pytest.approx(err)
    assert job.grid.xi_min_rad == pytest.approx(-radians(89))
    assert job.grid.xi_max_rad == pytest.approx(radians(89))
    assert job.grid.sigma_min == 0.15
    assert job.grid.sigma_max == job.reference_spin
    assert job.grid == recommend_grid(job.reference_spin)
