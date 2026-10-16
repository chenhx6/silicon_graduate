---
type: research-note
title: "135Pr 连接线混合比分支的观测量与标定输入合同"
aliases: [135Pr mixing branch input contract]
created: 2026-10-17
updated: 2026-10-17
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [matta-2015-transverse-wobbling-135pr, lv-2022-evidence-against-wobbling-135pr, herzan-2015-193bi-spectroscopy]
created_from: Day15 daily-learning uncredited Day16 preview
promotion_target: 135pr-wobbling-controversy
tags: [135pr, mixing-ratio, polarization, calibration, covariance, provisional]
---

# 135Pr：先对齐观测量，再比较混合比分支

## Research Trigger

同一 747/813-keV 连接线在不同论文中有大、小模混合比。需要分清符号约定、角分布的候选分支、独立实验，以及 count asymmetry 与物理偏振的不同归一化。本页是方法准备，不裁决 wobbling 或 tilted precession。

## Grounded Evidence

- [[matta-2015-transverse-wobbling-135pr]] M15-4/5/16：PRL Table I 的 mixing ratios 与 INGA 不对称度 A；角分布来自另一场 Gammasphere acquisition。
- [[lv-2022-evidence-against-wobbling-135pr]] L22-4/14/16/17/18/19：新 JUROGAM II 的 P、Rac、Ap、逐门污染控制及误差定义；旧角分布曲线的再分析与新实验分开。
- [[herzan-2015-193bi-spectroscopy]] HE15-10：Lv SI Ref.6 采用的 Q(E) 标定，PDF10 Fig.4 及 Qpoint 公式。它是标定依赖，不能另算一场 135Pr 实验。

## 逐线观测量和数据身份

以下能量按各原表保留。747.0/747.3 与 812.8/813.2 的对应由相同连接关系及 Ji→Jf 建立，不要求两次实验的舍入能量完全相等。

| 来源与线 | Ji→Jf | 角度量/混合比 | 表列 A 或 Ap | 表列 P |
| --- | --- | --- | --- | --- |
| Matta 747.0 | 17/2−→15/2− | δ=−1.24(13)，angular distribution | .047(12) | 未列 |
| Lv 747.3 | 17/2−→15/2− | Rac=.37(4)，δ=−.47(+.09/−.22) | .006(+.012/−.019) | .04(+.08/−.13) |
| Matta 812.8 | 21/2−→19/2− | δ=−1.54(9)，angular distribution | .054(34) | 未列 |
| Lv 813.2 | 21/2−→19/2− | Rac=.48(6)，δ=−.37(+.10/−.14) | −.004(+.007/−.016) | −.03(+.05/−.12) |
| Lv 450.2 | 19/2−→17/2− | Rac=.49(4)，δ=−.31(+.10/−.13) | −.017(+.022/−.023) | −.07(+.09/−.10) |

Matta 的 A 不能直接与 Lv 主文的 P 比较；先需要各自 Q(E)、分析轴、门和背景。Lv SI 的 Ap 与主文 P 来自相同事件，不是互相独立的两次偏振测量。三条 Lv 的 P 字面误差区间均跨零；这不抹去其联合 P–Rac 分析，也不支持只用一个符号作分支判决。

Lv 747、813、450 偏振门分别为 450、796、747 keV；最后一项采用窄门排除邻近 449-keV 污染。813 的 660 门受 663-keV 污染，原文只保留 796 门；不能用更多受污染门补统计。SI p4 一处把 551 线的 band 标签写作 4→3，而同文纲图/Table1 把 550.9 线列在 band5，故门的可用性与 band 标签要分别保存。本页不据此重新指认能级。

Rac 的待测线位于两个不同角组，同一 all-detector 轴开门：

$$R_{ac}=\frac{I_\gamma(157.6^\circ+133.6^\circ;\ {\rm all\!-\!angle\ gate})}
{I_\gamma(75.5^\circ+104.5^\circ;\ {\rm same\ gate})}.$$

