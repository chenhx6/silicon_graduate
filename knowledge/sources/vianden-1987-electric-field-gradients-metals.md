---
type: source
title: "Vianden1987：金属EFG编译表与Ce/Sn校准谱系"
title_original: "Electric field gradients in metals"
aliases: [Vianden1987 EFG compilation, CeSn quadrupole calibration]
created: 2026-10-23
updated: 2026-10-23
status: ai-draft
review_status: unreviewed
source_type: review-compilation
reading_depth: read
authors: ["R. Vianden"]
year: 1987
journal: Hyperfine Interactions
volume: 35
pages: "1079-1118"
pages_crossref: "1077-1118"
doi: "10.1007/BF02394554"
citation_key: ""
canonical_source: "https://doi.org/10.1007/BF02394554"
source_url: "http://link.springer.com/content/pdf/10.1007/BF02394554.pdf"
raw_file: "raw/papers/day20-20261022/vianden-1987-efg-metals.pdf"
raw_sha256: "ec9cfaa6f2f47b9ecacde62f226b575c5002915b620dd971b1eac5a63f3f1508"
raw_storage_status: reserved-unpopulated-public-publisher-pdf-only
raw_archive_verified_at: 2026-10-23
analysis_status: selected-public-staging-read-raw-archive-verified
public_staging_file: "tmp/day20-calibration105/PDFs/Electric_field_gradients_in_metals.pdf"
license: not-established-from-tdm-metadata
nuclei: [134Ce, 136Ce, 138Ce]
methods: [TDPAD, quadrupole-interaction]
observables: [quadrupole-coupling-frequency, quadrupole-moment, electric-field-gradient]
tags: [calibration, source-lineage, static-quadrupole-moment, ce-sn]
---

# EFG编译值要追溯到参考矩与原测量

## Bibliographic Record

R. Vianden，*Hyperfine Interactions* 35 (1987)，DOI10.1007/BF02394554。实际PDF3刊头为1079–1118，与[[ionescu-bujor-1998-static-moments-129-131ce]] Ref14的1079一致；Crossref给1077–1118。42页publisher PDF的第一页是APPENDIX分隔页，正式题名页在PDF3。保留两种分页记录，不把metadata差异误判为两篇独立来源。

通过nature-downloader公开publisher路线获得PDF并核验题名页、内容、页数及SHA256。脚本标为open_access_downloaded，返回的license字段为Springer TDM URL；此处只确认公开端点可访问，未据此认定开放再分发许可。SI按本轮auto配置关闭，不宣称不存在。原件暂存在tmp，raw_file只是尚未填入的归档槽；未写raw、PLAN或Bib。下载manifest与实际scope见Day20 run02的calibration-access-discovery-105.json、calibration-download-identity-105.json与source-reading-scope-105.json。

## Scope and Reading Depth

定向读取PDF3/4（printed1079/1080，定义、列语义和编译范围）、PDF17的Ce条目（printed1093），以及PDF40的Ref371（printed1116）；这些关键页作视觉核。另观察PDF1的APPENDIX分隔页，未读完整42页所有核素行或全部references。Ce条目按原表视觉转录，不以OCR的13~Ce等形式猜核素。

本页105范围不含Ref371；106已另原读[[dafni-1983-ce-isomers-tin-quadrupole]]四页，发现绝对Q含模型归一。原Q参考producer/理论不确定度、事件谱与共同Cov仍未得。本文是编译表，不是1998年129/131Ce的新实验或独立重复。

## Question and Evidence Chain

1998年Ce异能态的绝对Qs使用CeSn室温EFG标定（该源Ref14）。本页核对该标定入口究竟报告原始EFG还是汇集已有νQ和Q，以及三条Ce参考之间有哪些同源关系。

## Summary

Ce/Sn三行共享Dafni1983 Ref371，编译表不是独立绝对标定。新原读primary及其模型归一边界见[[dafni-1983-ce-isomers-tin-quadrupole]]；不能把编译行的Q当成模型无关参考或把三次转载当三次实验。

