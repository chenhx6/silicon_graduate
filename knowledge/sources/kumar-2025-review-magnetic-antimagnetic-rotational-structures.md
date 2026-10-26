---
type: source
title: "Review of Magnetic- and Antimagnetic-Rotational Structures in Nuclei"
aliases: [Kumar 2025 magnetic antimagnetic rotation review]
created: 2026-07-15
updated: 2026-10-26
status: ai-draft
review_status: unreviewed
source_type: journal-article-review
reading_depth: deep-read
title_original: "Review of magnetic- and antimagnetic-rotational structures in nuclei"
authors: [Sushil Kumar, Sukhjeet Singh, Balraj Singh, Amita, Ashok Kumar Jain]
journal: Atomic Data and Nuclear Data Tables
year: 2025
volume: 165
pages: 101735
doi: 10.1016/j.adt.2025.101735
language: en
canonical_source: doi:10.1016/j.adt.2025.101735
zotero_item_key:
citation_key: kumar_2025_Reviewmagnetic
zotero_uri:
library_file:
raw_file: "raw/papers/2025_Kumar et al_Review of magnetic- and antimagnetic-rotational structures in nuclei.pdf"
raw_sha256: 3E7EECF9CB084AA24174A41886A0B2372B00322C3343AB2825D1F142BD76567E
nuclei: []
reactions: []
experiments: []
models: [tilted-axis-cranking, particle-rotor-model, cranked-shell-model]
observables: [bm1-be2-ratio, b-m1, b-e2, moments-of-inertia, level-lifetimes]
methods: [in-beam-gamma-spectroscopy, lifetime-measurement, angular-correlation]
tags: [magnetic-rotation, antimagnetic-rotation, shears, review, high-spin]
---

# Kumar 等（2025）：磁转动与反磁转动结构综述

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

Atomic Data and Nuclear Data Tables 165 (2025) 101735. DOI `10.1016/j.adt.2025.101735`; BibTeX key `kumar_2025_Reviewmagnetic`。

## Scope and Reading Depth

全文 deep-read，覆盖 MR/AMR 一般性质、shears 几何、TAC/PRM 等模型背景、判据、数据表说明、歧义排除案例和结论。文献汇编截止 2025-03-31，整理 117 个核中的 228 个 magnetic-rotational（MR/shears）结构和 28 个核中的 40 个 antimagnetic-rotational（AMR）结构。表中数值主要来自原始论文、ENSDF、XUNDL 和 NSR；本文不是这些实验的原始观测来源。

## Summary

综述把 MR 与 AMR 作为弱形变或近球形背景中的高 `j` 角动量耦合问题来整理。MR 的典型图像是粒子-空穴 shears blades 逐渐闭合，产生强 M1、弱 E2 和随自旋下降的 `B(M1)`；AMR 则由两组相反磁矩的 shears 近似抵消，通常表现为 `Delta I=2`、很弱且随自旋下降的 E2。作者同时强调，许多文献中的 MR/AMR 标签仍是 tentative，缺少寿命、`B(M1)`/`B(E2)` 或细致模型时不能作 firm assignment。

## Experimental or Theoretical Setup

