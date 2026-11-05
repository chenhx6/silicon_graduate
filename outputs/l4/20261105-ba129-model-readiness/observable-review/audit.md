# Frozen 129Ba observable audit

**Outcome:** the frozen predictions are arithmetically consistent with their declared protocol. Existing checks covered seven energy starts, both dual partners, 84 photon rows, 140 mapped-state diagnostics and 42 transition-phase comparisons. No phase-space, normalization, ordinal-indexing or anchor-calibration error was found. Results and input hashes are preserved in [audit-results.json](audit-results.json); this final handoff adds no analysis or tests.

**Rate convention and mapping.** For dimensionless strengths,
\[
r=a+\eta_\gamma b,\quad
 a=(E_t/E_r)^5B_{Q,t}/B_{Q,r},\quad
 b=E_t^3B_{j,t}/(E_r^5B_{Q,r}).
\]
Here \(\eta_\gamma\ge0\) has units MeV² and b has units MeV⁻². The E2 and M1 contributions add in the angle-integrated radiative rate. The runner, lines 69–113, uses the correct final-row/initial-column indexing and common \(2I_p+1\) normalization. All six reference transitions have ΔI=2 and zero computed rank-1 strength. Published photon energies supply phase space; same-parent photon ratios need neither lifetime nor internal-conversion factors.

The mapping assigns ordinal 0 at each selected spin, except ordinal 1 for 883.43, 1210.0, 1545.3 and 1845.0 keV. This assumes no omitted lower state in the selected model comparison. Transfer normalization and its model-energy window use the ordinal-0 11/2 reference at 278.81 keV.

Exactly **153.8/518.6 = 0.074** calibrates one common photon scale per parameter set; five ratios remain withheld. Negative eta is not clipped. Contract predeclaration chronology was not independently established. Reference purity and the interpretation of corrected RI as integrated photon strengths remain experimental assumptions; the ratios share an acquisition lineage.

| Frozen energy-best case | Pair, keV | Reported ratio | Electric floor | Anchored prediction |
| --- | --- | ---: | ---: | ---: |
| C60 irrotational | 364.7/461.6 | 3.936364 | 5.542485 | 10.587014 |
| C120 free inertias | 604.7/701.3 | 0.608333 | 0.974149 | 9.174466 |
| C120 free inertias | 157.0/678.0 | 0.066583 | 0.000121051 | 0.000313190 |

C120 gives \(\eta_\gamma=56.96119956\) MeV². The first two floors cannot match their central observations with any nonnegative magnetic contribution at those frozen wavefunctions. This is a conditional model/operator/mapping discrepancy, not a statistical exclusion or identification of physical shape.

**Signed duality.** The map is \(\gamma'=60^\circ-\gamma\), \(\lambda'=-\lambda\), and \(J'=(J_1,J_3,J_2)\), with fixed positive gap. The tested D₂ rotation gives
\[
S_f^\dagger Q'S_i=-Q,\qquad S_f^\dagger j'S_i=+j.
\]
Signed diagonal Q therefore reverses. For the C120 state mapped to 278.81 keV, its unit diagonal RME is −0.751465276 versus +0.751465276.

The transition product \(\mathcal C_{fi}=Q_{fi}j_{fi}^*\) is invariant under independent eigenstate rephasing, but **odd under duality**. Its normalized phase changes by π when both amplitudes are nonzero. Selected photon B strengths remain equal within \(1.114\times10^{-13}\). Signed observables require fixed physical prefactors/sign conventions; the fitted squared scale supplies no magnetic sign. No physical δ, polarization, complete diagonal M1 or structural-mode conclusion is established.

**Discarded Nambu coupling.** Its coefficient \(\eta^N_{\mu\nu}=u_\mu v_\nu-v_\mu u_\nu\) differs from \(\eta_\gamma\). The omitted block and exact frozen-state diagnostic are
\[
K=P^\dagger(UH_RV-VH_RU)P,\qquad
\sigma_n=\|Kv_n\|=\|H_{\rm Nambu}X_+v_n-E_nX_+v_n\|.
\]
Both residual routes were independently checked. Formal perturbative diagnostics were computed without applying corrections:

| Energy-best case | Residual range, MeV | Formal mixing norm | Formal relative-shift RMS, keV |
| --- | ---: | ---: | ---: |
| C60 irrotational | 0.0519–0.5775 | 0.00774–0.09879 | 26.92 |
| C60 free inertias | 0.7106–1.6076 | 0.15575–0.61019 | 266.95 |
| C120 free inertias | 0.7012–1.5884 | 0.13698–0.41173 | 208.40 |

Relative shifts subtract the 11/2 anchor shift; RMS excludes that anchor. For C120 these formal scales exceed its 39.93-keV energy-fit RMS, while mixing up to 0.412 does not establish controlled perturbation theory. They are not probabilities, error bars or corrected predictions. Adding K has not been shown to repair the ratios; any alternate Hamiltonian requires separate calibration.

**Evidence and limitations.** Original source: `raw/papers/1975_MeyerTerVehn_CollectiveOddANuclei_PartI.pdf`, printed p.118 Eqs. (2.28)–(2.31), p.119 Eq. (2.33), and p.120 Eqs. (2.40)–(2.41). This audit concerns the declared custom kernel, not original-code certification.

Existing maximum discrepancies were \(3.553\times10^{-15}\) for photon ratios and \(6.859\times10^{-14}\) MeV between Nambu residual routes. All 15 locked input hashes remained unchanged during those checks. Runner lines 172–182 record EM duality error without gating failure on it: a minor future robustness item, not a current numerical failure.

Publisher crops/text remain local-only in `tmp/ba129-model-readiness/observable-review/`. Publication outputs contain derived review material only. No physical validation, novelty claim, refit or replacement spectrum is asserted. Core, fits, runner, knowledge, PLAN, get-paper and other sessions’ files are unchanged by this handoff.
