---
type: source
title: "Bernard et al. 2016：144Ba 的对称性恢复与四极—八极组态混合"
aliases: [Bernard 2016 144Ba SCCM, Gogny D1S 144Ba projected GCM]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
source_type: theory
reading_depth: deep-read
title_original: "Octupole correlations in the 144Ba nucleus described with symmetry-conserving configuration-mixing calculations"
authors: [Rémi N. Bernard, Luis M. Robledo, Tomás R. Rodríguez]
journal: Physical Review C
year: 2016
volume: 93
pages: "061302(R)"
doi: "10.1103/PhysRevC.93.061302"
citation_key: Bernard2016SCCM144Ba
citation_key_origin: agent-local-key-with-Crossref-metadata
citation_key_verified: 2026-10-28
canonical_source: "Bernard, Robledo and Rodríguez, Phys. Rev. C 93, 061302(R) (2016); actual reading: arXiv1604.06706v1"
raw_file: "raw/papers/gpt/day26-20261028/bernard-2016-144ba-sccm-arxiv1604.06706v1.pdf"
raw_sha256: d339bbdde6991e19148ec2d619c79dba4fbb5ca95173084a33ed36a39232b997
nuclei: [144Ba]
models: [Gogny-D1S, HFB, SCCM, projected-GCM]
observables: [E1, E2, E3, excitation-energy, collective-amplitude]
tags: [octupole, quadrupole, symmetry-restoration, GCM, model-domain]
---

# 144Ba：投影 GCM 的实际计算对象与适用域

## Bibliographic Record

Crossref DOI 记录与 INSPIRE 的题名、三名作者和 arXiv `1604.06706` 相符。实际读取的是标注 `1604.06706v1 [nucl-th], 22 Apr 2016` 的六页 PDF；不是已取得的出版版。来源 URL 为 https://arxiv.org/pdf/1604.06706 。文件签名 `%PDF-`、页数与上述 SHA-256 已实际核验。

## Scope and Reading Depth

Day26 读取 PDF1–6 的全文主线、Eqs1–5、Figs1–4、Table I 和相关限制；参考文献仅按方法/实验谱系定向阅读。未取得生产代码、HWG norm/transition kernels、数值网格文件或原始实验协方差。SI 默认纳入获取范围，当前未确认出版商附件清单，不能将未检得写成不存在。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | source_independence | locator | needs_review |
| --- | --- | --- | --- | --- | --- | --- |
| BE16-D26-001 | 先作轴对称四极/八极约束 HFB，再恢复 J、宇称、N、Z，最后解 HWG 组态混合；只恢复对称性不等于已经进行 GCM 混合。 | model-method | direct-original-preprint | model-calculation | PDF1–2 Eqs1–3 | true |
| BE16-D26-002 | 本实现保轴对称、时间反演和 simplex，故只含偶 J 正宇称与奇 J 负宇称；不含三轴 K 混合与 cranking intrinsic states。谱伸展和偏小转动惯量是作者明列限制。 | model-domain | direct-original-preprint | model-calculation | PDF2 first two paragraphs; PDF4 discussion | true |
| BE16-D26-003 | 采用 130 个 intrinsic states、11 个球谐振子壳，β2∈[−0.4,0.5]、β3∈[−0.5,0.5]；β Euler 与 gauge 积分分别用32与9点。作者报告这些设置的收敛，不是本任务重算收敛。 | calculation-input | direct-original-preprint | model-calculation | PDF2 after Eq5 | true |
| BE16-D26-004 | HFB 最小值在(β2,β3)=(0.2,±0.1)，同时沿 β3∈[−0.2,0.2]较软。非零 mean-field minimum 与软性在该计算中共存；不能仅凭 minimum 给实验刚性认证。 | model-result | direct-original-preprint | model-calculation | PDF2–3 Fig1 | true |
| BE16-D26-005 | 可观测量含双坐标求和 f* O(q,q′) f；绘出的 F=N^(1/2)f 不是非正交基中的 f 本身。相似的 collective-amplitude 图不能取代 E1/E3 各自的投影算符核。 | model-method | direct-original-preprint | model-calculation | PDF2 Eqs4–5 | true |
| BE16-D26-006 | 2D GCM 的基态能低于两条1D路径；作者指出相对能级排序更好，但未声称全谱精确符合。三条1D/2D强度结果接近，不表示基底、谱与算符核相同。 | model-comparison | direct-original-preprint | model-calculation | PDF3–4 Fig3 and text | true |
| BE16-D26-007 | 2D 的0+↔3− E3矩阵元为0.460 e b^(3/2)，作者给向下 B(E3)=25 W.u.，落在 BU16 报告的宽误差内；4+↔6+、6+↔8+ E2偏差与缺少cranking/配对响应一并保留。 | model-result-and-limit | direct-original-preprint | dependent-on-Bucher2016-data | PDF4 Table I and discussion | true |
| BE16-D26-008 | 作者强调 good-J 计算跃迁强度可避免对许多不够强形变的构型套用转子近似；其本身仍受EDF、密度依赖 prescription 与截断空间约束。 | model-domain | direct-original-preprint | model-calculation | PDF2 density prescription; PDF4 before Table I | true |

## Summary

投影GCM把轴向四极与八极坐标共同混合，支持144Ba强八极相关的模型解释。其软PES、谱伸展与缺失自由度限制了从单个E3强度推断唯一刚性内禀形状的能力。

## Competing Interpretations and Limitations

文章使用“permanent octupole deformation”的作者措辞；其计算同时报告软 PES、宇称恢复和形状混合。实验大 E3 支持八极集体性，单个强度不足以独立选择刚性局域形状或大振幅相关。该预印本 Table I 的实验参考号字面指向[29]，而数值对应 [[bucher-2016-144ba-direct-octupole]]；本任务按数值与独立原文交叉回链，不假定出版版保留此编号。

## Model Dependence

Gogny D1S、轴对称/时间反演/simplex、有限HO空间与有限GCM坐标、密度依赖项的 prescription 均属模型输入。作者明说 particle-number projected density 的影响尚待厘清。没有利用模型最低能来宣称唯一实验解释。

## Knowledge Impact and Learning Decision

`supports` 对称性恢复后的八极集体性计算；`limits` 用平均场梨形图、F图或 v² 单独恢复有符号 E1 振幅；`revises` “E3测到以后即可无模型给静态β3”的过强读法。本源是 [[bucher-2017-146ba-direct-octupole]] 的 Ref24 方法链，不增加一次独立实验。

## Extracted Pages

- [[octupole-deformation]]、[[octupole-correlation]]、[[octupole-mr-amr-evidence-gradient]]。

## Sources

- [[bucher-2016-144ba-direct-octupole]]
- [[bucher-2017-146ba-direct-octupole]]
- [[octupole-mr-amr-evidence-gradient]]

## Review Status

Codex source self-audit；所有新 claim 保留 needs_review，不标为 human-reviewed。
