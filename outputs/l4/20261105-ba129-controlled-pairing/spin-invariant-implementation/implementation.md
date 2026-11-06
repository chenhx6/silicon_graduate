Implemented the requested scalar kernel and independent numerical controls in [quadrupole_scalar_invariants.py](/workspace/wiki/system/scripts/analysis/quadrupole_scalar_invariants.py) and [test_quadrupole_scalar_invariants.py](/workspace/wiki/system/tests/test_quadrupole_scalar_invariants.py). Both target files were absent before this task. The final run passed **28 tests**, with no failures, errors or skips. Actual results and timestamps are in [validation.json](validation.json), and the complete test output is in [validation.log](validation.log).

The direct calculation requires an explicit `FullRepresentation(label, dimension)`, five finite square components, spherical Hermiticity \(Q_m^\dagger=(-1)^mQ_{-m}\), and a normalized full-space vector. It computes

\[
q_2=\sum_m\|Q_m\psi\|^2,\qquad
q_3=-\sqrt{7/2}\sum_{mn}(-1)^{m+n}
(2m\,2n|2,m+n)
\langle\psi|Q_mQ_nQ_{-m-n}|\psi\rangle .
\]

The operator order is retained. The implementation moves only the leftmost operator to the bra using spherical Hermiticity; this changes the displayed phase to \((-1)^n\) in its vector contraction. Complex contributions and complex totals remain available. Conversion to real scalar values occurs only after the imaginary residual passes a scale-dependent check. Components are not symmetrized, and the state is not automatically normalized.

**Rotational invariance and polynomial closure are separate properties.** The restricted \(J+2\) quantities are rotationally invariant functions of RMEs and fixed projectors onto complete selected magnetic multiplets. Restricting intermediate states does not remove that symmetry. These quantities differ from the complete charge-polynomial moments defined above, and their shape conversion has limited regimes. The API flag `complete_scalar_closure=False` denotes incomplete charge-polynomial closure, not failure of rotational invariance. Full model-space polynomial moments also do not automatically determine physical intrinsic shape: fluctuations and projection of the charge operator into the chosen representation affect that interpretation.

| Interface | Contract |
|---|---|
| `direct_invariants(Q, psi, representation=..., angular_generators=None)` | Dense or SciPy sparse components. Optional lab `(Jz,Jplus)` checks SU(2) and rank-2 covariance. Returns signed `q3`, raw ratio, conditional angle, complex totals and diagnostics. |
| `ReducedQuadrupole(representation, multiplets, rme, complete)` | One normalized angular multiplet per row/column; rows final, columns initial. Explicit completeness declaration; NaN means unknown. A complete registry must account for the full dimension via \(\sum(2J+1)\). |
| `reduced_invariants(table, initial_index)` | Complete general-spin closure, or `invariants=None` with missing-entry diagnostics and labelled partial sums. Decomposes quadratic contributions by state/spin and complex cubic contributions by ordered state/spin pairs. |
| `direct_from_spectrum(solution, operator, state_index, representation_label=...)` | Checks model identity and orthonormality, then lifts the fixed-M vector through `basis.full_indices` into the full operator representation. |
| `reduced_table_from_spectrum(...)` | Extracts same-M, \(q=0\) RMEs. Allowed zero-CG channels remain NaN. Higher-M omissions and truncated eigenvector sets do not acquire a complete-registry declaration. |
| `j_plus_two_proxy(table, initial_index, max_states=5)` | Rotationally invariant restricted absolute-chain proxy, in caller registry order. `max_states=None` retains all \(J+2\) states but still omits other spin sectors from the complete polynomial closure. Its fields distinguish these restricted quantities from the complete `q2` and `q3` moments. |
| `wigner_6j(...)` | Six doubled nonnegative integer arguments; independent exact-Fraction Racah sum, followed by a signed square root. |

The reduced convention is
\[
\langle J_fM_f|Q_m|J_iM_i\rangle
=\frac{(J_iM_i\,2m|J_fM_f)}{\sqrt{2J_f+1}}R_{fi}.
\]
With \(i=(J,\alpha)\), complete insertion of intermediate multiplets gives
\[
q_2=\frac{1}{2J+1}\sum_a|R_{ai}|^2,
\qquad
q_3=-\frac{\sqrt{35/2}\,(-1)^{2J}}{2J+1}
\sum_{ab}
\begin{Bmatrix}2&2&2\\J&J_a&J_b\end{Bmatrix}
R_{ia}R_{ab}R_{bi}.
\]

One way to derive the phase is to first reduce \([Q\times Q]^2\), whose product formula supplies \((-1)^{J+J_a+2}\sqrt5\), and then form the scalar dot product, supplying \((-1)^{J_a-J}/(2J+1)\). Their product is \((-1)^{2J_a+2}=(-1)^{2J}\) in an allowed integer-rank chain. Permutation symmetry of the 6j and relabelling of the two intermediate states give the expression above. For \(J=0\), only \(J_a=J_b=2\) survive and the 6j is \(1/5\), so
\[
q_3=-\sqrt{0.7}\sum_{ab}R_{0,2a}R_{2a,2b}R_{2b,0}.
\]
The tests also evaluate the unreduced magnetic-substate sums directly, without calling the 6j implementation.

