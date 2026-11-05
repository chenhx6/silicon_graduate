#!/usr/bin/env python3
"""Read supplied primary OCR; independently derive the rank-2 companion bound.

Writes only rank2-result.json beside this script. OCR uncertainty assignments
are provisional scenarios, not replacements for visually verified table cells.
"""
import hashlib
import json
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE / "deps"))

import sympy as sp
from sympy.physics.wigner import clebsch_gordan, wigner_6j


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    original = ROOT / "raw/papers/gpt/query/20261105-ba129-primary/gizon1977-full-json.json"
    derived = ROOT / "tmp/ba129-primary-review/gizon1977-full.txt"
    document = json.loads(original.read_text())
    text = document["full-text-retrieval-response"]["originalText"]
    before = {str(p.relative_to(ROOT)): sha(p) for p in (original, derived)}
    checks = []

    def check(name, condition):
        passed = bool(condition)
        checks.append({"name": name, "passed": passed})
        assert passed, name

    def equal(name, value, expected):
        check(name, sp.simplify(value - expected) == 0)

    j, jt, jr = sp.Rational(13, 2), sp.Rational(11, 2), sp.Rational(9, 2)

    def standard_f(rank, ell, ellp, jf):
        return sp.simplify(
            (-1) ** int(j + jf + ell + ellp - 1)
            * sp.sqrt((2*j+1)*(2*ell+1)*(2*ellp+1))
            * clebsch_gordan(ell, ellp, rank, 1, -1, 0)
            * wigner_6j(j, j, rank, ellp, ell, jf))

    reference_f2 = standard_f(2, 2, 2, jr)
    a = sp.simplify(standard_f(2, 1, 1, jt) / reference_f2)
    b = sp.simplify(standard_f(2, 1, 2, jt) / reference_f2)
    d = sp.simplify(standard_f(2, 2, 2, jt) / reference_f2)
    matrix = sp.Matrix([[a, b], [b, d]])
    equal("M00", a, -sp.Rational(7, 10))
    equal("M01", b, 7*sp.sqrt(11)/10)
    equal("M11", d, -sp.Rational(1, 10))
    lower, upper = (-2-sp.sqrt(137))/5, (-2+sp.sqrt(137))/5
    equal("lower_eigenvalue", (matrix-lower*sp.eye(2)).det(), 0)
    equal("upper_eigenvalue", (matrix-upper*sp.eye(2)).det(), 0)
    delta = sp.symbols("delta", real=True)
    vector = sp.Matrix([1, delta])
    quotient = sp.factor((vector.T*matrix*vector)[0]/(1+delta**2))
    delta_min = (3-2*sp.sqrt(137))/(7*sp.sqrt(11))
    equal("rayleigh_minimum_attained", quotient.subs(delta, delta_min), lower)
    equal("stationary_at_minimum", sp.diff(quotient, delta).subs(delta, delta_min), 0)
    flip = sp.diag(1, -1)
    check("delta_phase_flip_preserves_spectrum", matrix.eigenvals() == (flip*matrix*flip).eigenvals())
    central = -sp.Rational(7, 10)/sp.Rational(11, 50)
    equal("central_ratio", central, -sp.Rational(35, 11))
    check("central_below_lower_eigenvalue_at_s2_one", central < lower)
    s2_needed = sp.simplify(central/lower)
    check("central_requires_s2_above_one", s2_needed > 1)

    rows = []
    for name, t2_error, r2_error, r4_error in (
        ("ENSDF_as_in_manuscript", sp.Rational(3, 100), sp.Rational(1, 50), sp.Rational(1, 20)),
        ("literal_OCR_provisional", sp.Rational(1, 20), sp.Rational(1, 25), sp.Rational(3, 50)),
    ):
        for n in (1, 2):
            t2lo, t2hi = -sp.Rational(7, 10)-n*t2_error, -sp.Rational(7, 10)+n*t2_error
            r2lo, r2hi = sp.Rational(11, 50)-n*r2_error, sp.Rational(11, 50)+n*r2_error
            check(f"{name}_reference_rank2_nonzero_box_{n}", r2lo > 0)
            ratlo, rathi = sp.simplify(t2lo/r2lo), sp.simplify(t2hi/r2hi)
            overlap2 = bool(max(ratlo, lower) <= min(rathi, upper))
            r4lo, r4hi = sp.Rational(2, 25)-n*r4_error, sp.Rational(2, 25)+n*r4_error
            t4lo, t4hi = sp.Rational(4, 25)-n*sp.Rational(1, 20), sp.Rational(4, 25)+n*sp.Rational(1, 20)
            image = [sp.S.Zero, -sp.Rational(8, 3)*r4lo, -sp.Rational(8, 3)*r4hi]
            overlap4 = bool(max(min(image), t4lo) <= min(max(image), t4hi))
            expected2 = n == 2 or name == "literal_OCR_provisional"
            expected4 = n == 2 and name == "literal_OCR_provisional"
            check(f"{name}_rank2_box_result_{n}", overlap2 == expected2)
            check(f"{name}_rank4_box_result_{n}", overlap4 == expected4)
            rows.append({
                "scenario": name, "marginal_error_multiplier": n,
                "A2_ratio_box": [str(ratlo), str(rathi)],
                "rank2_box_has_solution_s2_one": overlap2,
                "A4_reference_box": [str(r4lo), str(r4hi)],
                "A4_target_box": [str(t4lo), str(t4hi)],
                "A4_target_image_s4_one": [str(min(image)), str(max(image))],
                "rank4_box_has_solution_s4_one": overlap4,
                "no_joint_confidence_interpretation": True,
            })
    check("derived_text_matches_JSON_originalText", derived.read_text().strip() == text.strip())
    after = {str(p.relative_to(ROOT)): sha(p) for p in (original, derived)}
    check("supplied_primary_files_not_changed", before == after)
    report = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "runtime": {"python": platform.python_version(), "sympy": sp.__version__},
        "script_sha256": sha(Path(__file__)),
        "supplied_primary": {
            "hashes_before": before, "hashes_after": after,
            "JSON_field": "full-text-retrieval-response.originalText",
            "originalText_characters": len(text),
            "table1_365_offset_zero_based": text.find("365.0 62.5"),
            "table1_461_offset_zero_based": text.find("461.8 6.2"),
            "alignment_attenuation_offset_zero_based": text.find("attenuation factors"),
            "boundary": "User reports only page-one visual PDF; OCR missing signs cannot be certified.",
        },
        "rank2": {
            "standard_F2_reference": str(reference_f2),
            "matrix": [[str(matrix[i, k]) for k in range(2)] for i in range(2)],
            "quotient": str(quotient),
            "eigenvalue_minimum": {"exact": str(lower), "float": float(lower)},
            "eigenvalue_maximum": {"exact": str(upper), "float": float(upper)},
            "delta_at_minimum_in_declared_phase": str(delta_min),
            "central_A2_ratio": str(central),
            "central_s2_minimum_for_positive_s2": {"exact": str(s2_needed), "float": float(s2_needed)},
            "ENSDF_one_margin_s2_threshold": float((-sp.Rational(67, 24))/lower),
            "correct_forward_relation": "A2_target/A2_reference = s2*g2*q(delta); g2=1 only for common selected parent density",
            "boundary": "This bound cancels common rank2 orientation; it does not determine actual Q2 or actual delta.",
        },
        "uncertainty_scenarios": rows,
        "interpretation": [
            "The user's matrix and eigenvalue lower bound are correct in the stated phase convention.",
            "The rank2 central mismatch assumes s2=1 and g2=1; positive response alone is insufficient.",
            "ENSDF one-marginal box misses the rank2 range, but s2 about 1.018507 already permits contact.",
            "The literal OCR one-marginal rank2 box overlaps; this is provisional uncertainty sensitivity.",
            "The literal OCR two-marginal rank4 box overlaps at s4=1, unlike the ENSDF box.",
            "Do not use the 701.4-keV-specific nuclear attenuation alpha2/alpha4 as global rho or detector Q.",
            "Rank2 and rank4 summaries share sources and potentially fit/calibration covariance; do not count as independent confirmations.",
            "No OCR missing sign, original table error or 2024 fit error is diagnosed.",
        ],
        "checks": checks, "passed": all(c["passed"] for c in checks),
        "number_of_checks": len(checks),
    }
    (HERE / "rank2-result.json").write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({
        "passed": report["passed"], "checks": len(checks), "matrix": report["rank2"]["matrix"],
        "lower_eigenvalue": report["rank2"]["eigenvalue_minimum"],
        "central_s2_minimum": report["rank2"]["central_s2_minimum_for_positive_s2"],
        "scenario_results": [{"scenario": r["scenario"], "n": r["marginal_error_multiplier"],
                              "rank2_overlap": r["rank2_box_has_solution_s2_one"],
                              "rank4_overlap": r["rank4_box_has_solution_s4_one"]}
                             for r in rows],
        "output": str(HERE / "rank2-result.json"),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
