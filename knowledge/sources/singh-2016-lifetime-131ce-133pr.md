---
type: source
title: "Lifetime measurements in the yrast band of the gamma-soft nuclei 131Ce and 133Pr"
aliases: [Singh 2016 131Ce lifetime, Singh 2016 133Pr lifetime]
created: 2026-07-28
updated: 2026-10-26
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Lifetime measurements in the yrast band of the gamma-soft nuclei 131Ce and 133Pr"
authors: [R. P. Singh, P. Joshi, S. K. Chamoli, S. Muralithar, G. Mukherjee, R. K. Bhowmik, S. C. Pancholi]
journal: Pramana - Journal of Physics
year: 2016
volume: 87
pages: 7
doi: 10.1007/s12043-016-1218-6
language: en
canonical_source: doi:10.1007/s12043-016-1218-6
citation_key: singh_2016_Lifetimemeasurements
raw_file: "raw/papers/2016_Singh et al_Lifetime measurements in the yrast band of the gamma-soft nuclei 131Ce and 133Pr.pdf"
raw_sha256: 95E0831B9864A58FD1A896A1B20E227D88D9B7AA5DE56C738C3792441CAA1A30
nuclei: [131ce, 133pr]
reactions: [119Sn(16O,4n)131Ce, 118Sn(19F,4n)133Pr]
experiments: [iuac-gda-131ce-o16-rdds-dsam, iuac-gda-133pr-f19-rdds]
models: [cranked-hartree-fock-bogoliubov, total-routhian-surface]
observables: [transition-quadrupole-moment]
methods: [recoil-distance-doppler-shift, doppler-shift-attenuation-method]
tags: [131ce, lifetime, qt, gamma-soft, dsam, rdds]
---

# Singh 等（2016）：`131Ce/133Pr` yrast 带寿命

## Day20正式原读更正与当前证据入口

本轮实际读11页全文（含references）并视觉核PDF3–10的12图、2表、5式；不是沿旧hash继承原读。阅读scope与原表ledger见本日run-02的source-reading-scope-001.json/singh-table-ledger-001.json。旧review_status及全部原claim flags保持。SI16-D18-2/3/4与SI16-D20-4已在原ID下明示纠正；旧result JSON保持原字节，不作为科学认证。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SI16-D20-F01 | Table1当前27/2−、827keV的mean寿命是1.25(+.41/−.25)ps，Qt=2.26(+.37/−.23)eb；旧1.24(+.23/−.13)不是此表。Ref32列的1.23(23)ps是转载旧寿命，不是新增测量。 | literal-table-correction | direct-original-and-visual | PDF5 Table 1 | true |
| SI16-D20-F02 | Table2侧馈列按15/2−、19/2−、23/2−给1.1(2)ns、1.9(2)ps、14(3)ps。14ps与正文由正宇称23/2+态14.0(+2.7/−3.3)ps约束的682keV馈入相符；0.014ps、单调下降与跨5数量级均撤回。1100/14≈78.57只为中心比，不测定feeding偏差。 | feeding-unit-and-role-correction | direct-original-and-visual | PDF8 Table 2 | true |
| SI16-D20-F03 | 对Present有限Qt点、上下误差平均且独立Gaussian控制，131Ce斜率−.030175±.047215eb/ℏ、z−.63910；133Pr−.116674±.048608、z−2.40034。若额外估计共同未知尺度并以χ²/dof缩放，分别t−.60202(df2)、−1.67818(df1)，双尾Student概率约.6083/.3421。旧−1.68不是前一种Gaussian模型；未得原Cov/limits likelihood，所有结果仅条件诊断，不能选取有利统计量当原实验CI。 | explicit-statistical-model-comparison | task-derived | PDF5 Table 1; PDF8 Table 2 | true |
| SI16-D20-F04 | 131Ce低自旋plunger使用本工作高自旋DSAM矩约束Bateman拟合；并非所有技术点相互独立。DSAM谱由下方510/642/750keV门之和构成，作者报告两停止方案结果取平均、误差取较大值，并设寿命最小10%误差；这不是发表完整跨点Cov。 | joint-analysis-dependency | direct-original | PDF3 data analysis; PDF4 DSAM analysis; PDF5 error paragraph | true |
| SI16-D20-F05 | 本文Eq4明确采用R=1.2A^(1/3)fm与β2(1+.36β2)，假设prolate且无hexadecapole；Eq5 Qt=Q20 cos(γ+30°)/cos30°另需转轴/γ约定。γ=−80°是借TRS的输入再与Qt相容性检查，不能从一个Qt独立量出β、γ或γ刚性。 | formula-and-inverse-problem-boundary | direct-original-and-visual | PDF9 Eq. (4); PDF9 Eq. (5) | true |
| SI16-D20-F06 | Figure5包含本工作circles与旧Refs31/32的star/diamond，不得把所有图点作新独立样本；131Ce23/2−表只列τ>1.3ps，但PDF5正文还记plunger上界约3ps，两种界限不补造成Gaussian点或完整likelihood。 | sample-selection-and-limit-boundary | direct-original-and-visual | PDF6 Fig. 5; PDF5 first paragraph | true |

