---
type: source
title: "Bucher et al. 2017 - Direct evidence for octupole deformation in 146Ba"
aliases: [Bucher 2017 146Ba direct E3]
created: 2026-09-21
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Direct Evidence for Octupole Deformation in 146Ba and the Origin of Large E1 Moment Variations in Reflection-Asymmetric Nuclei"
authors: [B. Bucher, S. Zhu, C. Y. Wu, R. V. F. Janssens, R. N. Bernard, L. M. Robledo, T. R. Rodriguez, D. Cline, A. B. Hayes, A. D. Ayangeakaa, M. Q. Buckner, C. M. Campbell, M. P. Carpenter, J. A. Clark, H. L. Crawford, H. M. David, C. Dickerson, J. Harker, C. R. Hoffman, B. P. Kay, F. G. Kondev, T. Lauritsen, A. O. Macchiavelli, R. C. Pardo, G. Savard, R. Vondrasek]
journal: "Physical Review Letters"
year: 2017
volume: 118
pages: "152504"
doi: "10.1103/PhysRevLett.118.152504"
citation_key: Bucher_2017
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "https://doi.org/10.1103/PhysRevLett.118.152504"
alternate_source: "https://arxiv.org/abs/1703.05268"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/external-146ba/PDFs/Direct_Evidence_for_Octupole_Deformation_in_146Ba_and_the_Origin_of_Large_E1_Moment_Variations_in_Reflection-Asymmetric_Nuclei.pdf"
raw_sha256: "c49cb44350cd24f25d172efe405cd9e78360692eb4087bb3eef1801534264beb"
nuclei: [146Ba, 144Ba, 148Ba, 208Pb]
reactions: [sub-barrier-coulomb-excitation]
experiments: [CARIBU, ATLAS, CHICO2, GRETINA]
models: [GOSIA, symmetry-conserving-configuration-mixing, Gogny-D1S-HFB]
observables: [B(E3), B(E1), Q3, electric-dipole-moment, octupole-collectivity]
methods: [coulomb-excitation, gamma-ray-tracking, particle-gamma-coincidence]
tags: [146Ba, octupole, E3, E1, external-research]
---

# Direct evidence for octupole deformation in `146Ba`

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

- B. Bucher *et al.*, *Phys. Rev. Lett.* **118**, 152504 (2017), DOI `10.1103/PhysRevLett.118.152504`.
- Local full text: lawful arXiv copy `1703.05268`, SHA-256 recorded in `EXT-20260921-001`.

## Scope and Reading Depth

- Six-page manuscript read end-to-end: motivation, CARIBU/ATLAS/CHICO2/GRETINA setup, GOSIA fit, Table I, `B(E3)`/`B(E1)` comparison, SCCM/GCM interpretation, orbital-occupancy explanation and alternative high-spin interpretations.
- No SI was requested or supplied. The local copy is used for evidence audit; the published DOI is the bibliographic anchor.

## Question and Evidence

The paper tests whether the sharp reduction of the intrinsic electric-dipole moment in `146Ba` signals weakened octupole collectivity. A `659 MeV` `146Ba` beam was Coulomb excited on `208Pb`; CHICO2 separated `A=146` products and GRETINA measured the γ yields. GOSIA fitted E1/E2/E3 matrix elements, then released rigid-rotor coupling when estimating uncertainties (PDF pp.2–3, Fig.1–2, Table I).

The direct ground-state E3 matrix element is `0.65(+0.14/−0.20) eb^{3/2}`, corresponding to `B(E3;3−→0+)=48(+21/−29) W.u.`. This is essentially the same strength as the `144Ba` result. The small E1 strength is therefore not evidence for quenched octupole collectivity; the SCCM calculation attributes the E1 suppression to neutron-orbital occupancy and cancellation of intrinsic dipole contributions (PDF pp.3–5, Table I, Figs.3–5).

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| EXT146-1 | Direct Coulomb excitation measures `B(E3;3−→0+)=48(+21/−29) W.u.` in `146Ba`. | experiment-result | direct | PDF pp.2–3, Table I | true |
| EXT146-2 | `146Ba` has strong octupole collectivity despite a more than order-of-magnitude dipole-moment reduction relative to `144Ba`. | cross-isotope-result | mixed | PDF pp.1, 3–5 | true |
| EXT146-3 | SCCM/GCM connects E1 variation to neutron-orbital occupancy and projected intrinsic-state overlap. | model-result | mixed | PDF pp.3–5, Figs.3–5 | true |

