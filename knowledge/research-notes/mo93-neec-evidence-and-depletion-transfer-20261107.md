---
type: research-note
title: "Mo-93m NEEC controversy, experimental evidence, theoretical mechanisms, and cross-region isomer depletion transfer"
aliases: [Mo93m NEEC evidence and depletion transfer, NEEC controversy synthesis 20261107]
created: 2026-11-07
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
authors: [Research Worker R2]
created_from: project
promotion_target: high-spin-isomers-and-decay-modes-systematics
evidence_sources: [knowledge/sources/walker-2001-180ta-k5-band-intermediate-depletion.md, knowledge/sources/volotka-2016-two-photon-electron-transition-netp.md, knowledge/sources/chiara-2018-mo93m-isomer-depletion-neec.md, knowledge/sources/vanacore-2018-attosecond-coherent-control-free-electrons.md, knowledge/sources/wu-2019-mo93m-neec-stopping-theory.md, knowledge/sources/guo-2021-mo93m-depletion-contamination-challenge.md, knowledge/sources/rzadkiewicz-2021-mo93m-neec-resonant-transfer.md, knowledge/sources/gargiulo-2022-neec-excited-ions.md, knowledge/sources/guo-2022-mo93m-isomer-beam-depletion-limit.md, knowledge/sources/wu-2022-isomer-depletion-vortex-electron-beams.md, knowledge/sources/wang-2023-neec-ebit-feasibility.md, knowledge/sources/li-2026-isomer-depletion-neies.md]
tags: [mo93m, neec, isomer-depletion, 180ta, ebit, vortex-electrons, netp, nuclear-battery, cross-region-transfer]
---

# 93mMo耗散：机制、停靶积分与争议证据的适用域

## Research Trigger

本页比较同核异能态耗散的核/原子通道与实际测量归因。
R3修订旧稿的“唯一证明/普遍排除”及无源实验门槛，加入NEIES理论原作。
检索边界是本地已核原件与本轮身份查询；不作“截至2026年底”的未来声明。

## Grounded Evidence

| 来源 | 实际locator | 证据身份 |
|---|---|---|
| [[chiara-2018-mo93m-isomer-depletion-neec]] | 印刷216–219, Figs.1–3, Methods | 符合计数与作者NEEC归因分开 |
| [[wu-2019-mo93m-neec-stopping-theory]] | PDF2–4, Eqs.(1)–(3), Tables I–II | 停止/电荷/核输入下的理论概率 |
| [[guo-2021-mo93m-depletion-contamination-challenge]] | Matters Arising正文及谱图 | 污染竞争解释，非唯一重建原事件 |
| 原作者2021 Reply | 同争论的答复，见Chiara source回链 | 保留门/谱线身份的异议 |
| [[guo-2022-mo93m-isomer-beam-depletion-limit]] | PDF2–4, Fig.2, Eqs.(1)–(5), Table I | 隔离异能束的本实验上限 |
| [[rzadkiewicz-2021-mo93m-neec-resonant-transfer]]、[[gargiulo-2022-neec-excited-ions]] | 各source对应模型与实际版本 | 原子组态/电子分布的理论修改 |
| [[li-2026-isomer-depletion-neies]] | 实际v1 PDF1–2,4–5 | 连续态电子散射理论，非NEEC确证 |

原2018实验、评论和答复不是三套独立测量。
总控本轮回核新Li原件及其arXiv/Crossref身份；旧原件的阅读范围以各source为准。

## Provisional Reasoning

### 1. 先看电子的初末态，再给过程命名

NEEC是连续态电子被俘获到可用束缚轨道并激发核；
简化共振能量关系 \(E_e+E_b\simeq E_N\)，还须给总原子/核状态和线型。
目标轨道须有允许占据，不必普遍为“内层空穴”。
基态离子某壳填满不排除其激发组态有空穴；宽度也非普适0.1–1eV。
NEET涉及束缚电子跃迁和核激发的能量/矩阵元匹配。
NEIES的初末电子均为连续态，电子损失核激发能，不需俘获到空穴。
直接光吸收又是不同初态；中间gateway的衰变不是激发机制本身的唯一标记。

Li2026是理论研究，DOI为10.1103/slrl-9yfr、PRC113,044329；
撤回G55稿的044607。其一般扫描令各多极B=1W.u.以看趋势，
不能把扫描曲线当所有实核截面，更不能把该文当新的NEEC测量。

### 2. 强度、峰截面、折叠率与净耗散为何不同

