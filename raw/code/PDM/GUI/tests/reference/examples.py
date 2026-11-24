"""Emit standalone point fixtures as JSON for comparison with another kernel."""

from dataclasses import asdict
from json import dumps
from math import pi, radians, tan

from .angular_correlation import Transition, dco_ratio, gaussian, joint, singles


def point_cases():
    e2_gate = Transition.pure(4, 2, "E", 2)
    for degrees in (-70, 70):
        first = Transition.mixed(5, 4, tan(radians(degrees)))
        yield (
            f"droste_{degrees:+d}",
            gaussian(5, 1.5),
            first,
            e2_gate,
            (),
            (pi / 2, 0),
            (pi / 2, 0),
        )
    for delta in (-0.7, 0.7):
        first = Transition.mixed(3.5, 2.5, delta)
        last = Transition.mixed(2.5, 1.5, -0.4)
        gap = Transition.mixed(2.5, 2.5, -0.8)
        p = gaussian(3.5, 1.4)
        yield (
            f"half_integer_{delta:+g}",
            p,
            first,
            last,
            (gap,),
            (1.18, 0.28),
            (1.83, 1.7),
        )
        yield f"adjacent_{delta:+g}", p, first, last, (), (0.89, 0.13), (1.18, 0.28)
    first = Transition.pure(0, 2, "E", 2)
    last = Transition.pure(2, 0, "E", 2)
    yield "zero_spin_pole", (1,), first, last, (), (0, 1.7), (1.45, 0.2)


def point_fixtures():
    for name, p, first, last, gap, a, b in point_cases():
        yield {
            "name": name,
            "populations_ascending_m": p,
            "first": asdict(first),
            "last": asdict(last),
            "between": [asdict(step) for step in gap],
            "first_direction_rad": a,
            "last_direction_rad": b,
            "joint_scaled": joint(p, first, last, a, b, between=gap),
            "target_first_scaled": asdict(
                joint(p, first, last, a, b, between=gap, target=1)
            ),
            "target_last_scaled": asdict(
                joint(p, first, last, a, b, between=gap, target=2)
            ),
            "first_single_scaled": asdict(singles(p, first, a[0])),
            "last_single_scaled": asdict(singles(p, last, b[0], before=(first, *gap))),
            "dco_target_first_at_0_vs_90": dco_ratio(
                p, first, last, 1, (0, 0), (pi / 2, 0), between=gap
            ),
        }


if __name__ == "__main__":
    print(dumps(list(point_fixtures()), indent=2, allow_nan=False))
