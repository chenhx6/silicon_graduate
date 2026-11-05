"""Independent mathematical checks for the custom paired single-j kernel.

These checks establish identities of a declared finite model, not a fit to a
nucleus, a mode assignment, a physical EM validation, or a Gizon replay.
In particular Q_j differs in sign and normalization from the conventional
spinor projection of the unit-normalized Y_2 combination. An independent
angular integral makes that convention boundary explicit.

The spherical reference uses D2 group characters, not the implementation's
basis enumeration. The paired-block reference builds the full original
Nambu Hamiltonian with direct (I-j)^2 matrices, independently of the kernel's
factorized assembly, and then checks its positive-subspace projection.
Only strictly positive gaps are supported; zero gap is deliberately rejected.
No data files, caches, fitted nuclear levels, or output artifacts are used.
"""

from dataclasses import FrozenInstanceError, replace
import math
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))

import paired_single_j_rotor as kernel
from paired_single_j_rotor import (
    PairedRotorParameters,
    d2_embedding,
    irrotational_moments,
    lambda_from_top_pair,
    quadrupole_operator,
    single_particle_spectrum,
    solve,
    tilde_lambda_from_top_pair,
)


def parameters(**overrides):
    """Generic test inputs, not a nuclear parameter set."""
    values = dict(
        two_j=11, C_MeV=3.2, gamma_deg=23.0,
        inertias_hbar2_per_MeV=(17.0, 8.0, 3.0),
        lambda_F_MeV=0.63, Delta_MeV=0.74,
    )
    values.update(overrides)
    return PairedRotorParameters(**values)


def reference_spin(two_spin):
    """Independent angular-momentum matrices, descending projection order."""
    spin = two_spin / 2
    projection = np.arange(spin, -spin - 1, -1)
    ladder = np.diag(np.sqrt((spin + projection[:-1]) * (spin - projection[:-1] + 1)), 1)
    return (
        (ladder + ladder.T) / 2,
        (ladder - ladder.T) / (2j),
        np.diag(projection),
    )


def reference_rotor(two_I, two_j, inertias):
    """Direct product-space rotor; convert independent matrices to ascending order."""
    total = [op[::-1, ::-1].copy() for op in reference_spin(two_I)]
    total[1] *= -1
    particle = [op[::-1, ::-1].copy() for op in reference_spin(two_j)]
    dim = (two_I + 1) * (two_j + 1)
    h = np.zeros((dim, dim), complex)
    for i, j, inertia in zip(total, particle, inertias):
        difference = np.kron(i, np.eye(two_j + 1)) - np.kron(np.eye(two_I + 1), j)
        h += difference @ difference / (2 * inertia)
    return h