它不是 KF89 的门角/待测角交换单元之比。全角门不自动证明在任意 cuts、self-exclusion 或有限 joint response 下完全独立于门性质。SI 的 stretched dipole≈.8、quadrupole≈1.4 属于本文标定；mixed transitions 的 .37/.48 不能据这两个阈值直接改成 pure multipoles。

## Provisional Reasoning

### 独立标定闭合了 Ap 与 P 的中央值

Lv SI Eq.2 给

$$A_p=\frac{a(E)N_\perp-N_\parallel}{a(E)N_\perp+N_\parallel},
\qquad P=A_p/Q(E),\qquad
a(E)=.9844+2\times10^{-5}E_{\rm keV}.$$

其 Q 采用 Herzáň Fig.4，而 a 采用 Lv 自己的系数：

$$Q(E)=\frac{1+x}{1+x+x^2}\,[.42-1.9\times10^{-4}E_{\rm keV}],
\qquad x=\frac{E_\gamma}{m_ec^2}.$$

本次复算声明 me c²=510.998950 keV；不是恢复原文精确常数集。这个能量范围位于原 Q 标定图内。由原件系数得：

| Eγ/keV | a_Lv | Q_adopted | Ap/Q | 主文 P |
| --- | ---: | ---: | ---: | ---: |
| 747.3 | .999346 | .148787 | .040326 | .04 |
| 813.2 | 1.000664 | .134271 | −.029791 | −.03 |
| 450.2 | .993404 | .236763 | −.071802 | −.07 |

把 SI 的 Ap 上下误差各除中央 Q，三组 P 误差也与主文末位舍入相容。这只核数据身份，不能由相容性证明作者包含或遗漏了任何系统误差。不能把 A/P 中央商当作独立测得的 Q，尤其 P 的区间跨零时。

### 共享校准的条件敏感性，不是实验总误差

对固定真实计数比 r=Nparallel/Nperp，

$$A=(a-r)/(a+r),\quad
\frac{\partial P}{\partial a}=\frac{1-A^2}{2aQ},\quad
\frac{\partial P}{\partial p_0}=-\frac{P}{p_0+p_1E}.$$

对斜率参数的导数分别再乘 E。它们给多线共享校准的低秩协方差 GΣcalGᵀ，不能将每条线的同一标定误差独立抽样。

原文给 a0、a1、p0、p1 的边际误差尺度，按此顺序为 .0021、1×10⁻5 keV⁻1、.04、7×10⁻5 keV⁻1，没有 joint calibration covariance。本任务只为敏感性选定模型：把这些尺度暂作 std，分别让两组截距/斜率相关系数取 −1、0、+1，a 与 Q 两组 cross covariance 指定为零；能量与计数比固定。后一个零不是实验事实。

| 线 | 截距/斜率各不相关模型的 σP,cal | 相关系数网格下范围 |
| --- | ---: | ---: |
| 747 | .027795 | .018155–.034864 |
| 813 | .032214 | .022527–.039599 |
| 450 | .015198 | .005420–.020798 |

这些数是条件校准敏感性，未加 count/background、P–Rac 共享事件或几何迁移项；不能作为新的 P 测量、置信区间或从主文误差中扣除的“系统部分”。原始计数未得，以舍入 Ap 反推的 r 只是代数 proxy。

固定该 proxy，要使 A 的中央值归零，a 的相对变动为 −1.1928%、+.8032%、+3.4588%（按 747/813/450 顺序）。这不是校准错误指控，也不替代已跨零的源误差。实际换门还会改变 r 与条件密度，不能只改 a。

### 大、小模差异不是符号约定

在 M1/E2 两分量截断下，radiative E2 fraction 为 δ²/(1+δ²)。KS/RB 符号改写不改变它；裸 RME 与含能量归一的振幅比仍须按 [[multipole-mixing-ratio]] 核对。

| 线 | Matta 已选 δ 的 E2 中央份额/字面端点像 | Lv 已选 δ 的 E2 中央份额/字面端点像 |
| --- | --- | --- |
| 747 | .6059；[.5520,.6524] | .1809；[.1262,.3225] |
| 813 | .7034；[.6777,.7265] | .1204；[.0679,.2064] |

