---
type: source
title: "Angular distribution of stretched E2 transitions for Gaussian substate population of side feeding in (particle, xn gamma) reactions"
aliases: [Draper 1970 Gaussian substate side feeding, Gaussian substate population side feeding]
created: 2026-07-08
updated: 2026-07-08
status: ai-draft
review_status: human-reviewed
source_type: theory-method-article
reading_depth: deep-read
title_original: "Angular Distribution of Stretched E2 Transitions for Gaussian Substate Population of Side Feeding in (Particle, Xnγ) Reactions"
authors: [James E. Draper, Rainer M. Lieder]
journal: Nuclear Physics A
year: 1970
volume: 141
pages: 211--224
doi: 10.1016/0375-9474(70)90304-0
language: en
canonical_source: doi:10.1016/0375-9474(70)90304-0
citation_key: draper_1970_Angulardistribution
raw_file: "raw/papers/1970_Draper et al_Angular distribution of stretched E2 transitions for Gaussian substate population of side feeding in.pdf"
raw_sha256: DCCCB5F22352E1998896997B13E4C306D80C5AE6DC08F86AD192ECA5C36C093F
nuclei: [76se, 168hf, 172hf, 184os]
reactions: ["74Ge(alpha,2n)76Se", "159Tb(14N,5n)168Hf", "165Ho(11B,4n)172Hf", "182W(alpha,2n)184Os"]
observables: [angular-distribution-coefficient]
methods: [angular-distribution]
tags: [magnetic-substate-population, gaussian-width, side-feeding, angular-distribution, stretched-e2, pado-support]
---

# Draper and Lieder (1970): Gaussian Substate Population of Side Feeding

## Bibliographic Record

James E. Draper and Rainer M. Lieder, *Nuclear Physics A* **141**, 211--224 (1970), DOI `10.1016/0375-9474(70)90304-0`. The title, author list, journal, year, DOI and file name uniquely match citation key `draper_1970_Angulardistribution`.

## Scope and Reading Depth

Full text was read from the PDF text layer. Key equations, figure captions and result paragraphs were checked for pp.211--224: Eq.1 for angular distribution coefficients, Eq.2 for Gaussian magnetic-substate population, Eqs.3--8 for exact stretched-E2/cascade/side-feeding treatment, Fig.3 for the allowed `(A2,A4)` domain, Figs.4--7 for comparisons with experimental angular distributions, and Eqs.9--10 for an increasing-with-`M` population test. Figure curves were not re-digitized.

This is a `theory-ingest + method-ingest + project-ingest` source for [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]]. It provides a formal side-feeding model and coefficient-space constraints, not a general experimental proof that all fusion-evaporation substate populations are Gaussian.

## Summary

Draper and Lieder analyze stretched E2 angular distributions when each level is populated by previous stretched-E2 cascade feeding plus side feeding represented by one Gaussian or a mixture of Gaussians. Their `σ` is the Gaussian width of the side-feeding magnetic-substate distribution; it is not automatically the same object as practical `σ/I` in later P-ADO fitting.

The central project-relevant point is methodological: even in a simplified stretched-E2 problem, observed `A2` and `A4` depend on spin, cascade feeding, side-feeding intensity and the assumed side-feeding substate distribution. The authors explicitly avoid the approximation that an E2 transition from a Gaussian substate population necessarily produces a Gaussian population in the final level. Instead, the final level can contain the non-Gaussian population `P(M)` produced by the previous E2 transition plus additional side-feeding Gaussian components; the combined final-level population is therefore a weighted mixed distribution, denoted here as `\bar{P}(M)` for later Q&A clarity.

## Experimental or Theoretical Setup

