#!/usr/bin/env python3
"""Source-specific even-core checks for the 129Ba model investigation.

The rigid-rotor trace identity holds for three constant principal inertias.
Its failure does not distinguish gamma softness from other omitted dynamics.
The E2 calculation is a declared irrotational-rotor comparison, not a fit
of a measured shape. Experimental source versions are retained separately.
"""
from __future__ import annotations

import csv
from decimal import Decimal
import hashlib
import json
import math
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent / "analysis"))
from paired_single_j_em import clebsch_gordan

RAW = ROOT / "raw/papers/gpt/query/20261105-ba129-core-constraints"
OUT = ROOT / "outputs/l4/20261105-ba129-controlled-pairing/core"
SELECTION = {
    128: {"2_1": "284.00", "2_2": "884.50", "3_1": "1324.37", "4_1": "763.32"},
    130: {"2_1": "357.38", "2_2": "908.02", "3_1": "1361.06", "4_1": "901.85"},
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def levels(path, mass):
    result = {}
    for line_number, line in enumerate(path.read_text().splitlines(), 1):
        s = line.ljust(80)
        if s[:5] == f"{mass}BA" and s[5:9] == "  L ":
            energy, error = s[9:19].strip(), s[19:21].strip()
            result[energy] = {
                "energy_keV": float(energy), "energy_literal": energy,
                "quoted_error_keV": float(Decimal(error) * Decimal(10) ** Decimal(energy).as_tuple().exponent)
                if error.isdigit() else None,
                "Jpi_literal": s[21:39].strip(), "half_life_literal": s[39:49].strip(),
                "half_life_error_literal": s[49:55].strip(),
                "band_flag_literal": s[76:77].strip(), "locator": f"line {line_number}",
            }
    return result


def spin(R):
    m = np.arange(-R, R + 1)
    raising = np.diag(np.sqrt((R - m[:-1]) * (R + m[:-1] + 1)), -1)
    return (raising + raising.T)/2, (raising - raising.T)/(2j), np.diag(m)


def basis(R):
    columns = []
    for k in range(0, R + 1, 2):
        if k == 0 and R % 2:
            continue
        v = np.zeros(2*R + 1)
        if k == 0:
            v[R] = 1
        else:
            v[R+k], v[R-k] = 1/math.sqrt(2), (-1)**R/math.sqrt(2)
        columns.append(v)
    return np.column_stack(columns) if columns else np.empty((2*R+1, 0))


def rotor(R, constants):
    """A_k=hbar²/(2J_k), in any one common energy unit."""
    p = basis(R)
    h = sum(a * j @ j for a, j in zip(constants, spin(R)))
    return np.linalg.eigh(p.T @ h @ p), p


def rme(Ri, Rf, gamma_deg, constants):
    (_, vi), pi = rotor(Ri, constants)
    (_, vf), pf = rotor(Rf, constants)
    q = {0: math.cos(math.radians(gamma_deg)),
         -2: math.sin(math.radians(gamma_deg))/math.sqrt(2),
         2: math.sin(math.radians(gamma_deg))/math.sqrt(2)}
    product = np.zeros((2*Rf+1, 2*Ri+1))
    for ki in range(-Ri, Ri+1):
        for nu, value in q.items():
            kf = ki+nu
            if abs(kf) <= Rf:
                product[kf+Rf, ki+Ri] += math.sqrt(2*Ri+1)*clebsch_gordan(
                    2*Ri, 2*ki, 4, 2*nu, 2*Rf, 2*kf)*value
    return vf.conj().T @ pf.T @ product @ pi @ vi


def branch_test(gamma_deg):
    moments = np.array([math.sin(math.radians(gamma_deg)-2*math.pi*k/3)**2
                        for k in (1, 2, 3)])
    if np.min(moments) < 1e-15:
        raise ValueError("evaluate the axial limit at nonzero gamma")
    constants = 1/(2*moments)
    m20, m22 = rme(2, 0, gamma_deg, constants), rme(2, 2, gamma_deg, constants)
    b20, b22 = abs(m20[0, 1])**2/5, abs(m22[0, 1])**2/5
    b02 = np.abs(rme(0, 2, gamma_deg, constants)[:, 0])**2
    s2 = math.sin(3*math.radians(gamma_deg))**2
    d = 9-8*s2
    analytic_ratio = 7/20 * (d-(3-2*s2)*math.sqrt(d))/s2
    return {"gamma_deg": gamma_deg, "unit_B_2second_to_0": float(b20),
            "unit_B_2second_to_2first": float(b22),
            "ratio_matrix": float(b20/b22), "ratio_analytic": analytic_ratio,
            "total_unit_0_to_2_strength": float(b02.sum())}


def main():
    source_hashes = {}
    results = {}
    for mass, chosen in SELECTION.items():
        path = RAW / f"nndc{mass}-adopted-text.ens"
        source_hashes[str(path.relative_to(ROOT))] = digest(path)
        found = levels(path, mass)
        selected = {key: found[value] for key, value in chosen.items()}
        e21, e22, e3, e4 = (selected[k]["energy_keV"] for k in ("2_1", "2_2", "3_1", "4_1"))
        difference = e3-e21-e22
        ratio = e22/e21
        sin2 = 9*ratio/(2*(1+ratio)**2)
        gamma = math.degrees(math.asin(math.sqrt(sin2)))/3 if 0 <= sin2 <= 1 else None
        results[str(mass)] = {
            "source": str(path.relative_to(ROOT)), "selected_levels": selected,
            "E3_minus_sum_E2_keV": difference, "difference_over_E2first": difference/e21,
            "equal_weight_three_energy_RMS_lower_bound_keV": abs(difference)/3,
            "R_4_over_2": e4/e21, "E2second_over_E2first": ratio,
            "irrotational_gamma_from_two_energies_only_deg": gamma,
            "other_gamma_branch_deg": 60-gamma if gamma is not None else None,
            "conditional_irrotational_E2_prediction": branch_test(gamma) if gamma is not None else None,
        }
    rng = np.random.default_rng(20261105)
    max_trace = max_closed = 0.
    for constants in np.exp(rng.uniform(-4, 3, (64, 3))):
        (e2, _), _ = rotor(2, constants)
        (e3, _), _ = rotor(3, constants)
        a, b, c = constants
        disc = a*a+b*b+c*c-a*b-a*c-b*c
        closed = 2*sum(constants) + np.array([-2, 2])*math.sqrt(max(0, disc))
        max_trace = max(max_trace, abs(e3[0]-sum(e2)))
        max_closed = max(max_closed, float(max(abs(e2-closed))))
    tests = [branch_test(g) for g in (0.1, 1, 10, 20, 24, 29, 30, 31, 40, 50, 59, 59.9)]
    checks = {
        "random_positive_inertia_cases": 64,
        "maximum_trace_identity_residual": float(max_trace),
        "maximum_I2_closed_form_residual": max_closed,
        "maximum_E2_ratio_matrix_vs_analytic_residual": max(abs(t["ratio_matrix"]-t["ratio_analytic"]) for t in tests),
        "maximum_E2_upward_closure_residual": max(abs(t["total_unit_0_to_2_strength"]-1) for t in tests),
        "gamma30_forbidden_branch_unit_B": branch_test(30)["unit_B_2second_to_0"],
        "small_gamma_ratio_0p1_deg": branch_test(0.1)["ratio_matrix"],
    }
    assert max_trace < 1e-10 and max_closed < 1e-10
    assert checks["maximum_E2_ratio_matrix_vs_analytic_residual"] < 1e-9
    assert checks["maximum_E2_upward_closure_residual"] < 1e-12
    assert checks["gamma30_forbidden_branch_unit_B"] < 1e-25
    assert abs(checks["small_gamma_ratio_0p1_deg"]-.7) < 1e-4
    ko = ROOT / "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/纲图/2001_Königshofen et al_Multipole mixing ratios in 130 Ba.pdf"
    source_hashes[str(ko.relative_to(ROOT))] = digest(ko)
    photon_ratio = .74
    delta = -75.
    ko_ratio = photon_ratio*(550.5/907.7)**5*(1+delta**2)/delta**2
    comparison = {
        "source": str(ko.relative_to(ROOT)), "locator": "printed037302-2 TableI, first two rows; visually checked",
        "gamma_keV": [907.7, 550.5], "photon_ratio": photon_ratio,
        "delta_E2_over_M1_Rose_Brink": delta, "delta_quoted_margin": 20.,
        "reported_relative_B_E2_ratio": .061, "reported_margin": .002,
        "derived_from_same_photon_and_mixing_inputs": ko_ratio,
        "irrotational_prediction_from_separate_2001_ENSDF_two_energy_version":
            results["130"]["conditional_irrotational_E2_prediction"]["ratio_matrix"],
        "not_independent_of_original_RI_delta": True,
        "source_versions_not_pooled_into_likelihood": True,
    }
    dp_path = RAW / "nndc131-dp-text.ens"
    source_hashes[str(dp_path.relative_to(ROOT))] = digest(dp_path)
    dp_rows = [s.ljust(80) for s in dp_path.read_text().splitlines() if s.ljust(80)[5:9] == "  L "]
    dp_check = {"level_count": len(dp_rows),
                "literal_L_fields": sorted({s[55:64].strip() for s in dp_rows}),
                "number_with_explicit_L5": sum(s[55:64].strip() in {"5", "(5)"} for s in dp_rows),
                "boundary": "No explicit l=5 strength in this evaluated object; blank L or S fields are not zero strength or upper limits. Evaluation cutoff2006 is not an exhaustive2026 literature survey."}
    for name, sha in source_hashes.items():
        assert digest(ROOT/name) == sha
    OUT.mkdir(parents=True, exist_ok=True)
    record = {"scope": "constant-inertia core and source-specific operator constraints",
              "source_hashes": source_hashes, "runner_sha256": digest(Path(__file__)),
              "core_results": results, "mathematical_checks": checks,
              "konigshofen2001_branch_check": comparison, "131Ba_addition_data_readiness": dp_check,
              "boundaries": ["No experimental covariance or confidence level supplied.",
                             "A failed constant-inertia identity is not unique proof of gamma softness.",
                             "Two-energy gamma is a conditional model coordinate, not a measured shape.",
                             "The core-to-odd-system transfer still requires a polarization and pairing contract."]}
    (OUT/"core-constraints.json").write_text(json.dumps(record, indent=2, allow_nan=False)+"\n")
    with (OUT/"rotor-branch-controls.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(tests[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(tests)
    print(json.dumps({"core": {a: {k: v for k, v in r.items() if k not in {"selected_levels","conditional_irrotational_E2_prediction"}} for a,r in results.items()},
                      "E2_check": comparison, "checks": checks, "addition_readiness": dp_check}, indent=2))


if __name__ == "__main__":
    main()
