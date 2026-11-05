---
type: source
title: "Gizon 1977：129Ba 原始角分布、同母态连接与版本边界"
aliases: [Gizon 1977 Ba129 primary, 1977Gi02 angular distributions]
created: 2026-11-05
updated: 2026-11-05
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-theory
reading_depth: read
title_original: "Triaxial shape and onset of high-spin bands in 129Ba"
authors: [J. Gizon, A. Gizon, J. Meyer-ter-Vehn]
journal: Nuclear Physics A
year: 1977
volume: 277
pages: 464-476
doi: 10.1016/0375-9474(77)90714-X
canonical_source: "https://doi.org/10.1016/0375-9474(77)90714-X"
citation_key: Gizon1977
citation_key_origin: agent-local-manuscript-bibliography
raw_file: raw/papers/gpt/query/20261105-ba129-model-readiness/gizon1977-main.pdf
raw_sha256: 017e979cea49b19daecc5394a5ca90e460ad0cb2c1a60edaf510e3b7dc446795
acquisition_manifest_file: raw/papers/gpt/query/20261105-ba129-model-readiness/manifest.json
acquisition_manifest_sha256: bc6ad44bff5658934c28d1df417453364db5f95d0f036369532454180b7187c6
archive_required: true
raw_storage_status: archived-local-publisher-api
nuclei: [129ba]
reactions: [120Sn-12C-3n]
observables: [angular-distribution-coefficient, multipole-mixing-ratio, relative-intensity]
methods: [angular-distribution, gamma-gamma-coincidence]
tags: [a130, source-version, same-parent, alignment, primary-source]
---

# Gizon 1977：129Ba 原始角分布

## Bibliographic Record

J. Gizon, A. Gizon and J. Meyer-ter-Vehn, *Nuclear Physics A* **277**,
464–476 (1977), DOI `10.1016/0375-9474(77)90714-X`。出版商 API 元数据、
所取首页及 HAL 记录相符。实际访问和时间以归档 manifest 为准。

## Scope and Reading Depth

初次取得全文 JSON/OCR 和两个仅首页的 PDF，旧访问回执保留在
`20261105-ba129-primary/evidence/manifest.json`。本轮改读出版商
`FULL XML` 的 `web-pdf-purpose=MAIN` 元素，从其明确给出的
`attachment-eid` 经标准 Object API 取得完整13页扫描 PDF；不是从首页
或下载器状态推断全文。

全文主线与方法/结果已结合先前OCR和本轮PDF读取。实际视觉核验包括
printed p.466 Table 1 的365.0、461.8行及表头/脚注，p.471
Tables 2–3，p.473 Fig.4参数，p.474–475模型讨论。没有声称逐像素核验
每一个谱峰或理论衰变箭头。旧“Table 1扫描页缺失”的边界现已关闭。

Gizon 1978 偏振论文仍只有本轮题录/访问记录：APS PDF 403、Harvest
401、HAL notice、CORE 精确 DOI 检索无结果。未读其正文。

## Summary

