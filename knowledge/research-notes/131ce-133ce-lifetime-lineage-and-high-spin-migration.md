---
type: research-note
title: "131Ce与133Ce能级寿命谱系、跨带绝对时钟拓扑与高自旋多准粒子迁移合同"
aliases: [131Ce 133Ce lifetime lineage and high spin migration, Ce同位素绝对时钟与高自旋能带迁移, 131ce-133ce-lifetime-lineage]
created: 2026-10-28
updated: 2026-10-28
status: active
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [wakudyanaye-2022-triaxiality-rotational-bands-133ce, alwaleedi-2013-band-structures-131ce, emediato-1997-133ce-rdds-lifetimes, joss-1998-133ce-triaxial-band-lifetimes, hauschild-1996-133ce-triaxial-bands, ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce]
created_from: Day25 checkpoint017 blueprint audit
confidentiality: public
tags: [131ce, 133ce, lifetime, dsam, rdds, high-spin, band-crossing, analysis-blueprint]
---

# 131Ce与133Ce能级寿命谱系、跨带绝对时钟拓扑与高自旋多准粒子迁移合同

## Research Trigger

落实用户关于 [[133ce-thesis-analysis-blueprint]] 的第 6 项核心要求：系统梳理 $^{131}\text{Ce}$ 与 $^{133}\text{Ce}$ 的独立能级寿命谱系，杜绝“全核无寿命”的泛化断言；厘清 DSAM/RDDS 绝对时钟在衰变网络中的逐态接入合同；确立低自旋单准粒子论文向高自旋多准粒子能带交叉迁移时的严格映射边界，禁止跨源凭借能带字母代号或参考 Harris 参数进行非物理拼接。

## Grounded Evidence

### 1. $^{131}\text{Ce}$ 独立寿命测量谱系

文献中关于 $^{131}\text{Ce}$ 的寿命测量具备坚实的实验支持，不可笼统定性为“无寿命测量核”：
- **Li et al. (2004) PRC 69, 064315**（DSAM 测量，100 MeV $^{116}\text{Cd}(^{19}\text{O}, 4n)$）：
  - 负宇称序列（$\nu h_{11/2}$）：$19/2^- \to 15/2^-$ 642 keV（$\tau > 4\text{ ps}$）；$23/2^- \to 19/2^-$ 750 keV（$\tau = 1.44(54)\text{ ps}$）；$27/2^- \to 23/2^-$ 827 keV（$\tau = 1.23(23)\text{ ps}$）；$31/2^- \to 27/2^-$ 892 keV（$\tau_{\text{eff}} < 1.04\text{ ps}$，未扣除顶端馈送）；
  - 正宇称序列：$13/2^+ \to 9/2^+$ 610 keV（$1.46(56)\text{ ps}$）；$17/2^+ \to 13/2^+$ 725 keV（$1.32(10)\text{ ps}$）；$21/2^+ \to 17/2^+$ 796 keV（$0.60(26)\text{ ps}$）；$25/2^+ \to 21/2^+$ 649 keV（$\tau_{\text{eff}} < 2.19\text{ ps}$）；
  - **关键边界**：正序列与负序列宇称相反，分属不同内禀组态，**严禁跨宇称拼接为同宇称手征双重带**，亦不可按 yrast 能量简单合并。
- **Singh et al. (2016) PRC 93, 034327**（RDDS 柱塞法结合 DSAM）：
  - 负宇称序列高精度测量：$15/2^-$ 510 keV 给出 $\tau = 9.6_{-3.8}^{+1.9}\text{ ps}$；$27/2^-$ 827 keV 给出 $1.25_{-0.25}^{+0.41}\text{ ps}$；$31/2^-$ 892 keV 给出 $0.51(5)\text{ ps}$；$35/2^-$ 922 keV 给出 $0.60_{-0.10}^{+0.11}\text{ ps}$；
  - 上下限约束：$19/2^-$ 642 keV 给出 $<7.31\text{ ps}$；$23/2^-$ 750 keV 给出 $>1.3\text{ ps}$（正文述约 3 ps 上界，不可虚构单峰联合置信区间）；
  - 柱塞法低自旋拟合依赖高自旋 DSAM 寿命作为级联馈送输入，两者属于同一分析链的不同区段，不宜视作完全独立的两次测定。