- The formalism considers `(particle,xnγ)` reactions feeding quasirotational ground-state bands, with each level receiving cascade feeding and side feeding.
- The angular distribution of a stretched E2 transition is written as `W(θ)=1+A2P2(cos θ)+A4P4(cos θ)`.
- A normalized Gaussian magnetic-substate population is defined as `Pσ(M)=exp(-M^2/2σ^2)/Σ exp(-M'^2/2σ^2)` over `M=-J...J`.
- The paper distinguishes the side-feeding Gaussian `Pσ(M)` from the substate population `P(M)` produced by a previous stretched E2 transition.
- In this source, "E2" is shorthand for stretched E2: a `J -> J-2` transition between states of the same parity. It should not be read as a generic non-stretched E2 case.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DR70-1 | 作者把 `(particle,xnγ)` 反应中由带外 neutron/gamma side feeding 形成的某一自旋 `J` 能级 magnetic-substate population 表示为不同宽度 Gaussian 的混合，并分析随后 stretched E2 γ 射线相对束流方向的角分布。 | method-formalism | direct | Abstract, p.211 | false |
| DR70-2 | 对 stretched E2 transition，作者使用 `W(θ)=1+A2P2(cosθ)+A4P4(cosθ)`；本文目标是理解实验 `A2` 和 `A4`。 | method-formalism | direct | p.212, Eq.1 | false |
| DR70-3 | normalized Gaussian population `Pσ(M)` 只有宽度 `σ` 一个参数；作者强调不近似认为 Gaussian initial substate distribution 经 stretched E2 退激发后在 final level 仍产生 Gaussian distribution。若 final level 还受到其它 side-feeding components 布居，实际 final population 是 cascade-produced `P(M)` 与不同 `σ` 标记的 Gaussian `Pσ(M)` 按强度混合形成的 `\bar{P}(M)`。 | method-formalism | direct | Abstract; p.213, Eq.2 and paragraph after Eq.2; p.217, Eq.7 | false |
| DR70-4 | 对未混合 multipole order `L` 的跃迁，角分布系数写成 `Ak=ρk(Ji)Fk(JfLLJi)`，其中 statistical tensor `ρk` 只依赖 initial substate population。 | method-formalism | direct | p.213, Eqs.3--4 | false |
| DR70-5 | 对 pure stretched-E2 cascade，无论 initial `P(M)` 是否 Gaussian，作者推导相邻 cascade steps 的 angular distribution coefficients 保持相同，即 `Ak(J+2→J)/Ak(J→J-2)=1`。 | method-formalism | direct | pp.214--216, Eqs.5--6 | false |
| DR70-6 | Fig.3 讨论的是 stretched E2 `J→J-2`。当 side feeding 可由任意 Gaussian mixture 构成时，给定 transition 的 `(A2,A4)` 可位于 single-Gaussian curve 与 `J→J-2 bdry` 围成的区域内；`bdry` 不是扫描某个 Gaussian 宽度得到的曲线，而是从 `(0,0)`（`σ -> ∞`、各 `M` 子态近似均匀、`A2=A4=0`）到该 `J→J-2, σ=0` complete-alignment 点的 mixture straight-line boundary。 | model-calculation | direct | p.217, Sec.4, Fig.3 | false |
| DR70-7 | 若实验 transition intensities 可用，作者给出由相邻 stretched E2 transition intensities 与 angular-distribution coefficients 精确求 side-feeding contribution to statistical tensor 的方法。这里的 E2 是 `J -> J-2`、同宇称的 stretched E2。 | method-formalism | direct | pp.212--213 definition; p.218, Eq.8 | false |
| DR70-8 | 对 `184Os`、`172Hf`、`168Hf` 的比较中，作者用来自实验的 smoothed side-feeding intensities，并指出单一 Gaussian side feeding with `σJ=2.8` 可合理再现实验趋势；不同核素的 qualitative differences 主要来自 side-feeding proportion。 | model-calculation | direct | pp.218--223, Table 1, Figs.4--6 | false |
| DR70-9 | 对 `74Ge(α,2n)76Se`，作者报告使用 side feeding `σ=1.6+0.1J` 可较好拟合 `10→8` 至 `2→0` angular distributions。 | model-calculation | direct | p.223, Fig.7 | false |
| DR70-10 | 对 concave-up / increasing-with-`M` population 的测试，作者给出 `Pinc(M)` 并说明相对于 Gaussian case，`A2` 与 `A4` 同时变号并按同一因子改变幅度。 | model-calculation | direct | pp.223--224, Eqs.9--10 | false |

