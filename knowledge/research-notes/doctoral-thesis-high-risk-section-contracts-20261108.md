---
type: research-note
title: "博士论文设计：六个易误写环节的原件与推导合同"
aliases: [doctoral thesis high risk section contracts]
created: 2026-11-08
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "R1–R3原件/纠错形成的总控写作设计"
promotion_target: ""
evidence_sources: [bohr-1952-surface-particle-coupling, bohr-mottelson-1953-collective-individual-original, cline-1986-nuclear-shapes-coulomb-excitation, poves-2020-limits-assigning-nuclear-shape, matsuzaki-2004-nuclear-inertia-and-wobbling, wu-hongyi-2020-general-purpose-digital-daq-thesis, liu-chen-2016-78br-chirality-reflection-symmetry-thesis]
tags: [doctoral-thesis, section-contract, conventions, evidence, pedagogy]
---

# 不让熟悉的名词掩盖论证缺口

## Research Trigger

本页将第一阶段纠正过的高风险环节变成具体写作合同，
与[[doctoral-thesis-argument-and-writer-contract-20261108]]的通用模板配套。
F编号是设计模块，尚不是已选定的正式章号；不依赖worker架构投票。
它们是结构/来源合同，不是六段论文正文。

## Grounded Evidence

每个合同按已有source定位原文；writer起草前须核实际文件、版本与locator。
source旧文字若有“deferred”等历史归档描述，应以实际原件/哈希重新判断可用性，
不能直接承袭相互矛盾的摘要；也不自动扩大阅读范围。
R3数学控制可用作明确标注的教学控制，不伪装为真实核数据。

## Provisional Reasoning

### F01：有限原子核为何仍有形状

- **读者问题：** 实验室0⁺四极矩为零，形变模型为何仍有用？
- **先修：** 旋转不变Hamiltonian、I与M、标量/张量；先给物理图像再引入Wigner–Eckart约定。
- **原件：** [[bohr-1952-surface-particle-coupling]] pp.9–13,19–21；
  [[cline-1986-nuclear-shapes-coulomb-excitation]] PDF16–18/印刷698–700；
  [[poves-2020-limits-assigning-nuclear-shape]]实际v2 PDF2–6, Eqs.(3)–(17), Table I。
- **必须推导：** 一阶实验室矩的角动量条件，二/三阶标量网络，
  以及正权测度下“矩比不等于无权平均角”的一个声明条件反例。
  不直接从q₂/q₃写出完整概率分布。
- **公式合同：** 坐标电四极、有效电荷算符与物质四极分别命名；
  明确q₂/q₃归一、单位、初态统计权和截断。
  图4等旧印刷歧义不可自动修为另一论文公式。
  按R1/T03声明的可交换电四极坐标/张量归一，
  \(q_2=\langle Q^2\rangle\)、\(q_3=\langle Q^3\cos3\gamma\rangle\)，
  q₃本身已是三次不变量，不能又写成q₃³；电荷情形单位分别为e²fm⁴、e³fm⁶。
  \(q_3/q_2^{3/2}\)不是一般无权平均cos3γ；能否将它解释为实有效角还需检查范围/假设。
  任意截断有效算符不自动满足同一坐标恒等式。
- **图规格：** 自有概念图并列实验室对称密度和有效内禀分布；
  另用已声明控制模型展示同低阶矩可有不同分布，标“教学模型”。
- **比较/反方：** Ni、Kr与Hg可显示离散混合、连续涨落和有限网络，
  不以其中一种语言排除全部其它模型。大q₂或超过Weisskopf参考值
  不普遍排除球振动，也不证明刚性；CoulEx约束矩阵元网络，不直接给完整电荷密度。
- **叙事边界：** 可以用“长时间曝光留下圆影”帮助理解平均，
  必须说明它是认知类比，单个量子态不等同于一只不断转动的经典椭球。
- **读者检查：** 0⁺的Qs=0为什么不能独证刚性球？增加哪一类矩阵元才可能缩小解释空间？

### F02：壳占据、配对与惯量怎样进入集体动力学

- **读者问题：** 两个形状接近的核/组态，为什么可以转得不一样？
- **先修：** 平均场/费米面、占据与配对的区别，广义坐标和动能量纲。
- **原件：** [[bohr-mottelson-1953-collective-individual-original]] pp.12–25,90,94–95；
  [[doctoral-r1-g28-otsuka-2023-type-ii-shell-evolution]]独立文章PDF7–8,13,17–19；
  [[matsuzaki-2004-nuclear-inertia-and-wobbling]] PDF3–8及R2中响应定义；
  其它惯量来源按[[doctoral-r2-collective-inertia-response-crosswalk-20261108]]逐式回源。
- **必须推导：** 从 \(T=\frac12B_{\mu\nu}\dot q^\mu\dot q^\nu\)
  到所选坐标下的Hamiltonian/测度，明确B与吸收β因子的D不是同一记号。
  先解释IB与残余响应的物理差异，再在需要处给TV/QRPA形式。
