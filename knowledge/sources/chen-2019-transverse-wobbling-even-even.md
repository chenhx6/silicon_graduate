---
type: source
title: "Transverse wobbling in an even-even nucleus"
aliases: [Chen Frauendorf Petrache 2019, transverse wobbling 130Ba]
created: 2026-07-15
updated: 2026-07-16
status: ai-draft
review_status: unreviewed
source_type: theory-article
reading_depth: deep-read
title_original: "Transverse wobbling in an even-even nucleus"
authors: [Q. B. Chen, S. Frauendorf, C. M. Petrache]
journal: Physical Review C
year: 2019
volume: 100
pages: 061301(R)
doi: 10.1103/PhysRevC.100.061301
arxiv:
language: en
canonical_source: doi:10.1103/PhysRevC.100.061301
zotero_item_key:
citation_key: chen_2019_Transversewobbling
zotero_uri:
library_file:
raw_file: "raw/papers/2019_Chen et al_Transverse wobbling in an even-even nucleus.pdf"
raw_sha256: 26E305B496B2FDFF4596670F772E3B030540B3C24D0830B8E4B4176C8070C768
nuclei: [130ba]
reactions: [122sn-13c-5n]
experiments: [gamma-ray-spectroscopy]
models: [triaxial-covariant-density-functional-theory, particle-rotor-model, tilted-axis-cranking]
observables: [wobbling-energy, mixing-ratio, interband-e2-strengths, bm1-be2-ratio, moments-of-inertia]
methods: [angular-distribution]
tags: [wobbling, transverse-wobbling, even-even, 130ba, two-quasiparticle, triaxiality]
---

# Chen, Frauendorf and Petrache (2019): Transverse wobbling in an even-even nucleus

## Bibliographic Record

Q. B. Chen, S. Frauendorf and C. M. Petrache, *Physical Review C* **100**, 061301(R) (2019), DOI `10.1103/PhysRevC.100.061301`. The BibTeX key is uniquely matched as `chen_2019_Transversewobbling`.

## Scientific Question and Motivation

The paper asks whether transverse wobbling can be realized with two aligned quasiprotons in an even-even nucleus. The candidate is the pair of `130Ba` bands S1 and S1-prime, assigned to a pi(h11/2)^2 configuration in the preceding spectroscopy work. The authors combine constrained triaxial covariant density functional theory (CDFT) with particle-rotor model (PRM) calculations rather than presenting a new level-scheme measurement.

## Scope and Reading Depth

Full five-page Rapid Communication read. Covered: the motivation and prior experimental input, angular-distribution mixing-ratio ambiguity, constrained CDFT deformation, TAC checks, PRM energy and transition-probability calculations, angular-momentum probability distributions, higher-band phonon assignments and limitations. Not covered: an independent reanalysis of the `130Ba` gamma-ray data or lifetime measurements beyond the ratios quoted from the experimental source.

## Summary

The CDFT/TAC plus PRM calculation proposes a stable transverse-wobbling interpretation for two `130Ba` bands built on pi(h11/2)^2. It combines energy, mixing-ratio-derived strength ratios and angular-momentum geometry, while retaining the two-solution delta ambiguity.

## Method and Design Logic

The constrained CDFT calculation supplies a triaxial shape and pi(h11/2)^2 configuration. TAC explores deformation sensitivity, while the PRM uses spin-dependent moments of inertia adjusted to the observed zero- and one-phonon bands. The paper tests the candidate through wobbling-energy trend, interband mixing-ratio-derived B(M1)/B(E2) and B(E2)/B(E2) ratios, and the angular-momentum probability distributions for the n = 0 and n = 1 states.

