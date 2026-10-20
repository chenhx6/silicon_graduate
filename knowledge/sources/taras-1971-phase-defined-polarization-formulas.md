---
type: source
title: "Gamma-Ray Linear Polarization and Angular Distribution Formulas in Terms of Phase-Defined Reduced Matrix Elements"
aliases: ["Taras 1971 phase-defined mixing ratios", "Taras polarization angular distribution formulas"]
created: 2026-09-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: theory
reading_depth: deep-read
title_original: "Gamma-Ray Linear Polarization and Angular Distribution Formulas in Terms of Phase-Defined Reduced Matrix Elements"
authors: ["P. Taras"]
journal: "Canadian Journal of Physics"
year: 1971
citation_key: taras_1971_GammaRay
volume: 49
issue: 3
pages: "328-351"
doi: "10.1139/p71-039"
language: en
canonical_source: "Taras, P. Gamma-Ray Linear Polarization and Angular Distribution Formulas in Terms of Phase-Defined Reduced Matrix Elements. Can. J. Phys. 49, 328-351 (1971)."
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1971_Taras_Gamma-Ray Linear Polarization and Angular Distribution Formulas in Terms of Phase-Defined Reduced Ma.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1971_Taras_Gamma-Ray Linear Polarization and Angular Distribution Formulas in Terms of Phase-Defined Reduced Ma.pdf"
raw_sha256: "151e8a5274e3f9f510f3884a0e5e20a0ca8c9d883d609fe18ab7b4fb669e8a5d"
nuclei: ["35Cl", "19F", "26Mg", "29Si", "37Ar"]
models: ["Rose-Brink-formalism"]
observables: ["linear-polarization", "angular-distribution", "multipole-mixing-ratio", "statistical-tensor"]
methods: ["angular-distribution", "linear-polarization-asymmetry", "multipole-mixing-ratio"]
tags: [phase-defined-matrix-elements, mixing-ratio-sign, angular-distribution, gamma-polarization, statistical-tensor]
---

# Gamma-Ray Linear Polarization and Angular Distribution Formulas in Terms of Phase-Defined Reduced Matrix Elements

## Bibliographic Record

- 作者：P. Taras。
- 期刊：*Canadian Journal of Physics* 49(3), 328-351 (1971)。DOI：`10.1139/p71-039`。
- 原始文件：`raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1971_Taras_Gamma-Ray Linear Polarization and Angular Distribution Formulas in Terms of Phase-Defined Reduced Ma.pdf`；SHA-256：`151e8a5274e3f9f510f3884a0e5e20a0ca8c9d883d609fe18ab7b4fb669e8a5d`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: PDF pp.328-351 全文；phase-defined Rose-Brink matrix elements、statistical tensors/population parameters、angular-distribution Z coefficients、mixed-multipole formulas、linear-polarization relation、Litherland-Ferguson methods I/II、particle-gamma capture and particle-X-gamma capture cases、finite counter size and application discussion均已阅读。
- Not covered: 引用论文全文和原文 Appendix 表格的逐项数字转录。
- Coverage caveats: 公式 PDF 部分为 OCR/扫描层；论文级公式转引需回页面核对相位和系数索引。本文的重点是 phase convention consistency，不是某一核素的最终实验结论。

## Paper Question and Scientific Motivation

- 论文解决的核心问题是：如何把 γ 角分布、线偏振和 multipole mixing ratio `δ` 统一写在 Rose-Brink phase-defined reduced matrix-element convention 下，使 `δ` 的大小和符号可与核模型预测一致比较（摘要；PDF pp.328-329）。
- 作者强调，若不同实验使用不一致的 reduced-matrix-element phase convention，混合比符号会被错误解释，并可能导致错误的 polarization 参数。

## Method and Design Logic

- 初态是沿束流轴取向的 aligned state；磁子态 population `P(m)` 与 statistical tensors `p_k0` 通过 Clebsch-Gordan 变换互换。alignment condition 使奇 k tensors 消失（PDF p.329，式 (4)-(5)）。
- 角分布写成 statistical tensors、Z coefficients 和 phase-defined reduced matrix elements 的组合；混合跃迁的干涉项保留 `δ` 的相位和符号（PDF pp.329-334，式 (2)-(21)）。
- 论文分别处理 unobserved-particle angular distributions、Litherland-Ferguson particle-gamma angular correlations、particle-gamma capture 和 particle-X-gamma capture，并讨论有限粒子计数器对 population parameters 的限制（PDF §§3.2-3.5）。

