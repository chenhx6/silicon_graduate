---
type: research-note
title: "A130重写研学：准粒子顺排取向、横纵向分叉与进动动力学边界"
aliases: [A130 alignment frame wobbling bifurcation and precession boundaries]
created: 2026-11-13
updated: 2026-11-13
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "父根据已接受LaTeX正文与实际原件重建；旧稿仅留本地历史"
promotion_target: ""
evidence_sources: [frauendorf-2014-transverse-wobbling, matsuzaki-2004-nuclear-inertia-and-wobbling]
tags: [A130, doctoral-thesis, transverse-wobbling, longitudinal-wobbling, tilted-precession, high-K, alignment]
---

# 冻结顺排几何、频率与实验参考量

## Research Trigger

第3.3节需要分开几何定义、局域稳定性与实测能差，避免用下降曲线单独命名模式。
本轮按已接受正文重建本页，不沿用旧稿的普遍斜率或固定惯量轴假设。

## Grounded Evidence

[[frauendorf-2014-transverse-wobbling]]原PDF6的Eqs.(11)–(24)及相邻讨论给HFA起点，
PDF10保留完整QTR与M1等局限。[[matsuzaki-2004-nuclear-inertia-and-wobbling]]
原PDF3–6的Eqs.(1)–(24)给出指定推转RPA与频率相关响应例。
原件路径与实际哈希回各source；模型论文所引实验不再次算独立测量。

## Provisional Reasoning

本页按正文重标轴：令物理总角动量和核芯角动量带作用量单位，
mathcalI=Ihat/hbar；j是已经除以hbar的准粒子投影。定义Ak=hbar²/(2Jk)。
固定j沿1轴的模型为H=A1(mathcalI1−j)²+A2 mathcalI2²+A3 mathcalI3²。
用领先经典I²球且mathcalI1约等于I，在横向小幅展开中

$$C_2=A_2-A_1+A_1j/I,\qquad C_3=A_3-A_1+A_1j/I,$$
$$\hbar\omega=2I\sqrt{C_2C_3}.$$

所选正能局域极小要求C2和C3均正；仅C2C3非负并不足以说明是能量极小。
体轴负对易子中的mathcalI1也在同一领先阶才替换成I，因此玻色对易是局域近似。

TW/LW按准粒子优势取向相对于最大惯量轴定义；它不要求j相对于总I或核芯R
始终垂直。几何短/中/长轴与最大惯量的对应仍需具体模型，不能只由质量区指定。
选J2>J1>=J3时，Ic=j/(1−J1/J2)。把频率平方写为

$$
(\hbar\omega)^2/4=[(A_2-A_1)I+A_1j][(A_3-A_1)I+A_1j]
$$

可见TW支路可能先升后降，靠近Ic才在该局域模型中软化。超过该参考点的平面
倾斜分叉不是一准粒子模型自动产生的三维手征构型。固定FA参数的LW上升也不等于
所有实核能量都必须上升；实际j与惯量可随频率改变。

父用未展开的经典H作独立有限差分，核两曲率及平方因子；人工例
A=(.01,.008,.03)、j=6.5在I8与20的频率平方导数异号。
这些是任意能量单位的模型控制，不是Lu或Pr拟合。完整有限I量子谱、EM与真实惯量
没有被这个控制复现。j=6.5表示投影，而非量子角动量模长的精确定义。

实测Ewob常用相邻参考带I−1/I+1的平均插值，限于所声明的交错自旋序列。
其它同I能差也可以合法定义，但不能不说明参考就混用。判别需比较模型对能谱、
E2/M1及相位敏感量的共同预言，而不是套一个普适delta阈值。

## Assumptions

冻结j、固定正惯量、选定主轴与小振幅大I展开。能量极小与高阶修正须分别检查；
完整QTR可解除冻结，不能以HFA代表所有粒子转子计算。

## Competing Explanations

准粒子重取向、惯量变化、普通signature伴带或带混合均可改变能差趋势。
M1大小受组态和磁算符影响，不能由冻结内禀j推断实验室带间M1恒零。

## Transfer Conditions

可迁移的是上述模型条件与比较方法；目标核的轴序、占据、配对和可观测自旋窗须重新确定。

## Failure Conditions

混用带hbar与无量纲j；把领先阶对易当精确；由下降曲线或质量区直接确证TW；
把完整QTR当成全程冻结；把曲率零点当成所有有限量子谱的精确零能隙。

## Falsification or Reverse Tests

使用未参与调参的电磁量比较所选模型及替代解释，保留数据协方差和参考带身份。
具体模型预测失败可推翻该实现，不能因单项吻合就认证整类模型。

## Open Questions

同输入的量子转子及微观响应怎样限定局域展开的窗口？哪些实际EM分支最能区分重取向与形状混合？

## Human Review

本轮为智能体原件与模型代数核查，没有新增真实用户审核事件。

## Promotion or Rejection History

2026-11-13：父按接受的3.3节重建，撤回旧稿中普遍下降、固定物理角和过度惯量轴对应。
