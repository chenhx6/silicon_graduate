#!/usr/bin/env python3
"""Replay T08's exact finite angular-momentum controls for the A130 draft.

Requires SymPy (the recorded run uses 1.13.3).  No package installation, source
modification or real-nucleus fit is performed.  Wigner--Eckart convention:
<a ma|T_kq|b mb> = (-1)^(a-ma) (a k b; -ma q mb) <a||T_k||b>.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

import sympy
from sympy import S, simplify, sqrt
from sympy.physics.wigner import clebsch_gordan, wigner_3j, wigner_6j


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "outputs/l4/20261108-A130-invariant-angular-controls"


def projections(j):
    return [-j + n for n in range(int(2 * j) + 1)]


def we(a, ma, k, q, b, mb):
    return (-1) ** (a - ma) * wigner_3j(a, k, b, -ma, q, mb)


def direct2(s, r):
    total = S.Zero
    for mr in projections(r):
        for u in range(-2, 3):
            total += (
                clebsch_gordan(2, 2, 0, u, -u, 0)
                * we(s, s, 2, u, r, mr)
                * we(r, mr, 2, -u, s, s)
            )
    return simplify(total)


def direct3(s, r, t):
    total = S.Zero
    for mr in projections(r):
        for mt in projections(t):
            for u in range(-2, 3):
                for v in range(-2, 3):
                    k = u + v
                    if abs(k) > 2:
                        continue
                    total += (
                        clebsch_gordan(2, 2, 2, u, v, k)
                        * clebsch_gordan(2, 2, 0, k, -k, 0)
                        * we(s, s, 2, u, r, mr)
                        * we(r, mr, 2, v, t, mt)
                        * we(t, mt, 2, -k, s, s)
                    )
    return simplify(total)


def candidates(s):
    return [
        r for r in projections(s + 2)
        if r >= 0 and (2 * r) % 2 == (2 * s) % 2
        and abs(s - r) <= 2 <= s + r
    ]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    quadratic = []
    cubic = []
    for s in [S(0), S(1) / 2, S(1), S(3) / 2, S(2), S(5) / 2]:
        for r in candidates(s):
            coefficient = (-1) ** (s - r) / (sqrt(5) * (2 * s + 1))
            assert simplify(direct2(s, r) - coefficient) == 0, (s, r)
            positive = (
                (-1) ** (s + r) * wigner_6j(2, 2, 0, s, s, r)
                / sqrt(2 * s + 1)
            )
            assert simplify(positive - 1 / (sqrt(5) * (2 * s + 1))) == 0
            quadratic.append({
                "I": str(s), "Ir": str(r),
                "Rsr_Rrs_coefficient": str(coefficient),
                "absolute_square_coefficient": str(positive),
            })
            for t in candidates(s):
                if not abs(r - t) <= 2 <= r + t:
                    continue
                coefficient3 = (
                    (-1) ** (2 * s) * wigner_6j(2, 2, 2, s, r, t)
                    / (2 * s + 1)
                )
                assert simplify(direct3(s, r, t) - coefficient3) == 0
                cubic.append({
                    "I": str(s), "Ir": str(r), "It": str(t),
                    "Rsr_Rrt_Rts_coefficient": str(coefficient3),
                })
    assert len(quadratic) == 20 and len(cubic) == 61

    a, b = S(5) / 2, S(9) / 2
    va, vb, covariance = S(9) / 4, S(49) / 4, S(21) / 4
    linear_variance = simplify(
        vb / a**3 + S(9) / 4 * b**2 * va / a**5
        - 3 * b * covariance / a**4
    )
    assert linear_variance == S(121) / 6250
    zero_spin = direct3(S.Zero, S(2), S(2))
    assert zero_spin == S(1) / 5
    result = {
        "quadratic_channels": quadratic, "cubic_channels": cubic,
        "quadratic_channel_count": 20, "cubic_channel_count": 61,
        "I0_cubic_coefficient": str(zero_spin),
        "I0_frozen_draft_coefficient": str(1 / (5 * sqrt(5))),
        "I1_Ir1_positive_coefficient": str(1 / (3 * sqrt(5))),
        "positive_two_point_coordinate_model": {
            "Q": [1, 2], "probabilities": ["1/2", "1/2"],
            "gamma_degrees": [0, 0], "q2": str(a), "q3": str(b),
            "moment_ratio": str(simplify(b / a**S("3/2"))),
            "actual_cos3gamma_variance": "0",
            "linearized_variance": str(linear_variance),
        },
        "boundary": "Exact finite angular-channel and declared coordinate-model checks, not real nuclear data",
    }
    OUT.mkdir(parents=True, exist_ok=True)
    result_path = OUT / "controls.json"
    result_path.write_text(json.dumps(result, indent=2) + "\n")
    context = [
        "raw/writing/gpt/A130/review-inputs/G63-v1/section-1-2.md",
        "raw/papers/gpt/query/20261108-r3-bohr-1952/originals/bohr-1952-mfm26-14.pdf",
        "raw/papers/gpt/learning-daily/20261022-DAY20-be2-qt-deformation-systematics/cline-1986-nuclear-shapes-coulomb-excitation.pdf",
        "raw/papers/gpt/learning-daily/20261022-DAY20-be2-qt-deformation-systematics/poves-2020-limits-assigning-nuclear-shape.pdf",
        "raw/books/From nucleons to nucleus concepts of microscopic .pdf",
    ]
    provenance = {
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "producer": str(Path(__file__).relative_to(ROOT)),
        "producer_sha256": sha(Path(__file__)),
        "python": sys.version, "sympy": sympy.__version__,
        "context_inputs": [{"path": p, "sha256": sha(ROOT / p)} for p in context],
        "artifacts": [{
            "path": str(result_path.relative_to(ROOT)), "sha256": sha(result_path),
        }],
        "numeric_inputs": "Dimensionless spins I=0,1/2,1,3/2,2,5/2; rank-2 tensor; stated two-point model",
        "real_nucleus_calculation": False,
    }
    (OUT / "run-provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
    print(json.dumps({"quadratic_channels": 20, "cubic_channels": 61, "all_pass": True}))


if __name__ == "__main__":
    main()