- **公式合同：** 固定j=J/ħ及频率/能量记号、求和双计数、
  A±B实/虚方向和空间/配对NG合同。
  Hinohara源内因子疑点以边界呈现，不从不一致原式编造整齐教材定理。
- **历史图规格：** 1953 Table XXIII只重绘已核行，标历史采用量与条件β映射，
  同时说明Q几何映射与B都可能贡献偏差；不是现代TV数值验证。
- **比较/反方：** Zr占据反馈、Se/Kr局域响应和Lu横向响应作用不同，
  相近PES并不固定所有动力学；配对减弱也不保证理想刚体。
- **读者检查：** E(2⁺)先约束什么？由惯量再读β额外用了什么假设？
  沿带J(2)为何不自动等于摆动的有效横向惯量？

### F03：模式的标签、稳定性和混合

- **读者问题：** γ振动、摆动、进动和手征何时真的有不同预言？
- **先修：** 体轴/实验室轴、Iπ、K、signature、旋转参考系及小振幅。
- **原件：** [[book-bohr-mottelson-nuclear-structure-vol2]]印刷190–193；
  [[matsuzaki-2004-nuclear-inertia-and-wobbling]] PDF2–8；
  [[kvasil-2006-dy156-yb162-crpa-wobbling]]实际v1 PDF1–4,16；
  手征原作/模型按R3量子标签note回链。
- **必须推导：** 有单位约定的纯转子高自旋频率，
  两种不同轴对称极限及冻结内禀K粒子转子与纯转子的区别；
  同标签的两态模型说明“允许”与V/能差决定的实际混合强度。
- **公式合同：** D₂只在声明的标量模型空间使用；
  \(C=TR_y(\pi)\)的反幺正相位不能照搬宇称±；
  y为所声明的轴，不普遍就是实际转轴。signature仅在相应Hamiltonian保留该π转动时使用，
  不给所有手征/TAC伴带强行加同一signature。
  能量交错指标S(I)按各论文原定义，不生成通用混合公式。
  转动系伪模不是另一条可观察核带。
- **图规格：** R3完整有限I矩阵控制可展示非等间距，但不能先命名三态为实核0/1/2声子。
  实核波函数/节点图须来自对应模型，不能拿概念陀螺画法当证据。
- **比较/反方：** 130Ba、163Lu与178W为不同输入合同，
  指出普通组态带、软核芯耦合和带交叉如何竞争；不设普适γ=30°或δ门。
- **读者检查：** 固定惯量为何不保证有限I完整谱精确简谐？
  同π/signature为什么既不强迫混合，也不能排除混合？

### F04：由电子学和谱学反演绝对电磁强度

- **读者问题：** 一个γ峰面积和一条寿命，经过哪些选择才能变成B(E2)？
- **先修：** 信号/触发、列表事件、概率和联合分布，发射振幅与率的区别。
- **原件：** [[wu-hongyi-2020-general-purpose-digital-daq-thesis]]
  PDF53–56、104–109、127–128；
  [[lange-kumar-hamilton-1982-multipole-admixtures]]印刷121–122；
  [[campaign-g07-gorgen-2004-163lu-quadrupole-moments]] PDF2–4, Tables I–II。
- **必须推导：** 共同busy的联合接受度反例，δ的二次有理多根，
  \(\lambda_{\gamma i}=b_i/[\tau(1+\alpha_i)]\)中的总分支定义，
  光子分支的另一归一，以及上下行B的统计因子。
- **公式合同：** Γ=ħλ，τ与半衰期区分；δ为有相位约定的光子振幅比，
  混合ICC与分多极率一致；同母态τ消去与跨母态Cov不同。
  J V Jᵀ是局部误差近似，遇多根/边界保留完整似然。
- **实用率系数的原件校验：** Suhonen实际PDF133–135/印刷118–120，
  Eqs.(6.1)–(6.4),(6.12)–(6.14)；Eq.(6.13)只是列常数，
  不是分支/ICC公式。用原文印出的圆整数代入Eq.(6.14)的λ=2，
  \(C_{E2}=5.498\times10^{22}[3/(2\cdot15^2)]/197.33^5
  \simeq1.2250\times10^9\)；
  若E以MeV、B以e²fm⁴计，\(\lambda_\gamma(E2)=C_{E2}E^5B(E2)\)，单位s⁻¹。
  因而对声明的M1+E2支路，
  \(B(E2)=b_i\delta^2/[\tau(1+\alpha_i)(1+\delta^2)C_{E2}E^5]\)。
  这是以圆整数重建的教学换算，不报为新精密常数；使用该率系数后没有额外ħ或ln2。
  原书本处不展开IC，分支/ICC关系另按率定义及对应谱学来源推导。
- **图规格：** 信号→事件→选择→响应→RME的自有链图；
  逐环标哪些已校准/拟合/采用输入。未知用户模块参数留空。
