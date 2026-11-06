**Single-j IBFM implementation and generic validation — 2026-11-05**

Implemented the explicitly defined sd-boson, one-half-integer-fermion model in `system/scripts/analysis/single_j_ibfm.py`. This is a new kernel, not a PBOS clone, an exact replay of Nomura et al., or a physical fit. The only test implementation is `system/tests/test_single_j_ibfm.py`.

No experiment-specific \(^{129}\mathrm{Ba}\) spectrum, EM prediction, photon anchor, or lifetime calibration was run. The parent's `ibfm-test-contract.json` was not read or modified. The kernel has no isotope or core-mass inference: `n_b` and every numerical parameter are caller inputs. There is no automatic \(128/8\leftrightarrow130/7\) substitution.

**Implemented conventions.** Normalized boson occupation states have order \((s,d_{-2},d_{-1},d_0,d_1,d_2)\). Fermion \(m\) ascends from \(-j\) to \(+j\), varying fastest in the product index. The full fixed-\(N_B\) boson basis is retained, with no \(n_d\) truncation.

All angular momenta are in \(\hbar\) units; tensor coupling uses Condon–Shortley CGs and
\(\widetilde a_{jm}=(-1)^{j-m}a_{j,-m}\). The pure CG helper is imported from the frozen `paired_single_j_em.py`; no legacy analyzer is used. Its existing rotor import is a module dependency, not an invoked rotor calculation.

\[
H_B=\epsilon_d n_d+\kappa Q_\chi\cdot Q_\chi,
\quad
Q_\chi=s^\dagger\widetilde d+d^\dagger\widetilde s+
\chi[d^\dagger\times\widetilde d]^{(2)}.
\]

The quadrupole product retains its one-body contractions, with no \(1/N_B\) scale. The single-j \(H_F\) is dropped as a common shift. The fermion coupling coefficients are

\[
\Gamma_{jj}=\Gamma_0(1-2v^2)Q_{jj},\qquad
\Lambda_{jj}^{j}=-2\Lambda_0\sqrt{\frac5{2j+1}}
\left(2\sqrt{v^2(1-v^2)}Q_{jj}\right)^2,
\quad A_j=-A_0\sqrt{2j+1}.
\]

`Q_jj` is an explicit signed reduced matrix element; no radial matrix element is guessed. The exchange scalar
\[
:\left[[d^\dagger\times\widetilde a]^j
\times[a^\dagger\times\widetilde d]^j\right]^0:
\]
is expanded into normal-ordered \(-d^\dagger a^\dagger a d\), including the CG and tilde phases. The monopole is implemented through the scalar tensor and reduces to \(A_0 n_d\) for \(N_F=1\). Hermiticity is checked before diagonalization; no averaging with an adjoint is performed.

The reduced-matrix convention is
\[
\langle J_fM_f|T_{kq}|J_iM_i\rangle
=\frac{(J_iM_i\,kq|J_fM_f)}{\sqrt{2J_f+1}}
\langle J_f\Vert T_k\Vert J_i\rangle,\qquad
B=\frac{|\langle J_f\Vert T_k\Vert J_i\rangle|^2}{2J_i+1}.
\]

The public EM accessors are:

