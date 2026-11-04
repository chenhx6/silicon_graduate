---
type: method
title: "Utsuno：中心力、二体自旋–轨道力与张量力驱动的壳演化合同"
aliases: [Utsuno shell evolution, SDPF-MU force decomposition, monopole ESPE contract]
method_type: "shell-evolution-force-decomposition-and-experimental-test"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Nuclear Shell Model 70 Years article 8, full main-text reading"
confidence: "high for article equations and reported comparisons; conditional for model attribution"
tags: [shell-model, shell-evolution, monopole-interaction, espe, tensor-force, spin-orbit, spectroscopic-factor, magic-numbers]
sources: [book-nuclear-shell-model-70-years]
---

# Utsuno：中心力、二体自旋–轨道力与张量力驱动的壳演化合同

## Purpose

这篇文章把“壳隙随质子数或中子数变化”拆成可检验的单极相互作用问题。核心链条是

\[
\text{two-body monopole matrix elements}
\longrightarrow
\text{effective single-particle energies (ESPE)}
\longrightarrow
\text{shell-gap evolution}
\longrightarrow
\text{single-particle-like levels and spectroscopic distributions}.
\]

它的价值在于把中心力、张量力和二体自旋–轨道力放在同一套
SDPF-MU 有效相互作用中逐项比较，并用核素链上的能级、核子去除谱因子和
单粒子强度分布检验这种分解。文章研究的是 \(25\lesssim A\lesssim55\) 的富中子核，
因此它提供的是壳演化微观机制合同，不能直接当作 A≈130 三轴集体运动的实验结论。

## Inputs and Assumptions

### Monopole matrix element

对轨道 \(j_1,j_2\)，文章定义固定同位旋道的单极矩阵元

\[
V^T_m(j_1,j_2)=
\frac{\sum_J(2J+1)
\langle j_1j_2;JT \vert V \vert j_1j_2;JT \rangle}
{\sum_J(2J+1)}.
\]

质子–中子通道在轨道不同的情形下用 \(T=0\) 与 \(T=1\) 的平均：

\[
V^{m}_{pn}(j_1,j_2)
=\frac12\left[V^{m}_{T=0}(j_1,j_2)+V^{m}_{T=1}(j_1,j_2)\right].
\]

SDPF-MU 的跨壳层部分由密度依赖中心力、M3Y 型二体自旋–轨道力和
\(\pi+\rho\) 介子交换型张量力构成；整体强度还带有 \(A^{-0.3}\) 标度。
这是一种有效相互作用分解，不能把三个分量直接等同为实验上可分离的力。

### Qualitative pair labels

为快速判断中心力和张量力的相对趋势，文章给轨道对使用两个字符的标签：

- 第一字符描述中心力：\(-\) 表示 \(\Delta n=0\) 的强空间重叠和较强吸引，
  \(+\) 表示 \(\Delta n\ne0\) 的相对弱吸引；
- 第二字符描述张量力与相对自旋方向：自旋平行与反平行决定符号和相对吸引性；
- \(\{--\},\{-+\},\{+(-)\},\{+(+)\}\) 等标签只是排序和预估工具，不能替代
  具体矩阵元数值。

表 1 给出的 \(A=42\) 代表性结果显示：中心力的绝对值通常约为 \(-1.1\) MeV
或较弱一档；张量力的绝对值较小，但同一轨道集合内最大和最小值的差异可达约
\(0.5\) MeV，因此其对壳隙演化的差分作用可以和中心力同量级。二体自旋–轨道
单极元通常更小，但 \(s\)-\(p\) 轨道对因相对轨道角动量 \(L_{\rm rel}=1\) 可有
异常显著的贡献。

### ESPE and shell-gap evolution

在质量无关的两体相互作用近似下，填满质子轨道 \(j_p\) 后，中子轨道 \(j_n\) 的
ESPE 变化为

\[
\Delta_{\pi j_p}\epsilon_{\nu j_n}
=(2j_p+1)V^m_{pn}(j_n,j_p).
\]

因此两个中子轨道之间的壳隙变化为

