#!/usr/bin/env python3
"""Unobserved multipole transfer from exact CG-squared kernels.

All spin/projection arguments in the CG helper are doubled integers. This is
an independent finite-sum audit of Yamazaki's tensor transfer and printed rows,
not a fitted feeding model or a direction-selected coincidence response.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
from math import factorial as fact, sqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02"


@lru_cache(None)
def cg_squared(j1, j2, j, m1, m2, m):
    if (m1 + m2 != m or abs(m1) > j1 or abs(m2) > j2 or abs(m) > j
            or not abs(j1 - j2) <= j <= j1 + j2
            or any(n % 2 for n in [j1 + m1, j2 + m2, j + m, j1 + j2 + j])):
        return F(0)
    a, b, c = (j1 + j2 - j) // 2, (j1 - m1) // 2, (j2 + m2) // 2
    d, e = (j - j2 + m1) // 2, (j - j1 - m2) // 2
    pref = F((j + 1) * fact(a) * fact((j1 - j2 + j) // 2)
             * fact((-j1 + j2 + j) // 2), fact((j1 + j2 + j) // 2 + 1))
    for n in [(j1 + m1) // 2, (j1 - m1) // 2, (j2 + m2) // 2,
              (j2 - m2) // 2, (j + m) // 2, (j - m) // 2]:
        pref *= fact(n)
    total = sum((F((-1) ** z, fact(z) * fact(a - z) * fact(b - z)
                   * fact(c - z) * fact(d + z) * fact(e + z))
                 for z in range(max(0, -d, -e), min(a, b, c) + 1)), F(0))
    return pref * total * total


def kernel(ti, tf, multipole):
    return [[cg_squared(tf, 2 * multipole, ti, mf, mi - mf, mi)
             for mi in range(-ti, ti + 1, 2)] for mf in range(-tf, tf + 1, 2)]


def tensor(tj, rank):
    """Return exact rational m-weights and their common squared prefactor."""
    const = F((tj + 1) * (2 * rank + 1) * fact(tj - rank) * fact(rank) ** 4,
              fact(tj + rank + 1))
    values = []
    for tm in range(-tj, tj + 1, 2):
        jm, jp = (tj - tm) // 2, (tj + tm) // 2
        total = sum((F((-1) ** z, fact(z) * fact(tj - rank - z)
                       * fact(jm - z) ** 2 * fact(rank - jm + z) ** 2)
                     for z in range(max(0, jm - rank), min(tj - rank, jm) + 1)), F(0))
        values.append((-1) ** jm * fact(jm) * fact(jp) * total)
    return values, const


def transfer(ti, tf, multipole, rank):
    if rank > min(ti, tf):
        return dict(U=0.0, tensor_rank_absent=True, alpha_factor=None)
    k = kernel(ti, tf, multipole)
    vi, ci = tensor(ti, rank)
    vf, cf = tensor(tf, rank)
    ratios = set()
    for col, initial in enumerate(vi):
        propagated = sum((vf[row] * k[row][col] for row in range(tf + 1)), F(0))
        if initial:
            ratios.add(propagated / initial)
        else:
            assert propagated == 0
    assert len(ratios) == 1, "tensor eigenvalue must agree for every parent m"
    ratio = ratios.pop()
    u = float(ratio) * sqrt(float(cf / ci))
    bi, bf = float(vi[ti // 2]) * sqrt(float(ci)), float(vf[tf // 2]) * sqrt(float(cf))
    return dict(U=u, rational_eigenvalue=str(ratio), tensor_prefactor_squared=str(cf / ci),
                B_parent=bi, B_child=bf, alpha_factor=u * bi / bf if bf else None)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=RUN / "yamazaki1967-U-transfer-audit.json")
    args = parser.parse_args()
    data = json.loads((RUN / "yamazaki1967-U-table-input.json").read_text())
    proof = json.loads((RUN / "yamazaki1967-pdf-verification-working.json").read_text())
    checks = {}

    def check(name, value):
        checks[name] = bool(value)
        if not value:
            raise AssertionError(name)

    check("source_hash_unchanged", hashlib.sha256((ROOT / proof["path"]).read_bytes()).hexdigest() == data["source_sha256"])
    rows = []
    for row in data["table_U"]:
        ti, tf, l = int(2 * row["Ji"]), int(2 * row["Jf"]), row["L"]
        k = kernel(ti, tf, l)
        check(f"positive_normalized_kernel_{ti}_{tf}_{l}", all(x >= 0 for r in k for x in r) and all(sum(k[r][c] for r in range(tf + 1)) == 1 for c in range(ti + 1)))
        check(f"rank0_{ti}_{tf}_{l}", transfer(ti, tf, l, 0)["U"] == 1)
        results = {str(rank): transfer(ti, tf, l, rank) for rank in [2, 4]}
        check(f"printed_U2_U4_{ti}_{tf}_{l}", all(abs(results[str(rank)]["U"] - row[f"U{rank}"]) <= 0.00000501 for rank in [2, 4]))
        rows.append(row | {"computed": results})
    k22 = kernel(4, 4, 2)
    daughter = [r[2] for r in k22]
    check("negative_U2_with_positive_daughter", daughter == [F(2, 7), F(1, 14), F(2, 7), F(1, 14), F(2, 7)] and transfer(4, 4, 2, 2)["rational_eigenvalue"] == "-3/14")
    check("alpha_is_not_U_when_spins_differ", abs(transfer(4, 6, 1, 2)["U"] - transfer(4, 6, 1, 2)["alpha_factor"]) > 0.01)
    mixed = {}
    for delta in [-0.5, 0.5]:
        mixed[str(delta)] = (transfer(4, 4, 1, 2)["U"] + delta ** 2 * transfer(4, 4, 2, 2)["U"]) / (1 + delta ** 2)
    check("unobserved_mixed_U_even_in_delta", mixed["-0.5"] == mixed["0.5"])
    check("spin0_daughter_rank_absent", transfer(4, 0, 2, 2)["tensor_rank_absent"] and all(x == 1 for x in kernel(4, 0, 2)[0]))
    # Exact P2/P4 expansion coefficients from the printed complete-alignment row.
    a2, a4 = F(5, 7), F(-12, 7)
    for x in [F(0), F(1, 3), F(1)]:
        p2, p4 = (3*x*x-1)/2, (35*x**4-30*x*x+3)/8
        assert 1 + a2*p2 + a4*p4 == F(15, 2)*(1-x*x)*x*x
    check("radiation_rank4_survives_spin0_daughter", a4 != 0 and abs(float(a4) - data["radiation_2to0_pureE2_completealignment"]["A4max"]) < 0.00000501)
    partial = {str(rank): transfer(17, 13, 2, rank) for rank in [0, 2, 4]}
    parent = data["IO81_partial_feed"]
    for rank in [2, 4]:
        partial[str(rank)]["conditional_partial_child_tensor"] = partial[str(rank)]["U"] * parent[f"parent_rho{rank}"]
        partial[str(rank)]["scaled_parent_quoted_error_no_new_CI"] = abs(partial[str(rank)]["U"]) * parent["quoted_parent_errors"][(rank - 2) // 2]
    check("actual_branch_not_total_child_reconstruction", parent["actual_child_total_rho_not_inferred"] is True)
    output = dict(kind="source-defined unobserved radiative tensor transfer; not actual feeding fit", checks=checks,
                  check_count=len(checks), passed=all(checks.values()), source_rows=rows,
                  exact_M0_2to2_E2_daughter_probabilities=[str(x) for x in daughter],
                  negative_example_U2="-3/14", negative_example_U4="2/7", mixed_chosen_delta_control=mixed,
                  spin0_daughter_and_rank4_radiation=dict(A2max=str(a2), A4max=str(a4), W="15/2 sin(theta)^2 cos(theta)^2", child_higher_tensors=0),
                  IO81_271_partial_component=partial, actual_child_total_tensor=None, actual_covariance=None,
                  limitations=["no preceding-photon direction/polarization selection", "no actual partial intensity/sidefeeding/branch weights", "no claim of Poletti1965 original normalization or code replay", "no measured sigma/delta or detector response fit"])
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(dict(checks=len(checks), passed=output["passed"], table_rows=len(rows), negative_U2="-3/14", partial_IO81=partial, no_actual_child_fit=True)))


if __name__ == "__main__":
    main()
