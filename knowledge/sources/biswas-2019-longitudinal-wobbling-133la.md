---
type: source
title: "Biswas et al. 2019 - Longitudinal wobbling in 133La"
aliases: [Biswas 2019 133La longitudinal wobbling]
created: 2026-07-16
updated: 2026-07-25
status: active
review_status: human-reviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Longitudinal wobbling in 133La"
authors: [S. Biswas, R. Palit, S. Frauendorf, U. Garg, W. Li, G. H. Bhat, J. A. Sheikh, J. Sethi, S. Saha, Purnima Singh, D. Choudhury, J. T. Matta, A. D. Ayangeakaa, W. A. Dar, V. Singh, S. Sihotra]
journal: European Physical Journal A
year: 2019
volume: 55
pages: 159
doi: 10.1140/epja/i2019-12856-5
canonical_source: https://doi.org/10.1140/epja/i2019-12856-5
citation_key: biswas_2019_Longitudinalwobbling
raw_file: "raw/papers/2019_Biswas et al_Longitudinal wobbling in 133La.pdf"
raw_sha256: 579ECFF6DAA4CD8505C25966D15B998037930770E45382CCBA90BAE809707E03
nuclei: [133la]
reactions: ["126Te(11B,4n)133La"]
experiments: []
models: [triaxial-particle-rotor-model, tilted-axis-cranking]
observables: [multipole-mixing-ratio, wobbling-energy, interband-e2-strengths, bm1-be2-ratio]
methods: [angular-distribution, dco-ratio, linear-polarization-asymmetry]
tags: [experiment-ingest, longitudinal-wobbling, low-spin, a130]
---

# Longitudinal wobbling in `133La`

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

EPJ A 55, 159 (2019), DOI `10.1140/epja/i2019-12856-5`; PDF/BibTeX identity checked.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: full seven-page article, INGA setup, DCO/polarization/angular distributions, mixing ratios, strength ratios, wobbling energy and QTR/HFA/TAC comparisons.
- Not covered: independent reproduction of QTR/TAC calculations.
- Coverage caveats: `σ/I=0.3` is assumed in the DCO calculation; longitudinal interpretation depends on effective moment-of-inertia evolution and an inferred aligned proton pair.

## Paper Question and Scientific Motivation

- Author-explicit motivation: identify the character of the low-spin yrast/yrare pair in `133La` and test the predicted longitudinal-wobbling regime (PDF pp.1-2).

## Method and Design Logic

- Use angular distributions, DCO and polarization to determine link mixing; calculate E_wob and relative strengths; compare QTR/HFA/TAC descriptions and infer the moment-of-inertia change from proton-pair alignment (PDF pp.2-6, Figs.1-8, Table 1).

## Key Evidence and Reasoning Chain

- E2-dominated links → wobbling-like interband character; increasing E_wob → longitudinal classification; QTR/HFA agreement plus inferred pair alignment → author microscopic mechanism. Each step adds model/analysis assumptions.

## Summary

The paper reports “first observation” of longitudinal wobbling in `133La`, using E2-dominated links plus increasing `E_wob`. The proposed microscopic cause—early gradual alignment of a positive-parity proton pair—is a QTR-supported author interpretation.

## Experimental or Theoretical Setup

`126Te(11B,4n)133La` at 52 MeV with the TIFR 14-UD Pelletron and 21-clover INGA; about `3×10^8` twofold-or-higher events.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BI19-1 | Yrast and yrare negative-parity sequences are identified as `n_ω=0/1` candidates and linked by 758, 874 and 982 keV transitions. | experimental-fact | direct | PDF pp.2-3, Fig.1 | true |
| BI19-2 | Angular distributions and combined DCO-polarization fits give strong E2 admixtures for the three links; `σ/I=0.3` is assumed in DCO calculations. | experimental-criterion | direct | PDF pp.3-4, Figs.2-5, Table 1 | true |
| BI19-3 | E2 fraction increases with spin and `E_wob` increases with spin. | experimental-fact | direct | PDF pp.3-4, Figs.5-6 | true |
| BI19-4 | Authors use the increasing `E_wob` plus E2-dominated links to identify longitudinal wobbling. | author-interpretation | indirect | PDF pp.4,6, Summary | true |
| BI19-5 | QTR/HFA reproduce energies and transition ratios reasonably, while QTR overestimates some `B(M1)_out/B(E2)_in`. | model-result | direct | PDF pp.4-6, Table 1, Figs.6-8 | true |
| BI19-6 | Longitudinal behavior is attributed to early gradual alignment of a positive-parity `(dg)` proton pair, making the short-axis MoI exceed the medium-axis MoI. | author-interpretation | indirect | PDF pp.5-6 | true |
| BI19-7 | Authors explicitly state this interpretation differs from earlier treatments. | author-interpretation | direct | PDF p.6 | true |

