#!/usr/bin/env python3
"""Predict declared transfer and photon observables after energy calibration.

No parameter is optimized here. The one photon scale anchor and five withheld
pairs come from a pre-existing contract. Both members of the exact energy
duality and every recorded energy-fit start are retained. Reported intensity
errors are not used to manufacture a likelihood or significance.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict, replace
import hashlib
import json
from pathlib import Path
import platform
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent / "analysis"))
from paired_single_j_rotor import PairedRotorParameters, solve
from paired_single_j_transfer import strengths
from paired_single_j_em import unit_em


ROOT = Path(__file__).resolve().parents[2]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parameters(row):
    names = ("two_j", "C_MeV", "gamma_deg", "inertias_hbar2_per_MeV",
             "lambda_F_MeV", "Delta_MeV")
    return PairedRotorParameters(**{key: row["model_parameters"][key] for key in names})


def partner(p):
    j1, j2, j3 = p.inertias_hbar2_per_MeV
    return replace(p, gamma_deg=60 - p.gamma_deg, lambda_F_MeV=-p.lambda_F_MeV,
                   inertias_hbar2_per_MeV=(j1, j3, j2))


def transfer_prediction(solution, anchor_keV):
    result = strengths(solution)
    energies = 1000 * (solution.eigenvalues_MeV - solution.eigenvalues_MeV[0]) + anchor_keV
    reference = float(result.removal_strengths[0])
    excited_window = (energies < 2000) & (np.arange(len(energies)) > 0)
    return {
        "operator": "bare single-j removal/addition from even-core R=0",
        "sum_rule_error": result.sum_rule_error,
        "removal_sum": result.removal_sum,
        "addition_sum": result.addition_sum,
        "excited_below_2000keV_removal_over_first": (
            float(result.removal_strengths[excited_window].sum() / reference)
            if reference > 0 else None),
        "states": [
            {"ordinal": n, "model_excitation_keV": float(ex),
             "removal_strength": float(sr), "addition_strength": float(sa),
             "relative_removal_to_first": float(sr / reference) if reference > 0 else None}
            for n, (ex, sr, sa) in enumerate(zip(
                energies, result.removal_strengths, result.addition_strengths))
        ],
    }


def photon_prediction(solutions, mapping, contract):
    rows = []
    for pair in contract["pairs"]:
        parent = mapping[pair["parent_id"]]
        target = mapping[pair["target_final_id"]]
        reference = mapping[pair["reference_final_id"]]
        ip, it, ir = (row["model_ordinal_assumed"] for row in (parent, target, reference))
        target_em = unit_em(solutions[parent["twice_I"]], solutions[target["twice_I"]])
        reference_em = unit_em(solutions[parent["twice_I"]], solutions[reference["twice_I"]])
        bqt = float(target_em.collective_quadrupole.unit_B[it, ip])
        bjt = float(target_em.particle_j.unit_B[it, ip])
        bqr = float(reference_em.collective_quadrupole.unit_B[ir, ip])
        bjr = float(reference_em.particle_j.unit_B[ir, ip])
        if bqr <= 1e-20:
            raise ValueError("vanishing model E2 reference; the ratio contract is undefined")
        if bjr > 1e-20:
            raise ValueError("the reference has a nonzero rank-1 strength")
        et, er = pair["target_energy_MeV"], pair["reference_energy_MeV"]
        rows.append({
            **pair, "unit_BQ_target": bqt, "unit_Bj_target": bjt, "unit_BQ_reference": bqr,
            "electric_ratio_a": (et / er) ** 5 * bqt / bqr,
            "magnetic_ratio_coefficient_b_per_MeV2": et ** 3 / er ** 5 * bjt / bqr,
        })
    anchors = [r for r in rows if r["role"] == "scale-calibration"]
    if len(anchors) != 1:
        raise ValueError("exactly one predeclared scale anchor is required")
    anchor = anchors[0]
    b = anchor["magnetic_ratio_coefficient_b_per_MeV2"]
    if b <= 1e-20:
        eta = None
        status = "anchor-has-no-magnetic-sensitivity"
    else:
        eta = (anchor["reported_photon_ratio"] - anchor["electric_ratio_a"]) / b
        status = "central-anchor-calibrated" if eta >= 0 else "negative-scale-required-anchor-fails"
    for row in rows:
        a, b = row["electric_ratio_a"], row["magnetic_ratio_coefficient_b_per_MeV2"]
        row["eta_required_by_individual_central_ratio_MeV2"] = (
            (row["reported_photon_ratio"] - a) / b if b > 1e-20 else None)
        prediction = a + eta * b if eta is not None and eta >= 0 else None
        row["predicted_photon_ratio"] = prediction
        row["prediction_over_reported_ratio"] = (
            prediction / row["reported_photon_ratio"] if prediction is not None else None)
        row["predicted_radiative_E2_fraction"] = (
            a / prediction if prediction is not None and prediction > 0 else None)
    return {"status": status, "anchor_eta_MeV2": eta, "pairs": rows}


def run(fit_paths, contract_path, output_dir):
    code_paths = [Path(__file__), *[
        ROOT / "system/scripts/analysis" / name for name in (
            "paired_single_j_rotor.py", "paired_single_j_em.py",
            "paired_single_j_transfer.py")]]
    locked = {path: sha(path) for path in [*code_paths, contract_path, *fit_paths]}
    contract = json.loads(contract_path.read_text())
    branch_file = contract_path.parent / "lifetime/branches.csv"
    if sha(branch_file) != contract["normalized_branch_input_sha256"]:
        raise ValueError("photon branch input hash mismatch")
    locked[branch_file] = sha(branch_file)
    all_rows, checks = [], []
    for fit_path in fit_paths:
        fit = json.loads(fit_path.read_text())
        if fit["model_sha256"] != sha(code_paths[1]):
            raise ValueError(f"energy-fit model code differs: {fit_path}")
        fit_contract_path = ROOT / fit["contract"]
        if sha(fit_contract_path) != fit["contract_sha256"]:
            raise ValueError("energy contract hash mismatch")
        fit_contract = json.loads(fit_contract_path.read_text())
        locked[fit_contract_path] = sha(fit_contract_path)
        energy_source = ROOT / fit_contract["source_raw"]
        if sha(energy_source) != fit_contract["source_sha256"]:
            raise ValueError("energy source hash mismatch")
        locked[energy_source] = sha(energy_source)
        mapping = {row["level_id"]: row for row in fit_contract["energy_data"]}
        anchor_keV = mapping[fit_contract["energy_reference_level"]]["energy_keV"]
        spins = {r["twice_I"] for r in mapping.values()} | {fit_contract["twice_j"]}
        for fit_start in fit["starts"]:
            original = parameters(fit_start)
            pair_outputs = []
            pair_solutions = []
            for dual, p in ((False, original), (True, partner(original))):
                solutions = {spin: solve(spin, p) for spin in sorted(spins)}
                pair_solutions.append(solutions)
                row = {
                    "energy_fit": str(fit_path.relative_to(ROOT)),
                    "energy_start": fit_start["start"], "dual_partner": dual,
                    "is_recorded_best_start": fit_start["start"] == fit["best_start"],
                    "energy_RMS_keV": fit_start["RMS_residual_keV_excluding_anchor"],
                    "active_energy_bound_mask": fit_start["active_bound_mask"],
                    "parameters": asdict(p),
                    "transfer": transfer_prediction(solutions[p.two_j], anchor_keV),
                    "photon": photon_prediction(solutions, mapping, contract),
                }
                pair_outputs.append(row)
                all_rows.append(row)
            first, second = pair_outputs
            energy_error = max(float(np.max(abs(
                pair_solutions[0][spin].eigenvalues_MeV
                - pair_solutions[1][spin].eigenvalues_MeV))) for spin in spins)
            ta, tb = first["transfer"]["states"], second["transfer"]["states"]
            transfer_error = max(
                max(abs(a["removal_strength"] - b["addition_strength"]),
                    abs(a["addition_strength"] - b["removal_strength"]))
                for a, b in zip(ta, tb))
            em_error = max(
                abs(a[key] - b[key])
                for a, b in zip(first["photon"]["pairs"], second["photon"]["pairs"])
                for key in ("unit_BQ_target", "unit_Bj_target", "unit_BQ_reference"))
            checks.append({"energy_fit": str(fit_path.relative_to(ROOT)),
                           "energy_start": fit_start["start"],
                           "dual_energy_max_difference_MeV": energy_error,
                           "transfer_addition_removal_exchange_max_error": transfer_error,
                           "dual_unit_EM_B_max_difference": em_error})
            if energy_error > 1e-9 or transfer_error > 1e-8:
                raise RuntimeError("exact energy/transfer duality check failed")
    for path, digest in locked.items():
        if sha(path) != digest:
            raise RuntimeError(f"input changed during prediction: {path}")
    output = {
        "schema": "ba129-energy-calibrated-observables-v1",
        "runtime": {"python": platform.python_version(), "numpy": np.__version__},
        "hashes": {str(p.relative_to(ROOT)): digest for p, digest in locked.items()},
        "predictions": all_rows, "duality_checks": checks,
        "boundaries": [
            "No state or Hamiltonian parameter is selected using these photon results.",
            "One predeclared photon ratio determines eta; the other five are withheld observables.",
            "The six photon ratios share a publication/acquisition and are not independent experiments.",
            "Published photon energies supply phase space; they are not predictions.",
            "The transfer model has no induced IBFM operator, other j orbitals or reaction corrections.",
            "The <2000-keV sum uses model excitation energies and is not a complete experimental sum.",
            "No experimental p-value, confidence interval, mode assignment or novelty claim is made.",
        ],
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "observable-predictions.json"
    if output_path.exists():
        raise FileExistsError("use a new output directory to preserve the previous calculation")
    output_path.write_text(json.dumps(output, indent=2, allow_nan=False) + "\n")
    print(json.dumps({
        "output": str(output_path), "parameter_sets": len(all_rows),
        "max_energy_duality_error_MeV": max(c["dual_energy_max_difference_MeV"] for c in checks),
        "max_transfer_exchange_error": max(c["transfer_addition_removal_exchange_max_error"] for c in checks),
        "max_unit_EM_duality_difference": max(c["dual_unit_EM_B_max_difference"] for c in checks),
    }))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fit", type=Path, action="append", required=True)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    run([p.resolve() for p in args.fit], args.contract.resolve(), args.output_dir.resolve())
