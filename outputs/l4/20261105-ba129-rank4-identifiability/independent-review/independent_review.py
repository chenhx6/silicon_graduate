#!/usr/bin/env python3
"""Independent, bounded review; write artifacts only next to this file.

The proof uses SymPy's standard Wigner/CG APIs, not the submitted routines.
The reviewed module is loaded only after the independent proof, for comparison.
Photon controls sum over unobserved final substates and both helicities.
All statistical and gate examples are explicitly chosen mathematical controls.
"""
from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
import platform
import sys
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE / "deps"))

import sympy as sp
from sympy.physics.wigner import clebsch_gordan, wigner_6j, wigner_d_small

J = sp.Rational(13, 2)
JT, JR = sp.Rational(11, 2), sp.Rational(9, 2)
X, THETA = sp.symbols("x theta", real=True)
CHECKS: list[dict] = []
TEX = ROOT / "raw/writing/gpt/ba129-rank4-identifiability/main.tex"
SUBMITTED = TEX.parent / "analysis/rank4_invariant.py"
EXPECTED_HASHES = {
    str(TEX.relative_to(ROOT)):
        "3c9d9a2bfded468af0069381115b3de112cbfff756adde94cd392770d3868f36",
    str(SUBMITTED.relative_to(ROOT)):
        "3ad6b43008cf24f1bbaf6d1ff3b7467be722cb85e46656580fe3061a99042c21",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def equal(name, got, expected):
    residual = sp.simplify(got - expected)
    CHECKS.append({"name": name, "passed": residual == 0,
                   "got": str(got), "expected": str(expected)})
    if residual != 0:
        raise AssertionError(f"{name}: {residual}")


def truth(name, condition):
    passed = bool(condition)
    CHECKS.append({"name": name, "passed": passed})
    if not passed:
        raise AssertionError(name)


def exact_and_float(value):
    return {"exact": str(value), "float": float(value)}


def f4_standard(jf):
    # Convention for pure E2: (-1)^(Ji+Jf-1) sqrt[25(2Ji+1)]
    # times <2,1;2,-1|4,0> times {Ji Ji 4;2 2 Jf}.
    return sp.simplify(
        (-1) ** int(J + jf - 1) * sp.sqrt(25 * (2 * J + 1))
        * clebsch_gordan(2, 2, 4, 1, -1, 0)
        * wigner_6j(J, J, 4, 2, 2, jf)
    )


@lru_cache(None)
def helicity_sum(ell, q):
    d = wigner_d_small(ell, THETA)
    expression = sp.expand(sum(d[ell-q, ell-h] ** 2 for h in (-1, 1)))
    result = sp.expand(expression.subs({
        sp.cos(THETA / 2): sp.sqrt((1 + X) / 2),
        sp.sin(THETA / 2): sp.sqrt((1 - X) / 2),
    }))
    return sp.Poly(result, X).as_expr()


@lru_cache(None)
def photon_distribution(jf, ell, m):
    """Normalized W(cos(theta)) for a pure multipole and one parent m.

    W=(2L+1)/2 sum_mf |<Jf mf,L q|Ji m>|^2 sum_h=+-1 |d^L_qh|^2.
    No F coefficients or 6j symbols are used by this route.
    """
    total = sp.S.Zero
    for mf2 in range(-int(2 * jf), int(2 * jf) + 1, 2):
        mf = sp.Rational(mf2, 2)
        q = m - mf
        if q.is_integer and abs(q) <= ell:
            cg = clebsch_gordan(jf, ell, J, mf, q, m)
            total += cg ** 2 * helicity_sum(ell, int(q))
    return sp.expand(sp.Rational(2 * ell + 1, 2) * total)


def ak(distribution, k):
    return sp.simplify(
        sp.Rational(2 * k + 1, 2)
        * sp.integrate(distribution * sp.legendre(k, X), (X, -1, 1))
    )


def make_csv(path, rows):
    columns = ["label", "Ji_twice", "Jf_twice", "energy_keV",
               "A2", "A2_sigma", "A4", "A4_sigma"]
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, columns)
        writer.writeheader()
        writer.writerows(rows)


