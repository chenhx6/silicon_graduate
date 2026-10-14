---
type: source
title: "Herzáň et al. 2015 - Detailed spectroscopy of 193Bi"
aliases: [Herzan 2015 193Bi spectroscopy]
created: 2026-09-21
updated: 2026-10-14
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Detailed spectroscopy of 193Bi"
authors: [A. Herzáň, S. Juutinen, K. Auranen, T. Grahn, P. T. Greenlees, K. Hauschild, U. Jakobsson, P. Jones, R. Julin, S. Ketelhut, M. Leino, A. Lopez-Martens, P. Nieminen, M. Nyman, P. Peura, P. Rahkila, S. Rinta-Antila, P. Ruotsalainen, M. Sandzelius, J. Sarén, C. Scholey, J. Sorri, J. Uusitalo]
journal: "Physical Review C"
year: 2015
volume: 92
pages: "044310"
doi: "10.1103/PhysRevC.92.044310"
citation_key: Herz__2015
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "https://doi.org/10.1103/PhysRevC.92.044310"
library_file: "raw/papers/gpt/high-spin-20260920/纲图/2015_Herzáň et al_Detailed spectroscopy of Bi 193.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/纲图/2015_Herzáň et al_Detailed spectroscopy of Bi 193.pdf"
raw_sha256: "f727485ad0f52269a66b27272dac75d34d9e67aaf8b073631cfeac5fe81d3aea"
nuclei: [193Bi, 192Pb, 191Bi, 193Tl]
reactions: [165Ho-32S-4n]
experiments: [JYFL, JUROGAM-II, RITU, GREAT]
models: [Nilsson, oblate-configuration-coupling, superdeformation, shears-like-interpretation]
observables: [level-scheme, RDCO, IPDCO, isomer-half-life, E2, M1, alpha-decay]
methods: [gamma-gamma-coincidence, recoil-decay-tagging, isomer-tagging, linear-polarization-asymmetry]
tags: [193Bi, high-spin, isomer, superdeformation, shape-coexistence]
---

# Detailed spectroscopy of `193Bi`

## Bibliographic Record

- A. Herzáň *et al.*, *Phys. Rev. C* **92**, 044310 (2015), DOI `10.1103/PhysRevC.92.044310`.

## Scope and Reading Depth

- The 20-page article was read end-to-end: reaction/detector setup, RDT and isomer tagging, Tables I–II, Figs.1–18, all band/group discussions, high-spin isomers, spherical/oblate interpretation, superdeformed band, systematics and conclusion.

## Experimental Evidence

`193Bi` was produced in `165Ho(32S,4n)` at 152 MeV with JUROGAM II, RITU and GREAT. Prompt γ rays were analyzed with recoil-gated matrices/cubes; delayed γ rays and conversion electrons were recorded at the focal plane (PDF pp.1–3). DCO ratios used 157.6°/75.5° matrices; IPDCO used single-crystal versus same-clover two-crystal events, with the measured clover sensitivity fitted as `Q(Eγ)=Qpoint(0.42(4)−1.9(7)×10−4 Eγ)` (pp.2, 9–10, Eq./Fig.4).

The level scheme extends Band 1 (`πi13/2`) to `45/2+`, Band 2 to `29/2−`, and identifies new Bands 3–4 and groups D/F. DCO/IPDCO and coincidence/energy-sum evidence assign M1/E2 characters where statistics permit; weak Group D/F links retain uncertain assignments (pp.9–12, Table I, Fig.2).

## Isomers and Shape Interpretation

The known `(29/2−)` isomer has `T1/2=3.02(8) μs`; a `49 keV` transition is observed in delayed γ–electron coincidence and has a conversion coefficient consistent with E2, placing the isomer at about `2405 keV` (pp.12–15, Figs.6–9). A new `29/2+` isomer at `2350 keV` has `T1/2=85(3) μs` and decays through an `84 keV` E2 transition with `B(E2)=1.6(1)×10−3 W.u.`; the authors associate it with the three-quasiparticle `π(h9/2² i13/2)` configuration, interpreted as an i13/2 proton coupled to the oblate8+ proton-pair state in192Pb (PDF pp.18–19, Sec.IV.B and conclusion). This is an author interpretation, separate from the measured decay.

