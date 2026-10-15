---
type: source
title: "Matev等2007：A≈130有效四极矩与对齐的可加性"
aliases: [Matev 2007 quadrupole alignment additivity, A130 effective quadrupole additivity]
created: 2026-10-15
updated: 2026-10-15
status: ai-draft
review_status: unreviewed
source_type: journal-article-theory-and-method
reading_depth: deep-read
title_original: "Additivity of effective quadrupole moments and angular momentum alignments in the A~130 nuclei"
authors: [M. Matev, A. V. Afanasjev, J. Dobaczewski, G. A. Lalazissis, W. Nazarewicz]
journal: Physical Review C
year: 2007
volume: 76
pages: 034304
doi: 10.1103/PhysRevC.76.034304
arxiv: 0707.4324v1
language: en
canonical_source: "https://doi.org/10.1103/PhysRevC.76.034304"
citation_key: ""
raw_file: "raw/papers/2007-Matev-A130-quadrupole-alignment-additivity.pdf"
raw_sha256: 40d485c653f2016cd6dc38ef95a7694e9ced6d09458004039b5be92541d07586
nuclei: [131Ce, 128Ba, 142Sm]
models: [cranked-Hartree-Fock, cranked-relativistic-mean-field, independent-particle-additivity]
observables: [charge-quadrupole-moment, transition-quadrupole-moment, effective-alignment]
methods: [self-consistent-cranking, multivariate-least-squares]
tags: [a130, quadrupole, alignment, reference-configuration, uncertainty, unpaired-regime]
---

# Matev等（2007）：A≈130有效四极矩与对齐的可加性

## Bibliographic Record

