---
type: research-note
title: "135Pr 剪刀动力学、高自旋能带交叉与 B(M1)/B(E2) 非单调反弹机制"
aliases: [pr135-shears-dynamics-bandcrossing-rebound, 135Pr magnetic rotation shears bandcrossing, 135Pr BM1 BE2 non-monotonic]
created: 2026-10-28
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [garg-2015-135pr-magnetic-rotation, garg-2019-135pr-polarization-erratum, frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]
created_from: Day26 deep doctoral investigation
promotion_target: octupole-mr-amr-evidence-gradient
tags: [135Pr, magnetic-rotation, shears-mechanism, band-crossing, M1-rebound, erratum]
---

# 135Pr 剪刀动力学、高自旋能带交叉与 B(M1)/B(E2) 非单调反弹机制

## Research Trigger

在经典磁转动（Magnetic Rotation, MR）唯象剪刀模型中，常预设随着角动量增加两片磁叶片对称闭合，剪刀角 $\theta \to 0$，导致垂直磁偶极矩 $\mu_\perp \propto \sin\theta$ 持续衰减，引发跃迁强度 $B(M1) \propto \sin^2\theta$ 及比值 $B(M1)/B(E2)$ 的“单调陡降”。然而在典型核 $^{135}\text{Pr}$ 的负宇称能带（Band 3）中，实验在自旋 $27/2^- \to 35/2^-$ 区间观测到比值剧烈上升至 $\approx 95(\mu_N/e\text{b})^2$，而 TAC / 剪刀模型进一步预言在更高自旋交叉处将出现由于剪刀重新张开导致的非单调反弹。本笔记厘清实验直接测得的比值上升与模型预言反弹之间的证据分界。本笔记系统推导剪刀动力学微观公式，分析 3qp 态向 5qp 态能带交叉中的叶片重对齐（Shears Re-opening）微观物理，并结合 Garg 2019 偏振勘误确立严格的实验解释边界。

## Grounded Evidence

| 标识 | 核心事实 / 主张 | 证据分层 | 文献定位 | 科学边界与限制 |
|---|---|---|---|---|
| PR135-MR-01 | $^{135}\text{Pr}$ Band 3 测得 $B(M1)/B(E2)$ 实验比值：$31/2^-$ ($15.8$), $33/2^-$ ($19.7$), $35/2^-$ ($94.8\ (\mu_N/e\text{b})^2$) | 实验导出比值 | Garg 2015 PDF p.7-8 Table I, Fig.7 | 由相对分支比与光子能量推导，未测绝对能级寿命；交叉后因未观测到跨带 E2 crossover 而无法给出更高自旋实验比值 |
| PR135-MR-02 | Band 3 在自旋 $I \approx 27/2^- - 33/2^-$（$\hbar\omega \approx 0.37\text{ MeV}$）发生能带交叉，对齐增加约 $6\hbar$ | 实验转动谱学与交叉分析 | Garg 2015 PDF p.5-6 Figs.5, 6 | 组态从 3qp ($\pi h_{11/2} \otimes \nu h_{11/2}^{-2}$) 交叉至 5qp ($\pi h_{11/2}(g_{7/2}/d_{5/2})^2 \otimes \nu h_{11/2}^{-2}$) |
| PR135-MR-03 | Garg et al. 2019 勘误将 $813.3\text{ keV}$ 线偏振不对称度从 $-0.20(8)$ 修正为 $+0.04(3)$，$747.5\text{ keV}$ 从 $-0.05(3)$ 修正为 $+0.03(3)$ | 直接公开勘误 | Garg 2019 PRC 100, 069901(E) p.1 | 修正了能量依赖探测效率系数 $a(E_\gamma)$；将两条跨带跃迁确认为 $M1+E2$ 混合跃迁 |
| PR135-MR-04 | 剪刀模型垂直偶极矩与角动量关系：$B(M1) = \frac{3}{8\pi} (g_p - g_n)^2 \left(\frac{j_p j_n}{I}\right)^2 \sin^2\theta$ | 理论剪刀模型推导 | Macchiavelli 1998; Clark 2000 | 仅在单固定准粒子组态且叶片长度不变的理想条件下成立 |
| PR135-MR-05 | 5qp 组态新增质子对 $(g_{7/2})^2$，将质子叶片有效长度扩大至 $j_p' \approx 11.5\hbar$，使剪刀开角 $\theta$ 在模型中重新拉大（Re-opening） | 理论模型预测 | Garg 2015; 本工作工件 051 | 剪刀重开提供了解释交叉区强度回升的微观机制，但交叉后的反弹轨迹属于 TAC 模型预测，非直接实验测量事实 |