## Key Results

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CH19-1 | The experimental input consists of two observed `130Ba` bands S1 and S1-prime, populated in the 122Sn(13C,5n) reaction at 65 MeV; their connecting Delta-I = 1 mixing ratios and transition-probability ratios were taken from prior angular-distribution work. | review-background / observed-fact-input | direct | PDF p. 1 and Table I | true |
| CH19-2 | The prior angular-distribution fits can produce two chi-squared solutions for a mixing ratio delta, one with absolute value below 1 and one above 1; the paper adopts the smaller solution because it has the lower chi-squared, while explicitly noting that the larger solution cannot be excluded from angular distributions alone. | method / experimental-criterion | direct | PDF p. 2, paragraph before Table I | true |
| CH19-3 | Constrained CDFT assigns the pi(h11/2)^2 configuration to S1/S1-prime and finds a triaxial minimum near beta = 0.24, gamma = 21.5 degrees, with an excited-shape energy comparable to the experimental band excitation; this is a model assignment and not a direct shape measurement. | model-calculation / author-interpretation | direct | PDF p. 2, CDFT and TAC paragraphs | true |
| CH19-4 | The PRM uses spin-dependent moments of inertia whose fitted short-to-medium ratio is larger than the irrotational-flow value; the authors associate this choice with stabilizing transverse wobbling and note microscopic-cranking and deformation-fluctuation caveats. | model-calculation / limitation | direct | PDF p. 2, PRM parameter paragraph | true |
| CH19-5 | The PRM reproduces the S1 and S1-prime energy sequences and gives a wobbling energy that decreases through the displayed spin interval, which the authors use as evidence supporting transverse wobbling. | model-calculation / author-interpretation | direct | PDF p. 2, Fig. 1(a)-(c) | true |
| CH19-6 | Calculated B(E2)out/B(E2)in ratios agree with the available experimental values within uncertainties and vary approximately as tan-squared(gamma); the large interband E2 strength is treated as a collective wobbling fingerprint, not as a sufficient model-independent proof. | model-calculation / experimental-criterion | direct | PDF p. 3, Table I and text below Fig. 1 | true |
| CH19-7 | The calculated B(M1)out/B(E2)in values are somewhat larger than experiment; with two high-j protons the ratio is larger than in one-quasiparticle odd-A examples, so the E2 fraction of the Delta-I = 1 transition is smaller and does not dominate as strongly. | model-calculation / limitation | direct | PDF pp. 2-3, Table I and transition-strength discussion | true |
| CH19-8 | PRM angular-momentum distributions for S1 and S1-prime are centered in the short-medium plane, with maxima characteristic of phi-symmetric n = 0 and phi-antisymmetric n = 1 wavefunctions; the probability density itself is even; the authors interpret the stable rim and short-axis proton alignment as a two-quasiparticle transverse-wobbling geometry. | model-calculation / author-interpretation | direct | PDF pp. 3-4, Figs. 2-3 | true |
| CH19-9 | The calculated n = 2 and n = 3 candidates show additional nodes and wider precession cones, while their interband E2 and M1 strengths grow more slowly than the harmonic n scaling and Delta-n = 2 transitions remain suppressed. | model-calculation | direct | PDF p. 4, Fig. 4 and multiphonon discussion | true |
| CH19-10 | The authors distinguish the proposed wobbling connection from the higher AC configuration by its much smaller calculated connecting E2/M1 strengths; this is a PRM comparison and does not by itself exclude all signature-partner alternatives. | model-calculation / competing-interpretation criterion | direct | PDF p. 4, AC-band paragraph and Fig. 4 | true |
| CH19-11 | The paper concludes that S1-prime is the first proposed two-quasiparticle transverse-wobbling band in an even-even nucleus and calls this the most stable transverse-wobbling case known at publication time; this is the authors' synthesis of experimental inputs and model calculations. | author-interpretation | direct | PDF pp. 1 and 4, Abstract and Summary | true |

## Analytical Reconstruction

The evidence chain is deliberately layered: prior gamma spectroscopy supplies bands, angular-distribution mixing ratios and reduced-transition ratios; CDFT/TAC supplies a plausible triaxial two-proton configuration; PRM tests whether the same inputs generate decreasing wobbling energy, collective interband E2 strength and the expected angular-momentum topology. The two-solution delta ambiguity is an explicit gate: adopting the small solution is a choice supported by chi-squared ranking, not a unique experimental determination.

## Competing Interpretations and Limitations

- The source is a theory paper using prior `130Ba` spectroscopy, not a new transition measurement.
- The adopted small-|delta| solution is not unique from angular distributions alone.
- CDFT deformation, spin-dependent MoI and PRM geometry are model inputs; signature-partner alternatives remain a reverse test.

