#!/usr/bin/env python3
"""Independent bounded 129Ba source/convention audit; writes only beside this file."""
import csv
import hashlib
import io
import json
import math
import platform
from pathlib import Path

import numpy as np

OUT = Path("/workspace/wiki/tmp/ba129-model-replay-review")
J2 = 11
J = J2 / 2
MASS = 129
BETA = 0.24
GAMMA_DEG = 21.0
GAP = 1.0
LAMBDA_TILDE = 1.5
INPUTS = [
    "raw/papers/1975_MeyerTerVehn_CollectiveOddANuclei_PartI.pdf",
    "raw/papers/gpt/query/20261105-ba129-model-readiness/gizon1977-main.pdf",
    "tmp/ba129-model-readiness/model_probe.py",
    "tmp/ba129-model-readiness/model-probe.json",
    "system/scripts/day23_prm_basis_rotor.py",
]
FIG4_LEVELS = [
    # Printed theory levels, transcribed visually; eigenvalue rank fixed before comparison.
    (7, 0, 277), (9, 0, -31), (11, 0, 0), (13, 0, 301), (15, 0, 435),
    (17, 0, 1037), (19, 0, 1095), (21, 0, 2005), (23, 0, 1995), (27, 0, 3147),
    (9, 1, 844), (9, 2, 1038), (11, 1, 758), (11, 2, 1106), (11, 3, 1331),
]


def write(name, text):
    path = OUT / name
    assert OUT.resolve() == OUT and path.resolve().parent == OUT
    path.write_text(text, encoding="utf-8")


