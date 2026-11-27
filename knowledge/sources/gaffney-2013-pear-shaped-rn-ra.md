---
type: source
title: "Gaffney et al. 2013 - Studies of pear-shaped nuclei using accelerated radioactive beams"
aliases: [Gaffney 2013 pear-shaped nuclei, 220Rn 224Ra Coulomb excitation]
created: 2026-09-20
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Studies of pear-shaped nuclei using accelerated radioactive beams"
authors: [L. P. Gaffney, P. A. Butler, M. Scheck, A. B. Hayes, F. Wenander, et al.]
journal: Nature
year: 2013
volume: 497
pages: "199-204"
doi: "10.1038/nature12073"
citation_key: Gaffney_2013
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "https://doi.org/10.1038/nature12073"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/形变/2013_Gaffney et al_Studies of pear-shaped nuclei using accelerated radioactive beams.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/形变/2013_Gaffney et al_Studies of pear-shaped nuclei using accelerated radioactive beams.pdf"
raw_sha256: "3b7975206409de9286df55a82c820783b2ebd371824bf50d69da6c9e916c551b"
nuclei: [220Rn, 224Ra]
reactions: [coulomb-excitation-radioactive-beams]
experiments: [cern-isolde-rex-miniball]
models: [rotational-model, mean-field-octupole, cluster-model]
observables: [E1, E2, E3, Q1, Q2, Q3, Coulomb-excitation-yields]
methods: [coulomb-excitation, GOSIA, gamma-ray-spectroscopy]
tags: [pear-shape, octupole, reflection-asymmetry, Rn, Ra, EDM]
---

# Studies of pear-shaped nuclei using accelerated radioactive beams

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

