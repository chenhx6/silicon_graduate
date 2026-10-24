---
type: source
title: "Guo et al. 2020 - Pseudospin-chiral quartet bands in 131Ba"
aliases: [Guo 2020 131Ba, pseudospin-chiral quartet 131Ba]
created: 2026-08-11
updated: 2026-08-11
status: active
review_status: unreviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Evidence for Pseudospin-Chiral Quartet Bands in the Presence of Octupole Correlations"
authors: [S. Guo, C. M. Petrache, D. Mengoni, Y. H. Qiang, Y. P. Wang, Y. Y. Wang, J. Meng, Y. K. Wang, S. Q. Zhang, P. W. Zhao, et al.]
journal: Physics Letters B
year: 2020
volume: 807
pages: 135572
doi: 10.1016/j.physletb.2020.135572
language: English
canonical_source: https://doi.org/10.1016/j.physletb.2020.135572
citation_key: guo_2020_Evidencepseudospinchiral
raw_file: "raw/papers/2020_Guo et al_Evidence for pseudospin-chiral quartet bands in the presence of octupole.pdf"
raw_sha256: 109019D2EF7338BA705462374E6CF30C0CF9D61175510DD92D63021271E8F29D
nuclei: [131ba]
reactions: ["122Sn(13C,4n)131Ba"]
experiments: [galileo-131ba-c13-65mev]
models: [reflection-asymmetric-triaxial-particle-rotor-model, tac-cdft]
observables: [two-point-angular-correlation-ratio, energy-staggering-parameter, bm1-be2-ratio, angular-momentum-alignment]
methods: [gamma-gamma-coincidence, two-point-angular-correlation-ratio, angular-distribution]
tags: [experiment-ingest, project-ingest, a130, nuclear-chirality, pseudospin, octupole-correlation]
---

# Evidence for Pseudospin-Chiral Quartet Bands in the Presence of Octupole Correlations

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

