# Observable candidates from the calibrated parent calculation

These are **conditional predictions of the declared model family**, read from `shape-closure-v1/study.json` with eF=0.125 and calibrated core charges. They are not experimental determinations, a claim of source-figure reproduction, or a demonstration that the required measurements are feasible. The parent's static-moment benchmark is pending.

The useful experimental question is whether diagonal and angular-channel strengths evolve differently from a common charge scale. It can be asked without first assigning an intrinsic gamma.

For the selected state \(i\) with \(J=11/2\), define upward-normalized strengths
\[
S_+=\sum_\nu B(E2;i\to (J+2)_\nu),\qquad
S_0^{\rm inel}=\sum_{\nu\ne i}B(E2;i\to J_\nu),
\]
and the diagonal contribution
\[
D_0=\frac{|\langle iJ\Vert T(E2)\Vert iJ\rangle|^2}{2J+1}.
\]
The diagonal term is not a zero-energy gamma decay. With the standard spectroscopic-moment convention,
\[
D_0=\frac{5}{16\pi}
\frac{Q_s(J)^2}{|\langle JJ;20|JJ\rangle|^2},
\qquad
|\langle JJ;20|JJ\rangle|^2=\frac{J(2J-1)}{(J+1)(2J+3)}
=\frac{55}{91}\quad(J=11/2).
\]
This relation was arithmetic-checked against the parent JSON. It is standard angular-momentum algebra, not a new method.

Useful dimensionless quantities are
\[
R_{\rm stat}=\frac{D_0}{S_+},\qquad
R_{\rm inel}=\frac{S_0^{\rm inel}}{S_+},\qquad
R_{\rm same}=R_{\rm stat}+R_{\rm inel}.
\]
A common rescaling of the whole E2 tensor cancels from these ratios. Their variation therefore cannot be explained by that rescaling alone. It does not by itself establish constant total q2 or uniquely identify particle-core recoupling: changes in the relative boson/fermion operator or other structural mixing must also be considered.

| Odd Ba A | Model \(Q_s\), eb | \(R_{\rm stat}\) | \(R_{\rm inel}\) | \(R_{\rm same}\) |
|---:|---:|---:|---:|---:|
| 129 | −0.16348 | 0.00990 | 0.24763 | 0.25753 |
| 131 | +0.14234 | 0.00953 | 0.27523 | 0.28476 |
| 133 | +0.94260 | 0.63454 | 0.38463 | 1.01917 |
| 135 | +1.17693 | 1.68250 | 0.18679 | 1.86930 |
| 137 | +0.77296 | 0.95557 | 0.40910 | 1.36467 |

All denominators in this table include every J+2 state in the declared finite model. The physically important prediction is **diagonal dominance of the 135Ba same-spin channel**, not an enhancement of its inelastic same-spin sum. Its static contribution is 0.227971 e2b2 and its inelastic same-spin contribution only 0.025309 e2b2. The static share is 90.007%. Therefore a proposal to seek enhanced same-spin gamma transitions alone would miss the model's main effect.

**A smaller, directly specified candidate** uses one identified crossover:
\[
R_{\rm stat}^{(1)}
=\frac{D_0}{B(E2;i\to (J+2)_1)}.
\]
The parent model gives 0.01057, 0.01020, 0.71402, 2.27221 and 1.35653 for A=129,131,133,135,137, respectively. A measured \(Q_s\), including its separately reported sign, and the absolute E2 strength of the corresponding transition would test this ratio. The model's state ordinal and excitation energy are not automatic experimental level assignments.

If the measured transition is the reverse decay, use
\[
B(E2;11/2\to15/2)=\frac{16}{12}B(E2;15/2\to11/2).
\]
For equal-spin transitions the two directions have equal B(E2). Conversion corrections, E2 branching fractions, E2/M1 separation where relevant, and absolute normalization must accompany the matrix elements. Relative gamma intensities alone do not supply these strengths.

This two-observable candidate is useful as a **matrix-element benchmark**, without a gamma inversion. It is analogous in spirit to few-element tests such as Lawrie–Orce2025, but their even-even rotational-2+ conversion curve is not being applied to 11/2. \(R_{\rm stat}^{(1)}\) is not the complete-channel \(R_{\rm stat}\): omitted positive denominator strength makes the former an upper bound on the latter for the same D0. The first crossover carries only about 74% of the complete J+2 strength in the 135Ba model, so the distinction is numerically material.

**What a fuller network would add.** Measuring additional same-spin and J+2 transitions permits comparison of \(R_{\rm inel}\), \(R_{\rm same}\), and energy-window versions of these observables. Always calculate the identical window and state subset in the model. Do not normalize by an incompletely measured total and call the result a complete strength fraction. In the parent 129Ba model, the two displayed excited same-spin states contain only about 41% of the inelastic same-spin channel, despite the strong saturation of the five-state J+2 sum. Experimental incompleteness can therefore differ greatly between numerator and denominator.

To distinguish **total charge collectivity** from redistribution experimentally, one additionally needs measured or credibly bounded strength in the other allowed spin channels, including the diagonal contribution. Positive measured subsets bound q2 from below, but do not prove saturation. A ratio change alone demonstrates a change in the measured relative matrix-element pattern; it does not establish that full q2 is unchanged.

**Signed cubic cancellation needs more information.** The full q3 requires signs of closed-loop matrix-element products, including elements between intermediate states. In 135Ba the model's largest ordered spin sectors include positive (11/2,11/2) and (11/2,13/2) terms and negative (15/2,15/2), (11/2,15/2) and (11/2,7/2) terms. Their sum is small after cancellation. Neither a static moment nor a collection of unsigned B(E2) values determines those mixed loops. State-resolved loop ranking should precede any claim that a small measured network can test this cancellation; spin-sector sums alone do not identify a sufficient experimental set.

Multistep excitation/interference information or another justified source of relative loop signs would be required, together with quantified missing-path sensitivity. A lifetime-only campaign could test important quadratic ratios while remaining unable to reconstruct q3. The large cancellation factor is also not a causal or uncertainty measure by itself: the parent factor is about 24.93 in 129Ba and 21.69 in 135Ba, while only the latter has the reported conversion-domain failure.

**Decision before an experimental proposal.** First reconcile the odd-state static-moment benchmark, particularly the flagged 137Ba value, with verified state, sign, units and calibration provenance. Then map the selected modeled states to actual levels and inventory existing lifetimes, branching/mixing information, quadrupole moments and population possibilities. This sidecar has not done that inventory and makes no beamtime, precision or feasibility claim. A mismatch in the static sector would challenge the model pattern underlying these predictions even if all closure checks pass.

Exact numbers, fractions and input hashes are retained in [calibrated-observable-candidates.csv](calibrated-observable-candidates.csv) and [calibrated-observable-checks.json](calibrated-observable-checks.json). The new build script performs stored-number arithmetic only and was run once; it does not run the parent's model or Huygens' controls.
