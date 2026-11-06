**Independent manuscript review, 6 November 2026**

**Verdict — credible focused EPJA model-study contribution; targeted scientific revisions remain.** The calibrated chain and the completed operator and coupling controls support substantially more than a comparison of two definitions. The strongest result is a controlled redistribution of static and transition strength at fixed initial spin, with little change in total quadratic strength, and an explicit explanation of the signed cubic network. The latest abstract and conclusions now center that result and acknowledge the imperfect static benchmark. I find no demonstrated fatal algebraic or headline numerical error. The remaining must-fix items concern the exact novelty claim, its observable consequence, and a few consequential definitions and reporting details. Empirical validation of the full odd-Ba network remains incomplete.

This is one independent assessment, informed by the requested earlier algebra and Noether reviews, not a mutually blind panel or a claim of reviewer consensus. I read the manuscript, its populated operator-control insert, stored calibrated results, the focused precedent comparison, and the now-available coupling/path and static-moment sidecars. I inspected stored numbers and performed simple readback arithmetic only. I did not import or run model producers, run tests, compile the manuscript, edit it, or judge the parent's PDF build. Input fingerprints and the exact read boundary are in [input-receipt.json](input-receipt.json). Administrative placeholders are outside the scientific verdict.

The source changed during the review. This report incorporates the refreshed 189-line `main.tex`, SHA-256 `8d72b717753b7bf31480d236893909bd6053afe9dd4b13dbabec89c8ada22e6a`, and the populated 78-line `controls.tex`, SHA-256 `9d572f8b643eee9494ccf582ed92424b584525726debad418a99b4d5761cea90`. The new coupling-path and static-moment sections close earlier presentation gaps. They are not listed as missing work below.

**What is already established**

The manuscript's RME convention and complete \(q_2,q_3\) expressions agree with the supplied [independent algebra review](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-algebra/report.md:25). In particular, the factor \((-1)^{2J}\) in the cubic expression must remain under that convention. It is not a sign error. The \(e_F\) coefficient has quadrupole units, the angular \(Q_{jj}\) needs no additional radial factor, and the upward/downward core-strength factor of five is consistent with the stated transition directions. The restricted quantity is a legitimate scalar; its distinction from complete closure is correctly maintained.

The following primary values were read from `calibrated-chain.json`, using `cases[odd_A].primary.full` and the `restricted` entries with `max_states=5` and `null`. Here the isotope selector is descriptive; the file stores `cases` as a list.

| Odd Ba | \(q_2\), \(e^2b^2\) | \(r\) | \(100c_5\) | \(100f_5\) | \(z_5\) | \(z_\infty\) |
|---|---:|---:|---:|---:|---:|---:|
| 129 | 1.531871 | +0.005524 | 99.6177 | 28.9016 | 0.038881 | 0.035138 |
| 131 | 1.263918 | −0.070047 | 99.5889 | 27.5600 | 0.129367 | 0.133389 |
| 133 | 0.946369 | −0.144654 | 99.8434 | 24.3128 | 0.632159 | 0.636864 |
| 135 | 0.676623 | −0.050521 | 99.8539 | 19.9960 | 1.026115 | 1.024144 |
| 137 | 0.476766 | −0.066704 | 99.6232 | 21.5026 | 0.729020 | 0.738227 |

The manuscript's headline percentages, endpoint \(q_2\) ratio \(0.3112308\), static fractions, and recorded closure residuals agree with these artifacts. The unrounded cubic sector sum is \(0.2908557020-0.3189743380=-0.0281186360\ e^3b^3\). The apparent last-digit discrepancy when subtracting the rounded prose values is rounding, not an arithmetic failure.

