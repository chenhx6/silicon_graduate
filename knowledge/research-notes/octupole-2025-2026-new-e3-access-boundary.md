---
type: research-note
title: "2025–2026 新八极 E3 证据的访问与梯度边界"
aliases: [recent octupole E3 evidence boundary, 2025 2026 direct E3 leads]
created: 2026-10-31
updated: 2026-10-31
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole, gaffney-2013-pear-shaped-rn-ra]
created_from: "Day31 external literature discovery during full-library review"
promotion_target: "post-30-day-nuclear-structure-paper-prospectus"
scope: octupole/e3/e1/recent-literature/source-access
tags: [octupole, e3, e1, recent-literature, source-access, evidence-ladder]
---

# 2025–2026 新八极 E3 证据的访问与梯度边界

## Research Trigger

现有 Wiki 的八极证据梯度以 `144Ba/146Ba` 直接 `B(E3)`、`220Rn/224Ra` E1/E3 与静态/动态解释为主。2025–2026 的新 primary 线索正在改变跨质量区证据排序：`90Zr` 2024/2026、`148Dy` 和 `224Ra` 已完成正文读取，`209Pb` 仍为 metadata-only。

## Grounded Evidence

| Candidate source | Current public locator | Discovery-level evidence | Boundary |
|---|---|---|---|
| `148Dy` | arXiv `2609.21499`; *Phys. Rev. C* **114**, 024338 (2026) | 已取得公开全文；GRIFFIN fast-timing/branching 分析报告低激发 `B(E3)`，并讨论其在 N=82 附近的系统学位置 | 仍需完成 version-of-record、反应响应、feeding 和协方差审计 |
| `90Zr` 2024/2026 pair | *Phys. Rev. C* **110**, 064312 (2024), DOI `10.1103/PhysRevC.110.064312`; *Phys. Lett. B* **879**, 140670 (2026), DOI `10.1016/j.physletb.2026.140670` | The 2024 full text reports plunger/fast-timing `T1/2(3−)=7.8(16) ps` and `B(E3;3−→0+)=16(3) W.u.`; it accounts for about `0.2 ps` possible `4+→3−` feeding and target-stopped recoil contributions, and compares the result with RPA. The 2026 full text now confirms safe Coulomb excitation in `32S+90Zr`, ADSSD plus 16-clover INGA detection, simultaneous projectile normalization, `gosia/gosia2` fitting, `B(E3;3−→0+)=19.6^{+1.7}_{-1.6} W.u.`, `Q_s(2+)=+0.09(10) eb`, and a fully correlated `χ²` uncertainty surface; QVSM reproduces the strength while harmonic-vibrator/RPA variants can overestimate it | Different methods and source versions still require a matched response/feeding/lineage audit before treating them as an independent validation pair; the 2026 body is read, but producer-level data release and cross-method joint covariance remain unavailable |
| `148Dy` | arXiv `2609.21499`, PDF pp.1–8, SHA in `tmp/day31-octupole-fulltext/` | GRIFFIN fast-timing GCD lifetime + ground-state branching gives `B(E3;3−→0+)=46(3) W.u.` and `B(E1;3−→2+)=2.7(3)×10^-3 W.u.`; paper reports this as enhanced E3 beyond `Z=64` | Full source is now locally readable, but exact reaction/response covariance and final version-of-record lineage still need paper-level audit |
| `224Ra` | arXiv `2609.07556`, PDF pp.1–7, SHA in `tmp/day31-octupole-fulltext/` | Independent GRIFFIN/PACES lifetime and IC analysis reports `B(E1)` values of `(3.5±0.1)×10^-5`, `(7.4±0.4)×10^-5`, `(3.6±0.2)×10^-5 W.u.`, `B(E3;3−→1−)=98(4) W.u.`, and `Q_10≈0.029–0.033 efm`; authors state agreement with prior Coulomb excitation while using different observables | The analysis is now full-text readable, but covariance across branching/IC/timing and exact independence from all cited datasets still needs audit |
| `90Zr` 2024 | *Phys. Rev. C* **110**, 064312 (2024) | 已取得 APS 正文；`T1/2=7.8(16) ps`、`B(E3)=16(3) W.u.`、feeding 与 RPA 比较已定位 | plunger response、feeding 和 systematic discussion 已读，但没有 producer-level event files 或联合 covariance |
| `150Gd` | *Phys. Rev. Lett.* **134**, 092501 (2025) | 公开发现线索指向新 `B(E3)` systematics，可作为中重核补充质量区 | 需核对全文和与现有 E3 数据的 measurement lineage |
| `209Pb` | *Nuclear Physics A* **1066**, 123273 (2026), DOI `10.1016/j.nuclphysa.2025.123273` | Crossref 题名确认一项 `15/2−` 八极态新寿命测量 | 当前只有元数据；没有数值寿命、分支、响应或全文，保持 metadata-only |

