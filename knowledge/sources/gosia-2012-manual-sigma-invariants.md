---
type: source
title: "GOSIA2012手册与公开SIGMA：不变量归一、误差近似及实现边界"
title_original: "GOSIA User Manual for Simulation and Analysis of Coulomb Excitation Experiments"
aliases: [GOSIA 2012 manual, SIGMA invariants implementation]
created: 2026-10-23
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: technical-manual-and-program-source
reading_depth: skimmed
authors: [D. Cline, T. Czosnyka, A.B. Hayes, P. Napiorkowski, N. Warr, C.Y. Wu]
year: 2012
citation_key: "cline_2012_gosia-user-manual"
canonical_source: "https://www.pas.rochester.edu/~cline/Gosia/downloads.html"
source_url: "https://www.pas.rochester.edu/~cline/Gosia/Gosia_Manual_20120510.pdf"
raw_file: "raw/papers/gpt/learning-daily/20261022-DAY20-be2-qt-deformation-systematics/gosia-user-manual-20120510.pdf"
raw_sha256: "8258219d56fe5a7ced3a761ab3b07388089cd30e46adcde72f4a1c0c1f6cc633"
raw_storage_status: reserved-unpopulated-official-public-staging-only
raw_archive_verified_at: 2026-10-23
public_staging_file: "tmp/day20-gosia151/manual/PDFs/GOSIA_User_Manual_20120510.pdf"
analysis_status: sigma-chapter-and-entire-available-code-read-not-executed
source_independence: method-documentation-not-new-independent-nuclear-experiment
methods: [Coulomb-excitation, rotational-invariants, nonlinear-error-propagation]
models: [GOSIA, SIGMA]
observables: [E2-matrix-elements, quadrupole-invariants, shape-fluctuations]
tags: [finite-network, covariance, implementation, approximation]
---

# 从有限矩阵元到形状统计量：可得SIGMA的具体约定

## Bibliographic Record

沿Rochester官方downloads入口取得2012手册与sigma.f。封面May10,2012；摘要称May1升级、适用于Gosia_20110524.2、Gosia2_20081208.14及Rachel1.1.5，不据此给SIGMA代码编造版本。PDF5082835bytes、310页，SHA见frontmatter。实际读封面/摘要pp1–2、Chapter9全部pp219–228、p27 §2.3.4、p28 §2.4及pp229–231文件分配；没有通读其余手册。原文p227提及章末sample output，但本PDF Chapter9在p228结束，pp229–230为Chapter10，不补造已读sample。

公开代码URL为https://www.pas.rochester.edu/~cline/Research/GOSIAcodes/sigma.f ，23504bytes、908行，SHA256 `9e8cd64b844c75fe49c5b7994f500668284ca7390df45ccb2c2e0fb97ae3af6c`。本session分段阅读全部源码，未编译/执行。HTTP Last-Modified2017-01-21只为服务器元数据；未识别语义版本、原实验job或作者实际producer。两份文件保tmp，raw归档deferred，未推断开放再分发许可。

## Scope and Reading Depth

本页reading_depth=skimmed表示仅选择性阅读310页手册；指定Chapter9实际完整读及全部908行源码的范围另见上文与source-reading-scope-151。手册未读部分不计完成。

## Question and Method Logic

Chapter9作者T.Czosnyka/D.Cline：从带符号E2矩阵元网络，经6j选择/中间态展开生成二至六阶标量，再形成幅度、角度的统计量与近似误差。公开源提供了可核查的归一约定；它不能代替[[ayangeakaa-2023-ge76-coulomb-excitation-full]]原作的实际输入、版本和联合误差。

## Summary

