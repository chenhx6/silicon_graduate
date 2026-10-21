---
type: source
title: "General properties of the πh9/2[541]1/2− configuration and level scheme of 165Tm"
aliases: ["Jensen 2001 165Tm", "NPA695 Jensen 165Tm", "HS-006 HS-007 canonical duplicate group"]
created: 2026-09-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: experiment
reading_depth: deep-read
title_original: "General properties of the πh9/2[541]1/2− configuration and level scheme of 165Tm"
authors: ["H. J. Jensen", "R. A. Bark", "P. O. Tjøm", "G. B. Hagemann", "I. G. Bearden", "H. Carlsson", "S. Leoni", "T. Lönnroth", "W. Reviol", "L. L. Riedinger", "H. Schnack-Petersen", "T. Shizuma", "X. Z. Wang", "J. Wrzesinski"]
journal: "Nuclear Physics A"
year: 2001
volume: 695
issue: "1-4"
pages: "3-50"
doi: "10.1016/S0375-9474(01)01111-3"
citation_key: Jensen_2001
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
language: en
canonical_source: "Jensen, H. J. et al. General properties of the πh9/2[541]1/2− configuration and level scheme of 165Tm. Nucl. Phys. A 695, 3-50 (2001)."
library_file: "raw/papers/gpt/high-spin-20260920/NPA695-Jensen-2001-3.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/NPA695-Jensen-2001-3.pdf"
raw_sha256: "0fde4a838d94fdc23dcd4d4034a945073cb569c47c153e9e3b90676c44838770"
duplicate_ids: ["HS-006", "HS-007"]
nuclei: ["165Tm", "164Tm", "164Er", "166Yb"]
reactions: ["150Nd(19F,4n)165Tm", "154Sm(15N,4n)165Tm"]
experiments: ["nordball-165tm-f19-85mev", "nordball-165tm-n15-70mev"]
models: ["cranked-shell-model", "cranked-nilsson-strutinsky-model", "potential-energy-surface", "two-band-mixing"]
observables: ["level-scheme", "dco-ratio", "mixing-ratio", "transition-quadrupole-moment", "lifetime", "alignment", "crossing-frequency", "B(M1)/B(E2)", "B(E1)/B(E2)"]
methods: ["gamma-gamma-coincidence", "dco-ratio", "doppler-shift-attenuation-method", "band-mixing"]
tags: [165Tm, h9-2, delayed-alignment, i13-2-alignment, gamma-vibration, DSAM, quadrupole-moment, rare-earth]
---

# General properties of the πh9/2[541]1/2− configuration and level scheme of 165Tm

## Bibliographic Record

- 作者：H. J. Jensen 等；*Nuclear Physics A* 695(1-4), 3-50 (2001)。DOI：`10.1016/S0375-9474(01)01111-3`。
- 规范来源：HS-006 `NPA695-Jensen-2001-3.pdf`。HS-007 是同一 SHA-256 的第二个外部路径副本，已完成逐条 duplicate audit，不重新摄入。
- 规范 raw 文件：`raw/papers/gpt/high-spin-20260920/NPA695-Jensen-2001-3.pdf`；SHA-256：`0fde4a838d94fdc23dcd4d4034a945073cb569c47c153e9e3b90676c44838770`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: 48 页全文；引言、两次熔合蒸发实验、Nordball γγ/γγγ 与 DCO 分析、完整 `165Tm` 能级图、四条新带、DSAM lineshape/lifetime/Qt、band mixing、B(M1)/B(E2)、CSM/Ultimate Cranker 形变和 crossing-frequency 系统学、E1 概率与总结均已阅读。Fig.2-3、5-8、9-19 和 Tables 1-8 的关键图表视觉核对。
- Not covered: 原始事件树、DSAM stopping-power Monte Carlo code、Ultimate Cranker code/input 和引用来源全文。
- Coverage caveats: 大量 Table 1 逐线数据保留在 source 原文；本页只固化改变组态、形变、alignment 和竞争解释排序的结果。部分新带自旋/组态仍为作者建议或多解 DCO 解释。

