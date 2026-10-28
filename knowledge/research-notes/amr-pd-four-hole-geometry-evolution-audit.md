---
type: research-note
title: "Pd四空穴AMR：多叶片几何、104Pd形变收缩与Cd/Pd系统学审计"
aliases: [Pd four-hole AMR audit, 104Pd epsilon2 closure, Pd Cd AMR comparison]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [rather-2014-104pd-antimagnetic-first-page, zhang-2019-104pd-pnc-antimagnetic-rotation, roy-2011-cd110-systematics-antimagnetic, kumar-2023-amr-review, qiao-2025-pd-systematic-amr-metadata, diwanshu-2025-106cd-amr-metadata]
created_from: Day26 delegated Pd AMR four-hole and cross-isotope research
promotion_target: antimagnetic-rotation
tags: [antimagnetic-rotation, 104Pd, 106Pd, 108Pd, four-holes, geometry, shape-evolution, systematics]
---

# Pd四空穴AMR：多叶片几何、形变收缩与Cd/Pd系统学

## Research Trigger

本页检验三个容易被混写的问题：104Pd的四个g9/2质子空穴能否直接当成四个独立经典刃；Zhang 2019的PNC-CSM是否证明了104Pd的形变在终止处真实坍缩；以及104,106,108Pd能否像106,108Cd一样建立同等级的AMR系统学。结果显示，104Pd有直接DSAM E2证据和完整理论原件，106/108Pd在本轮文献范围内没有找到相应AMR来源；这只能作为检索边界，不能写成不存在定理。

## Grounded Evidence

| 问题 | 来源与定位 | 证据层级 | 适用边界 |
|---|---|---|---|
| 104Pd直接实验范围 | [[rather-2014-104pd-antimagnetic-first-page]] printed061303-1摘要及Eqs.1–2 | DSAM实验报告+模型定义 | 只取得5页中的第一页，未读逐点寿命表 |
| 104Pd完整PNC结果 | [[zhang-2019-104pd-pnc-antimagnetic-rotation]] PDF pp1–7 | 理论计算、模型解释 | 实验点取自Rather，不是独立实验 |
| 106/108Pd文献范围 | [[kumar-2023-amr-review]] PDF pp8–10、99–105 | 综述检索边界 | 未列出不等于物理上不存在 |
| Cd对照 | [[roy-2011-cd110-systematics-antimagnetic]] printed324 Table1、pp324–326 | 实验寿命与粒子加转子解释 | 110Cd高自旋末端及Roy Eq3映射有既有边界 |
| 更高质量Pd理论方向 | [[qiao-2025-pd-systematic-amr-metadata]] | Crossref身份信息 | 题名只涉及103,105,107,109Pd，正文本轮未读 |
| 106Cd后续入口 | [[diwanshu-2025-106cd-amr-metadata]] | Crossref身份信息 | 仅确认题名，未读取正文和数据 |

## Provisional Reasoning

### 1. 四空穴的几何与量子反对称化必须分两层

在理想多叶片图像中，把四个g9/2空穴分成两组等权时间反演对：

$$
\mathbf j_{a\pm}=j_h(\pm\sin\theta_a\cos\phi_a,\n\pm\sin\theta_a\sin\phi_a,\cos\theta_a),
$$

$$
\mathbf j_{b\pm}=j_h(\pm\sin\theta_b\cos\phi_b,\n\pm\sin\theta_b\sin\phi_b,\cos\theta_b).
$$

每一组的横向磁矩和为零，所以理想几何下

$$
\boldsymbol\mu_\perp=0,
\qquad
\mu_z=2g_a j_h\cos\theta_a+2g_bj_h\cos\theta_b.
$$

如果两组相同角度、相同有效电荷和同一方位角，四刃的不可约四极张量满足

$$
Q_{21}=0,
\qquad
Q_{22}\propto4\sin^2\theta e^{2i\phi},
$$

因此固定幅度下的几何相对强度仍为

$$
B(E2)\propto16\sin^4\theta.
$$

系数16相对于两刃模型只是振幅归一化变化；角度幂次没有改变。若两组角度不同，结果变为两个 sin²θe²ⁱφ 项的相干和，不能压成一个普适四刃sin⁴曲线。

