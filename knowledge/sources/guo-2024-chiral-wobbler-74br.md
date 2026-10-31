---
type: source
title: "Guo et al. 2024 - Evidence for Chiral Wobbler in Nuclei"
aliases: [Guo 2024 74Br chiral wobbler]
created: 2026-07-16
updated: 2026-09-20
status: active
review_status: human-reviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Evidence for Chiral Wobbler in Nuclei"
authors: [R. J. Guo, S. Y. Wang, C. Liu, R. A. Bark, J. Meng, S. Q. Zhang, B. Qi, A. Rohilla, Z. H. Li, H. Hua, Q. B. Chen, H. Jia, X. Lu, S. Wang, D. P. Sun, X. C. Han, W. Z. Xu, E. H. Wang, H. F. Bai, M. Li, P. Jones, J. F. Sharpey-Schafer, M. Wiedeking, O. Shirinda, C. P. Brits, K. L. Malatji, T. Dinoko, J. Ndayishimye, S. Mthembu, S. Jongile, K. Sowazi, S. Kutlwano, T. D. Bucher, D. G. Roux, A. A. Netshiya, L. Mdletshe, S. Noncolela, W. Mtshali]
journal: Physical Review Letters
year: 2024
volume: 132
pages: 092501
doi: 10.1103/PhysRevLett.132.092501
canonical_source: https://doi.org/10.1103/PhysRevLett.132.092501
citation_key: guo_2024_EvidenceChiral
raw_file: "raw/papers/2024_Guo et al_Evidence for Chiral Wobbler in Nuclei.pdf"
raw_sha256: 1783B784C3843E15DE39406182613757F9C3B928A2791E45A7D650F117EA4333
supplementary_raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/三轴/进动/实验/2024_Guo et al_Evidence for Chiral Wobbler in Nuclei 1.pdf"
supplementary_raw_sha256: 1eb2c1af4ff7d1bf6460c154baabacb80e3ca7e63fa1832ca1d1b3d58b5ea9a0
alternate_version_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/三轴/进动/实验/2024_H. Amro et al_Evidence for Chiral Wobbler in Nuclei.pdf"
alternate_version_sha256: f8ca78604264fc3cf5081d8ddd20c2a8e708e3fe4526d73fa037f1f75c532fe6
nuclei: [74br]
reactions: ["58Ni(19F,2p1n)74Br"]
experiments: []
models: [particle-rotor-model]
observables: [multipole-mixing-ratio, interband-e2-strengths, bm1-be2-ratio]
methods: [angular-distribution, linear-polarization-asymmetry, doppler-correction]
tags: [experiment-ingest, chiral-wobbler, chirality, wobbling, lifetime, odd-odd, a80]
---

# Evidence for Chiral Wobbler in Nuclei

## Bibliographic Record

PRL 132, 092501 (2024), DOI `10.1103/PhysRevLett.132.092501`; PDF/BibTeX identity checked. On 2026-08-11 the local PDF identity was reverified from its title page, author list, journal/article number and DOI, and `raw_sha256` was synchronized to the current local binary; the raw PDF itself was not modified.

## Scope and Reading Depth

- Completed reading_depth: `deep-read` for the supplied main PRL and its supplied Supplemental Material.
- Covered scope: complete main PRL, level scheme, ADO/polarization, mixing-ratio logic, DSAM lifetimes, absolute transition-probability figures, PRM interpretation, and Supplement pp.1–3 including Table I, gated spectra and upper-limit rows.
- Not covered: raw event matrices, detector-response files, PRM source code and the cited independent spectroscopy sources.
- Coverage caveats: the supplement closes the local numerical-table gap, but it does not remove the parent paper's configuration, branch-choice or model-dependence boundaries.
- HS-126 alternate PDF audit: the seven-page APS PDF differs from the canonical copy only in minor typesetting/reference-line text; title, DOI, figures, tables, equations and claims agree. It is attached evidence for this PRL, not a second experiment.

