---
type: research-note
title: "98Mo与100Ru：消去共同E2分母的同母态E1/E3约束"
aliases: [98Mo 100Ru denominator-free E1 E3, same-parent dipole octupole ratio]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [karmakar-2025-2026-98mo-octupole-preview, karmakar-2023-2024-100ru-alternate-parity-bands, book-bohr-mottelson-nuclear-structure]
created_from: "20261107 nuclear-structure continuation; published-branch analysis"
promotion_target:
tags: [98mo, 100ru, octupole, e1, e3, branching-ratio, covariance, conditional-model]
---

# 同母态E1/E3比：分母消除后还剩下什么信息？

## Research Trigger

[[karmakar-2025-2026-98mo-octupole-preview]]的Tables 2–3分别列
`B(E3)/B(E2)`和`B(E1)/B(E2)`。两者共享E2分母，不能将它们的增强简单计为两条
独立证据。不过，同一母态的两比值之商消去E2，提供一个无需寿命的额外结构约束。
本页首次在本任务中重建这一量；不是来源作者已经完成的E1/E3拟合。

## Grounded Evidence

| 证据 | 来源与实际locator | 实际范围 | 限制 |
|---|---|---|---|
| 98Mo母态2620.4 keV、5−的1110.8-keV E1及1833.3-keV E3，光子强度10.33(55)、0.24(9) | [[karmakar-2025-2026-98mo-octupole-preview]]，PDF4 Table1 | 同母态两支；E2为603.1 keV | 弱E3无直接DCO/偏振 |
| 98Mo母态3095.4 keV、7−的752.4-keV E1及1585.8-keV E3，光子强度8.52(40)、0.74(16) | 同上，PDF4 Table1 | 同母态两支；E2为475.1 keV | 强度误差只含统计/拟合，另报约4%效率系统误差 |
| 100Ru两母态的E1/E2、E3/E2光子比及能量 | 同上，PDF6 Table2、PDF7 Table3 | 采用本文重印的Ru数据；E3列含`×10^-2` | 不是又一次独立Ru实验；两比值的共同分母协方差未给 |
| 电多极光子率、向下B的初态归一 | [[book-bohr-mottelson-nuclear-structure]]，PDF401/printed382，Eqs3C-16–17 | 总控回读原页并检查公式图像 | 本分析采用通式及现代ℏc，不将书中舍入常数当额外数据 |

Ru预印本[[karmakar-2023-2024-100ru-alternate-parity-bands]]的PDF13 TableII
可复核5−、7−的E1/E2比；其7−母态写2951.7 keV，Mo文重印2951.9 keV。
本分析保留重印表版本，未把此小差异当新能级，也未把另一个9−态混入。

## Provisional Reasoning

记效率等已按来源处理后的同母态光子强度为`I1,I3`，则

\[
 S_i\equiv\frac{B(E1;i\to f_1)}{B(E3;i\to f_3)}
 =\frac{I_1}{I_3}
   \frac{2}{3675(\hbar c)^4}
   \frac{E_3^7}{E_1^3}.
\]

能量以MeV代入，`ℏc=197.3269804 MeV fm`，系数为
`3.5894406075×10^-13 fm^-4 MeV^-4`；最终`S`为`fm^-4`。
这里系数的MeV负四次与后方能量四次相消。光子率比消去母态寿命、总支路归一和
共同E2强度。直接输入光子强度时不再乘`1+α`；若使用总转换支路，必须先还原光子部分。
式中假定来源的纯E1/E3指认，多极混合会改变这一解释。

| 核素、母态 | 本任务由光子输入重建的S，fm^-4 | 同文印刷B比之商，fm^-4 | 读数来源 |
|---|---:|---:|---|
| 98Mo，5− | 7.84590×10^-10 | 7.82740×10^-10 | Table1原始强度 |
| 98Mo，7− | 2.44696×10^-10 | 2.44457×10^-10 | Table1原始强度 |
| 100Ru，5− | 1.50222×10^-9 | 1.50086×10^-9 | Tables2–3重印光子比 |
| 100Ru，7− | 2.34798×10^-9 | 2.33433×10^-9 | Tables2–3重印光子比 |

两种重建最大差异约0.59%，保留为舍入/表列重建差异，不反过来修改原表。
98Mo的`S7/S5=0.31188`，100Ru为`1.56300`。因此，按这些名义表值，
两核低自旋E1相对E3的演化方向不同；这项差别不能仅由共同E2分母的变动造成。
它没有告诉我们绝对E1下降还是绝对E3上升，更没有确定静态八极形状。

