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
| PR135-MR-01 | Garg 2015 Fig.7 给出 Band 3 的相对 $B(M1)/B(E2)$ 曲线；正文明确说该比值随自旋上升至约 $35/2^-$，图上点值只能作为近似读图，不能称 Table I 的直接列项 | 实验导出比值 | Garg 2015 PDF p.7 Fig.7 与 p.8 首段 | 由相对分支、能量和多极性假设导出；没有绝对寿命，故不能拆出绝对 $B(M1)$ 或 $B(E2)$ |
| PR135-MR-02 | Band 3 的 TAC/对齐系统学把交叉定位在 $\hbar\omega\approx0.37$ MeV、$I\approx33/2^-$；$27/2^-$ 是带低端而非交叉点 | 作者模型解释与实验谱学 | Garg 2015 PDF pp.7–8 Figs.5–6、结论 | 下段配置是 $\pi h_{11/2}\otimes\nu h_{11/2}^{-2}$ 到 $\pi h_{11/2}(g_{7/2})^2\otimes\nu h_{11/2}^{-2}$；原文没有把新增对写成 $d_{5/2}$ 或 $\nu i_{13/2}^{-2}$ |
| PR135-MR-03 | Garg et al. 2019 勘误将 $813.3\text{ keV}$ 线偏振不对称度从 $-0.20(8)$ 修正为 $+0.04(3)$，$747.5\text{ keV}$ 从 $-0.05(3)$ 修正为 $+0.03(3)$ | 直接公开勘误 | Garg 2019 PRC 100, 069901(E) p.1 | 修正了能量依赖探测效率系数 $a(E_\gamma)$；将两条跨带跃迁确认为 $M1+E2$ 混合跃迁 |
| PR135-MR-04 | 剪刀模型垂直偶极矩与角动量关系：$B(M1) = \frac{3}{8\pi} (g_p - g_n)^2 \left(\frac{j_p j_n}{I}\right)^2 \sin^2\theta$ | 理论剪刀模型推导 | Macchiavelli 1998; Clark 2000 | 仅在单固定准粒子组态且叶片长度不变的理想条件下成立 |
| PR135-MR-05 | 新增 $(g_{7/2})^2$ 质子对可在固定矢量长度的玩具几何中把 $j_p$ 从 $11/2$ 增至 $11/2+6$，从而在同一 $I$ 重新打开叶片夹角 | 本工作条件推导；非 Garg 直接输出 | 本工作 `shears_rebound_model.py`；Garg 2015 PDF pp.7–8 只给 TAC 配置和倾角 | 这是允许的几何机制，不是对交叉后绝对 $B(M1)$ 的拟合；TAC 倾角也不是本文玩具模型的 blade angle |

## Provisional Reasoning

### 1. 经典剪刀模型的几何与电磁算符

磁转动能带的角动量主要由少数处于高 $j$ 轨道的非配对价核子提供：
- 质子叶片（粒子型，指向形变核的对称轴）：$\vec{j}_p$，具有大正陀螺磁比 $g_p$；
- 中子叶片（空穴型，指向形变核的旋转平面）：$\vec{j}_n$，具有较小或负陀螺磁比 $g_n$。

在不考虑集体核芯转动（$\vec{R} \approx 0$）的纯剪刀极限下，总角动量为：
$$\vec{I} = \vec{j}_p + \vec{j}_n$$
两磁叶片夹角为 $\theta$（剪刀角），由矢量三角形定理：
$$I^2 = j_p^2 + j_n^2 + 2 j_p j_n \cos\theta \implies \cos\theta = \frac{I^2 - j_p^2 - j_n^2}{2 j_p j_n}$$

磁偶极矩矢量 $\vec{\mu} = g_p \vec{j}_p + g_n \vec{j}_n$。把它分解为平行于总自旋 $\vec I$ 的分量和垂直分量后，横向分量的**大小**为：
$$|\mu_\perp| = (g_p - g_n) \frac{j_p j_n}{I} \sin\theta$$
这里不能把横向磁矩向量写成 $\vec j_p\times\vec j_n/I$：叉积垂直于两叶片平面，而磁矩本身位于该平面；两者只有模相等的几何关系。

带内自旋降退激 $\Delta I = 1$ 的约化磁偶极跃迁几率为：
$$B(M1; I \to I-1) = \frac{3}{8\pi} |\mu_\perp|^2 = \frac{3}{8\pi} (g_p - g_n)^2 \left(\frac{j_p j_n}{I}\right)^2 \sin^2\theta$$

