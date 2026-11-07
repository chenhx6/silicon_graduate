---
type: research-note
title: "A≈100：Zr形状变化的绝对E2与占据反馈"
aliases: [A100 Zr shape and occupancy feedback]
created: 2026-11-08
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [doctoral-r1-g28-togashi-2016-zr-mcsm-qpt, doctoral-r1-g28-singh-2018-98zr-lifetimes, doctoral-r1-g28-otsuka-2023-type-ii-shell-evolution]
created_from: "G28研学；总控原件/题录/拟合输入复核后重建"
promotion_target: ""
tags: [zr, shape-coexistence, mcsm, type-ii-shell-evolution, absolute-e2, doctoral-foundations]
---

# 形变不是核子在固定壳层上的被动排列

## Research Trigger

Zr链在N≈60的集体性变化，为壳占据与集体形变的相互反馈提供了具体案例。
目标是把实测寿命/分支、作者形变解释及微观计算分开，而不是把整个A≈100区命名为O(6)软核。
本页以98Zr实验和Zr链MCSM原件为中心，100Zr一手寿命并未在本轮补齐。

## Grounded Evidence

| Evidence | source / locator | provenance | limitation |
|---|---|---|---|
| 98Zr的2₁、4₁、6₁平均寿命τ=3.8(8)、7.5(15)、2.6(9)ps | [[doctoral-r1-g28-singh-2018-98zr-lifetimes]]，PDF3 Table I | 本篇RDDS；总控核原表和实验段 | 采用外部分支比；不能把与B共享寿命的量计成独立 |
| 2₁向0₁的B=2.9(0.6)ₐ(0.2)ᵦW.u.，向0₂为28.3(6.0)ₐ(2.4)ᵦ；4₁向2₁为43.3(8.7)ₐ(10.8)ᵦ、向2₂为67.5(13.5)ₐ(16.9)ᵦ；6₁向4₁为103.0(35.7)ₐ | 同上Table I | a寿命误差，b外部分支误差，均为向下强度 | 不把多行当独立寿命，不私自合并未知Cov |
| 计算Hamiltonian有局部T=1微调，随后固定 | [[doctoral-r1-g28-togashi-2016-zr-mcsm-qpt]]，PDF2 | 模型输入 | 使用90–96Zr的2₁/4₁及94–100Zr的0₂；并非全部重核数据留出或无经验输入 |
| 98Zr0₁→0₂模型占据πg₉/₂从0.4到3.5，长椭态3.5–5.5；特定ESPE范围4→2MeV以内 | 同上PDF4 Fig3及正文 | 模型输出；总控原读 | 同核不同态与不同核比较分开；ESPE不是实验单粒子峰位 |
| 154Sm单极冻结依参考态改变谱及形状；166Er有低γ三轴模型解释 | [[doctoral-r1-g28-otsuka-2023-type-ii-shell-evolution]]，重印书PDF114、116 | Otsuka2022综述所引模型 | 不是Zr实验的独立重复；冻结后仍可形变，不能推出普适必要条件 |

本轮总控回查Singh PDF2–3、Togashi PDF2/4和Otsuka重印书相关页。
Singh装置是VAMOS++与EXOGAM十Clover（非旧稿AGATA），
其未观测feeding处理依原文引用方法，未得到事件数据与完整似然。

## Provisional Reasoning

### 1. 实测变化首先是逐态连接的变化

小B(2₁→0₁)与强得多的2₁→0₂、4₁/6₁跃迁，说明不能只看yrast能级排序和一条基态强度。
作者把这组数据用于形状共存与N=60突变解释；
“弱基态连接”和“激发集体构型”比“刚性球态”的笼统说法更贴近实际测量。
单条B换成β需要模型，不能凭它证明γ刚性或唯一内禀形状。

### 2. Hamiltonian为什么既能固定，又出现壳重排

Togashi模型在指定质子/中子价空间中用JUN45、SNBG3和VMU组成有效相互作用。
MCSM选择投影Slater行列式并变分优化，不能称在完整天文维数基中精确完全对角化。
“固定Hamiltonian”指其后计算不逐核重调，
不等于该Hamiltonian没有经验构造或输入的能级全是留出测试。

