---
type: source
title: "Improved Analysis of gamma-Ray Angular Distributions in (Particle, xn) Experiments"
aliases: [Ionescu 1981 improved angular distributions, Ionescu 1981 feeding-aware population model, Ionescu 1981 Gaussian hypothesis test]
created: 2026-07-09
updated: 2026-10-15
status: ai-draft
review_status: human-reviewed
source_type: experiment-method-article
reading_depth: deep-read
title_original: "Improved Analysis of γ-Ray Angular Distributions in (Particle, xn) Experiments"
authors: [V. A. Ionescu, J. Kern, C. Nordmann, S. Olbrich, W. Reichart]
journal: Nuclear Instruments and Methods in Physics Research
year: 1981
volume: 190
number: 1
pages: 19--27
doi: 10.1016/0029-554X(81)90200-7
language: en
canonical_source: doi:10.1016/0029-554X(81)90200-7
citation_key: ionescu_1981_Improvedanalysis
raw_file: "raw/papers/1981_Ionescu et al_Improved analysis of γ-ray angular distributions in (particle, xn) experiments.pdf"
raw_sha256: 233B11888D8143A17B89DA3332AFAC1342803B35024AC2EC7708C7BD51D435F1
nuclei: [167tm]
reactions: ["165Ho(alpha,2n)167Tm"]
observables: [angular-distribution-coefficient, multipole-mixing-ratio]
methods: [angular-distribution]
tags: [angular-distribution, gaussian-hypothesis, direct-feeding, side-feeding, yrast-feeding, pado-support]
---

# Ionescu et al. (1981): Improved Angular-Distribution Analysis in `(particle,xn)` Experiments

## Bibliographic Record

V. A. Ionescu, J. Kern, C. Nordmann, S. Olbrich and W. Reichart, *Nuclear Instruments and Methods in Physics Research* **190**(1), 19--27 (1981), DOI `10.1016/0029-554X(81)90200-7`, citation key `ionescu_1981_Improvedanalysis`.

The raw PDF uniquely matches the title, journal, year and DOI. Local file size verified in DAY14 is `606539` bytes (the previous `375432`-byte description was stale; the recorded SHA-256 still matches); local timestamp `2026-07-01 16:35:16`; SHA-256 is recorded above.

## Scope and Reading Depth

The full nine-page paper was read from the PDF text layer. Key checks covered the Introduction on the Gaussian substate-population hypothesis, the experimental measurement and fitting precautions, the general angular-distribution formalism and Gaussian test in Secs.3--4, the improved feeding-aware population model in Eqs.(9)--(11), the pure-E2 and mixed-transition applications in Tables 1--3 and Figs.2--6, and the concluding cautions on side feeding and level-dependent widths.

This is an `experiment-ingest + method-ingest + project-ingest` source. It is a strong example that feeding-aware magnetic-substate population modeling can be necessary for accurate angular-distribution analysis and mixing-ratio determination, but it is not a direct P-ADO paper.

## Summary

The paper reports carefully measured angular distributions for the `165Ho(alpha,2n)167Tm` reaction and uses them to test the commonly assumed Gaussian magnetic-substate population hypothesis. The authors show that the global Gaussian hypothesis is inadequate for their `167Tm` dataset and introduce an improved model in which the population of a level is written as the sum of a Gaussian side-feeding component plus direct feeding through discrete yrast-region gamma transitions.

For the current project, the paper matters because it demonstrates a concrete route from population-model choice to spin and `delta` assignment. Pure-E2 transitions are used first to constrain the population width and the statistical-tensor factors `rho2/rho4`; only then are mixed transitions fitted for multipole mixing ratios. In Sec.5 the fitted `delta` values are also compared with values inferred from branching ratios, and the paper explicitly labels that branching-ratio route as model dependent. The authors treat the full procedure as a way to obtain unambiguous and nuclear-model-independent spin determinations for the studied case.

## Experimental or Theoretical Setup

- Reaction: `165Ho(alpha,2n)167Tm`, chosen because the `167Tm` level scheme had already been studied carefully and because operation below the `(alpha,3n)` threshold minimizes contamination from parasitic channels.
- Two detector setups were used: one intrinsic Ge detector for `50--500 keV` and one `50 cm^3` Ge(Li) detector for `180--600 keV`; measurements covered 7 or 8 angles with detector-target distance `40 cm`.
- Great care was taken with monitor normalization, dead-time correction and peak fitting so that angular-distribution coefficients could be determined with uncertainties at or below the statistical level.
- The analysis focuses on pure-E2 transitions and mixed `M1+E2` transitions in the `1/2+[411]` and `1/2-[541]` rotational bands of `167Tm`.