Band 3 resembles a low-energy M1 sequence but receives E2 links and is extended to `(37/2−)`; the authors do not promote it to a universal shears assignment. A superdeformed band based on the favored `1/2[651]` proton orbital is nearly identical in transition energies to the SD band in `191Bi` and `193Tl`, but absolute transition probabilities are still needed to confirm SD character (pp.11, 18–19, Fig.18).

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HE15-1 | The `193Bi` level scheme is extended with new bands and DCO/IPDCO-supported multipolarities. | experiment-result | direct | PDF pp.2–3, 9–12, Table I | true |
| HE15-2 | `29/2−` and `29/2+` isomer energies/half-lives and E2 decays are established by delayed γ/e− tagging. | isomer-result | direct | PDF pp.12–18, Figs.6–9 | true |
| HE15-3 | The `1/2[651]` SD band is a candidate until absolute transition probabilities are measured. | shape-boundary | mixed | PDF pp.18–19, Fig.18 | true |
| HE15-4 | Band1 Table I reports 299.2(1),323.4(1),622.4(1) keV connecting the rounded 1228 (17/2+),929 (15/2+),605 (13/2+) levels in Fig.2. Their Rexp values are 0.68(2),0.74(4),1.30(16); ΔIPDCO values −0.032(1),−0.012(1),+0.086(10); authors list M1,M1,E2. Rexp uses efficiency-corrected intensities at157.6°/75.5° with the same gate on all-angles projections. Table I also asks for about0.3-keV statistical error in addition to listed fitting errors. | experimental-fact | direct | PDF p.3, Table I; PDF p.8, Fig.2; PDF p.2 ratio definition | true |
| HE15-5 | Fig.5(a), gated on the154-keV transition, describes the peak labeled323 keV as a quadruplet of315,320,323,327-keV transitions. Fig.5(b) is gated on323.4 keV and shows feeding into Band1. Table I also places299.8(1) keV higher in Band1 (41/2+→39/2+), distinct from299.2(1) (17/2+→15/2+). | experimental-fact | direct | PDF p.10, Fig.5 caption; PDF p.3, Table I | true |
| HE15-6 | The SD Table II retains an unknown bandhead energy X and parenthesized spin/parity assignments. A weak1836(5)-keV candidate is seen in coincidence with168.3 and331.7 keV; authors require more statistics to confirm it as a link to Band6. It cannot fix X as a confirmed absolute level in the present evidence. | experimental-fact | direct | PDF p.15, Table II; Fig.13; Sec.III.B | true |
| HE15-7 | The authors do not observe the expected low-energy SD transitions near87 and46 keV. They discuss overlap with the87.4-keV Bi x ray and large E2 conversion coefficients as reasons the γ rays could be very difficult to observe; the assumed intensity flow through these lines remains an interpretation. | author-interpretation | direct | PDF p.19, Sec.IV.D | true |
| HE15-8 | Band1 Table I adds 327.4(1) keV, 19/2+→17/2+, Iγ=196(6), Rexp=0.68(2), ΔIPDCO=−0.004(1); 626.2(1) keV, 19/2+→15/2+, Iγ=102(4), Rexp=1.48(6), ΔIPDCO=+0.094(9); and 646.9(1) keV, 21/2+→17/2+, Iγ=108(4), Rexp=1.47(6), ΔIPDCO=+0.091(4). The 319.8(1) keV 21/2+→19/2+ row is under Other transitions on p.7: Iγ=125(4), Rexp=0.60(2), ΔIPDCO=−0.039(2), listed M1. Figure2 rounds these levels to605,929,1228,1556,1875 keV. | experimental-fact | direct | PDF p.3, Table I; PDF p.7, Table I continuation; PDF p.8, Fig.2 | true |
| HE15-9 | Table I footnote f explicitly says the DCO/IPDCO value applies to both 393.4(1) and394.0(1) keV transitions and their order is unclear because their energies are too close in the coincidence spectrum. The displayed Rexp is1.26(16), and the displayed ΔIPDCO is−0.076(11); parenthesized spins and (E2) labels remain tentative. These are shared doublet quantities, not two independent line-resolved polarization measurements. | experimental-fact | direct | PDF p.7, Table I footnote f | true |
| HE15-10 | Figure3 fits a(Eγ)=a0+a1Eγ with a0=1.113(7), a1=−5.4(8)×10−5 per keV; p.7 defines a=Nparallel(unpolarized)/Nperpendicular(unpolarized), measured with152Eu. Figure4 uses A=Q P and Q=Qpoint(p0+p1Eγ), p0=0.42(4), p1=−1.9(7)×10−4 per keV. The paper does not provide a joint calibration covariance for these parameters. | experimental-method | direct | PDF p.10, Fig.3; PDF p.10, Fig.4; PDF p.7, normalization definition | true |
| HE15-11 | The85(3)-μs isomer is placed at2350 keV using the84-keV decay and parallel prompt paths614.0 keV and158.5+609.1 keV. The authors explicitly condition its29/2+ assignment on the correctness of Band1. Conversion analysis reports αK=0.133(19) for436 keV and0.032(6) for455 keV, and jointly assigns455/137-keV E2 character; the84-keV E2 character follows the level assignment. | experimental-assignment | mixed | PDF p.13, Sec.III.A.5; PDF p.14, conversion analysis | true |
| HE15-12 | Band1's13/2+ bandhead half-life153(10) ns is cited from Nieminen et al., Ref.[7], not measured anew for the seven higher prompt lines selected here. Table I uses the323.4-keV line as normalization and prints1000(57), with299.2 at258(8) and622.4 at121(5). These are relative intensities, not absolute photon probabilities. | experimental-fact | direct | PDF p.10, Sec.III.A.1; PDF p.3, Table I | true |
| HE15-13 | For the unobserved low-energy SD candidates, the authors quote αtot=261(4) at46 keV and12.82(18) at87 keV for E2 from Ref.[41]. Their assumed intensity flow,3/2+ or1/2+ endpoint, and calculated SD minimum near2.4 MeV remain interpretation/model, separate from the observed13-transition sequence and the unconfirmed1836-keV link. | author-interpretation | mixed | PDF p.19, Sec.IV.D | true |
| HE15-14 | The authors propose the three-quasiparticle π(i13/2 h9/2²) configuration for the29/2+ isomer and describe the most likely scenario as an i13/2 proton coupled to the oblate8+ proton-pair state in192Pb. This is a configuration interpretation, not a direct observation of three orbitals; the earlier Wiki summary's missing square on h9/2 is corrected. | author-interpretation | direct | PDF p.18, Sec.IV.B; PDF p.19, conclusion | true |
| HE15-15 | Table I lists352.3(1)keV at1610keV as(13/2−)→(11/2−), M1, Rexp=0.73(16), ΔIPDCO=−0.023(7). Figure2 continued instead labels the1610-keV state15/2− above an11/2− level. The displayed spin difference would be2, not1; the source contains a figure/table assignment discrepancy that must not be silently resolved from the M1 label. | experimental-assignment-boundary | direct | PDF p.7, Table I Other transitions; PDF p.9, Figure2 continued | true |

