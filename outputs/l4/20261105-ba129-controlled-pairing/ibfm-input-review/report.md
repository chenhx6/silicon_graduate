**Nomura–Nikšić–Vretenar (2017): input and reproducibility audit for negative-parity \(^{129}\mathrm{Ba}\)**

Audit date: 2026-11-05 UTC. This is a source-reading and input audit, not a new IBFM calculation, a reproduction of published spectra, or a fit to the controlled-pairing project. Evidence classes below distinguish printed model inputs, author calibration statements, publication metadata, and explicitly conditional audit deductions. No new experimental measurement is involved.

The strongest paper-supported reconstruction uses the **\(^{128}\mathrm{Ba}\) core** for \(^{129}\mathrm{Ba}\). With the conventional proton-particle/neutron-hole counting of that core, this gives **\(N_B=8\)**. The paper does **not** print an explicit \(^{129}\mathrm{Ba}\)-to-core input row or its numerical \(N_B\); these two conclusions have different evidence status. \(^{130}\mathrm{Ba}\), \(N_B=7\), is a different particle/hole reference choice and cannot be silently substituted because it suits a rotor fit.

The paper supplies a useful, physically motivated soft-core comparator, but its printed material and public arXiv source package are **not a complete numerical replay package**. It shows \(^{129}\mathrm{Ba}\) low-energy level predictions and E2-derived shape invariants; it does not publish transition-resolved \(^{129}\mathrm{Ba}\) \(B(E2)\), \(B(M1)\), or mixing-ratio predictions for the proposed band-discrimination test.

**1. Original inspected and version identity.** The primary object read is the user-specified [13-page local PDF](</workspace/wiki/raw/papers/2017_Nomura et al_Shape-phase transitions in odd-mass γ -soft nuclei with mass A ≈ 130.pdf>). Its SHA-256 is:

```text
481e6a9e0f6b01e9c5db5e2b06d9b350dba0638393c7da7f532c3040e9efaea9
```

This agrees with the supplied source page. The file is 1,039,399 bytes. PDF pages 1–13 carry the manuscript pagination used throughout this report; these are not asserted to be the typeset journal's page positions.

| Identity item | Directly checked result | Evidence boundary |
|---|---|---|
| Article | K. Nomura, T. Nikšić, D. Vretenar, *Shape-phase transitions in odd-mass γ-soft nuclei with mass A ≈ 130*, PRC **96**, 014304 (2017), DOI `10.1103/PhysRevC.96.014304` | Bibliographic identity, not a new 2021 paper |
| Publication metadata | Publisher-deposited Crossref record gives online publication 2017-07-07 | Metadata checked separately from manuscript text |
| Visible arXiv watermark | `arXiv:1704.07101v2 [nucl-th] 8 Jul 2017` | PDF p. 1, left margin |
| Internal date | `Dated: November 21, 2021` | PDF p. 1, title block |
| PDF metadata | Creation and modification dates `D:20211121104452Z` | Generated PDF metadata |
| Source explanation | Public arXiv v2 `v4.tex`, line 32, contains `\date{\today}` | Supports a compilation-date explanation; no claim about who recompiled it |
| Current public PDF | The retrieved `1704.07101v2` PDF is byte-identical to the supplied local PDF | Version identity checked by SHA-256, not merely by title |
| Publisher full text | APS Harvest returned 401; accepted-manuscript route returned 403 | No new journal-full-text comparison is claimed |

All 13 local pages were read as text. Visual checks covered pp. 1–5, 7–8, 11 and 13, including the relevant tables, tensor equations, core example, spectrum, shape-invariant figure, and references. The existing [Wiki source](/workspace/wiki/knowledge/sources/nomura-2017-odd-mass-gamma-soft-shape-transitions.md) was read for context but was not used as a substitute for these original-page checks.

**2. Core and boson-number decision.** The evidence must be kept in the following order.

