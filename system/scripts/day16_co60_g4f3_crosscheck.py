#!/usr/bin/env python3
"""Compare the explicit Geant4 F/F3 contraction with the helicity trace."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp
from sympy.physics.wigner import wigner_3j, wigner_6j, wigner_9j

from day16_co60_cascade_theory import coefficients, intermediate_population


def f_coefficient(k, ell, upper, jf, ji):
    return ((-1)**(ji+jf-1)
            *sp.sqrt((2*k+1)*(2*ji+1)*(2*ell+1)*(2*upper+1))
            *wigner_3j(ell, upper, k, 1, -1, 0)*wigner_6j(ell, upper, k, ji, ji, jf))


def f3_coefficient(k, k2, k1, ell, upper, jf, ji):
    return ((-1)**(upper+k2+k1+1)
            *sp.sqrt((2*ji+1)*(2*jf+1)*(2*ell+1)*(2*upper+1)*(2*k+1)*(2*k1+1)*(2*k2+1))
            *wigner_3j(ell, upper, k, 1, -1, 0)
            *wigner_9j(jf, ell, ji, jf, upper, ji, k2, k, k1))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.contract.read_text())
    source = Path(cfg["source"])
    assert hashlib.sha256(source.read_bytes()).hexdigest() == cfg["source_sha256"]
    rows = []
    for value in cfg["cases"]:
        delta = sp.Rational(str(value))
        def first(k):
            return sp.simplify(f3_coefficient(k, k, 0, 2, 2, 2, 4)
                               +2*delta*f3_coefficient(k, k, 0, 2, 3, 2, 4)
                               +delta*delta*f3_coefficient(k, k, 0, 3, 3, 2, 4))
        norm = first(0)
        exact = [sp.simplify((-1)**k*f_coefficient(k, 2, 2, 0, 2)*first(k)/norm) for k in [0, 2, 4]]
        trace = coefficients(intermediate_population(float(delta), True), 12)
        expected = [trace["a0_to_a4"][k] for k in [0, 2, 4]]
        error = max(abs(float(a)-b) for a, b in zip(exact, expected))
        rows.append({"delta_native": float(delta), "a0_a2_a4_exact": list(map(str, exact)),
                     "a0_a2_a4": list(map(float, exact)), "helicitytrace": expected,
                     "max_difference": error})
    result = {"source_formula": "G4 F/F3 and daughter update k1=0,n1=z",
              "contract_sha256": hashlib.sha256(args.contract.read_bytes()).hexdigest(),
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "rows": rows, "no_new_experimental_fit": True,
              "passed": all(r["max_difference"] < 1e-12 for r in rows)}
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
