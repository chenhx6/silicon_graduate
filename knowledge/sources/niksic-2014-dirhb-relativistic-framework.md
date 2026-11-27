---
type: "source"
title: "DIRHB – a relativistic self-consistent mean-field framework for atomic nuclei"
title_original: "DIRHB – a relativistic self-consistent mean-field framework for atomic nuclei"
authors: ["T. Nikšić et al."]
aliases: ["niksic-2014-dirhb-relativistic-framework"]
tags: ["archive-learning", "nuclear-structure"]
created: "2026-11-27"
updated: "2026-11-27"
status: "ai-draft"
review_status: "unreviewed"
source_type: "journal-article"
reading_depth: "read"
year: 2014
canonical_source: "arXiv:1403.4039v1"
raw_file: "raw/papers/gpt/query/20261105-model-runtime-audit/dirhb-arxiv-1403.4039.pdf"
raw_sha256: "1dba19846af702bfe5e1abed57d610cd0ddd20df21a541d4e6aef3cafef67184"
raw_storage_status: "archived-local"
archive_required: true
---

# DIRHB – a relativistic self-consistent mean-field framework for atomic nuclei

## Bibliographic Record

T. Nikšić, N. Paar, D. Vretenar and P. Ring. arXiv:1403.4039v1 dated 2014-03-17, local submitted preprint.

## Scope and Reading Depth

作者稿 PDF 1–39 正文，先前定向覆盖 1–4、11–18、33–39，本轮补 5–10、19–32。39–42 核相关依赖引文。

## Summary

偶偶核静态相对论 Hartree–Bogoliubov 框架的软件实现说明，按球形、轴对称、三轴分开。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| S-1 | 球形、轴形和三轴实现各用对应振子基。大分量截断 Nmax，小分量 Nmax+1 用于抑制伪解。 | implementation | source-reported | PDF 19–24、28–30，Eqs. (68)–(72)、(97)–(108)、(134)–(147) | false |
| S-2 | 介子交换与点耦合是两个粒子–空穴实现。有限程可分离配对按 Gogny D1S 的对称核物质配对隙拟合。 | model-input | source-reported | PDF 5–16，Eqs. (8)–(59) | false |
| S-3 | 三种静态求解预设空间反射和时间反演对称。增广拉格朗日处理形状约束，Broyden 和线性混合用于迭代。 | implementation | source-reported | PDF 1–2、17–18、33–38，Table 1，Eqs. (167)–(170) | false |

## Competing Interpretations and Limitations

- 源代码发布工件、编译、数值重放及刊版改写未在本次核对。保留 Eq. (24) 与 p. 29 的印稿异文。

## Extracted Pages

作者稿 PDF 1–39 正文，先前定向覆盖 1–4、11–18、33–39，本轮补 5–10、19–32。39–42 核相关依赖引文。