## Assumptions, Limits and Reverse Tests

- The source is a theory/model paper using prior experimental data. It should not replace the original `130Ba` spectroscopy source for transition energies, detector details or mixing-ratio extraction.
- Spin-dependent moments of inertia and a constrained CDFT shape are inputs to the PRM. A reverse test is to vary the deformation and MoI within the quoted ranges or compare a signature-partner/TPSM interpretation.
- Decreasing wobbling energy and strong E2 links are joint criteria; neither excludes a competing band explanation without independent configuration, polarization, lifetime or complete transition data.
- The adopted small-|delta| branch should be revisited if later angular-distribution, polarization or conversion data discriminate the second solution.

## Related Knowledge and Project Relation

- Concepts: [[wobbling-motion]], [[transverse-wobbling]], [[triaxial-deformation]], [[signature-partner-bands]], [[angular-momentum-alignment]]
- Models: [[particle-rotor-model]], [[tilted-axis-cranking]], [[covariant-density-functional-theory]]
- Methods/observables: [[angular-distribution]], [[multipole-mixing-ratio]], [[wobbling-energy]], [[interband-e2-strengths]], [[bm1-be2-ratio]]
- Projects/synthesis: [[low-spin-wobbling-controversies]], [[wobbling-vs-signature-partner]]

This source extends the wobbling theory lineage to an even-even two-quasiparticle configuration; it is not direct evidence for the later low-spin `135Pr` controversy.

## Extracted Pages

- Nucleus: `130Ba` (theory interpretation of previously reported bands)
- Concepts: [[wobbling-motion]], [[transverse-wobbling]], [[triaxial-deformation]], [[signature-partner-bands]]
- Models/observables: [[particle-rotor-model]], [[covariant-density-functional-theory]], [[multipole-mixing-ratio]], [[wobbling-energy]]
- Project: [[low-spin-wobbling-controversies]]

## Human Review Triage

P0:

1. **CH19-1/CH19-2, PDF pp. 1-2 and Table I.** Verify the reaction/beam details, the source of the angular-distribution data and the two-solution delta statement; this is essential for the evidence gate.
2. **CH19-5/CH19-6, PDF pp. 2-3, Fig. 1 and Table I.** Check the wobbling-energy definition, ratio directions and whether “evidence” is attributed to the PRM comparison.
3. **CH19-8/CH19-10, PDF pp. 3-4, Figs. 2-4.** Verify the angular-momentum geometry, multiphonon nodes and the distinction from the AC/signature-partner-like configuration.

P1:

- CH19-3/CH19-4: verify the CDFT/TAC deformation and fitted-MoI wording.
- CH19-7/CH19-9/CH19-11: check the quantitative M1 limitation and the strength of the publication-era “first example” wording.

## Review Status

Page and all CH19 claims remain unreviewed with `needs_review: true`. Human review is deferred until use: perform targeted claim review when this content is used for paper writing, a key project decision, synthesis finalization or a paper-level evidence pool.

## Day18 checkpoint053修订：两准粒子M1主导与PRM模型边界

原CH19-claims保持；旧CH19-D18-1降格为superseded。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CH19-D18-1 | **superseded**：旧关于“无法确立横向wobbling”的断言降格，由CH19-D18-2/3分层记录作者对130Ba带间跃迁72%-75% M1主导的承认与两准粒子/剪刀振动物理机制解释。 | task-correction | superseded-interpretation | 本段D18-2/3；旧chen19-130ba-wobbling-result-029 | true |
| CH19-D18-2 | 本文Table I报告130Ba两准粒子带S1_prime向S1连接线混合比为delta = -0.58至-0.62，对应E2份额25.2%-27.8%、M1份额72.2%-74.8%；作者明确指出该跃迁以磁偶极为主，并将其解释为两准粒子构型中多一个高j准粒子使M1矩阵元增大；scissor耦合则从TW抽走M1强度，PRM未包括后者（Day23原件纠正）。 | source-result-and-method | direct | PDF pp.2-3 Table I；Sec. III | true |
| CH19-D18-3 | PRM理论计算在I=13至21范围内预测B(M1_out)/B(E2_in)为0.63至1.11，系统高出实验测量（0.23至0.43）1.47至3.30倍；作者指出可由PRM未包括scissor耦合从TW抽走M1强度来解释（Day23按原文纠正），但能量与角动量取向仍支持两准粒子横向摆动图像。 | author-interpretation-boundary | direct-and-boundary | PDF pp.2-3 Table I；Sec. IV | true |

