---
type: source
title: "Petrache et al. 2006 - Risk of misinterpretation of nearly degenerate pair bands as chiral partners"
aliases: [Petrache 2006 chiral-band caution]
created: 2026-09-21
updated: 2026-10-27
status: ai-draft
review_status: unreviewed
source_type: critical-analysis-and-model
reading_depth: deep-read
title_original: "Risk of Misinterpretation of Nearly Degenerate Pair Bands as Chiral Partners in Nuclei"
authors: [C. M. Petrache, G. B. Hagemann, I. Hamamoto, K. Starosta]
journal: "Physical Review Letters"
year: 2006
volume: 96
pages: "112502"
doi: "10.1103/PhysRevLett.96.112502"
citation_key: Petrache_2006
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "https://doi.org/10.1103/PhysRevLett.96.112502"
library_file: "raw/papers/gpt/high-spin-20260920/三轴/手征/2006_Petrache et al_Risk of Misinterpretation of Nearly Degenerate Pair Bands as Chiral Partners in.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/三轴/手征/2006_Petrache et al_Risk of Misinterpretation of Nearly Degenerate Pair Bands as Chiral Partners in.pdf"
raw_sha256: "ec32a76efbeebf1a924a1c95eb9d404a99158fc9226605414b324e982cfe1d4f"
nuclei: [134Pr, 136Pm]
reactions: [literature-systematics, band-crossing-analysis]
experiments: [134Pr-transition-probabilities]
models: [band-mixing, ultimate-cranking, total-routhian-surface]
observables: [B(E2), quadrupole-moment-ratio, alignment, signature-staggering, band-degeneracy]
methods: [critical-analysis, energy-systematics, transition-strength-analysis]
tags: [chirality, counterexample, band-mixing, A130]
---

# Risk of misinterpretation of nearly degenerate pair bands as chiral partners

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

- C. M. Petrache *et al.*, *Phys. Rev. Lett.* **96**, 112502 (2006), DOI `10.1103/PhysRevLett.96.112502`.

## Scope and Reading Depth

- The four-page PRL was read end-to-end, including Figs.1–4, Eqs.(1–5), Table I, `134Pr` and `136Pm` systematics, potential-energy surfaces and the conclusion.

## Core Argument

The paper tests whether near-degenerate same-parity `ΔI=1` bands in the `N=75` isotones are genuinely chiral. It argues that ideal chiral partners should have not only similar energies but also similar alignments, shapes and electromagnetic transition probabilities (PDF p.1). In `134Pr`, several 4-qp crossings compress the yrast/yrare separation over `13<I<19`; the energy near-degeneracy therefore does not by itself identify a chiral regime (pp.1–2, Fig.1).

For the `I=14–18` region the alignment difference is about `2ℏ` and the observed 15/16 energy splittings imply an interaction `|V|<18 keV`. Using a two-band mixing wave function (Eqs.1–3) and measured in/out E2 branching ratios, the authors obtain `|V|≈14–17 keV` and `Q0,1/Q0,2=2.0(4)` (pp.2–3, Table I). The ratio is far larger than the `~1.25` expected from the cited UC shape minima, and even the TRS comparison gives only `~1.7`; the bands therefore have substantially different intrinsic shapes.

The `136Pm` pair shows different signature staggering and disappears at different 4-qp crossings; the available data are likewise not favorable to a chiral assignment, although transition-probability measurements are required for a decisive test (p.4, Fig.4).

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PE06-1 | Several crossings can mimic a near-degenerate `134Pr` pair over a finite spin range. | counter-evidence | direct | PDF pp.1–2, Fig.1 | true |
| PE06-2 | `Q0,1/Q0,2=2.0(4)` and alignment differences disfavor ideal chiral partners. | derived-observable | mixed | PDF pp.2–3, Table I | true |
| PE06-3 | `136Pm` signature/crossing behavior is not favorable to chirality but needs electromagnetic tests. | evidence-boundary | direct | PDF p.4, Fig.4 | true |

