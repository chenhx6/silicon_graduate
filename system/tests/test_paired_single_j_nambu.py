"""Mathematical tests of the declared full Nambu object, not physical branches.

The original-basis reference squares direct (I-j) matrices independently
of the kernel's factorized H_R. A spherical C=0 reference uses D2 character
multiplicities and both analytic energies R(R+1)/(2J) +/- E_qp. Covariance
uses a proper spin rotation plus a particle/hole swap, not a fitted spectrum.

There is no nucleus, source-figure energy, refit, EM observable, sign-based
state selection or branch-continuation validation in these tests.
"""

from dataclasses import replace
import math
from pathlib import Path
import sys
import unittest

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))

from paired_single_j_rotor import PairedRotorParameters
from paired_single_j_nambu import (
    build_nambu,
    hamiltonian_at,
    original_d2_hamiltonian_at,
    solve_nambu,
)


def parameters(**updates):
    values = dict(two_j=3, C_MeV=4.1, gamma_deg=23.0,
                  inertias_hbar2_per_MeV=(11.0, 7.0, 4.0),
                  lambda_F_MeV=0.37, Delta_MeV=0.83)
    values.update(updates)
    return PairedRotorParameters(**values)


def reference_spin(two_j):
    """Ordinary spin matrices built in descending order, then reordered."""
    j = two_j / 2
    m = np.arange(j, -j - 1, -1)
    raising = np.diag(np.sqrt((j + m[:-1]) * (j - m[:-1] + 1)), 1)
    operators = ((raising + raising.T) / 2,
                 (raising - raising.T) / (2j), np.diag(m))
    return [op[::-1, ::-1].copy() for op in operators]


def reference_original_H(two_I, p):
    body = reference_spin(two_I)
    body[1] *= -1
    particle = reference_spin(p.two_j)
    eye_I, eye_j = np.eye(two_I + 1), np.eye(p.two_j + 1)
    dim = (two_I + 1) * (p.two_j + 1)
    hrot = np.zeros((dim, dim), complex)
    for i, j, inertia in zip(body, particle, p.inertias_hbar2_per_MeV):
        r = np.kron(i, eye_j) - np.kron(eye_I, j)
        hrot += r @ r / (2 * inertia)
    j = p.two_j / 2
    x, y, z = particle
    gamma = math.radians(p.gamma_deg)
    q = (math.cos(gamma) * (3 * z @ z - j * (j + 1) * eye_j)
         + math.sqrt(3) * math.sin(gamma) * (x @ x - y @ y)) / (4 * j * (j + 1))
    xi = np.kron(eye_I, p.C_MeV * q - p.lambda_F_MeV * eye_j)
    gap = p.Delta_MeV * np.eye(dim)
    return np.block([[hrot + xi, gap], [gap, hrot - xi]]), hrot


def spin_rotation(two_j, axis, angle):
    generator = sum(coefficient * op for coefficient, op in zip(axis, reference_spin(two_j)))
    values, vectors = np.linalg.eigh(generator)
    return (vectors * np.exp(-1j * angle * values)) @ vectors.conj().T