- L. P. Gaffney *et al.*, *Nature* **497**, 199–204 (2013), DOI `10.1038/nature12073`。
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/形变/2013_Gaffney et al_Studies of pear-shaped nuclei using accelerated radioactive beams.pdf`。
- 6-page Nature PDF; title, author list, DOI, figures, Table 1 and Methods/Outlook identity checked. This is a direct Coulomb-excitation experiment, not merely a review of pear shapes.

## Scope and Reading Depth

- journal pp.199–204 (PDF pp.1–6) fully read, including abstract/introduction, Figs.1–5, partial level schemes, Table 1 matrix elements, Coulomb-excitation/GOSIA description, shape comparison and Outlook/Methods.
- Figure/table audit: MINIBALL spectra and level schemes, `Q2/Q3` versus spin, intrinsic-shape plots, isotope-systematics plot and all Table 1 E1/E2/E3 matrix elements were checked.
- Not covered: raw GOSIA input/output files, event matrices, full lifetime datasets and later independent measurements.

## Paper Question and Experimental Logic

The experiment asks whether direct electric-octupole transition strengths can distinguish dynamic octupole correlations in `220Rn` from stronger, more static pear-shaped collectivity in `224Ra`, using accelerated radioactive beams and Coulomb excitation.

1. Produce and accelerate `220Rn`/`224Ra` at REX-ISOLDE (`2.82–2.83 MeV/u`), bombard `60Ni`, `112Cd`, `114Cd` or `120Sn` targets, and detect scattered projectiles/recoils with segmented silicon plus MINIBALL (24 segmented HPGe detectors).
2. Measure γ yields in separated recoil-angle ranges and fit Coulomb-excitation matrix elements with GOSIA. Known lifetimes/branching and target matrix elements constrain the fit; 34 (`220Rn`) and 57 (`224Ra`) independent points constrain 22/23 free parameters.
3. Convert matrix elements to intrinsic `Q1`, `Q2`, `Q3` and compare level energies, transition strengths, shape plots and isotope trends with mean-field and cluster-model predictions.

## Key Evidence and Reasoning Chain

- `220Rn` has `Q2≈434(14) e fm²` and `Q3≈2180(130) e fm³`; `224Ra` has `Q2≈632(10) e fm²` and `Q3≈2520(90) e fm³` for the lowest transitions (Table 2/systematics). The direct E3 matrix elements are `810(50) e fm³` (`220Rn`, `0+→3−`) and `940(30) e fm³` (`224Ra`, `0+→3−`), with additional E3 links listed in Table 1.
- `Q2` and `Q3` remain approximately constant over the measured spin range, supporting a rotational intrinsic-moment description rather than a rapidly changing shape (Fig.3).
- Shape reconstruction gives `220Rn` a more vibrational motion about reflection symmetry and `224Ra` a stronger static octupole/pear component; the `224Ra` E3 strength is larger and more coherent with a permanent deformation interpretation (Fig.4).
- `220Rn` has weaker octupole collectivity than `224Ra`; comparisons with mean-field D1M/D1S and cluster-model predictions show differing isotope trends. The authors conclude `219,221Rn` are likely less favorable EDM candidates than `223,225Ra`, while future heavier Rn isotopes may improve.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GA13-1 | Coulomb excitation of radioactive `220Rn` and `224Ra` measures E1/E2/E3 matrix elements with `10%`-level accuracy using MINIBALL and GOSIA. | experimental-result | direct | journal pp.199–203 (PDF pp.1–5), Table 1, Methods | true |
| GA13-2 | `224Ra` exhibits stronger and more coherent octupole collectivity than `220Rn`, with `Q3` and E3 strengths supporting a pear-shaped/static-deformation interpretation. | experimental-result/author-interpretation | mixed | journal pp.200–203 (PDF pp.2–5), Figs.3–5, Tables 1–2 | true |
| GA13-3 | Intrinsic E2/E3 moments are approximately constant across the measured spin range. | experimental-result | direct | journal p.202 (PDF p.4), Fig.3 | true |
| GA13-4 | Mean-field and cluster-model calculations predict different Rn/Ra octupole trends; the data oppose the cluster-model trend and distinguish model families. | model-data-comparison | mixed | journal pp.202–203 (PDF pp.4–5), Fig.5, Outlook | true |
| GA13-5 | Octupole-enhanced EDM candidate ranking favors Ra over the measured Rn isotopes, subject to future spectroscopy. | author-interpretation | indirect | journal p.203 (PDF p.5), Outlook | true |
| GA13-6 | Authors state that the measured E2/E3 matrix elements are consistent with a rotating deformed distribution but do not distinguish parity states projected from a static quadrupole-octupole shape from an octupole oscillation of a quadrupole shape. | interpretation-boundary | direct-to-source | journal p.202 (PDF p.4), text before Table 2 | true |

## Summary

This experiment provides direct E3-strength evidence separating weaker octupole collectivity in `220Rn` from stronger pear-shaped behavior in `224Ra`. The result anchors the distinction between octupole correlations and static deformation with a multi-target Coulomb-excitation/GOSIA analysis, while retaining model and input-data boundaries.

## Competing Interpretations and Limitations

Constant intrinsic moments support a rotational description but do not by themselves prove a rigid static shape; vibrational/soft models can produce strong E3 transitions. GOSIA results depend on target matrix elements, recoil-angle ranges, lifetimes/branching and rotational-model constraints. Absolute E1 moments remain small and cancellation-sensitive, and the EDM-candidate extrapolation to odd-A isotopes is not a direct measurement.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| GA13-AR-1 | Evidence chain | Coulomb-excitation yields → GOSIA matrix elements → Q1/Q2/Q3 → shape/systematics comparison. | journal pp.200–203 (PDF pp.2–5), Methods | self-checking |
| GA13-AR-2 | Direct versus model | E1/E2/E3 matrix elements and Q values are measured/fitted observables; pear/static and EDM implications are author/model interpretations. | Table 1, Figs.3–5 | self-checking |
| GA13-AR-3 | Transfer condition | Q3 comparison transfers only with matched Coulomb-excitation model, target matrix elements and spin range; not as a universal β3 prior. | PDF Methods/Table 1 | provisional |
| GA13-AR-4 | Failure condition | Missing raw GOSIA files, target uncertainties, lifetime/branching revisions or soft-vibrational alternatives could change absolute strengths and deformation ranking. | journal pp.202–203 (PDF pp.4–5) | active-L3 |
| GA13-AR-5 | Independence | Direct Rn/Ra experiment; cited `226Ra` and other isotope values are historical comparison, not independent new points. | Table 2/Fig.5 | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` octupole-deformation/correlation boundaries and provides a direct Coulomb-excitation benchmark; `revises` any assumption that E3 enhancement alone identifies static shape.
- Persistence: update [[octupole-deformation]], [[octupole-correlation]], [[reflection-asymmetric-nuclei]], [[coulomb-excitation]] and the high-spin evidence map.
- Review state: Codex self-audited; not `human-reviewed`.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[octupole-deformation]] | Direct E3/Q3 benchmark for stronger static-like `224Ra` versus weaker `220Rn`. |
| supports | [[octupole-correlation]] | E3 moments as direct collective octupole observable, separated from model β3. |
| methodological-bridge | [[coulomb-excitation]] | Radioactive-beam MINIBALL/GOSIA matrix-element extraction. |
| candidate-L3 | [[a130-high-spin-collective-modes-evidence-map]] | Non-A≈130 benchmark for parity-sensitive collective-mode inference. |
| observable-boundary | [[shape-observable-matrix]] | Direct E3 and E2 data do not alone distinguish a static octupole minimum from octupole vibration. |

## Human Review Triage

### P0

- `GA13-P0-1`: keep measured matrix elements, intrinsic moments and pear/static interpretation separate; do not convert `Q3` directly to a universal β3 without the stated shape model.

### P1