本文通过重离子反应研究 129Ba 能带及连接，角分布用于多极性和混合比，
并与三轴核芯模型比较。此次取得原始正文补充了角分布的单谱采集条件、
强度归一条件和原作者的取向假设，也暴露出原始表格与后续评价之间的
误差尺度差异。差异原因尚未确定，不能默合两种版本。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| GI77-1 | §2 描述 Grenoble 碳束和 120Sn 靶；角分布测量使用七个角度，γ–γ 符合用于能级连接。正文将单谱强度与符合分析分别介绍。 | experimental-method | publisher-original-text | printed pp.465–466, §2；JSON originalText 的 “The experiment” 段 | true |
| GI77-2 | Table 1 强度在相对束流 55° 处给出；不能不经角分布/效率核对就把该列当全立体角光子分支。 | experimental-definition | publisher-original-text | printed p.465, paragraph before Table 1 | true |
| GI77-3 | §3.1 将 365.0 与 461.8-keV 线放在同一母态退激分支；后续评价的 364.7/461.6 标签须按连接关系映射，不能精确能量等同。 | level-connection | publisher-original-text | printed p.469, §3.1; Table 1 and Fig.3 references | true |
| GI77-4 | 在讨论 701.4-keV 线的自旋判别时，作者提到 α2 约0.5与 α4 小于0.2的部分取向修正；这些数不能自动移给365-keV母态，也不是 detector Q4。 | method-and-scope | publisher-original-text-with-OCR-boundary | printed p.469, end of §3.1 | true |
| GI77-5 | 扫描Table 1确认365.0行 A2=−0.70(5)、A4=+0.16(5)，461.8行 A2=+0.22(4)、A4=+0.08(6)。2014评价误差分别为(0.03,0.05)/(0.02,0.05)。正号与误差差异已视觉核实；差异是否来自1978修订或评价处理仍未确定。 | primary-table-and-version-difference | direct-original-visually-checked | printed p.466 Table1；ENSDF129056013 lines137/141 | true |
| GI77-6 | Table 2 的365.0行给历史混合比区间约 −0.97至−0.79；2024重分析的大模结果是另一个分析层，不能称作本原始表测量值。 | attributed-derived-result | publisher-original-text | printed p.471 Table 2；同页Table 3为派生相对E2强度 | true |
| GI77-7 | 作者明确以三轴核芯模型作为一种理论解释，讨论振子模型等替代描述；能谱比较不直接给本任务所需的探测器响应或系数协方差。 | interpretation-and-boundary | publisher-original-text | printed p.465 Introduction; pp.472–475 §4 and conclusion | true |
| GI77-8 | 作者在讨论末尾明确说已计算混合比与相对B(E2)，但与Tables 2–3的实验派生量符合不佳，因此未给显式比较。能谱的定性符合没有同时闭合电磁预测。 | author-reported-model-limitation | publisher-original-text | printed p.475, final paragraph of §4.2 immediately before §5 | true |
| GI77-9 | Fig.4模型标注β=0.24、γ=21°、无量纲 \(\widetilde\lambda_F=+1.5\)、Δ=1.0 MeV；caption以最高两单粒子能量定义无量纲Fermi坐标。不能把+1.5直接作为MeV的λ。 | model-input-definition | direct-original-visually-checked | printed p.473 Fig.4 header/caption | true |

## Competing Interpretations and Limitations

原始单谱采集描述减少了“必有不同符合门”的猜测空间，但没有给本任务可重放的
逐角净峰、接受函数、污染控制与协方差。既有 [[ba129-365-mixing-reference-boundary]]
中的同母态代数仍为条件检验。共同母态取向、有限接受、参考纯度和坐标约定是
不同条件；其中任一失效不能都改名为“负 Q4”。

已核实的1977原表与2014评价分别输入，不能因后者精度更高便默认它是同一次
拟合的原始误差。采用原表参考误差0.06，二倍边际区间为 −0.04至0.20；
在 s4=1、0≤fE2≤1 的
假设下映射的目标上界变为0.1067，与目标二倍区间0.06至0.26相交。
这是误差尺度改变导致的代数敏感性，不是新的实验置信区间；也表明不能把
上一版“二倍边际盒不相交”解释为稳健排除。

## Knowledge Impact and Learning Decision

`revises`：Gizon1977全文和关键原表视觉核验均已完成；此前临时OCR尺度
已升级为原始表格版本。1978正文和误差修订来源仍未取得。

`limits`：[[ba129-rank4-identifiability]] 的算术闭合不构成文献新颖性
或实验裁决。下一步先完成来源版本与同母态 joint-coefficient 检验，
避免仅凭一个 marginal box 选根。

`motivates`：GI77-8给出一个真实的历史模型缺口。若开展129Ba模型研究，
应在明确band/state mapping后用能量确定参数，再检查独立保留的电磁量；
不能把能谱重现本身当作已经解决1977年报告的电磁不符合。该缺口不是
本任务新发现的物理效应，也不证明2024年的模型必然有同样偏差。

## Extracted Pages

- [[ba129-rank4-identifiability]]
- [[ba129-365-mixing-reference-boundary]]
- [[nndc-2014-129ba-365-coefficient-records]]
- [[chakraborty-2024-possibility-wobbling-129ba]]
- [[diamond-1966-nuclear-alignment-heavy-ion-reactions]]

## Self-audit

首页预览、全文OCR、完整扫描PDF分开登记并保留历史回执。没有修改原件，
没有补实验协方差，没有把 self-audit 写作 human-reviewed。