端点像来自原表各自的 δ±误差直接变换，没有共同置信水平，不能据两列不相交报告显著性。它们说明原表已选分支的模不同，不能仅靠换号消除。份额不是绝对 B(E2)、总核态分支或一场独立寿命实验。

Lv Fig.2 还把旧 Matta 角分布的小模再分析标为 −.64/−.5；这与 Lv 新数据的 −.47/−.37 是不同输入身份，不能合并成同一个“反方 δ”或重复计为独立实验。后续支持方的旧数据 χ² 重析另由 [[135pr-wobbling-controversy]] 导航，本页未复算其 raw likelihood。

## Competing Explanations

- 大、小模分支可能受 alignment、feeding、背景、有限接受和校准处理影响；只读已发表点和图不能定位差异原因。
- 正偏振并非所有混合跃迁均为大模分支，具体 P–Rac 曲线与 σ/I 约束仍须匹配实际选择。SI p4 称 sigma 为 variance，但未在该段给 Gaussian 指数式；不能自动当成 D96 的 std。
- 新 JUROGAM acquisition 独立于旧 Gammasphere/INGA；其旧曲线重析、主文、SI 及采用的 Q 校准具有依赖关系。独立采集不等于所有理论与标定假设独立。

## Assumptions

只用原文舍入 summaries 和显式采用的 Q；M1/E2 fraction 采用两分量辐射模型。没有重新积分实际 clover 接受，也没有将仅整数 spin 验证过的计算核用于 135Pr 半整数路径。

## Knowledge Impact and Lifecycle

判断为 supports 既有争议保留，limits 直接比较 A/P、用 phase 解释模差异或把校准当独立证据；新增的是可复算的逐量合同及 Q 采用链，不形成 collective-mode 裁决。

[脚本](../../system/scripts/day16_pr135_branch_calibration.py)、[冻结输入](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-pr135-branch-calibration-input.json)、[结果](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-pr135-branch-calibration.json) 保存 hash、全部端点与校准相关模型；可复用公式、数据表和边界已在本页。

## Transfer Conditions

可迁移的是先保存 observable identity、response adoption、shared events 和完整 nuisance covariance 的流程。本文数值只适用于这些原表与声明的条件敏感性，不是任意阵列的校准参数。

## Failure Conditions

若实际 cuts/阈值/geometry 不支持 Q 的迁移、原 raw background 或 count ratio 不同，当前复算不能预测真实 P。完整 calibration cross covariance 改变时，网格范围也不能当通用上下界。

## Falsification or Reverse Tests

取得逐 gate/角组的净峰与 sidebands、polarimetric Nparallel/Nperp、a/Q fit covariance、同事件 P–Rac covariance，并保存σ的明确定义。按共同响应比较两分支的完整 profile likelihood，再用独立寿命/转换或匹配参考作 companion。另一次同 counts 的比值变形不能增加独立信息。

## Open Questions

Matta 后续完整分析或学位论文是否给出可重放的角分布输入、INGA Q 和逐门计数？ M15-17现保存DataCite登记候选DOI [10.7274/sj13902283h](https://doi.org/10.7274/sj13902283h)，题名为Exotic Nuclear Excitations: The Transverse Wobbling Mode in 135Pr；registry仅Text、无file URL，机构正文未取得，不能宣称已核对PhD全文。Lv 的 calibration/error budget 是否有未列出的 joint covariance？这些输入将决定能否从合同进入实验重析；目前未取得，L4 not-ready。

## Human Review

本页为 Codex self-audit，review_status 为 unreviewed。原 Matta/Lv source 页的人审仅保留旧 claim 范围，不自动覆盖本页或新来源行。

## Promotion or Rejection History

2026-10-17：Day15 窗口内的 Day16 无学分预习创建；source 原件/标定闭合和条件敏感性已检查。完整 response/Σ 未得，保留 provisional，不给 Day16 正式学分或实验模式结论。
