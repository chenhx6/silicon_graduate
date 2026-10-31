---
type: source
title: "Ragnarsson–Semmes 1988：粒子转子模型中的核矩和能谱"
title_original: "Description of nuclear moments and nuclear spectra in the particle-rotor model"
aliases: [Ragnarsson Semmes 1988 particle rotor, RS88核矩]
created: 2026-10-26
updated: 2026-10-26
status: ai-draft
review_status: unreviewed
source_type: theory-method-and-applications
reading_depth: deep-read
authors: [Ingemar Ragnarsson, Paul B. Semmes]
year: 1988
journal: Hyperfine Interactions
volume: "43"
pages: "425-440 (article); 423-440 (publisher wrapper)"
doi: "10.1007/BF02398323"
citation_key: ""
canonical_source: "https://doi.org/10.1007/BF02398323"
source_url: "https://link.springer.com/content/pdf/10.1007/BF02398323.pdf"
raw_file: "raw/papers/gpt/learning-daily/20261025-DAY23-signature-partner-low-spin-wobbling-magnetic-rotation/ragnarsson-semmes-1988-particle-rotor-moments.pdf"
raw_sha256: "af5b8588ac78f40ecb7ac5eb8f2dd8070c3457296e8fdcd63e9ea0d828a2fa6d"
raw_storage_status: reserved-unpopulated-public-publisher-staging-only
public_staging_file: "tmp/day23-theses/ragnarsson-semmes-1988.pdf"
nuclei: [185au, 185hg, 186hg, holmium-isotopes]
models: [particle-rotor, Nilsson, BCS, residual-proton-neutron-interaction]
methods: [strong-coupling-basis, core-spin-recoupling]
tags: [qtr, nuclear-moments, model-contract, source-lineage]
---

# 核矩、能谱和程序约定的原方法来源

## Bibliographic Record

Ingemar Ragnarsson and Paul B. Semmes，*Hyperfine Interactions* **43** (1988)，DOI10.1007/BF02398323。本次出版商18页PDF前两页是章节扉页/空白，文章实印425–440，对应PDF3–18；133Ce thesis Ref62列423–440的wrapper范围，不能把前2页当正文。Crossref核定title/authors/DOI；未唯一匹配本地Bib故citation_key空。原PDF只在tmp公开staging，raw路径为reserved-unpopulated，未写raw或声称再分发许可。

## Scope and Reading Depth

父代理读取文章16页全文主线、公式文字/图表caption/参考；视觉核PDF3/4/5/6/7/8/11/12/14/16/17/18的contact sheet，PDF8/17大图核参数与Tables2/3。子代理定向独立视觉核§2关键形式及p439。PDF为旧扫描/OCR，重要符号和表值以原页图像为准，未把native提取的损坏字母当数学。不是重新取得/读过所有35引用原件，也未运行旧程序或作者2022job。

本source在距离Day23原截止超过120分钟时作为133Ce既有QTR输入问题的原件路线打开；它不另开课程卡或新session。

## Summary

