---
type: research-note
title: "形变、配对涨落与0νββ矩阵元：从投影波函数到算符约定"
aliases: [G35 deformation pairing double beta]
created: 2026-11-08
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [doctoral-r1-g35-rodriguez-2010-prl-0nubb-edf, doctoral-r1-g35-vaquero-2013-prl-shape-pairing-0nubb]
created_from: "G35研学；总控回两原件PDF1–4及Table I后缩减重建"
promotion_target: ""
tags: [double-beta-decay, deformation, pairing, gcm, effective-operator, doctoral-foundations]
---

# 为什么低能形变重要，却不能直接给一个0ν矩阵元

## Research Trigger

核结构的电荷形状、配对和组态关联怎样进入双贝塔矩阵元，是核心与弱相互作用翼的实质接口。
本页用两项EDF/GCM原始工作解释这条链，不把一个形变参数或单β淬灭直接升级为通用0ν缩放。

## Grounded Evidence

| Evidence | source / locator | provenance | limitation |
|---|---|---|---|
| GognyD1S、轴向HFB、粒子数投影变分、初末态粒子数/角动量投影和形状GCM | [[doctoral-r1-g35-rodriguez-2010-prl-0nubb-edf]]，实际arXiv1008.5260v2 PDF1–2 Eqs1–4 | 模型框架，11个大振子壳 | 不是完整无截断精确解；不含所有准粒子/三轴自由度 |
| 150Nd/150Sm的形变分布及归一GT核在β_i/β_f平面中变化 | 同原件PDF2–3 Figs1–2 | 作者模型输出 | 图2核还要用初末态权重积分，不能把局部峰当最终NME |
| 增加配对坐标δ=√⟨(ΔÂ)²⟩，在同一投影GCM中混合 | [[doctoral-r1-g35-vaquero-2013-prl-shape-pairing-0nubb]]，arXiv1401.0650v1 PDF1–3 Eqs2–5 | HFB内禀生成坐标 | δ无量纲，不是BCS能隙Δ；最终投影态仍有好粒子数 |
| 2013 Table I的48Ca2.370→2.229、76Ge4.601→5.551、136Xe4.199→4.773 | 同原件PDF4 Table I | 形状一维与形状/配对二维GCM的理论总NME | 同一文内比较；不是实验测得增强 |

两份实际PDF均5物理页；总控独立读PDF1–4的主线/表图，未重跑作者producer。
PDF内部Dated均为2018，与arXiv版本水印及期刊2010/2013年份不同；
本任务只记录这一差异，未查明PDF内部日期产生原因，不发明一次2018新研究。

## Provisional Reasoning

### 1. 明确算符与归一，才可比较NME

这两篇研究采用轻Majorana中微子交换的既定约定，写
\[
[T^{0\nu}_{1/2}]^{-1}=G_{01}|M^{0\nu}|^2
(\langle m_{\beta\beta}\rangle/m_e)^2.
\]
R2010 Eq2为
\(M^{0\nu}=M_{GT}^{0\nu}-(g_V/g_A)^2M_F^{0\nu}-M_T^{0\nu}\)，
取gV=1、gA=1.25，认为tensor较小而忽略；没有原文支持的“<2%”数字。
V2013同样忽略tensor并沿用其算符/势的归一。

Eq1未单列gA⁴，若要把相空间/算符换为另一文献约定，必须一起转换；
不能在原式外无说明再乘一次，也不能认为NME的全部gA依赖只有一个显式系数。
中微子势还包含所选有限核子尺寸、高阶流和短程关联处理。
本页未重核所有被引算符文献，不给改变gA后的无条件数值预言。

### 2. 投影为什么不排斥形变和配对生成坐标

GCM用一组非正交内禀态，经粒子数和I=0投影后叠加。
内禀破缺对称性用于构造关联；最终实验室态仍恢复指定N、Z、I。
所以HFB生成态有非零粒子数涨落，与最终核有确定粒子数并不矛盾。
用δ约束产生不同配对内容后再投影，不是让真实核在测量中改变核子数。

非正交基的原始混合系数g不能直接以|g|²叫概率。
两文用范数核正交化构造集体波函数，再分析分布与跃迁。
这个区别与四极不变量或T-plot也不同，不能把不同图的“概率”不经定义混用。

### 3. 形状匹配与配对是相关约束，不是一个几何定理