class OriginalBasisAndBlockTests(unittest.TestCase):
    def test_direct_original_basis_Hamiltonian(self):
        p = parameters()
        system = build_nambu(7, p)
        original, hrot = reference_original_H(7, p)
        np.testing.assert_allclose(system.rotor_product_MeV, hrot, atol=2e-14, rtol=0)
        np.testing.assert_allclose(system.endpoint_product_MeV, original, atol=2e-14, rtol=0)
        y = system.original_d2_embedding
        np.testing.assert_allclose(system.endpoint_original_d2_MeV,
                                   y.conj().T @ original @ y, atol=2e-14, rtol=0)

    def test_full_isometry_and_unitary_D2_Bogoliubov_transform(self):
        for two_I, two_j in ((1, 1), (5, 3), (9, 11)):
            with self.subTest(two_I=two_I, two_j=two_j):
                system = build_nambu(two_I, parameters(two_j=two_j))
                x, y, w = system.embedding, system.original_d2_embedding, system.d2_transform
                eye = np.eye(2 * system.sector_dimension)
                np.testing.assert_allclose(x.conj().T @ x, eye, atol=2e-14, rtol=0)
                np.testing.assert_allclose(y.conj().T @ y, eye, atol=2e-14, rtol=0)
                np.testing.assert_allclose(w.conj().T @ w, eye, atol=2e-14, rtol=0)
                np.testing.assert_allclose(w @ w.conj().T, eye, atol=2e-14, rtol=0)
                np.testing.assert_allclose(y @ w, x, atol=2e-14, rtol=0)
                np.testing.assert_allclose(x @ x.conj().T, y @ y.conj().T, atol=2e-14, rtol=0)
                np.testing.assert_allclose(system.positive_embedding.conj().T @ system.negative_embedding,
                                           0, atol=2e-14, rtol=0)

    def test_upper_right_K_sign_and_direct_full_transform(self):
        system = build_nambu(7, parameters())
        xp, xm = system.positive_embedding, system.negative_embedding
        direct = xp.conj().T @ system.endpoint_product_MeV @ xm
        np.testing.assert_allclose(system.K_MeV, direct, atol=3e-14, rtol=0)
        np.testing.assert_allclose(system.K_MeV.conj().T, -system.K_MeV, atol=3e-14, rtol=0)
        self.assertGreater(np.linalg.norm(system.K_MeV), 0.01)
        direct_full = system.embedding.conj().T @ system.endpoint_product_MeV @ system.embedding
        np.testing.assert_allclose(hamiltonian_at(system, 1), direct_full, atol=4e-14, rtol=0)
        self.assertLess(system.direct_transform_error_MeV, 4e-14)

    def test_Hplus_matches_frozen_positive_solver(self):
        for two_I in (9, 13, 27):
            with self.subTest(two_I=two_I):
                system = build_nambu(two_I, parameters(two_j=11))
                reference = system.reference_plus
                np.testing.assert_allclose(system.Hplus_MeV, reference.hamiltonian_MeV,
                                           atol=2e-13, rtol=0)
                np.testing.assert_allclose(np.linalg.eigvalsh(system.Hplus_MeV),
                                           reference.eigenvalues_MeV, atol=3e-13, rtol=0)
                self.assertLess(system.positive_reference_error_MeV, 2e-13)

    def test_Hermiticity_and_D2_leakage(self):
        system = build_nambu(13, parameters(two_j=11))
        original, x = system.endpoint_product_MeV, system.embedding
        np.testing.assert_allclose(original, original.conj().T, atol=5e-14, rtol=0)
        np.testing.assert_allclose(original @ x, x @ hamiltonian_at(system, 1), atol=3e-13, rtol=0)
        self.assertLess(system.hermiticity_error_MeV, 5e-14)
        self.assertLess(system.D2_leakage_MeV, 3e-13)
        for t in (0, 0.25, 1):
            h = hamiltonian_at(system, t)
            np.testing.assert_allclose(h, h.conj().T, atol=5e-14, rtol=0)