Existing anchors remain [[bucher-2016-144ba-direct-octupole]], [[bucher-2017-146ba-direct-octupole]] and [[gaffney-2013-pear-shaped-rn-ra]]. The new `90Zr` 2024/2026, `148Dy` and `224Ra` items now have full-text staging or local PDF locators, while `209Pb` is metadata-only. Their response/covariance manifests and final lineage audits remain pending.

## Full-text locator map

| Source | Atomic claim | Exact locator |
|---|---|---|
| `148Dy` arXiv `2609.21499` | combined lifetime/branching method and `B(E3)=46(3) W.u.` | extracted text lines 59–70, 298–355; PDF pp.1, 5 |
| `148Dy` arXiv `2609.21499` | `B(E1;3−→2+)=2.7(3)×10^-3 W.u.` and N=82 trend | extracted text lines 346–365; PDF p.5 |
| `224Ra` arXiv `2609.07556` | lifetime/IC-derived transition strengths and independent validation statement | extracted text lines 215–279; PDF pp.4–5 |
| `224Ra` arXiv `2609.07556` | table values for `B(E1)`, `B(E3)` and `Q_10` | extracted text lines 315–330; PDF p.5, Table I |
| `90Zr` 2024 full text | `T1/2(3−)=7.8(16) ps`, `B(E3)=16(3) W.u.`, feeding and RPA comparison | APS PRC PDF pp.1, 3–6; `tmp/day31-octupole-fulltext/90zr-2024-prc.txt` lines 18–28, 216–246, 270–320, 410–430; SHA-256 `0e5dd420ca551f176eb2cee1ceb39eb5f7b4fbff85147a7cfec4a30f9f6a0f35` |
| `90Zr` 2026 full text | safe Coulomb excitation, `3−→0+` direction, `B(E3)`, `Q_s`, `gosia/gosia2` fit, correlated `χ²` surface and model comparison | Elsevier TDM XML/text, `tmp/day31-octupole-fulltext/90zr-2026-plb.xml` and `.txt`; PDF/object producer and SI objects are available through the licensed API route; raw event matrices and cross-method joint covariance were not acquired |
| `90Zr` Crossref lineage | distinct 2024 PRC and 2026 PLB records | `tmp/day31-octupole-fulltext/90zr-2024-crossref.json`; `90zr-2026-crossref.json` |

The extracted text and PDF hashes are preserved under `tmp/day31-octupole-fulltext/`; no raw archive was modified.

## Provisional Reasoning

这些新来源最可能改变的是证据梯度的质量区覆盖和“直接 E3 是否能跨质量区迁移”的问题，而不是自动证明静态梨形。`148Dy` provides an E3-first direct-strength anchor with an explicitly measured E1 branch; `224Ra` supplies an independent lifetime/IC validation and a strong E3–quenched-E1 contrast. 论文级 comparison 至少要统一：

1. `B(E3)` 的跃迁方向、单位和自旋统计因子；
2. Coulomb-excitation/fast-timing/γ-spectroscopy 的响应、feeding 和效率；
3. E1 dipole、E3 matrix element 与 PES/`β3` 的 evidence tier；
4. 同一实验复测、评估库和模型预测的 source lineage；
5. 至少一个静态/动态竞争解释和一个 holdout。

