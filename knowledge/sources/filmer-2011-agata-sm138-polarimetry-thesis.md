---
type: source
title: "Filmer 2011 - AGATA commissioning data and 138Sm Compton polarimetry"
title_original: "Methodology development for the analysis of AGATA data"
aliases: []
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: doctoral-thesis
reading_depth: read
authors: ["Fay Eleanor Elizabeth Filmer"]
year: 2011
institution: "University of Liverpool"
doi: "10.17638/00008353"
canonical_source: "University of Liverpool doctoral thesis, December 2011"
raw_file: raw/theses/gpt/query/20261119-international-nuclear-structure/W594465998.pdf
raw_sha256: 096fc82973057ae9e8f33671e8d15a2691eff42d0706c687b51132f37b2c5f85
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/theses/gpt/query/20261119-international-nuclear-structure/manifest-acquisition-batch1.json
nuclei: ["138Sm"]
tags: ["AGATA", "pulse-shape-analysis", "Compton-polarimetry", "thesis"]
---

# Filmer 2011：AGATA 数据重放与 ¹³⁸Sm 康普顿偏振

## Bibliographic Record

Fay Eleanor Elizabeth Filmer，利物浦大学博士论文，2011 年 12 月，原件 150 页。正文和附录印刷页为 PDF 页减 20。

## Scope and Reading Depth

已核 146/150 页，包括装置原理、NARVAL 配置、跟踪选择、跃迁和算例附录。PDF 2–4 为献词、题词和致谢，PDF 135 为附录分隔页。书中的实际运行版本和原事件未重放。

## Summary

以 135 MeV ³²S 打 ¹¹⁰Pd，选用 80° 的一组三晶体分析 ¹³⁸Sm γ 射线。NARVAL 重放链依次提供数据解析、预处理、脉冲形状分析和跟踪输出，所用的偏振统计量基于恰好两个可解析相互作用点。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| FIL-RUN | ¹³⁸Sm 反冲速度以 346 keV 峰的 Doppler 校正后能量分辨率得到 \(v/c=2.30(1)\%\)。分析使用第二组三晶体 A003/B003/C005。两击计数在图 4.15 附近有 24,000 与 240,000 的文字差异，图轴乘 \(10^3\)，两击柱约 240,000，与正文相合。 | commissioning-geometry-and-count-audit | direct-original-visual | PDF 65–70、79–80，图 4.4、4.15 |
| FIL-Q | 表 D.2 的 \(Q\) 数列由所选峰的代表位置角和能量量计算。139.7、346.9、406.0、1287.0 keV 分别报 5.0(3)%、34.5(9)%、40.1(8)%、16.4(1)%。346.9 keV 的 \(F=\epsilon Q^2\) 由 \(\epsilon=0.326\)、\(Q=0.345\) 得 0.0388，与报告的 3.9% 相合。这里 \(\epsilon\) 的分母是该光峰的总计数。 | reduced-response-and-denominator | direct-original-pages-and-arithmetic | PDF 84、88–89、99–103、130–134，表 D.2 |
| FIL-A | 346.9 keV 表 E.1 给 \(N_\perp=775(28)\)、\(N_\parallel=557(23)\)、\(a=1.10(1)\)。式 E.3 的共同因子约掉后得 \(A=0.1637\)，正文式 4.11 给 \(A=0.2096\)。若式 4.10 的无偏振比确为 \(N_\perp/N_\parallel\)，对式 4.11 应先取倒数才保持同样本零点。原文仍报 \(A=0.18(3),P=0.51(9)\)，待原事件和程序确认计算口径。 | literal-formula-consistency-check | direct-original-visual-and-arithmetic | PDF 88、94、125、143–145，式 4.10–4.12、E.3–E.4、表 E.1 |
| FIL-ANGLES | 附录以 126°、345.9 和 191.5 keV 代入式 E.2 报 \(Q=34.7(9)\%\)。印刷中间数 \(0.55+1.80\) 给约 38.6%。Klein–Nishina 的 \(\sin^2\) 因子应使用光子运动方向之间的极散射角。正文式 4.9 与附录又把所用角记为方位角 \(\phi\)，实际角定义及逐事件加权需另核。 | angle-and-arithmetic-consistency-check | direct-original-visual-and-arithmetic | PDF 32–35、81–85、138–140，式 4.5、4.9、E.2 |

## Competing Interpretations and Limitations

- 无偏振 ¹³³Ba 最上能量 383.9 keV，本实验把校正延用到约 1.3 MeV。角接受、相互作用排序、同段多击的质心合并和交叉串扰都可能影响响应。原文指出部分不对称度符号不符合预期，不据弱线的符号单独作多极性指认。PDF 94–110。
- [[bizzeti-2015-agata-triple-cluster-polarimetry]] 用另一套 Pd 库仑激发和 Cs 参考数据来确定分析能力。两项使用的参考、角门、效率分母和响应定义均需随源保留。Filmer 能谱给出 \(P\)、计数和已知多极性资料，这些跃迁未报告配对 DCO/ADO 比值及联合 \(\delta\) 提取。PDF 60–110、124–134。

## Extracted Pages

- PDF 1、5–44：书证、导航、康普顿截面、调制与偏振计。
- PDF 45–110：AGATA 晶体、PSA、数据流、刻度、偏振分析、结果和限制。
- PDF 111–134、136–150：¹³⁸Sm 谱系、配置和事件流、计数和 \(Q\) 数据表、算例和参考文献。
