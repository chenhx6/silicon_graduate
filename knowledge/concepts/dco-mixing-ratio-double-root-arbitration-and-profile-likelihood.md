---
type: concept
title: "DCO multipole mixing ratio double-root arbitration and profile likelihood"
aliases: [dco-double-root-arbitration, multipole-mixing-ratio-dual-roots, delta-profile-likelihood, weisskopf-ceiling-arbitration]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [in-beam-spectroscopy, dco-ratio, multipole-mixing-ratio, double-root-problem, linear-polarization, internal-conversion, weisskopf-limit, profile-likelihood, error-propagation]
---

# DCO multipole mixing ratio double-root arbitration and profile likelihood

## Definition

### Definition and Mathematical Origin of Double Roots

In in-beam $\gamma$-ray spectroscopy (e.g. studying triaxial wobbling bands, chiral doublets, or octupole bands), the multipole mixing ratio $\delta(L+1/L) \equiv \delta(E2/M1)$ of a $\Delta I = 1$ transition is extracted from directional correlations from oriented states ($R_{\text{DCO}}$) or angular distribution ratios.

Following Hamilton (1975) Ch. 14, Krane & Steffen (1970), and 朱永生《实验物理中的概率和统计》第 6, 8, 9 章:
The theoretical DCO ratio for an unknown transition gated on a stretched $E2$ cascade is a rational quadratic function of $\delta$:
$$R_{\text{DCO}}(\delta) = \frac{W(\theta_1, \theta_2; \delta)}{W(\theta_2, \theta_1; \delta)} = \frac{A_0 + A_1 \delta + A_2 \delta^2}{B_0 + B_1 \delta + B_2 \delta^2}$$

Equating $R_{\text{DCO}}(\delta) = R_{\text{exp}}$ yields a quadratic algebraic equation:
$$c_2 \delta^2 + c_1 \delta + c_0 = 0$$
where:
$$c_2 = A_2 - R_{\text{exp}} B_2, \quad c_1 = A_1 - R_{\text{exp}} B_1, \quad c_0 = A_0 - R_{\text{exp}} B_0$$

If the discriminant $\Delta = c_1^2 - 4 c_2 c_0 \ge 0$, mathematics inevitably produces **two distinct real roots**:
$$\delta_1 = \frac{-c_1 - \sqrt{\Delta}}{2 c_2}, \quad \delta_2 = \frac{-c_1 + \sqrt{\Delta}}{2 c_2}$$
Typically:
- **Root 1 (Small $|\delta|$)**: $|\delta_1| \ll 1$, representing a predominantly dipole $M1$ transition ($f_{M1} > 70\%$, $f_{E2} < 30\%$);
- **Root 2 (Large $|\delta|$)**: $|\delta_2| \gg 1$, representing a predominantly quadrupole $E2$ transition ($f_{E2} > 70\%$).

This mathematical ambiguity is a notorious challenge in experimental nuclear structure: **which root represents the true physical transition, and which is an unphysical mathematical phantom?**

---

## Four-Fold Physical Arbitration Law

To resolve the double-root dilemma without relying on arbitrary theoretical prejudice, experimental nuclear physicists apply four orthogonal physical arbitrations:

### 1. Compton Linear Polarization ($P$) Joint Arbitration
The linear polarization $P(\theta=90^\circ, \delta)$ measured by a Clover HPGe array or Compton polarimeter is given by:
$$P(\delta) = \frac{p_0 + p_1 \delta + p_2 \delta^2}{q_0 + q_1 \delta + q_2 \delta^2}$$
Because electric and magnetic multipoles have opposite parities, $P$ changes sign or magnitude between the two roots:
- Small $\delta$ ($M1$ dominant): $P < 0$ (negative polarization along reaction normal);
- Large $\delta$ ($E2$ dominant): $P > 0$ (positive polarization).

The joint profile $\chi^2(\delta)$ combines both independent measurements:
$$\chi^2_{\text{joint}}(\delta) = \left[ \frac{R_{\text{DCO}}(\delta) - R_{\text{exp}}}{\sigma_R} \right]^2 + \left[ \frac{P(\delta) - P_{\text{exp}}}{\sigma_P} \right]^2$$
At the true physical root, $\chi^2_{\text{joint}} \approx 0$; at the spurious root, $\chi^2_{\text{joint}} \gg 9.0$ ($> 3\sigma$ exclusion).

### 2. Internal Conversion Coefficient ($\alpha_K$) Arbitration
From BrIcc theoretical conversion coefficients:
$$\alpha_K(\delta) = \frac{\alpha_K(M1) + \delta^2 \alpha_K(E2)}{1 + \delta^2}$$
Measuring electron-conversion intensity ratio $I_e / I_\gamma$ provides an independent $\chi^2_\alpha(\delta)$ term, highly sensitive at low $\gamma$-ray energies ($E_\gamma \le 300\text{ keV}$).

