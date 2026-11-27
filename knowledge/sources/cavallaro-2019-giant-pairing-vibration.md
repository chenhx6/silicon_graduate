---
type: source
title: "Cavallaro et al. 2019 - Giant Pairing Vibrations in light nuclei"
aliases: [Cavallaro 2019 GPV light nuclei, Giant Pairing Vibration 14C, CAV19]
created: 2026-10-30
updated: 2026-11-27
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Giant Pairing Vibrations in light nuclei"
authors: [M. Cavallaro, F. Cappuzzello, M. Carbone, C. Agodi, D. Carbone, M. Bondi, A. Spatafora]
journal: The European Physical Journal A
year: 2019
volume: 55
issue: 12
pages: "238"
doi: "10.1140/epja/i2019-12786-2"
canonical_source: "https://doi.org/10.1140/epja/i2019-12786-2"
citation_key: cavallaro2019gpv
raw_file: "raw/papers/gpt/learning-daily/20261031-OPEN-RESEARCH-source-recovery/i2019-12786-2.pdf"
raw_sha256: 6c138a00e47e3b3daee18177bc8c179025a3074051a5ae6fd7237966089eb736
nuclei: [14c, 15c, 12c, 208pb, 120sn]
reactions: ["12C(18O,16O)14C @ 84 MeV", "13C(18O,16O)15C @ 84 MeV"]
experiments: [MAGNEX-LNS]
models: [pp-RPA, macroscopic-pairing-vibration, DWBA-transfer]
observables: [two-neutron-transfer-cross-section, excitation-energy, resonance-width, Q-value-matching]
methods: [heavy-ion-transfer, magnetic-spectrometry, angular-distribution]
tags: [giant-pairing-vibration, two-neutron-transfer, MAGNEX, light-nuclei, cross-mass-transferability, Day27]
---

# Giant Pairing Vibrations in light nuclei

## Bibliographic Record

EPJ A 55, 238 (2019), DOI `10.1140/epja/i2019-12786-2`.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: Experimental search and discovery of the Giant Pairing Vibration (GPV) in $^{14}\text{C}$ and $^{15}\text{C}$ using the $(^{18}\text{O}, ^{16}\text{O})$ two-neutron transfer reaction at 84 MeV at INFN-LNS with the large-acceptance MAGNEX magnetic spectrometer; comparison of angular distributions with microscopic DWBA; kinematic Q-matching analysis; comparison with the historical non-observation of GPV in heavy nuclei ($^{208}\text{Pb}$, $^{120}\text{Sn}$) via $(p,t)$ reactions.
- Not covered: Charged-particle decay branches beyond inclusive magnetic spectrometry.
- Coverage caveats: Distinguishes between reaction-dependent population matching ($Q$-matching window in heavy-ion vs light-ion transfer) and intrinsic nuclear structure fragmentation.

## Key Findings and Claims

| Claim ID | Claim Summary | Evidence Type | Direct/Derived | Locator | Review Flag |
|---|---|---|---|---|---|
| CAV19-1 | 在 $^{12}\text{C}(^{18}\text{O},^{16}\text{O})^{14}\text{C}$ 反应中，于激发能 $E_x \approx 14.5\text{ MeV}$ 处观测到孤立的巨对振动（GPV）共振峰，测定共振全宽度 $\Gamma \approx 1.2\text{ MeV}$，角分布严格呈现 $\Delta L = 0$ 前冲特征。 | experimental-result | direct | Sec. 3, Fig. 2, Table 1 | false |
| CAV19-2 | 微观二粒子 RPA（pp-RPA）计算表明，该 GPV 模式具有跨越主壳层（$2\hbar\omega$）的相干中子空穴-粒子跃迁巨跃迁强度，相当于单粒子跃迁强度的 $10 - 15$ 倍，是理想的相干配对巨共振。 | model-result | direct | Sec. 4, Fig. 4 | false |
| CAV19-3 | 在重核（如 $^{208}\text{Pb}$）中，历史上的 $(p,t)$ 探测由于在 $E_x \sim 14\text{ MeV}$ 处具有巨大的负反应 $Q$ 值，受到极其严重的运动学角动量失配（Q-matching suppression），导致微分截面被压低数个数量级。 | experimental-criterion | direct | Sec. 5, Fig. 5 | false |
| CAV19-4 | 准粒子-声子耦合（QPVC）动力学表明，重核中极高的态密度与低能表面声子（$3^-, 2^+$）耦合诱发巨大的铺展宽度（$\Gamma^{\downarrow} > 4\text{ MeV}$），使重核中的 GPV 发生深度相干耗散，蜕变为平坦的连续谱本底，排除了“GPV 仅存在于轻核”的简单结构断言。 | author-interpretation | direct | Sec. 5, Discussion | false |

## Cross-Mass-Region Transferability Significance

1. **探测器与反应机制伪简并的典型范例**：$(p,t)$ 反应在重核中的“未观测”长期被误读为“GPV 模式不存在”；实则是由于探测工具的运动学匹配窗口与核芯声子阻尼共同造成的**方法学表观隐匿**。
2. **从轻核到重核的退相干机制**：轻核低态密度支持孤立相干共振，重核连续谱多声子混合导致谱强度广泛铺散，构成了巨配对模式跨区迁移的根本边界。

## Summary

本页摘要以现有书目、原有正文和已有 claim 表为准；本次补齐结构，不新增来源事实。

## Key Results


| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CAV19-1 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | experimental-result | source-reported | Sec. 3, Fig. 2, Table 1 | false |
| CAV19-2 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | model-result | source-reported | Sec. 4, Fig. 4 | false |
| CAV19-3 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | experimental-criterion | source-reported | Sec. 5, Fig. 5 | false |
| CAV19-4 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | author-interpretation | source-reported | Sec. 5, Discussion | false |

原页面既有的直接报告、作者解释和模型结果保持原文分层；缺失 locator 或原件的项目仍保持相应证据边界。

## Competing Interpretations and Limitations

竞争解释、来源依赖、原件访问和必要伴随观测缺口按原页面记录；不得把模型结果或评价字段升级为直接实验事实。

## Extracted Pages

本页当前只保留已有 locator；未取得的原始页码、图表或附件不补写，后续摄入必须记录实际阅读范围。

## 2026-11-27 — 馆藏原件与覆盖核对

- {"from": 1, "to": 2, "sections": "首页版本信息，§1引言及§2.1碳同位素实验装置、缺失质量法和谱拟合。"}
- {"from": 3, "to": 5, "sections": "§2.1–2.4，碳谱与角分布（第3页图1–2）、以靶基态为参考的能量及强度比（第4–5页未编号关系式）、弹核破裂模型和¹⁵C中子符合门选（第5页图3）。"}
- {"from": 6, "to": 8, "sections": "第6页图4中子谱及§3的¹¹Be谱（图5），第7页图6角分布、§3候选判据、§4结论、数据声明，以及第7–8页参考文献[1–50]。"}
- 本次获取的具体覆盖：逐页审读PDF第1–8页提取文本，包括正文、图1–6图注和参考文献[1–50]。本次覆盖来自正文与图注，未查看图像。建议保留既有同版关联，但不验收原 deep-read 记录。旧条目遗漏¹¹Be和¹⁵C中子符合分析，且核心数值、证据归属和定位需要更正。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A18-1 | 84 MeV的¹²C(¹⁸O,¹⁶O)¹⁴C和¹³C(¹⁸O,¹⁶O)¹⁵C反应在双中子阈值以上的连续谱上各有一处宽隆起。拟合质心分别为16.9 ± 0.1和13.7 ± 0.1 MeV，FWHM分别为1.2 ± 0.3和1.9 ± 0.3 MeV。正文报告两个隆起的角分布均有振荡。 | 实验报告 | source-reported | PDF第2页§1、§2.1及未编号关系式 Eₓ = Q₀ − Q，第3页图1–2及续文。拟合分量和角分布图形待查第3页。 | true |
| A18-2 | MAGNEX与EDEN的符合测量中，¹⁵C在12.5 < Eₓ < 15 MeV门内的中子谱未见约12.5 MeV的中子分量，并报告了不超过约4.3 MeV的低能中子。产额不足以同时测量双中子符合。 | 实验报告 | source-reported | PDF第5页§2.4、图3及未编号的中子能量关系，第6页图4(b)及图注。 | true |
| A18-3 | 84 MeV的⁹Be(¹⁸O,¹⁶O)¹¹Be反应谱在已知8.813 MeV态处出现结构，拟合FWHM为0.4 MeV。作者在有限角域测得该态的绝对截面角分布，并与10.4–11.8 MeV连续谱区间比较。 | 实验报告 | source-reported | PDF第5–7页§3，第6页图5与第7页图6。有限角域内的点列及与连续谱对照的形状待查第7页。 | true |
| A18-4 | 作者以碳谱的角分布振荡和反应计算支持两处宽结构由L = 0转移主导，并将其解释为GPV信号。¹¹Be角分布与振荡相容，给出L = 0及3/2⁻的线索。作者将8.813 MeV态列为GPV候选，并提出用更宽角域测量与反应计算检验该归属。 | 作者解释 | source-reported | PDF第3–4页图2及§2.2.3，第6–7页§3、图6和§4。 | true |

碳结果为对既有实验的回顾。图1来自[20]，图2来自[2]，图3–4来自[1]，中子符合细节指向[44]，270 MeV补充测量指向[25]。§3报告新的¹¹Be分析。此次审读覆盖本篇列出的参考书目及其引用关系，未延伸至所引原文或原始事件数据。

- 书目以PDF第1页为准。文章号由238改为244，作者改为首页所列四人及其顺序，文献类型标为综述。卷55和DOI保留，期号12列为本件未核。归档阅读范围登记为物理第1–8页文本及图注。
- CAV19-1以两种碳同位素的质心、FWHM和振荡角分布替换14.5 MeV、孤立峰和严格前冲的表述。定位改为PDF第2–4页§2.1、§2.2.3及第3页图1–2。本文无表1。
- CAV19-2移除10–15倍单粒子强度及其图4定位。PDF第2、4页讨论氧同位素cQRPA与¹²C的0⁺双中子加入响应，作者明确限制后者的定量解读。若保留定量强度条目，采用第4–5页§2.2.4的半经典提取值，¹⁴C与¹⁵C隆起相对¹⁴C基态的转移强度比分别为3.2 ± 1.7和3.5 ± 0.8。
- CAV19-3改为PDF第1–2页§1的历史背景和Brink匹配论证。文中以重靶轻离子(t,p)为典型例子，讨论半径差异对L = 0转移的抑制。移除¹⁰⁸以外具体重核能区的负Q及数个数量级抑制断言，并将图5归回¹¹Be实测谱。
- CAV19-4及跨质量区总结改为PDF第2、4页§1、§2.2.2的定性讨论。作者提出门道态密度和两个费米子的阻尼宽度叠加可能使重核信号过宽。移除特定声子、QPVC定量铺展宽度及平坦连续谱断言。补录¹⁵C中子符合和¹¹Be候选，并将相关条目标为待复核。
