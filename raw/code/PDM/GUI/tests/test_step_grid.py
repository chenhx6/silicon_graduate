import numpy as np
import pytest

from multipolepdm.grid import stepped_axis


def test_step_kept_and_short_last_cell():
    np.testing.assert_allclose(stepped_axis(0.03, 1, 0.3), [0.03, 0.33, 0.63, 0.93, 1])


def test_exact_multiple_no_roundoff_cell():
    axis = stepped_axis(-1.0, 1.0, 0.1)
    assert axis.size == 21
    assert axis[-1] == 1
    np.testing.assert_allclose(np.diff(axis), 0.1)


@pytest.mark.parametrize("step", [0, -1, float("nan"), float("inf"), 1e-30, 3])
def test_invalid_steps(step):
    with pytest.raises(ValueError):
        stepped_axis(0, 1, step)


def test_grid_spec_steps_override_counts_and_record_input_units():
    from multipolepdm.contracts import GridSpec

    grid = GridSpec(
        xi_min_rad=-1,
        xi_max_rad=1,
        xi_step_rad=0.3,
        sigma_min=0.15,
        sigma_max=5,
        sigma_step=0.5,
        xi_input_unit="deg",
        sigma_input_unit="sigma/I",
    )
    xi, sigma = grid.axes(5)
    assert len(xi) == 8
    assert sigma[0] == 0.15 and sigma[-1] == 5
    np.testing.assert_allclose(np.diff(xi)[:-1], 0.3)
    assert np.diff(xi)[-1] == pytest.approx(0.2)


def test_nonuniform_last_cell_derivative_and_mass():
    from scipy.integrate import trapezoid

    from multipolepdm.pdm.mapping import _differentiate

    x = stepped_axis(-1, 1, 0.3)
    np.testing.assert_allclose(_differentiate(x * x, x, 0), 2 * x, atol=2e-14)
    assert trapezoid(2 + x, x) == pytest.approx(4)
