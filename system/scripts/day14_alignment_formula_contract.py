#!/usr/bin/env python3
"""Finite-J and Gaussian-parameter checks of explicitly transcribed formulas.

This compares printed polynomials with source-defined CG statistical tensors.
It does not establish the author's code, textbook approximation context or
experimental sigma/delta, nor fit any GRETINA data.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from math import exp, sqrt
from pathlib import Path

from day14_unobserved_feeding_transfer import kernel, tensor, transfer

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02"


def polynomial_weights(tj):
    j = F(tj, 2)
    s, h = j*(j+1), F(tj % 2, 2)
    if tj < 4:
        raise ValueError("rank 4 absent; do not divide by a zero reference tensor")
    m = [F(tm, 2) for tm in range(-tj, tj+1, 2)]
    t2 = lambda x: 3*x*x-s
    t4 = lambda x: 35*x**4-(30*s-25)*x*x+3*s*s-6*s
    exact = {2:[t2(x)/t2(h) for x in m], 4:[t4(x)/t4(h) for x in m]}
    printed = {2:[1-3*x*x/s for x in m],
               4:[1-10*x*x/s+F(35, 3)*x**4/s**2 for x in m]}
    basis = dict(rank4=t4(h)/(3*s*s), rank2=25*(s-3*h*h)/(9*s*s), rank0=-F(7, 9)/s)
    return dict(J=j, S=s, reference_abs_m=h, m=m, exact=exact, printed=printed, basis=basis)


def gaussian_population(tj, variance):
    if variance <= 0:
        raise ValueError("positive variance parameter required")
    values = [exp(-(tm/2)**2/(2*variance)) for tm in range(-tj, tj+1, 2)]
    norm = sum(values)
    return [p/norm for p in values]


def mean(weights, p):
    return sum(float(w)*q for w, q in zip(weights, p))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=RUN / "alignment-formula-contract-audit.json")
    args = parser.parse_args()
    path = RUN / "alignment-formula-contract-input.json"
    data = json.loads(path.read_text())
    literal_path = RUN / data["literal_record"]
    literal = json.loads(literal_path.read_text())
    checks = {}
    def check(name, value):
        checks[name] = bool(value)
        if not value:
            raise AssertionError(name)
    for role in ["publisher_pdf", "YA67_definition"]:
        p = ROOT/data[role]["path"]
        check(role+"_hash", hashlib.sha256(p.read_bytes()).hexdigest() == data[role]["sha256"])
    check("literal_Gaussian_denominator_sigma_not_sigma_squared", r"2\sigma }" in literal["Equ13"] and r"2\sigma ^2" not in literal["Equ13"])
    rows = []
    for tj in data["chosen_spin_twice"]:
        g = polynomial_weights(tj)
        for rank in [2, 4]:
            v, _ = tensor(tj, rank)
            norm = v[tj//2]
            check(f"polynomial_matches_independent_CG_J{tj}_rank{rank}", g["exact"][rank] == [x/norm for x in v])
        check(f"exact_uniform_tensors_zero_J{tj}", all(sum(g["exact"][k]) == 0 for k in [2, 4]))
        p2, p4 = g["printed"][2], g["printed"][4]
        uniform4 = sum(p4)/F(tj+1)
        check(f"printed_uniform_residual_J{tj}", sum(p2) == 0 and uniform4 == -F(7, 9)/g["S"])
        b = g["basis"]
        check(f"rank4_rank2_rank0_basis_identity_J{tj}", all(p4[i] == b["rank4"]*g["exact"][4][i]+b["rank2"]*g["exact"][2][i]+b["rank0"] for i in range(tj+1)))
        check(f"reference_convention_J{tj}", all(g["exact"][k][tj//2] == 1 for k in [2, 4])
              and (all(g["printed"][k][tj//2] == 1 for k in [2, 4]) if tj % 2 == 0 else all(g["printed"][k][tj//2] != 1 for k in [2, 4])))
        rows.append(dict(spin_twice=tj, uniform_exact_alpha2="0", uniform_exact_alpha4="0",
                         uniform_printed_alpha4=uniform4,
                         printed_reference_alpha2=p2[tj//2], printed_reference_alpha4=p4[tj//2],
                         printed_rank4_basis=b, max_pointwise_rank4_difference=max(abs(a-b) for a,b in zip(g["exact"][4], p4))))
    # Same spin on both sides removes the B_parent/B_child normalization issue.
    g = polynomial_weights(4)
    k = kernel(4, 4, 2)
    u4 = F(transfer(4, 4, 2, 4)["rational_eigenvalue"])
    uniform = [F(1, 5)]*5
    daughter = [sum((x*p for x,p in zip(row, uniform)), F(0)) for row in k]
    parent_raw = sum((x*p for x,p in zip(g["printed"][4], uniform)), F(0))
    daughter_raw = sum((x*p for x,p in zip(g["printed"][4], daughter)), F(0))
    check("positive_unobserved_channel_preserves_uniform_state", daughter == uniform)
    check("printed_rank4_not_pure_U4_without_change_of_basis", daughter_raw == parent_raw and daughter_raw != u4*parent_raw)
    large = []
    for j in data["chosen_large_integer_J"]:
        g = polynomial_weights(2*j)
        maximum = max(abs(a-b) for a,b in zip(g["exact"][4], g["printed"][4]))
        bound = F(35, 3)/(g["S"]-2)
        check(f"integer_uniform_pointwise_O_inverse_S_bound_J{j}", maximum <= bound)
        check(f"integer_exact_difference_identity_J{j}", all(a-b == 35*m*m*(2*m*m-g["S"])/(3*g["S"]**2*(g["S"]-2)) for m,a,b in zip(g["m"],g["exact"][4],g["printed"][4])))
        large.append(dict(J=j, S=g["S"], maximum_difference=maximum, bound=bound))
    check("large_J_difference_decreases_on_declared_sequence", all(a["maximum_difference"] > b["maximum_difference"] for a,b in zip(large, large[1:])))
    gaussians = []
    for tj in data["chosen_gaussian_spin_twice"]:
        g = polynomial_weights(tj)
        ratio = float(data["chosen_same_label_ratio"])
        j, sigma = tj/2, ratio*tj/2
        width_values = [exp(-.5*(tm/(2*sigma))**2) for tm in range(-tj, tj+1, 2)]
        width = [p/sum(width_values) for p in width_values]
        literal_variance = gaussian_population(tj, sigma)
        remapped = gaussian_population(tj, sigma**2)
        check(f"variance_equals_width_squared_mapping_J{tj}", max(abs(a-b) for a,b in zip(width,remapped)) < 1e-15)
        check(f"same_numeric_label_different_population_J{tj}", sum(abs(a-b) for a,b in zip(width,literal_variance)) > .01)
        check(f"chosen_Gaussians_positive_normalized_J{tj}", all(min(p) >= 0 and abs(sum(p)-1) < 1e-12 for p in [width,literal_variance]))
        gaussians.append(dict(spin_twice=tj, same_numeric_label=ratio,
                              width_parameter=sigma, literal_variance_parameter=sigma,
                              literal_equivalent_width_over_J=sqrt(sigma)/j,
                              remapped_variance_parameter=sigma*sigma,
                              width_contract_exact_alpha={k:mean(g["exact"][k],width) for k in [2,4]},
                              literal_variance_contract_exact_alpha={k:mean(g["exact"][k],literal_variance) for k in [2,4]},
                              width_contract_printed_alpha={k:mean(g["printed"][k],width) for k in [2,4]},
                              literal_variance_contract_printed_alpha={k:mean(g["printed"][k],literal_variance) for k in [2,4]}))
    try:
        polynomial_weights(3)
    except ValueError:
        check("absent_rank_not_divided", True)
    else:
        check("absent_rank_not_divided", False)
    check("author_code_and_experimental_fit_not_invented", data["author_implementation"] is None
          and data["actual_sigma_or_delta_fit"] is None and data["Ref39_body_read"] is False)
    result = dict(kind="literal formula versus exact finite-J tensor and declared Gaussian parameter contracts",
                  checks=checks, check_count=len(checks), passed=all(checks.values()), inputs=data,
                  finite_spin_rows=rows, large_integer_J=large, chosen_Gaussian_contracts=gaussians,
                  unobserved_channel_control=dict(J="2->2", L=2, U4=u4, parent_uniform_printed_rank4=parent_raw,
                                                  child_uniform_printed_rank4=daughter_raw,
                                                  inappropriate_pure_U4_prediction=u4*parent_raw),
                  input_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                  literal_sha256=hashlib.sha256(literal_path.read_bytes()).hexdigest(),
                  helper_sha256=hashlib.sha256((ROOT/"system/scripts/day14_unobserved_feeding_transfer.py").read_bytes()).hexdigest(),
                  limitations=["no read of Morinaga/Yamazaki1976 textbook approximation context",
                               "no assertion of official erratum or author's numerical implementation",
                               "no actual response, fit, sigma/delta or confidence interval recovered",
                               "large-J approximation and exact finite-J reference are separate contracts",
                               "same numeric Gaussian label is a chosen comparison, not original code input"])
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, default=str)+"\n")
    print(json.dumps({k:result[k] for k in ["kind", "check_count", "passed", "unobserved_channel_control", "chosen_Gaussian_contracts"]}, default=str))


if __name__ == "__main__":
    main()
