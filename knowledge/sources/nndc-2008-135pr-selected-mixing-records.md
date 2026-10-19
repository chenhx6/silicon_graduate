---
type: source
title: "135Pr官方记录：旧评价、不同POL语义与2026混合比分支"
aliases: [NNDC135Pr selected MR POL records, Pr135 XUNDL version audit]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: evaluated-and-unevaluated-nuclear-data-objects
reading_depth: skimmed
title_original: "135PR Adopted and XUNDL-3/6/7 selected records"
authors: [Balraj Singh, Alexander A. Rodionov, Yuri L. Khazov, J. Chen, E. A. McCutchan]
journal: Nuclear Data Sheets
year: 2008
volume: 109
pages: "517-698"
doi: "10.1016/j.nds.2008.02.001"
citation_key: ""
citation_key_status: no-unique-local-BibTeX-entry
canonical_source: "NNDC135059001/009/012/013; actual2026-10-19 access"
source_url: "https://www.nndc.bnl.gov/ensdf/"
raw_file: "raw/data/gpt/day16-20261018/pr135-adopted-b7f044ae3ac8.ens"
raw_sha256: "b7f044ae3ac8eb6f2b420a539f039a92ebe2ed6c28f5470af4ad5d2f1995e698"
raw_storage_status: official-staging-verified-raw-archive-deferred
nuclei: [135Pr]
reactions: []
observables: [multipole-mixing-ratio, polarization, DCO, transition-identity]
methods: [ENSDF-fixed-column, provenance-and-version, observable-semantics]
tags: [XUNDL, shared-dataset, MR-uncertainty, calibration]
---

# 先确认记录版本，再比较同名POL和MR

## Bibliographic Record

