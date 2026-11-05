"""Independent checks of lab-tensor phases, normalization and projections.

No nuclear levels or source-model B values are reference data. Reference
CGs are built by diagonalizing total J^2 at M=J, fixing the coefficient
with m1=j1 positive, then lowering. This does not use the implementation's
factorial/Racah formula. Analytical tests use a spherical free rotor:

* R=0, I=j: <j||j||j>=sqrt(j(j+1)(2j+1)), unit B=j(j+1).
* Particle j leaves spectator R (and core K) unchanged.
* Core R=0 -> R=2: for each symmetrized core K=0,2,
  B(If,K)=(2If+1)/(5(2j+1))*{cos^2 gamma,sin^2 gamma}.
  Summing over the whole If multiplet and both K branches gives one.

These are mathematical tests of the declared D* / CG convention. They do
not validate physical effective charges, g factors, photon branching,
delta signs, the rotor approximation, or a structural-mode interpretation.
Tests perform no file I/O and do not import any legacy analyzer.
"""

from dataclasses import replace
from functools import lru_cache
import math
from pathlib import Path
import sys
import unittest

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))

from paired_single_j_rotor import PairedRotorParameters, solve
from paired_single_j_em import clebsch_gordan, collective_quadrupole, particle_j, unit_em


def parameters(**changes):
    values = dict(two_j=11, C_MeV=3.1, gamma_deg=23.0,
                  inertias_hbar2_per_MeV=(17.0, 8.0, 3.0),
                  lambda_F_MeV=0.41, Delta_MeV=0.72)
    values.update(changes)
    return PairedRotorParameters(**values)


def free_parameters(two_j=11, gamma=23.0):
    return parameters(two_j=two_j, C_MeV=0, gamma_deg=gamma,
                      inertias_hbar2_per_MeV=(10.0,) * 3, lambda_F_MeV=0, Delta_MeV=0.7)


def reference_raising(two_j):
    """Independent ordinary-spin ladder matrix in ascending projection order."""
    j = two_j / 2
    m = np.arange(-j, j + 1)
    return np.diag(np.sqrt((j - m[:-1]) * (j + m[:-1] + 1)), -1)


@lru_cache(maxsize=32)
def coupled_reference(two_j1, two_j2):
    """Return {(two_J,two_M): product-state amplitudes} using J^2 and J_-."""
    n1, n2 = two_j1 + 1, two_j2 + 1
    m1 = np.arange(-two_j1, two_j1 + 1, 2) / 2
    m2 = np.arange(-two_j2, two_j2 + 1, 2) / 2
    mz = (m1[:, None] + m2[None, :]).ravel()
    raising = (np.kron(reference_raising(two_j1), np.eye(n2))
               + np.kron(np.eye(n1), reference_raising(two_j2)))
    lowering = raising.T
    total_squared = np.diag(mz * mz) + (raising @ lowering + lowering @ raising) / 2
    table = {}
    for two_J in range(abs(two_j1 - two_j2), two_j1 + two_j2 + 1, 2):
        J = two_J / 2
        subset = np.flatnonzero(mz == J)
        energy, vector = np.linalg.eigh(total_squared[np.ix_(subset, subset)])
        match = int(np.argmin(abs(energy - J * (J + 1))))
        if abs(energy[match] - J * (J + 1)) > 1e-10:
            raise AssertionError("independent J^2 reference did not resolve its target J")
        state = np.zeros(n1 * n2)
        state[subset] = vector[:, match]
        m2_at_m1max = two_J - two_j1
        phase_index = (n1 - 1) * n2 + (m2_at_m1max + two_j2) // 2
        if abs(state[phase_index]) < 1e-12:
            raise AssertionError("highest-weight phase anchor unexpectedly vanished")
        state *= 1 if state[phase_index] > 0 else -1
        table[(two_J, two_J)] = state.copy()
        for two_M in range(two_J, -two_J, -2):
            M = two_M / 2
            state = lowering @ state / math.sqrt((J + M) * (J - M + 1))
            table[(two_J, two_M - 2)] = state.copy()
    return table


