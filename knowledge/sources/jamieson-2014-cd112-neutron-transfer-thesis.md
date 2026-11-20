---
type: source
title: "Jamieson 2014 - 112Cd single-neutron transfer and negative-parity states"
title_original: "The nuclear structure of 112Cd studied through the 111Cd(d,p)112Cd single neutron transfer reaction"
aliases: []
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: masters-thesis
reading_depth: skimmed
authors: ["Andrew Spencer Jamieson"]
year: 2014
institution: "University of Guelph"
url: "https://hdl.handle.net/10214/7791"
canonical_source: "University of Guelph MSc thesis, title page January 2014"
raw_file: raw/theses/gpt/query/20261119-international-nuclear-structure/W2607914770.pdf
raw_sha256: 79ebd6d80dee3a3a37ecad57eacf400a925396e35e2aba39d5f1c87f3d11c352
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/papers/gpt/query/20261120-jamieson-cd112-crosswalk/manifest.json
nuclei: ["111Cd", "112Cd"]
tags: [neutron-transfer, quadrupole-octupole-coupling, DWBA, ADWA, thesis]
---

# Jamieson 2014：¹¹²Cd 的单中子转移与负宇称组态

## Bibliographic Record

Andrew Spencer Jamieson，University of Guelph 物理硕士论文。题页标为 2014 年 1 月，原件 179 页，馆藏标识 `10214/7791`。正文印刷页为 PDF 页减 9。

## Scope and Reading Depth

定向核验转移观测量、模型归一、两条负宇称谱强度及和规则。附录中逐能级的角分布尚待核对。

## Summary

该研究在 Garching MLL 用 22 MeV 极化氘束及 Q3D 测 ¹¹¹Cd(d,p)¹¹²Cd。质子截面角分布、束流翻转的 analyzing power 对转移的 \(\ell\) 和 \(j\) 有不同的灵敏度。在所测试的模型下，2373 keV 的 \(5^-\) 及 2818 keV 的 \(6^-\) 两态有大 \(h_{11/2}\) 转移强度。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| JAM-DATA | 在约 4.2 MeV 内报告 129 个态，其中 49 个此前未报告。角截面配合 \(A_y\) 识别主要 \(\ell,j\)，若有多种自旋耦合仍看已有证据与反应灵敏度。 | experiment-and-assignment | direct-original-pages | PDF 36、65–74、80、108 |
| JAM-5 | 2373.28(3) keV 的 \(5^-\) 在低动量接受段给 \(S_{h_{11/2}}=2.66(3)\)（ADWA）和 \(1.59(19)\)（DWBA）。高动量接受段同一态给 2.63(4)、1.70(2)。 | model-extraction | direct-original-pages | PDF 83、90–91、97，表 4.1–4.2、图 4.2 |
| JAM-6 | 2817.74(6) keV 的 \(6^-\) 在表 4.2 给 \(S_{h_{11/2}}=6.07(7)\)（ADWA）和 \(3.47(4)\)（DWBA）。作者把它和 2373 keV 态联系为 \(s_{1/2}\otimes h_{11/2}\) 两准中子组态。 | model-extraction-and-author-interpretation | direct-original-pages | PDF 78、91、99、109 |
| JAM-SUM | 加入早先 (d,t) 的 0.50，\(h_{11/2}\) 总和从 DWBA 7.6 到 ADWA 12.1，后者接近 \(2j+1=12\)。\(d_{3/2}\) 则为 4.8 与 6.4，ADWA 中心值超 4 约 60%。该比较按轨道和截断范围使用。 | model- and coverage-dependent | direct-original-pages | PDF 105–107，表 4.3–4.4 |

## Competing Interpretations and Limitations

- \(A_y\) 是由极化氘束上下方向的截面差与和得到的粒子反应分析本领，其中 \(P\) 为束流极化。此处没有用于 γ 混合比的线偏振观测。PDF 65–68，式 3.6。
- \(S_{\ell j}\) 按式 1.16–1.17 的约定从测量与单粒子截面之比提取，包含约定的自旋统计因子。这个参数不是组态概率。表 4.1–4.2 的误差含统计和靶厚，另有约 30% 光学势系统不确定度。相同实验的两段动量设置提供交叉核查。PDF 25–27、82、88–91。
- §§4.3.4、4.3.9 文字说 2373 keV 的 \(S\) 与基态相等，2818 keV 的约为两倍。表中基态 \(S\) 为 0.185(2)（ADWA）和 0.189(3)（DWBA），不能直接得这两个比率。若按式 1.17 比较乘 \( (2J_i+1)/(2J_f+1) \) 后的缩放系数，ADWA 比率约 1.31 和 2.52，DWBA 约 0.76 和 1.41。文字摘要与表列原量分别留存。PDF 25、90–91、97、99。
- Garrett 等 `10.1103/PhysRevC.59.2455` 的独立 (n,n′γ) 光谱以通往八极 \(3_1^-\) 的增强 E2 支持四极–八极耦合。转移数据对 \(5^-\) 给强单中子重叠，支持重审纯集体组态。不同算符可对同一混合态给不同选择性。\(B(E2)\) 与转移强度都需保留，¹⁰⁶Cd 的类比还要回到该核本身的衰变与布居证据。见 [[kalaydjieva-2023-cd106-zr100-shape-coexistence-thesis]]。
- Jamieson 等 `10.1103/PhysRevC.90.054312`（2014）聚焦低位负宇称，`10.1103/PhysRevC.98.044309`（2018）覆盖 129 态并比较两反应模型。相同作者、22 MeV 极化氘束、Q3D 及对应能区和数据支持与学位论文归入同一次转移实验。已核三篇 APS 摘要，论文之间的版本细表仍待全文核验。

## Extracted Pages

- PDF 1–2、4–6：学位、摘要与导航。
- 定向页 PDF 25–27、36、65–74、78、80、82–91、97、99、105–110：反应输入输出、转移强度、拟合、组态、和规则和书证入口。