## Paper Question and Scientific Motivation

- 论文研究稀土 `165Tm` 中 `πh9/2[541]1/2−` 的形变、`i13/2` 中子延迟 alignment 和 crossing-frequency shift，并扩展高自旋能级纲图（PDF pp.3-4）。
- 主要问题是：变形改变、质子-中子相互作用和 pairing/Cor iolis effects 各自能解释多少 `πh9/2` 带相对于邻近 even-even 核的 delayed alignment；同时建立四条新带及其 γ-vibrational/3qp 性质。

## Method and Design Logic

- 两次实验：`150Nd(19F,4n)`，`85 MeV`；`154Sm(15N,4n)`，`70 MeV`。Nordball 使用 20 个 Compton-suppressed HPGe 和 60 元 BaF2 inner ball；最高统计达 `1.4×109` 和 `0.8×109` coincidence events（PDF pp.4-6）。
- `Eγ-Eγ` 矩阵和 `Eγ-Eγ-Eγ` cube 建立 level scheme；四环探测器角度约 `37.4°/79.2°/100.8°/142.6°`。DCO 用 `W(37×79)/W(79×37)`，dealignment 用 `W(37×37)/W(79×79)`；测得 `σ/I=0.26(4)`（PDF pp.6-7）。
- DSAM 用电子/核 stopping、Monte Carlo recoil velocities、Bateman feeding 和 lineshape least-squares 拟合；每个 backing 的四角谱用于 lifetime/Qs/Qt（PDF pp.23-27）。
- 相对形变用 two-band mixing；crossing frequencies、aligned angular momenta 和 `B(M1)/B(E2)` 约束新带组态；Ultimate Cranker diabatic PES/CSM 计算比较形变与 alignment（PDF pp.27-43）。

## Key Evidence and Reasoning Chain

1. Level scheme 扩展到 `71/2−`，新建四条带：两条 `K=17/2` 三准粒子候选带，另两条归为与 h9/2 质子耦合的 γ-vibrational bands（摘要；PDF pp.3, 19-23）。
2. `[541]1/2−` favoured signature 延伸至 `53/2−`，unfavoured signature 至约 `39/2−/43/2−`；`[411]1/2+` 和 `[404]7/2+` 分别扩展至 `67/2+`、`53/2+`（PDF pp.19-23）。
3. Bands 3/4 的 in-band DCO 多数支持 stretched E2，band 3 到 `[541]1/2−` 的平均 DCO `0.36(5)` 给出两个 δ 分支；band 4 的自旋/负宇称仍需结合 signature-partner、B(E2) 和邻核 γ band 系统学（PDF pp.22-23，Fig.5）。
4. DSAM 给出 `[541]1/2−` 加权 `Qt=8.3(5) eb`、`β2≈0.33`；`[411]1/2+` 为 `Qt=7.4(5) eb`、`β2≈0.30`。相对两带 mixing 进一步给 `[404]7/2+≈7.1(6) eb`、`[523]7/2−≈7.2(7) eb`，说明 h9/2 `[541]1/2−` 带形变约高 `12-15%`（PDF pp.25, 33-35，Tables 2,5,6）。
5. `[541]1/2−` 的 AB crossing 约 `355 keV`，显著高于 `[523]7/2−`、`[404]7/2+`、`[411]1/2+` 和邻近 even-even bands 的约 `247-281 keV`；CSM/PES 只解释部分 shift，剩余部分需要 pairing、configuration effects 或 residual proton-neutron interaction（PDF pp.36-43，Tables 3,8，Figs.17-18）。
6. `[411]1/2+↔[541]1/2−` interband E1 transitions 的强度比单粒子估计增强约 3-5 个数量级；加入 core octupole-vibrational coupling 后定性改善，但 spin/signature dependence 仍未完全解释（PDF pp.44-46，Fig.19）。