- Review/compendium；无新的反应、探测器或 level scheme 数据集。
- 汇总原始来源提供的 gamma 能量、能级、自旋宇称、寿命、`B(M1)`、`B(E2)`、比值和可能组态。
- 用 TAC、CSM、CNS、PRM 及相关模型解释候选带，但模型标签与实验观测分开记录。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KU25-1 | 作者的汇编范围是 117 个核中的 228 个 MR/shears 结构和 28 个核中的 40 个 AMR 结构；截止日期为 2025-03-31。 | review-background | direct | PDF pp.1-2, Abstract and Introduction | true |
| KU25-2 | 多数 MR 候选呈近似 `I(I+1)` 的能级趋势、强 `Delta I=1` M1 带内跃迁、弱 E2 crossover 和较大的 `B(M1)/B(E2)`；这些是统计性特征，不是单独充分判据。 | review-background / experimental-criteria | direct | PDF pp.2-3, Sec.2 and Table 1 | true |
| KU25-3 | 综述列出 MR 常用的经验范围：`B(M1)` 约为 `2-10 mu_N^2`、`B(E2)` 可低至 `1-0.01 (eb)^2`，以及 `J^(2)/B(E2)` 通常大于约 `150 MeV^-1(eb)^-2`；具体适用性取决于核素和数据质量。 | review-background / experimental-criteria | direct | PDF pp.2-3, Sec.2, Eq.(1), Table 1 | true |
| KU25-4 | shears 机制把高 `j` 质子粒子与中子空穴角动量看作两把 blade；随自旋增加，夹角减小、垂直磁矩 `mu_perp` 减小，因此 `B(M1)` 的下降趋势是重要但模型依赖的 MR 证据。 | review-background / model-result | direct | PDF pp.2-4, Sec.3 and Fig.1 | true |
| KU25-5 | AMR 由两组 shears 的横向磁矩近似相消；常见结构是 `Delta I=2` 序列、弱 E2，且 `B(E2)` 随自旋下降。作者给出的 `J^(2)/B(E2)` 大于约 `100 MeV^-1(eb)^-2` 是经验筛选条件，而非普适定律。 | review-background / experimental-criteria | direct | PDF pp.4-5, Sec.3, Fig.4 and AMR discussion | true |
| KU25-6 | 作者总结 MR/AMR 需要粒子-空穴耦合、较大的 active `j` 和足够小的芯形变，以避免普通集体转动压过 shears 机制；这些是配置与模型前提。 | review-background / model-formalism | direct | PDF p.3, MR conditions; p.4, AMR conditions | true |
| KU25-7 | 综述指出约只有三成 MR 表和少数 AMR 结构有寿命、`B(M1)`、`B(E2)` 和详细模型的联合信息；缺少这些信息时，规则能级序列也可能是 collective、signature-partner 或其他激发。 | author-synthesis / evidence-gap | direct | PDF pp.4-6, Conclusions and data-availability discussion | true |
| KU25-8 | 作者因实验数据或模型不足排除了若干文献中的 MR-like 候选，并保留 established、likely、tentative 等不同等级；这说明“dipole band”或 M1 假设不能自动升级为 MR。 | review-background / evidence-policy | direct | PDF p.5, Sec.5 and table policies | true |
| KU25-9 | 综述中的表格数据原则上取自原始 publications，部分缺失能级来自 ENSDF/XUNDL 或作者推断；因此表格可用于候选筛选，但进入 paper evidence gate 仍需回到原始 source。 | method-formalism / review-background | direct | PDF pp.5-6, Policies and Explanation of Table | true |
| KU25-10 | 对当前 wobbling 研究，MR/AMR 证据链提供一个竞争解释框架：M1/E2、`J^(2)`、寿命和配置几何可帮助区分 shears、普通集体转动、signature partner 与 wobbling，但本综述不裁决任何 A≈130 争议。 | Wiki synthesis / project note | direct | Cross-source comparison; Secs.2-6 | true |

## Analytical Reconstruction

作者先用大样本汇编建立 MR/AMR 的候选筛选，再用 shears 角动量几何解释 `B(M1)`、`B(E2)` 和能级趋势，最后以寿命和详细模型的缺失率说明 assignment 的不确定性。证据链的关键不是某个比值的阈值，而是配置、multipolarity、寿命和模型几何是否相互一致。

## Competing Interpretations and Limitations

- 本文的核素和带表格是 review/background；具体 gamma、寿命和组态不可当作本文原始实验结果。
- 强 M1、弱 E2、规则能级或大的 `J^(2)/B(E2)` 都可能在配置混合、signature partners、普通集体/倾斜转动或数据缺失时出现。
- 表中 tentative/probable/configuration-from-model 标记必须保留；缺寿命时不应写成 firm MR/AMR。
- MR/AMR 与 wobbling、chirality、tilted precession 的角动量图像有交叉，但物理自由度和判据不同，不能只凭“倾斜”一词合并。

