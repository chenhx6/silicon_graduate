**Conditional moment-calibrated E2 operators with unchanged Hamiltonians**

**Result:** each of the five distinct central \(^{136}\)Ba moment targets has one finite real solution with positive \(e_B\) and positive fitted \(e_F\), when conditioned on the same \(B_\uparrow(^{136}\mathrm{Ba})=0.407\,e^2b^2\) and \(Q_s(^{137}\mathrm{Ba},11/2)=+0.78\,e\,b\). Four of the five alternatives reduce the absolute \(^{135}\)Ba moment discrepancy relative to the primary; the \(+0.25\,e\,b\) core target worsens it. The \(+0.01\) and \(+0.02\,e\,b\) alternatives place the withheld \(^{135}\)Ba prediction inside both quoted \(0.08\,e\,b\) margins. These are conditional validation results; no branch is chosen on that basis.

The full-versus-selected distinction persists, but the location of angle-domain failure changes. In particular, the \(+0.01\) and \(+0.02\,e\,b\) targets that bring \(Q_s(135)\) inside the quoted margins give full signed ratios **−1.093167111 and −1.096209270**. Their full formal angles are undefined. Agreement with a static moment therefore does not make a complete-moment angle automatically physical. All raw ratios are preserved, and undefined angles remain null.

The [contract](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-calibrated-operator/calibrated-operator-contract.json) was frozen at **2026-11-06 04:43:36 UTC**, before matrix coefficients were computed at **04:47:09 UTC**. Calibration and prediction were separate driver stages. No \(^{135}\)Ba state, moment, or proxy was evaluated in the calibration stage. The frozen contract hash is:
`5d49a9ceda150dea250e80eceb1389fdc6b96f6af4307ca2c6c8c2aabb75b6ff`.

**Source alternatives and dependence**

The [static-moment source page](/workspace/wiki/knowledge/sources/nndc-ba135-ba137-static-e2-constraints.md:80) was checked against the following local raw records:

- [\(^{136}\)Ba adopted, lines 58–61](/workspace/wiki/raw/papers/gpt/query/20261106-ba-core-E2-calibration/nndc136-adopted-text.ens:58): outside parentheses denotes constructive interference, inside parentheses destructive interference.
- [\(^{136}\)Ba Coulomb, lines 47–58](/workspace/wiki/raw/papers/gpt/query/20261106-ba-core-E2-calibration/nndc136-coulomb-text.ens:47): adopted \(B_\uparrow\), its components/alternatives, and the moment branches.
- [\(^{137}\)Ba adopted, line 64](/workspace/wiki/raw/papers/gpt/query/20261106-ba-spin-moment-benchmark/nndc137-adopted-text.ens:64): \(Q_s=+0.78(9)\,e\,b\), used here only at its central value as a calibration target.
- [\(^{135}\)Ba adopted, line 111](/workspace/wiki/raw/papers/gpt/query/20261106-ba-spin-moment-benchmark/nndc135-adopted-text.ens:111): withheld \(Q_s=+0.96(8)\,e\,b\). The source page also records N17 Table VI's \(+0.98(8)\,e\,b\); that presentation is retained separately, not averaged with the adopted value.

| Study group | Constructive \(Q_s(136)\), \(e\,b\) | Destructive \(Q_s(136)\), \(e\,b\) | Listed \(B_\uparrow\) information not propagated in this pass |
|---|---:|---:|---|
| 1986BaZJ / 1986Ro15 | −0.19(6) | +0.07(7) | 0.419(4), with 0.417(4) in parentheses |
| 1984Be20 | +0.01(5) | +0.25(5) | 0.399(3); a paired destructive value is not established here |
| 1972Ke16 | −0.19(17) | +0.02(18) | 0.418(11), with 0.417(12) in parentheses |

The repeated \(-0.19\) central value is one mathematical target carrying two provenance entries. It is not two independent measurements with the same complete error contract, and it receives no extra weight. Likewise, constructive/destructive solutions of one study are alternatives, not independent observations.

Every row below pairs its moment target with the same averaged \(B_\uparrow=0.407\), as requested. Moment and strength can covary through the interference solution, and some branch pairings or their covariance are unavailable. **These are conditional calibration scenarios, not a joint fit to independent moment and transition-strength data.** The listed strength alternatives were not substituted or scanned after seeing the holdout. Quoted errors were not converted into a posterior, confidence distribution, or branch probability.

