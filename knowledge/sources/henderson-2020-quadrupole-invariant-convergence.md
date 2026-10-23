---
type: source
title: "Henderson2020：四极不变量的有限矩阵元收敛与形状解释边界"
title_original: "Convergence of electric quadrupole rotational invariants from the nuclear shell model"
aliases: [Henderson quadrupole invariant convergence]
created: 2026-10-23
updated: 2026-10-23
status: ai-draft
review_status: unreviewed
source_type: theory-and-method
reading_depth: read
authors: ["J. Henderson"]
year: 2020
journal: Physical Review C
volume: "102"
pages: "054306"
doi: "10.1103/PhysRevC.102.054306"
arxiv: "2005.11210v4"
citation_key: ""
canonical_source: "https://doi.org/10.1103/PhysRevC.102.054306"
source_url: "https://arxiv.org/pdf/2005.11210v4"
raw_file: "raw/papers/day20-20261022/henderson-2020-quadrupole-invariant-convergence.pdf"
raw_sha256: "ed2d48f63e1e18a721e1bb3e01676ca91160d1a683d7447e574788a6f5c8e044"
raw_storage_status: reserved-unpopulated-arxiv-staging-only
raw_archive_verified_at: 2026-10-23
analysis_status: public-staging-original-read-raw-archive-verified
public_staging_file: "tmp/day20-henderson112/PDFs/Convergence_of_electric_quadrupole_rotational_invariants_from_the_nuclear_shell_model.pdf"
nuclei: [24Mg, 26Si, 28Si, 52Fe]
models: [shell-model, USDB, KB3G]
methods: [quadrupole-rotational-invariants, intermediate-state-expansion]
observables: [E2-matrix-element, quadrupole-invariant, quadrupole-softness]
tags: [shape, triaxiality, convergence, charge-matter, model-dependence]
---

# 有限强度网络与不变量收敛

## Bibliographic Record

J. Henderson，Physical Review C102，054306(2020)，DOI10.1103/PhysRevC.102.054306。本session取得并读取的是arXiv2005.11210v4，11页、1182893bytes，SHA256见frontmatter；没有核对publisher最终版逐字一致性。PDF首页同时打印“Dated: July 27, 2021”和边栏“15 Oct 2020”，Crossref精确DOI端点给发表2020-11-04；保留版本日期差异，不改成年份2021。

PDF在tmp公开staging；raw_file为未填的归档槽，raw/PLAN/Bib均未写，citation_key空白而不虚造Bib条目。SI沿本次auto配置关闭，不声称不存在。在112时Kumar1972与Cline1986均未得正文；148已新读[[cline-1986-nuclear-shapes-coulomb-excitation]]，PDF683–716核实；Kumar仍metadata-only，Ref1的转述不等于原读，Ref2打印681与已核Crossref683起页的字面差异也保留。

## Scope and Reading Depth

primed-recall-112在正文获取前冻结，已知题名/作者及旧不变量问题，非盲测。本session实际读PDF1–11全部正文、结论与参考文献；视觉核PDF2–10的Fig1–6、TableI/II与关键公式，阅读Eq1–36。scope112逐页留证。未运行NuShellX、未取得34核的全部矩阵元、未重建作者原采样程序；没有读完被引原文或重新做实验拟合。

## Paper Question and Scientific Motivation

PDF1摘要/Introduction：不变量原则上把实验室系E2张量约束连接到内禀形状，但实际只知道有限个矩阵元；作者用可算较多态的壳模型网络考察求和截断与软度收敛。问题是有限网络提供多少信息，而不是给所有核设统一的最少态数或实验精度门。

## Method and Design Logic

PDF5/7：NuShellX@MSU；sd用USDB及(eπ,eν)=(1.36,.45)，pf用KB3G及(1.5,.5)，另比较bare(1,0)。34核，每种相关spin算前40态；nI指每种spin纳入前nI态，不是总共nI个能级。把nI=40作为已收敛参考，依据是该处增态变化<1%及与Ref11的部分核比较；这仍是模型内参考而非完整物理Hilbert空间的证明。

## Key Evidence and Reasoning Chain

