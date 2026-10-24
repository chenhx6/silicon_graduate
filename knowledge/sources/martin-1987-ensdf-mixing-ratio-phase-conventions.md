---
type: source
title: "Martin 1987：ENSDF混合比相位、未观测转换与参考角色"
aliases: [Martin 1987 ENSDF phase convention, ENSDF procedures phase chapter]
created: 2026-10-18
updated: 2026-10-18
status: ai-draft
review_status: unreviewed
source_type: method-chapter
reading_depth: read
title_original: "Phase Conventions for Mixing Ratios in Electromagnetic Transitions from Angular Correlations and Angular Distributions"
authors: [M. J. Martin]
year: 1987
chapter_date: August1987
parent_title: "Procedures Manual for the Evaluated Nuclear Structure Data File"
parent_editor: M. R. Bhat
parent_report: BNL-NCS-40503
parent_date: October1987
doi: "10.2172/5262270"
doi_scope: edited-parent-manual-not-chapter-specific
citation_key: ""
citation_key_status: no-unique-local-BibTeX-entry
canonical_source: "Martin August1987 phase chapter pp1-9 in NNDC BNL-NCS-40503"
source_url: "https://www.nndc.bnl.gov/ensdf/evalcorner/pdfs/ensdf-procedures.pdf"
raw_file: "raw/papers/gpt/day16-20261018/ensdf-procedures-1987-f08bf2c3e780.pdf"
raw_sha256: "f08bf2c3e7802ed741377c13344a701f54670f19e6c143be5901cd151cc256c8"
raw_storage_status: verified-raw-archive
raw_archive_verified_at: 2026-10-23
nuclei: []
reactions: []
experiments: []
models: [Steffen, Rose-Brink, Biedenharn-Rose]
methods: [angular-correlation, angular-distribution, phase-convention, deorientation, internal-conversion]
observables: [multipole-mixing-ratio, directional-correlation-coefficient]
tags: [ensdf, phase-convention, reference-role, unobserved-transition]
---

# Martin 1987：相位定义与完全未观测跃迁

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