The [35-setting operator control](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-operator-control/report.md:54) supplies an important negative result. Alternative \(\chi'\) values remove the \(^{135}\)Ba arccos violation and reverse several cubic signs/trends while leaving channel saturation distinct from full coverage. This result is retained in [controls.tex](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/controls.tex:48) and now qualified in the abstract. It should survive all further revisions.

**MF-1 — Make the precise advance over existing channel-sensitive diagnostics explicit. Required for the originality case.**

Affected claims are the abstract, Introduction closing paragraph, and Conclusions in [main.tex](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:13).

The \(99.5\%\)-versus-\(20\)–\(29\%\) contrast is correct but cannot carry the novelty alone. For the core-only \(R=0\otimes j\) spectator control, the complete \(J+2\) fraction is already
\[
f_{J+2}=\frac{2j+5}{5(2j+1)}=\frac4{15}
\quad(j=11/2).
\]
Thus roughly a quarter of total strength in this channel is expected even without the interacting mechanism. The relevant new information is the departure from such coupling limits, the diagonal/inelastic partition, and the signed loop response. This follows directly from the existing algebra review's spectator result, not from a new computation here.

The focused [contrary-precedent comparison](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-precedent-review/focused-sidecar/comparison.md:13) makes the priority boundary concrete. Nomura2016 already interprets channel-dependent odd-A indicators through coupling. Rouoof2025 already compares restricted and larger microscopic E2 networks. Lawrie–Orce2025 shows why a reduced diagnostic can remain useful within a stated regime. Neither a new implementation nor a large difference between angle definitions establishes a new general method.

The revised manuscript now supports the narrower statement:

> In this fixed-spin IBFM family, a quadrupole-coupling intervention strongly redistributes static strength and signed E2 paths while changing total quadratic strength only modestly. Completing a selected spin channel does not recover that information. Operator alternatives preserve this separation but alter the cubic sign, angle trend and conversion domain.

**Minimum change.** Add one short comparison paragraph that identifies the new result as a fixed-operator Hamiltonian intervention, resolved into static/inelastic and signed-loop contributions, with a separately checkable matrix-element consequence. Nomura2016 and Rouoof2025 are already cited; make the difference explicit rather than implying that restricted-versus-complete comparison itself is new. Include or acknowledge the Lawrie–Orce regime counterexample if arguing for a general diagnostic prescription. No additional broad search, new closure theorem, or source-figure correction is required. The fixed-\(J\) spectator fraction would be a useful compact baseline.

**The updated coupling mechanism is supported within its stated scope**

The [coupling report](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-coupling-control/report.md:91) is now the strongest physics evidence, but its original endpoint warning must be read together with the supplemental [Gamma-path results](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-coupling-control/gamma-path.json).

With the core, operator, exchange and monopole terms fixed, changing \(\Gamma_0\) from zero to its primary value gives:

| \(\Gamma_0/0.6\) | \(q_2\), \(e^2b^2\) | \(z_\infty\) | Static fraction of \(q_2\) |
|---|---:|---:|---:|
| 0 | 0.680126 | 0.087945 | 0.0000913 |
| 0.25 | 0.691797 | 0.357592 | 0.038911 |
| 0.50 | 0.694132 | 0.664207 | 0.155551 |
| 0.75 | 0.686595 | 0.890756 | 0.267015 |
| 1 | 0.676623 | 1.024144 | 0.336925 |

The recorded adjacent maximum-overlap matches stay at the lowest same-\(J\) ordinal in both directions; the minimum adjacent squared overlap is about \(0.9073\), and the smallest sampled gap is \(0.4813\) MeV. This supports sampled continuous reconfiguration. It resolves the endpoint-only ambiguity sufficiently for a bounded model claim; it is not proof of absence of every unsampled crossing.

The \(+0.5178\%\) change in \(q_2\) is the **removal endpoint relative to the primary**, not the largest excursion along the path. The path's \(q_2\) span is about \(2.6\%\) of the primary value. Neither nearly equal endpoint \(q_2\) nor nearly equal \(\langle n_d\rangle\) proves an unchanged intrinsic shape.

The refreshed [coupling subsection](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/controls.tex:3) now includes the path, overlap/gap qualification, full \(q_2\) span and calculated changes in selected \(S\), signed \(C\), and its middle-diagonal/off-diagonal contributions. This closes the original endpoint-only causal objection. The seven-operator scan and the \(\Gamma\) path remain separate designs; they do not demonstrate the same causal response for every alternate operator. The current bounded wording is adequate if that separation is retained.

Keep the roles of \(A_0\) and exchange distinct. In this single-fermion space \(A_0n_d\) changes the odd-system \(n_d\) coefficient even when the bare even-core Hamiltonian is fixed. Single-term removals do not define additive causal percentages. Large cubic cancellation is also not sufficient to identify the anomaly: the focused review notes an even larger cancellation factor in \(^{129}\)Ba.

The updated abstract has also removed the earlier ambiguous statement that all Hamiltonian parameters were held fixed. No new coupling scan is requested by this review.

**MF-2 — Complete the observable bridge beyond the now-disclosed static benchmark. Required for the paper's practical nuclear-structure contribution.**

The relevant manuscript paragraph is [main.tex line 175](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:175). The [static-moment benchmark](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-moment-benchmark/report.md:12) and the new [manuscript subsection](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/controls.tex:54) already make the empirical limit concrete:

- \(^{135}\)Ba gives model \(Q_s=+1.17693\ eb\), versus the source-paper experimental entry \(+0.98(8)\ eb\) and the separately archived adopted value \(+0.96(8)\ eb\). Retain the two source versions separately. The overprediction matters for a mechanism dominated by the diagonal term; it does not invalidate the closure identities. A discrepancy divided only by an experimental quoted margin is not a model-rejection significance.
- \(^{137}\)Ba gives \(+0.77296\ eb\), consistent with the archived \(+0.78(9)\ eb\) entry. However, that state was the source's neutron effective-charge calibration target. Likewise, \(\chi'\) was set using a \(^{136}\)Ba core static moment. These are calibration-consistency checks, not two independent electromagnetic validations.
- The core calibration-state alternatives and the source's electromagnetic replay discrepancy remain relevant to operator selection. Selecting the alternate \(\chi'\) merely because it removes \(z>1\) would not resolve them.

The fitting lineage is also documented in the existing [input review](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/ibfm-input-review/report.md:201). Reusing published couplings does not make their original calibration energies independent predictions.