class InputContractTests(unittest.TestCase):
    def test_parameters_copy_inertias_and_are_frozen(self):
        moments = [3.0, 11.0, 7.0]
        p = parameters(two_j=np.int64(11), inertias_hbar2_per_MeV=moments)
        moments[0] = -4
        self.assertEqual(p.inertias_hbar2_per_MeV, (3.0, 11.0, 7.0))
        self.assertIs(type(p.two_j), int)
        with self.assertRaises(FrozenInstanceError):
            p.C_MeV = 4

    def test_half_integer_spin_input_boundaries(self):
        for bad in (0, -1, 2, 11.0, 3.5, True, False, "11", float("nan"), float("inf")):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    parameters(two_j=bad)
                with self.assertRaises(ValueError):
                    d2_embedding(bad, 11)
                with self.assertRaises(ValueError):
                    solve(bad, parameters())

    def test_nonfinite_and_non_numeric_parameter_boundaries(self):
        for name in ("C_MeV", "gamma_deg", "lambda_F_MeV", "Delta_MeV"):
            for bad in (float("nan"), float("inf"), -float("inf"), True, "1.0", 1j):
                with self.subTest(name=name, bad=bad):
                    with self.assertRaises(ValueError):
                        parameters(**{name: bad})

    def test_inertia_boundaries(self):
        for bad in ((), (1, 2), (1, 2, 3, 4), (0, 1, 2), (-1, 1, 2),
                    (1, float("nan"), 2), (1, float("inf"), 2),
                    (True, 1, 2), 3.0, "123"):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    parameters(inertias_hbar2_per_MeV=bad)

    def test_zero_gap_rejected_at_and_away_from_fermi_degeneracy(self):
        for lam in (0.0, 0.7):
            with self.subTest(lam=lam):
                with self.assertRaisesRegex(ValueError, "strictly positive.*Fermi degeneracy"):
                    parameters(C_MeV=0, lambda_F_MeV=lam, Delta_MeV=0)
        with self.assertRaises(ValueError):
            parameters(Delta_MeV=-0.1)

    def test_explicit_object_types_and_unsupported_numerical_scale(self):
        with self.assertRaises(TypeError):
            solve(9, {"two_j": 11})
        with self.assertRaises(TypeError):
            lambda_from_top_pair([1.0, 2.0], 1.5)
        with self.assertRaises(ValueError):
            solve(9, parameters(inertias_hbar2_per_MeV=(1e-320, 1, 1)))

    def test_zero_and_signed_strengths_are_valid(self):
        for strength in (0, 1.4, -1.4):
            result = solve(3, parameters(two_j=3, C_MeV=strength))
            self.assertTrue(np.all(np.isfinite(result.eigenvalues_MeV)))
            self.assertGreaterEqual(result.eigenvalues_MeV[0], result.parameters.Delta_MeV - 1e-12)


class SingleParticleConventionTests(unittest.TestCase):
    def test_axial_quadrupole_spectrum_is_analytic(self):
        for two_j in (1, 3, 7, 11):
            with self.subTest(two_j=two_j):
                j = two_j / 2
                m = np.arange(-j, j + 1)
                strength = -2.7
                expected = np.sort(strength * (3 * m * m - j * (j + 1)) / (4 * j * (j + 1)))
                sp = single_particle_spectrum(two_j, strength, 0)
                np.testing.assert_allclose(sp.eigenvalues_MeV, expected, atol=2e-14, rtol=2e-14)

    def test_Qj_is_not_silently_the_standard_normalized_Y2(self):
        # In the stretched l=5,j=11/2 spinor, |Y_55|^2 is proportional
        # to (1-cos(theta)^2)^5. Integrate independently over cos(theta).
        cosine, weight = np.polynomial.legendre.leggauss(40)
        density = (1 - cosine * cosine) ** 5
        normalized_y20 = math.sqrt(5 / (16 * math.pi)) * (3 * cosine * cosine - 1)
        integral = float(np.dot(weight * density, normalized_y20) / np.dot(weight, density))
        q_stretched = quadrupole_operator(11, 0)[-1, -1].real
        self.assertAlmostEqual(q_stretched, 5 / 13, places=14)
        self.assertAlmostEqual(integral, -math.sqrt(5 / (4 * math.pi)) * q_stretched, places=14)
        self.assertGreater(abs(integral - q_stretched), 0.5)

    def test_kramers_pairs_trace_and_eigenvectors(self):
        sp = single_particle_spectrum(11, 3.1, 19)
        self.assertEqual(sp.eigenvalues_MeV.shape, (12,))
        self.assertEqual(sp.kramers_pair_energies_MeV.shape, (6,))
        np.testing.assert_allclose(sp.eigenvalues_MeV[::2], sp.eigenvalues_MeV[1::2], atol=1e-14)
        np.testing.assert_allclose(sp.eigenvectors.conj().T @ sp.eigenvectors, np.eye(12), atol=2e-14)
        np.testing.assert_allclose(sp.hamiltonian_MeV @ sp.eigenvectors,
                                   sp.eigenvectors * sp.eigenvalues_MeV, atol=2e-14)
        self.assertAlmostEqual(np.trace(sp.hamiltonian_MeV).real, 0, places=14)

    def test_top_pair_lambda_conversion_uses_negative_interval(self):
        # For j=3/2, C=5, gamma=0, the two pair energies are -1,+1 MeV.
        sp = single_particle_spectrum(3, 5, 0)
        np.testing.assert_allclose(sp.kramers_pair_energies_MeV, [-1, 1], atol=1e-14)
        self.assertAlmostEqual(lambda_from_top_pair(sp, 1.5), -2, places=14)
        for tilde in (-2.3, 0, 0.5, 1, 1.5, 3.7):
            with self.subTest(tilde=tilde):
                lam = lambda_from_top_pair(sp, tilde)
                self.assertAlmostEqual(tilde_lambda_from_top_pair(sp, lam), tilde, places=14)

    def test_top_pair_degeneracy_and_input_boundaries(self):
        for sp in (single_particle_spectrum(1, 5, 23), single_particle_spectrum(11, 0, 23)):
            with self.subTest(two_j=sp.two_j):
                with self.assertRaises(ValueError):
                    lambda_from_top_pair(sp, 1.5)
                with self.assertRaises(ValueError):
                    tilde_lambda_from_top_pair(sp, 0)
        sp = single_particle_spectrum(3, 5, 0)
        for bad in (float("nan"), float("inf"), True, "1.5"):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    lambda_from_top_pair(sp, bad)
                with self.assertRaises(ValueError):
                    tilde_lambda_from_top_pair(sp, bad)

    def test_single_particle_direct_entry_boundaries(self):
        for args in ((2, 1, 23), (3, float("nan"), 23), (3, 1, float("inf"))):
            with self.subTest(args=args):
                with self.assertRaises(ValueError):
                    single_particle_spectrum(*args)