对给定两体单极分解，ESPE变化可示意为
\[
\Delta\epsilon_n(j)=\sum_{j'}V^{\rm mono}_{nn}(j,j')\Delta n_n(j')
+\sum_{j'}\widetilde V^{\rm mono}_{pn}(j',j)\Delta n_p(j').
\]
矩阵元单位为能量，占据差无量纲；同类轨道、自相互作用和pn等效项须使用该定义的约定。
这是指定模型下的占据反馈，不是从实验数一条转移峰就直接得到的能级移动公式。

Togashi PDF4明确：πg₉/₂与νg₇/₂耦合中中心力和张量力相干，下拉约2MeV；
与νh₁₁/₂时两者相消，但净效应仍下拉。不能只归因“张量吸引”。
较紧密的ESPE有利于多构型四极相干，形变和占据重排又互相促进。
T-plot用于分析所选非正交基与本征态重叠，不等于实验测得的经典形状概率密度。

### 3. 急剧转变的两态直观及其边界

用两构型示意Hamiltonian
\[
H=\begin{pmatrix}E_a&V\\V&E_b\end{pmatrix},\qquad
\Delta E=\sqrt{(E_b-E_a)^2+4|V|^2}.
\]
当未混合能量差经过零，若V较小，组态成分变化可以陡峭；
但跨核子数的离散链不是可连续调参的单个实验系统，有限维模型无热力学非解析奇点。
Togashi以不同重排构型的弱混合解释Zr突变，未在此给通用10–50keV混合阈值。
不能由占据数差自动计算V，也不能把一阶QPT语言当所有微观机制已唯一确立。

### 4. 单极冻结真正告诉了什么

Otsuka2022原作在2023书中重印，正确DOI是`10.3390/physics4010018`。
154Sm的“冻结”是把某参考态的单极期望编码为SPE、去掉活动单极项后重算。
原书PDF114：以基态为参考，0₂带上移约0.5MeV；以球形HF态为参考，基态成为三轴。
后者仍形变，直接限制“没有单极重排就不能形变”的过宽说法。
干预结果证明这一模型中的定量重要性，不证明所有核相同的必要条件。

## Assumptions

- 所列绝对E2采用原表方向、平均寿命和分离误差，不把外部分支当新测。
- ESPE、单极/多极分解、T-plot与形状分类依给定模型空间和有效算符。
- 100Zr的理论图箭头73/101等不能添加实测误差；本页没有使用未核的一手寿命数字。
- 两态示意不取代多构型计算，0⁺的实验室Qs仍恒零。

## Competing Explanations

单极反馈、配对和四极相干不是简单互斥；不同EDF/集体模型也能构造相变/共存图像。
Singh Fig2所比较的几种计算对突变有不同表现，不能据此宣布所有平均场理论失效。
作者关于平均粒子数使演化变平缓的讨论是可能解释，尚非排除了其它误差来源的定理。
近期后续实验/模型现状不因读了2016/2018原文而自动核准。

## Transfer Conditions

跨Ni/Kr/Zr/Mo/Ru比较要指定闭壳基准、允许的跨壳轨道、径向/张量矩阵元、
配对、占据反馈与自旋窗口。共享一个高j轨道或同一N不构成充分条件。
Sr/Mo/Ru的具体演化需各自原始数据，不能以本Zr模型替它们定义整个γ分布。
转移反应可约束强度分布，但占据抽取依赖反应模型、算符分辨尺度和缺失强度。

## Failure Conditions

把拟合能级当独立留出、把MCSM叫无经验精确解、
把Q4幅度方差当γ方差、用任意角宽/比值阈值裁决刚软，
或由一个模型的单极冻结推出普适禁戒，均需撤回。

## Falsification or Reverse Tests

在固定相互作用下联合比较能级、不同0⁺连接、绝对E2、E0及转移强度。
逐项说明哪些用于构造相互作用，哪些是真正未拟合的预测。
若某种简化机制不能再现弱/强分支的共同模式，应增加竞争构型或改变输入，而非只重调一个β。
γ分布需足够的带符号E2网络和高阶/动力学约束，不能只看一个平均q₃。

## Open Questions

- **idea：** Ni与Zr的跨壳反馈是否可在同一模型分解下比较相对能标？
  assumption是映射有效相互作用、模型空间与反应探针；
  竞争解释为不同四极容量及配对。先预测未拟合EM/转移强度，不预设质中交换对偶或一个固定ESPE阈值。
- **idea：** N=60同中子素中哪些占据变化影响β幅度，哪些主要影响非轴自由度？
  prediction由逐核共同算符计算产生；不能预设Zr纯SU3、Ru纯O6。
  竞争解释为构型混合/有效算符/惯量变化；若现有矩阵元不能区分，保留不可识别并选择新连接。
- 搜索集中于上述原件与综述，未穷尽Mo/Ru及Zr后续工作；“未核后续”不等于“尚未发现”。

## Human Review

- Review scope: G28研学和总控原件复核/重写；未有用户逐项审核。
- Decision: provisional，具体结论按原件与条件使用。
- Complete unresolved P0/P1 inventory: Otsuka文章身份误写已修；P1为100Zr一手寿命、
  全Cov、共同留出测试与反应强度映射尚未完成，不自动成为用户待办。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-11-08 | 核实验表、微调范围及原书 | worker draft | provisional | 修正EXOGAM/拟合数据/理论箭头，撤回普适刚软和单极必要性 | doctoral-nuclear-structure-foundations |
