---
type: project
title: "同核异能态与六区集体动力学：证据、机制迁移和研究队列"
aliases: [isomer六区研究, isomer-six-region-transfer, 跨核区新现象研究]
created: 2026-11-07
updated: 2026-11-08
status: active
review_status: unreviewed
research_status: active-L3
project_stage: L3-mechanism-transfer-with-bounded-L4
confidentiality: public
sources: [book-jain-nuclear-isomers, paper-dracoulis-2016-metastable-states-heavy-nuclei, liu-chen-2016-78br-chirality-reflection-symmetry-thesis, xiao-xiao-2019-high-spin-74as-thesis, hayes-2005-k-conservation-178hf, dracoulis-2013-192os-isomers-gamma-soft]
tags: [isomer, cross-region, triaxiality, octupole, hypothesis, l3, l4]
---

# 同核异能态与六区动力学研究

## Agent active summary

用户于2026-11-07指定摄入 `raw/papers/isomer/`，优先综述/学位论文，
并授权开放的L3/L4机制迁移研究。本轮建立51个PDF的逐文件台账，
重读相关学位论文并实质修订三篇主综合、条件化动力学综合及两个观测量入口。
研究是持续课题；本轮文献/模型里程碑不等于所有核区、整本专著或所有新现象均已研究完。

工作模型分工遵循用户偏好：Sol/xhigh总控、Gemini Flash Tiered/high主力，
Terra/xhigh处理复杂推导和精确数值；模型身份不替代来源与独立核验。
本项目不是daily-learning课程，不改变学分或调度。

## 当前续接：原始推导与共同观测合同

继续按Gemini主力推进。执行计划与调度记录为
`outputs/plans/20261107-nuclear-structure-continuation.md`及相应任务回执；
可复用科学内容以以下知识页和直接source为准。worker草稿须经原件核查，
返回状态或篇幅不代替实验独立性和推导正确性。

- [[continuation-g14-ru102-si-thesis-20261107]]与
  [[ru102-si-strength-concentration-20261107]]：已补5页SI、106行跃迁表和六项相互作用形式；
  保留BR、括号多极性、强度集中度与完整Cov/响应缺口。
- [[continuation-g15-effective-e1-origin-20261107]]、
  [[continuation-t02-ru102-covariant-effective-e1-20261107]]：取得1989/1993原有效E1文献，
  区分静态极化、QRPA态混合、有效顶角及旋转协变；最低阶轴向构造并不唯一。
- [[continuation-g16-soft-core-wobbling-20261107]]：Chen2026的21页正文将核芯软度
  与费米面位置一起比较；未扰动邻核芯近似不能直接裁决奇A核的真实动力学。
- [[mo98-ru100-same-parent-e1-e3-constraints-20261107]]与
  [[continuation-g17-mo98-absolute-constraints-20261107]]：相对E1/E3可消去E2分母，
  低自旋名义趋势不同；绝对寿命与可靠联合误差仍需同态输入。
- [[continuation-g18-ir-os-common-model-20261107]]：形状极小点、低能带EM比较
  与高自旋异能态多极分支预测分开；未报告矩阵元不等于算符为零。
- [[continuation-g19-cd-in-common-weak-operator-20261107]]：母态、Q窗、分支、GT/FF
  与相互作用/淬灭须按同一版本映射；近等寿命不唯一固定有效gA。
- [[continuation-g20-thesis-e1-d0-contract-20261107]]与
  [[continuation-g21-a80-a130-parity-chiral-transfer-20261107]]：学位论文E1/D0依赖及
  A130手征/八极关联案例，用于检验迁移条件而不是指定整区静态形状。
- [[continuation-g23-lu163-absolute-quadrupole-20261107]]：163Lu的4页DSAM原件补齐
  绝对E2基准；新寿命与旧分支/δ的依赖分别登记，Qt相近单独不是摆动证明。

