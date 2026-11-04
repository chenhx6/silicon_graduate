---
type: synthesis
title: "Casten 第十章：实验技术、反应选择与结构问题映射"
aliases: [Casten experimental design, reaction-to-observable mapping, Casten Ch.10]
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Page-level verification of Casten Chapter 10, physical PDF pp. 350-385 / printed pp. 335-363"
confidence: "high for the listed textbook design principles; not a modern detector or coupled-channel prescription"
tags: [casten, experimental-design, coulomb-excitation, arc, fusion-evaporation, heavy-ion-transfer, high-spin, spectroscopy]
sources: [book-casten-nuclear-structure-simple-perspective, book-lu-nuclear-physics-chinese, book-wu-nuclear-experiment-methods]
---

# Casten 第十章：实验技术、反应选择与结构问题映射

## Question and Scope

第十章的核心不是列举反应，而是回答：

> 一个反应和探测策略究竟能约束哪个核结构矩阵元、能级完备性、角动量布居或组态选择性？

本页核对 Casten physical PDF pp. 350–385 / printed pp. 335–363，覆盖库仑激发、
ARC/完备能谱、重离子熔合蒸发和重离子转移。原书明确这是入门设计地图，不能替代
现代 coupled-channel、Geant4/探测器响应或完整统计拟合。

## Evidence Matrix

| 结构问题 | 反应/方法 | 主要观测量 | 原书条件与实验含义 |
|---|---|---|---|
| 绝对 \(E2\) 矩阵元、集体性、四极矩 | 库仑激发 | 粒子散射角、\(\gamma\) 产额、粒子-\(\gamma\) 符合、多步激发 | 低于库仑势垒并保持足够最近接距离，避免核力作用 |
| 矩阵元相对符号和虚激发路径 | 多步库仑激发 | 多能量/多角度产额、相干干涉 | 需要同时拟合连接所有相关能级的矩阵元 |
| 选定 \(J^\pi\) 区间内是否缺级 | ARC | 归一化主跃迁强度、能级完备性、缺失的反证 | “没有观察到”只有在完备性合同成立时才是结构证据 |
| 高自旋转动带 | \((\mathrm{HI},xn)\) 熔合蒸发 | 离散 \(\gamma\) 线、多重符合、fold、连续谱 | 复合核高自旋布居、蒸发中子降激发能和角动量 |
| 组态/自旋选择性 | 重离子转移 | 出射粒子角分布、\(Q\) 值、\(\gamma\) 符合 | grazing collision 的角动量和轨道选择性 |

## Synthesis

### 1. 库仑激发：从轨道控制到矩阵元

Casten 强调库仑激发的设计逻辑：入射能量应低于库仑势垒，使最近接距离足够大，
核力影响可以忽略；电磁相互作用可计算，因而产额能反演核的电磁矩阵元。关键
控制量是 \(Z_1Z_2\)、入射能量、散射角和最近接距离 \(p\)。原书指出，实际实验
常使用低于势垒约束下的较高能量，以增加激发概率，但仍需检查核力污染。

半经典近似把入射粒子轨道视为不受小激发能显著改变的双曲线轨道。多步库仑激发
非常常见；虚激发路径可以通过不满足瞬时能量守恒的短时间中间过程贡献产额，
所以矩阵元反演一般是一个耦合方程组，而不是一次产额除以一个单步系数。

后角散射具有特殊价值：在接近 \(180^\circ\) 的几何中，横向动量转移受限，
可近似只激发 \(m=0\) 子态，从而显著减少未知取向分量。原书还指出，对主要由
E2 贡献的角分布，\(55^\circ\) 附近 \(P_2(\cos\theta)\) 近似为零，产额可近似
代表角度积分；这只是设计近似，不能替代真实有限立体角响应。

### 2. 结构设计中的相干性

多步和虚激发意味着不同路径相干叠加。对于两个路径连接同一终态，矩阵元相对
符号可以使产额增强或相消；改变入射能量会改变各路径权重，因此多能量测量能够
帮助约束相对符号。库仑激发也可以通过重取向效应约束静态四极矩，但这要求其它
连接矩阵元已被足够精确地确定。

这条原则与 Casten 第 1 章的跃迁相消定理相连：大混合或大集体性不自动等于强
跨带跃迁，矩阵元的相位和差分结构必须进入实验设计。

### 3. ARC：完备性是一种实验合同

平均共振俘获（ARC）把许多相邻共振的谱累加，使 Porter–Thomas 强度涨落平均化，
在指定自旋、宇称和激发能窗口内为“观测到全部能级”提供先验完备性条件。

