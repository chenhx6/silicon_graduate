---
type: research-note
title: "EPJA、PRC、PLB 投稿路线与模板审计"
aliases: [journal route audit 20261105, EPJA PRC PLB template audit]
created: 2026-11-05
updated: 2026-11-05
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [zobel-1983-energy-projectile-alignment, pado-alignment-response-dependence-paper]
created_from: "Official journal and publisher submission pages retrieved for the A≈130 manuscript candidates"
tags: [journal-selection, template, epja, prc, plb, data-availability]
---

# EPJA、PRC、PLB 投稿路线与模板审计

## Archived official pages

The retrieved HTML snapshots and access-failure records are indexed by:

`raw/papers/gpt/query/20261105-journal-guidelines/manifest.json`

The Springer Nature December 2024 LaTeX package and CTAN REVTeX archive are
stored under `raw/writing/template/`; their hashes are listed in
`raw/writing/template/README.md`.

## Current route decision

- **P-ADO alignment-response paper:** EPJA Regular Article is the first target.
  Its contribution is a response/coverage method with a public benchmark, and
  it needs enough space for covariance contracts, family profiles and
  pseudo-experiment limits.
- **133Ce response-aware identifiability paper:** EPJA Regular Article first;
  PRC Research Article only after response, producer lineage, holdout and
  user-data access are closed.
- **PLB:** reserve for a later short result with one compact, independently
  validated physical conclusion. Neither current candidate has reached that
  threshold.

## Official requirements used in the decision

The EPJA pages describe Letters, Regular Articles and Code Papers, recommend the
Springer Nature LaTeX template with the `[iicol]` double-column option, and
require a Data Availability Statement for original research. The EPJA Letter
page limit is a journal-specific constraint; the current P-ADO draft is being
treated as a Regular Article candidate.

The APS PRC pages distinguish Research Articles and Letters, point authors to
REVTeX, and require a Data Availability Statement. The current REVTeX archive
is retained for a possible later PRC route.

Elsevier's general author and research-data policies were retrieved, while the
live PLB Guide for Authors endpoint returned an access failure in this runtime.
No PLB page-limit claim is admitted until the official guide can be directly
read.

## Evidence boundary

These are current submission and policy facts, not scientific evidence for
wobbling, chirality or alignment. The journal fit is a planning inference from
the official scope and article types; final submission requirements must be
checked again immediately before submission.

## Research Trigger

用户要求在 EPJA、PRC 和 PLB 中选择适合当前单点创新的投稿路线，并下载可用
的官方 LaTeX 模板。

## Grounded Evidence

官方 Springer、APS 和 Elsevier 页面快照及访问边界保存在上面的 manifest；
Zobel source 和 P-ADO project 提供当前 primary paper 的科学范围。

## Provisional Reasoning

P-ADO 公开数据方法学结果目前更像 EPJA Regular Article；`133Ce` 在 response
和数据权限闭合后才有 PRC Research Article 的可能。PLB 需要更短、更独立、
更强的单一结果。

## Assumptions

期刊路线判断基于 2026-11-05 取得的官方页面，不把第三方投稿经验或无法访问
的 PLB 旧版页数当作当前硬要求。

## Competing Explanations

期刊选择可能因编辑范围、数据权限、作者署名和结果强度变化；模板可用不等于
稿件已满足投稿门。

## Transfer Conditions

本路线只适用于当前 P-ADO 与 `133Ce` 候选；其它文章仍需按提交时的官方页面
重新核对。

## Failure Conditions

若 official guide 更新、数据不能按要求提供、或核心 claim 不能通过 evidence
gate，当前模板和期刊选择必须回退为 local draft。

## Falsification or Reverse Tests

提交前重新打开官方 aims/scope、submission guidelines、data policy 和 template
版本，逐项对照 manuscript、DAS、code availability 和 source package。

## Open Questions

- P-ADO coverage/feeding-aware result 是否达到 EPJA Regular Article 的实质创新门？
- `133Ce` private-data release/controlled-access 条件能否满足 PRC/EPJA DAS？
- PLB 当前官方 Guide for Authors 何时可在本运行环境直接取得？

## Human Review

本页记录 Codex self-audit；未发生用户或编辑部审核。

## Promotion or Rejection History

2026-11-05：P-ADO 设为 primary EPJA candidate；`133Ce` 设为 secondary
EPJA/PRC candidate；PLB 暂不作为当前默认路线。