### Day20逐态标量闭合与几何反问题（checkpoint002）

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SI16-D20-F07 | 按原Eq1、固定K=1/2和同一行printed中央τ/Qt计算p=τTγ，131Ce15/2、27/2、31/2、35/2分别为1.12446、1.04797、.87396、1.02065；133Pr三有限态约1.01300、1.01932、1.02283。声明half-last-digit舍入不能使所有行精确达到p=1。若这些量满足同一meanτ/部分γ率合同，p应为photon branch且≤1；这里仅暴露标量中央换算并非全部精确闭合，不能由残差推断实际branch/K/producer或实验显著性，不替换原表。 | conditional-central-rate-closure | task-derived-with-literal-input | PDF5 Eq. (1); PDF5 Table 1; PDF8 Table 2 | true |
| SI16-D20-F08 | 在本文Eq5的声明参数化中，γ=−80°与+20°有同一cos(γ+30°)因子；Qt=2.5eb均可对应Q20≈3.36824eb，γ=0°则Q20=2.5eb。再照本文Eq4映射给β约.19313/.14567，这是条件逆解，不是已测两种核形状或一般三轴不变量。原文−80°取自TRS，Qt单独不能选择γ或恢复刚软。 | inverse-parameter-counterexample | task-derived | PDF9 Eq. (5); PDF9 Eq. (4) | true |

[新程序](../../system/scripts/day20_rate_geometry_contract.py)与[rate-geometry-result-002.json](../../outputs/learning-daily/20261022-DAY20-be2-qt-deformation-systematics-run-02/rate-geometry-result-002.json)使用正确CG闭式及独立factorial核、现代常数单位重构和allowed零Qs反例，共19项数学/身份控制；不是19项实验认证。因无原joint profile、branch/ICC与exact producer，p>1的printed中央必要合同失败只列需解释边界，不将quoted误差当独立Gaussian抽样或估实验冲突概率。本文Qt系数1.224×10^12与现代B系数约1.22519×10^13的输入量不同；由现代强耦合5/(16π)转换的Qt系数约1.21872×10^12，不静默替换原Eq1。

| SI16-D20-F09 | checkpoint007纠正003认证：Ref31三条旧寿命7.53(37)、64.2(39)、3.42(10)ps与Klemme1999 TableIII逐项相同，是依赖复用；2016 Present与1999为不同反应/实验室采集，不因此认定全部共同系统误差为零。以K=1/2、原Eq1和Klemme印能509/310/552keV计算Qt为3.13519/3.70924/3.73369eb，未精确重现Singh打印3.24/3.74/3.77。原003失败后放宽容差到4%不构成科学验证，残差不印证mixK、ICC或实际producer。 | lineage-and-unresolved-conversion-correction | direct-table-and-bounded-calculation | Table 1; Table 2; KL99-D20-1 | true |
| SI16-D20-F10 | checkpoint034撤回旧全核素误差覆盖认证；同aK的j11/2对齐极限代数保留，Ce四点修正小于打印误差，但Pr15/2约+.19555eb超过.13/.15，19/2约+.11396超过上侧.09。PDF6理由用于Table1，不能泛认证Pr全带精度；详见SI16-D20-R34-1。 | k-mixing-cg-derivation-and-boundary | direct-original-and-derived | PDF5-6 Eqs. (2)-(3); Table 1; singh16-k-mixing-derivation-result-009.json | true |

> checkpoint007：klemme-companion-result-003.json只保历史算术；其“4%通过即吻合/混K或ICC已解释/跨装置精度认证”撤回。原文明确本表简化K=1/2，不能用未知修正替中央残差闭合。实际旧脚本已退役，原代码与JSON哈希见rejected-analysis-registry-007.json。

### Day20定量诊断的可复现合同

[新程序](../../system/scripts/day20_literal_trend_audit.py)只读原表ledger和raw，输出[literal-trend-result-001.json](../../outputs/learning-daily/20261022-DAY20-be2-qt-deformation-systematics-run-02/literal-trend-result-001.json)。14项代数/输入控制包括独立标量回归对照、观测顺序不变、nested Δχ²=z²、全值/Cov同尺度变换、共同加性offset与自旋相关nuisance的不同作用；这些不是14项实验验证。声明共同offset .30eb不改变含截距拟合的斜率精度；声明slope nuisance .05eb/ℏ增加斜率方差(.05)²，可改变z。它们展示误差方向的重要性，不估计实际校准误差。

