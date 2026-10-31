---
type: source
title: "Bucher et al. 2016 - Direct evidence of octupole deformation in neutron-rich 144Ba"
aliases: [Bucher 2016 144Ba E3]
created: 2026-09-21
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Direct Evidence of Octupole Deformation in Neutron-Rich 144Ba"
authors: [B. Bucher, S. Zhu, C. Y. Wu, R. V. F. Janssens, D. Cline, A. B. Hayes, M. Albers, A. D. Ayangeakaa, P. A. Butler, C. M. Campbell, M. P. Carpenter, C. J. Chiara, J. A. Clark, H. L. Crawford, M. Cromaz, H. M. David, C. Dickerson, E. T. Gregor, J. Harker, C. R. Hoffman, B. P. Kay, F. G. Kondev, A. Korichi, T. Lauritsen, A. O. Macchiavelli, R. C. Pardo, A. Richard, M. A. Riley, G. Savard, M. Scheck, D. Seweryniak, M. K. Smith, R. Vondrasek, A. Wiens]
journal: "Physical Review Letters"
year: 2016
volume: 116
pages: "112503"
doi: "10.1103/PhysRevLett.116.112503"
citation_key: Bucher_2016
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "https://doi.org/10.1103/PhysRevLett.116.112503"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/形变/2016_Bucher et al_Direct Evidence of Octupole Deformation in Neutron-Rich Ba 144.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/形变/2016_Bucher et al_Direct Evidence of Octupole Deformation in Neutron-Rich Ba 144.pdf"
raw_sha256: "f0da6d0a56cd10d1023633aed1a25d021f88a0ff48787c4569a26031e1b3dc4d"
nuclei: [144Ba, 144La, 208Pb, 134Xe]
reactions: [sub-barrier-coulomb-excitation]
experiments: [ATLAS, CHICO2, GRETINA]
models: [GOSIA, rigid-rotor, octupole-deformation]
observables: [B(E3), Q3, beta3, Coulomb-excitation-yield]
methods: [coulomb-excitation, gamma-ray-tracking, particle-gamma-coincidence]
tags: [144Ba, octupole, E3, radioactive-beam, Coulomb-excitation]
---

# Direct evidence of octupole deformation in neutron-rich `144Ba`

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

- B. Bucher *et al.*, *Phys. Rev. Lett.* **116**, 112503 (2016), DOI `10.1103/PhysRevLett.116.112503`.

## Scope and Reading Depth

- All five PRL pages were read, including CHICO2/GRETINA setup, contaminant rejection, GOSIA fit, Fig.1–2, Table I, lifetime discussion, shape conversion, model comparison and conclusion.

## Experiment and Evidence Chain

Post-accelerated `650 MeV 144Ba` was Coulomb excited on a `1.0 mg/cm² 208Pb` target below the barrier. CHICO2 measured charged-particle trajectories and separated beam contaminants; GRETINA tracked γ rays with event-by-event Doppler correction (PDF pp.1–3, Fig.1). The radioactive intensity was about `8×10³ ions/s`; E1 yields used `30°–40°` and E2 yields `40°–75°` laboratory ranges.

GOSIA varied E1/E2/E3 matrix elements, with 70 elements for states up to `14+`/`15−`; rigid-rotor coupling reduced the free parameters and existing lifetimes/branching ratios constrained E2/E1 values (pp.3–4, Fig.2). The independent `134Xe` `4+→2+ / 2+→0+` yield check gives calculated `0.077` versus measured `0.078(4)` (p.3).

The central result is `⟨3−‖M(E3)‖0+⟩=0.65^{+0.17}_{−0.23} eb^{3/2}`, or `B(E3;3−→0+)=48^{+25}_{−34} W.u.` (Table I, p.4). The fitted intrinsic octupole moment is `Q3=1.73^{+0.45}_{−0.62}×10³ efm³`; with `β2=0.18` the inferred `β3=0.17^{+0.04}_{−0.06}` (p.4). Upper limits only are obtained for `2+→5−` and `4+→7−` E3 links. The E1/E3 relative sign is an assumption; changing it shifts the main E3 element by about 10% (p.4).

## Interpretation and Limitations

