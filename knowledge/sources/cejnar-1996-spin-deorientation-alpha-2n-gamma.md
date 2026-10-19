---
type: source
title: "Calculation of the spin deorientation in (alpha,2n gamma) reactions"
aliases: [Cejnar 1996 spin deorientation, Avalanche II spin deorientation, Gaussian side-feeding hypothesis Cejnar]
created: 2026-07-09
updated: 2026-07-09
status: ai-draft
review_status: human-reviewed
source_type: theory-method-article
reading_depth: deep-read
title_original: "Calculation of the Spin Deorientation in (α,2nγ) Reactions"
authors: [P. Cejnar, S. Drissi, J. Kern]
journal: Nuclear Physics A
year: 1996
volume: 602
pages: 225--243
doi: 10.1016/0375-9474(96)00131-5
language: en
canonical_source: doi:10.1016/0375-9474(96)00131-5
citation_key: cejnar_1996_Calculationspin
raw_file: "raw/papers/1996_Cejnar et al_Calculation of the spin deorientation in (α,2nγ) reactions.pdf"
raw_sha256: 47765AE583940610CF4B19BB53E727308719BC23A949C6CC1E76084F6DC0BCCD
nuclei: [110cd, 112cd]
reactions: ["108Pd(alpha,2n gamma)110Cd", "110Pd(alpha,2n gamma)112Cd"]
models: [statistical-model, avalanche-ii]
observables: [angular-distribution-coefficient, multipole-mixing-ratio]
methods: [angular-distribution]
tags: [deorientation, magnetic-substate-population, gaussian-width, side-feeding, pado-support]
---

# Cejnar et al. (1996): Spin Deorientation in `(α,2nγ)` Reactions

## Bibliographic Record

P. Cejnar, S. Drissi and J. Kern, *Nuclear Physics A* **602**, 225--243 (1996), DOI `10.1016/0375-9474(96)00131-5`. The title, author list, journal, volume, pages, year and DOI match citation key `cejnar_1996_Calculationspin`.

## Scope and Reading Depth

Full PDF text layer was read for pp.225--243. Key checks include the Introduction for the physical motivation, Eqs.1--9 for orientation-flow and Gaussian-parameter extraction, Figs.1--2 for Gaussian-curve/deorientation-curve comparisons, Figs.3--5 for calculated versus experimental `σ` systematics, Fig.6 for discrete/quasicontinuum feeding regions, Fig.7 for sensitivity of `χ²(δ)` to the imposed `σ` interval, and the Conclusions. Figure curves were not digitized.

This is a `theory-ingest + method-ingest + project-ingest` source for [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]]. It provides a reaction-specific statistical-model calculation of spin deorientation and side-feeding Gaussian parameters. It does not establish a universal `σ/I` prior for all fusion-evaporation or P-ADO analyses.

## Summary

Cejnar et al. extend the Avalanche statistical-model calculation from side-feeding intensities to spin orientation. The method follows many angular-momentum routes through compound and daughter nuclei, accumulates feeding flow and orientation flow, and uses deorientation coefficients for particle and γ emissions. The authors test whether the side-feeding part of the magnetic-substate population can be approximated by a Gaussian and compare calculated Gaussian widths with angular-distribution analyses of `110,112Cd` populated in `108,110Pd(α,2nγ)` reactions.

The project-relevant result is two-sided: for the studied `Pd(α,2nγ)Cd` cases the calculated side-feeding population is approximately Gaussian, but the paper explicitly warns that this validation is case-specific. The paper also shows that using a physically wrong projectile-energy-dependent `σ` constraint can change the extracted `M1+E2` mixing-ratio conclusion.

## Experimental or Theoretical Setup

