---
type: research-note
reasoning_status: provisional
title: "A130重写：低能核结构模式判据、联合前向预言与可证伪研究候选"
aliases: [a130-rewrite-joint-predictions-and-discriminating-program-20261113]
created: 2026-11-13
updated: 2026-11-13
status: active
review_status: unreviewed
note_scope: "博士论文第3.8节方法论核心：理论前向映射结构、竞争解释重叠与阈值不可通约性、四类协方差机制与数据分层架构、三个具体可证伪实证候选（98Mo弱E3跃迁、102Ru低能偶极聚集、135Pr负宇称带取向进动）及跨区物理迁移准则"
created_from: "父级派发第3.8节任务指令及98Mo、102Ru、135Pr原件核查与R3反演边界"
promotion_target: ""
evidence_sources: [lawrie-2020-tilted-precession-wobbling, frauendorf-2014-transverse-wobbling, nomura-2022-questioning-wobbling-ibfm, lv-2022-evidence-against-wobbling-135pr, matta-2015-transverse-wobbling-135pr, karmakar-2025-2026-98mo-octupole-preview, saracino-2026-102ru-scissors-octupole-resonances, ding-2025-chiral-rotation-a60-residual-interactions]
tags: [doctoral-thesis, section-3-8, joint-predictions, holdout-validation, falsification, research-program]
---

# 模式判断需要怎样的联合预言

## Research Trigger

能级序列、寿命和角关联记录不同侧面的核响应。把这些资料放在一起时，需要说明哪些量用于定参、哪些量提供新的检验，以及派生量共享了哪些输入。本页保存第3.8节在三个实核候选上形成的可复用方法。

## Grounded Evidence

| 原件 | 实际载荷与定位 | 解释边界 |
|---|---|---|
| [[karmakar-2025-2026-98mo-octupole-preview]] | PDF2反应；PDF4 Table1：603.1(2)、475.1(2)keV带内E2强度8.94(45)、9.89(25)；弱1833.3(5)、1585.8(6)keV强度0.24(9)、0.74(16)，DCO/偏振栏空白。PDF6 Table2给强度比及B3/B2。 | E3是相应端态允许的最低阶次，纯E3是作者提取强度比时的假定。全谱强度以787.2(3)keV线为100(3)，不能直接读作母态分支。 |
| [[saracino-2026-102ru-scissors-octupole-resonances]] | PDF3 Fig2图注确实列2953.2(19)keV；正文给B(E1)↑=0.016 e²fm²、E1聚集和约0.1 e²fm²、2–4MeV内M1和约1μN²。PDF5式(2)为内禀增强偶极算符；PDF6给E(2+)+E(3−)=2518keV。 | 2953.2(19)有原件依据，保留；未经支持的单声子末态精确能量不补写。孤立态二声子解释和5MeV强度聚集解释是不同模型问题。 |
| [[matta-2015-transverse-wobbling-135pr]]、[[lv-2022-evidence-against-wobbling-135pr]] | 前者报道135Pr横向摆动；后者PDF3 Table1/Fig2给747.3keV线δ=−0.47(+0.09/−0.22)等小根结果。 | 使用各自真正的PRL/PLB原件，不能把通用摆动学位论文或TPSM论文填成其raw身份。符号δ须保留作者相位和响应约定。 |
| [[lawrie-2020-tilted-precession-wobbling]] | SecIII/PDF5–6与canonical来源的LAW20-6/7，检验冻结准粒子下的取向近似。 | 与Lv2022放开准粒子方向的QTR不等同；一套QTR拟合不能凭名称证明某种模式。 |
| [[nomura-2022-questioning-wobbling-ibfm]] | PDF2显示134Ce用DD-PC1与可分离配对映射，其他指定核芯用D1M；比较软核与奇粒子耦合。 | 不是对所有核芯采用Gogny，亦不能仅因小混合比就唯一选定IBFM。 |
| [[frauendorf-2014-transverse-wobbling]]、[[ding-2025-chiral-rotation-a60-residual-interactions]] | 具体PRM组态、惯量与残余力下的取向计算，分别作为模型预言和A≈60迁移例子。 | 不把其特定条件提升为跨全部核素的数值阈值。 |

