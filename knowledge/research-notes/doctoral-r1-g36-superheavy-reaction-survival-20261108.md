---
type: research-note
title: "超重核合成：逐分波形成、蒸发存活与实验产额"
aliases: [G36 superheavy reaction survival]
created: 2026-11-08
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [zagrebaev-2001-superheavy-synthesis-survival]
created_from: "G36原件研学；总控核PDF1/6–7/9/11及量纲后重建"
promotion_target: ""
tags: [superheavy, fusion, survival-probability, fission, reaction-dynamics, doctoral-foundations]
---

# 静态壳稳定性怎样接入一次合成实验

## Research Trigger

形状与壳结构影响裂变势垒和能级密度，但实验蒸发剩余核产额还经过进入、形成、冷却及探测。
本页把三因子公式落实到共同能量/分波与蒸发路径，避免用一项稳定性直接预言事件数。

## Grounded Evidence

| Evidence | source / locator | provenance | limitation |
|---|---|---|---|
| 三阶段分解及作者明确approximation声明 | [[zagrebaev-2001-superheavy-synthesis-survival]]，PDF1 Eq1后 | 反应模型近似；总控原读 | 时间尺度分离支持分步，不证明完全独立 |
| 状态密度、Kramers/壳阻尼及集体增强 | 同文PDF6 Eqs7–9 | 模型输入 | 不把参数化β分界或阻尼常数当核区普适定理 |
| 多步中子动能积分及最后γ级联概率 | 同文PDF7 Eqs10–11 | 统计蒸发模型 | 最后G_Nγ由作者定义为概率，不是带能量单位的宽度 |
| 254No 2n剩余自旋比分波俘获分布窄 | 同文PDF9 Fig6，E*=25MeV | 引用实验直方图与模型比较 | 没有本任务新实验；不补图外固定自旋硬门 |
| 48Ca+244Pu的capture/近对称裂变与4n单点比较 | 同文PDF11 Fig10及正文 | 引用历史实验及多组模型输入 | 一个4n点不是完整4n实验激发函数，更不唯一反演势垒 |

实际出版原件14页，SHA `0fbce3d3faded1e072ce25eeb8a758cabb81d54b2df2eee71f55efd1686116c8`。
PDF首页及Crossref在线发表日期为2001-12-12；本页用其出版记录，不把历史参数叫2026最新。

## Provisional Reasoning

### 1. 三个概率必须在同一分波内相乘

在原文入口自旋处理合同下，
\[
\sigma_{\rm ER}(E)\simeq\frac{\pi\hbar^2}{2\mu E}
\sum_l(2l+1)T(E,l)P_{\rm CN}(E,l)W_{\rm sur}(E^*,l).
\]
l是无量纲量子数，角动量为lℏ；若处理非零入口自旋，需要相应通道耦合/统计平均。
原文定义\(E^*=E-Q_{gg}^{fus}\)，其Q定义为复合核质量减初始两质量，
与另一些文献把正放热Q加到E的写法须先对齐符号。
几何因子有面积单位，\(1\mathrm{fm}^2=.01b=10mb=10^{10}pb\)。

T描述接触的进入通道，P_CN描述接触后形成复合核的条件概率，
W描述给定复合态冷却到所选剩余道的概率。
共同l/E依赖意味着不能随意把一个独立常数W提出求和。
可以定义对特定形成分布加权的平均W，但它不是额外独立实测因子。
Fig6展示的窄存活分布给出具体例子，不等于所有超重体系都在相同自旋截断。

### 2. 逐蒸发步保持能量、角动量和归一

令每步残余激发能
\(E_k^*=E_{k-1}^*-S_n^{(k)}-\epsilon_k\)。
原文Eq10对中子动能概率密度与\(\Gamma_n/\Gamma_{tot}\)逐步卷积；
其选用的\(P_n\propto\sqrt\epsilon e^{-\epsilon/T}\)在各步允许窗口归一。
不能把它未经说明替换成另一种谱或统一平均“2T”，也不能忽略截断。

末端作者的G_Nγ为γ级联完成冷却的**无量纲概率**，Eq11用多个
\(\Gamma_\gamma/\Gamma_{tot}\)作近似。这里Γ宽度有能量单位，Γ比与G才无量纲。
给最终概率乘一个裸宽度会量纲错误；相似符号不表示相同对象。
实际J_k演化与可竞争n/p/α/γ/f通道还要由同一统计模型处理。

