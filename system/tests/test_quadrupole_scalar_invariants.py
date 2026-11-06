"""Independent limits and closure tests; no fit, nuclear data, or probe replay.

The rotor tests use lab matrix elements of D*_{m0} on whole angular multiplets.
At the lowest I=K, I=K,K+1,K+2 includes every intermediate state needed by
q2/q3, so the rigid axial answers are Q0^2 and Q0^3, independently of spin.
The 6j implementation is compared against explicit magnetic-substate sums.
IBM checks use finite N_B=1,2 and known O(6) limits, not experimental cases.
The restricted J+2 contractions are rotational invariants for fixed projectors
onto whole magnetic multiplets. Their different axial shape conversion tests
polynomial closure and interpretation, not a failure of rotational symmetry.

Run with OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1 and Python -B:
python3 -B -m unittest discover -s system/tests -p test_quadrupole_scalar_invariants.py -v
"""

from dataclasses import replace
from fractions import Fraction
import math
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest

import numpy as np
from scipy import sparse

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts/analysis"))
from paired_single_j_em import clebsch_gordan as cg
from quadrupole_scalar_invariants import (
    FullRepresentation, Multiplet, ReducedQuadrupole, direct_invariants,
    reduced_invariants, j_plus_two_proxy, wigner_6j,
    direct_from_spectrum, reduced_table_from_spectrum,
)
from single_j_ibfm import BosonCore, CoreParameters, IBFMKernel, IBFMParameters


OBSERVATIONS = {}


def allowed(ji, jf):
    return abs(ji-jf) <= 4 <= ji+jf and (ji+jf) % 2 == 0


