---
type: source
title: "Rohozinski et al. 1988 - The collective 1+ state in triaxial nuclei"
aliases: [Rohozinski 1988 triaxial scissors mode, scissors mode splitting triaxiality, ROH88]
created: 2026-10-30
updated: 2026-10-30
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "The collective 1+ state in triaxial nuclei"
authors: [S. G. Rohozinski, D. Troltenier, J. A. Maruhn, W. Greiner]
journal: Zeitschrift für Physik A Atomic Nuclei
year: 1988
volume: 330
issue: 3
pages: "241-248"
doi: "10.1007/bf01287259"
canonical_source: "https://doi.org/10.1007/bf01287259"
citation_key: rohozinski1988triaxialscissors
raw_file: "raw/papers/gpt/learning-daily/20261031-OPEN-RESEARCH-source-recovery/BF01287259.pdf"
raw_sha256: 3a8c54033a22443700329bf860d0ca5d51b7ec34ab3193dd059f426d23228abc
nuclei: [156gd, 160er, 164dy, 134ce, 192os]
reactions: []
experiments: []
models: [two-rotor-model, triaxial-collective-model, QRPA]
observables: [B-M1, excitation-energy, scissors-energy-splitting, gamma-deformation-dependence]
methods: [triaxial-two-rotor-formalism, normal-coordinate-transformation, M1-transition-matrix]
tags: [scissors-mode, triaxial-deformation, energy-splitting, two-rotor, K-degeneracy-breaking, Day27]
---

# The collective 1+ state in triaxial nuclei

## Bibliographic Record

Z. Phys. A 330, 241-248 (1988), DOI `10.1007/BF01287259`.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: Extension of the Two-Rotor Model (TRM) to nuclei with non-axial triaxial deformation ($\gamma \ne 0^\circ$); derivation of the kinetic energy tensor and harmonic restoring potential for coupled proton and neutron ellipsoids; proof of the breaking of the $K=1$ scissors mode degeneracy; analytical expressions for the energy splitting $\Delta \omega$ and transition probabilities $B(M1)_1, B(M1)_2$ to the two split $1^+$ states; application to transitional rare-earth ($^{160}\text{Er}$) and $\gamma$-soft ($^{192}\text{Os}$) nuclei.
- Not covered: Microscopic shell-model core polarization.
- Coverage caveats: Focuses on the collective orbital mode.

## Key Findings and Claims

| Claim ID | Claim Summary | Evidence Type | Direct/Derived | Locator | Review Flag |
|---|---|---|---|---|---|
| ROH88-1 | 在具有静态三轴形变（$\gamma \ne 0^\circ$）或大振幅 $\gamma$ 软度的原子核中，绕两主垂直横轴（中轴与短轴）的转动惯量解除简并，导致轴对称核中简并的 $K=1$ 剪刀模分裂为两个物理性质不同的 $1^+$ 本征振动分支。 | model-result | direct | Sec. 2, Eqs. (12)-(15) | false |
| ROH88-2 | 两个剪刀分立峰的能量差 $\Delta E_{\text{split}} = |\omega_1 - \omega_2|$ 在领先级近轴对称展开下直接正比于三轴参数：$\Delta E_{\text{split}} \approx \frac{2}{\sqrt{3}} E_{\text{sc}} \tan\gamma$。 | method/formalism | direct | Sec. 3, Eq. (24) | false |
| ROH88-3 | 在中等三轴核（$\gamma \sim 20^\circ - 25^\circ$）中，理论导出能级劈裂可达 $0.8 - 1.2\text{ MeV}$，使原本集中于 $3.0\text{ MeV}$ 的单一剪刀峰分裂为分别处于 $\sim 2.4\text{ MeV}$（绕短轴反相摆动）与 $\sim 3.4\text{ MeV}$（绕中轴反相摆动）的非对称双峰。 | model-result | direct | Sec. 3, Table 1 | false |
| ROH88-4 | 两个分裂 $1^+$ 态的磁偶极辐射强度 $B(M1)_1$ 与 $B(M1)_2$ 满足总求和规则分配：$B(M1)_1 / B(M1)_2 \approx \cot^2(\gamma + 30^\circ)$，呈现强烈的非对称分支比。 | model-result | direct | Sec. 4, Eq. (31) | false |

## Cross-Mass-Region Transferability Significance

1. **单洛伦兹剪刀模强度函数的模型迁移边界**：该三轴转子模型显示，将轴对称转子的单峰参数直接套用到三轴或 $\gamma$-软核区可能产生错误的双峰/展宽解释；这是一条形式模型的迁移警告，不是对 `^{134}Ce` 或 `^{192}Os` 已测双峰的证明。
2. **三轴度 $\gamma$ 的模型敏感 observable**：在该形式中，低激发态 `1+` 的能量劈裂和分支比对 $\gamma$ 敏感；它们可作为实验设计候选，但不能脱离 response、背景和竞争模型直接称为独立的基态 $\gamma$ 测量。

## Summary

本页摘要以现有书目、原有正文和已有 claim 表为准；本次补齐结构，不新增来源事实。

## Key Results


| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ROH88-1 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | model-result | source-reported | Sec. 2, Eqs. (12)-(15) | false |
| ROH88-2 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | \omega_1 - \omega_2 | source-reported | method/formalism | direct |
| ROH88-3 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | model-result | source-reported | Sec. 3, Table 1 | false |
| ROH88-4 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | model-result | source-reported | Sec. 4, Eq. (31) | false |

原页面既有的直接报告、作者解释和模型结果保持原文分层；缺失 locator 或原件的项目仍保持相应证据边界。

## Competing Interpretations and Limitations

竞争解释、来源依赖、原件访问和必要伴随观测缺口按原页面记录；不得把模型结果或评价字段升级为直接实验事实。

## Extracted Pages

本页当前只保留已有 locator；未取得的原始页码、图表或附件不补写，后续摄入必须记录实际阅读范围。
