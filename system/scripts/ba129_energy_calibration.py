#!/usr/bin/env python3
"""Declared energy-only calibration of a paired single-j reference model.

The objective is descriptive relative-energy RMS, not a likelihood. The
ordinal state correspondence and parameter bounds come from a frozen input
contract. No photon intensity, lifetime or transfer strength enters the fit.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
import time

import numpy as np
from scipy.optimize import least_squares
import scipy

sys.path.insert(0, str(Path(__file__).resolve().parent / "analysis"))
from paired_single_j_rotor import (
    PairedRotorParameters, irrotational_moments, lambda_from_top_pair,
    single_particle_spectrum, solve, tilde_lambda_from_top_pair,
)


def parameters(x, contract):
    gamma, log_c = x[:2]
    c = math.exp(log_c)
    if contract.get("inertia_family", "irrotational") == "independent":
        moments = tuple(math.exp(value) for value in x[2:5])
        tilde = x[5]
        j0 = None
    else:
        j0, tilde = math.exp(x[2]), x[3]
        moments = irrotational_moments(j0, gamma)
    sp = single_particle_spectrum(contract["twice_j"], c, gamma)
    lam = lambda_from_top_pair(sp, tilde)
    return PairedRotorParameters(
        two_j=contract["twice_j"], C_MeV=c, gamma_deg=gamma,
        inertias_hbar2_per_MeV=moments,
        lambda_F_MeV=lam, Delta_MeV=contract["gap_MeV"],
    ), j0


def mapped_energies(x, contract):
    p, _ = parameters(x, contract)
    spins = sorted({r["twice_I"] for r in contract["energy_data"]})
    solutions = {spin: solve(spin, p) for spin in spins}
    anchor = next(r for r in contract["energy_data"] if r["level_id"] == contract["energy_reference_level"])
    offset = solutions[anchor["twice_I"]].eigenvalues_MeV[anchor["model_ordinal_assumed"]]
    prediction = [
        float(solutions[r["twice_I"]].eigenvalues_MeV[r["model_ordinal_assumed"]] - offset)
        for r in contract["energy_data"]
    ]
    return np.array(prediction), solutions


def fit(contract_path: Path, output_dir: Path):
    root = Path(__file__).resolve().parents[2]
    contract = json.loads(contract_path.read_text())
    family = contract.get("inertia_family", "irrotational")
    if family not in {"irrotational", "independent"}:
        raise ValueError("unknown inertia family")
    runner_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    model_path = root / "system/scripts/analysis/paired_single_j_rotor.py"
    model_hash = hashlib.sha256(model_path.read_bytes()).hexdigest()
    source = root / contract["source_raw"]
    if hashlib.sha256(source.read_bytes()).hexdigest() != contract["source_sha256"]:
        raise ValueError("energy source hash mismatch")
    rows = contract["energy_data"]
    anchor = next(r for r in rows if r["level_id"] == contract["energy_reference_level"])
    reference_energy = anchor["energy_keV"]
    mask = np.array([r["level_id"] != contract["energy_reference_level"] for r in rows])
    observed = np.array([(r["energy_keV"] - reference_energy) / 1000 for r in rows])
    b = contract["fit_parameters"]
    def bound(side):
        values = [b["gamma_deg"][side], math.log(b["field_strength_MeV"][side])]
        if family == "independent":
            values += [math.log(b[f"J{k}_hbar2_per_MeV"][side]) for k in (1, 2, 3)]
        else:
            values.append(math.log(b["J0_hbar2_per_MeV"][side]))
        return values + [b["lambda_tilde_top_pair"][side]]
    lower, upper = bound(0), bound(1)
    output_dir.mkdir(parents=True, exist_ok=True)
    starts = []
    initial_key = ("initial_points_gamma_C_J1_J2_J3_lambda" if family == "independent"
                   else "initial_points_gamma_C_J0_lambda")
    for number, initial in enumerate(contract[initial_key]):
        x0 = [initial[0], *[math.log(value) for value in initial[1:-1]], initial[-1]]
        calls = 0
        start_time = time.perf_counter()
        def residual(x):
            nonlocal calls
            calls += 1
            pred, _ = mapped_energies(x, contract)
            return (pred - observed)[mask]
        result = least_squares(
            residual, x0, bounds=(lower, upper), x_scale="jac",
            xtol=contract["optimizer_tolerance"], ftol=contract["optimizer_tolerance"],
            gtol=contract["optimizer_tolerance"], max_nfev=contract["optimizer_max_nfev"],
        )
        pred, sols = mapped_energies(result.x, contract)
        p, j0 = parameters(result.x, contract)
        error = (pred - observed) * 1000
        row = {
            "start": number, "inertia_family": family, "initial_physical_coordinates": initial,
            "optimizer_success": bool(result.success), "optimizer_message": result.message,
            "function_evaluations_reported": result.nfev, "actual_residual_calls": calls,
            "elapsed_seconds": time.perf_counter() - start_time,
            "model_parameters": {"two_j": p.two_j, "C_MeV": p.C_MeV,
                "gamma_deg": p.gamma_deg, "J0_hbar2_per_MeV": j0,
                "lambda_tilde_top_pair": float(result.x[-1]),
                "lambda_F_MeV": p.lambda_F_MeV, "Delta_MeV": p.Delta_MeV,
                "inertias_hbar2_per_MeV": list(p.inertias_hbar2_per_MeV)},
            "RMS_residual_keV_excluding_anchor": float(np.sqrt(np.mean(error[mask] ** 2))),
            "maximum_abs_residual_keV": float(max(abs(error[mask]))),
            "active_bound_mask": result.active_mask.tolist(),
            "energy_comparison": [
                {**original, "model_relative_energy_keV": float(calculated * 1000),
                 "observed_relative_energy_keV": float(experimental * 1000),
                 "residual_keV": float(err)}
                for original, calculated, experimental, err in zip(rows, pred, observed, error)
            ],
            "maximum_D2_leakage_MeV": max(s.d2_leakage_MeV for s in sols.values()),
            "minimum_low_two_spacing_keV": min(float((s.eigenvalues_MeV[1]-s.eigenvalues_MeV[0])*1000) for s in sols.values()),
            "parameter_coordinates_internal": result.x.tolist(),
        }
        starts.append(row)
        (output_dir / f"energy-fit-start-{number}.json").write_text(json.dumps(row, indent=2) + "\n")
        print(json.dumps({"start": number, "success": row["optimizer_success"],
                          "RMS_keV": row["RMS_residual_keV_excluding_anchor"],
                          "seconds": row["elapsed_seconds"]}), flush=True)

    best = min(starts, key=lambda r: r["RMS_residual_keV_excluding_anchor"])
    x = best["parameter_coordinates_internal"]
    p, j0 = parameters(x, contract)
    dual_sp = single_particle_spectrum(p.two_j, p.C_MeV, 60 - p.gamma_deg)
    dual_tilde = tilde_lambda_from_top_pair(dual_sp, -p.lambda_F_MeV)
    if family == "independent":
        dual_x = [60 - p.gamma_deg, x[1], x[2], x[4], x[3], dual_tilde]
    else:
        dual_x = [60 - p.gamma_deg, x[1], x[2], dual_tilde]
    pred, solutions = mapped_energies(x, contract)
    dual_pred, dual_solutions = mapped_energies(dual_x, contract)
    dual_error = max(float(np.max(abs(solutions[i].eigenvalues_MeV
                                     - dual_solutions[i].eigenvalues_MeV))) for i in solutions)
    assert dual_error < 1e-9
    result = {
        "scope": "descriptive energy calibration of the declared positive-BCS single-j model",
        "inertia_family": family,
        "contract": str(contract_path), "contract_sha256": hashlib.sha256(contract_path.read_bytes()).hexdigest(),
        "model_sha256": model_hash,
        "runner_sha256": runner_hash,
        "runtime": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
        "starts": starts, "best_start": best["start"], "best": best,
        "energy_equivalent_partner": {
            "gamma_deg": 60 - p.gamma_deg, "lambda_F_MeV": -p.lambda_F_MeV,
            "lambda_tilde_top_pair": dual_tilde, "maximum_full_spectrum_difference_MeV": dual_error,
            "same_model_symmetry_not_an_independent_physical_hypothesis": True,
        },
        "boundaries": [
            "No electromagnetic data are fitted or predicted by this program.",
            "RMS is not experimental chi-square, confidence coverage or a mode assignment.",
            "Ordinal mapping, fixed gap, field convention, bounds and inertia family are assumptions.",
            "Multiple starts do not prove a global optimum or a unique parameter solution.",
            "The original Gizon numerical implementation is not claimed to be reproduced.",
        ],
    }
    if (hashlib.sha256(model_path.read_bytes()).hexdigest() != model_hash
            or hashlib.sha256(Path(__file__).read_bytes()).hexdigest() != runner_hash):
        raise RuntimeError("calculation code changed during the run; provenance is not stable")
    (output_dir / "energy-calibration.json").write_text(json.dumps(result, indent=2) + "\n")
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    fit(args.contract, args.output_dir)
