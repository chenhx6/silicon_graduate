---
type: source
title: "Stefanescu 2004 - 69As and 69Se with EUROBALL"
title_original: "Investigation of the nuclear structure of 69As and 69Se with the EUROBALL spectrometer"
aliases: []
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: doctoral-thesis
reading_depth: read
authors: ["Irina Stefania Stefanescu"]
year: 2004
institution: "Universität zu Köln"
canonical_source: "Universität zu Köln doctoral dissertation, 2004"
raw_file: raw/theses/gpt/query/20261119-international-nuclear-structure/irina_thesis.pdf
raw_sha256: c05751ed11dc0448f42d764f3c41d87c6a6be4f906aa06736ede21c8145105e8
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/theses/gpt/query/20261119-international-nuclear-structure/manifest-user-recheck.json
comparison_manifest_file: raw/papers/gpt/query/20261120-stefanescu-a69-crosswalk/manifest.json
comparison_manifest_sha256: d0c2f14fb15ff6c489f225a4b86de764a3237728a803fee5374f85c88e9d0d3d
nuclei: ["69Se", "69As"]
tags: ["EUROBALL", "angular-distribution", "DCO", "alignment", "shape-coexistence", "band-termination", "thesis"]
---

# Stefanescu 2004：EUROBALL 的 ⁶⁹Se 与 ⁶⁹As

## Bibliographic Record

Irina Stefania Stefanescu，Universität zu Köln 博士论文，2004 年，139 页。对应论文为 *Level structure of 69Se*（`10.1103/PhysRevC.69.034333`）和 *High-spin states and band terminations in As69*（`10.1103/PhysRevC.70.044304`）。已留档登记信息与摘要，反应、束能及阵列对应学位采集。APS 全文入口返回 401，其他尝试只得到摘要、目录或访问拦截页。逐表改动仍待期刊全文核对。

## Scope and Reading Depth

学位原件覆盖 136/139 页科研及书证范围。PDF 3、42、58 为无正文或分隔页。正文印刷页等于 PDF 页。内嵌字形映射损坏，按 PDF 页渲染并 OCR，关键数值、上下标与图表回到原页核实。

## Summary

