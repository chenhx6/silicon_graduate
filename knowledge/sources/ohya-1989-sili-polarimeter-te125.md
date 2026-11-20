---
type: source
title: "Ohya et al. 1989 - Si(Li) Compton polarimeter and 125Te"
title_original: "A Compton polarimeter constructed with a large Si(Li) scatterer and two Ge analysers"
aliases: []
created: 2026-11-21
updated: 2026-11-21
status: ai-draft
review_status: unreviewed
source_type: journal-article
reading_depth: read
authors: ["S. Ohya", "H. Miura", "K. Nishimura", "N. Mutsuro", "T. Aoki"]
year: 1989
doi: "10.1016/0168-9002(89)90636-0"
canonical_source: "Nuclear Instruments and Methods in Physics Research A 276 (1989), 223-227, published edition"
raw_file: raw/papers/gpt/query/20261119-polarization-delta-collection/10.1016_0168-9002_89_90636-0.pdf
raw_sha256: 0c5ab7bf5918acf969ffeddfdc8e134fdad2f049e97bb220ff19aa963cc813af
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/papers/gpt/query/20261119-polarization-delta-collection/manifest.json
nuclei: ["125Sb", "125Te"]
tags: ["linear-polarization", "Compton-polarimeter", "nuclear-orientation", "mixing-ratio"]
---

# Ohya 等 1989：Si(Li) 散射体与 ¹²⁵Te 的 176 keV 极化

## Bibliographic Record

S. Ohya、H. Miura、K. Nishimura、N. Mutsuro、T. Aoki，*Nuclear Instruments and Methods in Physics Research A* **276**, 223–227（1989）。PDF 1–5 对应印刷 223–227 页。

## Scope and Reading Depth

五页完整核读。核对 Monte Carlo 材料比较、低温源标定、原始角量与偏振、图 6 和两组混合比。

## Summary

用叠片 Si(Li) 散射体和两只 Ge 分析器测低能 γ 极化。¹²⁵Sb 低温取向源衰变到 ¹²⁵Te，作者用两个方向各向异性量与 176 keV 的线偏振约束 E2/M1 混合。原文仍给两个邻近的混合比分支。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| OH89-DET | 四片直径 39 mm、厚 9 mm 的 Si(Li) 堆叠作散射体，旁置两只高纯 Ge。Monte Carlo 比较同尺寸 Si/Ge，并分别改变低能门限。低于约 300 keV 的条件下，作者的 Si 方案品质因子较高。这来自模拟接受条件，而非同尺寸实物的直接比试。 | calculated-geometry-comparison | direct-original-pages | PDF 1–3，§§2–3、图 1–3 |
| OH89-CAL | 低温取向 ⁵⁶,⁵⁷,⁶⁰Co 和 ¹²⁵Sb 做标定。试验散射体门限 12 keV。按原仪器式 \(P=(N_{90}-N_0)/[qQ_0(N_{90}+N_0)]\)。¹²⁵Sb 谱的 463、601、607、671 keV 线按纯 E2，637 keV 的 \(\delta\) 借自 Ref. 18。 | calibration-and-derived-polarization | direct-original-pages | PDF 2–4，式 1–3、图 4–5 |
| OH89-176 | ¹²⁵Te 的 321→145.4 keV \(9/2^-\to11/2^-\) 线，7 mK 时 \(\rho_2A_2=-0.3638(25)\)、\(\rho_4A_4=-0.0024(29)\)，\(P=+0.395(34)\)。按式 3 得 \(H_2(1,2)=-0.86(8)\)，中心回算约 −0.858。图 6 及正文给 \(\delta_{\rm E2/M1}=-0.63^{+0.16}_{-0.65}\) 或 \(-0.95^{+0.48}_{-0.33}\)。 | measured-and-derived-mixing | direct-original-pages-and-arithmetic | PDF 3–4，式 3、图 6 |

## Competing Interpretations and Limitations

- 方向分布分析中的母态退取向受一级禁戒 β 衰变及更高态 γ 馈入影响。利用同次角分布中的 \(\rho_kA_k\) 可少用显式的 \(\rho_k\) 输入。原文仍给两个 \(\delta\) 表达，统计误差下区间重叠。不能把正文所说的「无歧义」泛化成这一实例有唯一根。
- 装置与已知线共享温区、姿态和标定。图 5 的平滑曲线为通过实验点的标定曲线。这里的 \(\rho_kA_k\) 属低温取向观测与反推，无在束 \(\sigma/I\)。
- PDF 1 引言末句把 176 keV 跃迁写成 ¹²⁵Sb。摘要、§4、图 6、结论表明 ¹²⁵Sb 是源核，176 keV 是 ¹²⁵Te 子核退激。与 [[garber-1974-sb125-polarization-direction-correlation]] 的 ¹²⁵Sn→¹²⁵Sb 数据分别索引。

## Extracted Pages

- PDF 1–3：双材料响应、阈值模拟、标定和线偏振定义。
- PDF 4–5：标定图、¹²⁵Te 两组 \(\delta\)、结论和书目。
