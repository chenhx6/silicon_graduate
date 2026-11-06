---
type: source
title: "Kumar等2024：129Ba分支报告与模型辅助混合比"
aliases: [Kumar DAE67 Ba129 branching]
created: 2026-11-06
updated: 2026-11-06
status: ai-draft
review_status: unreviewed
source_type: conference-experiment-model-report
reading_depth: read
title_original: "Measurement of the B(M1)/B(E2) ratios in 129Ba"
authors: [S. Kumar, Mallicka Kundu, P. S. Rawat, Ksh. Rojeeta Devi, H. Chutani, M. Goyal]
journal: DAE Symposium on Nuclear Physics
volume: 67
pages: 121-122
year: 2024
canonical_source: https://inspirehep.net/literature/2765575
citation_key: Kumar2024Ba129Branch
citation_key_origin: original-PDF-and-exact-document-key-metadata
raw_file: raw/papers/gpt/query/20261106-ba129-independent-branch-data/manifest.json
raw_sha256: 7623d5101ae3fa77712e476da52f449a3e2dca82863ecea5589d9a16f651d3a8
archive_required: true
nuclei: [129ba]
reactions: [121Sb-12C-p3n]
observables: [photon-branching-ratio, model-assisted-BM1-BE2]
tags: [a130, independent-acquisition, intensity, source-dependence, gate]
---

# 新采集不等于新的独立混合比测量

## Bibliographic Record

两页原件；精确document-key查询确认INSPIRE2765575与文件哈希对应，
出版登记为2024，会议标识C23-12-09。PDF无印刷年份；
其2023创建时间不替代出版年。作者以PDF六人名单为准，目录漏一人。

## Scope and Reading Depth

完整读两页，视觉核Eqs.1–4与图；从矢量图核六个点，
未取得原矩阵、峰面积表、校正文件或完整误差模型。

## Summary

独立的Sb/C–INGA采集提供候选强度信息。上面板为δ=0的强度代理量，
下面板使用转动假设估计混合；不能把两者当作独立电磁观测。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| KU-1 | 121Sb(12C,p3n)，66MeV，IUAC；靶1.2mg/cm²、Au背衬10mg/cm²，18clovers加2LEPS。原文未给总事件数或采集日期。 | acquisition | direct-original | PDFp.1 Experimental Details | true |
| KU-2 | 上面板量S按δ=0计算，若跃迁对和强度处理确定，可由r=S Ed³/(0.6967 Eq⁵)还原光子比。 | observable-definition-and-inference | direct-plus-rate-algebra | p.1 Eqs.1–2 | true |
| KU-3 | Fig.2/3重复同组六点；旧点来自Byrne1992，不能重复计数。 | dependency | direct-and-vector-check | p.2 Figs.2–3及Ref.3 | true |
| KU-4 | Eq.3按其λ定义缺少λ因子；补全的纯K关系须另满足0≤fE2≤1。不能据排印式断定原程序如何算。 | source-consistency | visual-original-plus-independent-CG | p.2 Eq.3；p.1 Eq.2 | true |
| KU-5 | 展示174.1-keV门谱，但未说明该门是否生成全部比值，也未列角关联、效率、时间及门路径校正。 | experimental-boundary | direct-original | p.1 Fig.1及正文 | true |

## Competing Interpretations and Limitations

用1992/2014候选能量对反演的新13/2点r约5.58，仅是图形审计候选。
尚未把图中误差条解释成σ/CL，也未认证新旧点的逐对身份。
174.1若对应评价173.6-keV门，列出的365/462路径均到达同一后续态；
连通性不证明接受率相同。下方混合结果及理论曲线保留模型依赖。

## Extracted Pages

- [[ba129-core-and-pairing-validity]]
- [[ba129-model-input-and-holdout-contract]]
- [[byrne-1992-129ba-bandcrossing-primary]]

## Human Review

Codex原件/代数/矢量图self-audit。状态为候选独立强度证据，
不作为已验证分支表或独立δ数据。
