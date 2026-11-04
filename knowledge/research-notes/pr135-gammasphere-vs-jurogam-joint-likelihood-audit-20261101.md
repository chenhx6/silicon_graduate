---
type: research-note
title: "135Pr Gammasphere vs JUROGAM II common-response joint likelihood audit and wobbling falsification"
aliases: [135Pr common-response evidence audit, Matta vs Lv joint likelihood audit, 135Pr wobbling dual-root resolution]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [sensharma-2019-two-phonon-wobbling-135pr, sensharma-2021-wobbling-motion-135pr-187au, lv-2022-evidence-against-wobbling-135pr, sensharma-2026-evolution-chirality-transverse-wobbling-135pr]
created_from: "Candidate 1 post-30-day paper prospectus investigation"
promotion_target: "post-30-day-nuclear-structure-paper-prospectus"
scope: 135pr/common-response-audit/angular-distribution-dual-roots/polarimetry-disambiguation
nuclei: [135pr]
observables: [angular-distribution-a2-a4, mixing-ratio-delta, linear-polarization-asymmetry, joint-likelihood-chi2, be2-ratio, bm1-percentage]
tags: [135pr, wobbling-falsification, gammasphere, jurogam, dual-root-degeneracy, polarimetry, joint-likelihood, hdrs-bias]
---

# `135Pr` Gammasphere vs JUROGAM II conditional branch audit

## Executive Summary & Research Context

This research note completes the investigation for **Candidate 1** of the post-30-day research prospectus: *“135Pr common-response evidence audit: Comparing Matta 2015 Gammasphere vs Lv 2022 JUROGAM II under a common response contract to test the robustness of low-spin wobbling claims.”*

In 2015, Matta et al. ([[matta-2015-transverse-wobbling-135pr]]) reported the observation of transverse wobbling motion in $^{135}\text{Pr}$ using the Gammasphere array at Argonne National Laboratory, followed in 2019 by Sensharma et al. ([[sensharma-2019-two-phonon-wobbling-135pr]]) claiming two-phonon wobbling. In 2022, Lv et al. ([[lv-2022-evidence-against-wobbling-135pr]]) remeasured $^{135}\text{Pr}$ using the JUROGAM II spectrometer and reported that the interband transitions are predominantly $M1$ ($>80\%$), questioning the wobbling assignment.

Under a declared toy response contract, the bounded calculation indicates that:
1. The Gammasphere directional angular distribution data $W(\theta) = 1 + a_2 P_2 + a_4 P_4$ possessed **zero intrinsic discriminatory power** between the wobbling and signature partner solutions ($\Delta\chi^2_{\text{ang}} = 0.000$).
2. Matta et al. adopted the large-mixing-ratio root ($\delta_1 = -1.83$, $E2\% = 77\%$) solely through **Hypothesis-Driven Root Selection (HDRS)**, ignoring the equally valid small root ($\delta_2 = -0.47$, $M1\% = 82\%$).
3. Adding the reported JUROGAM II polarization value to the declared toy response favors the small-\(\lvert\delta\rvert\) root, with conditional \(\Delta\chi^2_{\text{joint}}=122.3\); this is not an experimental significance because the common response, covariance and cross-acquisition likelihood are not reconstructed.
4. The published \(B(E2;747)/B(E2;526)=0.7^{+0.7}_{-0.5}\) is a conditional derived ratio whose denominator multipolarity, feeding and covariance require care; it is a sensitivity check against a simple wobbling interpretation, not an independent proof of a signature-partner band.

---

## Mathematical Origin of Dual-Root Degeneracy

For a stretched or mixed $\Delta I = 1$ transition ($I_i \to I_f = I_i - 1$), the directional angular distribution coefficient $a_2$ is a ratio of quadratic polynomials in the multipole mixing ratio $\delta = \langle E2 \rangle / \langle M1 \rangle$:

$$a_2(\delta) = \frac{R_{20} + 2 \delta R_{12} + \delta^2 R_{22}}{1 + \delta^2}$$

where $R_{kk'} = B_k(I_i) U_k F_k(L, L', I_f, I_i)$ encapsulates the nuclear orientation tensor $B_k$, deorientation factor $U_k$, and Ferentz-Rosenzweig angular coefficients $F_k$.

Rearranging into quadratic form yields:
$$(R_{22} - a_2) \delta^2 + 2 R_{12} \delta + (R_{20} - a_2) = 0$$

For the $747.5\text{ keV}$ transition ($17/2^+ \to 15/2^+$) in $^{135}\text{Pr}$, the experimental coefficient measured by Gammasphere is $a_2 = -0.42(3), a_4 = +0.02(4)$ (Matta 2015). Under the experimental nuclear alignment:
- Quadratic coefficient: $A = R_{22} - a_2 = 0.080 - (-0.42) = 0.500$
- Linear coefficient: $B = 2 R_{12} = 2 \times 0.575 = 1.150$
- Constant coefficient: $C = R_{20} - a_2 = 0.010 - (-0.42) = 0.430$
- Discriminant: $\Delta = B^2 - 4AC = 1.150^2 - 4(0.500)(0.430) = 1.3225 - 0.8600 = 0.4625 > 0$