class IrrotationalMomentTests(unittest.TestCase):
    def test_gamma30_values_and_axis_order(self):
        np.testing.assert_allclose(irrotational_moments(12, 30), (16, 4, 4), atol=2e-14)
        moments = irrotational_moments(12, 23)
        cycled = irrotational_moments(12, 143)
        np.testing.assert_allclose(cycled, (moments[2], moments[0], moments[1]), atol=2e-14)
        complement = irrotational_moments(12, 37)
        np.testing.assert_allclose(complement, (moments[0], moments[2], moments[1]), atol=2e-14)

    def test_axial_singularities_are_not_roundoff_positive_inertias(self):
        for angle in (-360, -120, -60, 0, 60, 120, 180, 240, 300, 360, 720):
            with self.subTest(angle=angle):
                with self.assertRaisesRegex(ValueError, "zero inertia"):
                    irrotational_moments(12, angle)
        self.assertTrue(all(x > 0 for x in irrotational_moments(12, 1e-5)))

    def test_moment_input_boundaries(self):
        for j0, angle in ((0, 23), (-1, 23), (float("inf"), 23), (12, float("nan")), (True, 23)):
            with self.subTest(j0=j0, angle=angle):
                with self.assertRaises(ValueError):
                    irrotational_moments(j0, angle)


