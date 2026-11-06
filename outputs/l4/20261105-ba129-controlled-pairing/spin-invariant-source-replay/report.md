**Nomura 2017 invariant source replay and version audit**

Review date: **2026-11-06**. The existing November 5 run directory is retained. Actual retrieval/run timestamps are recorded separately as observed UTC; some fall on November 5. No timestamp was synthesized from the directory name.

**Finding.** The declared \(^{128}\mathrm{Ba}/N_B=8\) reconstruction reproduces the previously checked low-energy source subset, but its electromagnetic shape invariants do **not** reproduce the inspected arXiv figures. The decisive comparison is already present for the even core: Fig. 13(b) gives \(\gamma_{\rm eff}=8.975^\circ\), whereas the printed \(J'=J+2,n=5\) prescription applied to the frozen physical E2 operator gives \(29.496^\circ\). Finite-spin closure cannot explain this \(J=0\) mismatch.

The v1/v2 comparison supplies no reconciliation: the relevant E2 definitions, \(\chi'=+0.35\), charge-calibration text and invariant equations are identical, and the numerical drawing geometry of both invariant figures is unchanged. The remaining result is an unresolved correspondence between the declared reconstruction and the original electromagnetic/invariant calculation. This audit does not establish which producer-level difference causes it, or that the authors calculated the figures incorrectly.

**Evidence and claim boundaries.** Source-figure values below are **author model results extracted from original vector graphics**, not measured deformations. The source statements about calibration and implementation are **author method descriptions**. Literal numerical replay, unit conversion, charge decomposition and comparison are **this audit's calculations** with the frozen local kernel. The complete-scalar and alternative-operator diagnostics are explicitly attributed to the **parent probe**. There is no new experimental result in this audit.

The source-calibration JSON was frozen before reading numerical probe/case values. The parent had supplied approximate expectations, so the exercise was not blind; independence means that axes and marker anchors were determined solely from the source, without changing them to match a model. Its immutable SHA-256 is:

```text
source-invariants-frozen.json
4987fa80589b6a278edba95865665d4f7ec5bf742eb1feaeec46eb2f7d6aaf5b
```

**Source points and literal comparison.** These are the \(N=72\) black-circle core points and \(N=73\) olive down-triangle \(11/2_1^-\) points. The exact figure files are members of the held arXiv-v2 source archive. Figure locators refer to the held arXiv-v2 manuscript: Fig. 13(a,b), PDF p. 10; Fig. 14(a,c), PDF p. 11.

| State | Source \(\beta_{\rm eff}\) | Declared literal \(\beta_{\rm eff}\) | Source \(\gamma_{\rm eff}\) | Declared literal \(\gamma_{\rm eff}\) | Literal minus source \(\gamma\) |
|---|---:|---:|---:|---:|---:|
| \(^{128}\mathrm{Ba}\), \(0_1^+\) | 0.23725 | 0.25802 | 8.975° | 29.496° | +20.521° |
| \(^{129}\mathrm{Ba}\), \(11/2_1^-\) | 0.52080 | 0.56633 | 23.110° | 29.257° | +6.147° |

The additional core source points are:

| Core | Neutron number | Source \(\beta_{\rm eff}\) | Source \(\gamma_{\rm eff}\) |
|---|---:|---:|---:|
| \(^{130}\mathrm{Ba}\) | 74 | 0.21364 | 11.942° |
| \(^{132}\mathrm{Ba}\) | 76 | 0.18511 | 15.524° |
| \(^{134}\mathrm{Ba}\) | 78 | 0.16330 | 17.826° |
| \(^{136}\mathrm{Ba}\) | 80 | 0.10755 | 13.698° |

No isotope beyond the declared \(128/8\) case was numerically reconstructed here.

**Vector method and precision.** Coordinates are PDF points, top-left origin, \(y\) increasing downward. Labeled vector tick segments define each linear axis. Intermediate ticks verify it. The neutron-number ticks identify the selected isotope independently.

| Panel | Value as a function of vector \(y\) |
|---|---|
| Fig. 13(a), core beta | \(0.315524979874-0.00215624994653y\) |
| Fig. 13(b), core gamma in degrees | \(63.6525042468-0.215625027761y\) |
| Fig. 14(a), odd beta | \(0.659999956343-0.00357638871835y\) |
| Fig. 14(c), odd gamma in degrees | \(64.7999991269-0.178819452182y\) |

Circles use their Bezier-segment symmetry center. For these particular down-triangle symbols, the graph anchor is the midpoint of the tip/base extrema, verified against the connecting-curve vertex; their polygon centroid is not used as the data coordinate. The \(^{129}\mathrm{Ba}\) beta/gamma anchors are respectively \((63.3992595673,38.9219360352)\) and \((63.3992595673,233.1415863037)\). Their disagreement with independently transformed curve vertices is \(1.91\times10^{-6}\) PDF point.

Across all selected points, the maximum marker/curve distance is \(3.412\times10^{-5}\) point. The maximum unused-tick residual is \(5.46\times10^{-8}\) for beta and \(3.84\times10^{-6}\) degree for gamma. These are numerical geometry checks, **not source error bars**. The displayed five beta decimals and three gamma decimals are reporting precision; the original numerical plotting tables and rounding rule remain unavailable.

The source JSON preserves the initial failed fixed-tolerance check and its replacement by a coordinate-resolution guard before model values were read. It also preserves the incomplete serialization attempt as a separate file. Neither incident changed an axis or marker position.

**What the source defines.** The archived v2 manuscript is `v4.tex`; the v1 manuscript is `v2.tex`. These internal filenames do not label arXiv versions. The following locators refer directly to their line numbers:

| Definition | v1 `v2.tex` lines | v2 `v4.tex` lines |
|---|---|---|
| Total E2 decomposition | 537–538 | 552–553 |
| Boson E2, Eq. (7) | 540–542 | 555–557 |
| Fermion E2, Eq. (8) | 544–552 | 559–567 |
| Charges and \(\chi'\) calibration | 555–565 | 570–580 |
| E2 matrix-element description | 1225–1232 | 1258–1265 |
| \(q_2\), Eq. (12) | 1234–1236 | 1267–1269 |
| \(q_3\), Eq. (13) | 1238–1243 | 1271–1276 |
| \(J'=J+2\), lowest \(n=5\) | 1244–1249 | 1277–1282 |
| \(\beta,\gamma\), Eqs. (14)–(15) | 1272–1278 | 1305–1311 |

In the Hamiltonian, the explicitly defined tensor is \(Q_B(\chi)\), with \(\chi_H=-0.18\) for the declared core. The explicitly defined electromagnetic tensor is

\[
T(E2)=e_B Q_B(\chi')
-\frac{e_F}{\sqrt5}(1-2v^2)Q_{hh}
[a_h^\dagger\times\widetilde a_h]^{(2)}
\]

in the present single-\(j\) restriction. The source fixes \(\chi'=+0.35\) from the \(^{136}\mathrm{Ba}\) first-\(2^+\) spectroscopic quadrupole moment. It determines each core's \(e_B\) from its measured \(B(E2;2_1^+\to0_1^+)\), and quotes \(e_n=0.125\,eb\) from the \(^{137}\mathrm{Ba}\) \(11/2_1^-\) moment; the proton calibration uses \(^{137}\mathrm{La}\). The numerical \(e_B\) values and a producer transition-matrix table are not supplied in these source packages. These are calibration prescriptions, not evidence that the authors used the exact adopted strength in the frozen local contract.

Section III D says that the invariants use **E2 matrix elements**, which supports the physical-E2 interpretation. However, its generic \(\hat Q\) is not explicitly equated to \(T(E2)\), \(T(E2)/e_B\), or \(Q_B(\chi_H)\), and the archive contains no invariant-evaluation code or producer RME/units dictionary. Thus the source supports the E2 reading most directly; it does not positively establish a different tensor as the explanation.

Both versions also label the fermion expression in Eq. (8) as \(T(E2)\) without a subscript \(F\), although the surrounding sentences identify it as the fermion contribution. That notation omission does not itself specify an alternative invariant tensor. A commented generic \(Q\) RME in the TeX is not a printed definition of \(\hat Q\) in Eqs. (12)–(15).

**Literal replay and normalization.** The frozen case uses \(e_B=0.13268018236134518\,eb\), \(e_F=0.125\,eb\), \(e_F/e_B=0.9421150753288176\), \(\chi'=+0.35\), \(v^2=0.453\), and \(Q_{hh}=-\sqrt{525/(143\pi)}\). Its core, Hamiltonian and boson-fermion couplings are unchanged.

The audit obtains standard reduced matrix elements directly from the same fixed-\(M\) eigenvectors using

\[
\langle J_f M|T_{20}|J_i M\rangle
=\frac{(J_iM\,20|J_fM)}{\sqrt{2J_f+1}}
\langle J_f\Vert T_2\Vert J_i\rangle .
\]

Only the lowest five states of \(J'=J+2\) enter the literal comparison. Equation (12) is evaluated without inserting an extra \(1/(2J+1)\). Equation (13) takes the absolute value **after** summing the coherent triple products. Since \(J'-J=2\), the Hermitian reverse-RME phase is positive; the closed chain is evaluated as \(u^\dagger M u\). State rephasing cancels around this chain.

| Literal quantity | Core \(J=0\) | Odd \(J=11/2\) |
|---|---:|---:|
| \(q_2\), \(e^2b^2\) | 1.591636730250284 | 5.312822486431527 |
| \(q_3\), \(e^3b^3\) | 0.052950926722168 | 0.476129554826055 |
| \(q_3/q_2^{3/2}\) | 0.026369848586 | 0.038880978156 |
| Argument implied by source gamma and Eq. (15) | 0.891594800229 | 0.352997324526 |
| Eq. (14) spin factor \(G_J=[(2J'+1)\langle J',J;2,0\mid J,J\rangle^2]^{-1}\) | 1 | 35/24 |

For beta, the calculation strips the elementary-charge unit from E2 RMEs, uses \(1\,b=100\,\mathrm{fm}^2\), \(Z=56\), and \(R_0=1.2A^{1/3}\,\mathrm{fm}\), with each isotope's own \(A\). The declared absolute betas exceed the graph points by 8.7545% and 8.7423%, respectively. No charge was inferred from these residuals.

For the core, including **all 15 \(J=2\) intermediate states** changes gamma only from \(29.4963146^\circ\) to \(29.5061337^\circ\). Thus the printed five-state truncation is not responsible for the approximately \(20.5^\circ\) discrepancy in this reconstruction. The parent full-scalar folded core result is also \(29.5061337^\circ\). The odd full-scalar value \(29.8945007^\circ\) remains a parent diagnostic, not a substitute for the printed restricted prescription or an independently rederived finite-spin closure result.

For any common real tensor rescaling \(T\to cT\), \(q_2\to c^2q_2\) and \(q_3\to|c|^3q_3\). Therefore an unknown common charge, a common unit conversion, or a global tensor sign cannot repair the core gamma mismatch. This argument does not rule out an undocumented state-dependent RME convention or another producer-level difference.

The parent's other checks are retained as attributed diagnostics: \(Q_H\) with \(\chi_H=-0.18\) gives \(21.888^\circ\); changing the EM \(\chi'\) sign gives \(19.271^\circ\); one intermediate state with the printed \(\chi'\) gives \(15.692^\circ\). None matches the source core point. Taking the absolute value of each triple term separately at \(\chi'=+0.35\) instead gives an arccos argument \(1.14083749>1\). That altered prescription has no real angle here and differs from the printed coherent sum. No such alternative was fitted or adopted.

**Odd/core beta ratio.** The graph ratio is

\[
\frac{\beta_{\rm odd}}{\beta_{\rm core}}=2.195152958,
\]

while the declared literal-E2 ratio is \(2.194905957\), a relative difference of \(-0.0112521\%\). This is a close conditional comparison of the printed beta prescription, including its spin and radius factors. It is not independent certification of an intrinsic deformation ratio or the original E2 implementation.

Even assuming the odd system uses its core's \(e_B\), fixed nonzero \(e_F\) prevents exact cancellation of an otherwise unknown boson charge:

\[
q_{2,o}=e_B^2 C_B+2e_Be_F C_X+e_F^2 C_F,\qquad
q_{2,c}=e_B^2 C_c.
\]

At the frozen case,

\[
C_B=301.7471562756,\quad C_X=0.02574139466,\quad
C_F=0.00015442514.
\]

The odd \(q_2\) terms are \(5.311966230304\), \(0.000853843234\), and \(0.000002412893\), respectively. The net interference-plus-fermion contribution is **0.0161168% of \(q_2\)**. It is small here, but it is retained and proves the ratio is not exactly independent of \(e_F/e_B\). Simultaneously scaling both charges with their ratio fixed would cancel; leaving \(e_F=0.125\,eb\) fixed while the source's \(e_B\) is unreported is a different operation. No charge scan was performed.

**Version and publication boundary.** The archived arXiv record dates v1 to **2017-04-24 09:13:22 UTC** and v2 to **2017-07-08 04:43:46 UTC**. Publisher-deposited Crossref metadata give **2017-07-07** for PRC **96**, 014304, DOI `10.1103/PhysRevC.96.014304`.

Both TeX manuscripts contain `\date{\today}`. The retrieved v1 PDF says September 10, 2022; the held v2 PDF says November 21, 2021. Their PDF creation metadata match those dates. These are regenerated PDF identities, not new 2022/2021 papers.

Nine relevant equation/parameter blocks compare byte-for-byte equal. Both invariant figures have exactly equal `get_drawings()` geometry in PyMuPDF 1.28.2. Their PDF bytes differ, and their extracted text changes the gamma unit label from `(deg.)` to `(deg)`; figure metadata also differ. The two energy-figure members, `even.level.pdf` and `ba.level.pdf`, are byte-identical. Other manuscript edits, including an exchange-index correction and an M1 prefactor correction, are recorded separately; the exchange-index change has no effect when all indices are the same single \(j\).

The original APS article request returned an archived HTTP 403 challenge. The version-of-record full text was **not compared**. Therefore this audit establishes identity/differences between the exact archived preprint versions and the held regenerated preprint PDF. Journal DOI and date metadata alone do not establish equality with the final publisher text or figures.

**Allowed endpoint.** The earlier independently checked energy subset remains: five core levels within 0.365 keV and six lowest odd negative-parity levels within 0.721 keV of the source plot values. The extended case's nonyrast residuals and experimental energy RMS are unchanged. Those source-energy agreements do not certify the original eigenvectors or electromagnetic implementation, and the present mismatch does not invalidate that limited spectrum comparison.

The defensible description is **a declared single-\(j\) reconstruction with partial source-energy replay and unresolved electromagnetic/invariant source correspondence**. Further discrimination would require the original invariant code/input deck or an author matrix-element dump specifying \(\hat Q\), charges, RME convention and intermediate-state list. No conclusion about the correctness of the original figures follows from this audit alone. Planck's finite-\(J\) derivation and pure-angular counterexamples remain separate.

**Execution and artifacts.** The unchanged kernel was run with one BLAS thread. Direct literal replay and the fixed-charge decomposition took **0.477 s** internally; source-version comparison took **0.435 s**. This task did not rerun or claim the earlier 25-test suite. Frozen source/probe/case/kernel hashes were checked before and after numerical replay; closeout records the final hash and archive-gate checks.

The scripts use exclusive output creation to protect frozen results. Publisher text, manuscript diffs and rendered pages are confined to the authorized temporary directory; originals and metadata are in the authorized raw archive. All new analysis artifacts are in this audit directory. No engine, case, knowledge, PLAN or get-paper file was edited, and no Git operation, package installation or parameter adjustment was performed.

Relevant artifacts:

- [Frozen source coordinates and axes](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-source-replay/source-invariants-frozen.json)
- [Literal comparison and charge decomposition](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-source-replay/literal-comparison.json)
- [Source-version comparison and exact locators](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-source-replay/version-comparison.json)
- [New-originals archive manifest](/workspace/wiki/raw/papers/gpt/query/20261106-nomura-invariant-version-audit/manifest.json)
- [Earlier case/source energy audit](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/ibfm-case-review/report.md)
- [Held-v2 p. 11 rendering: formulas and odd figure](/workspace/wiki/tmp/ba129-spin-invariant-source-replay/nomura-v2-p11.png)
- [Held-v2 p. 4 rendering: E2 definitions](/workspace/wiki/tmp/ba129-spin-invariant-source-replay/nomura-v2-p4.png)
- [Source-only extraction script](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-source-replay/extract_source_invariants.py)
- [Literal replay script](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-source-replay/compare_literal.py)
- [Version audit script](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-source-replay/audit_versions.py)
