---
type: concept
title: "Nuclear chiral doublet electromagnetic selection rules, in-phase B(M1) staggering and inter-band M1 transition suppression"
aliases: [chiral-selection-rules, m1-staggering-phase, chiral-m1-suppression, electromagnetic-chiral-rules, koike-selection-rules]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [triaxiality, nuclear-chirality, chiral-doublets, selection-rules, m1-staggering, interband-m1, 128cs]
---

# Nuclear chiral doublet electromagnetic selection-rule screening, in-phase B(M1) staggering and inter-band M1 transition suppression

## Definition

### Definition and Phenomenological Origin

Spontaneous breaking of time-reversal-rotation symmetry $\mathcal{T}\mathcal{R}_y(\pi)$ in triaxial nuclei produces two degenerate left- and right-handed states, which quantum-mechanically superpose into partner bands with identical parity and spin sequences.

Based on *Chirality and Wobbling in Atomic Nuclei* (CRC Press 2025) Chapter 7 (E. Grodner) & Chapter 8, T. Koike, K. Starosta, I. Hamamoto (Phys. Rev. Lett. 93, 172502, 2004), and E. Grodner et al. (Phys. Rev. Lett. 97, 172501, 2006):
Energy degeneracy alone ($\Delta E(I) \le 100\text{ keV}$) is NOT a sufficient condition for chirality—shape coexistence or accident degenerate rotational bands can mimic energy similarity. Genuine chiral doublets must satisfy rigorous electromagnetic selection rules.

---

## The Three Fundamental Chiral Selection Rules

### 1. In-Phase Intra-Band $B(M1)$ Staggering
The reduced transition probabilities $B(M1; I \to I - 1)$ exhibit odd-even spin staggering parameterized by:
$$S_{M1}(I) = \frac{B(M1; I \to I - 1)}{\frac{1}{2} \left[ B(M1; I + 1 \to I) + B(M1; I - 1 \to I - 2) \right]}$$
**Criterion**: In both Band 1 and Band 2, $S_{M1}(I)$ must oscillate **in-phase**:
$$\text{sign}\left( S_{M1}^{(1)}(I) - 1.0 \right) \equiv \text{sign}\left( S_{M1}^{(2)}(I) - 1.0 \right)$$
An out-of-phase oscillation indicates that the quasiparticles align differently in the two bands (signature splitting from planar rotation), completely disproving the chiral doublet interpretation.

### 2. Intra-Band $B(E2)$ Smoothness and Equality
The in-band quadrupole transitions $B(E2; I \to I - 2)$ reflect the underlying triaxial core shape.
They must be smooth (no staggering) and match within $\le 20\% - 25\%$ between partner bands:
$$\left| \frac{B(E2; \text{Band 1}) - B(E2; \text{Band 2})}{B(E2; \text{Band 1})} \right| \le 0.25$$

### 3. Inter-Band $\Delta I = 0$ $M1$ Transition Suppression
In the laboratory frame, the symmetric and antisymmetric chiral states are:
$$|1\rangle = \frac{|L\rangle + |R\rangle}{\sqrt{2}}, \quad |2\rangle = \frac{|L\rangle - |R\rangle}{\sqrt{2}}$$
The inter-band magnetic dipole transition matrix element is:
$$\langle 1 | \hat{\mu} | 2 \rangle = \frac{1}{2} \left[ \langle L | \hat{\mu} | L \rangle - \langle R | \hat{\mu} | R \rangle \right]$$
Since time-reversal symmetry dictates $\langle L | \hat{\mu} | L \rangle = \langle R | \hat{\mu} | R \rangle$, the matrix element vanishes at exact degeneracy:
$$B(M1; \text{Band 2}(I) \to \text{Band 1}(I)) \xrightarrow{\Delta E \to 0} 0 \quad (\text{Deep Minimum})$$

---

## Executable Analysis Tool: `chirrules`

The Python analysis suite integrates `chiral_doublet_selection_rules_m1_staggering_arbitrator.py`, accessible via:

```bash
# Published-strength-derived fixture 1: 128Cs (Grodner 2006, Koike 2004)
python3 system/scripts/analysis/nuclear_analyzer.py chirrules --preset 128Cs_chiral_doublet_benchmark

# Published-strength-derived fixture 2: 134Pr (Tonev 2006)
python3 system/scripts/analysis/nuclear_analyzer.py chirrules --preset 134Pr_chiral_doublet_benchmark

# Counterexample: Planar bands with out-of-phase M1 staggering
python3 system/scripts/analysis/nuclear_analyzer.py chirrules --preset spurious_out_of_phase_counterexample
```

### Derived fixture screening: $^{128}\text{Cs}$
- The hardcoded fixture gives 100% in-phase agreement across the tested rows;
- Mean fixture $B(E2)$ discrepancy is $4.8\%$;
- The smallest fixture inter-band $B(M1)$ value is $0.040\ \mu_N^2$;
- The output is a `heuristic_score_pct` and `selection-rule-screening-pass`, not a confidence estimate or chirality confirmation.

## Evidence boundary

The CLI presets are `published-strength-derived-hardcoded-fixture` values, while the
counterexample is a `synthetic-test-fixture`. They are retained to test the arithmetic
screening path. They do not load raw spectra, source tables, line-by-line locators,
covariance, configuration assignments, or independent geometry observables.

The source chain must keep experiment, author interpretation, and model result separate.
Grodner's reported $B(E2)$/$B(M1)$ values are derived through lifetime, branching,
side-feeding, and multipolarity assumptions. Koike's selection rule is a model result and
does not by itself establish non-coplanar chiral geometry. Current outputs should be
marked `derived` or `selection-rule-screening-pass`, with `needs_review: true` for
paper-facing use.


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

本 Wiki 将该页面作为选择规则和证据边界的说明。当前 CLI 只提供启发式筛选和
测试 fixture，不自动裁决手征性，也不把硬编码或派生强度写成实验确认。


## Sources

- [[triaxial-collective-modes-unified-theory-and-spectroscopy]]
- [[nuclear-spectroscopy-and-structure-master-field-manual]]