## Related Concepts, Models and Projects

- Concepts: [[magnetic-rotation]], [[antimagnetic-rotation]], [[shears-mechanism]], [[band-termination]], [[angular-momentum-alignment]]
- Models: [[tilted-axis-cranking]], [[cranked-shell-model]], [[particle-rotor-model]]
- Project context: [[low-spin-wobbling-controversies]]

## Project Relation

为现有 wobbling project 增加 MR/AMR 竞争解释的 review 背景，特别是“寿命和 `B(M1)/B(E2)` 缺失会限制 firm assignment”的证据门槛。该页不把表中任何核素自动加入 wobbling 或 MR evidence matrix。

## Human Review Triage

### P0 Focus

1. **KU25-2--KU25-5, PDF pp.2-5, review-background/experimental-criteria.** 核对 MR/AMR 的 Delta-I、M1/E2、`B(M1)`/`B(E2)` 和 `J^(2)/B(E2)` 表述，确认阈值没有被写成普适定律。
2. **KU25-7/KU25-8, PDF pp.4-6, evidence-gap/review-background.** 核对“约三成”联合寿命/模型覆盖和 ambiguous-candidate 排除逻辑。
3. **KU25-9, PDF pp.5-6, method-formalism.** 核对表格数据来源政策，避免把 ENSDF/XUNDL 或作者推断当作原始实验定位。

### Remaining P0

- **KU25-1/KU25-6/KU25-10**：核对综述范围、shears 前提和与 wobbling project 的迁移边界。

### P1

- 若未来需要某一 MR/AMR 核素的数值或 configuration，应从本页表格追溯到表中原始引用并单独摄入。

## Extracted Pages

- Concepts: [[magnetic-rotation]], [[antimagnetic-rotation]], [[shears-mechanism]], [[band-termination]], [[angular-momentum-alignment]]
- Models: [[tilted-axis-cranking]], [[cranked-shell-model]], [[particle-rotor-model]]
- Project: [[low-spin-wobbling-controversies]]

## Review Status

Page and all KU25 claims remain unreviewed with `needs_review: true`. Human review is deferred until use: perform targeted claim review when this content is used for paper writing, a key project decision, synthesis finalization or a paper-level evidence pool.


## Day17定向自审：110In同数据与能级能量口径

2026-10-20原Day17session的Day18无学分知识预习。旧全页与KU25-1–10逐字保留；新审计仍unreviewed/needs_review，不重称本session全文deepread。本次实际视觉/文本为PDF5/49/50/59/60；文字检索还暴露PDF47/48的Cd表，未完整视觉核。原PDF60页/hash `3e7eecf9cb084aa24174a41886a0b2372b00322c3343ab2825d1f142bd76567e`。

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KU25-11 | Table3的110In第二条序列列17/19/21/(23)四个寿命.774/.554/.403/.205ps和B(E2).136/.265/.266/.281(eb)²，引用2001Ch71；(25)/(27)/(29)只有能量/跃迁而无τ/B。本表没有给这三个点新增寿命。 | review-data / source-dependence | direct | PDF p.50, Table 3, 110In second band | true |
| KU25-12 | 同条的printed comment3称level energies未随spin monotonically increase，但表列Elevel从2220.2到12744.3keV严格增加；不单调的是Eγ，977.0→950.4→889.1后再升。这是literal词义不闭合，可能涉及spacing/rotor意图，不能擅改原句或据此声称实验能级倒置。 | review-wording / Codex table-check | direct-and-derived | PDF p.50, Table 3, 110In comment 3 | true |
| KU25-13 | PDF5的AMR经验特征包括近恒定J2、small/decreasing B(E2)，但同页明确证据稀缺、混合collective机制/判定限制；对110In的综述归类与原2001实验/2016模型不能作独立实验重复确认。 | review-background / independence-boundary | direct | PDF p.5, AMR discussion and Conclusions | true |
| KU25-14 | Ref26指向CHI01 PRC64 054314；Ref29指向Simons2005 PRC72 024318；Ref28与30–32指向其它Cd primary。这些是检索入口，不是本session已取得/读过Cd正文或已独立验证其τ、stopping、feeding。 | bibliography / access-boundary | direct | PDF p.59, References 26/28; PDF p.60, References 29–32 | true |
| KU25-15 | 本次110In原表复核：19/21/23的quoted marginal B(E2)区间交集为[.258,.279](eb)²；这只是一维box相容性，不是constant-B fit、jointCI或AMR概率。原CHI01 TableVI明确误差不含可能达±20%的stopping系统量，不能从综述抄表制造fullCov。 | Codex analysis / statistical-boundary | derived | PDF p.50, Table 3, 110In lifetime comment | true |

