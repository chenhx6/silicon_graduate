---
type: source
title: "Lifetimes of Excited Levels in 131Ce"
aliases: [Li 2004 131Ce lifetimes, Guang-Sheng Li 2004]
created: 2026-07-28
updated: 2026-09-28
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Lifetimes of Excited Levels in 131Ce"
authors: [Li Guang-Sheng, Meng Rui, Zhu Li-Hua, Zhang Zhen-Long, Wang Yue, Wang Zhi-Min, Wen Shu-Xian, Lu Jing-Bin, Zhao Guang-Yi, Li Xian-Feng, Wen Li-Jun, Zheng Yong-Nan, Zheng Yong, Liu Yun-Zuo, Yuan Guan-Jun, Yang Chun-Xiang]
journal: Chinese Physics Letters
year: 2004
volume: 21
pages: 461-463
doi:
language: en
canonical_source: journal:Chinese Physics Letters:21:461-463
citation_key: guang-sheng_2004_LifetimesExcited
raw_file: "raw/papers/2004_Lifetimes of Excited Levels in 131Ce.pdf"
raw_sha256: 100A06FC1BB6D7061A153552529C9245F123248F213A93F022B202AF97DCDCC5
nuclei: [131ce]
reactions: [116Sn(19F,p3n)131Ce]
experiments: [ciae-hi13-131ce-f19-95mev]
observables: [transition-quadrupole-moment]
methods: [doppler-shift-attenuation]
tags: [131ce, lifetime, qt, dsam, positive-parity, negative-parity]
---

# Li 等（2004）：`131Ce` 激发态寿命

## Bibliographic Record

Li Guang-Sheng 等，*Chinese Physics Letters* **21**, 461–463 (2004)；citation key `guang-sheng_2004_LifetimesExcited`。DOI 未在所给论文或 BibTeX 中确认。

## Scope and Reading Depth

全文 3 页在 2026-08-11 再次逐页视觉复核。PDF 文本层损坏，全部数值均以页面图像、Figure 1–3 和 Table 1 为准；未用 2016 年论文的转载值反向补写原文。LI04-1–4 保留既有用户 claim-level review 状态，不因本次 corpus on-touch 重新设为待审。

## Paper Question and Scientific Motivation

作者用 odd neutron 作为 core-shape sensitivity probe，询问 `131Ce` 正、负宇称高自旋序列的寿命/`Q_t` 是否揭示组态依赖的集体性，以及轻 Ce 同位素的形变是否随中子数接近 `N=82` 而下降（PDF pp. 1, 3）。

## Method and Design Logic

- 以 `116Sn(19F,p3n)131Ce` 建立 prompt γ-γ coincidence 数据；用 `132°` backward spectra 和能级门抑制重叠峰，再拟合 Doppler-broadened line shapes（PDF pp. 1-2；Figs. 1-2）。
- 线形计算显式纳入 beam/recoil energy loss、recoil-velocity distribution、detector resolution/geometry、known cascade feeding、unobserved side feeding、Ziegler stopping powers 与 Blaugrund angular straggling（PDF p. 2）。
- 由寿命按 rotational formula 提取 `B(E2)` 与 `Q_t`，再比较正负宇称序列、`130Ce` yrast band 和 `128-131Ce` 系统学。组态—形变联系属于作者解释，不是 DSAM 直接观测（PDF pp. 2-3；Table 1；Fig. 3）。

## Summary

论文用 DSAM 测量 `131Ce` 正、负宇称 yrast 序列的寿命并提取 `B(E2)` 和 `Q_t`。负宇称序列平均 `Q_t=3.09(61) eb`，正宇称序列平均 `Q_t=4.56(145) eb`；作者将差异与 `νh11/2`、`νg7/2` 轨道的形状驱动倾向联系。该组态—形变联系是作者解释，且寿命提取依赖 side feeding 和转子假设。

## Experimental Setup