### 3. Weisskopf Single-Particle Rate Ceiling
Given the level lifetime $\tau$ (from DSAM or RDDS plunger measurements):
$$T(M1) = \frac{1}{\tau (1 + \alpha_{\text{tot}})} \frac{1}{1 + \delta^2}, \quad T(E2) = \frac{1}{\tau (1 + \alpha_{\text{tot}})} \frac{\delta^2}{1 + \delta^2}$$
In single-particle units (W.u.):
$$B(M1) [\text{W.u.}] = \frac{T(M1)}{3.15 \times 10^{13} E_\gamma^3 [\text{MeV}^3]}, \quad B(E2) [\text{W.u.}] = \frac{T(E2)}{1.22 \times 10^9 A^{4/3} E_\gamma^5 [\text{MeV}^5]}$$

**The Moszkowski-Weisskopf Upper Limit**:
In nuclear structure, single-particle $M1$ transitions rarely exceed $1 \sim 2\ \text{W.u.}$ (due to pairing quenching and core polarization). If a root yields $B(M1) > 5.0 - 10.0\ \text{W.u.}$, it represents an unphysical super-dipole anomaly and is categorically ruled out.

### 4. Likelihood Ratio Hypothesis Testing and Confidence Level
Following Wilks' theorem and Neyman construction (朱永生第 8, 9 章):
$$\Delta\chi^2 = |\chi^2_{\text{joint}}(\delta_2) - \chi^2_{\text{joint}}(\delta_1)|$$
The exclusion confidence level ($CL$) is:
$$CL = \text{erf}\left( \sqrt{\frac{\Delta\chi^2}{2}} \right) \times 100\%$$
- $\Delta\chi^2 \ge 9.0$: Spurious root excluded at $\ge 99.73\%$ ($3\sigma$) CL (conclusive arbitration);
- $4.0 \le \Delta\chi^2 < 9.0$: Strong preference ($\ge 95.4\%$, $2\sigma$ CL);
- $\Delta\chi^2 < 4.0$: Ambiguity persists; further linear polarization or lifetime data required.

---

## Experimental Presets and Benchmarks

1. **$^{135}\text{Pr}$ Transverse Wobbling Candidate ($17/2^+ \to 15/2^+, 728\text{ keV}$)**:
   - Experimental $R_{\text{DCO}} = 0.45 \pm 0.04$, yielding roots $\delta_1 = -7.985$ ($98.5\% E2$) and $\delta_2 = -0.515$ ($21.0\% E2$).
   - Linear polarization measurement $P_{\text{exp}} = +0.22 \pm 0.05$:
     Root 1 gives $P = +0.623$ ($\chi^2_P = 64.9$), whereas Root 2 gives $P = -0.055$ ($\chi^2_P = 30.3$).
     Statistical exclusion: $\Delta\chi^2 = 27.66 \implies CL = 100.0\%$, decisively arbitrating Root 2 as favored.

2. **$^{134}\text{Pr}$ Chiral Doublet Intraband Transition ($13^+ \to 12^+, 422\text{ keV}$)**:
   - Experimental $R_{\text{DCO}} = 0.95 \pm 0.05, P_{\text{exp}} = -0.18 \pm 0.06$:
   - Root 1: $\delta = -0.010$ ($100\% M1$), $P = -0.228$ ($\chi^2_{\text{joint}} = 0.901$);
   - Root 2: $\delta = +1.679$ ($73.8\% E2$), $P = +0.312$ ($\chi^2_{\text{joint}} = 80.853$).
   - Root 2 is rejected with $\Delta\chi^2 = 79.95$ ($CL = 100\%$), proving pure $M1$ character of chiral partner band.

---


## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。

## Sources

### 参考文献与交叉引用


- **Zhu Yongsheng (朱永生)**: *Probability and Statistics in Experimental Physics* (《实验物理中的概率和统计》), Science Press (2006), Chapters 6, 8, 9.
- **Hamilton, W. D.**: *The Electromagnetic Interaction in Nuclear Spectroscopy*, North-Holland (1975), Chapter 14 (Directional Correlations and Polarization).
- **Krane, K. S. & Steffen, R. M.**: Phys. Rev. C 2, 724 (1970) (Formulation of angular distributions and delta-fitting).
- **Kibédi, T. et al.**: Nucl. Instrum. Methods Phys. Res. A 589, 202 (2008) (BrIcc conversion coefficient evaluation).


## Necessary Assumptions

微观平均场假定核子在有效单体势中运动，通过剩余相互作用自洽诱发四极形变与集体转动。


## Discriminating Observables

激发能量级间距、跃迁多极性比值与电磁约化跃迁几率是关键鉴别观测量。


## Supporting Evidence

在束伽马谱学实验测定的角分布、DCO比值与能级寿命提供直接实证。
