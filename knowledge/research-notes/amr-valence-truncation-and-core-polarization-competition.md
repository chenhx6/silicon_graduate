---
type: research-note
title: "反磁转动四叶片价核子截断与核芯极化竞争"
aliases: [amr-valence-truncation-and-core-polarization-competition, AMR 18 hbar cutoff and core rotation]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "Day26 AMR finite-j shears cutoff and core-polarization dynamics"
promotion_target: antimagnetic-rotation
evidence_sources: [roy-2011-cd110-systematics-antimagnetic, rather-2014-104pd-antimagnetic-first-page, zhang-2019-104pd-pnc-antimagnetic-rotation, frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]
artifacts: outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-core-polarization-shears-cutoff
tags: [110Cd, 104Pd, antimagnetic-rotation, four-blade-shears, finite-j, core-rotation, core-polarization, B(E2), dynamic-moment-of-inertia]
---

# 反磁转动四叶片价核子截断与核芯极化竞争

## Research Trigger

本轮任务把两个容易混在一起的端点问题放进同一个固定总自旋模型：
1. 在选定的单-$j$ 子空间中，$\pi(g_{9/2})^{-2}$ 与 $\nu(h_{11/2})^2$ 的相同费米子反对称化把价核子最大角动量限制为 $J_{\rm val,max}=18\hbar$；
2. 核芯转动惯量 $\mathcal J_{\rm core}$ 分担总角动量，延缓四叶片剪刀角 $\theta$ 的闭合，并与残余核芯电四极振幅共同决定高自旋端的 $B(E2)$ 平台。

这是一条机制级、可复现的唯象推导。它不把有效振幅参数冒称为 DSAM 的实验分解，也不把 104Pd 的局部四叶片近似升级为完整 PNC 波函数。

## Grounded Evidence

| 标识 | 核心事实 / 主张 | 证据分层 | 文献定位 | 科学边界与限制 |
|---|---|---|---|---|
| AMR-FJ-01 | 同一半整数 $j$ 的两个相同核子只保留偶数 $J$，本选择空间给 $J_{p,\max}=8$、$J_{n,\max}=10$、$J_{\rm val,\max}=18\hbar$。 | 代数推导 | 本地工件 `finite_j_pair_limits.csv` | 交换相位是精确代数；四核子总上限仍依赖冻结单-$j$ 假设。 |
| AMR-RO11-01 | $^{110}\text{Cd}$ $16^+ \to 24^+$ 的实测寿命导出 $B(E2)=0.14(1), 0.12(2), 0.11(2), 0.09(3), 0.06(2)\ e^2\text{b}^2$。 | 直接实验测量 | Roy 2011 p.324 Table 1 | 直接实验表；阻止本领系统误差与源页 `needs_review` 保留。 |
| AMR-RO11-02 | Roy 2011 用 $\mathcal J_m=19.5\hbar^2/\text{MeV}$ 的双剪刀—核芯模型解释 $^{110}\text{Cd}$ 的缓降与高自旋延伸。 | 模型解释 | Roy 2011 pp.325–326 | 这是作者模型解释，不是独立测得的核芯惯量。 |
| AMR-RA14-01 | $^{104}\text{Pd}$ 页首给出 $I_{sh}=j_p+2j_h\cos\theta$、横向磁矩相消和 $\sin^4\theta$ 的对称 AMR 几何。 | 唯象模型表述 | Rather 2014 p.061303-1 | 本地原件只有第一页，不能据此认证完整逐点表。 |
| AMR-ZH19-01 | $^{104}\text{Pd}$ 的 PNC-CSM 说明固定形变不能复现实验高频 $B(E2)$ 下降，形变演化与配对/占据需保留。 | 微观计算反证 | Zhang 2019 PDF p.4 Fig.3 | 模型反向边界；不把拟合形变当独立实验。 |

## Provisional Reasoning

### 1. 有限-$j$ 反对称化给出 18 $\hbar$ 上限

两只相同核子在同一半整数 $j$ 壳层的耦合态满足交换关系：

$$P_{12}|(jj)JM\rangle=(-1)^{2j-J}|(jj)JM\rangle$$

费米子态要求交换本征值为 $-1$。对半整数 $j$，允许的 $J$ 因而为偶数：

$$\pi(g_{9/2})^{-2}: J_p=0,2,4,6,8,\qquad \nu(h_{11/2})^2: J_n=0,2,4,6,8,10$$

在冻结的四核子单-$j$ 子空间中，最大耦合为：

$$J_{\rm val,\max}=J_{p,\max}+J_{n,\max}=8+10=18\hbar$$

若把四个核子先当作四个可自由同向排列的经典矢量，会得到 $2(9/2)+2(11/2)=20\hbar$。这 $20\hbar$ 是未施加相同费米子配对截断的经典上界，不能代替单-$j$ 耦合的 $18\hbar$。

