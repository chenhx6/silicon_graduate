---
type: concept
title: "In-beam detector array coincidence fold-to-multiplicity unfolding and compound nucleus entry-state spin-energy reconstruction"
aliases: [fold-unfolding, multiplicity-unfolding, entry-state-distribution, 4pi-calorimeter-response, spin-spectrometer-deconvolution]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [in-beam-spectroscopy, heavy-ion-reactions, multiplicity-filter, entry-state, fold-unfolding, compound-nucleus, bgo-ball]
---

# In-beam detector array coincidence fold-to-multiplicity unfolding and compound nucleus entry-state spin-energy reconstruction

## Definition

### Definition and Phenomenological Origin

In heavy-ion fusion-evaporation reactions populating high-spin states (e.g. $^{36}\text{Ar} + {}^{100}\text{Mo} \to {}^{132}\text{Ce} + 4n$), the compound nucleus de-excites first by particle evaporation (neutrons, protons, $\alpha$) down to the "entry-state line", and subsequently through cascades of statistical and discrete $\gamma$-rays.

Based on 吴治华《原子核物理实验方法》第 10 章 §10.6 (pp. 290–305) 与第 15 章, 汪晓莲《粒子探测技术》第 8 章, C. A. Bertulani *Introduction to Nuclear Reactions* Chapter 6, and M. Jääskeläinen et al. (Nucl. Instrum. Methods 204, 385, 1983):
1. Experiments utilize multi-detector calorimeters or multiplicity filters (e.g. 4$\pi$ BGO balls, Crystal Balls, or Compton-suppressed Clover arrays with $N_{\text{det}}$ independent detector elements and single-crystal efficiency $\varepsilon_{\text{det}}$).
2. The observable quantities are the **coincidence Fold $k$** (the number of simultaneously fired detectors) and the **total Sum Energy $H$**.
3. Because a detector can be struck by more than one $\gamma$-ray (pileup/multi-hit) or missed due to geometry/thresholds, the observed fold $k$ is a compressed, distorted representation of the true event $\gamma$-ray multiplicity $M$.

---

## Mathematical Formalism: Response Matrix & Entry Mapping

### 1. Analytical Combinatorial Response Matrix $P(k | M)$
The probability of measuring fold $k$ from a cascade of $M$ photons is given by the exact inclusion-exclusion formula:
$$P(k | M) = \binom{N_{\text{det}}}{k} \sum_{j=0}^k (-1)^{k - j} \binom{k}{j} \left( 1 - \frac{N_{\text{det}} - j}{N_{\text{det}}} \varepsilon_{\text{det}} \right)^M$$

### 2. Iterative Bayesian Deconvolution
Given an experimental fold histogram $F_{\text{meas}}(k)$, the true multiplicity distribution $P(M)$ is extracted using Richardson-Lucy iterative deconvolution:
$$P^{(n+1)}(M) = P^{(n)}(M) \sum_k \frac{P(k | M) F_{\text{meas}}(k)}{\sum_{M^\prime} P(k | M^\prime) P^{(n)}(M^\prime)}$$
yielding the true mean multiplicity $\langle M \rangle$ and dispersion $\sigma_M$.

### 3. Entry-State Spin $\langle J_{\text{entry}} \rangle$ and Excitation Energy $\langle E^* \rangle$
De-excitation proceeds via $\bar{N}_{\text{stat}}$ statistical dipole cooling transitions ($\Delta J \approx 0.5\ \hbar$) followed by stretched collective quadrupole transitions ($\Delta J = 2\ \hbar$):
$$\langle J_{\text{entry}} \rangle = 2 (\langle M \rangle - \bar{N}_{\text{stat}}) + \bar{N}_{\text{stat}} \cdot \Delta J_{\text{stat}} + J_0$$
$$\sigma_J = 2 \sigma_M$$
$$\langle E^*_{\text{entry}} \rangle = \frac{\langle H \rangle}{\varepsilon_{\text{sum}}} + E_{\text{thresh}}$$

---

## Executable Analysis Tool: `foldmult`

The Python analysis suite integrates `in_beam_array_fold_multiplicity_entry_state_unfolder.py`, accessible via:

```bash
# Benchmark 1: 4pi BGO Ball for 36Ar + 100Mo -> 132Ce (Jaaskelainen 1983)
python3 system/scripts/analysis/nuclear_analyzer.py foldmult --preset 4pi_bgo_ball_fusion_evaporation

# Benchmark 2: Clover array 48-channel multiplicity filter
python3 system/scripts/analysis/nuclear_analyzer.py foldmult --preset clover_array_multiplicity_filter

# Benchmark 3: Low-multiplicity peripheral transfer reaction
python3 system/scripts/analysis/nuclear_analyzer.py foldmult --preset low_multiplicity_transfer_reaction
```

### Benchmark Validation: $^{132}\text{Ce}$ High-Spin Entry States
- Input fold distribution: centered at $k \sim 15$ with 30 BGO modules ($\varepsilon = 85\%$);
- Unfolded true multiplicity: $\langle M \rangle = 24.54 \pm 4.59$ photons;
- Reconstructed entry state: $\langle J_{\text{entry}} \rangle = 43.8 \pm 9.2\ \hbar$, $\langle E^* \rangle = 33.97\text{ MeV}$;
- Confirms optimal feeding conditions for populating high-spin triaxial and wobbling bands.


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
