#!/usr/bin/env python3
"""Exact unpaired, fixed-geometry particle-rotor control in a declared I window."""
import os

THREAD_KEYS = (
    "OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
    "BLIS_NUM_THREADS", "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS",
)
for _key in THREAD_KEYS:
    os.environ[_key] = "1"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

import csv
import ctypes
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import sys
import time

import numpy as np
from scipy import linalg, sparse

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
sys.path.insert(0, str(ROOT / "system/scripts/analysis"))
from paired_single_j_rotor import d2_embedding, _spin_matrices, quadrupole_operator
from paired_single_j_em import _product_rme, clebsch_gordan as cg
from quadrupole_scalar_invariants import (
    FullRepresentation, Multiplet, ReducedQuadrupole,
    reduced_invariants, direct_invariants, j_plus_two_proxy,
)


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def maxabs(value):
    data = value.data if sparse.issparse(value) else np.asarray(value)
    return float(np.max(abs(data))) if data.size else 0.0


def real(value):
    z = complex(value)
    assert abs(z.imag) < 1e-10, z
    return float(z.real)


def check_small(value, tol=1e-10):
    value = float(value)
    if not math.isfinite(value) or value > tol:
        raise AssertionError(f"Residual {value} exceeds {tol}")
    return value


def write_json(name, data):
    with (OUT / name).open("x", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, allow_nan=False)
        handle.write("\n")


def write_csv(name, records):
    with (OUT / name).open("x", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)


def frozen_inputs(protocol):
    for rel, expected in protocol["input_sha256"].items():
        assert sha(ROOT / rel) == expected, rel


def independent_spin(two_J):
    """Local SU(2) definition used in the independent rotation-integral route."""
    spin = two_J / 2
    projections = np.arange(two_J + 1) - spin
    raising = np.zeros((two_J + 1, two_J + 1), complex)
    for col in range(two_J):
        m = projections[col]
        raising[col + 1, col] = math.sqrt(spin * (spin + 1) - m * (m + 1))
    return (raising + raising.T) / 2, (raising - raising.T) / (2j), np.diag(projections)


def small_d(two_J, beta):
    jy = independent_spin(two_J)[1]
    d = linalg.expm(-1j * beta * jy)
    check_small(maxabs(d.imag))
    return d.real


def euler_integral(two_i, two_f, mu, q_intrinsic, nodes):
    """Numerical normalized rotor lab matrix, with alpha/gamma Fourier selection.

    No CG or reduced-matrix-element routine occurs inside this integral.
    Mi=1/2, Mf=Mi+mu. Product intrinsic particle coordinates are identity.
    """
    xi, weights = np.polynomial.legendre.leggauss(nodes)
    result = np.zeros((two_f + 1, two_i + 1))
    m_i, m_f = 1, 1 + 2 * mu
    ii, ff = (m_i + two_i) // 2, (m_f + two_f) // 2
    norm = math.sqrt((two_i + 1) * (two_f + 1)) / 2
    for x, weight in zip(xi, weights):
        beta = math.acos(float(x))
        di, df, d2 = small_d(two_i, beta), small_d(two_f, beta), small_d(4, beta)
        for col, ki in enumerate(range(-two_i, two_i + 1, 2)):
            for nu, amplitude in q_intrinsic.items():
                kf = ki + 2 * nu
                if abs(kf) <= two_f:
                    row = (kf + two_f) // 2
                    result[row, col] += (
                        weight * norm * df[ff, row] * d2[mu + 2, nu + 2]
                        * di[ii, col] * amplitude
                    )
    return result


