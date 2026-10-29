---
type: research-note
title: "轻锕系同质异能态、内禀八极形变与 K-混合选择定则"
date: 2026-10-29
created: 2026-10-29
updated: 2026-10-29
category: research-notes
aliases: [actinide isomers K mixing octupole selection rules, light actinide octupole isomers]
tags: [isomers, k-mixing, octupole, actinides, hindrance-factor]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: Day26 directed study of actinide isomers, octupole correlations, and K-forbidden electromagnetic decay
promotion_target: ""
evidence_sources: [butler-nazarewicz-1996-intrinsic-reflection-asymmetry, gaffney-2013-pear-shaped-rn-ra, nndc-2009-ra225-adopted-parity-doublet, walker-dracoulis-2001-exotic-isomers]
---

# 轻锕系同质异能态、内禀八极形变与 K-混合选择定则

## Research Trigger

本轮任务要求把轻锕系同质异能态、八极关联、K-禁戒跃迁和电磁速率放进同一个可检验框架，重点检查 $^{225}$Ra、$^{229}$Th、$^{234}$U，并以 $^{178}$Hf 作为传统轴对称 K-trap 对照。首先需要修正三个容易混淆的前提：

1. $^{229}$Th 的超低能异构态是同宇称的 $3/2^+$ 态（当前 NNDC adopted level 为基态 $5/2^+$、$E_x=8.355733554(11)$ eV 的 $3/2^+$ 态），不是正负宇称伙伴；
2. 当前 NNDC $^{234}$U 评价给出 $K^\pi=6^-$ 带头 $E_x=1421.275(45)$ keV、$T_{1/2}=33.5(20)~\mu$s，这是高-$K$ 异构态实例，但它不是 55-keV 量级的宇称双重态；
3. 轴对称 $β_3Y_{30}$ 保持轴向旋转对称性，因而单独不会混合不同 $K$。K-mixing 必须由 Coriolis、三轴/非轴向 $μ\ne0$ 分量、带 K 的八极声子或组态混合提供。

## Grounded Evidence

### 1. 轻锕系实验锚点

| 核素/体系 | 直接或评价事实 | 证据层级与 locator |
|---|---|---|
| $^{225}$Ra | adopted A 带含 $0.0~(1/2^+)$、$25.41~(5/2^+)$、$42.77~(3/2^+)$、$111.60~(7/2^+)$ keV；B 带含 $31.56~(3/2^-)$、$55.16~(1/2^-)$、$69.36~(7/2^-)$、$120.36~(5/2^-)$ keV。$31.50$-keV $3/2^-→1/2^+$ E1 的评价值为 $B(E1)=0.00081(20)$ W.u. | 评价谱学事实；[[nndc-2009-ra225-adopted-parity-doublet]]，ENSDF `225088001` L0.0–120.36 与 E1 B 行。 |
| $^{229}$Th | 现行 NNDC adopted scheme 将 $5/2^+$ 置于 0，$3/2^+$ 异构态在 $8.355733554(11)$ eV；中性原子的内部转换/环境寿命与裸核辐射寿命不同。 | 评价能级/跃迁事实；NNDC NuDat adopted `229Th`（直接能量记录与 `229Th IT decay` 数据入口）。 |
| $^{234}$U | $K^\pi=6^-$ 带头为 $E_x=1421.275(45)$ keV，$T_{1/2}=33.5(20)~\mu$s；评价注释给出构型 $(\nu7/2[743])(\nu5/2[633])$，143.78-keV 跃迁为 $(M1+E2)$，内转换显著。 | 评价事实；NNDC NuDat adopted `234U`，level row `1421.275` 及其 `T_{1/2}`/configuration comment。 |
| $^{178}$Hf | $K=8$、约 4 s 和 $K=16$、约 31 y 的异构态是轴对称 K-trap 的经典例子；高禁戒度和自旋势垒共同延长寿命。 | 综述/历史实例；[[walker-dracoulis-2001-exotic-isomers]]，PDF pp.88–90, Fig.3。 |

