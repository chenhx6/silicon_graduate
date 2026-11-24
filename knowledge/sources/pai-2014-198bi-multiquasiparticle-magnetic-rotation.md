---
type: source
title: "Pai et al. 2014：198Bi 多准粒子磁转动带交叉与剪刀相互作用强度"
aliases: [Crossing of large multiquasiparticle magnetic-rotation bands in 198Bi, 198Bi MR bands B1 B2, arXiv 1406.5494]
created: 2026-10-30
updated: 2026-11-22
status: ai-draft
review_status: unreviewed
source_type: experimental-paper
reading_depth: deep-read
title_original: "Crossing of large multiquasiparticle magnetic-rotation bands in 198Bi"
authors: [H. Pai, G. Mukherjee, S. Bhattacharyya, C. Bhattacharya, S. Bhattacharya, T. Bhattacharjee, S. K. Basu, S. Kundu, T. K. Ghosh, K. Banerjee, T. K. Rana, J. K. Meena, R. K. Bhowmik, R. P. Singh, S. Muralithar, S. Chanda, R. Garg, B. Maheshwari, D. Choudhury, A. K. Jain]
journal: "Physical Review C"
year: 2014
volume: "90"
pages: "064314"
doi: "10.1103/PhysRevC.90.064314"
arxiv: "1406.5494v3"
language: en
canonical_source: "arXiv:1406.5494v3"
citation_key: pai_2014_198Bi_MR
library_file: "raw/papers/gpt/learning-daily/20261029-DAY27-cross-mass-region-transferability/bi198/Crossing_of_large_multiquasiparticle_magnetic_rotation_bands_in_198Bi.pdf"
raw_file: "raw/papers/gpt/learning-daily/20261029-DAY27-cross-mass-region-transferability/bi198/Crossing_of_large_multiquasiparticle_magnetic_rotation_bands_in_198Bi.pdf"
raw_sha256: "464d4deb3317e16688fe49de136cbaff91f4dc1a7f570243d2143c74ebd1c5e0"
nuclei: [198Bi]
reactions: ["185Re(16O,3n)198Bi", "187Re(16O,5n)198Bi"]
experiments: [INGA-IUAC]
models: [Hybrid-TAC, semiclassical-shears]
observables: [energy-levels, DCO-ratio, linear-polarization-asymmetry, B-M1-to-B-E2-ratio, shears-angle, interaction-strength-V2]
methods: [in-beam-gamma-spectroscopy, clover-array, angular-correlation, polarization]
tags: [Day27, magnetic-rotation, shears, band-crossing, multiquasiparticle, 198Bi, A190]
---

# Pai et al. 2014：$^{198}\text{Bi}$ 多准粒子磁转动带交叉与剪刀相互作用强度

## Bibliographic Record

- 官方来源：**H. Pai et al., Physical Review C 90, 064314 (2014)**；DOI **10.1103/PhysRevC.90.064314**。
- arXiv 版本：`arXiv:1406.5494v3 [nucl-ex]`，v1 提交于 2014-06-20，v3 提交于 2014-12-23。
- 实验测量在印度 IUAC Pelletron 加速器上进行，采用 112.5 MeV $^{16}\text{O}$ 束流轰击天然铼（$^{185,187}\text{Re}$）靶，通过 INGA 阵列（15 台带康普顿抑制的 Clover HPGe 探测器）记录符合 $\gamma$ 谱、DCO 比与线偏振不对称度。
- 本原件直接填补了 Wiki 在 A≈190 奇奇核 $^{198}\text{Bi}$ 上缺乏主实验原件与模型自洽参数的历史资料缺口，对应 [[clark-2000-shears-mechanism]] 综述中提及的 Pb/Bi 区磁转动候选结构。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。完整分析 11 页正文、能级纲图、Hybrid-TAC 自洽形变极小化结果、半经典剪刀角度与相互作用强度拟合。
- Covered scope: 带 B1 与 B2 的自旋宇称、DCO 极化鉴定、准粒子组态、多准粒子带交叉（B1 的 6-qp $\to$ 8-qp，B2 的 4-qp $\to$ 6-qp）、自洽 TAC 倾斜角与三轴形变参数、剪刀相互作用常数 $V_2$。

## Summary