## Figure and Table Digest

- Fig.2 用 271 keV pure-`E2` transition 展示 Gaussian hypothesis 与改进模型的拟合差异：curve A 体现简单 Gaussian 假设的局限，curve B 展示引入 feeding-aware model 后的改善。
- Fig.3 的横纵轴不是 attenuation factors，而是 `rho2` 与 `rho4`；原文称测量最精确的 8 条 pure-`E2` transitions 的实验点明显偏离 Gaussian 预言曲线，是本文否定 global Gaussian hypothesis 的关键图。
- Fig.4 对应 Eqs.(9)--(11) 的 feeding-aware population model，把 side-feeding Gaussian 项与离散 direct-feeding 项如何组合成总 population 画成结构图。
- Table 1 汇总 pure-`E2` transitions，用来约束 `rho2/rho4` 与 side-feeding width `sigma`。
- Table 2 汇总 mixed transitions 的 `delta` 拟合结果，体现“先由 pure-`E2` 限定 population model，再拟合 mixed transitions”的两步法；文中还把这些 `delta` 与 branching-ratio 提取值比较，并明确指出后者是 model dependent。
- Table 3 实际汇总 E1 interband transitions 的 angular coefficients、σ/ΔJ 假设及 arctanδ；正文用其讨论小 M2 admixture，不能称为 adopted-spin 汇总表。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| IO81-1 | 本文在 `165Ho(alpha,2n)167Tm` 反应中测量了 carefully controlled gamma angular distributions，并说明选择该反应的原因是：已有较详细的 `167Tm` 能级纲图，且在 `(alpha,3n)` 阈值以下寄生反应污染很小。 | observed-fact | direct | p.19, Abstract; pp.19--20, Secs.1--2 | false |
| IO81-2 | 角分布写为 `W(theta)=1+A2^exp P2(cos theta)+A4^exp P4(cos theta)`；作者明确指出 `A2^exp` 与 `A4^exp` 由初态 magnetic-substate population、初末态自旋和跃迁多极性共同决定。 | method-formalism | direct | p.19, Eqs.(1)--(2); p.22, Eq.(3) | false |
| IO81-3 | 作者指出 following Diamond et al.，通常假定初态 substate population 服从 Gaussian 分布 `D(m)=exp(-m^2/2 sigma^2)`；对 pure quadrupole transitions，这一假设可被检验，因为同一个 `sigma` 必须同时再现 `A2^exp` 和 `A4^exp`。 | method-formalism | direct | p.19, Introduction; p.22, Eqs.(5)--(6); p.23, first paragraph of Sec.4 | false |
| IO81-4 | 对 `167Tm` pure-E2 transitions 的检验显示，全局 Gaussian substate-population hypothesis 不adequate：以 271 keV 纯 `E2` 线为例，Gaussian 模型既不能清晰识别正确 spin sequence，也给出较差的 `chi^2`；Fig.3 中实验 `rho2/rho4` 点也明显偏离 Gaussian 预言曲线。 | observed-fact | direct | pp.23--24, Fig.2, Fig.3 and surrounding text | false |
| IO81-5 | 改进模型把目标能级的总 population 写成 side-feeding Gaussian 分量 `Ds(m)` 与若干 discrete direct-feeding 分量 `Dj(m)` 的和：`DT(m)=Ds(m)+sum Dj(m)`；对应 statistical tensors 则写成含 side feeding、离散 parent-state feeding、强度分支和 disorientation coefficient `U` 的组合式。 | method-formalism | direct | pp.24--25, Eq.(9), Eq.(10), Eq.(11), Fig.4 | false |
| IO81-6 | 作者明确说明，式(11) 右端求和项实际编码了低能 yrast 区离散 feeding 的整个历史，因此 `sigma` 在此只表征 side-feeding contribution，而不是该能级 total population 的单一全局宽度。 | method-boundary | direct | p.25, text below Eq.(11) | false |
| IO81-7 | 用改进模型重新拟合 271 keV 纯 `E2` 线后，可得到满意的 `chi^2` 并清晰识别正确的 `17/2 -> 13/2` spin sequence；作者据此称可获得 unambiguous、nuclear-model-independent spin determinations。 | author-interpretation | direct | p.23, Fig.2 curves B; p.26, Sec.5; p.27, Conclusion | false |
| IO81-8 | 对 mixed `M1+E2` transitions，作者先用竞争的 pure-E2 transition 限定 `sigma` 的允许范围，再在该范围内最小化 `chi^2` 提取 `delta`；Table 2 中得到的小 `chi^2` 表明实验与计算符合良好，并且所得 `delta` 与 branching-ratio 派生值相容。 | experimental-practice | direct | pp.22--23, end of Sec.3; p.26, Sec.5; Table 2 | false |
| IO81-9 | 结论中作者强调：`167Tm` 中不存在可泛化的单一 `sigma` 规律；某些带中 `sigma` 近似常数，另一些只在 `sigma/J` 上近似稳定，而且取值范围很大，因此给定能级的 population 不能用一个 single Gaussian 描述，因为少数 discrete transitions 可能带来宽度差异很大的 feeding components。 | author-interpretation | direct | p.27, Conclusion | false |
| IO81-10 | 在 `1/2+[411]` rotational band 的 mixed transitions 分析中，作者把 angular-distribution fit 得到的 `delta` 与 branching ratios 推得的对应值作比较，并明确说明 branching-ratio 提取路线是 model dependent；对本文例子，两类结果相容。 | experimental-practice | direct | p.26, Sec.5 paragraph around Table 2 and col.9 note | false |
| IO81-11 | Table1有10条pureE2的experimental/calculated成对行，Q/D/T指复合峰；Fig3只说8条最精确线，不据此减去两表行或把上下行算独立测量。Table3实际为E1 interband/可能M2混合表，不是adopted-spin清单。 | table-role-and-scope | direct | printed21 Tables1–2; printed22 Table3; printed24 Fig3 / PDF3–6 | true |
| IO81-12 | Eq11的ρ总和以Is/IT和I0j/IT加权，I0j为angle-averaged、含conversion的total transition intensity；parent实验tensor乘disorientation U承接整段离散历史。σ只属于本层Gaussian sidefeeding，不是total population的全局σ。 | feeding-model-and-input-contract | direct | printed24 Eqs.(9)–(10); printed25 Eq.(11) / PDF6–7 | true |
| IO81-13 | 对低强度虚线输入，作者近似δ=0计算U、在favored levels间插值parenttensor、将I0取比90°强度低12%；作者说其影响小并已检查，但未给fullinput/Σ可供本任务重放。这些不是各线直接测得的σ或通用12%校正。 | author-approximation-and-replay-boundary | direct-and-derived | printed26 Sec.5 approximations a–c / PDF8 | true |
| IO81-14 | Table2三条mixed线有7个hypothesis/root行，列为arctanδ[degrees]；251.03的ΔJ−1有+76°/+18°、ΔJ+1有−7.5°，各χ²约.4/.5/.5。branch比较列为model-dependent的绝对角，不给δ符号。 | measured-coefficient-fit-alternatives-and-units | direct | printed21 Table2/footnote a; printed26 Fig6 / PDF3/8 | true |
| IO81-15 | 改进feeding后，mixed-line角分布仍可在不同spin假设下给同样好的χ²；作者明确用Ref5 excitation functions消除该歧义。其“unambiguous/model independent”结论须连同reaction/feeding/外部spin材料，不等于任何angular ratio单独唯一赋值。 | author-practice-and-conclusion-boundary | direct-and-derived | printed26 Sec.5 mixed-transition paragraph; printed27 Conclusion / PDF8–9 | true |
| IO81-16 | Eq7采用A2/A4的对角误差权重；本任务从Table1印刷值重算10个χ²，在最近舍入条件下均有相容区间。这只是已报模型输出的条件算术，不重建原fit、parent误差/共同Σ或实验置信度；432-keV triplet仍保留作者questionable标记。 | conditional-table-audit-and-uncertainty-boundary | direct-and-derived | printed23 Eq.(7); printed21 Table1; printed26 Sec.5 / PDF3/5/8 | true |
| IO81-17 | Table3的143.46行footnote b明确Is=0；固定parenttensor/U/强度后，Eq11对本层sidefeeding σ的导数为零，σ无需且不能从该层角分布拟合。这不消除parent输入的不确定度。 | source-input-and-derived-identifiability | direct-and-derived | printed22 Table3 footnote b; printed25 Eq.(11) / PDF4/7 | true |
| IO81-18 | 26.5MeV α束、10mg/cm²Ho、40cm探测距离；作者在此忽略有限立体角修正。0.5°角精度、0.5% isotropy测试与monitor/deadtime约10^-3是不同控制，不是现代clover ADO通用误差或响应。 | apparatus-specific-controls | direct-and-derived | printed20 Sec.2 / PDF2 | true |
| IO81-19 | Table1的ρ2列为负，而Fig3横轴以正刻度画ρ2；本文未说明该反号关系，本任务保留图/表原标记，不据图擅改Table1或未校约定就数字拟合Gaussian曲线。 | figure-table-sign-reading-boundary | direct-and-derived | printed21 Table1; printed24 Fig3 / PDF3/6 | true |
| IO81-20 | 表中实验系数通常为两组detector测量平均；Fig5 partial scheme引用Ref5完整研究，parent coefficients又进入Eq11。因此表、图、同峰拟合和Ref5并非可任意重复计权的独立证据，实际event/Σ仍未恢复。 | source-dependency-and-shared-input-boundary | direct-and-derived | printed22 opening paragraph; printed25 Fig5 caption; printed26 Sec.5 / PDF4/7–8 | true |
| IO81-21 | 本文Eq11的target/parent U参数须按实际feeding方向映射Yamazaki Eq12；本文B是辐射几何组合，后者B为completealignmenttensor，p/ρ与α亦不同。当前直接映射evenrank，不声明已读Poletti原25页或复跑其代码。 | cross-source-notation-and-direction | direct-and-derived | printed22 Eqs.(3)–(5); printed25 Eq.(11); YA67 printed3 Eqs.(12)–(15) | true |
| IO81-22 | Table1/Fig5的271.12支为17/2→13/2 pureE2；在Yamazaki定义/未观测模式条件下，parentρ2/4经U给单支normalized tensor−.67182033/.37541768，未乘实际feeding权重，不能当全childρ或新测量。 | conditional-source-input-application | derived | printed21 Table1 row271.12; printed25 Fig5; YA67 printed19 TableIIb | true |
| IO81-23 | p22 Eq4下方字面写λmax=min(2Ji,2Jf,2L′)。Yamazaki独立2→0 E2表行有非零radiation A4却零daughter高ranktensor，故不把该字面式当一般singleγ上限。原式保留，未判断官方erratum；本次Tables1–2所分析跃迁的spins下该额外cap对k≤4不活跃，不据此否定所报fits。 | literal-rank-cap-and-applicability-boundary | direct-and-derived | printed22 text below Eq.(4); YA67 printed7 TableIIa Ji2 Jf0 | true |