- 95 MeV `116Sn(19F,p3n)131Ce`，HI-13 tandem / CIAE。
- `1.05 mg/cm²` `116Sn` 靶与 `22.7 mg/cm²` Pb backing。
- 11 个 BGO-suppressed HPGe：3 个 `90°`、4 个 `48°`、4 个 `132°`。
- 用 Doppler-shift attenuation 分析；Figure 1 给出本工作使用的部分纲图。
- 事件逐事例记录约 `10^8` 个 γ-γ coincidence events；DSAM matrix 以一条 γ 在 `132°`、另一条在任意其它探测器为条件。
- Figure 2 展示 827-keV `27/2−→23/2−` 与 725-keV `17/2+→13/2+` line-shape fits。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LI04-1 | 负宇称序列的 `19/2−,23/2−,27/2−,31/2−` 分别为 `τ>4.0, 1.44(54), 1.23(23), <1.04 ps`。 | experimental-fact | direct-visual | PDF p.3, Table 1 | false |
| LI04-2 | 原表相应 `Q_t` 为 `<3.81, 3.55(67), 2.72(25), >2.31 eb`。 | derived-observable | direct-visual | PDF p.3, Table 1 | false |
| LI04-3 | 正宇称序列的 `13/2+,17/2+,21/2+,25/2+` 为 `τ=1.46(56),1.32(10),0.60(26),<2.19 ps`，`Q_t=7.04(135),3.80(14),4.06(88),>3.36 eb`。 | derived-observable | direct-visual | PDF p.3, Table 1 | false |
| LI04-4 | 作者给出负、正宇称带平均 `Q_t=3.09(61)` 与 `4.56(145) eb`。 | derived-observable | direct-visual | PDF p.3, paragraph below Table 1 | false |
| LI04-5 | 作者把负宇称带较低集体性与 `[514]9/2− (h11/2)` 的 oblate-driving 倾向、正宇称带与 `[404]7/2+ (g7/2)` 的 prolate-driving 倾向联系。 | author-interpretation | direct-visual | PDF p.3, discussion | true |
| LI04-6 | 约 `10^8` coincidence events 由 11 个 BGO-suppressed HPGe 获取；DSAM 使用 `132°` gated backward spectra。 | experimental-fact | direct-visual | PDF pp.1-2 | true |
| LI04-7 | Line-shape calculation accounts for energy loss, recoil-velocity distribution, detector response/geometry, known cascade feeding, unobserved side feeding, stopping power and angular straggling. | experimental-method | direct-visual | PDF p.2, first paragraph | true |
| LI04-8 | `31/2−` 与 `25/2+` 只给未作 feeding correction 的 effective-lifetime upper limits；`19/2−` 的 `τ>4 ps` 来自 642-keV peak 未见 Doppler broadening。 | experimental-criterion | direct-visual | PDF p.2, text below Fig.1 and attenuation-factor derivation | true |
| LI04-9 | 作者把负宇称带平均 `Q_t=3.09(61) eb` 与 `130Ce` yrast `3.73(105) eb` 比较，并称 unpaired neutron reduces collectivity/changes shape。 | author-interpretation | direct-visual | PDF p.3, first paragraph | true |
| LI04-10 | `128-131Ce` comparison in Fig.3 is interpreted as a gradual reduction of collectivity/deformation with increasing neutron number。 | author-interpretation | direct-visual | PDF p.3, Fig.3 and Summary | true |
| LI04-11 | The source measures two opposite-parity rotational sequences, not a same-parity partner doublet, and makes no chirality assignment。 | evidence-boundary | direct-visual | Full paper; Fig.1; Summary | true |
| LI04-D18-1 | checkpoint062完全闭合结论撤回：固定B(E2)=1723 e2fm4与候选轴对称K=11/2、1/2，解析CG平方76/325、26/75给Qt约2.722与2.235 eb；后者与printed2.28仍差约2%。sqrt(169/114)约1.2176不等printed2.72/2.28约1.1930。1.224/1.225常数变化对Qt仅约.041%，不足解释残差。此为条件几何敏感性，不能反认Li实际采用K，原branch/ICC/producer仍需核；复用旧寿命不是新实验。 | task-correction | derived-and-boundary | 原Table1；strength-boundary-correction-result-078 | true |

