---
type: source
title: "Ayangeakaa2023：76Ge多步Coulomb激发完整矩阵元与三轴性解释"
title_original: "Triaxiality and the nature of low-energy excitations in 76Ge"
aliases: [Ayangeakaa2023 Ge76 full Coulomb excitation]
created: 2026-10-23
updated: 2026-10-23
status: ai-draft
review_status: unreviewed
source_type: experiment-and-model-comparison
reading_depth: read
authors: ["A. D. Ayangeakaa", "R. V. F. Janssens", "S. Zhu", "J. M. Allmond", "B. A. Brown", "C. Y. Wu", "et al."]
year: 2023
journal: Physical Review C
volume: "107"
pages: "044314"
doi: "10.1103/PhysRevC.107.044314"
citation_key: ""
canonical_source: "https://doi.org/10.1103/PhysRevC.107.044314"
source_url: "https://link.aps.org/accepted/10.1103/PhysRevC.107.044314"
raw_file: "raw/papers/day20-20261022/ayangeakaa-2023-ge76-coulomb-excitation-full.pdf"
raw_sha256: "4907cd6d64d74fe7aea247d9be1c3e056fb026d9b76e4385c69c3b8784917a96"
raw_storage_status: reserved-unpopulated-accepted-manuscript-staging-only
raw_archive_verified_at: 2026-10-23
analysis_status: public-staging-original-read-raw-archive-verified
public_staging_manifest: "tmp/day20-ge76-119/manifest.json"
nuclei: [76Ge, 76Se, 208Pb]
reactions: ["208Pb(76Ge,76Ge*)208Pb"]
experiments: [ATLAS-GRETINA-CHICO2]
models: [GOSIA, GTRM, jj44b, JUN45]
methods: [multistep-Coulomb-excitation, rotational-invariants]
observables: [reduced-matrix-elements, transition-strengths, static-quadrupole-moments, triaxiality-softness]
tags: [full-matrix-set, followup-identity, poves-citation, model-softness, ge76]
---

# 2019短文所指完整后续论文与长文矩阵元

## Bibliographic Record

Ayangeakaa等，Physical Review C107，044314(2023)，DOI10.1103/PhysRevC.107.044314，Crossref精确端点核发表2023-04-19。实际读取为APS/CHORUS accepted manuscript，cover1页+正文/参考15页，共16页、6275352bytes，SHA256见frontmatter。首页Dated2023-04-06，下载version标签不替代cover原样 accepted；未逐字核排版最终版。

这是[[ayangeakaa-2019-rigid-triaxial-ge76]] Ref37的真正后续长文原件。PDF只在tmp公开staging，raw_file是未填归档槽，raw/PLAN/Bib未写。SI沿auto关闭，不断言不存在。旧TableI/II寿命/混合比/branch作为约束进入GOSIA，表输出非独立。

## Scope and Reading Depth

primed-recall-119在原件lookup前冻结；本session实际读PDF1–16全部文字与参考文献，此前记录视觉核图1–11及5表；146发现实际有Fig12，旧全图清单不完整。未取得原event、21组产额全数值、完整GOSIA job/producer与全协方差矩阵；未运行NuShellX重现原CI波函数。119时Kumar/Cline均未得正文；148已新读[[cline-1986-nuclear-shapes-coulomb-excitation]]，Kumar仍metadata-only。

## Paper Question and Scientific Motivation

给2019短文承诺的完整实验与模型分析：发表完整E1/E2/E3/M1矩阵元表，用广义三轴转子(GTRM)与CI壳模型(jj44b/JUN45)比较低激发态和三轴性，并用CI wavefunctions研究76Ge与76Se的软度差异。0νββ仍是应用动机，不是本文测得弱相互作用矩阵元。

## Method and Design Logic

291/304/317MeV三束能，208Pb靶，GRETINA+CHICO2；三能量各分七角区得21个数据集、约118条校准γ强度，GOSIA以归一化χ²=0.98联合拟合。TableIII列出81个E1/E2/E3/M1 reduced matrix elements；TableI/II为外源约束。GTRM参数Q0=1.69(1)eb、γ=25.4(5)°、Γ=−15.8(4)°从实验三矩阵元解析反演。

## Key Evidence and Reasoning Chain

21组yield与外源约束 → 81个矩阵元与静态矩 → GTRM解析参数与能带/跨带比较 → 壳模型矩阵元求不变量 → 76Ge与76Se在jj44b/JUN45下的软度对比。软度比较同时展示实验不变量Fig10(a)及CI计算(b)/(c)；计算网络截到2₆⁺。不可将前者抹去，也不能由图恢复原jointCov（146修订）。

