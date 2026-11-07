---
type: source
title: "Karmakar et al. 2024：100Ru高自旋增强电偶极跃迁强度与DSAM能级寿命测量（PRC Letter）"
aliases: ["Karmakar 2024 PRC Letter 100Ru lifetimes", "arXiv:2411.10976", "PRC 110 L051302"]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: read
title_original: "Measurement of enhanced electric dipole transition strengths at high spin in 100Ru: Possible observation of octupole deformation"
authors: ["A. Karmakar", "Nazira Nazir", "P. Datta", "J. A. Sheikh", "S. Jehangir", "G. H. Bhat", "S. S. Nayak", "Soumik Bhattacharya", "Suchorita Paul", "Snigdha Pal", "S. Bhattacharyya", "G. Mukherjee", "S. Basu", "S. Chakraborty", "S. Panwar", "Pankaj K. Giri", "R. Raut", "S. S. Ghugre", "R. Palit", "Sajad Ali", "W. Shaikh", "S. Chattopadhyay"]
journal: Physical Review C
year: 2024
volume: 110
pages: L051302
doi: 10.1103/PhysRevC.110.L051302
arxiv: "2411.10976"
canonical_source: "https://doi.org/10.1103/PhysRevC.110.L051302"
citation_key: ""
raw_file: raw/papers/gpt/query/20261107-a100-octupole-lifetimes/arxiv-2411.10976v1.pdf
raw_sha256: 3370f77e28fa053f1ab2829588602a4fe9d6cb1ea5ccdf6350d82bd52624e8d5
raw_storage_status: fully-archived-local
archive_required: true
nuclei: ["100ru"]
tags: ["dsam-lifetimes", "octupole-collectivity", "enhanced-e1", "a100", "tpsm"]
---

# 100Ru高自旋DSAM寿命测量：绝对B(E1)增强、TPSM微扰偏差与八极形变假说

## Bibliographic Record

A. Karmakar et al., *Measurement of enhanced electric dipole transition strengths at high spin in $^{100}$Ru: Possible observation of octupole deformation*, Physical Review C **110**, L051302 (published 2024-11-25), DOI: 10.1103/PhysRevC.110.L051302。
底本为合法获取的官方预印本全文及其完整源码：
1. PDF全文：`raw/papers/gpt/query/20261107-a100-octupole-lifetimes/arxiv-2411.10976v1.pdf` (SHA-256: `3370f77e28fa053f1ab2829588602a4fe9d6cb1ea5ccdf6350d82bd52624e8d5`，共 6 页)；
2. LaTeX源码：`raw/papers/gpt/query/20261107-a100-octupole-lifetimes/arxiv-2411.10976v1.src.tar.gz` (解包源文件 `000_resubmit_nov8.tex`，335 源码行)。

## Scope and Reading Depth

对官方预印本 PDF 全文共 6 页（PDF pp. 1–6，包括 p.1 引言与厚靶实验装置、p.2 线形拟合与 Table I 寿命表、p.3/p.4 偶极矩与 TPSM 模型参数、p.5 $B(E1)$ 比较与总结讨论、p.6 参考文献）以及配套 LaTeX 源码 `000_resubmit_nov8.tex` 进行了全量逐行深度阅读。重点核查：
1. DSAM 实验分析条件：$45\text{ MeV}$ $\alpha + {}^{100}\text{Mo}$ 厚靶（$10\text{ mg/cm}^2$ 自减速箔）、SRIM 阻止截面模型（步长 $0.001\text{ ps}$，10000 轨迹，约 4% 未停止轨迹）、5 步级联侧向馈送唯象模型、顶门交叉验证；
2. 角度设置张力：记录正文中的 $40^\circ, 90^\circ, 125^\circ$ 与 Fig. 1 图注中 $40^\circ, 90^\circ, 157^\circ$ 的原文文本不一致；
3. Table I 数值与 7 条 E1 对应关系：确认仅有 6 个能级（$14^+, 16^+, 18^+$ 与 $13^-, 15^-, 17^-$）测出有限寿命与数值绝对 $B(E1)$，高自旋端 $20^+$ 与 $19^-$ 仅给出有效寿命上限故 $B(E1)$ 缺测，低自旋端 $12^+ \to 11^-$ 未测寿命；记录作者摘要/总结声称“seven rates”与 Table I 实际仅给 6 个数值的张力；
4. 偶极矩演化：$D_0$ 在 $I \le 16\hbar$ 时为 $0.04(1)\text{ }e\text{fm}$，在 $I > 16\hbar$ 时为 $0.07(2)\text{ }e\text{fm}$，保留完整误差并指出增大趋势，不作过强统计跳变断言；
5. TPSM 微观模型设置：$\epsilon=0.24, \epsilon\x27=0.14$，基底与有效电荷，不含八极项（TPSM1）比实验低一个数量级，含八极微扰（TPSM2）仍偏低，平均场保持空间反射对称性（宇称好量子数）；
6. 证据边界与实验依赖：明确高自旋未测直接 $B(E3)$ 与静态 $\beta_3$；区分本篇厚靶实验与前篇（PRC 109, 054312）薄靶实验的不同采集与分支比输入依赖。

