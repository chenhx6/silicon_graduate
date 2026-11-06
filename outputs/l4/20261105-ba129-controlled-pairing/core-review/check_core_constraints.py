#!/usr/bin/env python3
"""Independent integer-D2/low-spin E2 audit; writes only derived review files.

The parent runner is not imported or executed. D2 spaces are obtained from
finite-group rotation projectors. Reference CG coefficients come from
diagonalizing coupled angular momenta and lowering, not the parent's CG code.
Publisher images/text are neither generated nor stored here.
"""
import csv
from functools import lru_cache
import hashlib
import io
import json
import math
from pathlib import Path

import numpy as np
import pymupdf

ROOT = Path("/workspace/wiki")
BASE = ROOT / "outputs/l4/20261105-ba129-controlled-pairing"
OUT = BASE / "core-review"
PARENT = ROOT / "system/scripts/ba129_core_constraints.py"
RECORD = BASE / "core/core-constraints.json"
GREINER = ROOT / "raw/books/Nuclear Models (Walter Greiner, Joachim A. Maruhn) (Z-Library).pdf"
RAW = ROOT / "raw/papers/gpt/query/20261105-ba129-core-constraints"
METRICS = {}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(name, content):
    path = OUT / name
    assert OUT.resolve() == OUT and path.resolve().parent == OUT
    path.write_text(content, encoding="utf-8")


def check(name, a, b, atol=3e-12, rtol=3e-12):
    a, b = np.asarray(a), np.asarray(b)
    error = float(np.max(abs(a - b))) if a.size else 0.0
    METRICS[name] = max(METRICS.get(name, 0.0), error)
    if not np.allclose(a, b, atol=atol, rtol=rtol):
        raise AssertionError((name, error, a, b))


def spin(I):
    m = np.arange(I, -I - 1, -1, dtype=float)
    plus = np.diag(np.sqrt((I + m[:-1]) * (I - m[:-1] + 1)), 1)
    return [(op[::-1, ::-1]).copy() for op in
            ((plus + plus.T) / 2, (plus - plus.T) / (2j), np.diag(m))]


@lru_cache(maxsize=16)
def d2_group_basis(I):
    """Project the ordinary integer-spin irrep onto the trivial D2 irrep."""
    projector = np.eye(2 * I + 1, dtype=complex)
    for axis in spin(I):
        value, vector = np.linalg.eigh(axis)
        projector += (vector * np.exp(-1j * math.pi * value)) @ vector.conj().T
    projector /= 4
    check("D2_projector_Hermitian", projector, projector.conj().T)
    check("D2_projector_idempotent", projector @ projector, projector)
    value, vector = np.linalg.eigh((projector + projector.conj().T) / 2)
    selected = vector[:, value > 0.5]
    multiplicity = (2 * I + 1 + 3 * (-1) ** I) // 4
    assert selected.shape[1] == multiplicity
    return selected


def cartesian_spectrum(I, A):
    p = d2_group_basis(I)
    h = sum(a * j @ j for a, j in zip(A, spin(I)))
    return np.linalg.eigvalsh(p.conj().T @ h @ p)


def H2(A):
    a, b, c = A
    return np.array([[3 * (a + b), math.sqrt(3) * (a - b)],
                     [math.sqrt(3) * (a - b), a + b + 4 * c]])


def H4(A):
    a, b, c = A
    return np.array([
        [10 * (a + b), 3 * math.sqrt(5) * (a - b), 0],
        [3 * math.sqrt(5) * (a - b), 8 * (a + b) + 4 * c, math.sqrt(7) * (a - b)],
        [0, math.sqrt(7) * (a - b), 2 * (a + b) + 16 * c],
    ])


