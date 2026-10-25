#!/usr/bin/env python3
"""Declared core-only normalized E2 tensor on the fixed H009 task variant."""
import argparse
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day23_prm_basis_rotor import clebsch_gordan, direct_rotor, spin_matrices, transformation
from day23_prm_fixed_state_mapping import c_value, intrinsic


@lru_cache(None)
def strong_embedding(two_i, two_j=11):
    strong, _, _ = transformation(two_i, two_j)
    embed = np.zeros(((two_i+1)*(two_j+1), len(strong)))
    phase = (-1)**((two_i-two_j)//2)
    for col, (k, omega) in enumerate(strong):
        a, b = int(round(k+two_i/2)), int(round(omega+two_j/2))
        embed[a*(two_j+1)+b, col] = 1/math.sqrt(2)
        embed[(two_i-a)*(two_j+1)+(two_j-b), col] = phase/math.sqrt(2)
    return embed


def charge_tensor(gamma_deg, scale=1.0):
    g = math.radians(gamma_deg)
    return {0: scale*math.cos(g), 2: scale*math.sin(g)/math.sqrt(2),
            -2: scale*math.sin(g)/math.sqrt(2)}


@lru_cache(None)
def reduced_tensor(two_i, two_f, gamma_deg, two_j=11, scale=1.0):
    q = charge_tensor(gamma_deg, scale)
    k_matrix = np.zeros((two_f+1, two_i+1))
    for col, k in enumerate(np.arange(-two_i, two_i+1, 2)/2):
        for row, kf in enumerate(np.arange(-two_f, two_f+1, 2)/2):
            nu = int(round(kf-k))
            if nu in q:
                k_matrix[row, col] = math.sqrt(two_i+1)*q[nu]*clebsch_gordan(
                    two_i/2, k, 2, nu, two_f/2, kf)
    return strong_embedding(two_f, two_j).T @ np.kron(k_matrix, np.eye(two_j+1)) @ strong_embedding(two_i, two_j)


@lru_cache(None)
def model_sector(two_i, prescription):
    strong, _, _ = transformation(two_i, 11)
    hc, embed = direct_rotor(two_i, 11, strong, [13, 21, 4])
    hj = intrinsic(c_value(prescription), math.radians(-26), spin_matrices(11))
    h = hc+embed.T@np.kron(np.eye(two_i+1), hj)@embed
    values, vectors = np.linalg.eigh(h)
    return values, vectors, embed


def strength(two_i, two_f, ordinal_i, ordinal_f, prescription, gamma_deg):
    _, di, _ = model_sector(two_i, prescription)
    _, df, _ = model_sector(two_f, prescription)
    reduced = np.vdot(df[:, ordinal_f], reduced_tensor(two_i, two_f, gamma_deg)@di[:, ordinal_i])
    return float(abs(reduced)**2/(two_i+1))


@lru_cache(None)
def jy_eigensystem(two_j):
    return np.linalg.eigh(spin_matrices(two_j)[1])


def little_d(two_j, angle):
    values, vectors = jy_eigensystem(two_j)
    return (vectors*np.exp(-1j*angle*values))@vectors.T.conj()


def quadrature_lab_amplitude(two_i, two_f, ni, nf, prescription, gamma_deg, nodes):
    _, di, ei = model_sector(two_i, prescription)
    _, df, ef = model_sector(two_f, prescription)
    ai = (ei@di[:, ni]).reshape(two_i+1, 12)
    af = (ef@df[:, nf]).reshape(two_f+1, 12)
    # Integrate beta numerically, alpha/gamma analytically by projection rules.
    # These little-d matrices come from exp(-i beta J_y), not the CG routine.
    mi, mf = two_i/2, two_f/2
    mu = mf-mi
    if abs(mu) > 2:
        return 0j
    points, weights = np.polynomial.legendre.leggauss(nodes)
    result = 0j
    for x, weight in zip(points, weights):
        angle = math.acos(x)
        fi, ii, rank2 = little_d(two_f, angle), little_d(two_i, angle), little_d(4, angle)
        for ki in range(two_i+1):
            k = -two_i/2+ki
            for nu, value in charge_tensor(gamma_deg).items():
                kf = k+nu
                row = int(round(kf+two_f/2))
                if 0 <= row <= two_f:
                    coefficient = np.vdot(af[row, :], ai[ki, :])
                    result += (weight*coefficient*value*fi[-1, row].conjugate()*ii[-1, ki]
                               * rank2[int(round(mu+2)), nu+2])
    return result*math.sqrt((two_i+1)*(two_f+1))/2


def validate(prescription, gamma_deg):
    controls, details = {}, {}
    q = charge_tensor(gamma_deg)
    controls["unit_intrinsic_rank2_tensor_norm"] = math.isclose(sum(v*v for v in q.values()), 1, abs_tol=1e-14)
    for two_i in [7, 11, 17, 21]:
        dimension = strong_embedding(two_i).shape[1]
        closure = np.zeros((dimension, dimension))
        worst_reverse = 0
        for two_f in range(max(1, two_i-4), two_i+5, 2):
            t = reduced_tensor(two_i, two_f, gamma_deg)
            reverse = reduced_tensor(two_f, two_i, gamma_deg)
            worst_reverse = max(worst_reverse, float(np.max(abs(t-(-1)**((two_f-two_i)//2)*reverse.T))))
            closure += t.T@t/(two_i+1)
        closure_error = float(np.max(abs(closure-np.eye(dimension))))
        controls[f"I2_{two_i}_operator_closure_all_final_states"] = closure_error < 1e-12
        controls[f"I2_{two_i}_Hermitian_reduced_reverse"] = worst_reverse < 1e-12
        details[f"I2_{two_i}_closure_error"] = closure_error
        details[f"I2_{two_i}_reverse_error"] = worst_reverse
    controls["rank2_triangle_forbidden_zero"] = bool(np.max(abs(reduced_tensor(17, 11, gamma_deg))) == 0)
    # Pure K=Omega=1/2 axial states, not nuclear eigenstate identifications.
    ki, _, _ = transformation(9, 11)
    kf, _, _ = transformation(5, 11)
    axial_amplitude = reduced_tensor(9, 5, 0.0)[kf.index((.5, .5)), ki.index((.5, .5))]
    controls["pure_axial_fixedK_CG_limit"] = math.isclose(
        abs(axial_amplitude)**2/10, clebsch_gordan(4.5, .5, 2, 0, 2.5, .5)**2, abs_tol=1e-14)
    t = reduced_tensor(21, 19, gamma_deg)
    controls["common_tensor_scale_multiplies_amplitude"] = bool(np.allclose(
        reduced_tensor(21, 19, gamma_deg, scale=2), 2*t, atol=1e-13))
    for two_i, two_f in [(17, 15), (21, 19), (17, 13)]:
        _, di, _ = model_sector(two_i, prescription)
        _, df, _ = model_sector(two_f, prescription)
        reduced = np.vdot(df[:, 0], reduced_tensor(two_i, two_f, gamma_deg)@di[:, 0])
        lab = reduced/math.sqrt(two_f+1)*clebsch_gordan(
            two_i/2, two_i/2, 2, (two_f-two_i)/2, two_f/2, two_f/2)
        a = quadrature_lab_amplitude(two_i, two_f, 0, 0, prescription, gamma_deg, 24)
        b = quadrature_lab_amplitude(two_i, two_f, 0, 0, prescription, gamma_deg, 40)
        controls[f"I2_{two_i}_to_{two_f}_independent_Wigner_integral"] = abs(b-lab) < 1e-11
        controls[f"I2_{two_i}_to_{two_f}_quadrature_convergence"] = abs(b-a) < 1e-11
        details[f"I2_{two_i}_to_{two_f}_quadrature_error"] = float(abs(b-lab))
    return {name: bool(value) for name, value in controls.items()}, details


def calculate(prescription, gamma_deg, reference_path):
    controls, details = validate(prescription, gamma_deg)
    previous = json.loads(reference_path.read_text())
    if previous["parameters"]["C_prescription"] != prescription:
        raise ValueError("Reference Hamiltonian prescription differs")
    same_h_error = 0.0
    for two_i in [17, 21, 25]:
        values, _, _ = model_sector(two_i, prescription)
        old = next(r for r in previous["results"] if r["I"] == two_i/2)
        same_h_error = max(same_h_error, max(abs(values[n]-old["states"][n]["energy_MeV"])
                                             for n in range(3)))
    controls["same_H_as_frozen_stage009"] = same_h_error < 1e-12
    details["same_H_as_frozen_stage009_error_MeV"] = float(same_h_error)
    rows = []
    for two_i in [17, 21, 25]:
        for parent_ordinal in [0, 1]:
            ei = float(model_sector(two_i, prescription)[0][parent_ordinal])
            ef_out = float(model_sector(two_i-2, prescription)[0][0])
            ef_same = float(model_sector(two_i-4, prescription)[0][parent_ordinal])
            ef_other = float(model_sector(two_i-4, prescription)[0][1-parent_ordinal])
            bout = strength(two_i, two_i-2, parent_ordinal, 0, prescription, gamma_deg)
            b_same = strength(two_i, two_i-4, parent_ordinal, parent_ordinal, prescription, gamma_deg)
            b_other = strength(two_i, two_i-4, parent_ordinal, 1-parent_ordinal, prescription, gamma_deg)
            reverse = strength(two_i-2, two_i, 0, parent_ordinal, prescription, gamma_deg)
            controls[f"I2_{two_i}_ordinal_{parent_ordinal}_detailed_balance"] = math.isclose(
                (two_i+1)*bout, (two_i-1)*reverse, abs_tol=1e-12)
            rows.append({"I": two_i/2, "parent_ordinal": parent_ordinal,
                         "target_Iminus1_ordinal": 0,
                         "delta_E_out_MeV": ei-ef_out,
                         "delta_E_sameordinal_Iminus2_MeV": ei-ef_same,
                         "delta_E_otherordinal_Iminus2_MeV": ei-ef_other,
                         "B_out_over_unknown_S_squared": bout,
                         "B_Iminus2_sameordinal_over_unknown_S_squared": b_same,
                         "B_Iminus2_otherordinal_over_unknown_S_squared": b_other,
                         "out_over_sameordinal_Iminus2": bout/b_same if b_same > 1e-14 else None,
                         "out_over_otherordinal_Iminus2": bout/b_other if b_other > 1e-14 else None})
    mappings = []
    for ordinal, name in [(0, "B3_to_ordinal0_B2_to_ordinal1"), (1, "B3_to_ordinal1_B2_to_ordinal0")]:
        low = next(r for r in rows if r["I"] == 8.5 and r["parent_ordinal"] == ordinal)
        high = next(r for r in rows if r["I"] == 10.5 and r["parent_ordinal"] == ordinal)
        mappings.append({"hypothesis": name, "same_ordinal_mapping_across_spins_is_assumed": True,
                         "formal_B_matrix_747_over_526": low["out_over_otherordinal_Iminus2"],
                         "gamma_decay_B_ratio_747_over_526": low["out_over_otherordinal_Iminus2"]
                             if min(low["delta_E_out_MeV"], low["delta_E_otherordinal_Iminus2_MeV"]) > 0 else None,
                         "model_delta_E_526_candidate_MeV": low["delta_E_otherordinal_Iminus2_MeV"],
                         "formal_B_matrix_813_out_over_726_in": high["out_over_sameordinal_Iminus2"],
                         "gamma_decay_B_ratio_813_over_726": high["out_over_sameordinal_Iminus2"]
                             if min(high["delta_E_out_MeV"], high["delta_E_sameordinal_Iminus2_MeV"]) > 0 else None,
                         "boundary": "Conditional mapping/operator diagnostic; same-H energy mismatch from009 remains, no likelihood or best-model claim."})
    return {"status": "conditional-core-E2-computed", "C_prescription": prescription,
            "C_MeV": c_value(prescription), "gamma_E_deg": gamma_deg, "gamma_H_deg": -26,
            "operator": "T2mu=S sum D2_mu,nu qnu; q0=cos(gammaE),q+-2=sin(gammaE)/sqrt2 in axes1s/2i/3l; core only",
            "reduced_convention": "labM=CG(IiMi,2mu|IfMf)/sqrt(2If+1)*reduced; B=abs(reduced)^2/(2Ii+1)",
            "scope": "Unknown common S factored out. No actual charge moment, absolute experimental strength, M1, delta, lifetime or response fit supplied.",
            "results": rows, "conditional_mappings": mappings, "controls": controls,
            "frozen_H_reference": {"path": str(reference_path),
                                   "sha256": hashlib.sha256(reference_path.read_bytes()).hexdigest()},
            "control_details": details, "all_controls_pass": all(controls.values()),
            "implementation_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                for p in [Path(__file__), Path(__file__).with_name("day23_prm_basis_rotor.py"),
                          Path(__file__).with_name("day23_prm_fixed_state_mapping.py")]},
            "limitations": ["Coaxial charge/potential gamma equality is a declared assumption, not measured.",
                            "Single-particle E2 is omitted from this operator; it is not asserted physically absent.",
                            "The operator closure test includes upward and elastic/diagonal matrix elements; it is not a gamma branching/count sum.",
                            "A nonzero upward B matrix element cannot be used as a spontaneous gamma-decay outlet; deltaE must be positive under the same H.",
                            "Energy ordinals across spin are only the proposed mapping; adiabatic band identity is not proven.",
                            "The 526-keV experimental denominator is a separate interband outlet, assumed E2 in the published extraction; its SI multipolarity/Rac fields are blank.",
                            "Both007 historical-source boundaries and009 fixed-H energy-mapping inadequacy remain in force.",
                            "Numerical controls validate this tensor implementation, not model adequacy or a nuclear mode."]}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--C-prescription", choices=["Wang2009-Eq11", "Wang2009-Eq3"], required=True)
    p.add_argument("--gamma-E-deg", type=float, required=True)
    p.add_argument("--reference-model", type=Path, required=True)
    a = p.parse_args()
    x = calculate(a.C_prescription, a.gamma_E_deg, a.reference_model)
    a.output.write_text(json.dumps(x, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"all_controls_pass": x["all_controls_pass"], "checks": len(x["controls"]),
                      "conditional_mappings": x["conditional_mappings"]}, ensure_ascii=False))
    return 0 if x["all_controls_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