### 2. $^{133}\text{Ce}$ 寿命测量谱系与多能带断裂

与 $^{131}\text{Ce}$ 相比，$^{133}\text{Ce}$ 的寿命覆盖具有明显的能带与自旋局域性：
- **Emediato et al. (1997) PRC 56, 2105**：利用反冲距离多普勒频移法（RDDS）测定低自旋负宇称态寿命，主要覆盖 $9/2^-$ 带头附近低自旋跃迁；计算 PTR 模型明确采用 $\lambda = 50.6\text{ MeV}, \Delta = 0.92\text{ MeV}, \hbar\omega_0 = 8.41\text{ MeV}$；
- **Joss et al. (1998) PRC 58, R2638**：利用 Gammasphere 及 DSAM 测定高自旋常规三轴带（normal-triaxial band），提取出过渡电四极矩 $Q_t \approx 2.2(1)\text{ eb}$（折合 $B(E2) \approx 35\text{ W.u.}$），并与 $^{132}\text{Ce}$ 超形变带（$Q_t \approx 7.4(3)\text{ eb}, 490\text{ W.u.}$）对比；
- **Hauschild et al. (1995, 1996)**：报告 $^{133}\text{Ce}$ 三条超形变（SD）能带与六条约 100 keV 间距的三轴序列（1996Ha20），但**完全缺失能级寿命、跃迁分支比与绝对 $B$ 值**；
- **Wakudyanaye 2022（WK22）与 Ayangeakaa 2013（A13）**：
  - WK22 重点研究的低自旋负宇称带（Band 4，母态 1409.8 keV 582.7 keV 线等）**完全未测定态寿命**；
  - A13 报告的两对候选手征双重带（Bands 2–3 与 Bands 5–6）亦明确记录“由于实验条件限制未测定态寿命（lifetimes could not be performed）”。

## Provisional Reasoning

### 1. 绝对时钟接入衰变网络的拓扑原则
任何寿命 $\tau$ 必须严格按照其测量跃迁的母态激发能 $E_x$、自旋宇称 $J^\pi$、全分支比 $b_\gamma$ 以及内转换系数 $\alpha$ 接入衰变网络：
$$B(E2; I_i \to I_f) = \frac{b_\gamma(E2)}{\tau (1+\alpha) \cdot 1.225 \times 10^9 \cdot E_\gamma^5}$$
- 严禁跨核将 $^{131}\text{Ce}$ 的实测寿命直接赋给 $^{133}\text{Ce}$ 的同位素对应态；
- 严禁跨带将 Joss 1998 测得的高自旋常规三轴带四极矩（$Q_t \approx 2.2\text{ eb}$）平移给 WK22 的低自旋 Band 4 或 A13 的候选手征带；
- 严禁将 Hauschild 1995 的超形变四极矩（$Q_t \approx 7.5\text{ eb}$）混同于非超形变带。

### 2. 高自旋多准粒子迁移合同：拒绝盲目拼接能带字母与 Harris 参数
从低自旋单准粒子（1qp）描述向高自旋多准粒子（3qp/5qp）转动带过渡时，必须遵循可复核的映射合同：
1. **禁止单纯依赖能带字母（Band A/B/C/1/2/4）**：不同作者、不同阵列甚至同一课题组在不同论文中对能带的编号屡有变更。例如 WK22 的 Band 4 为负宇称单粒子倾斜进动带，而 A13 的 Band 4 为四极跃迁序列；必须以**能级能量、自旋宇称与主跃迁级联**为唯一主键进行跨文献对齐；
2. **禁止搬用固定 Harris 参数**：低自旋段拟合的参考转动惯量参数（$\mathcal{J}_0, \mathcal{J}_1$）在经历高自旋角动量对齐（如 $\nu h_{11/2}$ 对或 $\pi h_{11/2}$ 对破裂）后必然发生剧烈重整；直接借用低自旋 Harris 参数会人为伪造角动量对齐度 $i_x$ 的虚假阶跃；
3. **高自旋回弯与手征候选的解耦**：$^{133}\text{Ce}$ 高自旋端（$I > 35/2\hbar$）出现的多带交叉与曲率变化属于典型的多准粒子对齐行为，不能无先验地将其视作三维手征转动；必须逐态考察跨带连接跃迁强度与角分布。

