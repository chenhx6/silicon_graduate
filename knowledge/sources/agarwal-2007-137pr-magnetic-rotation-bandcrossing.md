---
type: source
title: "Agarwal et al. 2007 - Bandcrossing of magnetic rotation bands in 137Pr"
aliases: [Agarwal 2007 137Pr magnetic rotation]
created: 2026-09-30
updated: 2026-09-30
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Bandcrossing of magnetic rotation bands in 137Pr"
authors: [Priyanka Agarwal, Suresh Kumar, Sukhjeet Singh, et al.]
journal: Physical Review C
year: 2007
volume: 76
pages: 024321
doi: 10.1103/PhysRevC.76.024321
arxiv:
language: en
canonical_source: "https://doi.org/10.1103/PhysRevC.76.024321"
zotero_item_key: ""
citation_key: ""
zotero_uri: ""
library_file: ""
raw_file: "raw/papers/gpt/day3-mean-field-20260929/137pr-2007-magnetic-rotation/PDFs/Bandcrossing_of_magnetic_rotation_bands_in_137Pr.pdf"
raw_sha256: 83ccf538913d777f60832ee7ff304ffa8ca0678399b893f827236a6ab33c6a55
nuclei: [137Pr]
reactions: ["122Sn(19F,4n)137Pr"]
experiments: [INGA-137Pr-80MeV-2007]
models: [tilted-axis-cranking, cranked-shell-model]
observables: [RDCO, IPDCO, B(M1)/B(E2), band-crossing]
methods: [gamma-gamma-coincidence, directional-correlation, linear-polarization]
tags: [a130, 137pr, magnetic-rotation, band-crossing, high-spin]
---

# Agarwal 等（2007）：137Pr 磁转动带交叉

## Bibliographic Record