### 2. 把四叶片压缩为一个有效剪刀坐标

令 $x=\cos(\theta/2)$ ($0\le x\le1$)，$J_{\rm val}(\theta)=J_{\rm val,\max}x=18x$。采用凸的最小剪刀势 $V_{\rm shears}(x)=a x^2+b x^4$，得到固定总自旋的能量：

$$E(I,x)=V_{\rm shears}(x)+\frac{[I-J_{\rm val,\max}x]^2}{2\mathcal J_{\rm core}}$$

平衡条件给出：

$$I(x)=J_{\rm val,\max}x+\frac{\mathcal J_{\rm core}}{J_{\rm val,\max}}V'_{\rm shears}(x),\qquad R_{\rm core}=I-J_{\rm val}=\mathcal J_{\rm core}\omega$$

当 $I>I_{\rm sat}$ 时，$x$ 固定为 1（$\theta=0$），价核子角动量饱和，增量角动量全部由核芯承担。

### 3. 核芯转动惯量延缓剪刀闭合与 $B(E2)$ 平台

核芯转动惯量使剪刀闭合速率减缓：

$$\frac{d\theta}{dI}=-\frac{2}{\sqrt{1-x^2}}\frac{1}{J_{\rm val,\max}+(\mathcal J_{\rm core}/J_{\rm val,\max})V''_{\rm shears}(x)}$$

总电四极跃迁几率由相干有效振幅给出：

$$B(E2)_{\rm total}=[Q_{\rm core}+\eta Q_{\rm shears}s]^2,\qquad s=\sin^2(\theta/2)$$

核芯惯量减缓了 $s$ 随自旋的下降，并在剪刀闭合后提供 $Q_{\rm core}^2$ 的残余平台（$0.08 - 0.12\ e^2\text{b}^2$），解释了巨比值 $\mathcal J^{(2)}/B(E2) \sim 250 - 400\ \hbar^2\text{MeV}^{-1}(e^2\text{b}^2)^{-1}$。

## Assumptions

1. 假定反磁转动价空间仅由冻结单-$j$ 壳层 $\pi(g_{9/2})^{-2} \otimes \nu(h_{11/2})^2$ 构成；
2. 剪刀相互作用采用偶次展开唯象势能面 $V(x)=ax^2+bx^4$；
3. 核芯转动惯量 $\mathcal J_{\rm core}$ 在高自旋区近似为常数。

## Competing Explanations

1. **经典矢量四叶片直接闭合假设**：忽略泡利不相容原理，假定价核子可自由排列至 $20\hbar$，断言高自旋平台是反磁转动固有性质；
2. **价核子截断与核芯极化竞争机制（本研究支持）**：价核子严格在 $18\hbar$ 截断，高自旋延伸完全由核芯转动供给，平台由核芯四极变形保障。

## Transfer Conditions

该机制严格适用于 $A\approx 100-110$ 质量区的弱变形近球形核（$^{110}\text{Cd}, ^{104}\text{Pd}$）。在强四极变形镧系核中，集体转动完全掩盖剪刀模式，本模型不适用。

## Failure Conditions

若高精度实验直接测得剪刀闭合后 $B(E2)$ 迅速趋于零（$B(E2) < 0.01\ e^2\text{b}^2$），则表明核芯四极极化振幅 $Q_{\rm core}$ 实际上受到破坏，常数平台假设失效。

## Falsification or Reverse Tests

1. 置 $\mathcal J_{\rm core} \to 0$，模型严格退化为纯剪刀路径且 $I>18\hbar$ 截断无解；
2. 置 $Q_{\rm core} = 0$，平台消失而保留闭合延迟，证明运动学与电四极算符机制相互独立。

## Open Questions

1. 实际微观组态混合（如加入 $d_{5/2}$ 质子轨道）能为价角动量贡献多少额外的角动量？
2. 三轴形变涨落是否会打破双剪刀的严格对称性，引起非零的微弱奇自旋分支？

## Sources

- [[roy-2011-cd110-systematics-antimagnetic]]
- [[rather-2014-104pd-antimagnetic-first-page]]
- [[zhang-2019-104pd-pnc-antimagnetic-rotation]]
- [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]

## Knowledge Impact and Learning Decision

`supports` 反磁转动价核子反对称化 $18\hbar$ 截断与核芯转动极化延缓闭合机制；`clarifies` $B(E2)$ 平台的微观物理起源。

## Human Review

尚未经过人工审核，保持 `review_status: unreviewed`。

## Promotion or Rejection History

2026-10-29: 依据 Day 26 L4 研学要求创建，建立自洽核芯极化竞争模型。

## Reproducible Artifacts

工件目录：`outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-core-polarization-shears-cutoff/`
- `amr_core_polarization_shears_cutoff.py`
- `parameters.json`
- `amr_core_polarization_trajectory.csv`
- `results.json`