- Model: Avalanche II statistical-model calculation of feeding flow and orientation flow.
- Reactions compared with data: `108Pd(α,2nγ)110Cd` at `Eα=27 MeV`; `110Pd(α,2nγ)112Cd` at `Eα=25 MeV` and `15 MeV`.
- Calculated quantities: side-feeding orientation parameters `Bλ^(SF)` for discrete levels, deorientation coefficients `Uλ(Ji L Jf)`, and the Gaussian side-feeding width `σ`.
- Experimental input for comparison: angular-distribution coefficients `A2` and `A4` from discrete γ transitions and previously extracted Gaussian `σ` values.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| C96-1 | 作者指出 capture/fusion 后 γ 各向异性来自 compound-state `m` 子态围绕束流轴的取向，以及 particle/γ evaporation 过程中初始取向在一定程度上保留，因此低能 residual levels 仍可有 noticeable alignment。 | review/background | direct | p.225, Introduction | false |
| C96-2 | 对任一 residual-nucleus discrete level，详细 deorientation 处理需要对所有 angular-momentum routes 做加权平均；权重由 spin-dependent level density 与 emitted particle/γ angular momenta 的 partial transition rates 给出。 | method-formalism | direct | p.226, Introduction | false |
| C96-3 | Avalanche II 同时计算 total feeding flow `φ(j)` 与 orientation flow `Ωλ(j)`；`Ωλ(j)=φ(j)Bλ(j)` 连接了 feeding-flow components 与 conventional orientation parameters。 | method-formalism | direct | pp.228--229, Eqs.1--2 | false |
| C96-4 | partial exit orientation flow 由 feeding branch、初态取向参数 `Bλ(i)`、角动量权重 `wL` 和 deorientation coefficient `Uλ(Ji L Jf)` 共同给出；原文指出 `Uλ` 在 0 到 1 之间，因此对任一中间态，进入该态的 orientation flow 大于或等于从该态流出的总 orientation flow，表示反应链中 `λ>0` orientation/alignment component 逐步衰减，而不是 total feeding flow `φ` 本身衰减。 | method-formalism | direct | pp.229--230, Eqs.5--8 | false |
| C96-5 | 对 discrete levels，Avalanche II 计算的是来自 quasicontinuum 的 side-feeding orientation parameters `Bλ^(SF)`，不是该能级的 total population；离散 parent-state feeding 在提取 `σ` 时需显式加入。 | method-formalism | direct | p.230 and p.235, Eq.9 | false |
| C96-6 | Gaussian ansatz `PM∝exp(-M²/2σ²)` 的实用意义是把角分布分析未知量缩减为 `σ` 与 multipole mixing ratio `δ`；但作者认为 random-walk 和“许多相近强度路径”论证本身不足，路径数增加甚至可能恶化 Gaussian 近似。 | author-interpretation | direct | pp.230--231, Sec.3 | false |
| C96-7 | 作者解释 side-feeding `B2^(SF),B4^(SF)` 可能接近 Gaussian curve 的原因是 compound-state orientation 靠近 Gaussian curve 顶端，以及低 transferred momentum `L` 时 deorientation curves 与 Gaussian curve 相近；但 total orientation 是否 Gaussian 没有先验保证。 | author-interpretation | direct | pp.231--233, Fig.1 | false |
| C96-8 | 对 `110Pd(α,2nγ)112Cd` 的模型测试中，`J=10` 的 `B2^(SF),B4^(SF)` 与 Gaussian assumption 符合较好，`J=2` 偏差较大但仍合理；`σ2` 与 `σ4` 的相对差从 `J=10` 的 `0.2--0.4%` 到 `J=2` 的 `3--5%`。 | model-calculation | direct | pp.233--235, Fig.2 | false |
| C96-9 | 与实验比较时，计算较好再现 `110Cd` at `Eα=27 MeV` 的平均 `σ=2.2±0.5` 和 `112Cd` at `Eα=25 MeV` 的平均 `σ=2.1±0.4`；`112Cd` at `15 MeV` 的实验平均为 `σ=1.1±0.3`，计算平均值偏高，作者讨论了有效能量、少量可用 levels 和低能 neutron angular momentum 的影响。 | model-calculation | direct | pp.235--240, Figs.3--6 | false |
| C96-10 | Fig.7 用 `110Pd(α,2nγ)112Cd` 的 `851.2 keV` transition 说明，若把 side-feeding `σ` 限制在正确的 `2.1(4)` 或错误示范的 `1.1(3)` 区间，`χ²` 对 `M1+E2` mixing ratio `δ` 的结论会明显不同；作者据此强调给定 projectile energy 下可靠的 `σ` 区间对角分布解释很重要。 | model-calculation | direct | pp.240--241, Fig.7 | false |
| C96-11 | 结论中作者称 side-feeding part of the m-substate population 在本工作研究的 `110,112Cd` cases 中 approximately Gaussian，并支持相关角分布分析方法；但这是基于特定 statistical-model calculation 和数据比较。 | author-interpretation | direct | p.242, Conclusions | false |

