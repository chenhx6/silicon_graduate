"""Recommended/manual grids preserve physical coordinates and legacy inputs."""

from dataclasses import replace
from math import radians

import numpy as np
import pytest
from multipolepdm.contracts import GridSpec
from multipolepdm.grid import recommend_grid
from multipolepdm.gui.editors import GridEditor
from multipolepdm.gui.window import MainWindow
from multipolepdm.io.input import (
    example_data,
    job_from_dict,
    job_to_dict,
    load_jobs,
    save_input,
)


def assert_axes_equal(actual, expected, spin):
    for a, b in zip(actual.axes(spin), expected.axes(spin)):
        np.testing.assert_array_equal(a, b)


@pytest.mark.parametrize("spin,lower", [(1, 0.15), (5, 0.15), (0.5, 0.20), (6.5, 0.20)])
def test_shared_recommendation(spin, lower):
    spec = recommend_grid(spin)
    assert spec.xi_min_rad == radians(-89)
    assert spec.xi_max_rad == radians(89)
    assert spec.xi_step_rad == radians(0.1)
    assert spec.sigma_min == lower
    assert spec.sigma_max == spin
    assert spec.sigma_step == 0.005 * spin
    xi, sigma = spec.axes(spin)
    assert len(xi) == 1781
    assert sigma[0] == lower and sigma[-1] == spin


@pytest.mark.parametrize("spin", [0, -1, 0.3, float("nan"), float("inf")])
def test_shared_recommendation_rejects_invalid_source_spin(spin):
    with pytest.raises(ValueError):
        recommend_grid(spin)


def test_recommended_lock_unlock_and_reset(qtbot):
    editor = GridEditor()
    qtbot.addWidget(editor)
    editor.set_reference_spin(5)
    assert editor.recommended.isChecked()
    assert all(not box.isEnabled() for box in editor.values.values())
    assert editor.angle_unit.isEnabled() and editor.width_unit.isEnabled()
    assert_axes_equal(editor.spec(), recommend_grid(5), 5)
    editor.recommended.setChecked(False)
    assert all(box.isEnabled() for box in editor.values.values())
    assert all(word in editor.hint.text() for word in ("coverage", "precision", "runtime", "replace"))
    editor.values["angle_min"].setValue(-70)
    editor.values["angle_step"].setValue(0.5)
    editor.values["width_min"].setValue(0.1)
    editor.values["width_max"].setValue(0.8)
    editor.values["width_step"].setValue(0.01)
    assert editor.spec().sigma_min == 0.5
    editor.recommended.setChecked(True)
    assert_axes_equal(editor.spec(), recommend_grid(5), 5)
    assert all(not box.isEnabled() for box in editor.values.values())


@pytest.mark.parametrize("manual", [False, True])
def test_unit_switches_only_change_representation(qtbot, manual):
    editor = GridEditor()
    qtbot.addWidget(editor)
    editor.set_reference_spin(6.5)
    editor.recommended.setChecked(not manual)
    if manual:
        editor.values["width_min"].setValue(0.08)
        editor.values["angle_step"].setValue(0.7)
    before = editor.spec()
    for _ in range(10):
        for angle, width in (("rad", "sigma"), ("deg", "sigma/I")):
            editor.angle_unit.setCurrentText(angle)
            editor.width_unit.setCurrentText(width)
            after = editor.spec()
            assert after.xi_input_unit == angle and after.sigma_input_unit == width
            assert_axes_equal(after, before, 6.5)
    editor.width_unit.setCurrentText("sigma")
    assert editor.values["width_min"].value() == before.sigma_min
    assert editor.values["width_max"].value() == 6.5


@pytest.mark.parametrize("unit", ["sigma", "sigma/I"])
def test_recommended_source_spin_change_updates_absolute_sigma(qtbot, unit):
    editor = GridEditor()
    qtbot.addWidget(editor)
    editor.width_unit.setCurrentText(unit)
    for spin in (5, 6.5, 2, 0.5):
        editor.set_reference_spin(spin)
        assert_axes_equal(editor.spec(), recommend_grid(spin), spin)
        scale = spin if unit == "sigma/I" else 1
        assert editor.values["width_min"].value() == pytest.approx(editor.spec().sigma_min / scale)
        assert editor.values["width_max"].value() == pytest.approx(spin / scale)
        assert editor.values["width_step"].value() == pytest.approx(0.005 * spin / scale)


