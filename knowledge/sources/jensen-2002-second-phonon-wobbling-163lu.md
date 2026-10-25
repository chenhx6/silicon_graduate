---
type: source
title: "Jensen et al. 2002 - Evidence for Second-Phonon Nuclear Wobbling"
aliases: [Jensen 2002 163Lu second phonon wobbling, Evidence for Second-Phonon Nuclear Wobbling]
created: 2026-07-16
updated: 2026-10-24
status: active
review_status: human-reviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Evidence for Second-Phonon Nuclear Wobbling"
authors: [D. R. Jensen, G. B. Hagemann, I. Hamamoto, S. W. Ødegård, B. Herskind, G. Sletten, J. N. Wilson, K. Spohr, H. Hübel, P. Bringel, A. Neußer, G. Schönwaßer, A. K. Singh, W. C. Ma, H. Amro, A. Bracco, S. Leoni, G. Benzoni, A. Maj, C. M. Petrache, G. Lo Bianco, P. Bednarczyk, D. Curien]
journal: Physical Review Letters
year: 2002
volume: 89
pages: 142503
doi: 10.1103/PhysRevLett.89.142503
arxiv:
language: English
canonical_source: https://doi.org/10.1103/PhysRevLett.89.142503
zotero_item_key:
citation_key: jensen_2002_EvidenceSecondPhonon
zotero_uri:
library_file:
raw_file: "raw/papers/2002_Jensen et al_Evidence for Second-Phonon Nuclear Wobbling.pdf"
raw_sha256: C6FD99C17C09763F742CBE36443F7039F21B3E28A5CAA548748BDF0718630A8A
nuclei: [163lu]
reactions: ["139La(29Si,5n)163Lu"]
experiments: []
models: [particle-rotor-model]
observables: [multipole-mixing-ratio, interband-e2-strengths, bm1-be2-ratio, moments-of-inertia]
methods: [gamma-gamma-coincidence, dco-ratio, angular-distribution]
tags: [experiment-ingest, wobbling, two-phonon, triaxial-superdeformation, lutetium]
---

# Evidence for Second-Phonon Nuclear Wobbling

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

PRL 89, 142503 (2002), DOI `10.1103/PhysRevLett.89.142503`; first-page title/DOI and BibTeX key `jensen_2002_EvidenceSecondPhonon` match.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: full article, level scheme, TSD3 decay links, DCO/angular-distribution ratios, two mixing-ratio branches, relative transition strengths and particle-rotor comparison.
- Not covered: independent reproduction of efficiency corrections or model calculations.
- Coverage caveats: the decisive 476-keV link lacks usable polarization, so branch selection is model- and similarity-dependent.

## Paper Question and Scientific Motivation

- Test whether TSD3 is a two-phonon wobbling excitation by establishing `TSD3→TSD2` links and checking the phonon-rule enhancement relative to `TSD2→TSD1` (PDF pp.1-2).

## Method and Design Logic

- A higher-statistics Euroball IV run establishes four `ΔI=1` TSD3→TSD2 and eight `ΔI=2` TSD3→TSD1 transitions.
- DCO/angular-distribution ratios constrain multipolarity; the 476-keV link's two `δ` branches are compared with band similarities and particle-rotor transition strengths.

## Key Evidence and Reasoning Chain

- Similar `J^(2)` and relative alignment for TSD2/TSD3 → shared intrinsic family (PDF pp.3-4, Fig.4).
- Large-`abs(δ)` solution for the 476-keV link gives `B(E2)_out/B(E2)_in=0.51(13)`, approximately twice the one-phonon value `0.21(1)` → consistent with the phonon rule (PDF p.3, Table II; p.4, Fig.5).
- Small-`abs(δ)` solution cannot be rejected experimentally because polarization failed; authors reject it through model/band-family consistency and assign TSD3 as two-phonon wobbling.

## Summary

The paper presents evidence, not a polarization-complete experimental determination, for a second-phonon wobbling band in `163Lu`. Its strongest claim depends on choosing the large-E2 branch of one measured TSD3→TSD2 transition.

## Experimental or Theoretical Setup