class InterpolationAndResidualTests(unittest.TestCase):
    def test_t0_blocks_and_union_spectrum(self):
        system = build_nambu(7, parameters())
        d = system.sector_dimension
        h0 = hamiltonian_at(system, 0)
        np.testing.assert_array_equal(h0[:d, d:], 0)
        np.testing.assert_array_equal(h0[d:, :d], 0)
        np.testing.assert_array_equal(h0[:d, :d], system.Hplus_MeV)
        np.testing.assert_array_equal(h0[d:, d:], system.Hminus_MeV)
        expected = np.sort(np.concatenate((np.linalg.eigvalsh(system.Hplus_MeV),
                                           np.linalg.eigvalsh(system.Hminus_MeV))))
        np.testing.assert_allclose(solve_nambu(system, 0).eigenvalues_MeV, expected, atol=3e-14, rtol=0)

    def test_t_changes_only_offdiagonal_coupling(self):
        system = build_nambu(7, parameters())
        h0, h1 = hamiltonian_at(system, 0), hamiltonian_at(system, 1)
        d = system.sector_dimension
        for t in (0.17, 0.5, 0.93):
            with self.subTest(t=t):
                ht = hamiltonian_at(system, t)
                np.testing.assert_allclose(ht, h0 + t * (h1 - h0), atol=2e-15, rtol=0)
                np.testing.assert_array_equal(ht[:d, :d], system.Hplus_MeV)
                np.testing.assert_array_equal(ht[d:, d:], system.Hminus_MeV)
                np.testing.assert_allclose(ht[:d, d:], t * system.K_MeV, atol=0, rtol=0)

    def test_original_D2_interpolation_is_consistent(self):
        system = build_nambu(7, parameters())
        w = system.d2_transform
        np.testing.assert_allclose(original_d2_hamiltonian_at(system, 1),
                                   system.endpoint_original_d2_MeV, atol=5e-14, rtol=0)
        for t in (0, 0.37, 1):
            original = original_d2_hamiltonian_at(system, t)
            np.testing.assert_allclose(w.conj().T @ original @ w, hamiltonian_at(system, t),
                                       atol=5e-14, rtol=0)

    def test_eigenpair_norms_residuals_and_full_endpoint_residual(self):
        system = build_nambu(9, parameters(two_j=11))
        coupling = hamiltonian_at(system, 1) - hamiltonian_at(system, 0)
        for t in (0, 0.35, 1):
            with self.subTest(t=t):
                result = solve_nambu(system, t)
                v, energy = result.eigenvectors, result.eigenvalues_MeV
                np.testing.assert_allclose(v.conj().T @ v, np.eye(len(v)), atol=3e-14, rtol=0)
                np.testing.assert_allclose(result.eigenvectors_product.conj().T @ result.eigenvectors_product,
                                           np.eye(len(v)), atol=5e-14, rtol=0)
                np.testing.assert_allclose(result.hamiltonian_MeV @ v, v * energy, atol=2e-13, rtol=0)
                self.assertLess(np.max(result.interpolated_residual_norms_MeV), 3e-13)
                self.assertLess(np.max(result.original_d2_residual_norms_MeV), 3e-13)
                expected = np.linalg.norm((1 - t) * coupling @ v, axis=0)
                np.testing.assert_allclose(result.full_endpoint_residual_norms_MeV,
                                           expected, atol=3e-13, rtol=0)
                np.testing.assert_allclose(result.plus_sector_weights + result.minus_sector_weights,
                                           1, atol=3e-14, rtol=0)
                self.assertTrue(np.all(result.plus_sector_weights >= 0))
                self.assertTrue(np.all(result.minus_sector_weights >= 0))
                if t == 0:
                    self.assertGreater(np.max(result.full_endpoint_residual_norms_MeV), 0.01)
                if t == 1:
                    self.assertLess(np.max(result.full_endpoint_residual_norms_MeV), 3e-13)

    def test_chosen_Hplus_seed_residual_equals_K_adjoint_action(self):
        system = build_nambu(9, parameters(two_j=11))
        reference = system.reference_plus
        seed = np.concatenate((reference.eigenvectors[:, 0], np.zeros(system.sector_dimension)))
        residual = hamiltonian_at(system, 1) @ seed - reference.eigenvalues_MeV[0] * seed
        expected = np.concatenate((np.zeros(system.sector_dimension),
                                   system.K_MeV.conj().T @ reference.eigenvectors[:, 0]))
        np.testing.assert_allclose(residual, expected, atol=6e-14, rtol=0)


