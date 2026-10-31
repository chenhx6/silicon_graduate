---
type: source
title: "Dafni1983：Ce/Sn频率比与绝对四极矩的模型归一"
title_original: "Electric quadrupole interaction of Ce isomers in tin"
aliases: [Dafni1983 CeSn calibration, Ce isomers in tin]
created: 2026-10-23
updated: 2026-10-23
status: ai-draft
review_status: unreviewed
source_type: experiment-and-model-normalization
reading_depth: read
authors: ["E. Dafni", "F. D. Davidovsky", "A. Gelberg", "M. Hass", "E. Naim", "G. Schatz"]
year: 1983
journal: Hyperfine Interactions
volume: "15/16"
pages: "101-104"
doi: "10.1007/BF02159726"
citation_key: ""
canonical_source: "https://doi.org/10.1007/BF02159726"
source_url: "http://link.springer.com/content/pdf/10.1007/BF02159726.pdf"
raw_file: "raw/papers/gpt/learning-daily/20261022-DAY20-be2-qt-deformation-systematics/dafni-1983-ce-tin-quadrupole.pdf"
raw_sha256: "5b08557f5fd79724547485c93fd729ecce97540cd9a2b5b45df40abc1734ce08"
raw_storage_status: reserved-unpopulated-public-publisher-pdf-only
raw_archive_verified_at: 2026-10-23
analysis_status: public-staging-original-read-raw-archive-verified
public_staging_file: "tmp/day20-dafni106/PDFs/Electric_quadrupole_interaction_of_Ce_isomers_in_tin.pdf"
license: not-established-from-tdm-metadata
nuclei: [134Ce, 136Ce, 138Ce]
methods: [TDPAD, quadrupole-interaction]
observables: [quadrupole-coupling-frequency, quadrupole-moment, electric-field-gradient]
tags: [calibration, reference-moment, effective-charge, ce-sn, source-lineage]
---

# 频率比是实验约束，绝对矩另含参考模型

## Bibliographic Record

E. Dafni等，*Hyperfine Interactions*15/16(1983)101–104，DOI10.1007/BF02159726。PDF1刊头、题名与六作者实际核对；[[vianden-1987-electric-field-gradients-metals]] Ref371的Davidowsky拼写与原文Davidovsky并存，不新增一个作者/实验。

由nature-downloader取得公开publisher PDF，175845bytes、4页，SHA256见frontmatter。返回TDM metadata不建立开放再分发许可。SI按本轮auto配置关闭，不断言不存在。只读public staging，raw_file是未填归档槽，raw/PLAN/Bib均未改。下载身份与scope106保存在Day20 run02。

## Scope and Reading Depth

primed-recall-106先冻结，再做metadata查询与正文获取；本session实际读PDF1–4全部文字/参考文献，视觉核全部四页，涵盖Figs1–4、Tables1/2、R(t)/G22、νQ–ω0定义与温度律。未取得原事件、fit producer、原jointCov或Refs5/7/9正文，不把原文曲线当原数据重拟合。

## Summary

作者测得134/136/138Ce(10+)在Sn中的耦合频率和相对Q，并直接声明未知CeSn EFG使本数据不能给绝对矩或符号。Table2的绝对Q用138Ce的模型矩77 e·fm²归一，含从116/118Sn迁移的有效电荷1.87。该源是[[ionescu-bujor-1998-static-moments-129-131ce]]所引EFG编译链的上游，不能把其模型归一抹去后当独立无模型绝对标尺。

## Extracted Pages

PDF1/101：问题、Fig1和相对矩动机；PDF2/102：反应、NaI与Sn宿主、谱比/固定relax及温度范围，Figs2/3；PDF3/103：实验与模型比值、绝对矩不可得声明、Tables1/2及脚注；PDF4/104：有效电荷迁移警告、Fig4温度律与全部参考文献。

## Method and Evidence Chain

