**Current scientific verdict, 6 November 2026**

**A defensible focused EPJA controlled-model paper, with targeted revisions.** Missing causal and operator controls are no longer grounds to block this manuscript. The updated abstract states the conditional mechanism, the operator dependence and the \(^{135}\)Ba static-moment overprediction. The remaining empirical question is whether the diagnostic separation survives where the model matches that static constraint. The new \(Q_s\)-conditioned calculation addresses this specific question; it is not needed to establish the already demonstrated intervention result.

This addendum assesses `main.tex` SHA-256 `945361b49dadc03bf85ebadfc8fd8e9cb60dae60d5a1c2ac80e0046ae2616fe1` and `controls.tex` SHA-256 `9d572f8b643eee9494ccf582ed92424b584525726debad418a99b4d5761cea90`. I made one bounded read of the current sources and available readiness artifacts. I did not wait for, fit, interpolate, or assume results from the newly assigned \(Q_s\)-matching calculation.

**Issues closed or substantially resolved**

- The [Gamma-only intervention](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/controls.tex:3) now supports a conditional dynamical explanation, with sampled state continuity and explicit numerator/denominator changes. It goes beyond a correlation between two output diagnostics.
- The [operator study](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/controls.tex:48) retains contrary outcomes. The disappearance of the domain violation and changes of cubic sign/trend are reported, so the paper does not require an operator-independent \(z>1\) anomaly.
- The [static benchmark](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/controls.tex:54) distinguishes calibration consistency from additional EM evidence and discloses the unfavorable \(^{135}\)Ba comparison.
- The abstract/conclusion now center the controlled mechanism, and the discussion includes Lawrie–Orce2025 as a regime-dependent reduced-observable precedent. The exact advance is a quantitative fixed-\(J\) intervention and matrix-element decomposition in the declared odd-Ba family. This is a plausible incremental physics contribution, not a new invariant formalism or a correction of published figures.

**Current must-fix items**

**1. Keep the empirical claim at the level the available transitions permit.**

Galileo's available [Rstat-readiness artifact](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-moment-benchmark/rstat-readiness.json) already reports a substantive negative result within its bounded source check:

| Nucleus | What the inspected records support | Remaining boundary |
|---|---|---|
| \(^{135}\)Ba | A tentative \(15/2^-\) candidate and a corresponding decay to \(11/2^-\) | No established parent half-life or absolute E2 denominator; assignment, conversion and decay accounting require closure |
| \(^{137}\)Ba | The known \(11/2^-\) static calibration anchor | No assigned matching \(15/2\) level in the two checked datasets and no established absolute E2 denominator |

Both empirical ratios remain null in that artifact. This is not evidence that the measurements do not exist anywhere. It is sufficient to prevent calling the proposed \(^{135,137}\)Ba ratio comparison an achieved empirical validation.

The minimum manuscript addition is the explicitly defined, presently predictive quantity
\[
R_{\rm stat}^{(1)}
=\frac{D_0}{B(E2;11/2_1^-\to15/2_1^-)},
\qquad
D_0=\frac{91}{176\pi}Q_s^2.
\]
Retain \(B_\uparrow=(16/12)B_\downarrow\), identify the actual states before comparison, and distinguish this one-transition denominator from the complete \(15/2\) sum. The lower isomer lifetime cannot replace the lifetime of the decaying \(15/2\) parent. A measured \(Q_s\) combined with a theoretical transition strength is a hybrid diagnostic, not a measured \(R_{\rm stat}^{(1)}\).

No complete experimental cubic network or new measurement is demanded for the bounded model paper. The necessary correction is the explicit observable definition, present data-access boundary and prediction label.

**2. Label the new static-conditioned result by its fitting dependence, and let either outcome narrow the conclusion.**

The prescribed \(Q_s=+0.88,+0.96,+1.04\ eb\) points are sensible fixed diagnostic targets around the selected adopted value. They are not three independent measurements or a complete confidence band.

The minimum result record should contain the target and achieved signed \(Q_s\), fitted \(s\) or \(\Gamma_0\), state identity/continuity, \(q_2\), signed \(q_3\), \(r\), \(z_\infty\), selected-channel fraction and static fraction. Use folded-angle differences only where both conversions are real. Keep the original nominal endpoint alongside these conditioned points.

Only \(\Gamma_0\) should be determined by \(Q_s\), with the stated exchange, monopole, core and E2 choices fixed. Identify multiple solutions or failure to reach a target within the declared path instead of choosing a branch by the resulting proxy separation. No global fit is implied.

Matching \(Q_s\) also constrains \(D_0\propto Q_s^2\) by construction. The fitted moment, its squared strength and ratios using that numerator cannot be counted as independent confirmations. Predictions for the unfitted transitional network remain informative, but their agreement with data has not followed from the static fit.

The scientific decision is conditional:

- If substantial full/restricted separation persists at the static-compatible targets, the supported extension is that this model effect survives conditioning on the selected static datum. The domain crossing need not survive.
- If the separation largely disappears there, retain the original intervention as a model/regime result and reduce its proposed relevance to actual \(^{135}\)Ba. Do not retune another operator or parameter to preserve the headline.

Pending those results, the current model-intervention claim stands. A claim of demonstrated separation in the static-compatible part of the path remains **review pending**.

**3. Complete the localized normalization and convergence corrections.**

[Main line 115](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:115) still uses \(q_2=Q_0^2,\ q_3=Q_0^3\) without identifying the rotor amplitude. Define it as the intrinsic tensor component, or distinguish the conventional electric quadrupole moment using \(T_{20}^{\rm body}=\sqrt{5/(16\pi)}Q_0\).

Include the single-\(j\) interaction contractions and the Hermitian RME convention alongside the supplied coefficients. Preserve the existing \((-1)^{2J}\) cubic phase; the prior algebra audit supports it.

[Main line 129](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:129) should qualify cubic convergence in raw-ratio terms as well as angle shifts. In the stored primary \(^{129}\)Ba result, \(z_5=0.038881\) and \(z_\infty=0.035138\), a roughly \(10.65\%\) relative difference despite a small angle change. This does not undermine the main separation or the \(^{135}\)Ba domain classification.

**Optional work and stopping point**

The spectator \(4/15\) channel-fraction baseline and an explicit common-denominator cubic decomposition remain useful exposition. Broader parameter surveys, additional isotope families, a new empirical campaign and further general novelty searches are unnecessary for this review's closeout.

The updated scientific story is coherent: a specified coupling intervention reorganizes a converged angular-channel diagnostic, operator changes delimit its shape interpretation, and available static data limit its physical transfer. The \(Q_s\)-conditioned follow-up can sharpen that boundary. It should not turn the conditional result into a claimed empirical discovery merely because one calibration target is reproduced.

Only this addendum was written. No manuscript/model tests, edits, fit, compilation or commit were performed.