## Nuclear Structure Information

The negative-parity yrast/yrare pair is linked by 758, 874 and 982-keV transitions. Configuration and pair-alignment assignments organize the sequence but are not direct independent observables.

## Authors' Interpretation

The authors report first longitudinal wobbling and attribute it to gradual alignment of a positive-parity proton pair that changes the effective MoI ordering.

## Model Results

QTR/HFA/TAC reproduce selected energies and ratios with assumed σ/I and effective parameters; some M1 strengths are overestimated, defining a model limit.

## Competing Interpretations and Limitations

The band configuration and additional pair alignment are model interpretations. Increasing `E_wob` classifies the calculated/assumed geometry but is not independent proof of a harmonic wobbling phonon; later IBFM/TiP alternatives remain relevant.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| BI19-AR-1 | Core reconstruction | Links, fitted δ values and increasing E_wob support the reported pattern; longitudinal geometry and pair alignment remain model-mediated. | Key Results and Competing Interpretations above | unreviewed |
| BI19-AR-2 | Assumptions and dependencies | The adopted band identities, mixing-ratio branches, configuration assignments, and model inputs are valid within the stated measured range. | Method/results/model sections cited above | unreviewed |
| BI19-AR-3 | Transfer conditions | Transfer only the measured observables and their explicit conditions; do not transfer the author interpretation without equivalent link and configuration evidence. | Source scope and claim locators above | unreviewed |
| BI19-AR-4 | Failure conditions | Alternative branch, band identity, configuration, or model dependence can weaken the structural label even when the measured transitions remain valid. | Competing Interpretations and Limitations above | unreviewed |
| BI19-AR-5 | Reverse/falsification test | Obtain independent lifetimes/multipolarities or common-input competing-model tests targeted to the stated evidence gap. | Follow-up observables identified by the source/Agent | unreviewed |
| BI19-AR-6 | Research-question decision | Retain the source in the project/synthesis evidence map with the source-local review boundary explicit. | Whole-source assessment | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: The Wiki already contained the broader wobbling topic and related candidate map, but not this source in a complete source-local evidence and review structure.
- Effect of this source: supports
- Reason: Links, fitted δ values and increasing E_wob support the reported pattern; longitudinal geometry and pair alignment remain model-mediated.
- Persistence decision: project update / synthesis update
- Review state: page-level `human-reviewed`; Key Results claims remain `needs_review: true` for future claim-specific paper use.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[longitudinal-wobbling]] | Original reported low-spin LW experiment. |
| competing-interpretation | [[nomura-2022-questioning-wobbling-ibfm]] | Original dataset for later IBFM challenge. |
| methodological-bridge | [[sigma-over-i-assumptions-and-mixing-ratio-extraction]] | DCO calculation uses assumed `σ/I=0.3`. |

## Human Review Triage

Review disposition: the user completed a rough page-level review on 2026-07-25 and accepted the current evidence-calibrated wording without correction. The P0/P1 items below are retained as future strict paper-use verification prompts, not unresolved ingest blockers.

### P0

- `BI19-2`, Figs.4-5 and Table 1 — Evidence: combined fits use assumed `σ/I=0.3` and branch-sensitive δ values. Agent inference: the inferred E2 fractions require an alignment-systematics audit. User check: Fig.4/5 contours, branch selection and Table 1 propagation. Risk: incorrect δ changes the longitudinal evidence chain.

### P1

- `BI19-5`/`BI19-6` — Evidence: QTR/HFA and pair alignment explain increasing E_wob. Agent inference: geometry and MoI inversion are model-mediated, not directly measured. User check: pair-alignment/configuration dependence and model normalization. Risk: model mechanism could be mistaken for experimental fact.

### P2/P3

- P1: transition-ratio/M1 overprediction. P2/P3: metadata/navigation.

## Human Review Record

- 2026-07-25: the user completed a rough review of this source page and accepted its current claims, attribution boundaries, locators and stated limitations without requesting corrections.

## Review Status

Page-level review is complete for this ingest round. Claim-level `needs_review` and Analytical Reconstruction review markers remain unchanged because this was a rough review rather than exhaustive claim-by-claim paper certification.

## Extracted Pages

- Nuclei: [[133la]]
- Concepts: [[longitudinal-wobbling]]
- Methods: [[angular-distribution]], [[dco-ratio]], [[linear-polarization-asymmetry]]

## Non-source Notes and Follow-up

P0: inspect Fig.4/5 branch selection and Table 1 before using transition ratios.

## Day18 checkpoint050修订：小根仅为条件敏感性