def lab_tensor(spins, rme):
    """Wigner--Eckart construction, independent of scalar contraction/6j code."""
    basis = [(a, m) for a, j in enumerate(spins) for m in range(-j, j+1, 2)]
    dim = len(basis)
    q = {m: np.zeros((dim, dim), dtype=complex) for m in range(-2, 3)}
    jz = np.diag([m/2 for _, m in basis])
    jp = np.zeros((dim, dim), dtype=complex)
    index = {item: n for n, item in enumerate(basis)}
    for col, (i, mi) in enumerate(basis):
        ji = spins[i]
        if mi < ji:
            jp[index[i, mi+2], col] = math.sqrt((ji-mi)*(ji+mi+2))/2
        for row, (f, mf) in enumerate(basis):
            jf = spins[f]
            mu2 = mf-mi
            if abs(mu2) <= 4 and mu2 % 2 == 0:
                q[mu2//2][row, col] = cg(ji, mi, 4, mu2, jf, mf)*rme[f, i]/math.sqrt(jf+1)
    return q, basis, (jz, jp)


def axial_rotor(two_k, q0=1.):
    spins = [two_k, two_k+2, two_k+4]
    rme = np.array([
        [math.sqrt(ji+1)*cg(ji, two_k, 4, 0, jf, two_k)*q0 for ji in spins]
        for jf in spins
    ], dtype=complex)
    q, basis, angular = lab_tensor(spins, rme)
    representation = FullRepresentation(f"axial K={two_k}/2 band, three full spins", len(basis))
    table = ReducedQuadrupole(representation, tuple(Multiplet(f"I={j}/2", j) for j in spins), rme, True)
    return q, basis, angular, table


def ket(basis, state, two_m):
    vector = np.zeros(len(basis), dtype=complex)
    vector[basis.index((state, two_m))] = 1
    return vector


def random_reduced(spins, seed=418):
    rng = np.random.default_rng(seed)
    matrix = np.zeros((len(spins), len(spins)), dtype=complex)
    for f, jf in enumerate(spins):
        for i in range(f+1):
            ji = spins[i]
            if allowed(ji, jf):
                value = rng.normal() + (0j if f == i else 1j*rng.normal())
                matrix[f, i] = value
                matrix[i, f] = (-1)**((jf-ji)//2)*value.conjugate()
    return matrix


class DirectLimits(unittest.TestCase):
    def test_rigid_axial_lowest_spin_all_M_and_sign(self):
        records = []
        for two_k in (0, 1, 11, 13):
            for q0 in (1., -1.7):
                q, basis, angular, table = axial_rotor(two_k, q0)
                errors = []
                for m in range(-two_k, two_k+1, 2):
                    value = direct_invariants(q, ket(basis, 0, m), representation=table.representation,
                                              angular_generators=angular)
                    self.assertAlmostEqual(value.q2, q0**2, places=11)
                    self.assertAlmostEqual(value.q3, q0**3, places=11)
                    self.assertAlmostEqual(value.raw_ratio, math.copysign(1., q0), places=12)
                    self.assertIsNotNone(value.rigid_equivalent_angle_deg)
                    errors.append(max(abs(value.q2-q0**2), abs(value.q3-q0**3)))
                records.append(dict(two_K=two_k, Q0=q0, M_count=two_k+1, max_abs_error=max(errors)))
        OBSERVATIONS["axial_controls"] = records

    def test_Jplus2_proxy_has_nonzero_angle_or_domain_failure_for_axial_rotor(self):
        records = []
        for two_k in (1, 11, 13):
            _, _, _, table = axial_rotor(two_k)
            closure = reduced_invariants(table, 0)
            proxy = j_plus_two_proxy(table, 0)
            self.assertTrue(closure.complete)
            self.assertAlmostEqual(closure.invariants.q2, 1., places=12)
            self.assertAlmostEqual(closure.invariants.q3, 1., places=12)
            # Closed axial CG expressions, independent of the contraction:
            # |R(J+2,J)|^2 = 6(2J+1)/[(J+2)(2J+3)] and
            # CG(L K,20|L K)=(3K^2-L(L+1))/sqrt(L(L+1)(2L-1)(2L+3)).
            j = Fraction(two_k, 2)
            expected_ratio_squared = (
                7*(2*j+5)*(2*j*j-5*j-6)**2 / (60*(2*j+1)*(j+3)*(2*j+7))
            )
            self.assertAlmostEqual(proxy.raw_proxy_ratio**2, float(expected_ratio_squared), places=12)
            if two_k == 13:
                self.assertGreater(proxy.raw_proxy_ratio, 1.)
                self.assertIsNone(proxy.proxy_angle_deg)
                self.assertEqual(proxy.angle_status, "outside_rigid_domain")
            else:
                self.assertGreater(proxy.proxy_angle_deg, 1.)
            self.assertLess(proxy.quadratic_closure_contribution, 1.)
            self.assertFalse(proxy.complete_scalar_closure)
            self.assertFalse(hasattr(proxy, "q2"))
            records.append(dict(two_K=two_k, proxy_ratio=proxy.raw_proxy_ratio,
                                proxy_angle_deg=proxy.proxy_angle_deg,
                                angle_status=proxy.angle_status,
                                retained_quadratic=proxy.quadratic_closure_contribution))
        OBSERVATIONS["axial_Jplus2_proxy"] = records

    def test_unit_scaling_and_zero_operator(self):
        q, basis, _, table = axial_rotor(1)
        psi = ket(basis, 0, 1)
        for factor in (0., 1e-12, .73, -3.2):
            result = direct_invariants({m: factor*t for m, t in q.items()}, psi,
                                       representation=table.representation)
            if factor:
                self.assertAlmostEqual(result.q2/factor**2, 1., places=12)
                self.assertAlmostEqual(result.q3/factor**3, 1., places=12)
            else:
                self.assertEqual(result.q2, 0)
                self.assertEqual(result.q3, 0)
                self.assertIsNone(result.raw_ratio)
                self.assertIsNone(result.rigid_equivalent_angle_deg)

    def test_magnitude_fluctuations_outside_rigid_interval_are_not_clipped(self):
        q, basis, angular, _ = axial_rotor(1)
        psi = np.concatenate([ket(basis, 0, 1), ket(basis, 0, 1)]) / math.sqrt(2)
        representation = FullRepresentation("two radial sectors of an axial band", len(psi))
        for sign in (1, -1):
            components = {m: sparse.block_diag((sign*t, sign*2*t), format="csr") for m, t in q.items()}
            generators = tuple(sparse.block_diag((j, j), format="csr") for j in angular)
            result = direct_invariants(components, psi, representation=representation,
                                       angular_generators=generators)
            self.assertAlmostEqual(result.q2, 2.5, places=12)
            self.assertAlmostEqual(result.q3, sign*4.5, places=12)
            self.assertGreater(abs(result.raw_ratio), 1.1)
            self.assertIsNone(result.rigid_equivalent_angle_deg)
            self.assertEqual(result.angle_status, "outside_rigid_domain")

    def test_only_tiny_boundary_rounding_and_raw_value_preserved(self):
        q, basis, _, _ = axial_rotor(1)
        psi = np.concatenate([ket(basis, 0, 1), ket(basis, 0, 1)]) / math.sqrt(2)
        representation = FullRepresentation("near-equal radial sectors", len(psi))
        components = {m: sparse.block_diag((t, (1+1e-6)*t), format="csr") for m, t in q.items()}
        result = direct_invariants(components, psi, representation=representation)
        self.assertGreater(result.raw_ratio, 1)
        self.assertLess(result.raw_ratio-1, 1e-12)
        self.assertEqual(result.angle_status, "rounded_numerical_boundary")
        self.assertEqual(result.rigid_equivalent_angle_deg, 0.)
        strict = direct_invariants(components, psi, representation=representation, angle_tolerance=0.)
        self.assertIsNone(strict.rigid_equivalent_angle_deg)

    def test_arbitrary_complex_basis_and_state_rephasing(self):
        spins = [1, 3, 5, 5]
        q, basis, angular = lab_tensor(spins, random_reduced(spins))
        psi = ket(basis, 1, 1)
        rep = FullRepresentation("complex tensor with repeated multiplets", len(basis))
        original = direct_invariants(q, psi, representation=rep, angular_generators=angular)
        rng = np.random.default_rng(917)
        unitary, _ = np.linalg.qr(rng.normal(size=(len(basis), len(basis))) +
                                   1j*rng.normal(size=(len(basis), len(basis))))
        rotated = direct_invariants(
            {m: unitary.conj().T @ t @ unitary for m, t in q.items()},
            np.exp(.71j)*(unitary.conj().T @ psi), representation=rep,
            angular_generators=tuple(unitary.conj().T @ j @ unitary for j in angular),
        )
        self.assertAlmostEqual(rotated.q2, original.q2, places=11)
        self.assertAlmostEqual(rotated.q3, original.q3, places=11)
        self.assertLess(abs(rotated.q3_complex.imag), 1e-12)

    def test_sparse_and_dense_agree(self):
        q, basis, _, table = axial_rotor(11)
        psi = ket(basis, 0, 1)
        a = direct_invariants(q, psi, representation=table.representation)
        b = direct_invariants({m: sparse.csr_matrix(v) for m, v in q.items()}, psi,
                              representation=table.representation)
        self.assertAlmostEqual(a.q2, b.q2, places=13)
        self.assertAlmostEqual(a.q3, b.q3, places=13)


class ReducedClosureTests(unittest.TestCase):
    def test_6j_against_explicit_magnetic_sum_including_half_integer_phase(self):
        errors = []
        for tj, ta, tb in [(0, 4, 4), (1, 3, 5), (1, 3, 3), (11, 7, 9),
                          (11, 11, 13), (13, 13, 15), (4, 2, 4), (4, 4, 6)]:
            for tm in range(-tj, tj+1, 2):
                coefficient = 0.
                for m in range(-2, 3):
                    for n in range(-2, 3):
                        p = -m-n
                        if abs(p) > 2:
                            continue
                        ma, mb = tm+2*p, tm-2*m
                        coefficient += (
                            (-1)**(m+n)*cg(4, 2*m, 4, 2*n, 4, 2*(m+n))
                            * cg(tb, mb, 4, 2*m, tj, tm)
                            * cg(ta, ma, 4, 2*n, tb, mb)
                            * cg(tj, tm, 4, 2*p, ta, ma)
                            / math.sqrt((tj+1)*(ta+1)*(tb+1))
                        )
                sixj_value = math.sqrt(5)*(-1)**tj/(tj+1)*wigner_6j(4, 4, 4, tj, ta, tb)
                errors.append(abs(coefficient-sixj_value))
                self.assertAlmostEqual(coefficient, sixj_value, places=13)
        OBSERVATIONS["sixj_magnetic_sum"] = dict(cases=len(errors), max_abs_error=max(errors))

    def test_6j_known_values_symmetries_and_boundaries(self):
        self.assertAlmostEqual(wigner_6j(4, 4, 4, 0, 4, 4), .2, places=14)
        self.assertAlmostEqual(wigner_6j(1, 1, 0, 1, 1, 0), -.5, places=14)
        value = wigner_6j(4, 4, 4, 11, 9, 13)
        self.assertAlmostEqual(value, wigner_6j(4, 4, 4, 13, 11, 9), places=14)
        self.assertEqual(wigner_6j(0, 0, 4, 0, 0, 0), 0)
        for bad in (-1, 1., True):
            with self.assertRaises(ValueError):
                wigner_6j(bad, 4, 4, 4, 4, 4)

    def test_general_spin_closure_direct_complex_and_M_invariant(self):
        largest = 0.
        for spins in ([0, 2, 4, 4, 6], [1, 3, 5, 5]):
            rme = random_reduced(spins)
            q, basis, angular = lab_tensor(spins, rme)
            rep = FullRepresentation("general complex angular multiplets", len(basis))
            table = ReducedQuadrupole(rep, tuple(Multiplet(f"a{i}", j) for i, j in enumerate(spins)), rme, True)
            has_complex_terms = False
            for initial, tj in enumerate(spins):
                result = reduced_invariants(table, initial)
                self.assertTrue(result.complete)
                self.assertFalse(result.missing_entries)
                self.assertAlmostEqual(sum(result.quadratic_by_two_J.values()), result.invariants.q2)
                self.assertAlmostEqual(abs(sum(result.cubic_by_two_J_pair.values()) - result.invariants.q3), 0.)
                has_complex_terms |= any(abs(v.imag) > 1e-5 for v in result.cubic_by_state_pair.values())
                for tm in range(-tj, tj+1, 2):
                    direct = direct_invariants(q, ket(basis, initial, tm), representation=rep,
                                               angular_generators=angular)
                    error = max(abs(direct.q2-result.invariants.q2), abs(direct.q3-result.invariants.q3))
                    largest = max(largest, error)
                    self.assertLess(error, 2e-11)
            self.assertTrue(has_complex_terms)
        OBSERVATIONS["general_reduced_vs_direct_max_abs_error"] = largest

    def test_J0_standard_chain_normalization(self):
        spins = [0, 4, 4]
        rme = random_reduced(spins, seed=94)
        table = ReducedQuadrupole(FullRepresentation("J0 and two J2 multiplets", 11),
                                  tuple(Multiplet(str(i), j) for i, j in enumerate(spins)), rme, True)
        chain = sum(rme[0, a]*rme[a, b]*rme[b, 0] for a in (1, 2) for b in (1, 2))
        actual = reduced_invariants(table, 0).invariants
        self.assertAlmostEqual(abs(actual.q3_complex + math.sqrt(.7)*chain), 0., places=13)

    def test_reduced_eigenstate_rephasing_keeps_loops_and_strengths(self):
        spins = [1, 3, 5, 5]
        rme = random_reduced(spins)
        phase = np.exp(1j*np.array([.1, .7, -.4, 2.1]))
        table = ReducedQuadrupole(FullRepresentation("rephased multiplets", sum(j+1 for j in spins)),
                                  tuple(Multiplet(str(i), j) for i, j in enumerate(spins)), rme, True)
        changed = replace(table, rme=phase[:, None].conj()*rme*phase[None, :])
        for i in range(len(spins)):
            a, b = reduced_invariants(table, i), reduced_invariants(changed, i)
            self.assertAlmostEqual(a.invariants.q2, b.invariants.q2, places=12)
            self.assertAlmostEqual(a.invariants.q3, b.invariants.q3, places=12)
            for key in a.cubic_by_state_pair:
                self.assertAlmostEqual(abs(a.cubic_by_state_pair[key]-b.cubic_by_state_pair[key]), 0., places=12)

    def test_missing_allowed_RME_is_reported_not_zero(self):
        _, _, _, table = axial_rotor(11)
        rme = table.rme.copy()
        rme[1, 0] = rme[0, 1] = np.nan
        result = reduced_invariants(replace(table, rme=rme), 0)
        self.assertFalse(result.complete)
        self.assertIsNone(result.invariants)
        self.assertIn((table.multiplets[1].label, table.multiplets[0].label), result.missing_entries)
        self.assertIsNone(result.quadratic_by_state[table.multiplets[1].label])

    def test_unrepresented_states_and_explicit_completeness_declaration(self):
        _, _, _, table = axial_rotor(11)
        partial = replace(table, multiplets=table.multiplets[:2], rme=table.rme[:2, :2], complete=False)
        result = reduced_invariants(partial, 0)
        self.assertIsNone(result.invariants)
        self.assertGreater(result.unrepresented_dimension, 0)
        self.assertFalse(result.declared_complete_registry)
        self.assertLess(result.quadratic_partial, 1.)
        self.assertIsNone(reduced_invariants(replace(table, complete=False), 0).invariants)
        with self.assertRaises(ValueError):
            replace(partial, complete=True)

    def test_known_selection_zeros_are_distinct_from_unknown_allowed_entries(self):
        _, _, _, table = axial_rotor(1)
        rme = table.rme.copy()
        rme[0, 0] = np.nan  # 1/2 -> 1/2 rank 2 is forbidden independently.
        result = reduced_invariants(replace(table, rme=rme), 0)
        self.assertTrue(result.complete)
        self.assertAlmostEqual(result.invariants.q2, 1., places=12)

    def test_nonhermitian_and_forbidden_RME_rejected(self):
        _, _, _, table = axial_rotor(11)
        rme = table.rme.copy()
        rme[1, 0] *= np.exp(.3j)
        with self.assertRaisesRegex(ValueError, "reciprocity"):
            reduced_invariants(replace(table, rme=rme), 0)
        _, _, _, small = axial_rotor(1)
        bad = small.rme.copy()
        bad[0, 0] = 1
        with self.assertRaisesRegex(ValueError, "forbidden"):
            reduced_invariants(replace(small, rme=bad), 0)

    def test_proxy_cutoff_ordering_missing_entries_and_global_partial_registry(self):
        spins = [0] + [4]*6
        rme = random_reduced(spins)
        table = ReducedQuadrupole(FullRepresentation("six J2 multiplets", 31),
                                  tuple(Multiplet(str(i), j) for i, j in enumerate(spins)), rme, True)
        proxy = j_plus_two_proxy(table, 0)
        self.assertEqual(len(proxy.selected_labels), 5)
        self.assertEqual(len(j_plus_two_proxy(table, 0, max_states=None).selected_labels), 6)
        self.assertFalse(j_plus_two_proxy(replace(table, complete=False), 0).complete_scalar_closure)
        for count in (0, -1, True, 2.5):
            with self.assertRaises(ValueError):
                j_plus_two_proxy(table, 0, max_states=count)
        bad = rme.copy()
        bad[1, 2] = np.nan
        with self.assertRaisesRegex(ValueError, "unknown"):
            j_plus_two_proxy(replace(table, rme=bad), 0)


class BosonAndAdapterControls(unittest.TestCase):
    def test_spectator_R0_core_NB1_NB2_all_fermion_M(self):
        records = []
        for nb in (1, 2):
            core = BosonCore(CoreParameters(nb, .7, -.08, -.5))
            solution = core.solve()
            state = int(solution.indices_for_J(0)[0])
            operator = core.e2(1.3, -.6)
            baseline = direct_from_spectrum(solution, operator, state, representation_label="core R0")
            corepsi = np.zeros(core.bosons.dimension, dtype=complex)
            corepsi[solution.basis.full_indices] = solution.vectors[:, state]
            largest = 0.
            for tj in (1, 11, 13):
                dimension = core.bosons.dimension*(tj+1)
                q = {m: sparse.kron(t, sparse.eye(tj+1), format="csr") for m, t in operator.components.items()}
                rep = FullRepresentation("R0 core tensor spectator product", dimension)
                for fm in range(tj+1):
                    psi = np.kron(corepsi, np.eye(tj+1)[:, fm])
                    value = direct_invariants(q, psi, representation=rep)
                    error = max(abs(value.q2-baseline.q2), abs(value.q3-baseline.q3))
                    largest = max(largest, error)
                    self.assertLess(error, 2e-11)
            self.assertGreater(abs(baseline.q3), .01)
            records.append(dict(NB=nb, core_q2=baseline.q2, core_q3=baseline.q3, max_abs_error=largest))
        OBSERVATIONS["spectator_NB1_NB2"] = records

    def test_O6_chi0_ground_state_cubic_zero_and_quadratic_Casimir(self):
        records = []
        for nb in (1, 2):
            core = BosonCore(CoreParameters(nb, 0., -.3, 0.))
            solution = core.solve()
            state = int(solution.indices_for_J(0)[0])
            operator = core.e2(1., 0.)
            value = direct_from_spectrum(solution, operator, state, representation_label="O6 core")
            closure = reduced_invariants(reduced_table_from_spectrum(
                solution, operator, representation_label="O6 core"), state)
            self.assertTrue(closure.complete)
            self.assertAlmostEqual(value.q2, nb*(nb+4), places=11)
            self.assertAlmostEqual(value.q3, 0., places=11)
            self.assertAlmostEqual(closure.invariants.q3, 0., places=11)
            records.append(dict(NB=nb, q2=value.q2, q3=value.q3))
        OBSERVATIONS["O6_ground_state"] = records

    def test_IBFM_adapter_fixedM_lift_and_complete_reduced_closure(self):
        records = []
        for nb in (1, 2):
            parameters = IBFMParameters(nb, 11, .7, -.08, -.5, .3, -1.2, .13, -.05, .01)
            kernel = IBFMKernel(parameters)
            solution = kernel.solve()
            state = int(solution.indices_for_J(11)[0])
            operator = kernel.e2(1.1, .13, -.6)
            direct = direct_from_spectrum(solution, operator, state, representation_label="synthetic coupled model")
            table = reduced_table_from_spectrum(solution, operator, representation_label="synthetic coupled model")
            closure = reduced_invariants(table, state)
            self.assertTrue(closure.complete)
            self.assertLess(abs(closure.invariants.q2-direct.q2), 5e-10)
            self.assertLess(abs(closure.invariants.q3-direct.q3), 5e-10)
            other = kernel.solve(two_M=3)
            other_state = int(other.indices_for_J(11)[0])
            other_value = direct_from_spectrum(other, operator, other_state, representation_label="synthetic coupled model")
            self.assertLess(abs(other_value.q2-direct.q2), 5e-10)
            self.assertLess(abs(other_value.q3-direct.q3), 5e-10)
            phase = np.exp(1j*np.linspace(.2, 2., solution.vectors.shape[1]))
            rephased = replace(solution, vectors=solution.vectors*phase[None, :])
            rephased_result = reduced_invariants(reduced_table_from_spectrum(
                rephased, operator, representation_label="synthetic coupled model"), state)
            self.assertAlmostEqual(rephased_result.invariants.q3, direct.q3, places=9)
            records.append(dict(NB=nb, dimension=kernel.dimension, q2=direct.q2, q3=direct.q3,
                                closure_error=max(abs(closure.invariants.q2-direct.q2),
                                                  abs(closure.invariants.q3-direct.q3))))
        OBSERVATIONS["synthetic_IBFM_adapter"] = records

    def test_allowed_zero_CG_is_unknown_in_adapter(self):
        spins = [2, 4]
        rme = random_reduced(spins)
        q, basis, _ = lab_tensor(spins, rme)
        indices = np.array([i for i, (_, m) in enumerate(basis) if m == 0])
        solution = SimpleNamespace(
            basis=SimpleNamespace(full_dimension=len(basis), full_indices=indices, two_M=0),
            vectors=np.eye(2), two_J=np.array(spins), model_key="integer test representation",
        )
        operator = SimpleNamespace(rank=2, components=q, model_key=solution.model_key)
        self.assertEqual(cg(2, 0, 4, 0, 4, 0), 0)
        table = reduced_table_from_spectrum(solution, operator, representation_label="zero CG control")
        self.assertTrue(table.complete)
        self.assertTrue(np.isnan(table.rme[1, 0]))
        self.assertTrue(table.unresolved)
        result = reduced_invariants(table, 0)
        self.assertIsNone(result.invariants)
        self.assertIn(("state_1", "state_0"), result.missing_entries)
        direct = direct_from_spectrum(solution, operator, 0, representation_label="zero CG control")
        self.assertGreater(direct.q2, result.quadratic_partial)

    def test_higher_M_missing_multiplets_are_not_complete(self):
        core = BosonCore(CoreParameters(2, .7, -.08, -.5))
        solution = core.solve(two_M=4)
        table = reduced_table_from_spectrum(solution, core.e2(1., -.6), representation_label="higher M")
        self.assertFalse(table.complete)
        self.assertIsNone(reduced_invariants(table, 0).invariants)

    def test_adapter_rejects_mismatch_and_bad_embeddings(self):
        core = BosonCore(CoreParameters(1, 1., 0., 0.))
        solution, operator = core.solve(), core.e2(1., 0.)
        with self.assertRaisesRegex(ValueError, "matching model"):
            direct_from_spectrum(solution, replace(operator, model_key="wrong"), 0,
                                 representation_label="bad")
        bad_basis = replace(solution.basis, full_indices=np.zeros_like(solution.basis.full_indices))
        with self.assertRaisesRegex(ValueError, "full_indices"):
            direct_from_spectrum(replace(solution, basis=bad_basis), operator, 0,
                                 representation_label="bad")


class InputBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.q, self.basis, self.angular, self.table = axial_rotor(1)
        self.psi = ket(self.basis, 0, 1)

    def test_missing_extra_or_invalid_components(self):
        for bad in ({m: t for m, t in self.q.items() if m != 1},
                    {**self.q, 3: self.q[0]}, {str(m): t for m, t in self.q.items()}):
            with self.assertRaises(ValueError):
                direct_invariants(bad, self.psi, representation=self.table.representation)

    def test_nonhermitian_tensor_rejected_without_symmetrizing(self):
        bad = {m: t.copy() for m, t in self.q.items()}
        bad[1][0, 0] += .2j
        original = bad[1].copy()
        with self.assertRaisesRegex(ValueError, "Hermiticity"):
            direct_invariants(bad, self.psi, representation=self.table.representation)
        np.testing.assert_array_equal(bad[1], original)

    def test_covariance_is_checked_only_when_generators_are_supplied(self):
        bad = {m: t.copy() for m, t in self.q.items()}
        bad[0][0, 0] += .2
        self.assertEqual(direct_invariants(bad, self.psi, representation=self.table.representation)
                         .diagnostics["rank2_covariance"], "caller_declared")
        with self.assertRaisesRegex(ValueError, "covariance"):
            direct_invariants(bad, self.psi, representation=self.table.representation,
                              angular_generators=self.angular)

    def test_bad_state_dimension_norm_and_nonfinite_values(self):
        for state in (self.psi*2, self.psi[:-1], self.psi[:, None], self.psi*np.nan):
            with self.assertRaises(ValueError):
                direct_invariants(self.q, state, representation=self.table.representation)
        for bad_value in (np.inf, np.nan):
            bad = {m: t.copy() for m, t in self.q.items()}
            bad[0][0, 0] = bad_value
            with self.assertRaises(ValueError):
                direct_invariants(bad, self.psi, representation=self.table.representation)

    def test_representation_table_tolerance_and_index_boundaries(self):
        with self.assertRaises(TypeError):
            direct_invariants(self.q, self.psi, representation=None)
        for label, dimension in [("", 3), ("test", 0), ("test", True)]:
            with self.assertRaises(ValueError):
                FullRepresentation(label, dimension)
        for name in ("rtol", "atol", "norm_tolerance", "angle_tolerance"):
            with self.assertRaises(ValueError):
                direct_invariants(self.q, self.psi, representation=self.table.representation, **{name: -1})
        for initial in (-1, True, 0.5):
            with self.assertRaises(ValueError):
                reduced_invariants(self.table, initial)
        with self.assertRaises(IndexError):
            reduced_invariants(self.table, 100)
        with self.assertRaises(ValueError):
            replace(self.table, complete=1)
        with self.assertRaises(ValueError):
            replace(self.table, rme=np.full_like(self.table.rme, np.inf))
        with self.assertRaises(ValueError):
            replace(self.table, multiplets=(Multiplet("x", 1),)*3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