- `139La(29Si,5n)163Lu`, 157 MeV Vivitron beam at IReS Strasbourg.
- Euroball IV: 15 cluster, 25 clover and 27 tapered Compton-suppressed Ge detectors plus BGO multiplicity filter.
- Approximately `6×10^9` γ-coincidence events; `γ^3` cube plus angle-pair matrices.
- Alignment parameter `σ/I=0.25(2)` over `61/2` to `29/2`.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| JE02-1 | Four `ΔI=1` TSD3→TSD2 and eight `ΔI=2` TSD3→TSD1 transitions were established; TSD3 reaches `85/2`. | experimental-fact | direct | PDF p.2, Figs.1-2 | true |
| JE02-2 | Angular-distribution and DCO ratios support stretched E2 character for TSD3→TSD1 links and mixed E2/M1 for the 476-keV TSD3→TSD2 link. | experimental-criterion | direct | PDF pp.2-3, Tables I-II | true |
| JE02-3 | Polarization of the 476-keV link could not be measured; experiment alone therefore could not select between `δ=-3.60^{+0.97}_{-1.93}` and `δ=-0.19^{+0.08}_{-0.12}`. | experimental-fact | direct | PDF p.3 | true |
| JE02-4 | The adopted large branch corresponds to about `92.8%` E2 and `B(E2)_out/B(E2)_in=0.51(13)`; the small branch gives `0.019^{+0.024}_{-0.017}`. | experimental-fact | direct | PDF p.3, Table II | true |
| JE02-5 | TSD2 and TSD3 have nearly identical dynamic moments of inertia and relative alignments, differing by only about `0.1ħ`. | experimental-fact | direct | PDF pp.3-4, Fig.4 | true |
| JE02-6 | Particle-rotor calculations associate TSD1/TSD2/TSD3 with `n_w=0/1/2` and reproduce the large-E2 branch and approximate phonon scaling. | model-result | direct | PDF pp.3-4, Figs.3 and 5 | true |
| JE02-7 | The authors assign TSD3 as two-phonon wobbling and state that this proves triaxial deformation. | author-interpretation | indirect | PDF p.4, conclusion | true |
| JE02-8 | Calculated M1 strength exceeds the experimental upper limit by more than a factor two; authors attribute this partly to omitted gradual neutron alignment. | model-result | direct | PDF p.4 | true |

## Nuclear Structure Information

TSD1, TSD2 and TSD3 populations are reported as about 10%, 3% and 1.2% of yrast. TSD3 decays both to TSD2 (`ΔI=1`) and directly to TSD1 (`ΔI=2`), the latter weak links being attributed to anharmonicity.

## Authors' Interpretation

TSD3 is assigned as `n_w=2`, mainly because the large-E2 branch yields the expected enhancement and the three bands share rotational properties. The paper's “proves triaxial deformation” wording is preserved as attribution.

## Model Results

The particle-rotor calculation identifies four low bands as a wobbling family and uses angular-momentum components to illustrate increasing tilt with phonon number. The predicted M1 discrepancy and the dependence on the selected `δ` branch are material limitations.

## Competing Interpretations and Limitations

- No experimental polarization branch selection for the 476-keV transition.
- Only one of four TSD3→TSD2 links yields a transition-strength ratio.
- The small-`δ` branch is rejected by comparison with calculated band families, not by an independent direct observable.
- Relative rather than absolute strengths are used.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| JE02-AR-1 | Core reconstruction | TSD3 adds an experimentally connected third band and a proposed n_w=2 hierarchy, but the decisive strength point depends on an unpolarized 476-keV link. | Key Results and Competing Interpretations above | unreviewed |
| JE02-AR-2 | Assumptions and dependencies | The large-|δ| solution for the 476-keV link and the common TSD band family selected by the PRM comparison are correct. | Method/results/model sections cited above | unreviewed |
| JE02-AR-3 | Transfer conditions | Require multiple adjacent-band links, branch-independent electromagnetic information, and stable band identity before transferring a multiphonon label. | Source scope and claim locators above | unreviewed |
| JE02-AR-4 | Failure conditions | The small-|δ| solution removes the phonon-rule enhancement; one usable TSD3→TSD2 point cannot establish robust scaling by itself. | Competing Interpretations and Limitations above | unreviewed |
| JE02-AR-5 | Reverse/falsification test | Obtain polarization and lifetimes for several TSD3→TSD2 links and retest Table II without model-selected branch choice. | Follow-up observables identified by the source/Agent | unreviewed |
| JE02-AR-6 | Research-question decision | Keep as an early two-phonon benchmark with a prominent single-point/branch-selection warning. | Whole-source assessment | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: The Wiki contained the one-phonon TSD1/TSD2 benchmark but no independently reviewed two-phonon strength test.
- Effect of this source: revises
- Reason: TSD3 adds an experimentally connected third band and a proposed n_w=2 hierarchy, but the decisive strength point depends on an unpolarized 476-keV link.
- Persistence decision: project update / synthesis update
- Review state: page-level `human-reviewed`; Key Results claims remain `needs_review: true` for future claim-specific paper use.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[wobbling-motion]] | Early adjacent-band phonon-scaling test. |
| limits | [[interband-e2-strengths]] | Demonstrates how an unresolved `δ` branch controls the inferred enhancement. |
| foundational-background | [[low-spin-wobbling-controversies]] | High-spin multiphonon benchmark, not direct low-spin evidence. |

