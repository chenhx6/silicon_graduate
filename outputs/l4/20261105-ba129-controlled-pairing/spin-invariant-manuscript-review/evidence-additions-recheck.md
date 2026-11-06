**Final bounded science recheck of the two evidence additions, 6 November 2026**

**Verdict.** The Vogt transition attribution and conditional empirical-operator results are numerically and interpretively consistent with their supplied evidence records. No new substantive algebraic or physical failure was identified. The manuscript remains a credible, explicitly conditional EPJA model study. Two small wording/scoping corrections should be made before closing this revision. Neither requires a new calculation.

This recheck covers only the new passages, Table 3, the associated abstract/discussion changes, Appendix B's quoted results and the documented replay boundary. Evidence was read locally, with arithmetic on stored numbers only. No new literature search, model execution, root fitting, test suite, code inspection or compilation was performed. The parent's ongoing replay is not certified by this review.

**Assessed snapshots**

| Input, relative to `raw/writing/gpt/odd-ba-quadrupole-closure/` | SHA-256 |
|---|---|
| `main.tex`, 296 lines | `b272ac9637cbdeecab4bcc4094a394ca9d193698f29f6bcf501a0a91c70cfece` |
| `controls.tex`, 129 lines | `d826e91421d1458a1b816e50e1b9e96683013f3ea64034d55ea012e1fa4825dc` |
| `data/vogt2017-transition-constraints.json` | `3321870a2bbdd0424eca9eb4e588d0f73577fa816f5ee1072d2e4a22ac1fde43` |
| `data/calibrated-operator-contract.json` | `5d49a9ceda150dea250e80eceb1389fdc6b96f6af4307ca2c6c8c2aabb75b6ff` |
| `data/results/calibrated-operator-predictions.json` | `834977b8b37be4201a05126e51c83cd90d1d9aadec29541f7a3e9989fb6bc20f` |
| `data/results/moment-matched.json` | `43ee036a616db4c76462a013b1b65eec23f50d3a194455f815d4e2ac1162f932` |

**1. Vogt2017 attribution passes**

[Main lines starting at 217](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:217) agree with the supplied transition-constraint JSON:

- The tentative \(^{137}\)Ba \((15/2^-)\) candidate is at 2229.8 keV and connects to the 661.7-keV \(11/2^-\) isomer through the tabulated 1568.2-keV transition.
- The 589(20)-ns half-life belongs to the upper 2349.9-keV \((19/2^-)\) state.
- The reported \(B(E2)=0.46(3)\) W.u. belongs to its 120.1-keV \(19/2\to15/2\) transition. It cannot normalize the \(15/2\to11/2\) denominator of \(R_{\rm stat}^{(1)}\).

The rounded level difference is 1568.1 keV, matching the figure label retained in the JSON; the table records 1568.2(5) keV. The 0.1-keV difference is not an internal attribution error. The lower state's independent lifetime and absolute E2 strength remain unavailable in this source record.

The text correctly replaces the earlier bounded ENSDF absence with a later primary candidate, preserves tentative assignments and avoids an all-literature absence claim. A candidate assignment does not yet establish that this is the experimentally complete lowest-\(15/2^-\) counterpart of the model ordinal. The manuscript's existing state-mapping qualification remains necessary and adequate.

This was a comparison against the supplied source audit and locators, not a fresh independent full-paper reading.

**2. Conditional empirical-operator calibration passes at its stated scope**

The predictions file identifies the unchanged calibration contract by the correct SHA-256. It contains the two primary reference rows and ten calibrated rows, one for each of five distinct core targets in each of \(^{135,137}\)Ba. Table 3 includes all five accepted targets represented in that file. I did not rerun the analytic root enumeration.

| \(Q_s(136)\) target, \(eb\) | Predicted \(Q_s(135)\), \(eb\) | Full \(r(135)\) | Selected \(z_\infty(135)\) | Within \(0.96\pm0.08\ eb\) |
|---:|---:|---:|---:|---|
| −0.19 | 1.088519 | −0.642347 | 1.029638 | No |
| +0.01 | 0.923290 | −1.093167 | 0.849643 | Yes |
| +0.02 | 0.914997 | −1.096209 | 0.839837 | Yes |
| +0.07 | 0.873492 | −1.092220 | 0.791879 | No |
| +0.25 | 0.723459 | −0.919537 | 0.640472 | No |

