---
type: concept
title: "In-beam reaction spin alignment parameter (sigma/I) calibration and directional distribution multipole mixing ratio (delta) joint extraction"
aliases: [spin-alignment, alignment-sigma-over-i, mixing-ratio-extraction, in-beam-angular-distribution, substate-gaussian-alignment]
created: 2026-11-04
updated: 2026-11-04
status: ai-draft
review_status: unreviewed
tags: [in-beam-spectroscopy, angular-distribution, spin-alignment, mixing-ratio, racah-algebra, clebsch-gordan, 130ba, 135pr, 128cs]
---

# In-beam reaction spin alignment parameter ($\sigma/I$) calibration and directional distribution multipole mixing ratio ($\delta$) joint extraction

## Definition

### Physical Formalism: Reaction Alignment & Magnetic Substates

In heavy-ion fusion-evaporation reactions ($HI, xn$), the orbital angular momentum $\vec{\ell}$ of the incoming projectile is perpendicular to the beam axis ($z$-axis). As a result, the compound nucleus is formed with its total angular momentum $\vec{J}$ strongly aligned in the plane perpendicular to the beam.
The magnetic substate population distribution $P(m)$ is well described by a Gaussian centered at $m=0$:
$$P(m) = \frac{\exp\left(-\frac{m^2}{2\sigma^2}\right)}{\sum_{m'=-I}^I \exp\left(-\frac{m'^2}{2\sigma^2}\right)}$$
where $\sigma$ is the magnetic substate population width.

The orientation statistical tensor $\rho_{k0}(I, \sigma)$ is defined as:
$$\rho_{k0}(I, \sigma) = \sqrt{2I+1} \sum_{m=-I}^I (-1)^{I-m} \langle I m I -m | k 0 \rangle P(m)$$
The alignment attenuation parameter $\alpha_k(I, \sigma)$ measures the attenuation relative to complete alignment ($\sigma \to 0$):
$$\alpha_k(I, \sigma) = \frac{\rho_{k0}(I, \sigma)}{\rho_{k0}(I, \sigma=0)}$$
In typical heavy-ion reactions, $\sigma / I \approx 0.30 - 0.45$, yielding $\alpha_2 \approx 0.60 - 0.85$ and $\alpha_4 \approx 0.25 - 0.50$.

---

## Directional Angular Distribution & Joint Extraction

The directional angular distribution of $\gamma$-rays emitted at angle $\theta$ relative to the beam axis is:
$$W(\theta) = A_0 [1 + a_2 P_2(\cos\theta) + a_4 P_4(\cos\theta)]$$
Where the expansion coefficients are:
$$a_k = \alpha_k(I_i, \sigma) \cdot Q_k(E_\gamma) \cdot \left[ B_k^{\text{max}}(I_i) \cdot A_k(I_i, I_f, \delta) \right]$$
Here:
- $Q_k$ is the finite solid-angle attenuation factor of the detector;
- $B_k^{\text{max}}(I_i) = \sqrt{2I_i+1} (-1)^{I_i} \langle I_i 0 I_i 0 | k 0 \rangle$ is the full-alignment statistical tensor;
- $A_k(I_i, I_f, \delta)$ is the Yamazaki/Hamilton coefficient for a mixed multipole transition ($L_1 = 1, L_2 = 2$):
  $$A_k(I_i, I_f, \delta) = \frac{R_k(I_i, I_f, 1, 1) + 2\delta R_k(I_i, I_f, 1, 2) + \delta^2 R_k(I_i, I_f, 2, 2)}{1 + \delta^2}$$
  with $R_k(I_i, I_f, L, L') = (-1)^{1 + I_i - I_f + L' - L - k} \sqrt{(2I_i+1)(2L+1)(2L'+1)} \langle L 1 L' -1 | k 0 \rangle W(I_i I_i L L'; k I_f)$.

### Two-Step Joint Protocol:
1. **Calibration Step**:
   Measure a known pure stretched $E2$ transition in the ground band ($I_{\text{ref}} \to I_{\text{ref}}-2, \delta \equiv 0$).
   Since $A_2(E2), A_4(E2)$ are completely fixed by Racah algebra, $\alpha_2^{\text{meas}} = \frac{a_2^{\text{exp}}}{Q_2 B_2^{\text{max}} A_2(E2)}$.
   Invert $\alpha_2(I_{\text{ref}}, \sigma)$ to obtain the reaction parameter $\sigma/I$.
2. **Target Inversion Step**:
   Apply $\sigma = (\sigma/I) \cdot I_{\text{tgt}}$ to compute $\alpha_k(I_{\text{tgt}})$.
   Fit the observed $(a_2^{\text{exp}}, a_4^{\text{exp}})$ of the unknown transition to extract the mixing ratio $\delta(E2/M1)$ and $\%E2$ fraction via $\chi^2$ minimization, resolving the physical nature (wobbling vs. magnetic rotation vs. chiral partner decay).

---

## Executable Analysis Tool: `alignmix`

The Python analysis suite integrates `in_beam_spin_alignment_sigma_mixing_ratio_extractor.py`, accessible via CLI:

```bash
# 1. 130Ba wobbling candidate 9+ -> 8+ mixing ratio extraction
python3 system/scripts/analysis/nuclear_analyzer.py alignmix --preset 130Ba_wobbling_candidate_delta

# 2. 135Pr 17/2+ -> 15/2+ transverse wobbling transition mixing
python3 system/scripts/analysis/nuclear_analyzer.py alignmix --preset 135Pr_transverse_wobbling_mixing

# 3. 128Cs chiral partner band 11+ -> 10+ pure M1 dipole confirmation
python3 system/scripts/analysis/nuclear_analyzer.py alignmix --preset 128Cs_chiral_partner_dipole
```

---

## Literature and Textbook Provenance

- **W. D. Hamilton (ed.)**, *The Electromagnetic Interaction in Nuclear Spectroscopy* (North-Holland 1975), Chapter 14.
- **吴治华**, 《原子核物理实验方法》 (第三版), 第 10 章 §10.3.
- **卢希庭**, 《原子核物理》 (修订版), 第 6 章 §6.3.
- **T. Yamazaki**, Nucl. Data A 3, 1 (1967).


## Necessary Assumptions

微观平均场假定核子在有效单体势中运动，通过剩余相互作用自洽诱发四极形变与集体转动。


## Discriminating Observables

激发能量级间距、跃迁多极性比值与电磁约化跃迁几率是关键鉴别观测量。


## Supporting Evidence

在束伽马谱学实验测定的角分布、DCO比值与能级寿命提供直接实证。

## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。


## Sources

- [[triaxial-collective-modes-unified-theory-and-spectroscopy]]
- [[nuclear-spectroscopy-and-structure-master-field-manual]]