### 3. 壳修正与集体增强怎样进入存活

原文统计模型的裂变宽度含势垒、能级密度、惯量与耗散等输入。
基态与鞍点的集体增强若相似可部分抵消；
若一个较近球形而另一个较变形，状态密度比及Γ_n/Γ_f可明显改变。
这说明形状信息重要，却不说明低能E2就直接测出了高激发能级密度增强。
壳阻尼、配对、蒸发后的逐核变化和角动量应共同输入。

PDF11的Fig10有两个明确竞争：
把近对称碎片都当fusion-fission会给P_CN约.1，但准裂变也可贡献该窗；
改用8.9或6.8MeV的模型势垒会明显改变ER曲线，K_vib也影响结果。
这些变化不能从一个4n点唯一分离；原文较高势垒计算高估约40倍，
不是我们测得一个“正确势垒”。

### 4. 理论截面还没有成为探测事件

以下是任务测量模型：期望计数需要对束流、靶层及响应积分，示意为
\[
N_{\rm sig}=\int dt\,\Phi_b(t)\int dx\,n_t(x)
\sigma_{\rm ER}(E(x,t))\,\epsilon_{\rm sep}(x,E,\ldots)
\epsilon_{\rm chain}(t,\ldots).
\]
这里Φ_b为每秒弹核数，n_t为体密度，dx积分成为面密度；
还可加入能散、反冲角、电荷态、live、背景与衰变链接收。
这不是本文所有实验已给出的参数表；本任务没有用户这些输入。
靶厚平均点也不应自动当作无能损的单能截面。

## Assumptions

- 三阶段时间尺度分离、复合态统计衰变和各输入沿作者模型处理。
- 每步能谱归一、总宽度与最终γ概率具有正确量纲；入口自旋统计不可漏。
- 作者拟合/采用的barrier、阻尼、集体增强与P_CN并非独立测量。
- 2001模型对当时数据的分析不自动给当前所有核的预测精度。

## Competing Explanations

形成概率、准裂变污染、势垒、能级密度、耗散及实验平均可补偿部分变化。
只有更多共同观测才能缩小这种解释重叠；同一曲线拟合好不证明参数唯一。
近对称碎片不是无模型复合核标签，低能集体态也不是高温K_coll的直接标尺。

## Transfer Conditions

迁移到新靶弹组合要重算接触势面/取向、质量Q、形成路径、逐步分离能和存活，
再卷积实际分离器/衰变接收。更强静态壳修正或更长某态寿命不保证更大产额。
核心的形状/配对知识可帮助建模，但需要相同激发能与自旋语境。

## Failure Conditions

把近似叫严格量子分解、丢(2l+1)、单位错千倍、
把最终级联概率叫宽度、把一个模型势垒阈值用于全区、
或无束流/效率输入便给事件数，均须撤回。

## Falsification or Reverse Tests

先核面积与Γ比量纲、逐步能量窗口及共同l依赖；
在共同校准下比较多个xn道、capture/裂变信息和剩余自旋，不能只重调一个4n点。
若不同模型在新增观测的响应卷积后仍不可分，保留参数边界而非强行归因。

## Open Questions

- **idea：** 中子/碎片质量角关联能否减少近对称裂变窗中的形成解释歧义？
  assumption为完整中子接收和共同动力学；竞争解释为长寿命准裂变及预平衡发射。
  先给两模型前向分布，不能预设一个通用时间/能量阈值或称模型无关上限。
- **idea：** 一致的微观集体态密度是否改变所需的存活/势垒输入？
  需同时处理基态附近与鞍点、温度及耗散；竞争解释为P_CN或实验透过率。
  若新输入不能改变未拟合观测，就不据它解释单点差异，也不预设势垒补偿方向。
- 后续现状及新体系数据未穷尽，不能把2001年的不确定性总结称2026普适精度极限。

## Human Review

- Review scope: G36研学与总控原件/量纲核查；无用户逐项审核。
- Decision: provisional，保留三阶段近似与多输入边界。
- Complete unresolved P0/P1 inventory: 单位与虚构普适阈值已修；P1为共同数据、
  模型参数Cov和实验响应未取得，不自动成为用户待办。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-11-08 | 核Eq1/10/11与Fig6/10 | worker draft | provisional | 恢复阶段近似、正确pb单位及无量纲级联末因子，撤回单点唯一反演 | doctoral-nuclear-structure-foundations |
