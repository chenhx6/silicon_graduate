#!/usr/bin/env python3
"""Explicit no-pairing single-j PRM variant; energy ordinals are not mode labels."""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day23_prm_basis_rotor import direct_rotor, rotor_blocks, spin_matrices, transformation


def c_value(prescription):
    j, beta, mass, shell = 5.5, 0.17, 135, 5
    factor = 195 if prescription == "Wang2009-Eq3" else 123/8*math.sqrt(5/math.pi)*(2*shell+3)
    return factor*mass**(-1/3)*beta/(j*(j+1))


def intrinsic(coupling, gamma, spin):
    j = (spin[0].shape[0]-1)/2
    return coupling/2*(math.cos(gamma)*(spin[2]@spin[2]-j*(j+1)/3*np.eye(int(2*j+1)))
                       + math.sin(gamma)/math.sqrt(3)*(spin[0]@spin[0]-spin[1]@spin[1]))


def compute(prescription):
    coupling, gamma = c_value(prescription), math.radians(-26)
    inertia, two_j = [13, 21, 4], 11
    j = two_j/2
    js = spin_matrices(two_j)
    hj = intrinsic(coupling, gamma, js)
    controls = {
        "intrinsic_single_j_trace_zero": bool(abs(np.trace(hj)) < 1e-12),
        "intrinsic_single_j_Hermitian": bool(np.max(abs(hj-hj.T.conj())) < 1e-12),
        "zero_C_intrinsic_zero": bool(np.max(abs(intrinsic(0, gamma, js))) == 0),
    }
    results, diagnostics = [], []
    for two_i in range(11, 38, 2):
        i = two_i/2
        strong, weak, u = transformation(two_i, two_j)
        hc, embed = direct_rotor(two_i, two_j, strong, inertia)
        v_full = np.kron(np.eye(two_i+1), hj)
        v = embed.T@v_full@embed
        h = hc+v
        hr = rotor_blocks(weak, inertia)+u.T@v@u
        values, vectors = np.linalg.eigh(h)
        weak_values = np.linalg.eigvalsh(hr)
        r2 = u@np.diag([r*(r+1) for r, kr in weak])@u.T
        ibody = spin_matrices(two_i); ibody[1] *= -1
        dot_ij = embed.T@sum(np.kron(ik, jk) for ik, jk in zip(ibody, js))@embed
        j_squared = [embed.T@np.kron(np.eye(two_i+1), jk@jk)@embed for jk in js]
        hermitian_error = float(np.max(abs(h-h.T.conj())))
        eigen_residual = float(np.max(abs(h@vectors-vectors*values)))
        d2_leak = float(np.max(abs(v_full@embed-embed@v)))
        two_route = float(np.max(abs(h-u@hr@u.T)))
        spectrum_error = float(np.max(abs(values-weak_values)))
        r2_comm_zero_c = float(np.max(abs(hc@r2-r2@hc)))
        # Scalar Casimir terms multiply the identity matrix, not every entry.
        casimir_error = float(np.max(abs(dot_ij-((i*(i+1)+j*(j+1))*np.eye(len(strong))-r2)/2)))
        states = []
        for ordinal in range(3):
            z = vectors[:, ordinal]
            prob = abs(u.T@z)**2
            r_margin = {r: float(sum(p for (rr, kr), p in zip(weak, prob) if rr == r))
                        for r in sorted({r for r, kr in weak})}
            expect = lambda op: float(np.vdot(z, op@z).real)
            r2_from_dist = sum(r*(r+1)*p for r, p in r_margin.items())
            a = expect(dot_ij)/(i*(i+1))
            j2 = [expect(op) for op in j_squared]
            e_coll, e_intr = expect(hc), expect(v)
            row = {
                "ordinal": ordinal, "label": f"energy-ordinal-{ordinal}",
                "energy_MeV": float(values[ordinal]), "Hcoll_MeV": e_coll, "Hintr_MeV": e_intr,
                "j_squared_s_i_l_hbar2": j2,
                "j_RMS_s_i_l_hbar": [math.sqrt(max(0, q)) for q in j2],
                "R_mean_hbar": sum(r*p for r, p in r_margin.items()),
                "R_squared_hbar2": expect(r2), "R_probabilities": r_margin,
                "g_geometry_a": a,
                "g_formula_only": "g = g_R + (g_j-g_R)*a; no physical g_j/g_R supplied",
                "norm_error": float(abs(np.vdot(z, z)-1)),
                "R_probability_norm_error": abs(sum(r_margin.values())-1),
                "R2_two_route_error": abs(expect(r2)-r2_from_dist),
                "j_casimir_error": abs(sum(j2)-j*(j+1)),
                "energy_decomposition_error_MeV": abs(float(values[ordinal])-e_coll-e_intr),
            }
            states.append(row)
        tag = f"I2_{two_i}"
        controls[tag+"_Hermitian_and_D2_closure"] = hermitian_error < 1e-12 and d2_leak < 1e-12
        controls[tag+"_total_H_two_routes"] = two_route < 1e-10 and spectrum_error < 1e-10
        controls[tag+"_eigenbasis_and_residual"] = eigen_residual < 1e-10 and float(np.max(abs(vectors.T.conj()@vectors-np.eye(len(strong))))) < 1e-12
        controls[tag+"_zero_C_rotor_R2_conserved"] = r2_comm_zero_c < 1e-10
        controls[tag+"_scalar_Casimir_identity"] = casimir_error < 1e-10
        controls[tag+"_state_normalization_and_invariants"] = all(
            max(z["norm_error"], z["R_probability_norm_error"], z["R2_two_route_error"],
                z["j_casimir_error"], z["energy_decomposition_error_MeV"]) < 1e-10 for z in states)
        diagnostics.append({"I": i, "dimension": len(strong), "H_two_route_error_MeV": two_route,
                            "eigenspectrum_two_route_error_MeV": spectrum_error,
                            "eigen_residual_MeV": eigen_residual, "D2_intrinsic_leak_MeV": d2_leak,
                            "R2_commutator_zeroC_norm": r2_comm_zero_c, "Casimir_matrix_error": casimir_error})
        results.append({"I": i, "states": states,
                        "ordinal1_minus_0_gap_MeV": float(values[1]-values[0]),
                        "a0_minus_a1": states[0]["g_geometry_a"]-states[1]["g_geometry_a"]})
    observations = {8.5: (1433.9, 1477.9), 10.5: (2159.4, 2203.9)}
    crosschecks = []
    for i, (band2, band3) in observations.items():
        result = next(q for q in results if q["I"] == i)
        gap = result["ordinal1_minus_0_gap_MeV"]*1000
        crosschecks.append({"I": i, "published_band2_level_keV": band2,
                           "published_band3_level_keV": band3,
                           "observed_E_band3_minus_band2_keV": band3-band2,
                           "mapping_B3_to_ordinal0_B2_to_ordinal1_predicted_difference_keV": -gap,
                           "mapping_B3_to_ordinal1_B2_to_ordinal0_predicted_difference_keV": gap,
                           "a0_minus_a1": result["a0_minus_a1"],
                           "boundary": "Central fixed-variant diagnostic, not a likelihood/p-value or proof that other states/models/parameter uncertainty are excluded."})
    return {"status": "declared-model-variant-computed", "parameters": {
                "A": 135, "N": 5, "j": j, "beta": .17, "gamma_deg": -26,
                "C_prescription": prescription, "C_MeV": coupling, "J_s_i_l_hbar2_per_MeV": inertia,
                "particle_hole_sign": 1, "pairing": False},
            "scope": "Independent task implementation, fixed Hamiltonian with source-specified and explicitly selected inputs. Energy ordinals are not physical mode labels; no data fitting, original producer replay or measured g/transition result.",
            "source_premises": [{"source": "knowledge/sources/streck-2018-behavior-collective-rotor-wobbling.md",
                                 "locators": ["ST18-D23-003", "ST18-D23-005"]}],
            "observational_premise": "Lv2022 SI Table1 bands2/3 same-I energy centres; no original energy covariance supplied",
            "results": results, "diagnostics": diagnostics, "published_level_crosschecks": crosschecks,
            "controls": controls, "all_controls_pass": all(controls.values()),
            "limitations": ["No full E2/M1 operator strengths, pairing, experimental response/Cov or physical g-factor calculated.",
                            "Earlier literature parameters may already be calibrated to energies; this task crosscheck is not a blind prospective held-out experiment.",
                            "The single-j model is a specified approximation; no representation of every possible TiP/SP/wobbling alternative is claimed.",
                            "Physical g_j/g_R and their calibration are still needed; a scalar g cannot reconstruct complete body-fixed geometry.",
                            "Small residuals validate this finite-matrix implementation only, not source model adequacy or actual nuclear identity."]}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--C-prescription", choices=["Wang2009-Eq11", "Wang2009-Eq3"], required=True)
    a = p.parse_args()
    result = compute(a.C_prescription)
    result["implementation_sha256"] = {
        f.name: hashlib.sha256(f.read_bytes()).hexdigest()
        for f in [Path(__file__), Path(__file__).with_name("day23_prm_basis_rotor.py")]
    }
    a.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"all_controls_pass": result["all_controls_pass"],
                      "checks": len(result["controls"]), "C_MeV": result["parameters"]["C_MeV"],
                      "same_I_central_diagnostics": result["published_level_crosschecks"]}, ensure_ascii=False))
    return 0 if result["all_controls_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