## Summary

长文确立了2019短文所缺的完整矩阵元集合，并明确引出[[poves-2020-limits-assigning-nuclear-shape]]（Ref60）作为替代不变量方法，承认其给出近乎等价的数值，同时在模型分支中主张jj44b下76Ge较刚、76Se很软。它把争议对准了模型软度与不变量计算方法，而不是否认Poves的存在；本任务尚未取得原producer与全Cov；不能由此断言作者未计系统误差。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| AY23-D20-1 | 确认为2019 PRL Ref37的完整后续长文，发表81个E1/E2/E3/M1 reduced matrix elements；2019短文另称103个混合矩阵元；不由两数差异反推全部拟合参数范围，二文为同谱系（146修订）。 | followup-lineage-and-published-size | direct-original-and-visual | PDF1/正文1; PDF6/7 TableIII | true |
| AY23-D20-2 | TableIII列出主要E2与静态矩：ground到2₁–2₆为.526(2)/.089(3)/.061(3)/.054(4)/.010(+.009/−.021)/.023(6)eb；2₁对角−.24(2)eb、2₂对角+.26(+.02/−.05)eb（146定向视觉更正）。保留符号、初末态和箭头，非单独B模。 | reported-full-matrix-elements | direct-table-and-visual | PDF6–8 TableIII | true |
| AY23-D20-3 | TableI/II沿用外源寿命、branch与混合比；GOSIA全三能量最小χ²=0.98。结果包含旧约束，非完全独立。 | experimental-fit-constraint-lineage | direct-tables-and-text | PDF5 TableI/II; PDF6 text | true |
| AY23-D20-4 | GTRM由0₁→2₁、0₁→2₂和2₁对角解析定出Q0=1.69(1)eb、γ=25.4(5)°、Γ=−15.8(4)°，再算整个能带与跨带；Fig6显示对ΔI=0,1;ΔK=2跨带跃迁仍有明确偏离。 | model-parameter-and-failure-boundary | direct-original-and-visual | PDF8 SecIV; PDF9/10 Figs5–7 | true |
| AY23-D20-5 | PDF12明确引用Poves2020（Ref60）为评估不变量的替代方法，称其提供almost exact solution且与本文结果effectively similar；作者据CI模型主张76Ge较刚而76Se很软。 | author-acknowledgment-of-competing-method | direct-author-text | PDF12 column text; PDF13 Fig10/text; PDF15 Ref60 | true |
| AY23-D20-6 | 146更正：Fig10(a)是实验矩阵元导出的不变量，(b)/(c)为jj44b/JUN45模型；PDF13称实验约29°/2°、模型约27°/4°。图的normal分布形状涨落不是实验参数的完整jointCI，原Cov/producer仍未取得。 | theoretical-invariants-generation | direct-original-and-visual | PDF12 SecIV; PDF13 Fig10 and caption | true |
| AY23-D20-7 | 76Se的软度也是用CI波函数计算并引[[henderson-2019-triaxiality-selenium76]]（Ref62）；作者认为76Ge/Se具有显著三轴但刚性不同。保留该模型结论，不据此消除Poves关于两核均有大γ涨落的断言。 | parent-daughter-comparison-boundary | direct-author-text | PDF13 column text; PDF14 SecV | true |

## Competing Interpretations and Limitations

本长文未推翻2019刚性主张，而是补充了完整表和模型计算，并把Poves方法纳入引用。实验不变量仍受有限截断制约；模型软度依赖所用相互作用（jj44b vs JUN45），且正如Poves指出的，截断算符对易性与大γ涨落仍可改变结论强度。本任务尚未取得原event数据、各角区完整yield与GOSIA联合误差协方差矩阵；论文明确报告其逐元素误差已计系统与交叉相关贡献。

## Analytical Reconstruction

AY23-D20-1/2提供了76Ge与76Se的平行长文表对照：两者均发表了低激发E2矩阵元集合，但不由此宣称子空间内的所有E2元素已给出，但Ge有负的2₁对角（−.24eb）且更接近25°，Se也是负的（−.35eb）但由作者归为平均三轴而模型更软。146修订：Fig10含实验与模型两类不变量图；它们共享不同输入与截断合同，不作为独立重复实验计数。

## Knowledge Impact and Learning Decision

revises：把2019短文“forthcoming Ref37”的未决状态闭合为已识别、已读完的2023长文原件。supports：[[day20-quadrupole-collectivity-systematics-synthesis]]关于“实验矩阵元 + 模型高阶”混合推断的边界，以及[[transition-quadrupole-moment]]中外源约束与矩阵元符号的需求。将81矩阵元表与Poves引证写入canonical笔记，review保持unreviewed。

