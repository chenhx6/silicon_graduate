**Independent mathematical and source audit: Klein arXiv v1 and the declared two-sector Nambu matrix**

**Disposition: the inspected source provides a more constrained, nonlinear CFP framework; it does not, by itself, justify a physical-state selector for `paired_single_j_nambu.py`.** Its particle-number and completeness conditions require an explicit identification with the neighboring even systems. Several of Appendix A's proposed iteration steps fail elementary matrix checks as printed. These failures can be isolated from the valid normalization identities, eigenproblem-to-commutator argument, and constrained-variation equation A18.

Every source inconsistency below is restricted to **arXiv:nucl-th/0004051v1, 23 April 2000**, in the supplied `klein2000-v1.pdf` and `klein2000-source.tex`. The eventual publication identification, *Physical Review C* **63**, 014316 (2001), is parent-supplied bibliographic context. **The published version of record has not been inspected or compared.** Nothing here establishes an error in that version, in other KK papers, or in the entire Kerman–Klein framework.

The audit read the specified source pair and the declared Nambu implementation. It did not run a nuclear solver, fit, spectrum calculation, branch continuation, or EM calculation. The exact finite-matrix examples are mathematical checks of stated implications, not nuclear models or putative complete KK solutions. No implementation or original source was changed.

**Source and notation**

The [local PDF](/workspace/wiki/raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-v1.pdf) has 29 pages. Its first-page version banner and metadata identify the requested v1; the numbered document pages used below coincide with PDF page numbers. The target formulas agree between the TeX and rendered PDF. In particular, the disputed factors and signs are visible on [page 25](/workspace/wiki/tmp/ba129-controlled-pairing/klein-review/klein-v1-p25.png), [page 26](/workspace/wiki/tmp/ba129-controlled-pairing/klein-review/klein-v1-p26.png), and [page 27](/workspace/wiki/tmp/ba129-controlled-pairing/klein-review/klein-v1-p27.png). They are not artifacts introduced by text extraction.

| Location | Content | Exact TeX entry |
|---|---|---|
| §II, p.4, Eqs. (2.9)–(2.11) | CFP definitions and compressed state labels | [L186](/workspace/wiki/raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-source.tex:186), labels `kc.cfp1`, `kc.cfp2`, `kc.sh` |
| §II, p.5, Eqs. (2.12)–(2.17) | Nonlinear equations and energy convention | [L205](/workspace/wiki/raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-source.tex:205), `kc.eom3`, `kc.eom4`, `kc.def1`–`kc.def4` |
| §II, pp.6–7, Eqs. (2.24)–(2.30) | Number constraints, total/orbital norms, lowercase CFP scaling | [L308](/workspace/wiki/raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-source.tex:308), `kc.numc` through `littleu` |
| Appendix A, p.24, A1–A8 | CFP vector, effective Hamiltonian, density and scaled idempotence | [L1361](/workspace/wiki/raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-source.tex:1361) |
| Appendix A, p.25, A9–A14 | Frozen-field step, core energies/basis updates, orbital rescaling | [L1407](/workspace/wiki/raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-source.tex:1407) |
| Appendix A, p.26, A15–A20 | Commutator, constrained variation, core-number equations | [L1467](/workspace/wiki/raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-source.tex:1467) |
| Appendix A, p.27, A21–A23 | Proposed elimination of the multiplier | [L1523](/workspace/wiki/raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-source.tex:1523) |
| Appendix A, p.27, A24–A28 | Residual, update and asserted tangent property | [L1536](/workspace/wiki/raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-source.tex:1536) |

In the following algebra, \(H\) abbreviates the source's **effective** matrix \(\mathcal H\), and \(R\) abbreviates \(\mathcal R\). The microscopic many-body Hamiltonian, also printed as \(H\) elsewhere in the source, is a different object. The density \(R\) is not the Euler-angle rotation variable used in the main text.

Here \(\Omega=\sum_a(2j_a+1)>0\) is the scalar number of active fermion modes, not a matrix, a particle number, or the body-fixed single-particle projection also called `Omega` in the code's product-basis documentation. Set