## Source table transcription audit (2026-09-28)

The original PDF was reopened at printed p.463 (PDF p.3), Table 1. The `27/2−` row reports `Q_t=2.72(25) eb`; the prior Wiki transcription `2.72(26)` was an error of the final uncertainty digit and is corrected in LI04-2. The row also gives `B(E2)=1723(322) e²fm⁴`. The local PDF SHA-256 remains `100a06fc1bb6d7061a153552529c9245f123248f213a93f022b202af97dcdcc5`. Page-level `review_status: unreviewed` and LI04-2 `needs_review: false` are unchanged; this correction is a Codex source self-audit, not a new human review.

## Data Lineage and Band Identity

Figure 1 的负宇称 510–642–750–827–892 keV 序列与 thesis Band 1/2016 yrast band 高度一致。正宇称 610–725–796–649 keV 序列是另一条带，不因同属 yrast 讨论而与 Band 1 合并。

Stable pages: [[131ce-negative-parity-yrast-reference-sequence]] and [[131ce-positive-parity-reference-sequence]]. These are parity-specific lifetime references, not a chiral-doublet pair.

Li 2004 与 Singh 2016 的当前实验结果来自两次独立实验，可分别保留和比较。Singh 2016 Table 1 转载或按其约定重算的 Li 2004 行仍属于 Li 的原始测量谱系，只用于 cross-check，不能算作第三份独立证据。两次实验不通过简单加权平均裁决“谁正确”；Singh 可作为较新的工作基线，但年代本身不证明其必然更准确。

## Interpretation Boundaries

- PDF 文本层损坏，但 LI04-1–4 的 Table 1 转录已由用户完成 claim-level 视觉审核；页面整体仍为 `unreviewed`，LI04-5 仍待审。
- `Q_t` 与平均值依赖转子系数、branching、internal conversion 和 side-feeding 处理。
- 轨道的形状驱动倾向支持竞争解释排序，但不直接证明静态 shape coexistence。
- `31/2−` 与 `25/2+` 是 feeding-uncorrected effective upper limits，不能与有限寿命点等权拟合。
- `19/2−` lower limit 依赖 paper's attenuation-factor/slowdown-time estimate；它不是 resolved line-shape lifetime。

## Competing Interpretations and Limitations

正负宇称序列的平均矩差异可由轨道形状驱动、组态依赖的芯极化或提取约定共同影响。现有点数、限值和较大误差不能唯一选择静态共存形状；文本层损坏还要求正式使用前复核原表。

The Ce isotope trend mixes different odd/even systems and reference configurations; it is a regional author interpretation rather than a controlled same-configuration sequence. This paper supplies deformation/collectivity control evidence for the chirality corpus, not partner-band electromagnetic evidence.

## Analytical Reconstruction

| ID | Audit item | Agent judgment | Evidence / locator | review_status |
|---|---|---|---|---|
| AR-1 | Core reconstruction | The direct result is a parity-dependent lifetime/`Q_t` map; the shape-driving narrative is an interpretation layered on rotational extraction and regional comparison. | LI04-1 to LI04-10; Table 1; Fig.3 | unreviewed |
| AR-2 | Assumptions and dependencies | Feeding, stopping powers, rotational formula and limit semantics control the extracted strengths; upper/lower limits must stay distinct from fitted lifetimes. | LI04-7/8; PDF p.2 | unreviewed |
| AR-3 | Transfer conditions | The negative-parity sequence can anchor later Band-1/yrast crosswalks only after transition-by-transition matching; the positive-parity sequence is a separate reference. | Fig.1; current lineage comparison | unreviewed |
| AR-4 | Failure conditions | Alternative stopping/feeding treatment or a different band mapping could change absolute `Q_t` and the parity contrast without invalidating the observed γ-ray scheme. | Method and Table 1 notes | unreviewed |
| AR-5 | Reverse/falsification test | Reanalyse line shapes with documented side-feeding histories and common stopping powers, then compare both bands and neighboring nuclei with matched configurations. | PDF pp.2-3 | unreviewed |
| AR-6 | Research-question decision | Use this paper as normal-deformed collectivity/shape-driving control; do not count it as direct chirality or partner-band lifetime evidence. | LI04-11 | unreviewed |

