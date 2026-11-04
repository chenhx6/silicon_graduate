---
type: method
title: "N=40 岛反转：核子去除反应与壳模型结构合同"
aliases: [Gade N40 island, nucleon-removal shell-model contract]
method_type: "rare-isotope-reaction-and-shell-model"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Nuclear Shell Model 70 Years article 9, selected article sections and figures"
confidence: "high for reaction-analysis workflow; conditional for individual configuration assignments"
tags: [n40-island, knockout-reaction, nucleon-removal, gamma-spectroscopy, lnps, shell-evolution]
sources: [book-nuclear-shell-model-70-years]
---

# N=40 岛反转：核子去除反应与壳模型结构合同

## Purpose

把 Gade 文章中的 \(N=40\) 岛反转实验方法转成可复用的稀有束流分析合同：

```text
projectile identification
-> nucleon removal / knockout
-> residue momentum and channel selection
-> prompt gamma spectroscopy
-> partial cross sections + spectroscopic overlaps
-> LNPS shell-model configuration test
```

## Inputs and Assumptions

- 研究对象为近 \(N=40\) 的 neutron-rich Fe、Cr、Ti 等稀有核；
- 采用逆运动学快速束流，靶可为 \(^{9}\mathrm{Be}\)、\(^{12}\mathrm C\)、液氢或其它
  适合反应机制的材料；
- 核子去除被视为短时间、直接反应，通常与 eikonal/冲量近似和壳模型波函数结合；
- 需要区分 inclusive cross section、partial cross section、gamma feeding 和
  未观测高能级；
- LNPS 等有效相互作用的构型组分、谱因子和反应模型必须保存版本和参数。

## What It Can Establish

### Reaction selectivity

快速一核子去除反应的残核平行运动量分布对被去除核子的轨道角动量 \(l\) 和
分离能敏感；部分截面与壳模型波函数重叠/谱因子相关。因而它可以：

- 区分单粒子主导和多粒子关联的候选态；
- 检验 \(f_{7/2}\)、\(p\)、\(g_{9/2}\) 等轨道占据；
- 将实验残核态与 LNPS 构型组分联系起来。

两核子去除反应还需要 two-nucleon amplitudes，残核平行运动量分布对被去除两核子
总角动量敏感，不能用两个独立单粒子截面简单相乘。

\((p,2p)\)、\((p,pn)\) 反应可在氢靶上进行准自由敲除，提供不同于重靶 knockout
的单粒子选择性，但反应模型和束流/靶响应必须重新标定。

### Gamma spectroscopy interface

厚靶和高效率阵列可以补偿稀有束流强度低的问题，但必须处理：

- 反应残核的 prompt \(\gamma\) 级联；
- 高能未观测 \(\gamma\) feeding；
- Pandemonium-like 漏失；
- 阵列效率、分辨率、门条件和随机符合；
- 激发能级的自旋宇称与 \(\gamma\) 线身份。

结合 \(E(2^+_1)\)、\(E(4^+_1)\)、\(R_{4/2}\)、\(B(E2)\) 和部分截面，可检验
从正常壳序到 intruder \(pf\)-\(g_{9/2}\) 变形组态的演化。

### N=40 structural interpretation

Gade 文章把 \(N=40\) 岛反转描述为：

- neutron \(g_{9/2}\)、\(d_{5/2}\) intruder 组态逐渐降低；
- proton–neutron 四极关联增强；
- 正常 \(pf\) 壳序和 intruder 多粒子–多空穴构型竞争；
- Fe、Cr、Ti 链的 \(2^+\)、\(4^+\) 能量和集体性沿 Z 变化；
- \(N=40\) 之后可继续向 \(N=50\) 岛反转外推，但仍需实验验证。

## What It Cannot Establish Alone

- knockout partial cross section 不能单独等同于纯谱因子；
- eikonal reaction model、核芯破碎、feeding 和占据淬灭都会影响反演；
- 一条 \(\gamma\) 线和一个 \(2^+\) 能量不能单独确认形状；
- LNPS 再现能谱不能独立证明唯一构型；
- \(N=40\) 岛反转的 \(\gamma\)-soft/刚性三轴程度需要 \(B(E2)\)、四极矩、寿命
  和多通道反应共同约束。

## Reproducibility Contract

每个稀有束流核子去除分析至少保存：

```text
beam PID -> target/energy/thickness -> reaction model/version
         -> residue PID -> momentum distribution
         -> gamma efficiency/feeding gates
         -> inclusive and partial cross sections
         -> shell-model interaction/model space
         -> spectroscopic overlap and uncertainty
```

## Sources and Locators

- 合集 article 9，目录范围 article pp.211–222；
- 文章正文 physical PDF 页码和原文章页码需按合集物理页与文章页双重记录；
- 重点覆盖 \(N=40\) Fe/Cr/Ti、LNPS、nucleon removal、prompt \(\gamma\) 和 partial
  cross-section 章节与图表。

## Sources

- [[book-nuclear-shell-model-70-years]]
- [[in-beam-charged-particle-pid-delta-e-telescope]]
- [[charged-particle-identification-and-stopping-power]]
- [[sn100-region-highspin-spectroscopy-contract]]
- [[heavy-ion-abrasion-ablation-fragmentation]]