[计算输入](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/amr-review-energy-contract.json)与[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/amr-review-energy-result.json)；script `system/scripts/day17_amr_review_energy_audit.py`。10个Elevel差与印刷Eg残差小于7e−13keV只核抄录算术，不是实验能量精度。局部J2=4/ΔEg的负值处于回弯离散差分，不是负质量或新rotor fit；不把中点J2任意配端点B作精确阈值判定。

本次Crossref/arXiv/APS/OSTI/York/UNT/SemanticScholar多数TLS失败，OpenAlex一次取得Simons2005身份但无OA全文URL；没有新Cd正文。metadata/综述不能冒称新独立实验。见run内`amr-primary-discovery-access.json`/`amr-primary-discovery-secondary.json`，保持input-readiness，不调TLS/凭据。

## Day21周考推断阶梯审计：反磁转动全球汇编与寿命判据证据门边界

依据独立审计程序 `system/scripts/day21_checkpoint012_antimagnetic_rotation_audit.py` 与审计产物 `outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/antimagnetic-rotation-audit-012.json`，确立本源在推断阶梯上的边界：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| KU25-D21-1 | Kumar 2025 全球汇编确立反磁转动（AMR）推断阶梯边界：汇编的 28 个核中 40 个 AMR 结构仅少数具有绝对能级寿命测量与微观模型支持，多数仅具 $\Delta I = 2$ 能级特征；推断阶梯审计强调，无寿命支持的规则偶极/四极带极易与扁椭集体转动或常规能带终止发生假象重叠；确证反磁转动必须联合微观组态、带内 $B(E2)$ 随自旋单调暴跌以及特征比值 $\mathcal{J}^{(2)}/B(E2) > 100\ \hbar^2	ext{MeV}^{-1}(e	ext{b})^{-2}$，严禁将未测寿命的表观 $\Delta I = 2$ 序列轻率升格为确定 AMR 模式。 | claim-boundary-audit | direct-and-derived | PDF pp.4-6 Table 3; antimagnetic-rotation-audit-012.json | true |

## Day23：原AMR模型的外部核阅与独立性边界

本次本综述只作定向ref-index/AMR背景与Cd表的输入定位；60页raw SHA相符，全文文本提取不是新全文阅读声明。Simons2003 DOI10.1103/PhysRevLett.91.162501与Simons2005 DOI10.1103/PhysRevC.72.024318已实际Crossref核身份；前者APS Harvest401、普通PDF403，ANU公开馆藏页有摘要而无下载正文，OpenAlex两篇均无可用OA正文。访问失败不是原实验无效、未测寿命或不存在反证。

