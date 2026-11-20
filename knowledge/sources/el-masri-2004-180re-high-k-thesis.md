---
type: source
title: "El-Masri 2004 - 180Re high-K bands and isomer spectroscopy"
title_original: "Nuclear Structure of the Doubly Odd 180Re"
aliases: []
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: doctoral-thesis
reading_depth: read
authors: ["Hasna M. El-Masri"]
year: 2004
institution: "University of Surrey"
canonical_source: "University of Surrey doctoral thesis, title page dated 24 May 2004"
raw_file: raw/theses/gpt/query/20261119-international-nuclear-structure/10147838.pdf
raw_sha256: 65a4943406c836ae42fb1f1ec5d2a6dec085bd116e5707b1085f3e396fc29f53
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/theses/gpt/query/20261119-international-nuclear-structure/manifest-user-recheck.json
comparison_manifest_file: raw/papers/gpt/query/20261120-el-masri-180re-crosswalk/manifest.json
comparison_manifest_sha256: dce026198aaf09c07fe722d45a65c9144047a87b66b243af8e8de29ea4d60589
publication_manifest_file: raw/papers/gpt/query/20261120-el-masri-180re-crosswalk/manifest-surrey-text.json
publication_manifest_sha256: edd126ef7fd9a4cc2ee31605d3281f9e457cdf233e81752bde06d3fc22fa1bb9
nuclei: ["180Re"]
tags: ["CAESAR", "K-isomer", "conversion-electrons", "DCO", "blocked-BCS", "thesis"]
---

# El-Masri 2004：¹⁸⁰Re 高 \(K\) 带和异能态谱学

## Bibliographic Record

Hasna M. El-Masri，University of Surrey 博士论文，题页日期 2004-05-24。馆藏 156 页，包含 Surrey 封面及 ProQuest 2017 年复制版说明。对应期刊为 El-Masri 等，Phys. Rev. C **72**, 054306（2005），`10.1103/PhysRevC.72.054306`。对照原件为 Surrey 机构库的 APS 排印本，PDF 23 页含一页机构封面。

## Scope and Reading Depth

核读学位原件 153/156 页的科研与书证范围。正文印刷页码为 PDF 页码减 7。核对三条寿命谱、转换谱、组态与交叉分析，并对照使用同一 CAESAR 采集的期刊分析。

## Summary

以 CAESAR γ 符合、束流相对时间和另行测量的转换电子建立高 \(K\) 带。清楚测得带 9 带头寿命。带 10 连到该异能态，宇称及六准粒子组态仍有条件。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| ELM-RUN | 71 MeV ¹¹B 打 5 mg/cm² 自支撑 ¹⁷⁴Yb，取 \(5n\) 通道。γ–γ 符合使用相隔 1.7 μs 的约 1 ns 束脉冲；μs 衰变与转换谱使用另设时间条件。DCO 示例按 145°/97°及门跃迁多极性给参照值。 | acquisition-and-geometry | direct-original-pages | 学位 PDF 44–52，§§3.3–3.6 |
| ELM-TAU | 3471.3 keV 态的延迟时间谱汇总 261、264、286、457、678 keV 门，指数拟合给 \(\tau=13(1)\,\mu\mathrm{s}\)。图 4.11 有硬件抑制后保留的 prompt 尖峰。 | observed-timing | direct-original-pages | 学位 PDF 82、84、86，§4.4，图 4.11 |
| ELM-NS | 符合时间谱给 284.4 keV 态 \(\tau=109(2)\) ns，1566.3 keV 态 \(\tau=107(2)\) ns。与早期半衰期作比较须先换算。 | observed-timing | direct-original-pages | 学位 PDF 76–81，图 4.8–4.9；Surrey 期刊 PDF 13、15，图 5、8 |
| ELM-21 | 456.8 keV 退激线的 K 转换系数为 0.0084(10)，电子谱先解叠近邻 Ta 线，作者据此选 E1。带 9 的 \(K^\pi=21^-\) 组态候选结合能量、对齐量和 \(\lvert g_K-g_R\rvert/Q_0\) 比较。 | measured-and-assigned | direct-original-pages | 学位 PDF 82–89、108–109，表 4.2、5.6，图 4.14 |
| ELM-22 | 带 10 以 424.0 keV 线馈入 3471.3 keV 态。该线的转换系数未提取，\(K^\pi=(22^+)\) 为暂定。摘要与表 5.6 给第三中子 \(\nu7/2^+[633]\)，PDF 110 正文写 \(\nu5/2^-[512]\)。取最大投影之和并乘各轨道宇称，表中组态给 \(22^+\)，正文所列六轨道给 \(21^-\)。 | alternative-assignment-and-internal-discrepancy | direct-original-pages-and-arithmetic | 学位 PDF 6、84、90、108–111，图 4.15、5.9，表 5.6–5.7 |
| ELM-PRC | 期刊 §III.C.2 的候选 \(22^+\) 组态使用 \(\nu7/2^+[633]\)，与学位表 5.6 一致。作者根据 424 keV 线未见明显延迟等迹象暂取偶极性。期刊 \(21^-\) 态的 456.8 keV E1 支路列 \(\nu=4\)、\(f_\nu=31.5(19)\)；学位表 6.4 的 457.2 keV 条目给 28，两套值按版本保留。 | version-comparison-and-conditional-assignment | direct-original-pages | 学位 PDF 109–110、143；Surrey 期刊 PDF 17、21，图 13，表 VI |
| ELM-MIX | 学位以带间和带内支路估计相互作用，并假设两组态使用同一 \(Q_0\)。带 2、3 相互作用的示例中一项平均为 \(7.3(4)\) keV；作者也用 8 keV 检查去混合后的对齐量。 | model-dependent-inference | direct-original-pages | 学位 PDF 117–125，§6.3，表 6.2，图 6.5–6.8 |

## Competing Interpretations and Limitations

- Fermi aligned 机制来自转动对齐量与模型比较。随频率变化的轨道对齐、PES 形变和近 yrast 态密度皆影响解读。阻碍因子须用分支对应的部分半衰期、转换订正和多极性。见学位 PDF 126–149，§§6.4–6.7。
- 2003 年 NPA 和 PRL 的候选引文对应 Os 核，直接对照为 PRC 72.054306。学位与这篇期刊共享 ¹⁷⁴Yb(¹¹B,5n) 反应、主要 γ 符合及转换电子证据。三条时间谱同源，各版本的门、结果可相互追溯。

## Extracted Pages

- 学位 PDF 1–4、6–7、10–42：身份、目录、背景及 Nilsson、配对、旋转和电磁退激理论。PDF 5、8–9 的献辞和致谢不计。
- 学位 PDF 43–90：实验、门、能级表、转换系数和时间谱。目视确认 PDF 48、51、86。
- 学位 PDF 91–156：准粒子、带交叉、PES、对齐、\(K\) 阻碍、总结及书证。目视确认 PDF 109–110 的原文差异。
- Surrey 的期刊原件用作证据定位和版本比较。逐事件重放、全模型复算与期刊整源计数均未纳入。