## Authors' Interpretation

- A quantitative description of several experimental angular-distribution patterns can be obtained with a single Gaussian for each side feeding, given the side-feeding intensities and E2 cascade effects.

## Competing Interpretations and Limitations

- The Gaussian side-feeding population is an assumed analysis form, not an experimental fact established for all reactions.
- The paper does not use the later practical ratio `σ/I`; project-level mapping must preserve the distinction between Gaussian width `σ`, spin `J`, and alignment/attenuation coefficients.
- Fig.3's `bdry` lines are allowed-domain mixture boundaries, not single-Gaussian curves. A high-`J` single-Gaussian curve approaches the `J -> ∞` curve, whereas a high-`J` boundary approaches the straight line from the origin to the corresponding complete-alignment point.
- Figure curves were not digitized in this ingest; numerical claims beyond values explicitly stated in the text should be checked against the PDF before paper use.

## Project Relation

For [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]], this source supplies the formal reason that side feeding and cascade history alter angular-distribution coefficients even before a mixed transition is considered. It supports the claim that fixing a single alignment-width parameter without examining feeding assumptions is model-dependent. It does not provide a universal default `σ/I` value.

## Extracted Pages

- Concepts: [[magnetic-substate-population]], [[side-feeding]], [[sigma-over-i]]
- Methods: [[angular-distribution]]
- Observables: [[angular-distribution-coefficient]]
- Projects: [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]]

## Personal Notes

User review on 2026-07-08 resolved DR70-3, DR70-6 and DR70-7 wording. Key reminders for later Q&A: final-level populations may be mixed `\bar{P}(M)` distributions, Fig.3 `bdry` is a mixture boundary, and E2 in this source means stretched E2.


## Day17自审补充：侧喂养反演与印刷Gaussian例子

