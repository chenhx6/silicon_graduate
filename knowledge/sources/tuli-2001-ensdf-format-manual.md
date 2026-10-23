---
type: source
title: "Tuli 2001 ENSDF格式：MR显式符号、未知与不对称误差"
aliases: [Tuli 2001 ENSDF format manual, ENSDF MR sign unknown]
created: 2026-10-18
updated: 2026-10-19
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
raw_storage_status: verified-raw-archive
raw_archive_verified_at: 2026-10-23
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
| TU01-4 | Gamma record的C在col77；&是multiply-placed transition且intensity not divided，@是intensity suitably divided。相同RI重复到两个placement不等于两次独立测量，也不能相加求总强度或默认对半分区。需同时保存level/placement和共享观测身份。 | multiplet-placement-and-intensity-semantics | direct-manual-and-use-boundary | printed28 GammaRecord C row/PDF34 | true |
| TU01-5 | Nrecord NR(cols10–19)把RI换成每100该decaybranch的photon yield，再由BR(cols32–39)换成每100parent；NB(cols42–49)用于B/E强度。不能用不同N倍率对象的RI直接比较或把Adopted归一100当EC绝对100。 | decay-normalization-field-semantics | direct-manual | PDF24/printed18 Normalization Record | true |
| TU01-6 | Erecord的IB(cols22–29)为β+强度、IE(cols32–39)为EC强度、TI(cols65–74)为两者合计，三者单位同并依NB。字段空白与numeric0不同；不能因dataset名EC便假定IB=0。 | electron-capture-beta-plus-field-semantics | direct-manual | PDF30/printed24 EC Record | true |
| TU01-7 | PrecordQP(cols65–74)为g.s.→g.s.总可用Q，E(cols10–19)为实际衰变母态能量，非daughter level；多parent有分开的Precord。用QP作能量可达性边界须同时核parentE与其标签，不能拿近能γ的能量替母态。 | parent-energy-and-Q-field-semantics | direct-manual | PDF23/printed17 Parent Record | true |


## Summary

MR的**显式signmarker、统计误差范围、operatorconvention和sourceprovenance**是四层信息。`−0.00(1)`可保留负号marker，但误差跨零并不证明物理相位已显著定负；unsigned`.5`也不能被解析器自动升级成+δ。source无phase定义时格式规则不能补测量。

## Knowledge Impact and Learning Decision

`supports`先前W178空MR/CC固定栏边界；`revises`以一般float解析器吞掉“signunknown”的做法。与[[martin-1987-ensdf-mixing-ratio-phase-conventions]]的物理定义互补：format规定如何保存字段，不自动认证每条旧primary按某套算符处理。所有新claims true。

## Competing Interpretations and Limitations

本页核的是2001版本规定及少量原始页，不认证现行全部ENSDF工具、每条评价实际采用的phase或任何primary实验。字段有号不等于误差排除零，unsigned值不等于已测正号，空栏不等于数值0；原producer或注释另有约定时须逐项回查。

## Extracted Pages

- [[multipole-mixing-ratio]]：MRfield显式号/未知/不对称误差。
- [[dco-pdco-ambiguity-worksheet]]、[[nndc-2009-178w-dco-reference-records]]：blankMR不借CC填δ的既有规则。

### Day17源参考的N/E字段定向应用

本session另核原hash、PDF24/printed18 Nrecord与PDF30/printed24 Erecord的文本和高分辨图像，新增TU01-5/6；旧TU01-1–4及flags保持，未把112页manual升级为全文read。[[nndc-2011-pb207-bi207-polarization-reference]]在NR/BR/NB=1下解释photon/EC/β+字段，并保留RI–ICC来源依赖与actualphase/Σ缺口；format本身不认证原实验。

对207Bi source的高母态near-energy排查再定向核PDF23/printed17 P旁态/QP字段，增加TU01-7；仍只是三页新field-scope，不覆盖整本manual或primaryphysics。

### 223Ra多重放置的实际应用

2026-10-19再次视觉核PDF34/printed28的col77 C；既有图片/hash保持。[[nndc-2001-223ra-reference-and-2026-intensity-records]]的113.1/314.9各重复两条& RI，是同一未分区观测在不同母态的placement；旧113.11两@ RI则已有分区。`float(RI)`列表若丢掉C/parent/版本，既可能多加一次总量，也可能凭空确定偏振weight。规则本身不恢复primarygate、分区Cov或具体响应。