All six columns of manuscript Table 3, including \(\chi'\) and \(e_F\), agree with the stored values at their displayed precision. Recomputing \(q_3/q_2^{3/2}\) and the selected-chain normalization from those stored scalars agrees to floating-point rounding.

The two specifically identified predictions have residuals −0.036710 and −0.045003 eb relative to 0.96 eb. Their placement within the quoted 0.08-eb margin is descriptive, as the manuscript states. It is not a propagated prediction interval, a significance test or evidence for preferring these experimental branches.

For these two rows, the full-angle fields are correctly null while the selected angles remain real. The additional \(^{137}\)Ba example also matches the data: at the +0.01-eb core target, \(z_5=1.0002661\), \(z_\infty=0.9948403\), and \(r=-1.0895673\). Completing the selected channel restores that selected angle only. It does not restore the full moment-angle conversion.

The new abstract and [discussion](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:193) correctly decline to treat complete finite-space moments as guaranteed physical intrinsic angles. An out-of-domain normalized cubic moment is not, by itself, an invalid tensor contraction. Conversely, a real selected angle is not established as the physical answer merely because the complete conversion is undefined.

The contract and [controls text](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/controls.tex:80) keep the empirical limitations visible: common averaged core \(B_\uparrow\) held fixed across interference alternatives, missing joint covariance, shared moment-source lineage, no use of \(Q_s(135)\) in the calibration equations, and no branch selection by its agreement. “Out of calibration” is supportable; statistically independent or blinded validation would not be.

The primary 35-setting scan's coverage ranges must remain scoped to that scan. The newly calibrated operators have different channel fractions and some lower five-state saturation values. The current abstract and control subsections distinguish these scopes adequately.

**3. Appendix B passes, subject to one numerical-scope clarification**

The three adopted-target roots, complete/selected angles and 13.53°–18.83° separations match `moment-matched.csv`. The fourth point is the separately retained 0.98-eb target, not another independent measurement.

The central \(Q_s=0.96\) match changes the calculated first \(15/2\to11/2\) spacing from 691.8633 to 526.6420 keV. The tentative experimental connection is 682.3 keV. Thus the quoted static improvement has a disclosed spectral cost and is not presented as a simultaneous successful fit.

**Required correction A, numerical scope.** [Main line 282](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:282) states that the largest panel energy change is 0.3684 MeV immediately after discussing the central match. That number is correct **for the central 0.96-eb match**. Across all four matched points, the largest recorded panel shift is 0.4321501 MeV at the 0.88-eb target. Make the scope explicit:

> At the central \(Q_s=0.96\ eb\) match, the largest panel energy shift is 0.3684 MeV.

If the intended statement is instead an envelope over all four points, use 0.4322 MeV. This is a reporting-ambiguity correction, not evidence of an erroneous spectrum.

**Required correction B, baseline versus recalibration.** [Controls line 75](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/controls.tex:75) says that the operator is not refitted to improve the comparisons, followed by explicit moment-based operator recalibration. Limit the first statement to the primary comparison, for example:

> The primary comparisons above use the unchanged operator. The following alternatives recalibrate to the \(^{136,137}\)Ba targets without using \(^{135}\)Ba.

For the same reason, “the overprediction of the measured static moment” in the conclusion would read more precisely as “the primary operator's overprediction.” The model results and branch-retention policy do not need to change.

**4. Replay boundary is documented without false historical reverification**

The [data README](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/data/README.md:69) distinguishes numerical-contract/producer/module verification from recording unbundled historical evidence hashes. The preserved [strict-replay boundary](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/analysis/calibrated-operator-replay-boundary.md:35) explicitly identifies the unavailable historical source-page bytes. Recording the old hash is not represented as verifying those absent bytes.

This is an appropriate documentary distinction. The inability to perform the original unmodified all-file hash check does not, on its own, demonstrate an error in the frozen numerical results. A successful adapted numerical replay would likewise not restore historical evidence-file verification. I did not inspect or execute the adapter, verify runtime-module bytes, or certify the parent's replay outcome; those remain the parent's execution responsibility.

**Disposition.** Make the two localized scope/wording corrections. The new evidence additions otherwise pass this bounded consistency review. No new research, parameter search, branch pruning or model rerun is requested. Only this new addendum was written; no other files were modified and no commit was made.
