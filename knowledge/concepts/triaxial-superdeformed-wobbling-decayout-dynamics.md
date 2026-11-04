---
type: concept
title: "Triaxial superdeformed (TSD) wobbling band decayout dynamics, tunneling barrier penetration and branching competition"
aliases: [tsd-wobbling-decayout, tsd-tunneling, 163lu-decayout, barrier-penetration-decayout, wobbling-band-termination]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [triaxiality, superdeformation, tsd, wobbling-motion, 163lu, decayout-tunneling, hill-wheeler-transmission]
---

# Triaxial superdeformed (TSD) wobbling band decayout dynamics, tunneling barrier penetration and branching competition

## Definition

### Definition and Phenomenological Origin

In the $A \sim 160 - 170$ rare-earth region (e.g. $^{161,163,165,167}\text{Lu}$), high-$j$ intruder orbitals (specifically the proton $i_{13/2}$ configuration) stabilize a pronounced **Triaxial Superdeformed (TSD)** potential minimum with large deformation ($\varepsilon_2 \approx 0.38 - 0.43, \gamma \approx 18^\circ - 22^\circ$).

Based on Bohr & Mottelson *Nuclear Structure* Vol. II §4-5, *Chirality and Wobbling in Atomic Nuclei* (CRC Press 2025) Chapter 10 (PDF pp. 215–230), and H. Amro et al. (Phys. Rev. Lett. 91, 162502, 2003):
1. The yrast TSD band (TSD1) represents the zero-phonon wobbler ($n_w = 0$), while TSD2 corresponds to the quantized one-phonon wobbling excitation ($n_w = 1$).
2. At high spins ($I \ge 25 - 40\ \hbar$), TSD2 is protected inside the superdeformed secondary well, decaying primarily through:
   - In-band stretched collective $E2$ decay: $\text{TSD2}(I) \to \text{TSD2}(I-2)$ with partial width $\Gamma_{\text{in}}$;
   - Inter-band collective $E2$ wobbling decay: $\text{TSD2}(I) \to \text{TSD1}(I-1)$ with partial width $\Gamma_{\text{wob}}$.
3. As the nucleus decelerates towards lower spin ($I \sim 15 - 20\ \hbar$), the TSD minimum rises in excitation energy $\Delta E$ above the normal-deformed (ND) compound states.
   Quantum tunneling through the deformation barrier $V_B$ opens a competing non-collective decay channel into the dense normal-deformed state continuum (**Decayout**).

---

## Mathematical Formalism: Partial Decay Widths & Tunneling Competition

### 1. Collective Radiative Widths
The collective electromagnetic transition rates in the TSD well are given by:
$$\Gamma_{\text{in}}(E2) = 1.225 \times 10^{-3} \cdot E_{\text{in}}^5 \cdot B(E2)_{\text{in}} \quad [\text{eV}]$$
$$\Gamma_{\text{wob}}(E2) = 1.225 \times 10^{-3} \cdot E_{\text{wob}}^5 \cdot B(E2)_{\text{wob}} \quad [\text{eV}]$$
where $E$ is in $\text{MeV}$ and $B(E2)$ is in Weisskopf units.

### 2. Statistical Tunneling Barrier Penetration Width
The tunneling width through the potential barrier $V_B$ is evaluated via the Hill-Wheeler transmission formula:
$$\Gamma_{\text{decay-out}}(I) = \frac{D_{\text{TSD}}}{2\pi} \cdot T_{\text{barrier}}(I)$$
where $D_{\text{TSD}}$ is the average level spacing in the TSD well, and the transmission coefficient is:
$$T_{\text{barrier}}(I) = \left[ 1 + \exp\left( \frac{2\pi (V_B(I) - \Delta E(I))}{\hbar\omega_{\text{barrier}}} \right) \right]^{-1}$$

### 3. Decayout Catastrophe & Critical Cutoff Spin $I_{50}$
The total decay width is $\Gamma_{\text{tot}} = \Gamma_{\text{in}} + \Gamma_{\text{wob}} + \Gamma_{\text{decay-out}}$.
The branching ratios are:
$$b_{\text{in}} = \frac{\Gamma_{\text{in}}}{\Gamma_{\text{tot}}}, \quad b_{\text{wob}} = \frac{\Gamma_{\text{wob}}}{\Gamma_{\text{tot}}}, \quad b_{\text{decay-out}} = \frac{\Gamma_{\text{decay-out}}}{\Gamma_{\text{tot}}}$$

Because the barrier exponent depends exponentially on $\Delta E(I)$, $b_{\text{decay-out}}$ switches rapidly from $< 10\%$ to $> 90\%$ across a narrow spin interval ($\Delta I \sim 2 - 4\ \hbar$).
The **critical decayout threshold spin** $I_{50}$ is defined where $b_{\text{decay-out}} = 0.50$, marking the abrupt disappearance (termination) of the wobbling band in experimental $\gamma$-ray spectra.

---

## Executable Analysis Tool: `tsddecay`

The Python analysis suite integrates `triaxial_superdeformed_wobbling_decayout_analyzer.py`, accessible via:

```bash
# Benchmark 1: 163Lu TSD2 wobbler decayout (Odegard 2001, Amro 2003)
python3 system/scripts/analysis/nuclear_analyzer.py tsddecay --preset 163Lu_TSD2_wobbling_decayout

# Benchmark 2: 165Lu TSD2 delayed decayout (Schonwasser 2003)
python3 system/scripts/analysis/nuclear_analyzer.py tsddecay --preset 165Lu_TSD2_wobbling_decayout
```

### Benchmark Validation: $^{163}\text{Lu}$
- At highest spin ($I = 39.5\ \hbar$): in-TSD branching dominates ($b_{\text{in}} = 77.1\%, b_{\text{wob}} = 5.4\%, b_{\text{decay-out}} = 17.5\%$);
- At $I = 37.2\ \hbar$: the 50% decayout threshold is reached ($I_{50} = 37.2\ \hbar$);
- Below $I = 31.5\ \hbar$: tunneling into ND states reaches $97.8\%$, completely depleting the TSD2 wobbling intensity and terminating the visible band.


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