def test_manual_source_spin_change_preserves_absolute_sigma(qtbot):
    editor = GridEditor()
    qtbot.addWidget(editor)
    editor.set_reference_spin(5)
    editor.recommended.setChecked(False)
    before = editor.spec()
    editor.set_reference_spin(6.5, reset_bounds=True)
    assert editor.spec() == before
    assert editor.values["width_max"].value() == pytest.approx(5 / 6.5)
    editor.width_unit.setCurrentText("sigma")
    assert editor.values["width_max"].value() == 5
    editor.recommended.setChecked(True)
    assert_axes_equal(editor.spec(), recommend_grid(6.5), 6.5)


@pytest.mark.parametrize("mode", ["P_ADO", "P_DCO", "PDCO"])
def test_window_starts_recommended_and_tracks_actual_source(qtbot, mode):
    window = MainWindow()
    qtbot.addWidget(window)
    window.mode.setCurrentText(mode)
    window.load_example()
    assert window.grid_editor.recommended.isChecked()
    window.fields["target_initial"].setValue(6.5)
    assert window.grid_editor.reference_spin == 6.5
    assert_axes_equal(window.grid_editor.spec(), recommend_grid(6.5), 6.5)
    window.fields["gate_initial"].setValue(8)
    window.target_first.setCurrentIndex(1)
    reference = 6.5 if mode == "P_ADO" else 8
    assert window.grid_editor.reference_spin == reference
    assert_axes_equal(window.grid_editor.spec(), recommend_grid(reference), reference)
    window.mode.setCurrentText("P_ADO")
    assert window.grid_editor.reference_spin == 6.5
    window.close()


@pytest.mark.parametrize("grid", [
    GridSpec(xi_min_rad=-1, xi_max_rad=1, xi_points=13, sigma_points=9),
    GridSpec(xi_min_rad=-1.569, xi_max_rad=1.569, xi_step_rad=0.013,
             sigma_min=0.13, sigma_max=4.7, sigma_step=0.07,
             xi_input_unit="deg", sigma_input_unit="sigma/I"),
])
def test_legacy_json_import_stays_manual_and_roundtrips(qtbot, tmp_path, grid):
    data = example_data("P_ADO")
    # Build an old payload without any new recommendation marker.
    data["grid"] = {key: value for key, value in job_to_dict(
        replace(job_from_dict(data), grid=grid))["grid"].items() if value is not None}
    job = job_from_dict(data)
    editor = GridEditor()
    qtbot.addWidget(editor)
    editor.load_spec(job.grid, job.reference_spin)
    assert not editor.recommended.isChecked()
    assert all(box.isEnabled() for box in editor.values.values())
    assert editor.spec() == job.grid
    editor.angle_unit.setCurrentText("rad")
    editor.width_unit.setCurrentText("sigma")
    assert_axes_equal(editor.spec(), job.grid, job.reference_spin)
    path = tmp_path / "legacy-roundtrip.json"
    save_input(replace(job, grid=editor.spec()), path)
    restored = load_jobs(path)[0]
    assert restored.grid == editor.spec()
    assert_axes_equal(restored.grid, grid, job.reference_spin)
    editor.load_spec(restored.grid, restored.reference_spin)
    assert not editor.recommended.isChecked()
    editor.recommended.setChecked(True)
    assert_axes_equal(editor.spec(), recommend_grid(job.reference_spin), job.reference_spin)


def test_recommended_gui_json_roundtrip(qtbot, tmp_path):
    window = MainWindow()
    qtbot.addWidget(window)
    before = window.read_job()
    path = tmp_path / "recommended.json"
    save_input(before, path)
    restored = load_jobs(path)[0]
    assert restored == before
    window.grid_editor.load_spec(restored.grid, restored.reference_spin)
    assert window.grid_editor.recommended.isChecked()
    assert window.read_job() == before
    window.close()


def test_equivalent_count_grid_retains_original_contract(qtbot):
    spec = replace(recommend_grid(5), xi_step_rad=None, sigma_step=None,
                   xi_points=1781, sigma_points=195)
    editor = GridEditor()
    qtbot.addWidget(editor)
    editor.load_spec(spec, 5)
    assert editor.recommended.isChecked()
    assert editor.spec() == spec


def test_zero_spin_is_an_editable_state_with_clear_error(qtbot):
    editor = GridEditor()
    qtbot.addWidget(editor)
    editor.set_reference_spin(0)
    assert "I_ref=0" in editor.hint.text()
    with pytest.raises(ValueError, match="I_ref=0"):
        editor.spec()
    editor.set_reference_spin(0.5)
    assert_axes_equal(editor.spec(), recommend_grid(0.5), 0.5)
