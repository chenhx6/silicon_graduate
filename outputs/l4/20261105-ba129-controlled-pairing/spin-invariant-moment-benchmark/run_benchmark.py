#!/usr/bin/env python3
"""Static-moment sidecar for fixed printed-input Ba cases; no parameter fitting.

All model calculations use the existing IBFM kernel read-only. Qs is contracted
directly at M=J and checked independently through a different M component and
the Wigner--Eckart conversion. The only charge determination is the specified
positive eB calibration from the already frozen first-2+ B(E2) input.
"""

from dataclasses import asdict
from datetime import datetime, timezone
import csv
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sys
import time

if any(os.environ.get(k) != "1" for k in
       ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")):
    raise RuntimeError("Run with all three BLAS/OpenMP thread variables set to 1")

import numpy as np

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "system/scripts/analysis"))
from paired_single_j_em import clebsch_gordan as cg
from single_j_ibfm import CoreParameters, BosonCore, IBFMParameters, IBFMKernel

CONTRACT = ROOT / "outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-chain-contract.json"
CALIBRATION = ROOT / "outputs/l4/20261105-ba129-controlled-pairing/core-E2-calibration/ba-core-E2.json"
TEX = ROOT / "raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex"
PDF = ROOT / "raw/papers/2017_Nomura et al_Shape-phase transitions in odd-mass γ -soft nuclei with mass A ≈ 130.pdf"
PREF = math.sqrt(16*math.pi/5)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def real_checked(value, label):
    value = complex(value)
    if not math.isfinite(value.real) or not math.isfinite(value.imag) or abs(value.imag) > 1e-10*max(1., abs(value)):
        raise ValueError(f"Non-real/non-finite {label}: {value}")
    return value.real


def component(solution, operator, final, initial):
    """Direct q=0 contraction of full operators restricted by full_indices."""
    indices = solution.basis.full_indices
    block = operator.components[0][indices][:, indices]
    return complex(np.vdot(solution.vectors[:, final], block @ solution.vectors[:, initial]))


def state_index(solution, two_j, ordinal=0):
    states = np.flatnonzero(solution.two_J == two_j)
    if len(states) <= ordinal:
        raise ValueError("Requested spin/state ordinal absent")
    return int(states[ordinal])


def qs_direct(solution, operator, two_j, ordinal=0):
    if solution.basis.two_M != two_j:
        raise ValueError("Direct spectroscopic moment requires M=J")
    i = state_index(solution, two_j, ordinal)
    return PREF*real_checked(component(solution, operator, i, i), "stretched Q20")


def qs_from_other_m(solution, operator, two_j, ordinal=0):
    i = state_index(solution, two_j, ordinal)
    cm = cg(two_j, int(solution.basis.two_M), 4, 0, two_j, int(solution.basis.two_M))
    cj = cg(two_j, two_j, 4, 0, two_j, two_j)
    if cm == 0:
        raise ValueError("Allowed diagonal channel unresolved by this M component")
    amplitude = component(solution, operator, i, i)
    rme = math.sqrt(two_j+1)*amplitude/cm
    value = PREF*cj*rme/math.sqrt(two_j+1)
    return real_checked(value, "RME-reconstructed Qs"), rme


def source_table_rows(lines, first, last):
    result = {}
    for number in range(first, last+1):
        line = lines[number-1]
        match = re.match(r"\$\^\{(\d+)\}\$Ba\s*&(.+)", line)
        if match:
            values = [float(s.strip().replace("\\\\", "").strip())
                      for s in match.group(2).split("&")]
            result[int(match.group(1))] = (values, number)
    return result


def source_parameters(contract):
    lines = TEX.read_text().splitlines()
    core = source_table_rows(lines, 298, 302)
    occupancy = source_table_rows(lines, 389, 393)
    coupling = source_table_rows(lines, 514, 518)
    assert r"\chi^{\prime}=0.35" in "\n".join(lines[568:580])
    assert r"e_n=0.125" in "\n".join(lines[568:580])
    verified = {}
    for case in contract["cases"]:
        odd, even = case["odd_A"], case["core_A"]
        cp, cline = core[even]
        vp, vline = occupancy[odd]
        bf, bfline = coupling[odd]
        printed = dict(zip(("eps_d", "kappa", "chi"), cp))
        printed["v2"] = vp[-1]
        printed.update(zip(("Gamma0", "Lambda0", "A0"), bf))
        for key, value in printed.items():
            assert case[key] == value, (odd, key)
        inferred_bosons = (56-50)//2 + (82-(even-56))//2
        assert case["n_b"] == inferred_bosons
        assert case["two_j"] == case["two_J_state"] == 11 and case["state_ordinal"] == 0
        verified[odd] = {"printed_numeric_values": printed,
                         "source_tex_lines": [cline, vline, bfline],
                         "n_b": inferred_bosons,
                         "n_b_basis": "3 proton-particle pairs plus neutron-hole pairs of the A-1 core",
                         "A0_mapping": "Table V A'_11/2 numeric entry assigned to frozen kernel A0 by the existing contract"}
    return verified