单共振可写 \(\sigma_c(E)=S_cL_c(E)\)，
其中 \(\int L_c(E)dE=1\)，L单位能量⁻¹，S单位面积×能量。
若L为FWHM=Γ的Lorentzian，峰值为2S/(πΓ)。
这是声明线型的数学关系；S的角动量/俘获因子依具体截面定义。
电子分布、可用电荷/组态和空穴权重必须再折叠，不能只比较峰值。

在弱激发、给定路径模型中，停止靶的累计激发量为

\[
\chi=\int dx\,n(x)\sum_c f_c(x)\bar\sigma_c[E(x)]
=\int dE\,\frac{n(E)\sum_cf_c(E)\bar\sigma_c(E)}{|dE/dx|}.
\]

χ无量纲；它是光学厚度/hazard型积分，不普遍自动≤1。
单向Poisson激发且无回流的模型给P=1−exp(−χ)，χ≪1时P≈χ。
有多次激发、竞争衰变或电荷态相关演化则需相应率方程。
如截面只到gateway，净向下产额还需bdown及探测接受度；
若σ已定义为depletion截面并含该支路，不能再乘同一个bdown。

比较gateway的γ竞争，除了Eγ^(2L+1)，还要核多极性和B(XL)；
IC/电子环境可能进一步改总分支。只比两个Eγ的五次方不能确定净耗散。

### 3. 三种不同的“没有看到/不能解释”

Chiara2018由其停止靶符合数据提取1.0(3)%并归因为NEEC。
Wu2019在指定电荷/组态与停止模型下给约2.6×10⁻¹¹量级，
这是对该实验归因的强挑战，非另一次低率测量。
Guo2021提出靶内核反应与随机符合等竞争解释；作者Reply持异议，须保留。
不能将其中一方写成已唯一查明全部2018计数的来源。

Guo2022将异能束与产生区隔离，460MeV条件下未见显著268keV峰，
按其统计/效率处理给约2×10⁻⁵上限。
它显著限制该设置中的大耗散率；2018/2022能量、电荷历史与环境不同，
跨设置比较需折叠共同模型，不能无条件排除所有停止条件或所有NEEC。
其上限远高于相应小概率理论计算，也不是对微观NEEC的普遍否定。
“上限与某小理论率相容”不等于已测到了该理论率。

### 4. 什么样的新增观测更有区分力

空间隔离能减少产生区反应污染；电荷/电子组态分辨和能量扫描能限制俘获机制。
核级联及时间谱验证gateway，但同一gateway也可能由其它过程布居。
电子共振位置、线型、俘获后电荷改变与核信号的联合依赖才增加机制信息。
离共振背景可随电子能量、束流条件和仪器响应变化，不能假定恒定。
不使用任意“离峰3个宽度必干净”或一条符合就唯一确证的判据。

对K异能态，寻找中间带可以减小某些分支阻碍，
但不能把一种180Ta路径的ΔK、支路和矩阵元复制到所有核。
EBIT/储存环允许控制部分原子变量，仍须给电子能展、离子数、时序、
碰撞/复合背景及探测效率；“环境更干净”不自动给可观测产额。

## Assumptions

每个数值绑定核能级、电子组态、停止路径、截面定义和统计处理。
激发概率、净depletion概率与检测计数分别归一。

## Competing Explanations

原位核反应、偶然符合、谱线重叠、其它电子/光子激发可能产生相似核级联。
不同文献的原子机制修正也依赖不同输入；不得任意相乘增强因子。

## Transfer Conditions

跨核区先检查gateway、自旋/宇称、多极/矩阵元、回衰变支路、
原子能量/空穴匹配与实验响应。局部截面增大不等于整体热交换或净耗散增大。

## Failure Conditions

把NEIES当NEEC、把峰截面当停靶概率、把上限当零、
重复乘同一支路或把目标低价基态当所有实际电子组态，均会误推。

## Falsification or Reverse Tests

以同一核/原子输入预先预测能量、电荷、级联与时间依赖，
同时拟合控制样本及可变化的背景，再比较竞争机制。
实验灵敏度若未触及预言，只记约束边界，不以零结果宣称过程不存在。

## Open Questions

在具体离子/激发电子组态中哪些共振有可获取且可辨识的计数？
哪些独立电子观测能约束停止过程中的空穴与电荷历史？
本页不声明2026全领域共识或未检索范围内的新颖性。

## Human Review

R3分域研学和总控自审，非人工审核事件。
旧稿“所有11篇已严格核实”不再作为任何具体claim的充分依据。

## Promotion or Rejection History

- 2026-11-07：初稿形成，正文保留在Git历史。
- 2026-11-08：收缩2018/2022跨设置归因，撤回恒定背景及唯一确证线；
  加入hazard/概率条件、空穴与支路定义，并校正Li2026身份及理论范围。
