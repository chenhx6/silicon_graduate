#!/usr/bin/env python3
"""Exact angular-only E3 audit; radial integrals and effective charges omitted.

Conventions: normalized spherical harmonics, Condon--Shortley CG coefficients,
spin s=1/2. B_angular means B(E3)/(e_eff^2 |R_fi^(3)|^2); it is NOT a
physical transition strength or a collectivity/deformation estimate.

The rank and parity rules are Suhonen (2007), Eqs. (2.27)--(2.29),
(6.18), (6.23). Three independent constructions are compared: a spinor
CG/Gaunt sum, orbital-to-j 6j recoupling, and the spinor 3j square.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path

import sympy as sp
from sympy.physics.wigner import clebsch_gordan, gaunt, wigner_3j, wigner_6j

HALF = sp.Rational(1, 2)
RANK = 3
PAIRS = [
    ("p1/2", 1, 1, "g9/2", 4, 9, "withdrawn legacy A100 driver"),
    ("p3/2", 1, 3, "g9/2", 4, 9, "light-region angular candidate"),
    ("d5/2", 2, 5, "h11/2", 5, 11, "medium-region angular candidate"),
    ("f7/2", 3, 7, "i13/2", 6, 13, "rare-earth angular candidate"),
    ("g9/2", 4, 9, "j15/2", 7, 15, "heavy-region angular candidate"),
    ("p1/2", 1, 1, "d5/2", 2, 5, "allowed delta-l=1 counterexample"),
    ("d3/2", 2, 3, "f5/2", 3, 5, "allowed delta-j=1 counterexample"),
    ("p1/2", 1, 1, "p3/2", 1, 3, "parity and triangle negative control"),
    ("s1/2", 0, 1, "p1/2", 1, 1, "j-sum negative control"),
    ("s1/2", 0, 1, "f7/2", 3, 7, "allowed stretched counterexample"),
]


def spinor_element(lf, jf, mf, li, ji, mi):
    q = mf - mi
    if q != int(q) or abs(q) > RANK:
        return sp.S.Zero
    total = sp.S.Zero
    for sigma in (-HALF, HALF):
        mlf, mli = mf - sigma, mi - sigma
        if abs(mlf) > lf or abs(mli) > li:
            continue
        total += (
            clebsch_gordan(lf, HALF, jf, mlf, sigma, mf)
            * clebsch_gordan(li, HALF, ji, mli, sigma, mi)
            * sp.Integer(-1) ** mlf
            * gaunt(lf, RANK, li, -mlf, int(q), mli)
        )
    return sp.simplify(total)


def recoupled_square(lf, jf, li, ji):
    orbital_sq = (
        (2 * lf + 1) * (2 * li + 1) * (2 * RANK + 1)
        * wigner_3j(lf, RANK, li, 0, 0, 0) ** 2 / (4 * sp.pi)
    )
    try:
        recoupling = wigner_6j(lf, jf, HALF, ji, li, RANK)
    except ValueError:
        return sp.S.Zero
    return sp.simplify((2 * jf + 1) * (2 * ji + 1) * recoupling ** 2 * orbital_sq)


def spinor_3j_square(lf, jf, li, ji):
    parity_factor = sp.Rational(1 + (-1) ** (lf + li + RANK), 2)
    return sp.simplify(
        parity_factor * (2 * jf + 1) * (2 * ji + 1) * (2 * RANK + 1)
        * wigner_3j(jf, RANK, ji, -HALF, 0, HALF) ** 2 / (4 * sp.pi)
    )


def audit():
    rows, checks = [], []
    for initial, li, two_ji, final, lf, two_jf, purpose in PAIRS:
        ji, jf = sp.Rational(two_ji, 2), sp.Rational(two_jf, 2)
        by_m = []
        for two_mi in range(-two_ji, two_ji + 1, 2):
            mi = sp.Rational(two_mi, 2)
            strength = sum(
                (spinor_element(lf, jf, sp.Rational(two_mf, 2), li, ji, mi) ** 2
                 for two_mf in range(-two_jf, two_jf + 1, 2)),
                sp.S.Zero,
            )
            by_m.append(sp.simplify(strength))
        reduced_sq = sp.simplify((two_ji + 1) * by_m[0])
        sixj_sq = recoupled_square(lf, jf, li, ji)
        threej_sq = spinor_3j_square(lf, jf, li, ji)
        assert all(sp.simplify(x - by_m[0]) == 0 for x in by_m)
        assert sp.simplify(reduced_sq - sixj_sq) == 0
        assert sp.simplify(reduced_sq - threej_sq) == 0
        reverse = recoupled_square(li, ji, lf, jf)
        assert sp.simplify(reverse - reduced_sq) == 0
        parity_ok = (lf + li + RANK) % 2 == 0
        j_triangle_ok = abs(jf - ji) <= RANK <= jf + ji
        l_triangle_ok = abs(lf - li) <= RANK <= lf + li
        if not (parity_ok and j_triangle_ok and l_triangle_ok):
            assert reduced_sq == 0
        rows.append({
            "initial": initial, "final": final, "purpose": purpose,
            "delta_l": abs(lf - li), "delta_j": str(abs(jf - ji)),
            "parity_ok": parity_ok, "j_triangle_ok": bool(j_triangle_ok),
            "l_triangle_ok": bool(l_triangle_ok),
            "reduced_angular_squared": str(reduced_sq),
            "B_angular": str(by_m[0]), "B_angular_numeric": float(by_m[0]),
            "nonzero_angular": reduced_sq != 0,
        })
        checks.append({
            "pair": initial + "->" + final, "all_initial_m_checked": len(by_m),
            "isotropy": True, "gaunt_vs_6j": True, "gaunt_vs_3j": True,
            "reverse_reduced_magnitude": True, "selection_rules": True,
        })
    assert rows[0]["reduced_angular_squared"] == "0"
    assert rows[5]["nonzero_angular"] and rows[6]["nonzero_angular"]
    return {
        "schema": "octupole-angular-audit-v1",
        "sympy_version": sp.__version__, "rank": RANK,
        "units": "dimensionless angular factors; radial integral and charge factored out",
        "operator": "Y_3q, spin independent, normalized spherical harmonics",
        "claims_excluded": [
            "physical B(E3)", "radial overlap", "actual orbital occupancy",
            "many-body collectivity", "static octupole shape", "global novelty",
        ],
        "rows": rows, "checks": checks,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output = args.output.resolve()
    args.output.mkdir(parents=True, exist_ok=True)
    result = audit()
    result_path = args.output / "angular-results.json"
    result_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    csv_path = args.output / "angular-pairs.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(result["rows"][0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(result["rows"])
    script = Path(__file__).resolve()
    root = script.parents[2]
    sources = [
        root / "raw/books/From nucleons to nucleus concepts of microscopic .pdf",
    ]
    files = [script, *sources, result_path, csv_path]
    provenance = {
        "schema": "research-run-provenance-v1",
        "command": "python3 system/scripts/octupole_orbital_selection_audit.py --output " + str(args.output),
        "actual_interpreter": sys.executable,
        "actual_argv": sys.argv,
        "dependencies": {"sympy": sp.__version__, "python": sys.version.split()[0]},
        "reading_scope": "Suhonen printed pp.29-30,121-124,127-128; PDF44-45,136-139,142-143",
        "files": [{
            "path": str(p.relative_to(root)), "size": p.stat().st_size,
            "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
        } for p in files],
    }
    (args.output / "run-provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
    print(json.dumps({"pairs": len(result["rows"]), "checks_passed": True,
                      "initial_m_values_checked": sum(c["all_initial_m_checked"] for c in result["checks"])},
                     indent=2))


if __name__ == "__main__":
    main()
