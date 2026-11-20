---
type: source
title: "Cubiss 2017 - At isotope shifts and isomer-selective 178Au decay"
title_original: "In-source laser spectroscopy of At isotopes and decay studies of 178Au"
aliases: []
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: doctoral-thesis
reading_depth: read
authors: ["James Gerald Cubiss"]
year: 2017
institution: "University of York"
canonical_source: "University of York doctoral dissertation, May 2017"
raw_file: raw/theses/gpt/query/20261119-international-nuclear-structure/W2768051990.pdf
raw_sha256: 2c1ea7982575d75c923241f6d4b4df9cee2e43da2e9d4c1de3f5c9f7a791fa8c
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/theses/gpt/query/20261119-international-nuclear-structure/manifest-acquisition-batch1.json
comparison_manifest_file: raw/papers/gpt/query/20261120-cubiss-at-au-crosswalk/manifest.json
comparison_manifest_sha256: 0c7c346870ae85228c46cf4c3ab36f9765d6adee3f16ec4f812334e27c4f4ebf
nuclei: ["178Au", "174Ir", "195At", "197At", "199At", "217At", "218At", "219At"]
tags: ["ISOLDE", "RILIS", "decay-tagging", "hyperfine-structure", "charge-radii", "octupole", "thesis"]
---

# Cubiss 2017：At 激光谱和 ¹⁷⁸Au 异能态选择性衰变

## Bibliographic Record

James Gerald Cubiss，University of York 博士论文，2017 年 5 月，PDF 130 页。期刊对照为 Cubiss 等，Phys. Rev. C **97**, 054327（2018），`10.1103/PhysRevC.97.054327`；Barzakh 等，Phys. Rev. C **99**, 054317（2019），`10.1103/PhysRevC.99.054317`；Cubiss 等，Phys. Rev. C **102**, 044332（2020，2021-10-14 更正版本），`10.1103/PhysRevC.102.044332`。三篇 APS 原件与获取路径见本页的 `comparison_manifest_file`。

## Scope and Reading Depth

覆盖学位原件 128/130 页的科研与书证范围。背景章节按问题和方法核读，核心谱图、表格、拟合与期刊对应关系逐项核对。PDF 页与印刷页在正文相同。卷首致谢 PDF 11–12 不计。

## Summary

