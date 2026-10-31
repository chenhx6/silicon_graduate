---
type: source
title: "Heyde & Wood 2011 - Shape coexistence in atomic nuclei"
aliases: [Heyde Wood 2011 shape coexistence review]
created: 2026-09-20
updated: 2026-10-26
status: ai-draft
review_status: unreviewed
source_type: rmp-review
reading_depth: deep-read
title_original: "Shape coexistence in atomic nuclei"
authors: [Kris Heyde, John L. Wood]
journal: "Reviews of Modern Physics"
year: 2011
volume: 83
pages: "1467-1521"
doi: "10.1103/RevModPhys.83.1467"
citation_key: Heyde_2011
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "https://doi.org/10.1103/RevModPhys.83.1467"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/review/2011_Heyde_Wood_Shape coexistence in atomic nuclei.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/review/2011_Heyde_Wood_Shape coexistence in atomic nuclei.pdf"
raw_sha256: "660c376e493e638501bfc8596d4eda46f490becb811ba5f30259d6f78c652183"
nuclei: [16O, 40Ca, 56Ni, 186Pb, 188Hg, 100Zr]
reactions: []
experiments: []
models: [shell-model, mean-field, IBM, beyond-mean-field, GCM]
observables: [E0-transition, B(E2), charge-radius, shape-coexistence, 0plus-states]
methods: [review-synthesis, spectroscopy]
tags: [shape-coexistence, shell-evolution, E0, E2, review]
---

# Shape coexistence in atomic nuclei

> Day24内Day25预习025：旧HW11-D21-1无定位混合百分比/绝对V硬门与“E0排他＋必须Coulex”认证已在原ID撤回；不是原件不存在这些结构，也不否认E0约束。新原读/精确scope见HW11-D25P-001–006；HW11-4既有needs_review:false保持。

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