def reference_cg(two_j1, two_m1, two_j2, two_m2, two_J, two_M):
    state = coupled_reference(two_j1, two_j2).get((two_J, two_M))
    if state is None or abs(two_m1) > two_j1 or abs(two_m2) > two_j2:
        return 0.0
    row = ((two_m1 + two_j1) // 2) * (two_j2 + 1) + (two_m2 + two_j2) // 2
    return float(state[row])


def weak_product_state(two_I, two_j, rotor_R, core_K):
    """Independent (j x R)I state with D2-symmetrized core K>=0 even.

    The coefficients follow the product theorem for the declared normalized
    D* functions. Independent reference_cg supplies the coupling amplitudes.
    No post-hoc normalization or fitted phase is applied.
    """
    raw = np.zeros((two_I + 1, two_j + 1), complex)
    factor = math.sqrt((2 * rotor_R + 1) / (two_I + 1))
    core_terms = [(0, 1.0)] if core_K == 0 else [
        (core_K, 1 / math.sqrt(2)), (-core_K, (-1) ** rotor_R / math.sqrt(2))]
    for ik, k in enumerate(range(-two_I, two_I + 1, 2)):
        for io, omega in enumerate(range(-two_j, two_j + 1, 2)):
            for kr, weight in core_terms:
                if k == omega + 2 * kr:
                    raw[ik, io] += factor * weight * reference_cg(
                        two_j, omega, 2 * rotor_R, 2 * kr, two_I, k)
    return raw.ravel()


def weak_eigen_coefficients(solution, rotor_R, core_K):
    raw = weak_product_state(solution.two_I, solution.parameters.two_j, rotor_R, core_K)
    np.testing.assert_allclose(np.vdot(raw, raw), 1, atol=2e-13)
    p = solution.product_embedding
    np.testing.assert_allclose(p @ (p.conj().T @ raw), raw, atol=2e-13)
    return solution.eigenvectors.conj().T @ p.conj().T @ raw


def free_R_labels(solution):
    inertia = solution.parameters.inertias_hbar2_per_MeV[0]
    shift = math.hypot(solution.parameters.lambda_F_MeV, solution.parameters.Delta_MeV)
    R = (-1 + np.sqrt(1 + 8 * inertia * (solution.eigenvalues_MeV - shift))) / 2
    np.testing.assert_allclose(R, np.rint(R), atol=2e-11)
    return np.rint(R).astype(int)


class ClebschGordanTests(unittest.TestCase):
    def test_known_phases_and_vector_coefficients(self):
        self.assertAlmostEqual(clebsch_gordan(1, 1, 1, -1, 0, 0), 1 / math.sqrt(2), places=15)
        self.assertAlmostEqual(clebsch_gordan(1, -1, 1, 1, 0, 0), -1 / math.sqrt(2), places=15)
        self.assertAlmostEqual(clebsch_gordan(2, 0, 2, 0, 0, 0), -1 / math.sqrt(3), places=15)
        self.assertEqual(clebsch_gordan(11, 11, 4, 4, 15, 15), 1)
        for two_j in (1, 3, 11, 27):
            j = two_j / 2
            for two_m in range(-two_j, two_j + 1, 2):
                self.assertAlmostEqual(clebsch_gordan(two_j, two_m, 2, 0, two_j, two_m),
                                       (two_m / 2) / math.sqrt(j * (j + 1)), places=14)

    def test_CG_against_independent_highest_weight_and_lowering(self):
        for j1, j2 in ((1, 1), (3, 2), (5, 4), (11, 4), (27, 2)):
            with self.subTest(two_j1=j1, two_j2=j2):
                reference = coupled_reference(j1, j2)
                for (J, M), state in reference.items():
                    for m1 in range(-j1, j1 + 1, 2):
                        m2 = M - m1
                        if abs(m2) <= j2:
                            index = ((m1 + j1) // 2) * (j2 + 1) + (m2 + j2) // 2
                            self.assertAlmostEqual(clebsch_gordan(j1, m1, j2, m2, J, M),
                                                   state[index], delta=3e-13)

    def test_CG_unitarity_and_scalar_coupling(self):
        j1, j2 = 5, 4
        columns = []
        for J in range(abs(j1 - j2), j1 + j2 + 1, 2):
            for M in range(-J, J + 1, 2):
                columns.append([clebsch_gordan(j1, m1, j2, m2, J, M)
                                for m1 in range(-j1, j1 + 1, 2)
                                for m2 in range(-j2, j2 + 1, 2)])
        matrix = np.array(columns).T
        np.testing.assert_allclose(matrix.T @ matrix, np.eye(len(matrix)), atol=1e-14)
        for m in range(-11, 12, 2):
            self.assertEqual(clebsch_gordan(11, m, 0, 0, 11, m), 1)

    def test_CG_selection_zeros_and_invalid_inputs(self):
        for args in ((1, 1, 1, 1, 0, 0), (1, 1, 2, 0, 9, 1),
                     (1, 0, 2, 0, 1, 0), (1, 3, 2, 0, 1, 3)):
            self.assertEqual(clebsch_gordan(*args), 0)
        for args in ((-1, 1, 1, -1, 0, 0), (1.0, 1, 1, -1, 0, 0),
                     (True, 1, 1, -1, 0, 0)):
            with self.assertRaises(ValueError):
                clebsch_gordan(*args)


class FreeRotorAnalyticTests(unittest.TestCase):
    def test_R0_particle_j_diagonal_RME_and_unit_B(self):
        for two_j in (1, 3, 11):
            with self.subTest(two_j=two_j):
                solution = solve(two_j, free_parameters(two_j))
                j = two_j / 2
                a = weak_eigen_coefficients(solution, 0, 0)
                result = particle_j(solution, solution)
                rme = np.vdot(a, result.rme @ a)
                self.assertAlmostEqual(rme.real, math.sqrt(j * (j + 1) * (2 * j + 1)), places=12)
                self.assertAlmostEqual(rme.imag, 0, places=13)
                self.assertAlmostEqual(abs(rme) ** 2 / (2 * j + 1), j * (j + 1), places=12)
                self.assertAlmostEqual(result.unit_B[0, 0], j * (j + 1), places=12)

    def test_particle_j_cannot_change_spectator_R(self):
        p = free_parameters()
        for two_Ii, two_If in ((9, 11), (11, 11), (11, 13)):
            with self.subTest(two_Ii=two_Ii, two_If=two_If):
                initial, final = solve(two_Ii, p), solve(two_If, p)
                ri, rf = free_R_labels(initial), free_R_labels(final)
                result = particle_j(initial, final)
                different_R = rf[:, None] != ri[None, :]
                np.testing.assert_allclose(result.rme[different_R], 0, atol=3e-12)
                self.assertGreater(np.max(abs(result.rme[~different_R])), 0.1)

    def test_particle_j_preserves_core_K_in_a_free_degenerate_R2_space(self):
        solution = solve(11, free_parameters())
        a0, a2 = (weak_eigen_coefficients(solution, 2, k) for k in (0, 2))
        result = particle_j(solution, solution)
        self.assertAlmostEqual(abs(np.vdot(a2, result.rme @ a0)), 0, places=12)
        self.assertGreater(abs(np.vdot(a0, result.rme @ a0)), 1)

    def test_core_R0_to_R2_K_resolved_multiplet_and_sum(self):
        for two_j, gamma in ((1, 0.0), (1, 23.0), (11, 23.0), (11, 90.0)):
            with self.subTest(two_j=two_j, gamma=gamma):
                p = free_parameters(two_j, gamma)
                initial = solve(two_j, p)
                ai = weak_eigen_coefficients(initial, 0, 0)
                weights = (math.cos(math.radians(gamma)), math.sin(math.radians(gamma)))
                by_K = np.zeros(2)
                for two_If in range(abs(two_j - 4), two_j + 5, 2):
                    final = solve(two_If, p)
                    result = collective_quadrupole(initial, final)
                    for index, K in enumerate((0, 2)):
                        af = weak_eigen_coefficients(final, 2, K)
                        rme = np.vdot(af, result.rme @ ai)
                        expected_rme = weights[index] * math.sqrt((two_If + 1) / 5)
                        self.assertAlmostEqual(rme.real, expected_rme, places=12)
                        self.assertAlmostEqual(rme.imag, 0, places=13)
                        strength = abs(rme) ** 2 / (two_j + 1)
                        expected_B = weights[index] ** 2 * (two_If + 1) / (5 * (two_j + 1))
                        self.assertAlmostEqual(strength, expected_B, places=12)
                        by_K[index] += strength
                    # No strength is allowed into other spectator-core R.
                    other_R = free_R_labels(final) != 2
                    np.testing.assert_allclose((result.rme @ ai)[other_R], 0, atol=3e-12)
                np.testing.assert_allclose(by_K, np.array(weights) ** 2, atol=3e-12)
                self.assertAlmostEqual(sum(by_K), 1, places=12)

    def test_particle_j_free_closure_for_all_initial_states(self):
        p = free_parameters()
        initial = solve(11, p)
        strength = np.zeros(len(initial.eigenvalues_MeV))
        for two_If in (9, 11, 13):
            strength += particle_j(initial, solve(two_If, p)).unit_B.sum(axis=0)
        j = p.two_j / 2
        np.testing.assert_allclose(strength, j * (j + 1), atol=6e-12)


class ProjectionAndTensorTests(unittest.TestCase):
    def test_core_BCS_cancels_but_particle_j_requires_projection(self):
        p = parameters()
        result = unit_em(solve(11, p), solve(13, p))
        core, angular = result.collective_quadrupole, result.particle_j
        np.testing.assert_allclose(core.d2_rme, core.bare_d2_rme, atol=2e-13)
        self.assertGreater(np.max(abs(angular.d2_rme - angular.bare_d2_rme)), 0.01)

    def test_explicit_BCS_then_D2_projection_matches_Nambu_maps(self):
        p = parameters(two_j=3)
        initial, final = solve(3, p), solve(5, p)
        result = unit_em(initial, final)
        si, sf = initial.single_particle.eigenvectors, final.single_particle.eigenvectors
        ui, vi = (si * initial.u) @ si.conj().T, (si * initial.v) @ si.conj().T
        uf, vf = (sf * final.u) @ sf.conj().T, (sf * final.v) @ sf.conj().T
        for tensor in (result.collective_quadrupole, result.particle_j):
            paired = (
                np.kron(np.eye(final.two_I + 1), uf) @ tensor.product_rme
                @ np.kron(np.eye(initial.two_I + 1), ui)
                + np.kron(np.eye(final.two_I + 1), vf) @ tensor.product_rme
                @ np.kron(np.eye(initial.two_I + 1), vi)
            )
            expected = final.product_embedding.conj().T @ paired @ initial.product_embedding
            np.testing.assert_allclose(tensor.d2_rme, expected, atol=2e-14)
            expected_eigen = final.eigenvectors.conj().T @ expected @ initial.eigenvectors
            np.testing.assert_allclose(tensor.rme, expected_eigen, atol=3e-14)

    def test_Hermitian_reduced_reciprocity(self):
        p = parameters()
        for two_Ii, two_If in ((9, 11), (11, 11), (11, 15), (25, 27)):
            with self.subTest(two_Ii=two_Ii, two_If=two_If):
                initial, final = solve(two_Ii, p), solve(two_If, p)
                forward, reverse = unit_em(initial, final), unit_em(final, initial)
                phase = (-1) ** ((two_If - two_Ii) // 2)
                for name in ("collective_quadrupole", "particle_j"):
                    f, r = getattr(forward, name), getattr(reverse, name)
                    np.testing.assert_allclose(f.rme, phase * r.rme.conj().T, atol=3e-13)
                    np.testing.assert_allclose((two_Ii + 1) * f.unit_B,
                                               (two_If + 1) * r.unit_B.T, atol=3e-12)

    def test_angular_momentum_triangle_selection(self):
        p = parameters()
        initial = solve(9, p)
        both_forbidden = unit_em(initial, solve(15, p))
        np.testing.assert_array_equal(both_forbidden.collective_quadrupole.rme, 0)
        np.testing.assert_array_equal(both_forbidden.particle_j.rme, 0)
        delta2 = unit_em(initial, solve(13, p))
        np.testing.assert_array_equal(delta2.particle_j.rme, 0)
        self.assertGreater(np.max(abs(delta2.collective_quadrupole.rme)), 0.01)
        small = solve(1, free_parameters(1))
        np.testing.assert_array_equal(collective_quadrupole(small, small).rme, 0)

    def test_eigenstate_rephasing_preserves_unit_B_and_expected_RME_phase(self):
        p = parameters()
        initial, final = solve(11, p), solve(13, p)
        before = unit_em(initial, final)
        phase_i = np.exp(1j * (0.17 + 0.29 * np.arange(len(initial.eigenvalues_MeV))))
        phase_f = np.exp(1j * (-0.43 + 0.37 * np.arange(len(final.eigenvalues_MeV))))
        rephased_i = replace(initial, eigenvectors=initial.eigenvectors * phase_i)
        rephased_f = replace(final, eigenvectors=final.eigenvectors * phase_f)
        after = unit_em(rephased_i, rephased_f)
        for name in ("collective_quadrupole", "particle_j"):
            old, new = getattr(before, name), getattr(after, name)
            expected = phase_f.conj()[:, None] * old.rme * phase_i[None, :]
            np.testing.assert_allclose(new.rme, expected, atol=2e-13)
            np.testing.assert_allclose(new.unit_B, old.unit_B, atol=2e-13)
            self.assertGreater(np.max(abs(new.rme.imag)), 0.01)

    def test_collective_closure_with_nonzero_field_and_pairing(self):
        p = parameters()
        initial = solve(11, p)
        strength = np.zeros(len(initial.eigenvalues_MeV))
        for two_If in (7, 9, 11, 13, 15):
            strength += collective_quadrupole(initial, solve(two_If, p)).unit_B.sum(axis=0)
        np.testing.assert_allclose(strength, 1, atol=3e-12)

    def test_common_spin_pairs_output_units_shapes_and_no_physical_scale(self):
        p = parameters()
        for two_Ii, two_If in ((11, 9), (13, 9), (19, 17), (27, 25), (27, 23)):
            with self.subTest(two_Ii=two_Ii, two_If=two_If):
                initial, final = solve(two_Ii, p), solve(two_If, p)
                result = unit_em(initial, final)
                for tensor, rank, name in ((result.collective_quadrupole, 2, "collective_quadrupole"),
                                          (result.particle_j, 1, "particle_j")):
                    self.assertEqual(tensor.operator, name)
                    self.assertEqual(tensor.rank, rank)
                    self.assertEqual(tensor.rme.shape, (len(final.eigenvalues_MeV), len(initial.eigenvalues_MeV)))
                    np.testing.assert_allclose(tensor.unit_B, abs(tensor.rme) ** 2 / (two_Ii + 1), atol=0)
                    self.assertTrue(np.all(tensor.unit_B >= 0))
                    self.assertFalse(tensor.rme.flags.writeable)
                    self.assertFalse(tensor.unit_B.flags.writeable)


class InputBoundaryTests(unittest.TestCase):
    def test_all_parameter_values_must_match_not_just_shape(self):
        p = parameters()
        initial = solve(9, p)
        changes = [
            dict(gamma_deg=p.gamma_deg + 1), dict(gamma_deg=p.gamma_deg + 360),
            dict(C_MeV=p.C_MeV + 0.1), dict(lambda_F_MeV=p.lambda_F_MeV + 0.1),
            dict(Delta_MeV=p.Delta_MeV + 0.1), dict(inertias_hbar2_per_MeV=(17, 8, 4)),
            dict(two_j=9),
        ]
        for change in changes:
            with self.subTest(change=change):
                final = solve(11, replace(p, **change))
                for operator in (unit_em, collective_quadrupole, particle_j):
                    with self.assertRaisesRegex(ValueError, "identical rotor parameter"):
                        operator(initial, final)

    def test_equal_parameter_values_do_not_require_object_identity(self):
        initial = solve(9, parameters())
        final = solve(11, parameters())
        result = unit_em(initial, final)
        self.assertGreater(np.max(result.collective_quadrupole.unit_B), 0)

    def test_invalid_solution_types_and_coordinate_matrices(self):
        good = solve(3, free_parameters(3))
        for invalid in (None, {}, "solution"):
            with self.assertRaises(TypeError):
                unit_em(invalid, good)
            with self.assertRaises(TypeError):
                unit_em(good, invalid)
        invalids = [
            replace(good, two_I=2),
            replace(good, eigenvectors=np.zeros_like(good.eigenvectors)),
            replace(good, product_embedding=good.product_embedding[:-1]),
            replace(good, positive_energy_embedding=np.full_like(good.positive_energy_embedding, np.nan)),
        ]
        for invalid in invalids:
            with self.assertRaises(ValueError):
                unit_em(invalid, good)


if __name__ == "__main__":
    unittest.main()