### 2. 八极形变和宇称伙伴的实验判据

Butler–Nazarewicz 的综述强调，低位反宇称带、交替宇称转动、E1 与 E3 应作为联合证据；E3 较集体，而 E1 对质子/中子电荷位移相消敏感。其原子核微观图像是费米面附近满足 $\Delta l=\Delta j=3$ 的相反宇称轨道对。综述同时区分静态八极极小、软八极振动、宇称投影和隧穿劈裂，不能从一个非零模型 $\beta_3$ 直接跳到“刚性梨形”。见 [[butler-nazarewicz-1996-intrinsic-reflection-asymmetry]]，Secs. II–VII。

Gaffney 等对 $^{220}$Rn/$^{224}$Ra 的库仑激发表明，$B(E3)$ 增强本身不足以决定静态或动态八极性质；需要把宇称位移随自旋、$Q_3$ 的自旋依赖、E1/E2 和模型敏感性一起检查。$^{224}$Ra 的低宇称位移和较稳定的 $Q_3$ 是静态样证据，仍不是对所有轻锕系核的无条件外推。见 [[gaffney-2013-pear-shaped-rn-ra]]，journal pp.199–204, Tables 1–2, Figs.3–5。

### 3. K-禁戒和阻尼因子

轴对称强耦合极限下，内禀投影 $K$ 是好量子数，多极 $L$ 的带间矩阵元要求

$$|K_i-K_f|\le L.$$

当 $\Delta K>L$ 时，禁戒度定义为 $\nu=\Delta K-L$，常用经验量为

$$f_\nu=\left(\frac{T_{1/2}}{T_{1/2}^{\mathrm{W.u.}}}\right)^{1/\nu}.$$

这里的 W.u. 基线必须说明多极性、$E_\gamma$、内转换和分支；不能把一个评价总寿命直接等同于纯辐射的 K-hindrance。

## Provisional Reasoning

### 1. 八极场如何以及何时进入 K-mixing

内禀场可写成

$$V_{\mathrm{def}}=V_0+\beta_2V_{20}+\beta_3V_{30}+\sum_{\mu\ne0}\beta_{3\mu}V_{3\mu}+V_{\mathrm{Coriolis}}+V_{\mathrm{res}}.$$

轴对称 $V_{30}$ 的磁量子数为 $\mu=0$，所以 $[V_{30},J_3]=0$；它混合相反宇称轨道，但不把 $K=8$ 直接变成 $K=2$。$\beta_{3\mu}$（$\mu\ne0$）或八极声子 $3^-_\mu$ 才能提供 $\Delta K=\mu$ 的非轴向通道。Coriolis 项 $-\hbar^2(I_+j_-+I_-j_+)/2\mathcal J$ 提供 $\Delta K=\pm1$，组态相互作用则可提供更高阶的有效路径。

含混合的态写作

$$|\Psi_{i,f}\rangle=\sum_K C^{(i,f)}_K|IMK\rangle,$$

于是多极矩阵元成为

$$\langle\Psi_f\|\mathcal M(EL)\|\Psi_i\rangle
=\sum_{K_fK_i}C^{(f)*}_{K_f}C^{(i)}_{K_i}
\langle I_fK_f\|\mathcal M(EL)\|I_iK_i\rangle,$$

其中每一项仍满足 $|K_i-K_f|\le L$。所谓 bypass 是高-$K$ 初态先取得允许的低-$K$ 分量，再沿低禁戒度通道衰变；其强度取决于 $C_K$、能级分母、Coriolis/三轴矩阵元和相位相消，而不是只由 $\beta_3$ 决定。

### 2. $B(E1)$、$B(E2)$、$B(M1)$、$B(E3)$ 和寿命

采用约化矩阵元定义

$$B(\Pi L;I_i\to I_f)=\frac{1}{2I_i+1}
\left|\langle I_f\|\mathcal M(\Pi L)\|I_i\rangle\right|^2.$$