其科学价值在于负证据：如果已知某 \(J^\pi\) 集合完整，缺少某条自旋序列成员可以
反向约束能带归属、未观测带头或能级安排。没有完备性合同时，“未观察到”只能表示
当前灵敏度、门条件或响应下没有看到，不能直接写成不存在。

### 4. 熔合蒸发：高自旋和冷离散谱

重离子捕获形成高激发、高角动量复合核，先通过中子蒸发降低激发能和角动量，再
沿 yrast 附近离散 \(\gamma\) 级联退激。Casten 把这一过程与高自旋研究连接起来：
熔合蒸发覆盖很宽的自旋区间，但产物偏向中子亏缺核；离散带与连续谱、fold 以及
多重符合共同决定可见结构。

多重 \(\gamma\) 符合的作用是提高谱的洁净度和选择性，按 fold 选择不同的布居/自旋
区间。对于高自旋回弯、超形变和转动带，能级放置必须结合 Doppler 校正、效率、
随机符合、本底和角关联，不能把一条看似规则的线列自动升级为带结构。

### 5. 重离子转移：直接反应和组态选择

重离子转移在 grazing 碰撞窗口内截面最大；远距离作用弱，近距离容易吸收形成
复合核，只有中间 impact parameter 区域同时具有可观转移概率和直接反应特征。
出射能量、\(Q\) 值和轨道角动量差决定可转移的角动量范围。

不同入射离子的末端核子轨道会改变 \(j=l\pm1/2\) 的选择性。与 \(\gamma\) 符合结合
后，重离子转移可以帮助识别高 \(j\) 组态和高自旋态，但能量分辨率通常不如轻粒子
转移；反应机制、角分布和模型计算必须同时核查。

## Counter-evidence

- 库仑激发低于势垒并不自动消除核力；接近势垒时 Coulomb–nuclear interference
  可能反而成为可利用的观测量。
- 后角 \(m=0\) 简化只在几何、动量转移和反应机制满足条件时成立；
  多步激发和 feeding 仍可能引入其它取向分量。
- ARC 的完备性只针对明确的 \(J^\pi\)、激发能窗口和探测灵敏度；它不能证明全能级
  图完整，也不能替代所有跃迁的强度测量。
- \((\mathrm{HI},xn)\) 的高自旋布居、转动带和超形变解释需要响应、组态和寿命/跃迁
  证据；高 fold 或规则线列本身不是充分条件。
- 转移反应的角分布既受组态选择影响，也受反应动力学、光学势和耦合道影响；不能
  只凭峰强度直接读出单粒子占据。

## Model Dependence

| 设计层 | 必须固定的输入 | 不能隐藏的模型依赖 |
|---|---|---|
| 库仑激发 | \(Z\)、能量、最近接距离、散射角、矩阵元集合 | 半经典轨道、核力污染、多步/虚路径 |
| ARC | 捕获自旋/宇称、能级窗、主跃迁和归一化 | Porter–Thomas 平均、级密度、探测下限 |
| 熔合蒸发 | 入口角动量、蒸发道、fold、响应 | 统计蒸发、feeding、连续谱和选择偏差 |
| 转移 | \(Q\) 值、光学势、grazing 轨道、出射粒子 | direct/compound 混合、组态重叠和反应耦合 |

## Research Design Bridge

对用户的在束 \(\gamma\) 谱学课题，Casten 第十章可转为以下设计顺序：

1. 先写清楚要测的是 \(B(E2)\)、\(Q_s\)、组态选择、能级完备性还是高自旋布居；
2. 再选择库仑激发、熔合蒸发或转移，而不是先选装置再寻找可解释的现象；
3. 在 proposal 阶段列出最近接距离、反应道、\(J\) 布居、feeding、Doppler 和效率；
4. 预先指定能够区分竞争解释的独立观测量，如寿命、偏振、DCO/ADO、转移角分布
   或完整性窗口；
5. 将模型矩阵元、响应矩阵和计数似然分开保存，避免把反应布居误写成结构强度。

## Limitations and Missing Evidence

Casten 第十章是 1990 年的实验方法入门，未覆盖现代 \(4\pi\) 阵列、粒子-\(\gamma\)
联合追踪、数字化获取、Geant4 响应、耦合道拟合和现代贝叶斯/似然分析。当前页面
仍需要与吴治华实验方法、Hamilton 角关联、HPGe 响应和具体 A≈130 反应源逐项对账。

## Sources

- [[book-casten-nuclear-structure-simple-perspective]]
- [[book-lu-nuclear-physics-chinese]]
- [[book-wu-nuclear-experiment-methods]]
- [[heavy-ion-fusion-evaporation-and-reaction-channel-design]]
- [[heavy-ion-fusion-experiment-design-guide]]
- [[in-beam-spectroscopy-experimental-master-manual]]