## Nuclear Structure Information

The nucleus-specific structure content is limited to the `1/2+[411]` and `1/2-[541]` rotational bands of `167Tm`, used here as the testbed for angular-distribution and feeding-model analysis rather than as a standalone `167Tm` structure ingest.

## Authors' Interpretation

- The global Gaussian substate-population hypothesis is inadequate for the `167Tm` case studied.
- A feeding-aware model with Gaussian side feeding plus discrete direct feeding is more realistic.
- With that model, the authors argue that spin determinations from angular distributions can become unambiguous for the studied bands.

## Model Results

- The Gaussian hypothesis produces poor `chi^2` behavior and does not sharply separate competing spin sequences for the example discussed.
- The improved model in Eqs.(9)--(11) produces satisfactory fits for pure-E2 transitions and then supports mixed-transition `delta` extraction.
- The fitted width/orientation parameters vary strongly enough across the studied bands that no single global Gaussian width describes all levels.

## Competing Interpretations and Limitations

- The paper does not show that all Gaussian assumptions are invalid in all `(particle,xn)` reactions; it shows that the global Gaussian hypothesis fails for this `167Tm` case.
- The improved model is still a model, not a universal theorem; the authors present it as a more realistic description for the studied feeding pattern.
- The argument depends on a reaction and nucleus where the yrast-region discrete feeding history can be reconstructed well enough to enter Eq.(11).
- Fig.3 uses `rho2/rho4` statistical-tensor factors rather than Ekstrom-style attenuation factors `alpha2/alpha4`; these notations are related but should not be merged.
- This source should not be rewritten as a direct precursor of modern P-ADO; its relevance is methodological and evidentiary.

