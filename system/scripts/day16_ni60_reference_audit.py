#!/usr/bin/env python3
"""Cross-check selected ENSDF branches, G4 source inputs and shared MR errors.

Quoted evaluation fields remain distinct from experimental raw data. All
polarization/error outputs use the explicitly assumed point-gate model.
"""
from __future__ import annotations

import argparse
from decimal import Decimal
import hashlib
import json
import math
from pathlib import Path

import numpy as np



def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decode_uncertainty(value: str, digits: str) -> float | None:
    if not digits:
        return None
    if not digits.isdigit():
        raise ValueError("This selected audit requires symmetric integer ENSDF uncertainty digits")
    return float(Decimal(digits)*Decimal(10)**Decimal(value).as_tuple().exponent)


def records(path: Path) -> dict:
    levels, gammas, parent, current = [], [], None, None
    for no, raw in enumerate(path.read_text().splitlines(), 1):
        line = raw.ljust(80)
        if line[5:7] == "  " and line[7] == "L":
            parent = {"line": no, "E": line[9:19].strip(), "DE": line[19:21].strip(),
                      "Jpi": line[21:39].strip()}
            levels.append(parent)
            current = None
        elif line[5:7] == "  " and line[7] == "G":
            current = {"line": no, "parent": parent, "E": line[9:19].strip(),
                "DE": line[19:21].strip(), "RI": line[21:29].strip(), "DRI": line[29:31].strip(),
                "M": line[31:41].strip(), "MR": line[41:49].strip(), "DMR": line[49:55].strip(),
                "attached": [], "raw": raw}
            gammas.append(current)
        elif line[7] == "G" and current is not None:
            current["attached"].append({"line": no, "raw": raw})
    return {"levels": levels, "gammas": gammas}


def unique(rows, **identity):
    found = [row for row in rows if all(row[k] == v for k, v in identity.items())]
    if len(found) != 1:
        raise ValueError(f"Missing/ambiguous exact record identity: {identity}")
    return found[0]


def cc(gamma: dict) -> float:
    found = [line["raw"].split("CC=", 1)[1].split()[0] for line in gamma["attached"] if " CC=" in line["raw"]]
    assert len(found) == 1
    return float(found[0])


