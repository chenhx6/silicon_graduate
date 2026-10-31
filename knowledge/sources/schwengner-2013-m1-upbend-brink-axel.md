---
type: source
title: "Schwengner et al. 2013 - Low-Energy Enhancement of Magnetic Dipole Radiation"
aliases: [Schwengner 2013 M1 upbend, Brink-Axel breakdown M1 upbend, SCH13]
created: 2026-10-30
updated: 2026-10-30
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Low-Energy Enhancement of Magnetic Dipole Radiation"
authors: [R. Schwengner, S. Frauendorf, A. C. Larsen]
journal: Physical Review Letters
year: 2013
volume: 111
issue: 23
pages: "232504"
doi: "10.1103/PhysRevLett.111.232504"
canonical_source: "https://doi.org/10.1103/PhysRevLett.111.232504"
citation_key: schwengner2013m1upbend
raw_file: "raw/papers/gpt/learning-daily/20261031-OPEN-RESEARCH-source-recovery/PhysRevLett.111.232504.pdf"
raw_sha256: d7a70974055150e736e3c07a5ba444e32e33bf41a44ada6ae8afff847520ce39
nuclei: [94mo, 95mo, 56fe, 160dy, 208pb]
reactions: []
experiments: [Oslo-Cyclotron, S-DALINAC]
models: [shell-model, tilted-axis-cranking, quasi-continuum-M1]
observables: [gamma-ray-strength-function, B-M1-transition-rate, level-density, low-energy-upbend]
methods: [large-scale-shell-model, TAC-shears-recoupling, GSF-deconvolution]
tags: [gamma-ray-strength-function, brink-axel-breakdown, M1-upbend, TAC, shears-recoupling, Day27]
---

# Low-Energy Enhancement of Magnetic Dipole Radiation

## Bibliographic Record

PRL 111, 232504 (2013), DOI `10.1103/PhysRevLett.111.232504`.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: Large-scale shell-model calculations of radiative transition rates in $^{94}\text{Mo}$ and $^{95}\text{Mo}$ up to high excitation energies ($E_x \sim 10\text{ MeV}$); extraction of the $\gamma$-ray strength function (GSF) as a function of transition energy $E_\gamma$ and excitation energy $E_x$; semiclassical TAC interpretation based on shears-like recoupling of transverse magnetic moments; comparison with experimental Oslo-method data; investigation of the validity and failure conditions of the Brink-Axel hypothesis.
- Not covered: Statistical neutron capture Hauser-Feshbach reaction calculations.
- Coverage caveats: Focuses on the dipole component $f(E_\gamma) = \langle \Gamma_{\gamma} \rangle / (D \cdot E_\gamma^3)$ in the quasi-continuum.

## Key Findings and Claims

| Claim ID | Claim Summary | Evidence Type | Direct/Derived | Locator | Review Flag |
|---|---|---|---|---|---|
| SCH13-1 | 大规模壳模型计算证实，在激发态（$E_x > 3\text{ MeV}$）的准连续谱跃迁中，磁偶极辐射强度在低能端（$E_\gamma < 2.5\text{ MeV}$）展现出剧烈的指数型抬升（Low-Energy M1 Upbend），完美重现了奥斯陆实验测得的 $f_{M1}(E_\gamma)$ 反常上升。 | model-result | direct | Sec. 1, Figs. 1-2 | false |
| SCH13-2 | 微观机制解析表明，该低能抬升源于高激发态中多个高-$j$ 准粒子（如质子 $1g_{9/2}$ 与中子 $2d_{5/2}, 1g_{7/2}$）具有巨大的横向磁偶极矩矢量 $\boldsymbol{\mu}_\perp$；相邻近简并态之间的微小取向重组通过剪刀式重耦合（Shears-like Recoupling）发射超强低能 $M1$ 辐射。 | author-interpretation | direct | Sec. 2, Fig. 3 | false |
| SCH13-3 | 这种低能 $M1$ 抬升严格依赖于母态具有高准粒子激发（$E_x > 3\text{ MeV}$），而在基态（$E_i = 0$）的吸收入射道中完全不存在；这在物理机制上决定性地打破了 Brink-Axel 假说在 $E_\gamma < 3\text{ MeV}$ 区间的普适性。 | model-result | direct | Sec. 3, Discussion | false |
| SCH13-4 | 跨质量区系统学比较表明，在重双幻核（$^{208}\text{Pb}$）与强形变转子核（$^{160}\text{Dy}$）中，超大壳隙或规则转子结构使低能 $M1$ 剪刀重耦合受到强烈空间抑制，Brink-Axel 假说在这些核中近似成立；而在中轻质量区与过渡核（$A \le 95$）中，Brink-Axel 假说发生严重系统性失效。 | cross-source-model-comparison | direct | Sec. 4, Conclusions | false |

## Cross-Mass-Region Transferability Significance

1. **Brink-Axel 假说跨区迁移的不适用性硬边界**：在核天体物理与反应截面评估中，长期假定“激发态 GSF 与基态光核吸收截面恒等”；本研究确立了该假说在 $A < 100$ 软核与开壳核中的**微观失效边界**。
2. **高能激发态新集体维度的确立**：证实了存在仅在有限温度/高激发能准连续谱中激活、但在冷基态中处于隐匿状态的新型多准粒子磁响应模式。

## Summary

本页摘要以现有书目、原有正文和已有 claim 表为准；本次补齐结构，不新增来源事实。

## Key Results


| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SCH13-1 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | model-result | source-reported | Sec. 1, Figs. 1-2 | false |
| SCH13-2 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | author-interpretation | source-reported | Sec. 2, Fig. 3 | false |
| SCH13-3 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | model-result | source-reported | Sec. 3, Discussion | false |
| SCH13-4 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | cross-source-model-comparison | source-reported | Sec. 4, Conclusions | false |

原页面既有的直接报告、作者解释和模型结果保持原文分层；缺失 locator 或原件的项目仍保持相应证据边界。

## Competing Interpretations and Limitations

竞争解释、来源依赖、原件访问和必要伴随观测缺口按原页面记录；不得把模型结果或评价字段升级为直接实验事实。

## Extracted Pages

本页当前只保留已有 locator；未取得的原始页码、图表或附件不补写，后续摄入必须记录实际阅读范围。
