---
type: research-note
title: "奇Ba论文的新颖性重叠与贡献边界：限定原件核查"
aliases: [odd Ba novelty overlap audit]
created: 2026-11-06
updated: 2026-11-06
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [quadrupole-invariant-spin-channel-precedents, nomura-2017-odd-mass-gamma-soft-shape-transitions]
created_from: "用户授权的当前odd-Ba稿件实质新颖性核查；额度限制下partial收束"
promotion_target:
tags: [a130, ibfm, novelty, quadrupole-invariants, evidence-boundary]
---

# 奇Ba候选稿：直接先例、增量与停止边界

## Research Trigger

本次限定核查回答：已发表工作与当前固定电荷几何控制、固定算符Gamma路径分别重叠到什么程度。此前额度中断的partial记录仍保留在`outputs/l4/20261106-evidence-closure/novelty/partial-audit.md`，本页由恢复后的直接原件阅读更新。

**结论：一般原理已有明确先例。** 可保留的是针对指定全J+2诊断的有界控制和具体重分配量化，不是通道依赖、几何／动力学分离或不变量代数的新发现。当前证据支持把稿件作为增量型模型研究候选供作者评估，不构成优先权认证或“创新性已充分达到某期刊”的保证。

## Grounded Evidence

原件和哈希集合回链[[quadrupole-invariant-spin-channel-precedents]]。本次实际读取并定位：

| 原件 | 本次直接阅读范围 | 关键对象 |
|---|---|---|
| Nomura2016，arXiv1610.00469，本地15页 | PDF2–3、9–11 | Eq.8、Fig.8/10及弱／强耦合解释 |
| Rouoof2025，arXiv2502.18076，本地24页 | PDF2–3、12–13、16–17 | Sec.IV C、Figs11–14、conclusion2/7/8 |
| Lawrie–Orce2025，publisher PDF | PDF1–5 | Eqs5–15、Fig.1/3、转动条件和Gamma(gamma)关系 |

N16 PDF9的Eq.8、R25 PDF13的正文／图、L25 PDF3的Eqs5–13另做页面图像核对。文本抽取按双栏分开读取，避免将左右栏公式混并。页图只作本地阅读派生物；原始PDF没有改写，哈希与读取清单记录在`novelty/source-audit.json`。

## Provisional Reasoning

| ID | 直接先例及重叠 | 与当前控制的具体关系 | 可保留的贡献边界 |
|---|---|---|---|
| NOV-N16 | Eq.8平均最低五个向带头的B(E2)，分DeltaJ=1/2；PDF10直接把相反同位素趋势联系到弱／强耦合。 | 所核对象是向下二次强度平均与跨核带头系统学，不是当前同一J、严格固定电荷几何、全J+2三次proxy的干预比较。 | “通道指标随耦合改变”已属先例，不能作为本文独立新发现。 |
| NOV-R25 | Sec.IV C比较四带、I<=10的187元网络与实验对应子集；结论2报告截断可减小涨落；结论8讨论固定Nilsson gamma之上的组态混合。 | 固定平均场gamma不是电荷张量满足q2/q3点态恒等式。文中报告混合改变形状诊断／涨落，所核比较没有施加本文刚性电荷恒等式或同一全J+2 proxy。 | 网络覆盖及混合改变诊断的思想已有覆盖；有限模型中小q2变化不能被本文升级为固定几何证明。 |
| NOV-L25 | Eqs5–8独立使用电荷gamma与惯量混合参数Gamma；Eq.12的一个比值显式同时依赖两者；两元反演再使用Eq.11。 | 固定gamma仍可随动力学混合改变个别矩阵元比值，在原式中已经直接可见。其2+转动比值不是本文11/2初态的全15/2三次proxy，但不能据自旋／核素不同就宣称新原理。 | 几何与转动响应分离也已有先例。本文最多量化这个特定诊断及静态／有符号环的响应。 |

L25 Eq.12为
\[
R_{22/02}=-\sqrt{10/7}\,
\frac{\cos(\gamma-2\Gamma)}{\cos(\gamma+\Gamma)}.
\]
这里Gamma是广义转子的惯量不对称／混合参数，不是IBFM的Gamma0。作者的两元gamma换算使用Eq.11中Gamma与gamma的关系，并限定相关2+态具有转动性质；原文也讨论混合例外。因而不能把本文反例解释成否定该方法的声明适用域。

当前稿的两个具体计算承担不同作用：固定电荷张量的无配对控制给出q2=1、q3=.5，同时全48个15/2态的z从.32262到1.02625；IBFM固定算符路径分开静态、同J非弹性和有符号中间路径。这些量化比较可以形成候选增量，但完整环求和、旁观者极限和常规数值验证本身不是创新。

## Assumptions

本次只对三份最接近先例的上述段落作直接比较，不声称系统性穷尽所有文献。文中“所核对象不同”不等于证明其它文献从未给出相同控制。固定平均场参数、固定有效算符、固定完整矩及严格刚性电荷几何必须分别说明。

## Competing Explanations

候选稿可能被评价为已有知识的一项具体模型演示，其价值取决于量化机制是否帮助理解指定诊断，而非增加小数位、同位素数量或代码检查数量。固定形状反例没有认证真实Ba形状，异能态条件失败也没有证明所有IBFM错误。

## Transfer Conditions

采用“有界控制及定量分解”的贡献表述；不使用首次、通用新形状判据、作者原图纠错或已确认实际核形状的主张。主文应直接承认L25已有几何／惯量自由度的分离，N16/R25已有通道和网络依赖。

## Failure Conditions

若把三个所核来源中的对象差异作为充分优先权证明，或把通用原理重新包装成新理论，超出本次证据。若后续找到同一控制的直接先例，应进一步收紧为复核／应用，不能用换核素维持优先权主张。

## Falsification or Reverse Tests

核查保留可证伪的对照：同一固定J、严格固定电荷几何、改变耦合、全J+2谱态求和、相同proxy定义，以及静态／有符号路径干预。如果原始先例同时满足这些条件，候选增量会被直接覆盖。本次没有为证明“首次”扩大检索或增加模型计算。

## Open Questions

期刊和作者对该增量的价值判断仍需真实学术评估；不由内部核查自动决定。本次预定的三源对照已经完成，原全库阅读与全球优先权调查不纳入这次限定收尾。

## Human Review

没有新增真实用户科学审核事件。本页是直接原件阅读及稿件对照的Agent自审记录。

## Promotion or Rejection History

- 2026-11-06：额度中断时保存partial，未认证创新。
- 2026-11-06恢复后：完成预定三源原件对照，确认一般原理重叠；保留有界增量型模型候选定位，并明确不能无保留标记新颖性充分或期刊接收。
