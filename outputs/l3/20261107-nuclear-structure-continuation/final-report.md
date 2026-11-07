# 六区核结构续接研究报告

本批继承`knowledge/projects/isomer-six-region-transfer-research.md`。
研究状态仍为active-L3，并交付有边界的L4分析；不代表全库、所有六区问题或作者模型均已完成。

## 模型、API与执行范围

本批派发12个Gemini Flash Tiered/high worker和1个Terra/xhigh worker。
Gemini承担原件获取、精读、表格抽取、解析代码和独立复核；Terra承担有效E1协变/识别性推导。
G20、G21另按具体错误返工。工具接受所指定路由；未声称改动主会话实际模型/effort，
也未把用户报告的可用token余额当作实测用量。

总控实际认证调用WoS机构Starter、Scopus、OpenAlex、Springer Meta、Springer OA，
五项请求均成功；这不等于所有候选相关或拥有所有全文权限。
关键全文沿官方/已配置合法通道取得。邮箱只用于API识别；未向人发送消息，凭据未写入交付物。
Scopus数字60命中136Nd、Springer命中材料学等词面假阳性已按题名排除；
API返回条数不计学习或证据数量。

## 改变研究判断的增量

| 问题 | 本批所得 | 长期知识入口 | 仍有边界 |
|---|---|---|---|
| 102Ru SI缺失 | 五页SI、106行TableI、六项相互作用形式 | [[continuation-g14-ru102-si-thesis-20261107]] | 作者实现、事件/响应及完整Cov未公开 |
| 102Ru强度误差优先级 | 可重放全表解析、预定窗口与留一线敏感性 | [[ru102-si-strength-concentration-20261107]] | 5080.93keV单行约占窗口名义E1一半；不是删除该线或独立误差认证 |
| 有效E1原始推导 | 1989五页、1993十一页原件；受限协变构造及更一般补全 | [[continuation-g15-effective-e1-origin-20261107]]、[[continuation-t02-ru102-covariant-effective-e1-20261107]] | 不是恢复作者生产QRPA、参数唯一性或严格退化 |
| 软核与费米面 | Chen2026二十一页全文、TR/WJ与两个占据代表值 | [[continuation-g16-soft-core-wobbling-20261107]] | 所选模型的四情景不是跨区禁戒定理 |
| 98Mo绝对量与相对量 | 同态评价/实验查核、消去E2的E1/E3比较 | [[continuation-g17-mo98-absolute-constraints-20261107]]、[[mo98-ru100-same-parent-e1-e3-constraints-20261107]] | 同母态绝对寿命/完整支路和联合误差仍缺 |
| Ir/Os模型 | 1979原始rawtext与2006全文XML的模型范围 | [[continuation-g18-ir-os-common-model-20261107]] | PES/低能带EM不自动给高自旋全部多极分支 |
| Cd/In弱率 | 新原件、母态归一与40行表修订、GT/FF合同 | [[continuation-g19-cd-in-common-weak-operator-20261107]] | 相互作用、质量版、FF实现与实验Cov不能混用 |
| 学位论文及跨区关联 | 78Br/74As定向原件回读；124Cs与131Ba原件 | [[continuation-g20-thesis-e1-d0-contract-20261107]]、[[continuation-g21-a80-a130-parity-chiral-transfer-20261107]] | E1不等于直接E3、非零D0或静态手征/宇称序参量 |
| A160绝对基准 | Görgen2004四页全文和15个态寿命/Qt | [[continuation-g23-lu163-absolute-quadrupole-20261107]] | 支路/δ沿用旧测量，Qt映射有K分布假设，阻止本领系统误差未计入 |

三篇主综合及project/index同步更新；可复用事实和合同已在knowledge，
本报告及运行文件不构成第二知识库。

## 定量研究与验证合同

1. `outputs/l4/20261107-e1-e3-denominator-free/`：固定实际光子输入，
   重建四个同母态E1/E3比。98Mo的S7/S5=.31188，100Ru为1.56300，
   说明名义差别不能仅来自共同E2分母；没有联合误差，不给显著性/静态形状结论。
   条件K0映射另列，不把它当真实态指认。原件哈希、闭式系数、CG及20个E2尺度控制、
   独立目录字节重放和错误哈希拒绝均有实际回执。附PDF/SVG/PNG，图中连线只引导阅读。
2. `outputs/l4/20261107-ru102-si-strength-audit/`：原件逐行解析与G14原报字段核验、
   缺失误差null、括号标签保留，预定能窗及留一线的名义和/质心敏感性。
   独立误差平方和仅是声明场景，不是恢复Cov；不拟合b/κ，也不把106行视为独立。
3. `outputs/l4/20261107-ru102-effective-e1/`：六个CG符号/有理数平方精确核查，
   条件轴向最低阶比b±1/b0=√(2/3)，更一般背景可实现共同b。
   是推导与角向核查，不是新核谱或模拟实验。

## 原件、纠错与下一步

原始PDF/XML保留本地；未覆盖用户原件、PLAN、私有凭据、既有get-paper或课程/调度。
新来源/集合均有raw哈希/清单；部分worker手填UTC偏移已由父核验伴随manifest限定，
原清单保留。原始worker长草稿存于ignored tmp，公开过程报告与receipt按最终canonical校准。
关键纠错含Hagemann耦合指数100倍、把未报告算符写0、无源Pn/GT损失、
同态归一与上限错配、D0公式与能级身份、轨道rank1/rank3条件及普适阈值。

下一步优先作者复响应/输入空间、102Ru关键分支、98Mo同态绝对量、两方向EM网络，
以及冻结相互作用/算符后对未拟合分支的预测。Saracino博士正文仍未取得；
连接超时不证明embargo或全球无镜像。不重复已闭合的seniority或角向toy。

本批沿用20261107任务目录。会话上下文日期已到2026-11-08，而执行环境UTC时钟仍报告
2026-11-07；运行时间按实际时钟读取，日期差和旧手填时间均不隐藏为精确获取时刻。

## 检查与发布

检查统计、归档范围、数值重放、检索刷新、显式文件范围及实际Git结果见本目录validation、
lint-delta和本地publication-final-receipt.local.json。稳定发布指针为
`main / research: reconstruct dipole operators and cross-region constraints`；
精确hash只保存在发布回执。本段由实际检查/发布结果在收尾核对，不把旧全库问题称为本批全绿。

最终检查：14个source、11份manifest归档通过；preflight通过。全库lint为129 errors/446 warnings，
相对129/435基线新增error0，新增warning11均为未核书目key。数值重放、原件hash保护和文本检索通过。
新增11source+12note，共34个知识页有本批增量；本报告不把全库遗留错误说成全绿。