## Assumptions

若`x=I1/I2`、`y=I3/I2`，一阶传播为

\[
 \operatorname{Var}(\ln S)
 =\operatorname{Var}(\ln x)+\operatorname{Var}(\ln y)
 -2\operatorname{Cov}(\ln x,\ln y).
\]

共同E2的误差项在使用原始联合强度时会相消。仅有两个边际误差时不能恢复
`Cov(x,y)`，也不能把两列强度比当独立测量。计算包保留`ρ=-1,0,.5,1`
四种明确标注的传播场景；这些不是恢复出的实验协方差或置信区间。
98Mo直接`I1/I3`仍可能有共同归一、效率斜率、门和峰拟合的相关性。
没有原始计数/响应模型，弱E3强度也不保证Gaussian似然；本页不给显著性或排他结论。

## Conditional Rotational Control

只作为声明了假设的对照，若两带均可用轴对称`K=0`强耦合映射，定义内禀振幅
`tλ=⟨intr|M(Eλ,0)|intr⟩`，则

\[
 U_i=S_i
 \frac{\langle I0,30\mid I-3,0\rangle^2}
      {\langle I0,10\mid I-1,0\rangle^2}
 =|t_1/t_3|^2.
\]

这是对照中共享、与自旋无关的两内禀振幅假设；不是对真实5−/7−组态的指认。
5−与7−的CG平方比分别为`10/21`和`75/143`。所得`U7/U5`
在Mo为`.34350`，Ru为`1.72149`，名义值均不等于1。
所以单靠角动量几何并不能使这些表值自动满足常量内禀比。
未指定K、形状混合和可靠联合误差时，不能据此拒绝真实核的转子族或八极相关。

## Competing Explanations

- 同母态E1/E3变化可来自质子—中子偶极极化、E3关联、不同末态重叠及组态混合；
  E1、E3响应同一个β3也不意味着两算符的矩阵元有固定比例。
- 5−的四极—八极两声子成分是来源提出的可能解释，不能先当作确定输入。
- 多极指认、弱峰本底或效率相关性变化也可能影响重建量；应以谱学和响应检验。
- 仅改变E2、同时固定所比较E1/E3强度的解释，不能改变S；它仍可能描述另一项
  单独的`B(E1)/B(E2)`变化。本分析并未排除一般带交叉或组态重排。

## Transfer Conditions

这一分母消除方法可迁移到其它质量区，条件是同一母态有已映射的E1、E3光子支路，
效率/门关系和多极混合可控。它不依赖某个质量区必定具备特定形状。
若E1/E3来自不同母态或不同未关联的实验归一，寿命和归一消除不成立。

反向检查包括：一般辐射通式与闭式系数一致、四组数据各五种任意E2尺度下不变、
四个CG平方与独立SymPy计算相符、与印刷B比之商比对、输入原件哈希核对和
独立目录重放JSON/CSV字节相同。这些验证公式和实现，没有补齐缺失的实验协方差。

## Open Questions

下一项高信息量证据是同态绝对寿命/支路，或能以共同波函数与E1、E2、E3有效算符
同时预测上述四组支路的模型。仅增加E1/E2点而不保留联合强度，不能关闭这一缺口。
9−没有同态E3约束时，不将本页低自旋趋势外推为高自旋结论。

程序`system/scripts/e1_e3_same_parent_constraints.py`，固定输入、结果与验证在
`outputs/l4/20261107-e1-e3-denominator-free/`。长期科学结论以本页及所列source为入口，
运行文件只保存计算证据。

## Self-audit and Promotion History

本页是基于发表表值的条件L4分析；没有新测量、绝对矩阵元或完整竞争模型拟合。
Codex自主核查，不是human-reviewed。保留E3指认、协方差和K映射的开放边界；
不将本页晋升为静态八极结论。


## Failure Conditions

若原件/态映射/算符规范改变、或必要响应未恢复，重新计算并收窄结论；不得以缺失伴随信号代替有灵敏度的排除。


## Falsification or Reverse Tests

闭式系数/CG、20项E2尺度控制、错误哈希拒绝与字节重放。 本页没有未执行的真实核模型排他认证。


## Human Review

本任务未发生用户逐项审核；记录的是Agent原件自审，未伪装human-reviewed。审核标注不作为检索或使用资格门。


## Promotion or Rejection History

本批根据直接原件与独立核查修订worker草案，撤回无源数值/普适断言；本页保持provisional。具体触发证据和仍存边界见正文，不以结构检查替代物理核验。