## Paper Question and Scientific Motivation

- Author-explicit motivation: test whether chirality and wobbling can coexist in bands assigned the same odd-odd configuration, forming a “chiral wobbler” (PDF pp.1-2).

## Method and Design Logic

- Combine three-band spectroscopy, ADO/polarization, DSAM lifetimes and absolute strengths; compare B1/B2 chiral fingerprints and B1/B3 wobbling fingerprints with PRM angular-momentum geometry (PDF pp.2-5, Figs.1-7, Table I).

## Key Evidence and Reasoning Chain

- Similar B1/B2 energies/strengths plus M1 interlinks → chiral-partner interpretation; increasingly E2 B1-B3 links → wobbling interpretation; same-configuration assignment and PRM mapping → coexistence claim. The supplied supplement closes the transition-table gap; configuration and PRM dependence remain.

## Summary

The paper proposes `74Br` bands B1/B2 as chiral partners and B3 as a one-phonon wobbling excitation built on B1, coining an experimental “chiral wobbler” candidate. The supplied supplement now makes the transition-level table and upper limits locally auditable. The conclusion remains evidence/interpretation supported by multiple observables and PRM, not a model-independent proof of coexistence.

## Experimental or Theoretical Setup

`58Ni(19F,2p1n)74Br`; AFRODITE with eight Compton-suppressed clovers (five at 90°, three at 135°), about `3.5×10^9` γ-γ events. A thick backed target stopped recoils for DSAM lifetime extraction with modified LINESHAPE and five-step side feeding.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GU24-1 | Three `ΔI=1` bands assigned the same `πg9/2⊗νg9/2` configuration were extended and interconnected. | experimental-fact | direct | PDF pp.2-3, Figs.1-2 | true |
| GU24-2 | Spin/parity and E2/M1 mixing were constrained by ADO ratios and linear polarization. | experimental-criterion | direct | PDF pp.2-3, Fig.3; Supplement Table I, pp.1-2 | true |
| GU24-3 | Level lifetimes were measured by DSAM and agree with earlier measurements within uncertainties. | experimental-fact | direct | PDF pp.2-4, Fig.4, Table I | true |
| GU24-4 | B1/B2 satisfy the authors' chiral-doublet fingerprint set, including similar energies/staggering/alignment/in-band strengths and M1-dominated interband links. | author-interpretation | indirect | PDF pp.3-4, Figs.5-6 | true |
| GU24-5 | B1-B3 E2 fractions rise with spin and reach about 90% at high spin; B3 is interpreted as one-phonon wobbling. | experimental-fact | direct | PDF p.4, Fig.6; Supplement Table I, pp.1-2 | true |
| GU24-6 | PRM angular-momentum components support chiral B1/B2 and wobbling B1/B3 pictures. | model-result | direct | PDF pp.4-5, Figs.6-7 | true |
| GU24-7 | Authors conclude evidence for coexistence of chirality and wobbling with the same configuration, notated as a chiral wobbler. | author-interpretation | indirect | PDF p.5, Summary | true |

## Nuclear Structure Information

B1/B2/B3 are interconnected ΔI=1 bands assigned πg9/2⊗νg9/2. Lifetimes and relative/absolute strengths provide unusually broad observables; the supplied supplement makes the transition table locally auditable.

## Authors' Interpretation

The authors conclude evidence for a same-configuration coexistence of chirality and wobbling, not a model-independent proof.

## Model Results

PRM angular-momentum components reproduce the proposed chiral and wobbling geometries. The mapping depends on common configuration and fitted deformation/coupling assumptions.

## Competing Interpretations and Limitations