def blas_threads():
    """Read actual loaded OpenBLAS thread counts when exported symbols exist."""
    records = []
    maps = Path("/proc/self/maps")
    if not maps.exists():
        return [{"query_available": False, "reason": "No local process maps"}]
    names = set()
    for line in maps.read_text().splitlines():
        fields = line.split()
        if fields and "openblas" in fields[-1].lower() and fields[-1].startswith("/"):
            names.add(fields[-1])
    for name in sorted(names):
        lib = ctypes.CDLL(name)
        found = False
        for symbol in (
            "openblas_get_num_threads", "openblas_get_num_threads64_",
            "scipy_openblas_get_num_threads", "scipy_openblas_get_num_threads64_",
        ):
            try:
                function = getattr(lib, symbol)
            except AttributeError:
                continue
            function.argtypes = []
            function.restype = ctypes.c_int
            count = int(function())
            assert count == 1, (name, count)
            records.append({"library": Path(name).name, "symbol": symbol, "num_threads": count})
            found = True
            break
        if not found:
            records.append({"library": Path(name).name, "query_available": False})
    return records or [{"query_available": False, "reason": "No OpenBLAS library found"}]


def scalar_record(result):
    return {
        "q2": result.q2, "q3": result.q3, "signed_ratio": result.raw_ratio,
        "angle_deg": result.rigid_equivalent_angle_deg, "angle_status": result.angle_status,
    }


def proxy_record(table, initial, count):
    proxy = j_plus_two_proxy(table, initial, max_states=count)
    selected = [i for i, state in enumerate(table.multiplets) if state.two_J == 15]
    if count is not None:
        selected = selected[:count]
    u = table.rme[selected, initial]
    terms = u[:, None].conj() * table.rme[np.ix_(selected, selected)] * u[None, :]
    diagonal = real(np.trace(terms))
    return {
        "n": count, "states_used": len(selected),
        "strength_S": proxy.quadratic_strength_sum,
        "q2_closure_contribution": proxy.quadratic_closure_contribution,
        "signed_chain_C": real(proxy.cubic_chain),
        "chain_middle_diagonal": diagonal,
        "chain_middle_offdiagonal": real(proxy.cubic_chain) - diagonal,
        "raw_ratio": proxy.raw_proxy_ratio,
        "angle_deg": proxy.proxy_angle_deg, "angle_status": proxy.angle_status,
    }


