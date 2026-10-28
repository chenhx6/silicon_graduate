---
type: research-note
title: "AMR动态转动惯量 J(2)：剪刀闭合、背弯与端点系统学"
aliases: [AMR dynamic moment of inertia audit, J2 endpoint systematics]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [roy-2011-cd110-systematics-antimagnetic, rather-2014-104pd-antimagnetic-arxiv-full, zhang-2019-104pd-pnc-antimagnetic-rotation, kumar-2023-amr-review]
created_from: Day26 delegated J2 derivation and Cd-Pd endpoint systematics
promotion_target: antimagnetic-rotation
tags: [antimagnetic-rotation, dynamic-moment-of-inertia, J2, 104Pd, 106Cd, 108Cd, 110Cd, band-termination]
---

# AMR动态转动惯量 J(2)：剪刀闭合、背弯与端点

## Research Trigger

本页把三种对象分开：用户给出的局部线性\(\omega(I)\)表达式、标准粒子加转子能量极小化、以及从实验\(E_\gamma\)有限差分得到的\(\mathcal J^{(2)}\)。如果把它们直接等同，会把110Cd的非规则能级差误写成物理负惯量，也会把104Pd的\(J^{(2)}/B(E2)\)峰值误写成纯剪刀终止定理。

## Grounded Evidence

| 核 | 原始证据 | 可复算内容 | 限制 |
|---|---|---|---|
| 106Cd | [[roy-2011-cd110-systematics-antimagnetic]] p324 Table1、Rather全文p2 | Eγ=980.8,1150.6,1310.6,1487.6,1675.5 keV，\(\mathcal J^{(2)}\)有限差分约21.3–25.0 | 低端缺I=16→14点；来源复列早期测量 |
| 108Cd | Roy p324 Table1、Rather全文p2 | Eγ=956,1105,1260,1469 keV，\(\mathcal J^{(2)}\)约19.1–26.8 | I=22点为effective lifetime；能级范围短 |
| 110Cd | Roy p324 Table1、pp325–326 | Eγ=1075,1224,1323,1314,1358 keV，有限差分有大峰、负值和异常末端 | 1323/1314接近且线重合；不能把负值当稳定物理平台 |
| 104Pd | [[rather-2014-104pd-antimagnetic-arxiv-full]] p10 Table1 | B(E2)、\(J^{(2)}/B(E2)\)和由两者相乘得到的派生\(J^{(2)}\) | 直接从完整图1逐点重算Eγ尚未完成；26+为effective lifetime |

## Provisional Reasoning

### 1. 用户给出的局部线性式：直接微分结果

设所有角动量以\(\hbar\)为单位，并把\(A=j_1j_2\)或其它明确的剪刀斜率常数固定，则用户给出的式子为

$$
\omega(I)=\frac{I-J_s}{\mathcal J_c}
+\frac{3V_2}{A^2}(I-I_0).
$$

直接微分得到

$$
\frac{d\omega}{dI}=\frac1{\mathcal J_c}+\frac{3V_2}{A^2},
$$

以及

$$
\boxed{\mathcal J^{(2)}
=\frac{dI}{d\omega}
=\left(\frac1{\mathcal J_c}+\frac{3V_2}{A^2}\right)^{-1}}.
$$

因此，只要\(\mathcal J_c,V_2,A\)不随\(I\)或\(\theta\)变化，该局部线性式本身预测的是常数\(\mathcal J^{(2)}\)，而不是剪刀闭合时自动变化的曲线。要得到\(\mathcal J^{(2)}(\theta)\)，必须显式加入\(V_2(\theta)\)、有效刃长度/占据变化、核芯惯量变化、配对重排或更高阶项。

若\(V_2>0\)，该线性化惯量为正；若\(V_2\to0\)且无核芯项，则惯量趋于无穷，表示剪刀能量对角动量的一阶曲率消失，而不是一个有限的终止尖峰。

### 2. 从P2剪刀能量重新推导：物理约束下是串联而非并联

取

$$
E_s(\theta)=V_2P_2(c),\quad c=\cos\theta,
$$

$$
I_s=I_0+A c.
$$

由于

$$
\frac{dP_2}{dc}=3c,
$$

得到剪刀自身频率

$$
\omega_s=\frac{dE_s/dc}{dI_s/dc}
=\frac{3V_2c}{A}
=\frac{3V_2}{A^2}(I_s-I_0).
$$

若核芯与剪刀共享同一旋转频率，核芯角动量为\(I_c=\mathcal J_c\omega_s\)，总角动量满足

$$
I=I_s+I_c
=I_0+\left(A+\frac{3\mathcal J_cV_2}{A}\right)c.
$$

于是

$$
\boxed{\mathcal J^{(2)}
=\frac{dI}{d\omega_s}
=\mathcal J_c+\frac{A^2}{3V_2}}.
$$