原文将strong-coupling与good-core-R基区分，明确配对因子/衰减项/physical operator和stretched坐标的约定；应用中同时有spin/矩支持与明确EM失败。它加强133Ce的分析蓝本：参数名字或程序名字相同不足以建立同一计算合同，能量拟合需以未用于定标的电磁量继续检验。本文185Au案例不作为187Au的新增实测。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| RS88-01 | 本文回顾strong-coupling粒子转子formalism，并扩到odd-odd Vpn、磁/四极矩和185Au能量面；没有新133Ce/135Pr/187Au采集。 | source-scope-and-lineage | direct-original-and-explicit-boundary | PDF3, printed425, Introduction | true |
| RS88-02 | 单粒子势在stretched坐标内便于截断，而物理算符在physical spherical坐标定义；相同数值的ε4与δ4通常不对应最佳形状重合，不能混数值/径向矩阵元。 | model-coordinate-convention | direct-original-and-explicit-boundary | PDF4, printed426, §2.1, final paragraph | true |
| RS88-03 | Hcore=ΣAk(Ik−jk)²，Ak=ħ²/(2Jk)；Eq12以body-fixed I±在K指标上降/升而展开，不能把lab升降号直接照搬。 | model-formalism | direct-original-and-explicit-boundary | PDF5, printed427, Eqs11–13 and following paragraph | true |
| RS88-04 | core-H中配对后的相关单粒子矩阵元乘UU′+VV′，off-diagonal单粒子矩阵元可另乘ad hoc Coriolis ξ；二者不是同一因子，也不是所有M1普适淬火。 | model-prescription | direct-original-and-explicit-boundary | PDF5, printed427, paragraph after Eq13 | true |
| RS88-05 | 作者用good-core-R²基变换把core eigenenergies ERα带回strong-coupling基的Eq15，因而可用任意core能量参数化。R-dependent MoI不能未经定义直接用总I替代coreR。 | model-recoupling-and-input | direct-original-and-explicit-boundary | PDF5–6, printed427–428, Eqs14–15 | true |
| RS88-06 | odd-odd保留两个不同粒子与conjugate产品，轴对称K=Ωp±Ωn；这是组态耦合partner结构，不自动等同signature或wobbling声子。 | model-basis-and-classification | direct-original-and-explicit-boundary | PDF6, printed428, Eqs16–21 | true |
| RS88-07 | Vpn含central/spin/exchange/tensor项及pairing factors；u0不贡献给定pair的GM splitting/Newby shift并不意味着对不同组态的bandhead无影响，作者也保留offdiagonal项。 | model-interaction-boundary | direct-original-and-explicit-boundary | PDF7, printed429, Eqs22–25 and discussion | true |
| RS88-08 | B定义用reduced matrix element；M1=gR R+Σ(gl l+gs s)，E2有core与odd-particle部分；混合比Eq29含sqrt(.7)Eγ。原论文给一般formalism，仍需完整矩阵元、数值单位与相位才能复跑。 | electromagnetic-formalism | direct-original-and-explicit-boundary | PDF7–8, printed429–430, Eqs26–31 | true |
| RS88-09 | 本文应用的Fermi energy和BCS gap由指定pairing方法导出；gs=.7gfree、gR=Z/A、coreQ microscopic、惯量按Grodzins。不能把这些1988应用选择直接覆盖133Ce thesis的gs=.6及Harris。 | model-parameter-version | direct-original-and-explicit-boundary | PDF8, printed430, §2.7 | true |
| RS88-10 | 作者在其odd核用10–15 deformedorbitals称收敛、odd-odd典型4n/4p称误差可忽略；这是本文特定应用的报告，不能替133Ce九轨道收敛测试或full infinite space。 | author-convergence-and-scope | direct-original-and-explicit-boundary | PDF8, printed430, §2.7 | true |
| RS88-11 | Ho应用总体解释部分spin/moments但156Ho仍困难，作者认为需调查triaxial形状；相似能谱和部分矩拟合不等于所有组态唯一确定。 | model-comparison-and-limit | direct-original-and-explicit-boundary | PDF11–12, printed433–434, §3.2 | true |
| RS88-12 | 185Au模型的prolate能量相对oblate总体约低500keV，作者归入计算不确定性并讨论specialisation/配对塌缩；该500不是统计CI或187Au实验差。 | author-model-limitation | direct-original-and-explicit-boundary | PDF14, printed436, §4.1 | true |
| RS88-13 | 185Au Table2中两条到5/2基态的rates较合理，但(7/2)1→(9/2)1被观测为M1而模型近纯E2：印刷BM1exp=(1.1±.5)×10^-2、calc3×10^-5。这是作者明确承认的分项失败，数据来自Ref28，不是本文新测。 | reused-experiment-and-model-failure | direct-original-and-explicit-boundary | PDF17, printed439, Table2 and §4.2 | true |
| RS88-14 | Table3为两种strongcoupled候选内部ΔI1序列的模型值：prolate h11/2的δ约+.256–.262，oblate h9/2约−.69至−.72；作者称合理参数/γ离轴20°内符号稳。不是实测δ，也不是187Au带间links。 | model-prediction-and-test | direct-original-and-explicit-boundary | PDF17, printed439, Table3 and §4.2 | true |
| RS88-15 | p439末段在oblateh9/2 feed oblateh11/2及cross-talk语境字面仍写intraband transitions，不能未经核验静默改成带间再移用小B；Table3与该句身份分别保留。 | literal-wording-and-identity-boundary | direct-original-and-explicit-boundary | PDF17, printed439, paragraph immediately before Table3 | true |
| RS88-16 | 作者outlook提出改进pairing及R²基下更真实惯量；本文不是2022作者GAMPN/ASYMO/PROBMO输入/代码发布或其实际job证明。 | readiness-and-producer-boundary | direct-original-and-explicit-boundary | PDF18, printed440, Outlook; PDF3 Introduction | true |