当前科学问题仍active-L3，并含可重放的有界L4分析。Saracino博士全文未取得，
作者生产代码、理论复振幅与完整实验Cov也没有因SI出现就自动恢复。
下一阶段按同态绝对多极矩阵元、两方向支路及未拟合预测的信息增益选择，
不重复已有seniority或单轨道角向控制。

## 上一批规模化续接：新增正文、跨区问题与精确控制

用户补充Gemini可用额度并授权规模化研究；本轮实际派发13个Gemini/high任务与1个
Terra/xhigh任务，包含独立原件核查，按运行器容量分波推进。工作状态见执行回执，
不能把可用额度当必须消耗量，也不声称已启动后台常驻服务。

- 三篇用户正文均已核读：[[campaign-g01-mo98-fulltext-20261107]]、
  [[campaign-g02-ru102-fulltext-20261107]]、[[campaign-g03-ding60-fulltext-20261107]]。
  98Mo低自旋弱E3多极性指定与相对强度现在可定位；绝对E3/寿命仍缺。102Ru的
  有效算符和联合拟合参数已可核；本轮后续已补SI，完整Cov仍缺。Ding揭示能谱指纹与取向概率不同响应。
- 新的N=56实验参照：[[campaign-g13-zr96-revised-e3-20261107]]。
  已核Iskra2019报告向下42(3)W.u.，Mach1990的65(10)保持历史；不认证2026全部评价。
- 六区分支：[[campaign-g04-a60-a80-transfer-20261107]]、
  [[campaign-g05-a100-softness-octupole-20261107]]、
  [[campaign-g06-a130-wobbling-discrimination-20261107]]、
  [[campaign-g07-a160-tsd-kmix-20261107]]、
  [[campaign-g08-a190-shape-isomer-20261107]]。新增69Ga准集体、96Zr投影、105Pd N4
  反证、稀土RPA/TAC与Ir完整原件，均保留局部模型/采集谱系，未立整区禁戒。
- 弱衰变的具体检验：[[campaign-g09-shell-weak-isomer-20261107]]，以129Cd母态
  寿命/强度分布及In异能态质量，区分相空间、组态、禁戒算符与有效gA。
- [[campaign-t01-finite-system-symmetry-identifiability-20261107]]明确有限宇称态
  实验室<Q3>=0与内禀图像的区别，以及102Ru同一累计曲线拟合参数的依赖。
- [[octupole-orbital-eligibility-and-collectivity-boundary-20261107]]完成10轨道对、
  42磁投影的精确角向控制；旧πp1/2–g9/2作为单粒子E3驱动的指定因Δj=4撤回。
  不将角向允许性当实际集体性，模型结果不是真实核寿命。

### 下一轮按信息增益选择的研究合同

| 问题 | 已有输入 | 下一项可改变排序的证据 | 失败/转向条件 |
|---|---|---|---|
| 98Mo9−附近比值变化由E1还是E2驱动 | 新正文相对分支、E3/E2与E1/E2 | 同母态绝对寿命/完整分支，反射对称重排与八极模型共同预测 | 无绝对量与共同Hamiltonian时不造固定W.u.预言 |
| 102Ru八极极化与残余力能否区分 | 正文Eq2、5页SI与两篇原有效算符文献 | 完整Cov/复响应、模型空间匹配及未拟合E3/其它探针 | 不把拟合好或同曲线两参数自动称唯一/严格退化 |
| Ir/Os的瓶颈是否需形状/K混合 | Ir完整分支/PES、Os同母态率 | 共同算符的多分支预测和逐态响应 | 不以长寿命/低fν独立指定形状 |
| 组态依赖β率能否用共同gA描述 | 129Cd门选母态、In独立质量 | 实际Q/母态排序、未见feeding、允许/禁戒联合算符与留出分支 | 不用有限Q窗强度除裸Ikeda总和反推通用淬灭 |