The ratio \(q_3/q_2^{3/2}\) is always retained without clipping. The signed conditional angle is \(\arccos(\mathrm{ratio})/3\), in degrees over \(0\)–\(60^\circ\). A material overshoot gives `None` and `outside_rigid_domain`; an overshoot no larger than the caller's `angle_tolerance` (default \(10^{-12}\)) permits boundary rounding while preserving the original ratio and reporting the rounding. Zero \(q_2\) gives an undefined ratio and angle. Tests explicitly use two radial sectors with different quadrupole magnitudes to obtain \(|q_3/q_2^{3/2}|>1\) in a valid rotational representation.

**A requested proxy expectation needed correction.** For the axial \(K=I\) band, the complete direct and reduced scalars satisfy \(q_2=Q_0^2\), \(q_3=Q_0^3\), including \(I=1/2,11/2,13/2\). The defined restricted proxy has a nonzero angle at the first two spins, but at \(13/2\) its angle is undefined, rather than another finite nonzero angle:

| Initial \(I=K\) | Restricted raw argument | Restricted angle | Retained fraction of full quadratic scalar |
|---|---:|---:|---:|
| \(1/2\) | 0.8944271910 | 8.855017° | 0.6000000000 |
| \(11/2\) | 0.8609160648 | 10.193468° | 0.0571428571 |
| \(13/2\) | 1.2924884200 | undefined | 0.0441176471 |

This follows independently from the closed axial CG formulas. For this one-state \(J+2\) sector, the squared proxy argument is
\[
\rho_{\rm proxy}^2
=\frac{7(2I+5)(2I^2-5I-6)^2}
 {60(2I+1)(I+3)(2I+7)}.
\]
The first test run had 27 passing tests and one error because its proxy expectation incorrectly required a finite angle for every tested spin. The test was corrected using this analytic expression; no clipping or physical parameter adjustment was introduced. That run is retained as `test-attempt-1.log/json`.

Measured verification:

- Whole axial bands contained \(I=K,K+1,K+2\), every \(M\), and signed \(Q_0=1,-1.7\). Lowest-spin direct scalars recovered the analytic values with maximum absolute error \(1.78\times10^{-15}\). These spins exhaust the intermediate states needed for these particular lowest-state quadratic/cubic expectations; this does not assert closure of the infinite rotor for arbitrary higher initial spins.
- **53** explicit magnetic-substate coefficient sums matched the general 6j expression to \(1.11\times10^{-16}\). Generic complex integer/half-integer tensors, including repeated multiplets, matched direct versus reduced scalar expectations to \(4.44\times10^{-16}\).
- \(R=0\) cores with \(N_B=1,2\), tensor-product spectators \(j=1/2,11/2,13/2\), and all spectator projections retained the core scalars; largest observed difference was zero at the recorded precision.
- O(6), \(\chi=0\), \(R=0\) ground-state controls gave \(q_2=5,12\) and \(q_3=0\) for \(N_B=1,2\). This is a specified-state control, not a claim that every arbitrary superposition has zero cubic expectation.
- Synthetic coupled IBFM adapter checks used full dimensions **72** and **252**. Direct/reduced closure errors were \(3.32\times10^{-13}\) and \(4.00\times10^{-12}\). M invariance and complex eigenstate rephasing passed.
- Missing components, bad normalization, nonfinite input, spherical-Hermiticity failure, RME reciprocity failure, forbidden nonzero RMEs, incomplete state registries, and allowed zero-CG channels were checked. Dense/sparse equivalence, arbitrary complex basis changes, and explicit unit scaling down to \(10^{-12}Q\) passed.

Actual execution used `unittest.TextTestRunner` to load this one test module under Python `-B`, with `OPENBLAS_NUM_THREADS`, `OMP_NUM_THREADS`, and `MKL_NUM_THREADS` set to 1 and bytecode writing disabled. To reproduce the same suite:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest discover \
  -s system/tests -p test_quadrupole_scalar_invariants.py -v
```

Only the two requested new Python files and this notes directory were written. The frozen IBFM, EM, rotor, prototype script and prototype JSON hashes remained unchanged; their before/final hashes are recorded locally. Syntax compilation in memory and whitespace checks passed. No other test suite, get-paper operation, git operation, fit, or publication workflow was run.

Completeness of a physical model remains a caller assertion. Without supplied angular generators, rank-2 covariance is explicitly marked `caller_declared`; reduced tables assume normalized orthogonal multiplets. The adapter checks its available coordinates but cannot discover omitted physical configurations. These tests validate algebra and the stated finite model-space limits. They do not validate a nuclear shape, an experimental interpretation, or a novelty claim.

The parent subsequently reported that its direct probe passes M invariance, the spectator control and quadratic full-spin closure. Its odd-system \(J=11/2\) result has \(q_2=1.5318714\) and folded full-moment angle \(29.8945^\circ\), versus restricted \(n\le5\) angle \(29.2572^\circ\) and \(\beta_{\rm proxy}/\sqrt{q_2}=2.24895\). These are parent-provided context, not additional runs of this implementation. The parent also reports that the even-core literal \(\chi'=+0.35\) calculation gives approximately \(29.496^\circ\), rather than the published approximately \(9^\circ\). The source-operator replay remains unresolved. This kernel does not establish that the published figures have been corrected.

The conceptual correction changes documentation only. [documentation-correction.json](documentation-correction.json) records before/after hashes and an AST comparison with docstrings removed. The numerical implementation and test logic remain identical to the 28-test validation above; that historical validation record is preserved.
