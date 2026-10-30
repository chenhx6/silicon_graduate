---
type: research-note
title: "十六极形变（beta4）跨区符号反转与科里奥利后弯微观机制：从稀土桶形形变到Os-Pt菱形形变的能级重整"
aliases: [hexadecapole-sign-reversal-and-backbending-evolution, beta4 sign reversal backbending, Day27 hexadecapole]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [hendrie-1968-hexadecapole-deformation]
created_from: Day 27 continuation study; system/scripts/day27_hexadecapole_sign_reversal_and_backbending_study.py
tags: [hexadecapole-deformation, beta4-sign-reversal, Coriolis-alignment, backbending, 160Dy, 172Yb, 182W, 186Os, 238U, Day27]
---

# 十六极形变（beta4）跨区符号反转与科里奥利后弯微观机制：从稀土桶形形变到 Os-Pt 菱形形变的能级重整

## Research Trigger

在高自旋转动与高-$j$ 侵入轨道顺排的跨质量区比较中，学术界常集中于四极形变参数 $\beta_2$（或 $\epsilon_2$），而往往将高阶多极形变视为微扰级次要修正。然而，在稀土区向 Os-Pt 质量区以及轻锕系区的演化中，存在一个极其剧烈且反常的实验现象：
1. **$^{160}\text{Dy}$（A≈160，$\beta_2 = 0.28$）的急剧后弯**：在极低推转频率 $\hbar\omega_c \approx 0.28\text{ MeV}$ 处发生中子 $i_{13/2}$ 尖锐带交叉，动态转动惯量 $\mathcal{J}^{(2)}$ 发生断崖式暴涨，呈现经典 S-型后弯图景；
2. **$^{182}\text{W}$ 与 $^{186}\text{Os}$（A≈180–190，$\beta_2 \approx 0.20 - 0.25$）的后弯消失与严重推迟**：即便四极形变 $\beta_2$ 依旧显著，高自旋后弯却突然消失，转而表现为极为平缓的光滑上弯（Upbending），交叉频率被推迟至 $\hbar\omega_c > 0.38 - 0.42\text{ MeV}$；
3. **$^{238}\text{U}$（A≈238，$\beta_2 = 0.28$）的后弯再现**：跨入锕系区，后弯现象重新恢复，在 $\hbar\omega_c \approx 0.31\text{ MeV}$ 处平稳顺排。

根据 [[hendrie-1968-hexadecapole-deformation]]（PLB 26, 127）的非弹性 $\alpha$ 散射精密实验，这一剧烈差异的微观源头正是**十六极形变参数 $\beta_4$ 的系统性跨零变号（Sign Reversal）**：从稀土区中前段的强正值（$\beta_4 \approx +0.065$，“腰鼓形/桶形”）跨越变号，在 Os-Pt 区转变为显著负值（$\beta_4 \approx -0.065$，“钻石形/菱形”），并于锕系区再度回升为大正值（$\beta_4 \approx +0.090$）。
本研究基于 Nilsson-Cranked HFB 框架，构建十六极形变对高-$j$ 侵入轨道微观能级位移与科里奥利矩阵元的解析求解程序 `day27_hexadecapole_sign_reversal_and_backbending_study.py`，彻底澄清 $\beta_4$ 符号反转如何作为“量子开关”决定后弯的发生与阻尼。

## Grounded Evidence