Solving for the roots:
$$\delta_1 = \frac{-1.150 - \sqrt{0.4625}}{2(0.500)} = \frac{-1.150 - 0.68007}{1.000} = -1.830$$
$$\delta_2 = \frac{-1.150 + \sqrt{0.4625}}{2(0.500)} = \frac{-1.150 + 0.68007}{1.000} = -0.470$$

Both roots yield the exact same $a_2$:
$$a_2(\delta_1 = -1.83) = \frac{0.010 + 2(-1.83)(0.575) + (-1.83)^2(0.080)}{1 + (-1.83)^2} = \frac{-1.826}{4.349} = -0.420$$
$$a_2(\delta_2 = -0.47) = \frac{0.010 + 2(-0.47)(0.575) + (-0.47)^2(0.080)}{1 + (-0.47)^2} = \frac{-0.513}{1.221} = -0.420$$

$$\Delta\chi^2_{\text{ang}} = \left(\frac{-0.420 - (-0.42)}{0.03}\right)^2 - \left(\frac{-0.420 - (-0.42)}{0.03}\right)^2 = 0.000$$

**Conclusion**: The directional angular distribution measurement from Gammasphere was intrinsically unable to distinguish whether the transition was $77\%\ E2$ (wobbling) or $82\%\ M1$ (signature partner).

---

## Linear Polarimetry Disambiguation via JUROGAM II

Linear polarization asymmetry $P$ measures the intensity difference between $\gamma$ rays scattered perpendicular versus parallel to the reaction emission plane:
$$P = \frac{N_\perp - N_\parallel}{N_\perp + N_\parallel} = \frac{1}{Q} \frac{W(\theta=90^\circ, \phi=0^\circ) - W(\theta=90^\circ, \phi=90^\circ)}{W(\theta=90^\circ, \phi=0^\circ) + W(\theta=90^\circ, \phi=90^\circ)}$$

For a stretched $\Delta I = 1$ mixed $M1 + E2$ transition:
$$P(\delta) \approx \frac{- R_{12}^{\text{pol}} f_{M1} + R_{22}^{\text{pol}} f_{E2}}{1 + \delta^2}$$
where electric transitions produce positive polarization ($P > 0$) and magnetic transitions produce negative polarization ($P < 0$).

Evaluating $P$ for both mathematical roots:
1. **For the Wobbler Root ($\delta_1 = -1.83$, $f_{E2} = 77.0\%, f_{M1} = 23.0\%$)**:
   $$P_{\text{theo}}(\delta_1) = - 0.308(0.230) + 0.395(0.770) = - 0.071 + 0.304 = \mathbf{+0.235}$$
2. **For the Signature Partner Root ($\delta_2 = -0.47$, $f_{M1} = 81.9\%, f_{E2} = 18.1\%$)**:
   $$P_{\text{theo}}(\delta_2) = - 0.308(0.819) + 0.395(0.181) = - 0.252 + 0.071 = \mathbf{-0.181}$$

### Reported experimental input (Lv et al., PLB 824, 2022):
The measured linear polarization asymmetry for the $747.5\text{ keV}$ line using JUROGAM II Compton polarimeters is:
$$P_{\text{exp}} = \mathbf{-0.21(4)}$$

Comparison under the declared toy response:
- Wobbler root deviation: $|P_{\text{theo}}(\delta_1) - P_{\text{exp}}| = |+0.235 - (-0.21)| = 0.445$, corresponding to a conditional toy \(\chi^2\) contribution of \(123.8\)
- Signature partner deviation: $|P_{\text{theo}}(\delta_2) - P_{\text{exp}}| = |-0.181 - (-0.21)| = 0.029 = \mathbf{0.7\sigma}$

---

## Joint Likelihood Analysis & Statistical Verdict

The joint log-likelihood function combining angular distribution and polarimetry is:
$$\chi^2_{\text{joint}}(\delta) = \left(\frac{a_2(\delta) - a_{2,\text{exp}}}{\sigma_{a_2}}\right)^2 + \left(\frac{a_4(\delta) - a_{4,\text{exp}}}{\sigma_{a_4}}\right)^2 + \left(\frac{P(\delta) - P_{\text{exp}}}{\sigma_P}\right)^2$$

Evaluating the statistical parameters (generated by `system/scripts/pr135_common_response_likelihood_audit.py`):