## Project Relation

For [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]], this is one of the strongest source-level examples that a population model can materially change angular-distribution interpretation. It shows that pure-E2 transitions can be used to constrain alignment/population width first, that mixed-transition `delta` extraction then depends on that constraint, and that feeding-aware modeling may be required when a single Gaussian description fails.

The boundary is important: Ionescu 1981 does not provide a universal rejection of Gaussian ideas and does not define the user's `sigma/I`. Its value is as a carefully worked case showing that direct gamma feeding and side feeding can require a more detailed population model before one trusts spin or `delta` assignments.

## Extracted Pages

- Nuclei:
- Bands:
- Concepts: [[direct-feeding]], [[magnetic-substate-population]], [[side-feeding]]
- Methods: [[angular-distribution]]
- Projects: [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]]

## Day14补读：feeding递归、表格角色与δ角单位

本轮读取原9页全主线、Figs1–6、Tables1–3、Eqs3–11和影响判断的误差/限制/refs，关键PDF3–8视觉核。原件SHA256 `233b11888d8143a17b89da3332afac1342803b35024ac2ec7708c7bd51d435f1`匹配source；实际606539 bytes，更正旧字节描述，raw不改。**本页原human-reviewed是旧版状态，原IO81-1–10的false保持；本轮IO81-11–20全部needs_review true，旧人审不覆盖增量。**