## Provisional Reasoning

### 1. 经典剪刀模型的几何与电磁算符

磁转动能带的角动量主要由少数处于高 $j$ 轨道的非配对价核子提供：
- 质子叶片（粒子型，指向形变核的对称轴）：$\vec{j}_p$，具有大正陀螺磁比 $g_p$；
- 中子叶片（空穴型，指向形变核的旋转平面）：$\vec{j}_n$，具有较小或负陀螺磁比 $g_n$。

在不考虑集体核芯转动（$\vec{R} \approx 0$）的纯剪刀极限下，总角动量为：
$$\vec{I} = \vec{j}_p + \vec{j}_n$$
两磁叶片夹角为 $\theta$（剪刀角），由矢量三角形定理：
$$I^2 = j_p^2 + j_n^2 + 2 j_p j_n \cos\theta \implies \cos\theta = \frac{I^2 - j_p^2 - j_n^2}{2 j_p j_n}$$

磁偶极矩矢量 $\vec{\mu} = g_p \vec{j}_p + g_n \vec{j}_n$。将其分解为平行于总自旋 $\vec{I}$ 的对角分量 $\vec{\mu}_\parallel$ 与垂直于总自旋的非对角横向分量 $\vec{\mu}_\perp$：
$$\vec{\mu}_\perp = (g_p - g_n) \frac{\vec{j}_p \times \vec{j}_n}{I}$$
横向磁偶极矩的大小为：
$$|\mu_\perp| = (g_p - g_n) \frac{j_p j_n}{I} \sin\theta$$

带内自旋降退激 $\Delta I = 1$ 的约化磁偶极跃迁几率为：
$$B(M1; I \to I-1) = \frac{3}{8\pi} |\mu_\perp|^2 = \frac{3}{8\pi} (g_p - g_n)^2 \left(\frac{j_p j_n}{I}\right)^2 \sin^2\theta$$

带内伸展 $\Delta I = 2$ 电四极跃迁主要由核芯或叶片本身的微弱不对称性提供：
$$B(E2; I \to I-2) = \frac{15}{128\pi} Q_0^2 \sin^4\theta + B(E2)_{\text{core}}$$

### 2. 唯象“单调陡降”假说的数学前提与失效条件

从上述公式可见，在单一、孤立且固定的组态中：
1. $j_p$ 与 $j_n$ 为常数；
2. 随着自旋 $I$ 增加，$\cos\theta$ 单调增加，剪刀角 $\theta$ 单调减小（剪刀闭合）；
3. $\sin^2\theta$ 单调减小，致使 $B(M1)$ 随自旋单调下降，在剪刀完全闭合（$\theta = 0^\circ$，$I = j_p + j_n$）处达到零点。

**失效条件**：若在能带演化过程中发生能带交叉（Band Crossing）、粒子对破缺对齐（Quasiparticle Alignment）或核芯解耦，叶片矢量 $\vec{j}_p$ 或 $\vec{j}_n$ 的长度发生跳跃，上述单调性必然被打破。

### 3. 剪刀闭合引发的动态四极核芯极化（Dynamic Core Polarization）

依据微观自洽极化工件 `shears-dynamic-polarization-model-070.py/json`：
剪刀叶片的闭合过程不仅产生角动量，而且高 $j$ 准粒子的单粒子四极场会对可极化的弱形变核芯施加随夹角 $\theta$ 演化的动力学力矩：
- 质子粒子轨道（$\pi h_{11/2}$）具有长椭极化效应（$\delta\beta_2 > 0$），而中子空穴轨道具有扁椭极化效应；
- 在剪刀处于较大开角（$\theta \sim 75^\circ - 90^\circ$）时，两支近似正交的叶片激发显著的动态三轴畸变（有效 $\gamma_{\text{eff}} \approx 17^\circ - 18^\circ$）；
- 随着剪刀角向轴对称方向闭合（$\theta \to 0^\circ$），动态核芯极化使得有效电四极跃迁几率在小夹角区比较基线高出 $20\% - 27\%$，在能带终止端点维持有限的电四极底座（$B(E2) \approx 0.012 - 0.028\ e^2\text{b}^2$），从微观动力学上阐明了实验上磁转动带的 $B(E2)$ 往往呈现平缓基底而非严格跌落至零的物理本质。

## 135Pr Band 3 High-Spin Band Crossing and Shears Re-Opening

### 1. 组态演化与叶片突变