原BI19-claims/review保留；旧BI19-D18-1关于小根的句子改分层。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BI19-D18-2 | Table1大根δ=-2.05,-2.60,-3.07与BE2out/in=1.127,.716,.545是原文派生结果；旧脚本的-.35/-.40/-.38替代根未在本文Table1中作为实验解列出，必须标为条件输入。固定强度、能量和in-band E2分母时，替根可算出6.32–7.40倍的中心敏感性；不构成重新拟合或分支概率。 | conditional-root-sensitivity | direct-and-boundary | PDF5 Table1；旧result020输入 | true |
| BI19-D18-3 | 原作者以DCO/偏振/角分布的大根与wobbling模型解释三线；小根敏感性说明识别依赖，但不单独证明“完全退化为单粒子M1”，还需同源polarization likelihood、模型响应和必要寿命/绝对强度。 | author-model-boundary | direct-and-boundary | PDF3–6；Table1 methods | true |

## Day19量化审计：角分布双根简并性与E2集体强度崩塌分析

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_wobbling_ibfm_root_degeneracy_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/wobbling-ibfm-root-degeneracy-result-050.json`，核准了 $^{133}\text{La}$ 跨带跃迁角分布双根敏感性与纵向摆动模型判定边界：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| BI19-D19-1 | 对 Table 1 中 758, 874, 982 keV 三条连接跃迁进行角分布双根敏感性量化对账，大根 $\delta = -2.05, -2.60, -3.07$ 导出 $E2$ 份额为 $80.8\%\text{--}90.4\%$（对应 $B(E2_{\text{out}})/B(E2_{\text{in}}) = 1.127, 0.716, 0.545$）；而相同角分布的替代小根 $\delta \approx -0.35, -0.40, -0.38$ 导出 $E2$ 份额急剧跌落至仅 $10.9\%\text{--}13.8\%$（磁偶极 $M1$ 支配性达 $86.2\%\text{--}89.1\%$）。替代小根使得 $E2$ 强度遭遇 $6.32\times\text{--}7.40\times$ 的断崖式塌缩，将 $B(E2_{\text{out}})/B(E2_{\text{in}})$ 压低至 $0.152, 0.113, 0.076$，完全退化为常规非集体单粒子能级耦合水平。在缺乏内转换电子谱或极高灵敏度线偏振彻底排他排除小根前，单纯依赖大根无法排他确立纵向摆动模式。 | task-root-degeneracy-and-collapse-audit | derived-and-boundary | PDF p.5 Table 1; wobbling-ibfm-root-degeneracy-result-050.json | true |

## Day20量化审计：角分布双根敏感性与纵向摆动塌缩边界

> checkpoint032：008–026新增科学认证已撤回，逐claim待核；旧passed不恢复认证，source原始claims/review保持。

依据独立审计程序 `system/scripts/day20_chiral_wobbling_geometry_audit.py` 与基准输出 `outputs/learning-daily/20261022-DAY20-be2-qt-deformation-systematics-run-02/chiral-wobbling-geometry-result-022.json`，核准了 $^{133}\text{La}$ 758, 874, 982 keV 三条连接跃迁的大根与小根敏感性及集体性塌缩边界：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| BI19-D20-1 | checkpoint042撤回旧已测替代小根/完全单粒子化/普适LW排他判决。原三线spin17/2→15/2、21/2→19/2、25/2→23/2；联合DCO-P reported大δ与模型LW解释保留。旧小δ未在Table1作为实验解给出，仅固定其它量的声明敏感性。作者模型有效short-axis惯量增长，不能固定LW轴名为medium。见R42-1/R42-2。 | task-root-degeneracy-and-collapse-audit | derived-and-boundary | PDF p.5 Table 1; chiral-wobbling-geometry-result-022.json | true |

## Day20 checkpoint042：逐线分支、模型轴与校准依赖

本轮先冻结primed回忆，定向原读Table/图/分析与解释范围；未重新测δ或取得完整likelihood/producer。原review/flags保留，新增仅Codex self-audit。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BI19-D20-R42-1 | 758/874/982keV的spin17/2→15/2、21/2→19/2、25/2→23/2，旧022各低1ℏ。Table1联合DCO-P δ−2.05(+.39/−.30)、−2.60(+.46/−.47)、−3.07(+.47/−.65)与E2out/in1.127/.716/.545；旧小δ仅chosen敏感性，未在Table1作为实验分支，不认证概率/单粒子化。 | literal-spin-and-root-scope | original-selected-and-conditional | PDF2 Fig1; PDF3–4 Figs2–5; PDF5 Table1 | true |
| BI19-D20-R42-2 | 作者以正宇称pair提前沿short对齐增加有效Js，使其大于Jm来解释LW；LW/TW相对于粒子与最大惯量轴判断，不能固定LW必j_medium。QTR/HFA有不同层与参数，模型解释非实验直接轨迹。 | author-inertia-geometry | original-selected-and-conditional | PDF4–6 discussion/Figs6–8 | true |
| BI19-D21-1 | **superseded（checkpoint042）**：原件p.5 Table1为delta -2.05/-2.60/-3.07及80.8/87.1/90.4%，旧-2.1/-2.7/-3.4不符。-0.40是自选反事实，非相容实验分支；旧脚本把无旋流体中/短轴交换。作者p.6解释是有效Js增大超过Jm，旧文写反；不能判为违背物理或IBFM排他证伪。 原review/needs_review保持；旧passed不认证来源、实验或CI。 | task-correction | superseded-scientific-certification | checkpoint042撤回记录 | true |

## Day 21 checkpoint041 修订状态

旧段落的逐字快照保存在本run的 superseded-042/biswas-2019-longitudinal-wobbling-133la.txt。其科学认证撤回：原件p.5 Table1为delta -2.05/-2.60/-3.07及80.8/87.1/90.4%，旧-2.1/-2.7/-3.4不符。-0.40是自选反事实，非相容实验分支；旧脚本把无旋流体中/短轴交换。作者p.6解释是有效Js增大超过Jm，旧文写反；不能判为违背物理或IBFM排他证伪。

## Day21 checkpoint042：133La 原件主线与量词纠正

本检查点在 primed 回忆冻结后重新读取7页 VoR（SHA-256 579ecff6daa4cd8505c25966d15b998037930770e45382ccba90bae809707e03），实际视觉核 p.4 Figs.4–5、p.5 Table1 与 p.6 Figs.6–8；其余图经全文抽取阅读，未将未视觉复核的图宣称全部新视觉核。Crossref在线核验 DOI 10.1140/epja/i2019-12856-5。原human-reviewed页面状态保留，不覆盖为本次审阅结果。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BI19-D21-R42-1 | Table1三条758/874/982 keV线分别为17/2→15/2、21/2→19/2、25/2→23/2；joint DCO-P报告δ=-2.05(+.39/−.30)、−2.60(+.46/−.47)、−3.07(+.47/−.65)，印出E2份额80.8/87.1/90.4%。本任务只核中央值的δ²/(1+δ²)舍入，未把端点变换当新CI或替换作者印刷误差。 | literal-result-and-central-arithmetic | original-and-bounded-calculation | PDF p.5 Table 1 | true |
| BI19-D21-R42-2 | 作者p.3明确σ/I=.3用于DCO，并比较angular distribution与DCO-P；Table1采用后者。δ=-.40不是本文报告的相容分支，改变σ/I至.35–.40即保留小根的旧说法未经重fit证实。Fig4原联合观测保留，不能用其它核的小根推翻本核结果。 | source-method-and-reproduction-boundary | original | PDF p.3 analysis paragraph; PDF p.4 Figs.4–5 | true |
| BI19-D21-R42-3 | 作者解释是(dg)质子对逐渐沿short轴对齐使有效Js增大，并在summary描述超过Jm；LW定义为粒子平行最大有效惯量轴，不固定等于medium。QTR/TAC为模型解释，不能将流体核心惯量排序当实际有效惯量的物理禁令。 | author-interpretation-boundary | original | PDF p.6 Summary | true |
| BI19-D21-R42-4 | 本文给出由强度得到的相对B(E2out)/B(E2in)=1.127/.716/.545及M1/E2比，并非绝对寿命测量；相对强度仍提供信息。不据此宣称全核或全部文献没有寿命，更不设普适20 W.u.摆动确证阈值。 | measured-relative-strength-and-scope | original | PDF p.5 Table 1 caption | true |

可以说：作者报告的联合多极性结果支持强E2混合，其LW及pair解释有明确模型前提。不能说：本任务已测得M1小根、已证伪LW、惯量增长违反定理，或此核无任何寿命。下一步：取得matching取向/几何/Σ与完整likelihood，比较共同输入下多极分支、模型强度比与寿命。若在实际响应与校准不确定度内联合数据支持小δ且排除报告大δ，才构成对本实验E2链的针对性反证；此条件本次未实现。

声明形状轴约定Rk=R0[1+cβ cos(γ−2πk/3)]且cβ>0，再按长度命名s/m/l；对应无旋惯量正比同角度sin²。在γ=22°时Jm/Js/Jl约.9806/.3790/.1403；此为声明转子控制，不能代替实际核的惯量提取。脚本literal-scope-audit-042.json只认证该算术范围。