\[
\Delta_{\pi j_p}
(\epsilon_{\nu j_n}-\epsilon_{\nu j'_n})
=(2j_p+1)
\left[
V^m_{pn}(j_n,j_p)-V^m_{pn}(j'_n,j_p)
\right].
\]

文章强调，这个差分量在两体相互作用近似下不依赖于选择哪个惰性核芯来定义
ESPE，因此可以用较容易测量的较稳定同位素链，间接约束更富中子的壳演化。
对质量依赖的相互作用，上式不再严格，但仍可作为诊断和实验设计的近似坐标。

## What It Can Establish

### 1. 张量力主导 Ca 链质子 \(d\) 轨道自旋–轨道分裂变化

填充中子 \(f_{7/2}\) 时，质子 \(d_{3/2}\) 与 \(d_{5/2}\) 的单极差分主要由
张量力放大。SDPF-MU 计算的质子 \(d\) 轨道自旋–轨道分裂从
\(^{40}\mathrm{Ca}\) 核芯的约 \(7.42\) MeV 降到 \(^{48}\mathrm{Ca}\) 核芯的
约 \(5.05\) MeV，变化超过 \(2\) MeV。单质子去除反应的谱因子分布不仅比较
质心，还比较各主要峰的位置和碎裂模式：\(^{48}\mathrm{Ca}(d,{}^3\mathrm{He})\)
和 \(^{40}\mathrm{Ca}(d,{}^3\mathrm{He})\) 的 \(s_{1/2},d_{3/2},d_{5/2}\)
强度分布与相应计算的主要峰结构相符。

这里的证据强度来自“力分量去除后的计算对照 + 多个主要谱因子峰”的联合比较。
它不是从单一能级直接测出张量力。

### 2. K 链的非单调反转是两体有效相互作用的指纹

在中子数 \(N=20\to28\) 时，质子 \(d_{3/2}\)-\(s_{1/2}\) 间隔快速减小；
填充 \(p_{3/2}\) 后，中心力差分改变符号，使该间隔在 \(N=28\) 后重新增大。
实验上 \(^{39,47}\mathrm{K}\) 的 \(1/2^+-3/2^+\) 能级差从约 \(2.52\) MeV
变为 \(-0.36\) MeV，文章把这种“下降后上升”的形状解释为
\(\pi s_{1/2}\) 与 \(\pi d_{3/2}\) 的重新反转。

这一结论的关键不是“能级有斜率”，而是同一轨道间隔沿核素链出现非单调行为，
并且其拐点方向与不同填充轨道的单极差分一致。文章指出，简单一体势模型通常给出
单调变化；不过非单调形状本身仍是有效相互作用模型的强支持，而不是对某个裸核力
分量的唯一实验分离。

### 3. 模型修正暴露了中心力单极项的不确定度

SDPF-MU 对 \(^{51,53}\mathrm{K}\) 的第一激发 \(1/2^+\) 能量给出约
\(1.40\) 和 \(1.74\) MeV，而实验值约为 \(0.74\) 和 \(0.84\) MeV。
仅调整 \(s\)-\(p\) 的 \(T=0\) 单极项得到 SDPF-MUs 后，计算改善到约
\(0.85\) 和 \(0.79\) MeV。文章把这解释为中心力经验构造中的约
\(0.2\) MeV 级修正需求；张量项保持不变，避免把不同物理来源混在一起。

因此，对实验数据的良好拟合必须同时记录“原始相互作用”和“调整后的相互作用”；
调参后的结果不能直接作为独立机制证据。

### 4. N=28 壳隙随 Z 的演化与形变/组态混合相互耦合

从 \(Z=20\) 去除 \(d_{3/2}\) 质子时，\(N=28\) 壳隙明显减小。以 \(N=20\)
同位素作为较可控的代理，\(^{36}\mathrm{S}\) 的实验单粒子强度显示
\(f_{7/2}\) 与 \(p_{3/2}\) 强度相隔小于约 \(1\) MeV，SDPF-MU 计算的壳隙约
\(0.32\) MeV；对 \(^{40}\mathrm{Ca}\)，实验谱因子质心给出的尺度约 \(2.5\) MeV，
计算约 \(2.94\) MeV。N=28 闭壳破缺的一个观测接口是低能
\(\nu p_{3/2}\) 去除强度，但必须警惕未观测激发态、形变和强度碎裂。

在 \(^{44}\mathrm{S}\) 附近，\(\Omega^\pi=7/2^-\) 与 \(3/2^-\) 的近简并会使
基态组态混合；因此第一 \(3/2^-\) 态的 \(C^2S\) 只占总
\(\nu p_{3/2}\) 占据的一部分，不能把单个低能峰当作总占据。

### 5. N=34 与 N=32 的两个不同机制入口

对 \(N=34\)，文章用 \(^{52}\mathrm{Ar}\) 的
\(E(2^+_1)=1.656(18)\) MeV 作为壳闭合增强的实验入口，并用
\(d_{3/2}\)-\(p_{1/2}\) 与 \(d_{3/2}\)-\(f_{5/2}\) 的单极差分解释
从 \(Z=20\) 向更低 Z 时壳隙增强的趋势。

对 \(N=32\)，\(^{34}\mathrm{Si}(d,p)\) 反应的 \(l=1\) 峰给出约
\(0.910\) 和 \(2.044\) MeV 的 \(3/2^-\)、\(1/2^-\) 候选间隔；从
\(^{37}\mathrm{S}\) 到 \(^{35}\mathrm{Si}\) 的实验变化约为 \(0.857\) MeV，
ESPE 估计约 \(0.54\) MeV，完整壳模型能级差变化约 \(0.758\) MeV。
在 SDPF-MU 中，\(s_{1/2}\)-\(p\) 的中心力差分几乎相同且张量力不贡献，
因此二体自旋–轨道项成为主要壳隙变化来源，剩余百 keV 量级可由多体关联贡献。

文章同时保留 Woods–Saxon 弱束缚解释：一体势也能产生自旋–轨道分裂随 Z
逐渐减小的趋势；区分两种解释需要比较 \(^{40}\mathrm{Ca}\to{}^{36}\mathrm{S}\)
与 \(^{36}\mathrm{S}\to{}^{34}\mathrm{Si}\) 的变化陡峭程度，而现有谱因子精度尚
未完全解决这一竞争。

### 6. N=28 向氧、氖、镁、硅方向的收缩

从 \(Z=14\to8\) 去除 \(d_{5/2}\) 质子时，中心力差分使 \(N=28\) 壳隙再次显著减小。
\(^{27}\mathrm{Ne}\)、\(^{29}\mathrm{Mg}\)、\(^{31}\mathrm{Si}\) 的
\(3/2^- - 7/2^-\) 能级差近似线性变化，但相关单中子添加谱因子通常只有约
\(0.5\)，因此这些能级差不能直接当成完整 N=28 壳隙。它们更适合被视为
“单粒子样能级随 Z 的趋势”。

文章的一个重要细节是：实际本征态含有显著的中子激发到 \(d_{3/2}\)，
\(d_{3/2}\)-\(f_{7/2}\) 与 \(d_{3/2}\)-\(p_{3/2}\) 的 \(T=1\) 单极差异会
把观测能级差相对 ESPE 平移。因此，把实验能级差与 ESPE 一一相等是错误的；
应比较斜率、碎裂、占据和关联修正。

## Experimental analysis contract

对于将壳演化结论用于实验分析，推荐按以下顺序组织证据：

1. 先定义目标壳隙和参考轨道，明确是 ESPE 差、能级差、谱因子质心还是
   \(E(2^+_1)\)；
2. 把单极矩阵元按中心、张量、二体 \(LS\) 和总值分开列出；
3. 对核子去除/添加数据报告反应模型、归一化、未观测强度和
   \(\sum C^2S\) 是否接近求和规则；
4. 优先比较完整谱因子分布和主要峰，而不是只比较一个质心；
5. 对低能 \(0^+\)、\(2^+\) 和强烈变形核，先检查组态混合、形变和
   多粒子–多空穴激发，再把能量变化映射到壳隙；
6. 至少保留一个竞争解释：弱束缚一体势、关联能、模型空间截断或经验调参；
7. 若将该机制迁移到 A≈130，必须重新确定价空间、有效相互作用、形变与
   高自旋占据，不能直接外推 SDPF-MU 的数值。

## What It Cannot Establish Alone

- ESPE 是模型依赖的诊断量，不是直接测量的单粒子能级；
- 单个 \(E(2^+_1)\)、单个 \(C^2S\) 或一条能级斜率不能独立分离中心力、
  张量力和二体自旋–轨道力；
- 质心受未观测弱强度和反应模型影响，不能把实验有限窗口内的质心当作精确总和；
- 拟合到 SDPF-MUs 的改良不能被当作独立实验验证，因为单极项已经被调整；
- 文章中的 \(A\approx25\)–55 机制不能直接证明 A≈130 的三轴刚性、
  \(\gamma\)-soft 性、wobbling、手征双带或 TiP；
- 壳演化机制需要与 \(B(E2)\)、四极矩、寿命、转移/敲除反应、质量和分离能
 共同约束；不同观测量对同一模型参数的敏感性并不相同。

## Knowledge Impact and Learning Decision

这篇文章把已有 Otsuka 单极/张量力框架补成了“力分量—ESPE—谱因子分布”的实验接口，
并为 A≈100/A≈130 的后续研究提供一个必须保留的反向检验：高自旋或形变增强不应
被直接解释为集体模型胜出，先检查占据改变是否重排单极场。它还把“中心力经验调参”
和“张量力机制支持”明确分开，避免用调整后的能级拟合过度宣称微观来源。

本单元授予 Utsuno 文章主文本阅读和关键图表核验的有界学分；合集其余文章以及
Utsuno 参考文献的独立回查仍不计入本单元。

## Evidence and locators

- Article pp.193–195 / physical PDF pp.204–206：研究范围、\(V_m^T\)、SDPF-MU
  中心/张量/二体 \(LS\) 力和表 1；
- Article pp.196–198 / physical PDF pp.207–209：ESPE、式 (5)–(7)、图 1–2、
  模型空间与 KSHELL；
- Article pp.198–201 / physical PDF pp.209–212：Ca/K 链、谱因子定义式 (8)、
  图 3–4 及张量力/中心力解释；
- Article pp.201–204 / physical PDF pp.212–215：N=28、N=32、N=34、
  \(^{52}\mathrm{Ar}\)、\(^{34}\mathrm{Si}\) 和弱束缚竞争解释；
- Article pp.204–207 / physical PDF pp.215–218：Z=14–8、图 6 和结论。

## Sources

- [[book-nuclear-shell-model-70-years]]
- [[otsuka-shell-evolution-monopole-contract]]
- [[n40-island-nucleon-removal-shell-model-contract]]
- [[low-energy-coulomb-excitation-shell-model-contract]]
- [[sn100-region-highspin-spectroscopy-contract]]
- [[nuclear-shape-coexistence-and-e0-transitions]]
