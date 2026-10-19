---
type: research-note
title: "207Pb偏振参考：交换门角色与小E5振幅的条件影响"
aliases: [Pb207 gated polarization reference, Bi207 conditional Stokes]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: daily-learning-Day17-official-reference-analysis
evidence_sources: [nndc-2011-pb207-bi207-polarization-reference, garnsworthy-2019-griffin-facility]
promotion_target: ""
tags: [polarization, reference, gamma-gamma-correlation, mixing-ratio, covariance]
---

# 207Pb双光子参考的门角色与混合振幅

## Research Trigger

[[garnsworthy-2019-griffin-facility]] GF19-10的Fig20以同一207Pb级联展示1064 M4(+E5)和570 E2两种目标角色。[[nndc-2011-pb207-bi207-polarization-reference]] N207-2/3给实际13/2+→5/2−→1/2−序列、上支MR+.02(.01)、下支E2而MR空栏。新问题是这些实际输入在何种条件下能给参考P；不能把两角色只当作换γ能量，也不能把E5强度份额当P的误差界。

## Grounded Evidence

- N207-2：1063.656从1633.358/13/2+到569.6988/5/2−，M4+E5；+.02(.01)为评价字段，1976primary正文/phase未得（N207-11）。
- N207-3：569.6988的5/2−→1/2−标E2但MR空；本页采用pureE2是声明模型，非测得δ=0。
- GF19-10：Fig20a为1064散射/570门，b为570散射/1064门；原图a在ξ0附近负、b正，公式A=.5QPcos2ξ（GF19-6）。这里只作图形正负核对，不从图重拟δ/Q。
- GF19-7：cloverpair90°对应crystal Θ约68–113°，不是一个已知均匀角接受。

## Assumptions

初态ρ=I14/14；下支pureE2；gate的光子偏振与最终核磁子态完全求迹，忽略hyperfine/deorientation、反冲和材料响应。δ_native定义为当前CG/Jones算符中E5/M4的实振幅比；native核含(−1)^L，RB核去此因子并取δ_RB=−δ_native。未从评价正号直接识别实验nativephase；±.01/.02/.03和±.12是条件输入，非新的CI/原primaryfit。

本页P_plane=(I_plane−I_normal)/(I_plane+I_normal)，轴由target与gate方向构成的平面定义。Q_J是光子Stokes分量，**不是**polarimeter Q。I=(4π)²倍双光子方向概率，满足½∫I dx=1；不是探测符合效率。x=cosΘ，Θ为两γ夹角。

## Provisional Reasoning

### 交换门角色不能只交换能量

纯M4/E2极限给

\[
I(x)=\frac{505+228x^2-45x^4}{572}
=1+\frac{221}{1001}P_2(x)-\frac{18}{1001}P_4(x).
\]

\[
P_{1064}(x)=\frac{-60(1-x^2)(2-x^2)}{505+228x^2-45x^4},\quad
P_{570}(x)=\frac{(1-x^2)(45x^2+183)}{505+228x^2-45x^4}.
\]

在90°，P1064=−24/101≈−.23762376，P570=183/505≈.36237624。同一I不意味着同一P；这与Co60 pureE2的角色相等是不同序列，不能迁用1/6。Fig20两曲线的正负与此条件极限相符，不认证实际幅度/response。

### 小E5强度不约束P到同等精度

下表均为本任务模型；±号表示未完成primaryphase桥接前两个native选择，不能读成评价的双测量或实验置信区间。

| δ_native | P1064(90°) | P570(90°) |
| --- | --- | --- |
| 0 | −.2376237624 | .3623762376 |
| +.02 | −.2501487272 | .3742040184 |
| −.02 | −.2252215439 | .3501181518 |

E5强度δ²/(1+δ²)在|δ|=.02时约.00039984；P1064相对pure的幅度变化约±5.2%，P570约±3.3%。来源是振幅干涉的一阶项，不把它写成实测Q系统误差。只有另假定实际m=.5Q_true Pδ、其它response完全相同且分析硬用P0，才有Q_apparent/Q_true=Pδ/P0；原作者采用的phase、mixedP、角平均与fit没有从本模型恢复。

完整δ的I/Q_J有理式保存在结果artifact；I的独立rank展开为

\[
a_2=\frac{221+78\sqrt{22}\,d-198d^2}{1001(1+d^2)},\quad
 a_4=\frac{2(220d^2-54\sqrt{22}\,d-27)}{3003(1+d^2)}.
\]

这里d就是声明的δ_native；不能把旧1977A2或+.12输入当独立phase验证/新拟合。