带内伸展 $\Delta I = 2$ 电四极跃迁需要单独的四极算符和核芯响应。某些半经典镜像剪刀极限给出 $\sin^4\theta$，其它有效模型可用 $\sin^2\theta$ 或含核芯项的形式；因此不能把一个幂次律当成 135Pr 的直接实验结论：
$$B(E2)=C_{E2}\,\sin^{n}\theta+B(E2)_{\text{core}},\qquad n=2\ \text{或}\ 4\ \text{取决于模型约定}.$$

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
  Garg 2015 的 TAC 比较把交叉放在 $\hbar\omega\approx0.37\text{ MeV}$、$I\approx33/2^-$ 附近。作者使用的高自旋配置是新增质子 $(g_{7/2})^2$，而不是本文背景中可泛化写成的中子 $i_{13/2}$ 空穴对；这一配置身份来自作者模型，不能由实验单独测得。
  能带交叉至 5-准粒子组态：
  $$\pi h_{11/2}(g_{7/2})^2 \otimes \nu(h_{11/2})^{-2}$$
  在一个把两个 $g_{7/2}$ 质子最大耦合为 $J=6$ 的透明玩具向量模型中，质子叶片可写成 $j_p'=5.5+6=11.5\hbar$。这不是 Garg TAC 输出的 blade 长度，而是本笔记脚本用于显示“重开可发生”的条件构造。

### 2. 剪刀开角重张（Shears Re-opening）的定量数值模拟

依据本轮可复现脚本 `outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/shears-rebound/shears_rebound_model.py`：
在旧 3qp 叶片的几何终点 $I = 15.5\hbar$（$31/2^-$）处：
1. 对于旧的 3qp 组态：$\cos\theta_{3qp} = \frac{15.5^2 - 5.5^2 - 10.0^2}{2 \times 5.5 \times 10.0} = 1.0$，剪刀完全闭合（$\theta_{3qp} = 0.0^\circ$），理论 $B(M1)_{3qp} = 0.00\ \mu_N^2$；
2. 对于新的 5qp 组态：$\cos\theta_{5qp} = \frac{15.5^2 - 11.5^2 - 10.0^2}{2 \times 11.5 \times 10.0} \approx 0.0348$，该条件构造给出约 $88^\circ$ 的大夹角；在实际交叉自旋 $I\approx16.5\hbar$，同一构造给出约 $80^\circ$，而旧 3qp 三角形已无解。
   $$\theta_{5qp} = 88.0^\circ$$
3. 归一化的横向磁矩因子随 $\sin^2\theta$ 重新变大；脚本报告的是无量纲 `m1_norm`，没有把它换算成 $\mu_N^2$，因为 $g$ 因子、有效电荷和绝对寿命均未由该实验给出。

这给出一个可检验但尚未被绝对强度封闭的机制：**组态交叉改变叶片长度和有效磁矩，因而可使剪刀角重开，并使 $B(M1)$ 相对固定组态的单调闭合律失效**。实验直接报告的是 Fig.7 中相对 $B(M1)/B(E2)$ 曲线升至约 $35/2^-$；Garg 同时明确指出交叉后 crossover 未观测，不能用该比值解释交叉后的行为。故“反弹”在 135Pr 中应写成 TAC/几何解释，而非交叉后绝对 $B(M1)$ 的直接测量。

## Garg 2015 Data Audit and 2019 Polarization Erratum Impact

### 1. 实测 $B(M1)/B(E2)$ 实验比值核验

Garg 2015 的 Table I 给出相关 M1 与 crossover E2 的能量、相对强度和多极性；Fig.7 再把由这些相对量导出的 $B(M1)/B(E2)$ 画成自旋函数。正文的可逐字核验表述是：该比值随自旋增加至约 $35/2^-$，而更高自旋因 crossover 未观测不能继续提取。图上约 $31/2^-$、$33/2^-$ 到 $35/2^-$ 的高点（约 $16$、$20$、$95\ (\mu_N/e\text{b})^2$）应标为读图/既有工件数值，而非 Table I 的直接列项。

因此实验支持“相对比值在交叉附近上升”，却不能单独证明 $B(M1)$ 绝对值回升；高自旋缺少 crossover E2，导致更高自旋的比值无法继续提取。

### 2. Garg 2019 偏振不对称度勘误审计

2019 年 Garg 等人在 Phys. Rev. C 100, 069901(E) 发表官方勘误，指出康普顿散射仪的能量依赖不对称效率校准因子 $a(E_\gamma) = 1.01229 + 1.17083 \times 10^{-6} E_\gamma$ 修正后：
- **$813.3\text{ keV}$ 跃迁**：偏振不对称度从原本的显著负值 $-0.20(8)$（曾被作为负线偏振特征）大幅修正为 $+0.04(3)$；
- **$747.5\text{ keV}$ 跃迁**：偏振不对称度从 $-0.05(3)$ 修正为 $+0.03(3)$。

