---
type: method
title: "Shimizu：壳模型、MCSM 与 QVSM 的大模型空间计算合同"
aliases: [Shimizu MCSM QVSM, Monte Carlo shell model, quasiparticle vacua shell model]
method_type: "large-scale-shell-model-computation-and-convergence"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Nuclear Shell Model 70 Years article 6, full main-text reading"
confidence: "high for reviewed computational framework and benchmark values; conditional for physics transfer"
tags: [shell-model, configuration-interaction, lanczos, monte-carlo-shell-model, qvsm, pairing, shape-coexistence, numerical-convergence]
sources: [book-nuclear-shell-model-70-years]
---

# Shimizu：壳模型、MCSM 与 QVSM 的大模型空间计算合同

## Purpose

这篇综述解决的是一个直接影响核结构研究的问题：当模型空间进入中重核、
跨主壳层或需要显式配对时，传统壳模型的完整对角化如何继续提供可信的
低能谱和波函数信息。它把三层对象分开：

1. 常规 configuration-interaction 壳模型和 Lanczos 对角化；
2. 用投影形变 Slater 行列式压缩模型空间的 Monte Carlo Shell Model (MCSM)；
3. 用粒子数投影准粒子真空处理重核配对的 QVSM。

这篇文章对本 Wiki 的直接价值是建立“计算结果—收敛诊断—结构解释”的合同。
它解释了为什么 MCSM/QVSM 可以进入形状共存、\(\gamma\) 带、壳演化和
\(^{100}\mathrm{Sn}\) 邻域问题，但也明确了计算收敛不等于实验模式确认。

## Inputs and Assumptions

### Conventional shell-model representation

壳模型哈密顿量写成

\[
\hat H=\sum_i\epsilon_i c_i^\dagger c_i
+\sum_{ijkl}v_{ijkl}c_i^\dagger c_j^\dagger c_l c_k .
\]

波函数在 M-scheme 基底中展开为

\[
|\Psi\rangle=\sum_{\alpha=1}^{D}v_\alpha|M_\alpha\rangle ,
\]

其中 \(D\) 是固定 \(M^\pi\) 子空间的 M-scheme 维数。J-scheme 基底具有好角动量
\(J\)，维数通常小约两个数量级，但 M-scheme 哈密顿量更稀疏，适合矩阵—向量
乘法和大规模并行。

文章表 1 给出的量级示例为：

| 核素 | 模型空间 | M-scheme 维数 | J-scheme 维数 |
| --- | --- | ---: | ---: |
| \(^{12}\mathrm C\) | p 壳 | 51 | 9 |
| \(^{28}\mathrm{Si}\) | sd 壳 | \(9.371\times10^4\) | 3372 |
| \(^{56}\mathrm{Ni}\) | pf 壳 | \(1.08\times10^9\) | \(1.54\times10^7\) |
| \(^{78}\mathrm Y\) | \(f_{5/2}pg_{9/2}\) | \(1.31\times10^{10}\) | \(1.11\times10^8\) |
| \(^{130}\mathrm{Sm}\) | jj55 | \(2.06\times10^{15}\) | \(9.58\times10^{12}\) |
| \(^{172}\mathrm{Dy}\) | jj56 | \(1.71\times10^{19}\) | \(5.54\times10^{16}\) |

这些数字是计算复杂度的证据，不是模型空间正确性的证据。模型空间、惰性核芯、
SPE、TBME、有效算符和截断必须单独记录。

### Lanczos and block Lanczos

Lanczos 方法在 Krylov 子空间

\[
\mathcal K_n(H,v_0)
=\operatorname{span}\{v_0,Hv_0,H^2v_0,\ldots,H^{n-1}v_0\}
\]

中求 Ritz 值。低能本征值通常比高能态更早收敛；文章给出的经验是约
\(n\simeq300\) 次迭代可以获得十个低能本征值，但这个数不是普适误差界。

KSHELL 的 thick-restart block Lanczos 用一组初始向量
\(V_0=(v_{0,1},\ldots,v_{0,q})\) 构造块 Krylov 子空间，降低每次重新生成
on-the-fly 哈密顿量矩阵元的成本。它改善的是计算效率和目标态覆盖，不会自动
消除模型空间截断、近简并、内部本征值或复杂共振的困难。

### MCSM

MCSM 波函数写成带宇称和角动量投影的形变 Slater 行列式叠加：

\[
|\Psi^{(N_b)}\rangle
=\sum_{n=1}^{N_b}\sum_{K=-J}^{J}
f_{nK}P^J_{MK}|\phi_n\rangle .
\]