## Summary

Petrache *et al.* establish a reusable critical test: near-degeneracy is necessary at most, while shape, alignment and transition-strength equality must be checked explicitly.

## Competing Interpretations and Limitations

- The `Q0` ratio is obtained through a simplified two-band mixing model and depends on the adopted branching data.
- The analysis critiques the ideal-pair interpretation of these cases; it does not prove that all future near-degenerate pairs are nonchiral.

## Analytical Reconstruction and Self-Audit

| ID | Audit item | Agent judgment | Locator | Status |
|---|---|---|---|---|
| PE06-AR-1 | Degeneracy mechanism | Crossings can mimic a near-degenerate pair over a finite spin interval; energy spacing is not a chiral observable by itself. | PDF pp.1–2, Fig.1 | self-checking |
| PE06-AR-2 | Shape inference | `Q0` ratio is extracted through a two-band mixing model and measured E2 branches; it is stronger evidence than a visual level-spacing argument but remains assumption-dependent. | PDF pp.2–3, Eqs.1–5, Table I | self-checking |
| PE06-AR-3 | Transfer boundary | The critique supplies a necessary-condition test for candidate chirality, not a universal claim that every near-degenerate pair is nonchiral. | PDF pp.1–4 | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `limits` energy-degeneracy-only claims in [[nuclear-chirality-and-multiple-chiral-doublet-bands]], and provides a direct counterexample to compare with HS-083/HS-119/HS-012.
- L3 question: for each candidate pair, can partner-resolved `B(E2)`, `B(M1)` and alignment data reject crossing/shape-coexistence alternatives before a chiral label is retained?
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `PE06-P0-1`: Do not promote near-degeneracy to chirality without transition strengths, alignment and band-crossing checks; preserve the two-band-mixing assumptions behind `Q0,1/Q0,2`.

## Extracted Pages

- Project/concept: [[nuclear-chirality-and-multiple-chiral-doublet-bands]], [[signature-inversion]]。

## Day24内Day25无学分预习：134Pr比较行

root本次重新读VoR四页全文文本，fresh visual PDF2–4覆盖Figs1–4/Eqs1–5/TableI，raw SHA `ec32a76efbeebf1a924a1c95eb9d404a99158fc9226605414b324e982cfe1d4f`相符。与既有PE06-D18-1/PE06-D21-R45-1–4相符，不另造新的2.0(4)测量或回归；可复用增量是[[chirality-shape-coexistence-companion-matrix]]中的原件支撑比较/companion设计。Tonev2006寿命正文仍未取得，本文的定性引用不代该body。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PE06-D25P-001 | 本文是既有134Pr资料的critical analysis；near-gap/不同alignment和crossing支持检验简单ideal-pair。分支数据Ref11与寿命Ref9不同，Q比1.6–2.4依忽略off-diagonalE2/短段固定V的解混合，不是独立新τ/直接形状测量/已知Gaussian CI。 | direct-input-model-and-comparison-scope | direct-original | printed112502-1 scope; 112502-2 mixingassumptions; 112502-3 Eqs3–5/TableI; 112502-4 Refs9/11 | true |
| PE06-D25P-002 | UC与TRS势面/shape解释是条件模型支持，不证明实验多个刚性形状或唯一分解；源结论仍问手征几何残余存在程度。三核companion对照可限制近简并充分性，不把此核结论推成所有手征动力学否定。 | direct-author-conclusion-and-labelled-synthesis | direct-original-plus-design-boundary | printed112502-3 Fig3/UCcomparison; 112502-4 conclusion | true |
| PE06-D25P-003 | 在源两带空间引入额外real symmetric forward-E2 q12时，M=Rf^T Q Ri的振幅干涉会改变Eq4/5捷径；对固定Q的Frobenius/det²/SVD基变换不变量仍在，但仅两个parent比没有绝对列norm/branch-loop sign，不能恢复它们。q12=q21本身是额外ansatz，非Hermiticity自动结论；源α仅原提取的前向基线，未重fit或证明替代获胜。 | declared-two-band-operator-extension | source-premise-plus-task-algebra | printed112502-2 Eqs1–2/assumptions; 112502-3 Eqs3–5/TableI; task two-band-em-022 | true |

