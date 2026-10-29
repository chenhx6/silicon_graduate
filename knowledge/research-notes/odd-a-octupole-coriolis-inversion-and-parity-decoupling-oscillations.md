---
type: research-note
title: "奇 A 八极反射不对称诱发的科里奥利反转与宇称退耦振荡"
aliases: [odd-A octupole Coriolis inversion, parity-decoupling oscillation, Delta-j-3 parity mixing]
created: 2026-10-29
updated: 2026-10-29
category: research-notes
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: Day26 directed study of odd-A octupole Coriolis inversion
evidence_sources: [nndc-2009-ra225-adopted-parity-doublet, nndc-2022-ac225-adopted-parity-doublet, nomura-2018-odd-mass-ba-octupole, odd-a-actinide-parity-doublet-direct-e3-transitions-angular-coupling, ra225-parity-doublet-coriolis-064]
tags: [odd-A, octupole, parity-doublet, Coriolis, decoupling, Delta-j-3, 225Ra, 225Ac, 145Ba, ENSDF, reproducible-model]
promotion_target: octupole-mr-amr-evidence-gradient
---

# 奇 A 八极反射不对称诱发的科里奥利反转与宇称退耦振荡

## Research Trigger

本任务追问：奇核子占据一对由八极场连接的异宇称轨道（典型 $\Delta j=3$）时，为什么 $^{225}$Ra 的同自旋异宇称能级差在 $I=3/2,7/2$ 变成负值，而 $^{225}$Ac 的低带差值保持正且平滑？目标是把 ENSDF 能级、$K$ 依赖的退耦几何和八极轨道混合放入同一可复现三参数模型。

## Grounded Evidence

- NNDC $^{225}$Ra 评价列出正带 0.00, 25.41, 42.77, 111.60 keV 和负带 55.16, 120.36, 31.56, 69.36 keV（按同自旋配对）。因此 $\Delta_{-+}=E_- - E_+$ 为 55.16, -11.21, 94.95, -42.24 keV，负值在 $3/2,7/2$。[NNDC source，225088001 低能 L/G 记录]
- NNDC $^{225}$Ac 评价的清晰低带配对为 $3/2$: 0.00/40.10，$5/2$: 29.91/64.69，$7/2$: 77.13/105.01 keV，差值 40.10, 34.78, 27.88 keV；更高带含重复的 $5/2,7/2,9/2$，不是唯一双重态序列。[NNDC source，225089001 L90–170]
- $^{225}$Ra 31.50-keV E1 的评价强度为 0.00081(20) W.u.；$^{225}$Ac 40.09-keV E1 为 0.00171(15) W.u.。它们支持相反宇称之间的跃迁联系，不能单独给出 Coriolis 轨道矩阵元或静态梨形的唯一证明。
- Nomura 等的 $^{145}$Ba CDFT+sdf-IBFM 计算显示低能态与较高八极成分具有状态依赖性；该模型不是 ENSDF 低能宇称双重态数据集，故本工件将 145Ba 作为阻塞对照而非拟合对象。

## Provisional Reasoning

### 1. 直接矩阵元与微观有效项

宇称守恒的 Coriolis 算符 $H_C=-A(I_+j_-+I_-j_+)$（$A=\hbar^2/(2\mathcal J)$）不改变单粒子宇称。因此在纯宇称本征态上 $\langle +,K|H_C|-,K\rangle=0$，不能把该直接矩阵元写成非零实验事实。轴向八极场 $V_3\propto Q_{30}$ 是宇称奇算符，可连接 $\Delta l=3,\Delta j=3$ 的轨道。消去中间态后，最低阶有效异宇称项为

$$H^{+-}_{\rm eff}=\sum_n\left[\frac{\langle +|H_C|n\rangle\langle n|V_3|-\rangle}{E_--E_n}+\frac{\langle +|V_3|n\rangle\langle n|H_C|-\rangle}{E_+-E_n}\right].$$

令 $a^{(\pm)}$ 表示正、负宇称投影带的有效退耦常数，则 $d_C=A[a^{(+)}-a^{(-)}]$ 是上述二阶路径、轨道占据、能量分母和核芯极化的压缩量。八极场改变的是有效差异，不是制造违反宇称选择定则的直接 $\langle +|H_C|-\rangle$。

### 2. 三参数能谱与 $S(I)$