M. Matev等，*Physical Review C* **76**, 034304 (2007)，DOI [10.1103/PhysRevC.76.034304](https://doi.org/10.1103/PhysRevC.76.034304)。Crossref/arXiv精确DOI、题名和五作者匹配。实际读[arXiv0707.4324v1](https://arxiv.org/pdf/0707.4324v1)，14页，425027 bytes，SHA256如frontmatter；边栏印30 Jul 2007，首页另印Dated: November 13, 2018，保留日期差异，不据此改发表年。

本文全部locator均指这份v1。**未核出版商正式排版/勘误**，不能把下述字面不一致称官方错误。实际PDF位于`tmp/day14-20261014/matev2007/PDFs/Additivity_of_effective_quadrupole_moments_and_angular_momentum_alignments_in_the_A~130_nuclei.pdf`。按daily-learning授权建立来源记录，但**未完成raw归档摄入**；`raw_file`是未填保留槽。citation key未匹配本地Bib，留空；未改raw/Bib。

## Scope and Reading Depth

- **Covered scope**：14页主线、动机与结论、Eqs.(1)–(34)对当前判断相关的定义/回归/误差假设、Figs.1–6、Tables I–III和原实验引用链；视觉核PDF3–12的关键公式、core、图与表。
- **Not covered**：未重跑CHF/CRMF；缺实际配置设计矩阵C、各配置算出的O、权重/残差文件及代码。Laird2002原实验全文仍未得；Riley2001作者报告后续公开取得但本页建立时仅核身份，未代其读取实验分析。未请求SI。
- 来源前回忆和量化前预测均记录priming；本页`unreviewed`，全部MT07 claims保留`needs_review: true`。

## Summary

作者在无配对的高/超形变自洽推转计算中，以131Ce的一个组态作reference，拟合有效四极矩与对齐的可加性。论文给出Qt与坐标/转轴的直接定义，也给出183/105个计算组态的拟合和误差假设；实验图复用早期工作。它能校准Qt解释与输入契约，不能当新寿命测量或直接迁移到136Pr的实际阻塞、形状/转轴。

## Method and Physical Logic

对每个独立粒子组态的one-body算符期望，先减去reference值，再用相对占据cα=0、+1、−1表示不变、加particle或去hole，拟合`δO=C o_eff`。有效量含直接轨道贡献与核极化；neutron的bare charge quadrupole为零，但可通过质子密度极化产生非零effective charge moment。它不是把中子当成带电粒子。

CHF用HFODD v1.75/SLy4，CRMF用NL1。相对矩和对齐的拟合均在ℏω=.65 MeV的选定无配对高形变组态集开展；crossing、混合/收敛歧义组态被排除。该条件是适用域，不能仅因同属A≈130就套到低频、配对显著或另一转轴分支。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| MT07-1 | 电四极算符取q20=2z²−x²−y²、q22=sqrt3(x²−y²)；电荷矩只显式求和occupied protons。Q2=sqrt(Q20²+Q22²)、tanγ=Q22/Q20，spherical component是Q22/sqrt2，不能混用别的Q22归一。 | theoretical-definition | direct | PDF p.2 Eqs.(1)–(4); PDF p.3 Eqs.(5)–(8) | true |
| MT07-2 | y推转取Qt=Q20−Q22/sqrt3，x推转右端为Q20+Q22/sqrt3；作者说明同一物理问题换轴时Q22反号，Qt相同。这里坐标换轴不要求不同EDF的预测相同。 | theoretical-definition-and-scope | direct-and-derived | PDF p.4 Eqs.(11)–(14); PDF p.5 Eq.(15) | true |
| MT07-3 | 有效四极矩包含bare和polarization项；neutron的bare charge moment为零，有效量由极化给出。 | model-definition | direct | PDF p.5 Eqs.(20)–(21) | true |
| MT07-4 | 最终CHF/CRMF集各183/105个计算配置，排除crossing/收敛/赋态歧义；以131Ce最低SD组态作core并在ℏω=.65 MeV测试。其占据blocks计得N73/Z58/A131，确为奇A reference；不提供Pr136的实际reference。 | model-input-and-scope | direct-and-derived | PDF p.6 Sec.II.E; PDF p.7 reference paragraph | true |
| MT07-5 | δO相对core拟合为Σcα oα_eff，c的符号由该core occupied/empty状态定义；不能把未列深层core轨道当零占据，或跨reference直接移用particle/hole标签。 | theoretical-method | direct-and-derived | PDF p.5 Eq.(19) and coefficient definitions | true |
| MT07-6 | 给出OLS解(CᵀC)^−1CᵀδO，要求normal matrix非奇异；方差以零均值、同方差、不相关模型残差假设及Nc−m自由度估计。Table误差是理论配置拟合误差，不是实验寿命σ或完整理论系统误差。 | model-statistical-method-and-boundary | direct-and-derived | PDF p.6 Eqs.(24)–(28) | true |
| MT07-7 | Figs.5–6比较计算配置的self-consistent量与additivity近似之差；作者据选定集的窄分布支持可加性。183/105不是新测band/独立实验数，未排除所有EDF、reference或其他构型系统误差。 | model-validation-and-scope | direct-and-derived | PDF p.11 Eq.(34); PDF p.12 Figs.5–6 | true |
| MT07-8 | Fig4闭点/误差条为实验输入、空点为CRMF；数据取Refs20 Riley2001与21 Laird2002，正文说它们来自一次覆盖多个核素的差分寿命实验。本工作不新增独立τ测量。 | acquisition-lineage-and-model-comparison | direct-and-secondary | PDF p.2 experimental overview; PDF p.10 Fig4; PDF p.14 Refs20–21 | true |
| MT07-9 | 源文给calculated core Qt=7.64 eb，并提出可改用Ref39转述的7.4(3) eb实验baseline；这是另一绝对reference输入，不等于Fig4提供了新的绝对寿命分析。原Ref39本轮未读，标签还有MT07-13版本边界。 | source-reported-model-and-experimental-input | direct-and-secondary | PDF p.9 Eqs.(30)–(32); PDF p.14 Ref39 | true |
| MT07-10 | v1 TableII CHF ν[402]5/2,+i印(q20,q22,qt)=(−.35,.14,−.04) eb。在共享C/同权线性估计器且用Eq15的条件下，末项与前两项中心值偏差约+.390829 eb，超过两位小数舍入必要界限；不判实际代码或给替换值。 | conditional-source-table-audit | derived | PDF p.11 TableII CHF ν[402]5/2,+i | true |
| MT07-11 | v1 TableII CHF π[532]5/2,+i印(.43,−.05,−.46) eb；同上述条件的偏差约−.918868 eb，也不能仅以两位小数舍入解释。实际C/权重/VOR缺失，保留条件而不修表。 | conditional-source-table-audit | derived | PDF p.11 TableII CHF π[532]5/2,+i | true |
| MT07-12 | Eq14文字/左端为x推转，中间项却标ω∥y；本次使用其右端与Eq15作terminal-expression控制，未将该链全式静默修正。 | literal-version-boundary | direct | PDF p.4 Eq.(14) | true |
| MT07-13 | Eq31上方印core 131Cs，而p7正文、占据blocks和Fig2用131Ce。原标保留；不把7.64或7.4(3)当已独立核原实验的核素数值。 | literal-reference-label-boundary | direct | PDF p.9 core paragraph above Eq.(31) | true |
| MT07-14 | Fig4 inset及正文为142Sm，caption却印132Sm；图中Z62/N80也对应A142。保留caption冲突，不自动当已核官方勘误或新核素证据。 | literal-version-and-identity-boundary | direct-and-derived | PDF p.10 Fig4 inset and caption | true |
| MT07-15 | Eq33中CG bracket未显平方。本轮没有用它作τ/B(E2)/Qt换算；沿用其他已核rate约定前须确认幂次、单位和geometry，不能直接移植这份字面式。 | literal-rate-formula-boundary | direct | PDF p.9 Eq.(33) | true |
| MT07-16 | p7的occupied core与hole叙述包含π[404]9/2，TableI的A130 p/h栏却标p；本次未据该栏重建actual C，也不选择一个标签当作者代码输入。 | literal-occupation-label-boundary | direct | PDF p.7 core/hole paragraph; PDF p.8 TableI π[404]9/2 | true |
| MT07-17 | 对齐的误差和极化更复杂，含time-odd fields；作者要求宽频率范围比较，且不能像非自洽Nilsson图那样从routhian斜率直接取bare alignment。 | model-limitation | direct | PDF p.10 Sec.III.C | true |
| MT07-18 | 以源core为参考的声明1p1h应用，移除ν6_1,−i并增加ν6_2,+i，neutron数和N6 intruder总count不变；所报有效系数给CHF/CRMF的名义δQt约+.11/+.04eb、δJ约−1.36/−1.44ℏ。这不是实际重跑或测量，且不是沿同位素链改变N的同一比较；仅看intruder数不足以唯一指认状态。 | declared-application-of-model-coefficients | derived | PDF p.11 TableII ν6_1/ν6_2; PDF p.12 TableIII ν6_1/ν6_2 | true |

## Table and Operator Cross-Check

[[transition-quadrupole-moment]]“从旋转系算符到Qt的输入契约”记录本任务24项验证。实际扫TableII 34行，61组完整triple，7组CRMF空项保留None。假定每个中心值最近舍入到.01 eb，且共同reference减法、设计/估计器使系数满足Eq15，则残差的必要界限为`.005(2+1/sqrt3)≈.012887 eb`；MT07-10/11两组超界。其余59组通过这一必要舍入检查，不是对其模型正确性的全面认证。

在将表中理论误差当对应σ并考虑其两位小数舍入的条件下，逐组Cauchy/rounding必要区间均有相容空间；这**没有恢复真实跨observable covariance**。不能忽略误差舍入或实际估计器前提去反推精确相关系数。共享C的控制验证系数线性，不同权重控制说明该前提必要；实际配置/权重文件未给，不能判两条异常的最终原因。

### TableII v1的可复用数值矩阵

以下均为模型系数与其理论fit误差，单位eb；按原表保留两条⚠，未填补缺项。未标⚠仅表示通过前述必要舍入检查，不是human review或物理正确性认证。来源定位：PDF p.11 TableII。

| Row / state | CHF+SLy4 (q20; q22; qt) | CRMF+NL1 (q20; q22; qt) |
| --- | --- | --- |
| 1 nu[402]5/2,+i ⚠ | –0.35±0.01; 0.14±0.06; –0.04±0.04 | –0.26±0.02; –0.02±0.01; –0.25±0.02 |
| 2 nu[402]5/2,-i | –0.34±0.02; 0.08±0.08; –0.38±0.05 | –0.26±0.02; –0.07±0.02; –0.22±0.03 |
| 3 nu[411]1/2,+i | –0.15±0.02; –0.24±0.10; –0.01±0.06 | –0.11±0.02; 0.09±0.02; –0.16±0.02 |
| 4 nu[411]1/2,-i | –0.12±0.01; 0.06±0.06; –0.16±0.04 | –0.06±0.02; –0.17±0.02; 0.04±0.02 |
| 5 nu[411]3/2,+i | –0.15±0.04; 0.20±0.20; –0.26±0.12 | –0.13±0.03; –0.02±0.03; –0.11±0.03 |
| 6 nu[411]3/2,-i | –0.11±0.05; –0.05±0.24; –0.08±0.15 | –0.12±0.03; 0.02±0.03; –0.12±0.03 |
| 7 nu[413]5/2,+i | –0.13±0.02; –0.05±0.10; –0.10±0.06 | –0.13±0.03; –0.04±0.03; –0.10±0.03 |
| 8 nu[413]5/2,-i | –0.12±0.03; –0.12±0.13; –0.05±0.08 | –0.11±0.02; 0.15±0.03; –0.20±0.03 |
| 9 nu[523]7/2,+i | 0.03±0.01; –0.00±0.05; 0.03±0.03 | 0.05±0.01; 0.00±0.01; 0.04±0.01 |
| 10 nu[523]7/2,-i | 0.04±0.01; –0.01±0.05; 0.05±0.03 | 0.01±0.02; –0.00±0.02; 0.01±0.02 |
| 11 nu[530]1/2,+i | 0.22±0.01; –0.21±0.05; 0.34±0.03 | 0.17±0.01; –0.09±0.01; 0.22±0.01 |
| 12 nu[530]1/2,-i | 0.17±0.01; –0.01±0.05; 0.18±0.03 | 0.19±0.01; 0.10±0.01; 0.13±0.01 |
| 13 nu[532]3/2,+i | 0.21±0.03; 0.21±0.13; 0.09±0.08 | 未列 |
| 14 nu[532]3/2,-i | 0.17±0.03; 0.03±0.13; 0.15±0.08 | 未列 |
| 15 nu[532]5/2,+i | 0.19±0.03; –0.08±0.20; 0.24±0.12 | 0.17±0.03; –0.02±0.03; 0.18±0.03 |
| 16 nu[532]5/2,-i | 0.24±0.03; –0.01±0.20; 0.25±0.12 | 0.38±0.03; 0.00±0.03; 0.38±0.03 |
| 17 nu[541]1/2,+i | 0.35±0.03; –0.04±0.13; 0.38±0.08 | 0.35±0.02; –0.00±0.02; 0.35±0.03 |
| 18 nu[541]1/2,-i | 0.37±0.03; 0.01±0.14; 0.36±0.08 | 0.33±0.03; 0.04±0.03; 0.30±0.03 |
| 19 nu6_1,-i | 0.38±0.01; 0.21±0.03; 0.26±0.02 | 0.40±0.01; 0.12±0.01; 0.33±0.01 |
| 20 nu6_2,+i | 0.36±0.01; –0.01±0.04; 0.37±0.03 | 0.36±0.01; –0.01±0.01; 0.37±0.01 |
| 21 nu6_3,-i | 0.35±0.05; –0.06±0.22; 0.38±0.13 | 未列 |
| 22 pi[301]1/2,+i | 0.51±0.05; –0.10±0.24; 0.57±0.14 | 未列 |
| 23 pi[404]9/2,+i | –0.32±0.01; 0.10±0.04; –0.38±0.02 | –0.37±0.01; 0.02±0.01; –0.38±0.01 |
| 24 pi[404]9/2,-i | –0.32±0.01; 0.09±0.04; –0.37±0.02 | –0.37±0.01; 0.02±0.01; –0.38±0.01 |
| 25 pi[411]3/2,+i | –0.05±0.02; 0.10±0.07; –0.10±0.05 | 未列 |
| 26 pi[411]3/2,-i | 0.00±0.01; –0.22±0.07; 0.12±0.04 | 未列 |
| 27 pi[422]3/2,+i | 0.33±0.02; –0.27±0.10; 0.48±0.06 | 0.33±0.03; –0.13±0.02; 0.40±0.03 |
| 28 pi[422]3/2,-i | 0.34±0.02; 0.14±0.10; 0.25±0.06 | 0.28±0.02; 0.16±0.02; 0.19±0.02 |
| 29 pi[532]5/2,+i ⚠ | 0.43±0.01; –0.05±0.05; –0.46±0.03 | 0.41±0.02; –0.04±0.01; 0.43±0.02 |
| 30 pi[532]5/2,-i | 0.56±0.03; –0.07±0.09; 0.60±0.05 | 0.54±0.03; 0.05±0.03; 0.51±0.04 |
| 31 pi[541]1/2,-i | 0.58±0.02; –0.01±0.10; 0.59±0.06 | 未列 |
| 32 pi[541]3/2,+i | 0.50±0.01; –0.05±0.06; 0.52±0.04 | 0.48±0.01; –0.10±0.01; 0.54±0.01 |
| 33 pi[541]3/2,-i | 0.57±0.01; –0.12±0.04; 0.63±0.03 | 0.50±0.01; –0.10±0.01; 0.56±0.01 |
| 34 pi[550]1/2,-i | 0.49±0.05; –0.06±0.22; 0.52±0.14 | 0.47±0.04; –0.02±0.04; 0.48±0.04 |

## Competing Interpretations and Limitations

加性模型包含极化，不是bare单粒子矩的简单相加。该文检验的是无配对、固定频率、选定高形变/SD组态集；配置混合、配对和跨越稳定轴/形状分支会限制迁移。作者也承认对齐不如四极矩精确。相近两种EDF结果不是独立实验确认。

Qt只给特定rotating-frame线性组合；单一Qt不能唯一解Q20/Q22/γ。坐标的x/y变换、signedγ和物理相对转轴须分别处理；同A≈130核区不保证可把该方法系数直接移给136Pr。

## Counter-Evidence and Missing Companion Observables

必要伴随材料是明确reference与occupied标签、共同C/权重/各配置输出与残差、实际转轴/几何、原寿命/feeding/branching/系统误差链。原始Laird2002数据分析未读，Fig4只可作已知上游输入的模型比较；不能拿来给Pr136生成新寿命或实验γ。

差分量的common-systematic处理也需定义：一个共同加性offset可在difference中取消，共同multiplicative normalization则在ratio中取消，通常不会在非零difference中取消。这里是定义控制，不是对Laird实际方法的反证；原分析仍待直接核验。

## Related Knowledge and Project Relations

- `methodological-bridge` → [[transition-quadrupole-moment]]：坐标/转轴和operator归一、系数线性、模型fit误差与实验提取分开。
- `limits` → [[configuration-occupation-audit]]：真实奇A reference例子不等于Pr136实际reference；p/h标签不能跨core移植。
- `foundational-background` → [[a130-model-choice-card]]：提供CHF/CRMF方法与迁移边界，不新增PSM/TPSM投影覆盖。
- [[petrache-2015-nd-exotic-rotations-triaxiality]] Ref47是本理论研究；其Ref32/46重复Laird文献也不增加独立测量。

## Knowledge Impact and Learning Decision

Decision: **supports** Qt需要实际坐标/几何与reference，**limits** 单一Qt反演γ、将模型fit误差当实验σ或不筛版本地照搬表值。固化source、Qt observable、reference审计与model-choice卡，不新建核素/独立研究note。原Pr136 π、转轴/共存和2/7投影覆盖不变。overview update deferred：当前为同一证据链的必要方法校准。

## Agent self-audit triage

- **P0: none identified**。paper身份/hash/版本已核；数值使用限于明确的v1/条件审计，未采用歧义作实验结论。
- **P1 / MT07-10–16**：保留准确locator、舍入和共享估计器前提；不修表/核素/公式，不称official erratum或代码错误。VOR和原输入未得。
- **P1 / MT07-4–8、17**：无配对/固定频率/筛配置范围、残差假设与原实验复用必须保留；误差条不是完整理论或实验置信度。
- **P1 / MT07-2、9**：坐标变换不等于不同EDF同预测；7.4(3)是Ref39转述，未重读原始实验，不能独立加权。
- **P2**：raw保留槽与空citation key列入lint；原PDF/已有review不改。

## Extracted Pages

- Observables: [[transition-quadrupole-moment]]
- Methods: [[configuration-occupation-audit]]
- Projects: [[a130-model-choice-card]]

## Provenance

- [arXiv v1](https://arxiv.org/pdf/0707.4324v1)与[DOI](https://doi.org/10.1103/PhysRevC.76.034304)：本文locator/版本与书目身份。
- [reading audit](../../outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/matev2007-reading-audit.json)、[24-check审计](../../outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/matev2007-qt-operator-audit.json)、[程序](../../system/scripts/day14_qt_operator_table_audit.py)。