这些是继续调查合同，不是已计算的新模式。Saracino2026博士论文
[[campaign-g12-saracino-2026-thesis]]仅取得真实题录，正文/目录仍未取得；
学位/期刊若共用数据，不算独立重复。经典综述与所给学位论文的既有阅读范围继续有效，
不以本轮论文数量声称整本馆藏或整个领域学习完毕。

## Evidence Available

### 资料身份与实际学习范围

本轮所给目录有51个PDF、692个物理页、49种PDF字节内容。
Taprogge2014两份和Dracoulis2016两份分别为相同字节；
Martin2016出版版与CHORUS稿是同一工作的不同版本。
Zhang2024频率比文件是同行评审记录，已另取原始论文，
不能把评审记录算成另一份实验。

登记、提取文本、阅读正文、核查公式/图表和事件级重放属于不同深度。
分组台账记录实际范围；Jain专著另有151物理页的分块阅读账，
重点代数与K章节、其它章节的阅读及未回查的转引实验分别保留。
该书目录以Summary结束，没有旧稿所称的附录，不用“全文提取”充当逐图/数据重放完成率。
原件访问和版本边界也保留到对应source。

| 主题 | 长期知识入口 | 本轮重点 |
|---|---|---|
| 综述/专著 | [[isomer-review-learning-and-transfer-20261107]] | 机制、seniority、K/形状陷阱、弱衰变与应用的来源层次 |
| 学位论文 | [[liu-chen-2016-78br-chirality-reflection-symmetry-thesis]]、[[xiao-xiao-2019-high-spin-74as-thesis]]、[[hayes-2005-k-conservation-178hf]] | 78Br的CPQ展望、74As的硕士论文身份/负宇称对、K混合发生在跃迁两端 |
| NEEC/耗散 | [[mo93-neec-evidence-and-depletion-transfer-20261107]] | 原始报告—评论/答复—隔离束上限；模型截面与实验率分开 |
| 核钟 | [[nuclear-clock-isomer-learning-and-transfer-20261107]] | 能隙/寿命/宿主、比频、锁定与不确定度分别记录 |
| 壳演化/天体/超重核 | [[isomer-shell-evolution-astrophysics-and-superheavy-transfer-20261107]] | 预测与观测、热化网络、稳定性与产额不同 |
| 六区原始比较 | [[six-region-primary-counterexamples-and-transfer-20261107]] | 对整区禁戒的反例；逐组态、有条件的迁移判断 |
| L4精确模型 | [[seniority-mid-shell-cross-region-model-test-20261107]] | 相消节点、非配对扰动及粒子—空穴对称性 |

过程台账与报告在 `outputs/l3/20261107-isomer-cross-region/`；
可复用结论以本页及下列综合/source为准。

## 2. 三篇主综合与模型共同输入

- [[triaxial-collective-evolution-across-mass-regions]]：六区组态、观测合同、
  迁移条件和未见/未覆盖/有反证的区别。
- [[octupole-and-chiral-coexistence-in-transitional-nuclei]]：78Br与74As原件、
  三带/四带、静态/动态、E1/M2与M1/E2及可检验耦合模型。
- [[high-spin-isomers-and-decay-modes-systematics]]：异能态机制、精确相消、
  Ikeda/gA、热化、超重级联和应用边界。
- [[universal-triaxial-collective-mechanics-and-cross-region-migration]]：
  正确的局部频率、恢复力、坐标/轴序与势垒；旧的“普适禁戒总律”已撤回。

## 3. 已完成的有界L4与认识修订

问题：半满壳E2相消是否在真实多费米子有限基中成立，
一个非配对但旋转不变的相互作用是否一定解除它？

j=11/2、n=2/4/6/8/10、v=2的10→8精确计算得到
B(n)/B(2)=1/0.25/0/0.25/1，半满值只剩数值舍入。
加入J=2对关联后，n=4/8强度变化，跟踪的n=6态之间仍相消；
共同粒子—空穴signature与E2变换性质解释了节点保护。
这改变“任何组态混合都恢复E2”的过宽假设。