Pai 等人（2014）通过 $^{185,187}\text{Re}(^{16}\text{O}, xn)^{198}\text{Bi}$ 熔合蒸发反应，使用 INGA 阵列系统研究了奇奇核 $^{198}\text{Bi}$ 的高自旋态。建立了包含三条转动带（B1, B2, B3）的全新高自旋能级纲图，其中 B1 与 B2 具有典型的磁转动特征（强 $\Delta I = 1$ $M1$ 跃迁，理论与推导的 $B(M1)$ 随自旋单调下降）。通过微观 Hybrid-TAC 计算自洽确定了形变参数（B1 6-qp 为 $\epsilon_2=-0.083, \gamma=6.9^\circ, \theta=57^\circ$；B2 4-qp 为 $\epsilon_2=-0.085, \gamma=16.4^\circ, \theta=70^\circ$），并在两带中首次观察到多准粒子磁转动带交叉（B1 发生 6-qp $\to$ 8-qp 交叉，B2 发生 4-qp $\to$ 6-qp 交叉）。采用半经典剪刀模型提取了剪刀相互作用常数 $V_2 = 610\text{ keV}$（B1）与 $865\text{ keV}$（B2），单个高-$j$ 粒子—空穴对强度约为 $288 - 300\text{ keV}$。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PAI14-1 | $^{185,187}\text{Re}(^{16}\text{O}, xn)^{198}\text{Bi}$ 反应在 112.5 MeV 布居高自旋态，INGA 15 Clover HPGe 测量符合 $\gamma$ 谱与 DCO 偏振。 | experimental-fact | direct | PDF pp.1–2 Sec.II | false |
| PAI14-2 | 识别出磁转动带 B1 与 B2，B1 经历 6-qp 向 8-qp 剪刀带交叉，B2 经历 4-qp 向 6-qp 剪刀带交叉。 | experimental-and-model | direct | PDF pp.2–6 Sec.III | false |
| PAI14-3 | 自洽 Hybrid-TAC 给出的形变参数：B1 6-qp 为 $\epsilon_2=-0.083, \gamma=6.9^\circ, \theta=57^\circ$；B2 4-qp 为 $\epsilon_2=-0.085, \gamma=16.4^\circ, \theta=70^\circ$。 | model-result | direct | PDF pp.6–7 Sec.III.A | false |
| PAI14-4 | 剪刀相互作用强度拟合：带 B1 $V_2 = 610\text{ keV}$，带 B2 $V_2 = 865\text{ keV}$，单高-$j$ 粒子—空穴对强度约为 $288 - 300\text{ keV}$。 | model-analysis | direct | PDF pp.7–8 Sec.III.B | false |
| PAI14-5 | Hybrid-TAC 给出弱 E2 以及带内 \(B(M1)\) 随自旋变化的趋势。Fig. 8(b) 的两个点由 B2 的 \(20^-\)、\(21^-\) 分支强度按 \(\delta=0\) 推导 \(B(M1)/B(E2)\)，再乘上 TAC 的 \(B(E2)\)。这项比较支持作者的磁转动解释，绝对强度仍依赖模型。 | experimental-derived-and-model | conditional | arXiv v3 PDF pp.10–11, Fig. 8 and text | false |

## Competing Interpretations and Limitations

PDF pp.2–3 的 Eq. (2) 和 Fig. 1 定义积分不对称度 \(\Delta_{\mathrm{IPDCO}}\) 和非偏振 \(^{152}\mathrm{Eu}\) 校准的 \(a(E_\gamma)=0.88(2)+0.00012(3)E_\gamma\)，其中 \(E_\gamma\) 用 keV。Table I 的列与该积分不对称度对应。由该量换算物理线偏振度还需探测器灵敏度。

1. **绝对跃迁强度**。实验未测量能级寿命。B2 仅有两个采用实验强度比和 TAC \(B(E2)\) 得到的 \(B(M1)\) 比较点，完整的自旋依赖曲线来自计算。
2. **多准粒子组态与杂质轨道**：对于带 B1，若将全部 5 个粒子—空穴对计入，每对强度为 $122\text{ keV}$，低于 Pb 区标准 $300\text{ keV}$；作者推测仅高-$j$ 侵入轨道（$\pi h_{9/2}, \nu i_{13/2}$）主导剪刀机制，低-$j$ 轨道主要贡献背景核心对齐，表明在多准粒子剪刀中存在轨道参与有效性分层。

## Extracted Pages

- PDF1–3 记录实验、DCO 及不对称度定义。PDF4 的 Fig. 3 给出能级纲图。
- PDF5–6 的 Table I 给出观测跃迁、相对强度、DCO 和积分偏振不对称度。
- PDF8–11 给出 Hybrid-TAC 形变、转动和跃迁比较，重点见 Figs. 6–9。PDF11–13 讨论半经典剪刀模型和 \(V_2\)，见 Figs. 10–11。PDF13–14 涵盖总结及参考文献。

## Research Decisions

- `supports` [[magnetic-rotation]]：确立了 A≈190 奇奇核中多准粒子磁转动带交叉（6-qp $\to$ 8-qp 与 4-qp $\to$ 6-qp）的微观图像与剪刀相互作用常数 $V_2 \approx 865\text{ keV}$。
- `limits` [[nuclear-chirality]]。本篇为 B1、B2 提供磁转动候选的光谱和模型比较。B2 的 \(\gamma=16.4^\circ\) 来自 Hybrid-TAC 的构型计算。旧注的 \(\hbar\omega_{\rm crit}>0.82\) MeV 缺少本文定位，移出由该论文支持的物理判断。