E2张量零耦合积 → 插入中间态，形成带6j和带符号矩阵元乘积的闭合环 → 逐步增加每spin的态数 → 与40态参考比较 → 用模型样本评估典型收敛。进一步把矩比转为角度/软度时又引入相关性、分布及形状解释假设。

## Summary

低阶不变量在此样本平均收敛较快，高阶软度需要更多信息；样本散布、有效电荷、有限价空间和混合都会影响判断。电荷形状δ不必等于物质形状γ；只有少量B(E2)或一个Qs不足以通用识别γ刚性。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| HE20-D20-1 | 定义内禀电荷E20=Qcosδ、E2±2=Qsinδ/√2；q2=√5⟨[E2×E2]0⟩，q3=−√(35/2)⟨{[E2×E2]2×E2}0⟩。Eq9/10的中间态展开含带符号的二/三矩阵元乘积和6j；不只是一组B(E2)模方。 | tensor-definition-and-closure | direct-original-equations-and-visual | PDF2–3 Eq3–10; Fig1 | true |
| HE20-D20-2 | Eq11用q3/q2^(3/2)定义cos3δ；仅保0₁、2₁时Eq12/13给q2≈B(0₁→2₁)及相应Qs比。PDF5在Eq27后明示角度/软度定义假设Q、δ无协方差；这项文字本身不能被扩写成任意涨落分布下的严格恒等式。 | angle-and-single-state-approximation | direct-original-with-explicit-boundary | PDF3 Eq11–13; PDF5 Eq27 and following paragraph | true |
| HE20-D20-3 | nominal charge样本在nI=4的q2平均偏差印为−9.4(+6.9/−3.4)%；bare样本印−15.6(+7.8/−5.4)%。作者报告低阶平均较快收敛但有散布，高阶softness较慢；这些是模型样本的打印偏差/散布，非实验CI或所有核的10%保证。 | model-ensemble-convergence | direct-model-table-and-visual | PDF6 TableI; PDF7 TableII; PDF10 Conclusions | true |
| HE20-D20-4 | 两个相近q2而不同δ的组态混合可与单一δ-soft结构在这些提取不变量上不可区分；相近δ而不同幅度的混合也可给宽Q2分布。作者用26Si/24Mg与52Fe讨论，没有提取A≈130真实混合角。 | author-competing-shape-interpretation | direct-author-discussion | PDF8 SecIIIB | true |
| HE20-D20-5 | bare电荷下镜像核的质子/中子形状可解耦，电荷δ与物质γ不必相同；β公式Eq1/32需电荷/物质分布关系。不能把电磁Q与某平均场mass deformation无条件同一。 | model-dependent-charge-matter-boundary | direct-model-discussion | PDF1 Eq1; PDF8 SecIIIA/Eq32; Figs2/3 | true |
| HE20-D20-6 | 有限价空间的结论明确是model dependent，即使sum-rule方法本身不依赖具体形状模型。更重核可能收敛较快是作者预期；当前分析实际限A≲70，不能把nI=4移植为Ce/Nd认证。 | methodology-transfer-limit | direct-author-limitation | PDF9 SecIIID/E/G | true |
| HE20-D20-7 | Eq34–36以高阶矩构造Q2与Q3cos3δ的Cov并以二元Gaussian采样。作者承认Fig6有不物理的abs(cos3δ)>1区域、需更完整协方差/物理边界参数化。此处是形状分布的模型表达，不是实验矩阵元测量误差Cov或事件CI。 | shape-moment-distribution-limit | direct-original-and-visual | PDF9 SecIIIF/Eq34–36; PDF10 Fig6 | true |

## Competing Interpretations and Limitations

不变量的张量学恒等、给定模型的有限态收敛、从矩到角度/软度的统计解释是三层不同主张。本文的模型结果不能认证Singh、Petrache或TDPAD的实验精度。完整强度求和与缺失环的符号仍须实测/模型合同；35核之类的样本数不得补造（本文是34）。

## Analytical Reconstruction

由HE20-D20-1作任务推断：改变单个态的整体相位会改变相连矩阵元符号但不改闭合环；仅给各B(E2)的模则不能一般确定环乘积。这不是本文原数据的phase提取，待以明示小型张量网络独立核验。

