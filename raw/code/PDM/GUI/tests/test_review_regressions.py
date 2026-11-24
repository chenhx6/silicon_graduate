"""Concrete numerical regressions from the independent 0.1.1 review."""

from dataclasses import replace

import numpy as np
import pytest

from multipolepdm.contracts import Geometry, GridSpec
from multipolepdm.io.input import example_data, job_from_dict
from multipolepdm.models.registry import evaluate_response
from multipolepdm.pdm.mapping import map_density
from multipolepdm.physics.detectors import DetectorDirection, DetectorGroup


@pytest.mark.parametrize("mode", ["P_DCO", "PDCO"])
@pytest.mark.parametrize("rows", [1, 2])
def test_complementary_point_groups_are_exactly_degenerate(mode, rows):
    a = [DetectorDirection(49, 0, 2)]
    b = [DetectorDirection(131, 37, 3)]
    if rows == 2:
        a.append(DetectorDirection(49, 72, 1))
        b.append(DetectorDirection(131, -21, 1))
    job = replace(
        job_from_dict(example_data(mode)),
        grid=GridSpec(xi_min_rad=-1.4, xi_max_rad=1.4, xi_points=51, sigma_points=31),
        geometry=Geometry(
            ratio_group_a=DetectorGroup(tuple(a)),
            ratio_group_b=DetectorGroup(tuple(b)),
            polarization_group=DetectorGroup((DetectorDirection(75),)),
            polarization_gate_group=DetectorGroup((DetectorDirection(51, 88),)),
            select_azimuth=True,
        ),
    )
    response = evaluate_response(job)
    from multipolepdm.physics.joint import response_channels

    _, raw = response_channels(
        job, response.xi_rad, response.sigma, conditional=mode == "PDCO"
    )
    np.testing.assert_allclose(raw[0] / raw[1], 1, atol=1e-13, rtol=0)
    np.testing.assert_array_equal(response.angular_ratio, 1)
    with pytest.raises(ValueError, match="Jacobian is zero"):
        map_density(job, response)


def test_tiny_valid_width_unit_switch_does_not_clamp(qtbot):
    from multipolepdm.gui.editors import GridEditor

    editor = GridEditor()
    qtbot.addWidget(editor)
    editor.set_reference_spin(0.5)
    for key, value in zip(("min", "max", "step"), (1e-10, 1e-8, 1.5e-10)):
        editor.values[f"width_{key}"].setValue(value)
    before = editor.spec().axes(0.5)[1]
    editor.width_unit.setCurrentText("sigma")
    after = editor.spec().axes(0.5)[1]
    assert len(before) == len(after) == 67
    np.testing.assert_allclose(after, before, rtol=1e-12, atol=0)
    editor.width_unit.setCurrentText("sigma/I")
    np.testing.assert_allclose(editor.spec().axes(0.5)[1], before, rtol=1e-12, atol=0)


def test_complementary_point_identity_in_independent_9j_reference():
    from reference import angular_correlation as ref

    population = ref.gaussian(5, 1.5)
    gate = ref.Transition.pure(4, 2, "E", 2)
    for delta in (-1, 0.1, 5):
        target = ref.Transition.mixed(5, 4, delta)
        ratio = ref.dco_ratio(
            population,
            target,
            gate,
            1,
            (np.deg2rad(49), 0),
            (np.deg2rad(131), np.deg2rad(37)),
        )
        assert ratio == pytest.approx(1, abs=1e-13)


def test_width_units_remain_consistent_after_temporary_zero_spin(qtbot):
    from multipolepdm.gui.editors import GridEditor

    editor = GridEditor()
    qtbot.addWidget(editor)
    editor.set_reference_spin(0)
    editor.width_unit.setCurrentText("sigma")
    editor.set_reference_spin(5, reset_bounds=True)
    before = editor.spec().axes(5)[1]
    editor.width_unit.setCurrentText("sigma/I")
    np.testing.assert_allclose(editor.spec().axes(5)[1], before, rtol=1e-12, atol=0)


def test_unit_limits_do_not_compound_when_source_spin_changes(qtbot):
    from multipolepdm.gui.editors import GridEditor

    editor = GridEditor()
    qtbot.addWidget(editor)
    for _ in range(6):
        editor.set_reference_spin(2, reset_bounds=True)
        editor.width_unit.setCurrentText("sigma")
        editor.set_reference_spin(40, reset_bounds=True)
        editor.width_unit.setCurrentText("sigma/I")
        assert editor.values["width_max"].maximum() >= 1e4
    editor.set_reference_spin(2, reset_bounds=True)
    grid = editor.spec()
    assert grid.sigma_min == pytest.approx(0.15)
    assert grid.sigma_max == pytest.approx(2)