- **比较/反方：** DSAM/RDDS与CoulEx各增加不同信息，
  但都有feeding/响应/采用输入；不将任何方法写成无模型绝对真值。
- **读者检查：** 为什么单道live相乘可能错？总b与归一光子a混用会怎样改变部分寿命？
  同母态τ消去后，δ、ICC、效率、gate/本底及其相关误差为何还可能存在？
  具体应用还需实际能级身份、谱、τ、分支、feeding/接受度与Cov等，
  不能声称只补效率曲线和阻止本领就能完成所有反演。

### F05：反射对称性、八极与手征的证据层级

- **读者问题：** 看见E1连接与近简并四条带，距离联立破缺的判断还有多远？
- **先修：** 空间宇称、有效偶极/八极算符、有限体系恢复、各条带的态身份。
- **原件：** [[liu-chen-2016-78br-chirality-reflection-symmetry-thesis]]
  PDF78–82和90；[[xiao-xiao-2019-high-spin-74as-thesis]] PDF43–49；
  有效E1见[[continuation-g15-effective-e1-origin-20261107]]、
  [[continuation-t02-ru102-covariant-effective-e1-20261107]]的原作与条件推导。
- **必须推导：** 非正交的宇称投影能量含重叠S；
  E3振幅/强度和E1质中极化/质心修正分开；
  转子D0抽取的分支、混合、多极、K与几何假设。
- **公式合同：** Δl/Δj有利组合不保证真实强八极；
  rank-1/rank-3网络分别记录；强E1、强E3、八极软性与稳定内禀形状不是同一陈述。
- **图规格：** 每条实验E1连接画在真实两条带之间，标未测绝对量和缺连接；
  不为构造漂亮四重带示意而补画原件未报告的线。
- **比较/反方：** A80 Br/As、A100 Mo/Ru与A130相应组态，
  对齐实际费米轨道/有效算符/自旋区间；模型极小与测得形变区别。
- **读者检查：** 78Br论文展望和其已报告的关联有何区别？
  同时拟合谱和E1参数为什么不是两次独立检验？

### F06：异能态与弱/反应探针的共同输入和不同过程

- **读者问题：** 哪些结构信息能跨电磁、弱衰变、热环境和形成反应复用，哪些不能？
- **先修：** 多极率、seniority/K、完整/有限空间、通道分支与级联。
- **原件：** Jain Ch.3–6；Suhonen印刷541–543；
  Zhi2013 PDF2–4；IAEA2021 PDF4–11,21,24,84–85；
  Gintautas2009 PDF2–5；Zagrebaev2001 PDF1,6–7；Xu2004 PDF3–4。
- **必须推导：** 单j同v一体E2节点的条件；
  单体Ikeda的Pauli代数；至少一次γ/n级联说明feeding非最终Pn；
  成对详细平衡与开放网络不同，以及ER三阶段的分波和量纲。
- **公式合同：** 未知LEC不先求解，0ν明确轻Majorana机制和闭合/短程条件；
  P1n、P≥1n、平均中子数、β条件归一与母态总归一分开；
  总/部分寿命、光学厚度/耗散概率、冷态稳定/产额分开。
- **图规格：** 同一假设组态可输入若干前向计算的关系图，
  明示相互作用/有效算符/环境/反应响应的独立假设，不能画成“一条B测出全部参数”。
- **比较/反方：** 核钟/NEEC作环境选择的专题框，
  深入材料/原子计算若与中央论证无直接关系可放附录，不能由此宣称未学。
- **读者检查：** “寿命长所以好合成”“Ikeda满足所以已知有限Q窗”
  “γ喂到Sn以上就发中子”各错在哪里？

## Assumptions

本页从已核知识选定必须解释的环节，不要求每节机械使用相同篇幅。
具体标题、章号与正文分配等待样本/架构比较；个人成果接口未知。

## Competing Explanations

过度分节也可能打断论证，所以这六份合同可以合并或作为跨章回链，
不能为保留每个合同而制造重复的教材章节。

## Transfer Conditions

每个合同均可成为Gemini的独立窄任务；
writer起草前必须填真实输出范围与原件，不能默认本文件授权修改所有章节。

## Failure Conditions

用正文名词替代必要推导、按旧稿目录机械套合同、将样本结果写成用户结果、
或把缺数据改成默认数字，均不得进入后续正文。

## Falsification or Reverse Tests

总控将对每节的科学论证、读者先修和反方逐项检查；
未完成的章节合同不能以生成了大量文本视为完成。

## Open Questions

哪种正式结构能用最少的重复容纳这些必要推理环节？
样本已有的优秀解释应怎样转成写作方法，而非复制其文本？

## Human Review

总控的写作设计建议，不是读者效果实测或用户新确认记录。

## Promotion or Rejection History

- 2026-11-08：建立六份原件/推导合同，等待正式章节选择后映射和补全。