代码为 `system/scripts/isomer_seniority_transfer_validation.py`；
完整模型、无量纲单位、源哈希、控制和剩余验证边界见研究笔记与L4回执。
它不是Sn、Ba或其它真实核的拟合、寿命预报或实际形状测量。
对应的g9/2偶粒子v=2链因n−v奇偶限制不能达到n=5精确半满，
说明跨区迁移必须检查壳简并度与允许的态。

## Current Hypotheses

### 第二轮已推进的证据与计算

- [[ru100-e1-moments-and-covariance-round2-20261107]]：六个有限点的转子条件换算可重放。
  直接绝对B(E1)路线不需Q0；共享寿命可在同母态D0/Q0比中消去，未知Cov不能变成完整显著性。
- [[os192-branch-rates-and-shape-identifiability-round2-20261107]]：同母态两E2的强度比约220，
  光子率比0.217、采用原表ICC的转换总率比0.806；大B比不是同倍数的衰变流或势垒测量。
- [[seniority-node-three-body-breaking-round2-20261107]]：归一纯三体标量解除先前受保护节点，
  B在小耦合以λ²起始。能量相空间的λ⁷代理只属于零基线能隙；
  加保PH两体项形成有限基线能隙后，同样的代理以λ²起始，均不是真实核寿命。
- [[sn136-seniority-anomaly-and-three-body-identifiability-round2-20261107]]：
  真实Sn的多轨道有效两体比较说明，单个非零中壳B不能唯一反演基本3N。
- [[mo98-e3-and-n56-octupole-evidence-round2-20261107]]与
  [[ru102-low-spin-dipole-and-high-spin-transfer-round2-20261107]]：
  补得学位研究会刊、96Zr原始E3及102Ru新摘要/作者网页，保持低/高自旋和E1/E3身份；
  该段为第二轮历史边界；后续已取得98Mo/102Ru正文及102Ru SI，完整Cov仍缺，见上方续接。
- [[light-and-rare-earth-orientation-window-round2-20261107]]追踪轻区残余力与稀土取向窗口，
  不从局部带的观测终点反推整核或全球实验上限。

### 后续候选与可推翻条件

### C1：N≈56三轴—八极耦合是否改变取向模式

**依据。** 本轮进一步取得100Ru的谱学预印本和后续寿命预印本，
见[[karmakar-2023-2024-100ru-alternate-parity-bands]]与
[[karmakar-2024-100ru-enhanced-e1-lifetimes]]。
后者实际6物理页，Table I列出6个有限寿命及相应B(E1)，另两高自旋态为有效寿命上限；
作者以增强E1和TPSM比较提出稳定八极形变的可能性，并要求进一步微观计算。
98Mo本轮已补出版正文，见[[campaign-g01-mo98-fulltext-20261107]]。78Br论文明确提出八极、γ软性与手征能否以不同组合共存的问题。
这些数据尚未提供奇粒子取向—八极耦合的完整定量L4输入。

**可检验假设。** 在指定组态中，八极混合改变高j成分与惯量响应，
使相同γ软性参照下的取向分布/带间强度发生可分辨变化。
κ的符号需由微观计算或多观测量约束，不能从E1强度直接决定。

**比较对象。** 98Mo与100Ru是N=56同中子素；应再比较相邻同位素、
奇A及奇奇组态。不能把两核同一作者的模型转述计成独立实验。
第二轮增加96Zr直接E3锚点；102Ru为N=58低自旋NRF的有边界比较，不是同一N=56组态的复测。

**反证与区分观测。** 若不含八极的共同输入模型已再现全部绝对矩阵元，
或所谓关键E1/E3线经偏振/寿命核对不支持增强，降低该解释。
下一步是已取得寿命表的共同输入/误差与feeding审计、98Mo全文、
E3及奇A/奇奇组态的取向计算；取得可靠输入后才选择具体L4。
全球新颖性与当前实验发现状态尚未穷尽检索。