ISOLDE 的离子源内共振电离用频率步进分辨超精细谱。衰变能量门提供态选择，飞行时间质谱提供质量与低产额离子辨识。¹⁷⁸Au 的 α–γ 符合需要区分部分能量求和与真实支路。At 的频移需经原子质量位移和场位移因子转换为均方电荷半径差。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| CUB-TAG | 2014 年 9 月 At 与 2015 年 5 月 Au 使用 IS534 的不同运行。窄带激光步进，Windmill 按 α 或 γ 能量门累计各步的计数。¹⁹⁹ᵐAt 的 α 分支约 1%，改用 103–141 keV 级联中可见的 141 keV 线，核对关激光与两侧本底门。 | measurement-chain | direct-original-pages | 学位 PDF 49–60、96–100，图 4.5、4.7、6.4–6.5 |
| CUB-AU | 先由两组 HFS 查出两态，再选相应激光频率测衰变。学位 §5.1 报激发能 188(14) keV，图 5.8 亦给 188(14) keV；期刊表 I 给 189(14) keV，依据纯束的 ToF-ICR 与 ¹³³Cs⁺ 参考。学位的基态/异能态半衰期分别为 3.4(5) s、2.7(5) s，α 分支 16(1)%、18(1)%。分支估计依赖 ¹⁷⁸Pt 的已知 α 分支和关激光对照。 | measured-versioned-values | direct-original-pages | 学位 PDF 61–62、71、81–83，图 5.1、5.8、5.16，式 5.4；PRC 102 PDF 3–4、6–7，表 I |
| CUB-GATE | ¹⁷⁸Pt 的 5291–158.6 keV 组用于设 \(20<\Delta t<230\) ns 的 α–γ 门。该门内仍有强 170 keV 线的随机符合。弱 98.2 keV 线存在先后相反的两种级联放置：缺失的 17.8 keV 可以在它之后或之前。5753–116 keV 门仅有一候选计数，学位偏向第二种并保留第一种。 | gating-and-alternative-placements | direct-original-pages | 学位 PDF 64、67–72，图 5.4、5.6–5.9，表 5.1 |
| CUB-SUM | 5925 keV α 与 56.8 keV 强转换跃迁的电子或 X 射线在 Si 中求和，向 5977 keV 区送计数。论文对单谱拟合和 GEANT4 响应做比较后才估计真正 5977 keV 支路。不能把原始峰区总数直接当分支强度。 | response-correction | direct-original-pages | 学位 PDF 76–81，图 5.11–5.14；PRC 102 PDF 5–6，§III.C |
| CUB-IR | 5521–472.1 和 5571–421.4 keV α–γ 组均给总 \(Q_\alpha=6120(10)\) keV。学位报告 JYFL JR121 各约 40 个符合事件，支持这两组；未再见 5521–421.4 keV。低 α 阻碍可与相似或混合组态相容，期刊也保留同一转动带成员的解释。 | coincidence-and-competing-structure | direct-original-pages | 学位 PDF 72–76、84–89，表 5.2、5.4–5.6；PRC 102 PDF 6–7、10，图 6–7、§IV.B |
| CUB-HFS | ¹⁹⁷At 的两套 HFS 处理给出 1698(113) 和 1868(106) MHz 的异能位移。学位采用考虑谱线强度非统计效应的 Seliverstov–Barzakh 处理。两值共用谱，比较拟合策略时须保留这种依赖。 | shared-spectrum-model-comparison | direct-original-pages | 学位 PDF 99–102，表 6.2，图 6.6 |
| CUB-LIGHT | 2018 年终稿用 216、795 nm 两线作 King 图，分别报告同位素位移、转换后的半径差和电磁矩，并保留原子因子系统误差。¹⁹⁷,¹⁹⁹At 的 \(9/2^-\) 与 \(1/2^+\) 半径差为形状共存解释提供约束。其 ¹⁹⁹ᵐAt 还引用先前工作约束拟合，不能把整表视作源于一条 141 keV 门。 | analysis-and-interpretation | direct-original-pages | 学位 PDF 99–106、110–114；PRC 97 PDF 1、5–10，表 I–II，图 4–7 |
| CUB-HEAVY | 2019 年终稿对 ²¹⁸At 的 \(2^-\) 和 \(3^-\) 候选分别给奇偶交错指标 \(\gamma=1.45(11)\) 和 1.29(11)，阈值为 1。学位 PDF 109 的 1.45(9) 须与期刊值分版本保留。反常交错与八极关联相容，定量幅度依赖自旋和 HFS 拟合。 | hypothesis-conditional-observable | direct-original-pages | 学位 PDF 107–109、115–116，图 6.10、表 6.6；PRC 99 PDF 3–4、7，图 1、4，表 I |

## Competing Interpretations and Limitations

- 论文 ¹⁷⁸Au 与学位第五章共享 ISOLDE 的核心衰变数据。JYFL 独立复查的覆盖对象是指定 α–γ 组。α 阻碍因子比较还依赖选定的参考分支及角动量假设。学位讨论 421.4/472.1 keV 的可能 E0 分量，同时检验转换、电子求和与计数局限；本案没有可用于直接确认形状共存的 \(E0\) 强度（学位 PDF 84–86；PRC 102 PDF 6、10）。
- 原始观测是频率与计数，均方半径与磁矩在其后提取。半径转换保留共同的原子因子误差。形变大小还依赖液滴模型参照，核电荷半径单独不能决定形变的符号或唯一势能面。重端的八极解释应并列 ²¹⁸At 自旋未定、磁矩加和不闭合与四极/八极模型条件。

## Extracted Pages

- 学位 PDF 1–10、13–48：身份、目录、引言、核结构解读和激光谱原理。重点为式 3.3–3.6 的质量/场位移分解和 §3.2 的 HFS 参数。
- 学位 PDF 49–91：IS534 装置、能量与效率标定、时间窗、α–γ 组、支路/半衰期和竞争指认。已目视核图 5.8、5.14。
- 学位 PDF 92–130：At 标签和 HFS 强度处理、半径差及磁矩、结论和参考文献。已目视核图 6.4、6.6、6.10。保留 §7.1 原文的后续测量建议及其 2017 年时点。
- 三篇期刊原件作定位对照，学习计数只给学位论文；事件级数据、拟合协方差和 JR121 原运行资料未获得。
