---
type: source
title: 'Singh等 2018: 98Zr能级寿命与形状共存RDDS柱塞测量（PRL）'
aliases: [Singh 2018 PRL 98Zr lifetimes, 'arXiv:1902.02637', PRL 121 192501]
created: 2026-11-08
updated: 2026-11-08
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: Evidence for coexisting shapes through lifetime measurements in 98Zr
authors: [Purnima Singh, W. Korten, T. W. Hagen, A. Görgen, L. Grente, M.-D. Salsac, F. Farget, E. Clément, G. de France, T. Braunroth, B. Bruyneel, I. Celikovic, O. Delaune, A. Dewald, A. Dijon, J.-P. Delaroche, M. Girod, M. Hackstein, B. Jacquot, J. Libert, J. Litzinger, J. Ljungvall, C. Louchart, A. Gottardo, C. Michelagnoli, C. Müller-Gatermann, D. R. Napoli, T. Otsuka, N. Pillet, F. Recchia, W. Rother, E. Sahin, S. Siem, B. Sulignano, T. Togashi, Y. Tsunoda, Ch. Theisen, J. J. Valiente-Dobon]
journal: Physical Review Letters
year: 2018
volume: 121
pages: '192501'
doi: 10.1103/PhysRevLett.121.192501
arxiv: 1902.02637v1
canonical_source: https://doi.org/10.1103/PhysRevLett.121.192501
citation_key: ''
raw_file: raw/papers/gpt/query/20261108-foundations-G28/singh-2018-98zr-coexisting-shapes.pdf
raw_sha256: 37f2d5ee16f799feb66617787d45d25c4f3e0cb4f0f996689a0576811c5a05e3
raw_storage_status: fully-archived-local
archive_required: true
nuclei: [98zr]
reactions: ['9Be(238U,f)98Zr @ 6.2 MeV/u']
experiments: [ganil-vamos-exogam-plunger-rdds]
models: [mcsm, 5dch-d1s, 5dch-pc-pk1, 5dch-sly4, hfb-ibm]
observables: [level-lifetime, b-e2, branching-ratio, quadrupole-deformation]
methods: [recoil-distance-doppler-shift, differential-decay-curve-method, in-flight-fission]
tags: [shape-coexistence, lifetime-measurement, rdds-plunger, a100, zr98, absolute-b-e2]
---

# Singh等：98Zr能级寿命与形状共存RDDS柱塞测量

## Bibliographic Record

