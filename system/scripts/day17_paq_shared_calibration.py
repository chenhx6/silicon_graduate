#!/usr/bin/env python3
"""Day17: matched-reference counting design, shared geometry calibration and P.

This is a declared statistical design, never a fit to ST99 or SG98 data.
Run from the Wiki root; all files and original hashes are checked explicitly.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def asymmetry(kind, first, second, geometry):
    if kind == "clover":
        return (geometry * first - second) / (geometry * first + second)
    if kind == "sg98":
        return (geometry * first - second) / (np.sqrt(geometry) * (first + second))
    raise ValueError(kind)


def probability(kind, amplitude, geometry):
    if kind == "clover":
        return (1 + amplitude) / (geometry * (1 - amplitude) + 1 + amplitude)
    return (1 + np.sqrt(geometry) * amplitude) / (1 + geometry)


def complex_gradient(fun, point):
    result = []
    for i in range(len(point)):
        z = np.array(point, dtype=complex)
        z[i] += 1e-22j
        result.append(np.imag(fun(z)) / 1e-22)
    return np.asarray(result)


def symbolic_map(kind):
    t1, t2, r1, r2, u1, u2, pref = variables = sp.symbols(
        "t1 t2 r1 r2 u1 u2 pref", positive=True
    )
    h = u2 / u1

    def form(n1, n2):
        if kind == "clover":
            return (h * n1 - n2) / (h * n1 + n2)
        return (h * n1 - n2) / (sp.sqrt(h) * (n1 + n2))

    at, ar = form(t1, t2), form(r1, r2)
    expression = sp.factor(pref * at / ar)
    jacobian = sp.Matrix([expression]).jacobian(variables)
    outputs = sp.Matrix([at, ar, ar / pref, expression])
    output_jacobian = outputs.jacobian(variables)
    return variables, expression, jacobian, outputs, output_jacobian


def audit_case(case, config, rng):
    kind = case["name"]
    vars_, expr, jac, outputs, output_jac = symbolic_map(kind)
    p = np.asarray(case["target"] + case["reference"] + case["unpolarized"] + [case["reference_P"]], dtype=float)
    variance = np.r_[p[:6], case["reference_P_sigma"] ** 2]
    h = p[5] / p[4]
    numeric = sp.lambdify([vars_], expr, "numpy")
    j = np.asarray(sp.lambdify([vars_], jac, "numpy")(p), dtype=float).reshape(-1)
    jo = np.asarray(sp.lambdify([vars_], output_jac, "numpy")(p), dtype=float)
    vals = np.asarray(sp.lambdify([vars_], outputs, "numpy")(p), dtype=float).reshape(-1)
    at, ar, q, pt = vals
    covariance = (jo * variance) @ jo.T
    checks = []

    def check(name, condition, evidence):
        checks.append({"name": name, "passed": bool(condition), "evidence": evidence})

    j_complex = complex_gradient(numeric, p)
    check("symbolic Jacobian versus complex-step on primitive counts", np.allclose(j, j_complex, rtol=1e-6, atol=1e-13), float(np.max(np.abs(j - j_complex))))
    check("covariance positive semidefinite", np.linalg.eigvalsh(covariance).min() > -1e-14, np.linalg.eigvalsh(covariance).tolist())
    check("common Poisson exposure cancels in each sample", all(abs(np.dot(j[a:a+2], p[a:a+2])) < 1e-12 for a in (0, 2, 4)), [float(np.dot(j[a:a+2], p[a:a+2])) for a in (0, 2, 4)])
    check("declared P recovered", abs(pt - .3) < 1e-12, float(pt))
    check("declared Q recovered", abs(q - (.2 if kind == "clover" else .05)) < 1e-12, float(q))

    # Independent route: conditional-binomial likelihood Fisher matrix.
    theta = np.asarray([np.log(h), np.log(q), pt, p[6]])
    fisher = np.zeros((4, 4))
    for name, counts, value_index in [("unpolarized", case["unpolarized"], None), ("reference", case["reference"], 3), ("target", case["target"], 2)]:
        def prob(v):
            amp = 0 if value_index is None else np.exp(v[1]) * v[value_index]
            return probability(kind, amp, np.exp(v[0]))

        prob0 = float(prob(theta))
        gradient = complex_gradient(prob, theta)
        fisher += sum(counts) / (prob0 * (1 - prob0)) * np.outer(gradient, gradient)
        check(name + " expected first-category proportion", abs(prob0 - counts[0] / sum(counts)) < 1e-12, prob0)
    fisher[3, 3] += 1 / case["reference_P_sigma"] ** 2
    inverse_fisher = np.linalg.inv(fisher)
    local_variance = float(np.dot(j * variance, j))
    check("full joint likelihood Fisher agrees with delta variance", np.isclose(inverse_fisher[2, 2], local_variance, rtol=1e-6), {"fisher": float(inverse_fisher[2, 2]), "delta": local_variance})

    # Cov(At,Q) is induced by the common U calibration. It is retained here.
    expanded_variance = covariance[0, 0] / q**2 + at**2 * covariance[2, 2] / q**4 - 2 * at * covariance[0, 2] / q**3
    independent_variance = covariance[0, 0] / q**2 + at**2 * covariance[2, 2] / q**4
    check("expanded At-Q covariance agrees with primitive variance", np.isclose(expanded_variance, local_variance, rtol=1e-12), float(expanded_variance))
    check("reference roundtrip is an identity, not validation", sp.simplify(vars_[-1] * outputs[1] / outputs[1] - vars_[-1]) == 0, "P_ref * A_ref/A_ref == P_ref")

    repeats = config["monte_carlo_replicates"]
    counts = rng.poisson(p[:6], size=(repeats, 6))
    pref_sample = rng.normal(p[6], case["reference_P_sigma"], size=repeats)
    hs = counts[:, 5] / counts[:, 4]
    ats = asymmetry(kind, counts[:, 0], counts[:, 1], hs)
    ars = asymmetry(kind, counts[:, 2], counts[:, 3], hs)
    samples = pref_sample * ats / ars
    finite = np.isfinite(samples)
    empirical_sigma = float(np.std(samples[finite], ddof=1))
    sigma = float(np.sqrt(local_variance))
    bias_sigma = float((np.mean(samples[finite]) - pt) / sigma)
    sigma_relative = empirical_sigma / sigma - 1
    contract = config["validation_contract"]
    check("finite design replicates", finite.all(), int(finite.sum()))
    check("Monte Carlo local-sigma agreement under declared tolerance", abs(sigma_relative) < contract["monte_carlo_sigma_relative_tolerance"], {"relative_difference": sigma_relative, "tolerance": contract["monte_carlo_sigma_relative_tolerance"]})
    check("Monte Carlo finite-sample bias under declared tolerance", abs(bias_sigma) < contract["monte_carlo_bias_in_sigma_tolerance"], {"bias_in_sigma": bias_sigma, "tolerance": contract["monte_carlo_bias_in_sigma_tolerance"]})
    result = {
        "kind": kind, "input_kind": config["input_kind"], "geometry": float(h),
        "At": float(at), "Ar": float(ar), "Q": float(q), "Pt": float(pt),
        "symbolic_target_P": str(expr), "primitive_order": [str(v) for v in vars_],
        "jacobian": j.tolist(), "covariance_order": ["At", "Ar", "Q", "Pt"],
        "derived_covariance": covariance.tolist(), "sigma_P_joint": sigma,
        "sigma_P_if_At_Q_incorrectly_independent": float(np.sqrt(independent_variance)),
        "variance_components_target_reference_unpolarized_Pref": [float(np.dot(j[a:b]**2, variance[a:b])) for a, b in [(0,2), (2,4), (4,6), (6,7)]],
        "fisher_parameter_order": ["ln_geometry", "ln_Q", "Pt", "Pref"],
        "fisher_matrix": fisher.tolist(), "monte_carlo": {"replicates": repeats, "mean": float(np.mean(samples[finite])), "sigma": empirical_sigma, "bias_in_local_sigma": bias_sigma},
        "checks": checks
    }
    if kind == "sg98":
        aa, hh = sp.symbols("A eta", positive=True)
        cc = (1 + sp.sqrt(hh) * aa) / (1 + hh)
        ss = 1 - cc
        balanced = (hh * cc - ss) / (hh * cc + ss)
        transformed = (1 + hh) * aa / (2 * sp.sqrt(hh) + (hh - 1) * aa)
        check("balanced-denominator nonlinear transformation exact", sp.simplify(balanced - transformed) == 0, str(transformed))
        check("balanced form becomes original only at eta one", sp.simplify(transformed.subs(hh, 1) - aa) == 0, "B(A,eta=1)=A")
        check("balanced form has zero unpolarized null", sp.simplify(transformed.subs(aa, 0)) == 0, "B(0,eta)=0 does not establish linear response")
        bt = (h * p[0] - p[1]) / (h * p[0] + p[1])
        br = (h * p[2] - p[3]) / (h * p[2] + p[3])
        result["wrong_balanced_denominator"] = {"B_target": float(bt), "B_reference": float(br), "P_using_original_Q": float(bt / q), "P_recalibrating_one_reference_only": float(p[6] * bt / br), "boundary": "A_bal is nonlinear in P; fitting its reference Q does not make a single scalar Q valid for all target P."}
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=RUN / "paq-design-input.json")
    parser.add_argument("--output", type=Path, default=RUN / "paq-shared-calibration-result.json")
    args = parser.parse_args()
    args.input.resolve().relative_to(ROOT)
    args.output.resolve().relative_to(ROOT)
    config = json.loads(args.input.read_text())
    provenance = []
    for source in config["sources"]:
        path = ROOT / source["path"]
        text = path.read_text()
        raw = ROOT / re.search(r'^raw_file: "(.+)"', text, re.M).group(1)
        observed = sha(raw)
        if observed != source["raw_sha256"]:
            raise RuntimeError("original source hash mismatch: " + source["path"])
        provenance.append({**source, "actual_raw_sha256": observed})
    rng = np.random.default_rng(config["monte_carlo_seed"])
    cases = [audit_case(case, config, rng) for case in config["cases"]]
    failed = [f"{r['kind']}: {c['name']}" for r in cases for c in r["checks"] if not c["passed"]]
    result = {"run_id": config["run_id"], "session_id": config["session_id"], "generated_at": datetime.now(timezone.utc).isoformat(), "script_sha256": sha(Path(__file__)), "input_sha256": sha(args.input), "dependencies": {"numpy": np.__version__, "sympy": sp.__version__}, "input_kind": config["input_kind"], "assumptions": config["assumptions"], "source_provenance": provenance, "cases": cases, "failed_checks": failed, "ok": not failed}
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"ok": result["ok"], "failed_checks": failed, "cases": [{k: r[k] for k in ["kind", "At", "Ar", "Q", "Pt", "sigma_P_joint", "sigma_P_if_At_Q_incorrectly_independent", "monte_carlo"]} for r in cases]}, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