## Summary

This external source materially strengthens the octupole evidence ladder: direct E3 strength persists from `144Ba` to `146Ba`, while E1 strength varies independently with microscopic occupancy.

## Counter-evidence and Competing Interpretations

- Sudden band alignment and the `146Ba` high-spin behavior had motivated hypotheses of quenched octupole strength, a reflection-symmetric shape, or aligned octupole phonons; the direct E3 result rejects the first as a sufficient explanation while leaving the alternatives as model questions.
- GOSIA uncertainties are statistics limited, and E1 matrix elements are constrained mostly by prior data rather than new yields.

## Model Dependence

The SCCM calculation uses axially symmetric quadrupole and octupole coordinates, angular-momentum/parity/particle-number projection and Gogny D1S. It explains E1 variation within that model space; it does not turn the inferred `β2/β3` landscape into a model-independent laboratory shape measurement.

## Limitations and Missing Evidence

- Raw event matrices, full GOSIA covariance and SCCM code are unavailable.
- `146Ba` is a related but independent experiment, so it strengthens the isotope systematics without replacing the `144Ba` source.

## Competing Interpretations and Limitations

The high-spin alignment and sudden E1 reduction had motivated quenched-octupole, reflection-symmetric-shape and aligned-octupole-phonon explanations. The direct E3 result rules out a simple “small E1 means weak octupole” inference, while the detailed microscopic occupancy mechanism remains model dependent.

## Knowledge Impact and Learning Decision

- Effect: `supports` and `revises` [[octupole-deformation]], [[octupole-correlation]], [[octupole-and-rare-electromagnetic-decay]]、[[recoil-distance-doppler-shift]]、[[lifetime-method-selection-response-contract]] and the `144Ba` direct-E3 evidence map.
- External increment: direct neighboring-isotope E3 evidence separates octupole strength from E1 dipole-moment size.
- Review state: Codex self-audited; not `human-reviewed`.

## Extracted Pages

- Nuclei/concepts: `146Ba`, [[octupole-deformation]], [[octupole-correlation]], [[octupole-and-rare-electromagnetic-decay]]、[[recoil-distance-doppler-shift]]、[[lifetime-method-selection-response-contract]]。

## Sources

- [[bucher-2016-144ba-direct-octupole]]
- [[octupole-deformation]], [[octupole-correlation]], [[octupole-and-rare-electromagnetic-decay]]、[[recoil-distance-doppler-shift]]、[[lifetime-method-selection-response-contract]]

## Day19量化审计：146Ba八极集体性保持与E1偶极矩相消破缺机制

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_ba144_ba146_octupole_e1_audit.py` 的 9 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/ba144-ba146-octupole-e1-result-046.json`，系统核准了 Bucher 2017（PRL 118, 152504）关于 $^{146}\text{Ba}$ 直接八极矩阵元测量与电偶极矩相消的量化机制：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| BU17-D19-1 | withdrawn：旧“严格1.000/宏观+.22微观−.21/93%相消/普适最高终判”认证缺原件支持；适用当前记录为EXT146-1–3及BU17-D25P-A005-01。保留强E3与E1非单调代理的有界结论，原字节在Git历史。 | withdrawn-overclaim | rejected-and-replaced | BU17-D25P-A005-01 | true |


## Day19量化审计：宏观微观电偶极矩D0相消、八极形变非可逆定理与单纯形带崩塌

**checkpoint088：撤回旧科学认证；原标题保留为历史anchor。**

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| BU17-D19-2 | 撤回checkpoint079的科学认证：0.65与48只是两次报告的舍入中心，不能称严格相等；0.180和−0.146等分解没有本练习原件定位，不能当实测壳修正。小E1不能唯一判弱八极这一边界保留，直接E3强度也不能单独证明静态刚性梨形。旧数值脚本是自设算术，不是独立实验审计。 | source-and-analysis-correction | direct-where-reread-otherwise-withdrawn | checkpoint088 source scope and rejection registry | true |
## Day21周考推断阶梯审计：八极跃迁集体性保持、D0解耦与转子模型约束边界