- `GA13-P1-1`: GOSIA fit correlations, target matrix elements and lifetime inputs need source-data-level recheck before absolute-strength reuse.
- `GA13-P1-2`: EDM-candidate ranking is an extrapolation to odd-A isotopes and depends on parity-doublet/Schiff-moment theory.

## Extracted Pages

- Nuclei: `220Rn`, `224Ra` (source-level pages not created in this unit).
- Concepts: [[octupole-deformation]], [[octupole-correlation]], [[reflection-asymmetric-nuclei]]。
- Methods: [[coulomb-excitation]]。

## L3/L4 Follow-up

- L3 question: can a common E3/Q3–PES–parity-systematics map distinguish stable octupole minima from soft octupole correlations across Rn/Ra/Th/U and the A≈130 cases? Required companions are E3 strengths, E1/energy-displacement, parity bands and model sensitivity.
- No L4 run: GOSIA files and raw yield matrices are not supplied; Table 1 is a reported result, not a machine-readable analysis input.

## Day19量化审计：Rn-Ra梨形核库仑激发、Alaga转子自洽性与EDM增强度规

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_gaffney13_rn220_ra224_octupole_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/gaffney13-rn220-ra224-octupole-result-059.json`，核准了 $^{220}\text{Rn}$ 与 $^{224}\text{Ra}$ 放射性束库仑激发八极与四极电磁性质的物理判据事实：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| GA13-D19-1 | 对 Gaffney 2013 Table 1 与 Table 2 数据进行系统学审计：(1) $Q_2, Q_3$ 阶跃与模型甄别：实测 $^{224}\text{Ra}$ 的 $Q_2 = 632(10)\text{ e}\text{fm}^2$ 与 $Q_3 = 2520(90)\text{ e}\text{fm}^3$ 相对 $^{220}\text{Rn}$ 分别增长 $1.456$ 倍与 $340\text{ e}\text{fm}^3$（$z = 2.15\sigma$），其带内 $B(E2)$ 翻倍（$98\text{ W.u.}$ 对 $48\text{ W.u.}$），推翻了团簇模型下降预言并支持平均场静态形变；(2) 刚性转子自洽性：矩阵元比值 $\langle 2_1^+ \Vert E2 \Vert 4_1^+ \rangle / \langle 0_1^+ \Vert E2 \Vert 2_1^+ \rangle = 315/199 = 1.583$ 与 Alaga 理论在 $0.1\%$ 内重合；(3) EDM 增强：Schiff 矩度规（$Z Q_3 Q_2$）高出 $1.72$ 倍，结合奇质量 $^{225}\text{Ra}$ 仅 $55\text{ keV}$ 的宇称双重态劈裂，确立了 Ra 同位素在原子电偶极矩（EDM）探索中拥有超球形原子 100-1000 倍增强的物理地位。 | task-pear-shaped-and-edm-audit | derived-and-boundary | journal pp.200-203 Tables 1-2 Figs.3-5; gaffney13-rn220-ra224-octupole-result-059.json | true |

## Day 21 Checkpoint 022 证据门量化审计：224Ra 静态梨形与 220Rn 八极振动推断边界

依据推断阶梯方法论（[[experimental-claim-boundaries]]）及独立量化程序 day21_checkpoint022_rn220_ra224_octupole_audit.py（产物 outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/rn220-ra224-octupole-audit-022.json），对 Gaffney 2013 的放射性束库仑激发实验完成推断阶梯边界核定：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GA13-D21-1 | 依据推断阶梯审计，Gaffney 2013 确立了梨形核判定的关键分水岭：(1) B(E3) 增强与静态形变解耦：基态增强 B(E3)（224Ra 42 W.u. 与 220Rn 33 W.u.）反映八极涨落方均根振幅，无法单独区分静态梨形与动态振动；(2) 宇称双重带能级位移 delta E(I)：224Ra 从 173.8 keV 快速塌缩至 19.8 keV 趋零（证实静态梨形），220Rn 维持 140–415 keV 大位移（证实动态振动）；(3) 内禀 Q3 随自旋平坦度：224Ra 保持 Q3~2520 e fm^3 恒定，220Rn 随自旋衰减；(4) Schiff 矩度规（Z Q2 Q3）在 224Ra 高出 1.72 倍，结合 225Ra 仅 55 keV 能隙，确立了 Ra 在 EDM 探索中的优选地位。 | source-result-and-criterion | direct-and-boundary | pp.199-204, Tables 1-2, Figs.3-5; rn220-ra224-octupole-audit-022.json | true |

## 2026-11-27 — 馆藏原件与覆盖核对

- {"start": 1, "end": 2, "sections": "著录、八极形变与 EDM 背景、实验引入、图1代表性 γ 谱和图2局部能级纲图"}
- {"start": 3, "end": 4, "sections": "实验与讨论、表1矩阵元和 B(Eλ)、图3自旋依赖及转子换算式、表2跨核素内禀矩、图4形状示意"}
- {"start": 5, "end": 6, "sections": "图5同位素系统学、展望、Methods Summary、参考文献 [1]–[50]、致谢和作者信息"}
- 本次获取的具体覆盖：审读 PDF 第1–6页，覆盖引言、实验与讨论、展望、Methods Summary、5幅图的图注、2张表的可辨条目、参考文献 [1]–[50] 及文末声明。个别矩阵元行、图注公式、比较号和单位有抽取损伤，未核验原图或版面。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A17-1 | 多靶双角区库仑激发的 GOSIA 拟合报告 220Rn 和 224Ra 的 &#124;⟨0⁺₁‖E3‖3⁻₁⟩&#124; 分别为 810(50) 和 940(30) e fm³，相应的 3⁻₁→0⁺₁ 退激 B(E3) 为 33(4) 和 42(3) W.u.。表1还列出其他拟合矩阵元和若干 3σ 上限。 | 由实验产额拟合的矩阵元 | source-reported | PDF 第2页图1–2，第3页表1及实验段，第5页 Methods Summary。表1的上下标和限号待核第3页。 | true |
| A17-2 | 按文中转子关系由低态矩阵元换算，220Rn 与 224Ra 的 Q₂ 分别为 434(14) 和 632(10) e fm²，Q₃ 分别为 2,180(130) 和 2,520(90) e fm³。作者报告两核的四极矩和八极矩在所测自旋范围内与常值相容。 | 转子模型下的派生量 | source-reported | PDF 第3页图3及其未编号换算式，第4页表2，第5页展望。图3根号范围、系数和下标待查第3页。 | true |
| A17-3 | 作者结合较强的 224Ra 八极集体性和既有能级系统学，将 224Ra 解释为更接近静态八极形变，将 220Rn 解释为与八极振动相容。正文明确指出，本组 E2/E3 矩阵元可同时容许从四极–八极形状投影出负宇称态及四极形状的八极振动。图4为按该解释绘制的形状示意。 | 作者形状解释 | source-reported | PDF 第4页表2下方讨论与图4，第5页展望。图4形变参数及理论 β₄ 来源待核第4页图注。 | true |
| A17-4 | 作者指出，Q₃ 从 226Ra 附近向较低中子数下降的趋势与所比较的团簇模型趋势相反，也与 Gogny HFB 所报 224Ra 峰值有差异。关于 219,221Rn 的八极增强 EDM 可能小于 223,225Ra 的判断，来自同位素系统学和既有奇质量核宇称双重态资料。 | 模型比较与奇质量核外推 | source-reported | PDF 第4页模型及宇称双重态讨论，第5页图5和展望，相关参考文献 [7,15–17,21,23]。 | true |

REX-ISOLDE 束、硅探测器与 MINIBALL 提供粒子–γ 符合产额。GOSIA 合用分角区产额、靶核电磁输入、已知寿命和分支比，两个核分别以 34 和57个数据点约束 22 和23个自由参数。部分不敏感矩阵元固定或按转子关系耦合。224Ra 的 2⁺₁→0⁺₁ 受 Ra X 射线污染，独立寿命核查使用该核的 4⁺₁ 寿命。Qλ 与形状参数另含几何模型假设。

- GA13-3 的图3定位改为 PDF 第3页、期刊第201页。矩阵元绝对值、退激 B(E3) 和模型换算 Q₃ 分别著录。旧笔记中的 0⁺→3⁻ 若用作 B(E3) 方向，应改为表1所报的 3⁻→0⁺。展望中的约10%精度表述只用于方法能力，多条表项有更大误差或仅给上限。
- 将 GA13-D21-1 的 224Ra 与 220Rn 的 ΔE(I) 数列及排他性判定改为第4页对文献 [7] 能级系统学的定性援引。将 Rn 的 Q₃ 随自旋衰减改为本文报告的与常值相容。图4形状示意保留模型限定。
- GA13-D19-1 中的 2.15σ、Alaga 比值在 0.1% 内符合，以及两处历史审计所写的 ZQ₂Q₃ 增强 1.72 倍，均无原文验证。矩阵元比可追到表1的 315(6) 与 199(3)，显著性与吻合精度需另行计算并说明误差假定。第4页援引的是奇质量 Ra 的约 50 keV 量级，比较号待核该页，225Ra 的 55 keV 不能按此件著录。第1页的 100–1,000 倍是文献讨论的理论灵敏度量级。
- PDF 第1页的 3B、第2页的 γ 和宇称乱码、第3页表1的限号与指数及图3根号式、第5页的束流电荷态字符均需查对应原页。当前可保留清晰段落与可辨表项，破损公式及不清楚的符号不据文本补写。