@lru_cache(maxsize=16)
def coupled_vectors(j1, j2):
    """Integer CG reference from total J^2, highest-weight phase, and J_-."""
    x1, y1, z1 = spin(j1)
    x2, y2, z2 = spin(j2)
    n1, n2 = 2 * j1 + 1, 2 * j2 + 1
    raising = np.kron(x1 + 1j * y1, np.eye(n2)) + np.kron(np.eye(n1), x2 + 1j * y2)
    lowering = raising.conj().T
    z = np.kron(z1, np.eye(n2)) + np.kron(np.eye(n1), z2)
    squared = z @ z + (raising @ lowering + lowering @ raising) / 2
    mz = np.diag(z).real
    states = {}
    for J in range(abs(j1 - j2), j1 + j2 + 1):
        indices = np.flatnonzero(mz == J)
        values, vectors = np.linalg.eigh(squared[np.ix_(indices, indices)])
        n = int(np.argmin(abs(values - J * (J + 1))))
        check("CG_J_squared_reference", values[n], J * (J + 1))
        state = np.zeros(n1 * n2, complex)
        state[indices] = vectors[:, n]
        anchor = (n1 - 1) * n2 + (J - j1 + j2)
        assert abs(state[anchor]) > 1e-12
        state *= np.exp(-1j * np.angle(state[anchor]))
        states[J, J] = state.copy()
        for M in range(J, -J, -1):
            state = lowering @ state / math.sqrt((J + M) * (J - M + 1))
            states[J, M - 1] = state.copy()
    return states


def cg(j1, m1, j2, m2, J, M):
    if m1 + m2 != M or abs(m1) > j1 or abs(m2) > j2:
        return 0.0
    state = coupled_vectors(j1, j2).get((J, M))
    if state is None:
        return 0.0
    value = state[(m1 + j1) * (2 * j2 + 1) + m2 + j2]
    assert abs(value.imag) < 1e-12
    return float(value.real)


def K_basis(I):
    columns = []
    for K in range(0, I + 1, 2):
        if K == 0 and I % 2:
            continue
        state = np.zeros(2 * I + 1)
        if K == 0:
            state[I] = 1
        else:
            state[I + K] = 1 / math.sqrt(2)
            state[I - K] = (-1) ** I / math.sqrt(2)
        columns.append(state)
    return np.column_stack(columns) if columns else np.empty((2 * I + 1, 0))


def tensor_K(Ri, Rf, gamma):
    angle = math.radians(gamma)
    q = {0: math.cos(angle), 2: math.sin(angle) / math.sqrt(2),
         -2: math.sin(angle) / math.sqrt(2)}
    matrix = np.zeros((2 * Rf + 1, 2 * Ri + 1))
    for ki in range(-Ri, Ri + 1):
        for nu, value in q.items():
            kf = ki + nu
            if abs(kf) <= Rf:
                matrix[kf + Rf, ki + Ri] += math.sqrt(2 * Ri + 1) * cg(Ri, ki, 2, nu, Rf, kf) * value
    return K_basis(Rf).T @ matrix @ K_basis(Ri)


def irrotational_A(gamma):
    if math.remainder(gamma, 60) == 0:
        raise ValueError("singular axial endpoint: evaluate only its limiting ratios")
    g = math.radians(gamma)
    return np.array([1 / (2 * math.sin(g - 2 * math.pi * k / 3) ** 2) for k in (1, 2, 3)])


def analytic_strengths(gamma):
    g = math.radians(gamma)
    s, one_minus_s = math.sin(3 * g) ** 2, math.cos(3 * g) ** 2
    d = 9 - 8 * s
    root, a = math.sqrt(d), 3 - 2 * s
    denominator = d + a * root
    return {
        "B21_2first_to_0": denominator / (10 * d),
        "B20_2second_to_0": 2 * s * one_minus_s / (5 * denominator),
        "B22_2second_to_2first": 2 * s / (7 * d),
        "B20_over_B22": (7 / 5) * root * one_minus_s / (root + a),
        "B22_over_B21": (20 / 7) * s / denominator,
    }


def angle_check(gamma):
    A = irrotational_A(gamma)
    energies, vectors = np.linalg.eigh(H2(A))
    energy4 = np.linalg.eigvalsh(H4(A))[0]
    c, s = math.cos(math.radians(gamma)), math.sin(math.radians(gamma))
    t20 = np.array([[c, s]])
    t22 = math.sqrt(10 / 7) * np.array([[-c, s], [s, c]])
    check("T20_from_independent_CG", tensor_K(2, 0, gamma), t20)
    check("T22_from_independent_CG", tensor_K(2, 2, gamma), t22)
    m20, m22 = t20 @ vectors, vectors.T @ t22 @ vectors
    b21, b20 = abs(m20[0, 0]) ** 2 / 5, abs(m20[0, 1]) ** 2 / 5
    b22 = abs(m22[0, 1]) ** 2 / 5
    predicted = analytic_strengths(gamma)
    for name, value in (("B21_2first_to_0", b21), ("B20_2second_to_0", b20),
                        ("B22_2second_to_2first", b22),
                        ("B20_over_B22", b20 / b22), ("B22_over_B21", b22 / b21)):
        check("matrix_vs_analytic_" + name, value, predicted[name])
    upward = vectors.T @ tensor_K(0, 2, gamma)
    check("upward_0_to_2_closure", np.sum(abs(upward) ** 2), 1)
    check("downward_strength_sum", b21 + b20, 1 / 5)
    return {"gamma_deg": gamma, "R4_over_2": float(energy4 / energies[0]),
            "matrix_B21": float(b21), "matrix_B20": float(b20), "matrix_B22": float(b22),
            "matrix_B20_over_B22": float(b20 / b22),
            "matrix_B22_over_B21": float(b22 / b21), **predicted}