## Summary

Jensen 等人的 `165Tm` 工作把高统计 γγ/γγγ 谱学、DCO、DSAM 寿命、band mixing、alignment 和 diabatic CSM/PES 系统学结合起来。实验扩展了能级图并发现四条新带；DSAM 直接支持 `πh9/2[541]1/2−` 带比其它近邻带有更大形变。模型能解释部分 delayed `i13/2` crossing shift，但系统性低估 `[541]1/2−` 的 shift，提示形变之外还需残余质子-中子相互作用等机制。E1 增强指向八极振动耦合，但仍保留模型依赖。

## Experimental or Theoretical Setup

- `150Nd(19F,4n)` at 85 MeV and `154Sm(15N,4n)` at 70 MeV；Nordball 20 HPGe + 60 BaF2。
- DCO geometry: 37.4°, 79.2°, 100.8°, 142.6°；`σ/I=0.26(4)` from known stretched cascades。
- DSAM: thin/backed targets, Au/Pb stopping, four angular spectra, cascade side-feeding model with fixed `J(2)=65.0 ħ²/MeV`。
- Theory: two-band mixing, Ultimate Cranker diabatic PES/CSM, semiclassical B(M1)/B(E2), particle-rotor/octupole-coupling E1 estimates。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| J01-1 | `165Tm` level scheme extends to `71/2−` and adds four bands: two K=17/2 3qp candidates and two γ-vibrational bands coupled to h9/2 proton. | experimental-result/author-interpretation | direct | PDF pp.3,19-23，Figs.2-5 | true |
| J01-2 | DSAM gives weighted `Qt=8.3(5) eb` for `[541]1/2−` and `7.4(5) eb` for `[411]1/2+`; relative mixing gives `[404]7/2+≈7.1(6) eb`, `[523]7/2−≈7.2(7) eb`. | experimental-result | direct | PDF pp.25,33-35，Tables 2,5,6 | false |
| J01-3 | `[541]1/2−` AB crossing is near `355 keV`, delayed relative to comparable bands and even-even neighbours near `247-281 keV`. | experimental-result | direct | PDF pp.36-43，Tables 3,8，Figs.17-18 | false |
| J01-4 | CSM/PES explains only part of the delayed crossing; residual proton-neutron interactions are proposed as an additional contribution. | author-interpretation/model-result | direct | PDF pp.36-43 | true |
| J01-5 | E1 strengths between `[411]1/2+` and `[541]1/2−` are enhanced by orders of magnitude over single-particle estimates; octupole-vibrational coupling improves qualitative agreement. | experimental-result/model-result | direct | PDF pp.44-46，Fig.19 | true |

| J01-6 | 实际DSAM用Au/Pb各四角矩阵，37/79/101/143度对allsum；由于统计不足不能在任何目标跃迁之上开门，采用[411]两signature的483/527和516/467门、[541]favoured474门，均below。不是用abovegate直接消sidefeeding。 | direct-experimental-selection | direct | PDF22–23 / printed24–25 Sec3.2 | true |
| J01-7 | 电子阻停empirical并shellcorrected、核阻停differentialLindhardt；Currie/Bacelar MC按5fs构造timeslicedshapes，Batemanyield加权后least-squares。sidefeeding为三步同Qs、固定J(2)=65.0，非MU08的五步/2fs/SRIM链。 | direct-analysis-model | direct | PDF21–23 / printed23–25 Sec3.2 | true |
| J01-8 | Table2报告Pb-backed十一组levelτ/Qt，Au统计不足Pb三分之一但Qt在uncertainty内相合；原文称additional5%电子阻停systematic has been added to tableuncertainties，没有给联合Σ或概率合同。不无条件再叠5%、或断言相对ratio完全取消。 | direct-uncertainty-and-lineage | direct-and-boundary | PDF23 / printed25 Table2及其上段 | true |
| J01-9 | Table6四bandQt中[541]/[411]两值来自本DSAM，另外[404]/[523]由mixing分析相对矩再用它们标尺得到；同链派生不是四套独立寿命。normalization reference及oneqp/Sband比较分开。 | direct-derivation-dependence | direct | PDF33/printed35 Eq5后；PDF36/printed38 Table6 | true |
| J01-10 | 本session按实际Table2十一行、声明p_gamma=1/ICC0/fixedK1/2条件，从levelτ算B再转Qt，最大central差约1.772%；全部在额外nearest-decimal打印box中有交集。不恢复原ICC/branch/Kmixing/fitCov、不判原表错或把算术相合计独立实验。 | task-conditional-table-audit | derived | PDF23 Table2；day18-lifetime-strength-result jensen_conditional_rows | true |