## Human Review Triage

Review disposition: the user completed a rough page-level review on 2026-07-25 and accepted the current evidence-calibrated wording without correction. The P0/P1 items below are retained as future strict paper-use verification prompts, not unresolved ingest blockers.

### P0

- `JE02-3`/`JE02-4`, 476-keV TSD3→TSD2 link, Table II — Evidence: polarization failed and two δ solutions remain; only the large-|δ| branch gives `B(E2)_out/B(E2)_in=0.51(13)`. Agent inference: the headline two-phonon scaling rests on one model-selected effective strength point. User check: Table II values, branch choice, and whether the band-family argument justifies rejection of the small branch. Risk: the n_w=2 evidence chain collapses if the small branch is viable.

### P1

- `JE02-6`/`JE02-8` — Review the PRM family assignment and M1 overprediction before using the paper as a quantitative multiphonon benchmark.

### P2/P3

- P2: weak direct TSD3→TSD1 links and anharmonicity wording. P3: metadata/navigation.

## Human Review Record

- 2026-07-25: the user completed a rough review of this source page and accepted its current claims, attribution boundaries, locators and stated limitations without requesting corrections.

## Review Status

Page-level review is complete for this ingest round. Claim-level `needs_review` and Analytical Reconstruction review markers remain unchanged because this was a rough review rather than exhaustive claim-by-claim paper certification.

## Extracted Pages

- Nuclei: [[163lu]]
- Bands: [[163lu-sd1]], [[163lu-sd2]], [[163lu-tsd3]]
- Concepts: [[wobbling-motion]]
- Methods: [[dco-ratio]], [[angular-distribution]]

## Non-source Notes and Follow-up

Keep the 476-keV/Table II branch issue in source-local P0 until user review.

## Day18 checkpoint051修订：163Lu 476-keV根选择的实验缺口

原JE02-claims/review保持；旧JE02-D18-1数值保为条件审计。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| JE02-D18-2 | 原文明确476-keV线统计不足、无法作线偏振分析，两个δ分支不能由该实验本身排除；大根−3.60是依据TSD2/TSD3相似转动性质与PRM选择，非偏振直接确证。 | source-branch-selection-boundary | direct | PDF p.199 TableII；p.200 text | true |
| JE02-D18-3 | 在固定其它输入下，大根与小根fE2比例约26.8，故.51与.019是条件分支差异；TSD3→TSD1的纯伸展E2表列则是另一组Δn=2观测/赋值，不构成476线根选择的独立偏振证据。 | conditional-strength-sensitivity | derived-and-boundary | PDF pp.199–200 Tables I–II；new highspin-root-boundary-result-051 | true |


## Day18定量审计：二声子谐振标度对476 keV无偏振混合比双解的极端依赖

在Day18正式学习中对本文Table I与Table II中163Lu二声子wobbling带（TSD3）的电磁跃迁强度比及多极解依赖进行定量审计，raw SHA256 `C6FD99C17C09763F742CBE36443F7039F21B3E28A5CAA548748BDF0718630A8A`已核。原JE02-1–8各claim及`human-reviewed`状态完全保留；新JE02-D18-1待审。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| JE02-D18-1 | superseded by checkpoint092：旧411.8/15.3/16.1 W.u.由额外绝对尺度换算，未由本文寿命测定；26.84是两个相对根中心值之商，不是物理动态塌缩。原文八条ΔI=2线与六行Table I均保留；见JE02-D22-R092-1/3/4。 | task-correction | direct-original-audit | 本页R092原件条目；旧任务数值不认证 | true |

