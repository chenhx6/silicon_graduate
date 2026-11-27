---
type: source
title: "Colò et al. 1995 - Isospin mixing in proton-rich N ~= Z nuclei"
aliases: [Colo 1995 isospin mixing 100Sn, ground-state isospin impurity via IVGMR, COL95]
created: 2026-10-30
updated: 2026-11-27
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
nuclei: [40ca, 80zr, 99in, 99sn, 100sn]
reactions: []
experiments: []
models: [Hartree-Fock-plus-RPA, Coulomb-isospin-mixing, Tamm-Dancoff]
observables: [ground-state-isospin-impurity, isovector-monopole-strength]
methods: [self-consistent-HF-plus-RPA, Coulomb-matrix-diagonalization, sum-rule-evaluation]
tags: [isospin-symmetry-breaking, isospin-mixing, 100Sn, IVGMR, Coulomb-mixing, Day27]
---

# Isospin mixing in proton-rich `N ~= Z` nuclei

## Bibliographic Record

PRC 52, R1175-R1178 (1995), DOI `10.1103/PhysRevC.52.R1175`.

## Scope and Reading Depth

本地 APS 刊版 PDF 1–4（印 R1175–R1178）全部正文、三表、三图及引用入口已核读。计算讨论基态同位旋杂质与等矢量巨单极响应。相关 E1 或 Fermi β 实验与计算代码不在本件覆盖中。

## Summary

作者用自洽质子／中子单粒子波函数重叠计算基态的 \(T_0+1\) 杂质，并用等矢量巨单极共振（IVGMR）的模型与 RPA 估计做对照。多种 ¹⁰⁰Sn 百分数属于不同计算设置。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| COL95-1 | ¹⁰⁰Sn 的基态 T=1 杂质为 9.12%（质子全 HF，中子轨道取无库仑 HF）与 4.25%（质子与中子均全自洽 HF）。表 II 的 HF 列给 ⁸⁰Zr 3.90%、¹⁰⁰Sn 4.25%、⁹⁹In 2.77%、⁹⁹Sn 2.83%。 | model-result | direct-original | PDF 2 Tables I–II and Fig. 1 | false |
| COL95-2 | ⁴⁰Ca 的基态杂质分别为 HF 0.70%、HF+RPA 0.29%、按式 (11) 估计 0.33%。 | model-result | direct-original | PDF 3 Table III and Fig. 2 | false |
| COL95-3 | ¹⁰⁰Sn 的 Fig. 3 给出无库仑平均场时的 RPA 等矢量单极强度，质心 35.9 MeV。作者据此估计杂质 5.2%，以含库仑的相关 RPA 基态另估 4.8%。 | model-result | direct-original | PDF 4 Fig. 3, Eq. (13) and text | false |
| COL95-4 | 作者提议用 E1 或 Fermi β 跃迁检验此类同位旋杂质。 | author-interpretation | direct-original | PDF 4 concluding paragraph | false |

## Competing Interpretations and Limitations

HF、HF+RPA 与求和规则估计共享相互作用与模型假设，不能当成独立测量。此前归给这篇论文的 GDR 铺展宽度、定量低能 E1 强度与宏观偶极分裂结论已撤回来源归属。相关历史推演见 [[isospin-mixing-gdr-and-coulomb-e1-selection-rules]] 的 2026-11-27 适用边界。

## Extracted Pages

- PDF 1（印 R1175）问题与 HF 形式化。PDF 2 的 Tables I–II 和 Fig. 1 对比 ¹⁰⁰Sn 及邻核估计。
- PDF 3 Table III 与 Fig. 2 给 ⁴⁰Ca 的比较。PDF 4 Fig. 3、式 (13) 与结论给 ¹⁰⁰Sn 的 RPA 对照及待测建议。

## 2026-11-27 — 馆藏原件与覆盖核对

PDF 2 Tables I–II 区分 ¹⁰⁰Sn 两种轨道重叠估计，9.12% 来自部分自洽处理，4.25% 来自全自洽 HF。PDF 4 Fig. 3 与式 (13) 的 5.2%、4.8% 是该模型体系的另外两个 ¹⁰⁰Sn 估计。源页已按原文纠正旧的 GDR 铺展和弱 E1 数值归属。