`148Dy` 还把八极梯度连接到现有 N=82 观测边界：它位于同一 N=82 等中子链的更高 Z 区域，而 Wiki 已有 `132Sn`/`134Te` 的 `E(2+)`、`B(E2)` 和质量/转移分层。这个并排比较可用于研究“壳闭合与八极关联如何共存”，但 `E(2+)`/`B(E2)` 与 `B(E3)` 约束不同自由度；不能把 `148Dy` 的 E3 增强直接解释成 `132Sn` 单粒子壳隙变化。`209Pb` 则提供了一个不同质量区的寿命方法入口，但当前仍没有可比较的数值。

For the `90Zr` method-separated pair, a bounded arithmetic check gives
`19.6−16.0=3.6 W.u.` and a symmetricized combined uncertainty
`sqrt(3.0²+1.65²)=3.42 W.u.`, or about `1.05σ` (using either asymmetric 2026 error
gives about `1.04–1.06σ`). This is only a conditional comparison of printed summaries.
It is not a pooled compatibility test because the plunger/fast-timing and
Coulomb-excitation feeding, response, normalization and cross-method covariance have
not been aligned.

## Assumptions

`90Zr` 2024 与 2026 均已跨过全文可读门；`209Pb` 仍停在
metadata-only。`209Pb` 的 Elsevier TDM shell 可达，但正文路径受 403/429 访问边界
限制。不同来源的数字仍按 source version、方法和 lineage 分层，不自动视为独立同分布实验。

## Competing Explanations

相近 `B(E3)` 可来自不同集体机制、feeding/响应合同或统计覆盖；显著不同 E1 仍可能由占据、偶极抵消和形状软化共同产生。弱 E1、PES 极小和单条 E3 都不能独立证明静态八极。

## Transfer Conditions

新来源只能在逐条 primary locator、实验反应、响应、误差和独立性清楚后加入跨质量区 evidence ladder。不能把一个核的 E3/E1 数值或模型解释直接迁移到另一个质量区。

## Failure Conditions

若只能取得搜索摘要、元数据或无完整表格的新闻稿，保持 `metadata-only`；`148Dy/224Ra` 已跨过全文可读门，但若缺分支/寿命/响应/协方差，仍不做统一显著性、模型拟合或原创物理结论。

## Falsification or Reverse Tests

对每个新候选预先检查：统一单位和方向后，E3-first ranking 是否仍稳定；若新正文显示 E3 依赖模型强约束或与同实验 E1/feeding 不一致，应降低其 evidence tier，而不是强行加入数据库。

## Open Questions

- `148Dy`、`224Ra`、`209Pb` 新来源的正式版本、完整表格和实验 response 是否公开？
- 新来源是否提供多态 E3、寿命或独立偶极/四极 observable？
- 哪个新核最适合形成跨质量区原创 data-map，而不是已有结果的综述重排？
- `148Dy` 的 E3 enhancement 与 `224Ra` 的 E3/E1 separation 能否在同一 occupancy-sensitive / response-aware table 中比较，而不把不同方法的误差当独立同分布？

## Human Review

本页是发现阶段 self-audit，`review_status: unreviewed`、`reasoning_status: provisional`。在全文和原始 locator 关闭前，不把新候选写成 Wiki 事实层或期刊主结论。

## Knowledge Impact and Learning Decision

`supports`: 现有八极 evidence ladder 值得扩展到 `90Zr/148Dy/224Ra` 等新质量区，并保留
`90Zr` 2024 lifetime/plunger 与 2026 Coulomb-excitation 两条正文级方法锚点。

`limits`: `90Zr` 2024/2026 的正文级方法链已进入 source-access ledger，但仍没有
event-level producer 或跨方法联合 covariance；不做 pooled mean、统一显著性或静态
梨形裁决。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-10-31 | recent-literature discovery and access pass | none | provisional full-text staging | `90Zr` 2024 APS PDF, `90Zr` 2026 licensed TDM XML/text and `148Dy/224Ra` PDFs were acquired to `tmp/`; `209Pb` remains metadata-only | [[post-30-day-nuclear-structure-paper-prospectus]] |