## Key Results

| ID | 实际可核验内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KM24-L1 | 实验在 VECC K-130 利用 $45\text{ MeV}$ $\alpha + {}^{100}\text{Mo}$ 厚靶（$10\text{ mg/cm}^2$ 自支撑箔）反应，使用 INGA 阵列 11 台 Clover 探测器采集 $4 \times 10^9$ $\gamma$-$\gamma$ 符合，通过 LINESHAPE 与 SRIM 阻止截面模型（10000 轨迹，步长 $0.001\text{ ps}$）分析多普勒展宽线形。 | experimental-setup | direct | PDF p.1-2, 源码行 95-96 | false |
| KM24-L2 | 正文与装置描述明确探测器角度为 $40^\circ, 90^\circ, 125^\circ$ 且三角度联合拟合，但 Fig. 1 图注写为 $40^\circ, 90^\circ, 157^\circ$；在缺乏原始探测器排布日志前保留此原文张力。 | text-tension | direct | PDF p.2 Fig. 1 图注 vs PDF p.1-2 源码行 95, 101, 105 | false |
| KM24-L3 | 侧向馈送建模为 5 步连续跃迁级联，有效时间由四极矩拟合确定；顶门验证提取 $14^+$ 寿命为 $1.07(5)\text{ ps}$、$13^-$ 寿命为 $0.44(3)\text{ ps}$，与全带拟合结果（$1.02(9)$ 与 $0.40(3)\text{ ps}$）在 $\pm 1\sigma$ 内符合。 | experiment-method | direct | PDF p.2, 源码行 95, 107 | false |
| KM24-L4 | 测得 Band 2 正宇称寿命：$14^+$ 为 $1.02(9)\text{ ps}$、$16^+$ 为 $0.32(3)\text{ ps}$、$18^+$ 为 $0.17(1)\text{ ps}$；$20^+$ 仅测得有效寿命上限 $\tau < 0.14^u\text{ ps}$。 | experimental-data | direct | PDF p.2 Table I, 源码行 121–126 | false |
| KM24-L5 | 测得 Band 3 负宇称寿命：$13^-$ 为 $0.40(3)\text{ ps}$、$15^-$ 为 $0.31(2)\text{ ps}$、$17^-$ 为 $0.29(2)\text{ ps}$；$19^-$ 仅测得有效寿命上限 $\tau < 0.12^u\text{ ps}$。 | experimental-data | direct | PDF p.2 Table I, 源码行 128–133 | false |
| KM24-L6 | 绝对 $B(E1)$ 仅测出 6 条有限数值，非 7 条全出：$14^+ \to 13^-$ ($1.4(4) \times 10^{-4}$)、$16^+ \to 15^-$ ($2.4(6) \times 10^{-4}$)、$18^+ \to 17^-$ ($7.7(25) \times 10^{-4}$)、$13^- \to 12^+$ ($2.0(4) \times 10^{-4}$)、$15^- \to 14^+$ ($2.7(6) \times 10^{-4}$)、$17^- \to 16^+$ ($4.4(15) \times 10^{-4}\text{ }e^2\text{fm}^2$)；$20^+$ 与 $19^-$ 因仅有寿命上限故 $B(E1)$ 标为破折号 `-`；$12^+ \to 11^-$ 未测寿命。作者在摘要与总结中宣称“seven interleaved transitions with enhanced rates”与 Table I 的 6 个有限数值存在明确张力。 | experimental-data | direct | PDF p.2 Table I, 源码行 123–133; PDF p.1, 5 源码行 86, 209 | false |
| KM24-L7 | 两带平均四极矩提取为 $Q_0 = 264(8)\text{ }e\text{fm}^2$。内禀偶极矩分段表现为：$I \le 16\hbar$ 时为 $D_0 = 0.04(1)\text{ }e\text{fm}$；$I > 16\hbar$ 时为 $D_0 = 0.07(2)\text{ }e\text{fm}$（若段间误差独立且近高斯，差值约 $1.34\sigma$，呈现增大趋势），伴随两带宇称劈裂闭合。 | experimental-derived | direct | PDF p.2-3, 源码行 156 | false |
| KM24-L8 | TPSM 理论使用 $\epsilon=0.24, \epsilon\x27=0.14$，$\Delta_n=1.08\text{ MeV}, \Delta_p=1.03\text{ MeV}$（负宇称带降低对力 $\Delta_n=0.72\text{ MeV}, \Delta_p=0.85\text{ MeV}$），标准有效电荷 $e_p=1.5e, e_n=0.5e$。无八极相互作用的 TPSM1 比实验低一个数量级；含八极微扰的 TPSM2 提高约 2 倍，仍远低于实验值。平均场严格保持空间反射对称性（宇称好量子数）。 | model-result | direct | PDF p.3-5, 源码行 175, 187, 190, 193; Fig. 5 | false |
| KM24-L9 | 实验未测得任何高自旋 $B(E3)$ 跃迁几率，也无静态八极形变 $\beta_3$ 的直接测量；作者基于 TPSM 保持空间反射对称性无法解释增强 $B(E1)$，唯象推测平均场破缺反射对称性形成稳定八极形变，并明确承认需要自洽破反射对称计算来排除平庸双准粒子解释。 | author-interpretation | direct | PDF p.4-5, 源码行 194, 209 | false |