| J01-11 | 本session在先前DSAM定向读之后，重新冻结新问题/承认强priming，完成48页主线/全部19图/8表角色和Eq1–9；密Table1/7/8只selectedrows定量核，不声称每格独立重建或原producer重跑。 | current-session-reading-scope | direct-original-provenance | jensen-fullmainline-reading-scope；PDF1–48 | true |
| J01-12 | positivepair用VMI未扰动带+spinindependentV共同拟energy/branch，K404=3.5/K411=.5且Q411=7.4在Table5固定，ratio=.96(.05)乘平均DSAMQ411得7.1(.6)，要求Q411随spin近constant。其支持之一是所用模型算Qt跨frequency变化通常<.2eb；不是实验已测全spin恒定。 | direct-bandmixing-reference-and-model-condition | direct-and-model | PDF31 Table5；PDF32 Sec5.1；PDF36 Sec6.2.1 | true |
| J01-13 | negativepair只在13/2近crossing混合、无offdiagonalM1，用163.9/177.5的rate与Eq5提相对矩；原文为可能50%Ω3/2混合计入ratio误差。configurationamplitude α/β与photonmultipoleδ不是同物理量，也不由强度得signedV。 | direct-mixing-model-and-purity-boundary | direct | PDF32–33 Eqs4–5/Fig14 | true |
| J01-14 | 本任务用actualTable1中心得α²≈.0166274/β²≈.9833726，|V|≈1.764615keV与Q541/Q523≈1.164763；选sinθ的principalasin会错分支，原rate选θ≈165.182°而非14.818°。sixTable5源模型eigenpairs的norm/interaction在额外printingbox内相合，非originalVMIfit/experimentCI复现。 | task-source-algebra-and-model-output-check | derived-model | Table1 PDF8/13；Table4/5 PDF31；Eq5 PDF33；jensen-bandmixing-result | true |
| J01-15 | 四Qt链为(A,B,rplusB,A/rminus)；即使额外让primitives独立，派生矩仍相关，Q523/Q541=1/rminus会消A。声明独立SDdesign给此ratio尺度.0668847，原Table6.87(.10)保持；未从summary差反解真实Cov或判作者错，5%已加不再重复叠。 | task-reference-dependency-and-covariance-boundary | derived-and-boundary | PDF23 Table2；PDF32/33；PDF36 Table6；jensen-bandmixing-result reference_dependency | true |
| J01-16 | Table7 N96modelωc给Tm255/Er225/Yb217keV，Table3/8实测355/281/269；中心双差Tm−Er为74obs−30model=44keV、Tm−Yb86−38=48keV。它们不是独立pninteraction测量，Tmgain>5.3不作点值；作者另指出evenbaseline偏差/pairing与deformation不足，residualpn是解释候选。 | direct-input-and-task-counter-baseline | direct-and-derived | PDF27 Table3；PDF37 Table7 N96；PDF39 Table8；PDF40–41 Sec6.3 | true |
| J01-17 | Bands3/4 DCO均有δ双根；band4最低spin13/2/15/2/17/2可能中17/2是signaturepartner/systematics建议且无3↔4link；higherthanquadrupoleexcluded是其枚举条件。不能以γ-vibration标签抹原多解或当已测唯一δ。 | source-counterevidence-and-assignment-condition | direct | PDF20 Sec3.1.4/footnote5；PDF29 Sec4.2.3 | true |
| J01-18 | Fig19的B(E1)用Table6DSAMQt及mixingbranch校正，不能当独立绝对strongE1测量；b0/b±1未做fit，只examples/qualitativeoctupole改善。按Eq8中r为长度、eeff为电荷的字面量纲，b应为fm−2，caption明确fm−2但prose一处字面fm2，原标记保留；频率依赖被忽略且spin/signature残差未闭合。 | direct-model-scope-and-derived-unit-boundary | direct-and-derived | PDF42 Eq7/Fig19caption；PDF43 Eqs8–9与末段 | true |

