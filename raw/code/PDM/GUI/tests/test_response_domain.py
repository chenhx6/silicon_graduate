import numpy as np
import pytest

from multipolepdm.io.input import example_data, job_from_dict
from multipolepdm.models.registry import evaluate_response


@pytest.mark.parametrize(
    "perp,ratio,expected_valid",
    [(-1e-5, 1, False), (0.5, -0.1, False), (-1e-15, 1, True), (0.5, -1e-15, True)],
)
def test_unphysical_theoretical_values_are_not_used_as_density_inputs(
    monkeypatch, perp, ratio, expected_valid
):
    import multipolepdm.physics.joint as joint

    def channels(*args, **kwargs):
        p = np.array([[[1.0]], [[perp]]])
        r = np.array([[[ratio]], [[1.0]]])
        return p, r

    monkeypatch.setattr(joint, "response_channels", channels)
    result = evaluate_response(
        job_from_dict(example_data()), np.array([0.0]), np.array([1.0])
    )
    assert bool(result.valid[0, 0]) is expected_valid
    if expected_valid:
        assert abs(result.polarization[0, 0]) <= 1
        assert result.angular_ratio[0, 0] >= 0
    else:
        assert np.isnan(result.polarization[0, 0])
        assert np.isnan(result.angular_ratio[0, 0])