| Question | What the paper actually supplies | Conclusion and status |
|---|---|---|
| Core species | Odd Ba/Xe are an unpaired neutron coupled to even-even Ba/Xe cores | Explicit: p. 2, left column, introduction |
| Boson count definition | \(N_B\) is the number of valence-fermion pairs; proton and neutron bosons are not distinguished; \(N_F=1\) | Explicit definition, not a per-nucleus numerical input: p. 2, end of left column and start of right column |
| Even-core inventory | Table I contains \(^{128,130,132,134,136}\mathrm{Ba}\) | Explicit: p. 3, Table I |
| Odd-Ba inventory | Tables II–V and Fig. 5 contain \(^{129,131,133,135,137}\mathrm{Ba}\) | Explicit: pp. 3–4, Tables II–V; p. 7, Fig. 5 |
| Explicit mass correspondence | The discussion identifies \(^{134}\mathrm{Ba}\) as the even-even core of \(^{135}\mathrm{Ba}\) | Explicit: p. 8, Sec. III C, left column; reiterated in the right column |
| Omission of \(^{128}\mathrm{Ba}\) from the PES figure | The \(^{128}\mathrm{Ba}\) surface is said to be nearly identical to \(^{130}\mathrm{Ba}\), so it is not plotted | Explicit: p. 5, end of Sec. III A paragraph across columns; this is not permission to replace its Hamiltonian parameters |
| Hole-counting context | The even-Ba discussion identifies valence neutron holes and the \(N=82\) closure | Explicit: p. 6, first paragraph |
| Exact \(^{129}\mathrm{Ba}\) run card | No row or sentence explicitly naming its core and numerical \(N_B\) was located in the paper or `v4.tex` | Missing run-level evidence |

The matched chains and the explicit \(135\to134\) example support \(A-1\), hence \(129\to128\). An \(A+1\) interpretation throughout the odd-Ba chain would require \(^{138}\mathrm{Ba}\), which is not in Table I. This is a text-based inference about the intended construction; it is not a recovered PBOS input.

Using the conventional core count, with proton particles above \(Z=50\) and neutron holes below \(N=82\), the two alternatives are:

| Core hypothesis | Proton-pair bookkeeping | Neutron-pair bookkeeping | Total \(N_B\) | Status |
|---|---:|---:|---:|---|
| \(^{128}\mathrm{Ba}\), \(Z=56,N=72\) | \((56-50)/2=3\) | \((82-72)/2=5\) | **8** | Conditional deduction for the paper-supported \(A-1\) core |
| \(^{130}\mathrm{Ba}\), \(Z=56,N=74\) | 3 | \((82-74)/2=4\) | **7** | Different \(A+1\) core choice, not established for this paper's \(^{129}\mathrm{Ba}\) run |

The proton/neutron split in this table is counting bookkeeping; the paper uses IBM-1, not separate proton and neutron boson degrees of freedom. Counting paired holes directly in the odd \(N=73\) nucleus after removing one odd hole also gives seven bosons, but that does not establish the paper's core mapping. Neither that arithmetic, the desired rotor answer, nor the occupation \(v_h^2=0.453\) can replace the core-definition evidence.

**Working choice for a future declared reconstruction:** \(^{128}\mathrm{Ba}\), \(N_B=8\), labeled as inferred from the stated core construction and conventional counting. **Exact-replay boundary:** request or recover the actual core/\(N_B\) run input before calling this the executed author setup.

**3. Printed Hamiltonian inputs.** The paper uses

\[
H=H_B+H_F+H_{BF},\qquad
H_B=\epsilon_d n_d+\kappa Q_B\cdot Q_B,
\]
\[
n_d=d^\dagger\cdot\widetilde d,\qquad
Q_B=s^\dagger\widetilde d+d^\dagger\widetilde s
       +\chi[d^\dagger\times\widetilde d]^{(2)}.
\]

Locator: p. 2, Eqs. (1)–(2) and adjacent definitions. No \(1/N_B\) rescaling or normal-ordering colons are printed on \(Q_B\cdot Q_B\). Substituting a normal-ordered two-body-only quadrupole interaction would change the operator unless its one-body terms were handled explicitly.

The Ba entries of Table I are:

| Core | \(\epsilon_d\) (MeV) | \(\kappa\) (MeV) | \(\chi\) |
|---|---:|---:|---:|
| \(^{128}\mathrm{Ba}\) | **0.03** | **−0.102** | **−0.18** |
| \(^{130}\mathrm{Ba}\) | 0.06 | −0.116 | −0.18 |
| \(^{132}\mathrm{Ba}\) | 0.13 | −0.122 | −0.18 |
| \(^{134}\mathrm{Ba}\) | 0.38 | −0.124 | −0.24 |
| \(^{136}\mathrm{Ba}\) | 1.15 | −0.122 | −0.85 |

