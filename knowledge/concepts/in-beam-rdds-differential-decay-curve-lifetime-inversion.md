---
type: concept
title: "In-beam recoil distance Doppler-shift (RDDS) differential decay curve method (DDCM) picosecond lifetime inversion and transition collectivity B(E2)"
aliases: [rdds-ddcm-lifetime, ddcm-plunger-inverter, differential-decay-curve, dewald-ddcm-lifetime, rdds-plateau-arbitration]
created: 2026-11-04
updated: 2026-11-04
status: ai-draft
review_status: unreviewed
tags: [in-beam-spectroscopy, lifetime-measurement, rdds, plunger, ddcm, b-e2, picosecond-lifetimes, 134ce]
---

# In-beam recoil distance Doppler-shift (RDDS) differential decay curve method (DDCM) picosecond lifetime inversion and transition collectivity B(E2)

## Definition

### Definition and Phenomenological Origin

The Recoil Distance Doppler-Shift (RDDS) or plunger method is the definitive experimental technique for measuring excited nuclear state lifetimes in the range $\tau \sim 1 - 200\text{ ps}$.
In an in-beam experiment, compound nuclei recoil from a thin target at velocity $v = \beta c$ ($\beta \sim 1\% - 4\%$) towards an adjustable metallic stopper foil separated by distance $d$.

Based on 吴治华《原子核物理实验方法》第 15 章 §15.2 (pp. 430–445), 汪晓莲《粒子探测技术》第 5 章, A. Dewald et al. (Z. Phys. A 334, 163, 1989), and A. Dewald et al. (Prog. Part. Nucl. Phys. 67, 786, 2012):
The measured $\gamma$-ray spectrum exhibits two resolved Doppler components:
1. **Flight / Shifted Peak ($I_s(d)$)**: Emitted in flight before striking the stopper ($E_s = E_0(1 + \beta\cos\theta)$);
2. **Stopped / Unshifted Peak ($I_u(d)$)**: Emitted after coming to rest inside the stopper ($E_u = E_0$).

---

## Mathematical Formalism: Differential Decay Curve Method (DDCM)

### 1. Bateman Differential Rate Equation
Traditional integral centroid-shift methods suffer from systematic overestimation when unknown slow side-feeding cascades are present.
The Dewald DDCM formulation solves the differential rate balance directly:
$$\frac{d I_u(d)}{dd} = \frac{1}{v\tau} \left[ I_s(d) - \sum_k b_k I_{s, k}^{\text{feed}}(d) \right]$$
In coincidence or gated data where higher feeding is accounted for, the point-by-point lifetime is:
$$\tau(d) = \frac{1}{v} \cdot \frac{1 - R(d)}{\frac{dR(d)}{dd}}$$
where $R(d) = \frac{I_u(d)}{I_u(d) + I_s(d)}$ is the normalized stopped-peak intensity ratio.

### 2. Plateau Region Arbitration & B(E2) Extraction
In the sensitive flight domain where $0.15 \le R(d) \le 0.85$, $\tau(d)$ forms a horizontal plateau strictly independent of feeding delays.
The weighted average plateau lifetime $\bar{\tau}$ yields model-independent transition observables:
- **Transition Rate**: $T(E2) = 1 / \bar{\tau}$ [$\text{s}^{-1}$];
- **Reduced Transition Probability**:
  $$B(E2; I \to I-2) = \frac{1}{1.225 \times 10^{13} \cdot E_{\gamma}^5 \cdot \bar{\tau}} \quad [e^2\text{b}^2] \quad (E_\gamma \text{ in MeV, } \bar{\tau} \text{ in s})$$
- **Transition Intrinsic Quadrupole Moment**:
  $$Q_0 = \sqrt{ \frac{16\pi}{5} \frac{B(E2; I \to I-2)}{\langle I 2 K 0 | I-2, K \rangle^2} } \quad [e\text{ b}]$$

---

## Executable Analysis Tool: `rddsddcm`

The Python analysis suite integrates `in_beam_rdds_ddcm_lifetime_inverter.py`, accessible via:

```bash
# Benchmark 1: 134Ce 2+_1 -> 0+ (409 keV) plunger measurement (beta = 0.0210)
python3 system/scripts/analysis/nuclear_analyzer.py rddsddcm --preset 134Ce_2plus_rdds_plunger

# Benchmark 2: 128Cs chiral bandhead 9+ (280 keV) plunger lifetime (beta = 0.0185)
python3 system/scripts/analysis/nuclear_analyzer.py rddsddcm --preset 128Cs_chiral_bandhead_lifetime

# Benchmark 3: Short-lived rapid decay limit (tau ~ 3.2 ps)
python3 system/scripts/analysis/nuclear_analyzer.py rddsddcm --preset rapid_decay_short_lifetime_limit
```

### Benchmark Validation: $^{134}\text{Ce}$ $2_1^+ \to 0^+$ ($409.0\text{ keV}$)
- Recoil velocity $v = 6.296\ \mu\text{m/ps}$ ($\beta = 0.0210$);
- Evaluates $R(d)$ across 8 distances ($12 - 350\ \mu\text{m}$);
- Plateau region ($R \in [0.21, 0.87]$, 5 distances) extracts lifetime $\bar{\tau} = 14.92 \pm 0.04\text{ ps}$;
- Deduces collective quadrupolarity $B(E2) = 0.4780\ e^2\text{b}^2$ ($123.8\text{ W.u.}$) and intrinsic quadrupole moment $Q_0 = 4.90\ e\text{ b}$.


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