有界推导和script结果进入[[chirality-shape-coexistence-companion-matrix]]“非对角E2扩展”，保17→15的原带continuity与y/ny端点倒数、18→16不倒数。该组件说明额外transition-kernel自由度如何改变推理条件，不把旧Q允许范围重命名新CI或实际equal-shape fit，不改变本源作者结论的历史身份。

## Day18参照核验：2.0(4)的实际提取链

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PE06-D18-1 | 2.0(4)指E2 transition moments的Q0,1/Q0,2；作者以实测E2 out/in分支和ΔE解混合振幅/V/矩比，假定无off-diagonal E2、短spin段V不变。允许范围1.6–2.4是该分析与输入的范围；寿命B的差异只作定性一致性对照，不是这项比值的直接来源，也不能把其转成beta两倍。 | source-derivation-and-lineage-audit | direct-and-boundary | PDF2最后两栏；PDF3 Eqs3–5/TableI及2.0(4)段；PE06-2 | true |

原PE06-1–3及review保持。此次独立worker完整四页文字、PDF2–3视觉；主代理定向原读PDF2–3及PDF3视觉，未重拟合V/Q或原实验CI。联系[[hecht-2001-chiral-symmetry-breaking-136pm-138eu]] HE01-D18-5，明确这是参照而非另两核的新测量。
## Day20量化审计：134Pr两带波函数解混合、四极矩2倍不对称与伪手征证伪（checkpoint030）

> checkpoint032：本节旧认证已撤回；程序通过只曾检自设输入。以下R32为本次定向原读纠正。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| PE06-D20-1 | checkpoint032：旧科学认证撤回，原因：Invented gap sequence conflicts with printed36/44keV; chosen V not extracted; arcsin branch ambiguity; allowed1.6-2.4 range not Gaussian; invented128Cs uncertainties; exclusive configuration/handedness labels not established.；当前可用陈述见下方R32原读纠正。 | withdrawn-task-certification | rejected-and-replaced | checkpoint032; PE06-D20-R32-1 | true |

## checkpoint032：原件定位与科学认证纠正

本次Codex self-audit，原review状态与全部已有claim flags保持；不是新增独立实验或全文阅读认证。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PE06-D20-R32-1 | PDF2明确I15/16两态间隙36/44keV；PDF3奇/偶序列V约14/17keV、矩比允许1.6–2.4，TableI α15y=.894、α16ny=.427。旧31keV序列、37.7度等反解认证撤回；振幅需保yrast/nonyrast身份与混合分支。 | literal-model-table-correction | direct-original-and-visual | PDF2 near-gap paragraph; PDF3 Eq3/TableI | true |
| PE06-D20-R32-2 | 2.0(4)来自无off-diagonal E2、短spin段V固定的分支比解混合允许范围；作者用它反对理想手征带解释。未给该范围Gaussian抽样含义，不作z2.5/p.0124或所有手征动力学排除；寿命B仅定性对照。 | range-versus-CI-and-interpretation-boundary | direct-original-and-visual | PDF3 Eqs4–5 and possible-ranges paragraph; PE06-D18-1 | true |


### checkpoint051：两带混合矩阵元与伪简并电磁非对称性审计

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| PE06-D20-R51-1 | checkpoint101撤回旧“独立程序严格认证/终极唯一判据”。保留此前原读对36/44keV能隙及作者模型允许Q比1.6–2.4的分层记录；2.0(4)不能改称已知Gaussian测量。两能级模型DeltaE>=2|V|只给条件上限，不独立提取V/混合角。旧alpha/beta标签和过强排他裁决不沿用；矩阵元不对称需连同模型条件、带身份及替代解释讨论。 | withdrawn-overclaim-and-model-boundary | task-boundary-correction | PRL96,112502 TableI; PE06-D20 source corrections; checkpoint101 | true |
### checkpoint142：两带解混合、内禀四极矩双倍不对称与伪手征陷阱审查

