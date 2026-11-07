---
type: source
title: "Ding等2025：A≈60手征与残余质中力（摘要边界）"
aliases: [Ding 2025 A60 chirality, Ding2025CPC]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
source_type: theory-article
reading_depth: metadata-only
title_original: "Exploring chiral rotation in A≈60 nuclei: Role of residual interactions"
authors: [G. L. Ding, R. Dong, H. Y. Liu, J. Peng, Q. B. Chen]
journal: Chinese Physics C
year: 2025
volume: 49
pages: 074101
doi: 10.1088/1674-1137/adc3fd
canonical_source: "doi:10.1088/1674-1137/adc3fd"
citation_key:
raw_file: raw/papers/gpt/query/20261107-round2-orientation-window/ding-full/ding-2025-cpc-jats.xml
raw_sha256: 504ec53861a4a00c6d2deb178c3d29d847fc7b938bb3c201617b26011a448244
archive_required: true
tags: [chirality, a60, residual-interaction, prm, abstract-only]
---

# A≈60残余质中力：实际取得摘要而非正文

## Bibliographic Record

G. L. Ding et al., CPC49,074101(2025)，DOI10.1088/1674-1137/adc3fd。
取得Crossref查询XML，官方CPC正文/PDF路径在本轮终端访问失败；
失败不证明所有合法渠道或以后的请求均无法取得。

## Scope and Reading Depth

XML的根为crossref_result，query_result/body属于查询架构，
不是JATS论文article/body。它包含题录、JATS摘要及参考文献索引，没有正文sec。
摘要数学内容放在XML processing instruction（形如CDATA）中，普通itertext会漏掉，
本轮用原始XML文本核对公式；不声称完整PRM推导、图或73条文献均已读。

## Key Results

| ID | 实际摘要内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DC25-1 | 研究钴同位素的πf7/2−1⊗νg9/2¹组态，在PRM中含残余质中相互作用，考察能谱、强度、交错及主轴/取向分布。 | author-model-report | abstract-only | XML jats:abstract | true |
| DC25-2 | 摘要对该指定组态给β=.25、γ=34°、J=10ℏ²/MeV的理想手征参数。 | author-model-report | abstract-only | jats:abstract内tex-math processing instructions | true |
| DC25-3 | 摘要称ΔE(I)、S(I)对残余力敏感，较弱残余力更利于该研究中的手征；不能扩展为所有核的单调定律。 | author-interpretation | abstract-only | XML摘要后半 | true |

## Summary

这是轻区模型条件值得继续核查的新文献，不是新的手征实验确证。
摘要已能支持“组态与残余相互作用影响窗口”的问题，不能据此重建全部Hamiltonian。

## Competing Interpretations and Limitations

未核对力的具体形式/参数、扫描范围、概率图与完整电磁算符，
不据摘要推导固定的共面塌缩阈值、自旋转变点或所有多体构型的必要条件。
理想输入参数不是实测γ，也不等于自洽PES极小。

## Extracted Pages

无论文正文页读取。XML摘要/公式和题录读取；正文和PDF/SI未取得。
窗口比较见[[light-and-rare-earth-orientation-window-round2-20261107]]。