每个 \(|\phi_n\rangle\) 由复矩阵 \(D^{(n)}_{k\alpha}\) 参数化。系数由哈密顿量
矩阵与范数矩阵的广义本征值问题确定；形变基底通过辅助场候选、能量选择和
共轭梯度优化逐步加入。

MCSM 的一个关键收敛指标是能量方差

\[
\Delta E
=\langle H^2\rangle-\langle H\rangle^2.
\]

精确本征态满足 \(\Delta E=0\)。在有限 \(N_b\) 下，可把能量对
\(\Delta E\) 的关系拟合并外推到零方差；这是一种数值外推，不是实验统计置信区间。

### QVSM

QVSM 用粒子数投影的准粒子真空替代 Slater 行列式：

\[
 \vert \Psi^{(N_b)}\rangle
=\sum_{n=1}^{N_b}\sum_{K=-J}^{J}
f_{nK}P^J_{MK}P_ZP_N \vert \phi_n \rangle ,
\]

并以

\[
\beta_k \vert \phi_n \rangle=0
\]

定义准粒子真空。\(U,V\) 变换矩阵满足正交化条件；本文实现不混合质子和中子空间。
粒子数投影提高了配对相关性的表达能力，但代价是额外投影和更高计算时间。

## What It Can Establish

### 1. 传统壳模型的数值边界可以量化

完整对角化能给出模型空间内的基准低能本征值和本征矢，但维数随质量区、
开放壳层和跨壳层激发迅速增长。\(^{130}\mathrm{Sm}\) 与 \(^{172}\mathrm{Dy}\)
的表中维数说明，A≈130 以后完整 M-scheme 对角化通常不是默认可行路径。
这为 MCSM、QVSM、重要性截断和外推方法提供了明确的计算动机。

### 2. MCSM 能在中等质量区保持高精度

在 \(^{56}\mathrm{Ni}\)、FPD6、pf 壳 benchmark 中：

- \(N_b=150\) 时 MCSM 变分能量约为 \(-203.192\) MeV；
- 完整对角化值约为 \(-203.198\) MeV，差异约 \(6\) keV；
- 用能量方差二阶多项式外推后，结果与精确值达到 keV 级一致；
- MCSM 与精确基态波函数重叠在 \(N_b=7\) 时已超过 \(0.99\)，
  \(N_b=150\) 时约为 \(0.9998\)。

这说明 MCSM 的形变投影基底可以高效捕捉某些强关联低能态；它同时不代表
所有激发态、跃迁算符或其它相互作用都以相同速度收敛。

### 3. MCSM 的形变基底可连接形状共存，但不是实验形状测量

MCSM 的投影形变 Slater 行列式适合表达球形、轴对称、三轴和形状共存候选，
也能通过 T-plot 或基底权重帮助解释本征态的内禀结构。但内禀基底坐标是
模型表示，不是直接实验观测量。要把它用于三轴课题，仍需联合
\(B(E2)\)、四极矩、寿命、相对 E2 矩阵元和谱学布居。

### 4. QVSM 对重核配对和 \(\gamma\) 带具有明显优势

在 \(^{132}\mathrm{Ba}\)、SN100PN、jj55 模型空间 benchmark 中，文章比较了
轴对称/非轴对称 GCM、MCSM、QVSM 和完整 Lanczos：

- 只用 Slater 行列式的 GCM 会低估配对，导致 yrast 带激发能偏低；
- 轴对称 GCM 无法合理再现 quasi-\(\gamma\) 带；
- 非轴对称 HFB+GCM、MCSM 和 QVSM 可改善谱形；
- QVSM 与精确壳模型的能量偏差约 \(45\) keV，是该比较中最接近精确值的结果；
- QVSM 代价高于相同 \(N_b\) 的 MCSM，因为需要质子数和中子数投影。

因此，若研究 A≈130 开放壳层、配对明显且需要同时描述 yrast 与
\(\gamma\)-like 结构，QVSM 是重要的计算候选；但“再现 \(\gamma\) 带能量”
仍不是刚性三轴形变或 wobbling 的充分判据。

### 5. MCSM 与 QVSM 的选择应由小规模 pilot 决定

文章建议先用较小 \(N_b\) 同时运行 MCSM/QVSM，比较相同计算预算下的能量偏差、
方差下降、带结构和配对敏感性，再决定重计算路线。经验上，锡区以后的重核
配对更重要时 QVSM 往往更有优势；在 \(^{68}\mathrm{Ni}\) 等配对差异较小的区域，
MCSM 可能具有更好的时间效率。

### 6. \(^{101}\mathrm{Sn}\) benchmark 显示不同近似可收敛到相同结构排序

