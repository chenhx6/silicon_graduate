---
type: source
title: "Lifetime measurements in the yrast band of the gamma-soft nuclei 131Ce and 133Pr"
aliases: [Singh 2016 131Ce lifetime, Singh 2016 133Pr lifetime]
created: 2026-07-28
updated: 2026-10-09
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
| SI16-D18-2 | 对Table 2中133Pr yrast带三个有限态（15/2-、19/2-、23/2-）进行加权回归审计，其加权平均Qt为3.407(73) eb；线性回归斜率为dQt/dI = -0.1167(695) eb/hbar，显著性仅为-1.68sigma，在2sigma统计置信度下完全无法拒绝常数Qt假定。更为显著的是，侧馈平均寿命tau_SF在仅三个能级间发生跨越5个数量级的剧烈跃变（15/2-处为1100 ps，19/2-处降至1.9 ps，23/2-处骤降至0.014 ps）；低自旋态tau_SF是能级寿命（71 ps）的15倍，处于完全阻停前馈入区。这证实未获独立门控隔离的侧馈时延跃变能够轻易制造或扭曲高自旋形变演化的表观假象。 | task-regression-and-feeding-audit | derived-and-boundary | PDF p.8 Table 2；新babra19-singh16-qt-result-028 | true |

新[分析合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/babra19-singh16-qt-contract-028.json)及[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/babra19-singh16-qt-result-028.json)4项检查全过。

## Day18 checkpoint049修订：侧馈切换与回归可识别性

原SI16-D18-1/2保留为条件审计；新行明确其误差/回归约定，不把侧馈切换升级为已证实假象。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SI16-D18-3 | 131Ce四有限点回归使用对称化误差，133Pr三点也使用对称化误差；原文MINOS不提供这些跨点回归的联合协方差。133Pr的τSF=1100/1.9/.014ps与131Ce的tauSF/QSF切换是拟合输入合同，说明形变斜率对feeding模型敏感，但不单独证明Qt下降由feeding制造。 | regression-and-feeding-boundary | derived-and-boundary | PDF5 Table1/analysis；PDF8 Table2/analysis；新qt-systematics-boundary-result-049 | true |
| SI16-D18-5 | checkpoint062完全闭合结论撤回：固定B(E2)=1723 e2fm4与候选轴对称K=11/2、1/2，解析CG平方76/325、26/75给Qt约2.722与2.235 eb；后者与printed2.28仍差约2%。sqrt(169/114)约1.2176不等printed2.72/2.28约1.1930。1.224/1.225常数变化对Qt仅约.041%，不足解释残差。此为条件几何敏感性，不能反认Li实际采用K，原branch/ICC/producer仍需核；复用旧寿命不是新实验。 | task-correction | derived-and-boundary | 原Table1；strength-boundary-correction-result-078 | true |
| SI16-D18-4 | 新条件回归给133Pr z=−1.678、131Ce z=−.602；它们是中心值/对称误差下的诊断，不是论文CI。131Ce的15/2–27/2混合plunger/DSAM方法、stopping prescriptions和side-feed parameter switch必须保留，不能把常数Qt接受写成独立实验裁决。 | conditional-statistical-diagnostic | derived-and-boundary | PDF4–8；qt-systematics-boundary-result-049 | true |

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
| SI16-D20-4 | Singh 2016 Table 1 在 Ref. [32] 栏转载并重算 Li 2004 的 $27/2^-$ 态 $Q_t = 2.28(21)\text{ eb}$，与其实验测得的 $2.26(+0.37/-0.23)\text{ eb}$ 高度吻合。两次实验实测能级寿命严格重合（$\tau = 1.23\text{ ps}$ 对 $1.24\text{ ps}$，差异仅 $0.81\%$）；$Q_t$ 差异完全来自转子模型 $K$ 投影代数：Li 采用 $K=11/2$（$Q_t = 2.722\text{ eb}$），Singh 采用 $K=1/2$（$Q_t = 2.235\text{ eb}$），两者理论比值精确为 $\sqrt{169/114} \approx 1.2176$。在 $23/2^-$ 态上，Li 的寿命 $\tau = 1.44(54)\text{ ps}$ 完全符合 Singh 单侧限值 $\tau > 1.3\text{ ps}$，且其 $B(E2)$ 经 $K=1/2$ 转换后为 $Q_t = 2.67\text{ eb}$，完全落于 Singh 上限 $Q_t < 2.85\text{ eb}$ 之内。 | data-reconciliation-contract | direct-original-and-derived | PDF5 Table1；LI04 Table1；ce131-li-singh-reconciliation-result-026.json | true |