### Table1：实测与计算不是重复观测

印刷p21 Table1：以下每行保留实测A、作者calculated A和χ²；括号为原报误差。Q=quadruplet，D=doublet，T=triplet。原始ρ2符号不由Fig3正横轴覆盖。以下计算只核Eq7和舍入相容，不能代替fullfeeding fit或真实Cov。

| Eγ / keV | peak | A2 exp | A4 exp | A2 calc | A4 calc | χ² reported |
| --- | --- | --- | --- | --- | --- | --- |
| 209.92 | Q | 0.239(58) | -0.105(64) | 0.254 | -0.054 | 0.70 |
| 228.61 | Q | 0.205(7) | -0.055(9) | 0.205 | -0.048 | 0.59 |
| 295.585 | 未标复合 | 0.243(19) | -0.062(8) | 0.250 | -0.061 | 0.13 |
| 318.135 | 未标复合 | 0.256(9) | -0.067(10) | 0.259 | -0.058 | 0.93 |
| 371.52 | Q | 0.239(21) | -0.071(26) | 0.243 | -0.045 | 1.1 |
| 397.38 | D | 0.234(15) | -0.048(14) | 0.233 | -0.057 | 0.40 |
| 184.33 | D | 0.248(9) | -0.013(49) | 0.247 | -0.061 | 0.96 |
| 271.12 | 未标复合 | 0.266(10) | -0.074(12) | 0.266 | -0.073 | 0.01 |
| 354.85 | 未标复合 | 0.303(18) | -0.101(22) | 0.308 | -0.086 | 0.52 |
| 432.47 | T | 0.255(22) | -0.118(32) | 0.271 | -0.059 | 3.9 |

271.12的印刷中心值给χ²≈.006944、表报.01；其他行也仅做必要舍入范围检验。parenttensor、U和intensity共享输入的误差未因此消失，不能把每一行当独立的一自由度新检验或从这里重估整体confidence。432.47 triplet系数在正文明确questionable。

### Table2：三条mixed线、七个拟合分支

原列为arctanδ的度数，非dimensionless δ。每条line的A2/A4是同一组观测；不同ΔJ或root不可平均。Table2的σ范围按原表保留，不由本任务另造。branch列只是model-dependent的|arctanδγ|，不提供phase/sign。

| Eγ / keV | ΔJ hypothesis | arctanδ / deg（原报误差） | χ² | side σ range |
| --- | --- | --- | --- | --- |
| 304.41 | -1 | 24 ±9 | 0.8 | [3.4, 6.6] |
| 304.41 | +1 | -13 ±9 | 0.7 | [3.4, 6.6] |
| 251.03 | -1 | 76 ±2 | 0.4 | [2.65, 3.0] |
| 251.03 | -1 | 18 ±3 | 0.5 | [2.65, 3.0] |
| 251.03 | +1 | -7.5 ±1.5 | 0.5 | [2.65, 3.0] |
| 184.0 | -1 | 44 ±36 | 未给 | [1.1, 4.3] |
| 184.0 | +1 | -7 (+5/−10) | 0.03 | [1.1, 4.3] |

同一M1/E2 convention且只含这两种辐射时，`δ=tan(θ)`、`fγ,E2=δ²/(1+δ²)=sin²θ`。251.03的三解名义为：+76°→δ4.010781、94.1474%；+18°→δ.324920、9.54915%；−7.5°→δ−.131652、1.70371%。这些是原hypothesis/root的条件变换，不是本任务选择了三个等可信物理方案，更不是B(E2)/B(M1)、absolute strength或能级分支。误把−7.5°当δ−7.5会误得98.25%的E2份额。