## Nuclear Structure Information

- `165Tm` bands: `[523]7/2−`, `[541]1/2−`, `[411]1/2+`, `[404]7/2+`, `[402]5/2+`, new bands 1-4, and candidate `[514]9/2−`, `[411]3/2+`.
- New-band assignments: band 1 `π[523]7/2−⊗ν[642]5/2+⊗ν[523]5/2−`, Kπ=17/2+; band 2 `π[404]7/2+⊗ν[642]5/2+⊗ν[523]5/2−`, Kπ=17/2−; bands 3/4 likely γ bands coupled to h9/2 proton.
- `[541]1/2−` shape polarization and delayed alignment are the main structure results; E1 links to `[411]1/2+` connect opposite-parity configurations.

## Authors' Interpretation

- The h9/2 `[541]1/2−` proton drives a larger deformation and delayed i13/2 neutron alignment, but deformation changes alone cannot explain the full crossing shift.
- Bands 3/4 are interpreted as γ-vibrational structures because of low excitation, alignment behavior, and B(E2)out/B(E2)in comparisons with `164Er`; their detailed spins and δ branches remain less secure.

## Model Results

- Ultimate Cranker diabatic PES/CSM predicts relative deformations and crossing frequencies across rare-earth nuclei. For `165Tm`, calculated Q values are generally 1-8% below measured; relative deformation ratios agree better.
- Two-band mixing gives `Vint=5.0(5) keV`, `Q([404]7/2+)/Q([411]1/2+)=0.96(5)`; `[541]1/2−/[523]7/2−` mixing gives `Vint=1.75(18) keV`, `Q` ratio `1.16(9)`.
- Octupole-vibrational E1 operator improves qualitative trends but does not fully reproduce signature/spin dependence.

## Competing Interpretations and Limitations

