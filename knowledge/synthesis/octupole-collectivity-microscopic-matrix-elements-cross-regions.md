---
type: synthesis
title: "跨核区八极关联：轨道允许性、跃迁强度与形状推断"
aliases: [八极关联微观演化专题, octupole-collectivity-cross-regions, 八极跃迁矩阵元]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
scope: octupole-matrix-elements-and-cross-region-enhancement
confidence: medium
sources: [book-suhonen-from-nucleons-to-nucleus, mach-1990-96zr, karmakar-2025-2026-98mo-octupole-preview, karmakar-2024-100ru-enhanced-e1-lifetimes, saracino-2026-102ru-scissors-octupole-resonances, bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole, gaffney-2013-pear-shaped-rn-ra]
tags: [octupole, e3, e1, cross-region, selection-rules, identifiability]
---

# 跨核区八极关联：从轨道到观测量

## Agent active summary

2026-11-07按原件与角动量代数修订旧专题：撤回未来源化的区域强度/D0范围、
“Δl=Δj=3是守恒定则”、普适静态形变门槛与单粒子矩阵元必达极值的说法。
新98Mo、102Ru正文补齐获取缺口，使低自旋E3、NRF偶极响应和高自旋E1可以逐项比较；
它们测量的对象不同，不能拼接成一份静态三轴—八极形状证明。

## Question and Scope

为什么八极机制可能在不同质量区出现，为什么找到一对轨道或一条强E1还不够？
本页比较允许耦合、单粒子矩阵元、多体相干、谱学响应与形状解释五个层次。
A≈130仍是研究锚点；Ba/Ra的直接E3提供校准，不能把其数值直接移植给Ru/Mo/Br。

## Microscopic Conditions

对自旋无关的电多极算符，必要角动量与宇称条件是
\[
 |j_f-j_i|\leq\lambda\leq j_f+j_i,\qquad
 (-1)^{l_f+l_i+\lambda}=+1,
\]
并满足轨道角动量三角条件。E3因而允许Δl=1或3（同时满足其它条件），
并不要求Δj恰为3。常见的Δl=Δj=3驱动轨道对是一类有利结构，
其集体效果还取决于径向积分、能级间隔、费米面占据、配对和多体跃迁密度。
来源为[[book-suhonen-from-nucleons-to-nucleus]] printed29–30、121–124，Eqs2.27–2.29、6.18、6.23。

旧表把πp1/2↔g9/2列为单粒子E3驱动：其Δj=4，秩3角向元严格为零。
p3/2↔g9/2、d5/2↔h11/2、f7/2↔i13/2、g9/2↔j15/2的角向允许性
则可直接核查。允许性不能认证这些轨道在具体核中的占据，也不排除
经过其他组态、有效算符或多体关联形成八极响应。精确控制见
[[octupole-orbital-eligibility-and-collectivity-boundary-20261107]]。

## Evidence Matrix

| 对象/观测 | 直接来源及locator | 可支持的层次 | 仍不能唯一决定 |
|---|---|---|---|
| A≈80 78Br异宇称E1连接与手征候选 | [[liu-chen-2016-78br-chirality-reflection-symmetry-thesis]]，对应谱学章节与CPQ展望 | 作者讨论八极关联与取向模式可能并存 | E1不等于静态β3，多个候选带不等于CPQ确证 |
| N=56 96Zr低自旋E3 | [[mach-1990-96zr]] pp.R811–R814，寿命与分支 | B(E3;3−→0+)=65(10) W.u.的直接低自旋集体性锚点 | 不把模型两种PES版本合并为唯一球形/唯一八极极小 |
| 98Mo两新E3指定与相对比值 | [[karmakar-2025-2026-98mo-octupole-preview]] PDF4 Table1、PDF6–7 Tables2–3 | 两弱线的态对、相对强度，以及E3/E2、E1/E2的自旋变化 | 缺直接寿命/绝对E3；约四倍指E3/E2比，不是绝对E3四倍 |
| 100Ru高自旋E1 | [[karmakar-2024-100ru-enhanced-e1-lifetimes]] PDF2 TableI | 有限寿命与绝对E1；高自旋另有上限 | 增强E1与共同模型失配尚不能唯一选择永久八极形状 |
| 102Ru低自旋NRF | [[saracino-2026-102ru-scissors-octupole-resonances]] PDF3 Figs1–2、PDF4–6 | M1/E1宇称分辨响应；约5-MeV E1聚集及作者八极共振解释 | SI/逐态分支未得；累计强度拟合不测静态β3，也不恢复高自旋取向 |
| 144/146Ba直接库仑激发 | [[bucher-2016-144ba-direct-octupole]] TableI；[[bucher-2017-146ba-direct-octupole]] TableI/Figs3–5 | 向下E3分别48(+25/−34)、48(+21/−29) W.u.，同时E1明显不同 | 中心舍入相同不是严格恒定；小E1不意味着弱E3，转换Q3/β3仍有模型条件 |
| 220Rn/224Ra跨区校准 | [[gaffney-2013-pear-shaped-rn-ra]] 原文E3/矩阵元分析 | 用同一测量框架比较不同八极响应 | 不能把两核合成一个固定B(E3)或统一“刚性金标准” |

各数值保留退激/激发方向，3−→0+与0+→3−的B值相差7倍。
本文未重拟合CoulEx事件、DSAM线形、完整NRF分支或其协方差。

## Synthesis

质量区迁移的可检验因果链为：价空间和占据→允许的径向/角向矩阵元→
残余相互作用与多体相干→自旋/组态依赖的波函数→实验可见的能级和矩阵元。
同一N=56链有比较价值，但增加质子或阻塞一个轨道，不会自动给出
统一的八极增强或抑制规律。模型若要跨区迁移，应更换目标核的实际输入，
而保留同一算符定义和竞争解释比较。

## Counter-evidence

E1可因质子/中子偶极贡献相消而很小；146Ba是本任务相关的实验证据。
因此撤回旧页D0≥0.2 e fm、B(E3)≥40–50 W.u.等静态形状阈值。
E3增强、交替宇称带和模型非零极小分别提供信息；没有任何一项在所有核中
单独区分动态涨落与局域内禀形变。

能级位移也要写明定义与参考：对E(I)=A I(I+1)的同一理想转子，
未加权的E(I)−[E(I−1)+E(I+1)]/2本身等于−A，不是零。
若采用
\[
 \delta E_w(I)=E_-(I)-\frac{(I+1)E_+(I-1)+I E_+(I+1)}{2I+1},
\]
则共同I(I+1)项消去。这是本任务解析控制，不能代替原文S(I)的定义或数据。

## Model Dependence

有限核宇称本征态的实验室奇宇称算符期望为零；讨论“静态”内禀八极形状
需要说明对称性恢复、局域波包/内禀表示及可测跃迁网络，不能要求直接测得
非零实验室< Q3 >。偶次矩、相关性、能谱、绝对E3网络与共同模型
提供互补限制；E1和E3并非相同算符。

## Limitations and Missing Evidence

98Mo绝对矩阵元、102Ru SI/分支与共同模型生产输入仍缺；
不能因正文获取完成而宣称解释已经闭合。
P0: none identified in the registered originals。P1：轨道矩阵元与多体相干、
模型静态坐标与实验室观测、独立采集与同一资料重述分别核对。
本页是跨来源综合，不替代其source和实际原件。

## Sources

来源与locator已逐行给出；研究队列见[[isomer-six-region-transfer-research]]。