在 \(^{101}\mathrm{Sn}\) 的 \(0g_{9/2},0g_{7/2},1d_{5/2},1d_{3/2},2s_{1/2}\)
模型空间和 VS-IMSRG 有效相互作用下，ITSM、跨 \(N=Z=50\) 壳隙的
粒子–空穴截断 Lanczos 以及 QVSM 方差外推都预测：

- \(7/2^+\) 为基态；
- \(5/2^+\) 为低激发态；
- 二者间隔较小。

但 \(t=6\) 的粒子–空穴 Lanczos 维数已达 \(9.6\times10^9\)，仍未完全收敛；
QVSM 的结论来自零方差外推，ITSM 也包含重要性截断外推。因此“方法间一致”
是鲁棒性证据，却不是无模型误差的精确预测。

## Experimental and research-analysis contract

将这些计算用于束内 \(\gamma\) 谱学或三轴集体模式研究时，应分别报告：

1. 模型空间、惰性核芯、SPE/TBME、有效电荷和有效跃迁算符；
2. \(N_b\)、能量方差、基态/激发态重叠、带能量和矩阵元的收敛曲线；
3. 对 MCSM/QVSM/GCM/Lanczos 的方法差异，区分数值截断误差与物理模型差异；
4. 对 \(\gamma\)-band、wobbling 或 chiral candidate，加入
   \(B(E2)\)、\(B(M1)\)、四极矩、混合比、寿命和 feeding 的联合比较；
5. 不把方差外推的零点、能量差或一条准 \(\gamma\) 带直接转换为实验模式确认；
6. 对 \(^{100}\mathrm{Sn}\) 邻域或 A≈130 迁移，重新核验模型空间是否覆盖
   \(g_{9/2}\)、\(h_{11/2}\)、跨壳层激发和配对相关性。

## What It Cannot Establish Alone

- MCSM/QVSM 的能量收敛不能单独证明实验核素具有刚性三轴形变；
- \(\gamma\)-like 带的能级再现不能单独确认 wobbling、TiP、chirality 或
  \(\gamma\)-rigid 而非 \(\gamma\)-soft；
- 能量方差外推不是统计误差、置信区间或实验系统误差；
- 计算方法之间的一致不能替代不同有效相互作用、模型空间和有效算符的敏感性分析；
- \(^{101}\mathrm{Sn}\) 的 \(7/2^+\)–\(5/2^+\) 排序不能直接外推 A≈130 高自旋组态；
- 计算得到的内禀形变、T-plot 权重和准粒子构型不是直接实验观测量；
- Lanczos、MCSM 或 QVSM 的数值精度不能消除连续谱、三体力、反应布居和探测器
  响应带来的实验解释不确定度。

## Knowledge Impact and Learning Decision

该文章为已有壳演化和实验谱学知识增加了“算法适用域”层：在 A≈130 研究中，
不能只问哪个模型能给出相似的能级，还必须问模型空间是否容纳配对、三轴基底、
跨壳层激发和有效算符，以及数值结果是否随 \(N_b\)、方差和截断稳定。
它也为今后的 Python 工具提供了收敛审计接口：能量—方差曲线、多个方法的
差分、模型空间表和观测量联合残差应作为独立输出。

本单元完成 Shimizu 文章主文本与关键 benchmark 图表的有界核读；参考文献、
实际 KSHELL/MCSM/QVSM 源码和生产级输入文件未独立重读。

## Evidence and locators

- Article pp.161–163 / physical PDF pp.172–174：CI 壳模型、M/J-scheme 维数、
  表 1、Hamiltonian 和 Lanczos 基础；
- Article pp.163–165 / physical PDF pp.174–176：Lanczos、block Lanczos 和近似方法总览；
- Article pp.165–167 / physical PDF pp.176–178：MCSM 方程 (7)–(9)、\(^{56}\mathrm{Ni}\)
  图 1–2、能量方差和波函数重叠；
- Article pp.167–169 / physical PDF pp.178–180：QVSM 方程 (10)–(11)、
  \(^{132}\mathrm{Ba}\) 图 3、配对与 quasi-\(\gamma\) 带；
- Article pp.169–170 / physical PDF pp.180–181：\(^{101}\mathrm{Sn}\) 图 4、
  ITSM/Lanczos/QVSM 对照和 \(t=6\) 维数；
- Article pp.170–173 / physical PDF pp.181–184：总结、巨共振/统计性质的开放问题
  与参考文献边界。

## Sources

- [[book-nuclear-shell-model-70-years]]
- [[utsuno-shell-evolution-force-decomposition-contract]]
- [[otsuka-shell-evolution-monopole-contract]]
- [[sn100-region-highspin-spectroscopy-contract]]
- [[nuclear-spectroscopy-and-structure-master-field-manual]]
- [[triaxial-collective-modes-unified-theory-and-spectroscopy]]