## Related Knowledge and Project Relations

- foundational-background：[[ayangeakaa-2019-rigid-triaxial-ge76]]，本文是其长文原件。
- competing-interpretation：[[poves-2020-limits-assigning-nuclear-shape]]，本文Ref60，针对模型软度与涨落。
- limits：[[henderson-2019-triaxiality-selenium76]]，本文Ref62，Se仅平均三轴性且模型更软。
- supports：[[day20-quadrupole-collectivity-systematics-synthesis]]、[[transition-quadrupole-moment]]。

## Human Review Triage

按ingest-strategies的Agent self-audit定义，保持unreviewed。P0: none identified。P1：AY23-D20-1/2与2019短文矩阵元口径消歧；AY23-D20-5对Poves方法的引用与模型刚性争论的对准；AY23-D20-6模型不变量与实验有限网络的区分。P2/P3：accepted cover优先、raw deferred、81/103数字分层。

## Extracted Pages

PDF1：CHORUS accepted cover；2/正文1：引言与0νββ背景；3/正文2：Ge同位素谱学与模型概述；4/正文3：实验setup、GRETINA/CHICO2与Fig1；5/正文4：Doppler谱Fig2、能级纲图Fig3、角区谱Fig4与TableI/II约束；6/正文5：GOSIA拟合与TableIII前段；7/正文6：TableIII后半；8/正文7：讨论起、静矩比较；9/正文8：GTRM分析与Fig5/6；10/正文9：Fig7静矩与Fig8惯量；11/正文10：能级Fig9与TableIV强度；12/正文11：TableV静矩与不变量软度起；13/正文12：Fig10软度图与76Se讨论；14/正文13：结论与致谢；15/正文14：Refs1–62。
### checkpoint144：多步库仑激发完整矩阵元集合、静四极矩与三轴软度争论审查

> checkpoint146：本节121–145批次的科学认证已撤回。旧文本/输入与指纹保存在本run的history-before-repair-146.json；原始原件与既有review/flags保留。自设数值或flag的passed只验证算术，不识别实际producer、共同Cov、实验CI或唯一模式。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| AY23-D20-R144-1 | checkpoint146撤回旧认证；不据此恢复错误表值、跨态强度阶梯、硬阈值或完全闭合。请使用本页较早原件纠错与checkpoint146。 | withdrawn-task-certification | rejected-and-replaced | checkpoint146; history-before-repair-146.json | true |

## checkpoint146：原件身份与推断边界更正

本轮为Codex定向self-audit；已有review_status与原claim flags不变。121–145旧认证撤回；实际新阅读范围见source-reading-scope-146.json，引用较早纠错不冒称新全文阅读。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| AY23-D20-R146-1 | 实际身份PRC107,044314，非144的034306。TableIII共81个E1/E2/E3/M1矩阵元，不是全Hilbert空间完备集。0₁→2₅为.010(+.009/−.021)eb、0₁→2₆为.023(6)eb；2₂对角+.26(+.02/−.05)eb。旧AY23-D20-2相应错行/误差已更正。Qs(2₁)=−.18(2)由同一对角−.24(2)换算，不能计为独立重复测量；负Qs单独不唯一决定内禀形状。 | direct-original-table-and-lineage-correction | source-and-bounded-self-audit | CHORUS cover/PDF1; PDF6/7 TableIII; PDF12 TableV | true |
| AY23-D20-R146-2 | Fig10(a)为实验不变量，(b)/(c)为jj44b/JUN45；原文称实验角度/展宽约29°/2°，模型约27°/4°。因此旧119/144中“只有模型高阶、没有实验软度图”的概括过强。第12页正文承认Ref60方法almost exact且results effectively similar，同时继续主张Ge较刚/Se较软，不能解释为接受Poves的Ge反刚性结论或数学全一致的独立复现。未得完整原Cov/producer，保争议。 | direct-original-author-claims-and-boundary | source-and-bounded-self-audit | PDF12/printed11 Fig10; PDF13/printed12讨论/Figs11/12; PDF14结论 | true |
| AY23-D20-R146-3 | 实际accepted稿有Fig12。旧scope119的figures只列1–11，故“全部11图”清单不完整；原16页文字/此前视觉记录作为历史保留，本轮仅声明scope146列出的定向重读与视觉范围，不以一次表核验补认证全文全图。 | reading-scope-correction | source-and-bounded-self-audit | PDF13/printed12 Figs11/12; source-reading-scope-119 | true |

## checkpoint147：已列矩阵元网络与误差合同

