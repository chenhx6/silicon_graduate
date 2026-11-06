"""Analytical and independent-Fock controls for the new single-j IBFM.

No nuclear levels, fits or journal claims. The exchange reference uses full
fermion Fock creation/annihilation matrices and rectangular boson number
sectors: the un-normal-ordered product minus its vacuum contraction is
compared with the kernel's NF=1 normal-ordered expansion. Its CGs are built
independently by highest-weight J^2 diagonalization and lowering, rather
than the implementation's Racah sum.

Run: OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
     PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest discover
     -s system/tests -p test_single_j_ibfm.py -v
"""

from dataclasses import replace
from functools import lru_cache
import itertools
import math
from pathlib import Path
import sys
import unittest

import numpy as np
from scipy import sparse

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))

from single_j_ibfm import (
    IBFMParameters, CoreParameters, BosonSpace, BosonCore, IBFMKernel,
    TensorOperator, ZeroClebschGordanError, diagonalize_scalar,
    fermion_tensor, spin_components, reduced_matrix_elements,
    transition_rme, calibrate_core_e2, max_abs,
)


def parameters(**changes):
    values = dict(n_b=2, two_j=3, eps_d=.8, kappa=-.06, chi=.2,
                  v2=.35, Q_jj=-1.3, Gamma0=.22, Lambda0=.17, A0=-.09)
    values.update(changes)
    return IBFMParameters(**values)


def dense(matrix):
    return matrix.toarray() if sparse.issparse(matrix) else np.asarray(matrix)


def reference_raising(two_j):
    j = two_j/2
    m = np.arange(-two_j, two_j+1, 2)/2
    return np.diag(np.sqrt((j-m[:-1])*(j+m[:-1]+1)), -1)


@lru_cache(maxsize=16)
def reference_coupled_states(tj1, tj2):
    """Independent normalized CS states, built without the production CG."""
    m1 = np.arange(-tj1, tj1+1, 2)/2
    m2 = np.arange(-tj2, tj2+1, 2)/2
    mz = (m1[:, None] + m2).ravel()
    plus = (np.kron(reference_raising(tj1), np.eye(tj2+1))
            + np.kron(np.eye(tj1+1), reference_raising(tj2)))
    j2 = np.diag(mz*(mz+1)) + plus.T @ plus
    result = {}
    for tj in range(abs(tj1-tj2), tj1+tj2+1, 2):
        j = tj/2
        ix = np.flatnonzero(mz == j)
        values, vectors = np.linalg.eigh(j2[np.ix_(ix, ix)])
        k = np.argmin(abs(values-j*(j+1)))
        if abs(values[k]-j*(j+1)) > 2e-12:
            raise AssertionError("independent angular coupling failed")
        state = np.zeros(len(mz))
        state[ix] = vectors[:, k]
        phase_index = tj1*(tj2+1) + (tj-tj1+tj2)//2
        if abs(state[phase_index]) < 1e-12:
            raise AssertionError("CS highest-weight phase anchor is zero")
        state *= np.sign(state[phase_index])
        result[(tj, tj)] = state.copy()
        for tm in range(tj, -tj, -2):
            m = tm/2
            state = plus.T @ state/math.sqrt((j+m)*(j-m+1))
            result[(tj, tm-2)] = state.copy()
    return result