> checkpoint146：本节121–145批次的科学认证已撤回。旧文本/输入与指纹保存在本run的history-before-repair-146.json；原始原件与既有review/flags保留。自设数值或flag的passed只验证算术，不识别实际producer、共同Cov、实验CI或唯一模式。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| PE06-D20-R142-1 | checkpoint146撤回旧认证；不据此恢复错误表值、跨态强度阶梯、硬阈值或完全闭合。请使用本页较早原件纠错与checkpoint146。 | withdrawn-task-certification | rejected-and-replaced | checkpoint146; history-before-repair-146.json | true |

## Day 21周考对比：134Pr能量伪简并与135Nd寿命不对称之推断阶梯对照

本节001旧认证由checkpoint045定向原件审计取代。134Pr的2.0(4)来自分支比加两带解混合允许范围；不是直接寿命矩比，不能由“B约4倍”就唯一确定静态形状。135Nd的tau与B恒等式也未独立识别真实分支补偿。两核可作方法对照，均不能替代对方的测量。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| PE06-D21-1 | superseded：旧文字把解混合允许范围称直接测得并过强认证两核机制；改用PE06-D21-R45-1至R45-4，保留模型、输入谱系及非排他范围。 | wiki-synthesis | indirect | PRL 96, 112502 Table I; [[experimental-claim-boundaries]] | true |


## Day21 checkpoint045：两带解混合、身份交换与证据谱系

source前回忆已冻结，明确受既有Wiki priming；本轮重读VoR四页全文，视觉核全部4页Figs.1–4、Eqs.1–5与Table I。raw SHA256 `ec32a76efbeebf1a924a1c95eb9d404a99158fc9226605414b324e982cfe1d4f`未变。原review/flags保持，非human-reviewed。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PE06-D21-R45-1 | 原文以忽略off-diagonal E2、短spin段相互作用无spin依赖的两带混合模型，结合分支比与能隙，给odd/even V约14/17 keV、Q0,1/Q0,2允许范围1.6–2.4。2.0(4)不是本轮新拟合，也未声明Gaussian抽样意义。36/44 keV本身只约束两能级模型的|V|上限。 | model-dependent-extraction | direct-original | printed 112502-3 Eqs.3–5 | true |
| PE06-D21-R45-2 | Table I印17ny/y实验B(E2)out/in为.3(.1)/.6(.1)，计算.33/.70；18ny/y为.22(.09)/<.08，计算.17/.062。其α17=.118、α15=.894、α18=.099、α16=.427；α定义以Eq.1的yrast中原带1振幅为准，不能由数字印在ny行就擅自改成互补振幅。 | table-and-convention | direct-original | printed 112502-3 Table I | true |
| PE06-D21-R45-3 | Table I caption明确实验分支数据来自Ref.11；Ref.11在本论文末列to be published。Ref.9的寿命/带内B差异被本文作qualitative agreement对照。本文是已有数据的批判分析，不是独立再采集的一套寿命，也不自动取得Ref.11底层Cov。 | source-lineage | direct-original | printed 112502-4 Ref.11 | true |
| PE06-D21-R45-4 | 作者结论反对所分析两带的简单手征解释，同时明确所用transition moments不基于rigid shape假设，并以questionable if and to what extent a reminiscence of the chiral geometry提问。因此不能把结果改述成所有动态手征或任何手征几何残余均被排除。136Pm仍需电磁跃迁几率检验。 | author-conclusion-and-scope | direct-original | printed 112502-4 conclusion | true |

### 身份明确后的有界复算