数值审计在91×91个\((\theta_a,\theta_b)\)网格上验证了理想等权模型的\(\mu_\perp=0\)、\(Q_{21}=0\)和\(R_z(\pi)\)交换残差均为0。该结果只验证矢量几何恒等式，不认证104Pd本征态。

### 2. Rz(π)与Ry(π)T的角色不同

取所有刃位于xz平面。\(R_z(\pi)\)将每个\(+x\)刃交换到对应的\(-x\)刃，并保持每组密度不变；它保护的是成对交换和偶数自旋序列的几何结构。四空穴时必须将两个轨道组的占据和权重一并纳入密度，不能只画四根箭头就宣称对称性。

对一个xz平面矢量，时间反演先令\(\mathbf j\to-\mathbf j\)，再施加\(R_y(\pi)\)后返回原矢量。因此\(R_y(\pi)T\)可保持选定平面构型，但它不是AMR独有判据；普通平面主轴转动也可能共享这一反幺正操作。单独时间反演在有向自旋和旋转电流的内禀系中通常破缺。更一般的三维方位或不等权配对不能直接使用该结论。

PNC-CSM给出更严格的微观限制：104Pd在低频\(\hbar\omega=0.45\)–0.60 MeV时质子配对造成显著off-diagonal alignment，不能唯一拆成四个独立有向刃；超过约0.60 MeV后四个g9/2空穴接近空轨道，off-diagonal贡献减小，分刃图才是近似可读的。因而“四刃”是高频近似图像，不能反向证明低频本征波函数是四个经典粒子。

### 3. 104Pd的实验—PNC对账：E2快速下降需要形变输入

Rather 2014第一页直接报告：104Pd高自旋yrast态的E2由DSAM测量，随角动量增加而下降；作者用半经典粒子加转子模型得到对Routhian和跃迁率的良好描述，并以

$$
I_{sh}=j_p+2j_h\cos\theta,
\qquad
B(E2)=\frac{15}{32\pi}(eQ_{eff})^2\sin^4\theta
$$

描述双刃闭合。该页同时回顾106,108Cd的\(\pi(g_{9/2})^{-2}\)构型和110Cd的芯转动效应。Rather在此半经典构型中采用两质子空穴；这与Zhang PNC计算的四个部分空g9/2空穴构型并不矛盾，因为两者代表不同层次的有效构型，但不能把它们当同一个“已实验证实的四空穴波函数”。

Zhang的PNC-CSM给出以下逐层机制：

- 采用\(\epsilon_2=0.18\)固定形变时，低频B(E2)下降趋势可以得到，但\(\hbar\omega>0.6\) MeV的快速下降无法重现；
- 将\(\epsilon_2\)作为频率函数从约0.18逐步压低，在\(\hbar\omega>0.65\) MeV后急剧下降，并在约0.75 MeV附近趋近零时，才能拟合高频实验趋势；
- 该\(\epsilon_2(\omega)\)路径是由同一B(E2)数据反拟合的模型输入，不是独立静态四极矩测量；
- 配对对惯量、质子占据重排和背弯位置有重要作用，但论文明确说B(E2)主要对形变更敏感，不能写成配对坍缩单独造成E2归零；
- 约0.4 MeV的背弯主要与一对h11/2中子占据/对齐有关；随后质子g9/2占据重排和中子\((g_{7/2},d_{5/2})\)对齐共同构成高自旋AMR演化；
- 约0.45–0.60 MeV质子对齐增益较快，之后中子对齐增长更快，作者据此划分两个AMR阶段；这不是固定核芯角动量比例。

所以104Pd的“终止”更准确地写成：在PNC拟合轨迹中，\(\epsilon_2\)向零收缩、四空穴几何闭合速度改变、并且预测四准粒子带交叉；它尚未成为“全核波函数在某一自旋发生突变”的直接实验结论。Zhang还指出固定形变的自洽TAC-CDFT也未重现实验高频快速E2下降，说明该形变问题仍开放。

### 4. 四个g9/2空穴的量子上界不等于四根经典刃的长度和

若把四个空穴严格视为同一\(j=9/2\)壳层的四个相同费米子，完全对齐行列式只能占据

$$
m=9/2,7/2,5/2,3/2,
$$

所以

$$
J_{p,\max}=12.
$$

标准单j计数给出允许总角动量