class IndependentRotorTests(unittest.TestCase):
    def test_D2_embedding_is_orthonormal_and_rotation_invariant(self):
        for two_I, two_j in ((1, 1), (1, 11), (9, 11), (13, 3), (27, 11)):
            with self.subTest(two_I=two_I, two_j=two_j):
                p = d2_embedding(two_I, two_j)
                dim = (two_I + 1) * (two_j + 1) // 4
                self.assertEqual(p.shape, ((two_I + 1) * (two_j + 1), dim))
                np.testing.assert_allclose(p.T @ p, np.eye(dim), atol=3e-15)
                k = np.arange(-two_I, two_I + 1, 2) / 2
                omega = np.arange(-two_j, two_j + 1, 2) / 2
                # exp[-i*pi*(I_3-j_3)] acts diagonally in product coordinates.
                phases = np.exp(-1j * math.pi * (k[:, None] - omega[None, :])).ravel()
                np.testing.assert_allclose(phases[:, None] * p, p, atol=4e-15)
                # Independent pi rotation about y: both factors rotate with
                # +pi ordinary-spin matrices because total I is body-fixed.
                ry_I = np.fliplr(np.eye(two_I + 1)) @ np.diag((-1.0) ** (two_I / 2 + k))
                ry_j = np.fliplr(np.eye(two_j + 1)) @ np.diag((-1.0) ** (two_j / 2 + omega))
                np.testing.assert_allclose(np.kron(ry_I, ry_j) @ p, p, atol=3e-15)

    def test_spherical_free_rotor_spectrum_and_D2_character_multiplicities(self):
        # The multiplicity is (chi_R(0)+3*chi_R(pi))/4, independently
        # of strong-coupling K/Omega enumeration: chi_R(pi)=(-1)^R.
        for two_I, two_j in ((1, 1), (5, 3), (9, 11), (11, 11), (27, 11)):
            with self.subTest(two_I=two_I, two_j=two_j):
                inertia, lam, gap = 10.0, 0.7, 0.4
                result = solve(two_I, parameters(
                    two_j=two_j, C_MeV=0, lambda_F_MeV=lam, Delta_MeV=gap,
                    inertias_hbar2_per_MeV=(inertia,) * 3))
                expected = []
                for rotor_R in range(abs(two_I - two_j) // 2, (two_I + two_j) // 2 + 1):
                    multiplicity = (2 * rotor_R + 1 + 3 * (-1) ** rotor_R) // 4
                    energy = rotor_R * (rotor_R + 1) / (2 * inertia) + math.hypot(lam, gap)
                    expected.extend([energy] * multiplicity)
                self.assertEqual(len(expected), len(result.eigenvalues_MeV))
                np.testing.assert_allclose(result.eigenvalues_MeV, sorted(expected), atol=5e-13, rtol=3e-14)

    def test_positive_block_matches_independent_full_Nambu_projection(self):
        p = parameters(two_j=3, C_MeV=3.7, gamma_deg=28,
                       inertias_hbar2_per_MeV=(7, 12, 4), lambda_F_MeV=0.13, Delta_MeV=0.45)
        result = solve(7, p)
        hrot = reference_rotor(7, 3, p.inertias_hbar2_per_MeV)
        xi = np.kron(np.eye(8), result.single_particle.hamiltonian_MeV - p.lambda_F_MeV * np.eye(4))
        gap = p.Delta_MeV * np.eye(32)
        full_Nambu = np.block([[hrot + xi, gap], [gap, hrot - xi]])
        x = result.positive_energy_embedding
        np.testing.assert_allclose(x.conj().T @ x, np.eye(x.shape[1]), atol=3e-14)
        np.testing.assert_allclose(x.conj().T @ full_Nambu @ x, result.hamiltonian_MeV, atol=3e-14)
        # Projection intentionally discards eta; do not falsely assert full
        # Nambu invariance or claim these are full-Nambu eigenvectors.
        discarded = full_Nambu @ x - x @ result.hamiltonian_MeV
        self.assertGreater(np.linalg.norm(discarded), 0.01)

    def test_Hermitian_D2_leakage_and_eigenvector_residuals(self):
        for two_I in (9, 11, 27):
            with self.subTest(two_I=two_I):
                result = solve(two_I, parameters())
                h = result.hamiltonian_product_MeV
                p = result.product_embedding
                v = result.eigenvectors
                np.testing.assert_allclose(h, h.conj().T, atol=6e-14)
                np.testing.assert_allclose(h @ p, p @ result.hamiltonian_MeV, atol=2e-13)
                np.testing.assert_allclose(v.conj().T @ v, np.eye(len(v)), atol=5e-14)
                np.testing.assert_allclose(h @ (p @ v), (p @ v) * result.eigenvalues_MeV, atol=3e-13)
                self.assertLess(result.hermiticity_error_MeV, 6e-14)
                self.assertLess(result.d2_leakage_MeV, 2e-13)
                self.assertGreaterEqual(result.eigenvalues_MeV[0],
                                        np.min(result.quasiparticle_energies_MeV) - 1e-12)

    def test_cyclic_axis_and_full_period_symmetry(self):
        p = parameters()
        a, b, c = p.inertias_hbar2_per_MeV
        for two_I in (9, 13, 27):
            with self.subTest(two_I=two_I):
                reference = solve(two_I, p).eigenvalues_MeV
                cycled = solve(two_I, replace(p, gamma_deg=p.gamma_deg + 120,
                                              inertias_hbar2_per_MeV=(c, a, b))).eigenvalues_MeV
                full_turn = solve(two_I, replace(p, gamma_deg=p.gamma_deg + 360)).eigenvalues_MeV
                np.testing.assert_allclose(cycled, reference, atol=2e-13, rtol=3e-14)
                np.testing.assert_allclose(full_turn, reference, atol=2e-13, rtol=3e-14)

    def test_complement_gamma_requires_lambda_and_inertia_permutation(self):
        p = parameters()
        a, b, c = p.inertias_hbar2_per_MeV
        conjugate = replace(p, gamma_deg=60 - p.gamma_deg,
                            lambda_F_MeV=-p.lambda_F_MeV, inertias_hbar2_per_MeV=(a, c, b))
        eps = single_particle_spectrum(p.two_j, p.C_MeV, p.gamma_deg).eigenvalues_MeV
        other_eps = single_particle_spectrum(p.two_j, p.C_MeV, conjugate.gamma_deg).eigenvalues_MeV
        np.testing.assert_allclose(other_eps, -eps[::-1], atol=2e-14)
        for two_I in (9, 11, 19):
            with self.subTest(two_I=two_I):
                reference = solve(two_I, p).eigenvalues_MeV
                transformed = solve(two_I, conjugate).eigenvalues_MeV
                np.testing.assert_allclose(transformed, reference, atol=2e-13, rtol=3e-14)
        wrong_lambda = replace(conjugate, lambda_F_MeV=p.lambda_F_MeV)
        difference = solve(11, wrong_lambda).eigenvalues_MeV - solve(11, p).eigenvalues_MeV
        self.assertGreater(np.max(abs(difference)), 0.01)

    def test_Kramers_basis_rotation_does_not_change_positive_block(self):
        p = parameters()
        reference = solve(9, p)
        sp = single_particle_spectrum(p.two_j, p.C_MeV, p.gamma_deg)
        rotation = np.eye(p.two_j + 1, dtype=complex)
        block = np.array([[1, 1j], [1j, 1]], complex) / math.sqrt(2)
        for start in range(0, p.two_j + 1, 2):
            rotation[start:start + 2, start:start + 2] = block
        rotated_sp = replace(sp, eigenvectors=sp.eigenvectors @ rotation)
        with patch.object(kernel, "single_particle_spectrum", return_value=rotated_sp):
            rotated = solve(9, p)
        np.testing.assert_allclose(rotated.hamiltonian_product_MeV,
                                   reference.hamiltonian_product_MeV, atol=3e-14)
        np.testing.assert_allclose(rotated.eigenvalues_MeV, reference.eigenvalues_MeV, atol=1e-13)

    def test_common_j_spin_range_and_returned_EM_coordinate_maps(self):
        p = parameters()
        for two_I in range(9, 28, 2):
            with self.subTest(two_I=two_I):
                result = solve(two_I, p)
                dimension = (two_I + 1) * (p.two_j + 1) // 4
                self.assertEqual(result.eigenvalues_MeV.shape, (dimension,))
                self.assertEqual(result.eigenvectors.shape, (dimension, dimension))
                self.assertEqual(result.positive_energy_embedding.shape,
                                 (2 * (two_I + 1) * (p.two_j + 1), dimension))
                self.assertEqual(len(result.d2_basis_twice_K_Omega), dimension)
                self.assertTrue(np.all(np.isfinite(result.eigenvalues_MeV)))
                self.assertTrue(np.all(np.diff(result.eigenvalues_MeV) >= 0))
                self.assertFalse(result.eigenvalues_MeV.flags.writeable)
                self.assertFalse(result.product_embedding.flags.writeable)
                self.assertFalse(result.positive_energy_embedding.flags.writeable)


if __name__ == "__main__":
    unittest.main()
