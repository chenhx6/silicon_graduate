---
type: research-note
title: "Egido–Robledo 1990 正文获取边界"
aliases: [Egido Robledo 1990 retrieval boundary, Day26 Egido access audit]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [bernard-2016-144ba-sccm-octupole, bucher-2017-146ba-direct-octupole]
created_from: Day26 lawful full-text retrieval audit
promotion_target: octupole-correlation
tags: [retrieval-boundary, octupole, Egido-Robledo, evidence-boundary]
---

# Egido–Robledo 1990 正文获取边界

## Research Trigger

BU17和Bernard 2016都引用 Egido–Robledo 1990 作为 Ba 区偶极/八极微观机制谱系。此前只取得 DOI、PII 和元数据，未取得正文；本单元按新的公开入口再次探测。

## Grounded Evidence

DOI `10.1016/0375-9474(90)90141-8`、PII `0375947490901418` 已由 Crossref/INSPIRE 元数据确认。`reader.elsevier.com` 返回 TLS handshake failure，ScienceDirect PDF 入口返回 HTTP 403；Elsevier API 在此前尝试仅返回 1852-byte metadata XML。完整尝试账本见 `egido-route-audit-042.json`。

## Provisional Reasoning

当前证据只支持“该文献存在且被后续来源引用”，不支持从书目信息恢复质子/中子偶极分项、有符号壳修正或生产HFB数值。Day26现有 007/015 自设分项已撤回，不能用二手引用填补。

## Assumptions

访问探测使用普通公开HTTPS请求，不绕过403、TLS限制、机构认证或付费墙；HTTP状态和元数据不等于正文。

## Competing Explanations

即使取得正文，Egido 1990仍可能是宏观微观平均场模型而非现代SCCM生产核；其结果需与BU17的占据解释和Bernard的投影算符核分层比较。

## Transfer Conditions

只有取得实际正文、页码/图表和模型版本后，才可把其数值写入source或偶极机制综合；作者解释和后续引用不能代替原文定位。

## Failure Conditions

若继续只有元数据、403或TLS失败，保持 `needs_review`，不宣称已阅读、不制造分项数值。

## Falsification or Reverse Tests

未来取得正文后，逐项核对其D0符号、轨道占据、β2/β3输入和E1/E3矩阵元，检查是否真的支持BU17的模型转述；若版本不同，保留谱系差异。

## Open Questions

作者或机构仓储是否有合法副本？1990模型使用的相互作用、配对与形变自由度与现代SCCM有何可比性？

## Human Review

本页为Codex self-audit，保持 `unreviewed`。

## Promotion or Rejection History

2026-10-28：新增公开入口探测记录；正文仍未取得，状态保持 provisional。
