#!/usr/bin/env python3
"""Toy particle-vibration/Nilsson-octupole transfer model.

This script is deliberately a transparent surrogate, not a DWBA producer.
It diagonalizes two-level blocks

    |j,0+>  <-->  |j',3->

for each parity.  The zero-phonon amplitude is the part directly visible in
transfer from a 0+ core; the 3- phonon component is a core-polarization proxy.
The neutron-number scan changes the input single-particle detuning and core
phonon energy to expose sensitivities, without fitting experimental data.
Only the Python standard library is required.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent


def lower_upper(e1: float, e2: float, coupling: float):
    """Return eigenpairs of [[e1,c],[c,e2]], ordered by energy."""
    mean = 0.5 * (e1 + e2)
    gap = math.sqrt((0.5 * (e1 - e2)) ** 2 + coupling**2)
    values = (mean - gap, mean + gap)
    vectors = []
    for energy in values:
        if abs(coupling) > 1.0e-14:
            vec = [coupling, energy - e1]
        elif abs(e1 - energy) < 1.0e-12:
            vec = [1.0, 0.0]
        else:
            vec = [0.0, 1.0]
        norm = math.sqrt(sum(x * x for x in vec))
        vectors.append([x / norm for x in vec])
    return list(zip(values, vectors))


def pair_levels(pair, beta3, omega3, neutron_number, scenario):
    """Generate both parity blocks for one opposite-parity orbital pair."""
    # The coupling g3 is a reduced matrix-element proxy.  beta3 is dimensionless.
    g = pair["g3"] * beta3
    drift = pair["detuning_slope"] * (neutron_number - pair["n_ref"])
    e_even = pair["e_even"] - 0.5 * drift
    e_odd = pair["e_odd"] + 0.5 * drift
    rows = []
    # Positive block: even orbital on the 0+ core mixes with odd orbital on 3-.
    for state_index, (energy, vec) in enumerate(
        lower_upper(e_even, e_odd + omega3, g), start=1
    ):
        direct, phonon = vec
        rows.append(
            {
                "scenario": scenario,
                "neutron_number": neutron_number,
                "pair": pair["name"],
                "state": f"positive_{state_index}",
                "parity": "+",
                "I": pair["j_even"],
                "direct_orbital": pair["even_orbital"],
                "phonon_orbital": pair["odd_orbital"],
                "energy_mev": energy,
                "direct_amplitude": direct,
                "phonon_amplitude": phonon,
                "S_0plus_direct": direct * direct,
                "core_polarization_norm": phonon * phonon,
                "transfer_amplitude_phase": "real, phase convention arbitrary",
            }
        )
    # Negative block: odd orbital on the 0+ core mixes with even orbital on 3-.
    for state_index, (energy, vec) in enumerate(
        lower_upper(e_odd, e_even + omega3, g), start=1
    ):
        direct, phonon = vec
        rows.append(
            {
                "scenario": scenario,
                "neutron_number": neutron_number,
                "pair": pair["name"],
                "state": f"negative_{state_index}",
                "parity": "-",
                "I": pair["j_odd"],
                "direct_orbital": pair["odd_orbital"],
                "phonon_orbital": pair["even_orbital"],
                "energy_mev": energy,
                "direct_amplitude": direct,
                "phonon_amplitude": phonon,
                "S_0plus_direct": direct * direct,
                "core_polarization_norm": phonon * phonon,
                "transfer_amplitude_phase": "real, phase convention arbitrary",
            }
        )
    return rows


def write_csv(path: Path, rows):
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def run():
    # The first pair is the neutron octupole-driving pair in the Ba region.
    # The second is the proton d5/2-h11/2 pair requested as a mechanism control.
    pairs = [
        {
            "name": "nu_f7/2_i13/2",
            "even_orbital": "nu_i13/2",
            "odd_orbital": "nu_f7/2",
            "j_even": 6.5,
            "j_odd": 3.5,
            "e_even": 0.45,
            "e_odd": 0.00,
            "g3": 0.65,
            "detuning_slope": 0.018,
            "n_ref": 88,
        },
        {
            "name": "pi_d5/2_h11/2",
            "even_orbital": "pi_d5/2",
            "odd_orbital": "pi_h11/2",
            "j_even": 2.5,
            "j_odd": 5.5,
            "e_even": 0.10,
            "e_odd": 0.55,
            "g3": 0.52,
            "detuning_slope": 0.012,
            "n_ref": 88,
        },
    ]

    all_rows = []
    scans = []
    scenarios = {
        # Ba-like soft octupole window: a broad minimum in omega_3 near N=88.
        "Ba_like": range(82, 97),
        # Ra-like static-octupole proxy: lower phonon energy and larger beta3.
        "Ra_like": range(132, 143),
    }
    for scenario, neutron_numbers in scenarios.items():
        for neutron_number in neutron_numbers:
            if scenario == "Ba_like":
                beta3 = 0.035 + 0.060 * math.exp(-((neutron_number - 88) / 4.2) ** 2)
                omega3 = 0.95 - 0.25 * math.exp(-((neutron_number - 88) / 4.2) ** 2)
            else:
                beta3 = 0.115 + 0.008 * math.tanh((neutron_number - 137) / 3.0)
                omega3 = 0.42 - 0.04 * math.exp(-((neutron_number - 137) / 3.5) ** 2)
            rows_for_n = []
            for pair in pairs:
                rows_for_n.extend(
                    pair_levels(pair, beta3, omega3, neutron_number, scenario)
                )
            all_rows.extend(rows_for_n)
            # Summary curve data: lowest state in each parity block for neutron pair.
            neutron_rows = [r for r in rows_for_n if r["pair"] == "nu_f7/2_i13/2"]
            positive = min((r for r in neutron_rows if r["parity"] == "+"), key=lambda x: x["energy_mev"])
            negative = min((r for r in neutron_rows if r["parity"] == "-"), key=lambda x: x["energy_mev"])
            scans.append(
                {
                    "scenario": scenario,
                    "neutron_number": neutron_number,
                    "beta3_input": beta3,
                    "omega3_mev": omega3,
                    "S_positive_direct": positive["S_0plus_direct"],
                    "S_negative_direct": negative["S_0plus_direct"],
                    "core_polarization_positive": positive["core_polarization_norm"],
                    "core_polarization_negative": negative["core_polarization_norm"],
                    "parity_asymmetry": positive["S_0plus_direct"] - negative["S_0plus_direct"],
                }
            )

    write_csv(HERE / "spectroscopic_factors.csv", all_rows)
    write_csv(HERE / "neutron_number_evolution.csv", scans)

    result = {
        "model": "two-level particle-vibration coupling / Nilsson-octupole surrogate",
        "purpose": "conditional transfer-strength and core-polarization map",
        "units": {"energy": "MeV", "beta3": "dimensionless", "spectroscopic_factor": "dimensionless"},
        "equations": {
            "block": "H=[[epsilon_j, g3*beta3],[g3*beta3, epsilon_jprime+omega3]]",
            "transfer": "S(I^pi,j;0+) = |<I^pi||a_j^dagger||0+>|^2 = |C_direct|^2 for I=j",
            "cross_section": "dSigma/dOmega = C2S * (dSigma/dOmega)_DWBA",
            "core_polarization": "P_core = |C_phonon|^2 = 1 - S_direct in each normalized block",
        },
        "assumptions": [
            "The initial core is 0+; a 3- core component is therefore not directly populated by the leading one-body transfer operator.",
            "The coupling and orbital energies are transparent toy inputs, not a fit to 225Ra, 225Ac, 143Ba or 145Ba transfer data.",
            "A DWBA or ADWA calculation with optical potentials, finite range and nonlocality is required before comparing an absolute cross section.",
            "Parity asymmetry is generated by different detunings in the positive and negative particle-phonon blocks; it is not a theorem that every parity doublet has unequal strengths.",
        ],
        "validation": {
            "normalization_max_error": max(
                abs(r["S_0plus_direct"] + r["core_polarization_norm"] - 1.0)
                for r in all_rows
            ),
            "rows_spectroscopic": len(all_rows),
            "rows_neutron_scan": len(scans),
        },
        "evidence_boundary": {
            "wiki_sources": [
                "butler-nazarewicz-1996-intrinsic-reflection-asymmetry",
                "gaffney-2013-pear-shaped-rn-ra",
                "nomura-2018-odd-ba-octupole",
                "nndc-2009-ra225-adopted-parity-doublet",
                "nndc-2022-ac225-adopted-parity-doublet",
            ],
            "missing_direct_inputs": [
                "225Ra/225Ac transfer angular distributions and DWBA normalizations",
                "225Ra/225Ac state-resolved magnetic moments or g factors",
                "blocked-HFB or particle-vibration matrix elements for the selected states",
            ],
        },
    }
    (HERE / "results.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    run()
