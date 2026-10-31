---
type: source
title: "NNDC 110Cd Adopted：高自旋寿命、E2 分支与内转换"
aliases: [NNDC110Cd adopted Roy lifetimes, 110Cd 1100-keV branch evaluation]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
source_type: evaluated-nuclear-data
reading_depth: skimmed
title_original: "110CD ADOPTED LEVELS, GAMMAS"
authors: [G. Gürdal, F. G. Kondev]
journal: Nuclear Data Sheets
year: 2012
volume: 113
pages: "1315"
citation_key: NNDC110CdAdopted2012
citation_key_origin: ENSDF-header-local-key
canonical_source: "NNDC ENSDF 110048001,110CD, ADOPTED LEVELS GAMMAS"
source_url: "https://www.nndc.bnl.gov/ensdf/"
data_version: "2012-06 listing; H header NDS 113, 1315 (2012), CUT 1-Aug-2011; H MOD 6-Mar-2018 for unrelated 164.26-keV B(E2)"
raw_storage_status: "official-response-archived-as-retrieved-html-wrapper"
raw_file: "raw/data/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/110cd-adopted-110048001-023.html"
raw_sha256: "83f11abd165777b820eb116d77bed3a7d71f30b789d0557c176cd7d987439647"
nuclei: [110Cd]
reactions: [heavy-ion-gamma, 96Zr-18O-4n]
observables: [level-half-life, gamma-branch-intensity, conversion-coefficient, B(E2)]
methods: [ENSDF-evaluated-fixed-column, DSAM-source-lineage]
tags: [antimagnetic-rotation, lifetime, E2, evaluated-data, branch-identity]
---

# $^{110}$Cd 评价寿命、分支与 $B(E2)$

## Bibliographic Record

NNDC `DatasetFetchServlet(nuc=110Cd,searchType=quick,datasource=ensdf)` 列出 `110048001,110CD` Adopted；以 `EnsdfDispatcherServlet(dbclass=ensdf,page-source=singular,datasetcheck=110048001,110CD,chooseit=ENSDF text format)` 获取固定栏对象。H 行为 G. Gürdal、F. G. Kondev，*Nuclear Data Sheets* **113**, 1315 (2012)，cutoff 2011-08-01；2018 年 E. A. McCutchan 修改涉及另一条 164.26-keV 跃迁的 $B(E2)$，不能当作本页五条高自旋线的新采集。归档文件为官方响应的 HTML 包裹 ENSDF `<pre>` 文本，SHA-256 如 frontmatter。

## Scope and Reading Depth

定向阅读 H 与 T(X) 总注、$16^+$–$24^+$ A/B L/G/S/B 记录；没有通读全部 2653 行，也没有重新分析 2011Ro01 的原始线形、feeding 或停止本领文件。这个评价对象引用 [[roy-2011-cd110-systematics-antimagnetic]] 的 2011Ro01 寿命，因此同一实验谱系的评价字段不能计为独立测量。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| NC110-1 | Adopted 中 $16^+,18^+,20^+,22^+,24^+$ 的 L 记录寿命字段依次为 $T_{1/2}=0.250(21),0.159(21),0.118(21),0.15(5),0.19(5)$ ps；总 T(X) 注指向 2011Ro01 的 heavy-ion DSAM 线形分析，并说明未计可能高达 20% 的停止本领系统误差。 | evaluated-lifetime-and-lineage | direct-evaluated-object | H 后 T(X) 注；L6100.87/L7325.3/L8648.3/L9962.3/L11320.3 | true |
| NC110-2 | 对应带内 E2 的 Adopted RI 为 100（$22^+$ 的 1314.1-keV 线注明 100(4)）；五线总内转换系数依次约 $9.73,7.47,6.56,6.63,6.32\times10^{-4}$。这些系数的量级不足以独立给出约一成的 $B(E2)$ 修正。 | evaluated-gamma-fields-and-derived-bound | direct-object-and-conditional-arithmetic | G1074.6/G1224.5/G1323.0/G1314.1/G1358.0 与各自 S 行 | true |
| NC110-3 | Adopted 的 $22^+$ L9962.3 同时列 1100-keV `RI=37(11)` 与 1314.1-keV `RI=100(4)`，但同一 cL T 注明确记载 Roy 2011 未在 $\gamma\gamma$ 符合门确认 1100-keV 线；此前含该线曾得 $T_{1/2}=0.11(4)$ ps，而 Roy 给 $0.15(5)$ ps。两套分支/寿命假设不可静默混算。 | evaluated-competing-branch-and-source-boundary | direct-evaluated-object | L9962.3 cL T 五至八行；G1100/G1314.1 | true |
| NC110-4 | Adopted B 行对五条带内线给 $B(E2)=50(5),41(6),38(7),22(8),21(6)$ W.u.；$22^+$ 的评价分支选择与 Roy Table 1 所用线形门/分支边界不同。 | evaluated-strength | direct-evaluated-object | 各 G 行后的 B 行；尤其 L9962.3 两支 | true |

## Summary

ENSDF 的 L 字段记录的是半衰期，除以 $\ln2$ 得到 Roy Table 1 的平均寿命中心值，分别约 $0.3607,0.2294,0.1702,0.2164,0.2741$ ps。此关系说明 023 审计中约 7–11% 的条件 $B(E2)$ 中心值偏差并非半衰期与平均寿命概念混淆。该偏差在同一寿命实验谱系的打印值之间，不能把 Adopted 的 B 行作为独立验证。

## Competing Interpretations and Limitations

内转换修正约千分之一。对 $16^+,18^+,20^+,24^+$，本对象所读 L 块各只列该条 RI=100 的带内线；其他未列分支不可凭空补入。$22^+$ 则存在明确的 1100-keV 分支争议，评价保留而 Roy 2011 不确认。原文 Table 1 的 $B(E2)$ 中心值与标准单分支寿命公式仍相差约一成，归一成因需要原作者计算输入、分支表或更正；不能由当前评价字段定因。条件合成误差的 $z$ 仅为尺度练习，因为 $B(E2)$ 与寿命取自同一拟合，协方差未知。

## Knowledge Impact and Learning Decision

`supports` 对平均寿命/半衰期和分支身份的来源对账；`limits` 把评价数据当独立实验或把 1100-keV 支线无条件加到 Roy Table 1 的做法。计算细目见 `outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/cd110-be2-normalization-audit-023.md/json`。

## Extracted Pages

- [[roy-2011-cd110-systematics-antimagnetic]]：原实验线形、Table 1 平均寿命与作者模型解释。
- [[antimagnetic-rotation]]：结果与模型解释分层的概念入口。

## Sources

- NNDC ENSDF `110048001,110CD`，官方响应与字段位置如上。
- [[roy-2011-cd110-systematics-antimagnetic]]，2011Ro01，评价寿命引用的同源实验。