这里核芯惯量与剪刀惯量是串联相加。用户给出的直接相加频率式则给出倒数相加的形式；它可以作为一种局部经验展开，但若要称为粒子加转子极小化结果，必须说明\(J_s,I_0,A\)的定义和约束，否则会把两个不同的响应组合规则混在一起。

### 3. 剪刀闭合端点\(\theta\to0\)没有自动奇点

在\(E_s=V_2P_2(\cos\theta)\)、\(I_s=I_0+A\cos\theta\)模型中，

$$
\frac{dE_s}{d\theta}=-3V_2\sin\theta\cos\theta,
\qquad
\frac{dI_s}{d\theta}=-A\sin\theta.
$$

两者都在\(\theta\to0\)时线性趋于零，但比值有限：

$$
\omega_s\to\frac{3V_2}{A},
\qquad
\mathcal J^{(2)}\to\mathcal J_c+\frac{A^2}{3V_2}.
$$

因此理想二次\(P_2\)模型在端点给出有限平台。真实端点出现尖峰或骤降，需要其它因素：

- 组态交叉或背弯，使\(A\)和有效\(I_s\)发生非解析变化；
- 配对和off-diagonal alignment改变角动量分解；
- \(\beta_2,\gamma\)随频率变化，令E2振幅和角动量响应不再由同一\(\theta\)控制；
- 有限差分遇到相邻\(E_\gamma\)几乎相等、能级重叠或side-feeding不稳。

### 4. 从实验能级提取\(\mathcal J^{(2)}\)

对\(\Delta I=2\)序列，取

$$
\hbar\omega(I)\simeq\frac12E_\gamma(I\to I-2),
$$

$$
\mathcal J^{(2)}(I)
=\frac{4\hbar^2}
{E_\gamma(I+2\to I)-E_\gamma(I\to I-2)}.
$$

本页脚本使用Roy复列的原始\(E_\gamma\)值，得到：

| 核 | 中心自旋 | \(\mathcal J^{(2)}\) (\(\hbar^2\)/MeV) | 解释 |
|---|---:|---:|---|
| 106Cd | 18,20,22,24 | 23.56,25.00,22.60,21.29 | 约22–25的平台并轻微下降 |
| 108Cd | 16,18,20 | 26.85,25.81,19.14 | 前两点近平台，末点下降 |
| 110Cd | 16,18,20,22 | 26.85,40.40,−444.44,90.91 | 非规则间隔；负值为有限差分结果，不能直接当负物理惯量 |
| 104Pd | 16,18,20,22,24 | 29.20(3.17),30.998(3.98),63.50(4.73),36.70(3.99),38.80(7.84) | 由Table1的B(E2)乘J(2)/B(E2)派生；I=20附近峰值 |

110Cd的\(I=20\)点来自1323→1314 keV的负差9 keV；Roy原文已指出1323和1314 keV线存在重合与门控分析问题，高自旋末端还含effective feeding lifetime。因此这个负值是“能级间隔不规则/有限差分不稳定”的诊断，不是核出现负惯量的证据。

104Pd的Table1直接给出\(J^{(2)}/B(E2)\)而不是单独的\(J^{(2)}\)。本页将比值乘B(E2)作为派生量，所以保留误差传播和来源层级；它显示I=20附近的比值峰与派生惯量峰共同出现，不能把高频比值上升简单解释成\(B(E2)\)单独下降。

### 5. 四核系统学的物理解释

**106Cd。** 两质子空穴和中子\((g_{7/2}/d_{5/2})^2(h_{11/2})^2\)构成较纯的双剪刀带。Eγ间隔的有限差分给出约22–25\(\hbar^2/\mathrm{MeV}\)的相对平坦响应。B(E2)随自旋下降，使\(\mathcal J^{(2)}/B(E2)\)上升；但这里的\(\mathcal J^{(2)}\)平台是能级曲率的结果，不能由E2几何幂次单独推出。

**108Cd。** 低中自旋点仍近似平台，末端差分降至约19\(\hbar^2/\mathrm{MeV}\)。该变化可与中子占据、背弯和有限带长共同相关；末端B(E2)又使用effective lifetime，不能把最后一点当作与前点同质量的精确独立证据。

**110Cd。** Roy的模型引入\(\mathcal J_c=19.5\ \hbar^2/\mathrm{MeV}\)，解释AMR和核芯转动共同产生更宽的自旋区间和较慢E2下降。但原始能级差本身在20–24附近不规则，不能从有限差分表直接宣布光滑平台。模型的“核芯缓降”是对I(ω)、B(E2)和配置的联合解释，不是单独由\(\mathcal J^{(2)}\)峰值证明。