正式旧评价为Singh/Rodionov/Khazov，*Nuclear Data Sheets*109,517–698(2008)，DOI[10.1016/j.nds.2008.02.001](https://doi.org/10.1016/j.nds.2008.02.001)；Crossref核作者/卷页，ENSDFheader给cut22-Jan-2008。新XUNDL是原2015Ga39、2022Lv01、2026Se03的unevaluated编译，非三次新的编译年实验。[[garg-2015-135pr-magnetic-rotation]]、[[lv-2022-evidence-against-wobbling-135pr]]、[[sensharma-2026-evolution-chirality-transverse-wobbling-135pr]]各自保留primary层。

## Scope and Reading Depth

只定向读Adopted的header1–40及L1478.2/G747.1、L2204.7/G814与decoyL1289.60/G746.1；三XUNDL197/124/117行完整读。不是全A135评价精读。初GET返回HTTP200“Not a valid input method”已识别为失败，按实际form改POST后取真实dataset。body仍在repo tmp，raw/Bib未改。

| datasetcheck | 实际对象/本地路径 | SHA-256 |
| --- | --- | --- |
| 135059001,135PR | 200803 Adopted，584行；tmp/day16-garg2015/adopted2008.ens | b7f044ae3ac8eb6f2b420a539f039a92ebe2ed6c28f5470af4ad5d2f1995e698 |
| 135059009,135PR | XUNDL3/2015Ga39，197行；tmp/day16-garg2015/garg-xundl3.ens | f1c3a52b846bfb46475673f82af86cb6c611f09b754a465f09f470d1af4bf0d6 |
| 135059012,135PR | XUNDL6/2022Lv01，124行；tmp/day16-garg2015/lv-xundl6.ens | ce2b463e45572ca4b8067fd7646ed10d4e458b0f5f8c25f234f463c068679990 |
| 135059013,135PR | XUNDL7/2026Se03，117行；tmp/day16-garg2015/sensharma-xundl7.ens | 1b8a7196b62dd583108dfae4b9528fc5d5b60feb3039561988831eca6ba06390 |

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| N135-1 | 当前selectedAdopted列表仍200803/cut22Jan2008，其Qrecord另有2012Wa38质量更新。header月份不保证所有字段同时更新，也不能将此旧评价当已裁决2015–2026偏振争议。 | object-version-boundary | direct-object | 135059001 header H/Q | true |
| N135-2 | 旧L1478.2/G747.1与L2204.7/G814仅D/空MR，不能用空MR补δ=0或把D定成M1。 | target-field-boundary | direct-fixed-column | 135059001 L1478.2/G747.1；L2204.7/G814 | true |
| N135-3 | 近能G746.1属于L1289.60、J=(11/2−)，不是目标17/2−母态的747branch。只按nearestenergy匹配会串错跃迁。 | identity-failure-control | direct-level-and-gamma | 135059001 L1289.60/G746.1 | true |
| N135-4 | XUNDL3由J.Chen于7Dec2015编译2015Ga39、base201601，selectedobject不含2019erratumkey；target747.5/813.3仍pol−.05(.03)/−.20(.08)、MR空，是旧original转录，非2019更正证据。 | compilation-lineage-and-correction-boundary | direct-XUNDL | 135059009 header；L1478.31/G747.5；L2204.30/G813.3 | true |
| N135-5 | GargXUNDL的pol对应countΔ，而LvXUNDL6明确pol fromTable1对应P=.04(+.08/−.13)、−.03(+.05/−.12)。同名pol不认证同物理/response对象，不能裸合并。 | observable-semantics | original-and-compiler-crosswalk | 135059009 targetpol；135059012 targetpol/Table1note | true |
| N135-6 | Lv对象base202510实际由McCutchan于10Feb2025编译2022Lv01，MR747.3=−.47(+.09/−.22)、813.2=−.37(+.10/−.14)转录其原paper，不是2025独立实验。 | MR-and-source-identity | direct-XUNDL | 135059012 header/L1477.9/G747.3/L2204/G813.2 | true |
| N135-7 | 最新selectedXUNDL7由26May2026编译、5Jun格式化，引用2026Se03；targetG746.3 MR−1.40+14−12、G811.6 MR−1.63+2−3。phase、samecampaign及primary争议仍回源，不由“更新月份”裁决分支。 | postcutoff-object-and-MR | direct-XUNDL | 135059013 header；L1476.8/G746.3；L2203.1/G811.6 | true |
| N135-8 | 保留MR字符串精度后，−1.40+14−12的误差为+.14/−.12，−1.63+2−3为+.02/−.03。8个selectedparent/Egamma身份与三组MR字段实际typed重放，未丢signedtoken或把DMR digits当绝对数。 | uncertainty-and-identity-replay | actual-fixed-column-computation | 135059013 targetMR/DMR；本页解析合同 | true |
| N135-9 | Garg编译L1478.31/2204.30等有least-squares compiler调整，不能将原TableI1478.2/2204.4与这些差值当独立重测。每dataset的parent/gamma/归一要成套保存。 | shared-input-and-level-version | direct-XUNDL | 135059009 cL E note/targetL | true |
| N135-10 | XUNDL7 header只列|g(|q)且MR源于AD，未给targetPOL/Q或jointΣ；XUNDL6的POL/δ来自Lv同一分析。重复编译、AD和其derivedδ不增加独立偏振数据。 | independence-and-readiness | direct-object-and-primary-boundary | 135059013 header cG M,MR；135059012 targetcomments | true |

## Selected record crosswalk

| 对象 | 17/2−母态 / gamma | 21/2−母态 / gamma | MR / POL语义 |
| --- | --- | --- | --- |
| Adopted2008 |1478.2 /747.1 |2204.7 /814 |MR空，仅D |
| GargXUNDL3 |1478.31 /747.5 |2204.30 /813.3 |MR空；pol为旧Δ |
| LvXUNDL6 |1477.9 /747.3 |2204 /813.2 |MR−.47/−.37；pol为Table1P |
| SH26XUNDL7 |1476.8 /746.3 |2203.1 /811.6 |MR−1.40/−1.63；无targetPOL |

## Summary

官方记录增加了可恢复的version/field/provenance合同，未增加一次实验或裁决wobbling。旧空MR、同名pol、编译年月及近能gamma都不能替原响应、相位和companion。

## Competing Interpretations and Limitations

- XUNDL3旧负Δ不是已读2019勘误；当前exacterratum只有metadata/readiness。
- XUNDL6与7保留不同原数据/分析的MR分支，不按日期投票或合并成一个δ。
- 原事件、逐门背景、Q/a(E)、alignment和联合Cov未恢复；当前不是experimentalL4fit。

## Knowledge Impact and Learning Decision

`supports`当前A130输入身份和uncertainty合同；`limits`旧Adopted/compiledPOL裁决争议；`revises`把XUNDL编译日期或nearestenergy当新实验/同transition的隐含假设。所有新claimsneeds_review。

## Extracted Pages

[[135pr-mixing-branch-input-contract]]、[[135pr-wobbling-controversy]]、[[multipole-mixing-ratio]]、[[linear-polarization-asymmetry]]、[[garg-2015-135pr-magnetic-rotation]]。

## Reproducibility

[typed字段程序](../../system/scripts/day16_pr135_official_record_audit.py)actualexit0；[合同/八行结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/pr135-official-record-audit-result.json)。原四对象hash/选择参数/方法错误与纠正保留，原件只tmp、raw槽未归档。