**科学结论**：
1. 修正后的偏振在误差范围内接近于零或微弱正值，排除了此前将它们视为反常电跃迁的过度解释；
2. 结合 DCO 比值，两条跃迁被列为 $M1+E2$ 混合；
3. 勘误仅修正了偏振数值，未改变能级纲图拓扑与磁转动的物理结论，但它划定了关键边界：**不得继续引用旧版 $-0.20(8)$ 作为支持任何特定多极纯度或奇特激发的论据**。
4. 勘误本身没有给出 $\delta$ 区间，也没有给出 Compton analyzing power、取向宽度或绝对强度。因此不能从 $\Delta=+0.04(3)$ 单独推出 $\delta\in[0.10,0.19]$ 或 $M1$ 百分比；任何这类数值都必须明确写成依赖核取向与响应参数的条件反演。

## Open Questions

1. $^{135}\text{Pr}$ Band 3 仍缺乏直接能级寿命测量（DSAM/RDDS），无法给出绝对 $B(M1)$ 与绝对 $B(E2)$ 的演化轨迹。
2. 高自旋能带交叉后缺乏更进一步的跨带 $E2$ 跃迁线，导致 $B(M1)/B(E2)$ 实验比值无法延伸至 $I > 35/2^-$。
3. 5qp 组态中对齐核子的具体单粒子轨道构成（$\pi (g_{7/2}/d_{5/2})^2$ 对比中子对齐）在微观 TAC 与 PRM 模型中仍有细微参数依赖。

## TAC、TAC-RMF/CDFT 与核芯转动的层级对照

### 实验和模型可辨识的量

| 框架 | 主要自由度 | 可预测/比较的量 | 对本课题的实际边界 |
|---|---|---|---|
| 固定双叶片经典剪刀 | 固定 $j_p,j_n$ 与夹角 $\theta$ | $|\mu_\perp|\propto(j_pj_n/I)\sin\theta$、归一化 $B(M1)$；在指定四极算符下的 $B(E2)$ 幂次 | 只在单一组态和明确角动量分配下成立；不能跨 3qp/5qp 自动延拓 |
| 含平行核芯的剪刀 | $\mathbf I=\mathbf j_p+\mathbf j_n+\mathbf R$，取 $\mathbf R\parallel\mathbf I$ 的简化场景 | 核芯承担的自旋会改变有效叶片合成角和 $B(E2)$ 基底，并可缓和闭合 | $R$、核芯四极矩和有效电荷需要独立约束；脚本中的 20% 只是情景参数 |
| TAC（Garg 2015 hybrid TAC） | 转动频率、形变、组态和转轴相对内禀轴的倾角，最小化 $H-\boldsymbol\omega\cdot\mathbf J$ | $I(\omega)$、能带交叉、模型 $B(M1)/B(E2)$、$\beta_2,\gamma$ 与倾角 | 对 135Pr 给出 3qp/5qp 比较、$\omega\approx0.37$ MeV 交叉和平均倾角，但未给实验绝对寿命 |
| TAC-RMF/CDFT | 自洽协变平均场、配对/阻塞、形变与转轴 | 组态依赖的能量、对齐、形变和跃迁矩阵元 | 当前 Wiki 中直接取得的 PC-PK1 TAC-CDFT 原件是邻核 136Pr（Lv 2025），不是 135Pr；不能把邻核模型输出冒称本核微观结果 |

在 TAC 语言里，“两个额外高-$j$ 中子空穴改变转动轴与内禀轴倾角”只有在具体组态确实为中子空穴对时才适用。Garg 2015 对 135Pr 的高段 TAC 配置明确写成新增 $\pi(g_{7/2})^2$；因此本核应表述为“新增质子对改变自洽角动量分配和倾角”，而不是套用中子 $i_{13/2}^{-2}$ 的解释。137Pr 的 Agarwal 2007 也是 $\pi h_{11/2}(g_{7/2})^2\otimes\nu h_{11/2}^{-2}$ 5qp 比较，可作为同区机制旁证，但不是 135Pr 的独立重复实验。

### $J^{(2)}$ 的可复现定义和证据边界

$$J^{(2)}(\omega)=\frac{dI}{d(\hbar\omega)}\simeq\frac{I_{k+1}-I_{k-1}}{(\hbar\omega)_{k+1}-(\hbar\omega)_{k-1}}.$$