2026-10-20原Day17session，属于Day18无学分知识预习。旧人审全文prefix/CRLF/DR70-1–10/false flags逐字保持；以下是本session新self-audit，**不属于human-reviewed**，新claims全needs_review。本次实际重新读完14页、7图、表1、Eqs1–10及12references，未digitize原图/重做原实验fit。原件hash `dcccb5f22352e1998896997b13e4c306d80c5ae6dc08f86ad192eca5c36c093f`；原扫描的创建日期不是实验日期。

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DR70-D17-1 | Eq6的相邻Ak不变限于pure stretched E2/无sidefeeding/未观测中间光子完整求迹，适于任意初始P(M)；不是Gaussian经退激仍Gaussian、有限γ门不变或实际时角可分离定理。 | method-and-selection-boundary | direct-source plus explicit scope | pp.214–216, Eqs5–6 | true |
| DR70-D17-2 | Eq7对每一P_i(M)先归一再按I_i混合；Eq8使用相邻转换的Γ(J)及AD，Sec5明确transition intensity含internal conversion。原始角组峰面积/γγ门计数不能无效率/分支/门合同直接代Γ。 | formal-input-contract | direct and synthesis | p.218, Eq8 | true |
| DR70-D17-3 | Table1把experimental Iγ与smoothed I_J分列，原experimental误差约±10%；作者明言raw相邻差会负，先拟smoothcurve再差分。因此smoothedI_J不是新的独立实验yield或精确无误差输入。 | actual-input-provenance | direct | pp.218–219, Table1 and Sec6 | true |
| DR70-D17-4 | 168Hf的raw Iγ(J6)−Iγ(J8)=.91−1.08=−.17，而表smoothed I6=.15；负差是作者平滑动机的实际例，不是负物理feeding。条件按表smooth列向上累加至截断，F6=.95、f6=.15/.95，Eq8反演对lower/upper A的系数为6.333/−5.333；无原smoothfit/Σ，不构造实验CI。 | table-arithmetic and inverse-conditioning | derived | p.218, Table1, 168Hf rows6/8 | true |
| DR70-D17-5 | p216明确print J12/σ12=5、A2=.225和等效σ2=.143；图2的2→0曲线在该A2落在σ约1量级。本session保留literal，不自行将.143改成1.43或称已发现官方erratum。 | source-literal-boundary | direct-text-and-figure | p.216, Fig2 example | true |
| DR70-D17-6 | 本session独立CG末态求迹+photon helicity±1投影核：J12σ5给(A2,A4)=(.2267563063,−.03063894581)，完整12→10→…→0每步不变。J2σ.143却给(.7142857143,−1.7142857141)，与printedA2=.225不闭合。 | Codex conditional source-number replay | derived not new experiment | p.213, Eqs2–4; p.216 example | true |
| DR70-D17-7 | 在同一声明Gaussian/纯E2合同下，匹配printedA2=.225的σ2=1.418668；匹配精确cascadeA2的σ2=1.412275。后者A4=−.04407903而exactcascade−.03063895，差−.01344009；只匹配A2不保证A4或population同一。根不是原实验测得σ或官方更正。 | Codex surrogate-boundary | derived | p.216, equivalent-Gaussian discussion | true |
| DR70-D17-8 | 独立J2→0角多项式与16/32点投影、uniform各J的isotropic、M0的(A2,A4)=(5/7,−12/7)以及归一/正population控制通过；这是组件物理核验，不能认证原全部figcurves/实验取向或后续δ。 | model-validation-scope | derived | p.213, Eqs2–4 | true |
| DR70-D17-9 | 原σJ=.28J的constantσ/J例在184Os图4给与data相反趋势，σJ=2.8仅在用smoothedI_J条件下合理；p223多组a+bJ给类似轨迹但点位不同。不能把固定σ/I当普适原实验证明。 | counter-evidence and parameter-dependence | direct-author | pp.219–223, Figs4–6 | true |
| DR70-D17-10 | Os/Hf观测来自Newton1967 Ref1而非本篇新采集；Se角分布为本组Ref12“to be published”，无独立原data/fitCov。p223还保168Hf 2→0受extranuclearfields可能；全文没有DSAM时间取向联合kernel，不能从Eq7积分权重推其时间分布。 | independence and time-response-readiness | direct-source and negative-check | p.223 discussion; p.224 References1/12 | true |

[新Gaussian结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/draper1970-gaussian-result.json)、[Table1实际输入审计](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/draper1970-table1-result.json)，可复算script `system/scripts/day17_draper1970_gaussian_audit.py`。用已经存在的Sympy/Numpy/Scipy；没有安装依赖或改原件。p216关于从Gaussian4曲线取A4的图解描述与exactcascade不同，是单Gaussian代理的边界，不替换Eq6精确求迹。

Eq8可写`A_side=(A_lower−r A_upper)/(1−r)`，`r=Γ_upper/Γ_lower`；Jacobian为`(1/f,−r/f,(A_lower−A_upper)/f²)`，`f=1−r`，完整误差为`gᵀΣg`。f→0时反演病态，Γ若共享归一/峰/效率必须保Cov。上述168Hf的f只取表中smooth输入及声明截断；不当实际原Γ反演、sigma误差或DSAMfeedingtime测量。

另见[[lifetime-strength-audit-165tm-136nd]]与[[doppler-shift-attenuation-method]]：积分AD对不同feeding路径的时间kernel尚无约束，本日新问题保留，不从当前结果推实际lifetimebias。
