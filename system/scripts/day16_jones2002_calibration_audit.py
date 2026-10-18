#!/usr/bin/env python3
"""Audit J02 reference-state, zero-intensity and relative-efficiency boundaries.

The four-count example is an expected-count design, not experimental data.
"""
from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import sympy as sp

from day16_co60_conditional_stokes import LINEAR_BASIS, operators
from day16_gretina_convention_audit import coefficients, trace_coefficients


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cross_ratio(counts: np.ndarray, covariance: np.ndarray) -> dict:
    if not np.all(np.isfinite(counts)) or np.any(counts <= 0):
        raise ValueError("Positive finite peak areas required for the log-ratio approximation")
    if covariance.shape != (4, 4) or not np.allclose(covariance, covariance.T):
        raise ValueError("Symmetric four-area covariance required")
    if np.linalg.eigvalsh(covariance).min() < -1e-10:
        raise ValueError("Area covariance must be PSD")
    c = np.array([.5, -.5, .5, -.5])
    log_r = float(c @ np.log(counts))
    value = -math.tanh(log_r/2)
    gradient = -(1-value*value)/2 * c/counts
    variance = float(gradient @ covariance @ gradient)
    return {"A": value, "R": math.exp(log_r), "log_R": log_r,
            "gradient_counts": gradient.tolist(), "variance_delta_method": variance,
            "sigma_delta_method": math.sqrt(variance)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.contract.read_text())
    assert cfg["identity"] == "J02-RECALIBRATION-BOUNDARIES-01"
    raw = Path(cfg["raw"])
    assert sha(raw) == cfg["raw_sha256"]
    x = sp.symbols("x", real=True)
    p2, p4 = sp.legendre(2, x), sp.legendre(4, x)
    expected = {"m0": (sp.Rational(5, 7), -sp.Rational(12, 7)),
                "abs1": (sp.Rational(5, 14), sp.Rational(8, 7)),
                "abs2": (-sp.Rational(5, 7), -sp.Rational(2, 7))}
    rows = {}
    max_trace_error = 0.
    for name, population in cfg["population_checks"].items():
        pop = np.array(population, dtype=float)
        assert np.all(pop >= 0) and abs(pop.sum()-1) < 1e-14
        racah = coefficients(4, 0, pop, None)
        trace = trace_coefficients(2, 0, pop, (("E", 2, 1.),))
        a2, a4 = expected[name]
        error = max(abs(racah[key]-float(val)) for key, val in [("a2", a2), ("a4", a4)])
        error = max(error, abs(trace["a2"]-float(a2)), abs(trace["a4"]-float(a4)))
        assert error < 1e-12
        w = sp.factor(1 + a2*p2 + a4*p4)
        # Eq.(9)'s electric-quadrupole numerator; its denominator is 2W.
        h = sp.factor((3*a2*(1-x*x) + sp.Rational(5, 4)*a4*(1-x*x)
                       - sp.Rational(35, 16)*a4*4*x*x*(1-x*x))/2)
        assert sp.integrate(w, (x, -1, 1)) == 2
        # Do not cancel the expression before retaining all intensity zeros.
        nodes = sp.solve(w, x)
        angle_controls = []
        for degrees in [10, 30, 60, 89, 90, 91, 120, 150, 170]:
            theta = math.radians(degrees)
            op = operators(4, 0, (("E", 2, 1.),), theta, 0., "native")
            rho = np.einsum("ami,i,bmi->ab", op, pop, op.conj())
            linear = LINEAR_BASIS @ rho @ LINEAR_BASIS.conj().T
            i = 4*math.pi*float(np.trace(linear).real)
            q = 4*math.pi*float((linear[0, 0]-linear[1, 1]).real)
            cosine = math.cos(theta)
            ew, eh = float(w.subs(x, cosine)), float(h.subs(x, cosine))
            max_trace_error = max(max_trace_error, abs(i-ew), abs(q-eh))
            exact_node = degrees == 90 and name == "m0"
            angle_controls.append({"theta_deg": degrees, "I_numeric": i, "Q_numeric": q,
                "exact_node": exact_node, "P_defined": not exact_node,
                "P": None if exact_node else q/i,
                "note": "Exact polynomial I=0; floating trigonometric residue is not a signal" if exact_node else ""})
        rows[name] = {"population": population, "a2": str(a2), "a4": str(a4),
            "W_polynomial": str(w), "Q_polynomial": str(h),
            "P_simplified_only_away_from_nodes": str(sp.cancel(h/w)),
            "I_zero_cosines": [str(v) for v in nodes],
            "W_at90_exact": str(w.subs(x, 0)), "Q_at90_exact": str(h.subs(x, 0)),
            "Racah_vs_direct_trace_error": error, "angle_controls": angle_controls}
    assert max_trace_error < 1e-12
    # A 0->2 photon along z has physical helicities +/-1, not +/-2.
    first = operators(0, 4, (("E", 2, 1.),), 0., 0., "native")
    daughter = np.einsum("ami,ani->mn", first, first.conj())
    daughter /= np.trace(daughter)
    assert np.linalg.eigvalsh(daughter).min() > -1e-14
    actual_pop = np.diag(daughter).real
    assert np.max(abs(actual_pop-cfg["population_checks"]["abs1"])) < 1e-14
    assert abs(rows["abs1"]["angle_controls"][4]["P"]-1) < 1e-12
    assert abs(rows["abs2"]["angle_controls"][4]["P"]+1) < 1e-12
    # Full-polarization at one angle is weaker than angularly constant P.
    p0 = sp.symbols("p0", real=True)
    a2, a4 = 5*(p0+1)/14, (8-20*p0)/7
    w_family = sp.factor(1+a2*p2+a4*p4)
    q_family = sp.factor((3*a2*(1-x*x)+sp.Rational(5, 4)*a4*(1-x*x)
                         - sp.Rational(35, 16)*a4*4*x*x*(1-x*x))/2)
    assert sp.simplify(q_family.subs(x, 0)-w_family.subs(x, 0)) == 0
    assert sp.simplify(w_family.subs(x, 0)-sp.Rational(5, 4)*(1-p0)) == 0
    d = cfg["design_inputs"]
    a, ta, tb, e1, e2 = (d[key] for key in ["A", "exposure_a", "exposure_b",
                                         "efficiency_A1", "efficiency_A2"])
    counts = np.array([ta*e1*(1-a), ta*e2*(1+a), tb*e2*(1-a), tb*e1*(1+a)])
    independent_cov = np.diag(counts)
    cr = cross_ratio(counts, independent_cov)
    assert abs(cr["A"]-a) < 1e-14
    assert abs(cr["variance_delta_method"]-(1-a*a)**2/16*sum(1/counts)) < 1e-16
    numerical_gradient = []
    for j in range(4):
        h = counts[j]*1e-5
        plus, minus = counts.copy(), counts.copy()
        plus[j] += h
        minus[j] -= h
        numerical_gradient.append((cross_ratio(plus, independent_cov)["A"]
                                   - cross_ratio(minus, independent_cov)["A"])/(2*h))
    assert np.max(abs(np.array(numerical_gradient)-cr["gradient_counts"])) < 1e-13
    # A common multiplicative exposure covariance cancels; a residual efficiency
    # ratio drift does not. These are declared controls, not recovered errors.
    common_cov = independent_cov + .01*np.outer(counts, counts)
    common = cross_ratio(counts, common_cov)
    assert abs(common["variance_delta_method"]-cr["variance_delta_method"]) < 1e-16
    drift_counts = counts.copy()
    kappa = d["efficiency_ratio_product_drift"]
    drift_counts[0] *= kappa
    drift = cross_ratio(drift_counts, np.diag(drift_counts))
    predicted = math.tanh(math.atanh(a)-math.log(kappa)/4)
    assert abs(drift["A"]-predicted) < 1e-14
    zero_rejected = False
    try:
        cross_ratio(np.array([0., *counts[1:]]), independent_cov)
    except ValueError:
        zero_rejected = True
    assert zero_rejected
    author_cases = []
    for n0, n90 in cfg["author_hypothetical_count_cases"]:
        asym = (n90-n0)/(n90+n0)
        sigma = math.sqrt(4*n0*n90/(n90+n0)**3)
        author_cases.append({"n0": n0, "n90": n90, "A": asym, "sigma_Poisson_A": sigma,
                             "relative_sigma_A": sigma/abs(asym), "status": "author hypothetical counts"})
    quote = cfg["quoted_actual_example"]
    q = quote["A"]/quote["P"]
    q_sigma_independent = math.sqrt((quote["sigma_A"]/quote["P"])**2
                                  + (quote["A"]*quote["sigma_P"]/quote["P"]**2)**2)
    result = {"identity": cfg["identity"], "at": datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(),
        "script_sha256": sha(Path(__file__)), "contract_sha256": sha(args.contract),
        "raw_sha256": sha(raw), "population_rows": rows,
        "point_0_to2_reference_daughter_population_m_minus2_to2": actual_pop.tolist(),
        "maximum_W_Q_trace_vs_polynomial_error": max_trace_error,
        "printed_w_abs2_matches_quoted_a2a4": False,
        "printed_a2a4_matches_physical_point_reference_abs1": True,
        "m0_node90_ratio_undefined": True,
        "only_m0_abs1_family_W90": str(sp.factor(w_family.subs(x, 0))),
        "family_P_at60_example_p0_point4": str(sp.cancel(q_family/w_family).subs({p0:sp.Rational(2,5),x:sp.Rational(1,2)})),
        "cross_ratio_design": {"counts_order": cfg["design_counts_order"], "expected_counts": counts.tolist(),
            "independent_Poisson_delta_method": cr,
            "common_exposure_covariance_control": common,
            "naive_first_orientation_asymmetry": float((counts[1]-counts[0])/(counts[1]+counts[0])),
            "efficiency_ratio_drift_kappa": kappa, "drift_result": drift,
            "predicted_drift_A": predicted, "zero_count_control_rejected": zero_rejected},
        "author_hypothetical_count_cases": author_cases,
        "actual_quoted_example_conditional_arithmetic": {"Q_from_rounded_A_P": q,
            "sigma_Q_if_A_P_independent": q_sigma_independent,
            "AP_cov_known": False, "new_experimental_Q": False},
        "human_prefix_or_claim_review_changed": False, "new_experiment_or_full_detector_response": False}
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")
    print(json.dumps({k: result[k] for k in ["point_0_to2_reference_daughter_population_m_minus2_to2",
        "maximum_W_Q_trace_vs_polynomial_error", "m0_node90_ratio_undefined", "family_P_at60_example_p0_point4",
        "cross_ratio_design", "author_hypothetical_count_cases", "actual_quoted_example_conditional_arithmetic"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