在强耦合转子记号中，可用内禀矩 $D_0,Q_0,Q_3$ 和 Clebsch–Gordan 因子写成

$$B(E1)=\frac{3}{4\pi}D_0^2|\langle I_iK\,10|I_fK\rangle|^2,$$

$$B(E2)=\frac{5}{16\pi}Q_0^2|\langle I_iK\,20|I_fK\rangle|^2,$$

$$B(E3)=\frac{7}{16\pi}Q_3^2|\langle I_iK\,30|I_fK\rangle|^2,$$

并以 $g$ 因子模型给出

$$B(M1)=\frac{3}{4\pi}(g_K-g_R)^2K^2|\langle I_iK\,10|I_fK\rangle|^2\mu_N^2.$$

辐射率的实用单位式（$E_\gamma$ 用 MeV）为

$$\lambda(E1)=1.59\times10^{15}E_\gamma^3B(E1),\quad
\lambda(M1)=1.76\times10^{13}E_\gamma^3B(M1),$$

$$\lambda(E2)=1.22\times10^9E_\gamma^5B(E2),\quad
\lambda(E3)=5.70\times10^2E_\gamma^7B(E3),$$

其中 $B(EL)$ 使用 $e^2\mathrm{fm}^{2L}$，$B(M1)$ 使用 $\mu_N^2$。总衰变需加上内转换和其它分支：

$$T_{1/2}=\frac{\ln2}{\sum_x(1+\alpha_x)\lambda_x+\lambda_\mathrm{other}}.$$

因此 $^{225}$Ra 的 31.50-keV E1 评价 $B(E1)$ 可作为直接强度锚点，但在没有完整 ICC 和 feeding 数据时不能仅由它声称总寿命。$^{234}$U 的 143.78-keV $(M1+E2)$ 支线尤其需要保留混合比和内转换；$^{229}$Th 的 eV 级跃迁更不能用 keV 核谱的裸辐射公式直接套用到中性原子寿命。

### 3. 可复现 toy scan 的结果

工件目录为 `outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/actinide-isomers-octupole/`。有限 $K=0,1,\ldots,8$ 基底加入 $\Delta K=1$ 与 $\Delta K=3$ 的有效耦合，扫描 $\beta_3=0\ldots0.20$ 和四个 $\epsilon_K$。当 $\epsilon_K=0$ 时，即使 $\beta_3\ne0$，高-$K$ 到低-$K$ 的 E1/E2/E3 bypass 振幅仍为零；当 $\epsilon_K>0$ 时，$K=2$、$K=0$ 概率随 $\beta_3$ 增长而出现，$f_\nu$ 可下降很多数量级。这个趋势是模型的条件结果，不是对真实核的定量拟合。

## Assumptions

- 使用轴向转子作为零阶基线，$K$ 基底截断到 8；
- 用有效相邻和 $\Delta K=3$ 耦合代表 Coriolis、三轴和八极声子机制，不把它们与静态 $\beta_3$ 混为一项；
- W.u. 采用 $r_0=1.2$ fm 的单粒子尺度；
- toy rate 忽略内转换、未观测分支、feeding 和实验效率；
- $^{225}$Ra 的评价 B(E1) 只用于量级对照，模型输出不重新拟合它；
- 数据源页面未被升级为 `human-reviewed`，本页全部推理保持 provisional。

## Competing Explanations

1. **静态反射不对称**：双势阱和宇称投影可产生低位伙伴，但不必产生强 K-mixing；需要 E3、宇称位移和自旋依赖的联合证据。
2. **软八极振动**：低位负宇称声子和动态波函数可增强 E1/E3，却可能没有冻结的内禀梨形。
3. **组态共存/多准粒子异构**：$^{234}$U 的 $K=6^-$ 异构态可主要由高-$K$ 双准粒子和内转换决定，八极关联不是唯一寿命机制。
4. **Coriolis 或三轴混合**：即使八极关联很弱，非轴向项也可能降低 K-hindrance；反过来，强八极但近轴对称时 K-hindrance 仍可保持。