由HE20-D20-2作下一问题：q3/q2^(3/2)与无权平均cos3δ之间还涉及Q的高阶涨落。应检查即使Q、δ独立是否足够，不能把“无Cov”当未经检验的充分条件；本页尚未给出新数值反例或宣称原壳模型样本无效。

## Knowledge Impact and Learning Decision

limits：[[day20-quadrupole-collectivity-systematics-synthesis]]的单标量形状解释。supports：[[transition-quadrupole-moment]]中完整矩阵元/几何/分支合同的要求。把有限网络、charge/matter和混合/softness退化写入canonical笔记；不建立新的核素实验页，不恢复旧037/046–100认证，review保持unreviewed。

## Related Knowledge and Project Relations

- methodological-bridge：[[transition-quadrupole-moment]]，转移到形状不变量需扩大矩阵元网络。
- limits：[[day20-quadrupole-collectivity-systematics-synthesis]]，软度与组态混合非唯一解释。
- not-direct-evidence：[[singh-2016-lifetime-131ce-133pr]]、[[petrache-1998-highly-deformed-lifetimes-131ce-nd]]；不同核区/方法，不给实际Ce/Nd误差。

## Human Review Triage

按ingest-strategies的Agent self-audit定义；非用户审核事件。

P0: none identified；没有把本文模型图当原实验数据。P1：HE20-D20-2的矩比/相关性充分条件待独立推导；HE20-D20-3/6的平均收敛不可外推实验CI；HE20-D20-4的混合/软度解释需更多观测区分。证据及边界均在相应行。P2/P3：v4日期/Ref2页码与metadata的字面差异、raw deferred与索引维护。

## Extracted Pages

PDF1：摘要、引言与Eq1；2：Fig1/张量与Eq2–8；3：6j展开/近似与Eq9–20；4：Fig2/Eq21–23；5：Eq24–31/方法；6：TableI/Fig3；7：TableII/Figs4/5与收敛依据；8：形变系统学/混合与Eq32/33；9：SecIIIC–G、Cov与Eq34–36；10：Fig6/结论；11：致谢/完整参考文献。

## Day20 checkpoint113：带符号环与涨落的条件核验

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| HE20-D20-R113-1 | 声明一个J=0和两个完整J=2 multiplet的11维Hermitian rank2张量，初态到两2态的RME取a=(.8,.6)，2态子块D的对角为−.4,.2，交叉为±.3。两者所有B模相同、q2=1，而q3=−sqrt(7/10)aᵀDa分别−.08701264和+.39490353。整体态重相位保持q3，单条边号改变则不是同一重相位。 | declared-signed-tensor-counterexample | task-derived-full-tensor-and-independent-Racah-contraction | HE20-D20-1 Eq7–10; day20_invariant_phase_fluctuation113.py | true |
| HE20-D20-R113-2 | 另声明正Q的可交换形状分布，p=(1/2,1/2)、Q=(1,2)、C=cos3δ=(1,1)。Q、δ独立，真实meanC=1、VarC=0；q2=5/2、q3=9/2、q6=65/2，R=q3/q2^(3/2)=1.13841996，Eq27根号内为1−R²=−37/125。它说明一般涨落下无Cov甚至独立也非把该矩比当meanC的充分条件；不证明作者实际34核结果数值违反其域。 | declared-commuting-shape-moment-counterexample | exact-rational-moments-and-limit-check | HE20-D20-2 Eq11/27; HE20-D20-7 physical-domain caveat | true |

R113-1只指定有限投影张量，不宣称存在唯一微观电荷坐标实现；R113-2是另一明确可交换形状模型，不把两者混为一个真实核Hamiltonian。CG构造经spherical Hermiticity、Jz/J+ rank2对易核验，直接分量收缩与独立整数Racah6j和比较；整体multiplet重相位、同尺度与constant-Q极限均核验。无数值网格/时间步；14项控制只核本声明，非实验精度/phase提取。初次执行缺sympy，后改用已有signed CG及精确Fraction Racah和，无安装/系统环境改动；最终结果以run的result-113-refined为准，旧结果保留。