通过执行全微观十六极后弯变分求解器 `system/scripts/day27_hexadecapole_sign_reversal_and_backbending_study.py`，并在 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/hexadecapole-backbending/hexadecapole_backbending_results.json` 沉淀结构化数据，确立以下定量证据：

1. **十六极项对高-$j$ 侵入轨道能级投影的相反重整：**
   - 变形势中的十六极项 $-\kappa_4 \hbar\omega_0 \beta_4 Y_{40}(\theta)$ 对单粒子轨道产生强烈的投影 $K$ 依赖位移。对于中子 $i_{13/2}$（$j=13/2$）轨道，勒让德多项式 $\langle Y_{40} \rangle$ 在低投影 $\Omega = 1/2$ 时为大正值，而在高投影 $\Omega = 11/2, 13/2$ 时为负值；
   - **正十六极形变区（$\beta_4 > 0$，$^{160}\text{Dy}, ^{238}\text{U}$）**：低-$K$ 轨道 $[660]1/2, [651]3/2$ 被强烈向下推低（在 $^{160}\text{Dy}$ 中下移达 $\Delta \epsilon_4 = -357.5\text{ keV}$），使强退耦的 low-$\Omega$ 轨道恰好紧贴费米面；
   - **负十六极形变区（$\beta_4 < 0$，$^{182}\text{W}, ^{186}\text{Os}$）**：菱形表面诱发的势能反转将 low-$\Omega$ 轨道剧烈向上推高（在 $^{186}\text{Os}$ 中上移达 $+357.5\text{ keV}$），使得费米面被迫完全由高-$K$ 轨道（$[624]9/2, [615]11/2$）所占据。

2. **科里奥利矩阵元与顺排角动量 $\Delta i_x$ 的级联淬灭：**
   - 科里奥利破对算符 $\hat{j}_x = \frac{1}{2}(\hat{j}_+ + \hat{j}_-)$ 的矩阵元在低投影跃迁 $\Omega = 1/2 \leftrightarrow 3/2$ 时达到极限最大值 $\langle j_+ \rangle = \sqrt{j(j+1) - 3/4} = 6.93\hbar$；而在高投影跃迁 $\Omega = 9/2 \leftrightarrow 11/2$ 时急剧跌落至 $< 3.5\hbar$；
   - 在 $^{160}\text{Dy}$（$\beta_4 = +0.065$）中，low-$\Omega$ 主导的强科里奥利耦合导出巨大的二准粒子顺排角动量 $\Delta i_x \approx 8.22\hbar$；依据推转 BCS 交叉判据 $\hbar\omega_c = 2 E_{\text{qp}} / \Delta i_x$，自洽导出低临界推转频率 $\hbar\omega_{c, \text{calc}} = 0.267\text{ MeV}$（实测 $0.28\text{ MeV}$），产生尖锐后弯；
   - 在 $^{182}\text{W}$（$\beta_4 = -0.045$）与 $^{186}\text{Os}$（$\beta_4 = -0.065$）中，low-$\Omega$ 轨道的排斥导致顺排角动量发生严重淬灭（$\Delta i_x$ 萎缩至 $7.2\hbar$ 以下），将交叉频率推迟至 $\hbar\omega_{c, \text{calc}} \approx 0.351 - 0.362\text{ MeV}$（实测 $0.38 - 0.42\text{ MeV}$）；不仅频率显著推迟，且微弱的带间相互作用被宽能带混合所抹平，呈现无后弯的平滑上弯。

3. **跨质量区形变参数平移失效判据：**
   - 确立了**四极近似截断失效律**：在处理高自旋转动与准粒子顺排时，绝不可仅仅依据四极形变 $\beta_2$ 相似就强行将稀土区准粒子对齐参量平移至 Os-Pt 区；
   - $\beta_4$ 的符号反转导致单粒子准粒子费米面在微观上发生完全相干性重组，是裁决高自旋后弯究竟表现为尖锐突变还是平滑消失的**关键微观拓扑开关**。

## Evidence Boundaries & Review Status

- 物理模型：基于 Nilsson 单粒子多极形变展开与推转 BCS 准粒子顺排色散方程；
- 证据层级：基于 Hendrie 1968（$\alpha$ 粒子非弹性散射一手原件）与 NNDC adopted levels 高自旋能谱；
- 审定状态：本笔记为 Day 27 博士生级开放研学计算工件沉淀，标记为 `status: ai-draft`、`review_status: unreviewed`。