**Analytic calibration, without a \(\chi_E\) search interval**

Both Hamiltonians, both lowest \(11/2\) states, and the relevant core \(0_1^+\) and \(2_1^+\) states remain fixed. In the shared real eigenvector convention, define

\[
T_{136}(\chi)=
\langle2_1^+\Vert Q_{\chi}\Vert0_1^+\rangle=a+b\chi,
\quad
S_{136}(\chi)=Q_s(2_1^+;e_B=1)=c+d\chi.
\]

The computed coefficients are

\[
\begin{aligned}
a&=5.216368397358274,&b&=-0.3961256291332322,\\
c&=-2.953662075250356,&d&=1.543201485941058.
\end{aligned}
\]

With \(g=\sqrt{0.407}\), the imposed positive charge is
\[
e_{B,136}=\frac{g}{|a+b\chi|}.
\]
For a core moment target \(t\) and an absolute-value sign branch
\(s=\operatorname{sign}(a+b\chi)\),
\[
(gd-tsb)\chi=tsa-gc,\qquad
\boxed{\chi_s=\frac{tsa-gc}{gd-tsb}}.
\]
Each candidate must satisfy \(s(a+b\chi_s)>0\), have a nonzero strength-calibration denominator, and reproduce the original unsquared equation
\(g(c+d\chi_s)/|a+b\chi_s|=t\).

The analytic sign \(s\) is the transition-RME sign in this fixed solver convention. It is not the experimental constructive/destructive interference label. Rephasing the core states can exchange the analytic sign labels without changing the calibrated physical operator.

All ten sign-equation candidates were recorded in [linear-calibration.json](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-calibrated-operator/linear-calibration.json). Five satisfy the original equation, all with \(s=+1\). The other five fail their required absolute-value sign condition and are not additional roots.

The pole is at \(\chi=-a/b=13.1684698331\); no finite \(e_B\) can reproduce a positive \(B_\uparrow\) there. The monotonicity on each side follows from
\[
\frac{d}{d\chi}\frac{g(c+d\chi)}{|a+b\chi|}
=\frac{g\,s(ad-bc)}{(a+b\chi)^2},
\qquad ad-bc=6.8798862142>0.
\]
The left interval covers moment values \((-2.4853462143,\infty)\), and the right interval \((2.4853462143,\infty)\). All five targets are below \(2.4853462143\), so there is exactly one root for each on the left interval and none on the right. This establishes completeness over the real line without imposing a “physical” bound on \(\chi_E\).

For the odd \(^{137}\)Ba calibration state,
\[
Q_s(137)=e_{B,136}(u+v\chi)+w e_F,
\]
\[
u=5.846171402301101,\quad
v=-0.9041620907204937,\quad
w=0.625674318063584.
\]
Therefore
\[
\boxed{e_F=\frac{0.78-e_{B,136}(u+v\chi)}{w}}.
\]
The fermion response is nonzero and no degeneracy occurs. \(e_{B,137}\) is the same \(^{136}\)Ba core calibration, not a second freely fitted parameter.

All roots are well separated from the \(^{136}\)Ba pole and from the \(^{134}\)Ba core pole at \(\chi=12.7924502442\). No singular or numerically ambiguous calibration was encountered.

**All finite solutions and the withheld moment**

The \(^{135}\)Ba charge is recalibrated positively to the unchanged \(^{134}\)Ba input \(B_\uparrow=0.679\,e^2b^2\), using the same \(\chi_E\) and fitted \(e_F\). No \(^{135}\)Ba moment or proxy enters any calibration equation.

| Core target \(t\), \(e\,b\) | \(\chi_E\) | \(e_{B,136}=e_{B,137}\), \(e\,b\) | \(e_{B,135}\), \(e\,b\) | \(e_F\), \(e\,b\) | Predicted \(Q_s(135)\), \(e\,b\) |
|---:|---:|---:|---:|---:|---:|
| −0.19 | 0.982379997 | 0.132159957 | 0.136794897 | 0.199398913 | 1.088518973 |
| +0.07 | 2.222283748 | 0.147130068 | 0.152841239 | 0.344398895 | 0.873491777 |
| +0.01 | 1.959085335 | 0.143675427 | 0.149127936 | 0.310937361 | 0.923289727 |
| +0.25 | 2.942599694 | 0.157493991 | 0.164018463 | 0.444783498 | 0.723459387 |
| +0.02 | 2.003827193 | 0.144251200 | 0.149746389 | 0.316514283 | 0.914997435 |