新[分析合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/jensen02-163lu-wobbling-contract-026.json)及[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/jensen02-163lu-wobbling-result-026.json)4项检查全过。

## Day 21 Checkpoint 023 证据门量化审计：163Lu 双声子候选带角分布选解漏洞与非谐性破缺

依据推断阶梯方法论（[[experimental-claim-boundaries]]）及独立量化程序 day21_checkpoint023_lu163_wobbling_phonon_audit.py（产物 outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/lu163-wobbling-phonon-audit-023.json），对 Jensen 2002 的双声子摇摆主张完成推断阶梯边界核定：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| JE02-D21-1 | superseded by checkpoint092：原认证撤回：476未测偏振是实际缺口，但作者选根还比较J(2)/i_x与PRM整套电磁性质；八条直接ΔI=2线是原文报告的非谐退激，不证明所有wobbling解释失败。见JE02-D22-R092-1/2。 | task-correction | direct-original-audit | 本页R092原件条目；旧任务数值不认证 | true |

## Day22 原件复核：476keV逐线身份与未选解边界

全文正文与图表实际重读；关键数据/图表视觉核验，raw哈希保持。以下仅Codex self-audit，原page review/既有claim flags不改；新增claims均needs_review:true。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| JE02-D22-001 | Fig1将476keV绑定TSD3 45/2+→TSD2 43/2+，其同母态带内E2为627keV至TSD3 41/2+。TableII λ=.14(.04)指该带外/带内光子分支；不能用任意spin的TSD2带内线作其分母。 | transition-identity | direct-original | 142503-2, Fig.1; 142503-3, Table II | true |
| JE02-D22-002 | 476keV因统计不足无法测偏振，作者明确说不能在实验上选两个δ分支；大解−3.60(+.97/−1.93)与小解−.19(+.08/−.12)对应rE2=.51(.13)与.019(+.024/−.017)。采用大解依赖band-family和PRM一致性，不能称偏振排他选解。 | experimental-limitation-and-author-choice | direct-original | 142503-3, post-Table-I discussion and Table II; 142503-4, small-root paragraph | true |
| JE02-D22-003 | TableII的.51/.21中央商约2.43支持作者的近二倍阶梯讨论，但分子为45/2的TSD3退激、基准为TSD2多线平均，未提供此商的jointCov或严格同I实验检验。相近i_x/J(2)并不消除476未测偏振。 | comparison-and-uncertainty-boundary | direct-original-and-bounded-inference | 142503-3, Table II; 142503-4, Figs.4-5 | true |
| JE02-D22-004 | 本文新采集为157MeV、约6×10^9事件，与OD01所述152MeV、2.4×10^9的采集条件不同；一声子指认/δ背景仍回指旧文，H03/F14再次引用这些点不增加采集数。旧基准的逐量来源与Cov应逐项确认。 | source-lineage | direct-original-and-cross-source-comparison | 142503-1–2, introduction and experiment; 142503-3, previous-value paragraph | true |

### Knowledge Impact and Learning Decision

Supports/limits：保留作者的支持或反对解释，并将逐线测量、选解前提、模型结果和依赖链分开。四列比较与条件强度重建见[[wobbling-geometry-phonon-observable-contract]]；不以模型或跨采集中心值差替代新实验置信区间。


## Day22 checkpoint092：163Lu原始观测与强度对象复核