## Competing Interpretations and Limitations

能谱/磁矩/四极矩和带内/带间rate指认须分项检验。固定形变的EM计算与每个态分别最小化总能量的做法不同；更改形变/配对后不能仍称纯configuration relabel。δ符号的模型预测需实际operator/phase convention、共同response和原observations才能检验，不能迁移为所有核素的几何标签。

OpenAlex/发现工具的closed/restricted只说明其索引/端点状态，本次明确出版商URL实际200/%PDF。取得本方法文仍未获得1978 explicit single-particle matrix elements全文、2022三个程序版本/input/输出；不由文献访问成功推断模型已重放。

## Extracted Pages

[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]] Ref62、WK22-10/11/16/18与本原文逐项对照；[[133ce-thesis-analysis-blueprint]]保存可复用合同/推导。[[signature-tip-shears-discrimination-contract]]承接Day23 A槽响应与B槽configuration-only边界。新claims全部needs_review:true，无human-reviewed晋升。

## Ref1访问边界与独立BCS/张量归一控制

本轮沿Ref1 Larsson/Leander/Ragnarsson NPA307(1978)189–223、DOI10.1016/0375-9474(78)90613-9核书目；受检合法入口未获全文，实际1978正文阅读0页。ScienceDirect403/API406、Lund无附件、OpenAlex无PDF、Scholar timeout及S2一次429均留访问记录，不重复撞失败端点；不以摘要冒显式矩阵元。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| RS88-17 | Eq10相位动机下，任务构造4模式16维精确Fock控制：T-odd一体散射给uu′+vv′，T-even prototype给uu′−vv′，对角电算符须分开BCS真空/core贡献。它不替Ref1完整M1/E2公式，不意味着整个particle+core E2统一乘minus，也不恢复actual λ/Δ。 | task-derived-BCS-control | conditional-Fock-algebra-not-author-code | printed427 Eq10 and paragraph afterEq13; printed429 Eqs26–28 | true |
| RS88-18 | 按声明Wigner–Eckart约定，固定Mi对所有Mf/q求和已为B=R²/(2Ji+1)，不可再除一次；反向详细平衡依初态spin权重。精确3j²控制为数学归一，非本核矩阵元或g/τ。 | task-derived-tensor-normalization | conditional-exact-angular-algebra | printed429 Eq26; printed430 Eqs29–31 | true |


## 2026-10-26 用户补充原件：获取状态更新

以下文件已由用户提供，核对 PDF 签名、可解析页数和首页身份，按原路径登记。此前未取得正文的记录保留为历史访问结果；本次仅解除文件获取缺口，尚未核查原表、公式或科学结论，不改变已有 review 状态。

- Nuclear core-quasiparticle coupling；DOI `10.1016/0375-9474(78)90613-9`；PDF 35 页；原件 [PDF](<../../raw/papers/1-s2.0-0375947478906139-main.pdf>)。SHA-256：`108c29bed9de467d99f330c0b8cef47be82a290263a85e398ba3b4f2e97d77eb`。

接收回执：[20261026 user PDFs](../../outputs/literature-acquisition/20261026-user-pdfs-elsevier-access.json)。