def source_levels(path: Path) -> dict:
    lines = [line.split() for line in path.read_text().splitlines() if line.strip()]
    rows, index = {}, 0
    while index < len(lines):
        header = lines[index]
        assert len(header) == 6
        number, energy, count = int(header[0]), float(header[2]), int(header[5])
        transitions = []
        for value in lines[index+1:index+1+count]:
            transitions.append({"daughter": int(value[0]), "nominal_gap_keV": float(value[1]),
                "relative_intensity": float(value[2]), "MP": int(value[3]),
                "mixing_ratio": float(value[4]), "CC": float(value[5])})
        rows[number] = {"E": energy, "J": float(header[4]), "transitions": transitions}
        index += count+1
        if number == 4:
            break
    assert {0, 1, 4} <= rows.keys()
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.contract.read_text())
    assert cfg["identity"] == "NI60-REFERENCE-QUANTITATIVE-02"
    base_path = args.contract.parent/cfg["base_contract"]
    assert sha(base_path) == cfg["base_contract_sha256"]
    base = json.loads(base_path.read_text())
    mass_path = Path(cfg["model_mass_result"])
    assert sha(mass_path) == cfg["model_mass_result_sha256"]
    mass = json.loads(mass_path.read_text())["mass_result"]["nuclear_mass_keV"]
    selected, energy_rows = {}, []
    for name, file in base["datasets"].items():
        path = Path(file["path"])
        assert sha(path) == file["sha256"]
        data, typed = records(path), base["typed_rows"][name]
        low = unique(data["levels"], E=typed["E2_level"][0])
        high = unique(data["levels"], E=typed["E4_level"][0])
        assert low["DE"] == typed["E2_level"][1] and high["DE"] == typed["E4_level"][1]
        assert low["Jpi"] == "2+" and high["Jpi"] == "4+"
        first = unique([g for g in data["gammas"] if g["parent"] == high], E=typed["first_gamma"][0])
        last = unique([g for g in data["gammas"] if g["parent"] == low], E=typed["last_gamma"][0])
        assert [first["MR"], first["DMR"]] == typed["first_MR"]
        assert [first["RI"], first["DRI"]] == typed["first_RI"]
        assert first["M"] == "E2(+M3)" and last["M"] == "E2" and not last["MR"]
        sigma = decode_uncertainty(first["MR"], first["DMR"])
        assert sigma == cfg["sigma_delta_from_field"]
        selected[name] = {"low": low, "high": high, "first": first, "last": last,
                          "quoted_delta": float(first["MR"]), "quoted_sigma_delta": sigma,
                          "CC_first_S_record": cc(first), "CC_last_S_record": cc(last)}
        for role, gamma, parent_e, daughter_e in [("first", first, float(high["E"]), float(low["E"])),
                                                 ("last", last, float(low["E"]), 0.)]:
            gap = parent_e-daughter_e
            predicted = gap*(2*mass+parent_e+daughter_e)/(2*(mass+parent_e))
            energy_rows.append({"dataset": name, "role": role, "level_gap_keV": gap,
                "recorded_gamma_E_keV": float(gamma["E"]), "rest_model_photon_E_keV": predicted,
                "rest_recoil_correction_keV": gap-predicted,
                "model_minus_recorded_keV": predicted-float(gamma["E"]),
                "E_gamma_sigma_keV": decode_uncertainty(gamma["E"], gamma["DE"]),
                "level_gamma_joint_covariance_known": False})
    source_file = Path(base["source_g4file"]["path"])
    assert sha(source_file) == base["source_g4file"]["sha256"]
    g4 = source_levels(source_file)
    first_source = unique(g4[4]["transitions"], daughter=1)
    last_source = unique(g4[1]["transitions"], daughter=0)
    assert first_source["mixing_ratio"] == selected["adopted"]["quoted_delta"]
    assert first_source["MP"] == 407 and last_source["MP"] == 4
    source_crosswalk = {"level1_E": g4[1]["E"], "level4_E": g4[4]["E"],
        "first_transition": first_source, "last_transition": last_source,
        "levels_match_adopted": g4[1]["E"] == float(selected["adopted"]["low"]["E"])
                                and g4[4]["E"] == float(selected["adopted"]["high"]["E"]),
        "source_MR_has_uncertainty": False}
    delta, sigma = selected["adopted"]["quoted_delta"], selected["adopted"]["quoted_sigma_delta"]
    from day16_co60_conditional_stokes import configuration

    def prediction(value):
        parts = (("E", 2, 1.), ("M", 3, value))
        return np.array([configuration(parts, math.pi/2, role)["normalized_Stokes"][0]
                         for role in ["first", "last"]])
    derivatives = [(prediction(delta+h)-prediction(delta-h))/(2*h) for h in cfg["derivative_steps"]]
    assert np.max(abs(derivatives[0]-derivatives[1])) < 1e-8
    derivative, central = derivatives[-1], prediction(delta)
    covariance = sigma*sigma*np.outer(derivative, derivative)
    eigenvalues = np.linalg.eigvalsh(covariance)
    assert eigenvalues.min() > -1e-18
    weights = np.array([1., -1.])
    difference_sigma = math.sqrt(float(weights@covariance@weights))
    naive_sigma = math.sqrt(float(np.trace(covariance)))
    probability = float(selected["co60beta"]["first"]["RI"])/100/(1+selected["co60beta"]["CC_last_S_record"])
    result = {"identity": cfg["identity"], "contract_sha256": sha(args.contract),
        "script_sha256": sha(Path(__file__)), "selected_records": selected,
        "SDK_nuclear_mass_keV": mass, "rest_frame_energy_crosschecks": energy_rows,
        "actual_source_crosswalk": source_crosswalk,
        "pointP_shared_delta_component": {"conditional_phase_assumption": cfg["phase_assumption_for_uncertainty"],
            "delta": delta, "quoted_delta_error": sigma, "central_Pfirst_Plast": central.tolist(),
            "derivative_steps": cfg["derivative_steps"], "derivatives": [v.tolist() for v in derivatives],
            "covariance": covariance.tolist(), "eigenvalues": eigenvalues.tolist(),
            "difference_central": float(weights@central), "difference_sigma_shared_input_only": difference_sigma,
            "difference_sigma_if_wrongly_independent": naive_sigma,
            "endpoint_input_range_not_CI": [{"delta": value, "Pfirst_Plast": prediction(value).tolist()}
                                           for value in [delta-sigma, delta+sigma]],
            "primary_phase_or_full_calibration_CI_recovered": False},
        "evaluated_pair_probability_central_conditional": probability,
        "pair_probability_scope": "RI_first per100decays times conditional last radiative branch; intensity/CC joint errors not recovered",
        "datasets_are_independent_experiments": False,
        "original_files_after_run_unchanged": all(sha(Path(v["path"])) == v["sha256"] for v in base["datasets"].values())
                                                and sha(source_file) == base["source_g4file"]["sha256"]}
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")
    print(json.dumps({"rest_frame_energy_crosschecks": energy_rows,
        "actual_source_crosswalk": source_crosswalk, "pointP_shared_delta_component": result["pointP_shared_delta_component"],
        "evaluated_pair_probability_central_conditional": probability}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
