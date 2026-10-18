---
type: source
title: "Tuli 2001 ENSDF格式：MR显式符号、未知与不对称误差"
aliases: [Tuli 2001 ENSDF format manual, ENSDF MR sign unknown]
created: 2026-10-18
updated: 2026-10-18
status: ai-draft
review_status: unreviewed
source_type: data-format-manual
reading_depth: skimmed
title_original: "Evaluated Nuclear Structure Data File: A Manual for Preparation of Data Sets"
authors: [Jagdish K. Tuli]
year: 2001
date_original: February2001
report_number: BNL-NCS-51655-01/02-Rev
citation_key: ""
citation_key_status: no-unique-local-BibTeX-entry
canonical_source: "NNDC official ENSDF format manual, Tuli February2001"
source_url: "https://www.nndc.bnl.gov/ensdf/ensdf-manual.pdf"
raw_file: "raw/papers/gpt/day16-20261018/tuli-2001-ensdf-format-3400f0ae84d2.pdf"
raw_sha256: "3400f0ae84d24f252f5bed4e6f0227304df9a4608aceb1d67e609db12605a0e9"
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: []
reactions: []
experiments: []
models: []
methods: [ENSDF-fixed-column, uncertainty-interpretation]
observables: [multipole-mixing-ratio, relative-photon-intensity, total-conversion-coefficient]
tags: [ensdf, format, phase-sign, data-identity]
---

# Tuli 2001：不能把MR省略符号读成已知正号

## Bibliographic Record

NNDC首页独立链接的Format Manual是JagdishK.Tuli February2001、BNL-NCS-51655-01/02-Rev，实际112PDF页/686034bytes；与M.R.Bhat1987 procedures manual是不同文档。书目/日期由PDF1原图核准，不以PDFcreationdate或2026下载日当版本年。新原件在tmp，raw槽未填，Bib无唯一命中，不造DOI/ISBN。

## Scope and Reading Depth

针对mixingratio/固定栏定向读取：封面、摘要/目录、printed28 Gamma Record（PDF34）、printed43 V.9–11（PDF49）、printed44 V.12–14（PDF50）。原图视觉校字段/含义与asymmetric例；textlayer的数字编码不可靠，没有仅靠破碎OCR提数。未通读112页，wholemanual仅skimmed。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| TU01-1 | gammaMR在42–49列、DMR50–55，CCtotal56–62/DCC63–64；原文明确“Sign must be shown explicitly if known. If no sign is given, it will be assumed to be unknown.” unsignedMR不能因float正值自动认定phase已测正。 | fixed-field-and-sign-semantics | direct-manual | printed28 GammaRecord MR/CC rows/PDF34 | true |
| TU01-2 | DMR可存+x−y不对称误差；原例MR=−3、DMR=+1−4表示−3^(+1/−4)、范围−7到−2，误差按代数上下端，不随负central翻向。字段空白和numeric0不同，不补0或把unsignedmagnitude当signed值。 | uncertainty-field-semantics | direct-manual-and-use-boundary | printed43 V.10–11/PDF49；printed44 V.12/PDF50 | true |
| TU01-3 | RI是relativephoton、TI是relativetotaltransition，单位由N record定义；M/MR/CC各字段不互代。强度字段带括号表示deduced或fromotherexperiment，不由括号决定一项新的独立采集。 | intensity-object-and-provenance | direct-manual | printed28 GammaRecord/footnote/PDF34；printed44 V.13/PDF50 | true |

## Summary

MR的**显式signmarker、统计误差范围、operatorconvention和sourceprovenance**是四层信息。`−0.00(1)`可保留负号marker，但误差跨零并不证明物理相位已显著定负；unsigned`.5`也不能被解析器自动升级成+δ。source无phase定义时格式规则不能补测量。

## Knowledge Impact and Learning Decision

`supports`先前W178空MR/CC固定栏边界；`revises`以一般float解析器吞掉“signunknown”的做法。与[[martin-1987-ensdf-mixing-ratio-phase-conventions]]的物理定义互补：format规定如何保存字段，不自动认证每条旧primary按某套算符处理。所有新claims true。

## Competing Interpretations and Limitations

本页核的是2001版本规定及少量原始页，不认证现行全部ENSDF工具、每条评价实际采用的phase或任何primary实验。字段有号不等于误差排除零，unsigned值不等于已测正号，空栏不等于数值0；原producer或注释另有约定时须逐项回查。

## Extracted Pages

- [[multipole-mixing-ratio]]：MRfield显式号/未知/不对称误差。
- [[dco-pdco-ambiguity-worksheet]]、[[nndc-2009-178w-dco-reference-records]]：blankMR不借CC填δ的既有规则。