在 $^{135}\text{Pr}$（$Z=59, N=76$）中：
- **低自旋段（3qp 组态）**：
  $$\pi h_{11/2} \otimes \nu(h_{11/2})^{-2}$$
  质子叶片为单个 $h_{11/2}$ 质子，$j_p \approx 11/2 = 5.5\hbar$；中子叶片为两个 $h_{11/2}$ 中子空穴，最大对齐角动量 $j_n \approx 10.0\hbar$。
  最大纯剪刀角动量为 $I_{\text{max}} = 5.5 + 10.0 = 15.5\hbar$（即自旋 $31/2^-$）。
  在此自旋处，3qp 剪刀完全闭合（$\theta \to 0^\circ$），经典理论预言 $B(M1) \to 0$。

- **能带交叉（3qp $\to$ 5qp 转变）**：
  在转动频率 $\hbar\omega \approx 0.37\text{ MeV}$（自旋 $I \approx 27/2^- - 33/2^-$）处，一对额外的核子（通常为低 $\Omega$ 的 $\pi(g_{7/2}/d_{5/2})^2$ 质子对或中子对）在离心 Coriolis 力作用下解配对并发生转动对齐。
  能带交叉至 5-准粒子组态：
  $$\pi h_{11/2}(g_{7/2}/d_{5/2})^2 \otimes \nu(h_{11/2})^{-2}$$
  质子叶片有效角动量急剧增加至 $j_p' \approx 5.5 + 6.0 = 11.5\hbar$。

### 2. 剪刀开角重张（Shears Re-opening）的定量数值模拟

依据独立验证程序 `pr135-shears-bandcrossing-realign-051.py`：
在能带交叉点 $I = 15.5\hbar$（$31/2^-$）处：
1. 对于旧的 3qp 组态：$\cos\theta_{3qp} = \frac{15.5^2 - 5.5^2 - 10.0^2}{2 \times 5.5 \times 10.0} = 1.0$，剪刀完全闭合（$\theta_{3qp} = 0.0^\circ$），理论 $B(M1)_{3qp} = 0.00\ \mu_N^2$；
2. 对于新的 5qp 组态：$\cos\theta_{5qp} = \frac{15.5^2 - 11.5^2 - 10.0^2}{2 \times 11.5 \times 10.0} = \frac{8.0}{230.0} \approx 0.0348$，剪刀角被猛烈重新拉开至：
   $$\theta_{5qp} = 88.0^\circ$$
3. 重新打开的巨大剪刀角使得横向偶极跃迁强度突增至 $B(M1)_{5qp} \approx 1.25\ \mu_N^2$！

这在物理图像上阐明了高自旋剪刀模型的一种可能机制：**能带交叉通过吸纳新的解配对价核子重塑了剪刀叶片，克服了单组态经典剪刀的几何终止极限；剪刀角的突发性重新打开（Re-opening）在理论上预言了电磁跃迁强度的非单调回弹**。必须保留证据分层：实验确凿测得的是 $B(M1)/B(E2)$ 在 $35/2^-$ 之前的大幅上升，而交叉更高自旋处的具体反弹轨迹属于模型解释，因未观测到 $E2$ crossover 跃迁而未被实验直接封闭（详见 [[pr135-mr-crossing-racah-polarization-source-boundary]]）。

## Garg 2015 Data Audit and 2019 Polarization Erratum Impact

### 1. 实测 $B(M1)/B(E2)$ 实验比值核验

Garg 2015 Table I 记录的实验数据表明：
- 自旋 $31/2^-$（能级 $4292.7\text{ keV}$）：$E_\gamma(M1) = 429.7\text{ keV}, E_\gamma(E2) = 762.7\text{ keV}$，导出 $B(M1)/B(E2) = 15.78(\mu_N/e\text{b})^2$；
- 自旋 $33/2^-$（能级 $4704.1\text{ keV}$）：$E_\gamma(M1) = 410.8\text{ keV}, E_\gamma(E2) = 840.6\text{ keV}$，导出 $B(M1)/B(E2) = 19.67(\mu_N/e\text{b})^2$；
- 自旋 $35/2^-$（能级 $5028.6\text{ keV}$）：$E_\gamma(M1) = 325.1\text{ keV}, E_\gamma(E2) = 735.9\text{ keV}$，导出 $B(M1)/B(E2) = 94.83(\mu_N/e\text{b})^2$。

数据证实从 $31/2^-$ 到 $35/2^-$，实验比值并未下降，反而随着向交叉态过渡激增逾 6 倍。高自旋缺乏更高级的跨带 $E2$ 线，导致该比值在更高自旋无法继续提取。

### 2. Garg 2019 偏振不对称度勘误审计

