import json

import numpy as np
import pytest

from multipolepdm.gui.window import MainWindow
from multipolepdm.models.registry import evaluate_response


def test_real_gui_azimuth_options_reach_the_saved_physics_job(qtbot, tmp_path):
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    window.mode.setCurrentText("PDCO")
    window.load_example()
    window.select_azimuth.setChecked(False)
    for editor in window.group_editors.values():
        assert not editor.table.cellWidget(0, 1).isEnabled()
    window.grid_editor.recommended.setChecked(False)
    window.grid_editor.values["angle_step"].setValue(1.0)
    window.grid_editor.values["width_step"].setValue(0.025)
    window.output_path.setText(str(tmp_path))
    truth = evaluate_response(window.read_job(), np.array([0.6]), np.array([1.2]))
    window.fields["P_value"].setValue(float(truth.polarization[0, 0]))
    window.fields["ratio_value"].setValue(float(truth.angular_ratio[0, 0]))
    window.calculate_button.click()
    identifier = next(iter(window.manager.handles))
    qtbot.waitUntil(
        lambda: window.manager.handles[identifier].state == "saved", timeout=30000
    )
    qtbot.waitUntil(lambda: identifier in window.result_windows, timeout=30000)
    record = json.loads(
        (window.manager.handles[identifier].directory / "manifest.json").read_text()
    )
    assert record["input"]["geometry"]["select_azimuth"] is False
    assert record["input"]["geometry"]["ratio_group_a"]["directions"]
    for flag in ("ratio_azimuth_average", "polarization_gate_azimuth_average"):
        assert record["response_metadata"][flag] is True
    window.close()


def test_group_rows_units_and_input_roundtrip(qtbot):
    from multipolepdm.io.input import job_from_dict, job_to_dict

    window = MainWindow()
    qtbot.addWidget(window)
    window.select_azimuth.setChecked(True)
    editor = window.group_editors["ratio_group_a"]
    editor.add_row(133.6, 61, 2)
    assert editor.table.cellWidget(1, 1).isEnabled()
    job = window.read_job()
    assert job_from_dict(job_to_dict(job)) == job
    assert len(job.geometry.ratio_group_a.directions) == 2
    xi_before, sigma_before = job.grid.axes(job.reference_spin)
    window.grid_editor.angle_unit.setCurrentText("rad")
    window.grid_editor.width_unit.setCurrentText("sigma")
    changed = window.read_job()
    xi, sigma = changed.grid.axes(changed.reference_spin)
    np.testing.assert_allclose(xi, xi_before, atol=1e-7)
    np.testing.assert_allclose(sigma, sigma_before, atol=1e-7)
    window.close()


@pytest.mark.parametrize("ratio_selected,polar_selected", [(False, False), (True, False), (False, True), (True, True)])
def test_manual_pdco_independent_azimuth_selection(qtbot, ratio_selected, polar_selected):
    from dataclasses import replace

    from multipolepdm.io.input import job_from_dict, job_to_dict

    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    window.mode.setCurrentText("PDCO")
    window.load_example()
    assert not window.select_azimuth.isChecked()
    assert not window.select_polarization_azimuth.isChecked()
    window.select_azimuth.setChecked(ratio_selected)
    window.select_polarization_azimuth.setChecked(polar_selected)
    for name, editor in window.group_editors.items():
        expected = ratio_selected if name.startswith("ratio_") else polar_selected
        assert editor.table.cellWidget(0, 1).isEnabled() == expected
        row = editor.table.rowCount()
        editor.add_row(57, 43, 0.4)
        assert editor.table.cellWidget(row, 1).isEnabled() == expected
    job = window.read_job()
    assert job.geometry.select_azimuth == (ratio_selected or polar_selected)
    assert job.geometry.ratio_azimuth_average == (not ratio_selected)
    assert job.geometry.polarization_gate_azimuth_average == (not polar_selected)
    assert job_from_dict(job_to_dict(job)) == job
    axes = (np.array([0.15]), np.array([1.2]))
    response = evaluate_response(job, *axes)
    point_job = replace(job, geometry=replace(
        job.geometry, select_azimuth=True,
        ratio_azimuth_average=False, polarization_gate_azimuth_average=False,
    ))
    point = evaluate_response(point_job, *axes)
    ring = evaluate_response(replace(job, geometry=replace(job.geometry, select_azimuth=False)), *axes)
    np.testing.assert_allclose(response.angular_ratio, (point if ratio_selected else ring).angular_ratio, atol=1e-13)
    np.testing.assert_allclose(response.polarization, (point if polar_selected else ring).polarization, atol=1e-13)
    assert abs(float(point.angular_ratio[0, 0] - ring.angular_ratio[0, 0])) > 1e-4
    assert abs(float(point.polarization[0, 0] - ring.polarization[0, 0])) > 1e-4
    window.mode.setCurrentText("P_DCO")
    assert window.select_polarization_azimuth.isHidden()
    assert window.read_job().geometry.select_azimuth == ratio_selected
    assert window.group_editors["polarization_group"].table.cellWidget(0, 1).isEnabled() == ratio_selected
    window.close()
