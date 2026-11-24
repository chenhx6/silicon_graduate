from dataclasses import FrozenInstanceError

import pytest

from multipolepdm.contracts import GridSpec, JobRequest, Measurement, Transition


def test_triangle_not_delta_i_one_restriction():
    assert Transition(4, 2, ("E2",)).spin_final == 2
    assert Transition(4, 4).multipoles == ("M1", "E2")
    with pytest.raises(ValueError, match="forbidden"):
        Transition(4, 2)


def test_inputs_immutable_and_units_explicit():
    target = Transition(5, 4)
    with pytest.raises(FrozenInstanceError):
        target.spin_initial = 6
    xi, sigma = GridSpec(xi_points=9, sigma_points=5).axes(5)
    assert xi[0] == -1.56 and sigma[0] == 0.15 and sigma[-1] == 5
    assert GridSpec().axes(4.5)[1][0] == 0.2


def test_required_gate_and_reference_identity():
    obs = Measurement(0.4, 0.1, 0.2)
    with pytest.raises(ValueError, match="require a gate"):
        JobRequest("P_DCO", Transition(5, 4), obs, obs)
    job = JobRequest(
        "P_DCO",
        Transition(4, 3),
        obs,
        obs,
        gate=Transition(6, 4, ("E2",)),
        target_first=False,
    )
    assert job.reference_spin == 6


def test_invalid_grid_and_measurement():
    with pytest.raises(ValueError):
        GridSpec(xi_min_rad=-90).axes(5)
    with pytest.raises(ValueError):
        Measurement(0, -1, 1)
    with pytest.raises(ValueError):
        Transition(1.25, 0.5)


def test_accepted_roundoff_spin_is_canonicalized():
    from multipolepdm.physics.populations import substates

    transition = Transition(4.5 + 1e-12, 3.5)
    assert transition.spin_initial == 4.5
    assert len(substates(transition.spin_initial)) == 10
