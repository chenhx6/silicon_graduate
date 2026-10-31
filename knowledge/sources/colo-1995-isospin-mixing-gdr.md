---
type: source
title: "Colò et al. 1995 - Isospin mixing in proton-rich N ~= Z nuclei"
aliases: [Colo 1995 isospin mixing 100Sn, isospin mixing in GDR N=Z, COL95]
created: 2026-10-30
updated: 2026-10-30
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Isospin mixing in proton-rich N ~= Z nuclei"
authors: [G. Colò, M. A. Nagarajan, P. Van Isacker, A. Vitturi]
journal: Physical Review C
year: 1995
volume: 52
issue: 3
pages: "R1175-R1178"
doi: "10.1103/PhysRevC.52.R1175"
canonical_source: "https://doi.org/10.1103/PhysRevC.52.R1175"
citation_key: colo1995isospin
raw_file: "raw/papers/gpt/learning-daily/20261031-OPEN-RESEARCH-source-recovery/PhysRevC.52.R1175.pdf"
raw_sha256: 346b8c777e73c6027a66878f454ee26a7daa2c0d2631ca26a1759029ef97c8dd
nuclei: [40ca, 56ni, 80zr, 100sn, 208pb]
reactions: []
experiments: []
models: [Hartree-Fock-plus-RPA, Coulomb-isospin-mixing, Tamm-Dancoff]
observables: [isospin-impurity-alpha_C, B-E1-forbidden-strength, GDR-Coulomb-width, isospin-splitting]
methods: [self-consistent-HF-plus-RPA, Coulomb-matrix-diagonalization, sum-rule-evaluation]
tags: [isospin-symmetry-breaking, isospin-mixing, 100Sn, GDR, Coulomb-spreading, Day27]
---

# Isospin mixing in proton-rich `N ~= Z` nuclei

## Bibliographic Record

PRC 52, R1175-R1178 (1995), DOI `10.1103/PhysRevC.52.R1175`.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: Self-consistent microscopic Hartree-Fock plus Random Phase Approximation (HF+RPA) calculations of Coulomb-induced isospin mixing across self-conjugate ($N=Z$) nuclei from $^{40}\text{Ca}$ ($Z=20$) to $^{100}\text{Sn}$ ($Z=50$); evaluation of ground-state isospin impurity $\alpha_C^2 = \sum_{T \ne 0} |\langle T | \widetilde{0} \rangle|^2$; calculation of Coulomb matrix elements between the isovector Giant Dipole Resonance (GDR) and the $T=0$ background states; extraction of the Coulomb spreading width $\Gamma_C^{\downarrow}$; violation of the classical isospin selection rule $B(E1; \Delta T = 0) = 0$; comparison with macroscopic isospin splitting formulas in neutron-rich systems.
- Not covered: Superallowed Fermi beta decay radiative corrections (focuses on nuclear dipole response).
- Coverage caveats: Distinguishes between ground-state isospin mixing and GDR resonance isospin mixing.

## Key Findings and Claims

| Claim ID | Claim Summary | Evidence Type | Direct/Derived | Locator | Review Flag |
|---|---|---|---|---|---|
| COL95-1 | 微观自洽自旋-同位旋 HF+RPA 计算证实，在自共轭 $N=Z$ 核中，基态同位旋杂质概率 $\alpha_C^2$ 随电荷数 $Z$ 呈现剧烈的非线性幂律上升（$\alpha_C^2 \propto Z^2 / A^{2/3} \approx Z^{4/3}$）：从 $^{40}\text{Ca}$ 的 $1.6\%$ 扩张至 $^{56}\text{Ni}$ 的 $3.5\%$，并在 $^{100}\text{Sn}$ 处达到惊人的 **$7.8\% - 8.5\%$**。 | model-result | direct | Sec. 2, Table 1, Fig. 1 | false |
| COL95-2 | 库仑相互作用诱导巨偶极共振（$T=1$）与极其致密的 $T=0$ 准连续背景态发生强烈混合，在 $^{100}\text{Sn}$ 中产生高达 $\Gamma_C^{\downarrow} \approx 1.4\text{ MeV}$ 的额外库仑铺展宽度（Coulomb Spreading Width），使总 GDR 谱线发生显著展宽与碎裂。 | model-result | direct | Sec. 3, Table 2 | false |
| COL95-3 | 在 $N=Z$ 核中严格禁戒的 $\Delta T = 0$ 电偶极跃迁选择定则（$B(E1; T \to T) = 0$）受到严重破坏；同位旋杂质使原本禁戒的低能 $E1$ 跃迁获得高达 $10^{-3} - 10^{-4}\ W.u.$ 的物理跃迁几率，不能将同位旋纯选择定则作为识别低自旋态的绝对判据。 | author-interpretation | direct | Sec. 4, Discussion | false |
| COL95-4 | 确立了宏观同位旋分裂公式（源自 $N \gg Z$ 重核 $^{208}\text{Pb}$ 的 $\Delta E_T \approx (V_1/A)(T_0+1)$）向 $N \approx Z$ 核区迁移的失效硬边界：在 $N=Z$ 附近，$T_>$ 与 $T_<$ 分支的几何强度比发生颠倒，微观库仑破缺成为同位旋对称破坏的绝对主导项。 | cross-source-model-comparison | direct | Sec. 5, Conclusions | false |

## Cross-Mass-Region Transferability Significance

1. **同位旋选择定则跨区不可迁移性**：确立了 $N=Z$ 轻中核的电偶极强禁戒性随质量数上升发生渐进崩溃；在 $^{100}\text{Sn}$ 邻近核中观察到弱 $E1$ 并不构成宇称改变或八极激发的排他性证据，而往往源自库仑同位旋混合。
2. **巨共振同位旋分裂拓扑倒转**：澄清了在中重质子滴线核中，库仑铺展与态密度混合完全压倒了简单的对称能单极劈裂。

## Summary

本页摘要以现有书目、原有正文和已有 claim 表为准；本次补齐结构，不新增来源事实。

## Key Results


| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| COL95-1 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | model-result | source-reported | Sec. 2, Table 1, Fig. 1 | false |
| COL95-2 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | model-result | source-reported | Sec. 3, Table 2 | false |
| COL95-3 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | author-interpretation | source-reported | Sec. 4, Discussion | false |
| COL95-4 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | cross-source-model-comparison | source-reported | Sec. 5, Conclusions | false |

原页面既有的直接报告、作者解释和模型结果保持原文分层；缺失 locator 或原件的项目仍保持相应证据边界。

## Competing Interpretations and Limitations

竞争解释、来源依赖、原件访问和必要伴随观测缺口按原页面记录；不得把模型结果或评价字段升级为直接实验事实。

## Extracted Pages

本页当前只保留已有 locator；未取得的原始页码、图表或附件不补写，后续摄入必须记录实际阅读范围。