Every listed branch has \(e_F>0\), so an additional positive-effective-charge requirement would exclude none. No finite real \(\chi_E\) root has been discarded. Four solutions have \(\chi_E>\sqrt7/2\); that does **not** automatically forbid them. A customary range for the Hamiltonian parameter \(\chi_H\) is not a universal bound on the independently specified E2-operator parameter \(\chi_E\). Both Hamiltonians and their \(\chi_H\) values remain unchanged. No source-prescribed admissible interval for \(\chi_E\) has been established in this audit; the printed \((0.35,0.125)\) is a reference point, not an interval or an admissibility theorem. The calibrated values differ from that reference and do not certify reproduction of the source authors' run.

The primary reference gives \(Q_s(135)=1.176930291\,e\,b\), with residuals \(+0.216930291\) against \(0.96\) and \(+0.196930291\) against \(0.98\).

| Core target | Residual to adopted \(0.96\) | Residual to paper \(0.98\) | Absolute discrepancy versus primary |
|---:|---:|---:|---|
| −0.19 | +0.128518973 | +0.108518973 | Reduced against both; outside both quoted margins |
| +0.07 | −0.086508223 | −0.106508223 | Reduced against both; outside both quoted margins |
| +0.01 | −0.036710273 | −0.056710273 | Reduced against both; inside both quoted margins |
| +0.25 | −0.236540613 | −0.256540613 | Increased against both; outside both quoted margins |
| +0.02 | −0.045002565 | −0.065002565 | Reduced against both; inside both quoted margins |

Residuals have units \(e\,b\). “Inside a quoted margin” is a descriptive comparison, not a significance test, posterior probability, or complete model-error assessment. The two \(^{135}\)Ba reference presentations have related provenance and are not counted as independent validations. The \(^{135}\)Ba and \(^{137}\)Ba moment evaluations also share source keys; computationally withholding \(^{135}\)Ba does not establish statistical independence of their experimental errors.

No branch is preferred or eliminated using this table. Selecting the \(+0.01\) or \(+0.02\) branch because it agrees with \(^{135}\)Ba would consume that holdout as selection information and would require a further independent test.

**Full scalar moments and selected-channel proxies**