- Bands 3/4: γ-vibration, 3qp bandheads, or mixed configurations are not completely separable with present weak links; band 4 signature-partner assignment is suggested but lacks direct 3↔4 linking transitions.
- CSM/PES underestimates `[541]1/2−` crossing shift by up to ~100 keV; pairing, deformation, p-n interaction and model assumptions compete.
- DSAM side-feeding is modeled with a three-transition cascade and fixed moment of inertia; stopping-power systematics receive an added 5% uncertainty, and statistics prevent gating above all transitions of interest.
- B(M1)/B(E2) calculations set δ=0 for many bands; ratios can be overestimated by up to ~10% where δ is not measured.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-J01-1 | Core reconstruction | The source is a rare complete chain from level scheme to DSAM Q moments and crossing systematics; the h9/2 deformation and delayed alignment are supported by independent observable classes. | PDF pp.19-46 | self-checking |
| AR-J01-2 | Assumptions and dependencies | Qt depends on stopping powers, side-feeding model and rotational formula; crossing interpretation depends on CSM/PES and reference moments of inertia. | PDF pp.23-43 | self-checking |
| AR-J01-3 | Transfer conditions | The method/physics transfers to other rare-earth h9/2 bands only with matched DSAM, band-mixing and crossing reference; numerical Qt/crossing values do not transfer. | PDF pp.25-43 | provisional |
| AR-J01-4 | Failure conditions | If new lifetimes, side-feeding or p-n interaction calculations change Q ratios or crossing shifts, the deformation-only explanation is insufficient and the configuration ranking changes. | PDF pp.36-43 | active-L3 |
| AR-J01-5 | Reverse/falsification test | Compare another h9/2 odd-Z chain with direct Qt, AB crossing and E1 strength; vary stopping powers/side feeding and add residual p-n interaction to CSM. | PDF pp.36-46 | candidate-L3 |
| AR-J01-6 | Research-question decision | This is a high-value comparative source for h9/2 shape polarization, delayed alignment and DSAM/systematics; no L4 is opened without raw lineshapes or executable CSM inputs. | PDF pp.23-46 | completed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki already contains DSAM, high-spin alignment, shape and rare-earth references, but this source adds a full `165Tm` lifetime/Qt/crossing/E1 chain and explicit deformation-versus-p-n-interaction failure boundary.
- Effect of this source: `supports`, `limits` and `methodological-bridge`。
- Reason: It links direct lifetimes and branching to model interpretation while keeping CSM/PES and E1 octupole explanations separate from measured quantities.
- Persistence decision: source page and existing DSAM/alignment method links; no new `165Tm` band pages in this first pass beyond source-level mapping.
- Review state: `unreviewed`; claims self-audited by Codex, not human-reviewed。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[doppler-shift-attenuation-method]] | Detailed DSAM lineshape, side-feeding and stopping-power uncertainty example. |
| supports | [[angular-momentum-alignment]] | AB crossing and aligned angular momentum systematics connect band structure to neutron alignment. |
| limits | [[triaxial-deformation]] | Measured deformation supports core polarization, but deformation alone fails to explain the full crossing delay. |
| foundational-background | [[high-spin-phenomena]] | Extended level scheme, DCO, band mixing and rare-earth crossing history. |

## Human Review Triage

### P0

- J01-P0-1：`Qt`、`β2` 和 crossing-frequency values depend on DSAM stopping/feeding and reference-model assumptions; paper use must preserve those conditions.

### P1

- J01-P1-1：Bands 3/4 γ-vibrational and band 4 signature-partner assignments remain interpretation-level, with weak/missing links and multiple DCO δ branches.
- J01-P1-2：CSM/PES residual p-n interaction claim is a model gap/interpretation, not a direct measurement.

### P2/P3

- HS-006 and HS-007 are exact byte duplicates; HS-007 has an explicit row-level audit event and no second source page.

## Extracted Pages

- Nuclei: `165Tm` source-level entry only; no independent nucleus page created in this batch unit.
- Bands: `[541]1/2−`, `[523]7/2−`, `[411]1/2+`, `[404]7/2+`, Bands 1-4 retained inside source; independent pages deferred until cross-source map.
- Concepts: delayed alignment, shape polarization, γ-vibrational bands, band mixing, octupole-enhanced E1.
- Methods: [[doppler-shift-attenuation-method]], [[dco-ratio]], [[angular-momentum-alignment]].

## Non-source Notes and Follow-up

- HS-006 is the canonical copy; HS-007 is duplicate and must be marked `audited-reused` in the execution ledger.
- Later direct sources can test whether the h9/2 deformation/crossing pattern is universal across the rare-earth region or specific to this lineage.

## 2026-10-19 Day17内无学分Day18定向自审

本session早期只新读DSAM主链与必要context/匹配Table1/2/6，具体scope见[readingreceipt](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/day18-preview-reading-scope.json)，不冒称重新全文48页。原J01-1–5及falseflags逐字保持，新J01-6–10全needs_review。Fig7右列图头[411]1/2+与Table2的729.4/51/2+一致；caption字面另写[541]1/2−，保留printedlabel边界，不据此另造母态、修原件或判实验失败。

新的[[lifetime-strength-audit-165tm-136nd]]分层实际spectra、fitτ、rate/B换算与Qt/形变解释；previews不授Day18信用。

## 2026-10-19剩余主线完成与新组态混合链