The same-configuration inference uses linking patterns, similar strengths and PRM. Chiral/wobbling fingerprints are not individually sufficient; configuration assignment and PRM dependence remain. Future thin-target and `g`-factor measurements are explicitly proposed.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| GU24-AR-1 | Core reconstruction | The three-band comparison, lifetimes and strengths are unusually rich; the supplement closes the table gap, while same-configuration coexistence still depends on configuration and PRM mapping. | Key Results and Competing Interpretations above | unreviewed |
| GU24-AR-2 | Assumptions and dependencies | The adopted band identities, mixing-ratio branches, configuration assignments, and model inputs are valid within the stated measured range. | Method/results/model sections cited above | unreviewed |
| GU24-AR-3 | Transfer conditions | Transfer only the measured observables and their explicit conditions; do not transfer the author interpretation without equivalent link and configuration evidence. | Source scope and claim locators above | unreviewed |
| GU24-AR-4 | Failure conditions | Alternative branch, band identity, configuration, or model dependence can weaken the structural label even when the measured transitions remain valid. | Competing Interpretations and Limitations above | unreviewed |
| GU24-AR-5 | Reverse/falsification test | Obtain independent lifetimes/multipolarities or common-input competing-model tests targeted to the stated evidence gap. | Follow-up observables identified by the source/Agent | unreviewed |
| GU24-AR-6 | Research-question decision | Retain the source in the project/synthesis evidence map with the source-local review boundary explicit. | Whole-source assessment | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: The Wiki already contained the broader wobbling topic and related candidate map, but not this source in a complete source-local evidence and review structure.
- Effect of this source: supports
- Reason: The three-band comparison, lifetimes and strengths are unusually rich; the supplement closes the table gap, while same-configuration coexistence still depends on configuration and PRM mapping.
- Persistence decision: project update / synthesis update
- Review state: page-level `human-reviewed` within the main-paper-only scope; Key Results claims remain `needs_review: true` for future claim-specific paper use.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[nuclear-chirality-and-multiple-chiral-doublet-bands]] | New same-configuration coexistence candidate outside existing `78Br/133Ce` cases. |
| supports | [[wobbling-motion]] | Lifetime/ADO/polarization-supported one-phonon candidate in an odd-odd nucleus. |
| limits | [[chiral-doublet-bands]] | Fingerprint conjunction still requires configuration and model review. |

## Human Review Triage

Review disposition: the user completed a rough page-level review on 2026-07-25 and accepted the current main-paper evidence boundary without correction. The P0/P1 items remain future strict paper-use verification prompts; the supplied supplement is audited, while raw matrices, detector response and PRM inputs remain unavailable.

### P0

- `GU24-2`/`GU24-5`, Fig.3/Fig.6 and Supplement Table I — Evidence: the supplied supplement gives the per-transition ADO/polarization/mixing and E2-fraction rows; exact values are now locally auditable, while interpretation still depends on branch and model assumptions. Agent self-audit: table-level coverage closed, claim-level paper gate remains open. Risk: numerical rows may be detached from the stated gates or uncertainty conventions.

### P1

- `GU24-1`/`GU24-4`/`GU24-7`, Figs.5-7 — Evidence: linking/strength similarities and PRM support same configuration and dual chiral/wobbling mapping. Agent inference: coexistence depends on configuration identity and model geometry. User check: configuration evidence and PRM parameter mapping. Risk: fingerprint conjunction may be overstated as model-independent proof.
- `GU24-3`, Fig.4/Table I — Review DSAM side-feeding assumptions and lifetime uncertainties before using absolute strengths quantitatively.

### P2/P3

- P2: exact level/transition transcription after the supplement is obtained. P3: metadata/navigation.

## Human Review Record

- 2026-07-25: the user completed a rough review of the main-paper source page and accepted its claims and attribution boundaries.

## Supplementary-material audit (2026-09-20)

- The supplied three-page supplement was read end-to-end. Table I provides transition energies/intensities, `R_ADO`, polarization `P`, mixing ratios `δ`, and `B(M1)/B(E2)`-related quantities for Bands 1–3; the spectra/gate panels and upper-limit E2 rows were checked against the surrounding text.
- This is attached evidence for the same PRL experiment, not a second experiment or independent source. It closes the transition-table coverage gap but preserves `needs_review` for claims whose interpretation requires the parent PRL's configuration assignment and PRM.