| Accessor | Contents | Excluded scales |
|---|---|---|
| `core_quadrupole(chi_prime)` | Core \(Q_{\chi'}\) in the full product space | No \(e_B\), fermion term, or inferred \(\chi'\) |
| `fermion_unit_tensor(rank)` | \([a^\dagger\times\widetilde a]^{(k)}\) | No \(Q_{jj}\), occupation factor or charge |
| `particle_j()` | Unit particle angular momentum | No magnetic prefactor or occupation factor |
| `core_L()` | Unit core angular momentum | No \(g_B\) |
| `e2(eB,eF,chi_prime)` | \(e_B Q_{\chi'}-e_F(1-2v^2)Q_{jj}[a^\dagger\times\widetilde a]^{(2)}/\sqrt5\) | No rate, W.u. or radial conversion |
| `magnetic_moment(gB,gj)` | \(\mu=g_BL+g_jj\) | No \(\sqrt{3/(4\pi)}\) |
| `m1(gB,gj)` | \(\sqrt{3/(4\pi)}\,\mu\) | No additional occupation factor |

All operators use the same saved eigenvectors. For different \(J\), the total-\(J\) contribution vanishes and the M1 RME is \(\sqrt{3/(4\pi)}(g_j-g_B)\) times the unit-particle-\(j\) RME. This identity is tested without assigning a physical \(g_B\). A common magnetic scale can therefore be handled externally. It must not be applied to diagonal moments as though the total-\(J\) term vanished there.

Dividing the E2 amplitude by a nonzero \(e_B\) retains the ratio \(e_F/e_B\):
\[
T(E2)/e_B=Q_{\chi'}-
\frac{e_F}{e_B}\frac{(1-2v^2)Q_{jj}}{\sqrt5}
[a^\dagger\times\widetilde a]^{(2)}.
\]
The corresponding strength is \(B(E2)/e_B^2\). This is tested using arbitrary scales, not the parent's experimental calibration.

**Solver and public results.** `IBFMKernel.solve(two_M=1)` diagonalizes the complete \(M=1/2\) block. `BosonCore.solve(two_M=0)` does the corresponding even-core calculation. Sparse full-space matrices and block indices are accessible; only fixed-M Hamiltonians are made dense.

Energy-degenerate eigenspaces are diagonalized with \(J^2\). A nearest half-integer/integer label is accepted only after checking the \(J^2\) eigenvalue and vector residual, projection bound and parity. Energy and orthonormality residuals are also checked after the rotation. Default degeneracy tolerances are \(10^{-12}\) absolute in caller energy units and \(10^{-12}\) relative. Residual acceptance is \(2\times10^{-10}\) times the recorded matrix infinity-norm scale. A largest-component phase is fixed once per vector.

The `Spectrum` exposes `energies`, `two_J`, `vectors`, `basis`, `hamiltonian`, `J2`, `degeneracy_groups`, `diagnostics`, and `indices_for_J(two_J)`. These are mathematical labels, not band/configuration/phonon assignments.

`reduced_matrix_elements(solution,tensor)` returns final-by-initial `rme`, `strength`, `selection_zero` and `unobservable`. Its default rejects allowed transitions with zero \(q=0\) CG denominator. With `zero_cg="mask"`, those entries are NaN with `unobservable=True`; triangle-forbidden transitions instead receive exact zero and `selection_zero=True`. Unexpected nonzero component values at selection zeros are rejected.

`transition_rme` handles one pair of state indices. `calibrate_core_e2` accepts explicit core \(J=0\) and \(J=2\) state indices and an **upward** target \(B(0\to2)\). A downward datum must first be multiplied by five. The strength determines \(|e_B|\); the API's default positive sign is a declared convention, with a negative sign selectable. No experimental values are embedded in the code.

Minimal synthetic API example:

```python
from single_j_ibfm import (
    IBFMParameters, IBFMKernel, CoreParameters, BosonCore,
    reduced_matrix_elements, calibrate_core_e2,
)

# Arbitrary validation parameters; no nucleus or fitted data.
p = IBFMParameters(
    n_b=2, two_j=3, eps_d=0.8, kappa=-0.06, chi=0.2,
    v2=0.35, Q_jj=-1.3, Gamma0=0.22, Lambda0=0.17, A0=-0.09,
)
kernel = IBFMKernel(p)
states = kernel.solve()
q_core = reduced_matrix_elements(states, kernel.core_quadrupole(0.35))
f2 = reduced_matrix_elements(states, kernel.fermion_unit_tensor(2))
j_unit = reduced_matrix_elements(states, kernel.particle_j())

core = BosonCore(CoreParameters(p.n_b, p.eps_d, p.kappa, p.chi))
core_states = core.solve()
i0 = int(core_states.indices_for_J(0)[0])
i2 = int(core_states.indices_for_J(4)[0])
calibration = calibrate_core_e2(
    core, core_states, i0, i2, chi_prime=0.35,
    target_B_0_to_2=7.5,  # arbitrary synthetic target, caller units
)
```

**Actual validation.** All 25 tests passed in 1.469 seconds (3.103 seconds including discovery/imports). The recorded test log is `tests.txt` and the receipt is `tests.json`. Controls include:

- \(N_B=0\) free fermion and signed free-fermion RMEs.
- Uncoupled spectator-core \(J\) multiplets, and a completely degenerate \(H=0\) space whose coordinate vectors are not \(J\) eigenvectors.
- \(O(6)\), \(\epsilon_d=\chi=0,\kappa=1\): for \(N_B=1\), eigenvalues \(5\) once and \(1\) five times; for \(N_B=2\), \(12\) once, \(8\) five times, \(2\) fourteen times and \(0\) once, from \(\sigma(\sigma+4)-\tau(\tau+3)\).
- Full-space scalar commutators with \(J^2,J_z,J_+\), tensor ladder identities, tensor Hermiticity and boson bilinear algebra.
- Independent exchange controls at \((N_B,2j)=(1,3),(2,3),(1,5)\): full Fock product minus its vacuum contraction agrees with the normal-ordered kernel to the \(3\times10^{-13}\) test tolerance. The un-normal-ordered product and the opposite sign both fail that comparison.
- \(A_0 n_d\), the E2/quadrupole \(1-2v^2\) factor and its absence from M1.
- E2/M1 reciprocity, detailed balance, common eigenvector rephasing, zero-CG rejection/masking, core upward/downward calibration, and explicit unit-tensor decomposition.
- Rejection of non-Hermitian or non-scalar Hamiltonians and invalid inputs.

The scale-up validation used the same **synthetic** Hamiltonian parameters shown above, with \(j=11/2\), first at \(N_B=4\), then \(N_B=8\). EM checks used arbitrary \(e_B=0.8,e_F=0.2,\chi'=0.35,g_B=0.4,g_j=-0.23\). The core calibration target was the synthetic upward strength 7.5. These values are not a case fit or a \(^{129}\mathrm{Ba}\) prediction.

| Quantity | \(N_B=4\) | \(N_B=8\) |
|---|---:|---:|
| Boson dimension | 126 | 1287 |
| Full product dimension | 1512 | 15444 |
| Odd \(M=1/2\) dimension | 119 | 965 |
| Even-core \(M=0\) dimension | 18 | 105 |
| Sparse construction | 0.0223 s | 0.0826 s |
| Odd full-block solve and \(J^2\) classification | 0.0177 s | 0.3373 s |
| Total, including three RME matrices, checks and core calibration | 0.1279 s | 7.4730 s |
| Maximum \(\|Hv-Ev\|_2\) | \(6.25\times10^{-15}\) | \(2.95\times10^{-14}\) |
| Maximum \(\|J^2v-J(J+1)v\|_2\) | \(1.14\times10^{-10}\) | \(4.79\times10^{-8}\) |
| Maximum H Hermiticity residual | 0 | 0 |
| Maximum entry of \([H,J^2]\) | \(2.84\times10^{-14}\) | \(1.14\times10^{-13}\) |
| Maximum orthonormality residual | \(2.00\times10^{-15}\) | \(2.89\times10^{-15}\) |
| E2 RME reciprocity residual | \(9.77\times10^{-15}\) | \(7.62\times10^{-14}\) |
| M1 RME reciprocity residual | \(4.22\times10^{-15}\) | \(1.07\times10^{-14}\) |

The \(N_B=8\) \(J^2\) infinity-norm scale is 634.2212; its maximum relative vector residual is \(7.55\times10^{-11}\), within the declared \(2\times10^{-10}\) tolerance. This absolute residual is reported rather than replaced with the much smaller energy residual. No residual tolerance was loosened for the larger run.

Runtime environment: NumPy 2.5.4, SciPy 1.18.1; `OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1`. The process reported one thread at completion. Combined peak resident memory for the validation process was 225,224 KiB, approximately 220 MiB. Full timing, sparse matrix sizes, all EM checks and core diagnostics are in `synthetic-validation.json`.

**Remaining scope.** RMEs currently use same-M, \(q=0\) solutions. Tensor components at every \(q\) and product/block bases are exposed, but phase transport between separately solved M blocks is not implemented. Same-\(E,J\) multiplicity is not uniquely resolved by \(J^2\); both EM operators still use the same arbitrary basis in that multiplicity. Very close levels are subject to the documented degeneracy and residual tolerances. Returned cached sparse matrices must not be mutated by callers.

This is a full fixed-M dense eigensolve after sparse construction, not a large-\(N_B\) iterative eigensolver. The generic \(N_B=8\) check establishes this workload's numerical behavior; it does not validate nuclear parameters, experimental likelihoods, physical state correspondence, or a collective-mode interpretation.

Only the two new Python files and this permitted notes directory were written. No Git action, edits to frozen helpers, `PLAN.md`, get-paper, prior audit files or other session outputs were performed.