## Summary

本项工作补充了 $^{100}\text{Ru}$ 高自旋交替宇称带的关键能级寿命数据。作者在印度 VECC 利用 INGA Clover 阵列和厚靶（$10\text{ mg/cm}^2$ $^{100}\text{Mo}$）DSAM 技术，测定了交替宇称带中 6 个高自旋能级（$14^+, 16^+, 18^+$ 与 $13^-, 15^-, 17^-$）的有限寿命（$0.17 \sim 1.02\text{ ps}$），提取了绝对 $B(E2)$（$1967 \sim 2672\text{ }e^2\text{fm}^4$）与绝对 $B(E1)$（$(1.4 \sim 7.7) \times 10^{-4}\text{ }e^2\text{fm}^2$）。
高自旋下的绝对 $B(E1)$ 强度相比于邻近单粒子跃迁（如 $^{110}\text{Cd}$ 的 $1.8(4) \times 10^{-6}\text{ }e^2\text{fm}^2$）增强约两个数量级，比保持空间反射对称性的 TPSM 理论计算高出整整一个数量级。
内禀电偶极矩在误差范围内呈现作者指出的数值增大趋势（从 $0.04(1)$ 增大至 $0.07(2)\text{ }e\text{fm}$，若段间误差独立且近高斯，差值约 $1.34\sigma$），且此时伴随两带宇称劈裂闭合。作者据此提出 $^{100}\text{Ru}$ 在高自旋双中子对准构型上可能具有稳定八极形变。

## Competing Interpretations and Limitations

