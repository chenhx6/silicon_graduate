---
type: research-note
title: "`32S` 四极矩早期比较源 Vermeer 1982 的访问边界"
aliases: [32S Vermeer 1982 source access boundary]
created: 2026-10-31
updated: 2026-10-31
status: active
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [mavela-2019-32s-quadrupole-moment-doppler-correction-thesis]
created_from: "Day28 bounded source-access audit"
promotion_target: "mavela-2019-32s-quadrupole-moment-doppler-correction-thesis"
scope: 32s/quadrupole-moment/source-access
nuclei: [32s]
observables: [spectroscopic-quadrupole-moment]
tags: [32s, quadrupole-moment, source-access, evidence-boundary, needs-review]
---

# `32S` 四极矩早期比较源 Vermeer 1982 的访问边界

## Research Trigger

Vermeer、Esat 和 Spear 1982 的 `32S` 第一激发态四极矩论文能否提供一个可与 Mavela 2019 GOSIA 结果逐项比较的独立历史测量？

## Grounded Evidence

Crossref DOI 元数据确认题名为 *Quadrupole moment of the first excited state of 32S*，作者为 W. J. Vermeer、M. T. Esat 和 R. H. Spear，刊载于 *Nuclear Physics A* 389(1), 185–190 (1982)，DOI 为 `10.1016/0375-9474(82)90297-4`，PII 为 `0375947482902974`。这些字段来自 `tmp/day28-32s-vermeer/crossref.json`，属于书目身份，不是科学结果。

DOI 落地页可返回 Elsevier 重定向页面。Crossref 暴露的 text-mining XML 端点在无授权请求下只返回最小化元数据警告；plain-text 请求返回 HTTP 400。当前没有取得正文、摘要、表格、方法、四极矩数值或符号约定。原始响应头和正文保存在 `tmp/day28-32s-vermeer/`，并由本轮命令记录其字节数与 SHA-256。

## Provisional Reasoning

当前唯一可复用结论是来源访问边界：书目身份已闭合，科学内容未闭合。没有正文时，不能把题名、卷页或 PII 当作 `Q_S` 的旧测量值，也不能从出版社的最小化元数据推断实验方法、符号约定或独立性。

## Evidence Boundary

Mavela 2019 的现有 source 页 `DD-20260910-32S-03` 已明确：`Q_S` 的符号是谱学观测量，形状解释依赖约定和模型；其历史比较源尚未闭合。本轮新增 `DD-20261031-32S-29` 只把“出版社路线未提供正文”变成可复现的访问边界，不把书目元数据升格为旧实验结果。

目前不能判断以下问题：

- Vermeer 1982 的 `Q_S` 数值及其不确定度；
- 旧论文采用的重定向、库仑激发或其它测量方法；
- `Q_S` 的符号、坐标和约定是否与 Mavela 2019 一致；
- 两个结果是否来自独立实验谱系，或是否存在共同前期数据。

## Assumptions

Crossref metadata、DOI/PII 和出版社接口响应属于来源身份与访问记录；它们不代表论文正文。临时响应文件未被写入 `raw/`，也未被当作完整原件。

## Competing Explanations

正文未取得可能只是访问权限、版本或托管路径问题，也可能存在作者手稿、机构扫描或摘要可得而正文不可得的情况。当前不能把“未访问到”解释为“论文没有结果”。

## Transfer Conditions

本访问审计模板可迁移到其它历史核结构比较源，但每个来源仍需独立确认 DOI、版本、正文状态和授权边界；不可用本页的访问失败推断其它论文的可得性。

## Failure Conditions

若后续只取得搜索摘要、书目元数据或无法逐页核对的二手引用，仍不能完成 `32S` 四极矩相容性判断；若新副本缺页、图表或实验方法，必须保留 partial source 状态。

## Falsification or Reverse Tests

取得 Vermeer 1982 正文、作者手稿或机构扫描后，逐项核对方法、反应、`Q_S` 定义、数值和误差，并检查是否与 Mavela 2019 独立。若新证据给出可比较的 `Q_S` 与相同符号约定，本页的“科学内容未闭合”状态应更新；若只确认书目信息，则不改变。

## Open Questions

- Vermeer 1982 的 `Q_S` 数值、误差和符号约定是什么？
- 该实验采用何种库仑激发或其它测量方法？
- 它与 Mavela 2019 是否真正独立，还是共享更早的数据或分析谱系？

## Next Route

下一条高信息路线是检索机构仓储、作者档案和可访问图书馆副本；若取得正文，按题名、方法、核反应、`Q_S` 定义、误差来源和实验谱系逐项建立 comparison table。若只取得摘要或二手引用，仍只能标为 partial source and metadata-assisted lead，不能裁决相容性。

## Knowledge Impact and Learning Decision

`limits`：本轮没有改变 `32S` 四极矩的科学排序，也没有增加独立实验权重。

`supports`：本轮支持把“早期比较源未读”写成可验证、可复跑的来源访问边界，避免后续把 Crossref 标题或出版社元数据误写成旧测量值。

## Sources

- [[mavela-2019-32s-quadrupole-moment-doppler-correction-thesis]] — `DD-20260910-32S-03` 与 `DD-20261031-32S-29`。
- Crossref DOI metadata: `10.1016/0375-9474(82)90297-4`，本轮保存于 `tmp/day28-32s-vermeer/crossref.json`。
- Elsevier text-mining response for PII `0375947482902974`，本轮保存于 `tmp/day28-32s-vermeer/`。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-10-31 | bounded source-access audit | none | provisional | DOI/PII identity verified; primary body unavailable | [[mavela-2019-32s-quadrupole-moment-doppler-correction-thesis]] |

## Human Review

`review_status: unreviewed`。本页只记录来源身份和访问失败边界；在取得 Vermeer 1982 正文前，不对历史四极矩作相容性或冲突判断。