### Knowledge Impact and Learning Decision — Day20

revises：更正τ/τSF原表身份与Gaussian/Student混用；limits：当前表不足以复原联合实验CI或认定feeding是趋势成因。保留作者γ-shape polarization解释与反例，不因低z恢复恒定形变、也不因条件z≈−2.4宣布γ变化已测定。与[[transition-quadrupole-moment]]及[[high-spin-lifetime-strength-deformation]]双向承接；高自旋HD实验[[petrache-1998-highly-deformed-lifetimes-131ce-nd]]是不同带/组态比较，不拼成同一自旋回归。

### Day20 Agent self-audit

P0：本轮无未隔离身份/raw/Git问题；科学旧认证已在原ID更正，旧结果不改。P1：原events/producer/Cov和限值likelihood未得；Eq4/5按作者符号保留；Fig7 caption的multiplicity>1与正文one-or-more并存，未替作者裁决。Self-audit不是human review，不改变原flags。

## Bibliographic Record

R. P. Singh 等，*Pramana – Journal of Physics* **87**, 7 (2016)，DOI `10.1007/s12043-016-1218-6`；citation key `singh_2016_Lifetimemeasurements`。

## Scope and Reading Depth

全文 11 页逐页阅读并视觉复核。重点覆盖实验设置、Table 1、Figures 1–12、Eqs. (1)–(5)、side feeding、`K`/Clebsch–Gordan 处理和 TRS 解释。

## Summary

论文用 plunger 与 DSAM 测得 `131Ce` 负宇称 `νh11/2` yrast 带的 4 个寿命和 3 个限值，并用 plunger 测得 `133Pr` `πh11/2` yrast 带 3 个有限寿命、2 个限值以及两项正宇称 feeding-band 约束。作者从 Figure 5 目视概括 `131Ce` 由约 `3 eb` 向约 `2.5 eb` 温和下降；Wiki 对四个有限点的重分析只得到 `0.64σ` 的负斜率。`133Pr` 的 `Q_t≈3.6 eb` 至多边际下降。作者把差异解释为高-Ω neutron 驱动 `131Ce` 高三轴性、低-Ω proton 稳定 `133Pr` 近 prolate 形状；具体 γ 值来自 TRS/转子映射，不是寿命直接测量。

## Experimental Setup

