---
type: source
title: "GOSIA2012手册与公开SIGMA：不变量归一、误差近似及实现边界"
title_original: "GOSIA User Manual for Simulation and Analysis of Coulomb Excitation Experiments"
aliases: [GOSIA 2012 manual, SIGMA invariants implementation]
created: 2026-10-23
updated: 2026-10-23
status: ai-draft
review_status: unreviewed
source_type: technical-manual-and-program-source
reading_depth: skimmed
authors: [D. Cline, T. Czosnyka, A.B. Hayes, P. Napiorkowski, N. Warr, C.Y. Wu]
year: 2012
citation_key: ""
canonical_source: "https://www.pas.rochester.edu/~cline/Gosia/downloads.html"
source_url: "https://www.pas.rochester.edu/~cline/Gosia/Gosia_Manual_20120510.pdf"
raw_file: "raw/papers/day20-20261022/gosia-user-manual-20120510.pdf"
raw_sha256: "8258219d56fe5a7ced3a761ab3b07388089cd30e46adcde72f4a1c0c1f6cc633"
raw_storage_status: reserved-unpopulated-official-public-staging-only
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