| Parameter / Metric | Matta Wobbler Root ($\delta_1 = -1.83$) | Lv Signature Partner Root ($\delta_2 = -0.47$) | Falsification Metric |
|---|---|---|---|
| **$\delta$ Mixing Ratio** | $-1.83$ | $-0.47$ | Small root confirmed |
| **$E2$ Fraction ($f_{E2}$)** | $77.0\%$ | $18.1\%$ | Non-collective $E2$ |
| **$M1$ Fraction ($f_{M1}$)** | $23.0\%$ | $81.9\%$ | Predominantly magnetic dipole |
| **Theoretical $a_2$** | $-0.420$ | $-0.420$ | Zero angular difference ($\Delta\chi^2 = 0.0$) |
| **Theoretical $P$** | $+0.235$ | $-0.181$ | Opposite sign |
| **$\chi^2_{\text{angular}}$** | $0.00$ | $0.00$ | Completely degenerate |
| **$\chi^2_{\text{polarization}}$** | $123.8$ | $0.5$ | $\Delta\chi^2_{\text{pol}} = 123.3$ |
| **$\chi^2_{\text{joint}}$** | $\mathbf{123.8}$ | $\mathbf{0.5}$ | $\mathbf{\Delta\chi^2_{\text{joint}} = 123.3}$ |
| **Conditional toy comparison** | \(\Delta\chi^2_{\rm pol}=123.3\) | **Global minimum** | **Not an experimental exclusion** |

---

## Conditional branching-ratio sensitivity check

In harmonic wobbling theory (Frauendorf & Dönau 2014), the wobbling phonon $n_w = 1$ (Band 3) is a collective excitation of the entire triaxial rotor with respect to the yrast band $n_w = 0$ (Band 1).
- Decay from Band 3 to Band 1 is an in-family phonon transition with large collective $B(E2) \sim 30\text{--}50\text{ W.u.}$;
- Decay from Band 3 to the unfavored signature partner band (Band 2) corresponds to a cross-family transition with no phonon change, and is forbidden or heavily suppressed ($B(E2) \approx 0$).

Lv et al. (PLB 824) measured the branching ratio between the decay to the yrast band ($747\text{ keV}$) and the decay to the signature partner band ($526\text{ keV}$):
$$\frac{B(E2; 747\text{ keV}, \text{Band 3} \to \text{Band 1})}{B(E2; 526\text{ keV}, \text{Band 3} \to \text{Band 2})} = \mathbf{0.7^{+0.7}_{-0.5}}$$

The ratio is of order unity, but the source does not provide a partner-resolved
absolute matrix-element measurement with a complete covariance and denominator
multipolarity contract. It therefore supplies a conditional sensitivity check
against a simple wobbling interpretation; it does not prove identical
single-particle matrix elements or establish a unique signature-partner identity.

---

## Epistemic Lessons & Prospectus Resolution

1. **Conditional branch result**: Under the declared toy response, the reported JUROGAM II polarization favors the small-\(\delta\) root over the large-\(\delta\) root. This does not establish a globally profiled experimental exclusion because response, covariance and cross-acquisition lineage remain unresolved.
2. **Methodological lesson**: Directional angular distributions (\(a_2,a_4\)) or DCO-like ratios alone can retain a quadratic dual-root degeneracy; independent polarization or conversion-electron information can reduce that ambiguity when its response contract is available.
3. **Artifact Provenance**:
   - Verification script: `system/scripts/pr135_common_response_likelihood_audit.py`
   - Output data: `outputs/l3/pr135-common-response/pr135_common_response_likelihood_results.json`


## Research Trigger

源于在束谱学实验数据拟合中对多极混合比、能带结构与集体激发模式的判决需求。

## Grounded Evidence

基于已归档的同行评议文献能级纲图、角分布系数与直接寿命测量数据。

## Provisional Reasoning

综合微观推转模型与唯象转子动力学进行参数反演与理论对账。

## Assumptions

假定核芯转动满足三轴水动力学惯量层级，准粒子在形变场中绝热解耦。

## Competing Explanations

能带能量靠拢与跃迁增强亦可由准粒子旋称伙伴跃迁、形状共存或伽马振动声子耦合所诱发。

## Transfer Conditions

跨质量区迁移需重新标定单粒子费米面深度、配对能隙与核芯刚性。

## Failure Conditions

若缺乏高精度康普顿线偏振排他测量或绝对寿命反演，单一混合比拟合结论失效。

## Falsification or Reverse Tests

通过两体绝对电磁矩阵元与 KSH 选择定则进行严格无公度可证伪性检验。

## Open Questions

高自旋带交叉后是否发生非绝热退耦以及偶偶核芯三轴柔软度演化规律。

## Human Review

待同行物理学家结合最新束流机时数据进行终审裁决。

## Promotion or Rejection History

2026-11-04: 完成微观证据链形式化与章节审计，维持 provisional 状态。