## Key Evidence and Reasoning Chain

1. 线偏振和角分布共享同一 phase-defined reduced matrix elements；因此从两类数据提取的 `δ` 必须使用同一相位 convention（PDF pp.328-329）。
2. Dipole-quadrupole mixtures 只出现到 `P4(cosθ)`，公式可同时用于 M1/E2 与 E1/M2；quadrupole-octupole mixtures 则加入相应更高 Legendre terms（PDF pp.333-334）。
3. 某些反应方法只允许有限 `m` populations，能唯一确定 statistical tensors；在不利情况下只有 `a2/a0`、`a4/a0` 两个系数，任意 `δ` 可能都能拟合，必须引入偏振或额外约束（PDF pp.334-335）。
4. 作者用一个近期 γ polarization measurement 展示 phase-consistent formulas 如何识别异常 inhibited transition；“预期 transition probability”不能替代直接 parity/polarization measurement（PDF pp.328-329）。


### Day17原件新增自审

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| T71-D17-1 | 原24页以RB phase/SharpZ的统一为主，35Cl1763 Table5/Fig2复述TarasMatas1969数据；不是本篇另一次独立采集。原3162 inhibitedE1动机和1763→ground示例不能按levelenergy混成同条γ。 | source-identity-and-independence | direct-and-self-audit | printed328 Introduction; printed344 Sec4.6 Table5 | true |
| T71-D17-2 | 原pko=fullstatisticaltensor，B=sqrt(2J+1)pko，p00=1/sqrt(2J+1)；m≥0 P为folded±M权重且sum1，逆变换2−δm0。只在alignedevenk域用折叠式，不拿它逐odd项计算任意orientedρ。 | normalization-and-domain | direct-and-self-audit | printed329 Eq1–5 | true |
| T71-D17-3 | 新parityindependent Z与旧Sharp/MethodII符号分层；Table2的δRB/−δBR须带emission/order，footnote8说明unobserved第一x与observed第二δ在BR比较不同号，不能全cascade只全局翻号。 | phase-and-role-boundary | direct-and-self-audit | printed330–331 Table1–2; printed337 footnote8 | true |
| T71-D17-4 | MethodII particle需0°或180°annular沿axis，只有m受限1/2或0的理想geometry才给unique tensor；finiteparticlecounter可布居higherm，精确修需formation/decaymatrix。19F例5%是假设对照，非通用correctionprior。 | method-and-finite-acceptance-boundary | direct-and-self-audit | printed334–335 Sec3.3 | true |
| T71-D17-5 | simpleAD/MethodII无需isolatedcompoundresonance；capture/cascadecases Sec3.4/3.5则限定isolatedresonance，singlepartialwave/channels等条件决定pop是否已知。不能把各反应类的前提互移。 | reaction-scope | direct-and-self-audit | printed335–337 Sec3.3–3.5 | true |
| T71-D17-6 | angularQk是finitecounter逐rank attenuation，不是instrument sensitivity；completeunobservedγ的Uk权重无interference、U0=1，但finitegate不等该trace，γ与totalICCbranch另匹配。 | response-and-trace-boundary | direct-and-self-audit | printed331 finitecounter discussion; printed337 Eq25–31 | true |
| T71-D17-7 | 同reaction/beamenergy且匹配条件的AD/P才能消同pko；作者建议同时测以减target/energy/resonance变化，长寿命perturbation亦需共享effective tensor，不自动消不同timing/feeding/response与Cov。 | companion-input-boundary | direct-and-self-audit | printed339 Sec4.1; printed341 Sec4.3–4.4; printed343 Sec4.5 | true |
| T71-D17-8 | 原p=J0/J90为ratio，R是Comptonσ90/σ0，N90/N0经Eq49与p相连；不是boundedP/A同量。footnote9指出Ω与φ物理意义不同，不按两个极值同0/90便混轴。 | observable-convention | direct-and-self-audit | printed338 Eq34; printed343 Eq49 footnote9 | true |
| T71-D17-9 | Table5原a2=−.369(.009)/a4=.213(.013)已finitecountercorrect、a0=1；NaI polarimeter/30ccGeAD在Ep3.115MeV的35Cl(p,p′γ)原例，γ1763→ground3/2+。 | reported-experiment | direct-and-self-audit | printed344 Table5 Sec4.6 | true |
| T71-D17-10 | Table5 R1.683(.017)列名calculated、N1.22(.01)、p2.30(.08)派生同链，不是三独立偏振测量。roundedR/N推p2.27486，printedp/R隐N1.22292可round1.22；localσp独立假设.09385，任意R/Ncorr可.04675–.12421，未取原Σ故不判印σ错误。 | reported-input-and-task-uncertainty | direct-and-self-audit | printed343 Eq49; printed344 Table5 | true |
| T71-D17-11 | 独立按sourceZ/Eq19/5的Table5 central replay给M1E2 δ2.683292/−.730446，E1M2 δ−.018784/104.34452；后者高M2份额.999908非数学∞。原pureM2表述保source近极限边界，不宣称原误差band已重放或实验矛盾。 | bounded-central-replay | direct-and-self-audit | printed333 Eq19; printed339 Eq39; printed344 Table5 | true |
| T71-D17-12 | 同centralAD自由foldedq反演，δ2.68329给q(.5,1.5,2.5)=(.703038,.240032,.056930)；其它central三候选各有负q。支持作者本例正性排根，但不是新Jπ/δ测量或jointCI。 | task-calculation-and-author-comparison | direct-and-self-audit | printed329 Eq5; printed344–345 Sec4.6 Fig2 | true |
| T71-D17-13 | centralAD完整正q域约[−15.83207,−.95118]与[.789966,3.042736]；原text排区−1到.73/3.27到∞口径未以完整误差recipe复现，不能拿central边界当原错误或真实CI。 | task-domain-and-statistical-boundary | direct-and-self-audit | printed344 Sec4.6 population paragraph | true |
| T71-D17-14 | 作者将a4非零/βlogft4.7(.3)与positivepopulation用于J5/2、再称排7/2；本任务只复算5/2→3/2中央族，未取a6/全spinfit/原βprimary或完整Σ，不能独立认证其全部J排除。 | author-interpretation-and-readiness | direct-and-self-audit | printed344–345 Sec4.6 | true |
| T71-D17-15 | 本session核Table3九K值、Table4六列十角60值、Table6五targetrow15Z值和Table7八CG，共92值。初Table4两个任务误读已高清原件纠为40°9.7674、80°P4=.2659，非sourceprintingfailure。 | source-table-crosscheck | direct-and-self-audit | printed341 Table3; printed342 Table4; printed346 Table6; printed349 Table7 | true |
| T71-D17-16 | source另举J3/2→3/2 δ≈.26或∞时ADisotropic但finiteδ p≠1、purelimit p1；不是VT74本session3/2→1/2两个finite根，二者不合并。第二角P可增加信息但取决于误差/角变化，非总保证唯一。 | theoretical-counterevidence | direct-and-self-audit | printed340–341 Sec4.1–4.2 | true |
| T71-D17-17 | 原MethodII示例为26Mg(α,nγ)29Si，质量/电荷与原文一致；旧Wiki nuclei的28Si修29Si，并补实际37Ar示例，非本run新测量或新核素指认。 | Wiki-identity-correction | direct-and-self-audit | printed335 Sec3.3; printed341 Sec4.3 | true |
| T71-D17-18 | 仅声明Table5 a2/a4各±所印sigma的矩形与positivefoldedq模型，新exactQQ算法26因子/51实根分52open cells，另31临界点与∞精确分类，无额外孤立点；完整条件ADbox域约[−17.590797,−.897283]∪[.750180,3.118689]。非原jointCI/误差recipe。 | task-feasibility-proof | derived-and-exact-cell-audit | printed344 Table5; Eq5 Eq19 | true |
| T71-D17-19 | 对同ADbox，literalpureM2极限p=(1−2a2−a4/4)/(1+a2+a4)范围1.920901–2.075426，与所印p±sigma箱2.22–2.38不交。它只限当前point/box解释，不能把近pure有限根或原误差band改称实验冲突。 | task-necessary-bound | derived-from-printed-marginals | printed340 Eq43–44; printed344 Table5 | true |
| T71-D17-20 | 当前1sigma-marginalbox也未重现作者.73/3.27口径，不反推作者实际用了哪个Cov/误差倍数或修表；原1969body/actualΣ/acceptance/producer仍缺。当前positivitybox仅AD，未完成finiteδ jointPbox的置信分析。 | analysis-readiness-boundary | direct-scope-plus-task-audit | printed344 populationparagraph; printed345 Fig2 | true |