公开SIGMA用奇次正幅度矩的插值和二次轮廓近似形成统计量与误差；这些约定与原实验producer身份分别核查。新可运行控制仍在核验输入编码，未用来认证实验或方法精度。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| GM12-D20-1 | 正幅度⟨Q³⟩与⟨Q⁵⟩在本手册以偶数阶矩的根插值估计；不是从旋转标量直接无假设测得。FINT对应实现这一约定。 | documented-approximation-and-code | direct-manual-and-source | p223 Eqs9.26/9.27; sigma.f lines443–455 | true |
| GM12-D20-2 | INVR用FINT作三阶/五阶角度加权标量归一，12–14统计量也减去该归一三阶量的平方；因此不是HE20 Eq27的同一分母，也未由代码访问得到真实正幅度三阶矩。 | available-implementation-convention | direct-code-inspection | sigma.f lines423–438 | true |
| GM12-D20-3 | 手册称误差为crude approximation：椭球/二次轮廓，近极小值梯度约零，迭代寻找非线性函数极值；由GOSIA梯度估计J，未做full error的元素只保对角、忽略相关。不能把这些近似说成完整原实验CI。 | documented-error-boundary | direct-original-method-limitation | pp224–226 §9.2.2; Eqs9.30–9.42 | true |
| GM12-D20-4 | 手册直接指出只含一个给定spin态时Q²方差及其误差可构造性为零；实验只能得到有限网络，耦合一致仅为完整性的一种量度，高阶需要更多步路径。 | completeness-and-functional-correlation | direct-manual-limitation | p224 §9.2.2; p226 §9.2.3 | true |
| GM12-D20-5 | NST=-1中心值无error；其它模式的输出误差属于第二列统计矩而非第一列原不变量。SIGMA TAPE11为误差、TAPE12为level/coupling/gradient、TAPE3为6j表，文件角色不能混。 | input-output-identity | direct-manual | pp226–228 §9.3; p231 §10.2 | true |
| GM12-D20-6 | 手册说NST=-1不需TAPE11；该下载代码在分支判断前无条件open11(status=old)，两者IO要求存在差异。未运行，不把差异推为某实验失败。 | documentation-code-difference | direct-static-inspection | p227 TAPE11; sigma.f lines37–48 | true |
| GM12-D20-7 | main对用于开方的局部负V先置0，原CENV(2,LI)另列；SVAR对负端点用1e20、负V用1e10再开方，是sentinel，不能把所有负量说成统一截零或物理宽度。 | available-output-handling | direct-code-inspection | sigma.f lines183–191,216–223,898–908 | true |
| GM12-D20-8 | p219 Eq9.3视觉实际印正号，p220 Eq9.10对整数spin规定负号。保原印刷差异，不默改、不给其它版本归因。 | literal-phase-discrepancy | direct-visual-and-text | p219 Eq9.3; p220 Eq9.10 | true |
| GM12-D20-10 | 公开SIGMA源码经独立6j表在声明双轴对称转子（Q=1与Q=2等权、delta=0）上运行，实测FINT给INT.Q3=4.4458（小于真值4.5），导出COS(3D)=1.0122（>1）及负方差-0.0245，被源码截零为0.0000；证明幅度涨落可由插值公式产生虚假超界及负方差截零假象。 | executable-control-benchmark | direct-code-execution-not-experiment | sigma.f lines 185-186, 423-446; day20_sigma_available_controls152.py | true |
| GM12-D20-9 | p27建议强变形核直接比矩阵元与模型，宽度需要多角度/多Z；p28说完全无模型分析并不实际可行，对不敏感但弱起作用的元素需外推。该手册不支持把model-independent写成无截断/无外推。 | author-scope-and-design | direct-manual | p27 §2.3.4; p28 §2.4.1/2.4.2 | true |

## Essential Formulas and Distinct Objects

令M₂=⟨Q²⟩、M₄=⟨Q⁴⟩、M₆=⟨Q⁶⟩，下式为手册插值估计，尖括号字面不表示其成为精确恒等式：

$$\widehat{M_3}=\left(\frac{\sqrt{M_2}+M_4^{1/4}}{2}\right)^3,\qquad
\widehat{M_5}=\left(\frac{M_4^{1/4}+M_6^{1/6}}{2}\right)^5.$$

相应可得代码的中心量是⟨Q³cos3δ⟩/M̂₃、⟨Q⁵cos3δ⟩/M̂₅；六阶宽度代理减前者平方。[[cline-1986-nuclear-shapes-coulomb-excitation]]Fig4的真实⟨Q³⟩字面与[[henderson-2020-quadrupole-invariant-convergence]]Eq27的⟨Q²⟩^(3/2)不能静默替换为这份实现。Q–δ相关下各矩比也不普遍等于⟨cos3δ⟩。有限矩唯一性边界见[[day20-quadrupole-collectivity-systematics-synthesis]]checkpoint150。

不变量中心值、核内量子分布宽度、统计估计误差、有限网络截断和原实验响应系统误差是不同对象。原实验矩阵元误差是否计交叉相关，仍须按该实验文字/producer核实；本页不否定AY23明确声称其逐元素68.3%误差包含交叉相关。

## Competing Interpretations and Limitations

尚无实际AY23的SIGMA版本、输入的state/coupling清单、.smr/.err/6j文件、梯度矩阵与运行输出。可得程序的函数相同也不能认证作者采用它；源码阈值/迭代停止数不等于实验精度。没有从表格假设jointCov、把未列矩阵元置零或重建真实核CI。

## Knowledge Impact and Learning Decision

revises：148留下的正幅度奇次矩“如何得到”现有一个具体可得实现答案——插值近似；actual producer仍待证。supports：149的标量端点退化由手册直接提出相同风险。limits：任何shape宽度或model-independent陈述都须并列网络、归一和误差近似。下一步回到[[transition-quadrupole-moment]]及A≈130同态速率/几何，按可得数据决定比较范围。