定义 $\Delta(I)=E_-(I)-E_+(I)$、$X_K(I)=I(I+1)-K^2$，模型为

$$\Delta(I)=d_0+d_A X_K(I)+d_C\,\eta_K(I),\qquad \eta_K(I)=\begin{cases}(-1)^{I+1/2}(I+1/2),&K=1/2\\0,&K\ge3/2.\end{cases}$$

交替宇称交错位移定义为 $S(I)=(-1)^{I+1/2}\Delta(I)$，故对 $K=1/2$ 有 $S(I)=(-1)^{I+1/2}[d_0+d_A X_K(I)]+d_C(I+1/2)$。它把规则的 $d_0,d_A$ 趋势与 Coriolis 核分开：大 $d_C$ 使原始 Delta 交替变号，而 $S(I)$ 具有平滑残差。$K=3/2$ 时一次 Coriolis 操作不能把 $+K$ 闭合到 $-K$，$\eta=0$；二阶/三轴混合仍可能留下小修正，但不产生纯 $K=1/2$ 的一阶交替项。

### 3. 数值结果

工件 `workers/odd-a-octupole-coriolis/` 对 Ra 四点拟合得到 $(d_0,d_A,d_C)=(31.31,0.438,-20.43)$ keV，最大残差 3.20 keV；负的观测 $\Delta$ 出现在 $I=3/2,7/2$，即表观排序反转。Ac 约束 $d_C=0$ 得到 $(d_0,d_A)=(41.54,-1.016)$ keV，最大残差 0.15 keV，差值从 40.10 降至 27.88 keV，未出现负值。数值是评价能级的有效描述，不是轨道波函数反演。

## Assumptions

采用轴对称粒子—转子展开、同一带内 A/B 配对和低阶 $V_3H_C$ 消去；把高阶组态混合、配对和核芯极化吸收到三个参数；Ra 的负宇称带标签按评价对象使用，Ac 仅使用明确低带配对；能量单位为 keV。

## Competing Explanations

能级交错也可能来自不同 $K$ 带误配、带交叉、四极惯量差、八极振动而非静态双阱、三轴 Coriolis 混合或评价 Jπ 的暂定性。单一四点拟合不能排除这些解释。

## Transfer Conditions

当相反宇称轨道有显著八极跃迁密度、能量分母不太大、且 $K=1/2$ 的镜像分量可由一次 $j_\pm$ 接通时，$d_C$ 可产生明显交错。对 $K\ge3/2$，应把一阶退耦核置零并检查二阶混合。145Ba 只有在获得同一 blocked-EDF 下的带连接和跃迁矩阵元后才能转为定量比较。

## Failure Conditions

若直接声称 $\langle +|H_C|-\rangle\ne0$，则违反宇称选择定则；若把 Ac 重复的同自旋能级自动合并为单一双重态，拟合对象不再可识别；若以 145Ba 模型预测当作评价实验值，证据层级失真。

## Falsification or Reverse Tests

1. 对每个候选轨道做 blocked-HFB/QRPA，分别计算 $V_3$、$j_\pm$ 和能量分母，检查其和能否同时给出 $d_C\approx-20$ keV 与 E1/E3 强度。
2. 加入 $I\ge9/2$ 的 Ra 评价能级；若单一 $d_C$ 不能维持交错残差，转向带交叉或多组态模型。
3. 对 Ac 检验近邻 $K=5/2$ 带混合；若出现大幅交错，说明孤立带的 $a=0$ 边界被组态混合突破。

## Open Questions

- $^{225}$Ra 正、负宇称组态的实际 Nilsson 成分及 Δj=3 主导对尚未由本地原始转移数据确定。
- $d_C$ 的符号是否主要来自八极矩相位、能量分母，还是粒子—核芯极化？
- $^{145}$Ba 的阻塞是否能在同一微观算符核中预测 E3 淬灭和退耦变化？

## Human Review

本页为 Codex self-audit 的 `ai-draft`，`review_status: unreviewed`。ENSDF 数值和局部模型结果已自洽复算，但轨道级微观矩阵元、原始实验带连接和静态八极形变仍需人工定向复核。

## Promotion or Rejection History

2026-10-29：由 Day26 任务建立；保留 Ra 的反转拟合与 Ac 的 $K=3/2$ 边界，并将“直接 Coriolis 异宇称矩阵元”修正为八极场诱发的二阶有效项。尚未晋升。
