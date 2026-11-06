"""Exact finite-matrix checks for the archived Klein arXiv v1 appendix.

This is an audit artifact, not a KK iteration or a nuclear calculation.
No model implementation is imported, and no files are written. JSON goes to
stdout. A passed check means the stated identity or counterexample was
reproduced; it does NOT mean that every equation in the source is valid.
"""

from fractions import Fraction as F
import json


def matrix(rows):
    return [[F(value) for value in row] for row in rows]


def diagonal(*values):
    return matrix([
        [values[i] if i == j else 0 for j in range(len(values))]
        for i in range(len(values))
    ])


def zero(n):
    return diagonal(*([0] * n))


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(c, a):
    return [[F(c) * x for x in row] for row in a]


def sub(a, b):
    return add(a, scale(-1, b))


def transpose(a):
    return [list(row) for row in zip(*a)]


def multiply(a, b):
    return [
        [sum(x * y for x, y in zip(ar, bc)) for bc in zip(*b)]
        for ar in a
    ]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def anticommutator(a, b):
    return add(multiply(a, b), multiply(b, a))


def commutator(a, b):
    return sub(multiply(a, b), multiply(b, a))


def display(value):
    if isinstance(value, list):
        return [display(item) for item in value]
    if isinstance(value, F):
        return str(value)
    return value


