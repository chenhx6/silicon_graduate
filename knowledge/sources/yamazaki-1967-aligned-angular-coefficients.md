---
type: source
title: "Yamazaki 1967 - Tables of coefficients for angular distributions from aligned nuclei"
aliases: [Yamazaki 1967 angular-distribution tables]
created: 2026-09-21
updated: 2026-10-16
status: ai-draft
review_status: unreviewed
source_type: reference-tables
reading_depth: deep-read
title_original: "Tables of Coefficients for Angular Distribution of Gamma Rays from Aligned Nuclei"
authors: [T. Yamazaki]
journal: "Nuclear Data, Section A"
year: 1967
citation_key: yamazaki_1967_Tables
volume: 3
pages: "1-23"
doi: 10.1016/S0550-306X(67)80002-8
canonical_source: "Yamazaki, Nuclear Data A 3 (1967)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/ADO/1967_Yamazaki_Tables of coefficients for angular distribution of gamma rays from aligned.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/ADO/1967_Yamazaki_Tables of coefficients for angular distribution of gamma rays from aligned.pdf"
raw_sha256: "e807782c580a0313ee3763f56df1dd424e5c97925d70e3d30a79a8b534c81f70"
nuclei: [generic]
reactions: [particle-xn-alignment]
experiments: [gamma-angular-distribution]
models: [statistical-tensor, gaussian-magnetic-substate-alignment]
observables: [A2, A4, A6, angular-distribution, mixing-ratio, attenuation]
methods: [angular-distribution, ADO, reference-tables]
tags: [aligned-nuclei, angular-distribution, high-spin, tables]
---

# Tables of coefficients for angular distributions from aligned nuclei

## Bibliographic Record

- T. Yamazaki, *Nuclear Data, Section A* **3** (1967), pp.1–23.

## Scope and Reading Depth

- The 23-page scan was read end-to-end: introduction, Eqs.(1–15), Figs.1–3, references, Table I and the integral- and half-integral-spin Table II coefficient pages. The dense scanned tables were checked visually on the page images; they are tabulations, not a new experiment.

## Core Method

The paper starts from statistical-tensor populations `p_k(J)` of an aligned state. For a mixed `L1/L2` transition it writes

`W(θ)=1+A2 P2(cosθ)+A4 P4(cosθ)`,

with `A_k` built from alignment tensors and `F_k` Racah/Clebsch–Gordan coefficients (PDF pp.1–3, Eqs.1–5). Complete-alignment tensors `B_k(J)` are tabulated for integer and half-integer spin (Table I). Partial alignment is represented by attenuation `α_k(J)=p_k(J)/B_k(J)` and `A_k=α_k A_k^max` (p.2, Eqs.9–10).

The practical one-parameter approximation is a Gaussian magnetic-substate population, `P_m∝exp[-m²/(2σ²)]`. The figures show that `α4` falls rapidly with `α2` and `α6` is usually negligible; therefore `σ/J` or `α2` can often parameterize the alignment only after the reaction mechanism is justified (pp.2–3, Figs.2–3). For a preceding transition `Ji→Jf`, the state tensor propagates through `U_k(Ji L1 L2 Jf)` and the previous alignment, making cascade feeding explicit (p.3, Eqs.12–15).

## Key Results

