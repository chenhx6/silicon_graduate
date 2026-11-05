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
raw_file: raw/papers/gpt/query/20261105-ba129-primary/evidence/manifest.json
raw_sha256: 3c613ebc9613aa4ee4a42e2084a935db5049530264b5647fe31982734d40ac44
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

已读 `gizon1977-full-json.json` 的
`/full-text-retrieval-response/originalText`：出版商返回的全文 OCR 文本
覆盖引言、实验、能级讨论、模型比较、总结与参考文献（印刷 pp.464–476）。
深读 §§2–3、Tables 1–3、§4.1 的模型输入及引用的 Yamazaki/Diamond
取向处理。它不是完整扫描 PDF 的视觉复核。

两次出版商 PDF 请求均只取得第一页（printed p.464）。HAL 的外链
ISTEX 端点重定向至身份认证；没有登录。Table 1 的正负号、误差分隔符和
分数自旋在 OCR 中有损，尚不能认证印刷表格全部数字。尤其不能由 OCR
中缺少一个负号推断原表一定为正，或据此修改 ENSDF 原件。

Gizon 1978 偏振论文仍只有本轮题录/访问记录：APS PDF 403、Harvest
401、HAL notice、CORE 精确 DOI 检索无结果。未读其正文。

## Summary

本文通过重离子反应研究 129Ba 能带及连接，角分布用于多极性和混合比，
并与三轴核芯模型比较。此次取得原始正文补充了角分布的单谱采集条件、
强度归一条件和原作者的取向假设，也暴露出原表 OCR 与后续评价之间的
误差尺度差异。差异原因尚未确定，不能默合两种版本。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| GI77-1 | §2 描述 Grenoble 碳束和 120Sn 靶；角分布测量使用七个角度，γ–γ 符合用于能级连接。正文将单谱强度与符合分析分别介绍。 | experimental-method | publisher-original-text | printed pp.465–466, §2；JSON originalText 的 “The experiment” 段 | true |
| GI77-2 | Table 1 强度在相对束流 55° 处给出；不能不经角分布/效率核对就把该列当全立体角光子分支。 | experimental-definition | publisher-original-text | printed p.465, paragraph before Table 1 | true |
| GI77-3 | §3.1 将 365.0 与 461.8-keV 线放在同一母态退激分支；后续评价的 364.7/461.6 标签须按连接关系映射，不能精确能量等同。 | level-connection | publisher-original-text | printed p.469, §3.1; Table 1 and Fig.3 references | true |
| GI77-4 | 在讨论 701.4-keV 线的自旋判别时，作者提到 α2 约0.5与 α4 小于0.2的部分取向修正；这些数不能自动移给365-keV母态，也不是 detector Q4。 | method-and-scope | publisher-original-text-with-OCR-boundary | printed p.469, end of §3.1 | true |
| GI77-5 | Table 1 的出版商 OCR 对365.0行读出 A2 的误差尺度0.05；对461.8行读出 A2/A4 的误差尺度0.04/0.06。现存2014 ENSDF 对应数为0.03与0.02/0.05。原扫描页及1978正文未得，不能认证这是哪一步修订、排印或OCR差异。 | version-discrepancy-candidate | publisher-OCR-versus-evaluated-record | printed p.466 Table 1；ENSDF129056013 lines137/141 | true |
| GI77-6 | Table 2 的365.0行给历史混合比区间约 −0.97至−0.79；2024重分析的大模结果是另一个分析层，不能称作本原始表测量值。 | attributed-derived-result | publisher-original-text | printed p.471 Table 2；同页Table 3为派生相对E2强度 | true |
| GI77-7 | 作者明确以三轴核芯模型作为一种理论解释，讨论振子模型等替代描述；能谱比较不直接给本任务所需的探测器响应或系数协方差。 | interpretation-and-boundary | publisher-original-text | printed p.465 Introduction; pp.472–475 §4 and conclusion | true |
| GI77-8 | 作者在讨论末尾明确说已计算混合比与相对B(E2)，但与Tables 2–3的实验派生量符合不佳，因此未给显式比较。能谱的定性符合没有同时闭合电磁预测。 | author-reported-model-limitation | publisher-original-text | printed p.475, final paragraph of §4.2 immediately before §5 | true |

## Competing Interpretations and Limitations

原始单谱采集描述减少了“必有不同符合门”的猜测空间，但没有给本任务可重放的
逐角净峰、接受函数、污染控制与协方差。既有 [[ba129-365-mixing-reference-boundary]]
中的同母态代数仍为条件检验。共同母态取向、有限接受、参考纯度和坐标约定是
不同条件；其中任一失效不能都改名为“负 Q4”。

原件 OCR 的误差尺度仅可用于明确标注的版本敏感性计算。若暂采用
参考误差0.06，二倍边际区间为 −0.04至0.20；在 s4=1、0≤fE2≤1 的
假设下映射的目标上界变为0.1067，与目标二倍区间0.06至0.26相交。
这是误差尺度改变导致的代数敏感性，不是新的实验置信区间；也表明不能把
上一版“二倍边际盒不相交”解释为稳健排除。

## Knowledge Impact and Learning Decision

`revises`：此前“Gizon1977 body unavailable”已被授权 FULL JSON
全文取代；可视 Table 1 和1978正文仍未取得。数字/符号层保持待核。

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

正文取得、扫描页缺失和 OCR 风险分别登记。没有把 metadata/首页当全文，
没有修改原件，没有补实验协方差，没有把 self-audit 写作 human-reviewed。