## Provisional Reasoning

同母态跃迁的部分光子率要先核归一口径。若给总支路概率（含内转换），
\[
\lambda_{\gamma i}=\frac{b_{{\rm tot},i}}{\tau(1+\alpha_i)};
\qquad b_{\gamma i}\text{若已是光子概率，则}\quad
\lambda_{\gamma i}=b_{\gamma i}/\tau.
\]
相对光子强度须在同一母态的全部出口上归一；其他出口的权重必须与强度处于同一任意刻度。未知分支只能保留界限或参数，不能因为写了一个求和符号就当作已测。固定能量、混合和分支后B随1/τ缩放，但多个B共享同一τ，不能计作独立寿命证据。

98Mo原表的比值是
\[
I_{1833.3}/I_{603.1}=(2.68\pm1.01)\times10^{-2},\qquad
I_{1585.8}/I_{475.1}=(7.48\pm1.62)\times10^{-2}.
\]
对应作者纯E3条件下的B3/B2为66.05(27.01)与153.81(33.31)fm²。寿命可以通过同母态较强支路研究；DSAM/RDM灵敏度须结合反冲速度、慢化、分辨和馈入判断，不设统一皮秒或速度阈值。低绝对B3且低B2会排除预言该支路增强的具体实现，不排除一切八极关联；强B3也须再区分动态关联和稳定形变。

102Ru的0+→1−单光子吸收是E1，1+剪刀通道是M1。作者内禀式rY1+bνr³Y3不是通用实验室秩1恒等式；旋转协变展开可含[Q2⊗O3]1型项，其系数仍依模型。理想二声子1−→3−的B2可以具集体大小而光子分支很弱，因为率须同时含辐射常数、能量幂与ICC。不能只比较不同单位的E⁵、E³就声称固定倍数压低。

135Pr比较的是相同可观测量在具体模型中的预言。Frauendorf的冻结顺排、Lawrie的冻结准粒子TiP对照、Lv的动态QTR和Nomura的IBFM内部参数不必逐项对应。给出可比较的输入约束与误差后，绝对寿命、完整分支和角关联/偏振联合解才可对其作区分。

## Assumptions

- 用于率反演的τ描述声明条件下的固定初态，分支和转换系数的归一相容。
- 多极混合的单位、发射振幅相位与几何系数分别声明；SI单位本身不能决定δ符号。
- GLS点估计和概率推断有各自的矩条件或分布假定；已约束分支的残差须位于允许子空间，协方差不能直接按满秩求逆。

## Competing Explanations

98Mo的大B3/B2可来自分子增强或分母受阻。102Ru的孤立1−与强度聚集不能因同为E1就视为同一构型。135Pr的小混合比约束电磁幅度，但不能只凭这一量唯一识别取向机制。

## Transfer Conditions

迁移时比较费米面轨道、配对、惯量和局部曲率、组态混合及反应布居。相似的γ参数或质量区名称不足以保证同一模式；缺少文献报道也不证明首次发现。

## Failure Conditions

错误的原件身份、全谱Iγ当母态分支、光子概率再除ICC、只改正文而留旧台账，都会破坏这一链条。固定百分比或一条拟合曲线不能替代指定模型在未用于定参数据上的检验。

## Falsification or Reverse Tests

先写下具体组态与输入范围内可区分的率、分支或相关响应，再将全部输入误差传播到预测。若不相容，只排除该实现及其条件范围；有限未见线给上限。新增测量还须核实与旧资料的采集依赖。

## Open Questions

弱E3分支的多极混合和绝对寿命、102Ru二声子末态分支、低自旋取向模型在共同输入约束下的差别仍是研究问题。本页没有提供新实验结果或一套已定机时的可行性证明。

## Human Review

无新增真实用户人工审核事件；以上为Agent原件与条件复核，不冒称human-reviewed。

## Promotion or Rejection History

- G91返修后，父审修正仍残留的假母态百分比、假带内线与错raw身份；2953.2(19)keV已重新核Fig2，保留。
- 与LaTeX3.8、证据台账和Python图同步；原输入仅留在任务审计快照，不作为事实源。