随后实际从`https://arxiv.org/pdf/1105.3622v2`取得Zhao/Peng/Liang/Ring/Meng, “Antimagnetic Rotation Band in Nuclei: A Microscopic Description”, PRL107,122501(2011), DOI10.1103/PhysRevLett.107.122501的公开10页版本。SHA256为a7f534e796f899f65f5dfb9d8b465caf7f1c52932d5c1f5c1b9e99dde0bf35ae，暂存`tmp/day23-originals/zhao2011-amr105cd.pdf`，完整读主线/refs并视觉核PDF3/5/6/7/8的Fig1–4、Eq1、限制。raw/本地Bib保护不改，**正式raw归档与独立source摄入deferred**；这里仅保存清楚标明原出处的外部核阅/provisional研究增量，不把该模型或图点冒称为本2025综述的新测量。arXiv标v2/2011-09-14而PDF内Dated2022-04-25分列，不据排版日期改论文年或认定新实验。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KU25-D23-001 | 外部原Zhao2011采用PC-PK1、x-z平面2D TAC、N=10 oscillator shells并忽略pairing；“no additional parameters”针对本模型使用已定functional，不是从未定标的第一性原理或忽略配对已获数据证明。其Fig3/4的观测点复用Choudhury2010 PRC82,061308(Ref11)，不是2011新增寿命采集。 | external-original-model-input-and-data-lineage | directly-read-external-original-with-archival-boundary | Zhao2011 arXiv1105.3622v2 PDF5 Eq.1 and implementation paragraphs; PDF7 Fig.3; PDF8 Fig.4; PDF10 Ref.11 | true |
| KU25-D23-002 | 外部原Zhao2011 Fig1/2支持其模型内双剪刀闭合，但所有粒子均参与而无inert core；除三价中子后作者给“corelike”增量约3ℏ，并指出低j中子混合使现象学固定core划分仅部分适用。这里的j/R/3ℏ为模型量，不是实测角动量分解；AMR横向磁矩相消图像也不推广为所有跨带M1禁戒或静态磁矩为0。 | external-microscopic-mechanism-and-core-partition-limit | directly-read-model-and-bounded-inference | Zhao2011 arXiv1105.3622v2 PDF3 Fig.1; PDF5–7 Fig.2 and neutron-mixing paragraphs | true |
| KU25-D23-003 | 外部原Zhao2011的“without polarization”是先求每频率107Sn势，再移去两个g9/2质子而冻结该势、放弃105Cd自洽重排；与selfconsistent情形相比，非自洽对照约17ℏ达最大I，Ω≥.5MeV处E2受压制。selfconsistent结果β约.2→.14、γ≤9°。polarization指密度/形变重排，非γ线偏振P；该ablation改变势/自洽性，不是固定H只换configuration标签，也不是第二次实验。 | external-model-ablation-and-observable-identity | directly-read-external-model | Zhao2011 arXiv1105.3622v2 PDF7–9 Fig.3/4 and107Sn frozen-potential paragraphs | true |

Knowledge Impact and Learning Decision：supports本卡AMR有具体微观支持链及形变/混合/自洽性伴随检验；limits把理想双剪刀闭合、M1抵消或decreasingB(E2)升级为唯一模式/硬门。原DSAM论文正文、2013Comment/Reply及原τ/feeding/branch系统误差未取得，不重造Cd逐点曲线或物理终审。Simons closed路线保为P1 retrieval/readiness，非技术性全局硬停。新claims仅Codex self-audit needs_review:true。

## Day23：105Cd实际γ谱新原件与DSAM评价字段