R2010 Fig2对150Nd/150Sm显示相近形变的局部GT核往往较大，
而最终态权重所在区域的形变差异和有限混合使总NME约1.71。
作者也比较配对能与局部核结构的相关；这不证明NME只由配对能或时间反演J=0对唯一决定。
其它多体关联及不同角动量对贡献仍需模型处理。
轻中微子势也不能简化为纯局域1fm接触算符，
“形状不匹配导致正交性灾难”不是从这两个图可推出的普适定理。

V2013 Fig1–2实际以136Xe/136Ba展示β与δ联合分布。
Fig2(a)固定指定配对坐标看形变，Fig2(b)固定β=.1看δ、δ′。
作者描述增强宽带在δ′≈δ±3附近，不能写成所有配对核沿δ=δ′达峰。
局部核要与实际集体权重共同积分，不能从某个δ阈值给所有核的配对判据。

### 4. 有条件的数值增量

同一V2013 Table I中增加δ坐标后，76Ge的NME比约1.207，
保持相同机制、相空间和有效质量时，半衰期比约(4.601/5.551)²=.69；
136Xe对应约.77，48Ca则约1.13。
这些是该样本/相互作用中的理论变化，不是实验半衰期已经缩短。
正文所述约10–40%增强也应限于其样本，Ca例外已保留。

不能把R2010与V2013所有1D值当逐字同一生产版本：
例如116Cd分别4.72与4.795。没有作者输入/代码差分，不能猜它由某个网格更新造成。
2010与2013的GT总强度表还有理论/实验两列与采用的(0.74)²因子，
本页不将理论S±错列为实测或由此自动确定0ν算符淬灭。

## Assumptions

- 机制、closure近似、gA/势归一、单粒子空间与GCM自由度按原文固定。
- 轴向形状和配对坐标不是全部关联；作者明确缺三轴、八极、同位旋恢复及显式准粒子等。
- NME与示例半衰期比均为模型量；本任务没有直接实验NME或作者代码重放。
- 内部日期与版本/发表年份分开，不猜重排原因。

## Competing Explanations

初末态形变/配对只是多体不确定度的一部分；同位旋恢复、seniority、其它构型、
核子电流和短程处理也能改变NME。必须在相同算符约定下比较不同方法。
低能E2和β数据可校验模型的一部分，2ν数据也可约束相应模型/算符，
但不自动提供跨动量与多极的单一0ν比例因子。

## Transfer Conditions

跨76Ge、100Mo、136Xe、150Nd等核比较时，保留形状分布、配对内容、
投影、模型空间及算符定义。源于一个轴向模型的趋势不能直接裁决三轴模型。
向双电荷交换等探针迁移还需反应机制和算符匹配，不能称模型无关量尺。

## Failure Conditions

把δ叫能隙、|g|²叫概率、模型NME叫测量、理论S列叫实验、
把样本增量普遍化或重复计入gA，都会使比较失效。

## Falsification or Reverse Tests

先核同一文内表/图和归一，再检查半衰期比与NME平方的关系。
真实模型测试应联合能谱、半径、EM、允许/禁戒弱分支及配对相关探针，
并明确哪些是拟合输入、哪些是留出；不能用一个单核E2值证明全部0ν波函数正确。

## Open Questions

- **idea：** 加入显式三轴坐标后，配对涨落带来的NME变化是否仍与轴向样本相似？
  assumption为同一EDF/算符/投影；竞争解释为模型空间或同位旋关联。
  先预测辅助结构观测与NME的共同变化，不能预设统一增强方向或百分比。
- **idea：** 何种可得的配对相关观测能排除“相近E2却不同配对内容”的模型？
  转移/双电荷交换都需反应理论；若核反应误差与模型差异重叠，保留不可识别。
- 新颖性及更近期计算未穷尽；不把上述2010/2013框架称截至2026的全部前沿。

## Human Review

- Review scope: G35研学、总控读原表/图与归一；未发生用户逐项审阅。
- Decision: provisional，保持作者结果和任务推断的区别。
- Complete unresolved P0/P1 inventory: 理论/实验列与源内日期误解已纠正；P1为作者producer、
  全算符约定差分和新增自由度的联合预测未完成。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-11-08 | 总控回原件后缩减 | worker draft | provisional | 撤回纯短程/唯一配对、DCX无模型阈值及未证日期/代码原因，保留三例同文NME变化 | doctoral-nuclear-structure-foundations |
