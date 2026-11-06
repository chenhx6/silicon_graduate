# Even-core rotor and E2 review

**The parent’s integer-D₂ calculation and stated branch formula are correct under the declared rigid irrotational-rotor assumptions.** Both requested γ=26° benchmarks are reproduced. Agreement with one experimental relative E2 strength does not establish γ rigidity. The source label `3(+)` is retained.

This review used the frozen `system/scripts/ba129_core_constraints.py`, its `core/core-constraints.json`, original source pages, and independent angular-momentum calculations. Neither the parent runner nor its CG implementation was imported or executed. Results are in [core-review-results.json](core-review-results.json) and [independent-ratio-controls.csv](independent-ratio-controls.csv).

## Independent matrix and normalization proof

Set \(A_k=\hbar^2/(2\mathcal J_k)\). For integer I, the normalized D₂ basis contains even nonnegative K, with
\[
|IK\rangle_s=\frac{|IK\rangle+(-1)^I|I,-K\rangle}
{\sqrt{2(1+\delta_{K0})}}.
\]
K=0 is absent for odd I. Independently, the group projector gives multiplicity
\[
m_I=\frac{2I+1+3(-1)^I}{4}.
\]
Thus I=2 has K=0,2; I=3 has only K=2. Direct application of the angular-momentum operators gives
\[
H_2=
\begin{pmatrix}
3(A_1+A_2)&\sqrt3(A_1-A_2)\\
\sqrt3(A_1-A_2)&A_1+A_2+4A_3
\end{pmatrix}.
\]
Writing \(S=A_1+A_2+A_3\) and
\(D=A_1^2+A_2^2+A_3^2-A_1A_2-A_1A_3-A_2A_3\),
\[
E(2_{1,2})=2S\mp2\sqrt D,\qquad E(3)=4S=E(2_1)+E(2_2).
\]
The trace identity requires constant inertias, **not** irrotationality.

For I=4, writing \(S_{12}=A_1+A_2\), \(\Delta_A=A_1-A_2\), the K=0,2,4 matrix has diagonal
\((10S_{12},8S_{12}+4A_3,2S_{12}+16A_3)\), adjacent off-diagonals
\((3\sqrt5\,\Delta_A,\sqrt7\,\Delta_A)\), and zero corners.

For the unit collective tensor \(q_{20}=\cos\gamma,\ q_{2,\pm2}=\sin\gamma/\sqrt2\), Wigner–Eckart algebra gives, in the normalized I=2 K basis,
\[
t_{20}=(\cos\gamma,\sin\gamma),\qquad
T_{22}=\sqrt{\frac{10}{7}}
\begin{pmatrix}-\cos\gamma&\sin\gamma\\ \sin\gamma&\cos\gamma\end{pmatrix}.
\]
The checker independently obtains these CG coefficients from total-\(J^2\) eigenstates and lowering. Transforming these tensors with the \(H_2\) eigenvectors, and dividing squared RMEs by 5, fixes the strength normalization.

## The two ratios

Define **\(B_{21}=B(E2;2_1\to0)\), \(B_{20}=B(E2;2_2\to0)\), \(B_{22}=B(E2;2_2\to2_1)\)**. With irrotational inertias, \(s=\sin^2(3\gamma)\), \(d=9-8s\), and \(F=(3-2s)/\sqrt d\), the preceding matrices reduce to
\[
B_{21}=\frac{1+F}{10},\qquad B_{20}=\frac{1-F}{10},
\qquad B_{22}=\frac{2s}{7d}.
\]
Their common physical quadrupole scale cancels from both ratios:
\[
\boxed{\frac{B_{20}}{B_{22}}=
\frac7{20}\frac{d-(3-2s)\sqrt d}{s}},\qquad
\boxed{\frac{B_{22}}{B_{21}}=
\frac{20}{7}\frac{s}{d+(3-2s)\sqrt d}}.
\]
The stable rationalized first expression is
\[
\frac{B_{20}}{B_{22}}=
\frac75\frac{\sqrt d(1-s)}{\sqrt d+3-2s}.
\]
It tends to 0.7 as γ→0 and vanishes at 30°. Exact axial irrotational inertias are singular: 0.7 is a limiting ratio. At 30°, \(B_{21}=1/5,\ B_{20}=0,\ B_{22}=2/7\), hence \(B_{22}/B_{21}=10/7\).

Consequently \(20s/(7d)\) cannot replace either requested ratio, and \(7/40\) is incorrect for \(B_{20}/B_{22}\) at 30°.

At **γ=26°**, independent calculations give:

