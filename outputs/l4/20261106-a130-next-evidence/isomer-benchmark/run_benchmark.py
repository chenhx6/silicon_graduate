#!/usr/bin/env python3
"""Fixed-input 137Ba isomer E2 comparison; no fit or strength-selected mapping."""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

import csv
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import sys
import time

import numpy as np

OUT = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "system/scripts/analysis"))
from single_j_ibfm import (
    IBFMParameters, IBFMKernel, CoreParameters, BosonCore,
    calibrate_core_e2, transition_rme,
)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def stamp():
    return datetime.now(timezone.utc).isoformat()


def write_new(name, value):
    with (OUT / name).open("x") as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write("\n")


def real(x):
    z = complex(x)
    if abs(z.imag) > 1e-11 * max(1., abs(z.real)):
        raise ValueError("Unexpected imaginary observable")
    return float(z.real)


def main():
    started, clock = stamp(), time.monotonic()
    protocol = json.loads((OUT / "protocol.json").read_text())
    for path, expected in protocol["input_sha256"].items():
        if sha(ROOT / path) != expected:
            raise ValueError(f"Frozen input changed: {path}")
    params = IBFMParameters(**protocol["parameters"])
    kernel = IBFMKernel(params)
    sol = kernel.solve()
    anchor = int(sol.indices_for_J(11)[0])
    parents, daughters = [int(x) for x in sol.indices_for_J(19)[:2]], [
        int(x) for x in sol.indices_for_J(15)[:2]]
    if len(parents) != 2 or len(daughters) != 2:
        raise ValueError("Both declared state alternatives are required")
    obs = protocol["experimental"]
    obs_ei = (obs["parent_energy_keV"] - obs["anchor_11half_energy_keV"]) / 1000
    obs_ef = (obs["daughter_energy_keV"] - obs["anchor_11half_energy_keV"]) / 1000
    energies = []
    for pi, i in enumerate(parents):
        for pf, f in enumerate(daughters):
            ei, ef = (float(sol.energies[x] - sol.energies[anchor]) for x in (i, f))
            energies.append({
                "pair": f"19half_{pi+1}_to_15half_{pf+1}",
                "parent_ordinal": pi, "daughter_ordinal": pf,
                "parent_state_index": i, "daughter_state_index": f,
                "parent_relative_MeV": ei, "daughter_relative_MeV": ef,
                "photon_model_MeV": ei - ef,
                "model_decay_direction_positive": ei > ef,
                "parent_energy_residual_keV": 1000 * (ei - obs_ei),
                "daughter_energy_residual_keV": 1000 * (ef - obs_ef),
                "energy_squared_distance_MeV2": (ei - obs_ei)**2 + (ef - obs_ef)**2,
            })
    nearest = min(energies, key=lambda x: x["energy_squared_distance_MeV2"])["pair"]
    write_new("energy-mapping-frozen.json", {
        "at_utc": stamp(), "frozen_before_any_new_E2_matrix_element": True,
        "primary_pair": energies[0]["pair"],
        "energy_nearest_in_declared_four_pairs": nearest,
        "physical_assignment_certified": False,
        "is_statistical_chi_square": False, "pairs": energies,
    })
    unit = ((1 / (4 * math.pi)) * (3 / 5)**2
            * (1.2 * obs["A"] ** (1 / 3)) ** 4 / 1e4)
    observed_b = obs["Bdown_Wu"] * unit
    roots_path = ROOT / "outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-calibrated-operator/linear-calibration.json"
    calibrated = json.loads(roots_path.read_text())
    settings = [
        {"root_id": "primary", "chi_E": .35, "eF_eb": .125},
        {"root_id": "core_only_control", "chi_E": .35, "eF_eb": 0.},
        *calibrated["roots"],
    ]
    core = BosonCore(CoreParameters(params.n_b, params.eps_d, params.kappa, params.chi))
    cs = core.solve()
    c0, c2 = (int(cs.indices_for_J(j)[0]) for j in (0, 4))
    state_hash = sha_array(sol.vectors)
    rows = []
    for setting in settings:
        chi, ef = setting["chi_E"], setting["eF_eb"]
        calibration = calibrate_core_e2(
            core, cs, c0, c2, chi_prime=chi,
            target_B_0_to_2=protocol["core_Bup_target_e2b2"])
        full_op = kernel.e2(calibration.eB, ef, chi)
        b_op, f_op = kernel.e2(calibration.eB, 0., chi), kernel.e2(0., ef, chi)
        for erow in energies:
            i, f = erow["parent_state_index"], erow["daughter_state_index"]
            full = transition_rme(sol, full_op, i, f)
            reverse = transition_rme(sol, full_op, f, i)
            boson = transition_rme(sol, b_op, i, f)
            fermion = transition_rme(sol, f_op, i, f)
            if abs(full - boson - fermion) > 1e-11:
                raise ValueError("E2 amplitude decomposition failed")
            if abs(full - reverse.conjugate()) > 1e-11:
                raise ValueError("Rank-two reverse-RME reciprocity failed")
            bdown = abs(full)**2 / 20
            bup = abs(reverse)**2 / 16
            if abs(bup - (20 / 16) * bdown) > 1e-12:
                raise ValueError("Transition-direction normalization failed")
            bb, ff = abs(boson)**2 / 20, abs(fermion)**2 / 20
            cross = 2 * real(boson.conjugate() * fermion) / 20
            if abs(bb + ff + cross - bdown) > 1e-12:
                raise ValueError("Strength interference decomposition failed")
            rows.append({
                "operator": setting["root_id"], **erow,
                "eB_eb": calibration.eB, "eF_eb": ef, "chi_E": chi,
                "is_primary_mapping": erow["pair"] == energies[0]["pair"],
                "is_energy_nearest_mapping": erow["pair"] == nearest,
                "signed_RME_eb": real(full),
                "Bdown_e2b2": float(bdown), "Bdown_Wu": float(bdown / unit),
                "Bup_reverse_e2b2": float(bup),
                "model_over_observed_strength": float(bdown / observed_b),
                "Bdown_boson_e2b2": float(bb), "Bdown_fermion_e2b2": float(ff),
                "Bdown_interference_e2b2": cross,
                "RME_reciprocity_residual": float(abs(full - reverse.conjugate())),
            })
    if sha_array(sol.vectors) != state_hash:
        raise ValueError("Operator loop changed the state basis")
    for path, expected in protocol["input_sha256"].items():
        if sha(ROOT / path) != expected:
            raise ValueError(f"Input changed during run: {path}")
    result = {
        "schema": "137Ba-isomer-withheld-E2-result-v1",
        "started_at_utc": started, "finished_at_utc": stamp(),
        "protocol_sha256": sha(OUT / "protocol.json"),
        "producer_sha256": sha(__file__),
        "energy_mapping_record_sha256": sha(OUT / "energy-mapping-frozen.json"),
        "parameters": protocol["parameters"],
        "core_Bup_target_e2b2": protocol["core_Bup_target_e2b2"],
        "experimental": obs,
        "Weisskopf_unit_down_e2b2": unit,
        "observed_Bdown_e2b2": observed_b,
        "observed_quoted_margin_e2b2": obs["Bdown_quoted_margin_Wu"] * unit,
        "energy_nearest_in_declared_pairs": nearest,
        "state_basis_sha256": state_hash, "rows": rows,
        "row_count": len(rows),
        "no_parameters_or_state_ordinals_selected_using_B": True,
        "experimental_half_life_not_reused_as_second_datum": True,
        "no_lifetime_or_decay_rate_predicted": True,
        "interpretation": protocol["interpretation"],
        "elapsed_seconds": time.monotonic() - clock,
    }
    write_new("results.json", result)
    with (OUT / "predictions.csv").open("x", newline="") as stream:
        w = csv.DictWriter(stream, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print("unit_Wu_down_e2b2", unit, "observed", observed_b)
    print("primary/energy-nearest predictions:")
    for row in rows:
        if row["is_primary_mapping"] or row["is_energy_nearest_mapping"]:
            print(row["operator"], row["pair"],
                  "Egamma_model_keV", 1000 * row["photon_model_MeV"],
                  "Bdown_Wu", row["Bdown_Wu"],
                  "ratio_to_observed", row["model_over_observed_strength"])


def sha_array(a):
    return hashlib.sha256(np.ascontiguousarray(a).tobytes()).hexdigest()


if __name__ == "__main__":
    main()