本任务由Eqs.4/5手动实现前向比值，假设Q比2，回用印刷α，未做新拟合。17→15跨越原带与yrast身份交换：α17很小，yrast17主要原带2；α15很大，yrast15主要原带1。因此原带连续性的in/out与Eqs.4/5按y/ny终态写出的分子分母互换。直接代入得2.9952/1.4214，取倒数得到Table I的.33387/.70352。18→16的两端α均小，不交换，得.17038/.062384。此身份解释为本任务按Eqs.1–5/Table I的重建，不伪装作者另写的一条原句；只验证这四个前向计算，不认证全部八行或重拟合V。

脚本`system/scripts/day21_checkpoint045_mixing_labels.py`→本run `mixing-label-scope-045.json`。不按yrast/原带身份追踪而机械叫“out/in”会引入比值倒数错误。Q范围平方为2.56–5.76，仅是采用相应transition-moment约定时未混合E2强度的条件换算，不是实测混合能级B比的区间、beta比或新CI。UC势能图与本解混合分析是不同模型层，作者说“不依赖rigid shape”不等于无模型输入。

对[[mukhopadhyay-2007-135nd-chiral-vibration-static]]的作用仅是约束理想伙伴解释的检验方式；134Pr的分支、寿命与Cov均不能借给135Nd。两篇不同核的结果不构成同一核机制的独立重复实验证据。

## Day21 checkpoint110：134Pr两带解混合模型假定与135Nd手征判据对账

124定向纠正：用PE06-D21-R45-1至4；B的平方根仅在共同几何条件下对应矩比，不能当135Nd内禀形变测量，未重拟合V。本节旧全文与脚本保留为历史，不恢复原件阅读/科学认证。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PE06-D21-R110-1 | superseded：124撤回本条过强科学认证；用PE06-D21-R45-1至4；B的平方根仅在共同几何条件下对应矩比，不能当135Nd内禀形变测量，未重拟合V；旧全文保存在superseded-124。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |
| PE06-D21-R110-2 | superseded：124撤回本条过强科学认证；用PE06-D21-R45-1至4；B的平方根仅在共同几何条件下对应矩比，不能当135Nd内禀形变测量，未重拟合V；旧全文保存在superseded-124。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |

## Day 25 正式核准：近简并反例、解混合模型与手征判据界限

Day 25 学习主线对本源进行了正式深度复核与核对。本篇确立了手征双重带研究中至关重要的反例事实：在自旋 $I=13–19$ 区间，134Pr 的能级近简并是由多个 4-qp crossings 压缩能隙造成的表观现象，绝非理想手征对称性的充分证据。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PE06-D25-001 | 134Pr 在 $I=14–18$ 间能隙虽小（36与44 keV），但两带 alignment 差约 $2\hbar$；两带解混合模型结合实测分支比给出内禀四极矩比值 $Q_{0,1}/Q_{0,2} = 2.0(4)$（允许区间1.6–2.4），证伪了两带具有相同内禀形状的理想手征假设。 | counter-evidence-and-unmixing | direct-original-and-model | PRL 96, 112502 PDF pp.1–3, Table I | true |
| PE06-D25-002 | 两带解混合模型假定相互作用矩阵元在奇/偶自旋分别固定（$|V| pprox 14/17	ext{ keV}$），且忽略了非对角 $E2$ 矩阵元；作者反对简单理想手征带模型，但明确指出不能因此排除手征几何残余或动态手征涨落的存在。 | model-scope-and-author-boundary | direct-original | PRL 96, 112502 PDF pp.2–4 | true |
| PE06-D25-003 | 134Pr 的分支比来自文献 Ref. 11，寿命定性对照来自 Ref. 9（Tonev 2006）；两组数据来自不同实验与处理，强调内禀四极矩不对称的判断必须结合寿命与分支比，单凭能谱简并不足以建立模式归属。 | data-lineage-and-companion-observables | direct-original | PRL 96, 112502 PDF p.4, Refs. 9, 11 | true |