76MeV束流的Sn+O反应布居10+异能态；厚多晶Sn靶置可加热/冷却铜指上，NaI计数给背景扣除和归一后的角度时间谱。作者按单一EFG和指数取向松弛拟合R(t)。相同I、宿主与温度下的νQ比消去共同EFG；绝对Q需要另加参考矩/场梯度，正号也来自结构解释。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| DA83-D20-1 | 作者明确：本数据因CeSn EFG幅度未知不能确定绝对Q；常规TDPAD只确定νQ的模，不能测得Q符号。原相对Q138:Q136:Q134=1:1.45(14):1.71(16)，正号/prolate解释依赖所设h11/2结构。 | experimental-ratio-versus-absolute-sign-boundary | direct-original-and-visual | PDF1 abstract; PDF3/103 first two paragraphs | true |
| DA83-D20-2 | Table1在297K列νQ134=52.4(16)、νQ136=44.4(16)、νQ138=30.6(28)MHz。134Ce的其他温度行70.2(48)/204K、60.5(28)/238K、50.4(20)/376K、49.6(32)/430K、47.6(24)/468K；138Ce另有34.7(32)/160K、31.8(32)/224K。不能用编译的134Ce54.8(24)/293K静默替换这些原表行。 | literal-frequency-temperature-table | direct-original-and-visual | PDF3/103 Table1; VI87-D20-2 comparison | true |
| DA83-D20-3 | Table2脚注假设138Ce(10+)为νh11/2^−2，取e_eff=1.87给Q138=77 e·fm²，再报Q136=111(11)、Q134=132(12)e·fm²。正文说1.87为116/118Sn中h11/2 quasiparticles的平均值，并警告mass116与138的有效电荷可能不同。77未给理论σ，不能视为实验精确参考矩。 | model-anchored-absolute-normalization | direct-original-and-visual | PDF3/103 Table2 footnote and final paragraph; PDF4/104 first paragraph | true |
| DA83-D20-4 | 作者先用Ref7 seniority波函数得到Q138:Q136:Q134=1:.91:.35，与实验比不同（PDF文字层把.35误识为.38，已放大视觉核）；随后给quasiparticle–core耦合的定性解释。磁矩相近支持子空间假设，不排除Q对collective admixtures的更强敏感性；不能将相近g当成K混合或形状唯一性。 | author-model-comparison-and-competing-description | direct-original-and-visual | PDF1/101 introduction; PDF3/103 discussion and Table2 | true |
| DA83-D20-5 | 单一EFG强度分布可能存在，但作者说实验不敏感。指数取向relax固定.8µs，改为.2µs至无穷时ω0改变小于10%；这是该文的参数敏感性报告，不是1998的通用10%CI。160K以下modulation减弱，不能可靠定ω0。 | identifiability-and-response-model-boundary | direct-original-and-visual | PDF2/102 column text and Figs2/3 | true |
| DA83-D20-6 | 160–468K有温度测量；T^(3/2)拟合只用于297K以上，B=1.6×10^−5 K^−3/2。低温偏离可涉及4f电子或辐照损伤，作者不能排除后者；不能把高温拟合当全部温区的精确EFG law。 | limited-temperature-fit-and-alternatives | direct-original-and-visual | PDF4/104 text and Fig4 caption | true |
| DA83-D20-7 | 当前可见链为Dafni的模型归一矩/频率→Vianden编译→Ionescu-Bujor所引CeSn EFG。按声明Q138=.77eb、ν138=30.6MHz与IB98 ν129/ν131，给1.32359/.91595eb，和打印1.32/.92中心相容；这只是一个可见归一合同的重建，不唯一识别1998采用值、原producer、完整校准预算或实验CI，也不宣称其测量无效。 | conditional-calibration-lineage-reconstruction | task-derived-from-original-sources | DA83-D20-2; DA83-D20-3; IB98-D20-R104-2/3 | true |

## Competing Interpretations and Limitations

绝对Q的模型参考尺度可能共同改变两核的归一，而共享EFG下的模值比仍保留频率比约束。原事件、频率拟合Cov、真实场/温度分布与参考矩理论不确定度均未恢复。Vianden134Ce行与本原表温度/νQ字面不同，保留差异，不推断修订、插值或笔误来源。

## Knowledge Impact and Learning Decision

更新[[ionescu-bujor-1998-static-moments-129-131ce]]的“known EFG”谱系边界：当前可见参考链含有效电荷与模型归一，不能把绝对Qs直接当无模型形变图像。[[day20-quadrupole-collectivity-systematics-synthesis]]继续区分频率/模值比、条件绝对标尺、PTR参数和高spin Qt；原review/flags不提升。