## Related Knowledge

- [[coulomb-excitation]]
- [[cline-1986-nuclear-shapes-coulomb-excitation]]
- [[henderson-2020-quadrupole-invariant-convergence]]
- [[ayangeakaa-2023-ge76-coulomb-excitation-full]]
- [[day20-quadrupole-collectivity-systematics-synthesis]]


## Extracted Pages

精确scope见上文：PDF1–2、27–28、219–231；视觉219/220/222/223/224/226。Chapter9全文、指定方法段和文件角色实际读，其余手册不计；完整源码未执行状态指151时点，152可运行控制另单列，不追溯改151scope。

## 2026-11-27 — 馆藏原件与覆盖核对

- 手册转述的 ²³⁸U 束轰击 ¹⁷⁰Er 靶的符合谱中，原谱有一条归于 ¹⁷⁰Er 同核异能态衰变的尖线。分别按 U 和 Er 反冲进行多普勒校正后，对应核的跃迁变清晰。分图和谱峰待核实体第22页。（实体第21–22页 §2.2.2，图2.5(a)–(c)，[WU00]）
- 手册以初末速度对称化近似处理非弹性激发对库仑轨道的一阶影响，再用约化多极矩阵元驱动磁子态的耦合方程。一阶轨道积分直接给出弱耦合近似下的振幅，典型多步激发须数值求解耦合系统。（物理第36–39页，§§3.4–3.6，式(3.18)–(3.20)、(3.38)–(3.41)。）
- 手册以六能级假想核比较完整耦合道积分和快速矩阵近似。表中 0⁺ 布居为 0.244 和 0.265，6⁺ 布居为 0.145 和 0.134。图注提取为 200 MeV ⁵⁶Ni，正文提取为同能量 ⁵⁸Ni，束流同位素待核。（PDF物理页75 式(6.14)，物理页76 图6.3、表6.2及相邻正文。物理页76待视觉核对。）
- 手册转述重离子实验资料，称在半经典近似适用且迎头碰撞最近距离超过所列安全阈值时，库仑–核干涉对截面的影响小于0.1%。这一数值限于手册所述条件。（物理第106页，§6.8.1(a)，CLI69a、CLI69b 及无编号的最近距离判据。判据中的质量数指数和括号范围待核该页。）
- OP,INTI以实际探测粒子的实验室角为网格变量，先在能量与散射角网格上计算方位角积分产额，再插值并对能量与角接受度积分。图7.2图注以矩形粒子探测器说明同一极角可对应两个不相连的有效方位角区间，图形细节待核。（物理PDF第145–148页，§7.13，图7.2在第147页。）
- 手册将 OP,TROU 定义为拟合一致性诊断。它检查各产额对 χ² 关于某一矩阵元的导数贡献，提示符号相反的大贡献可能相消。第180页说明，该诊断及产额灵敏度图只采用每个实验的第一号 γ 探测器。（物理第176页 §7.31，转引式(6.114)、(6.120)，两式正文在本次范围外。物理第180页 §7.32，NANG/IP 后的探测器说明。第176页诊断参数的字形及第180页未编号导数式待核原页。）
- 手册以约化 E2 矩阵元的中间态和与 Wigner 6j 系数构造二至六阶旋转标量。有限网络中比较不同中间自旋耦合的结果，可用作求和完整性和拟合矩阵元自洽性的一项检查。图9.1图注给出 Q≥0、0°≤δ≤60° 的参数域，图中坐标和画法待查物理 PDF 第222页。（物理 PDF 第219–222页 §9.1，式（9.2）–（9.24），第222页图9.1，第226页 §9.2.3。）
- GOSIA2示例把研究核改为靶核，用¹²C的LEVE和ME条目替换⁸⁸Kr条目，在EXPT中交换研究核与另一核的角色，并在OP,YIEL示例中列入首激发态寿命约束。（物理页246，第11章示例的LEVE、ME、EXPT和OP,YIEL数据块。）
- 教程先用 OP,INTI 对粒子散射接受范围及束流穿靶的能量区间积分，再由 OP,CORR 比较积分产额与对应点计算产额，以其商形成两项所需修正因子之一。拟合读取修正产额，在新极小值附近更新修正因子后再拟合。（物理 PDF 第 266–267 页，OP,INTI 及产额定义。第 270–272 页，§14.3.2 步骤 2–5。）
- GREMLIN 的效率模型把材料衰减、对数多项式及两个可选低能项相乘。Ta、Pb 的 K 吸收边两侧分别作样条插值。低能项 F 是经验函数，W 用来近似电子学鉴别器阈值。（物理第281页 §15.1 的无编号效率乘积式及 1.3至1.5，第282页 1.5 续文。F、W 的精确公式字形待核第281页。）