## Alternate-version audit (HS-126, 2026-09-21)

- The supplied `2024_H. Amro et al_...pdf` was compared with the canonical PRL copy. The DOI/title/author list, partial level scheme, ADO/polarization/lifetime analysis, PRM parameters and conclusion reconcile.
- Only presentation-level differences were found: text line wrapping and minor reference grammar (`parameter`/`parameters`, `Ref.`/`Refs.` and `et al.` placement). No numerical, equation, figure or interpretation change was identified.
- HS-126 remains `reused-and-audited-existing-source`; no new source or independent experiment count is added.

## Review Status

Page-level review is complete for this ingest round. `reading_depth: deep-read`; claim-level `needs_review` and Analytical Reconstruction review markers remain because the supplement is now read but this remains Codex self-audit, not human claim-by-claim paper certification.

## Extracted Pages

- Nuclei: [[74br]]
- Concepts: [[nuclear-chirality]], [[wobbling-motion]]
- Methods: [[angular-distribution]], [[linear-polarization-asymmetry]]

## Non-source Notes and Follow-up

For paper use, recheck any quoted Table-I number against the stated gate, uncertainty and branch convention; do not clear the model-dependent coexistence interpretation solely because the supplement is available.

## Day18定量审计：三带DSAM寿命测定与手征-wobbling电磁多极分立基准

**checkpoint048更正：旧GU24-D18-1的寿命列错位、绝对二分律及跨核判决部分已superseded。** 下列旧行原文保留作审计历史；7+的1.79 ps归Band 3而非Band 2，且补表不支持B2→B1所有线E2<10%或B3→B1所有线严格E2主导。校正输入与源内解释范围由GU24-D18-2–9承接，原GU24-1–7及review/flags不变。

在Day18正式学习中对本文Table I中74Br三条带（Band 1-3）在束DSAM寿命测量及其导出的绝对B(E2)与B(M1)多极性质进行定量审计，raw SHA256 `1783B784C3843E15DE39406182613757F9C3B928A2791E45A7D650F117EA4333`已核。原GU24-1–7各claim及`human-reviewed`状态完全保留；新GU24-D18-1待审。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GU24-D18-1 | 本文Table I通过AFRODITE反冲完全阻停DSAM测量，直接给出了74Br三条同组态pi(g9/2) x nu(g9/2)带的绝对能级寿命：Band 1为1.32至0.08 ps，Band 2为1.79至0.10 ps，Band 3为1.21至0.38 ps。定量对比确立了核物理中手征与wobbling共存时的电磁多极二分律黄金基准：(1) 手征伙伴带（Band 2向Band 1）的跨带连接线严格由M1主导（E2份额<10%），且带内与跨带B(M1)呈现清晰的反相奇偶交错；(2) wobbling声子带（Band 3向Band 1）的跨带连接线则严格由四极E2主导，其E2份额随自旋递增并达到约90%，且B(M1)呈现与Band 1反相的交错。这在同一原子核内直接以绝对寿命与跃迁几率证实：手征性以M1为主导，wobbling以E2为主导，二者多极性完全对立。此实验判据直接证明其他所谓‘偶偶核wobbling’（如130Ba中74% M1主导衰变）实质上属于手征/特征伙伴带物理范畴。 | task-rate-decomposition-audit | derived-and-boundary | PDF pp.2-4 Table I, Figs. 4-6；新guo24-74br-dsam-result-031 | true |

旧[分析合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/guo24-74br-dsam-contract-031.json)及[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/guo24-74br-dsam-result-031.json)保留用于追踪历史输入；脚本将Band 3的7+寿命误放Band 2，且参考卷页误写为PRL 133,082501（实际132,092501）。其中固定`checks_passed: true`不是DSAM拟合、强度复算或相位检验，本次未运行会覆盖旧输出的脚本。