These are mapped DD-PC1 RHB core-Hamiltonian parameters, not directly measured shape parameters and not the result of fitting the odd-Ba energy data. The mapping uses a finite-range separable pairing interaction. Locators: p. 2, final right-column paragraph through p. 3, opening paragraph; p. 3, Table I. The paper does not provide the full RHB mesh, convergence settings, mapping objective, or corresponding calculation files.

The negative-parity fermion space is **only \(1h_{11/2}\)**. The positive-parity space is \(3s_{1/2},2d_{3/2},2d_{5/2},1g_{7/2}\), which must not be imported into the negative-parity single-fermion block as additional active orbitals. Locator: p. 3, paragraph below Table I.

Table III's \(^{129}\mathrm{Ba}\) row gives, in this order,

\[
(v^2_{s_{1/2}},v^2_{d_{3/2}},v^2_{d_{5/2}},v^2_{g_{7/2}},v^2_{h_{11/2}})
=(0.597,0.708,0.938,0.974,\mathbf{0.453}).
\]

The \(0.453\) is an RHB occupation **probability**, not an amplitude \(v_h\), a measured spectroscopic factor, or a probability of the odd state having an \(h_{11/2}\) component. The authors obtain the canonical occupations at zero deformation, constrain the particle number to the desired odd number, and perform this step **without blocking**. Locator: p. 3, left-column paragraph starting with the fermion valence space; Table III. This is not a blocked, deformed odd-nucleus calculation.

The paper's Table II lists positive-parity single-particle energies only; it does not tabulate \(\epsilon_h\). In a strictly single-\(h_{11/2}\), fixed-\(N_F=1\) block, \(H_F\) contributes a common shift. Therefore the missing \(\epsilon_h\) does not by itself prevent a relative negative-parity spectrum or same-parity eigenvector calculation. It does prevent reconstructing an absolute or inter-parity offset without an additional convention. This is an audit deduction, not an extra author input.

**4. Coupling coefficients, signs, and normal ordering.** Table V, p. 4, prints the \(^{129}\mathrm{Ba}\) negative-parity row as:

| Printed parameter | Value (MeV) | Do not confuse with |
|---|---:|---|
| \(\Gamma_0^-\) | **+0.6** | The orbit-dependent \(\Gamma_{jj'}\) |
| \(\Lambda_0^-\) | **+2.1** | The signed tensor coefficient \(\Lambda_{jj'}^{j''}\) |
| \(A'_{11/2}\) | **−0.15** | The coefficient \(A_j\) multiplying a normalized scalar fermion tensor |

The printed Hamiltonian and coefficient definitions are:

\[
\begin{aligned}
H_{BF}={}&\sum_{jj'}\Gamma_{jj'}Q_B\cdot
             [a^\dagger_j\times\widetilde a_{j'}]^{(2)}\\
 &+\sum_{jj'j''}\Lambda_{jj'}^{j''}
 :\left[[d^\dagger\times\widetilde a_j]^{(j'')}
 \times[a^\dagger_{j'}\times\widetilde d]^{(j'')}\right]^{(0)}:\\
 &+\sum_j A_j[a^\dagger_j\times\widetilde a_j]^{(0)}n_d,
\end{aligned}
\]
\[
\Gamma_{jj'}=\Gamma_0\gamma_{jj'},\quad
\Lambda_{jj'}^{j''}=-2\Lambda_0
\sqrt{\frac{5}{2j''+1}}\beta_{jj''}\beta_{j'j''},\quad
A_j=-A_0\sqrt{2j+1},
\]
\[
\gamma_{jj'}=(u_ju_{j'}-v_jv_{j'})Q_{jj'},\qquad
\beta_{jj'}=(u_jv_{j'}+v_ju_{j'})Q_{jj'},\qquad
Q_{jj'}=\langle j\Vert Y^{(2)}\Vert j'\rangle.
\]

Locators: p. 2, Eqs. (3)–(6) and following paragraph; pp. 3–4, discussion of \(A_0\equiv A'_j\), and Table V. The creator index omitted in the printed monopole term has been restored above for readability; this does not change its intended single-orbit content.

For the negative-parity block \(h=11/2\), using the conventional real positive BCS amplitudes, simple input algebra gives:

\[
u_h^2=0.547,\qquad u_h^2-v_h^2=0.094,\qquad
2u_hv_h=2\sqrt{0.547\,0.453}.
\]
\[
\gamma_{hh}=0.094\,Q_{hh},\qquad
\Gamma_{hh}=0.0564\,Q_{hh}\ {\rm MeV},
\]
\[
\Lambda_{hh}^{h}
=-4.2\sqrt{5/12}
\left[2\sqrt{0.547\,0.453}\,Q_{hh}\right]^2\ {\rm MeV},
\qquad
A_h=+0.15\sqrt{12}\ {\rm MeV}.
\]

These are conditional algebraic reductions of printed inputs, not new fitted coefficients. The occupancy makes the quadrupole factor \(u_h^2-v_h^2\) small while leaving \(2u_hv_h\) near one; it does not determine a rigid-rotor pairing gap or Fermi energy.

The colon-enclosed exchange operator must retain fermion normal ordering. Reordering a fermion annihilator through a creator contributes the fermionic minus sign, and the normal-ordered product excludes the contraction. Thus \(+\Lambda_0\) is not a positive raw exchange-tensor coefficient, and the recoupled matrix elements cannot be assigned signs by reading Table V alone.

For an explicit conventional check, take
\(\widetilde a_{jm}=(-1)^{j-m}a_{j,-m}\) and standard Clebsch–Gordan tensors. Then

\[
[a^\dagger_j\times\widetilde a_j]^{(0)}_0
=-\frac{n_j}{\sqrt{2j+1}}
\quad\text{for half-integer }j,
\]

so Eqs. (3),(6) yield \(A_0\,n_jn_d\), namely \(-0.15\,n_d\) in this one-fermion block. The \(+0.15\sqrt{12}\) tensor coefficient and the \(-0.15\) number-operator coefficient are consistent. The paper does not explicitly define every tilde/reduced-matrix convention or provide the PBOS operator map, so this convention bridge must be declared and checked in a future implementation. No matrix construction has been performed here.

**5. Electromagnetic operators and calibration provenance.** The boson quadrupole operator used for transitions differs from the Hamiltonian quadrupole operator:

\[
T(E2)=T_B(E2)+T_F(E2),
\]
\[
T_B(E2)=e_B\left(s^\dagger\widetilde d+d^\dagger\widetilde s
             +\chi'[d^\dagger\times\widetilde d]^{(2)}\right),
\qquad \chi'=\mathbf{+0.35},
\]
\[
T_F(E2)=-\frac{e_F}{\sqrt5}
\sum_{jj'}\gamma_{jj'}[a^\dagger_j\times\widetilde a_{j'}]^{(2)}.
\]

Locator: p. 4, Eqs. (7)–(8), right column. Eq. (8) is labeled \(T(E2)\) in the PDF, but its surrounding prose identifies it as the fermion term; the \(F\) subscript above makes that role explicit. Preserve the minus sign and \(1/\sqrt5\).

For odd-neutron Ba, \(e_F=e_n=\mathbf{0.125\ e\,b}\). The corresponding proton value is \(e_p=0.250\ e\,b\). These carry quadrupole units because the printed single-particle \(Q_{jj'}\) is defined with the angular operator \(Y^{(2)}\); they are not dimensionless effective charges to be multiplied by a newly chosen radial \(r^2\) matrix element. In particular, \(e_n\) is not \(0.125e\) in a conventional radial shell-model operator.

The M1 prescription is

\[
T(M1)=\sqrt{\frac{3}{4\pi}}\left(g_B L+T_F(M1)\right),
\qquad
T_F(M1)=-\sum_{jj'}g_{jj'}
\sqrt{\frac{j(j+1)(2j+1)}3}
[a^\dagger_j\times\widetilde a_{j'}]^{(1)} ,
\]
\[
g_{jj'}=\begin{cases}
\big[(2j-1)g_l+g_s\big]/(2j),&j=j'=l+\tfrac12,\\
\big[(2j+3)g_l-g_s\big]/[2(j+1)],&j=j'=l-\tfrac12,\\
(g_l-g_s)\sqrt{\dfrac{2l(l+1)}
 {j(j+1)(2j+1)(2l+1)}},&j'=j-1,\ l=l'.
\end{cases}
\]

Locator: p. 5, Eqs. (9)–(11). For \(h_{11/2}\), \(l=5\), the applicable branch is \(j=l+1/2\); for a neutron \(g_l=0\), giving \(g_{hh}=0.7g_s^{\rm free}/11\). The authors quench free spin factors **by 30%**, i.e. retain 70%, not 30%. No factor \(u_h^2-v_h^2\) is printed in the M1 operator; imposing the E2 suppression factor on diagonal M1 would change the prescription.

| Parameter or component | Stated calibration / source | What remains absent from the printed input set |
|---|---|---|
| \(\epsilon_d,\kappa,\chi\) | RHB-to-IBM surface mapping with DD-PC1 and separable finite-range pairing; pp. 2–3 | Complete mapping/RHB job and numerical settings |
| \(v_h^2\) | Odd-number constrained spherical RHB without blocking; p. 3 and Table III | Full RHB job; needed only to regenerate this input rather than adopt it |
| \(\Gamma_0^-,\Lambda_0^-,A'_{11/2}\) | Adjusted separately for negative parity to a few lowest experimental levels of each odd nucleus; p. 3, lower left | Exact \(^{129}\mathrm{Ba}\) calibration-level list, weights, objective, residuals, parameter errors and correlations |
| \(e_B\) | Experimental \(B(E2;2_1^+\to0_1^+)\) in each chosen even-even core; p. 4 | Per-core \(e_B\), numerical adopted transition strength, evaluation vintage and sign convention for the charge |
| \(\chi'=+0.35\) | Experimental \(Q_s(2_1^+)\) of \(^{136}\mathrm{Ba}\); p. 4 | Numerical calibration datum and detailed fit; the fitted \(\chi'\) itself is supplied |
| \(e_p=0.250\ e\,b\) | Experimental \(Q_s(5/2_1^+)\) of \(^{137}\mathrm{La}\); p. 4 | Numerical calibration datum and uncertainty |
| \(e_n=0.125\ e\,b\) | Experimental \(Q_s(11/2_1^-)\) of \(^{137}\mathrm{Ba}\); p. 4 | Numerical calibration datum and uncertainty |
| \(g_B\) | Experimental core \(\mu(2_1^+)/2\); p. 5 | Per-core numerical magnetic moment and adopted \(g_B\); no printed fallback for a missing datum |
| Neutron \(g_l,g_s\) | \(g_l=0\); \(g_s=0.7g_s^{\rm free}\); p. 5 | No nucleus-specific M1 fit is stated |
| Experimental spectrum/comparison data | Broad NNDC reference [39], used in Figs. 3, 5–8 and comparison tables | Frozen evaluation, extraction list and covariance are not supplied |

Consequences for an independent calculation:

- Do not replace \(\chi'=+0.35\) by the core-Hamiltonian \(\chi=-0.18\).
- Do not replace \(g_B\) by \(Z/A\) and describe it as the paper's input.
- Choosing the wrong core also selects the wrong \(e_B\) and \(g_B\) calibration nucleus.
- An E2 ratio does not automatically remove the missing \(e_B\): boson and fermion amplitudes add, so their relative scale and interference matter.
- The paper does not specify a radiative E2/M1 mixing-ratio sign convention or provide a \(^{129}\mathrm{Ba}\) \(\delta\) table. A future conversion from reduced matrix elements to a signed \(\delta\) requires an explicit convention bridge.
- The PDF literally prints \(\mu_N^2\) beside proton \(g_l\) and magnetic-moment table headings. This is retained as a units/typography issue to resolve in a code comparison; it is not used to assign squared-moment units to an M1 amplitude.

The Hamiltonian's printed \(H_F=\sum_j\epsilon_j[a^\dagger_j\times\widetilde a_j]^{(0)}\) also does not spell out the normalization bridge from scalar tensors to orbital-number operators. This is important in a multi-\(j\) reconstruction. In the present fixed single-\(j\) block it remains a common energy-shift convention.

**6. What is actually predicted for \(^{129}\mathrm{Ba}\).**

| Published object | Relevant coverage | Classification |
|---|---|---|
| Fig. 5(c), p. 7 | \(N=73\) member of negative-parity Ba chain, with lowest plotted \(7/2^-,9/2^-,11/2^-,13/2^-,15/2^-,17/2^-\) levels | Graphical model spectrum; couplings were adjusted using low-energy data, so not an untouched energy prediction |
| Fig. 5(d), p. 7 | Corresponding experimental comparison | Imported experimental levels, not new data |
| Fig. 14(a,c), p. 11 | \(N=73\) \(^{129}\mathrm{Ba}\), including the \(11/2_1^-\) curve | Model E2-derived \(\beta_{\rm eff},\gamma_{\rm eff}\), not directly measured shapes |
| Fig. 13, p. 10 | Even-core \(0_1^+\) shape invariants | Even-even-core result, not the odd-Ba \(11/2^-\) result |
| Fig. 9 and Table VI, pp. 8–9 | \(^{135}\mathrm{Ba}\) | Not \(^{129}\mathrm{Ba}\) |
| Fig. 10 and Table VII, p. 9 | \(^{129}\mathrm{Xe}\) | Same mass number, different nucleus |
| Figs. 11–12 and Tables VIII–IX, pp. 9–10 | \(^{133}\mathrm{La}\) and \(^{131}\mathrm{Cs}\) | Other selected examples |

The selection of four detailed examples is explicit on p. 8, Sec. III C. Neither the 13-page paper nor its public source package provides a transition-resolved numerical \(^{129}\mathrm{Ba}\) \(B(E2)\), \(B(M1)\), \(Q_s\), \(\mu\), lifetime, or signed-\(\delta\) table. In particular, there is no printed prediction for the 365-keV \(13/2^-\to11/2^-\) link, its alternative 461-keV E2 branch, or the proposed 521/671-keV band links. No new number for those transitions has been inferred here.

The shape-invariant construction has a specific scope: pp. 11, Eqs. (12)–(15), take \(J'=J+2\) and retain the lowest **five** \(J'\) states in the sums. For \(11/2_1^-\), the specified intermediate spin is \(15/2^-\). The paper uses the absolute value in its \(q_3\) definition. These conventions and finite truncation must be reproduced if Fig. 14 is used as a benchmark; replacing them by another invariant prescription is a new analysis. Neither \(q_2,q_3\) nor \(\gamma_{\rm eff}\) identifies the individual E2/M1 transition amplitudes needed for the wobbling/TiP/signature comparison, or measures a \(\gamma\)-stiffness.

**7. PBOS and public input availability.** On p. 4, lower left, the authors state that they diagonalize in the spherical basis \(\lvert j,L,\alpha,J\rangle\), with \(\alpha=(n_d,\nu,n_\Delta)\), using **PBOS**. Reference [34] on p. 13 identifies T. Otsuka and N. Yoshida (1985), but prints only `JAERI-M ... Report No. 85`; the bibliography source `v4.bbl` is equally incomplete. No program version, input deck, source checksum, build instructions, truncation switches, or test output is supplied.

The actual public arXiv v2 source archive was inspected. It contains **19 regular members: 16 figure PDFs, `v4.tex`, `v4.bbl`, and `v4.synctex`**. All 16 PDFs report zero embedded files. This package contains no standalone PBOS code, nuclear run input, matrix-element table, occupation-generation job, or output log. TeX and SyncTeX are publication material, not the numerical implementation. The archive SHA-256 is:

```text
f7ed6dc746f50f16169d8796e4d12becd8827eaf4ac2ee4d5f1ff9cd04690faf
```

A bounded public search considered a candidate NPBOS manual at JAEA, `JAERI-M-85-094`. The terminal request returned an HTML access challenge rather than PDF bytes; the alternative INIS URL returned 404. OSTI searches returned no verified target implementation in the inspected results. Thus this audit has **not established the exact relationship between that NPBOS manual and the author's PBOS executable**, has not read the manual, and has not acquired the calculation code. This is an access/identity boundary, not proof that the code is unavailable everywhere or that the authors cannot supply it.

The code gap does not make independent diagonalization mathematically impossible. Once a core/\(N_B\), tensor convention, boson space and EM inputs are declared, the published Hamiltonian can be reconstructed independently. What is unavailable is an exact, fully specified author replay and transition-by-transition \(^{129}\mathrm{Ba}\) benchmark.

**8. Readiness judgment and the smallest remaining input request.**

| Intended use | Judgment | Remaining condition |
|---|---|---|
| Explain a soft-core alternative to a rigid paired rotor | **Supported at the model-framework level** | Keep IBM/IBFM dynamics, RHB inputs and empirical coupling fit distinct |
| Use the printed negative-parity input values | **Supported** | Preserve parameter role, signs and the \(\chi/\chi'\) distinction |
| Independently reconstruct a relative \(^{129}\mathrm{Ba}\) negative-parity spectrum | **Conditionally feasible; not executed** | Declare the inferred \(^{128}\mathrm{Ba}\), \(N_B=8\) choice, full/selected boson space and operator conventions; verify against a benchmark |
| Claim exact reproduction of Nomura et al.'s numerical run | **Not established** | Author core/\(N_B\) input, actual PBOS setup and reference numerical outputs |
| Predict absolute or relative \(^{129}\mathrm{Ba}\) electromagnetic observables using the exact published setup | **Input-incomplete** | Per-core \(e_B,g_B\), their calibration data and conventions; state identification and EM matrix elements |
| Treat 365-keV \(\delta\) or a wobbling/TiP classification as a published prediction of this paper | **Unsupported** | Such transition-specific results are not printed |
| Call the comparison a clean held-out test | **Requires a new declared design** | Recover which \(^{129}\mathrm{Ba}\) energies calibrated the couplings; freeze new EM targets before further tuning |

The smallest useful missing package is: (i) the \(^{129}\mathrm{Ba}\) core and \(N_B\) run line; (ii) the chosen U(5) basis/truncation and PBOS tensor/input convention; (iii) numerical \(e_B\) and \(g_B\) with the adopted core \(B(E2;2_1^+\to0_1^+)\) and \(\mu(2_1^+)\); (iv) the low-energy states used to set the three negative-parity couplings; and (v) a few reference eigenvalues and signed reduced E2/M1 matrix elements with explicit initial/final state labels.

Adopting the printed occupation \(0.453\) does not require refitting a rotor BCS gap. Regenerating that occupation from DD-PC1 would be a separate RHB reproduction project. Also, the absent \(\epsilon_h\) should not be made a false blocker for relative single-\(j\) spectra.

**9. Traceability and task boundary.** Primary-page images and extracted text are confined to [the permitted temporary directory](/workspace/wiki/tmp/ba129-controlled-pairing/ibfm-input-review). Key verification objects are:

- [Original p. 2: Hamiltonian and tensor coefficients](/workspace/wiki/tmp/ba129-controlled-pairing/ibfm-input-review/local-pdf-page-02.png).
- [Original p. 3: Tables I–III and RHB occupation procedure](/workspace/wiki/tmp/ba129-controlled-pairing/ibfm-input-review/local-pdf-page-03.png).
- [Original p. 4: Table V, E2 calibration and PBOS statement](/workspace/wiki/tmp/ba129-controlled-pairing/ibfm-input-review/local-pdf-page-04.png).
- [Original p. 5: M1 prescription and omitted \(^{128}\mathrm{Ba}\) PES](/workspace/wiki/tmp/ba129-controlled-pairing/ibfm-input-review/local-pdf-page-05.png).
- [Original p. 8: explicit \(^{135}\mathrm{Ba}\to{}^{134}\mathrm{Ba}\) core example](/workspace/wiki/tmp/ba129-controlled-pairing/ibfm-input-review/local-pdf-page-08.png).
- [Original p. 11: Fig. 14 and restricted invariant sums](/workspace/wiki/tmp/ba129-controlled-pairing/ibfm-input-review/local-pdf-page-11.png).
- [Public manuscript source, including dynamic date](/workspace/wiki/tmp/ba129-controlled-pairing/ibfm-input-review/arxiv-v2-v4.tex:32).
- [Public-source member audit](/workspace/wiki/tmp/ba129-controlled-pairing/ibfm-input-review/arxiv-v2-member-audit.json).
- [Publisher-deposited bibliographic metadata](/workspace/wiki/tmp/ba129-controlled-pairing/ibfm-input-review/crossref-nomura2017.json).

The source page, protected PDF, `PLAN.md`, get-paper files, other session outputs, handoff and knowledge pages were not edited. No Git commands, model implementation, PBOS execution, scientific fit, code build, or publication action was performed. Notes are confined to the user-authorized output directory; this report does not claim new raw archival or knowledge-layer ingestion.
