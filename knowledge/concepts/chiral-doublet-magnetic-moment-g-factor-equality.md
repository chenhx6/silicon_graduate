---
type: concept
title: "Chiral doublet magnetic moment g-factor equality theorem and spurious band arbitration"
aliases: [chiral-g-factor-equality, grodner-chiral-theorem, chiral-magnetic-moments, chiral-doublet-arbitration]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [chirality, g-factor, magnetic-moments, grodner-theorem, spontaneous-symmetry-breaking, time-reversal-breaking, 128cs-benchmark]
---

# Chiral doublet magnetic moment g-factor equality theorem and spurious band arbitration

## Definition

### The Grodner Chiral $g$-Factor Equality Relation

A major challenge in high-spin nuclear spectroscopy is that accidental degeneracies (e.g. signature partner bands, shape coexistence, or pseudo-spin doublets) can exhibit near-identical excitation energies ($\Delta E \le 100\text{ keV}$), masquerading as chiral doublet bands.

To provide a model-sensitive test of the idealized chiral limit, E. Grodner et al. (Phys. Rev. Lett. 120, 022502, 2018; CRC 2025 Ch. 7, PDF pp. 156–166) discussed a **Chiral Gyromagnetic Factor ($g$) Equality** relation:

### 1. Quantum Symmetry Principle
In a genuine chiral nucleus, spontaneous breaking of time-reversal $\mathcal{T}$ and $\mathcal{R}_y(\pi)$ in the body-fixed frame creates degenerate left-handed $|L\rangle$ and right-handed $|R\rangle$ chiral states.
In the laboratory frame, restoration of discrete symmetry splits the system into symmetric and antisymmetric eigenstates:
$$|\text{Band 1}\rangle = \frac{|L\rangle + |R\rangle}{\sqrt{2}}, \quad |\text{Band 2}\rangle = \frac{|L\rangle - |R\rangle}{\sqrt{2}}$$

The magnetic dipole moment operator $\hat{\mu} = g_R \vec{R} + g_p \vec{j}_p + g_n \vec{j}_n$ is **odd under time reversal** ($\mathcal{T} \hat{\mu} \mathcal{T}^{-1} = -\hat{\mu}$).
Consequently, the off-diagonal matrix elements between the left- and right-handed states cancel identically:
$$\langle L \mid \hat{\mu} \mid R \rangle = \langle R \mid \hat{\mu} \mid L \rangle = 0$$
The diagonal expectation values satisfy:
$$\langle \text{Band 1} \mid \hat{\mu} \mid \text{Band 1} \rangle = \frac{1}{2} \left[ \langle L|\hat{\mu}|L\rangle + \langle R|\hat{\mu}|R\rangle \right] = \langle \text{Band 2} \mid \hat{\mu} \mid \text{Band 2} \rangle$$

**Idealized-model relation**:
$$g(\text{Band 1}, I) \equiv g(\text{Band 2}, I)$$
The $g$-factors of the two partner bands are equal in this idealized limit over the modeled spin window.
If an experimental measurement reveals \(g_1(I)\ne g_2(I)\) with a discrepancy
of at least \(3\sigma\), that result strongly disfavors the idealized equality
model for the specified spin and response contract. It is not, by itself, a
model-independent classification of the bands.

---

## Microscopic 3D Aplanar Geometry Formula

In odd-odd nuclei with proton particle $j_p$ along the short ($s$) axis, neutron hole $j_n$ along the long ($l$) axis, and core rotation $R_m$ along the intermediate ($m$) axis:
$$g_{\text{chiral}}(I) = g_R + (g_p - g_R) \frac{j_p^2}{I(I+1)} + (g_n - g_R) \frac{j_n^2}{I(I+1)}$$
where:
- $g_R \approx Z / A$ is the collective rotational gyromagnetic ratio;
- $g_p \approx 1.25 - 1.35$ for $h_{11/2}$ protons;
- $g_n \approx -0.15 - -0.25$ for $h_{11/2}$ neutron holes.

---

## Statistical Arbitration Criterion

Given experimental measurements $g_1 \pm \sigma_1$ and $g_2 \pm \sigma_2$:
$$\Delta g = |g_1 - g_2|, \quad \sigma_{\Delta g} = \sqrt{\sigma_1^2 + \sigma_2^2}$$
$$\chi^2_g = \left( \frac{\Delta g}{\sigma_{\Delta g}} \right)^2, \quad p = \text{erfc}\left( \sqrt{\frac{\chi^2_g}{2}} \right)$$
- $\chi^2_g \le 1.0$: compatible with the equality model under the declared
  independent-error approximation;
- $1.0 < \chi^2_g \le 4.0$: Compatible within $2\sigma$;
- $\chi^2_g \ge 9.0$: the equality model is disfavored at the nominal
  $>99.73\%$ ($3\sigma$) level under the declared independent-error
  approximation; this is not a model-independent chiral rejection.

---

## Canonical Experimental Benchmarks

1. **$^{128}\text{Cs}$ Chiral Doublet Benchmark (Grodner et al. PRL 2018)**:
   - Measured $g$-factors at $I = 11^+$:
     $$g(\text{Band 1}) = +0.58 \pm 0.04, \quad g(\text{Band 2}) = +0.56 \pm 0.05$$
   - $\Delta g = 0.020 \pm 0.064 \implies \chi^2_g = 0.098$ ($0.31\sigma$ discrepancy, $p = 0.755$);
   - Supports the equality model for this measurement, while leaving the
     chiral geometry and its competing interpretations to the full
     electromagnetic evidence chain.
2. **Spurious Pseudo-Chiral Counterexample**:
   - Experimental doublet with $g_1 = +0.85 \pm 0.04$ and $g_2 = +0.32 \pm 0.05$:
   - $\Delta g = 0.530 \pm 0.064 \implies \chi^2_g = 68.51$ ($8.28\sigma$ discrepancy, $p = 1.26 \times 10^{-16}$);
   - Strongly disfavors the equality model for this constructed counterexample;
     it does not by itself classify the bands.

---


## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该关系作为理想化模型的可检验约束；相等结果支持该约束但不能单独建立手征性，不相等结果也需要结合组态、偏振、寿命和响应合同解释。

## Sources

### 参考文献与交叉引用


- **Grodner, E. et al.**: *Partner bands in $^{128}\text{Cs}$ as the first identification of chiral doublet bands by magnetic moment measurements*, Phys. Rev. Lett. 120, 022502 (2018).
- **Grodner, E.**: *Experimental Evidence of Chirality in $^{126,128}\text{Cs}$*, in *Chirality and Wobbling in Atomic Nuclei*, CRC Press (2025), Chapter 7, PDF pp. 156–166.
- **Frauendorf, S.**: *Spontaneous symmetry breaking in rotating nuclei*, Rev. Mod. Phys. 73, 463–514 (2001).


## Necessary Assumptions

微观平均场假定核子在有效单体势中运动，通过剩余相互作用自洽诱发四极形变与集体转动。


## Discriminating Observables

激发能量级间距、跃迁多极性比值与电磁约化跃迁几率是关键鉴别观测量。


## Supporting Evidence

在束伽马谱学实验测定的角分布、DCO比值与能级寿命提供直接实证。