- `119Sn(16O,4n)131Ce`；plunger 实验 86 MeV，DSAM 实验 90 MeV。
- IUAC GDA：12 个 Compton-suppressed HPGe，位于 `50°/98°/144°`。
- 分析对象为 `νh11/2` 负宇称 decoupled yrast band；寿命由距离相关强度与 Doppler 线形获得。
- Eq. (1) 用 `Eγ^5`、Clebsch–Gordan 系数和 `Q_t²` 连接 E2 跃迁率；作者还检验了非轴/K-mixing 修正，指出 `K=1/2` 简化只改变数个百分点。
- `118Sn(19F,4n)133Pr` at `92 MeV`; the same IUAC GDA and a gold-backed plunger target were used. Coincidence statistics were insufficient, so multiplicity-gated singles at `50°/98°/144°` supplied the decay curves.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SI16-1 | 本文对 `131Ce` 负宇称 yrast 带报告 4 个有限寿命和 3 个单侧限值。 | experimental-fact | direct | PDF p.5, Table 1 | false |
| SI16-2 | 当前工作给出 `15/2−, 27/2−, 31/2−, 35/2−` 的 `Q_t=2.93(+0.60/−0.30), 2.26(+0.37/−0.23), 2.66(+0.13/−0.12), 2.43(+0.22/−0.20) eb`。 | derived-observable | direct | PDF p.5, Table 1 | true |
| SI16-3 | `19/2−, 23/2−, 39/2−` 分别给出 `τ<7.31 ps`, `τ>1.3 ps`, `τ<0.54 ps`，对应 `Q_t>1.90 eb`, `<2.85 eb`, `>2.29 eb`。 | derived-observable | direct | PDF p.5, Table 1 | true |
| SI16-4 | 论文 Table 1 同时转载并按本工作约定比较 Li 2004 等早期值；这些不是独立的新测量，统计时不得与原文重复计权。 | evidence-dependency | direct | PDF p.5, Table 1, refs. [31–32] | false |
| SI16-5 | 作者概括 `131Ce` 带起始处平均 `Q_t≈3 eb`，约 `I=12ℏ` 以上降至约 `2.5 eb`。 | author-interpretation | direct | PDF p.6, Fig. 5 and text | true |
| SI16-6 | TRS 在低频给出近 prolate、`β2≈0.21` 的 γ-soft 极小；更高频出现 `γ≈−46°`、`−80°` 等极小。 | model-result | direct | PDF pp.8–10, Figs. 9–12 | true |
| SI16-7 | 作者以 TRS 和 `Q_t` 趋势解释 γ-soft/非轴芯响应；具体 γ 极小并非实验直接测量。 | author-interpretation | direct | PDF pp.8–10, Eqs. (4–5), Conclusions | true |
| SI16-8 | For `133Pr`, the present work gives `τ=71(+6/−5), 3.9(+0.3/−0.2), 1.43(+0.10/−0.14) ps` for `15/2−,19/2−,23/2−`, corresponding to `Q_t=3.55(+0.13/−0.15), 3.53(+0.09/−0.13), 3.09(+0.16/−0.11) eb`. | derived-observable | direct | PDF pp.7-8; Table 2 | true |
| SI16-9 | `133Pr` gives `τ<0.70/<0.60 ps` and `Q_t>3.18/>2.89 eb` at `27/2−/31/2−`. | derived-observable | direct | PDF p.8; Table 2 | true |
| SI16-10 | A positive-parity feeding band gives `τ(23/2+)=14.0(+2.7/−3.3) ps` and `τ(27/2+)<8 ps`, with `Q_t(27/2+)>3.3 eb`; the `23/2+` value constrains feeding into the yrast analysis. | experimental-fact | direct | PDF pp.7-8; Table 2 | true |
| SI16-11 | The `133Pr 15/2−` fit requires a roughly `1 ns` cascade-feeding lifetime, linked to partial feeding from a `T1/2≤35 ns` isomer; modelled band feeding is restricted to `Q=4–5 eb`. | analysis-assumption | direct | PDF p.7 | true |
| SI16-12 | Coincidence data for `133Pr` were statistically insufficient, so the lifetime curves use multiplicity-gated singles and prior level-scheme/feeding information. | evidence-boundary | direct | PDF pp.6-7 | true |
| SI16-13 | TRS for `133Pr` stays γ-soft but has minima near prolate (`γ=5°,−2°,−5°`) with `β2≈0.22–0.23`; the authors treat the precise γ minima as numerically uncertain on a flat surface. | model-result | direct | PDF pp.9-10; Fig.12 | true |
| SI16-14 | The authors interpret high-Ω `νh11/2` in `131Ce` as driving large triaxiality and low-Ω `πh11/2` in `133Pr` as stabilizing near-prolate shape. | author-interpretation | indirect | PDF pp.9-10; Figs.10-12; Summary | true |
| SI16-15 | The `133Pr` shape-polarization comparison is explicitly restricted to below its `>0.4 MeV/ħ` band crossing; extrapolation beyond the crossing is unsupported. | evidence-boundary | direct | PDF p.10 | true |
| SI16-16 | The `27/2−`, 827-keV row in Table 1's Ref. [32] column reproduces Li 2004's `τ=1.23(23) ps` but lists a re-derived `Q_t=2.28(21) eb` using the present paper's rotor/Clebsch–Gordan convention. This is dependent reuse of Li's lifetime, not an independent measurement. | derived-observable | direct | PDF p.5, Table 1, Ref. [32] column; Eq. (1)-(3) | true |
| SI16-17 | In the `K`-rotor extraction, `T(E2; I→I−2)=1.224×10^12 Eγ^5 CG(I,K)^2 Q_t²`, with `Eγ` in MeV, `Q_t` in eb and `T` in s−1; Eq. (2) replaces the single Clebsch–Gordan factor with a sum over `K` amplitudes for nonaxial or mixed-`K` states. This is a model-dependent extraction formula, not a direct measurement of `Q_t`. | extraction-formula-and-boundary | direct | PDF p.5, Eqs. (1)–(2) and accompanying text | true |

## Data Lineage and Band Identity

该 yrast 序列与 Alwaleedi thesis Band 1 在负宇称、`νh11/2` 身份以及 510、642、750、827、892 keV 级联上高度对应。当前 crosswalk 记为 `high-confidence provisional`：映射依赖自旋、宇称和多条 `Eγ` 联合一致，而不是仅按 “yrast” 标签。

The `133Pr` page persists the decoupled negative-parity `πh11/2` yrast sequence separately. Its long low-spin lifetimes and feeding constraints are not evidence for a chiral partner; the source uses it as an orbital-polarization control against `131Ce`.

Li 2004 原实验与 Singh 2016 当前实验是两条独立测量谱系；本文 Table 1 中归于 Li 的转载/再计算行仍是依赖证据，不构成第三条谱系。本 Wiki 保留 Singh 再计算值与 Li 原表值，不把差异静默抹平，也不以简单加权平均裁决两次实验；Singh 可作较新的工作基线，但不能仅凭年份断言正确性。

