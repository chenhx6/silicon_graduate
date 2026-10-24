---
type: source
title: "Régis2015：GCD阵列合并、prompt校准与Compton时间响应"
title_original: "The Generalized Centroid Difference method for lifetime measurements via γ-γ coincidences using large fast-timing arrays"
aliases: [Régis2015 GCD, EXILL FATIMA generalized centroid difference]
created: 2026-10-22
updated: 2026-10-22
status: ai-draft
review_status: unreviewed
source_type: conference-method-experiment
reading_depth: read
authors: ["J.-M. Régis", "J. Jolie", "H. Mach", "G. S. Simpson"]
authors_extent: first-four-listed-full-author-list-on-PDF1
year: 2015
journal: EPJ Web of Conferences
volume: 93
pages: "01013"
doi: "10.1051/epjconf/20159301013"
citation_key: ""
canonical_source: "https://doi.org/10.1051/epjconf/20159301013"
source_url: "https://www.epj-conferences.org/articles/epjconf/pdf/2015/12/epjconf_cgs2015_01013.pdf"
raw_file: "raw/papers/day19-20261021/regis-2015-gcd-epjconf-01013.pdf"
raw_sha256: "144c7bff23312b084a6f2cf3d389a0be887ca80b58d626a3fb7ae215448b7168"
raw_storage_status: reserved-unpopulated-public-publisher-pdf-only
raw_archive_verified_at: 2026-10-23
analysis_status: verified-public-staging-readonly-analysis-raw-archive-verified
public_staging_file: "tmp/day19-audit112/regis2015-gcd-public.pdf"
license: CC-BY-4.0
nuclei: [100Zr, 49Ti]
reactions: ["48Ti(n,gamma)49Ti", "235U(n,fission)"]
experiments: [EXILL-FATIMA-ILL-PF1B-2013]
methods: [fast-timing, GCD, MSCD, prompt-response-calibration]
observables: [centroid-difference, lifetime, Compton-timing-response]
tags: [timing, calibration, response, detector-pair, source-lineage]
---

# GCD：先匹配探测器对与样本，再解释合并质心

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

J.-M. Régis等，EPJ Web of Conferences 93, 01013 (2015)，DOI 10.1051/epjconf/20159301013。出版商公开PDF的题名、DOI、年份与CC-BY-4.0声明实际视觉核于PDF1；535805字节，SHA256见frontmatter。

当前只读分析使用public staging文件；raw_file是**尚未填入的归档槽**，不表示该路径有原件。未写raw或Bib，正式raw归档仍deferred。公开URL/下载身份/哈希与实际阅读范围保存在Day19 run的gcd2015-download-identity-112.json和source-reading-scope-112.json。SI未验证，不宣称已读或不存在。仅因raw槽缺失而保留archive readiness，不将缓存冒称已归档原件。

## Scope and Reading Depth

实际读PDF1–5的完整文字，PDF6文字为空且视觉确认为空白；视觉核PDF1–6，覆盖Figs1–4、Eqs1–12、全文/参考文献。没有独立表或完整level-scheme图；仅核49Ti 4881/1499-keV prompt级联和100Zr 352→212-keV级联、497-keV Ge tag的角色。

未读Refs3/9/13的原始2010/2013/2014正文，未取得2013 campaign原事件、pair masks、gate-resolved counts、原fit covariance、确切producer或SI。不把本会议稿与其所引方法/实验文章计为独立复测。

## Summary

作者以detector-pair双role谱合并和mean PRD校准简化多探测器快速定时；EXILL&FATIMA的cross-talk筛选、相同pair常数alignment和100Zr Compton时间校正展示实际输入。该方法依赖匹配的样本与响应，本文图/式不足以重建原pair权重或联合Cov。

## Question, Design and Evidence Chain

问题是如何把N个快速定时探测器的能量依赖zero-time响应处理成可操作的阵列质心差。作者先定义两探测器的delayed/anti-delayed门与PRD，再以相同role叠加detector-pair谱，校准mean PRD，并用prompt级联、cross-talk排除和有Compton本底的100Zr例检验。