## Extracted Pages

PDF3/4定义和列语义、PDF17/printed1093 Ce/Sn块、PDF40/printed1116 Ref371；关键页视觉核。PDF1 APPENDIX分隔页另已观察；其余核素行与全文未读。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| VI87-D20-1 | 本文明确是截至1986年7月数据的编译，Eq1定义νQ=eQVzz/h；νQ栏通常给绝对值，若原测定了符号则标出。没有S.Cry.说明时为多晶，(T)只表示温度依赖曾测量，不是某一已恢复温度校准曲线。 | compilation-and-column-semantics | direct-selected-original-and-visual | printed1079/PDF3 Eq1 and column2; printed1080/PDF4 abbreviations | true |
| VI87-D20-2 | Sn、293K中的134/136/138Ce参考均为10+激发态；原表依次列νQ=54.8(24)/44.4(16)/30.6(28)MHz，Q=1.32(12)/1.11(11)/.77(−)b，方法TDPAD并标(T)。.77的括号为横线，不能自行补成Gaussian标准差。 | literal-probe-host-reference-values | direct-selected-original-and-visual | printed1093/PDF17 Ce block | true |
| VI87-D20-3 | 三条Ce行的νQ和Q均指向同一Ref371：E.Dafni、F.Davidowsky、A.Gelberg、M.Hass、E.Naim、G.Schatz，Hyperfine Interactions15/16(1983)101。编译的三行不能当成三个独立EFG标定；105时尚未读该primary；106新原读DA83-D20-3确证参考Q为模型锚，仍不能认证其理论误差或共同Cov已知。 | shared-reference-dependency-and-readiness | direct-selected-original-and-visual | printed1093/PDF17 Ce block; printed1116/PDF40 Ref371 | true |
| VI87-D20-4 | 同一CeSn标尺若确实共享，在129/131Ce模值比中可约去；它不免除各频率拟合、radiation damage/松弛模型和样本差异。本文νQ/Q中心比只可用作约40MHz/b的粗略合同核对，不能当新独立测得EFG、重造原129/131Ce CI或给编译参考无限精度。 | calibration-transfer-boundary | synthesis-with-actual-source | VI87-D20-1; VI87-D20-2; IB98-D20-R104-1–5 in Ionescu-Bujor source | true |

## Competing Interpretations and Limitations

编译参考矩可能与其νQ测量共享模型或标定输入；仅靠本表不能区分独立Q测量、推导Q或共同EFG的依赖方向。106的Ref371原读显示138Ce77e·fm²为模型锚且未给理论σ；不能因为表头出现Q就把其不确定度解释为全统计或完整置信区间。

Barth等PRL45,1015(1980)、DOI10.1103/PhysRevLett.45.1015在本次仅核metadata，未取得正文；它是IB98磁相互作用的另一条参考链，不能以本EFG表替代。官方APS PDF端点403、公开harvest端点401的有界失败已记录，未转向机构身份或绕过访问控制。

## Knowledge Impact and Learning Decision

把[[ionescu-bujor-1998-static-moments-129-131ce]]的“已知CeSn EFG”定位到编译表中三个同源Ce参考，而不是新增独立标定。106已取得Ref371并发现模型归一，下一步仍需其参考波函数/有效电荷primary和实际共同误差；保留模值比的共同标尺条件，不恢复实际Cov或形变三相认证。完整Day20条件推导见[[day20-quadrupole-collectivity-systematics-synthesis]]。


## Day20原表与编译的字面差异（checkpoint106）

DA83-D20-2的134Ce原表为52.4(16)MHz/297K，本文编译为54.8(24)MHz/293K。两者逐字保留，未识别差异的producer/修订来源，不以某一条静默覆盖另一条。DA83-D20-3给出了Table2绝对矩的理论138Ce归一；本表继承参考矩也继承该模型边界。