1. **绝对 $B(E1)$ 测量有限**：前作识别出的 7 条交错 E1 跃迁中，最低端的 $12^+ \to 11^-$ 未测寿命，最高端的 $20^+$ 和 $19^-$ 因处于 DSAM 灵敏度极限仅给出了有效寿命上限（$<0.14\text{ ps}$ 与 $<0.12\text{ ps}$），其绝对 $B(E1)$ 缺测；因此仅有 6 条跃迁测出绝对 $B(E1)$ 数值，作者摘要和结论中的“seven rates”与 Table I 的 6 个有限数值存在明显张力；
2. **缺乏直接 $E3$ 或静态 $\beta_3$ 实验证据**：本实验测定的是能级寿命和由分支比推导出的跃迁几率，未测量高自旋库仑激发多极矩阵元或 $B(E3)$；“稳定八极形变”属于作者基于宇称守恒微扰模型不足所作的唯象假说与解释；
3. **微观机制的竞争解释未排除**：增强的 $E1$ 跃迁并不唯一证明静态八极形变，八极软振动声子与转动对准双准粒子的微观组态混合或局部反射不对称极化同样可能增强电偶极跃迁；作者在正文末尾明确指出仍需自洽破反射对称计算以排除平庸的双准粒子解释；
4. **TPSM 理论模型的局限**：计算中采用的 TPSM 平均场严格保持空间反射对称性（宇称守恒），八极相互作用仅作为微扰项处理，无法反映自发破宇称的形变平均场；
5. **重放与拟合边界**：DSAM 分析依赖 SRIM 阻止截面（声称 5% 误差）和 5 步级联侧向馈送唯象模型，未公开多角度线形拟合的原始多道能谱与完整误差协方差矩阵；正文中的 $40^\circ, 90^\circ, 125^\circ$ 与 Fig. 1 图注中的 $40^\circ, 90^\circ, 157^\circ$ 存在未解张力；
6. **实验采集差异与分支比依赖**：本篇使用的是 $45\text{ MeV}$ $\alpha + {}^{100}\text{Mo}$ **$10\text{ mg/cm}^2$ 厚靶**实验，而前篇（PRC 109, 054312）使用的是 $50\text{ MeV}$ $\alpha + {}^{100}\text{Mo}$ **$2\text{ mg/cm}^2$ 薄靶**实验。本篇能级分支比直接继承自前篇薄靶实验，不可因作者相同而混同为同一次物理采集。

## Knowledge Impact and Learning Decision

1. **补得 6 个关键高自旋寿命数据**：获取了官方 PDF 全文共 6 页及完整 LaTeX 源码，补全了 $^{100}\text{Ru}$ 高自旋 6 个有限寿命与绝对 $B(E1)$ 数据；但原始谱线数据、全协方差矩阵及高自旋 $E3$ 跃迁仍缺失；
2. **澄清事实张力**：纠正了“7条交错E1全部测出绝对B(E1)”的误读（实为 6 条测出绝对值，1 条未测，2 条顶端仅有寿命上限），澄清了 $D_0$ 的误差与条件误差比较（增大若段间误差独立且近高斯，差值约 $1.34\sigma$，未达 $2\sigma$ 显著），并将“已确证静态八极形变”矫正为“测得增强 $B(E1)$，静态八极形变仍为作者待排除竞争解释的理论假说”；
3. **跨质量区演化**：与 $N=56$ 同中子素 $^{96}\text{Zr}$（八极不稳定性）、$^{98}\text{Mo}$（八极自由度）形成对比，阐明了中子 $\nu h_{11/2} - \nu d_{5/2}$ 轨道强八极驱动机制在 A~100 区的表现边界。

## Extracted Pages

阅读了官方 PDF 全文共 6 页（PDF pp. 1–6，包括 p.1 装置描述、p.2 线形与 Table I、p.3/p.4 偶极矩与 TPSM、p.5 $B(E1)$ 与讨论、p.6 参考文献）以及 LaTeX 源文件 `000_resubmit_nov8.tex`（全量 335 源码行与全部参考文献）。

总控边界补充：两段D0的归一化和拟合相关性未完整给出，条件1.34σ不是完整协方差分析。绝对B(E1)可直接给条件D0，不需要Q0；只有从B(E1)/B(E2)间接提取才另需Q0，不能未经核实就将共用Q0指定为本篇的相关误差来源。精确有限核态保持宇称并不禁止相反宇称间的E1；作者关于内禀平均场需破反射对称的判断依赖所用TPSM截断及相互作用，不能从该模型失配逻辑上唯一推出静态β3。

第二轮条件重建见[[ru100-e1-moments-and-covariance-round2-20261107]]：保留六个有限点与两个上限，作者给出的分组矩和本任务的独立边际误差拟合不混用。
