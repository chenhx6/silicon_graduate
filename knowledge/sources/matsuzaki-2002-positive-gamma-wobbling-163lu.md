---
type: source
title: "Wobbling motion in atomic nuclei with positive-gamma shapes"
title_original: "Wobbling motion in atomic nuclei with positive-γ shapes"
aliases: [Matsuzaki 2002 163Lu wobbling RPA]
created: 2026-11-21
updated: 2026-11-21
status: ai-draft
review_status: unreviewed
source_type: journal-article-theory
reading_depth: deep-read
authors: [M. Matsuzaki, Y. R. Shimizu, K. Matsuyanagi]
journal: Physical Review C
year: 2002
volume: 65
pages: "041303(R)"
doi: 10.1103/PhysRevC.65.041303
arxiv: nucl-th/0201012v1
canonical_source: doi:10.1103/PhysRevC.65.041303
raw_file: raw/papers/gpt/query/20261108-r2-g42-inertia-observables/matsuzaki-2002-wobbling-163lu-prc65-041303R.pdf
raw_sha256: 49bcf5e774dfe3777529965ad02076dec5456af8623df1bac546c1b78dc5f2e1
archive_required: true
nuclei: [163lu, 147gd]
tags: [random-phase-approximation, wobbling, effective-inertia, alignment]
---

# Matsuzaki 等（2002）的正 \(\gamma\) 摆动响应

## Bibliographic Record

*Phys. Rev. C* **65**, 041303(R) (2002)，DOI `10.1103/PhysRevC.65.041303`。实际核读馆藏 `arXiv:nucl-th/0201012v1` 的 11 页。所有定位指作者稿。

## Scope and Reading Depth

作者稿 PDF 1–11，覆盖旋转参考态、色散式、Gd 比较、Lu 的频率和电磁强度检验及 Figs. 1–3。版面对照和独立 RPA 复算未执行。

## Summary

作者用 cranked-shell-model 加 RPA 研究正 \(\gamma\) 构型中的角动量顺排及同频率的摆动响应，并检验 \(^{163}\mathrm{Lu}\) TSD2 的能标与电磁跃迁。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MAT02-1 | 去除 Nambu–Goldstone 模后，横向惯量 \(\mathcal J_{y,z}^\mathrm{eff}(\omega)\) 依赖 RPA 本征频率，主轴 \(\mathcal J_x=\langle J_x\rangle/\omega_\mathrm{rot}\) 是共同运动学量。色散式有集体模及其它根。 | model-result | direct | PDF 4, Eq. (2) | false |
| MAT02-2 | \(^{163}\mathrm{Lu}\) 取 \(\epsilon_2=0.43,\gamma=20^\circ,\Delta_{n,p}=0.3\) MeV。作者在指定空间得到正 \(\gamma\) 摆动，并将惯量变化部分归因于顺排近饱和的 \(i_{13/2}\) 质子项 \(i_x/\omega_\mathrm{rot}\)。Fig. 2 的模型频率变化比从实测能级提取的曲线平缓。 | model-result | direct | PDF 5–6, 10, Fig. 2 | false |
| MAT02-3 | 模型给 \(Q_t=10.9–11.3\) eb，对照来自 Schmitz 1993 的 \(10.7(7)\) eb。作者指出计算只达到所比较带间 E2 强度的大约一半至三分之一。 | model-result | direct | PDF 5–7, 11, Fig. 3, Ref. 18 | false |

## Competing Interpretations and Limitations

该 \(Q_t\) 对照沿用历史输入。与 [[campaign-g07-gorgen-2004-163lu-quadrupole-moments]] 或 [[schonwasser-2002-lu163-lu164-dsam-lifetimes]] 比较时，应记录阻止本领、侧馈与 \(K\) 分布假设，也应区分频率依赖的有效惯量和带内能量差分。后续模型范围见 [[matsuzaki-2004-nuclear-inertia-and-wobbling]]。

## Extracted Pages

PDF 1–4 载模型与 Eq. (2)，5–7 载 \(^{147}\mathrm{Gd}\) 与 \(^{163}\mathrm{Lu}\) 比较，8 为引文，9–11 为三幅图。