## Summary

Herzáň *et al.* provide a dense high-spin/isomer spectroscopy reference in the transitional Bi region, with a clear separation between level facts, multipolarity assignments and shape/configuration interpretations.

## Competing Interpretations and Limitations

- Weak groups have incomplete DCO/IPDCO coverage and retain uncertain assignments.
- SD transition-energy similarity is not a direct deformation measurement without absolute strengths.

## Analytical Reconstruction and Self-Audit

| ID | Audit item | Agent judgment | Locator | Status |
|---|---|---|---|---|
| HE15-AR-1 | Assignment chain | Coincidences + RDCO + IPDCO + isomer tagging support the principal band multipolarities; weak groups retain explicit uncertainty. | PDF pp.2–3, 9–12, Table I | self-checking |
| HE15-AR-2 | Isomer identity | Half-lives, delayed γ/e− coincidence and E2 conversion provide a stronger identity chain than systematics alone; configuration remains an interpretation. | PDF pp.12–18, Figs.6–9, 17 | self-checking |
| HE15-AR-3 | SD boundary | Energy-pattern similarity is a candidate SD signature; without absolute transition probabilities it is not direct deformation proof. | PDF pp.18–19, Fig.18 | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` high-spin isomer/shape-coexistence evidence and [[linear-polarization-asymmetry]], [[signature-partner-bands]] and [[band-termination]] method comparisons; it broadens the A≈190 control region beyond the A≈130 focus.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `HE15-P0-1`: Preserve the setup-specific IPDCO calibration and the distinction between confirmed level/isomer evidence and configuration/SD interpretations.

## Extracted Pages

- Nucleus/methods: `193Bi`, [[linear-polarization-asymmetry]], [[gamma-gamma-coincidence]]。

## Selected transition and gate self-audit

原始PDF哈希复核一致；重点原图核验Table I(p.3)、Figure2(p.8)和Figure5(p.10)，并回读reaction/tagging(p.1–2)、Band1和isomer/SD主线(p.10–15)、configuration/SD解释与结论(p.16–20)的对应段落。本次预习不替代正式周考，也不改变原阅读/审核状态。[[level-scheme-reconstruction]] 固化三层子图、energy closure/covariance练习与复合峰/互斥branch控制；[[doppler-correction]] 使用HE15-5作独立的多线峰反例。

299.2+323.4−622.4=0.2keV是本任务算术，不是作者单独报告的closure test。TableI/Fig.2/Fig.5共享同次实验；relative intensities、DCO/IPDCO与coincidences不能重复计成独立实验。HE15-4/5/6保持needs_review=true。

## Day14 正式逐边复核与来源边界

本次正式周考在保存标明 priming 的来源前回忆后，回读全文主线：动机与反应/阵列/标记（pp.1–2），全部 Table I 及表注（pp.3–7），Figure2 的两页纲图（pp.8–9），角度/偏振标定与门谱（p.10），各带、isomer 和 SD 的结果（pp.11–15），组态/形状讨论、systematics、结论与引用身份（pp.16–20）。视觉重点核 p.3 Table I、p.7 表尾与 footnote f、p.8 Figure2、p.10 Figures3–5、p.15 Table II/Figure13。Crossref 结构化元数据与本地 PDF 的作者、题名、年、卷和 DOI 一致；Crossref 回应未给文章页号，044310 来自 PDF 页眉，不用空字段反向改写页号。

新增 HE15-8–14 只固化直接读到的行、表注、标定和条件性赋值，不清除任何既有 `needs_review`。七条 prompt 边、共享双线量和不定 X 的方法后果，见 [[level-scheme-reconstruction]] 的“Day14 五能级七跃迁逐边审计”和“能量图的闭合、标定与拓扑边界”。算术、GLS 和标定反事实均属于本任务 L2 练习，不能称为作者重新报告的能级或独立复测。

### Agent self-audit triage — Day14

- P0（科学边界，已 self-audit）：HE15-9 的 shared-doublet DCO/IPDCO 不能分配成两条已独立测量的电磁性质；保留未定顺序和括号赋值。HE15-6/7/13 的 SD、未知 X 和缺失弱线不能从模型或强内转换假设升格为确定绝对能级。技术 hard P0 未发现。
- P1（已 self-audit）：HE15-8 的319.8-keV行确在 Other transitions；HE15-10 的 Eγ 单位是keV，a(Eγ)与Q(Eγ)不同；HE15-11 的29/2+赋值明确依赖Band1，HE15-12 的153-ns bandhead寿命不是七条边的母态寿命。原始逐门/逐角计数、calibration covariance、逐母态寿命/δ仍不可由本文补造。
- P2：source→方法与方法→source 已互链，raw哈希一致。P3：本轮不是人类审核事件，原有 review_status 保持 unreviewed。

### Ref7 原始寿命来源的可得性边界

Ref7为Nieminen et al., “γ-ray spectroscopy of191,193Bi”, PRC69,064326(2004), DOI10.1103/PhysRevC.69.064326；Crossref身份已核。正文经有限公开来源路线仍未取得，故HE15-12的153(10)-ns只能按本篇引用记录，不追加原实验的寿命提取方法、完整branch或与2015的event-level独立性。作者重合/发表年份不同都不能替代acquisition指纹；metadata来源、数据库评估或重新引用也不增加一条新实验。当前边界不是断言此文永久不可得，后续有primary PDF或run provenance时再定向复核。

### NNDC comparison：独立处理与共享实验

[[nndc-2017-193bi-level-scheme-evaluation]] N193-2/3/4采用本篇2015He27的Eγ/RI，进行level least-squares与quadrature处理；它支持source-to-evaluation crosswalk，但不是新独立采集。N193-5在393/394保留Q并明确negativePOL与placement-implied(E2)矛盾；N193-6对352.3保留无multipolarity赋值。本页保留作者原Table I标签与HE15-9/15的不确定性，不将Q强行覆盖为E2，也不凭数据库选择352.3的最终spin。

N193-8记录compiler摘要From604.7γ(t)/2004Ni06及flight/intensity说明；这是公开评价的引用依赖，不替代Ni04原文方法核验。N193-7的BrIcc CC是有multipolarity前提的计算，未提供七条higher-parent τ、δ或unseenbranch闭合。全篇主线回读不等于认证所有弱线assignment，新的具体冲突已列P0科学边界且needs_review保留。