source Fig6/正文明确借excitation functions选择spin假设；不能把好χ²本身当唯一spin或δ。角区间须经tan和sin²非线性变换，保留多解/不对称，不给没有原grid支持的统一CI。

### Eq11：归一权重和零sidefeeding极限

`ρ_k=ρ_k^s(σ) Is/IT + Σj ρ_k^parent,j U_j I0j/IT`，`IT=Is+ΣjI0j`。权重含angle-averaged total intensity和conversion，不能把未修正90°计数直接代入。parenttensor/U/强度会承接整条离散feeding历史，所以论文要求whole bands处理；σ只给sidefeeding分量。

作者对弱虚线用δ0算U、parenttensor插值和I0=.88I90的近似，保留其小影响论断但不泛化12%校正（IO81-13）。Table3 143.46的Is0使本层局部σ系数为零：固定其他输入时`∂ρ/∂σ=(Is/IT)∂ρs/∂σ=0`；parenttensor自身的误差仍在。Table3是E1/M2问题，不能把上述E2份额套给它。

### 适用范围与缺失输入

globalGaussian失败不否认sidefeedingGaussian假设；改进模型还用离散feeding和外部spin信息。40cm/单Ge的Ω可忽略结论不外推γγ clover ADO。原per-angle counts/完整Cov、所有parenttensor/U/转换强度/插值输入、fitgrid与detector acceptance未提供，本轮没有复跑原model/σ/δ或给193Bi排序/Pr136新机制。Fig3正ρ2与Table1负ρ2先保留原样；旧source的Table3描述已按实际caption更正。

[25-check审计程序](../../system/scripts/day14_ionescu_feeding_table_audit.py)与[结果](../../outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/ionescu1981-feeding-table-audit.json)保存原行、单位、角色和条件变换，非全模型验证。Day15只无学分preview。

## Human Review Triage

- P0 focus: `IO81-4`, pp.23--24, Figs.2--3. Check that the paper really concludes the global Gaussian hypothesis is inadequate for this studied case, and that the Wiki keeps the claim case-specific.
- P0 focus: `IO81-5` / `IO81-6`, pp.24--25, Eqs.(9)--(11). Check that the improved model explicitly separates Gaussian side feeding from discrete direct feeding, and that `sigma` is kept as a side-feeding-width parameter rather than a total-population constant.
- P0 focus: `IO81-8`, pp.22--23 and p.26, Table 2. Check the two-step fitting logic: constrain width from pure-E2 transitions first, then fit mixed-transition `delta` within that range.
- P1: `IO81-10`, p.26 around Table 2. Check that the branching-ratio-derived comparison values are explicitly described as model dependent, and that the Wiki does not rewrite them as direct observables.
- Remaining P0: `IO81-7`, p.27 Conclusion and Fig.2 curves B, for the strong wording about unambiguous and nuclear-model-independent spin determination.
- P1: `IO81-2/IO81-3`, pp.19 and 22, for the formal relation between measured `A2/A4`, substate population and the Gaussian test.
- P1: `IO81-1`, pp.19--20, for the reaction choice, detector geometry and dead-time / monitor-control precision.
- P1: `Project Relation`, whole section, to ensure the Wiki uses this source as a feeding-aware population-model example rather than as a universal P-ADO antecedent.

## Personal Notes

This paper is especially useful because it does not stop at saying "the Gaussian hypothesis fails". It shows the next engineering step: use pure-E2 transitions to calibrate the population model, carry discrete feeding explicitly, and only then trust mixed-transition `delta` extraction. That makes it directly relevant to any argument against hard-wiring one fixed `sigma/I`.

## Yamazaki交叉核验：U与radiation rank不能混用

[[yamazaki-1967-aligned-angular-coefficients]] YA67-4–9提供直接定义与14条原表控制。IO81-21/22分开U的parent→target方向、radiation B与completealignment B，以及p/ρ与α；271支数值只属单支条件应用，不填全feeding或actualΣ。旧人审仍仅旧版，新IO81-21–23 needs_review true。

IO81-23的λmax字面已视觉回核：它包含2Jf。当前不拿该式作一般rank定理，也不静默改原PDF或称official erratum。2→0 E2的photon角图可有P4，而daughter J0没有高阶alignment，反例区分的正是两类对象。本论文Tables1–2相关spins均足够大，k≤4分析不因这项字面cap自动变化；原实验与所有旧claims/flags保留。