依据独立审计程序 `system/scripts/day21_checkpoint006_octupole_ba_audit.py` 与审计产物 `outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/octupole-ba-audit-006.json`，确立本源在推断阶梯上的边界：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| EXT146-D21-1 | Bucher 2017 测得 $^{146}\text{Ba}$ 维持了与 $^{144}\text{Ba}$ 相同的强八极跃迁几率 $B(E3; 3^- \to 0^+) = 48_{-29}^{+21}\text{ W.u.}$，但其实测电偶极跃迁矩阵元 $|\langle 1^- \Vert M(E1) \Vert 0^+ \rangle| = 0.000223\ e\text{b}^{1/2}$（$B(E1) \approx 9.3 \times 10^{-7}\text{ W.u.}$），内禀电偶极矩 $|D_0| \le 0.01\ e\text{fm}$ 较 $^{144}\text{Ba}$（$0.13\ e\text{fm}$）骤降逾 13 倍。该实验确证 $B(E1)$ 不是指示八极集体性强弱的单调代理量；另外，Table I 中激发态矩阵元与轴对称刚性转子预测的高度吻合源自 GOSIA 拟合所施加的转子耦合约束，在释放该约束时矩阵元误差扩大至 $+68\%/-80\%$，未构成转子模型的独立统计检验。 | claim-boundary-audit | direct-and-derived | PRL 118, 152504 pp.2-5, Table I; octupole-ba-audit-006.json | true |

## Day25内Day26无学分preview：相消机制的实际分解

checkpoint005独立代理定向核原PDF2–5/Figs4–5，保持已有Day19/21撤回，不将历史脚本算术作为实验证明。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BU17-D25P-A005-01 | SCCM将E1变化联系到中子占据引起的偶极贡献与质子贡献几乎相消；原段未认证+.22/−.21或宏观液滴/微观壳项的逐项对应。E3与144Ba报告中心舍入相同且误差相容，不证明严格恒定或静态刚性梨形。 | direct-model-explanation-and-observable-boundary | direct-original | PDF5 first paragraph | true |

E1低态约束主要来自既有寿命/BR，与本次CoulEx的E3提取须分谱系；70为纳入网络的矩阵元数而非70项独立无约束数据。正式Day26信用仍保留到自己的run。

## Day26：实际占据、E1定量偏差与投影算符核

本次重读本地六页主线，视觉核PDF3 Table I与PDF4 Figs3–5。文件带arXiv1703.05268v1标记；内部Dated字段为September12,2018，本次不据此重定义arXiv版本或冒称VoR。原raw/SHA、旧claim与review flags保留。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| BU17-D26-001 | E1实验幅度0.000223(+10/−8) e b^(1/2)，SCCM为0.00474；打印中心的模型/实验幅度比约21.26、强度比约451.8。作者的“fair agreement”不能当该E1绝对值已精确复现。E1实验约束主要来自此前τ/BR。 | direct-table-and-task-calculation | direct-original-plus-rounded-input-algebra | PDF3 Table I and following paragraph | true |
| BU17-D26-002 | 文中列h9/2、f7/2、i13/2球形parentage的三条变形中子轨道，Kπ标签依次3/2−、5/2−、1/2+，146Ba的v²依次0.40、0.27、0.20；不是三个完整j壳的总占据。其贡献近抵消质子贡献是作者模型解释。 | model-result-and-label-boundary | direct-original | PDF4 Fig5 and last paragraph; PDF5 opening | true |
| BU17-D26-003 | 计算D0随144→146→148由正到近零再负；实验E1/E3相对符号对产额不敏感，不能把计算的符号变化当已测符号。 | model-vs-measurement | direct-original | PDF3 after Table I; PDF4 left column | true |
| BU17-D26-004 | 投影跃迁含collective amplitudes与算符在投影intrinsic states间的核；仅给v²或相似F图不足以恢复绝对有符号E1分解。方法的双坐标相干求和见BE16 Eq4。 | model-method-and-readiness-boundary | direct-method-plus-inference | PDF4; BE16-D26-005 | true |
| BU17-D26-005 | 两Ba的E3区间相容且报告中心均舍入为48 W.u.，不证明严格相等，也不单独区分静态局域形状与软八极相关。0+→3−与3−→0+的B相差7倍。 | observable-and-inference-boundary | direct-original-plus-angular-momentum-definition | PDF3; BU16 printed112503-4 | true |

`supports` 占据驱动的E1/E3解耦解释；`limits` 精确相消百分比、实验符号与绝对E1拟合认证；`revises` 用F图相似直接代替transition-kernel求和。方法来源为 [[bernard-2016-144ba-sccm-octupole]]，综合见 [[octupole-mr-amr-evidence-gradient]]。Egido–Robledo1990 Ref35正文与生产核仍待取得；不补写不存在的质子/中子分项数值。