def signed_y2_rme():
    """h11/2 stretched spinor = Y_55 * spin-up, with no radial factor."""
    ell, two_j = 5, 11
    x, weights = np.polynomial.legendre.leggauss(32)
    probability_weight = (1-x*x)**ell
    y20 = math.sqrt(5/(16*math.pi))*(3*x*x-1)
    angular_integral = float(np.dot(weights, probability_weight*y20) /
                             np.dot(weights, probability_weight))
    closed = -ell/(2*ell+3)*math.sqrt(5/(4*math.pi))
    assert abs(angular_integral-closed) < 1e-14
    cg_stretched = cg(two_j, two_j, 4, 0, two_j, two_j)
    qjj = math.sqrt(two_j+1)*angular_integral/cg_stretched
    return qjj, {"stretched_Y20_expectation": angular_integral,
                 "closed_form_expectation": closed,
                 "quadrature_residual": angular_integral-closed,
                 "CG_stretched": cg_stretched,
                 "Q_jj": qjj, "radial_factor_inserted": False}


def calculate_case(case, strength, qjj, chi_e, ef):
    start = time.monotonic()
    core = BosonCore(CoreParameters(case["n_b"], case["eps_d"], case["kappa"], case["chi"]))
    m0 = core.solve(two_M=0)
    i0, i2 = state_index(m0, 0), state_index(m0, 4)
    unit = core.e2(1., chi_e)
    # CG(0 0,2 0|2 0)=1, R20=sqrt(5)<2,0|Q20|0,0>.
    amplitude = component(m0, unit, i2, i0)
    unit_bup = 5*abs(amplitude)**2
    eb = math.sqrt(strength["selected_strength"]["B_up_e2b2"] / unit_bup)
    core_e2 = core.e2(eb, chi_e)
    recalibrated_bup = 5*abs(component(m0, core_e2, i2, i0))**2
    assert abs(recalibrated_bup-strength["selected_strength"]["B_up_e2b2"]) < 1e-12
    core_stretched = core.solve(two_M=4)
    core_qs = qs_direct(core_stretched, core_e2, 4)
    core_qs_rme, core_rme = qs_from_other_m(m0, core_e2, 4)
    assert abs(core_qs-core_qs_rme) < 2e-9
    assert abs(core_stretched.energies[state_index(core_stretched, 4)] - m0.energies[i2]) < 2e-9

    keys = ("n_b", "two_j", "eps_d", "kappa", "chi", "v2", "Gamma0", "Lambda0", "A0")
    parameters = IBFMParameters(**{k: case[k] for k in keys}, Q_jj=qjj)
    kernel = IBFMKernel(parameters)
    stretched = kernel.solve(two_M=11)
    middle = kernel.solve(two_M=1)
    full_operator = kernel.e2(eb, ef, chi_e)
    boson_operator = kernel.e2(eb, 0., chi_e)
    fermion_operator = kernel.e2(0., ef, chi_e)
    total_qs = qs_direct(stretched, full_operator, 11)
    boson_qs = qs_direct(stretched, boson_operator, 11)
    fermion_qs = qs_direct(stretched, fermion_operator, 11)
    reconstructed_qs, rme = qs_from_other_m(middle, full_operator, 11)
    assert abs(total_qs-reconstructed_qs) < 2e-9
    assert abs(total_qs-boson_qs-fermion_qs) < 2e-10
    assert abs(stretched.energies[state_index(stretched, 11)] -
               middle.energies[state_index(middle, 11)]) < 2e-9
    # Parent outputs are comparison targets only, never parameters or wavefunctions.
    parent_path = ROOT / f"outputs/l4/20261105-ba129-controlled-pairing/shape-closure-v1/ba{case['odd_A']}.json"
    parent = json.loads(parent_path.read_text())
    parent_qs = parent["primary"]["same_spin"]["spectroscopic_Qs_eb"]
    return {
        "odd_A": case["odd_A"], "core_A": case["core_A"],
        "state": "lowest 11/2- in declared single-h11/2 model",
        "parameters": asdict(parameters), "chi_E2": chi_e, "eF_eb": ef, "eB_eb": eb,
        "core": {"state": "2_1+", "Qs_eb": core_qs, "Qs_from_M0_RME_eb": core_qs_rme,
                 "diagonal_RME_eb": core_rme.real,
                 "unit_Bup_eB1": unit_bup,
                 "target_Bup_e2b2": strength["selected_strength"]["B_up_e2b2"],
                 "reconstructed_Bup_e2b2": recalibrated_bup,
                 "M_conversion_residual_eb": core_qs-core_qs_rme},
        "odd": {"Qs_eb": total_qs, "Qs_boson_term_eb": boson_qs, "Qs_fermion_term_eb": fermion_qs,
                "Qs_from_Mhalf_RME_eb": reconstructed_qs, "diagonal_RME_eb": rme.real,
                "M_conversion_residual_eb": total_qs-reconstructed_qs,
                "term_sum_residual_eb": total_qs-boson_qs-fermion_qs,
                "full_dimension": kernel.dimension},
        "parent_comparison": {"path": str(parent_path.relative_to(ROOT)), "parent_Qs_eb": parent_qs,
                              "Qs_difference_eb": total_qs-parent_qs,
                              "parent_eB_eb": parent["calibration"]["eB"],
                              "eB_difference_eb": eb-parent["calibration"]["eB"]},
        "calibration_source": {
            "path": str(CALIBRATION.relative_to(ROOT)),
            "calibration_block_id": strength["calibration_block_id"],
            "adopted_path": strength["source"]["adopted_path"],
            "input_quantity": strength["selected_strength"]["input_quantity"],
            "B_margin_used_in_model_fit": False,
        },
        "elapsed_seconds": time.monotonic()-start,
    }


