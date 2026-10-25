#!/usr/bin/env python3
"""Exact rational vector controls for a classical two-blade model; no nuclear fit."""
import argparse
import json
from pathlib import Path
from fractions import Fraction as F


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def perpendicular(p, n, gp, gn):
    i = tuple(x+y for x, y in zip(p, n))
    mu = tuple(gp*x+gn*y for x, y in zip(p, n))
    i2 = dot(i, i)
    if not i2:
        raise ValueError("I=0 has no transverse projection axis")
    return dot(mu, mu)-F(dot(mu, i)**2, i2)


def derive():
    # Chosen Cartesian controls have no association with nuclear states.
    p, n, gp, gn = (2, 3, 5), (7, -1, 4), F(3, 2), F(-3, 7)
    i = tuple(x+y for x, y in zip(p, n))
    crosspn = cross(p, n)
    transverse = perpendicular(p, n, gp, gn)
    expected = (gp-gn)**2*F(dot(crosspn, crosspn), dot(i, i))
    # Equal blades with cos(chi)=0: theta_pi=theta_nu=chi/2.
    peq, neq = (1, 0, 1), (-1, 0, 1)
    equal_blades = perpendicular(peq, neq, gp, gn)
    scale = F(5, 3)
    controls = {
        "vector_projection_identity": transverse == expected,
        "equal_blades_half_angle_identity": equal_blades == (gp-gn)**2*F(dot(peq, peq), 2),
        "parallel_blades_zero_transverse": perpendicular(p, tuple(2*x for x in p), gp, gn) == 0,
        "identical_g_zero_transverse": perpendicular(p, n, gp, gp) == 0,
        "blade_exchange_invariance": perpendicular(n, p, gn, gp) == transverse,
        "angular_momentum_scaling_square": perpendicular(
            tuple(scale*x for x in p), tuple(scale*x for x in n), gp, gn) == scale**2*transverse,
    }
    return {
        "scope": "Classical fixed-length two blades, I=jp+jn, R=0, mu/mu_N=gp*jp+gn*jn, I^2>0. B(M1)=3/(8*pi)*mu_perp^2 is a semiclassical transition estimate.",
        "source": "knowledge/sources/clark-2000-shears-mechanism.md",
        "locator": "CL00-D23-001",
        "formula": "mu_perp^2=(gp-gn)^2*jp^2*jn^2*sin(chi)^2/I^2",
        "equal_blades_formula": "mu_perp^2=(gp-gn)^2*j^2*sin(chi/2)^2",
        "chosen_control": {"p": p, "n": n, "gp": str(gp), "gn": str(gn),
                           "mu_perp_squared": str(transverse)},
        "projection_identity_control_residual": str(transverse-expected),
        "controls": controls, "all_controls_pass": all(controls.values()),
        "boundaries": [
            "chi is the full blade angle; equal blades have theta_pi=theta_nu=chi/2.",
            "Neither chi nor theta_pi is automatically the TAC angle to a density principal axis.",
            "No measured nuclear angle, strength, lifetime, mixing ratio or confidence interval inferred.",
            "Finite-j quantum prescription using sqrt(j(j+1)) is separate from these classical vectors.",
            "The R=0 formula cannot infer blade closure when changing core rotation supplies the spin.",
            "I=0 is outside the transverse-projection domain; no zero-over-zero limit assigned.",
        ],
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    x = derive()
    args.output.write_text(json.dumps(x, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"all_controls_pass": x["all_controls_pass"],
                      "projection_identity_control_residual": x["projection_identity_control_residual"]}))
    return 0 if x["all_controls_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