本次完整重读4页，视觉核142503-2 Fig.1/Table I及142503-3 Table II；SHA256 c6fd99c17c09763f742cbe36443f7039f21b3e28a5caa548748bdf0718630a8a。表重建是任务算术，不重放原计数/响应/联合CI，未新增绝对B测量。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| JE02-D22-R092-1 | 新采集确立四条TSD3→TSD2 ΔI=1及八条TSD3→TSD1 ΔI=2线，后者由AD/DCO判伸展E2（文中说明disregarding M2）；Table I六条打印rE2=.021/.022/.018/.017/.022/.020。作者将这些约.02的有限强度解释为非谐性并与PRM比较，不是未观测跨两声子衰变。 | experimental-topology-and-author-interpretation | direct-original-and-bounded-reconstruction | 142503-2, observation paragraphs, Table I and Fig.1; 142503-4, first paragraph and Fig.5 | true |
| JE02-D22-R092-2 | 476 keV因统计不足不能测偏振；作者明确实验本身不能选δ根，大根选择还使用相近J(2)/相对i_x、band-family和PRM电磁性质比较，而非只有两倍强度预期。该解释有模型条件，但将其简化为代数循环或排他证伪均过强。 | branch-selection-and-support-boundary | direct-original-and-bounded-reconstruction | 142503-3, paragraphs on polarization and band similarities; 142503-4, small-root comparison and Conclusion | true |
| JE02-D22-R092-3 | 476/627同45/2母态的λ=.14及δ中心−3.60/−.19按γ率关系重建rE2≈.5154/.01934、rM1≈.00628/.08465，分别与打印.51/.019和.006/.083在输入末位舍入范围相容。这里全为相对B；没有τ不能换W.u.。打印.51/.019≈26.84是替代根的中央值敏感性，不是实测强度动态暴跌。 | task-rate-identity-and-input-boundary | direct-original-and-bounded-reconstruction | 142503-2, Fig.1; 142503-3, Table II; 142503-4, small-root paragraph; lu163-relative-strength-audit-092.json | true |
| JE02-D22-R092-4 | Table II的.51/.21≈2.43比较两个带各自归一的相对强度；要解释为绝对B(2→1)/B(1→0)，还须指定相应带内B尺度与spin匹配。本文以PRM及相近转动性质支持声子解释；该商不是独立寿命或精确同I两倍玻色子规则检验。 | normalized-ratio-and-phonon-test-boundary | direct-original-and-bounded-reconstruction | 142503-3, Table II; 142503-4, Fig.5 and comparison text | true |

## Day22 checkpoint100：同母态双带外E2比与归一消去

本次视觉回核142503-2 Fig1局部及TableI，和p3 TableII；不重称整篇新通读。45/2+ TSD3同母态的1119.2→TSD1(41/2+)、476→TSD2(43/2+)与627→TSD3(41/2+)已逐线映射。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| JE02-D22-R100-1 | 1119.2keV在TableI给λ=.33(.05)、rE2=.018(.003)，与TableII476的λ=.14(.04)及rE2=.51/.019共用627keV带内分母和TSD3 45/2+母态。故B(E2;1119)/B(E2;476)的打印中央商为.03529或.94737；直接光子式(λ1119/λ476)(476/1119.2)^5/fE2(δ476)给.03533/.94141，末位输入不同造成小偏差。此比不需τ或带内绝对B，但仍依赖476的未选δ及原E2赋值。 | same-parent-exit-ratio-and-normalizer-cancellation | direct-original-and-task-arithmetic | 142503-2 Fig1/TableI1119.2row;142503-3 TableII476row | true |
| JE02-D22-R100-2 | 两个out/in相对比相除因共母态/分母可消去带内尺度；不同母态的.51/.21则不能同样消去。新out/out重表达共享原γ计数/δ，不能作为第三个独立实验为大根投票，也不能在缺Cov时将两表误差当独立传播。大小根分别意味着直接TSD3→TSD1的E2约为邻带出口的3.5%或可比量级；与作者的非谐退激解释比较仍需明确模型，不能据有限Δn≈2排除所有wobbling。 | dependence-and-phonon-interpretation-boundary | source-conditioned-algebra | 142503-2 Fig1/TableI;142503-3 TableII;142503-4 anharmonicityparagraph | true |

## Day22 checkpoint122：已选δ条件下的M1上限

本次同SHA原件四页全文文本回读，fresh visual核142503-2 Fig1/TableI、142503-3 Fig2/3/TableII和142503-4 Fig4/5/模型比较。1119.2/476/627母态绑定及原双根/偏振缺口与现有条目一致。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| JE02-D22-R122-1 | 采用476大根后，作者报rM1=.006(+.006/−.004)，并将模型rM1=.026与称为experimental upper limit的.012比较，单位均μN²/(e²b²)；同文小根给.083(.024)。因此该.012属于既定大根解释下的比较，不能独立反过来选δ或被改写为绝对B(M1)上限。本文未提供可供本任务重报新σ排除度的完整likelihood。 | source-chosen-branch-and-statistical-boundary | direct-original-and-bounded-inference | 142503-3large-rootrM1paragraph;142503-4M1comparisonandsmall-rootparagraphs | true |