def main():
    clock = time.perf_counter()
    started = now()
    protocol_path = OUT / "protocol.json"
    protocol = json.loads(protocol_path.read_text())
    protocol_hash = sha(protocol_path)
    frozen_inputs(protocol)
    model = protocol["model"]
    spins = model["two_I_window"]
    two_j = model["two_j"]
    particle = _spin_matrices(two_j)
    eye_j = np.eye(two_j + 1)
    gamma = math.radians(model["gamma_deg"])
    q_intrinsic = {0: math.cos(gamma), -2: math.sin(gamma) / math.sqrt(2),
                   2: math.sin(gamma) / math.sqrt(2)}
    intrinsic = {nu: value * eye_j for nu, value in q_intrinsic.items()}
    qj = quadrupole_operator(two_j, model["gamma_deg"])
    blocks, preflight, bare = {}, {}, {}
    for two_I in spins:
        p = d2_embedding(two_I, two_j)
        ordinary = _spin_matrices(two_I)
        body = (ordinary[0], -ordinary[1], ordinary[2])
        eye_I = np.eye(two_I + 1)
        r_ops = [np.kron(b, eye_j) - np.kron(eye_I, j)
                 for b, j in zip(body, particle)]
        hrot = sum(r @ r / (2 * inertia)
                   for r, inertia in zip(r_ops, model["inertias_hbar2_per_MeV"]))
        field = np.kron(eye_I, qj)
        projector = p @ p.conj().T
        rotations = [
            np.kron(linalg.expm(-1j * math.pi * b), linalg.expm(1j * math.pi * j))
            for b, j in zip(body, particle)
        ]
        group = (np.eye(projector.shape[0]) + sum(rotations)) / 4
        metrics = {
            "two_I": two_I, "product_dimension": p.shape[0], "physical_D2_states": p.shape[1],
            "embedding_orthonormality": check_small(maxabs(p.conj().T @ p - np.eye(p.shape[1]))),
            "independent_D2_group_projector": check_small(maxabs(group - projector)),
            "D2_group_invariance": check_small(max(maxabs(u @ p - p) for u in rotations)),
            "Hrot_Hermiticity": check_small(maxabs(hrot - hrot.conj().T)),
            "field_Hermiticity": check_small(maxabs(field - field.conj().T)),
            "Hrot_D2_leakage": check_small(maxabs(hrot @ p - p @ (p.conj().T @ hrot @ p))),
            "field_D2_leakage": check_small(maxabs(field @ p - p @ (p.conj().T @ field @ p))),
            "right_body_anomalous_commutator": check_small(
                maxabs(body[0] @ body[1] - body[1] @ body[0] + 1j * body[2])),
        }
        preflight[str(two_I)] = metrics
        blocks[two_I] = {
            "p": p, "hrot": p.conj().T @ hrot @ p,
            "field": p.conj().T @ field @ p, "r2": p.conj().T @ sum(r @ r for r in r_ops) @ p,
        }
        if two_I == two_j:
            r0 = np.eye(two_j + 1).ravel() / math.sqrt(two_j + 1)
            r0_d2 = p.conj().T @ r0
            right_limit = max(maxabs(r @ r0) for r in r_ops)
            wrong_y = np.kron(ordinary[1], eye_j) - np.kron(eye_I, particle[1])
            wrong_energy = real(np.vdot(r0, wrong_y @ wrong_y @ r0)) / (
                2 * model["inertias_hbar2_per_MeV"][1])
            spectator = {
                "R0_vector_norm_residual": check_small(abs(np.vdot(r0, r0) - 1)),
                "R0_D2_membership_residual": check_small(maxabs(projector @ r0 - r0)),
                "all_Rk_annihilation_residual": check_small(right_limit),
                "R0_Hrot_energy_MeV": real(np.vdot(r0, hrot @ r0)),
                "wrong_Iy_sign_R0_energy_MeV": wrong_energy,
            }
            assert wrong_energy > 1e-6
    check_small(maxabs(particle[0] @ particle[1] - particle[1] @ particle[0] - 1j * particle[2]))

    max_em_leakage = 0.0
    for two_f in spins:
        for two_i in spins:
            product = _product_rme(two_i, two_f, two_j, 2, intrinsic)
            pi, pf = blocks[two_i]["p"], blocks[two_f]["p"]
            bare[two_f, two_i] = pf.conj().T @ product @ pi
            max_em_leakage = max(
                max_em_leakage, maxabs(product @ pi - pf @ bare[two_f, two_i]))
    check_small(max_em_leakage)

    euler_checks = []
    for two_i, two_f in ((11, 7), (11, 11), (11, 15), (15, 15)):
        product = _product_rme(two_i, two_f, two_j, 2, intrinsic)
        for mu in (0, 1):
            integral24 = euler_integral(two_i, two_f, mu, q_intrinsic, 24)
            integral48 = euler_integral(two_i, two_f, mu, q_intrinsic, 48)
            lab = product * cg(two_i, 1, 4, 2 * mu, two_f, 1 + 2 * mu) / math.sqrt(two_f + 1)
            euler_checks.append({
                "two_Ii": two_i, "two_If": two_f, "mu": mu,
                "quadrature_24_vs_48": check_small(maxabs(integral24 - integral48)),
                "independent_integral_vs_product_WE": check_small(
                    maxabs(np.kron(integral48, eye_j) - lab)),
            })

    # Independent even-core R=2 D2 rotor for the spectator energy/strength limit.
    core_spin = independent_spin(4)
    core_rotations = [linalg.expm(-1j * math.pi * x) for x in core_spin]
    core_projector = (np.eye(5) + sum(core_rotations)) / 4
    values, vectors = np.linalg.eigh(core_projector)
    core_p = vectors[:, values > .5]
    assert core_p.shape[1] == 2
    hcore = sum(x @ x / (2 * inertia)
                for x, inertia in zip(core_spin, model["inertias_hbar2_per_MeV"]))
    core2_energies = np.linalg.eigvalsh(core_p.conj().T @ hcore @ core_p)

    # Whole-multiplet projected window. No global infinite-rotor completeness claim.
    offsets, magnetic_offsets, multiplets = {}, {}, []
    states_total, dimension = 0, 0
    for two_I in spins:
        count = blocks[two_I]["p"].shape[1]
        offsets[two_I] = states_total
        magnetic_offsets[two_I] = dimension
        multiplets.extend(Multiplet(f"I{two_I}/2_state{rank}", two_I) for rank in range(count))
        states_total += count
        dimension += count * (two_I + 1)
    representation = FullRepresentation(
        "D2 unpaired rotor projected I=1/2..15/2 window; rank2 complete for initial I11/2 only",
        dimension,
    )
    q_lab = {}
    for mu in range(-2, 3):
        rows = []
        for two_f in spins:
            row = []
            for two_i in spins:
                magnetic = np.zeros((two_f + 1, two_i + 1))
                for col, mi in enumerate(range(-two_i, two_i + 1, 2)):
                    mf = mi + 2 * mu
                    if abs(mf) <= two_f:
                        magnetic[(mf + two_f) // 2, col] = (
                            cg(two_i, mi, 4, 2 * mu, two_f, mf) / math.sqrt(two_f + 1)
                        )
                row.append(sparse.kron(sparse.csr_matrix(bare[two_f, two_i]),
                                       sparse.csr_matrix(magnetic), format="csr"))
            rows.append(row)
        q_lab[mu] = sparse.bmat(rows, format="csr")
    jz_parts, jp_parts = [], []
    for two_I in spins:
        sx, sy, sz = independent_spin(two_I)
        multiplicity = blocks[two_I]["p"].shape[1]
        jz_parts.append(sparse.kron(sparse.eye(multiplicity), sparse.csr_matrix(sz), format="csr"))
        jp_parts.append(sparse.kron(sparse.eye(multiplicity), sparse.csr_matrix(sx + 1j * sy),
                                    format="csr"))
    jz, jp = sparse.block_diag(jz_parts, format="csr"), sparse.block_diag(jp_parts, format="csr")
    covariance = 0.0
    spherical_hermiticity = 0.0
    for mu, tensor in q_lab.items():
        spherical_hermiticity = max(spherical_hermiticity,
                                    maxabs(tensor.conj().T - (-1)**mu * q_lab[-mu]))
        covariance = max(covariance, maxabs(jz @ tensor - tensor @ jz - mu * tensor))
        target = math.sqrt((2 - mu) * (3 + mu)) * q_lab[mu + 1] if mu < 2 else 0 * tensor
        covariance = max(covariance, maxabs(jp @ tensor - tensor @ jp - target))
    check_small(covariance)
    check_small(spherical_hermiticity)

    initial_columns = (
        magnetic_offsets[11] + np.arange(blocks[11]["p"].shape[1]) * 12 + (11 + 1) // 2
    )
    first_action = {mu: tensor[:, initial_columns].toarray() for mu, tensor in q_lab.items()}
    q2_operator = sum(a.conj().T @ a for a in first_action.values())
    q3_operator = np.zeros_like(q2_operator)
    for m in range(-2, 3):
        for n in range(-2, 3):
            p = -m - n
            if abs(p) <= 2:
                coefficient = -math.sqrt(3.5) * (-1)**n * cg(4, 2*m, 4, 2*n, 4, 2*(m+n))
                q3_operator += coefficient * first_action[-m].conj().T @ (q_lab[n] @ first_action[p])
    expected3 = protocol["closure_scope"]["expected_q3"]
    identity_checks = {
        "initial_two_I": 11, "physical_initial_state_dimension": len(initial_columns),
        "q2_identity_matrix_max_residual": check_small(maxabs(q2_operator - np.eye(len(initial_columns))), 1e-9),
        "q3_cos3gamma_identity_matrix_max_residual": check_small(
            maxabs(q3_operator - expected3 * np.eye(len(initial_columns))), 1e-9),
        "lab_rank2_covariance_residual": covariance,
        "lab_spherical_Hermiticity_residual": spherical_hermiticity,
        "charge_product_D2_leakage_residual": max_em_leakage,
    }
    high_columns = (
        magnetic_offsets[15] + np.arange(blocks[15]["p"].shape[1]) * 16 + (15 + 1) // 2
    )
    high_q2 = sum(
        real(np.sum(abs(tensor[:, high_columns].data)**2)) for tensor in q_lab.values()
    ) / len(high_columns)
    assert high_q2 < 1 - 1e-6
    boundary_check = {
        "two_I": 15, "mean_q2_over_D2_basis_states_in_projected_window": high_q2,
        "geometric_infinite_rotor_q2": 1.0,
        "boundary": "Missing I=17/2,19/2 outer channels at this initial spin. Window is not globally complete.",
    }
    preflight_seconds = time.perf_counter() - clock
    print(json.dumps({"stage": "preflight_passed", "seconds": preflight_seconds,
                      "window_multiplets": states_total, "magnetic_dimension": dimension,
                      "operator_identity": identity_checks, "boundary_check": boundary_check}), flush=True)

    cases, summaries, sector_rows, states_for_overlap = [], [], [], []
    phase_check = None
    for coupling in model["C_MeV"]:
        case_clock = time.perf_counter()
        solutions = {}
        h_checks = []
        for two_I in spins:
            h = blocks[two_I]["hrot"] + coupling * blocks[two_I]["field"]
            check_small(maxabs(h - h.conj().T))
            energies, vectors = np.linalg.eigh(h)
            residual = check_small(maxabs(h @ vectors - vectors * energies[None, :]))
            ortho = check_small(maxabs(vectors.conj().T @ vectors - np.eye(len(energies))))
            solutions[two_I] = (energies, vectors)
            h_checks.append({"two_I": two_I, "eigenpair_residual": residual,
                             "orthonormality_residual": ortho})
        rme = np.zeros((states_total, states_total), complex)
        for two_f in spins:
            ef, vf = solutions[two_f]
            for two_i in spins:
                ei, vi = solutions[two_i]
                rme[offsets[two_f]:offsets[two_f]+len(ef),
                    offsets[two_i]:offsets[two_i]+len(ei)] = vf.conj().T @ bare[two_f, two_i] @ vi
        table = ReducedQuadrupole(representation, tuple(multiplets), rme, complete=True)
        initial = offsets[11]
        closure = reduced_invariants(table, initial)
        assert closure.complete and not closure.missing_entries
        check_small(abs(closure.invariants.q2 - 1), 1e-9)
        check_small(abs(closure.invariants.q3 - expected3), 1e-9)
        energies, vectors = solutions[11]
        states_for_overlap.append((coupling, vectors))
        direct = {}
        for two_M in (1, 11):
            indices = magnetic_offsets[11] + np.arange(len(energies)) * 12 + (11 + two_M) // 2
            state = np.zeros(dimension, complex)
            state[indices] = vectors[:, 0]
            direct_result = direct_invariants(q_lab, state, representation=representation)
            direct[str(two_M)] = scalar_record(direct_result)
            check_small(abs(direct_result.q2 - closure.invariants.q2), 1e-9)
            check_small(abs(direct_result.q3 - closure.invariants.q3), 1e-9)
            if two_M == 11:
                qs_direct = math.sqrt(16 * math.pi / 5) * real(np.vdot(state, q_lab[0] @ state))
        qs_rme = math.sqrt(16 * math.pi / 5) * cg(11, 11, 4, 0, 11, 11) * real(rme[initial, initial]) / math.sqrt(12)
        check_small(abs(qs_direct - qs_rme))
        static = abs(rme[initial, initial])**2 / 12
        proxies = [proxy_record(table, initial, count) for count in protocol["proxy_counts"]]
        sectors = [
            {"two_Ia": a, "two_Ib": b, "q3": real(value)}
            for (a, b), value in sorted(closure.cubic_by_two_J_pair.items())
        ]
        positive = sum(x["q3"] for x in sectors if x["q3"] > 0)
        negative = sum(x["q3"] for x in sectors if x["q3"] < 0)
        check_small(abs(positive + negative - expected3), 1e-9)
        core_r0 = float(abs(np.vdot(r0_d2, vectors[:, 0]))**2)
        if coupling == 0:
            spectator.update({
                "lowest_energy_MeV": real(energies[0]),
                "ground_fidelity_to_analytic_R0": core_r0,
                "static_Qs": qs_direct, "core_R2_eigenenergies_MeV": core2_energies.tolist(),
            })
            check_small(abs(energies[0]))
            check_small(abs(core_r0 - 1))
            check_small(abs(qs_direct))
            carrying_levels = []
            spin_fraction_residual = 0.0
            for two_f in model["required_outer_two_I"]:
                expected = (two_f + 1) / 60
                spin_fraction_residual = max(spin_fraction_residual,
                    abs(closure.quadratic_by_two_J[two_f] - expected))
                ef = solutions[two_f][0]
                strength = abs(rme[offsets[two_f]:offsets[two_f]+len(ef), initial])**2 / 12
                for rank in np.flatnonzero(strength > 1e-12):
                    delta = float(np.min(abs(core2_energies - ef[rank])))
                    check_small(delta)
                    carrying_levels.append({"two_I": two_f, "rank": int(rank),
                        "energy_MeV": float(ef[rank]), "q2_strength": float(strength[rank]),
                        "nearest_core_R2_energy_residual_MeV": delta})
            assert len(carrying_levels) == 10
            spectator["spin_fraction_analytic_max_residual"] = check_small(spin_fraction_residual)
            spectator["all_E2_carrying_levels"] = carrying_levels
            spectator["deliberately_omit_I15half"] = {
                "q2_partial": closure.invariants.q2 - closure.quadratic_by_two_J[15],
                "missing_q2": closure.quadratic_by_two_J[15], "complete": False,
            }
            assert spectator["deliberately_omit_I15half"]["missing_q2"] > .1
        if coupling == 2:
            phases = np.exp(1j * .173 * np.arange(states_total)**2)
            changed = phases[:, None].conj() * rme * phases[None, :]
            rephased = ReducedQuadrupole(representation, tuple(multiplets), changed, complete=True)
            rc = reduced_invariants(rephased, initial)
            rp = [proxy_record(rephased, initial, count) for count in protocol["proxy_counts"]]
            phase_check = {
                "C_MeV": coupling,
                "q2_difference": check_small(abs(rc.invariants.q2 - closure.invariants.q2)),
                "q3_difference": check_small(abs(rc.invariants.q3 - closure.invariants.q3)),
                "max_proxy_raw_difference": check_small(max(
                    abs(a["raw_ratio"] - b["raw_ratio"]) for a, b in zip(proxies, rp))),
            }
        own_label = multiplets[initial].label
        result = {
            "C_MeV": coupling, "state": {
                "two_I": 11, "same_I_ordinal": 0, "energy_MeV": float(energies[0]),
                "same_I_next_gap_MeV": float(energies[1] - energies[0]),
                "R2_expectation": real(np.vdot(vectors[:, 0], blocks[11]["r2"] @ vectors[:, 0])),
                "P_R0": core_r0,
            },
            "full_6j": scalar_record(closure.invariants),
            "direct_lab_by_two_M": direct,
            "closure": {"complete_within_window": closure.complete, "missing_required_RMEs": len(closure.missing_entries),
                        "reciprocity_residual": closure.reciprocity_residual,
                        "exact_for_initial_rank2_q2_q3": True, "globally_complete_rotor": False},
            "proxies": proxies,
            "quadratic_by_spin": [{"two_I": int(j), "q2": float(x)}
                                  for j, x in sorted(closure.quadratic_by_two_J.items())],
            "static": {"Qs_over_Qcal": qs_direct, "Qs_RME_over_Qcal": qs_rme,
                       "diagonal_RME_over_Qcal": real(rme[initial, initial]),
                       "q2_static_fraction": float(static),
                       "q2_other_same_I_fraction": float(closure.quadratic_by_two_J[11] - static)},
            "signed_cubic_spin_pairs": sectors,
            "cubic": {"positive_spin_pair_sum": positive, "negative_spin_pair_sum": negative,
                      "cancellation_fraction": 1 - abs(expected3) / (positive - negative),
                      "initial_triple": real(closure.cubic_by_state_pair[(own_label, own_label)])},
            "eigenpair_checks": h_checks,
            "elapsed_seconds": time.perf_counter() - case_clock,
        }
        cases.append(result)
        sector_rows.extend({"C_MeV": coupling, **sector} for sector in sectors)
        for proxy in proxies:
            summaries.append({
                "C_MeV": coupling, "proxy_n": proxy["n"] if proxy["n"] is not None else "all",
                "states_used": proxy["states_used"], "q2_full": closure.invariants.q2,
                "q3_full": closure.invariants.q3, "full_ratio": closure.invariants.raw_ratio,
                "full_angle_deg": closure.invariants.rigid_equivalent_angle_deg,
                "proxy_raw_ratio": proxy["raw_ratio"], "proxy_angle_deg": proxy["angle_deg"],
                "proxy_domain_status": proxy["angle_status"],
                "proxy_strength_S": proxy["strength_S"], "proxy_signed_chain_C": proxy["signed_chain_C"],
                "Jplus2_q2_retained": proxy["q2_closure_contribution"],
                "Qs_over_Qcal": qs_direct, "static_q2_fraction": float(static),
                "same_I_gap_MeV": result["state"]["same_I_next_gap_MeV"],
            })
        print(json.dumps({"stage": "case", "C_MeV": coupling,
                          "q2": closure.invariants.q2, "q3": closure.invariants.q3,
                          "proxies": [{"n": p["n"], "raw": p["raw_ratio"], "domain": p["angle_status"]}
                                      for p in proxies],
                          "gap_MeV": result["state"]["same_I_next_gap_MeV"],
                          "seconds": result["elapsed_seconds"]}), flush=True)
    overlaps = []
    for (cl, vl), (cr, vr) in zip(states_for_overlap, states_for_overlap[1:]):
        forward = abs(vr.conj().T @ vl[:, 0])**2
        backward = abs(vl.conj().T @ vr[:, 0])**2
        overlaps.append({
            "left_C_MeV": cl, "right_C_MeV": cr,
            "lowest_to_lowest_squared_fidelity": float(forward[0]),
            "left_lowest_best_right_rank": int(np.argmax(forward)),
            "right_lowest_best_left_rank": int(np.argmax(backward)),
            "forward_best_fidelity": float(np.max(forward)),
            "backward_best_fidelity": float(np.max(backward)),
            "forward_second_largest_fidelity": float(np.sort(forward)[-2]),
        })
    frozen_inputs(protocol)
    assert sha(protocol_path) == protocol_hash
    result = {
        "schema": "fixed-shape-exact-unpaired-rotor-results-v1",
        "started_at_utc": started, "finished_at_utc": now(),
        "actual_wall_seconds_before_serialization": time.perf_counter() - clock,
        "preflight_seconds": preflight_seconds,
        "protocol_sha256": protocol_hash, "driver_sha256": sha(Path(__file__)),
        "frozen_input_sha256": protocol["input_sha256"], "model": model,
        "finite_window": {"multiplets": states_total, "magnetic_dimension": dimension,
                          "closure_scope": protocol["closure_scope"]},
        "preflight_blocks": preflight,
        "Euler_integral_checks": euler_checks,
        "geometric_operator_identity": identity_checks,
        "spectator_R0_checks": spectator,
        "high_I_boundary_check": boundary_check,
        "multiplet_rephasing_check": phase_check,
        "cases": cases, "adjacent_state_overlaps": overlaps,
        "thread_environment": {key: os.environ[key] for key in THREAD_KEYS},
        "actual_loaded_BLAS_threads": blas_threads(),
        "boundary": "Mathematical rigid-charge control in an unpaired model. No nuclear calibration, paired projection, physical Ba assignment, global infinite-rotor truncation claim, or novelty claim.",
    }
    write_json("results.json", result)
    write_csv("summary.csv", summaries)
    write_csv("cubic-spin-sectors.csv", sector_rows)
    print("COMPLETE", json.dumps({
        "cases": len(cases), "wall_seconds": time.perf_counter() - clock,
        "BLAS": result["actual_loaded_BLAS_threads"], "overlaps": overlaps,
    }), flush=True)


if __name__ == "__main__":
    main()