$$
J_p=0,2,3,4,5,6,7,8,9,10,12
$$

及相应多重度；它不允许用四个\(j=9/2\)向量直接相加成18作为量子上限。Zhang的Nilsson轨道含形变混合，且四空穴在低频有配对和off-diagonal项，因此其图示\(j_\pi\)是分组后的期望对齐量，不是纯\(j^4\)谱的单一本征态。任何终止点都必须把中子、核芯和跨组态混合同时纳入。

### 5. Pd与Cd的系统学：现有证据不支持把104Pd直接外推到106/108Pd

| 维度 | 106/108Cd | 110Cd | 104Pd | 106/108Pd |
|---|---|---|---|---|
| 直接来源 | Roy复列寿命和B(E2)，原始实验依赖明确 | Roy Table1和110Cd寿命 | Rather摘要/第一页DSAM E2 | 本轮综述范围未找到AMR来源 |
| 质子空穴 | 2个g9/2空穴 | 2个g9/2空穴 | 半经典两空穴；PNC为4个部分空穴 | 未建立 |
| 中子角色 | 106/108Cd的\(h_{11/2}\)、\(g_{7/2}/d_{5/2}\)构型 | \(h_{11/2}^2\)+核芯转动 | 背弯后h11/2中子与gd中子共同作用 | 未建立 |
| E2行为 | 106/108Cd高自旋快速下降，但最高点有effective lifetime边界 | 16–24中心值缓慢下降，不是严格平台 | 高自旋E2快速下降 | 无直接数列可核验 |
| \(J^{(2)}/B(E2)\) | 可随B(E2)下降而升高，但不能设普适阈值 | 芯转动可延缓下降 | 104Pd在背弯附近有尖峰，形变拟合后高频比值可跟随 | 无数据 |
| 终止/交叉 | 需区分剪刀闭合、配对/中子对齐与effective lifetime | 110Cd最高观测态不自动归AMR | Zhang预测四准粒子带交叉和形变趋零 | 只能列为开放问题 |

Kumar综述的Pd参考链列出100Pd、101Pd、102Pd、103Pd和104Pd，并指出若干Pd归属仍较不确定；在该综述的参考和表格范围内没有106Pd或108Pd的AMR条目。2025年Qiao的理论题名研究的是奇A的103,105,107,109Pd，也没有覆盖106/108Pd。这说明现有Pd AMR研究沿着100–105及奇A链发展，不能把偶偶106/108Pd视为104Pd的自然已证实延伸。

### 6. 判据比的证据等级

\(J^{(2)}/B(E2)\)带有单位，且对寿命、分支比、stopping修正和二阶能级差敏感。它可以作为对照图，但不是单值AMR硬门。104Pd Zhang计算中，固定形变只能合理再现前两个比值点；引入由B(E2)反拟合的形变路径后，曲线才在高频跟随数据。这个结果说明比值对\(B(E2)\)系统学高度敏感，不能单独证明四空穴几何。

### 7. 终止后的波函数重组：目前可说到哪里

104Pd Zhang明确预测在约0.8 MeV附近会出现四准粒子带交叉，并认为AMR带可能在此附近终止；但该结论来自PNC-CSM的占据和能级轨迹。可直接核验的微观预兆是：

1. h11/2中子在约0.4 MeV发生占据跃迁，触发背弯；
2. g9/2质子空穴占据在约0.4–0.55 MeV重排；
3. 约0.60 MeV以后off-diagonal配对贡献减弱，四刃近似才更清楚；
4. 约0.65–0.75 MeV形变拟合急剧收缩；
5. 约0.8 MeV附近预测四准粒子带交叉。

这些现象支持“终止是占据、配对、形变和能带交叉的联合重组”这一研究假设，但尚不足以证明配对在终止点严格崩溃，也不足以证明实验已观察到终止后的新带。

## Reproducible Artifacts

目录：`outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-pd-four-hole-20261029/`。

- `pd_four_hole_audit.py`：四刃矢量、\(R_z(\pi)\)、\(R_y(\pi)T\)、\(Q_{21}\)、\(Q_{22}\)网格审计及单j四费米子计数。
- `pd_four_hole_audit.json`：8281个角度组合的残差、四空穴角动量允许值和来源边界。
- `four_hole_geometry.csv`：两刃/四刃固定幅度下的\(T_{22}\)及相对\(B(E2)\)角度律。
- `quantum_termination_comparison.py`：后续若需加入中子配置和终止交叉，可从该工件继续扩展。