- Table IIa gives `F_k`, `B_kF_k` and `U_k` functions for integral spins; Table IIb supplies the corresponding half-integral-spin entries through the tabulated spin ranges (pp.7–23).
- The paper explicitly warns that the sign of `δ` inferred from a single-transition angular distribution is opposite to the sign from the corresponding `Ji→Jf→J` γ–γ correlation under its stated ordering (p.2). This is a convention mapping, not a physical sign reversal.
- The Gaussian population follows the heavy-ion “random walk” alignment picture and is a useful approximation, not a universal prior; non-Gaussian feeding and side-feeding must be tested against the measured coefficients.
- Angular distributions alone constrain combinations of spin sequence, alignment and multipole mixing; the tables do not replace polarization, DCO, lifetime or level-scheme evidence.

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| YA67-1 | `B_k`, `F_k` and `U_k` tables provide aligned-state angular-distribution coefficients for integer and half-integer spins. | method-result | direct | PDF pp.1–3, 7–23, Eqs.1–15, Tables I–II | true |
| YA67-2 | Gaussian attenuation connects measured `A_k` to `σ/J`, but this is a feeding/alignment model assumption. | method-boundary | direct | PDF pp.2–3, Figs.2–3 | true |
| YA67-3 | δ signs require an explicit angular-distribution versus γγ-correlation convention map. | convention-boundary | direct | PDF p.2 | true |
| YA67-4 | 对只经该preceding transition形成的daughter，Eq12为p_k(Jf)=U_k p_k(Ji)；α=p/B使Eq15另有B_k(Ji)/B_k(Jf)。U不能不加该比率直接乘α；rank不存在或B=0时不能作该除法。 | tensor-versus-attenuation-transfer | direct-and-derived | printed p.3 Eqs.(12),(15); printed p.2 Eq.(10) | true |
| YA67-5 | Eq13的未观测preceding emission混合U=(u_L1+δ²u_L2)/(1+δ²)，没有Eq3辐射角系数的2δ干涉项；不测该γ方向/偏振是当前传递核条件，不能直接替已选γ gate的conditional response。 | unobserved-transfer-and-domain | direct-and-derived | printed p.3 Eq.(13); printed p.2 Eq.(3) | true |
| YA67-6 | 本文B_k是completealignmenttensor；Ionescu1981的同名B_k是radiation geometric combination。even-rank normalized p与IO的ρ可按Eq1/IOEq5映射，但不能按B同字母互换；finiteδ的相位约定仍保留。 | cross-source-symbol-map | direct-and-derived | printed p.1 Eq.(1); printed p.2 Eqs.(3),(6); IO81 printed22 Eqs.(3)–(5) | true |
| YA67-7 | TableIIa 2→2 pureE2给U2=−.21429、U4=.28571；正文说α可变负。本任务CG²正、列归一kernel给exact U2=−3/14、U4=2/7及合法daughter概率；负tensor不是负概率。 | source-table-and-derived-positivity-check | direct-and-derived | printed p.3 paragraph below Eq.(15); printed p.7 TableIIa Ji2 Jf2 L1=L2=2 | true |
| YA67-8 | TableIIa 2→0 pureE2中daughter U2/U4为0，但completealignment radiation A2max=.71429、A4max=−1.71429非零。daughtertensor rank与photon角分布rank是不同对象，不能将2Jf普遍作为singleγ radiation上限。 | observable-identity-and-derived-rank-check | direct-and-derived | printed p.7 TableIIa Ji2 Jf0 L1=L2=2 | true |
| YA67-9 | TableIIb的17/2→13/2 pureE2行给U2=.95294/U4=.84744。本任务计算.952936638/.847443971与五位舍入相容；给IO81 271支的条件tensor传递只是一条支的normalized component，不是全daughterfeeding拟合。 | table-crosscheck-and-application-boundary | direct-and-derived | printed p.19 TableIIb Ji17/2 Jf13/2 L1=L2=2 | true |
| YA67-10 | p19的17/2→13/2 L2行F2/F4=−.37757/−.16697，p18的13/2→9/2 L2行为−.39621/−.19702；乘IO81相应ρ2/4与其A2/4在印刷精度相容。此为符号/归一cross-check，不是独立新测量或完整角数据重拟合。 | radiation-coefficient-and-source-convention-crosscheck | direct-and-derived | printed19 TableIIb Ji17/2 Jf13/2; printed18 TableIIb Ji13/2 Jf9/2 | true |
| YA67-11 | TableIIb p18的15/2→13/2 pureL1给U2=.97321、U4=.91069，pureL2给.86752/.58103；本任务CG²计算与五位舍入相容，供IO81 218.90支的source-conditioned参考，不作实测alignment。 | source-table-second-feeder-transfer | direct-and-derived | printed18 TableIIb Ji15/2 Jf13/2 pureL1/pureL2 | true |
| YA67-12 | 在IO81 Table3正确spin解的arctanδ=.2°±2°端点区间内，按Eq13的radiative E1/M2 U变化在U2<.0002、U4<.0006；δ0仅参考，未认证conversion-weighted总转移或给该区间统计覆盖。 | radiative-mixing-sensitivity-and-domain | derived | printed3 Eq.(13); printed18 TableIIb; IO81 printed22 Table3 row218.90 | true |

## Summary

Yamazaki's tables provide the tensor and attenuation backbone for aligned-state angular-distribution analyses, with the useful warning that alignment and sign conventions are part of the measurement identity.

## Competing Interpretations and Limitations

