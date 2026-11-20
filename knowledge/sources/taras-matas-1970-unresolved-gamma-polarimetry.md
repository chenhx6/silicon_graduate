---
type: source
title: "Taras and Matas 1970 - Unresolved gamma-ray linear polarization"
title_original: "Analysis of Linear Polarization Measurements of Unresolved Gamma Rays"
aliases: []
created: 2026-11-21
updated: 2026-11-21
status: ai-draft
review_status: unreviewed
source_type: journal-article
reading_depth: read
authors: ["P. Taras", "J. Matas"]
year: 1970
doi: "10.1016/0029-554X(70)90578-1"
canonical_source: "Nuclear Instruments and Methods 77 (1970), 10-12, published edition"
raw_file: raw/papers/gpt/query/20261119-polarization-delta-collection/10.1016_0029-554X_70_90578-1.pdf
raw_sha256: 1f062ddb970e998dd71c3a7e58300f775dedaab4a6ac6b14cd3cea49347eead1
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/papers/gpt/query/20261119-polarization-delta-collection/manifest.json
nuclei: ["35Cl"]
tags: ["linear-polarization", "Compton-polarimetry", "unresolved-lines", "mixing-ratio"]
---

# Taras 与 Matas 1970：未分辨 γ 线的线偏振

## Bibliographic Record

P. Taras、J. Matas，*Nuclear Instruments and Methods* **77**, 10–12（1970）。本地原刊三页。Ref. 5 为 Taras、Oleksiuk、Azuma、Prentice 在 *Phys. Rev.* **164**, 1386（1967），`10.1103/PhysRev.164.1386` 的三重角关联研究。现次的对照值取自 1970 年文章转引。

## Scope and Reading Depth

PDF 1–3 全文及书目，印刷页 = PDF 页 + 9。目视核验 Table 1 的原生符号与区间。

## Summary

两条 γ 线在康普顿极化仪中重叠时，用高分辨 Ge(Li) 的分线强度约束计数分配。单个重叠峰的总计数和方位比不足以唯一给出两条线的偏振。作者先以弱线的物理可行范围限制强线，再引入其他共振对强线的偏振约束，反求弱线。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| TAR-RANK | 记分线 \(N_i=N_{90,i}/N_{0,i}\)、\(S_i=N_{90,i}+N_{0,i}\)。分线总量由 Ge(Li) 强度和相对响应约束。四个和式线性相依，直接给出的只是 \(A=(S_1 A_1+S_2 A_2)/(S_1+S_2)\)，其中 \(A_i=(N_i-1)/(N_i+1)\)。若 \(S_1/S_2=\alpha\)，弱线 \(A_2\) 的不确定范围传到强线 \(A_1\) 时缩小为 \(1/\alpha\)。 | identifiability-and-arithmetic | direct-original-pages-and-arithmetic | PDF 1–2，式 2–14 |
| TAR-CL | ³⁵Cl\((p,p'\gamma)\) 的 5.11 MeV 入射条件产生 3.00/3.16 MeV 双线。作者给 \(\alpha=5.45\)，以 \(0.711\le N''\le1.406\) 界定弱线时，3.00 MeV 的谱峰剥离和解析值分别给 \(N=0.89(4)\)、0.87(5)。二者来自同一主谱，只比较分析法。 | measured-and-cross-checked | direct-original-pages | PDF 2–3，图 1、表 1 |
| TAR-DELTA | 原表 3.00 MeV 的解析 \(\delta\) 区间是 \([-0.02,0.09]\)。其他共振把其 \(p\) 收紧至 [0.48,0.58] 后，用式 15 或 16 解 3.16 MeV 线，报告 \(\delta\in[-0.31,-0.21]\)。对照外来三重角关联区间分别为 [0.05,0.10] 和 [−0.25,−0.19]。 | bounded-inference-with-reference | direct-original-pages | PDF 3，§§2.2–3、表 1 |

表 1 的解析列原样记录如下。第二条线的区间使用其他共振对第一条线的约束。

| \(E_\gamma\) (MeV) | \(N_{\rm av}\) | \(p\) | \(\delta\) |
| --- | --- | --- | --- |
| 3.00 | \(0.88\pm0.03\) | \([0.37,0.58]\) | \([-0.02,0.09]\) |
| 3.16 | \(0.82\pm0.06\) | \([0.09,0.46]\) | \([-0.31,-0.21]\) |

## Competing Interpretations and Limitations

- 原文 \(p=J_0/J_{90}\) 是入射偏振分量的比，且式 1 用仪器比值 \(R\)。若采用 \(P=(J_0-J_{90})/(J_0+J_{90})\)，应显式换算 \(P=(p-1)/(p+1)\) 并保留方位。\(p\)、总峰不对称、分线 \(N\) 各有定义。
- 取总峰比值 0.88、另一线的物理比值界 [0.711,1.406] 及 \(\alpha=5.45\)，只做中心输入算术时得强线 \(N'\in[0.8075,0.9147]\)。这展示可行范围的映射，不复现表 1 的统计误差或置信区间。原文称约五倍强度差够用，属于该测量条件。
- Ge(Li) 强度测在相同发射角才适用于该计数分配。原文用两线能量相近近似康普顿响应相同；若响应不同，须保留式 13 的截面比。Postma 1959 用高低边门提供不同比例的额外信息，见 [[postma-1959-ho166m-er166-polarization]]。

## Extracted Pages

- PDF 1–2：极化量、方位计数、强度约束、秩亏、物理界及图 1。
- PDF 3：已知一线的反解、³⁵Cl 表 1、局限与引用。