## Summary

Taras 1971 是 γ 角分布、线偏振和混合比符号一致性的基础方法来源。它把 aligned-state population、statistical tensors、Rose-Brink phase-defined matrix elements、Z coefficients 和 polarization formulas 放进同一套约定，并明确区分不同反应几何和有限 counter-size 的适用条件。对本 Wiki，最重要的边界是：`δ` 的符号不是脱离 phase convention 的可移植标签；仅有两个角分布系数通常不能唯一选定混合比分支。

## Experimental or Theoretical Setup

- Formalism for aligned nuclei produced by unpolarized particle reactions/capture。
- Cases: particle unobserved, particle-gamma angular correlation, particle-gamma capture and particle-X-gamma capture。
- Quantities: `P(m)`, `p_k0`, `Z_k`, Legendre angular-distribution coefficients, polarization and phase-defined `δ`。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| T71-1 | 混合比 `δ` 必须与 phase-defined reduced matrix elements 使用同一 convention，才能比较符号和核模型预测。 | method-principle | direct | PDF pp.328-329 | false |
| T71-2 | `p_k0` 与磁子态 population `P(m)` 通过 CG 系数变换；alignment 使奇 k tensors 消失。 | formalism | direct | PDF p.329，式 (4)-(5) | false |
| T71-3 | Dipole-quadrupole angular distributions 只包含到 `P4`，并适用于 M1/E2 和 E1/M2。 | formalism | direct | PDF pp.333-334，式 (18)-(19) | false |
| T71-4 | 在 population/geometry 不充分时，只有 `a2/a0`、`a4/a0` 可能无法唯一确定 `δ`；线偏振提供额外约束。 | limitation | direct | PDF pp.334-335 | false |