The table retains signed \(q_3\) and signed full \(c=q_3/q_2^{3/2}\). The proxy arguments are the literal absolute-chain ratios, for the lowest five or all \(J'=15/2\) multiplets. “All” here means all states at that spin, not complete angular closure. \(q_2\) is in \(e^2b^2\), \(q_3\) in \(e^3b^3\); arguments are dimensionless.

| Odd Ba | Core target | Full \(q_2\) | Full signed \(q_3\) | Full signed \(c\) | Proxy \(c_{n=5}\) | Proxy \(c_{\rm all\,15/2}\) |
|---:|---|---:|---:|---:|---:|---:|
| 135 | primary | 0.676622790 | −0.028118636 | −0.050521277 | 1.026114565 | 1.024144143 |
| 135 | −0.19 | 0.739757601 | −0.408699130 | −0.642346790 | 1.038580675 | 1.029637979 |
| 135 | +0.07 | 1.131610828 | −1.314787527 | −1.092219520 | 0.816808476 | 0.791879265 |
| 135 | +0.01 | 1.009781795 | −1.109245976 | −1.093167111 | 0.871444103 | 0.849642601 |
| 135 | +0.25 | 1.611546333 | −1.881193605 | −0.919537192 | 0.672778493 | 0.640471845 |
| 135 | +0.02 | 1.028770528 | −1.143855702 | −1.096209270 | 0.862185842 | 0.839837071 |
| 137 | primary | 0.476765595 | −0.021958680 | −0.066703538 | 0.729020038 | 0.738227245 |
| 137 | −0.19 | 0.528077848 | −0.214786247 | −0.559705461 | 0.922812337 | 0.928010627 |
| 137 | +0.07 | 0.743527994 | −0.743639492 | −1.159889076 | 0.992978413 | 0.984511857 |
| 137 | +0.01 | 0.681182454 | −0.612560862 | −1.089567312 | 1.000266059 | 0.994840321 |
| 137 | +0.25 | 0.976019207 | −1.162396767 | −1.205498979 | 0.941393245 | 0.925114567 |
| 137 | +0.02 | 0.691047283 | −0.634069523 | −1.103761479 | 0.999630435 | 0.993684648 |

The full folded angle is \(\arccos|c|/3\) only where \(|c|\le1\); the signed angle is retained separately. Any ratio outside the real arccos domain remains raw, with a null angle. There is no clipping.

Three observations matter:

- The \(-0.19\) calibration retains the \(^{135}\)Ba proxy-domain excess, while its full moment ratio remains inside the domain. The full folded angle is \(16.677654^\circ\), and both selected proxy angles are undefined.
- The \(+0.01\) and \(+0.02\) calibrations improve the withheld moment, yet give full ratios below \(-1\) in both odd nuclei. Their selected proxies are generally in-domain. At \(^{135}\)Ba the all-\(15/2\) proxy angles are \(10.609061^\circ\) and \(10.959027^\circ\), while the full formal angles are undefined. Thus better agreement with a static moment does not force agreement between these observables or validate a rigid-shape angle.
- For \(^{137}\)Ba with the \(+0.01\) core target, \(n=5\) gives \(1.000266059\) but all \(15/2\) states give \(0.994840321\). This particular proxy-domain excess is removed by completing the spectral sum within the selected spin; the all-state proxy angle is \(1.940951^\circ\). The full ratio remains \(-1.089567312\). Spectral cutoff and omitted angular channels remain distinct issues.

The outside-domain full ratios are not numerical failures or grounds to reject otherwise finite algebraic calibration solutions. Quantum effective quadrupole operators and magnitude fluctuations do not impose an unconditional classical cosine bound. The full moments and spin-selected proxy contractions are rotational scalars with different operator content. None of the formal angles establishes physical gamma rigidity, softness, or a mode assignment.

**Verification and remaining boundary**

Both stages used the same fixed \(^{137}\)Ba state/Hamiltonian hashes; each prediction reused its isotope's eigenvectors for every calibrated operator. Direct all-component moments and complete reduced \(6j\) closure agree within \(9.43\times10^{-14}\,e^2b^2\) for \(q_2\) and \(1.46\times10^{-13}\,e^3b^3\) for signed \(q_3\). Moment-calibration residuals are below \(7\times10^{-16}\,e\,b\); \(B_\uparrow\) replay residuals are below \(3\times10^{-16}\,e^2b^2\). These digits characterize numerical replay, not experimental precision.

The [driver](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-calibrated-operator/driver.py), [branch enumeration](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-calibrated-operator/linear-calibration.json), [compact predictions](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-calibrated-operator/predictions.csv), and [structured prediction results](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-calibrated-operator/predictions.json) preserve all finite branches and both primary references. Separate calibration/prediction run records verify one thread in both loaded BLAS libraries, contract timing, and unchanged input/module hashes. No full state-pair JSON is emitted. [REPLAY.md](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-calibrated-operator/REPLAY.md) distinguishes the small computational dependency set from the original driver's additional provenance-verification dependencies.

A subsequent documentation-only hash check found that the current static-moment source page differs from its frozen historical hash. The six computational files, eight other provenance dependencies, and recorded numerical artifacts still match. [replay-files.json](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-calibrated-operator/replay-files.json) records both required and observed hashes, without changing the original contract or run records. The completed calculation is preserved; an unmodified strict replay from current paths requires the historical source-page bytes. A reduced verifier would need a separately identified adapter, which has not been implemented or tested here.

This closes the central conditional calculation for \(^{135,137}\)Ba. The other three isotopes were not needed to answer the prescribed calibration/holdout question. Branch-consistent \(B(E2)\)–moment pairs, their covariance, uncertainties in the model inputs, and the source authors' actual calibration choices remain unresolved. They could change the calibrated parameters and the interpretation of holdout agreement. No energy refit, source-operator reproduction claim, uncertainty posterior, change to pre-existing input/module files, or commit was made.