- 题名：Evidence for coexisting shapes through lifetime measurements in 98Zr
- 作者：Purnima Singh, W. Korten, T. W. Hagen, A. Görgen, L. Grente, M.-D. Salsac, F. Farget, E. Clément, G. de France et al.
- 期刊：*Physical Review Letters* **121**, 192501 (2018)
- DOI：[10.1103/PhysRevLett.121.192501](https://doi.org/10.1103/PhysRevLett.121.192501)
- arXiv 预印本：[arXiv:1902.02637v1](https://arxiv.org/abs/1902.02637) [nucl-ex] (7 Feb 2019)
- 本地底本：`raw/papers/gpt/query/20261108-foundations-G28/singh-2018-98zr-coexisting-shapes.pdf`（6 页，SHA-256：`37f2d5ee16f799feb66617787d45d25c4f3e0cb4f0f996689a0576811c5a05e3`）

## Scope and Reading Depth

### Covered scope

- 全文 6 页、Table I、Figs. 1–4 及参考文献。
- 实验测量条件：GANIL $6.2\text{ MeV/u}\ {}^{238}\text{U} + {}^{9}\text{Be}$（$2.3\text{ mg/cm}^2$ 厚靶）反向裂变反应；VAMOS++ 磁谱仪（位于束流方向 $20^\circ$）进行反冲核离子鉴别（平均速度 $37.3\text{ }\mu\text{m/ps}$）；$\gamma$ 射线由 EXOGAM 阵列探测（10 台分段 Clover 探测器，3 台位于 $135^\circ$、7 台位于 $90^\circ$）；采用柱塞装置在 7 个靶-减速板距离下采集数据（PDF p.2）。
- 微分衰减曲线法（DDCM）单重谱寿命提取过程，考虑已知馈送与未观测慢馈送（PDF p.3）。
- Table I 实验结果核验：
  - $2_1^+ \to 0_1^+$: $\tau_{\exp} = 3.8(8)\text{ ps}$；$B(E2,\downarrow) = 2.9(0.6)^a(0.2)^b\text{ W.u.}$
  - $2_1^+ \to 0_2^+$: $B(E2,\downarrow) = 28.3(6.0)^a(2.4)^b\text{ W.u.}$
  - $4_1^+ \to 2_1^+$: $\tau_{\exp} = 7.5(1.5)\text{ ps}$；$B(E2,\downarrow) = 43.3(8.7)^a(10.8)^b\text{ W.u.}$
  - $4_1^+ \to 2_2^+$: $B(E2,\downarrow) = 67.5(13.5)^a(16.9)^b\text{ W.u.}$
  - $6_1^+ \to 4_1^+$: $\tau_{\exp} = 2.6(9)\text{ ps}$；$B(E2,\downarrow) = 103.0(35.7)^a\text{ W.u.}$
  - 注脚明确区分误差源：上标 $a$ 为本次寿命测量误差，上标 $b$ 为 Urban 2017 分支比误差（PDF p.3, Table I）。
- 与平均场（5DCH D1S/PC-PK1/SLy4、HFB+IBM）及 MCSM 模型的对比（Figs. 2, 3，PDF pp.3–4）。
- $^{98}\text{Zr}$ 三重形状共存的讨论与 MCSM 局限（PDF pp.4–5）。

### Not covered

- 未重跑 VAMOS++ focal plane 离线校准重放程序。
- 本论文未包含新的 $^{100}\text{Zr}$ 寿命实验测量（Fig. 2 中 100Zr 数据点为引用文献 [24, 29, 38–40]）。

### Coverage caveats

- $\gamma$ 探测阵列为 EXOGAM（10 台 Clover 探测器），并非 AGATA。
- 涉及非 yrast 跃迁的 $B(E2)$ 提取依赖引用的外部 $\beta$ 衰变分支比（Urban 2017），误差中包含了分支比的不确定度（角标 $b$）。

## Paper Question and Scientific Motivation

- 测量 $^{98}\text{Zr}$ 的 $2_1^+, 4_1^+, 6_1^+$ 态寿命，确定基态 $B(E2; 2_1^+ \to 0_1^+)$ 是否在 $N=58$ 处已经开始增大，还是保持近球形态，从而检验不同理论模型对 $N=60$ 形变起始点的预言（PDF p.2）。

## Method and Design Logic

- 利用反向运动学裂变与 VAMOS++ 磁谱仪鉴别反冲核，结合 EXOGAM Clover 阵列进行多普勒位移反冲距离测量（RDDS）。
- 利用 VAMOS++ 鉴别的反冲离子数作为各距离谱的归一化基准。
- 使用单重柱塞谱的 DDCM 分析方法，并对已知跃迁的级联馈送进行修正（PDF p.3）。

## Key Evidence and Reasoning Chain

1. **首次测定 $2_1^+$ 寿命**：测得 $\tau(2_1^+) = 3.8 \pm 0.8\text{ ps}$，给出 $B(E2; 2_1^+ \to 0_1^+) = 2.9(0.6)^a(0.2)^b\text{ W.u.}$，表明 $^{98}\text{Zr}$ 基态保持较弱的集体四极跃迁强度（PDF p.3）。
2. **与平均场模型对比**：Fig. 2 比较显示，基于平均场的 5DCH（Gogny-D1S、PC-PK1、SLy4）和 HFB+IBM 模型预言 $B(E2; 2_1^+ \to 0_1^+)$ 从 $N \sim 54$ 即开始逐步上升，与实验测得的 $N=58$ 低值不一致；MCSM 计算则呈现更急剧的转变（PDF pp.3–4）。
3. **激发态形变共存**：结合分支比测得 $B(E2; 2_1^+ \to 0_2^+) = 28.3(6.4)\text{ W.u.}$（在刚性轴对称转子假设下对应 $\beta_2 \approx 0.21$），表明 $0_2^+$ 态具有中等形变；带内跃迁 $B(E2; 4_1^+ \to 2_1^+) = 43.3(13.9)\text{ W.u.}$ 与 $B(E2; 6_1^+ \to 4_1^+) = 103.0(35.7)\text{ W.u.}$ 表明高自旋态进入强形变带（PDF p.4）。
4. **模型差异指出**：作者指出 MCSM 预言 $0_2^+$ 态的形变从 $^{94}\text{Zr}$ 到 $^{98}\text{Zr}$ 持续单调递增，而本次实验测得 $^{98}\text{Zr}(0_2^+)$ 的形变（$\beta_2 \approx 0.21$）小于先前在 $^{96}\text{Zr}$ 中观测到的形变（$\beta_2 \approx 0.26$）（PDF p.4, col. 1）。

## Summary

Singh 等（2018）在 GANIL 利用 $^{238}\text{U} + {}^{9}\text{Be}$ 反向裂变反应、VAMOS++ 磁谱仪与 EXOGAM Clover 阵列，通过 RDDS 柱塞法测定了 $^{98}\text{Zr}$ 的 $2_1^+$（$3.8(8)\text{ ps}$）、$4_1^+$（$7.5(1.5)\text{ ps}$）与 $6_1^+$（$2.6(9)\text{ ps}$）态寿命。实验得到 $B(E2; 2_1^+ \to 0_1^+) = 2.9(0.6)\text{ W.u.}$，表明基态未出现显著形变跃迁；同时测得 $B(E2; 2_1^+ \to 0_2^+) = 28.3(6.4)\text{ W.u.}$ 及高自旋带内强跃迁（高达 $103\text{ W.u.}$），支持低能三态共存图景。数据表明平均场模型给出的渐变趋势过早，而 MCSM 在此区给出了更为陡峭的转变，但 MCSM 对 $0_2^+$ 形变演化的单调性预言与实验存在局部偏差。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SIN18-1 | 测得 $^{98}\text{Zr}(2_1^+)$ 寿命为 $\tau = 3.8 \pm 0.8\text{ ps}$（先前文献上限 $\le 6\text{ ps}$）。 | experimental-fact | direct | PDF p.3, Table I | false |
| SIN18-2 | 测得 $^{98}\text{Zr}(4_1^+)$ 寿命为 $7.5 \pm 1.5\text{ ps}$，$6_1^+$ 寿命为 $2.6 \pm 0.9\text{ ps}$。 | experimental-fact | direct | PDF p.3, Table I | false |
| SIN18-3 | 测定 $B(E2; 2_1^+ \to 0_1^+) = 2.9 \pm 0.6^a \pm 0.2^b\text{ W.u.}$，表明基态跃迁强度较小。 | derived-observable | direct | PDF p.3, Table I | false |
| SIN18-4 | 测定 $B(E2; 2_1^+ \to 0_2^+) = 28.3 \pm 6.0^a \pm 2.4^b\text{ W.u.}$，刚性轴对称转子假设下对应 $\beta_2 \approx 0.21$。 | derived-observable | direct | PDF p.3, Table I; p.4 | false |
| SIN18-5 | 测定带内高自旋跃迁 $B(E2; 4_1^+ \to 2_1^+) = 43.3(13.9)\text{ W.u.}$，$B(E2; 6_1^+ \to 4_1^+) = 103.0(35.7)\text{ W.u.}$。 | derived-observable | direct | PDF p.3, Table I; p.4 | false |
| SIN18-6 | 与 5DCH 及 HFB+IBM 模型对比显示平均场模型预言形变在 $N \sim 54$ 过早渐变上升，与测得的低 $B(E2; 2_1^+ \to 0_1^+)$ 不符。 | model-conflict | direct | PDF pp.3–4, Fig. 2 | false |
| SIN18-7 | 指出 MCSM 预言 $0_2^+$ 形变单调递增，但测得 $^{98}\text{Zr}(0_2^+)$ 的 $\beta_2 \approx 0.21$ 小于 $^{96}\text{Zr}$ 中的数值。 | model-discrepancy | direct | PDF p.4, col. 1 | false |

## Nuclear Structure Information

- 核素：$^{98}\text{Zr}$（$Z=40, N=58$）。
- 跃迁与寿命数据（来自 Table I）：
  - $2_1^+$ ($1222.9\text{ keV}$): $\tau = 3.8(8)\text{ ps}$；$B(E2; 2_1^+ \to 0_1^+) = 2.9(6)^a(2)^b\text{ W.u.}$；$B(E2; 2_1^+ \to 0_2^+) = 28.3(6.0)^a(2.4)^b\text{ W.u.}$
  - $4_1^+$ ($1843.4\text{ keV}$): $\tau = 7.5(1.5)\text{ ps}$；$B(E2; 4_1^+ \to 2_1^+) = 43.3(8.7)^a(10.8)^b\text{ W.u.}$；$B(E2; 4_1^+ \to 2_2^+) = 67.5(13.5)^a(16.9)^b\text{ W.u.}$
  - $6_1^+$ ($2491.1\text{ keV}$): $\tau = 2.6(9)\text{ ps}$；$B(E2; 6_1^+ \to 4_1^+) = 103.0(35.7)^a\text{ W.u.}$

## Authors' Interpretation

- 作者将数据解释为 $^{98}\text{Zr}$ 存在三种不同结构低自旋共存：近球形基态、中等形变 $0_2^+$ 态与强形变带（可能基于 $0_3^+$ 态）。
- 作者提出低自旋态之间可能存在组态混合，以此理解 $4_1^+ \to 2_1^+$ 跃迁与单极跃迁强度。

## Model Results

- 对比了 MCSM（Togashi 2016）、5DCH-D1S、5DCH-PC-PK1、5DCH-SLy4 与 HFB+IBM 的计算结果。

## Competing Interpretations and Limitations

- 依赖 Urban 2017 分支比提取非 yrast 跃迁强度，分支比不确定度对弱分支结果有直接贡献。
- 柱塞单重谱的慢馈送扣除依赖 DDCM 拟合模型。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-1 | Core reconstruction | 本文测定 $^{98}\text{Zr}(2_1^+)$ 寿命为 $3.8(8)\text{ ps}$，给出较弱的基态跃迁 $2.9\text{ W.u.}$ 与较强的激发态跃迁。 | SIN18-1–5, Table I, Fig. 2 | unreviewed |
| AR-2 | Assumptions and dependencies | 依赖 DDCM 单重分析与 Urban 2017 分支比。 | PDF p.3, Table I | unreviewed |
| AR-3 | Transfer conditions | 适用于重离子裂变产生的中等质量丰中子核皮秒能级寿命测量。 | PDF pp.2–3 | unreviewed |
| AR-4 | Failure conditions | 若存在未识别的慢馈送或减速板阻止本领系统误差，寿命测量可能发生漂移。 | PDF p.3 | unreviewed |
| AR-5 | Reverse/falsification test | 可通过高阶库仑激发独立检验跃迁矩阵元。 | PDF p.4 | unreviewed |
| AR-6 | Research-question decision | 作为确定 $^{98}\text{Zr}$ 跃迁强度与检验相变急剧性的关键实验 source。 | SIN18-1–7 | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: 建立了 Singh 2018 关于 $^{98}\text{Zr}$ 寿命测量的原始数据记录。
- Effect of this source: supports & experimental-data-contract。
- Reason: 澄清了 EXOGAM 探测器使用事实与 Table I 误差构成。
- Persistence decision: persistent source for [[doctoral-r1-g28-a100-shell-shape-20261108]]。
- Review state: unreviewed.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[doctoral-r1-g28-togashi-2016-zr-mcsm-qpt]] | 实验数据证实了 Togashi 2016 MCSM 对 $^{98}\text{Zr}$ 基态小 $B(E2)$ 的预报。 |
| foundational-background | [[doctoral-r1-g28-otsuka-2023-type-ii-shell-evolution]] | 实验测定的形状共存数据与 Type-II 壳演化分析相联系。 |

## Human Review Triage

### P0
none identified.

### P1
none identified.

### P2/P3
- P2: 区分寿命测量误差（角标 a）与分支比误差（角标 b）。

## Extracted Pages

- Nuclei: `98zr`
- Observables: `level-lifetime`, `b-e2`, `quadrupole-deformation`
- Methods: `recoil-distance-doppler-shift`, `differential-decay-curve-method`

## Non-source Notes and Follow-up

- 专属于 G28 独立研究任务。