- Gaussian magnetic-substate populations and single-parameter alignment may fail for non-Gaussian or strongly side-fed states.
- A table coefficient is not a detector-independent measured coefficient and cannot alone resolve spin, alignment and δ.

## Analytical Reconstruction and Self-Audit

| ID | Audit item | Agent judgment | Locator | Status |
|---|---|---|---|---|
| YA67-AR-1 | Tensor chain | Population/statistical tensor → `F_k` angular coefficients → attenuation → measured `A_k`. | PDF pp.1–3, Eqs.1–15 | self-checking |
| YA67-AR-2 | Alignment identifiability | Treating `σ/J` or `α2` as one free parameter is a Gaussian-model choice; higher tensors can carry information when statistics permit. | PDF pp.2–3, Figs.2–3 | self-checking |
| YA67-AR-3 | Convention safety | Map state order, operator phase and angular-distribution versus γ–γ correlation before transferring a δ sign. | PDF p.2 | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[angular-distribution]], [[angular-momentum-alignment]], [[angular-correlation]] and the later Der-Mateosian–Sunyar coefficient tables.
- Reusable rule: keep complete-alignment coefficients, attenuation factors and detector/feeding corrections as separate evidence layers; do not quote a table entry as an experiment-specific `A2/A4`.
- Review state: Codex self-audited; not `human-reviewed`.

## Day14定向回读：U、p与α的层级