def main():
    record = json.loads(RECORD.read_text())
    locked = dict(record["source_hashes"])
    locked.update({
        str(PARENT.relative_to(ROOT)): sha(PARENT),
        str(RECORD.relative_to(ROOT)): sha(RECORD),
        str(GREINER.relative_to(ROOT)): sha(GREINER),
    })
    assert locked[str(PARENT.relative_to(ROOT))] == record["runner_sha256"]
    for mass in (128, 130):
        path = RAW / f"nndc{mass}-adopted.pdf"
        locked[str(path.relative_to(ROOT))] = sha(path)
    for page in (164, 165, 166):
        path = ROOT / f"tmp/ba129-controlled-pairing/greiner/pdf-page-{page}.png"
        locked[str(path.relative_to(ROOT))] = sha(path)
    ko_image = ROOT / "tmp/ba129-controlled-pairing/source-pages/konigshofen-p2.png"
    locked[str(ko_image.relative_to(ROOT))] = sha(ko_image)
    for rel, digest in locked.items():
        assert sha(ROOT / rel) == digest, ("frozen input hash changed", rel)

    for I in range(9):
        p = K_basis(I)
        group = d2_group_basis(I)
        check("D2_K_basis_equals_group_projector", p @ p.T, group @ group.conj().T)
    random_constants = np.exp(np.random.default_rng(610169).uniform(-3, 2, (32, 3)))
    for A in random_constants:
        a, b, c = A
        expected2 = 2 * sum(A) + np.array([-2, 2]) * math.sqrt(a*a + b*b + c*c - a*b - a*c - b*c)
        e2 = cartesian_spectrum(2, A)
        check("I2_cartesian_vs_analytic_matrix", e2, np.linalg.eigvalsh(H2(A)))
        check("I2_closed_eigenvalues", e2, expected2)
        check("I3_scalar", cartesian_spectrum(3, A)[0], 4 * sum(A))
        check("constant_inertia_trace_identity", sum(e2), cartesian_spectrum(3, A)[0])
        check("I4_cartesian_vs_analytic_matrix", cartesian_spectrum(4, A), np.linalg.eigvalsh(H4(A)))

    controls = [angle_check(g) for g in (0.1, 1, 10, 20, 24, 26, 29, 30, 31, 40, 50, 59, 59.9)]
    g26 = next(r for r in controls if r["gamma_deg"] == 26)
    check("requested_gamma26_R4_over_2", g26["R4_over_2"], 2.7813583, atol=5e-8, rtol=0)
    check("requested_gamma26_B22_over_B21", g26["matrix_B22_over_B21"], 1.0488943, atol=5e-8, rtol=0)
    axial = analytic_strengths(0)
    maximum = analytic_strengths(30)
    check("axial_ratio_limit", axial["B20_over_B22"], 0.7)
    check("gamma30_zero_ground_branch", maximum["B20_over_B22"], 0, atol=1e-25, rtol=0)
    check("gamma30_B22_over_B21", maximum["B22_over_B21"], 10 / 7)
    assert next(r for r in controls if r["gamma_deg"] == 30)["matrix_B20"] < 1e-25

    # Literal source-expression check, not an alternative fitted Hamiltonian.
    example = np.array([1.0, 2.0, 3.0])  # A_k, with hbar=1.
    reciprocal_theta = 2 * example
    correct_h2 = H2(example)
    exercise_literal = correct_h2.copy()
    exercise_literal[0, 1] = exercise_literal[1, 0] = math.sqrt(6) * (reciprocal_theta[0] - reciprocal_theta[1])
    source_inconsistency = {
        "status": "local_printed_expressions_inconsistent_with_normalized_D2_basis",
        "locator": "Greiner printed p147 Exercise6.6(3)-(4), compared with normalized basis p145 Eq6.169 and Cartesian H on p146",
        "A_k_hbar1": example.tolist(),
        "normalized_H2": correct_h2.tolist(),
        "normalized_eigenvalues": np.linalg.eigvalsh(correct_h2).tolist(),
        "literal_exercise_H2": exercise_literal.tolist(),
        "literal_exercise_eigenvalues": np.linalg.eigvalsh(exercise_literal).tolist(),
        "offdiagonal_printed_to_normalized_factor": 2 * math.sqrt(2),
        "trace_identity_survives": True,
        "boundary": "No published erratum was searched; no skill, source page or knowledge file was changed.",
    }
    assert not np.allclose(np.linalg.eigvalsh(correct_h2), np.linalg.eigvalsh(exercise_literal))

    nuclei = {}
    for mass in (128, 130):
        item = record["core_results"][str(mass)]
        path = ROOT / item["source"]
        lines = path.read_text().splitlines()
        assert ("201510" if mass == 128 else "200107") in lines[1]
        selected = {}
        for label, stated in item["selected_levels"].items():
            number = int(stated["locator"].split()[-1])
            line = lines[number-1].ljust(80)
            assert line[:5] == f"{mass}BA" and line[5:9] == "  L "
            check("selected_ENSDF_energy_keV", float(line[9:19]), stated["energy_keV"], rtol=0)
            assert line[21:39].strip() == stated["Jpi_literal"]
            selected[label] = {"energy_keV": float(line[9:19]),
                               "Jpi_literal": line[21:39].strip(), "locator": stated["locator"]}
        e21, e22, e3, e4 = (selected[k]["energy_keV"] for k in ("2_1", "2_2", "3_1", "4_1"))
        delta = e3 - e21 - e22
        ratio = e22 / e21
        s = 9 * ratio / (2 * (1 + ratio)**2)
        gamma = math.degrees(math.asin(math.sqrt(s))) / 3
        angular = angle_check(gamma)
        controls.append(angular)
        check("core_energy_trace_violation_keV", delta, item["E3_minus_sum_E2_keV"])
        check("equal_weight_RMS_plane_lower_bound_keV", abs(delta)/3,
              item["equal_weight_three_energy_RMS_lower_bound_keV"])
        check("observed_R4_over_2", e4/e21, item["R_4_over_2"])
        check("conditional_two_energy_gamma_deg", gamma, item["irrotational_gamma_from_two_energies_only_deg"])
        check("conditional_branch_ratio_reproduced", angular["matrix_B20_over_B22"],
              item["conditional_irrotational_E2_prediction"]["ratio_matrix"])
        with pymupdf.open(RAW / f"nndc{mass}-adopted.pdf") as doc:
            first_page = doc[0].get_text()
            token = f"{e3:.2f}"
            assert token in first_page
            position = first_page.index(token)
            assert selected["3_1"]["Jpi_literal"] in first_page[position:position+70]
        nuclei[str(mass)] = {
            "selected_levels": selected, "PDF_locator": "adopted PDF physical page1",
            "E3_minus_E21_minus_E22_keV": delta, "unweighted_3point_RMS_lower_bound_keV": abs(delta)/3,
            "observed_R4_over_2": e4/e21,
            "conditional_gamma_deg": gamma, "complement_gamma_deg": 60-gamma,
            "conditional_irrotational_R4_over_2": angular["R4_over_2"],
            "conditional_B20_over_B22": angular["matrix_B20_over_B22"],
            "conditional_B22_over_B21": angular["matrix_B22_over_B21"],
            "conditional_on_3plus_assignment": selected["3_1"]["Jpi_literal"] != "3+",
        }
    assert nuclei["130"]["selected_levels"]["3_1"]["Jpi_literal"] == "3(+)"

    ko = record["konigshofen2001_branch_check"]
    # Visual source input: printed037302-2 TableI, first two rows. No table
    # image or extracted publisher text is copied to these review outputs.
    computed = (74 / 100) * (550.5 / 907.7)**5 * (1 + 1 / 75**2)
    check("Konigshofen_derived_same_input_B_ratio", computed,
          ko["derived_from_same_photon_and_mixing_inputs"])
    check("Konigshofen_reported_relative_B", 6.1 / 100, ko["reported_relative_B_E2_ratio"])
    check("Konigshofen_relative_B_margin", 0.2 / 100, ko["reported_margin"])
    assert ko["delta_E2_over_M1_Rose_Brink"] == -75
    assert ko["not_independent_of_original_RI_delta"] is True
    data_roles = {
        "locator": "Konigshofen2001 printed037302-2 TableI first two rows; publication22-Aug-2001",
        "parent_energy_keV": 907.7, "target_gamma_to_ground_keV": 907.7,
        "reference_gamma_to_2first_keV": 550.5,
        "photon_ratio": 0.74, "delta_E2_M1": -75, "delta_quoted_margin": 20,
        "reported_B20_over_B22": 0.061, "reported_margin": 0.002,
        "derived_from_same_RI_and_delta": computed,
        "IBA_CQF_prediction_not_measurement": 0.062,
        "NNDC130_separate_energy_version": {
            "header": "200107/01NDS; cutoff11-May-2001",
            "parent_energy_keV": 908.02, "ground_branch_RI": "66(3) relative to100(6)",
            "reference_gamma_keV": 550.7, "ground_gamma_keV": 908.0,
            "mixing_ratio_comment": "-0.296(7) or -40(13)",
            "boundary": "Do not merge these intensities/roots with the 2001 paper's rows into one dataset.",
        },
    }
    for rel, digest in locked.items():
        assert sha(ROOT / rel) == digest, ("input changed during review", rel)
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=list(controls[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(controls)
    write("independent-ratio-controls.csv", stream.getvalue())
    summary = {
        "status": "core_algebra_and_selected_source_roles_checked;no_shape_or_rigidity_certification",
        "input_sha256": locked, "input_hashes_unchanged_after_checks": True,
        "scope_exclusion": "The parent's 131Ba transfer/addition readiness conclusion is not independently assessed here; its input hash is checked only.",
        "checks": METRICS,
        "counts": {"arbitrary_positive_A_cases": len(random_constants),
                   "integer_D2_representations": 9, "angle_controls": len(controls)},
        "definitions": {
            "A_k": "hbar^2/(2 J_k), in one common energy unit",
            "B21": "B(E2;2_1->0_1)", "B20": "B(E2;2_2->0_1)", "B22": "B(E2;2_2->2_1)",
            "s": "sin^2(3 gamma)", "d": "9-8s",
            "B21_unit": "(1+(3-2s)/sqrt(d))/10",
            "B20_unit": "(1-(3-2s)/sqrt(d))/10",
            "B22_unit": "(2/7)*s/d",
            "B20_over_B22": "(7/20)*(d-(3-2s)*sqrt(d))/s",
            "stable_B20_over_B22": "(7/5)*sqrt(d)*(1-s)/(sqrt(d)+3-2s)",
            "B22_over_B21": "(20/7)*s/(d+(3-2s)*sqrt(d))",
        },
        "gamma26": g26, "limits_gamma0": axial, "limits_gamma30": maximum,
        "Greiner_printed_matrix_inconsistency": source_inconsistency,
        "core_data": nuclei, "Konigshofen_data_roles": data_roles,
        "source_locators": {
            "Greiner": "raw/books/Nuclear Models (Walter Greiner, Joachim A. Maruhn) (Z-Library).pdf; printed145-147/PDF164-166",
            "Greiner_E2_ratio_attribution": "The requested E2 branch formulas are not stated on these three pages; they are independently derived here.",
            "local_formula_crops": "tmp/ba129-controlled-pairing/core-review/",
        },
        "interpretation_limits": [
            "The trace identity applies to a single constant-inertia D2 rotor independently of irrotationality.",
            "Its failure, conditional on level assignments, does not uniquely identify gamma softness.",
            "The two-energy gamma is an inferred model coordinate with a complementary branch, not a directly measured shape.",
            "One relative E2 agreement does not validate gamma rigidity; other Hamiltonians/operators can reproduce it.",
            "No covariance, confidence level, novelty claim, re-fit, or promotion of 3(+) to3+ is made.",
        ],
    }
    write("core-review-results.json", json.dumps(summary, indent=2, ensure_ascii=False, allow_nan=False) + "\n")
    print(json.dumps({"counts": summary["counts"], "checks": METRICS, "gamma26": g26,
                      "Greiner_counterexample": source_inconsistency,
                      "core_data": nuclei, "Konigshofen_ratio": computed}, indent=2))


if __name__ == "__main__":
    main()