### Companion Evidence Audit

- 827- and 725-keV Doppler-broadened line shapes: `observed` and fitted in Fig.2.
- Table-1 finite lifetimes and `B(E2)/Q_t`: `derived-from-observed-line-shapes`.
- `31/2−` and `25/2+` lifetimes: `upper-limits/effective`, not feeding-corrected.
- `19/2−`: `lower-limit`, inferred from absence of visible broadening.
- Shape-driving orbital interpretation and triaxiality: `expected-but-not-established`.

## Human Review Triage

### P0

- LI04-1–4：用户已对照 PDF p.3 接受 Table 1 的视觉转录，本轮 claim-level P0 已解决。
- Li 2004 与 Singh 2016 的当前结果是独立实验；只有 Singh 表内转载/重算的 Li 行不得作为额外独立测量重复计权。

### P1

- 正、负宇称序列的 `Q_t` 差异提示组态依赖的芯响应；现有误差和不同提取约定不足以单独证明两个稳定形状共存。
- LI04-8：确认三个 limit/effective points 在任何 later trend fit 中保持与 finite fitted lifetimes 分离。
- LI04-9/10：确认 `130Ce` 与 `128-131Ce` 系统学只作为作者 shape/collectivity interpretation，不作为 matched-configuration proof。

## Related Knowledge

- [[131ce]]
- [[131ce-negative-parity-yrast-reference-sequence]]
- [[131ce-positive-parity-reference-sequence]]
- [[ciae-hi13-131ce-f19-95mev]]
- [[transition-quadrupole-moment]]
- [[singh-2016-lifetime-131ce-133pr]]
- [[alwaleedi-2013-band-structures-131ce]]

## Extracted Pages

- PDF p.1: motivation, experimental setup and acquisition.
- PDF p.2: partial level scheme, line-shape method, limit derivations and Fig.2 fits.
- PDF p.3: Table 1, `Q_t` interpretation, Ce isotope systematics and conclusion.
- Nucleus: [[131ce]]；observable: [[transition-quadrupole-moment]]；project: [[131ce-collective-mode-discrimination]]。


## Day 20预习：131Ce Li 2004 与 Singh 2016 的 K 投影代数对账

2026-10-21 checkpoint008纠错；旧LI04-1–11及Day18纠错、人审flags保持。原LI04-D20-1的“100%由K=5/2消解”撤回，旧JSON/提交仅作错误历史。本次实际视觉核PDF2 Fig1/2及PDF3 Table1，不冒全文新精读。新程序给条件代数，不识别作者实际K。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| LI04-D20-1 | superseded：旧K=5/2归因、2.761(518)和完全闭合撤回；截短CG公式漏掉(I+K)(I+K−1)/[I(I−1)]。正确CG在27/2,K=11/2时为76/325，在K=1/2时为26/75；不能用算术匹配证明原作者约定。 | task-correction | derived-and-boundary | PDF3 Table1；LI04-D18-1 | true |
| LI04-D20-2 | 原表23/2−列Eγ=750keV、τ=1.44(54)ps、B(E2)=2416(906)e²fm⁴、Qt=3.55(67)eb；27/2−列827keV、1.23(23)ps、1723(322)e²fm⁴、2.72(25)eb。不能把新程序的750.5keV当原表精度。 | table-transcription | direct-visual | PDF3 printed463 Table1 | true |
| LI04-D20-3 | 固定原B=0.2416e²b²的23/2候选K=1/2、5/2、11/2分别给Qt=2.66643、2.80680、3.55687eb；27/2的原B=.1723对应2.23530、2.31810、2.72162eb。候选K=11/2与原表相容并不证明作者用该K，也不能把保B几何变换和保τ重算混作同一验证。 | conditional-geometry | derived-and-boundary | PDF3 Table1；evidence-repair-result-008.json | true |