## Interpretation Boundaries

- 寿命与 `Q_t` 直接约束 E2 集体性及可能的芯响应；当前有限点未建立显著下降，也不能单独决定 γ 刚/软、γ 符号或建立 wobbling/chirality。
- `β2/γ` 来自 TRS 与转子映射；side feeding、K mixing、branching 和 stopping treatment 都是模型/分析依赖。
- lifetime 数据不能恢复 Alwaleedi Figure 5.5 未列表的 gated branching intensities。
- `133Pr` lifetime extraction depends more strongly on multiplicity-gated singles and modelled long side feeding; its pre-crossing shape statement cannot be extended through the band crossing.

## Competing Interpretations and Limitations

下降的 `Q_t` 可来自集体性变化、组态/带交叉响应或分析系统学；四个有限点的斜率不足 1σ。TRS 支持 γ-soft/nonaxial 背景，但不排除其它芯响应，也不提供 wobbling/chirality 的带间电磁矩阵。

For `133Pr`, a marginal `Q_t` decrease is likewise compatible with nearly constant collectivity within errors. The near-prolate conclusion combines a prolate rotor conversion, γ-soft TRS surfaces and single-particle calculations; it is not a model-independent γ measurement.

## Human Review Triage

### P0

- SI16-4：禁止把本文转载/再算的 Li 2004 行与 Li 原始测量重复计权。
- SI16-7：不得把 TRS 的 `γ≈−80°` 写成直接实验形变测量。

### P1

- SI16-5：作者的 `3→2.5 eb` 目视概括与 Wiki 的 `0.64σ` 有限点重分析必须分层；寿命/`Q_t` 为 E2 集体性和芯响应提供正交约束，但 γ-softness 本身仍主要由 TRS 与作者解释支持。
- SI16-11/12/15：`133Pr` 的 singles-only statistics、long side feeding 与 pre-crossing validity 必须随数值复用。
- SI16-16：Table 1 Ref. [32] 以 Eq. (1)–(3) 重算 Li 2004 的同一 `27/2−` 寿命；它是依赖的 `Q_t` 转换值，不得计作额外测量。保留 `needs_review: true` 直到对应的 source-use convention 被复核。

## Related Knowledge

- [[131ce]]
- [[133pr]], [[133pr-negative-parity-yrast-reference-sequence]]
- [[iuac-gda-131ce-o16-rdds-dsam]], [[iuac-gda-133pr-f19-rdds]]
- [[transition-quadrupole-moment]]
- [[doppler-shift-attenuation-method]]
- [[alwaleedi-2013-band-structures-131ce]]
- [[131ce-collective-mode-discrimination]]

## Extracted Pages

- Nuclei: [[131ce]], [[133pr]].
- Band: [[131ce-negative-parity-yrast-reference-sequence]], [[133pr-negative-parity-yrast-reference-sequence]].
- Experiments: [[iuac-gda-131ce-o16-rdds-dsam]], [[iuac-gda-133pr-f19-rdds]].
- Observables: [[transition-quadrupole-moment]]。
- Project: [[131ce-collective-mode-discrimination]]。


## Day18定量审计：侧馈参数转换与Qt下降显著性核验

在Day18正式学习中对本文Table 1中131Ce yrast带实验数据进行定量回归与侧馈模型审计，raw SHA256 `95e0831b9864a58fd1a896a1b20e227d88d9b7aa5de56c738c3792441caa1a30`已核。原SI16-1–17各claim及review状态保持；新SI16-D18-1待审。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SI16-D18-1 | 对Table 1四个有限点（15/2−、27/2−、31/2−、35/2−）进行加权线性回归，斜率为 $-0.0302 \pm 0.0472$ eb/$\hbar$，显著性仅为 $-0.64\sigma$（远低于 $1\sigma$）；常数 $Q_t$ 模型（加权均值 $2.58 \pm 0.10$ eb）给出 $\chi^2/	ext{dof} = 0.89$，三个单侧限值亦完全相容。侧馈处理在自旋序列中发生性质变化：低自旋用恒定时延 $	au_	ext{SF} = 0.73	ext{--}1.0$ ps，高自旋用集体转动级联 $Q_	ext{SF} = 5.01	ext{--}5.79$ eb。目视 $Q_t$ 下降可能主要源于侧馈拟合参数的切换而非内禀形变减小。 | task-regression-and-feeding-audit | derived-and-boundary | PDF p.5 Table 1；新singh16-131ce-result-015 | true |

新[分析合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/singh16-131ce-contract-015.json)及[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/singh16-131ce-result-015.json)4项检查全过，为形变演化结论提供了侧馈模型反证。