\[
P=R/\Omega,\qquad Q=1-P.
\]

The \(P/Q\) decomposition below is the range/null-space decomposition of the density projector. It is **not** an identification with either the particle/hole blocks or the code's BCS plus/minus blocks.

**1. What the §II CFPs mean and what their constraints require**

For an odd system with particle number \(N\), Eqs. (2.9) and (2.10) define

\[
V_i(\alpha\bar n)=\langle i,N|a_\alpha|\bar n,N+1\rangle,
\qquad
U_i(\alpha\underline n)=
\langle i,N|a^\dagger_{\bar\alpha}|\underline n,N-1\rangle.
\]

The first amplitude removes a particle from the heavier even neighbor; the second adds a particle to the lighter even neighbor. Both end in the **same number-conserving odd state**. They do not describe that state as a superposition of two different particle-number eigenstates. The source defines \(\bar\alpha=(j_a,-m_a)\) at [L184](/workspace/wiki/raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-source.tex:184); additional phase conventions cannot be imported from a BCS implementation without a mapping.

The bar/underline on core states distinguishes different nuclei. Compressing their quantum numbers to `n` does not turn them into the same Hilbert space. The original labels include core spin, magnetic projection, and any additional state index. In particular, source \(J\) denotes odd-system total spin and source \(I\) even-core spin; the code uses \(I\) for its fixed total-spin block.

Closure over the appropriate odd states gives the even-core number identities, Eq. (2.24) and A19–A20:

\[
\sum_{\alpha i}|V_i(\alpha\bar n)|^2=\bar N,
\qquad
\sum_{\alpha i}|U_i(\alpha\underline n)|^2=\Omega-\underline N.
\]

With orthonormal core bases and fixed particle numbers, the off-diagonal versions are