### C2：A≈190异能态能否提供逐组态形状与混合探针

**依据。** 192Os六页原文中的10−、12+和20+及多分支；
Hayes的178Hf原文提示低K末/初态混合不应归给高K态自身。

**假设。** 同核不同组态的寿命与fν不必共变，
同母态多分支比单一总寿命更能区分低Eγ/高L瓶颈、K混合和形状变化。

**比较合同。** 190/192/194Os同位素与192Os/194Pt/196Hg的N=116同中子素
可比较顺排，但每态/分支须保持独立身份。
2013文献的预测态必须先查后续现状，不能直接命名为2026仍未发现。

**反证/下一步。** 恢复分支、ICC、寿命定义与共同算符后，若能量因子和已知组态
即可解释所有宽度，则不需要新增形状隧穿机制。
需要响应/门灵敏度时必须计算后才把未见线作为排除证据。
第二轮已恢复原表分支/ICC并验证同母态比值消去τ；下一步转为有共同输入的模型比较，
不把这份数据表当作已经具备的微观Hamiltonian。

### C3：轻区和稀土激发组态的取向窗口

**依据。** 60Ni有跨壳PRM手征候选，74Br有三带电磁数据；
163Lu的TSD是摆动基准，但166Ta某个轴对称输入模型不封闭全部激发组态。

**假设。** 模式窗口由特定组态的恢复力、取向分布、配对和可布居范围控制，
可在质量区之间迁移，而不是由A单独决定。

**失败条件。** 解冻准粒子后局部最低能取向消失、带终止先发生，
或其它组态模型更好解释绝对强度时，不保留该模式标签。
先作共同输入计算和现有搜索审计，不从一个三轴核直接指定所有邻核，
也不预设某装置的固定十倍灵敏度或反应产额。

### C4：异能态热化与应用入口

**依据。** 132Sn邻区壳演化/异能态原始论文、93mMo耗散控制和核钟新原件，
分别提供核能级、电子通道及时间尺度。

**问题。** 哪些异能态需在天体网络单独作为物种？哪种触发/探测机制可以迁移？
答案需完整中间能级、跃迁宽度、电子/光子谱、温度轨迹或实验输运/探测输入。
一条能隙不能决定冻结温度，截面增强因子不等于净耗散率或可用发电效率。
没有这些输入时留在L3，不生成固定丰度效应、事件数或显著性阈值。

## Next Actions

### 研究优先级、停止原因和恢复入口

本轮优先完成原件身份、主综合的强断言更正以及已有解析条件的精确检验。
四候选的反方比较见[[isomer-cross-region-hypothesis-discrimination-20261107]]。
继续路线按信息增益选择：C1补98Mo全文及Ru链的联合矩阵元/误差，C2比较共同算符的多分支预测与搜索现状，
C3先指定共同Hamiltonian，C4先有可重放的级联/热化输入。
不是按“至少再找多少篇”推进。

停止或转向条件：新来源重复同一采集、不能区分竞争模型、关键数据不可得，
或数值试验超出可靠输入。记录失败与缺口后继续其它有价值分支；
当前授权允许L3/L4，无需把普通研究选择转成用户待办。

P0：原件、SHA和数据身份的技术问题须隔离；科学候选、争议和未完问题不等于发布阻塞。
P1：学位论文/期刊依赖、模式与局域形状的过度解释、算符/单位、
真实未见信号的灵敏度、旧预测的现时发现状态，均需在具体claim使用时自主复核。

## Research Question

哪些异能态/集体动力学机制可以在六区迁移，哪些只在指定组态和近似下成立？
如何用原件、多观测量和有界数值检验区分新候选与既有解释？

## Risks and Blockers

98Mo正文已得，绝对E3/寿命、真实核多轨道/形变与级联输入仍不完整；
所有模型及部分读取来源保持对应边界。没有尚待用户批准的普通研究步骤，
技术归档/Git问题若出现须单独隔离。