一般独立Q,C下，R=[E(Q³)/E(Q²)^(3/2)]E(C)。正Q时凸性给幅度因子≥1，恒定幅度时取等；C均值为0等特殊情形也可偶然相等。没有独立性时还含Q³权重/相关项。因此应把R作为实际定义的矩比保留，超域不裁剪后伪造一个角度；若需平均角度或其方差，须另给分布/涨落合同。这条推导不恢复旧037认证，也不量化真实核γ涨落。

## checkpoint147：收敛量词与外推限制

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| HE20-D20-R147-1 | nominal-charge TableI在nI=4时：q₂偏差−9.4(+6.9/−3.4)%、σ(Q²)−23.1(+10.0/−14.6)%、cos3δ差0.00(+.23/−.11)、σ(cos3δ)差−.13(+.08/−.14)。这些是34核模型样本相对nI=40的平均偏差/散布，各列单位也不同；不能读成任一真实核的95%保证、四态完备或四个同类百分误差。 | literal-ensemble-convergence-contract | targeted-original-table-and-text | PDF6 TableI; PDF5 Eq28–31; PDF7收敛讨论; PDF10结论 | true |
| HE20-D20-R147-2 | 作者明确有限价空间/有效电荷使结果model dependent；软度需要更多矩阵元，且更重核收敛更快只是讨论预期。AY23使用到2₆的选择须独立核其网络与softness阶数，不能由本文四/五态经验替代。 | transfer-and-order-boundary | direct-author-limitation-and-task-comparison | PDF9 SecIIID/E/G; PDF10 Conclusions; AY23 PDF13讨论 | true |

对q₃的任务推导：把a分为已保留p与遗漏u、D相应分块，则Δq₃=−√(7/10)[2pᵀD_PUu+uᵀD_UUu]。若另有可靠算符范数界，绝对值≤√(7/10)[2||D_PU||·||p||·||u||+||D_UU||·||u||²]。只知道遗漏q₂=||u||²小，还不足以定量界定q₃误差；还需耦合块界，且q₃接近相消时相对误差可很大。这个Cauchy–Schwarz界是声明实对称有限网络的数学结论，不是文中原实验CI或真实Ce/Nd截断误差。本日AY23中心值账本147给出了同一问题的可复核实例，未把未列D设为零。

## checkpoint149：标量方差的端点闭合（任务推导）

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| HE20-D20-R149-1 | 对Hermitian转动标量S，0⁺本征态s的Var(S)=Σ(r≠s,J=0)|⟨r|S|s⟩|²。只保s这个标量端点再平方会构造性地产生零方差；不能据此判真实核刚性。只有端点截断且每个保留标量元素内部求和已完整时，正项部分和才是方差下界；同时截内部2⁺路径则无此保证。 | task-derived-scalar-closure-boundary | exact-resolution-of-identity | HE20 Eq14–17/24–26 and Fig1; CL86-D20-5/6 | true |

令T为Hermitian rank2 E2张量，S=√5[T×T]⁰、C=−√(35/2){(T×T)²×T}⁰。对明确构造的实数0⁺/2⁺网络，A_ri=⟨0r||T||2i⟩、D_ij=⟨2i||T||2j⟩，有S₀=AAᵀ、C₀=−√(7/10)ADAᵀ。一个2⁺ multiplet、两个0⁺时A=(a,b)ᵀ、D=(d)，q₂=a²、q₃=kda²却不依赖b；VarS=a²b²、VarC=k²d²a²b²，k=−√(7/10)。同样的二/三阶中心值不能识别这两个高阶方差。这里只构造允许的有限球张量网络，未要求各T分量对易，不声称唯一真实电荷坐标或核Hamiltonian。

独立精确有理矩阵演算149用a=1、b=1/2、d=2/5核对因式分解；不传播实验误差或恢复原代码。这与[[cline-1986-nuclear-shapes-coulomb-excitation]] Fig4的印刷归一另属两个问题。后者分母⟨Q³⟩与本页Eq27的⟨Q²⟩^(3/2)不同，113的独立幅度反例必须保持其所检HE20公式身份，不能自动推及Cline原图或其实际算法。
