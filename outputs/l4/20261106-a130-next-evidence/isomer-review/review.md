# Interpretation review of the frozen 137Ba isomer test

**Conclusion:** the conditional upper-half-life argument is logically sound, and the stored unit conversions, E5 rates, sums and half-life arithmetic are consistent. Under either declared parent assignment and the unchanged modeled decay scheme, none of the seven tested operators is compatible with the 589(20)-ns isomer. Nearness of one selected B(E2) does not validate that scheme. This limits the physical reach claimed for this reconstruction; it does not directly falsify the initial-11/2 cubic moments, all IBFM, or the original authors' calculation.

This is a read-only interpretation and arithmetic audit. No kernel, parameter, operator, state assignment, article or other task was changed. The results of Planck's independent source-energy replay are not assumed known. Proposed minimal text is in [proposed-updates.md](proposed-updates.md); numerical checks and exact frozen-input hashes are in [arithmetic-checks.json](arithmetic-checks.json).

**Evidence and protocol.** The source values are those registered in `isomer-benchmark/protocol.json`: Vogt et al., PRC95,024316, the tentative negative-parity 2349.9-keV 19/2 and 2229.8-keV 15/2 levels, their 120.1-keV transition, B(E2)=0.46(3) downward W.u., and T1/2=589(20) ns. The recorded source locator is accepted-PDF Table III, printed p.13/PDF p.14, with the isomer discussion/figure on printed p.8/PDF p.9. The strength is already ICC-corrected. This review does not independently reanalyse the experiment.

The base protocol was recorded at 08:42:28 UTC on 2026-11-06; the energy-only mapping was saved at 08:45:16 before new E2 evaluation. The width addendum was recorded at 08:52:05 after the initial strength result and run at 08:56:15. This is a staged internal test with a prospectively frozen follow-up calculation, not a blind experiment or external preregistration.

The actual scope is **seven operators times two candidate parent states: fourteen width rows**. The strength comparison contains seven operators times four declared 19/2–15/2 pairs: twenty-eight rows. The observed lifetime and B(E2) come from the same experimental lineage and are not independent constraints to multiply into a joint significance.

**Units and direction check.** For A=137, the declared radius convention gives
\[
B_{\rm W}(E2)=\frac{1}{4\pi}\left(\frac35\right)^2
[1.2A^{1/3}]^4
=41.95448333\ e^2{\rm fm}^4
=0.004195448333\ e^2{\rm b}^2.
\]
Thus 0.46 W.u. corresponds to 0.001929906233 e2b2. Both compared strengths are downward; no even-core upward-W.u. convention is used.

The computed transition strength is \(|\langle15/2\Vert T(E2)\Vert19/2\rangle|^2/20\). Its reverse B(E2) has denominator 16 and is larger by 20/16=5/4. This is distinct from the 4/3 factor for the article's separate 11/2↔15/2 observable.

The frozen coefficient is
\[
\lambda_\gamma(E2)
=1.2239\times10^{13}\,E_\gamma^5[{\rm MeV}]\,
B_\downarrow[e^2{\rm b}^2]\ {\rm s}^{-1}.
\]
It is equivalent to \(1.2239\times10^9\) when B is expressed in e2fm4, or 0.012239 when energy is expressed in keV and B remains in e2b2. Re-evaluating all stored branch rates in those unit systems gives the same values. The summed quantities are **rates**, not energy widths; no additional hbar belongs in the code's half-life conversion:
\[
T_{1/2}^{\rm upper}[{\rm ns}]
=\frac{\ln2\,10^9}{\sum_f\lambda_{\gamma,f}(E2)}.
\]
This audit checks the frozen numerical convention and conversions; it does not infer missing ICC or reconstruct an observed total lifetime from the quoted B.

**E5 versus strength.** The following factors compare an individual model branch with the quoted experimental E2 branch, using the latter's E and B. These are diagnostic ratios, not independent experimental evidence:

| Operator and model branch | B ratio | \((E_{\gamma,\rm model}/120.1{\rm\,keV})^5\) | Radiative-rate ratio |
|---|---:|---:|---:|
| Primary, 19/2_1→15/2_1 | 48.8453 | 89,105.45 | \(4.3524\times10^6\) |
| Primary, 19/2_1→15/2_2 | 4.73396 | 0.0105474 | 0.0499311 |
| Conditional Q136=+0.07, 19/2_1→15/2_2 | 0.913097 | 0.0105474 | 0.00963082 |
| Same conditional operator, 19/2_1→15/2_1 | 47.5360 | 89,105.45 | \(4.2357\times10^6\) |