def main():
    paths = [CONTRACT, CALIBRATION, TEX, PDF, Path(__file__),
             ROOT/"system/scripts/analysis/single_j_ibfm.py",
             ROOT/"system/scripts/analysis/paired_single_j_em.py",
             ROOT/"system/scripts/analysis/quadrupole_scalar_invariants.py"]
    paths += [ROOT/f"outputs/l4/20261105-ba129-controlled-pairing/shape-closure-v1/ba{a}.json"
              for a in (129, 131, 133, 135, 137)]
    locked = {str(p.relative_to(ROOT)): digest(p) for p in paths}
    for name in ("benchmark-results.json", "model-static-moments.csv"):
        if (OUT/name).exists():
            raise FileExistsError(OUT/name)
    contract = json.loads(CONTRACT.read_text())
    calibration = {row["A"]: row for row in json.loads(CALIBRATION.read_text())["selected_rows"]}
    verified = source_parameters(contract)
    chi_e, ef = contract["E2_policy"]["chi_prime"], contract["E2_policy"]["eF_eb"]
    assert chi_e == .35 and ef == .125
    qjj, angular_check = signed_y2_rme()
    results = []
    for case in contract["cases"]:
        result = calculate_case(case, calibration[case["core_A"]], qjj, chi_e, ef)
        results.append(result)
        print(json.dumps({"A": result["odd_A"], "Qs": result["odd"]["Qs_eb"],
                          "core_Qs_2": result["core"]["Qs_eb"], "eB": result["eB_eb"],
                          "parent_residual": result["parent_comparison"]["Qs_difference_eb"],
                          "elapsed_s": result["elapsed_seconds"]}), flush=True)
    assert all(digest(ROOT/path) == value for path, value in locked.items())
    record = {
        "schema": "fixed-Ba-static-moment-benchmark-v1",
        "actual_finished_at": datetime.now(timezone.utc).isoformat(),
        "run_date_label": "2026-11-06",
        "scope": "Independent static moment contractions in a shared frozen finite Hamiltonian; no source-author code certification.",
        "Qs_definition": "sqrt(16*pi/5)*<J,M=J|T(E2)_20|J,M=J>; signed e b",
        "E2_definition": "eB Q_chi_prime -eF(1-2v^2) Q_jj F2/sqrt(5)",
        "source_numeric_checks": verified, "signed_Y2_check": angular_check,
        "cases": results, "input_sha256": locked, "inputs_unchanged": True,
        "eF_or_chi_refitted": False,
        "source_author_exact_eB_run_cards_available": False,
        "checks": {
            "case_count": len(results),
            "max_core_M_conversion_residual_eb": max(abs(r["core"]["M_conversion_residual_eb"]) for r in results),
            "max_odd_M_conversion_residual_eb": max(abs(r["odd"]["M_conversion_residual_eb"]) for r in results),
            "max_parent_Qs_difference_eb": max(abs(r["parent_comparison"]["Qs_difference_eb"]) for r in results),
            "max_parent_eB_difference_eb": max(abs(r["parent_comparison"]["eB_difference_eb"]) for r in results),
        },
        "thread_environment": {k: os.environ[k] for k in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
        "limits": [
            "Calibration moments are not independent EM holdouts.",
            "Core E2 calibration summaries carry method/branch dependence and no complete covariance.",
            "No uncertainty assigned to a model prediction from source rounding or missing author run cards.",
            "No source energy agreement is used as EM validation.",
            "No physical intrinsic shape or published-figure replication follows from these checks.",
        ],
    }
    with (OUT/"benchmark-results.json").open("x") as stream:
        json.dump(record, stream, indent=2, allow_nan=False)
        stream.write("\n")
    rows = [{
        "odd_A": r["odd_A"], "core_A": r["core_A"], "eB_eb": r["eB_eb"],
        "chi_E2": r["chi_E2"], "eF_eb": r["eF_eb"],
        "Qs_11over2_eb": r["odd"]["Qs_eb"],
        "Qs_boson_term_eb": r["odd"]["Qs_boson_term_eb"],
        "Qs_fermion_term_eb": r["odd"]["Qs_fermion_term_eb"],
        "core_Qs_2plus_eb": r["core"]["Qs_eb"],
        "odd_M_conversion_residual_eb": r["odd"]["M_conversion_residual_eb"],
        "parent_Qs_difference_eb": r["parent_comparison"]["Qs_difference_eb"],
    } for r in results]
    with (OUT/"model-static-moments.csv").open("x", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps(record["checks"], indent=2))


if __name__ == "__main__":
    main()