Physics Letters B 807, 135572 (2020), DOI `10.1016/j.physletb.2020.135572`. The protected BibTeX key is `guo_2020_Evidencepseudospinchiral`.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`.
- Covered scope: all six pages; experiment and partial level scheme; coincidence, `R_ac` and angular-distribution constraints; positive-parity D3-D6 quartet; negative-parity D7/D8 pair; alignments, `S(I)` and branching-derived ratios; E1 links; TAC-CDFT deformation input and RAT-PRM comparison.
- Not covered: Ref.27's full channel-selection/analysis details, unpublished Ref.35, or the promised Ref.41 azimuthal plots, angular-momentum components and full RAT-PRM discussion.
- Coverage caveat: several weak in-band mixing ratios are assumed rather than measured; no lifetimes or absolute reduced probabilities are reported.

## Extracted Pages

- PDF pp.1-2: motivation, experiment, `R_ac` method, prior bands and new/extended structures.
- PDF p.3: partial level scheme, representative double gates and `R_ac` examples.
- PDF p.4: positive-quartet configuration exclusions, pseudospin argument and experimental systematics for D3-D8.
- PDF p.5: RAT-PRM inputs/results, relative E1 comparison, model discrepancy and summary.
- PDF p.6: references.

## Paper Question and Scientific Motivation

The paper asks whether one odd-A nucleus can show a same-parity four-band manifold shaped jointly by pseudospin and chiral symmetries, while a directly E1-linked opposite-parity chiral system exposes octupole correlations without an intermediary nonchiral band.

## Experimental or Theoretical Setup

- `122Sn(13C,4n)131Ba`, `65 MeV`, LNL Tandem; two self-supporting `122Sn` foils, each `0.5 mg/cm²`.
- GALILEO: 25 Compton-suppressed Ge detectors at `90°`, `119°`, `129°` and `152°`; approximately `1.2×10^9` triple-or-higher events.
- Two-point `R_ac=Iγ(152°)/Iγ(90°)` calibration: approximately `1.5` for stretched quadrupole and `0.8` for stretched dipole; Fig.3 calculations adopt `σ/I=0.24`.
- Four-angle angular distributions determine mixing ratios for most in-band M1/E2 transitions.
- RAT-PRM uses TAC-CDFT `β2=0.22`, `γ=27.1°` for the `πh11/2g7/2⊗νh11/2` reference and tentatively adopts `β3=0.05`.

## Summary

The experiment newly establishes D4 and D8 and significantly extends D3 and D5-D7. D3-D6 form a positive-parity, mutually linked four-band manifold interpreted through mixed `πh11/2(g7/2,d5/2)⊗νh11/2` configurations as the first pseudospin-chiral quartet candidate. D7/D8 form a negative-parity chiral-doublet candidate assigned `π(h11/2)^2⊗νh11/2`. Many D7-to-D3-D6 E1 links support octupole correlations between the two systems. RAT-PRM reproduces much of the energy/ratio systematics but underpredicts feeding to D5, and the promised angular-momentum geometry is not contained in this paper.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GU20-1 | The data set contains about `1.2×10^9` triple-or-higher GALILEO events from `122Sn(13C,4n)` at `65 MeV`. | experimental-fact | direct | PDF p.2, Sec.2 | true |
| GU20-2 | D4 and D8 are newly established, while D3 and D5-D7 are significantly extended in the partial `131Ba` scheme. | experimental-fact | direct | PDF pp.2-3; Figs.1-2 | true |
| GU20-3 | `R_ac` and four-angle angular distributions constrain transition character; 549-keV D6→D3 and 715/721-keV D8→D7 links are M1/E2, supporting same parity within each linked group. | experimental-fact | direct | PDF pp.2-3; Fig.3 | true |
| GU20-4 | Four positive-parity D3-D6 bands are interconnected by many M1/E2 and some weak E2 transitions; energy ordering of D4-D6 changes with spin and links connect every pair. | experimental-fact | direct | PDF pp.2-4; Figs.1,4 | true |
| GU20-5 | The paper assigns all four positive bands to the `πh11/2(g7/2,d5/2)⊗νh11/2` family using parity, signature behavior, alignments near `8-10ℏ`, neighboring-nucleus systematics and exclusion of a low-Ω-neutron alternative. | configuration-assignment | indirect | PDF pp.3-4; Fig.4 | true |
| GU20-6 | An earlier D5/D6 interpretation as two signatures of the same `πh11/2g7/2⊗νh11/2` configuration is rejected because it predicts interband ΔI=1 strengths opposite to observation. | competing-interpretation | direct | PDF p.4, Sec.3.1 | true |
| GU20-7 | D3-D6 cannot be divided into two experimental pairs uniquely by energies or links; their pseudospin-chiral quartet interpretation treats pseudospin and chiral splittings as competing, comparable effects. | author-interpretation | direct | PDF pp.1,4, Abstract and Sec.3.1 | true |
| GU20-8 | Branching-derived `B(M1)/B(E2)` values are broadly similar for D3-D6, but several have large uncertainties; staggering appears above `29/2ℏ`, with D4/D5 opposite in phase to D3. | derived-observable | direct | PDF p.4; Fig.4 | true |
| GU20-9 | D7/D8 are proposed as a negative-parity chiral pair with `π(h11/2)^2⊗νh11/2`, based on energy, `S(I)`, ratio and alignment similarities to `133Ce/135Nd`. | author-interpretation | indirect | PDF p.4; Fig.4 | true |
| GU20-10 | More than half of D7's intensity decays to D3-D6 through many E1 links, supporting octupole correlations between configurations differing by `πh11/2` versus `π(g7/2,d5/2)`. | experimental-fact | direct | PDF pp.4-5; Figs.1,5 | true |
| GU20-11 | The measured same-initial-state relative E1 pattern supports a `πd5/2` component in all four positive bands, but RAT-PRM significantly underpredicts transitions feeding D5. | model-comparison | direct | PDF p.5; Fig.5 | true |
| GU20-12 | RAT-PRM gives dominant `πh11/2g7/2⊗νh11/2` components for D3/D4, stronger `πd5/2` mixing for D5/D6 and `π(h11/2)^2⊗νh11/2` for D7/D8. | model-result | indirect | PDF p.5, Sec.3.2 | true |
| GU20-13 | RAT-PRM broadly reproduces energies, D4/D5 crossing near `27/2ℏ`, `S(I)` and ratios, but transition amplitudes feeding D5 are sensitive to nearby mixed states and not reproduced. | model-discrepancy | direct | PDF p.5; Figs.4-5 | true |
| GU20-14 | `β3=0.05` is a tentative RAT-PRM input for octupole-correlation effects, not an experimental determination or evidence of stable octupole deformation. | model-assumption | direct | PDF p.5, Sec.3.2 | true |
| GU20-15 | The paper defers azimuthal plots, angular-momentum components and the detailed RAT-PRM geometry for all three proposed pairs to a future reference. | source-completeness-boundary | direct | PDF p.5, Sec.3.2; Ref.41 | true |
| GU20-16 | For a few weak in-band transitions the analysis assumes `δ=-0.2(1)`; no lifetimes or absolute reduced transition probabilities are measured. | evidence-boundary | direct | PDF p.4, Fig.4 caption; p.5, Summary | true |
| GU20-17 | A two-same-configuration-doublet alternative is excluded only within the calculated quasiparticle mapping, not by a direct configuration observable. | model-boundary | direct | PDF p.5, Sec.3.2 | true |

## Nuclear Structure Information

| Structure | Experimental identity | Configuration/interpretation status |
|---|---|---|
| D3-D6 | four mutually linked positive-parity dipole bands; D4 new | mixed pseudospin `πh11/2(g7/2,d5/2)⊗νh11/2`; pseudospin-chiral quartet candidate |
| D7/D8 | negative-parity linked doublet; D8 new | RAT-PRM `π(h11/2)^2⊗νh11/2`; chiral-doublet candidate |
| D7→D3-D6 | many E1 links and relative E1 ratios | octupole-correlation evidence; not stable octupole deformation |

## Competing Interpretations and Limitations

- The experimental four-band manifold is secure, but its decomposition into two chiral pairs and two pseudospin sectors is not uniquely defined by energy or links.
- Common-configuration and pseudospin-component assignments rely on systematics, alignment exclusions and RAT-PRM wavefunctions.
- The key chiral angular-momentum geometry is deferred; energy/`S(I)`/ratio similarity remains nonunique.
- Branching-derived ratios depend on angular-distribution mixing ratios, including assumed values for weak lines, and lack lifetime normalization.
- E1 links support reflection-asymmetric correlations but do not determine a static `β3`; the model's `β3=0.05` is tentative.
- D5 is a visible model stress point in relative E1 feeding and state mixing.

## Analytical Reconstruction

| ID | Audit item | Agent judgment | Evidence / locator | review_status |
|---|---|---|---|---|
| AR-1 | Core reconstruction | The durable experimental result is a six-band, two-parity linked manifold; “two positive chiral pairs plus one negative pair” is an experiment-model interpretation. | GU20-2 to GU20-10 | unreviewed |
| AR-2 | Quartet identifiability | D3-D6 should persist as one four-band object because the paper explicitly cannot pair them uniquely from energies/links. | GU20-4/7 | unreviewed |
| AR-3 | Octupole scope | Direct E1 connectivity supports octupole correlations between the proposed systems, not stable reflection-asymmetric deformation. | GU20-10/11/14 | unreviewed |
| AR-4 | Geometry gap | RAT-PRM agreement strengthens configuration consistency but cannot replace the missing azimuthal/angular-momentum demonstration. | GU20-12/13/15 | unreviewed |
| AR-5 | Failure condition | Lifetimes or a geometry calculation that separates the four positive bands into a different coupling scheme would revise the pseudospin-chiral label while preserving the level scheme. | GU20-7/15/16 | unreviewed |
| AR-6 | Research decision | Create one positive quartet page and one negative doublet page; do not force D3-D6 into two stable pair identities. | Full paper | unreviewed |

## Knowledge Impact and Learning Decision

- Effect: `supports` coupled pseudospin/chirality/octupole phenomenology in `131Ba` while `limits` model-independent pair counting and geometry claims.
- Persistence: source, positive-quartet and negative-doublet pages; on-touch update `131Ba`, GALILEO experiment, pseudospin/chiral and octupole concepts, project and index.
- Review state: all `GU20-*` and AR claims remain unreviewed and outside the paper evidence gate.

## Human Review Triage

### P0

P0: none identified.

### P1

- **GU20-4/7 — four-band identity.** Do not impose two fixed positive pairs that the experimental ordering/links do not select.
- **GU20-5/12/17 — configuration logic.** Keep systematics/exclusion and RAT-PRM wavefunctions separate from direct observables.
- **GU20-10/11/14 — octupole language.** E1 correlations are not stable octupole deformation; `β3` is tentative input.
- **GU20-13/15 — model completeness.** Retain D5 mismatch and missing angular-momentum geometry.
- **GU20-16 — electromagnetic gap.** Carry assumed mixing ratios and absent lifetimes into any use of the ratios.

## Related Knowledge and Project Relations

- [[131ba]], [[galileo-131ba-c13-65mev]].
- [[131ba-positive-parity-pseudospin-chiral-quartet]], [[131ba-negative-parity-chiral-doublet-candidate]].
- [[pseudospin-chiral-quartet-bands]], [[octupole-correlation]], [[chirality-parity-quartet-band]].
- [[nuclear-chirality-and-multiple-chiral-doublet-bands]].

## Sources

- Protected BibTeX record: `guo_2020_Evidencepseudospinchiral` in `raw/zotero/wiki-inbox.bib` (read-only).
- Raw PDF: `raw/papers/2020_Guo et al_Evidence for pseudospin-chiral quartet bands in the presence of octupole.pdf`.

## Day18 更正审计：相对电磁信息、131Ba 组态排除范围与 Qt 判据边界

批次048完整重读本文6页及全部图/caption，渲染核对Fig.1–5的连接、多极性、混合比说明与相对E1模式。raw SHA256 `109019D2EF7338BA705462374E6CF30C0CF9D61175510DD92D63021271E8F29D`匹配。原GU20-1–17、AR行、frontmatter及review标记均逐字节保持；以下仅更正Day18追加段。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GU20-D18-1 | **superseded / 更正**：撤回此前将本篇寿命缺失写成全领域穷尽、将少数弱线混合比假定扩展至全部数据、将131Ba的模型配置排除解释为反驳103Rh，以及将无寿命视为普适机制不可识别定理的复合断言。 | evidence-correction | superseded | 本节GU20-D18-2–12；旧Day18复合claim | true |
| GU20-D18-2 | 本文未报告D3–D8的寿命或绝对B值，结论提出后续测寿命以提取绝对约化跃迁概率。此处限本文报告范围，不代表后来文献无结果；D3–D8也不是全核所有能带，Fig.1另列D1/D2。 | evidence-boundary | source-scope | PDF pp.3,5, Fig.1及Summary；全文 | true |
| GU20-D18-3 | Fig.4比值所需的多数带内ΔI=1混合比由角分布测得；少数弱线才假定δ=−0.2(1)。没有逐态敏感性与误差传播，不能将所有比值概括为“严重依赖假定”；同初态分支比的寿命归一化可相消。 | method-boundary | direct | PDF pp.2,4, angular-distribution方法；Fig.4 caption | true |
| GU20-D18-4 | Fig.5给出D7的25/2−与27/2−初态分别向D3–D6衰变的相对B(E1)，每组除以自己的几何均值。该归一化保留组内相对模式，不提供绝对B(E1)，也不是用几何均值代替全部分支信息。 | derived-observable | direct | PDF p.5, Fig.5及caption | true |
| GU20-D18-5 | 作者仅因131Ba计算出的准粒子组态不同，排除将“两对同组态手征双带”用于本核的该种解释；103Rh是该机制的先例引用，不是本文被推翻的研究对象。这是配置计算范围内的结论，不是直接组态测量。 | model-boundary | direct | PDF p.5, §3.2的same-configuration alternative段；Ref.21 | true |
| GU20-D18-6 | RAT-PRM对D3/D4给出占优的g7/2组态成分，对D5/D6给出较多d5/2混合；文中还据E1模式支持四条带均含d5/2成分，不能强制分为两组纯轨道态。 | model-result | direct | PDF p.5, §3.2及Fig.5讨论 | true |
| GU20-D18-7 | 本文没有推导“同组态手征伙伴严格等Qt”或“赝自旋伙伴必不同Qt”。共同Q0模型输入、具体E2矩阵元与含转动几何的Qt应区分；定向核查Kuti2014所用经验Q0也只是模型输入，且其同组态两对带的角动量耦合不同。 | symmetry-boundary | source-and-targeted-companion | 本文PDF p.5；Kuti2014 PDF pp.3–4，非Qt测量定理 | true |
| GU20-D18-8 | β2=0.22、γ=27.1°是参考组态的TAC-CDFT/PC-PK1结果；β3=0.05是“tentatively adopted”的RAT-PRM输入，不是实验八极形变。 | model-assumption | direct | PDF p.5, §3.2 | true |
| GU20-D18-9 | 旧脚本用线性轴对称Q0与K=0高自旋B(E2)公式计算约3.464 eb和0.4475 e²b²，γ与β3未参与，并另乘自选1–3比值区间得到B(M1)。这些是额外toy假设下的算术，不是完整RAT-PRM结果、实测绝对强度或六条带统一范围。 | calculation-boundary | task-self-audit | 旧day18_guo20_131ba_pseudospin_chiral_audit.py的公式；本文Fig.4 | true |
| GU20-D18-10 | 本文将azimuthal plots、角动量分量和完整RAT-PRM几何分析留至Ref.41；不能将该后续承诺写作本篇已完成的独立几何验证。 | source-completeness-boundary | direct | PDF p.5, §3.2；p.6, Ref.41 | true |
| GU20-D18-11 | 模型显著低估向D5的相对E1跃迁；作者将此与混合幅度及D4/D5/D6邻近/交叉有关的敏感性联系。相对分支已能暴露该模型偏差，缺少绝对寿命不使其检验力消失。 | model-discrepancy | direct | PDF p.5, Fig.5及右栏首段 | true |
| GU20-D18-12 | 作者称D3–D6难以仅按能量和连接容易地分为两对；这不构成“无寿命必不可能区分任一四带机制”的定理，也不意味着取得寿命便能唯一分类。绝对矩阵元应结合具体配置、波函数混合、几何与竞争模型检验。 | synthesis-boundary | source-and-inference | PDF pp.4–5, §3.1–3.2与Summary | true |

必要companion [[kuti-2014-multiple-chiral-doublets-103rh]]仅在模型Q0输入与同组态不同耦合的pp.3–4定向重核，不宣称新完整原读或独立绝对率测量。旧分析合同与结果仅作历史运行记录，固定`passed`不验证物理适用性。本节不授课程学分，不升级review状态。
## Day21周考推断阶梯审计：四带流形、寿命缺失与对称性破缺边界

依据独立审计程序 `system/scripts/day21_checkpoint007_pseudospin_chiral_131ba_audit.py` 与审计产物 `outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/pseudospin-chiral-131ba-audit-007.json`，确立本源在推断阶梯上的边界：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| GU20-D21-1 | Guo 2020 在 $^{131}\text{Ba}$ 中建立的 D3–D6 正宇称四带流形具有密集的相互连接跃迁，但其实验测定仅限于能级与相对分支比，**绝对能级寿命 $\tau$ 完全缺失**；在同一自旋下四带能量分散度高达 $359 - 428\text{ keV}$（约为 $^{135}\text{Nd}$ 手征近简并间距的 8 倍），且 D4 与 D5 在 $I=27/2\hbar$ 处发生明显的能序交叉，无法唯一划分为两对双带。将该流形解释为“赝自旋—手征四重带”高度依赖 RAT-PRM 组态投影，未排除准粒子对齐交叉与 Coriolis 混合；试探性引入的 $\beta_3=0.05$ 亦非测得的八极形变量。 | claim-boundary-audit | direct-and-derived | PLB 807, 135572 pp.1-5, Figs.1,4; pseudospin-chiral-131ba-audit-007.json | true |