def write_json(name, value):
    write(name, json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def spin(two_j):
    m = np.arange(-two_j, two_j + 1, 2) / 2
    raising = np.zeros((two_j + 1, two_j + 1), complex)
    for n, projection in enumerate(m[:-1]):
        raising[n + 1, n] = math.sqrt((two_j / 2 - projection) * (two_j / 2 + projection + 1))
    return [(raising + raising.conj().T) / 2,
            (raising - raising.conj().T) / (2j), np.diag(m)]


def embedding(two_i):
    """Part I (2.16), (2.27): j+K and j+Omega even, partner phase (-1)^(I-j)."""
    keys = [(k, omega) for k in range(-two_i, two_i + 1, 2)
            for omega in range(-J2, J2 + 1, 2)
            if (J2 + k) % 4 == 0 and (J2 + omega) % 4 == 0]
    p = np.zeros(((two_i + 1) * (J2 + 1), len(keys)))
    phase = (-1) ** ((two_i - J2) // 2)
    for col, (k, omega) in enumerate(keys):
        pos = ((k + two_i) // 2) * (J2 + 1) + (omega + J2) // 2
        opposite = ((-k + two_i) // 2) * (J2 + 1) + (-omega + J2) // 2
        p[pos, col] = 1 / math.sqrt(2)
        p[opposite, col] = phase / math.sqrt(2)
    assert p.shape[1] == (two_i + 1) * (J2 + 1) // 4
    assert np.max(abs(p.T @ p - np.eye(p.shape[1]))) < 1e-14
    return p


def intrinsic(scale, gamma=GAMMA_DEG, beta=BETA, mass=MASS, lambda_override=None):
    axes = spin(J2)
    x, y, z = axes
    angle = math.radians(gamma)
    q = (math.cos(angle) * (3 * z @ z - J * (J + 1) * np.eye(J2 + 1))
         + math.sqrt(3) * math.sin(angle) * (x @ x - y @ y)) / (4 * J * (J + 1))
    kappa = 206 / mass ** (1 / 3)
    hsp = scale * kappa * beta * q
    eigenvalues, vectors = np.linalg.eigh(hsp)
    assert np.max(abs(eigenvalues[::2] - eigenvalues[1::2])) < 1e-12
    distinct = eigenvalues[::2]
    lam = distinct[-1] + LAMBDA_TILDE * (distinct[-2] - distinct[-1])
    if lambda_override is not None:
        lam = lambda_override
    energies = np.hypot(eigenvalues - lam, GAP)
    u = np.sqrt((1 + (eigenvalues - lam) / energies) / 2)
    v = np.sqrt((1 - (eigenvalues - lam) / energies) / 2)
    umat = (vectors * u) @ vectors.conj().T
    vmat = (vectors * v) @ vectors.conj().T
    emat = (vectors * energies) @ vectors.conj().T
    j0 = beta ** 2 * mass ** (7 / 3) / (2 * 204)
    moments = np.array([4 / 3 * j0 * math.sin(angle - 2 * math.pi * k / 3) ** 2
                        for k in [1, 2, 3]])
    return axes, hsp, umat, vmat, emat, moments, {
        "scale_relative_to_spin_quadrupole": scale,
        "mass_in_prescriptions": mass, "kappa_MeV": kappa, "beta": beta, "gamma_deg": gamma,
        "J0_hbar2_per_MeV": j0, "inertias_1_2_3": moments.tolist(),
        "epsilon_ascending_Kramers_pairs_MeV": distinct.tolist(),
        "lambda_tilde_anchor_input": LAMBDA_TILDE if lambda_override is None else None,
        "lambda_tilde_actual": float((lam - distinct[-1]) / (distinct[-2] - distinct[-1])),
        "lambda_F_MeV": float(lam),
        "gap_MeV": GAP,
        "mean_BCS_particle_count": float(np.sum(v * v)),
    }


def rotor_full(two_i, moments):
    axes = spin(J2)
    body = spin(two_i)
    body[1] = -body[1]  # transpose representation, anomalous body-frame commutator
    full_dim = (two_i + 1) * (J2 + 1)
    hrot = np.zeros((full_dim, full_dim), complex)
    for ia, ja, inertia in zip(body, axes, moments):
        r = np.kron(ia, np.eye(J2 + 1)) - np.kron(np.eye(two_i + 1), ja)
        hrot += r @ r / (2 * inertia)
    return hrot


def hamiltonian(two_i, scale, qp_sign=1, gamma=GAMMA_DEG, mass=MASS, lambda_override=None):
    axes, hsp, umat, vmat, emat, moments, info = intrinsic(
        scale, gamma, mass=mass, lambda_override=lambda_override)
    hrot = rotor_full(two_i, moments)
    p = embedding(two_i)
    u = np.kron(np.eye(two_i + 1), umat)
    v = np.kron(np.eye(two_i + 1), vmat)
    e = np.kron(np.eye(two_i + 1), emat)
    full = u @ hrot @ u + v @ hrot @ v + qp_sign * e
    reduced = p.conj().T @ full @ p
    info.update({
        "dimension": reduced.shape[0],
        "D2_sector_leakage_MeV": float(np.max(abs(full @ p - p @ reduced))),
        "hermiticity_error_MeV": float(np.max(abs(reduced - reduced.conj().T))),
    })
    assert info["D2_sector_leakage_MeV"] < 1e-10
    assert info["hermiticity_error_MeV"] < 1e-10
    return reduced, info


def controls(all_results, input_hashes):
    angular = spin(J2)
    body = spin(11)
    body[1] *= -1
    normal_error = np.max(abs(angular[0] @ angular[1] - angular[1] @ angular[0] - 1j * angular[2]))
    body_error = np.max(abs(body[0] @ body[1] - body[1] @ body[0] + 1j * body[2]))
    spherical = []
    for two_i in [7, 9, 11, 13, 19]:
        p = embedding(two_i)
        eigen = np.linalg.eigvalsh(p.T @ rotor_full(two_i, [10.0] * 3) @ p)
        analytic = []
        for r in range(abs(two_i - J2) // 2, (two_i + J2) // 2 + 1):
            multiplicity = r // 2 + (1 if r % 2 == 0 else 0)
            analytic += [r * (r + 1) / 20] * multiplicity
        error = float(np.max(abs(eigen - np.array(sorted(analytic)))))
        assert error < 1e-11
        spherical.append({"two_I": two_i, "dimension": len(eigen), "max_error_MeV": error})
    axes, hs, u, v, e, moments, meta = intrinsic(1, mass=130)
    xi = hs - meta["lambda_F_MeV"] * np.eye(12)
    w = np.block([[u, -v], [v, u]])
    bdg = np.block([[xi, GAP * np.eye(12)], [GAP * np.eye(12), -xi]])
    zero = np.zeros_like(e)
    nambu_error = float(np.max(abs(w.conj().T @ bdg @ w - np.block([[e, zero], [zero, -e]]))))
    hr = rotor_full(11, moments)
    ur = np.kron(np.eye(12), u)
    vr = np.kron(np.eye(12), v)
    wr = np.block([[ur, -vr], [vr, ur]])
    zeros = np.zeros_like(hr)
    rotated_rotor = wr.conj().T @ np.block([[hr, zeros], [zeros, hr]]) @ wr
    hxi = ur @ hr @ ur + vr @ hr @ vr
    eta_block = vr @ hr @ ur - ur @ hr @ vr
    rotor_bcs_error = float(np.max(abs(rotated_rotor[:144, :144] - hxi)))
    omitted_eta_error = float(np.max(abs(rotated_rotor[:144, 144:] - eta_block)))
    # Standard normalized Y20 evaluated independently in the stretched l=5 spinor.
    nodes, weights = np.polynomial.legendre.leggauss(48)
    density = (1 - nodes * nodes) ** 5
    y20 = math.sqrt(5 / (16 * math.pi)) * (3 * nodes * nodes - 1)
    gaunt = float(sum(weights * density * y20) / sum(weights * density))
    analytic_y20 = -math.sqrt(5 / (4 * math.pi)) * (2 * J - 1) / (4 * (J + 1))
    assert abs(gaunt - analytic_y20) < 1e-13
    source_axial = []
    for omega in [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]:
        q = (3 * omega * omega - J * (J + 1)) / (4 * J * (J + 1))
        source_axial.append({
            "Omega_at_gamma0": omega,
            "literal_Eq2_7_standard_Y2_epsilon_div_betaAminus1third_MeV": -206 * math.sqrt(5 / (4 * math.pi)) * q,
            "PartI_Fig4_scale_inference_epsilon_div_betaAminus1third_MeV": 206 * q,
        })
    cyclic = []
    conjugate = []
    for two_i in [7, 9, 11, 13, 19]:
        ref, _ = hamiltonian(two_i, 1, mass=130)
        shifted, _ = hamiltonian(two_i, 1, gamma=141, mass=130)
        transformed, transformed_meta = hamiltonian(
            two_i, 1, gamma=39, mass=130, lambda_override=-meta["lambda_F_MeV"])
        minus, _ = hamiltonian(two_i, 1, qp_sign=-1, gamma=39, mass=130,
                               lambda_override=-meta["lambda_F_MeV"])
        ref_e = np.linalg.eigvalsh(ref)
        cyc_error = float(np.max(abs(ref_e - np.linalg.eigvalsh(shifted))))
        conj_error = float(np.max(abs(ref_e - np.linalg.eigvalsh(transformed))))
        negative_e = np.linalg.eigvalsh(minus)
        wrong_sign_spacing_difference = float(np.max(abs(
            (ref_e - ref_e[0]) - (negative_e - negative_e[0]))))
        assert cyc_error < 1e-10 and conj_error < 1e-10
        cyclic.append({"two_I": two_i, "max_gamma_plus_120_spectrum_error_MeV": cyc_error})
        conjugate.append({
            "two_I": two_i, "positive_subspace_complement_spectrum_error_MeV": conj_error,
            "negative_e_subspace_relative_spacings_difference_MeV": wrong_sign_spacing_difference,
            "gamma_complement_deg": 39, "lambda_F_conjugate_MeV": -meta["lambda_F_MeV"],
            "lambda_tilde_in_conjugate_top_pair_convention": transformed_meta["lambda_tilde_actual"],
        })
    parent_results = json.loads((Path("/workspace/wiki") / INPUTS[3]).read_text())
    assert len(parent_results) == 4
    parent_check = []
    for original in parent_results:
        name = "literal_standard_Y2" if original["field_sign"] == 1 else "sign_reversed_standard_Y2"
        ours = next(r for r in all_results if r["case"] == name and r["qp_sign"] == original["quasiparticle_energy_sign"])
        max_error = 0.0
        for two_i, values in original["spin_twice_rows_keV_relative_to_lowest_11_2"].items():
            here = ours["relative_to_lowest_11_2_keV"][two_i][:len(values)]
            max_error = max(max_error, float(np.max(abs(np.array(here) - values))))
        assert max_error < 1e-7
        parent_check.append({"case": name, "qp_sign": ours["qp_sign"], "max_difference_keV": max_error})
    assert normal_error < 1e-12 and body_error < 1e-12
    assert nambu_error < 1e-12 and rotor_bcs_error < 1e-11 and omitted_eta_error < 1e-11
    final_hashes = {name: hashlib.sha256((Path("/workspace/wiki") / name).read_bytes()).hexdigest()
                    for name in INPUTS}
    assert input_hashes == final_hashes
    return {
        "status": "algebra_controls_pass;original_Fig4_replay_not_established",
        "normal_j_commutator_error": float(normal_error), "anomalous_body_I_commutator_error": float(body_error),
        "spherical_rotor_limit": spherical, "independent_D2_basis_matches_parent_four_cases": parent_check,
        "BCS_Nambu_Eq2_23_25_diagonalization_error_MeV": nambu_error,
        "rotor_Eq2_28_to_2_30_positive_block_error_MeV": rotor_bcs_error,
        "offdiagonal_eta_block_identity_error_MeV": omitted_eta_error,
        "omitted_eta_block_max_entry_MeV_for_I11_2": float(np.max(abs(eta_block))),
        "eta_boundary": "Part I explicitly neglects this coupling in (2.30); size is a diagnostic, not a fit correction.",
        "normalized_Y20_stretched_state_quadrature": gaunt,
        "normalized_Y20_stretched_state_formula": analytic_y20,
        "axial_field_normalization_controls": source_axial, "cyclic_axis_controls": cyclic,
        "particle_hole_complement_controls_in_explicit_matrix_convention": conjugate,
        "input_hashes_unchanged_during_run": True,
    }


def main():
    input_hashes = {name: hashlib.sha256((Path("/workspace/wiki") / name).read_bytes()).hexdigest()
                    for name in INPUTS}
    cases = {
        "literal_standard_Y2": -math.sqrt(5 / (4 * math.pi)),
        "sign_reversed_standard_Y2": math.sqrt(5 / (4 * math.pi)),
        "intrinsic_Fig4_normalization": 1.0,
        "reversed_intrinsic_Fig4_normalization": -1.0,
    }
    all_results = []
    configurations = [(name, scale, sign, 129) for name, scale in cases.items() for sign in [1, -1]]
    configurations.append(("intrinsic_Fig4_normalization_even_core_A130", 1.0, 1, 130))
    for name, scale, sign, mass in configurations:
        results, metadata = {}, None
        for two_i in [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 27]:
            h, info = hamiltonian(two_i, scale, sign, mass=mass)
            results[two_i] = np.linalg.eigvalsh(h)
            if two_i == 11:
                metadata = info
        zero = results[11][0]
        relative = {str(i): ((e[:5] - zero) * 1000).tolist() for i, e in results.items()}
        row = {
            "case": name, "qp_sign": sign, "metadata": metadata,
            "field_reference": "Part I 1975 printed p125 Fig4 inference"
                               if "intrinsic_Fig4" in name else "Part I printed Eq2.7 with standard normalized Y2",
            "relative_to_lowest_11_2_keV": relative,
        }
        all_results.append(row)
        print(name, sign, {i: round(relative[str(i)][0], 6) for i in [7, 9, 13, 15, 19]})
    assert OUT.resolve() == OUT
    write_json("convention-cases.json", all_results)
    check = controls(all_results, input_hashes)
    write_json("checks.json", check)
    comparison = []
    for result in all_results:
        for two_i, rank, printed in FIG4_LEVELS:
            calculated = result["relative_to_lowest_11_2_keV"][str(two_i)][rank]
            comparison.append({
                "case": result["case"], "qp_sign": result["qp_sign"],
                "two_I": two_i, "within_spin_rank_zero_based": rank,
                "printed_theory_keV": printed, "calculated_keV": calculated,
                "residual_calculated_minus_printed_keV": calculated - printed,
                "within_0p5_keV_printed_integer_rounding": abs(calculated - printed) <= 0.5,
                "locator": "Gizon1977 printed p473 Fig4 Theory panel; upright crop",
            })
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=list(comparison[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(comparison)
    write("fig4-comparison.csv", stream.getvalue())
    summary = []
    for result in all_results:
        rows = [r for r in comparison if r["case"] == result["case"] and r["qp_sign"] == result["qp_sign"]
                and not (r["two_I"] == 11 and r["within_spin_rank_zero_based"] == 0)]
        residuals = np.array([r["residual_calculated_minus_printed_keV"] for r in rows])
        summary.append({
            "case": result["case"], "qp_sign": result["qp_sign"],
            "nonreference_printed_levels_compared": len(rows),
            "RMS_residual_keV": float(np.sqrt(np.mean(residuals ** 2))),
            "max_abs_residual_keV": float(np.max(abs(residuals))),
            "pass_count_at_printed_integer_rounding_0p5_keV": sum(r["within_0p5_keV_printed_integer_rounding"] for r in rows),
            "is_original_replay": False,
        })
    write_json("review-summary.json", {
        "status": "bounded_convention_audit_complete;original_model_replay_not_established",
        "input_sha256": input_hashes, "environment": {"python": platform.python_version(), "numpy": np.__version__},
        "source_parameters_fixed": {"j": J, "beta": BETA, "gamma_deg": GAMMA_DEG, "gap_MeV": GAP,
                                    "lambda_tilde": LAMBDA_TILDE, "strength_coefficient": 206, "inertia_coefficient": 204},
        "field_inference": "scale=+1 is inferred from Part I p125 Fig4 axial ordering and approximate scale; it is not a silent correction to literal standard-Y2 Eq2.7.",
        "A130_boundary": "Part I p114 defines an even core of mass A; A130 is a conditional interpretation for a 129Ba hole system. Gizon Fig4 does not print the mass used in (2.52)-(2.53).",
        "parameter_search": "none; four algebraic field conventions and two signs at A129, plus one source-motivated A130 positive-branch check; no optimization",
        "comparison_rule": "rank fixed by ascending printed levels at each I; common energy zero is lowest 11/2; no fitted offset, energy scaling, or state cherry-picking",
        "comparison": summary,
        "still_missing": [
            "Unambiguous operator normalization/sign connecting Part I printed (2.7)/(2.52) to its p125 single-particle figure.",
            "Explicit physical hole/positive-energy branch selection and energy-order prescription connecting (2.31) to Gizon Fig4.",
            "Mass used in empirical field/inertia prescriptions; unrounded numerical beta, gamma, lambda anchors, and coefficients if exact integer-level reproduction is required.",
            "Original eigenvector/band-label assignment if a replay of Fig4 transition arrows and (Ktilde,Omegatilde) families is requested.",
        ],
        "writes_confined_to": str(OUT), "network_git_get_paper_subagents_used": False,
    })
    print(json.dumps({"checks": check["status"], "conditional_A130_case": summary[-1]}, indent=2))


if __name__ == "__main__":
    main()