- K. Heyde and J. L. Wood, *Reviews of Modern Physics* **83**, 1467–1521 (2011), DOI `10.1103/RevModPhys.83.1467`。
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/review/2011_Heyde_Wood_Shape coexistence in atomic nuclei.pdf`。
- 55-page RMP; theoretical approaches, systematic examples, spectroscopic fingerprints and outlook read.

## Scope and Reading Depth

- Full review read: shell-model/mean-field/IBM foundations; Z≈82, Z≈50, Z≈40/N≈60, Z≈64/N≈90, Z≈34/N≈40 and light nuclei; pairing/superdeformation; E0/E2/radii and 0+ states; global fingerprints and unsolved problems.
- Not covered: reanalysis of every cited isotope or post-2011 data.

本轮025是有界原件校准，并非重读55页：worker连续读PDF7–13/27–30/36–44（printed1473–1479/1493–1496/1502–1510），另读PDF1与背景段，视觉核相关17页；root读PDF1–3/13/36–41关键文本并视觉13/36/41的Eq14/fingerprints/TableVI。raw55页SHA `660c376e493e638501bfc8596d4eda46f490becb811ba5f30259d6f78c652183`相符。55页限定数值检索不冒充全文重读，综述举例不算本轮新primary；首页的2011-12-06 publisher-error correction字面保留，不猜其内容。

## Day24内Day25预习：定义、E0与证据量词校准

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HW11-D25P-001 | 摘要以不同electric quadrupole properties与proton/neutron pair分布的一组本征态描述核内结构共存；mean-field极小到实验谱还需相应恢复/混合。原文2011立场称low0+常与共存关联，同时在后文讨论seniority/振动等解释困难，不是普适iff定理。 | direct-review-definition-and-author-view | directly-read-review | PDF1 Abstract; PDF8/10 meanfield; PDF11 low0paragraph; PDF39–40 §III.C.3 | true |
| HW11-D25P-002 | §III.C.2区分direct/indirect/hints；diagonalE2与B(E2)为重要deformation信息，strongE0/particle-core patterns列indirect，radii/masses/transfer也提供线索。不是每例必须E0和multistepCoulex同时齐备；B(E2)单独也不分static/dynamic。 | direct-evidence-hierarchy | directly-read-review | PDF36–38 printed1502–1504 §III.C.2 | true |
| HW11-D25P-003 | Eq14在two-config前提给ρ²(E0)=Z²/R0⁴ a²(1−a²)[Δ⟨r²⟩]²，是混合与均方电荷半径差的组合；不能未声明density/shape模型就变成唯一β/γ。能隙另给V/δ组合，半径差输入/假定不能省去。 | direct-formula-and-labelled-inference | original-equation-plus-task-algebra | PDF13 printed1479 Eq14; PDF40 printed1506 | true |
| HW11-D25P-004 | 综述明确odd-Pb的i13/2同spin态E0、高K矩方法与highspinSD实例；PDF1506要求E0 mapping也含J≠0的ΔJ0，不能对所有odd/highspin结构强套同核0+清单。三轴/K混合转Q需另条件。 | direct-case-scope-with-review-lineage | directly-read-review-not-new-experiment | PDF13/Fig13; PDF27 Krdiscussion; PDF29–30 §III.A.8; PDF40 | true |
| HW11-D25P-005 | TableVI的Vmix跨多核/不同fit量约34–400keV，不是统一V门；186Pb0/532/650可定位，但旧28%/20–35%及其固定V归属未定位于所查本篇。Fig13 boxed28为αhindrance而非mixing百分比，未断它就是旧错来源。 | located-data-and-unlocated-attribution-correction | direct-original-plus-scoped-search-boundary | PDF12 Fig12; PDF13 Fig13; PDF41 TableVI; PDF42 TableVII | true |
| HW11-D25P-006 | E0的真实positive约束与无E0的非唯一解释均保：two-config半径公式中小ρ也可由mix/半径差/灵敏度导致，不能普适否定shape差别。综合三核companion须按具体pair/段选择，而非把综述例子计独立实验或普适排他门。 | explicitly-labelled-synthesis-and-quantifier-boundary | direct-premise-plus-task-inference | HW11-D25P-002 premises; PDF13 Eq14; PDF40 combined-observablesparagraph | true |
| HW11-D25P-007 | 在声明的同Iπ封闭二态块，radius T Hermitian作同U相似变换；offdiag t不零时E0幅另有相干项。trace/半径谱宽和commutator关系可检，但不由完整energy-basis H/T唯一识别物理unmixed配置；Eq14是同配置基T对角的子模型。此为本任务推导，非综述打印全式或186Pb新fit。 | declared-same-space-scalar-operator-extension | source-premise-plus-task-linear-algebra | PDF13 Eq14/two-configparagraph; task e0-two-state-029 | true |

Eq14的原文首先称E0 components为不同mean-square radii配置混合的“model-independent signature”，这一积极证据措辞保为作者观点。紧接式子却明确two configurations与a/√(1−a²)；在简单对角radius核及实两态H中，η=a²、observedgap D给η(1−η)=V²/D²，因此E0与D仍只约束abs[V Δ⟨r²⟩]的组合，不能分别唯一识别mix/radius/β/γ。off-diagonal E0或多配置需额外振幅，未由本篇一式消除。

本次withdrawal-audit-025只撤回源归属与过强认证，不声称旧百分比在任何其它文献物理上不可能。既有HW11-4的reviewflag不变；其meanfield-to-lab命题仍限于该建模路线，不把所有shell-model实现强制另作GCM。更新接入[[triaxial-shape-coexistence]]与[[chirality-shape-coexistence-companion-matrix]]，Day25无学分。

## Key Results

- Shape coexistence is simultaneous low-lying states with different quadrupole/electromagnetic structures, often driven by shell gaps versus proton-neutron correlation energy and multi-particle–multi-hole excitations.
- Spherical shell-model and self-consistent mean-field approaches are complementary; symmetry restoration and configuration mixing are required to turn intrinsic minima into laboratory spectra.
- Spectroscopic fingerprints include low-lying excited 0+ states, E0 transition strength, contrasting B(E2)/quadrupole moments, isotope inversions and shape-dependent radii; no single observable suffices.
- Coexistence appears across light, medium and heavy nuclei, including superdeformation and pairing isomers, but universality and predictive parameter control remain open.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HW11-1 | Shape coexistence requires distinct low-lying configurations/collective structures, not merely a single triaxial or vibrational band. | review-framework | direct | PDF Secs.I–III | true |
| HW11-2 | Shell gaps/monopole evolution oppose proton-neutron correlation and pairing energies, producing intruder configurations and shape inversions. | model-framework | direct | PDF Sec.II, Eqs.1–5 | true |
| HW11-3 | The review organizes E2, E0, radii, energies, transfer and configuration-dependent spectroscopy as complementary direct/indirect/hint routes; the appropriate combination depends on the actual states and question, not a universal all-observables requirement. | experimental-framework | direct-to-review | PDF Sec.III.C and Sec.III | true |
| HW11-4 | Symmetry restoration/configuration mixing are essential for quantitative coexistence spectra; mean-field minima alone are insufficient. | limitation | direct | PDF Sec.II.B–C | false |

## Summary

Heyde & Wood provide the major evidence and theory map for shape coexistence, emphasizing competition between shell structure and correlations and the need for multiple electromagnetic/structural observables.

## Competing Interpretations and Limitations

Low-lying 0+ states, E0 strengths or B(E2) changes can also arise from pairing, vibrational, intruder or configuration-mixing effects; model-space choices and symmetry restoration determine quantitative interpretation. Review-level isotope examples are not independent sources.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| HW11-AR-1 | Evidence chain | shell gap/correlation → competing configurations/minima → projection/mixing → E0/E2/radii/spectrum. | PDF Secs.II–III | self-checking |
| HW11-AR-2 | Transfer condition | Choose state- and problem-specific E0/E2/radius/configuration evidence; do not impose a 0+ or a fixed instrument list on every odd-mass/high-spin case. | PDF Sec.III | active-L3 |
| HW11-AR-3 | Independence | Review; all cited nuclei/data remain upstream sources. | Scope/Refs. | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` shape-coexistence evidence map and clarifies its separation from octupole/triaxial/wobbling labels.
- Persistence: link to [[triaxial-shape-coexistence]], [[a130-high-spin-collective-modes-evidence-map]] and shape/octupole concepts.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `HW11-P0-1`: do not infer shape coexistence from a single low-lying 0+ or band; retain problem-specific complementary E0/E2/radius/configuration evidence and avoid universal instrument requirements.

## Extracted Pages

- Concepts: [[triaxial-shape-coexistence]], [[octupole-deformation]]。
- Projects: [[a130-high-spin-collective-modes-evidence-map]]。
## Day21周考推断阶梯审计：形状共存、E0单极跃迁与多态混合推断边界

依据独立审计程序 `system/scripts/day21_checkpoint009_shape_coexistence_e0_audit.py` 与审计产物 `outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/shape-coexistence-e0-audit-009.json`，确立本源在推断阶梯上的边界：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| HW11-D21-1 | Day24内025原件复核撤回旧认证：186Pb的28%/20–35%混合百分比与固定V50–100keV普适强门未找到本篇对应支撑；E0排他唯一反演及必须E0+Coulex量词不成立。原行完整保存在withdrawal-audit-025.json；186Pb0/532/650能级本身可定位，不与未得百分比一并否定。用HW11-D25P-001–006的原件分层。 | withdrawn-unlocated-attribution-and-overclaim | corrected-with-direct-original-boundary | PDF13 Eq14; PDF36–41 §III.C/TableVI; task withdrawal-audit-025 | true |