[DOI](https://doi.org/10.1016/S0550-306X(67)80002-8)经Crossref核题名/作者/3(1),1–23(1967)，与原扫描刊头一致。原件23页、1103765 bytes、source SHA256不变。本轮作为Ionescu1981完整anchor的必要companion，回读全部定义主线pp1–3和p4 refs，视觉核p2/3及p7/19相关表行；未重新逐格认证全部17页TableII或原CDC6600程序。原source已有end-to-end阅读记录保留，新数值核仅14条选定pure rows。

### 先固定传递对象

Eq12的p是normalized statistical tensor；Eq10定义α_k=p_k/B_k，Eq6的B_k是相应spin的completealignment tensor。因此：

`p_child=U_k p_parent`，`α_child=U_k [B_parent/B_child] α_parent`。

后一个因子通常不同于U。低spin不存在的rank以及零B须另处理；不能把数组里的零当作可除的normalization。与[[ionescu-1981-improved-angular-distribution-analysis-particle-xn]]交叉时，其B_k是辐射几何组合，对应本书Eq3由F组成且包含1/(1+δ²)的完整辐射因子，而非本书Eq6的B；混合比约定仍须核。两式以同一归一/CG顺序映射even-rank p/ρ，不能据同字母猜。

IO81 Eq11的U以target、parent参数命名，本书Eq12写preceding parent Ji→child Jf；实际代码先明确物理流向。Eq13对未观测precedingγ使用L1/L2的强度加权，δ正负不影响该U；辐射角分布本身的Eq3仍有干涉项。选择了γ方向/偏振/finite gate时须用对应conditional kernel，不能把此未观测核直接套回DCO/ADO。

### 14条原表U行与独立CG²构造

`K(Mf,Mi)=|CG(Jf Mf,L (Mi−Mf)|Ji Mi)|²`，对precedingγ的模式不作选择。每个Mi列之和为1、全部非负；由本书Eq1计算daughtertensor，再验证每个parent-Mi给同一rank比例。Racah有限和用有理数算CG²，独立于照抄U列。

| 表位 | Ji→Jf | pure L | U2 printed | U4 printed |
| --- | --- | --- | --- | --- |
| p7 IIa | 1→1 | 1 | -0.50000 | 0.00000 |
| p7 IIa | 1→1 | 2 | 0.10000 | 0.00000 |
| p7 IIa | 1→2 | 1 | 0.59161 | 0.00000 |
| p7 IIa | 1→2 | 2 | -0.59161 | 0.00000 |
| p7 IIa | 2→1 | 1 | 0.59161 | 0.00000 |
| p7 IIa | 2→1 | 2 | -0.59161 | 0.00000 |
| p7 IIa | 2→2 | 1 | 0.50000 | -0.66667 |
| p7 IIa | 2→2 | 2 | -0.21429 | 0.28571 |
| p7 IIa | 2→3 | 1 | 0.82808 | 0.41786 |
| p7 IIa | 2→3 | 2 | 0.20702 | -0.62678 |
| p7 IIa | 3→2 | 1 | 0.82808 | 0.41786 |
| p7 IIa | 3→3 | 1 | 0.75000 | 0.16667 |
| p7 IIa | 3→3 | 2 | 0.31667 | -0.50000 |
| p19 IIb | 8.5→6.5 | 2 | 0.95294 | 0.84744 |

49项控制通过，14行的U2/U4都与五位舍入相容；这不是全表/原始code认证。2→2 E2且parent仅M0的演示给daughter M=−2…2概率`(2/7,1/14,2/7,1/14,2/7)`，exact U2=−3/14、U4=2/7。合法population仍可有负tensor/α；Gaussian parent不保证该daughter仍是同一Gaussian family。

2→0 E2的daughter只有M0，所有高ranktensor消失；photon仍有`W=1+(5/7)P2−(12/7)P4=(15/2)sin²θ cos²θ`。这区分了看daughter alignment与看photon angular pattern，不能混用rank上限。

### 167Tm一支的条件传递

本书p19的half-integer行对应IO81 Fig5的271.12-keV、17/2→13/2 pureE2支。计算U2=.952936638、U4=.847443971；α因子分别.955882353/.856753813，确实不同。输入IO81 Table1 parentρ2=−.705、ρ4=.443时，该支单独条件分布的tensor为−.67182033/.37541768。它尚未乘实际I0/IT，更不是总childρ；同目标的其他feeding、分支、门和共同Σ仍缺。

仅固定U时可把parent quoted errors按|U|缩放；跨rank covariance还要乘U2U4，原Cov未知，未生成新CI或重拟σ/δ。这些是源公式的条件应用，不把理论transfer变成新实测child。

### 原始伴随文献边界

IO81 Ref14的精确DOI metadata核为Poletti–Warburton，*Study of the Low-Lying Levels of F18 by Means of the O16(He3,pγ)F18 Reaction*, PhysRev137,B595–B619(1965)。尚未读其原25页/内部U定义，不能称已核原代码或完整约定；本轮直接定义来自本书原件。[[ionescu-1981-improved-angular-distribution-analysis-particle-xn]]保留其λmax字面和适用范围，未修式或判其167Tm结果失效。

[49-check程序](../../system/scripts/day14_unobserved_feeding_transfer.py)、[输入](../../outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/yamazaki1967-U-table-input.json)和[结果](../../outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/yamazaki1967-U-transfer-audit.json)保留normalization、表值、exact正概率控制和partial应用。Day15只作无学分preview；全部新YA67 claims true，原review不升级。

## Human Review Triage

### P0

- `YA67-P0-1`: Preserve the δ sign/state-order warning and the Gaussian-alignment assumption before using the tables for spin or mixing-ratio assignments.

## Extracted Pages

- Methods: [[angular-distribution]], [[angular-correlation]], [[angular-momentum-alignment]]。

## 167Tm原报ρ与radiation F的定向cross-check

YA67-10给两个pureL2行：17/2→13/2的(F2,F4)=(−.37757,−.16697)，13/2→9/2为(−.39621,−.19702)。与[[ionescu-1981-improved-angular-distribution-analysis-particle-xn]] Table1的parent/targetρ相乘，分别复原约(.266,−.074)/(.248,−.013)的A；这只验证当前使用的符号与归一，不把derivedρ与原A当两组独立证据。目标正population矩域还可用于条件feeding份额的可行性设计，详见IO81-24–26；未给实测branch、Cov或微观feeding结构。

## 第二已知馈入的U与small-M2范围

YA67-11补p18两条pure-mode：Ji15/2→Jf13/2的L1为(.97321,.91069)，L2为(.86752,.58103)。[[ionescu-1981-improved-angular-distribution-analysis-particle-xn]] IO81-30将它们用于218.90 E1/M2的显式pureE1参考；上一级ρ来自318.135 pureE2原表行，未用E1自身反推parent取向。

在arctanδ=.2°±2°的无覆盖声明端点范围，radiativeU的名义变化小于.0002/.0006。此处δ=M2/E1辐射振幅，不是E2/M1；符号在未观测核中平方消去。small-M2并不替代完整rate/内转换合同；[[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] KB08-2给αeff的率权重。本轮未提供actualICC或认证converted-total核，pureE1控制与mixed sensitivity分别记录，不生成新实测ρ/σ/δ。