## Day18 checkpoint048更正：74Br寿命列、逐线多极性与同数据解释边界

本次回读7页主文与3页SI全文，视觉核对主文p.4 Table I、p.5 Fig.6及SI pp.1–3；主文SHA256 `1783B784C3843E15DE39406182613757F9C3B928A2791E45A7D650F117EA4333`、SI SHA256 `1eb2c1af4ff7d1bf6460c154baabacb80e3ca7e63fa1832ca1d1b3d58b5ea9a0`一致。未取得实际DSAM/ADO/P producer、完整Cov或PRM作业，未拟合新的相位显著性/模式CI。新增行是Codex定向self-audit，保留`needs_review: true`，不改变原human-review范围。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GU24-D18-2 | 主文Table I本工作有限寿命（ps）按列为：B1的10+–15+依次1.32(13)、0.42(4)、0.19(3)、0.21(2)、0.14(3)、0.08(1)；B2的8+–12+依次0.62(6)、0.53(11)、0.43(4)、0.25(3)、0.10(+0.06/−0.03)；B3的7+–10+依次1.79(+0.14/−0.13)、1.21(18)、1.10(+0.24/−0.18)、0.38(+0.10/−0.09)。7+的1.79 ps明确位于Band 3列。 | observed-fact | direct | 主文PDF p.4 Table I视觉列核对 | true |
| GU24-D18-3 | 同表另给B1的16+、17+寿命<0.06、<0.23 ps，B2的13+、14+为<0.56、<0.29 ps，B3的11+为<0.60 ps；打印表未说明这些限的CL。B1低自旋6+–9+列为既有寿命，SI以星号标出使用旧寿命的强度；不能把全部强度当作此次新测。DSAM依赖下方门、阻停输入、五态侧馈/顶馈级联及背景/污染线拟合，完全阻停靶不使寿命成为无响应依赖的读数。 | experimental-method-and-boundary | direct-and-boundary | 主文PDF p.2 DSAM方法；p.4 Table I；SI p.1 Table I caption | true |
| GU24-D18-4 | SI中B2→B1的已测ΔI=1线为527.2（8+→7+）、661.2（9+→8+）、959.5（10+→9+）、1239.5 keV（12+→11+），δ依次−0.63(+0.08/−0.10)、+0.22(+0.09/−0.08)、−0.7(+0.1/−0.2)、−0.08(+0.05/−0.06)。中央f(E2)=δ²/(1+δ²)约28.4%、4.62%、32.9%、0.636%，支持这些线M1占优，但直接否定“全部E2<10%”；956.9线未列δ，799.6/818.0是ΔI=2 E2线，须分别对待。 | observed-and-conditional-fraction | direct-and-derived | SI p.2 Table I，Band 2→Band 1部分 | true |
| GU24-D18-5 | SI中B3→B1向低自旋的ΔI=1线600.3（6+→5+）、815.3（8+→7+）、1155.6（9+→8+）、1266.8 keV（10+→9+）δ为−0.5(1)、−1.1(+0.3/−0.4)、3.1(+1.8/−0.9)、8(+3/−2)，中央E2份额约20.0%、54.8%、90.6%、98.5%。这支持随自旋升高的趋势，不能称所有B3连接线严格E2主导；773.2 keV仅有强度上限，另有ΔI=0及向较高终态自旋的连接线。 | observed-and-conditional-fraction | direct-and-derived | SI p.2 Table I；主文p.3讨论与p.5 Fig.6(f) | true |
| GU24-D18-6 | SI给出逐线绝对强度，例如B2→B1的527.2 keV为B(M1)=0.24(3) mu_N²、B(E2)=0.5(1) e²b²，B3→B1的1155.6 keV为约0.0003(+0.0002/−0.0003) mu_N²与0.0032(+0.0010/−0.0009) e²b²。辐射多极份额不是绝对集体强度；这些B值由寿命、分支/相对强度与δ等组合导出，SI强度以383 keV=100归一，并非直接的绝对分支概率。 | derived-strength-input-contract | direct-and-boundary | SI pp.1–2 Table I及caption；主文pp.2–4测量链 | true |
| GU24-D18-7 | 作者以B1/B2带内及带间B(M1)的反相奇偶交错、B3带内与B1不同的交错相位作为组合指纹的一部分；本文/旧脚本未提供含完整Cov的相位拟合或统计显著性。同母态带内/带外强度共享寿命与分支归一，ADO/P、相对强度、寿命及派生B均来自同一AFRODITE采集，SI也不是独立实验，不能将这些派生量计成相互独立的重复验证。 | author-interpretation-and-lineage | direct-and-boundary | 主文p.3交错讨论；p.5 Fig.6(d)–(f)；SI Table I | true |
| GU24-D18-8 | 作者结合多个谱学/电磁指纹与采用给定形变、拟合惯量的PRM角动量几何，提出B1/B2手征伙伴和B3一声子wobbling的同核共存解释。这没有建立“所有手征衰变必M1、所有wobbling衰变必E2”的普适二分律，也不能由74Br数据直接改判130Ba或其它核为手征/特征伙伴/TiP。 | author-interpretation-and-scope | direct-and-boundary | 主文pp.3–5，Figs.5–7及Summary | true |
| GU24-D18-9 | SI门谱在可能B2→B1的ΔI=2连接能量1307、1443、1648 keV处给出相对Iγ<0.25、<0.6、<1.0，对应B(E2)<0.00025、<0.0011、<0.0047 e²b²；门为483、429、1244 keV。它们是在给定灵敏度/门条件下的打印上限，不是严格零；SI未给CL或可恢复的完整限构造producer，不能补写1σ排除或通用选择定则。 | observed-limit-and-boundary | direct-and-boundary | SI p.3 Fig.1及caption | true |
| GU24-D22-001 | 74Br“手征摆子”候选证据边界审计：(1) 声称E2主导的高自旋连线（1155.6与1266.8 keV）线偏振显著性仅0.31σ与0.35σ（P=-0.11(36)与-0.07(20)），实验完全无法排除M1小模解；(2) 实测带间B(E2)在1155.6 keV仅1.75 W.u.（0.0032 e²b²）、1266.8 keV仅9.3 W.u.，未达到集体增强阈值（>=20-30 W.u.）；(3) 低自旋连线600.3 keV呈80% M1支配；(4) 同为g9/2粒子性几何弱化正交手征构型。 | chiral-wobbler-evidence-boundary | direct-and-derived | PRL 132, 092501; Supplement Table I; br74-chiral-wobbler-audit-result-069.json | true |


## Day22 checkpoint091 直接原件纠错

本次定向核首页核素身份/实验方法，未据此认证旧069所有数值。χ错误属于本任务自设输入审计，非作者结果。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GU24-D22-R091-1 | 首页明确核素为74Br，Z=35、N=39；不是N=Z=35。作者报告三条πg9/2⊗νg9/2带的角分布、偏振和DSAM寿命，并结合PRM提出共存解释。仅凭粒子标签不能推导其实际三矢量必共面；旧χ=.027使用自设倾角，不是本篇测量或波函数输出。 | identity-and-geometric-inference-boundary | direct-original | 092501-1, Abstract and experimental setup; comparison with task artifact chiral-aplanarity-pn-coupling-result-078.json | true |


## 2026 theoretical follow-up and Day27 bounded replay

[[qureshie-2026-chiral-wobbling-four-band-74br]] uses this experimental B1-B3 network and predicts B4; it adds a model extension, not independent experimental replication. [[74br-four-band-branching-network-readiness]] replays Supplement Table I's 8+,9+,10+ B3 branches with lifetime cancellation, preserving the printed-input and missing-covariance boundary. This addition does not change the earlier human-review scope or clear existing claim-level review flags.