The measured E3 strength exceeds the cited beyond-mean-field/IBM predictions (largest cited `~20–24 W.u.`) and is presented as direct evidence for strong octupole correlations consistent with an octupole shape. The error analysis releases the rigid-rotor constraint, but the `β3` conversion neglects higher multipoles; varying `β4=0–0.20` changes `β3` by less than 10% (p.4). This is a direct E3 observable, not merely an E1/parity-doublet or model-PES inference.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BU16-1 | `144Ba` sub-barrier Coulomb excitation yields `B(E3)=48^{+25}_{−34} W.u.`. | experiment-result | direct | PDF pp.3–4, Table I | true |
| BU16-2 | The fitted `Q3` and inferred `β3` support strong octupole correlations, with conversion assumptions retained. | model-linked-observable | mixed | PDF p.4 | true |
| BU16-3 | CHICO2/GRETINA contaminant handling and `134Xe` control support the GOSIA yield chain. | method-result | direct | PDF pp.2–3, Figs.1–2 | true |

## Summary

Bucher *et al.* provide a direct E3 benchmark that is materially stronger than relative E1/parity-doublet indicators, while preserving the shape-conversion boundary.

## Competing Interpretations and Limitations

- Rigid-rotor relations, E1/E3 relative sign and higher multipoles enter the conversion from matrix element to `β3`.
- Several E3 links are only upper limits and contaminant peaks require coupled-yield treatment.

## Analytical Reconstruction and Self-Audit

| ID | Audit item | Agent judgment | Locator | Status |
|---|---|---|---|---|
| BU16-AR-1 | Yield-to-E3 chain | Particle gate/Doppler-corrected γ yields → GOSIA matrix elements → `B(E3)`/`Q3`; the `134Xe` control supports the response. | PDF pp.2–4, Fig.2, Table I | self-checking |
| BU16-AR-2 | Model independence | Releasing rotor constraints in the error analysis and the large E3 signal support direct evidence, while the β3 conversion remains shape-model dependent. | PDF pp.3–4 | self-checking |
| BU16-AR-3 | Contamination boundary | `134Xe`, charge-state contaminants and unresolved `5−→4+`/`8−→6+` peaks are explicitly handled; only upper limits follow for some E3 links. | PDF pp.2–4 | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[octupole-deformation]], [[octupole-correlation]], [[octupole-softness]], [[coulomb-excitation]] and the direct-observable tier of the A≈130/144Ba evidence map; it complements HS-028 `220Rn/224Ra`.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `BU16-P0-1`: Preserve the E3 matrix element and its uncertainty separately from the inferred `β3` and static-shape claim; retain E1-sign, rotor, higher-multipole and contaminant boundaries.

## Extracted Pages

- Nucleus/method: `144Ba`, [[coulomb-excitation]], [[octupole-deformation]], [[octupole-correlation]]。

## Day19量化审计：直接B(E3)与Q3测量、内禀电八极矩与形变反演

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_ba144_ba146_octupole_e1_audit.py` 的 9 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/ba144-ba146-octupole-e1-result-046.json`，系统核准了 Bucher 2016（PRL 116, 112503）关于 $^{144}\text{Ba}$ 直接八极库仑激发的量化事实：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| BU16-D19-1 | Bucher 2016 在 ATLAS 装置上利用 $650\text{ MeV}$ 的 $^{144}\text{Ba}$ 放射性束流轰击 $^{208}\text{Pb}$ 靶进行垒下库仑激发，通过 CHICO2 粒子径迹与 GRETINA $\gamma$ 射线追踪联合分析，直接测定基态跃迁八极矩阵元 $\langle 3^- \Vert \mathcal{M}(E3) \Vert 0^+ \rangle = 0.65_{-0.23}^{+0.17}\ e\text{b}^{3/2}$，对应跃迁几率 $B(E3; 3^- \to 0^+) = 48_{-34}^{+25}\text{ W.u.}$；结合转子模型反演得到内禀电八极矩 $Q_3 = (1.73_{-0.62}^{+0.45}) \times 10^3\ e\text{fm}^3$ 以及八极形变参数 $\beta_3 = 0.17_{-0.06}^{+0.04}$（固定 $\beta_2 = 0.18$）。该测量摆脱了依赖带间 $E1$ 跃迁间接推导八极形变的传统唯象方法，首次在富中子钡同位素中确立了微观八极集体性存在的确定性实验证据。 | quantitative-benchmark-and-criterion | direct-and-derived | PRL 116, 112503 pp.1-4; Table I, Fig.2; ba144-ba146-octupole-e1-result-046.json | true |
## Day21周考推断阶梯审计：八极跃迁集体性与静态八极形变边界