def main():
    checks = []

    def check(name, equation, actual, expected, interpretation):
        if actual != expected:
            raise AssertionError(
                f"{name}: actual={display(actual)} expected={display(expected)}"
            )
        checks.append({
            "id": name,
            "source_equation": equation,
            "passed": True,
            "actual_exact": display(actual),
            "expected_exact": display(expected),
            "interpretation": interpretation,
        })

    omega = F(2)
    eta = F(1, 10)
    p = diagonal(1, 0)
    q = diagonal(0, 1)
    r = scale(omega, p)
    h = diagonal(1, 2)
    theta = diagonal(F(1, 2), -1)

    def idempotence_residual(rho):
        return sub(multiply(rho, rho), scale(omega, rho))

    def tangent_residual(delta):
        return sub(anticommutator(r, delta), scale(omega, delta))

    def a23_residual(ham):
        return sub(ham, scale(1 / omega, anticommutator(r, ham)))

    check("scaled_idempotence", "A8 / A24",
          idempotence_residual(r), zero(2),
          "R=diag(2,0) satisfies the source's scaled projector constraint.")
    check("commuting_stationary_example", "A15",
          commutator(r, h), zero(2),
          "The nonzero H=diag(1,2) commutes with R.")
    check("stationary_example_A18", "A18",
          add(sub(h, anticommutator(theta, r)), scale(omega, theta)),
          zero(2),
          "Theta=diag(1/2,-1) satisfies the variational equation exactly.")
    check("stationary_example_A21_left", "A21",
          sub(multiply(r, h), multiply(multiply(r, theta), r)), zero(2),
          "Left multiplication of A18 is valid.")
    check("stationary_example_A21_right", "A21",
          sub(multiply(h, r), multiply(multiply(r, theta), r)), zero(2),
          "Right multiplication of A18 is valid.")
    check("A22_counterexample", "A21 -> A22",
          sub(h, scale(omega, theta)), diagonal(0, 4),
          "A18 and A21 hold, but H=Omega*Theta does not follow.")
    check("A23_false_negative", "A23",
          a23_residual(h), diagonal(-1, 2),
          "A23 rejects this valid nonzero commuting stationary example.")

    # A22 substituted literally into A18 produces 2H-{R,H}/Omega.
    literal_substitution = add(
        sub(h, anticommutator(scale(1 / omega, h), r)), h
    )
    check("A22_substitution_factor", "A18 + A22 -> A23",
          sub(literal_substitution, a23_residual(h)), h,
          "The actual substituted residual differs from printed A23 by H.")

    y = a23_residual(h)
    delta = scale(-eta, y)
    check("A26_linear_tangent_failure", "A25-A27",
          tangent_residual(delta), diagonal(F(1, 5), F(2, 5)),
          "The printed update violates the first-order constraint.")
    check("A26_sandwich_failure", "A25-A26 / A28",
          multiply(multiply(r, delta), r), diagonal(F(2, 5), 0),
          "The update does not even satisfy the necessary A28 condition.")
    check("A26_finite_step_idempotence_failure", "A24-A27",
          idempotence_residual(add(r, delta)),
          diagonal(F(21, 100), F(11, 25)),
          "The constraint defect contains a nonzero term linear in eta.")

    hx = matrix([[0, 1], [1, 0]])
    check("A23_false_positive", "A23 / A25",
          a23_residual(hx), zero(2),
          "A23 is zero for a nonstationary off-diagonal Hamiltonian.")
    check("A23_false_positive_noncommutation", "A15 versus A23",
          commutator(r, hx), matrix([[0, 2], [-2, 0]]),
          "The zero A23 residual does not imply commutation or stationarity.")
    check("A28_is_necessary_only_sandwich", "A28",
          multiply(multiply(r, q), r), zero(2),
          "deltaR=Q satisfies the sandwich condition.")
    check("A28_is_necessary_only_tangent", "A27",
          tangent_residual(q), diagonal(0, -2),
          "deltaR=Q nevertheless fails the full tangent condition.")

    h_uphill = diagonal(2, 1)
    delta_bad = scale(-eta, a23_residual(h_uphill))
    check("printed_step_can_increase_linear_functional", "A17 / A25-A26",
          trace(multiply(h_uphill, delta_bad)), F(3, 10),
          "For G=Tr(HR), the printed direction can increase G.")

    hg = matrix([[1, 3], [3, 2]])
    tangent_h = add(multiply(multiply(p, hg), q),
                    multiply(multiply(q, hg), p))
    delta_t = scale(-eta, tangent_h)
    check("independent_tangent_projection", "A27; auditor derivation",
          tangent_residual(delta_t), zero(2),
          "The off-diagonal projector gradient is tangent; no solver is implemented.")
    check("independent_tangent_descent", "auditor derivation",
          trace(multiply(hg, delta_t)), -F(9, 5),
          "For the linear test functional its directional derivative is nonpositive.")

    # One orbital block of a possibly multiorbital CFP vector.
    # Omega_a=2 and Lambda_a=4 give a measured block norm of 8.
    block = matrix([[2], [2]])
    check("A12_norm_definition", "A12",
          multiply(transpose(block), block), matrix([[8]]),
          "The observed block norm is Lambda_a*Omega_a=8.")
    printed_rescale = scale(2, block)  # sqrt(Lambda_a)
    reciprocal_rescale = scale(F(1, 2), block)
    check("A13_wrong_normalization_map", "A12-A13",
          multiply(transpose(printed_rescale), printed_rescale), matrix([[32]]),
          "The printed scale gives Lambda_a^2*Omega_a=32, not Omega_a=2.")
    check("reciprocal_scale_is_only_local_normalization", "auditor derivation",
          multiply(transpose(reciprocal_rescale), reciprocal_rescale), matrix([[2]]),
          "The reciprocal repairs this one nonzero block norm only.")

    psi = matrix([[1, 1], [1, -1]])
    reweighted = multiply(diagonal(2, 1), psi)
    check("nonunitary_rescale_changes_Gram_matrix", "A13 algorithm boundary",
          multiply(transpose(reweighted), reweighted), matrix([[5, 3], [3, 5]]),
          "Orbital-dependent scaling can destroy orthogonality; not a complete repair.")

    # Pure two-mode fermionic algebra; no nuclear parameters or nuclear solver.
    # Odd states |1>, |2>; heavy neighbor a1^dag a2^dag|0>; light neighbor |0>.
    # bar interchanges mode labels 1 and 2, as in the source's U definition.
    cfp = matrix([[0, 1], [-1, 0], [0, 1], [1, 0]])
    r_cfp = multiply(cfp, transpose(cfp))
    check("CFP_completeness_Gram", "2.9-2.10 / 2.25-2.26",
          multiply(transpose(cfp), cfp), diagonal(2, 2),
          "The physical CFP columns have norm Omega and are orthogonal.")
    check("CFP_density_scaled_idempotence", "A7-A8",
          idempotence_residual(r_cfp), zero(4),
          "Completeness and the Gram identity imply A8.")
    check("CFP_core_number_sums", "2.24 / A19-A20",
          [r_cfp[0][0] + r_cfp[1][1], r_cfp[2][2] + r_cfp[3][3]],
          [F(2), F(2)],
          "Heavy particle count=2 and light vacancy count=2.")
    for i in range(2):
        check(f"CFP_odd_sector_strengths_{i}", "2.9-2.10; completeness derivation",
              [sum(cfp[k][i] ** 2 for k in range(2)),
               sum(cfp[k][i] ** 2 for k in range(2, 4))],
              [F(1), F(1)],
              "For N_odd=1, V strength=Omega-N_odd and U strength=N_odd.")

    arbitrary_r = diagonal(2, 2, 0, 0)
    check("arbitrary_projector_idempotent", "A8 alone is insufficient",
          idempotence_residual(arbitrary_r), zero(4),
          "An arbitrary rank-two projector satisfies the algebraic norm.")
    check("arbitrary_projector_commutes", "A15 alone is insufficient",
          commutator(arbitrary_r, diagonal(1, 1, 1, 1)), zero(4),
          "It also commutes with a frozen Hermitian Hamiltonian.")
    check("arbitrary_projector_wrong_core_numbers", "A19-A20",
          [arbitrary_r[0][0] + arbitrary_r[1][1] - 2,
           arbitrary_r[2][2] + arbitrary_r[3][3] - 2],
          [F(2), F(-2)],
          "The same projector fails both required core-number sums.")

    print(json.dumps({
        "schema": "klein-v1-exact-algebra-audit/1",
        "source_scope": "arXiv:nucl-th/0004051v1, 23 April 2000 only",
        "published_VoR_checked": False,
        "arithmetic": "Python standard-library fractions.Fraction; exact rational",
        "nuclear_implementation_imported_or_run": False,
        "counterexample_parameters": {
            "Omega": str(omega), "eta": str(eta),
            "R": display(r), "H": display(h), "Theta": display(theta),
        },
        "check_count": len(checks),
        "passed": len(checks),
        "failed": 0,
        "pass_meaning": "Expected identities and counterexamples reproduced, not blanket source validation.",
        "checks": checks,
    }, indent=2))


if __name__ == "__main__":
    main()