def reference_cg(tj1, tm1, tj2, tm2, tj, tm):
    if (tm1+tm2 != tm or abs(tm1) > tj1 or abs(tm2) > tj2
            or (tj1-tm1) % 2 or (tj2-tm2) % 2):
        return 0.0
    state = reference_coupled_states(tj1, tj2).get((tj, tm))
    if state is None:
        return 0.0
    return state[((tm1+tj1)//2)*(tj2+1)+(tm2+tj2)//2]


def reference_normal_exchange(n_b, two_j):
    """Independent complete-Fock XY minus vacuum contraction, then NF=1.

    No normal-order expansion, recoupled coefficients or production CG
    are used. Actual annihilation/creation operators provide fermion signs.
    """
    modes = two_j+1
    fdim = 2**modes
    # Extra boson sector avoids a hard-wall creation artifact.
    occupations = [
        occ for total in range(n_b+2)
        for occ in itertools.product(range(total+1), repeat=6)
        if sum(occ) == total
    ]
    lookup = {occ: i for i, occ in enumerate(occupations)}
    bdim = len(occupations)
    bdag = []
    for mode in range(6):
        row, col, val = [], [], []
        for i, occ in enumerate(occupations):
            target = list(occ)
            target[mode] += 1
            if tuple(target) in lookup:
                row.append(lookup[tuple(target)])
                col.append(i)
                val.append(math.sqrt(target[mode]))
        bdag.append(sparse.csr_matrix((val, (row, col)), shape=(bdim, bdim)))
    ann = []
    for mode in range(modes):
        row, col, val = [], [], []
        for bits in range(fdim):
            if bits & (1 << mode):
                row.append(bits ^ (1 << mode))
                col.append(bits)
                val.append((-1)**((bits & ((1 << mode)-1)).bit_count()))
        ann.append(sparse.csr_matrix((val, (row, col)), shape=(fdim, fdim)))
    x, y = {}, {}
    size = bdim*fdim
    for mu in range(-two_j, two_j+1, 2):
        x[mu] = sparse.csr_matrix((size, size))
        y[mu] = sparse.csr_matrix((size, size))
        for md in range(-2, 3):
            for mf in range(-two_j, two_j+1, 2):
                c1 = reference_cg(4, 2*md, two_j, mf, two_j, mu)
                if c1:
                    x[mu] += (c1*(-1)**((two_j-mf)//2)
                              * sparse.kron(bdag[md+3], ann[(-mf+two_j)//2], format="csr"))
                c2 = reference_cg(two_j, mf, 4, 2*md, two_j, mu)
                if c2:
                    y[mu] += (c2*(-1.0)**md
                              * sparse.kron(bdag[-md+3].T, ann[(mf+two_j)//2].T, format="csr"))
    unnormal = sum(
        (reference_cg(two_j, mu, two_j, -mu, 0, 0) * (x[mu] @ y[-mu])
         for mu in range(-two_j, two_j+1, 2)), sparse.csr_matrix((size, size)))
    fixed = sorted(occ for occ in occupations if sum(occ) == n_b)
    vacuum = np.array([lookup[occ]*fdim for occ in fixed])
    one = np.array([lookup[occ]*fdim + (1 << m) for occ in fixed for m in range(modes)])
    contraction_boson = unnormal[vacuum][:, vacuum]
    contraction = sparse.kron(contraction_boson, sparse.eye(modes), format="csr")
    product_nf1 = unnormal[one][:, one]
    return product_nf1-contraction, product_nf1, contraction


class BasisAndTensorTests(unittest.TestCase):
    def assertMatrixClose(self, a, b, tol=3e-12):
        self.assertLessEqual(max_abs(a-b), tol)

    def test_boson_dimensions_and_bilinear_normalization(self):
        for nb in range(4):
            b = BosonSpace(nb)
            self.assertEqual(b.dimension, math.comb(nb+5, 5))
            for a in range(6):
                for c in range(6):
                    self.assertMatrixClose(b.bilinear(a, c).T, b.bilinear(c, a))
            number = sum((b.bilinear(a, a) for a in range(6)),
                         sparse.csr_matrix((b.dimension,) * 2))
            self.assertMatrixClose(number, nb*b.identity)
            # U(6) algebra: [b_a†b_b,b_c†b_d]=delta_bc b_a†b_d-delta_ad b_c†b_b.
            for a, c, d, e in ((0, 1, 1, 3), (2, 4, 5, 2), (1, 4, 4, 1)):
                lhs = b.bilinear(a, c) @ b.bilinear(d, e) - b.bilinear(d, e) @ b.bilinear(a, c)
                rhs = (int(c == d)*b.bilinear(a, e) - int(a == e)*b.bilinear(d, c))
                self.assertMatrixClose(lhs, rhs)

    def test_fermion_scalar_and_vector_normalization(self):
        for tj in (1, 3, 5, 11):
            self.assertMatrixClose(fermion_tensor(tj, 0, 0),
                                   -sparse.eye(tj+1)/math.sqrt(tj+1))
            j = tj/2
            for q, angular in spin_components(tj).items():
                self.assertMatrixClose(-math.sqrt(j*(j+1)*(tj+1)/3)*fermion_tensor(tj, 1, q),
                                       angular)

    def test_tensor_ladders_and_hermiticity(self):
        families = []
        for nb in (1, 2):
            b = BosonSpace(nb)
            families.append((b.angular[0], b.L_plus, 2, b.quadrupole(.37)))
            families.append((b.angular[0], b.L_plus, 1, b.angular))
            self.assertMatrixClose(math.sqrt(10)*b.d_tensor(1, 0), b.angular[0])
        for tj in (1, 3, 5):
            angular = spin_components(tj)
            for rank in range(tj+1):
                families.append((angular[0], -math.sqrt(2)*angular[1], rank,
                                 {q: fermion_tensor(tj, rank, q) for q in range(-rank, rank+1)}))
        for z, plus, rank, tensor in families:
            for q, t in tensor.items():
                self.assertMatrixClose(t.conj().T, (-1.0)**q*tensor[-q])
                self.assertMatrixClose(z @ t - t @ z, q*t)
                if q < rank:
                    self.assertMatrixClose(plus @ t-t @ plus,
                                           math.sqrt((rank-q)*(rank+q+1))*tensor[q+1])
                else:
                    self.assertLess(max_abs(plus @ t-t @ plus), 3e-12)

    def test_total_M_basis_ordering_and_selection(self):
        k = IBFMKernel(parameters())
        all_basis = k.basis(None)
        self.assertEqual(all_basis.dimension, k.dimension)
        for tm in (1, 3, -1):
            b = k.basis(tm)
            actual = 2*b.boson_occupations @ np.array((0, -2, -1, 0, 1, 2)) + b.two_m_fermion
            np.testing.assert_array_equal(actual, tm)
            self.assertEqual(b.dimension, len(set(b.full_indices)))
        with self.assertRaises(ValueError):
            k.basis(0)
        with self.assertRaises(ValueError):
            k.basis(101)


class HamiltonianTests(unittest.TestCase):
    def test_NB0_free_fermion_for_arbitrary_couplings(self):
        for tj in (1, 3, 11):
            k = IBFMKernel(parameters(n_b=0, two_j=tj))
            self.assertEqual(max_abs(k.hamiltonian), 0)
            s = k.solve()
            np.testing.assert_array_equal(s.two_J, [tj])
            np.testing.assert_allclose(s.energies, 0, atol=1e-14)
            np.testing.assert_allclose(k.J2.toarray(), np.eye(tj+1)*(tj/2)*(tj/2+1), atol=1e-13)

    def test_O6_Q_squared_analytic_multiplicities(self):
        # sigma=N,N-2,...; tau=0..sigma. NB2,tau2 has L=2 AND L=4.
        expectations = {
            1: sorted([5]+[1]*5),
            2: sorted([12]+[8]*5+[2]*14+[0]),
        }
        for nb, expected in expectations.items():
            b = BosonSpace(nb)
            h = b.hamiltonian(0, 1, 0)
            np.testing.assert_allclose(np.linalg.eigvalsh(h.toarray()), expected, atol=1e-12)
        core = BosonCore(CoreParameters(2, 0, 1, 0))
        s = core.solve()
        actual = sorted((round(e, 10), int(j)) for e, j in zip(s.energies, s.two_J))
        self.assertEqual(actual, [(0., 0), (2., 4), (2., 8), (8., 4), (12., 0)])

    def test_spectator_core_multiplets(self):
        for nb, tj in ((1, 1), (1, 5), (2, 3), (2, 11)):
            p = parameters(n_b=nb, two_j=tj, Gamma0=0, Lambda0=0, A0=0)
            core = BosonCore(CoreParameters(nb, p.eps_d, p.kappa, p.chi)).solve()
            odd = IBFMKernel(p).solve()
            expected = []
            for e, tl in zip(core.energies, core.two_J):
                expected.extend((round(e, 9), J) for J in range(abs(int(tl)-tj), int(tl)+tj+1, 2))
            observed = [(round(e, 9), int(J)) for e, J in zip(odd.energies, odd.two_J)]
            self.assertEqual(sorted(observed), sorted(expected))
            self.assertLess(odd.diagnostics["J2_residual_max"], 2e-11)

    def test_wholly_degenerate_H_resolves_J2(self):
        p = parameters(eps_d=0, kappa=0, Gamma0=0, Lambda0=0, A0=0)
        k = IBFMKernel(p)
        s = k.solve()
        self.assertEqual(len(s.degeneracy_groups), 1)
        self.assertGreater(len(set(s.two_J)), 3)
        # Raw H=0 coordinate basis is not a J eigenbasis.
        b = k.basis()
        j2 = b.restrict(k.J2)
        self.assertGreater(max_abs(j2-sparse.diags(j2.diagonal())), 1)
        np.testing.assert_allclose(j2 @ s.vectors,
                                   s.vectors * (s.two_J*(s.two_J+2)/4), atol=3e-12)
        np.testing.assert_allclose(s.vectors.T @ s.vectors, np.eye(b.dimension), atol=3e-13)

    def test_scalars_commute_with_J2_Jz_and_Jplus(self):
        k = IBFMKernel(parameters(two_j=5))
        plus = -math.sqrt(2)*k.angular[1]
        for name, h in k.components.items():
            with self.subTest(component=name):
                self.assertLess(max_abs(h-h.T), 2e-13)
                for angular in (k.J2, k.angular[0], plus):
                    self.assertLess(max_abs(h @ angular-angular @ h), 3e-12)
        s = k.solve()
        self.assertLess(s.diagnostics["energy_residual_max"], 1e-12)
        self.assertLess(s.diagnostics["J2_residual_max"], 2e-11)

    def test_M_blocks_have_the_same_J_multiplets(self):
        k = IBFMKernel(parameters(n_b=2, two_j=5))
        low, high = k.solve(1), k.solve(5)
        expected = sorted((round(e, 10), int(j)) for e, j in zip(low.energies, low.two_J) if j >= 5)
        observed = sorted((round(e, 10), int(j)) for e, j in zip(high.energies, high.two_J))
        self.assertEqual(expected, observed)

    def test_monopole_is_A0_nd_and_gamma_has_coherence_factor(self):
        for v2 in (0, .453, .5, 1):
            p = parameters(v2=v2, A0=-.15)
            k = IBFMKernel(p)
            nd = sparse.kron(k.bosons.n_d, k.fermion_identity)
            self.assertLess(max_abs(k.monopole_scalar-nd), 1e-13)
            self.assertLess(max_abs(k.components["monopole"]-p.A0*nd), 1e-13)
            self.assertLess(max_abs(k.components["quadrupole"]
                                   -p.Gamma0*(1-2*v2)*p.Q_jj*k.quadrupole_scalar), 1e-14)
        k = IBFMKernel(parameters(v2=.5))
        self.assertEqual(max_abs(k.components["quadrupole"]), 0)
        self.assertGreater(max_abs(k.components["exchange"]), 0)

    def test_exchange_independent_Fock_product_minus_contractions(self):
        for nb, tj in ((1, 3), (2, 3), (1, 5)):
            with self.subTest(n_b=nb, two_j=tj):
                k = IBFMKernel(parameters(n_b=nb, two_j=tj))
                normal, product, contraction = reference_normal_exchange(nb, tj)
                self.assertGreater(max_abs(contraction), .1)
                self.assertGreater(max_abs(product-k.bare_exchange), .1)
                self.assertGreater(max_abs(normal+k.bare_exchange), .1)
                self.assertLess(max_abs(normal-k.bare_exchange), 3e-13)
                p = k.parameters
                factor = -2*p.Lambda0*math.sqrt(5/(tj+1))*(2*math.sqrt(p.v2*(1-p.v2))*p.Q_jj)**2
                self.assertLess(max_abs(k.components["exchange"]-factor*normal), 3e-13)

    def test_non_Hermitian_and_non_scalar_input_are_rejected(self):
        k = IBFMKernel(parameters(n_b=1))
        b = k.basis()
        h, j2 = b.restrict(k.hamiltonian), b.restrict(k.J2)
        bad = h.toarray()
        bad[0, 1] += .02
        with self.assertRaisesRegex(ValueError, "not Hermitian"):
            diagonalize_scalar(bad, j2, b)
        with self.assertRaisesRegex(ValueError, "does not commute"):
            diagonalize_scalar(np.diag(np.arange(b.dimension)), j2, b)


class ElectromagneticTests(unittest.TestCase):
    def test_free_fermion_RMEs_signs_and_magnetic_normalization(self):
        for tj in (1, 3, 11):
            k = IBFMKernel(parameters(n_b=0, two_j=tj, v2=.2, Q_jj=-1.7))
            s = k.solve()
            j = tj/2
            mu = transition_rme(s, k.magnetic_moment(.8, -.4), 0, 0)
            self.assertAlmostEqual(mu.real, -.4*math.sqrt(j*(j+1)*(2*j+1)), places=12)
            m1 = reduced_matrix_elements(s, k.m1(.8, -.4))
            self.assertAlmostEqual(m1.rme[0, 0].real, math.sqrt(3/(4*math.pi))*mu.real, places=12)
            self.assertAlmostEqual(m1.strength[0, 0], 3/(4*math.pi)*.4**2*j*(j+1), places=12)
            e2 = reduced_matrix_elements(s, k.e2(9, .125, .35))
            if tj == 1:
                self.assertTrue(e2.selection_zero[0, 0])
                self.assertEqual(e2.rme[0, 0], 0)
            else:
                # The fermion tensor has RME -sqrt(5), canceling Eq.8's sign/factor.
                self.assertAlmostEqual(e2.rme[0, 0].real, .125*(1-.4)*(-1.7), places=12)

    def test_E2_coherence_factor_but_no_M1_occupation_factor(self):
        a = IBFMKernel(parameters(v2=.2))
        b = IBFMKernel(parameters(v2=.8))
        for q in range(-2, 3):
            np.testing.assert_allclose(dense(a.e2(0, .3, .35).components[q]),
                                       -dense(b.e2(0, .3, .35).components[q]), atol=3e-14)
        for q in (-1, 0, 1):
            np.testing.assert_array_equal(dense(a.m1(.4, -.2).components[q]),
                                          dense(b.m1(.4, -.2).components[q]))
        half = IBFMKernel(parameters(v2=.5))
        self.assertEqual(max_abs(half.e2(0, .3, .35).components[0]), 0)

    def test_chi_prime_is_independent_and_units_linear(self):
        k = IBFMKernel(parameters())
        for q in range(-2, 3):
            changed = k.e2(1, .2, .35).components[q]-k.e2(1, .2, -.18).components[q]
            expected = .53*sparse.kron(k.bosons.d_tensor(2, q), k.fermion_identity)
            self.assertLess(max_abs(changed-expected), 3e-14)
            self.assertLess(max_abs(k.e2(2, .4, .35).components[q]
                                   -2*k.e2(1, .2, .35).components[q]), 3e-14)

    def test_exposed_unit_tensors_share_phases_and_E2_scale(self):
        k = IBFMKernel(parameters())
        s = k.solve()
        qb = reduced_matrix_elements(s, k.core_quadrupole(.35)).rme
        tf = reduced_matrix_elements(s, k.fermion_unit_tensor(2)).rme
        eB, eF = 1.7, .23  # Arbitrary unit-test scales, no nuclear calibration.
        physical = reduced_matrix_elements(s, k.e2(eB, eF, .35))
        normalized = reduced_matrix_elements(s, k.e2(1, eF/eB, .35))
        np.testing.assert_allclose(physical.rme,
                                   eB*qb-eF*k.parameters.gamma_jj/math.sqrt(5)*tf,
                                   atol=3e-12)
        np.testing.assert_allclose(normalized.rme, physical.rme/eB, atol=3e-12)
        np.testing.assert_allclose(normalized.strength, physical.strength/eB**2, atol=3e-12)

    def test_different_J_magnetic_scale_uses_particle_j_without_assumed_gB(self):
        k = IBFMKernel(parameters())
        s = k.solve()
        particle = reduced_matrix_elements(s, k.particle_j()).rme
        core = reduced_matrix_elements(s, k.core_L()).rme
        different = s.two_J[:, None] != s.two_J[None, :]
        np.testing.assert_allclose((particle+core)[different], 0, atol=3e-12)
        for gB, gj in ((0., 1.), (.5, -.2), (-.3, .7)):
            m1 = reduced_matrix_elements(s, k.m1(gB, gj)).rme
            np.testing.assert_allclose(m1[different],
                                       math.sqrt(3/(4*math.pi))*(gj-gB)*particle[different],
                                       atol=3e-12)

    def test_total_J_magnetic_operator_has_no_spurious_transitions(self):
        k = IBFMKernel(parameters(n_b=2, two_j=5))
        s = k.solve()
        result = reduced_matrix_elements(s, k.magnetic_moment(.37, .37))
        j = s.two_J/2
        expected = np.diag(.37*np.sqrt(j*(j+1)*(2*j+1)))
        np.testing.assert_allclose(result.rme, expected, atol=4e-12)

    def test_reciprocity_detailed_balance_and_shared_eigenvector_phases(self):
        k = IBFMKernel(parameters(n_b=2, two_j=5))
        s = k.solve()
        phase = np.exp(1j*np.linspace(.2, 1.7, len(s.energies)))
        changed = replace(s, vectors=s.vectors.astype(complex)*phase)
        for operator in (k.e2(.8, .2, .35), k.m1(.4, -.23)):
            result = reduced_matrix_elements(s, operator)
            partner = reduced_matrix_elements(changed, operator)
            factor = phase.conj()[:, None]*phase[None, :]
            np.testing.assert_allclose(partner.rme, factor*result.rme, atol=2e-12)
            np.testing.assert_allclose(partner.strength, result.strength, atol=2e-12)
            for f, jf in enumerate(s.two_J):
                for i, ji in enumerate(s.two_J):
                    expected = (-1.0)**((int(jf)-int(ji))//2)*result.rme[i, f].conjugate()
                    self.assertAlmostEqual(abs(result.rme[f, i]-expected), 0, delta=4e-12)
                    self.assertAlmostEqual((ji+1)*result.strength[f, i],
                                           (jf+1)*result.strength[i, f], delta=5e-12)
        # Relative E2/M1 phase for one transition is invariant under a common rephase.
        e, m = (reduced_matrix_elements(s, op).rme for op in (k.e2(.8, .2, .35), k.m1(.4, -.23)))
        ep, mp = (reduced_matrix_elements(changed, op).rme for op in (k.e2(.8, .2, .35), k.m1(.4, -.23)))
        valid = (abs(e) > 1e-6) & (abs(m) > 1e-6)
        np.testing.assert_allclose(ep[valid]/mp[valid], e[valid]/m[valid], atol=2e-10)

    def test_core_0_to_2_calibration_and_direction(self):
        k = BosonCore(CoreParameters(1, 1, 0, 0))
        s = k.solve()
        i, f = int(s.indices_for_J(0)[0]), int(s.indices_for_J(4)[0])
        up = abs(transition_rme(s, k.e2(1, 0), i, f))**2
        down = abs(transition_rme(s, k.e2(1, 0), f, i))**2/5
        self.assertAlmostEqual(up, 5, places=13)
        self.assertAlmostEqual(down, 1, places=13)
        c = calibrate_core_e2(k, s, i, f, chi_prime=0, target_B_0_to_2=20)
        self.assertAlmostEqual(c.eB, 2, places=13)
        self.assertAlmostEqual(abs(transition_rme(s, k.e2(c.eB, 0), i, f))**2, 20, places=12)
        with self.assertRaises(ValueError):
            calibrate_core_e2(k, s, f, i, chi_prime=0, target_B_0_to_2=20)

    def test_zero_CG_is_not_a_selection_zero(self):
        k = BosonCore(CoreParameters(1, 1, 0, 0))
        s = k.solve()
        tensor = TensorOperator("core L", 1, k.bosons.angular, k.model_key)
        i = int(s.indices_for_J(4)[0])
        with self.assertRaises(ZeroClebschGordanError):
            transition_rme(s, tensor, i, i)  # J=2,M=0: vector q=0 denominator vanishes.
        with self.assertRaises(ZeroClebschGordanError):
            reduced_matrix_elements(s, tensor)
        masked = reduced_matrix_elements(s, tensor, zero_cg="mask")
        self.assertTrue(masked.unobservable[i, i])
        self.assertFalse(masked.selection_zero[i, i])
        self.assertTrue(np.isnan(masked.rme[i, i]))
        z = int(s.indices_for_J(0)[0])
        self.assertTrue(masked.selection_zero[z, z])  # 0->0 rank 1 forbidden by triangle.
        self.assertEqual(masked.rme[z, z], 0)

    def test_model_and_M_mismatch_rejected(self):
        k = IBFMKernel(parameters())
        s = k.solve()
        other = IBFMKernel(parameters(v2=.4))
        with self.assertRaises(ValueError):
            reduced_matrix_elements(s, other.e2(1, .1, .2))
        with self.assertRaises(ValueError):
            reduced_matrix_elements(s, k.e2(1, .1, .2), final=k.solve(3))


class InputTests(unittest.TestCase):
    def test_invalid_parameters(self):
        for changes in ({"n_b":-1}, {"n_b":True}, {"two_j":2}, {"two_j":0},
                        {"two_j":3.0}, {"v2":1.01}, {"v2":-.01},
                        {"Q_jj":float("nan")}, {"chi":float("inf")},
                        {"Gamma0":True}):
            with self.subTest(changes=changes):
                with self.assertRaises(ValueError):
                    parameters(**changes)

    def test_invalid_component_and_diagonalization_tolerance(self):
        with self.assertRaises(ValueError):
            fermion_tensor(3, 1, 2)
        k = IBFMKernel(parameters(n_b=0))
        for options in ({"degeneracy_atol":-1}, {"residual_tolerance":0}):
            with self.assertRaises(ValueError):
                k.solve(**options)
        with self.assertRaises(ValueError):
            k.e2(float("nan"), 1, .2)


if __name__ == "__main__":
    unittest.main()