**Minimum change.** Retain the new signed-\(Q_s\) comparison and add a falsifiable quadratic ratio that does not require measuring the full cubic network. The focused [observable sidecar](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-precedent-review/focused-sidecar/observables.md:44) provides
\[
R_{\rm stat}^{(1)}
=\frac{D_0}{B(E2;11/2_1^-\to15/2_1^-)},
\qquad
D_0=\frac5{16\pi}\frac{Q_s^2}{55/91}.
\]
The stored model predictions are \(2.27221\) and \(1.35653\) for \(^{135,137}\)Ba. They are predictions until the actual state identities and absolute transition strengths are established. For a measured reverse decay, use \(B_\uparrow=(16/12)B_\downarrow\).

Do not call this the all-\(15/2\) ratio \(R_{\rm stat}\). The first \(^{135}\)Ba crossover carries about \(74\%\) of that model channel, so the distinction is material. Match the experimental subset in the calculation. The isomer's parity-changing M4 lifetime cannot supply an E2 denominator. An empirical numerator plus a theoretical denominator is a hybrid comparison, not a measured ratio.

A complete new experimental E2 network is not a prerequisite for a bounded theory paper. The necessary revision is to confront the available static evidence, state the remaining transition gap, and limit claims about actual odd-Ba structure accordingly. Unsigned strengths and a static moment would still not validate signed cubic loops.

**MF-3 — Fix the remaining definition and reporting ambiguities. Required, localized corrections.**

1. **Rotor normalization.** [Main line 115](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:115) states \(q_2=Q_0^2,\ q_3=Q_0^3\) without defining \(Q_0\). This is correct if \(Q_0\) means the intrinsic component of the tensor used in the algebra control. For the conventional electric intrinsic quadrupole moment, \(T_{20}^{\rm body}=\sqrt{5/(16\pi)}Q_0\), and the corresponding powers of \(5/(16\pi)\) are required. Define a separate tensor amplitude or print that mapping. This changes the dimensional interpretation, not the validated normalized rotor angle.
2. **Phase and full interaction.** Preserve the displayed half-integer phase. Add \(R_{ab}=(-1)^{J_a-J_b}R_{ba}^{*}\), the ordered tensor-product convention, and the explicit restricted single-\(j\) boson–fermion Hamiltonian in a short appendix. The main text currently supplies coefficients and a source reference rather than the complete exchange contraction whose removal now supports the mechanism.
3. **Cubic convergence precision.** The primary \(^{129}\)Ba \(z_5\to z_\infty\) change is about \(10.65\%\) relative, although the angle shift is only \(0.0715^\circ\). Report raw \(z_\infty\) values or \(\Delta z\) alongside the maximum angle shift. “Nearly the same” should be tied to absolute changes and the physical comparison, not inferred from \(99.5\%\) quadratic saturation. The \(^{135}\)Ba domain result is unchanged by this correction.
4. **Uncertainty interpretation.** Keep the 35 calculations labeled deterministic one-factor scenarios. They are neither 35 independent confirmations nor a joint confidence envelope. The alternative-\(\chi'\) tests establish operator dependence, not an empirical preference for those operators. Numerical closure to \(10^{-13}\) and many printed digits do not imply comparable physical accuracy.

**Useful optional additions**

- A small plot of \(z_\infty\), static fraction and \(q_2/q_{2,\rm primary}\) along the existing \(\Gamma\) path would communicate the mechanism more directly than another isotope-angle plot. It requires no new scan.
- Show the selected \((15/2,15/2)\) and remaining-spin contributions on the same complete-\(q_2^{3/2}\) denominator. The current primary values are \(-0.1146727+0.0641514=-0.0505213\). This prevents the reader from comparing the differently normalized positive \(z\) and signed \(r\) as if they were the same estimator.
- For a later empirical extension, rank a few state-resolved signed loops and apply the same experimentally available matrix-element mask to the model. A broader model survey, expanded isotope chain, exact source-figure replay, or new beamtime proposal is not needed to complete the present bounded manuscript.

**Likely decisive EPJA objections and the smallest adequate response**

“Is this just the known difference between two scalar definitions?” Answer with the fixed-\(J\), fixed-operator coupling path and its static/network redistribution, while acknowledging the closest precedents.

“Why should the \(^{135}\)Ba feature be physical if changing \(\chi'\) removes it?” Separate the robust information-content result from the operator-conditional angle/domain result; do not choose the operator by the desired anomaly.

“What validates the odd-state wavefunction and tensor?” Show the imperfect \(^{135}\)Ba static comparison, the calibration status of \(^{137}\)Ba, and the precisely defined transition-ratio target. Algebraic closure alone cannot answer this question.

The refreshed manuscript has already integrated the decisive coupling and static-moment evidence with appropriately narrower claims. My recommendation is to finish the exact precedent comparison, add the specified observable consequence, and make the localized convention/reporting corrections. This is a defensible incremental controlled-model contribution for an EPJA referee to assess, not an acceptance forecast. The evidence does not support a unique empirical shape mechanism or a general replacement for established effective quadrupole diagnostics.
