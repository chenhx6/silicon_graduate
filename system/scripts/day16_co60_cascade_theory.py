#!/usr/bin/env python3
"""Trace the two-photon Co60 source cascade in explicit amplitude bases."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day16_ucgretina_stokes_oracle import cg_half, physical


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def intermediate_population(delta: float, native: bool) -> np.ndarray:
    # Ji=4 unpolarized; the first photon defines z and helicity is unobserved.
    values = []
    for mf in range(-2, 3):
        value = 0.0
        for helicity in [-1, 1]:
            mi = mf+helicity
            amplitude = 0.0
            for ell, coefficient, em_factor in [(2, 1.0, 1), (3, delta, helicity)]:
                phase = (-1)**ell if native else 1
                amplitude += (phase*coefficient*math.sqrt(2*ell+1)*em_factor
                              *cg_half(4, 2*mf, ell, helicity, 8, 2*mi))
            value += amplitude*amplitude/(9*(1+delta*delta))
        values.append(value)
    population = np.array(values)
    assert np.all(population >= 0) and population.sum() > 0
    return population/population.sum()


def coefficients(population: np.ndarray, order: int) -> dict:
    nodes, weights = np.polynomial.legendre.leggauss(order)
    case = {"Ji2": 4, "Jf2": 0, "MP": 4}
    values = np.array([physical(case, 0, math.acos(x), 0, population)["W"] for x in nodes])
    result = []
    for rank in range(5):
        p = np.polynomial.legendre.legval(nodes, [0]*rank+[1])
        result.append(float((2*rank+1)/2*np.sum(weights*values*p)))
    assert abs(result[0]-1) < 1e-12
    assert max(abs(result[1]), abs(result[3])) < 1e-12
    return {"population_m_minus2_to_plus2": population.tolist(),
            "a0_to_a4": result,
            "W_parallel": float(physical(case, 0, 0, 0, population)["W"]),
            "W_perpendicular": float(physical(case, 0, math.pi/2, 0, population)["W"])}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.contract.read_text())
    assert cfg["identity"] == "CO60-CASCADE-THEORY-01"
    level = Path(cfg["source_leveldata"])
    assert sha(level) == cfg["source_leveldata_sha256"]
    row = cfg["source_1173_row"]
    found = [line.split() for line in level.read_text().splitlines()
             if len(line.split()) >= 5 and line.split()[1] == str(row["energy_keV"])]
    assert len(found) == 1 and int(found[0][3]) == row["MP"]
    assert float(found[0][4]) == row["delta_native"]
    delta = row["delta_native"]
    native = coefficients(intermediate_population(delta, True), cfg["quadrature_order"])
    rb = coefficients(intermediate_population(-delta, False), cfg["quadrature_order"])
    wrong = coefficients(intermediate_population(delta, False), cfg["quadrature_order"])
    pure = coefficients(intermediate_population(0, True), cfg["quadrature_order"])
    pure_error = max(abs(pure["a0_to_a4"][2]-cfg["pure_control"]["a2"]),
                     abs(pure["a0_to_a4"][4]-cfg["pure_control"]["a4"]))
    bridge_error = max(abs(a-b) for a, b in zip(native["a0_to_a4"], rb["a0_to_a4"]))
    assert pure_error < 1e-12 and bridge_error < 1e-12
    result = {"identity": cfg["identity"], "contract_sha256": sha(args.contract),
        "script_sha256": sha(Path(__file__)), "source_leveldata_sha256": sha(level),
        "native_input_delta": delta, "RB_input_delta": -delta,
        "actual_source_mixed": native, "RB_same_physics": rb,
        "wrong_same_signed_amplitude_in_RB": wrong, "pure_E2_control": pure,
        "pure_expected_coefficient_error": pure_error,
        "native_RB_coefficient_error": bridge_error,
        "source_input_after_run_unchanged": sha(level) == cfg["source_leveldata_sha256"],
        "MC_or_experimental_fit_executed": False,
        "scope": cfg["assumptions"]}
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")
    print(json.dumps(result, indent=2, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
