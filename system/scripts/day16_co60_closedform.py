#!/usr/bin/env python3
"""Verify the pure E2 cascade polynomial and the invalid scalar averaging route."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import sympy as sp


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--joint", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    contract = json.loads(args.contract.read_text())
    assert contract["x_definition"] == "cosgamma_gamma_angle"
    x = sp.symbols("x", real=True)
    intensity = sp.Rational(5, 126)*(24+3*x*x+x**4)
    q_unnormalized = sp.Rational(5, 126)*(1-x*x)*(4-x*x)
    polarization = sp.factor(q_unnormalized/intensity)
    wrong = sp.simplify(sp.integrate(q_unnormalized, (x, -1, 1))/sp.integrate(intensity, (x, -1, 1)))
    joint = json.loads(args.joint.read_text())
    errors = []
    for row in joint["rows"]:
        if row["case"] != "pureE2first":
            continue
        cosine = math.cos(math.radians(row["gamma_gamma_angle_deg"]))
        errors += [abs(float(intensity.subs(x, cosine))-row["IQUV"][0]),
                   abs(float(q_unnormalized.subs(x, cosine))-row["IQUV"][1]),
                   abs(float(polarization.subs(x, cosine))-row["normalized_Stokes"][0])]
    assert max(errors) < 1e-12 and wrong == sp.Rational(19, 189)
    result = {"contract_sha256": sha(args.contract), "joint_result_sha256": sha(args.joint),
        "script_sha256": sha(Path(__file__)), "W_formula": str(intensity),
        "Q_J_unnormalized_formula": str(q_unnormalized), "P_parallel_formula": str(polarization),
        "max_error_all_pure_roles_and_angles": max(errors),
        "W_integral_dx": str(sp.integrate(intensity, (x, -1, 1))),
        "naive_local_P_event_weighted_average": str(wrong),
        "common_axes_ungated_reference_Stokes": joint["ungated_full_reference_solidangle_controls"][0]["normalized_Stokes"],
        "P90_exact": str(polarization.subs(x, 0)), "P60_exact": str(polarization.subs(x, sp.Rational(1, 2))),
        "scope": "Q_J is a photon density component; local scalar average is not the ungated lab observable",
        "experimental_Q_or_delta_fit": False}
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