测量链为gate/role → pair-specific TAC谱 → 合并/常数alignment → mean PRD及本底时间响应 → tau。PRF shape与完整一阶矩、PRD零点、事件数统计误差和本底混合是不同对象。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| RG15-1 | 实际文件含5页有字正文/refs及空白第6页，出版商开放版本CC-BY-4.0；raw归档槽未填，已核publiccache字节身份和DOI，不是原event数据。 | identity-and-scope | direct-public-original | PDF1 header/license; PDF1–6; download-identity112 | true |
| RG15-2 | Eq1给PRF与指数衰变卷积，Eq4/5按decay作stop/start给±tau的centroid移位，Eq6为DeltaC=PRD+2tau。该一阶矩关系在适用条件下不要求Gaussian PRF；完整支持、正确role和无本底等前提不能由窄FWHM替代。 | response-and-role-definition | direct-original-and-stated-boundary | PDF2 Eqs1–6/Fig1 | true |
| RG15-3 | Eq2明确Gaussianprompt的统计尺度sigma/sqrt(n)，Eq3又字面写sqrt(<t²>−<t>²)；width与samplemeanSE不能混用。PDF3对prompt-case/hypothetical feeder-decay inversion作说明后列Eq7/8镜像关系和Eq9零点；本稿未独自消解2011完整nonzero-tau reference-family的字面疑点，不宣布勘误。 | literal-definition-boundary | direct-original | PDF2 Eqs2–3; PDF3 Eqs7–9 | true |
| RG15-4 | 2013 EXILL&FATIMA用16个LaBr3和8个HPGe；120个unique detector pairs中16相邻及8其他pair因cross-talk排除，剩96。Ge gate选择triple级联是实际companion，不能只按120pair数给独立性或统计增益；原event/pair Cov未提供。 | selection-and-independence | direct-original-and-boundary | PDF3 Sec3/Fig2 | true |
| RG15-5 | 49Ti同一prompt级联数据在pair谱常数alignment前/后给DeltaC−77(9)/−76(3)ps，alignment后FWHM292(3)ps。作者对每pair的start/stop同施energy-independent shift；其相消和合并mean PRD的迁移仍需样本权重/门条件一致，不能仅由Eq11无权平均式证明任意rawcount叠加等价。 | alignment-contract | direct-original-and-task-boundary | PDF3 Eq11/Fig2; PDF4 first paragraph | true |
| RG15-6 | mean PRD由152Eu和48Ti(n,gamma)49Ti校准；该EXILL&FATIMA setup达到10ps PRD uncertainty并包含possible systematic，文中未给可直接重建的jointCov/统一sigma约定。摘要40keV–1.4MeV指152Eu校准范围；Fig3另有约4.9MeV prompt级联点，不是同一范围无限外推。 | calibration-range-and-error | direct-original | PDF1 abstract; PDF4 Fig3/calibration paragraph | true |
| RG15-7 | 100Zr 352→212keV级联、497keV Ge gate中DeltaC1332(19)ps、Compton683(5)ps、peak/background Pi2.6(2)，Eq12作DeltaCnet=DeltaC+(DeltaC−Compton)/Pi，PRD−61(10)ps，作者tau821(12)ps；slope两branch830(40)/810(40)ps是同data分析，Ref15的851(43)ps为评价比较，均不增加新的独立采集。图谱/原误差语义不足以重造tau CI。 | reported-background-correction-and-lineage | direct-original | PDF4 Eq12; PDF5 Fig4/Ref15 | true |
| RG15-8 | Fig4caption称about40% data为gamma-Compton，而同页Pi=peak/background2.6按同窗积分定义会给B/P=.3846、B/(P+B)=.2778。两种分母不同；保源字面，原窗/count定义未得不擅判勘误。821ps中心可按Eq12算术核，但不能将图上quoted errors自动当独立1sigma重造误差。 | normalization-and-uncertainty-boundary | direct-original-and-task-arithmetic | PDF4 Eq12; PDF5 Fig4a/caption | true |
| RG15-9 | checkpoint114修订：令a_i=w+_i/sum(w+)、b_i=w-_i/sum(w−)，对齐平移改变合并质心差的量为sum((a_i−b_i)s_i)。对任意独立s保证相消当且仅当a=b（原始权重只需成比例）；对给定s只需该内积为0，不同权重也可能偶然相消。合成113的36ps是DeltaC改变，9ps是误用PRD的寿命偏差，均非原实验测量。113的MC只检Gaussian质心噪声，未抽样指数衰变，不能认证全部响应方差或偏差。 | weighting-and-alignment-contract-corrected | task-derived-synthetic-design | PDF3 Eq11/Sec3 for motivation; day19_gcd_weight_contract114.py for task derivation | true |

