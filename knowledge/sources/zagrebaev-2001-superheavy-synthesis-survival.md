---
type: source
title: "Zagrebaev et al. 2001 - Synthesis of superheavy nuclei: How accurately can we describe it and calculate the cross sections?"
aliases: [Zagrebaev 2001 superheavy survival, superheavy multi-chance fission survival, ZAG01]
created: 2026-10-30
updated: 2026-10-30
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Synthesis of superheavy nuclei: How accurately can we describe it and calculate the cross sections?"
authors: [V. I. Zagrebaev, Y. Aritomo, M. G. Itkis, Yu. Ts. Oganessian, M. Ohta]
journal: Physical Review C
year: 2001
volume: 65
issue: 1
pages: "014607"
doi: "10.1103/PhysRevC.65.014607"
canonical_source: "https://doi.org/10.1103/PhysRevC.65.014607"
citation_key: zagrebaev2001superheavy
nuclei: [208pb, 248cm, 292114, 294116, 298114, 304120]
reactions: ["48Ca + 248Cm -> 296-x 116 + xn", "48Ca + 244Pu -> 292-x 114 + xn"]
experiments: [Dubna-FLNR-DGAS]
models: [multidimensional-langevin, statistical-model, Bohr-Wheeler-fission, Ignatyuk-level-density]
observables: [evaporation-residue-cross-section, survival-probability, fission-barrier, gamma-f-over-gamma-n]
methods: [coupled-channels-capture, Langevin-trajectory-simulation, multi-chance-fission-cascade]
tags: [superheavy-elements, multi-chance-fission, survival-probability, fission-barrier-inversion, Day27]
---

# Synthesis of superheavy nuclei: How accurately can we describe it and calculate the cross sections?

## Bibliographic Record

PRC 65, 014607 (2001), DOI `10.1103/PhysRevC.65.014607`.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: Unified theoretical framework for the synthesis of superheavy nuclei via hot fusion reactions ($^{48}\text{Ca}$ on actinide targets); multidimensional Langevin dynamics for capture and fusion into the compound nucleus; statistical model de-excitation of the hot compound nucleus competing against fission; calculation of $\Gamma_n / \Gamma_f$ ratios incorporating thermal damping of shell corrections; derivation of the multi-chance fission survival probability $W_{\text{surv}}(E^*)$; comparison with Dubna gas-filled separator (DGAS) experimental cross sections.
- Not covered: Cold fusion dynamics with $^{208}\text{Pb}$ targets.
- Coverage caveats: Focuses on the de-excitation and survival phase of superheavy compound systems.

## Key Findings and Claims

| Claim ID | Claim Summary | Evidence Type | Direct/Derived | Locator | Review Flag |
|---|---|---|---|---|---|
| ZAG01-1 | 在超重复合核（如 $^{296}116, ^{292}114$）中，由于宏观液滴裂变势垒完全归零，裂变势垒完全由微观壳修正能提供（$B_f(0) \approx 5.5 - 6.5\text{ MeV}$），其绝对值系统性低于中子分离能（$S_n \approx 7.0 - 7.5\text{ MeV}$），构成了**裂变势垒反转（$B_f < S_n$）**。 | model-result | direct | Sec. III.A, Fig. 8 | false |
| ZAG01-2 | 随着复合核激发能上升（$E^* \sim 30 - 45\text{ MeV}$，温度 $T \sim 1.2 - 1.5\text{ MeV}$），微观壳效应发生热阻尼消融（Ignatyuk 因子 $\exp(-E^*/E_d)$），导致有限温度裂变势垒暴跌至 $B_f(T) \le 1.5\text{ MeV}$。 | model-result | direct | Sec. III.B, Eq. (14) | false |
| ZAG01-3 | 势垒反转与热阻尼协同诱发雪崩式**多次裂变竞争（Multi-Chance Fission）**：每一个中子蒸发步长中，裂变分支比高达 $\Gamma_f / \Gamma_n \approx 10^2 - 10^3$，仅有不足 $1\%$ 的几率蒸发中子生存。 | model-result | direct | Sec. IV.A, Fig. 12 | false |
| ZAG01-4 | 经由 $3n$ 或 $4n$ 蒸发级联后，超重蒸发剩余核（ER）的总生存几率被极度压缩至 $W_{\text{surv}} \sim 10^{-6} - 10^{-8}$，将反应截面压制至皮靶（picobarn, pb）量级。 | model-result | direct | Sec. IV.B, Table 1 | false |

## Cross-Mass-Region Transferability Significance

1. **稳定核统计蒸发模型向超重区平移的彻底失效**：在稳定核（如 $^{208}\text{Pb}$）中 $B_f \gg S_n$，中子蒸发占绝对主导（$\Gamma_n / \Gamma_{\text{tot}} \sim 1$）；直接套用稳定核或轻锕系统计代码会严重高估超重核生成截面达 $10^4 - 10^6$ 倍。
2. **微观热相变与动力学耗散的双重控制**：形式化了超重核生存能力完全取决于复合核在达到鞍点前中子蒸发速率与热壳能耗散速率的微观赛跑。