class ExactLimitAndCovarianceTests(unittest.TestCase):
    def test_C0_has_zero_K_and_t_independent_spectrum(self):
        for lam in (0.0, 0.31):
            with self.subTest(lambda_F=lam):
                system = build_nambu(9, parameters(two_j=11, C_MeV=0, lambda_F_MeV=lam))
                np.testing.assert_allclose(system.K_MeV, 0, atol=2e-14, rtol=0)
                base = solve_nambu(system, 0).eigenvalues_MeV
                for t in (0.4, 1):
                    np.testing.assert_allclose(solve_nambu(system, t).eigenvalues_MeV,
                                               base, atol=4e-14, rtol=0)

    def test_spherical_free_spectrum_and_D2_character_multiplicities(self):
        for two_I, two_j in ((1, 1), (5, 3), (9, 11), (27, 11)):
            with self.subTest(two_I=two_I, two_j=two_j):
                p = parameters(two_j=two_j, C_MeV=0, inertias_hbar2_per_MeV=(10,) * 3)
                system = build_nambu(two_I, p)
                qp = math.hypot(p.lambda_F_MeV, p.Delta_MeV)
                expected = []
                for r in range(abs(two_I - two_j) // 2, (two_I + two_j) // 2 + 1):
                    multiplicity = (2 * r + 1 + 3 * (-1) ** r) // 4
                    er = r * (r + 1) / 20
                    expected.extend([er + qp] * multiplicity)
                    expected.extend([er - qp] * multiplicity)
                result = solve_nambu(system, 1)
                self.assertEqual(len(result.eigenvalues_MeV), len(expected))
                np.testing.assert_allclose(result.eigenvalues_MeV, sorted(expected), atol=3e-13, rtol=0)

    def test_exact_particle_hole_shape_covariance_at_all_tested_t(self):
        axis = np.array([0, 1, 1]) / math.sqrt(2)
        for two_I, two_j in ((7, 3), (9, 11)):
            with self.subTest(two_I=two_I, two_j=two_j):
                p = parameters(two_j=two_j)
                j1, j2, j3 = p.inertias_hbar2_per_MeV
                other_p = replace(p, gamma_deg=60 - p.gamma_deg,
                                  lambda_F_MeV=-p.lambda_F_MeV,
                                  inertias_hbar2_per_MeV=(j1, j3, j2))
                a, b = build_nambu(two_I, p), build_nambu(two_I, other_p)
                rotation = np.kron(spin_rotation(two_I, axis, math.pi).conj(),
                                   spin_rotation(two_j, axis, math.pi))
                zero = np.zeros_like(rotation)
                full_transform = np.block([[zero, rotation], [rotation, zero]])
                np.testing.assert_allclose(
                    b.endpoint_product_MeV,
                    full_transform @ a.endpoint_product_MeV @ full_transform.conj().T,
                    atol=3e-13, rtol=0)
                p_d2 = a.reference_plus.product_embedding
                s = p_d2.conj().T @ rotation @ p_d2
                zero_s = np.zeros_like(s)
                # X+ transforms with S, X- with -S at fixed positive gap.
                transformed_coordinates = np.block([[s, zero_s], [zero_s, -s]])
                np.testing.assert_allclose(b.K_MeV, -s @ a.K_MeV @ s.conj().T, atol=6e-14, rtol=0)
                for t in (0, 0.41, 1):
                    np.testing.assert_allclose(
                        hamiltonian_at(b, t),
                        transformed_coordinates @ hamiltonian_at(a, t) @ transformed_coordinates.conj().T,
                        atol=3e-13, rtol=0)
                    np.testing.assert_allclose(solve_nambu(a, t).eigenvalues_MeV,
                                               solve_nambu(b, t).eigenvalues_MeV, atol=3e-13, rtol=0)

    def test_cyclic_shape_and_inertia_permutation(self):
        p = parameters(two_j=11)
        j1, j2, j3 = p.inertias_hbar2_per_MeV
        a = build_nambu(11, p)
        b = build_nambu(11, replace(p, gamma_deg=p.gamma_deg + 120,
                                   inertias_hbar2_per_MeV=(j3, j1, j2)))
        for t in (0, 0.5, 1):
            np.testing.assert_allclose(solve_nambu(a, t).eigenvalues_MeV,
                                       solve_nambu(b, t).eigenvalues_MeV, atol=3e-13, rtol=0)


class OutputAndBoundaryTests(unittest.TestCase):
    def test_all_states_returned_without_energy_sign_cut(self):
        system = build_nambu(11, parameters(two_j=11, C_MeV=0, inertias_hbar2_per_MeV=(10,) * 3))
        result = solve_nambu(system, 0)
        self.assertEqual(len(result.eigenvalues_MeV), 2 * system.sector_dimension)
        self.assertTrue(np.any(result.eigenvalues_MeV < 0))
        self.assertTrue(np.any(result.eigenvalues_MeV > 0))
        self.assertTrue(np.any(np.linalg.eigvalsh(system.Hminus_MeV) > 0))
        self.assertFalse(np.allclose(result.eigenvalues_MeV, -result.eigenvalues_MeV[::-1]))

    def test_exact_degeneracy_is_exposed_without_state_matching(self):
        p = parameters(C_MeV=0, lambda_F_MeV=0, Delta_MeV=0.3,
                       inertias_hbar2_per_MeV=(10,) * 3)
        result = solve_nambu(build_nambu(3, p), 0)
        self.assertLess(np.min(abs(result.adjacent_spacings_MeV)), 1e-13)
        # R=0,+ and R=3,- share E=0.3; a unique tracked state is not implied.
        self.assertEqual(int(np.count_nonzero(abs(result.eigenvalues_MeV - 0.3) < 1e-12)), 2)
        self.assertLess(np.max(result.interpolated_residual_norms_MeV), 1e-13)

    def test_common_j_spin_range_and_coordinate_shapes(self):
        p = parameters(two_j=11)
        for two_I in range(9, 28, 2):
            with self.subTest(two_I=two_I):
                system = build_nambu(two_I, p)
                result = solve_nambu(system, 0.5)
                dim = (two_I + 1) * (p.two_j + 1)
                d = dim // 4
                self.assertEqual(result.eigenvectors.shape, (2 * d, 2 * d))
                self.assertEqual(result.embedding.shape, (2 * dim, 2 * d))
                self.assertEqual(result.eigenvectors_product.shape, (2 * dim, 2 * d))
                self.assertEqual(result.eigenvectors_original_d2.shape, (2 * d, 2 * d))
                self.assertTrue(np.all(np.isfinite(result.eigenvalues_MeV)))
                self.assertTrue(np.all(result.adjacent_spacings_MeV >= 0))
                self.assertFalse(result.eigenvalues_MeV.flags.writeable)
                self.assertFalse(system.K_MeV.flags.writeable)
                self.assertFalse(result.embedding.flags.writeable)

    def test_t_and_system_boundaries(self):
        system = build_nambu(3, parameters())
        for bad in (-0.1, 1.1, float("nan"), float("inf"), True, "0.5", 0.5j):
            with self.subTest(t=bad):
                for function in (hamiltonian_at, original_d2_hamiltonian_at, solve_nambu):
                    with self.assertRaises(ValueError):
                        function(system, bad)
        for function in (hamiltonian_at, original_d2_hamiltonian_at, solve_nambu):
            with self.assertRaises(TypeError):
                function(None, 0.5)
        self.assertEqual(solve_nambu(system, np.float64(0.5)).t, 0.5)

    def test_inherited_spin_and_parameter_boundaries(self):
        for bad in (0, -1, 2, 3.0, True):
            with self.subTest(two_I=bad):
                with self.assertRaises(ValueError):
                    build_nambu(bad, parameters())
        with self.assertRaises(TypeError):
            build_nambu(3, {})
        with self.assertRaises(ValueError):
            parameters(Delta_MeV=0)
        with self.assertRaises(ValueError):
            parameters(inertias_hbar2_per_MeV=(1, 0, 3))


if __name__ == "__main__":
    unittest.main()