本轮只定向重读PDF6–8 TableIII及相应误差/讨论文字，结合PDF12/13已读讨论；不是新一次全文阅读。原review与claim flags保持。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| AY23-D20-R147-1 | 作者说逐矩阵元误差取68.3%置信限，包含统计、系统和cross-correlation贡献；本任务未取得完整jointCov。这两件事同时成立。缺少jointCov不等于原误差未计系统或相关，也不能把各误差当独立Gaussian重造高阶矩CI。 | reported-uncertainty-contract | direct-original-text | PDF6/printed5 TableIII前最后一段 | true |
| AY23-D20-R147-2 | TableIII的六个ground→2⁺ E2振幅，连同其所列2⁺子块，给出14个独立实D元素；21元素对称6×6子块中仍有D34、D35、D36、D45、D46、D55、D56未列。此为公开表的列项审计，不断言这些元素在原GOSIA里均自由、未约束或取零。81个混合多极矩阵元不是这一E2子块的完备性证明。 | finite-published-network-inventory | direct-table-plus-task-index-audit | PDF6–8 TableIII; invariant-network-input-147.json | true |
| AY23-D20-R147-3 | TableIII的D22为+.26(+.02/−.05)eb，PDF8正文却写+.26(+.02/−.03)eb；TableIII的2₁→0₂ E2 RME为.085(2)eb，正文比较0₂→2₁时另写.144(+.002/−.003)eb。保留表/正文差异，不自行指认哪一处为作者修订，也不替换原不变量输入。 | literal-body-table-discrepancy | direct-original-and-selected-visual | PDF7 TableIII; PDF8/printed7左栏讨论 | true |

### 中心值求和账本（任务推导，不是原实验重拟合）

在同一实数相位约定下，令aᵢ=⟨0₁||E2||2ᵢ⟩、Dᵢⱼ=⟨2ᵢ||E2||2ⱼ⟩。由[[henderson-2020-quadrupole-invariant-convergence]] Eq7–10，J=0时q₂=aᵀa，q₃=−√(7/10)aᵀDa，其中q₃指⟨Q³cos3δ⟩。六个已列a中心值给q₂,listed=.291863 e²b²；2₁占该六项和94.7965%，不是全空间强度的94.7965%。

| 明示只保留的2⁺态 | q₂ / e²b² | q₃ / e³b³ | q₃/q₂^(3/2) | 映射有效角 / degree |
| --- | --- | --- | --- | --- |
| 2₁ | .276676 | .05555610 | .3817460 | 22.5194 |
| 2₁–2₂ | .284597 | .01192391 | .07853681 | 28.4985 |
| 2₁–2₃ | .288318 | .01598395 | .1032468 | 28.0246 |

三行只作已列中心值的明确截断变换，未赋误差或识别真实角度分布。加入2₂时q₂只增加约2.863%，但D12=.535eb的带符号环使q₃明显改变；不能由低阶强度接近饱和直接推得角度/高阶软度已收敛。第4至第6态网络缺项，程序不为它们打印一个“完整角度”。

六态q₃的已列项合计为.017471737 e³b³，尚须加七个未列D的线性项及六态之外路径。例：D34的系数为−.005511916 e²b²，D55为−.0000836660 e²b²；其实际范围未得，不能因系数小就认证总误差小。可复现：system/scripts/day20_invariant_network_ledger147.py读取run的input-147，输出result-147；Decimal逐项和与NumPy遮罩矩阵收缩差3.47×10⁻¹⁸ e³b³，整体态重相位差0。这些只核算术/相位一致性，不认证原实验精度、γ刚性或原fit producer。

## checkpoint148：历史方法原件与现代具体实现分开

[[cline-1986-nuclear-shapes-coulomb-excitation]]的第695页实际讨论强非线性与68.3%参数空间概率积分，补上此前只有转引的方法原件；它不能替代本实验的实际GOSIA版本、job、干涉符号起点、原产额或jointCov。其第699–700页明确高阶截断与对易性限制，也不能仅由该综述判本实验Fig10的真实截断误差。AY23报告已包含系统/交叉相关的逐元素误差仍照原文保留。

## checkpoint167：旧回路计算的输入身份修订

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| AY23-D20-R167-1 | TableIII的−.24(2)eb是D11约化E2矩阵元，不能当Qs后再除sqrt(32pi/175)；D12打印为.535(+.003/−.007)eb而非旧160用的.580。旧61.98%相消、2.63放大及相应角跃变数值撤回。有限投影可算中心值路径贡献，未列项和原Cov保持未知，不认证真实刚性或原CI。 | input-identity-correction | direct-table-plus-bounded-task-audit | PDF7 TableIII; invariant-network-input-147.json D11/D12 rows | true |