### 133Pr部分定量审计：Qt斜率显著性与跨5量级侧馈时延跃变

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SI16-D18-2 | Day20原读纠正：Table2的侧馈时间为1100(200)、1.9(2)、14(3)ps；旧0.014ps与跨5数量级断言撤回，序列非单调。原−1.68来自残差缩放cov=True，是额外未知共同误差尺度模型的t(df1)，不能称已知误差Gaussian z；新两模型并列见SI16-D20-F03。未证实feeding制造形变趋势。 | task-correction | direct-source-and-conditional | Table 2; SI16-D20-F02; SI16-D20-F03 | true |

新[分析合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/babra19-singh16-qt-contract-028.json)及[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/babra19-singh16-qt-result-028.json)4项检查全过。

## Day18 checkpoint049修订：侧馈切换与回归可识别性

原SI16-D18-1/2保留为条件审计；新行明确其误差/回归约定，不把侧馈切换升级为已证实假象。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SI16-D18-3 | Day20原读纠正：133Pr侧馈值为1100/1.9/14ps，旧末项.014撤回；131Ce的tauSF/QSF角色变化仍存在。旧回归用了残差缩放，须与已知误差Gaussian分开。原文没有跨点联合Cov，feeding变化不单独证明Qt下降的成因。 | regression-and-feeding-boundary | derived-and-boundary | Table 1; Table 2; SI16-D20-F03 | true |
| SI16-D18-5 | checkpoint062完全闭合结论撤回：固定B(E2)=1723 e2fm4与候选轴对称K=11/2、1/2，解析CG平方76/325、26/75给Qt约2.722与2.235 eb；后者与printed2.28仍差约2%。sqrt(169/114)约1.2176不等printed2.72/2.28约1.1930。1.224/1.225常数变化对Qt仅约.041%，不足解释残差。此为条件几何敏感性，不能反认Li实际采用K，原branch/ICC/producer仍需核；复用旧寿命不是新实验。 | task-correction | derived-and-boundary | 原Table1；strength-boundary-correction-result-078 | true |
| SI16-D18-4 | Day20重算纠正：旧133Pr−1.678及131Ce−.602是残差估计共同尺度的Student t（df1、2），不是已知误差Gaussian z。对平均上下误差/独立点声明控制，正确Gaussian z为−2.40034和−.63910；两模型均不恢复原实验CI。plunger由DSAM约束及feeding/停止模型依赖不能省略。 | conditional-statistical-diagnostic | derived-and-boundary | SI16-D20-F03; SI16-D20-F04 | true |

新结果不改变原Table I/II、limits、K/CG和human review状态。


## Day 20预习：Singh 2016 与 Li 2004 的 K 投影代数对账与形变系统学

checkpoint008：旧SI16-D20-1完全闭合撤回，保全部旧review flags。本次实际核PDF4–6分析/Eqs1–3/Table1及PDF5视觉；并非本次11页全文新读。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| SI16-D20-1 | superseded：不能以错误截短CG和候选K=5/2把两实验“完全闭合”。原先新计算所得2.761(518)不是本表印值；保留Day18 SI16-D18-5未闭合边界。 | task-correction | derived-and-boundary | PDF5 Table1；SI16-D18-5 | true |
| SI16-D20-2 | Table1 Ref[32]列23/2−的Li寿命1.44(54)ps被重算为Qt=2.72(51)eb；27/2−的1.23(23)ps被重算为2.28(21)eb。PDF6明确本表简化采用K=1/2，并称与混K式差数个百分点；这是同一旧寿命的依赖转换，不是第三次实验。 | source-convention-and-lineage | direct-original-and-visual | PDF5 Table1 Ref[32]；PDF6 first paragraph | true |
| SI16-D20-3 | 四有限点在独立Gaussian/误差上下幅平均的明确控制下，斜率−.030175±.047215eb/ℏ，z=−.63910；全lower和全upper给−.92262/−.54753。这不是联合实验CI，未含跨点Cov、方法差别或限值likelihood；未检出斜率不等常数形变已证明，也未证明下降由feeding或视觉制造。 | conditional-regression | derived-and-boundary | PDF5 Table1；SI16-D18-3 | true |

## Day 20预习：Singh 2016 与 Li 2004 真实寿命重合与K投影约定解耦

依据独立审计程序 day19_ce131_li_singh_reconciliation_audit.py 的 14 项检验与基准输出 ce131-li-singh-reconciliation-result-026.json，核准了 $^{131}\text{Ce}$ 负宇称 yrast 带两次测量间的物理与代数对应：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| SI16-D20-4 | Day20全文/视觉更正并撤回旧完全闭合：Table1当前27/2−为1.25(+.41/−.25)ps，不是旧1.24；Ref32转载1.23(23)ps，两中心差约1.63%不等测量精度或真实寿命相同。Table1重算Qt=2.28(21)eb为依赖证据；fixedK代数不识别Li真实K/producer，不能归因100%。 | data-reconciliation-correction | direct-original-and-boundary | Table 1; SI16-D20-F01; SI16-D18-5 | true |