\[
\sum_\alpha R_{11}(\alpha\bar n,\alpha\bar n')
 =\bar N\,\delta_{nn'},\qquad
\sum_\alpha R_{22}(\alpha\underline n,\alpha\underline n')
 =(\Omega-\underline N)\delta_{nn'}.
\]

These sums run over **odd states and single-particle labels at fixed core state**. They cannot be replaced by a single eigenvector's plus-sector weight. The paragraph following A20 explicitly discusses the core number matrices. Diagonalizing such a matrix changes its basis but cannot change incorrect eigenvalues into the required particle counts.

Conversely, completeness of both even-neighbor spaces and the fermionic anticommutator give, for each fixed odd state,

\[
\sum_{\alpha,\bar n}|V_i|^2=\Omega-N,\qquad
\sum_{\alpha,\underline n}|U_i|^2=N.
\]

These separate strength sums are a direct completeness derivation in this audit; the source displays their combined form in Eq. (2.26):

\[
\sum_{\alpha n}(|V_i|^2+|U_i|^2)=\Omega.
\]

Equation (2.28) additionally requires, for every active orbital \(a\),

\[
\sum_{m_a n}(|V_i|^2+|U_i|^2)=\Omega_a,\qquad \Omega_a=2j_a+1.
\]

The source itself stresses at [L344](/workspace/wiki/raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-source.tex:344) that these extra orbital constraints are not generally free normalizations of a frozen linear eigenproblem; they belong to its nonlinear problem.

Two limits matter for the proposed use:

- In a **strictly single-\(j\)** space, the displayed orbital norm is the same as the total norm. Multiplying a unit-normalized eigenvector by \(\sqrt{2j+1}\) therefore supplies no physical-state discrimination. It does not establish the core-number identities or the interpretation as transfer amplitudes.
- Exact closure requires the corresponding complete state spaces. Restricting the core to a band or truncating the odd states can discard strength. A derived truncation and its normalization conventions are needed; rescaling arbitrary vectors does not restore the missing many-body matrix elements. Particle counts must refer to the declared active fermion space, not blindly to the whole nuclear mass number.

For a complete physical CFP construction, the Gram identity is

\[
\Psi_i^\dagger\Psi_j=\Omega\delta_{ij},\qquad
R=\sum_i\Psi_i\Psi_i^\dagger
\quad\Longrightarrow\quad R^2=\Omega R.
\]

The repeated \(i\) in A7 is summed, whereas the norm of Eq. (2.26) is a condition on a fixed \(i\). Scalar norms alone do not prove this Gram identity; within degenerate eigenspaces an orthonormal basis must also be chosen. Idempotence and \([R,H]=0\) are necessary matrix conditions, but any chosen subset of orthonormal eigenvectors of a frozen Hermitian matrix generates such a spectral projector. Those conditions alone neither select a physical half nor prove CFP representability.

**2. Comparison with the declared implementation**

| Object or requirement | Klein v1 | Current code and implication |
|---|---|---|
| Amplitudes | \(V,U\) are matrix elements connecting odd \(N\) to even \(N\pm1\) | Code \(U,V\) are BCS matrix functions used in embeddings; not the same objects merely because the letters agree. See [code L13](/workspace/wiki/system/scripts/analysis/paired_single_j_nambu.py:13). |
| Effective problem | Eqs. (2.12)–(2.13), A3–A6 depend on the CFP-derived fields; A9 is a linear step with fields frozen | The code constructs a fixed \(H_R,\xi,\Delta\), [L235](/workspace/wiki/system/scripts/analysis/paired_single_j_nambu.py:235), without constructing neighboring-core CFP densities or solving their number equations. |
| Chemical potential | \(\lambda=(E_{\bar0}-E_{\underline0})/2\), Eq. (2.16) | `lambda_F_MeV` is an input to \(\xi\), [L238](/workspace/wiki/system/scripts/analysis/paired_single_j_nambu.py:238); the code does not enforce that core-energy relation. |
| Energy convention | \(\mathcal E_i=-E_i+(E_{\bar0}+E_{\underline0})/2\); A3 contains \(-E^*_{\bar n}\) and \(-E^*_{\underline n}\) | The declared matrix uses \(+H_R\) on both diagonal sectors. An explicit energy/sign, basis and field map is required before identifying its eigenvalues with Klein's \(\mathcal E_i\). |
| Selection | Physical interpretation requires the state-space and number/completeness structure | `solve_nambu` returns **all** eigenpairs, [L303](/workspace/wiki/system/scripts/analysis/paired_single_j_nambu.py:303), correctly without claiming a physical-state selection. |
| Reported weights | CFP strength sums involve specific neighboring states and particle counts | Code weights sum squared components in BCS coordinate sectors, [L320](/workspace/wiki/system/scripts/analysis/paired_single_j_nambu.py:320); they are explicitly not particle numbers or transfer strengths, [L188](/workspace/wiki/system/scripts/analysis/paired_single_j_nambu.py:188). |

The code's frozen interpolation is

\[
H_t=
\begin{pmatrix}A+E&tK\\tK^\dagger&A-E\end{pmatrix}.
\]

At \(t=0\), the rotor contribution in \(A\) is still present. Only the intersector blocks are removed; neither the rotor as a whole nor the pair gap is turned off ([code L23](/workspace/wiki/system/scripts/analysis/paired_single_j_nambu.py:23), [L284](/workspace/wiki/system/scripts/analysis/paired_single_j_nambu.py:284)). A positive energy, a dominant plus-sector weight, or a continuous eigenvector along this path does not acquire a CFP interpretation from Klein's normalization identities. The current module's explicit mathematical-diagnostics boundary is warranted.

The parent reports that **Protopapas and Klein, PRC 55, 699 (1997), DOI `10.1103/PhysRevC.55.699`**, discusses physical/unphysical halves and a continuation starting with zero core rotational energies. That source has not been acquired or inspected in this audit; acquisition belongs to the parent. Record it as a primary precedent to verify before any novelty claim. Its reported deformation path is distinct from keeping \(A\) fixed and scaling \(K\). The pre-existence of physical-state continuation must not be presented as this task's innovation, and that precedent cannot automatically certify this different path.

**3. A12–A14: the printed rescaling is not the stated norm repair**

Locations: PDF p.25; A12 at [TeX L1449](/workspace/wiki/raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-source.tex:1449), A13 at [L1454](/workspace/wiki/raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-source.tex:1454), A14 at [L1458](/workspace/wiki/raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-source.tex:1458).

Write the orbital-block squared norm as \(S_{ia}\). A12 defines

\[
S_{ia}=\Lambda_a\Omega_a.
\]

With that definition, A13's \(\Psi\mapsto\sqrt{\Lambda_a}\Psi\) gives

\[
S'_{ia}=\Lambda_a S_{ia}=\Lambda_a^2\Omega_a,
\]

which is not \(\Omega_a\) unless \(\Lambda_a=1\). For example, \(\Omega_a=2\) and a block \((2,2)^T\) give \(S=8\), \(\Lambda_a=4\), and the printed transformation gives \(S'=32\).

The reciprocal factor \(1/\sqrt{\Lambda_a}\) would normalize **one nonzero block**, given precisely A12's definition. It is an auditor-derived scalar correction, not an endorsed replacement iteration. A14 is consistent with the printed forward rescaling of the bilinear potentials, so fixing A13 alone would also leave inconsistent potential updates.

There are further algorithmic boundaries: \(\Lambda_a\) is not shown to be independent of the state \(i\); a common orbital-dependent nonunitary scaling can destroy the mutual CFP Gram identity, and state-dependent scaling changes the construction of the density and fields. A zero-strength block cannot be repaired by inverse scaling. In the single-\(j\) case, exact enforcement of Eq. (2.26) already fixes this \(\Lambda_a=1\), so this orbital-normalization step offers no additional selector.

**Finding:** do not implement A13/A14 as a corrective normalization algorithm as printed. The error origin is unresolved; no typographical explanation or published correction is assumed. The later requirement to iterate to self-consistency does not establish that this particular map repairs the measured norm defect.

**4. A18 and A21 are valid; the inference to A22 is not**

The source defines

\[
\mathcal D=\mathcal G-\operatorname{Tr}\Theta(R^2-\Omega R),
\qquad d\mathcal G=\operatorname{Tr}(H\,dR).
\]

Holding the other multipliers fixed, variation gives

\[
H-\Theta R-R\Theta+\Omega\Theta=0. \tag{A18}
\]

This is the correct derivative of A16 under A17. Its commutator with \(R\), using \(R^2=\Omega R\), yields \([R,H]=0\). Left/right multiplication also gives

\[
RH=R\Theta R=HR. \tag{A21}
\]

These valid statements do not require A22 or the later iteration. Their locations are [TeX L1482](/workspace/wiki/raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-source.tex:1482), [L1494](/workspace/wiki/raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-source.tex:1494), and [L1525](/workspace/wiki/raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-source.tex:1525).

In a basis with \(R=\Omega\operatorname{diag}(1_P,0_Q)\), write

\[
H=\begin{pmatrix}A&B\\B^\dagger&D\end{pmatrix},\qquad
\Theta=\begin{pmatrix}T&C\\C^\dagger&S\end{pmatrix}.
\]

A18 becomes

\[
\begin{pmatrix}A-\Omega T&B\\B^\dagger&D+\Omega S\end{pmatrix}=0.
\]

Thus \(B=0\), \(T=A/\Omega\), \(S=-D/\Omega\), and the off-diagonal multiplier \(C\) is undetermined. There is no implication \(H=\Omega\Theta\) on the full space. A21 cannot be cancelled through the projector's null space. A possible multiplier for a commuting \(H\) is

\[
\Theta=(PHP-QHQ)/\Omega,
\]

with arbitrary Hermitian off-diagonal additions. This also shows that, with unrestricted \(\Theta\), A18 does not supply a new physical subspace selection beyond stationarity on the projector manifold.

An exact counterexample is

\[
\Omega=2,\quad R=\begin{pmatrix}2&0\\0&0\end{pmatrix},
\quad H=\begin{pmatrix}1&0\\0&2\end{pmatrix},
\quad\Theta=\begin{pmatrix}1/2&0\\0&-1\end{pmatrix}.
\]

It satisfies A8, A15, A18 and A21, but
\(H-\Omega\Theta=\operatorname{diag}(0,4)\ne0\).

**Finding:** A22 at [TeX L1529](/workspace/wiki/raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-source.tex:1529) does not follow from the printed premises. This is not a failure of A18 or of the eigenproblem-to-commutator argument.

**5. A23 has a separate substitution error and the wrong stationary condition**

A22 would give \(\Theta=H/\Omega\). Even if that unsupported equality were imposed, substituting it into A18 produces

\[
2H-\{R,H\}/\Omega=0,
\]

not the printed

\[
H-\{R,H\}/\Omega=0. \tag{A23}
\]

The extra \(+H\) comes from \(+\Theta\Omega\) in A18. Changing a factor of two alone would not cure the invalid A21-to-A22 inference.

More decisively, with the actual scaled projector,

\[
H-\{R,H\}/\Omega=H-\{P,H\}
=\begin{pmatrix}-A&0\\0&D\end{pmatrix}.
\]

A23 sets the **diagonal** blocks to zero and leaves \(B\) unconstrained. Commutator stationarity instead sets **off-diagonal** blocks to zero. Consequently:

- A23 and \([R,H]=0\) together force \(H=0\). This holds for any positive scalar \(\Omega\), regardless of an energy-sign pairing assumption.
- The preceding commuting example has A23 residual \(\operatorname{diag}(-1,2)\ne0\).
- Taking \(H=\begin{pmatrix}0&1\\1&0\end{pmatrix}\) gives zero A23 residual but \([R,H]=\begin{pmatrix}0&2\\-2&0\end{pmatrix}\ne0\). Thus A23 can also falsely declare a nonstationary matrix solved.

A23 is printed at [TeX L1533](/workspace/wiki/raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-source.tex:1533), PDF p.27. The surrounding text does not redefine \(H\) as a tangent projection, a per-state eigenvalue residual, or a different Hamiltonian; it remains the effective Hermitian matrix of A2/A3 and A17. Restricting the equation to the range of \(P\) does not help: there it reduces to \(-H_{PP}=0\). An unprinted change of variables would be a different derivation, not validation of this formula.

**6. A25–A28: the proposed update is generally normal to the projector manifold**

Linearizing \(R^2-\Omega R=0\) correctly gives

\[
\{R,\delta R\}-\Omega\delta R=0. \tag{A27}
\]

At \(R=\Omega P\), this is equivalent to

\[
P\delta RP=0,\qquad Q\delta RQ=0.
\]

Allowed first-order variations are off-diagonal in the \(P/Q\) decomposition. A28, \(R\delta RR=0\), follows but is only one necessary block condition. For example, \(\delta R=Q\) satisfies A28 but fails A27.

In contrast, A25 defines \(Y=-PHP+QHQ\), and A26 proposes

\[
\delta R=-\eta Y=\eta PHP-\eta QHQ.
\]

It follows that

\[
\{R,\delta R\}-\Omega\delta R
=\eta\Omega(PHP+QHQ),
\qquad
R\delta RR=\eta\Omega^2 PHP.
\]

Neither expression is generally zero. For the commuting \(2\times2\) example above, the first-order constraint defect is \(\eta\operatorname{diag}(2,4)\), despite exact stationarity under A18. For a purely off-diagonal \(H\), \(Y=0\), so the update stalls even though \([R,H]\ne0\).

For the simple test functional \(\mathcal G(R)=\operatorname{Tr}(HR)\) with \(H=\operatorname{diag}(2,1)\), the proposed step gives
\(d\mathcal G=3\eta>0\). Thus the printed rule is not generally a steepest-descent direction even before restoring number or self-consistency constraints. This linear functional is an algebraic test of A17, not a replacement nuclear energy functional.

The relevant lines are [A25, L1540](/workspace/wiki/raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-source.tex:1540), [A26, L1545](/workspace/wiki/raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-source.tex:1545), [A27, L1551](/workspace/wiki/raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-source.tex:1551), and [A28 and its asserted verification, L1557](/workspace/wiki/raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-source.tex:1557).

For comparison only, an independently derived projector-tangent gradient is

\[
H_{\mathrm{tan}}=PHQ+QHP=[P,[P,H]].
\]

The infinitesimal direction \(\delta R=-\eta H_{\mathrm{tan}}\) satisfies A27 and, for the Frobenius metric and Hermitian \(H=d\mathcal G/dR\), gives
\(d\mathcal G=-\eta\operatorname{Tr}(H_{\mathrm{tan}}^2)\le0\).
A finite linear step still has a quadratic idempotence defect; unitary conjugation of \(P\), for example
\(P(s)=e^{s[P,H]}P e^{-s[P,H]}\), preserves projector rank and idempotence exactly and initially moves in the negative tangent-gradient direction. This is a **geometry check**, not Klein's printed algorithm and not a validated KK replacement. It does not by itself enforce individual-orbital norms, neighboring-core number sums, CFP representability, core spectra, or self-consistency.

**7. Safe subset and implementation boundary**

| Item | Safe use in this task |
|---|---|
| §II, (2.9)–(2.10) | Define removal/addition CFPs and keep both even-neighbor state spaces explicit. |
| §II, (2.14)–(2.17) | Preserve the energy sign, core-energy offsets and chemical-potential definition when attempting any later mapping. |
| §II, (2.24)–(2.30) | Use number/completeness identities and per-orbital norms as necessary checks, with truncation and degeneracy factors stated. The lowercase-CFP change of scale in (2.29)–(2.30) is not A13's iterative rescaling. |
| A2 and A9 | A frozen-field linear eigenproblem can be an iteration substep of the nonlinear theory. It does not certify arbitrary fixed model matrices or choose physical states. |
| A7–A8 | Construct a scaled projector from a suitable orthogonal CFP set. Do not use idempotence alone to choose that set. |
| A15–A18 and A21 | The commutator and constrained-variation algebra checked here are valid. Keep the multiplier and its block freedom; do not replace it by A22. |
| A19–A20 | Check neighboring-core particle/vacancy counts and off-diagonal number matrices in a declared core basis. |
| A12 | Use as a norm-defect diagnostic. **Do not port A13/A14 as a normalization repair.** |
| A22–A23, A25–A26 | **Do not implement as printed.** Both the multiplier elimination and the tangent/descent assertions fail. |
| A24, A27–A28 | A24 is the constraint; A27 is its correct linearization; A28 is necessary, not sufficient. |
| Fixed-rotor \(K(t)\) diagnostic | Retain the code's current all-eigenpair and nonphysical-label boundary. A separate many-body mapping and physical initial subspace would be required for a physical interpretation. |

The main-text operator equations are identified by the author as exact consequences of the stated shell-model Hamiltonian at [TeX L252](/workspace/wiki/raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-source.tex:252). This audit independently checks the CFP closure/normalization logic and the displayed Appendix matrix implications; it does **not** certify every interaction-index contraction in the full article. A failure of a proposed numerical iteration is not a refutation of the originating operator identities or the nonlinear KK formulation.

**Reproducibility and remaining boundary**

The companion [audit_checks.py](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/klein-review/audit_checks.py) uses exact `fractions.Fraction` arithmetic from the Python standard library. SymPy was unavailable in the current interpreter, so no package was installed. [audit_checks.json](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/klein-review/audit_checks.json) records the exact residuals, including a two-mode Fock-algebra check of the CFP number sums and a projector satisfying idempotence/commutation while violating those sums. Passing these checks means reproducing the expected counterexamples and identities, not approving the disputed source equations.

The review receipt records input hashes, versions inspected, output hashes, source locations, and the no-implementation-run boundary. Extractions and page images remain exclusively under `tmp/ba129-controlled-pairing/klein-review/`; reports and audit artifacts remain exclusively under this output directory.

The focused audit stops at the established algebraic counterexamples. The useful next decisions are to compare these exact formulas with the PRC version of record when that source is available, and separately inspect the parent's 1997 physical-state precedent and its initial-limit assumptions. Until that work is done, neither an alleged published erratum nor a justified physical-state prescription for the current \(K(t)\) path is established.