## Assumptions

四刃几何假设每组两刃等长、等磁权重、等电四极权重；PNC的刃分解在高频忽略小off-diagonal项；单j四空穴计数严格施加Pauli反对称性；\(\epsilon_2(\omega)\)为Zhang从B(E2)拟合的路径；Pd 106/108缺失结论仅是本次综述范围边界。

## Competing Explanations

104Pd高频E2下降可由多种机制共同产生，当前来源不能把剪刀闭合、形变收缩、配对重排和四准粒子交叉分离成唯一因果链。

## Competing Interpretations

104Pd高频E2下降可由剪刀闭合、形变收缩、质子占据重排、中子对齐、配对变化和四准粒子交叉共同造成。普通终止、弱集体性和DSAM side-feeding/stopping系统学仍是替代解释。核芯角动量增长与核芯电四极振幅不是同一输入。

## Transfer Conditions

可迁移的是成对交换的张量相消、Pauli计数和证据分层。不可迁移的是104Pd的\(\epsilon_2=0.18\to0\)、Zhang的约0.8 MeV四准粒子交叉、Rather的半经典\(Q_{eff}\)、以及Cd的\(J^{(2)}/B(E2)\)经验范围。

## Failure Conditions

若将四个经典箭头的总长度当作量子\(j^4\)上限，将RMS \(\sqrt{\langle J_z^2\rangle}\)当作有向单刃，将拟合形变写成独立实验，或把Kumar综述未列106/108Pd写成不存在，本页结论失效。

## Falsification or Reverse Tests

让两个空穴对子使用不同磁权重，检查\(\mu_\perp\)恢复；保留四刃几何但允许两组\(\theta_a\ne\theta_b\)，检查单一\(\sin^4\theta\)是否失效；在固定配对的多壳模型中移除h11/2交叉，检查背弯和高频E2是否仍出现；用独立静态四极矩或新寿命数据检验\(\epsilon_2(\omega)\)拟合。

## Open Questions

106Pd和108Pd是否存在未被综述收录的偶偶AMR候选带？104Pd四空穴PNC波函数投影后能否同时预测绝对E2、弱带间M1和终止交叉？Rather完整后4页的逐点DSAM数据、side-feeding和stopping修正能否取得？Qiao 2025奇A Pd理论是否能通过同一框架反推偶偶106/108Pd？

## Knowledge Impact and Learning Decision

`supports` 104Pd四空穴的高频近似多叶片图像、配对与形变共同控制E2、以及Pd/Cd证据分层；`revises` “四个g9/2空穴必为四根独立经典刃”“104Pd终止必然配对崩溃”“106/108Pd已建立AMR”的表述；`limits` 104Pd实验缺完整正文、106/108Pd缺独立AMR来源和Qiao正文未读。

## Sources

- [[rather-2014-104pd-antimagnetic-first-page]]
- [[zhang-2019-104pd-pnc-antimagnetic-rotation]]
- [[roy-2011-cd110-systematics-antimagnetic]]
- [[kumar-2023-amr-review]]
- [[qiao-2025-pd-systematic-amr-metadata]]
- [[diwanshu-2025-106cd-amr-metadata]]

## Human Review

Codex source/claim self-audit；保持`unreviewed`，未改变已有撤回和课程信用边界。

## Review Status

几何和单j计数已通过标准库审计；104Pd模型证据已逐页复核；Rather正文缺页；106/108Pd实验AMR状态和104Pd终止后的新带仍未解决。

## Promotion or Rejection History

2026-10-29：新增Pd四空穴研究笔记，明确区分四刃几何、PNC本征态和量子Pauli上界；加入综述范围证据，未把106/108Pd缺项升级为不存在结论。

## Continuation Handoff

下一步优先取得Rather 2014剩余4页和104Pd原始DSAM表；随后检索106/108Pd高自旋谱学、寿命和ENSDF/XUNDL，建立“无AMR证据”与“未检索到”两个状态的区别。若模型路线继续，应在同一PNC或投影框架中同时计算四空穴配对、\(\beta_2,\gamma\)、绝对E2和终止交叉。
