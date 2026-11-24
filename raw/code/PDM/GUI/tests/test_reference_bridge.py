"""Production traces versus independently recoupled radiation coefficients."""

import numpy as np
import pytest

from multipolepdm.contracts import JobRequest, Measurement, Transition
from multipolepdm.physics.joint import joint_channels, single_channels
from multipolepdm.physics.propagation import deorientation_coefficient
from reference.angular_correlation import joint, singles, transfer
from reference.examples import point_cases


def convert(tr):
    parts = tr.components
    if len(parts) == 1:
        return Transition(tr.initial, tr.final, (parts[0].kind + str(parts[0].order),))
    return Transition(tr.initial, tr.final, delta=parts[1].weight / parts[0].weight)


@pytest.mark.parametrize("case", list(point_cases()), ids=lambda item: item[0])
def test_independent_joint_and_singles_in_both_orders(case):
    name, p, first, last, gap, a, b = case
    rho = np.diag(p)
    obs = Measurement(0, 0.1, 0.1)
    for target_first in (True, False):
        target, gate = (
            (convert(first), convert(last))
            if target_first
            else (convert(last), convert(first))
        )
        td, gd = (a, b) if target_first else (b, a)
        job = JobRequest(
            "PDCO",
            target,
            obs,
            obs,
            gate=gate,
            target_first=target_first,
            intermediates=tuple(convert(x) for x in gap),
        )
        xi = np.arctan(target.delta)
        actual = joint_channels(job, xi, rho, td, gd) * (4 * np.pi) ** 2
        expected = joint(
            p, first, last, a, b, between=gap, target=1 if target_first else 2
        )
        np.testing.assert_allclose(
            actual, [expected.parallel, expected.perpendicular], atol=3e-13, rtol=1e-12
        )
        marginal = (
            singles(p, first, a[0])
            if target_first
            else singles(p, last, b[0], before=(first, *gap))
        )
        np.testing.assert_allclose(
            single_channels(job, xi, rho, td) * 4 * np.pi,
            [marginal.parallel, marginal.perpendicular],
            atol=3e-13,
            rtol=1e-12,
        )
    for step in gap:
        for k in [0, 2, 4]:
            assert deorientation_coefficient(convert(step), k) == pytest.approx(
                transfer(step, k), abs=3e-13
            )