| Quantity | Result |
| --- | ---: |
| \(E(4_1)/E(2_1)\) | 2.781358313064 |
| \(B_{22}/B_{21}\) | 1.048894326332 |
| \(B_{20}/B_{22}\) | 0.031250950868 |

## Greiner source boundary

The actual source is `raw/books/Nuclear Models (Walter Greiner, Joachim A. Maruhn) (Z-Library).pdf`, printed pp.145–147, PDF pp.164–166. Eq. (6.169) supplies the normalized basis; Eq. (6.174) states the valid trace identity. **These pages do not state the requested E2 branch formulas**; those formulas are derived above.

There is also a printed inconsistency in the held copy. Exercise 6.6(3)–(4), p.147, gives the off-diagonal entry as
\(\hbar^2\sqrt6(\Theta_1^{-1}-\Theta_2^{-1})\).
The normalized basis and Cartesian Hamiltonian instead give
\(\hbar^2\sqrt3(\Theta_1^{-1}-\Theta_2^{-1})/2\).
Their magnitudes differ by \(2\sqrt2\), which no basis rephasing removes.

For \(\hbar=1,\ A=(1,2,3)\), the correct matrix has diagonal (9,15), off-diagonal \(-\sqrt3\), and eigenvalues (8.535898,15.464102). The printed exercise entry gives off-diagonal \(-2\sqrt6\) and eigenvalues (6.255437,17.744563). Both retain the same trace. No external erratum was sought; skills and existing knowledge were not edited.

## Experimental data roles and interpretation

Königshofen 2001, original raw PDF named in the parent script, printed **037302-2, Table I, first two rows**, reports the 907.7-keV \(2_2^+\) state:

- 550.5-keV branch: δ(E2/M1)=−75(20), relative photon intensity 100.
- 907.7-keV ground-state branch: E2, intensity 74(2).
- Relative B(E2): experimental 6.1(2) versus reference 100; IBA-CQF prediction 6.2.

The same photon/mixing inputs yield
\[
0.74(550.5/907.7)^5(1+1/75^2)=0.0607272843,
\]
consistent with the printed 0.061(2). This B ratio is **derived from those inputs**, not another independent measurement. The IBA-CQF column is a model prediction, not evidence for a rigid rotor.

The separate 200107/01NDS \(^{130}\)Ba object has cutoff 11-May-2001; the paper was published 22-Aug-2001. Its energies, RI=66(3) versus 100(6), and older mixing-ratio alternatives must not be pooled with the paper’s table. \(^{128}\)Ba uses the 201510/15NDS object. Both adopted PDFs were checked on physical p.1 against their ENSDF records.

| Core | \(E_3-E_{21}-E_{22}\), keV | Equal-weight three-energy RMS lower bound | Observed \(R_{4/2}\) | Conditional irrotational \(R_{4/2}\) |
| --- | ---: | ---: | ---: | ---: |
| 128Ba | 155.87 | 51.96 keV | 2.687746 | 3.023332 |
| 130Ba | 95.66 | 31.89 keV | 2.523504 | 2.880239 |

The bound is \(|E_3-E_{21}-E_{22}|/3\), from distance to the trace-constraint plane; it is not a confidence interval. The conditional γ values from two energies are 21.829737° and 24.247000°, each with a complementary \(60^\circ-\gamma\) solution. The 130Ba identity test remains conditional on assigning its **`3(+)`** candidate as the rotor 3⁺ member (ENSDF line 80); the qualifier was not upgraded.

The 130Ba conditional branch prediction, 0.0648313, is close to the paper’s 0.061(2), but the same rotor fails other energy constraints. Neither this agreement nor the trace violation uniquely establishes γ rigidity or γ softness. State assignments, nonconstant inertias and other omitted collective dynamics remain relevant; no physical-shape, statistical-significance or novelty claim is made.

## Actual checks and preservation

The independent checker passed **32 positive-inertia cases, nine integer D₂ representations and 15 angle controls**. Maximum discrepancies were \(2.85\times10^{-14}\) for the trace identity, \(2.00\times10^{-14}\) for \(B_{20}/B_{22}\), and \(4.45\times10^{-16}\) for upward E2 closure. Requested γ=26° values agree to their supplied rounding precision.

All recorded input hashes remained unchanged. The parent’s separate 131Ba readiness interpretation was outside this core review. Publisher scans and the two new formula-detail crops remain under `tmp/ba129-controlled-pairing/`; no source pages or extracted publisher text are stored in these outputs. Parent files, skills, knowledge, PLAN and get-paper were not modified.