## Transfer Conditions

本框架可迁移到其它重变形核，前提是有可靠的 $J^\pi,K$、$E_\gamma$、寿命、内转换和分支数据，并能区分静态形变与振动态。$f_\nu$ 的跨核比较必须保持相同多极性、W.u. 半径约定和 ICC 处理。$^{225}$Ra 的宇称伙伴判据可迁移到相邻 Ra/Ac/Th 带，但不能把 $^{229}$Th 的同宇称 eV 异构态当成同一类 parity-doublet 证据。

## Failure Conditions

- 若假设的高-$K$ 初态没有可观测的低-$K$分量，bypass 速率会被高估；
- 若非轴向耦合是强烈的能量依赖或多组态，单一 $\epsilon_K$ 无法描述；
- 若寿命由内转换、粒子发射、$β$ 衰变或多个竞争分支主导，纯 gamma radiation rate 不代表总寿命；
- 若 $K$ 指认仅为括号指认，不能用一个名义 $\Delta K$ 生成高置信 hindrance；
- 若把模型的 2–4 个数量级下降写成实验普遍规律，将超出当前证据。

## Falsification or Reverse Tests

1. 在 $\beta_3\ne0$、$\epsilon_K=0$ 的计算中检验 K 概率和禁戒跃迁是否严格保持零；若不为零，说明实现错误或误把轴向场写成非轴向场。
2. 在相同 $\beta_3$ 下改变 $\epsilon_K$，检查速率变化是否由可追踪的 $C_{K=2}$、$C_{K=0}$ 控制，而不是数值标签跳变。
3. 对 $^{234}$U 的 1421.275-keV 态，把 143.78-keV $(M1+E2)$ 分支、ICC 和 33.5-μs 寿命联合重建；若纯 K=6 计算无法解释，需加入组态混合或未见分支。
4. 对 $^{225}$Ra，使用独立寿命和 ICC 数据检验 31.50-keV E1 的评价 B(E1)；不能用模型输出替代原始转换电子分析。
5. 对 $^{229}$Th，分别计算裸核辐射、Th$^{4+}$ 晶体和中性原子环境，若把 8.3-eV 线错误归为 E1 parity-doublet，应由宇称和 $J$ 直接否证。

## Open Questions

- $^{234}$U $K=6^-$ 异构态的八极声子耦合、Coriolis 混合和多准粒子组态各占多少？
- 在 $^{225}$Ra 的 $K=1/2^\pm$ 带中，E1 强度、Coriolis 解耦和静态八极矩能否由同一粒子-转子参数集同时再现？
- 对 $^{229}$Th，eV 级同宇称 M1/E2 异构跃迁是否存在可观测的八极振动修正，而不改变其主要的四极/单粒子性质？
- 高-$K$ 异构态的 bypass 是否能在完整 EDF+QRPA 或 GCM 中通过可测的 branching ratio 与 polarization 独立识别？

## Human Review

本页由 Codex 根据现有 Wiki source 页、NNDC NuDat 评价入口和 toy model 自审生成，`review_status: unreviewed`。需要人工重点检查：$^{229}$Th/$^{234}$U 的当前评价版本、ICC 与分支的完整来源、所有 W.u. 约定，以及把静态八极、软振动和 K-mixing 分开的表述。

## Promotion or Rejection History

2026-10-29：依据 Day26 研究任务创建。本轮将“$\beta_3\ne0$ 自动强 K-mixing、普遍降低 2–4 个数量级”降级为有条件 toy-model inference；确认 $^{229}$Th eV 异构态为同宇称案例，确认 $^{234}$U 6$^-$、$K=6$、1421.275-keV、33.5-μs 评价锚点。尚未晋升为 synthesis 或正式模型页。
