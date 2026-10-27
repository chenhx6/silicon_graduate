---
type: research-note
title: "134Pr两带解混合模型中的非对角E2矩阵元干涉与内禀四极矩比值敏感性研究"
aliases: [134Pr两带解混合非对角E2敏感性, 134Pr offdiagonal E2 sensitivity]
created: 2026-10-27
updated: 2026-10-27
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [petrache-2006-near-degenerate-chiral-misinterpretation, tonev-2006-134pr-lifetime-chiral, tonev-2007-134pr-dynamic-chirality]
created_from: Day25 task continuation
promotion_target: chirality-shape-coexistence-companion-matrix
tags: [134Pr, chirality, shape-coexistence, band-mixing, E2-matrix-elements, sensitivity-analysis]
---

# 134Pr两带混合：实验列、模型列与非对角E2敏感性

## Research Trigger

[[petrache-2006-near-degenerate-chiral-misinterpretation]] Eqs1–5/TableI在无off-diagonal E2、短spin段固定V等假定下给Q0,1/Q0,2允许1.6–2.4；不是直接静态形状测量。checkpoint005父/子代理fresh视觉核printed112502-3，新增needs_review:true。

旧版把计算列当实验目标、未写17→15连续带交换、无实际likelihood/producer，故撤回旧χ²/95%区间与“4–8%证明等形状手征/完全解释”。UC=ultimate cranking约1.25；TRS另约1.7，非共同1.25–1.4。旧稿由Git和入口快照保留。

## Grounded Evidence

|初态|Eγ,out/in, keV|Experiment|Calculation，Q1/Q2=2|abs(V), keV|αI|
|---|---|---|---|---|---|
|17ny|991/1027|.3(1)|.33|14|.118|
|17y|909/873|.6(1)|.70|14|—|
|15y|671/892|0(1)|.034|14|.894|
|15ny|928/707|1.1(5)|.78|14|—|
|18ny|1113/1069|.22(9)|.17|17|.099|
|18y|896/940|<.08|.062|17|—|
|16ny|813/976|0(1)|.12|17|.427|
|16y|933/770|1.3(3)|1.36|17|—|

Experiment来自Ref11；0(1)不是精确零，<.08不当高斯中心或已知置信度。2.0(4)未给Gaussian抽样含义。Ref9/11不同书目不证明统计独立；Tonev06/07复用同实验。

## Provisional Reasoning

固定原α、b=+sqrt(1−α²)、$R=\begin{pmatrix}a&b\\b&-a\end{pmatrix}$，另设共同实对称前向核$Q/q_1=\begin{pmatrix}1&x\\x&y\end{pmatrix}$：

$$M_{fi}=R_f Q R_i^T.$$

不同I前向核对称性是额外ansatz，不由Hermiticity自动推出。PE06连续带17→15交换yrast身份，Table out/in对应raw跨/内比倒数；18→16不倒。

|x=q12/q1|y=q2/q1|R17ny|R17y|R18ny|R18y|
|---|---|---|---|---|---|
|0|.50|.333870|.703522|.170382|.062384|
|.04|.73|.315145|.647261|.187283|.067046|
|.08|1|.303851|.600031|.201070|.073618|

实际producer：outputs/learning-daily/20261027-DAY25-chirality-counterevidence-shape-coexistence-run-01/forward-checks-005.py，同名JSON存输入与完整精度。首行重现原计算四点，后两行为额外假定下的敏感性例子；不是八行联合拟合。α来自原q12=0提取，不能当独立测量固定后声称替代模型获胜。

x=0,y=1时，同yrast排序的raw Ry=Rny=tan²(θi−θf)；连续带交换时两者一起取倒数仍相等。这是条件代数，不是所有手征态的普适定理。

## 4. 可识别量与解释边界

q12可改变分支比对对角元比的反演；q1=q2只说明选定基底两个对角transition moments相等，不等于完整形状相同或chiral波函数。部分数据相容不证明真实机制。

正交变换下：

$$\|M\|_F^2=q_1^2+q_2^2+2q_{12}^2.$$

局部比值不给绝对norm/相干phase，须补完整links、absoluteEM、相位约定及独立模型预报。总χ²不能直接与Δχ²=4比较；未恢复Cov、上限likelihood及α/V/能隙联合约束前不报CI或显著性。

## Learning Decision

revises旧数值认证；supports非对角核的可检验敏感性问题。134Pr对简单ideal-pair的挑战仍为原作者条件模型结论，不能借本练习排除所有手征动力学或实证刚性形状共存。

## Assumptions

固定原α、正根b与共同实对称forward核；q12=q21是额外ansatz。17→15的连续带身份交换随ratio一起处理；原表上限不转高斯点。

## Competing Explanations

对角元差、非对角干涉、mixing变化及更大配置空间可改变部分分支。局部前向例子不决定哪种实际机制成立。

## Transfer Conditions

该2×2练习仅作同spin-block的E2核控制；绝对单位、各spin几何及全links映射须另核。原α不能成为新模型独立测量。

## Failure Conditions

计算列充实验、漏掉17→15倒数、固定旧α后宣称联合拟合或用总χ²对Δχ²阈值，均不成立。

## Falsification or Reverse Tests

x=0/y=.5必须复现TableI四个计算值，已由独立矩阵乘法核；共同rephase不改B。若拟合新模型须用真实实验列/上限likelihood和能隙约束，当前未完成该检验。

## Open Questions

完整likelihood/Cov、能隙与V/α关联、actual signed核及未用于定标的EM约束尚缺，不报CI或机制唯一性。

## Human Review

本页未发生用户claim裁决，review_status保持unreviewed；不迁移其它source或Band5的人审到本推理。

## Promotion or Rejection History

2026-10-27 checkpoint005撤回旧强认证，以原件和声明条件的前向控制替代；reasoning_status为provisional。旧稿在Git和入口快照保留，未将self-audit写成human-reviewed。