**104Pd。** Rather Table1的\(B(E2)\)从0.26(2)降至0.02(1)，\(J^{(2)}/B(E2)\)从112.3(8.6)升至554.3(79.2)。由此派生的\(J^{(2)}\)在I=20处约63.5，随后回到约37–39，说明背弯/组态重排附近的尖峰或曲率变化。Zhang PNC给出约0.4 MeV的h11/2中子背弯、0.4–0.55 MeV的g9/2质子占据重排以及高频形变收缩；这些机制比“纯剪刀闭合”更符合端点附近的非平滑行为。

### 6. 端点行为的证据阶梯

1. **直接能级曲率：** 由相邻Eγ差分得到\(\mathcal J^{(2)}\)；这是端点行为最直接的谱学输入。
2. **派生强度比：** 将寿命转成B(E2)，再与\(\mathcal J^{(2)}\)组合；受stopping、feeding和误差协方差影响。
3. **模型解释：** 用\(P_2\)剪刀、核芯惯量、配对和占据交叉解释平台或尖峰；需保留参数依赖。
4. **终止判定：** 需要新带、终止后能级、组态重组或独立形变/配对观测；单个\(J^{(2)}\)尖峰不足以认证终止。

## Reproducible Artifacts

目录：`outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-j2-endpoint-20261029/`。

- `amr-j2-endpoint-20261029_j2.py`：标准库计算用户公式导数、受约束粒子加转子推导和四核有限差分。
- `j2_systematics.csv`：106/108/110Cd直接Eγ差分与104Pd派生\(J^{(2)}\)。
- `j2_model_derivation.json`：公式、端点极限、符号和物理解读边界。

## Assumptions

\(E_\gamma\)有限差分按\(\Delta I=2\)序列中心自旋定义；104Pd的\(J^{(2)}\)由表中\(B(E2)\)和\(J^{(2)}/B(E2)\)相乘得到，非独立Eγ重算；110Cd的负值保留为数据诊断。\(P_2\)模型把\(A,V_2,\mathcal J_c\)视为局部常数。

## Competing Explanations

\(\mathcal J^{(2)}\)平台可来自平滑剪刀势曲率、核芯转动或两者共同响应；尖峰/骤降可来自背弯、配置交叉、配对变化、形变变化、线重叠和有限差分放大。不能只凭\(J^{(2)}/B(E2)\)判定AMR。

## Transfer Conditions

公式微分、\(P_2\)端点极限和\(E_\gamma\)有限差分可跨核迁移。具体数值、bandhead、有效寿命、\(\mathcal J_c\)、\(A\)和构型必须绑定各核原始来源；104Pd表值不能外推到106/108Pd。

## Failure Conditions

若把用户局部线性式直接写成唯一粒子加转子极小化公式，把负有限差分当负物理惯量，把104Pd派生\(J^{(2)}\)当直接Eγ提取，或把110Cd非规则点删掉后声称光滑平台，本页结论失效。

## Falsification or Reverse Tests

对同一\(P_2\)势加入\(P_4(c)\)项，检验端点\(J^{(2)}\)是否保持常数；加入频率依赖\(\mathcal J_c\)和配对强度，检验平台是否转为峰值；将110Cd的1323/1314 keV互换或纳入线重合协方差，检查负有限差分是否消失；取得104Pd完整Eγ表后独立重算Table1的\(J^{(2)}/B(E2)\)。

## Open Questions

104Pd图1逐点Eγ与自旋约定能否完整数字化并独立复算Table1？110Cd 1323/1314 keV线重合后的协方差是否足以解释有限差分尖峰？同一PNC/投影框架能否同时描述Cd平台、Pd I=20峰和高频形变收缩？

## Knowledge Impact and Learning Decision

`supports` 106Cd约22–25平台、104Pd I=20附近动态惯量峰和110Cd有限差分不规则性；`revises` 用户公式的物理解释、110Cd平滑平台和104Pd完全恒定J(2)的表述；`limits` 104Pd直接Eγ复算、110Cd高自旋协方差和完整终止波函数仍未完成。

## Sources

- [[roy-2011-cd110-systematics-antimagnetic]]
- [[rather-2014-104pd-antimagnetic-arxiv-full]]
- [[rather-2014-104pd-antimagnetic-first-page]]
- [[zhang-2019-104pd-pnc-antimagnetic-rotation]]
- [[kumar-2023-amr-review]]

## Human Review

Codex source/claim self-audit；保持`unreviewed`，未改变既有撤回和课程信用边界。

## Review Status

公式和有限差分已通过标准库计算；104Pd派生惯量和110Cd异常点均保留来源层级与数据边界。

## Promotion or Rejection History

2026-10-29：新增AMR动态惯量研究笔记；从用户局部公式、P2约束模型和实验有限差分三层对账，未把经验平台或异常点升级为普适终止判据。

## Continuation Handoff

优先取得104Pd图1逐点Eγ数字化和110Cd线形协方差；随后在P2+P4、频率依赖核芯惯量和配对模型中测试端点峰值是否由组态交叉产生。
