**Bounded recheck of the MF1–MF3 revisions, 6 November 2026**

**Verdict.** The requested substantive revisions are correctly incorporated. I find no new substantive algebraic, normalization, sign, or numerical error in these changes. The earlier assessment of a credible, conditional EPJA controlled-model contribution is preserved. One small relative-change denominator clarification remains; it is nonblocking.

This assessment is pinned to:

| Inspected input | SHA-256 |
|---|---|
| `raw/writing/gpt/odd-ba-quadrupole-closure/main.tex`, 259 lines | `99ae9d4bfeffe14c4d72801369b69cf7ff18d6657dcd0dbfc398a259ab36a7dd` |
| `raw/writing/gpt/odd-ba-quadrupole-closure/controls.tex`, 78 lines | `9d572f8b643eee9494ccf582ed92424b584525726debad418a99b4d5761cea90` |
| `raw/writing/gpt/odd-ba-quadrupole-closure/references.bib` | `676e468cb0f6c571e96757c1a73dc54ffb8c0cec854dc3dc981b425519a53013` |
| `raw/writing/gpt/odd-ba-quadrupole-closure/data/results/calibrated-chain.json` | `45d3aafb4d02b2bf54620c4fd4356178c814a2a4b1eb5b6d15caa4132985ca0a` |

Only the specified manuscript changes, their immediate context, stored-number arithmetic, and relevant convention passages from the existing algebra/input reviews were checked. Nomura2017's official arXiv text, Eqs. (3)–(6), was also inspected for the interaction comparison. The Lawrie–Orce citation and scope were compared with the existing focused precedent review; a fresh publisher full-text verification was not obtained. No workflow documents, model producers, test suites or pending supplemental calculations were inspected or run.

**Revision findings**

| Revision | Result and evidence |
|---|---|
| Spectator baseline and added value | **Closed.** [Main line 121](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:121) correctly gives \(f_{J+2}=4/15\) in the stated core-only \(R=0\otimes j\) limit. [Line 191](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:191) identifies the added value as the fixed-operator Hamiltonian intervention, static/inelastic partition and signed-path response. It does not present the invariant algebra or channel dependence as new. |
| Contrary precedent | **Closed.** [Main line 189](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:189) acknowledges the useful, regime-dependent reduced-observable approach of Lawrie–Orce2025. It does not transfer their even-even conversion directly to the mixed odd-A state. The BibTeX key is present. |
| Rotor amplitude and units | **Closed.** [Main line 123](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:123) now distinguishes the tensor amplitude \(\mathcal Q\) from conventional electric \(Q_0\). The equations \(q_2=\mathcal Q^2,\ q_3=\mathcal Q^3\) and \(\mathcal Q=\sqrt{5/(16\pi)}Q_0\) are consistent. |
| RME phases, operator order and interaction | **Closed at the definition level.** [Main line 92](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:92) states the correct Hermitian reciprocity for the declared Wigner–Eckart convention. [Appendix line 224](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:224) specifies the quadrupole, normal-ordered exchange and monopole terms with consistent tilde and scalar-product definitions. The existing \((-1)^{2J}\) cubic phase remains appropriate. This is a source/convention comparison, not a new certification of executable implementation. |
| Table 2 and cubic convergence | **Numerically consistent; one wording clarification below.** Every displayed \(c_5,f_5,r,z_5,z_\infty\) entry agrees with the stored primary results at the printed precision. The maximum \(|z_5-z_\infty|\) is \(0.00920720754\), supporting the stated bound \(<0.0093\). The new common-denominator cubic contributions also sum to the stated signed ratio at their display precision. |
| Static-to-first-transition ratio | **Closed.** [Main line 195](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:195) correctly defines \(R_{\rm stat}^{(1)}\), identifies the diagonal term and reverse transition, distinguishes first-state and complete-channel denominators, and retains the empirical-data qualification. |

The monopole reduction deserves an explicit confirmation. For the declared half-integer single-\(j\), one-fermion space,
\[
F^{(0)}=-\frac{1}{\sqrt{2j+1}},
\qquad
-A_0\sqrt{2j+1}\,n_dF^{(0)}=A_0n_d.
\]
The appendix has neither introduced an extra sign nor counted the monopole term twice.

For the new observable, the stored results reproduce
\[
D_0=\frac{5}{16\pi}\frac{Q_s^2}{55/91}
    =\frac{91}{176\pi}Q_s^2,
\qquad
B(E2;11/2\to15/2)=\frac43B(E2;15/2\to11/2).
\]
Readback arithmetic gives \(R_{\rm stat}^{(1)}=2.2722073553\) for \(^{135}\)Ba and \(1.3565277480\) for \(^{137}\)Ba, matching 2.2722 and 1.3565. The first \(^{135}\)Ba \(15/2\) state carries \(0.74047147\) of the calculated complete \(15/2\) channel, so the approximately 74% statement is correct. These are checks of stored model outputs, not empirical ratio determinations.

**Only residual clarification**

[Main line 145](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:145) reports a 10.7% relative change for \(^{129}\)Ba without naming the denominator. The stored values give
\[
100\frac{|z_5-z_\infty|}{|z_\infty|}
=10.6514\%,\qquad
100\frac{|z_5-z_\infty|}{|z_5|}
=9.6261\%.
\]
The current number is correct as a deviation relative to the all-state reference. The minimum wording change is “a 10.7% deviation relative to \(z_\infty\).” No table, result or inference needs to change.

**Scope retained**

The manuscript continues to disclose operator dependence, static-moment overprediction and the finite-model boundary. Its observable ratio is labeled a prediction and does not substitute a theoretical denominator for experimental evidence. The pending \(Q_s\)-matched path and empirical E2 availability assessment therefore remain qualifications on any later empirical extension, not newly discovered errors in these revisions.

This closes the requested MF1–MF3 recheck apart from the nonblocking denominator clarification. Only this new addendum was written; earlier reviews, manuscript/model files and other work were unchanged. No tests, fit, compilation or commit were performed.