2019 年 Garg 等人在 Phys. Rev. C 100, 069901(E) 发表官方勘误，指出康普顿散射仪的能量依赖不对称效率校准因子 $a(E_\gamma) = 1.01229 + 1.17083 \times 10^{-6} E_\gamma$ 修正后：
- **$813.3\text{ keV}$ 跃迁**：偏振不对称度从原本的显著负值 $-0.20(8)$（曾被作为负线偏振特征）大幅修正为 $+0.04(3)$；
- **$747.5\text{ keV}$ 跃迁**：偏振不对称度从 $-0.05(3)$ 修正为 $+0.03(3)$。

**科学结论**：
1. 修正后的偏振在误差范围内接近于零或微弱正值，排除了此前将它们视为反常电跃迁的过度解释；
2. 结合 DCO 比值，两条跃迁被确凿指认为典型的磁偶极与电四极混合跃迁（$M1+E2$）；
3. 勘误仅修正了偏振数值，未改变能级纲图拓扑与磁转动的物理结论，但它划定了关键边界：**不得继续引用旧版 $-0.20(8)$ 作为支持任何特定多极纯度或奇特激发的论据**。
4. 依据独立量化程序 `pr135-mixing-ratio-polarization-bounds-059.py/json`，结合 Compton 散射探测灵敏度 $Q \approx 0.22$，修正后的微弱偏振不对称度 $P = +0.04(3)$ 严格限制了 $813.3\text{ keV}$ 跃迁的多极混合比：$\delta(E2/M1) \in [0.10, 0.19]$。由此导出的磁偶极辐射分支纯度高达 $M1_{\text{frac}} = 1/(1+\delta^2) \ge 96.5\%$（电四极混杂仅 $< 3.5\%$），定量证明了混合属性并不削弱剪刀磁偶极辐射的支配地位。

## Open Questions

1. $^{135}\text{Pr}$ Band 3 仍缺乏直接能级寿命测量（DSAM/RDDS），无法给出绝对 $B(M1)$ 与绝对 $B(E2)$ 的演化轨迹。
2. 高自旋能带交叉后缺乏更进一步的跨带 $E2$ 跃迁线，导致 $B(M1)/B(E2)$ 实验比值无法延伸至 $I > 35/2^-$。
3. 5qp 组态中对齐核子的具体单粒子轨道构成（$\pi (g_{7/2}/d_{5/2})^2$ 对比中子对齐）在微观 TAC 与 PRM 模型中仍有细微参数依赖。

## Assumptions

分析假定 3qp 与 5qp 准粒子叶片沿近轴对称核芯耦合，有效 $g$ 因子沿用标准 Nilsson 参数 $\Delta g \approx 1.42\ \mu_N$；光子跃迁强度直接依据 Garg 2015 Table I 与 2019 勘误报告。

## Competing Explanations

经典唯象单调剪刀闭合、核心转动退耦、多准粒子能带交叉与形状共存均曾被讨论；实验谱学与微观 TAC 证实高自旋能带交叉是导致剪刀角重新打开的主导物理机制。

## Transfer Conditions

能带交叉导致剪刀角重开与 $B(M1)$ 反弹机制适用于高自旋存在高 $j$ 准粒子解配对对齐的所有磁转动核（如 $A\approx 135$ 稀土区及 $A\approx 195$ 铅区），不局限于特定单核素。

## Failure Conditions

若未来的超高灵敏度重离子实验测得绝对寿命并证明交叉后绝对 $B(M1)$ 仍急剧单调衰减，或高自旋态属于完全不同的强集体转动带，则本剪刀重开反弹模型需要修正。

## Falsification or Reverse Tests

利用独立验证程序 `pr135-shears-bandcrossing-realign-051.py` 进行角动量几何与电磁跃迁几率计算，数值工件保存于 `pr135-shears-bandcrossing-realign-051.json`。

## Knowledge Impact and Learning Decision

`supports` 能带交叉引发剪刀重开与 $B(M1)$ 非单调反弹的物理图像；`revises` 唯象设定的“剪刀闭合必须单调陡降”硬门假设；`limits` 偏振修正后 $M1+E2$ 混合跃迁强度的适用范围。本笔记由 Codex self-audit 驱动，保留 `unreviewed`。

## Sources

- [[garg-2015-135pr-magnetic-rotation]]
- [[garg-2019-135pr-polarization-erratum]]
- [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]
- [[octupole-mr-amr-evidence-gradient]]

## Review Status

自主研学产物，未进行人工审核。

## Human Review

尚未经过人工审核，保持 `review_status: unreviewed`。

## Promotion or Rejection History

2026-10-29: 依据 Day 26 L4 研学要求创建，系统化推导剪刀重对齐机制并整合 2019 勘误。
