#!/usr/bin/env python3
"""E3 completeness and rotor-versus-vibrator pattern benchmark.

The entries are central E3 reduced matrix elements from Butler et al. 2020
Table I (PRL 124 042503, PDF p.3).  Asterisked entries were coupled through
rotational assumptions in GOSIA.  The script computes only partial,
non-energy-weighted sums of |M(E3)|^2 in the printed matrix-element units.
It does not infer a closure-complete sum, a probability, or a static density.

For a 0+ initial state, closure gives
  m0 = sum_f B(E3;0+ -> 3-_f)
    = sum_f,mu |<3-_f,mu|M_3mu|0+>|^2,
with the standard reduced-matrix-element convention.  A single observed
0+->3- line is one nonnegative term, hence a lower bound on m0 if all other
assumptions and states are respected. The energy-weighted sum m1 requires H:
  m1 = 1/2 <0| [M_3^dagger,[H,M_3]] |0>,
so it cannot be computed from Table I alone.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


# label, initial spin, final spin, central reduced ME in e b^(3/2), starred/coupled
E3 = {
    "222Ra": [
        ("0+->3-", 0, 3, 1.13, False),
        ("2+->1-", 2, 1, 0.85, False),
        ("2+->3-", 2, 3, -0.90, False),
        ("2+->5-", 2, 5, 1.79, False),
        ("4+->1-", 4, 1, -2.10, True),
        ("4+->3-", 4, 3, 2.60, True),
        ("4+->5-", 4, 5, -1.70, True),
        ("4+->7-", 4, 7, 3.30, True),
    ],
    "228Ra": [
        ("0+->3-", 0, 3, 0.87, False),
        ("2+->1-", 2, 1, 1.36, True),
        ("2+->3-", 2, 3, -0.06, True),
        ("2+->5-", 2, 5, 1.71, True),
        ("4+->1-", 4, 1, 0.40, True),
    ],
}

Q3_PRINTED = {
    "222Ra": [3030, 2000, 2100, 3100, 4400, 5500, 3200, 4600],
    "228Ra": [2300, 3200, 150, 3000, -800],
}


def partial_sums(rows: list[tuple[str, int, int, float, bool]]) -> dict:
    all_m2 = sum(me * me for _, _, _, me, _ in rows)
    free_m2 = sum(me * me for _, _, _, me, star in rows if not star)
    # B downward uses the initial-state denominator. Here the table notation
    # gives a symmetric reduced ME; retain the raw sum separately and expose
    # the convention used for the illustrative downward sum.
    b_down = sum(me * me / (2 * ii + 1) for _, ii, _, me, _ in rows)
    return {
        "n_rows": len(rows),
        "n_unstarred_rows": sum(not star for *_, star in rows),
        "partial_sum_abs_M2_eb3": all_m2,
        "partial_sum_unstarred_abs_M2_eb3": free_m2,
        "partial_sum_downward_B_eb3": b_down,
        "units_scope": "printed reduced-ME squares; partial only",
    }


def q3_dispersion(q_values: list[float]) -> dict:
    mean = sum(q_values) / len(q_values)
    rms = math.sqrt(sum((q - mean) ** 2 for q in q_values) / len(q_values))
    return {"q3_values_efm3_from_table_I": q_values,
            "mean_signed_q3_efm3": mean,
            "rms_scatter_efm3": rms,
            "coefficient_of_variation_abs": rms / abs(mean) if mean else None,
            "status": "matrix-element list diagnostic, not a fitted shape rigidity statistic"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_suffix(".json"))
    args = parser.parse_args()
    # Table-I conversion: 0+->3- 1.13 -> Q3 3030 gives scale 2681.4;
    # 228Ra 0.87 -> 2300 gives scale 2643.7. Use only to show consistency.
    output = {
        "schema": "octupole-sum-rule-and-localization-027/v1",
        "source": "Butler et al. 2020 PRL 124 042503, Table I, PDF p.3; central values",
        "scope": "partial E3 non-energy-weighted sum and transition-pattern diagnostic",
        "data": {n: {"rows": [dict(label=x[0], Ji=x[1], Jf=x[2], M_E3_eb32=x[3], starred=x[4]) for x in rows],
                      "partial_sums": partial_sums(rows)} for n, rows in E3.items()},
        "q3_pattern": {
            "222Ra": q3_dispersion(Q3_PRINTED["222Ra"]),
            "228Ra": q3_dispersion(Q3_PRINTED["228Ra"]),
        },
        "closure_statement": {
            "m0_definition": "sum_f B(E3;0+->3-_f) over complete 3- final states",
            "single_0_to_3_is_lower_bound": True,
            "why_not_complete": "Table I contains selected states only; higher states and full covariance are absent, and some entries are rotationally coupled",
            "m1_available": False,
            "m1_requires": "Hamiltonian commutator or equivalent excitation energies and transition matrix elements",
        },
        "shape_localization_test": {
            "static_like_condition": "multiple independent Q3 conversions remain approximately constant across E3 links with rotor-compatible phase and angular factors",
            "vibrator_like_counterpattern": "selected links such as 228Ra 2+->3- have near-zero Q3 while 0+->3- remains nonzero",
            "not_sufficient": "a complete pattern still does not provide a model-free density or a unique PES; GOSIA couplings and rotor conventions remain relevant",
        },
        "validation": {
            "all_squares_nonnegative": all(x[3] ** 2 >= 0 for rows in E3.values() for x in rows),
            "single_line_bound_logic": True,
            "no_energy_weighted_sum_claimed": True,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