def main():
    source_hashes_before = {str(p.relative_to(ROOT)): sha(p) for p in (TEX, SUBMITTED)}
    wt = wigner_6j(J, J, 4, 2, 2, JT)
    wr = wigner_6j(J, J, 4, 2, 2, JR)
    ft, fr = f4_standard(JT), f4_standard(JR)
    equal("standard_6j_ratio", wt / wr, sp.Rational(8, 3))
    equal("standard_6j_square_ratio", wt**2 / wr**2, sp.Rational(64, 9))
    equal("signed_F4_ratio", ft / fr, -sp.Rational(8, 3))
    equal("rank4_M1_M1_CG_zero", clebsch_gordan(1, 1, 4, 1, -1, 0), 0)
    equal("rank4_M1_E2_CG_zero", clebsch_gordan(1, 2, 4, 1, -1, 0), 0)

    # Prove for every parent m, hence for any common diagonal population.
    photon_rows = []
    for m2 in range(-13, 14, 2):
        m = sp.Rational(m2, 2)
        tw, rw, mw = (photon_distribution(JT, 2, m),
                      photon_distribution(JR, 2, m),
                      photon_distribution(JT, 1, m))
        ta4, ra4, ma4 = ak(tw, 4), ak(rw, 4), ak(mw, 4)
        for label, w in (("target_E2", tw), ("reference_E2", rw), ("target_M1", mw)):
            equal(f"{label}_normalization_m={m}", ak(w, 0), 1)
        equal(f"photon_rank4_relation_m={m}", ta4 + sp.Rational(8, 3)*ra4, 0)
        equal(f"photon_M1_rank4_zero_m={m}", ma4, 0)
        photon_rows.append({"m": str(m), "target_E2_A4": str(ta4),
                            "reference_E2_A4": str(ra4)})
    low = sp.Rational(1, 2)
    equal("low_m_target_A4", ak(photon_distribution(JT, 2, low), 4),
          sp.Rational(576, 1001))
    equal("low_m_reference_A4", ak(photon_distribution(JR, 2, low), 4),
          -sp.Rational(216, 1001))
    # Isotropic population: reference signal vanishes; ratio inversion is undefined.
    wi = sum(photon_distribution(JR, 2, sp.Rational(m2, 2))
             for m2 in range(-13, 14, 2)) / 14
    equal("isotropic_W", wi, 1)

    delta = sp.symbols("delta", real=True)
    f = delta**2 / (1 + delta**2)
    equal("delta_sign_invariance", f - f.subs(delta, -delta), 0)
    fvar, svar, gvar = sp.symbols("f s g", real=True)
    jac = sp.Matrix([fvar*svar]).jacobian([fvar, svar])
    truth("product_jacobian_rank_is_one", jac.rank() == 1)
    equal("product_null_direction", (jac * sp.Matrix([fvar, -svar]))[0], 0)
    product_pairs = [(sp.Rational(4, 5), 1), (sp.Rational(1, 5), 4)]
    for ff, ss in product_pairs:
        equal(f"same_product_f={ff}_s={ss}", ff*ss, sp.Rational(4, 5))
    # Both choices admit positive Q factors <=1, with the same Qr=1/4.
    q_choices = [{"f_E2": str(ff), "s4": str(ss), "Q4_reference": "1/4",
                  "Q4_target": str(sp.Rational(ss, 4)),
                  "abs_delta": str(sp.sqrt(ff/(1-ff)))}
                 for ff, ss in product_pairs]

    # Same parent, different positive diagonal postselections. These are ideal
    # substate filters, not an assertion about the historical gamma-gate response.
    mid = sp.Rational(7, 2)
    gt = ak(photon_distribution(JT, 2, low), 4)
    gr = ak(photon_distribution(JR, 2, mid), 4)
    rho_ratio = sp.simplify(
        ak(photon_distribution(JR, 2, low), 4) / gr)
    truth("different_postselection_same_sign_A4", gt > 0 and gr > 0)
    equal("gate_ratio_g_restores_algebra", gt,
          -sp.Rational(8, 3)*rho_ratio*gr)

    # A positive angular kernel need not have a positive rank-4 moment.
    c = sp.symbols("c", real=True)
    q4 = sp.simplify(sp.integrate(sp.legendre(4, X), (X, c, 1))/(1-c))
    equal("uniform_cone_Q4", q4, c*(1+c)*(7*c**2-3)/8)
    equal("positive_kernel_60deg_negative_Q4", q4.subs(c, sp.Rational(1, 2)),
          -sp.Rational(15, 128))
    equal("point_response_limit", sp.limit(q4, c, 1), 1)
    # A non-convolution response can mix ranks and cannot be absorbed in scalar Q4.
    ideal = 1 + sp.legendre(2, X)/3
    response = 1 + sp.legendre(2, X)/2
    observed = sp.expand(ideal*response/ak(sp.expand(ideal*response), 0))
    equal("unfolded_example_true_A4", ak(ideal, 4), 0)
    equal("polar_efficiency_leaks_rank2_into4", ak(observed, 4), sp.Rational(18, 217))

    t, r, sigma = sp.Rational(4, 25), sp.Rational(2, 25), sp.Rational(1, 20)
    equal("public_central_product", -sp.Rational(3, 8)*t/r, -sp.Rational(3, 4))
    # An independently known negative s4 still permits magnitude inversion.
    fn = sp.Rational(3, 4)
    equal("negative_known_s4_can_identify_f", fn*(-1), -sp.Rational(3, 4))
    equal("negative_known_s4_abs_delta", sp.sqrt(fn/(1-fn)), sp.sqrt(3))
    scale = -sp.Rational(8, 3)
    image1 = sorted([sp.S.Zero, scale*(r-sigma), scale*(r+sigma)])
    image2 = sorted([sp.S.Zero, scale*(r-2*sigma), scale*(r+2*sigma)])
    equal("two_margin_gap_at_s4_one", (t-2*sigma)-image2[-1], sp.Rational(1, 150))
    equal("s4_9_over_8_closes_two_margin_box",
          scale*sp.Rational(9, 8)*(r-2*sigma), t-2*sigma)
    cf = scale*fvar
    d2 = sp.factor((t-cf*r)**2/(sigma**2+cf**2*sigma**2))
    candidates = [sp.S.Zero, sp.S.One] + [
        q for q in sp.solve(sp.together(sp.diff(d2, fvar)).as_numer_denom()[0], fvar)
        if q.is_real and 0 <= q <= 1]
    best_f = min(candidates, key=lambda q: float(d2.subs(fvar, q)))
    equal("independent_diagonal_profile_min_f", best_f, 1)
    best_score = sp.simplify(d2.subs(fvar, best_f))

    # Compare the already-derived results with the supplied implementation.
    spec = importlib.util.spec_from_file_location("reviewed_rank4", SUBMITTED)
    supplied = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(supplied)
    for label, jf, exact in (("target", 11, ft), ("reference", 9, fr)):
        actual = supplied.native_f(13, jf, 4, 2, 2)
        truth(f"submitted_F4_matches_standard_{label}",
              abs(actual-float(exact)) < 2e-13)
    supplied_profile = supplied.diagonal_profile(float(t), float(sigma),
                                                  float(r), float(sigma), float(scale))
    truth("submitted_diagonal_score_matches_independent_minimum",
          abs(supplied_profile["minimum_diagnostic_score"]-float(best_score)) < 1e-12)
    rows = [
        {"label": "target_365", "Ji_twice": 13, "Jf_twice": 11, "energy_keV": 364.7,
         "A2": -0.70, "A2_sigma": 0.03, "A4": 0.16, "A4_sigma": 0.05},
        {"label": "reference_462", "Ji_twice": 13, "Jf_twice": 9, "energy_keV": 461.6,
         "A2": 0.22, "A2_sigma": 0.02, "A4": 0.08, "A4_sigma": 0.05},
    ]
    fixture = HERE / "summary_retyped_from_tex.csv"
    make_csv(fixture, rows)
    submitted_result = supplied.analyze(fixture)
    bad_spin = HERE / "negative_control_different_parent_spin.csv"
    make_csv(bad_spin, [rows[0], {**rows[1], "Ji_twice": 15}])
    bad_spin_result = supplied.analyze(bad_spin)
    truth("demonstrated_missing_same_spin_validation",
          bad_spin_result["algebra"] == submitted_result["algebra"])
    duplicate = HERE / "negative_control_duplicate_row.csv"
    make_csv(duplicate, rows + [rows[0]])
    duplicate_result = supplied.load_rows(duplicate)
    truth("demonstrated_duplicate_row_acceptance", len(duplicate_result) == 2)

    source_hashes_after = {str(p.relative_to(ROOT)): sha(p) for p in (TEX, SUBMITTED)}
    truth("reviewed_files_unchanged_during_execution",
          source_hashes_before == source_hashes_after)
    report = {
        "review_kind": "independent mathematical/scientific audit; no primary retrieval",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "runtime": {"python": platform.python_version(), "sympy": sp.__version__,
                    "executable": sys.executable},
        "review_script_sha256": sha(Path(__file__)),
        "initial_read_hashes": EXPECTED_HASHES,
        "execution_before_hashes": source_hashes_before,
        "execution_after_hashes": source_hashes_after,
        "same_as_initial_read": source_hashes_before == EXPECTED_HASHES,
        "proof": {
            "sixj_target": exact_and_float(wt), "sixj_reference": exact_and_float(wr),
            "sixj_ratio": str(sp.simplify(wt/wr)),
            "sixj_square_ratio": str(sp.simplify(wt**2/wr**2)),
            "F4_target": exact_and_float(ft), "F4_reference": exact_and_float(fr),
            "F4_ratio": str(sp.simplify(ft/fr)),
            "photon_route_all_parent_m": photon_rows,
            "scope": "diagonal parent density; unobserved final substates and helicities; point response",
        },
        "identifiability": {
            "rank4_only_identifies": "f_E2*s4 when common postselection holds and A4_reference != 0",
            "delta_sign": "not identifiable from rank4",
            "product_jacobian": str(jac),
            "nonidentifiable_positive_Q_examples": q_choices,
            "known_s4_inverse": "f=z/s4; |delta|=sqrt(f/(1-f)); 0<=f<1",
            "bounded_positive_s4_inverse": "f in [z/s_max,z/s_min] intersect [0,1], for z>=0",
            "known_negative_s4_example": {"z": "-3/4", "s4": "-1", "f": "3/4",
                                         "abs_delta": "sqrt(3)"},
            "zero_cases": ["rho4=0: no rank4 information", "Q4_reference=0: ratio undefined",
                          "Q4_target=0: no target rank4 sensitivity",
                          "f=1: pure-E2 infinite-delta endpoint"],
        },
        "gate_and_response_controls": {
            "different_postselection_toy": {
                "population_before_selection": "equal mixture of m=+-1/2 and m=+-7/2",
                "target_postselection": "m=+-1/2", "reference_postselection": "m=+-7/2",
                "f_E2": "1", "Q4_target": "1", "Q4_reference": "1",
                "target_A4": str(gt), "reference_A4": str(gr),
                "g4_rho_target_over_reference": str(rho_ratio),
                "status": "ideal positive substate filters, not historical gamma-gate simulation",
            },
            "correct_general_relation": "At=-(8/3)*f*s4*g4*Ar, g4=rho4t/rho4r, where scalar factorization holds",
            "nonnegative_kernel_negative_Q4": {"model": "uniform solid-angle cone, beta_max=60deg",
                                               "Q4": "-15/128"},
            "rank_mixing_response": {"W": str(ideal), "h": str(response),
                                    "true_A4": "0", "observed_A4": str(ak(observed, 4)),
                                    "status": "chosen positive polar efficiency; not a scalar convolution"},
        },
        "summary_checks": {
            "central_product": "-3/4",
            "one_marginal_box_image_s4_one": [str(image1[0]), str(image1[-1])],
            "two_marginal_box_image_s4_one": [str(image2[0]), str(image2[-1])],
            "two_marginal_gap_s4_one": "1/150",
            "two_marginal_overlap_threshold_s4": "9/8",
            "diagonal_profile": {"objective": str(d2), "candidate_f": [str(v) for v in candidates],
                                 "best_f": str(best_f), "minimum": exact_and_float(best_score),
                                 "not_experimental_test": True},
        },
        "implementation_findings": [
            "canonical-case F4 values and diagonal diagnostic match independent calculations",
            "reference Ji_twice is ignored; mismatched parent spin accepted",
            "duplicate labels silently accepted and overwritten",
            "exact_ratio is a literal -8/3; exact square plus independently handled phase should certify sign",
            "synthetic roundtrip validates an algebra product, not a new parameter-identification method",
        ],
        "checks": CHECKS,
        "passed": all(item["passed"] for item in CHECKS),
        "number_of_checks": len(CHECKS),
        "boundary": "No new experimental delta, covariance, p-value, B(E2), or mode assignment; no novelty search.",
    }
    (HERE / "result.json").write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({
        "passed": report["passed"], "number_of_checks": len(CHECKS),
        "F4_ratio": report["proof"]["F4_ratio"],
        "F4_target": str(ft), "F4_reference": str(fr),
        "photon_parent_m_values_checked": len(photon_rows),
        "source_hashes_unchanged": source_hashes_before == source_hashes_after,
        "same_as_initial_read": source_hashes_before == EXPECTED_HASHES,
        "output": str(HERE / "result.json"),
    }, indent=2))


if __name__ == "__main__":
    main()
