---
type: source
title: "Covariant density functional theory for nuclear chirality in 135Nd"
title_original: "Covariant density functional theory for nuclear chirality in 135Nd"
aliases: [Peng and Chen 2020 135Nd 3D TAC CDFT]
tags: [chirality, tilted-axis-cranking, archive-learning]
created: 2026-11-27
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: journal-article-preprint
reading_depth: read
authors: [J. Peng, Q. B. Chen]
year: 2020
canonical_source: "https://arxiv.org/abs/2009.08075"
raw_file: "raw/papers/gpt/learning-daily/20260912-PREPLAN-135nd-crosswalk/lawrie-2020-135nd-cdfT.pdf"
raw_sha256: d756bbd68c74684ecbc4dfc1bd1d16bf7a62ae23371d341d00924ddddac74946
archive_required: true
nuclei: [135nd]
models: [3d-tac-cdft, PC-PK1]
---

# Covariant density functional theory for nuclear chirality in 135Nd

## Bibliographic Record

J. Peng and Q. B. Chen，`arXiv:2009.08075v1`，2020-09-17。原件首页给出实际作者，馆藏文件名中的 Lawrie 是误标。下列定位采用本地 v1 的 PDF 页序。

## Summary

作者从自洽 3D-TAC CDFT 解分离价粒子、价空穴和类核芯转动，并以经典 Routhian 分解解释两种 ¹³⁵Nd 组态的转轴稳定性差别。

## Scope and Reading Depth

本地 PDF 1–6，含研究问题与前史、PC-PK1 计算输入、两种组态的比较、Figs. 1–4、结论和参考文献。参考文献只核本文依赖，未逐项阅读其原件。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| PC20-1 | 对 D3 的 config1，PC-PK1 计算在 ℏω=0.50 MeV 出现浅的 ±15° 等价极小；至 0.60 MeV，φ=0 势垒约 150 keV。 | model-result | source-reported | PDF 2–3，Fig. 1 | false |
| PC20-2 | 对 D5 的 config2，固定组态收敛到约 ℏω=0.55 MeV、I≈21ℏ，仍为平面解。更高频率有 νh₁₁/₂ 与 νh₉/₂ 轨道交叉，限制对此组态临界频率的判断。 | model-boundary | source-reported | PDF 3，Fig. 1 邻文 | false |
| PC20-3 | Fig. 3 的经典分解用选出的价轨道及余核角动量解释 φ 形状。PDF 4 给在 ℏω=0.30 MeV、φ=0 时，两组核芯转动惯量 Jₘ:Jₛ:Jₗ 分别为 1.00:0.65:0.50 和 1.00:0.78:0.76。 | model-result | source-reported | PDF 3–4，Figs. 2–3 | false |
| PC20-4 | Fig. 4 的实验点来自 Refs. 26–28。作者采用两组共用的带头能量平移，指出 D3 仅一个实验 B(M1)/B(E2) 点，且 D5 的计算 B(E2) 偏低。 | model-data-comparison | source-reported | PDF 4，Fig. 4 | false |

## Competing Interpretations and Limitations

计算略去了配对，PDF 2、4 点明临界频率和电磁量可能受此影响。平面解、Routhian 双极小与量子态的能量劈裂属于不同层次。实际寿命证据沿 [[mukhopadhyay-2007-135nd-chiral-vibration-static]] 等原始实验追溯，并与 [[lv-2019-chirality-135nd-reexamined]] 的谱学指定分列。

## Extracted Pages

PDF 2 为 Fig. 1 和计算设置，PDF 3 为 Figs. 2–3 与价轨道分解，PDF 4 为 Fig. 4 及数据比较，PDF 5–6 为结论和参考文献。

## Agent Self-Audit Triage

- Fig. 1 的势垒以及本文的类核芯转动惯量均为模型量。D5 收敛上限只约束本次固定组态计算。