依据独立审计程序 `system/scripts/day21_checkpoint006_octupole_ba_audit.py` 与审计产物 `outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/octupole-ba-audit-006.json`，确立本源在推断阶梯上的边界：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| BU16-D21-1 | Bucher 2016 在 $^{144}\text{Ba}$ 中直接测定的基态跃迁矩阵元 $\langle 3^- \Vert M(E3) \Vert 0^+ \rangle = 0.65_{-0.23}^{+0.17}\ e\text{b}^{3/2}$（$B(E3) = 48_{-34}^{+25}\text{ W.u.}$）确证了强的八极跃迁集体性（对应方均根振幅 $\sqrt{\langle \beta_3^2 \rangle} \approx 0.17$），但不能排他性认证为静态梨形形变；其实测交错宇称带在低自旋存在高达 $\Delta E(1^-) = +659.1\text{ keV}$ 的声子偏移（对比 $^{224}\text{Ra}$ 的 $173.8\text{ keV} \to 0$），激发态 $2^+ \to 5^-$ 与 $4^+ \to 7^-$ 仅得上界（$<1.2$ 与 $<1.6\ e\text{b}^{3/2}$），且微观势能面势垒（$<0.5-1.0\text{ MeV}$）低于八极零点振动能量（$\sim 1.0-1.5\text{ MeV}$），表明体系呈现强八极柔软动态涨落。 | claim-boundary-audit | direct-and-derived | PRL 116, 112503 pp.3-4, Table I; octupole-ba-audit-006.json | true |
## Day25内Day26无学分preview：直接八极与E1灵敏度边界核查

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| BU16-D25P-A005-01 | ATLAS CARIBU 垒下库仑激发直接测定 $^{144}\text{Ba}$ 的 $B(E3; 3^- \to 0^+) = 48_{-34}^{+25}\text{ W.u.}$，转子模型换算内禀 $Q_3 = (1.73_{-0.62}^{+0.45}) \times 10^3\ e\text{fm}^3$。本次库仑激发截面对一阶 $E1$ 弱敏感，表列 $E1$ 矩阵元主要受既有寿命与分支比先验约束，前角区不可视作 $E1$ 独立高灵敏度直接测量。 | direct-octupole-and-e1-sensitivity-boundary | direct-original | PRL 116, 112503 pp.3-4 | true |

## Day26：E3方向、误差与形状推断

本次回读PDF1–5，原raw/SHA不变。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| BU16-D26-001 | 原文给0+↔3−幅度0.65(+0.17/−0.23) e b^(3/2)，向下B=48(+25/−34) W.u.；反向B需按初态简并因子换算，0+→3−为3−→0+的7倍。 | direct-report-and-definition | direct-original-plus-unit-algebra | printed112503-1/4 Table I | true |
| BU16-D26-002 | E1/E3相反相对符号会使目标E3幅度约降低10%，作者说在报告误差内；这不等于新独立相位测量或概率分布。误差分析释放rigid-rotor约束并纳入矩阵元相关，但未提供本任务可重放的完整联合likelihood。 | fit-and-uncertainty-boundary | direct-original | printed112503-3/4 | true |
| BU16-D26-003 | Q3、β3转换需转子/轴对称及高阶形变约定。宽E3区间与146Ba相容不证明严格等强，也不以单一跃迁独立给刚性与软性裁决。BE16的投影GCM提供具体模型比较而非新增实验。 | inference-boundary | direct-original-and-limited-synthesis | printed112503-4; BE16-D26-004/007/008 | true |

`supports` 直接电磁八极集体性；`limits` 精确静态形状与区间相交的过强解释；关联 [[bernard-2016-144ba-sccm-octupole]] 与 [[octupole-mr-amr-evidence-gradient]]。打印值的舍入/一阶误差传播练习不冒称重新测量或新CI。
详见微观相消与势能面分析专页：[[ba-microscopic-octupole-dipole-cancellation]]。
