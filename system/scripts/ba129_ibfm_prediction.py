#!/usr/bin/env python3
"""Declared 129Ba single-j IBFM reconstruction and fixed photon-split test.

Hamiltonian parameters come from a source-supported 128Ba/NB8 reconstruction
of Nomura2017. This is not an author-code replay or a new fit. The common
magnetic scale uses the existing anchor; five other photon ratios are kept
out of that calibration. Earlier rigid-rotor results informed model choice.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
import time

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent / "analysis"))
from single_j_ibfm import (
    IBFMParameters, CoreParameters, IBFMKernel, BosonCore,
    transition_rme, calibrate_core_e2, fermion_tensor,
)
from paired_single_j_em import clebsch_gordan
from paired_single_j_rotor import quadrupole_operator


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def h11_angular_y2():
    """Signed <h11/2||Y2||h11/2>, with no radial/effective-charge factor."""
    qjj = -math.sqrt(525/(143*math.pi))
    x, w = np.polynomial.legendre.leggauss(48)
    # Highest-weight h11/2 is Y_55 times spin-up. Its |Y_55|² weight is
    # proportional to (1-x²)^5 after the azimuthal integral.
    density = (1-x*x)**5
    integral = float(np.sum(w*density*math.sqrt(5/(16*math.pi))*(3*x*x-1))
                     / np.sum(w*density))
    cg = clebsch_gordan(11, 11, 4, 0, 11, 11)
    from_integral = integral*math.sqrt(12)/cg
    represented = -qjj/math.sqrt(5)*fermion_tensor(11, 2, 0).toarray()
    from_spin_quadrupole = -math.sqrt(5/(4*math.pi))*quadrupole_operator(11, 0)
    error = float(np.max(abs(represented-from_spin_quadrupole)))
    assert abs(from_integral-qjj) < 1e-12 and error < 1e-12
    return qjj, {"exact_radical": "-sqrt(525/(143*pi))",
                 "Gauss48_highest_weight_Y55_integral": integral,
                 "Qjj_from_integral_and_CG": from_integral,
                 "maximum_full_Y20_matrix_identity_error": error}


def run(contract_path, output_dir):
    started = time.perf_counter()
    contract = json.loads(contract_path.read_text())
    locked = {contract_path: sha(contract_path)}
    for name, digest in contract["source_inputs"].items():
        p = ROOT/name
        if sha(p) != digest:
            raise ValueError(f"source input hash changed: {name}")
        locked[p] = digest
    for name in ("system/scripts/analysis/single_j_ibfm.py",
                 "system/scripts/analysis/paired_single_j_em.py",
                 "system/scripts/analysis/paired_single_j_rotor.py"):
        p = ROOT/name
        locked[p] = sha(p)
    locked[Path(__file__)] = sha(Path(__file__))
    if (output_dir/"prediction.json").exists():
        raise FileExistsError("use a new output directory; preserve the previous case")

    h = contract["hamiltonian_inputs"]
    qjj, qcheck = h11_angular_y2()
    if h["two_j"] != 11 or h["N_F"] != 1:
        raise ValueError("this source-specific runner only supports one h11/2 fermion")
    core_params = CoreParameters(h["N_B"], h["epsilon_d_MeV"], h["kappa_MeV"], h["chi_H"])
    core = BosonCore(core_params)
    core_solution = core.solve()
    ground = int(core_solution.indices_for_J(0)[0])
    first2 = int(core_solution.indices_for_J(4)[0])
    if ground != int(np.argmin(core_solution.energies)):
        raise ValueError("declared core does not have a J=0 ground state")
    em = contract["EM_inputs"]
    calibration_data = em["core_calibration"]
    computed_down = math.log(2)/(
        calibration_data["T_half_ps"]*1e-12*(1+calibration_data["alpha_total"])
        *calibration_data["rate_coefficient_s-1_MeV-5_per_e2b2"]
        *(calibration_data["E_gamma_keV"]/1000)**5)
    assert abs(computed_down-calibration_data["derived_BE2_down_e2b2"]) < 1e-14
    calibration = calibrate_core_e2(
        core, core_solution, ground, first2, chi_prime=em["chi_E2"],
        target_B_0_to_2=5*computed_down)
    p = IBFMParameters(h["N_B"], h["two_j"], h["epsilon_d_MeV"],
                       h["kappa_MeV"], h["chi_H"], h["v_squared"], qjj,
                       h["Gamma0_MeV"], h["Lambda0_MeV"], h["A0_MeV"])
    kernel = IBFMKernel(p)
    solution = kernel.solve()

    energy_path = ROOT/"outputs/l4/20261105-ba129-model-readiness/energy-fit-contract.json"
    if energy_path not in locked:
        raise ValueError("the state mapping contract is not locked")
    energy_contract = json.loads(energy_path.read_text())
    mapping = {}
    for row in energy_contract["energy_data"]:
        choices = solution.indices_for_J(row["twice_I"])
        ordinal = row["model_ordinal_assumed"]
        if len(choices) <= ordinal:
            raise ValueError(f"missing model spin/ordinal: {row['level_id']}")
        mapping[row["level_id"]] = {**row, "spectrum_index": int(choices[ordinal])}
    anchor = mapping[energy_contract["energy_reference_level"]]
    offset = solution.energies[anchor["spectrum_index"]]
    energy_rows = []
    for row in mapping.values():
        predicted = float(1000*(solution.energies[row["spectrum_index"]]-offset))
        observed = row["energy_keV"]-anchor["energy_keV"]
        energy_rows.append({**row, "model_relative_energy_keV": predicted,
                            "observed_relative_energy_keV": observed,
                            "residual_keV": predicted-observed})
    residuals = [r["residual_keV"] for r in energy_rows if r["level_id"] != anchor["level_id"]]
    energy_rms = float(np.sqrt(np.mean(np.square(residuals))))
    print(json.dumps({"stage": "energy-and-core-calibration",
                      "RMS_keV_not_refitted": energy_rms, "eB_eb": calibration.eB}), flush=True)

    # Dividing E2 by eB preserves the fixed eF/eB interference. Photon
    # a,b and eta then have the same unit-tensor convention as the old test.
    eq = kernel.e2(1., em["e_F_eb"]/calibration.eB, em["chi_E2"])
    jt = kernel.particle_j()
    photon_contract = json.loads((ROOT/contract["photon_contract"]).read_text())
    photon_rows = []
    for pair in photon_contract["pairs"]:
        ip, it, ir = (mapping[pair[k]]["spectrum_index"]
                      for k in ("parent_id", "target_final_id", "reference_final_id"))
        statistical = solution.two_J[ip]+1
        qt = transition_rme(solution, eq, ip, it)
        qr = transition_rme(solution, eq, ip, ir)
        j = transition_rme(solution, jt, ip, it)
        jr = transition_rme(solution, jt, ip, ir)
        bqt, bqr, bjt = (float(abs(v)**2/statistical) for v in (qt, qr, j))
        if bqr <= 1e-20 or abs(jr) > 1e-10:
            raise ValueError("reference branch violates the declared E2 ratio contract")
        et, er = pair["target_energy_MeV"], pair["reference_energy_MeV"]
        photon_rows.append({
            **pair, "unit_BQ_target": bqt, "unit_BQ_reference": bqr, "unit_Bj_target": bjt,
            "physical_BE2_target_e2b2": calibration.eB**2*bqt,
            "physical_BE2_reference_e2b2": calibration.eB**2*bqr,
            "electric_ratio_a": (et/er)**5*bqt/bqr,
            "magnetic_ratio_coefficient_b_per_MeV2": et**3/er**5*bjt/bqr,
            "signed_RME_Q_normalized": [float(qt.real), float(qt.imag)],
            "signed_RME_j": [float(j.real), float(j.imag)],
        })
    anchors = [r for r in photon_rows if r["role"] == "scale-calibration"]
    if len(anchors) != 1:
        raise ValueError("one and only one existing anchor is required")
    scale = anchors[0]
    b = scale["magnetic_ratio_coefficient_b_per_MeV2"]
    eta = ((scale["reported_photon_ratio"]-scale["electric_ratio_a"])/b
           if b > 1e-20 else None)
    valid = eta is not None and eta >= 0
    for row in photon_rows:
        a, b = row["electric_ratio_a"], row["magnetic_ratio_coefficient_b_per_MeV2"]
        prediction = a+eta*b if valid else None
        row["predicted_photon_ratio"] = prediction
        row["prediction_over_reported_ratio"] = prediction/row["reported_photon_ratio"] if valid else None
        row["predicted_radiative_E2_fraction"] = a/prediction if valid and prediction > 0 else None
        row["eta_required_by_individual_central_ratio_MeV2"] = (
            (row["reported_photon_ratio"]-a)/b if b > 1e-20 else None)
    core_rows = []
    for two_J in (0, 4, 6, 8, 12):
        for ordinal, index in enumerate(core_solution.indices_for_J(two_J)[:2]):
            core_rows.append({"two_J": two_J, "ordinal": ordinal,
                              "excitation_keV": float(1000*(core_solution.energies[index]
                                                           - core_solution.energies[ground]))})
    for path, digest in locked.items():
        if sha(path) != digest:
            raise RuntimeError(f"input/producer changed during case: {path}")
    result = {
        "schema": "ba129-declared-ibfm-prediction-v1",
        "scope": contract["scope"], "parameters": asdict(p), "Qjj_validation": qcheck,
        "effective_HBF_coefficients": {"Gamma_jj": p.Gamma0*p.gamma_jj,
                                      "Lambda_jj_j": p.exchange_coefficient,
                                      "monopole_coefficient_of_nd": p.A0},
        "core_calibration": {**asdict(calibration), "target_B_2_to_0_e2b2": computed_down,
                             "eF_eb": em["e_F_eb"], "eF_over_eB": em["e_F_eb"]/calibration.eB,
                             "chi_E2": em["chi_E2"]},
        "core_levels": core_rows, "energy_comparison": energy_rows,
        "energy_RMS_keV_not_refitted": energy_rms,
        "energy_max_abs_residual_keV": max(abs(x) for x in residuals),
        "photon_scale_status": ("central-anchor-calibrated" if valid else
                               "anchor-fails-negative-or-undefined-scale"),
        "anchor_eta_MeV2": eta, "photon_pairs": photon_rows,
        "dimensions": {"full_product": kernel.dimension, "odd_Mhalf": len(solution.energies),
                       "core_Mzero": len(core_solution.energies)},
        "core_diagnostics": dict(core_solution.diagnostics),
        "odd_diagnostics": dict(solution.diagnostics),
        "input_sha256": {str(p.relative_to(ROOT)): v for p,v in locked.items()},
        "runtime": {"python": platform.python_version(), "numpy": np.__version__,
                    "elapsed_seconds": time.perf_counter()-started},
        "boundaries": [
            "Source-supported reconstruction; exact author core/NB card and full PBOS convention are not established.",
            "No Hamiltonian parameter was fitted here; original calibration-state selection is not supplied.",
            "One common magnetic scale is calibrated. No experimental core gB or physical delta sign is invented.",
            "Previous rotor results informed comparator choice; the research process is not blinded.",
            "Quoted source errors are not converted into model confidence intervals or p-values.",
            "No transfer strength, complete lifetime or collective-mode verdict is produced.",
        ],
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir/"prediction.json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")
    print(json.dumps({"output": str(output_dir/"prediction.json"),
                      "eta_MeV2": eta, "photon_scale_status": result["photon_scale_status"]}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    run(args.contract.resolve(), args.output_dir.resolve())