本节单独标明外部原文/评价，不把它们归为2025综述的新采集。M. Kumar Raju et al.，*High Spin Spectroscopy and Shape Evolution in105Cd*，arXiv1501.07655v1，对应PRC91,024319(2015)，DOI[10.1103/PhysRevC.91.024319](https://doi.org/10.1103/PhysRevC.91.024319)，由arXiv metadata与精确Crossref核定；v1实际13页/834222bytes，SHA256 c237e3c4d71df3de9369b31235a798aa900ad585321654ff8ef0d69e20bad3f2。正文/表/refs主线实际读完，fresh视觉核PDF3/6/11，未逐点重算所有模型曲线或称已核VoR内容。上传Jan2015与PDF题头Oct24,2018编译分开。PDF仅tmp/day23-originals/cd105-read051-raju2015.pdf，正式raw归档deferred。

另按[NNDC真实表单](https://www.nndc.bnl.gov/ensdf/DatasetFetchServlet)取得105048001,105CD adopted与105048006,105CD HI：两200/pre文本803/339行，只定向读header及目标B链时钟/γ，不称全NDS原读。response SHA依次8e64f15d2e1cbaa0f6ee0be954660fed580cc284cf0126858bce5792b8098103、30498af198124f733a74c9cfacb6cd25783a08c34c73ea33e7354121992a3da5，暂存tmp，未改raw。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| RA15-D23-001 | 实际2015原实验为92Mo(16O,2pn)、75MeV、1mg/cm²靶/10mgAu背衬、TIFR15clover，>2×10^9 fold≥2记录；它与评价所述2010Ch54的IUAC93MeV16O+94Zr、1.35mg靶/8.86mgAu、14clover不同采集。共享INGA名或低spin采用值不把逐事件/feeding/归一合成同样本。2015本文未给新DSAM寿命表，AMR/B(E2)趋势引用其Ref13的2010数据。 | primary-campaign-and-reused-lifetime-lineage | directly-read-external-primary-and-evaluation | Raju2015v1PDF1/2/10; PDF13Ref13; HI105048006 experimentheader | true |
| RA15-D23-002 | Eq1的RDCO用157/90角矩阵、TableI按539keV E2门；Eq2 ΔIPDCO=(aNperp−Nparallel)/(aNperp+Nparallel)，a=.99由133Ba/152Eu定，是散射asymmetry而非已除完整Q(E)的P或δ。105In强通道差谱用作同一采集的EM参考，不能当独立Cd偏振实验。近0仅可为可能混合提示，未由此唯一选δ。 | primary-response-and-observable-semantics | direct-external-primary | Raju2015v1PDF2Eqs1/2; PDF3Figs1/2; PDF6TableIcaption | true |
| RA15-D23-003 | TableI对yrast负宇称B4的905/1044/1179/1331分别采用E2，列ΔIPDCO约+.04(2)/+.12(7)/+.08(5)/+.22(9)；这些支持本次谱学EM身份，不是四个新绝对B(E2)。同表1009线27/2−→27/2−被指认为M1、Δ≈−.12(4)，属B3→B4连接。AMR特定对称横向磁矩抵消不等本核所有跨带M1被禁戒；该连接也不单独推翻B4的AMR解释。 | primary-companion-observables-and-M1-scope | direct-external-table-and-author-assignment | Raju2015v1PDF6TableI targetrows; PDF7/8B3discussion | true |
| RA15-D23-004 | 本文CSM/shape分析用β2约.151/γ约6°解释crossing，TPSM在固定β2=.150下扫γ，γ25.01°使若干激发带能量更合、yrast B4对γ较不敏感；γ-soft/rigid为作者模型解释而非新直接形变测量。作者指出高spin B3/B2波函数/能量偏差反映未含5或更多qp；这些模型与Zhao2011无pairing自洽2DTAC输入不同，不能说只换configuration同H或新独立寿命验证。 | primary-model-input-and-author-limit | direct-external-model-discussion | Raju2015v1PDF9–12 Figs11–16 andSecsIV A/B | true |
| CD19-D23-001 | 官方header为Lalkovski/Timar/Elekes，NDS161,1(2019)，CUT1-Apr-2019，记录block实际尾日期为202002，编译日期不作新采集年。HI明确cL T来自2010Ch54 DSAM，E/RI来自2015Ra02，多极性主要2015/1978资料；评价把不同观测来源归在同scheme，不自动提供它们的联合Cov或原2010stopping/SF误差。 | evaluated-field-provenance-and-version | actual-official-record | 105048006 H/cL T/cG E,RI/cG M headers; 105048001 H | true |
| CD19-D23-002 | HI B链的(27/2−)4248.0、(31/2−)5291.6、(35/2−)6471.0、(39/2−)7802.0、(43/2−)9267.0keV母态在ENSDF T1/2栏列.74PS(+10−7)/.43PS(6)/.277PS(+31−21)/.143PS(+21−20)/.164PS(+32−34)，相关γ为905/1044/1179/1331/1465。它们是评价转述的2010时钟，不是2015新寿命或meanτ；末态/其它band同spin时钟不能移用，目标只列一γ也不证明branch完整。本任务不据这些字段重建新τ/B或CI。 | evaluated-state-clock-and-quantity-role | actual-official-fixed-field-record | 105048006 L4248.0/G905; L5291.6/G1044; L6471.0/G1179; L7802.0/G1331; L9267.0/G1465 | true |

注：上条CD19-D23-001的记录尾日期实际字面为202002，对应文件版本；不据排版串改实验年份。原2010PRC82,061308全文仍未取得，源停能/SF/全branch/likelihood仍缺；2013Roy/Chattopadhyay Comment DOI10.1103/PhysRevC.87.059801仅metadata核定，未据题名臆测内容。猜测Reply87.059802返回ResourceNotFound，未建立该Reply身份；猜测Raju91.024320实际是无关Cr/Fe论文，已剔，正式本源DOI为verified91.024319。访问失败/无关结果不当物理反证，未把它们纳入AMR判票。

[[antimagnetic-rotation]]和[[signature-tip-shears-discrimination-contract]]承接AMR正支持、actualmultipole与寿命/模型依赖的分层。新claims均needs_review:true，原综述/来源review状态不变，不移植任何τ/Q/机时到Pr/Au。

## Day23：显式AMR子组态的Pauli角动量容量

本节为任务条件推导，原动机限于外部Zhao2011 PDF5引用的现象学占据，以及Raju2015 PDF10的同一组态：$\pi(g_{9/2})^{-2}\otimes\nu[h_{11/2}(g_{7/2})^2]$。两相同核子或空穴必须反对称化；不能将两个经典blade各长j直接相加成精确量子最大J。代码system/scripts/day23_amr_pauli_capacity.py从归一wedge嵌入构造完整两粒子空间中的总J，Casimir给出允许多重态，再按三角规则耦合。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KU25-D23-004 | 在冻结的上述显式占据内，两相同g9/2质子空穴允许J=0,2,4,6,8，wedge维数45；两g7/2中子允许J=0,2,4,6，维数28。再加不同轨道h11/2中子，显式中子子集最大J=23/2，总显式子集最大J=39/2；耦合总维数45×28×12=15120。此为Pauli/角动量条件数学，不是105Cd全部核子的微观模型。 | Codex-conditional-angular-momentum-derivation | derived-from-stated-occupancy | Zhao2011 PDF5 phenomenological configuration paragraph; Raju2015 PDF10 SecIV A configuration paragraph | true |
| KU25-D23-005 | 仅在其余自由度J=0且该占据冻结时，显式子集不能给I>39/2。若保持占据且接受源中较高自旋指派，(43/2−)/(47/2−)在该分解至少需另有2/4ℏ角动量。该必要下界既不测出唯一core R，也不否定AMR；最高自旋括号仍保留。Zhao自洽模型含全部核子、低j混合和corelike贡献，未假设这个inert remainder，不能被此条件界排除。 | Codex-conditional-bound-and-model-domain | derived-and-source-limited | Zhao2011 PDF5–7 all-nucleon and neutron-mixing paragraphs; Raju2015 PDF1 tentative47/2 abstract | true |

八项限定控制实际通过：wedge正交/总J扇区封闭、Hermiticity/对易代数、Casimir与每个J的2J+1维数、Pauli最大Mz和耦合维度。最大矩阵残差约6×10⁻14，只说明所述角代数实现；不认证实际占据、spin或实验模式。高spin Jπ、其它中子混合/参与和组态连续性是必要伴随检验；未生成新δ/g/B/Q/τ、CI、设施率或机时。见[[antimagnetic-rotation]]与[[signature-tip-shears-discrimination-contract]]；新needs_review:true，旧review不变。
