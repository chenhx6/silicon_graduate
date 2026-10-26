---
type: source
title: "Diversity of shapes and rotations in the γ-soft 130Ba nucleus"
aliases: [petrache-2019-diversity-shapes-rotations-130ba]
tags: [130ba, wobbling, source-lineage]
title_original: "Diversity of shapes and rotations in the γ-soft 130Ba nucleus"
year: 2019
canonical_source: "https://doi.org/10.1016/j.physletb.2019.06.040"
raw_file: "raw/papers/day23-20261025/petrache-2019-diversity-shapes-rotations-130ba.pdf"
raw_sha256: 98c3128b3d88528b56aa075748065dc2b1f13778a45ad3efedd3058a21a18340
raw_storage_status: reserved-unpopulated-public-staging-only
public_staging_file: "tmp/day23-originals/ba130-primary061-2019.pdf"
created: 2026-10-26
updated: 2026-10-26
status: ai-draft
review_status: unreviewed
source_type: experiment-and-model-article
reading_depth: deep-read
citation_key: petrache_2019_diversity130ba
doi: 10.1016/j.physletb.2019.06.040
nuclei: [130ba]
---

# Diversity of shapes and rotations in the γ-soft 130Ba nucleus

## Bibliographic Record

C. M. Petrache et al., Physics Letters B **795**, 241–247 (2019)。DOI为正文；补充URL https://ars.els-cdn.com/content/image/1-s2.0-S0370269319304228-mmc1.pdf 。
## Scope and Reading Depth

本轮直接公开出版商PDF正文已读，并核关键图表；原文件仅在tmp公开访问staging，raw正式归档deferred，绝不写成raw已存或human-reviewed。正文/附录页码与以下SHA可识别当前版本。

正文7页SHA256 `98c3128b3d88528b56aa075748065dc2b1f13778a45ad3efedd3058a21a18340`；补充4页SHA256 `d12be86b119f5d5212dac23b49fa7e4ab3ff855510fb6fd5eea6310a076b7cb7`。全文主线和图表的原读完成，不等于重放实验响应。

身份：C.M. Petrache et al., *Diversity of shapes and rotations in the γ-soft 130Ba nucleus: First observation of a t-band in the A=130 mass region*, PLB795(2019)241–247, DOI10.1016/j.physletb.2019.06.040；experiment-and-model-article。已读取7页全文及4页supp，原件身份哈希见worker reading-manifest；主代理决定合法canonical raw落点，本worker不改raw。

原实验槽：122Sn(13C,5n) 65MeV；GALILEO25个Ge分四环90°(10)、119°/129°/152°(各5)，EUCLIDES/Neutron Wall用于通道区分（p242 Sec2）。新识别S1′/S2o′连接带与t-band相关结构；形变、组态及轴示意均属于理论解释，不能写作直接形状测量。p243 Fig1与supp p2 Fig1分别提供身份/门控谱定位。

补充TableI仅D1/t带强度比；TableII D1的literal `νh²⊗πh⁻²`与主Table1/正文 `νh⁻²⊗πh²`存在符号差，保留needs_review而非按某一处强修。补充S1′行文字为γ-vibration/wobbling，不能追认原实验已唯一排除γ-vibration。

good-K对照：p245 Fig5前后原文解释，低自旋同一good-K带的CG系数可使B(E2;I→I−1)>B(E2;I→I−2)，t与K=8−均展示该性质。这里的out/in不应替代S1′→S1的带间定义。K=8固定Q的CG演算是本任务控制，证据类别必须记为derived-model-exercise，不是新实验数据。

磁算符与参数合同：p245 Table1给PRM各配置独立β/γ/J0/ξ，p244–245给不同轨道有效g；p246强调PSM/TAC的磁算符从多体波函数计算，不另引集体/单粒子g。t与K=8−相似B(M1)被作者认为有偶然g因素（p244末），不能凭磁比值相似判同组态。PSM对t→GSB的相对强度/带间形变差有未解决边界（p246 Sec3.4），不能把所有衰变都称定量解释完毕。


## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BA130-D23-061-01 | Petrache2019是原实验；Chen2019 PRM与Wang2020 PSM复用S1/S1prime实验输入，不能计为独立实验重复。 边界：Different model frameworks provide model comparison, not repeated experimental acquisition. | source-dependency-synthesis | direct-original-plus-labeled-synthesis-or-inference | printed p242, Sec2 Experimental results | true |
| BA130-D23-061-02 | GALILEO25个Ge位于90度10个、119/129/152度各5个四环；Chen四角强度角分布选小模delta因chi2较低，仍明确角分布不能完全排除大模delta。 边界：No unique-root, polarization or lifetime inference is supplied by this apparatus description. | experimental-method-and-ambiguity | direct-original | printed p242, Sec2 first paragraph | true |
| BA130-D23-061-03 | 2019supp TableI只列D1/t-band而非S1prime完整delta向量；TableII D1 literal为nu h^2 tensor pi h^-2，与main Table1/正文的nu h^-2 tensor pi h^2不同，须保留冲突。 边界：Do not silently repair signs. Chen TableI I19/21 display delta without uncertainties; do not invent uncertainties. | source-scope-and-literal-conflict | direct-original | printed p244 D1 assignment paragraph; p245 Table1 | true |
| BA130-D23-061-04 | 原文将t与K=8minus低自旋的大E2out/in部分归于同一good-K带内CG投影系数；此机制不能作为S1prime→S1声子定义。 边界：GoodK fixedQ benchmark is a model exercise, not an actual t-band fit or new B/Q/lifetime measurement. | source-mechanism-and-derived-control | direct-original-plus-labeled-synthesis-or-inference | printed p245, final left paragraph continuing in right column below Fig5; Fig5(c) | true |
| BA130-D23-061-05 | Petrache Table1中各组态PRM的Coriolis attenuation xi和CDFT形变合同，与Chen S1/S1prime按能量拟合的自旋相关三轴惯量合同分开；不得移用D1的xi到S1prime。 边界：No new attenuation value, fit or parameter uncertainty is inferred. | model-contract-boundary | direct-original | printed p245 Sec3.3 and Table1 | true |
| BA130-D23-061-06 | t与K=8minus相似磁强度在原文中有偶然g因子成分；PRM有效g与PSM/TAC直接多体磁算符的说明不同，不是独立测得转动g。 边界：Model operator prescriptions must be preserved; no magnetic-moment measurement is fabricated. | author-model-comparison | direct-original | printed p244 final note paragraph; p245 effectiveg paragraph; p246 magneticoperator paragraph | true |

## Competing Interpretations and Limitations

保留作者的两准粒子wobbling支持与模型局限；不由M1占优一票否决、不恢复跨核δ/W.u.硬门。原producer、原始计数和统一holdout分割未获得。

## Summary

原实验建立130Ba多带结构；形变与机制仍由不同模型解释。

## Extracted Pages

[[chen-2019-transverse-wobbling-even-even]] · [[signature-tip-shears-discrimination-contract]]。新主张needs_review:true，未新增human-reviewed。