## checkpoint032：原表回归权重与科学认证边界

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SI16-D20-R32-1 | 本任务对Present有限点、平均上下误差/独立Gaussian控制，Ce归一化逆方差权重4.81/10.82/62.30/22.07%，Pr27.06/43.84/29.10%；Ce删最低点斜率+.00573eb/ℏ。旧最低点为Ref31且89.9/96.3%支配、删点+.15的说法均错误，撤回；限值、Ref31/32与positive-feeding行不纳入。未恢复实际Cov/实验CI。 | conditional-regression-correction | task-derived-from-literal-table | PDF5 Table1; PDF8 Table2; SI16-D20-F03/F04; evidence-repair-result-032.json | true |

checkpoint032：SI16-D20-F10的009脚本认证尚待逐式重审；原表/原文事实与原review/flags保持，不以旧passed延续科学认证。

## checkpoint033：观测量身份与形状约定原读纠正

本次为定向原文/表图self-audit，非新增独立实验或全文认证；原review和claim flags保持。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SI16-D20-R33-1 | PDF3 plunger未给高态27/2−可用距离分析；使用高于23/2−的本工作DSAM矩约束低spin plunger拟合。PDF4–5 DSAM得到27/2−1.25(+.41/−.25)ps、τSF.73(+.15/−.12)ps；旧017把它当RDM是错误。Table1 Ref32转载Li1.23(23)ps并按本文K1/2重算Qt2.28(21)，不是第三个实验。 | method-identity-and-lineage | direct-original-and-visual | PDF3 Sec2.2; PDF4 Sec2.3; PDF5 Table1; PDF6 first paragraphs | true |
| SI16-D20-R33-2 | Eq4 prolate/无hexadecapole，R=1.2A^(1/3)fm与β(1+.36β)明确。2.57894±.09866eb是本任务四Present有限Qt点对称化误差/独立Gaussian常数诊断，不是单态RDM原测量；不与IB98异能态Qs构造直接形变闭环。 | shape-convention-and-derived-mean-boundary | direct-and-task-derived | PDF9 Eq4; PDF5 Table1; observable-identity-shape-result-033.json | true |

### checkpoint034：混K适用范围与完整拟合身份

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SI16-D20-R34-1 | 保留声明极限的混K代数，撤回全核素误差覆盖认证。** [[singh-2016-lifetime-131ce-133pr]] SI16-D20-R34-1：Eq2需初末态振幅乘积；本任务仅取同一对齐单准粒子j=11/2、相同aK、K对角四极算符。独立梯算符旋转矩阵核对binomial振幅与相位，带符号CG和给Qt倍率约1.05508、1.03228、1.02128、1.01511、1.01129、1.00876（I=15/2至35/2）。Ce四有限点上移.16139/.03414/.03003/.02128eb，小于各自两侧打印误差；Pr15/2上移.19555eb，超过.13/.15，19/2上移.11396eb，超过上侧.09而小于下侧.13。因此不能将作者PDF6对Table1的理由泛认证为Pr全带实验精度；不识别真实K分布、producer或原CI，也不解释中央换算残差。 | conditional-algebra-and-source-scope | original-selected-and-conditional | PDF5 Eqs2–3; PDF6 first paragraph; PDF5 Table1; PDF8 Table2 | true |


### checkpoint043：Present趋势图的选择与区间边界

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| SI16-D20-R43-1 | Table1/2的Present负宇称Qt共12行：7个有限值和5个单侧界限，均在本任务趋势图保留；Table2另2个positive-parity feeding行属于另一带，不拼入回归。Ref31/32转载不当新增独立测量。原非对称误差条照画，有限点回归另声明sigma=(minus+plus)/2及已知独立Gaussian误差，Ce/Pr条件斜率−.030175±.047215/−.116674±.048608eb/ℏ。只画finite自旋范围15/2–35/2与15/2–23/2，无CI带或限值likelihood。Pr高spin限值不能当沿低spin直线下降的实测证据，Ce低z也不证明恒定；原Cov/profile/producer未得。 | literal-table-and-conditional-visualization | source-derived-with-declared-model | PDF5 Table1; PDF8 Table2; SI16-D20-F03; SI16-D20-F04 | true |


