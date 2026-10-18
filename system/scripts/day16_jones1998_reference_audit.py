#!/usr/bin/env python3
"""Replay declared point-reference theory and the J98/J02 calibration crosswalk.

No original spectra, gate efficiency or fit covariance is recovered here.
"""
from __future__ import annotations

import argparse
from datetime import datetime
from decimal import Decimal
import hashlib
import json
import math
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import sympy as sp
from sympy.physics.wigner import clebsch_gordan

from day16_co60_conditional_stokes import LINEAR_BASIS, operators
from day16_gretina_convention_audit import coefficients


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def point_population(ji2: int) -> np.ndarray:
    assert ji2 % 2 == 1
    result = np.zeros(ji2+1)
    result[ji2//2:ji2//2+2] = .5
    return result


def photon_rate(ji2: int, jf2: int, parts: tuple, theta: float, pop: np.ndarray,
                basis: str = "native") -> tuple[float, float]:
    op = operators(ji2, jf2, parts, theta, 0., basis)
    matrix = np.einsum("ami,i,bmi->ab", op, pop, op.conj())
    assert np.linalg.eigvalsh(matrix).min() >= -1e-14
    linear = LINEAR_BASIS @ matrix @ LINEAR_BASIS.conj().T
    return (4*math.pi*float(np.trace(linear).real),
            4*math.pi*float((linear[0, 0]-linear[1, 1]).real))


def full_trace(row: dict, pop: np.ndarray, basis: str = "native") -> dict:
    mode = row["multipole"]
    if mode == "mixed":
        delta = row["delta_RB"] * (-1 if basis == "native" else 1)
        parts = (("M", 1, 1.), ("E", 2, delta))
    else:
        parts = ((mode[0], int(mode[1:]), 1.),)
    nodes, weights = np.polynomial.legendre.leggauss(8)
    values = np.array([photon_rate(row["Ji2"], row["Jf2"], parts,
                                  math.acos(float(x)), pop, basis)[0] for x in nodes])
    a0 = float(weights @ values / 2)
    a2 = float(5/2 * weights @ (values*np.polynomial.legendre.legval(nodes, [0, 0, 1])))
    a4 = float(9/2 * weights @ (values*np.polynomial.legendre.legval(nodes, [0, 0, 0, 0, 1])))
    i, q = photon_rate(row["Ji2"], row["Jf2"], parts, math.pi/2, pop, basis)
    assert abs(a0-1) < 1e-12 and i > 1e-13
    return {"a0": a0, "a2": a2, "a4": a4, "W90": i, "Q90": q, "P90": q/i}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.contract.read_text())
    assert cfg["identity"] == "J98-ALPHA-GAMMA-REFERENCE-AUDIT-01" and cfg["version"] == 2
    assert len(cfg["rows"]) == cfg["source_row_count_verified_visual"] == 47
    assert sha(Path(cfg["raw"])) == cfg["raw_sha256"]
    assert sha(Path(cfg["J02raw"])) == cfg["J02raw_sha256"]
    populations = []
    for ji2 in sorted({row["Ji2"] for row in cfg["rows"]}):
        j = sp.Rational(ji2, 2)
        for ell in [(ji2-1)//2, (ji2+1)//2]:
            p = np.array([sum(abs(float(clebsch_gordan(j, ell, sp.Rational(1, 2),
                sp.Rational(m, 2), 0, m0)))**2/2 for m0 in [sp.Rational(-1, 2), sp.Rational(1, 2)])
                for m in range(-ji2, ji2+1, 2)])
            p /= p.sum()
            assert np.max(abs(p-point_population(ji2))) < 1e-14
            populations.append({"Ji2": ji2, "alpha_L": ell, "point_daughter_population": p.tolist()})
    results = []
    maximum_racah_trace_error = maximum_phase_bridge_error = 0.
    for row in cfg["rows"]:
        pop = point_population(row["Ji2"])
        mode = row["multipole"]
        delta = None if mode == "E2" else (row["delta_RB"] if mode == "mixed" else 0.)
        racah = coefficients(row["Ji2"], row["Jf2"], pop, delta)
        racah_p = racah["P90_parity_plus"] * (-1 if mode == "E1" else 1)
        value = full_trace(row, pop)
        rb = full_trace(row, pop, "RB")
        bridge = max(abs(rb[key]-value[key]) for key in value)
        maximum_phase_bridge_error = max(maximum_phase_bridge_error, bridge)
        error = max(abs(racah[key]-value[key]) for key in ["a2", "a4", "W90"])
        error = max(error, abs(racah_p-value["P90"]))
        maximum_racah_trace_error = max(maximum_racah_trace_error, error)
        control = None
        if mode == "mixed":
            wrong = dict(row, delta_RB=-row["delta_RB"])
            wrong_value = full_trace(wrong, pop)
            control = {key: wrong_value[key] for key in ["a2", "a4", "P90"]}
        printed = {}
        for year in [1998, 2002]:
            if row[f"a2_{year}"] is not None:
                printed[str(year)] = {key: {"printed": row[f"{key}_{year}"],
                    "calculated": value[key], "residual": value[key]-row[f"{key}_{year}"],
                    "inside_literal_2dp_cell": abs(value[key]-row[f"{key}_{year}"]) <= .005+1e-12}
                    for key in ["a2", "a4"]}
        if row["P90_2002_theory"] is not None:
            printed["P2002"] = {"printed": row["P90_2002_theory"], "calculated": value["P90"],
                "residual": value["P90"]-row["P90_2002_theory"]}
        results.append({"identity": {key: row[key] for key in ["parent_keV", "gamma_keV", "Ji2", "Jf2", "multipole", "delta_RB"]},
            "point_reference_model": value, "Racah_trace_error": error, "native_RB_bridge_error": bridge,
            "same_signed_delta_wrong_basis_control": control, "printed_diagnostics": printed})
    assert maximum_racah_trace_error < 1e-12 and maximum_phase_bridge_error < 1e-12
    m = cfg["mixture"]
    e1 = np.array([m["E1_a2"], m["E1_a4"]])
    e2 = np.array([m["E2_a2"], m["E2_a4"]])
    y = np.array([m["measured_a2"], m["measured_a4"]])
    sig = np.array([m["sigma_a2"], m["sigma_a4"]])
    d = e2-e1
    f = (y-e1)/d
    f_sigma = sig/abs(d)
    lower = max(f-f_sigma)
    upper = min(f+f_sigma)
    assert 0 < lower < upper < 1
    def total_fraction(photon_fraction):
        return photon_fraction*(1+m["CC_E2"])/(photon_fraction*(1+m["CC_E2"])
            +(1-photon_fraction)*(1+m["CC_E1"]))
    n = np.array([-d[1], d[0]])
    residual = float(n @ (y-e1))
    variance_limits = [(abs(n[0])*sig[0]-abs(n[1])*sig[1])**2,
                       (abs(n[0])*sig[0]+abs(n[1])*sig[1])**2]
    interval = [math.sqrt(v) for v in variance_limits]
    assert min(interval) > abs(residual)
    cap = cfg["PIN_component_design"]
    radius, distance = cap["collimator_radius_mm"], cap["distance_mm"]
    c = distance/math.hypot(distance, radius)
    q2, q4 = c*(1+c)/2, c*(1+c)*(7*c*c-3)/8
    # Physical null controls in both parity/multipole classes.
    nulls = [v for v in results if v["identity"]["Ji2"] == 1]
    assert len(nulls) == 5
    assert max(abs(v["point_reference_model"][key]) for v in nulls for key in ["a2", "a4", "P90"]) < 1e-12
    out = {"identity": cfg["identity"], "at": datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(),
        "contract_sha256": sha(args.contract), "script_sha256": sha(Path(__file__)),
        "source_sha256": cfg["raw_sha256"], "rows": results,
        "alpha_population_controls": populations, "point_reference_null_controls": len(nulls),
        "maximum_Racah_helicity_error": maximum_racah_trace_error,
        "maximum_native_RB_phase_bridge_error": maximum_phase_bridge_error,
        "literal2dp_nonclosure_rows": {str(year): [v["identity"] for v in results
            if str(year) in v["printed_diagnostics"] and not all(q["inside_literal_2dp_cell"]
               for q in v["printed_diagnostics"][str(year)].values())] for year in [1998, 2002]},
        "unresolved113_keV_design": {"E2_photon_fraction_from_each_moment": f.tolist(),
            "marginal_fraction_errors_only_fixed_theory": f_sigma.tolist(),
            "literal_marginal_box_overlap_not_jointCI": [float(lower), float(upper)],
            "line_normal_residual": residual, "line_normal_sigma_bounds_all_covariances": interval,
            "total_E2_fraction_at_individual_centrals": [total_fraction(v) for v in f],
            "equal_total_gamma_E1_over_E2": (1+m["CC_E2"])/(1+m["CC_E1"]),
            "equal_total_photon_E2_fraction": (1+m["CC_E1"])/(2+m["CC_E1"]+m["CC_E2"]),
            "actual_joint_fit_or_total_branch_recovered": False},
        "PIN_only_pointcap_design": {"half_angle_deg": math.degrees(math.acos(c)), "Q2_component": q2,
            "Q4_component": q4, "actual_total_source_gamma_Qk_recovered": False},
        "new_experimental_P_Q_delta_fit": False, "physical_claims_scope": cfg["scope"]}
    args.output.write_text(json.dumps(out, indent=2, allow_nan=False)+"\n")
    print(json.dumps({key: out[key] for key in ["maximum_Racah_helicity_error", "maximum_native_RB_phase_bridge_error",
        "point_reference_null_controls", "literal2dp_nonclosure_rows", "unresolved113_keV_design", "PIN_only_pointcap_design"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