## Day 20预习：Li 2004 与 Singh 2016 真实寿命重合与K投影约定解耦

依据独立审计程序 day19_ce131_li_singh_reconciliation_audit.py 的 14 项检验与基准输出 ce131-li-singh-reconciliation-result-026.json，核准了 $^{131}\text{Ce}$ 负宇称 yrast 带两次测量间的物理与代数对应：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| LI04-D20-4 | checkpoint033：旧1.24ps/plunger/100%K归因与完全相容结论撤回；Singh真实Present27/2来自DSAM、1.25(+.41/−.25)ps，Li原表Qt2.72(25)eb。正确候选CG相容不识别实际K/producer；见LI04-D20-R33-1/R33-2。 | withdrawn-task-certification | source-correction-and-boundary | checkpoint033 | true |

## checkpoint033：观测量身份与形状约定原读纠正

本次为定向原文/表图self-audit，非新增独立实验或全文认证；原review和claim flags保持。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LI04-D20-R33-1 | 真实刊物Chinese Physics Letters21,461–463(2004)，非旧017脚本PRC69,064320。原Table1 27/2−、827keV：τ1.23(23)ps，B(E2)1723(322)e²fm⁴，Qt2.72(25)eb；23/2−、750keV：1.44(54)ps、2416(906)e²fm⁴、3.55(67)eb。不得错用Singh转载别行2.72(51)误差。 | literal-bibliography-and-table | direct-original-and-visual | PDF3 printed463 Table1; article page header | true |
| LI04-D20-R33-2 | 本方法DSAM含停止、velocity/geometry、known/unknownfeeding等建模；31/2−和25/2+仅未校正feeding的effective upper limits。候选K11/2能重现原B→Qt数字，不证明作者K；与Singh同态DSAM中心比较不排除共同校准，不能称正交技术验证或零物理差异已证明。 | method-and-comparison-boundary | direct-original-and-correction | PDF2 Fig1/Fig2 and effective-lifetime paragraph; PDF3 Table1 | true |
### checkpoint143：131Ce 跨实验室 DSAM 寿命重合与宇称分岔四极集体性审计

> checkpoint146：本节121–145批次的科学认证已撤回。旧文本/输入与指纹保存在本run的history-before-repair-146.json；原始原件与既有review/flags保留。自设数值或flag的passed只验证算术，不识别实际producer、共同Cov、实验CI或唯一模式。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| LI04-D20-R143-1 | checkpoint146撤回旧认证；不据此恢复错误表值、跨态强度阶梯、硬阈值或完全闭合。请使用本页较早原件纠错与checkpoint146。 | withdrawn-task-certification | rejected-and-replaced | checkpoint146; history-before-repair-146.json | true |

## checkpoint146：原件身份与推断边界更正

本轮为Codex定向self-audit；已有review_status与原claim flags不变。121–145旧认证撤回；实际新阅读范围见source-reading-scope-146.json，引用较早纠错不冒称新全文阅读。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| LI04-D20-R146-1 | Li原27/2−为1.23(23)ps、Qt2.72(25)eb；Singh Present同态为1.25(+.41/−.25)ps、Qt2.26(+.37/−.23)eb，两篇换算约定不能直接等同。143自设2.58(12)计算Z=.505不对应原同态对账；小Z也不能排除共同系统误差。正负宇称平均Qt之比及其平方非匹配态实际B比，更不独自证明显著形状分岔。 | cross-source-identity-and-statistics-correction | source-and-bounded-self-audit | LI04-D20-R33-1/R33-2; Singh2016 PDF5 Table1 | true |