For the primary branch, the modeled photon is 1173.610 keV, not 120.1 keV. Both the strong matrix element and the much larger energy accelerate the radiative rate. In the alternate branch the modeled photon is only 48.325 keV, so even a strength near the measured value does not give a comparable partial gamma rate.

The energy-only nearest pair is the minimum of the declared **two-level excitation-energy distance**. It is not a physical assignment or a statistical chi square. For 19/2_1→15/2_2, the parent and daughter residuals relative to the fixed 11/2 anchor are still +454.284 and +526.059 keV. “Nearest” should not be shortened to “spectroscopically matched.”

The conditional selected strength 0.420024 W.u. is outside the quoted interval [0.43,0.49] W.u. Its central difference is −1.3325 times the quoted 0.03-W.u. margin. That is not a p-value and includes no complete model uncertainty. More importantly, the 21.86655-W.u. route to 15/2_1 remains open. It carries **99.998076%** of the conditional E2-only radiative sum; the near-strength 15/2_2 branch carries only **\(2.2737\times10^{-9}\)** of that sum. These fractions are model E2-radiative fractions, not measured total branching probabilities.

**Meaning of the width bound.** For a state that actually follows the declared model energies and E2 amplitudes,
\[
\lambda_{\rm total}
=\sum_f\lambda_{\gamma,f}(E2)+\lambda_{\rm other}
\ge\sum_f\lambda_{\gamma,f}(E2),
\]
because additional decay rates are nonnegative. Hence
\[
T_{1/2}\le \frac{\ln2}{\sum_f\lambda_{\gamma,f}(E2)}.
\]
Omitting internal conversion, M1 and other contributions makes the bound conservative for that unchanged scheme. There is no need to impute an ICC. Adding such widths cannot lengthen its lifetime. Enlarging/reconstructing the model can, however, change its energies and amplitudes; that is a different problem and is not excluded by this monotonic-rate argument.

The primary upper bounds are 0.000269817 ns for parent1 and 0.0000602153 ns for parent2. The **largest** bound anywhere among the fourteen combinations is 0.000281041 ns, or 0.281041 ps. The observed central half-life is over \(2.0958\times10^6\) times that largest bound. In the primary parent1 case, the 19/2_1→15/2_1 branch alone accounts for 99.992785% of the E2-radiative rate.

Thus the unchanged proposed scheme fails the isomer compatibility check under the proposed identification. This is neither a model-independent empirical lifetime bound nor a complete predicted lifetime. Predicted lower states are not thereby observed states, and a fast model branch is not an experimental non-observation limit. No measured 120.1-keV photon was substituted for unrelated model branches.

**What this constrains in the article.** For initial J=11/2 and a rank-two operator, the two intermediate spins in the cubic loop can only lie from 7/2 to 15/2. A 19/2→15/2 element does not enter that loop, since 19/2 cannot connect directly back to 11/2 by E2. The failed check therefore does not directly disprove the computed q3, its closure identity or the controlled 135Ba mechanism. It does constrain claims of broader spectroscopic or decay-scheme validation of the common reconstruction/operator family.

The extra width calculation tests **decay completeness in the model**, not a second independent experimental datum. Treating the B and lifetime discrepancies as independent likelihood terms would double-count their measurement origin.

The inspected article already distinguishes the 19/2 isomer lifetime from the missing 15/2→11/2 denominator. That remains correct, but after this test it is incomplete to present the isomer only as an irrelevant datum. The minimal additional statement is the conditional failure of this high-spin check. The numerical model-mechanism result can remain, with that limitation; a selected-branch near-match must not be presented as validation or as establishing physical readiness.

**One most useful next question:** does Planck's fixed-input source-energy replay establish that the level ordering and the fast 19/2_1→15/2_1 escape route are faithful consequences of the intended reconstruction?

If the answer is yes, the high-spin coverage limitation becomes a well-identified failure of that declared family and mapping. If the answer is no, the attribution stops at reconstruction fidelity until the discrepancy is understood. At present neither outcome is known, so the original authors' model cannot be declared wrong. Further broad parameter/operator searching would not resolve that question.

**Checks completed.** Protocol/producer/mapping hashes match the frozen artifacts. All 28 RME-to-strength conversions, all 84 stored open E2 branch rates, fourteen sums and half-life bounds, radiative fractions and alternate unit conversions were checked arithmetically. The benchmark inputs were unchanged. No model code was imported or executed.