### 3. 582.7 keV / 817.7 keV 缺失跃迁的终审边界
结合寿命谱系核查，进一步确立：
- WK22 Table 6.11 中的出带跃迁比 $B(E2)_{out/out} / B(E2)_{out/in} = 5.06$ 所依赖的 817.7 keV 跃迁，在 Table 5.2 实验账本中完全缺失；
- 该跃迁不仅缺乏实测光子产额，亦缺乏任何相关的态寿命支持；
- 严禁以“Emediato 或 Joss 曾测定过相关能区寿命”为由，逆向构造 817.7 keV 的绝对跃迁强度或分支比。

## Learning Decision

`supports` 将 $^{131}\text{Ce}$ 与 $^{133}\text{Ce}$ 的寿命数据严格定位于具体的能态、自旋段与衰变网络，维护其作为绝对时钟的硬基准；`limits` 任何跨核、跨宇称、跨形变带借用寿命或电磁强度的做法；`revises` 关于“全核无寿命”的过度简化断言，明确区分有寿命约束的能带（如 $^{131}\text{Ce}$ 负宇称带、$^{133}\text{Ce}$ 高自旋常规三轴带）与零寿命支持的候选带（如 $^{133}\text{Ce}$ 低自旋 Band 4、A13 候选手征带）。

## Assumptions

寿命测量值按原文献报告数值与误差区间提取；从寿命推导绝对 $B(E2)$ 假定跃迁能量、分支比与内转换系数遵循标准多极场衰变几率公式；高自旋多准粒子对齐假定核芯转动惯量与对齐角动量满足角动量加法法则。

## Competing Explanations

高自旋带交叉与能级近简并可由多准粒子（3qp/5qp）转动对齐（顺对齐）产生，亦可由三维非共面手征转动或三轴形状共存产生；低自旋 $B(M1)/B(E2)$ 下降可由倾斜进动（TiP）产生，亦可在特定参数下由晃动或签名伙伴带产生。未测定寿命的能态在缺乏绝对时钟前保持竞争解释开放。

## Transfer Conditions

寿命数据只能逐态接入其明确测定的激发能、自旋与分支衰变网络；严禁跨核（$^{131}\text{Ce} \leftrightarrow {}^{133}\text{Ce}$）、跨宇称（正宇称 $\leftrightarrow$ 负宇称）、跨形变带（常规三轴带 $\leftrightarrow$ 超形变带）借调寿命或电磁跃迁强度。

## Failure Conditions

笼统断言“$^{131}\text{Ce}$ 全核无寿命”使本推断失效；将 Joss 1998 高自旋带的过渡四极矩赋给 WK22 低自旋 Band 4 使本合同失效；凭借能带字母（Band 1/2/4）在不同文献间随意合并使高自旋组态重排映射失效；在缺乏 817.7 keV 观测线下假想已定标出带比值使电磁分析失效。

## Falsification or Reverse Tests

若未来实验测定 WK22 Band 4 母态具有皮秒级寿命且带内 $B(E2)$ 显著大于单粒子强度，则倾斜进动模型需接受绝对电四极矩的重新检验；若 $^{131}\text{Ce}$ 测定同宇称双重带且两带寿命在扣除能量因子后呈现显著不对称，则可作为手征破缺的反例。

## Open Questions

1. 未来若对 $^{133}\text{Ce}$ Band 4（$1409.8\text{ keV}$ 态）实施超快定时或反冲距离寿命测量，其实测绝对 $B(E2)$ 是否会进一步验证倾斜进动（TiP）模型的微观预言？
2. 在 $^{131}\text{Ce}$ 中，Singh 2016 测得的 $19/2^-$ 与 $23/2^-$ 寿命极限区间，如何通过多步符合粒子-转子模型给出更窄的理论容许带？

## Human Review

本页整合了公开文献事实，未发生用户定向 claim 裁决，review_status 保持 unreviewed。文中涉及的寿命比较与边界不标注为 human-reviewed。

## Promotion or Rejection History

2026-10-28 由 Day 25 任务根据用户指令建立，用于规范 $^{131}\text{Ce}$ 与 $^{133}\text{Ce}$ 的独立时钟谱系，拒绝跨带跨核借调与粗糙能带字母迁移。