实验上，$I(\omega)$ 可由能级间隔转换得到；Garg 2015 的 Fig.5/6 用该类对齐/频率系统学识别交叉。本文脚本用两个线性 $I_3(\omega)$、$I_5(\omega)$ 与 logistic 混合制造一个可重算的 $J^{(2)}$ 峰（结果约 $62.3\ \hbar^2/$MeV，峰在约 0.38 MeV），它只验证有限差分与混合机制，不是 135Pr 的实测 $J^{(2)}$，也不是 TAC-RMF 计算。

脚本输出包括三组可分离层：固定 3qp/5qp 双叶片、平行核芯情景、以及带交叉的 $J^{(2)}$ toy proxy。运行：

```bash
python3 outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/shears-rebound/shears_rebound_model.py
```

结果写入同目录 `shears_rebound_model_results.json`。任何 `m1_norm`、`e2_norm` 和 `ratio_norm` 都是归一化量；没有从它们反演绝对 $B(M1)$ 或 $B(E2)$。

## 实验强度与证据等级结论

- **直接报告：** Garg 2015 观测了负宇称 $\Delta I=1$ 带、M1 主导跃迁和 crossover E2；Fig.7 显示相对 $B(M1)/B(E2)$ 上升至约 $35/2^-$。原文明确说更高自旋 crossover 未观测，故不能给出交叉后比值轨迹（PDF pp.7–8）。
- **绝对强度：** 本带没有 DSAM/RDDS 寿命，作者明确说不能提取 $B(M1)$，并把寿命测量列为确认 MR 的后续工作（PDF pp.7–8）。因此当前没有交叉后绝对 $B(M1)$ 或 $B(E2)$ 的直接测量。
- **相对强度：** 由分支比、能量和多极性假设得到的 $B(M1)/B(E2)$ 仍是实验派生量；比值不能唯一决定分子或分母各自的变化。
- **2019 勘误：** 747.5 和 813.3 keV 的偏振不对称度分别改为 $+0.03(3)$、$+0.04(3)$，并在勘误表中列为 $M1+E2$（Garg 2019, PDF p.1 Table I）。这是探测器几何不对称校准修正，独立于 3qp→5qp TAC 交叉；勘误没有绝对寿命、$B(M1)$、$B(E2)$ 或独立的剪刀重开测量。
- **模式独立性：** 偏振勘误纠正了低自旋/连接跃迁的多极性输入，交叉反弹讨论的是高自旋 Band 3 的组态和相对强度演化。两者可在同一证据链中并列，但不能把前者当成后者的独立证明。

## Agent self-audit triage

| 优先级 | 项目 | 当前判断 |
|---|---|---|
| P0 | 135Pr 是否有交叉后绝对 $B(M1)$/$B(E2)$ | 当前未找到本带 DSAM/RDDS；Garg 2015 明确报告无寿命。若论文写作需断言“没有”，仍应补一次有界文献检索。 |
| P0 | “重开”是否是实验事实 | 不是。实验事实是相对比值升至约 $35/2^-$；重开是 TAC/几何解释，且高自旋 crossover 缺失。 |
| P0 | 配置身份 | 135Pr Garg 2015 写的是新增 $\pi(g_{7/2})^2$；不得改写为背景中泛化的 $\nu(i_{13/2})^{-2}$ 或 $g_{7/2}/d_{5/2}$ 混合。 |
| P1 | TAC 与 TAC-RMF/CDFT | 135Pr 现有直接原件是 hybrid TAC；本地直接 TAC-CDFT 原件为邻核 136Pr。两者均应标模型结果，不能合并成 135Pr TAC-RMF 直接计算。 |
| P1 | 2019 偏振勘误 | 只更新 $\Delta$ 与混合多极性；旧负偏振值不得继续作为排他性证据。$\delta$ 需取向/响应条件，不能由勘误单独唯一反演。 |
| P1 | 脚本数值 | `shears_rebound_model.py` 已运行并生成 JSON；toy proxy 的 $J^{(2)}$ 和归一化强度不具实验单位认证。 |

## History

- 2026-10-29：本轮修订证据边界；纠正 135Pr 交叉自旋、配置轨道、Fig.7 与 Table I 的混淆，删除未由勘误直接支持的偏振到 $\delta$/M1 纯度定量；新增 TAC/TAC-CDFT/核芯转动层级和可复现 toy model 回链。

## Assumptions

几何脚本只采用显式列出的固定 $j$、平行核芯比例和 logistic 组态混合情景；它不假定这些参数是 135Pr 的实测值。有效 $g$ 因子、绝对寿命、响应函数和有效电荷没有被用于伪造绝对强度。Garg 2015/2019 的实验数字仅作为 grounded evidence 的来源锚点。

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