用 EUROBALL IV、Neutron Wall 与 EUCLIDES 在 95/105 MeV 两次 ³²S + ⁴⁰Ca 运行中分辨 \(2pn\) 的 ⁶⁹Se 与 \(3p\) 的 ⁶⁹As。角分布提供部分混合比，DCO 和级联关系约束自旋。低自旋用刚性三轴转子加粒子模型比较，高自旋用 CNS 讨论组态、交叉、形状演化和终止。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| STE-GATE | 95 MeV 的主触发要求至少 2 Ge 与一项 Wall 事例，105 MeV 有 2 Ge + 中子和 3 Ge + 一项 Wall 事例两路。离线用 TOF–Z/C 与 \(\Delta E-E\) 门择中子和带电粒子，再建 \(n\gamma\gamma\)、\(3p\gamma\gamma\) 等矩阵及立方体。两束能与门选择的可见性、邻道污染须保留。 | acquisition-and-selection | direct-original-pages | 学位 PDF 11–13、20–21、25–33，图 2.7、2.8、2.14–2.18 |
| STE-ALIGN | 105 MeV 的 ⁶⁹Se 单 γ 角分布先以强拉伸 E2 线和 CHIPLO-2 标定 \(\sigma/J_i=0.35\pm0.05\)，随后将此值作为最终角分布分析的共同参考。属于先独立校准再沿用共同取向值的实例。对单条 \(\delta\) 是否传播这项取向误差，原文此处仅说明沿用参考值。 | reported-alignment-calibration | direct-original-pages | 学位 PDF 34–38，表 2.2–2.3，图 2.19 |
| STE-ROOT | ⁶⁹Se 403.1 keV 的角分布给 \(\delta=0.16(5)\)。773.3 keV 给 \(2.30(39)\) 与 \(0.57^{+0.10}_{-0.07}\)，相应约化 \(\chi^2\) 为 0.867、1.245。675.9 keV 给 \(2.52^{+0.55}_{-0.44}\) 与 \(0.57^{+0.10}_{-0.08}\)。保留两个极小值，选支叙述须和 675.9 keV 门、714.2 keV 门及所用自旋假设一起读。 | multiple-solutions | direct-original-pages | 学位 PDF 37–38、44–45，表 2.3、图 2.19；PDF 121–122，表 A.1 |
| STE-DCO | 粒子门统计有限时合并后角组和近 90° 角组，代表角 155°/90°。表 A.1 的 403.1 keV 在 675.9 keV 门下为 \(R_{\rm DCO}=0.53(10)\)，773.3 keV 在 714.2 keV 门下为 1.08(11)。675.9 keV 本身有两种 \(\delta\) 解。 | gated-correlation | direct-original-pages | 学位 PDF 39–40，式 2.15；PDF 44–45、121–122 |
| STE-BR | 对 773.3 keV 光子线，两根对应 E2 分数约 84.1% 和 24.5%。按式 4.14 固定同母态 662.3 keV 参照及表 4.5 的中心 BR，换根得到 \(B(M1)/B(E2)\) 约 0.27 与 1.26 \((\mu_N/eb)^2\)。原表采用大根给 0.25(9)，小根结果为条件算术。403.1 keV 的同母态 E2 参照为 1079.1 keV。 | conditional-root-sensitivity | direct-original-pages-and-arithmetic | 学位 PDF 73、75–76、122，表 4.5、式 4.13–4.14 |
| STE-MODELS | ⁶⁹Se 的 RTRP 表 4.3 用 \(\epsilon_2=0.33,\gamma=-36^\circ\) 比较 yrast 低旋，结论 PDF 118 则写 \(-33^\circ\)。同组参数对 yrare 结果有偏差。⁶⁹As 的 \(15/2^+,17/2^+\) 近邻态和更高旋态分别偏好不同 \(\gamma\) 区间。CNS 的 [1,2]、[2,3] 比较是组态与终止候选，保留与最高观测自旋的差值。 | model-assumptions-and-positive-evidence | direct-original-pages | 学位 PDF 66–80、100–103、114–120，表 4.3、4.7、图 4.4–4.10 |

## Competing Interpretations and Limitations

- 773.3 keV 的 DCO 近四极参照，作者并用馈入线和邻核系统学支持 \(13/2^+\) 与较大混合；DCO 单独不足以区分拉伸四极与大 E2/M1 混合。403.1 与 773.3 keV 的初态分别为 1653.7 与 2023.8 keV，二者共享 \(13/2^+\) 标记但对应不同能级。
- 学位实验表给了角分布系数、DCO、\(\delta\) 和门能量。§2.4.2 为极化原理，PDF 49 的极化佐证引用 Ge 邻核。未定位本次 ⁶⁹Se 两线的线偏振 \(P\)。因此本案可用于比较取向处理和多解，P–角量联合样本仍缺 \(P\)。
- 附录 A.3 记录 RTRP 与 CNS 计算流程。刚性转子是低旋比较；CNS 的固定占据与配对处理限制了跨交叉区的统一描述。本次没有绝对寿命或模型重算，也未把标注的模型极小作为直接形变观测。

## Extracted Pages

- 学位 PDF 1–2、4–41：题页、两种语言摘要、装置与方法。关键数值目视 PDF 37–38、40。
- 学位 PDF 43–57、59–120：两核谱图、带演化、RTRP/CNS 比较与结论。目视 PDF 46、49、52、73、79、100、102、119。
- 学位 PDF 121–139：逐跃迁表、代码流程、参考文献。目视 PDF 122 的门、能量、强度和 DCO 列。期刊范围为摘要与书目。