## Nuclear Structure Information

This paper is method-oriented. It uses `110Cd` and `112Cd` as test cases for spin deorientation and side-feeding Gaussian widths, not as a new level-scheme or band-assignment source for the current Wiki.

## Authors' Interpretation

- The Gaussian hypothesis is plausible for the side-feeding part of the magnetic-substate population in the studied reactions, but must be checked for concrete cases.
- Reaction- and energy-dependent deorientation calculations can improve angular-distribution analysis when a reliable range of `σ` is needed.

## Model Results

- Avalanche II calculates orientation-flow propagation through angular-momentum routes using statistical-model ingredients.
- For the `Pd(α,2nγ)Cd` cases, calculated side-feeding `B2/B4` values are close enough to Gaussian curves to justify a single average `σ=(σ2+σ4)/2` in the authors' analysis.
- The calculated and experimental `σ` comparison is good at higher `Eα`; the lower-energy `112Cd` case remains less well reproduced.

## Competing Interpretations and Limitations

- The paper explicitly rejects indiscriminate generalization of the approximate Gaussian validity found for these reactions.
- The calculation constrains side-feeding population, not the total population of a level.
- The source uses Gaussian `σ`; it does not define the later practical `σ/I` or `σ/J` convention.

## Project Relation

For [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]], this source strengthens the evidence chain that alignment-width inputs are reaction- and feeding-history dependent. It also provides a direct example where the chosen `σ` interval changes the `δ` inference. It should be used as deorientation-method background, not as proof of one universal `σ/I` value.

## Extracted Pages

- Concepts: [[deorientation]], [[magnetic-substate-population]], [[side-feeding]], [[sigma-over-i]]
- Methods: [[angular-distribution]]
- Observables: [[angular-distribution-coefficient]], [[multipole-mixing-ratio]]
- Projects: [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]]

## Personal Notes

Review note: C96-4/C96-5/C96-10 were the source's most important P0 items for NST/P-ADO writing and were user-reviewed on 2026-07-09. Recheck Eq.5--9 symbol mapping and Fig.7 when converting this source into paper text.


## 2026-10-19 Codex续核：signed U、原Fig1与定义域