Priyanka Agarwal et al., Physical Review C 76, 024321 (2007), DOI [10.1103/PhysRevC.76.024321](https://doi.org/10.1103/PhysRevC.76.024321)。Crossref 核实题名、作者、卷和文章号；Crossref 为 APS standard license，OpenAlex 未检出 OA 仓储全文。本次通过 APS 官方 PDF URL 直接取得文件，HTTP 响应为 application/pdf 且以 %PDF 开头；访问 manifest 为 raw/papers/gpt/day3-mean-field-20260929/137pr-2007-magnetic-rotation/manifest.json。此记录为 publisher-direct retrieval，不标为开放许可。

## Scope and Reading Depth

- 已通读 8 页正文，视觉核对 Fig. 2 部分能级纲图、Table I、Fig. 3 的 gated crossover spectra、Fig. 4 的 DCO、Figs. 5–7 的 TAC 能量/频率/跃迁比比较。
- 未重新分析 γ-γ coincidence 数据，也未摄入 Xu et al. 1989、Dragulescu et al. 1992 两篇早期 137Pr 实验全文。
- 文中没有报告绝对 lifetime；Table I 的 B(M1)/B(E2) 是从相对强度派生，混合比 δ² 假设可忽略。
- 新 claim 均保留 needs_review: true；页面仍为 unreviewed。

## Summary

该实验用 INGA 扩展 137Pr 负宇称 ΔI=1 带至 47/2−，DCO 与线偏振支持其 M1 性质，并首次报告若干弱 crossover E2。作者从相对 γ 强度和能量派生 B(M1)/B(E2)，观察到它在约 37/2 后下降，并用 TAC 的 3qp→5qp 构型交叉解释 back-bending。TAC 对趋势有解释力，但 5qp 计算与实验能量/自旋存在系统偏移；这是一条同核后续 TAC 路线，不是角动量投影，也不独立确定 Hara–Sun 的形状标签。

## Active Recall Before Opening the Full Text

开原文前的预期是：137Pr 为 Z=59,N=78 奇质量奇质子核；Hara–Sun N=78 星号是形状候选。磁转动若成立，应有 M1 主导的 ΔI=1 带、较弱的 crossover E2 和随自旋演化的 B(M1)/B(E2)；band crossing 也可能改变这些趋势。未知点是带身份与宇称是否由 DCO/IPDCO 闭合、强度比是否依赖 δ 假设、TAC 组态是否拟合了同一数据以及后半段计算是否可靠。原文核对后发现：M1 带与弱 E2 连接由新 INGA 数据建立；强度比假设 δ² 可忽略；TAC 的 5qp 支支配高自旋，但计算能量归一与自旋仍有偏差。

## Experimental or Theoretical Setup

- 实验反应为 122Sn(19F,4n)137Pr，19F 束流 80 MeV，靶厚 1.2 mg/cm²，使用 IUAC 的 INGA 八个 Compton-suppressed clover，4 个置于 81°、4 个置于 141°；收集约 6.3×10^8 γ-γ coincidence events（Sec. II，PDF p. 2）。
- DCO 使用 517-keV E2 gate 与 112-keV M1 gate；作者给出与多极次相应的 DCO 参考值。线偏振的 IPDCO 符号用于区分磁性与电性跃迁。
- TAC 为 Woods-Saxon 球形单粒子能级与变形各向异性谐振子结合的 hybrid implementation；配对间隙取奇偶质量差的 80%：Δp=1.048 MeV、Δn=0.65 MeV，磁矩衰减因子 η=0.6。
- 3qp 配置为 πh11/2⊗ν(h11/2)−2；5qp 配置为 πh11/2(g7/2)2⊗ν(h11/2)−2。带头模型形变分别约 (ε2,ε4,γ)=(0.135,0.009,58°) 与 (0.126,0,58°)，平均倾角约 25°、26°；5qp 极小值在 3qp 之上约 2.2 MeV。Lund convention 中 γ=60° 为 oblate 极限。这些是模型参数/输出，不是测得形变（Sec. IV，PDF p. 6）。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AG07-1 | 新 INGA 实验用 122Sn(19F,4n) 反应、80-MeV 束流和 6.3×10^8 个 γ-γ coincidence events 研究 137Pr。 | experimental-fact | direct | Sec. II, PDF p. 2 | true |
| AG07-2 | 负宇称 Band 2 的 ΔI=1 序列由新数据扩展至 47/2−，新增 507、577、657-keV 三条带内跃迁。 | experimental-fact | direct | Fig. 2; Table I, PDF pp. 3–4 | true |
| AG07-3 | 对 517-keV E2 gate，Band 2 大部分拉伸 ΔI=1 跃迁的 RDCO 约为 0.5；负 IPDCO 与 DCO 联合支持 M1 带指认。 | experimental-criterion | direct | Table I; Fig. 4; PDF pp. 4–5 | true |
| AG07-4 | 本文首次观测到 Band 2 的弱 ΔI=2 crossover E2，支撑 M1 带能级次序；其强度明显弱于 ΔI=1 M1。 | experimental-fact | direct | Figs. 2–3; Table I, PDF pp. 3–5 | true |
| AG07-5 | Table I 的 B(M1)/B(E2) 由 γ 强度和能量按正文公式派生，作者假设 δ² 可忽略；弱 E2 强度常由多组 gated spectra 平均。它不是绝对 lifetime/B 值。 | experimental-criterion | direct | Eq. following IPDCO discussion; Table I, PDF pp. 5–6 | true |
| AG07-6 | Band 2 派生 B(M1)/B(E2) 随自旋先增，在约 37/2− 达峰后下降；表中 37/2− 值为 62.1(12.0)，41/2− 为 17.2(2.9)。 | experimental-fact | direct | Table I; Fig. 7, PDF pp. 4, 7 | true |
| AG07-7 | 作者将 Back-bending 与 3qp、5qp 两条磁转动组态带的交叉联系起来；低自旋接近 3qp、高自旋接近 5qp，混合转变区在约 35/2–37/2。 | author-interpretation | indirect | Figs. 5–7; Sec. IV, PDF pp. 6–7 | true |
| AG07-8 | TAC 3qp 解的带头参数约为 ε2=0.135、ε4=0.009、γ=58°、θ≈25°；5qp 解约为 ε2=0.126、ε4=0、γ=58°、θ≈26°，5qp 能量极小高约 2.2 MeV。 | model-result | direct | Sec. IV; Figs. 5–6, PDF p. 6 | true |
| AG07-9 | 5qp TAC 带相对实验存在约 2ℏ 的自旋/能量归一偏差，且高自旋 B(M1)/B(E2) 拟合并不完整；作者称整体趋势仍可解释交叉，但需谨慎对待参数细节。 | author-interpretation | direct | Figs. 5–7; Sec. IV, PDF pp. 6–7 | true |
| AG07-10 | Band 3 结构较不规则，数据不足以可靠给出自旋宇称；作者要求更多实验测量。 | author-interpretation | direct | Sec. III–IV, PDF pp. 3, 6 | true |
| AG07-11 | 本文报告一项新的 INGA 测量；作者称相对强度大体与 Xu et al. 1989 相符，131.0、725.8、842.0-keV 三线例外，且若干低能自旋宇称沿用早期实验假设。 | synthesis | direct | Sec. II–III; Table I, PDF pp. 2–4 | true |

## Analytical Reconstruction

正文的强度比公式为

R = 0.697 × [Iγ(M1) Eγ(E2)^5] / [Iγ(E2) Eγ(M1)^3]，能量用 MeV，单位为 (μN/eb)^2。

用 29/2− 态的 321.0(1)-keV M1，Iγ=50.9(17)，与 432.6(4)-keV E2，Iγ=1.6(3)，代入得 R≈10.16。忽略能量误差后仅用相对强度传播，约为 10.2(1.9)；Table I 列 10.4(1.9)，二者相符。这个重算复现的是作者的强度比算法，依赖 δ²≈0 和相对强度，不能替代 absolute lifetime。

以表列值比较 37/2− 的 62.1(12.0) 与 41/2− 的 17.2(2.9)，比值下降约 3.61 倍；若暂把两误差视作独立，差值约 3.6σ。该趋势支持跨带强度结构改变，但 band crossing 的组态归因仍依赖 TAC 图和模型输入。

## Competing Interpretations and Limitations

- 实验建立 M1 带与弱 crossover E2；“磁转动”是作者结合 M1/E2、强度比和 TAC 几何提出的模式解释，不是一个单独被直接测到的量。
- B(M1)/B(E2) 由分支强度导出并假设 δ² 可忽略；很弱 E2 转换的强度还采用多组门控谱平均。没有绝对寿命、绝对 B(E2)/B(M1) 或独立形变测量。
- TAC 给出近 oblate、弱形变模型解并包含 3qp→5qp crossing；高自旋计算有约 2ℏ、2.2-MeV 的偏移和归一化问题，不是同精度的逐点拟合。
- Hara–Sun 的 N=78 “presumably triaxial” 标签是早期模型候选；本篇 TAC gamma≈58° 属模型参数/解，既不等于直接形状测量，也不构成 angular-momentum projection 验证。
- 作者称若干强度与早期 Xu 1989 结果相符，并沿用早期低能级赋值；核素级综合时需保留同核谱系而不将论文数等同独立实验数。

## Knowledge Impact and Learning Decision

Decision: revises the Hara Table 5 coverage map. 137Pr 现在有可读的后续 INGA 实验和 3qp/5qp TAC 磁转动模型比较，但没有 direct PSM/TPSM angular-momentum projection source；M1 带和强度比支持作者的磁转动解释，同时模型能量/自旋偏差限制其唯一性。

## Extracted Pages

- Nuclei: [[137pr]]
- Models: [[tilted-axis-cranking]], [[cranked-shell-model]]
- Projects: [[a130-model-choice-card]]