### 角接受与共同坐标的边界

仅作**均匀cosΘ设计**、区间68–113°时，pure的∫Q_J/∫I为−.21602989/.34123680（1064/570），与point90不同；这不是GRIFFIN实际平均P。固定native+.02时为−.22710990/.35252739，−.02时为−.20502089/.32950826。真实逐台geometry/efficiency/Comptonselection/平面角迁移未知，不能据此把这些值乘paperQ或重标Fig19。

固定pure且只讨论此角域内非负方向权重，P1064的点值范围约[−.237624,−.174322]、P570约[.298616,.362376]；它们是理想核的角域范围，不含实际detector harmonic response、lowerlevel扰动或其它系统误差。

把gate整个4π不分方向地去掉，在固定target实验室横轴求迹得到I=1、Q_J=U=V=0。局部eventplane的Q_J积分却一般非零；先对每event旋转到共同轴再加密度，与直接平均eventplane标量是两个不同对象。本次直接8×16球面积分与解析spin2方位积分均核该限制，不把无gate singles叫已偏振参考。

## Competing Explanations

- tinyE5fraction未使pointP变化到10⁻4级，直接否定“near-pure强度保证同精度P”的推断；没有否定源评价或原GRIFFIN分析。
- 交换角色保持I而改变P，故仅验证γγ角关联不足以验证polarimetry的target/gate桥接。
- 全gate共同轴Stokes为零反对把局部标量平均当无门偏振；有限角设计又反对直接把nominal90°迁成实际arrayP。

## Evidence Gaps

1976primaryphase/fitCov未得；lowerE2 purity不是独立测量零MR。实际source取向/扰动、门/晶体接受、background/fitΣ、historicalproducer与paper mixedP均未得。不能从本页重造P/Q/δ实验CI或指认source错误。

## Falsification or Reverse Tests

先取得matching原primaryphase及实际Θ/ξ接受或原event/response；把本页I/Q_J逐event前向折叠并保持共享calibration参数。若要检验门交换，需同时预测两角色和相同branch背景，不能各自自由重标Q消差。

## Reproducibility

- [来源前问题冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/pb207-stokes-before.md)与session/hash receipt先于计算。
- [合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/pb207-stokes-contract.json)核两个真实ENSDF原对象hash和固定helpers；旧Day16代码只复用已说明算符，不兑换本session卡信用。
- [新程序](../../system/scripts/day17_pb207_conditional_stokes.py)与[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/pb207-stokes-result.json)：新13/2→5/2→1/2对象、9个native参数×9个角×2角色；独立exactCG/阶乘d、3j/6j/9j F/F3和directsphere控制。
- `PYTHONPATH=/workspace/wiki/tmp/day16-jt74/python-deps python3 system/scripts/day17_pb207_conditional_stokes.py --contract outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/pb207-stokes-contract.json --output tmp/pb207-stokes-replay.json`。

## Links

[[polarimetry-shared-calibration-count-design]]、[[triumf-griffin-compton-source-calibration]]、[[compton-polarimetry]]、[[nndc-2011-pb207-bi207-polarization-reference]]、[[garnsworthy-2019-griffin-facility]]。

## Knowledge Impact and Learning Decision

`supports`原两角色expectedsign；`revises`只按能量替换referenceP或用强度纯度代偏振精度；`limits`nominalP90、角域平均及evaluationMR对真实Q的保证。模型与实验/作者解释分层，全新增needs_review，不提升humanreview。

## Open Questions

最有信息的新输入是原phase与matchingresponse/实际countΣ；重复当前参数网格不能补它。若无新输入，当前条件模型局部闭合，回到候选池和课程时间门。

## Promotion or Rejection History

L2解析/数值对象闭合、L3 reference设计边界已持久化；L4实验偏振重拟未ready。实际check数只对应声明条件，不认证历史producer或原数据。

## Transfer Conditions

仅迁移到同自旋/EM、同phase、同gate与target定义的理想photonkernel；真实应用须有matchingresponse和lowerlevel扰动条件。本页不以仪器同名或同γ能量作迁移条件。

## Failure Conditions

若下支存在未计混合/门对偏振不作完全trace、source非未取向、核扰动或实际plane迁移不同，当前闭式P不直接适用；不存在用一个Q任意修复所有不匹配的保证。

## Human Review

新增推导和sourceclaims全为needs_review/self-audit；没有设置human-reviewed或修改原claimflags。后续若用于论文级实测P/Q裁决，应按具体claim核phase/response与原数据，不把当前readiness缺口自动变成用户待办。