## Nuclear Structure Information

- 论文不建立单核素能级图；`35Cl`、`19F`、`26Mg`、`29Si` 仅作为方法和示例反应背景。
- 可复用内容是 mixing-ratio / parity / polarization 的证据逻辑，不是这些核素的长期结构页面。

## Authors' Interpretation

- 线偏振对 parity 和 mixing ratio 的价值来自 phase-consistent interference term；错误的 `δ` phase 会直接污染 interpretation。
- 在 population information 不足时，测量 polarization 是减少 angular-distribution 多解的必要方向之一。

## Model Results

- 不提供新的 shell-model spectrum；论文讨论如何把实验 `δ` 与核模型中 phase-defined transition matrix elements 比较。

## Competing Interpretations and Limitations

- 不同 convention、符号定义和角度坐标可产生表面上相反的 `δ` 或 polarization sign；跨来源比较必须先做 convention mapping。
- 有限 detector/particle-counter acceptance 会改变可达到的 population constraints；不能直接把理想公式用于真实阵列。
- 仅有两个 angular-distribution coefficients、未知 alignment 或混合跃迁多解时，偏振本身也需结合 DCO/角分布/寿命等证据。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-T71-1 | Core reconstruction | 该来源的核心贡献是把“混合比符号”从经验标签变为 phase-defined matrix-element convention 下的可比量。 | PDF pp.328-334 | self-checking |
| AR-T71-2 | Assumptions and dependencies | 依赖 alignment、statistical tensors、reaction geometry、counter acceptance 和 multipole convention。 | PDF §§2-3 | self-checking |
| AR-T71-3 | Transfer conditions | 公式可作为 P-ADO/DCO/polarization convention bridge；具体 sign/δ 仍需按 source 的 phase and axis definitions 转换。 | PDF §§2-5 | provisional |
| AR-T71-4 | Failure conditions | 只用少量 angular coefficients、忽略 finite counter size 或混合 branch 会导致 δ 不唯一/符号错误。 | PDF pp.334-335 | active-L3 |
| AR-T71-5 | Reverse/falsification test | 对同一 transition 用 source convention 重算 angular distribution 与 polarization，并与已知 pure E2/M1 reference 比较；若符号无法同时闭合则暂停 claim。 | PDF §§3-5 | candidate-L3 |
| AR-T71-6 | Research-question decision | 作为 mixing-ratio/polarization 方法核心来源接入方法项目，不启动 L4。 | PDF pp.328-351 | completed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki 已有 multipole-mixing-ratio、linear-polarization、ADO/DCO pages，但 phase-defined sign consistency 和 population-tensor conversion 尚未有这篇基础来源。
- Effect of this source: `foundational-background` and `methodological-bridge`。
- Reason: 该来源为后续 ADO/偏振/混合比 claims 提供统一 phase convention 和多解边界。
- Persistence decision: update [[linear-polarization-asymmetry]], [[angular-distribution]] and [[multipole-mixing-ratio]] source lists; no standalone nucleus page。
- Review state: `unreviewed`; formalism claims self-audited by Codex, not human-reviewed。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| foundational-background | [[multipole-mixing-ratio]] | phase-defined matrix elements and sign-consistent δ。 |
| methodological-bridge | [[linear-polarization-asymmetry]] | polarization and angular-distribution formulas share convention and statistical tensors。 |
| methodological-bridge | [[angular-distribution]] | `a2/a0`, `a4/a0`, finite alignment and reaction-method boundaries。 |

