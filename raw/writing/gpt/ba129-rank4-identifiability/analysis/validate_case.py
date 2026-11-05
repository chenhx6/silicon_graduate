#!/usr/bin/env python3
"""Check physical input identity, independent algebra and profile numerics."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
import tempfile

import numpy as np

from companion_profile import analyze as profile
from rank4_invariant import analyze, load_rows


def validate(root: Path, wiki_root: Path | None = None) -> dict:
    csv_path = root / "data/ba129_same_parent_A4.csv"
    rows = load_rows(csv_path)
    result = analyze(csv_path)
    saved = json.loads((root / "analysis/results/rank4-invariant.json").read_text())
    assert result == saved, "saved rank-4 output is stale"
    rerun = profile(root)
    old_profile = json.loads((root / "analysis/results/companion-profile.json").read_text())
    assert np.allclose([c["global"]["distance"] for c in rerun["cases"]],
                       [c["global"]["distance"] for c in old_profile["cases"]], atol=1e-10, rtol=1e-10)
    assert rerun["script_sha256"] == old_profile["script_sha256"]
    assert rerun["input_sha256"] == old_profile["input_sha256"]
    assert rerun["contract_sha256"] == old_profile["contract_sha256"]
    with csv_path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames
        originals = list(reader)
    failures_rejected = []
    with tempfile.TemporaryDirectory(prefix="ba129-validation-") as temp:
        cases = {
            "duplicate_target": [*originals, dict(originals[0])],
            "different_parent_id": [dict(originals[0]), {**originals[1], "parent_id": "different-level"}],
            "different_parent_spin": [dict(originals[0]), {**originals[1], "Ji_twice": "15"}],
            "nonfinite_coefficient": [{**originals[0], "A4": "nan"}, dict(originals[1])],
            "nonpositive_error": [{**originals[0], "A4_sigma": "-0.05"}, dict(originals[1])],
            "zero_ratio_denominator": [dict(originals[0]), {**originals[1], "A4": "0"}],
            "wrong_reference_multipoles": [dict(originals[0]), {**originals[1], "multipolarity": "M1+E2"}],
        }
        for name, test_rows in cases.items():
            path = Path(temp) / (name + ".csv")
            with path.open("w", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(test_rows)
            try:
                load_rows(path)
            except ValueError:
                failures_rejected.append(name)
            else:
                raise AssertionError(f"invalid physics input accepted: {name}")
        zero_rows = load_rows(Path(temp) / "zero_ratio_denominator.csv", require_reference_nonzero=False)
        assert zero_rows["reference_462"]["A4"] == 0

    exact = {}
    try:
        from sympy import Rational as R, Matrix, sqrt, simplify, symbols, lambdify
        from sympy.physics.wigner import clebsch_gordan, wigner_6j, wigner_d_small
    except ImportError:
        exact["status"] = "not-run: install declared optional SymPy validation dependency"
    else:
        ji = R(13, 2)
        def coefficient(jf, k, a, b):
            return ((-1) ** (ji + jf + a + b - 1) * sqrt((2*a+1)*(2*b+1)*(2*ji+1))
                    * clebsch_gordan(a, b, k, 1, -1, 0) * wigner_6j(ji, ji, k, b, a, jf))
        ft, fr = coefficient(R(11,2), 4, 2, 2), coefficient(R(9,2), 4, 2, 2)
        assert simplify(ft/fr) == -R(8,3)
        ref2 = coefficient(R(9,2), 2, 2, 2)
        mat = Matrix([[simplify(coefficient(R(11,2), 2, a, b)/ref2) for b in [1,2]] for a in [1,2]])
        assert mat == Matrix([[-R(7,10), 7*sqrt(11)/10], [7*sqrt(11)/10, -R(1,10)]])
        eigen = set(mat.eigenvals())
        assert eigen == {(-2-sqrt(137))/5, (-2+sqrt(137))/5}
        assert clebsch_gordan(1,2,4,1,-1,0) == 0
        exact = {"status": "passed", "rank4_ratio": str(simplify(ft/fr)),
                 "rank2_matrix": str(mat), "rank2_eigenvalues": sorted(map(str, eigen))}
        # Pure-E2 photon-amplitude route uses standard CG and rotation matrices,
        # not the case script's Racah/CG implementation or coefficient formula.
        angle = symbols("angle", real=True)
        d_function = lambdify(angle, wigner_d_small(2, angle), "numpy")
        x, weights = np.polynomial.legendre.leggauss(16)
        d_matrices = [d_function(np.arccos(c)) for c in x]
        p4 = np.polynomial.legendre.legval(x, [0, 0, 0, 0, 1])
        photon_checks = []
        normalization_errors = []
        for twice_mi in range(-13, 14, 2):
            coefficients = []
            for twice_jf in (11, 9):
                intensity = np.zeros_like(x)
                for twice_mf in range(-twice_jf, twice_jf + 1, 2):
                    mu = (twice_mi - twice_mf) // 2
                    if abs(mu) > 2:
                        continue
                    cg = float(clebsch_gordan(R(twice_jf, 2), 2, ji,
                                             R(twice_mf, 2), mu, R(twice_mi, 2)))
                    helicity_sum = np.array([d[2-mu, 1]**2 + d[2-mu, 3]**2 for d in d_matrices])
                    intensity += 2.5 * cg**2 * helicity_sum
                integral = weights @ intensity
                normalization_errors.append(abs(integral / 2 - 1))
                coefficients.append(float(9 * (weights @ (intensity * p4)) / integral))
            photon_checks.append(abs(coefficients[0] + (8 / 3) * coefficients[1]))
        assert max(photon_checks) < 1e-12
        assert max(normalization_errors) < 1e-12
        exact.update(photon_substates_checked=14,
                     maximum_photon_route_cancellation_error=max(photon_checks),
                     maximum_photon_normalization_error=max(normalization_errors))

    upstream = []
    if wiki_root:
        contract = json.loads((root / "data/input-contract.json").read_text())
        entries = [contract["canonical_summary"], *contract["uncertainty_scenarios"][1:]]
        for entry in entries:
            path = wiki_root / entry["upstream_raw"]
            assert hashlib.sha256(path.read_bytes()).hexdigest() == entry["upstream_sha256"]
            upstream.append(entry["upstream_raw"])
    return {"ok": True, "rows": len(rows), "profile_cases": len(rerun["cases"]),
            "invalid_inputs_rejected": failures_rejected, "independent_sympy": exact,
            "upstream_hashes_checked": upstream, "numerical_controls": rerun["controls"],
            "scope": "code, identity and algebra validation; no experimental or novelty certification"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--wiki-root", type=Path)
    args = parser.parse_args()
    print(json.dumps(validate(Path(__file__).resolve().parents[1], args.wiki_root), indent=2))