本页来源是M.J.Martin署名、August1987的九页方法章，不把编辑M.R.Bhat当该章作者。母本为BNL-NCS-40503 informal report、October1987，现由[NNDC ENSDF首页](https://www.nndc.bnl.gov/ensdf/)直接链接[Procedures Manual](https://www.nndc.bnl.gov/ensdf/evalcorner/pdfs/ensdf-procedures.pdf)。实际文件186PDF页/5478759bytes；本章PDF132–140对应章内printed1–9。所列DOI来自ALPACA参考7所指母本，非声称章节有独立DOI；原PDF封面/目录/章首身份已核。

## Scope and Reading Depth

来源前primed假设冻结后，读完本章九页完整主线：相位/定义Eqs1–8、六项Comments and Special cases及Eqs9–20、TableI相位表与24组references。原图核PDF133–139的关键式/特例/表；目录/母本封面另核。未通读186页其余统计、寿命或核结构章节；不以read称整manual精读。新原件实际位于repo tmp，raw_file为未填归档槽，raw/Bib不改，无新humanreview。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| MA87-1 | 一致计算须同时说明B/A的展开、emission/absorption RME、Wigner–Eckart和EM算符定义；本章Steffen用初态在右的emission元素，Bfirst干涉因子为(−1)^(L−Lprime+k)，Alast为正linear项。evenk且相邻multipoles时前者为负。 | phase-definition-and-role | direct-method | chapterp1–2 Eqs1–5/PDF132–133 | true |
| MA87-2 | Eq7给δRB=(−1)^(L−Lprime)δS；TableI的RB两步负、Biedenharn–Rose first负/second正相对Steffen。文中称RB为absorption元素/initialleft，KS70原文却将其initialleft用于emission notation；相同数值桥不许可用文字标签推断真实吸收过程或省掉各文normalization。 | convention-crosswalk-and-terminology-boundary | direct-and-cross-source | chapterp3 Eq6–8/PDF134；p8 TableI/PDF139；KS70printed727 Eq5 | true |
| MA87-3 | 完全未观测mixed跃迁的U采用总衰变权重Δ²=[(1+alpha(Lprime))/(1+alpha(L))]δgamma²，alpha为purecomponent totalICC；U=(U_L+Δ²U_Lprime)/(1+Δ²)，无干涉且U0=1。alpha≪1时Δ趋δ；δ符号仍不由U识别。作者将该修正归给Anicin等Ref21，不冒称本run已读该primary。 | unobserved-total-decay-transfer | direct-method | chapterp4 Eq9/PDF135；p5 Eq10/PDF136；p9 Ref21/PDF140 | true |
| MA87-4 | 若实际观测i-shell转换电子，须δcei=sqrt(alpha_i(Lprime)/alpha_i(L))δgamma，并以electron particleparameters b_k乘F；此为电子角关联的conditional ratio，不等于完全未观测总衰变Δ，K-shell不能替totalICC。 | observed-electron-versus-total-channel | direct-method | chapterp5 Eqs12–13/PDF136 | true |
| MA87-5 | Resonance fluorescence特例采用原Eqs1–5且同一exciting/deexciting pair给δS1=−δS2，Eq14变为sum[A_k(gamma2)]²P_k；它证实ENSDF原manual这一原系数合同，不认证RU09actualproducer或后来的modifiedKSW脚注。 | NRF-phase-special-case | direct-method | chapterp5 ResonanceFluorescence/Eq14/PDF136 | true |
| MA87-6 | 用lowtemperature或nuclearreaction产生orientation时B_k应作为alignment参数由实验/经验/模型给定，不自动用firstγ产生的B；Coulomb/alpha/电子等有各自particleparameters，evenk的域与possibleoddterms也需保留。 | orientation-and-domain-boundary | direct-method | chapterp4 intro；p6 Eqs15–18；p7 Eqs19–20/Othercases | true |

## Summary

这份原manual使先前仅有ALPACA README转述的ENSDF相位立场有了直接来源，也区分radiative δ、观测电子δcei和完全未观测totaldecay的Δ。章内的operator/normalization与物理观测必须同时携带，不能把同一“δ”用于三种conditional对象。

## Competing Interpretations and Limitations

- p1关于relative phase“physically significant”的语境不取消后文对operator/RME/系数约定的要求；本任务不由此声称所有原始有符号数字不变。
- p3的RB absorption用语与KS70的emission说明保留为文字约定差别，采用完整式桥核物理量；本章Eq6不是KS70裸T_RB定义的逐字符替代。
- 本章是方法/评价指南，非新实验；其Ref21 Aničin/Vukanović/Kukoč NIM103,395–396(1972)，Crossref定位DOI10.1016/0029-554X(72)90401-6，publisher候选/公开XML只有metadata未得body。不把chapter转述当该primary已原读。
- totalchannel推导要求该跃迁所有γ/ce路线均未被selection区分；若middleγ被额外门、multiplicity或veto选择，应按实际条件重新传播。这里只给两multipole/无E0/无额外atomic核异常的nominal框架。

## Knowledge Impact and Learning Decision

`supports`first/last相位和ENSDF原NRF反号合同；`revises`把未观测跃迁一律按radiativeδ²混合的直觉，须先说明中间光子是否被postselect；`limits`只凭来源名称替代完整RME/response定义。[[internal-conversion-analysis]]与[[deorientation]]保存权重推导/真实nominalICC设计；[[multipole-mixing-ratio]]区分观测对象。新claims均true，原source/producer边界不擅清。

## Extracted Pages

- [[internal-conversion-analysis]]、[[deorientation]]：总衰变/光子选择的未观测传播。
- [[dco-pdco-ambiguity-worksheet]]、[[multipole-mixing-ratio]]：三种mixing coordinate与first/last合同。
- [[polarized-photon-branch-audit]]：原manualNRF与modified系数/真实producer区别。
- [[tuli-2001-ensdf-format-manual]]：独立文件格式规则，非同一份manual或科学实验。

## checkpoint032：Steffen 与 Rose-Brink 相位跨网对账与未观测退定向 U_k 审计

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| MA87-D21-1 | 依据 Martin 1987 ENSDF 手册对混合比相位体系展开代数对账审计证明：(1) 对相邻多极（L'=L+1），Steffen 体系与 Rose-Brink 体系严格满足 delta_RB = - delta_S；混淆两体系将直接反转角分布干涉项 2*delta*F_k 符号，在 delta=0.5 时致使 A2 发生 0.765 的巨大虚假漂移（从 -0.1937 变为 +0.5713）；(2) 始发跃迁 B_k 与后续跃迁 A_k 在 Steffen 展开中干涉项符号相反（前者为负，后者为正）；(3) 经由未观测中间混合级联退激时，必须通过全衰变参数 Delta^2（考虑总内转换系数比值）计算退定向因子 U_k，忽略内转换在低能区可造成退定向衰减几百分点的系统失真。 | phase-convention-deorientation-boundary | direct-original-and-quantitative-audit | pp.1–9 Eqs.(1)–(10), Table I; phase-conventions-deorientation-audit-032.json | true |