## Day22 checkpoint091 直接原件纠错

本次读本地5页全文，视觉核061301-2 Table I/参数与061301-3说明；未复跑CDFT/PRM或原实验。SHA256 26e305b496b2fdff4596670f772e3b030540b3c24d0830b8e4b4176c8070c768。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CH19-D22-R091-1 | Table I在I=13/15/17给实验输入δ=−.58(.13)/−.62(.10)/−.62(.10)，rE2=.32(+.18/−.15)/.36(+.70/−.19)/.22(+.27/−.10)。它们是复用早期谱学的相对值。作者明确约25% E2仍可与集体E2增强及两准粒子TW模型相容，不能由M1份额较大直接改判为磁转动剪刀带。 | source-reported-ratios-and-interpretation | direct-original | 061301-2, Table I; 061301-3, electromagnetic discussion | true |
| CH19-D22-R091-2 | 角分布选小模δ因χ²较低，但作者说明大模解不能仅由角分布完全排除。惯量参数按两带能量调整；Fig.2–3给模型取向分布/RMS而非实验测量。支持解释与选解、定标边界须同时保留。 | model-dependency-and-experimental-limit | direct-original | 061301-2, paragraphs below Table I and PRM parameters; 061301-3, Figs.2–3 | true |

## Day23 checkpoint061：原实验复用、轴映射及scissor方向纠正

本次重新读取Petrache PLB795(2019)241–247全文及4页supp、Chen PRC100(2019)061301全文、Wang PLB802(2020)135246全文，并视觉核对关键图表。Petrache是原实验；Chen Ref16与Wang Ref19均回指Petrache，Wang Ref20回指Chen。后二者是不同模型框架对既有S1/S1′输入的解释，不构成新实验票。Petrache补充TableI只涉及D1和t-band；S1′的δ表需回Chen 061301-2 TableI，不能由该supp拼出完整S1′向量。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BA130-D23-061-01 | Petrache2019提供原实验谱学；Chen2019与Wang2020分别用PRM和PSM解释复用的S1/S1′实验输入。它们不构成独立实验重复。 | source-dependency-synthesis | direct-original-and-synthesis | Petrache p242 Sec2；Chen 061301-1末两段/-5 Ref16；Wang pp1–3和p5 Ref19/20 | true |
| BA130-D23-061-09 | 两个高j准粒子增大M1矩阵元，与约25%的E2份额相容；作者随后用QRPA背景指出scissor coupling从TW抽走M1强度，而PRM未包含此耦合，用来解释PRM对M1的高估。 | author-interpretation-and-correction | direct-original | Chen 061301-3左栏，TableI讨论及以The overestimation开头段落 | true |

纠错关系：CH19-D18-2中“与剪刀振动模式耦合带来的M1增强”应替换为“多一个高j准粒子使M1矩阵元增大”；CH19-D18-3中“模型对集体声子与粒子自由度耦合强度的过高估计”应替换为“文中援引QRPA对scissor耦合抽走TW的M1强度、而PRM未包含此耦合的解释”。原来的实验δ与表比值不因此抹除。BA130-D23-061-09只核准Chen的叙述，未独立读其QRPA Ref29。

补充方法边界：Chen惯量按零/一声子能量调参；P(θ,ϕ)、RMS和AC连接强度均为模型输出。Wang采用β=.24、γ=30°，Chen PRM采用β=.24、γ=21.5°，不能混成同一个参数集。Chen从s轴起算ϕ，Wang从i轴起算φ，短轴分别在0°和90°；须先映射轴再比较。Wang I=23可能接近临界自旋、Chen范围未达失稳点，都保留各自模型语境。


同一实验谱系见[[petrache-2019-diversity-shapes-rotations-130ba]]与[[wang-2020-two-quasiparticle-wobbling-130ba]]。没有新采集或独立选根证据。