本节是本run新self-audit，**不属于旧用户审核**。原19页225–243/Eq1–9/七图主线重新读，旧人审前缀、C96-1–11与review字段保持；新claims仍needs_review。[[unobserved-feeding-alignment-sign]]保存完整推导、原图序列输入、反例、适用域和代码。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| C96-D16-1 | 原Eq6是带符号的6j定义；其后原句U∈(0,1)不能迁移成任意允许Ji/Jf/L/rank的恒等式。按同式1→1/L1/k2=−1/2、2→2/L2/k2=−3/14。原literal与本run定义域核验分列，不据此判Cd实际程序/实验失效。 | literal-versus-mathematical-domain | direct-plus-exact-control | p229 Eq6及紧随段落 | true |
| C96-D16-2 | Eq1归一的B基在均匀m下单位二阶范数，完整CGtrace使Eq6的U为两端基的内积，故一般abs(U)≤1；正号需附加路径域。rank4亦可负，如5/2→5/2/L2/k4=−1/2。 | signed-transfer-bound | Codex-CG-and-6j-model | Eqs1/6；本页新模型入口 | true |
| C96-D16-3 | Ω=φB是signedflow；本图J5/L1给U2=.9、B2<0，signedΩout>Ωin而幅度减小。因此“entry≥exit”的迁移须保留幅度/符号含义，不能当非负粒子流不等式。 | flow-definition-boundary | original-definition-plus-model | Eqs1/2/5；p232 Fig1 | true |
| C96-D16-4 | Fig1两条作者模型链是5→(j.5)11/2→(j.5)5，以及5→(j1.5)11/2→(j1.5)5→(L1)5→(L1)5；初m0。它们不是实验PM或完整side-feedingensemble。 | model-input-identity | direct-figure | p232 Fig1及下方说明 | true |
| C96-D16-5 | 本run重放两链的全部PM和rank0/2/4/6/8/10，CG与Eq6逐步闭合；只匹配B2/B4的Gaussianσ分别(.675686,.681492)与(2.146137,2.571571)，四个r多项式Sturm均1物理根。这是条件modelreplay，不是Fig2实验或新的Cd/Rh99σ。 | source-authored-model-replay | actual-exact-and-numeric-calculation | Fig1；unobserved-feeding-alignment-sign原链重放 | true |
| C96-D16-6 | Fig7的J2实线在两套σ约束下各仍有多个极小；正文以正确能量对应的σ=2.1(.4)支持小正δ，并用错误σ=1.1(.3)展示左极小变负。图不提供本run可重拟的原A2/A4/Σ/phaseproducer，未把各极小读成新δ/CI。 | branch-and-prior-boundary | direct-attributed-and-visual | pp240–241 Fig7/正文 | true |
| C96-D16-7 | 原低能模型限制含0.5MeV中子传输网格、起点.25MeV已有pwave，故近s-wave极限不能正确复现；约σ.8是作者讨论的反应极限，不等于Fig1任意单链的精确σ。 | computation-resolution-boundary | direct-original | p239 footnote4/Fig6；p240 Discussion | true |

`limits/revises`：保留本文反应特定的side-feeding结论，同时收紧一般positiveU、signedflow和Gaussian的迁移。`lnU4/lnU2`关系只在相同且正的U、分母非零等原条件下使用；当前未恢复AvalancheII实际routes/strength/transmission输入，也未拟新的851.2δ。新增结论只属Codex核验，不清旧/新needs_review或伪造人审。


### 原producer的限定可用性与旧知识重叠

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| C96-D16-8 | Ref8已核为Cejnar/Kern,NPA561,317–342(1993)，DOI10.1016/0375-9474(93)90015-P。当前仅取得metadata，公开producer/input包未得；API full401、publisherPDF403、authorpage证书失败及限定GitHub/Zenodo无匹配分开留档，不声称全球不存在代码。 | producer-readiness | metadata-and-bounded-access | p242 Ref8；本页可用性记录 | true |
| C96-D16-9 | [[yamazaki-1967-aligned-angular-coefficients]]原p3明确α可负，p7 2→2/L2给U2=−.21429。Day14的YA67-7已保存该反例；本session定向复核只新增与本文literal范围的对照，不把旧反例/旧49checks计新credit或独立实验。 | overlap-and-definition-crosscheck | primary-reinspection-and-provenance | YA67printedpp3/7；本页Eq6 | true |

2026-10-19限定路线未得AvalancheI/II版本化代码、粒子transmission/grid、gamma-strength/leveldensity、discrete分界和compoundentry/各levelinput；本日自有CG程序不是原producer重放。元数据与正文/代码访问、数学定义核验与实测σ分别保留。不会修复/更换凭据、关闭SSL验证或联系作者来绕过这一边界。