## Human Review Triage

### P0

- T71-P0-1：任何跨文献 `δ` 符号、electric/magnetic polarization sign 或 model comparison，必须先核对 phase convention、axis convention 和 `P(m)`/tensor definitions。

### P1

- T71-P1-1：少量 angular coefficients 下的 δ branch ambiguity；不得以单一 polarization sign 宣称唯一 mixing ratio。

### P2/P3

- 24 页公式 OCR/扫描混合；论文写作逐式引用时必须回到视觉页核对系数索引。

## Extracted Pages

- Nuclei: 不创建。
- Bands: 不创建。
- Concepts: phase-defined reduced matrix elements、statistical tensors、mixing-ratio sign。
- Methods: [[angular-distribution]], [[linear-polarization-asymmetry]], [[multipole-mixing-ratio]]。

## Non-source Notes and Follow-up

- 下一步：把 T71 的 phase/sign bridge 与 HS-011 之后的 Taras/Brink/PDCO sources 对照，检查方法页公式的 convention consistency。

## Day17原件复核：35Cl1763的positivepopulation筛选

本session先冻taras1971-before/exercise并声明旧T71/VT74/Day16phase priming，原24页328–351完整text/visual，Eq1–50、Fig1/2、Tables1–7及29bibliographicentries核主线与关键行。Appendix巨表仅结构/声明目标92系数数值复算，不称逐全部Table6/7重放。1157959bytes/hash `151e8a5274e3f9f510f3884a0e5e20a0ca8c9d883d609fe18ab7b4fb669e8a5d`保持；旧T71-1–4false与review/cite不改，20新待审。

[[cl35-1763-polarization-population-replay]]保存原Table5计数比/计算R/p派生、parity-independentZ与foldedq中央解、Σ/finiteacceptance/同1969数据谱系边界。新的script不用旧Day16模型；92typed系数核过，原任务Table4两输入误读/初结果快照完整保，不给原文添加假勘误。frozenexercise说Table3八nonempty，实际为九，冻结原文不改。

本例显示positivepopulation在实际数值/指定J和two-multipole域中可以排掉其余central候选；不把“保多解”变成永远不能选根的规则。原Table5pureM2近极限、printedpopulation区间与本任务centraldomain不同，尚无原bandrecipe/Σ/全J7/2/a6 producer，保而不自由调参数强配。MethodII同axis/finiteparticlecounter与reactionclass前提保；更强实际结论需原TarasMatas1969primary与匹配响应。

决定`supports`此source的M1E2正根中央逻辑与P/AD/正性互补，`limits`普适唯一、以p/R/N多列计独立测量、不同门pko自动相同的简写。没有新的实验Jπ/δ/P或模型升实验。

### 本session后续：AD边际误差箱的完整条件投影

T71-D17-18–20及[[cl35-1763-polarization-population-replay]]“AD边际误差箱：精确分区与原口径边界”保存同source输入的新问题。初open-only结果/脚本/合同与boundary前冻结保留，后以QQ不可约因子根域的精确sign分类补完31点和∞，不由grid称完整。原GoogleScholar新primaryquery失败且无records/body，未将snippet/metadata充原件。此步没有给实验jointCI或归因作者recipe。