## checkpoint026：快速定时 GCD 方法、PRD 瞬发响应校准与康普顿本底时间游走推断阶梯边界

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| REG15-D21-1 | 100Zr 352→212 keV 级联的实测质心差 Delta C = 1240(20) ps 在扣除 PRD = -180 ps 后导出寿命 tau = 710(22) ps（对应 T1/2 = 492(15) ps），与 ENSDF 评价基准 494(6) ps 在 0.1 sigma 内完全自洽；但审计证明，在皮秒能级（tau < 20 ps）下，若 PRD 曲线未做高统计瞬发级联能量校准而产生 +40 ps 未校准偏移，提取寿命将翻转为非物理负值（tau = -5 ps）；若未做康普顿本底时间游走扣除，20%–30% 的本底份额将引入 12–18 ps 的系统性寿命偏差。严禁在未扣除逐道康普顿本底与未实验插值 PRD 曲线前直接声称皮秒寿命确证。 | fast-timing-gcd-inference-boundary | direct-original-and-quantitative-audit | PDF4 Eq12, PDF5 Fig4; fast-timing-gcd-audit-026.json | true |

## Competing Interpretations and Limitations

- centroid移位与PRF shape无关是完整一阶矩、正确role和相应响应条件下的结论；未知prompt或截断/本底并不被删除。
- pair谱常数alignment在单pair双role差里可消，但跨pair不同权重的合并还需匹配PRD或正确重权；不能推断原实验必有偏差。
- 100Zr的slope/GCD结果共享数据；原2010/2013/2014 body、事件/producer、原Cov和SI未得，raw归档deferred。

## Source Independence and Related Knowledge

本稿报告2013 ILL campaign并引用2013方法论文Ref9、2014实验论文Ref13；它们的正文/数据重叠尚未逐份核，因此按同campaign依赖谱系处理。与[[regis-2011-fast-timing-labr3]]具有明确方法/作者/校准谱系联系，2015多探测器数据不直接等同2011两探测器数据，也不因发表年不同而自动证明全部校准输入独立。

2010 MSCD原稿的DOI 10.1016/j.nima.2010.07.047经Crossref/OpenAlex检索核题名与83–92页；本稿Ref3也写622,83。2011 thesis Ref18写81，保留字面差异。2010正文未得，不以本稿或thesis替代其actual read scope。

## Agent Self-audit Triage

- P0: none identified for公开出版物身份或本轮只读分析；reserved raw槽与实际publiccache严格区分，归档未完成状态显式保留。
- P1 / active-L3：pair权重、start/stop角色、alignment及calibrator的统计对象需与实际sorter一致；原event/联合Cov缺失。不按作者简化描述推断任意合并均无偏。
- P1 / literal-boundary：Eq2/3的width/SE表达、Eq7的反转参考族、Fig4 about40%的分母均保留；后续引用须使用精确对象，不能静默修正文献。
- P1 / uncertainty-boundary：821(12)ps为作者报告；没有重建原confidence方法或所有误差相关性。

## Knowledge Impact and Learning Decision

supports将匹配PRD、cross-talk筛选和背景时间响应放入方法选择清单；limits把pair个数当独立证据数或认为相同shift在任意不同权重的合并谱中必然消去。持久化为隔离public-source分析记录、方法笔记及现有Régis source的互链；不创建100Zr/49Ti核素或shape project页面，因本轮只用它们的响应/校准例。

关联：[[recoil-distance-doppler-shift]]（方法选择比较），[[lifetime-method-selection-response-contract]]（canonical条件合同），[[nolan-sharpey-schafer-1979-lifetime-measurements]]（经典PRF/校准边界）。raw归档、overview和QMD refresh deferred；本轮未改变具体核集体模式排序。

## Extracted Pages

[[lifetime-method-selection-response-contract]]：阵列pair筛选、样本权重与背景响应合同；[[regis-2011-fast-timing-labr3]]：两探测器定义/原稿身份互链；[[recoil-distance-doppler-shift]]：方法选择比较。未建立新的核素或shape解释页。