早期J01-6–10只记录当时DSAM定向scope，现本session在新问题冻结后完成全主线；[actualscope](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/jensen-fullmainline-reading-scope.json)把19图/8表/9式与密表selectedrows分开。原J01-1–10/flags保持，不由后续扩scope重写历史独立性。新[[lifetime-strength-audit-165tm-136nd]]保存原Eq5与共同标尺Jacobian/模型baseline反证，只有conditionalalgebra没有新τ/Q/δ/interactionCI。

## Day18独立session：定向原读与停止时钟诊断

2026-10-20新session的[知情回忆](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/active-recall-before-sources.md)承认上述Day17预习。其后实际文本读PDF1–3、21–25、31–33、36、44–45，视觉核PDF23–25、33、36；本次是DSAM Sec3.2及必要实验/混合context，**不是新读48页全文**。原哈希、J01-1–18及旧reviewflags保持，详[实际scope](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/source-reading-scope-001.json)。Fig7右栏图头与caption的旧差异也保留。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| J01-D18-1 | 本次定向原读再次核：Table2是两条直接DSAM带的Pb数据，5% electronic-stopping systematic已经加进tableuncertainties；Table6另两带由mixing比值共用DSAM标尺。新阅读不增加独立寿命，原文不提供5%的联合概率/相关合同。 | current-session-original-audit | direct-and-boundary | PDF21–25 Sec3.2/Table2/Figs7–8；PDF31–33 Table5/Eq4–5；PDF36 Table6 | true |
| J01-D18-2 | 以Table2平均Qt中心8.3/7.4作声明的时钟敏感性：共同s→a s、全部τ/feeding→τ/a且固定branch/geometry时Qt均乘sqrt(a)，比值1.12162不变；若允许两带不同常数a，则a541/a411=(7.4/8.3)²≈.794890可使更正后中心相等。这不是实际阻停偏差估计，也不能与5%字样作概率检验；真实材料/feeding/Σ未得。 | task-conditional-clock-design | derived-and-boundary | PDF23 Table2均值；PDF36 Table6；lifetime-strength-audit的Day18停止时钟与带间contrast；clock-contrast-result-001 jensen_mean_Qt_sensitivity | true |
| J01-D18-3 | 十一行在p_gamma=1/ICC=0/pureE2/fixedK1/2条件下中心Qt最大相对差约1.76%；另加最近小数box可作舍入诊断，不能称实际branch库存/原实验CI或唯一producer认证。两直接DSAM带与mixing派生两带共享标尺，旧检查不变成新增实验。 | task-conditional-audit | derived-and-boundary | 原Table2或TableII；checkpoint078修订 | true |
| J01-D18-4 | Jensen 2001 Sec 3.2 明确报告采用 Currie (1969) 蒙特卡罗算法与 Bacelar (1987) 代码按 5 fs 时间步长求解 Bateman 方程合成谱形；电子阻停采用 Northcliffe-Schilling (1970) 附带 Ziegler-Chu (1974) 与 Sie (1977) 壳修正，核阻停采用微商 Lindhard 截面；侧馈模型为 3 步级联（固定惯性矩 J(2)=65.0 hbar^2/MeV 与同 Qs）；Table 2 寿命与 Qt 误差明确已直接计入额外 +5% 电子阻停系统误差；全部门控均位于感兴趣能级下方。这与 Mukhopadhyay 2008 的 2 fs / SRIM / 5 步可变 Qs 级联及表外排除 15% 误差形成严格方法学分层。 | task-methodology-contrast-audit | direct-and-boundary | PDF pp.23-25 Sec 3.2 & Table 2；dsam-systematics-contrast-result-059 | true |

Knowledge impact：`limits`把共同绝对停止标尺当作带间形变差的任意解释，也`limits`把共用backing当作所有系统误差必然抵消。两方向均须检查actual速度场、位置响应、feeding和branch。此处不修正原Qt、β2、误差或结构指认。