### checkpoint102：边际误差不识别联合Cov

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| SI16-D20-R102-1 | 原Present有限点四Ce/三Pr，按上下误差平均并保持同一WLS线性斜率估计式不动时，未知PSD相关矩阵容许SE包络Ce[0,.078284]、Pr[0,.069607]。明确构造闭合多边形Gram矩阵与严格正定近似。它说明边际误差不能识别实际斜率方差；不是实际Cov、重拟合GLS、原MINOS profile/CI，也不将Pr比值−1.676185与残差尺度模型Student−1.67818混同。 | declared-fixed-contrast-correlation-sensitivity | task-derived-not-experimental-CI | PDF5 Table1; PDF8 Table2; SI16-D20-F03/F04; correlation-envelope-result-102.json in Day20 run02 | true |


### checkpoint110：二阶形变式的明确模型与归属

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| SI16-D20-R110-1 | Eq4明示r0=1.2与舍入.36、prolate/no-β4；本任务另声明R=cR0(1+β2Y20+β4Y40)均匀电荷族，精确Legendre/Gaunt积分给c22=.3604475、c24=.9671821、c44=.3276795。常体积与密度重标族二阶相同、高阶/反演不同；Q6.8eb/Z60/A134/r1.2的条件β根约.352324(二阶)、.355659(常体积)、.349337(密度重标)。这些不是作者β4结果、实际核β/误差或Petrache真实算法；31项只检声明数学与数值。 | source-formula-versus-declared-surface-model | task-derived-not-experimental-CI | PDF9 Eq4; SI16-D20-F05; surface-charge-contract-result-110.json in Day20 run02 | true |

## checkpoint146：原件身份与推断边界更正

本轮为Codex定向self-audit；已有review_status与原claim flags不变。121–145旧认证撤回；实际新阅读范围见source-reading-scope-146.json，引用较早纠错不冒称新全文阅读。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| SI16-D20-R146-1 | 原件为Pramana87:7，DOI10.1007/s12043-016-1218-6。27/2− Present为τ=1.25(+.41/−.25)ps、Qt=2.26(+.37/−.23)eb；2.58(12)和1.37(13)不属于这行。2.57894附近是所选多点条件加权常数，不能写成该态独立测量。143/145的跨实验室Z、零漂移与8倍B认证撤回；几何/branch/响应/Cov未恢复。 | direct-original-correction | source-and-bounded-self-audit | PDF5 Table1; PDF9 Eqs4/5 | true |


## Day24：131Ce实际节点、clock与目标核迁移

独立worker本轮11页主线文本读、fresh visual PDF3–10覆盖12图/两表/关键式，另高分辨率Fig1；leader独立抽核PDF5 Table1和其单位/limits段。实际raw SHA95e0831b9864a58fd1a896a1b20e227d88d9b7aa5de56c738c3792441caa1a30相符；不冒称leader单独重读所有图。原Day20更正、用户flags及未闭合producer/Cov保持。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SI16-D24-001 | Table1 present负宇称15/2、27/2、31/2、35/2的meanτ为9.6(+1.9/−3.8)、1.25(+.41/−.25)、.51(5)、.60(+.11/−.10)ps，分别走510/827/892/922keV的ΔI2边；19/2、23/2、39/2为<7.31/>1.3/<.54ps。Ref32列27/2的1.23(23)复用Li而非present1.25，其Qt2.28(21)为本表Eq1的再转换。Fig5旧星/菱形不加实验票；不能把23/2正文约3ps上界与>1.3拼成完整联合置信区间。 | direct-state-clock-and-reuse-identity | direct-original-and-independent-worker-check | PDF3 Fig1; PDF5 Table1/caption and firstparagraph; PDF6 Fig5 | true |
| SI16-D24-002 | Fig1的7/2+基态10.3min和9/2−异构态88ns标注为half-lives，不能塞作Table1 present meanτ/sidefeeding；本工作低spin plunger拟合又用高spin DSAM矩作约束，两个方法输出非全独立。本文只给该νh11/2 yrast参考链，PDF9称近15ℏ另一变yrast带因统计不足未测寿命，因此不提供完整双partner absoluteB矩阵或本核全部band的τ。 | clock-analysis-dependency-and-network-coverage | direct-original-and-scope-boundary | PDF3 Fig1/analysis; PDF5 errorparagraph; PDF9 discussion | true |

逐态方法/feeding/旧列机器台账在本run workers/singh-state-005，root已抽核；可复用长期合同见[[133ce-thesis-analysis-blueprint]]及[[li-2004-lifetimes-131ce]] LI04-D24-001/002。Ex由整数γ加和的版本只作身份辅助，不把它当精确采用值或跨核共零点；不搬本核10%误差处方、sidefeeding、Qt/K/TRS到133Ce。

### Day24 checkpoint005 Agent self-audit triage

P0: none identified（新增范围）。P1：worker原读/leader抽核支持Table1行身份、限值方向、Ref32依赖和clock区分；jointCov/各limit likelihood及actualproducer不补造。旧均场/Qt/趋势认证未由本次提取恢复，人审状态不变。
