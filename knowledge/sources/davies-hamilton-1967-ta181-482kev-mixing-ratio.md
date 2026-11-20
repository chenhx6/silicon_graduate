---
type: source
title: "Davies and Hamilton 1967 - 181Ta 482 keV mixing ratio"
title_original: "The Linear Polarization of the 482 keV Transition in 181Ta"
aliases: []
created: 2026-11-21
updated: 2026-11-21
status: ai-draft
review_status: unreviewed
source_type: journal-article
reading_depth: read
authors: ["K. E. Davies", "W. D. Hamilton"]
year: 1967
doi: "10.1016/0375-9474(67)90695-1"
canonical_source: "Nuclear Physics A 96 (1967), 65-80, published edition"
raw_file: raw/papers/gpt/query/20261119-polarization-delta-collection/10.1016_0375-9474_67_90695-1.pdf
raw_sha256: 0050920af3e7b86a525088350fa84148a72e4457cd171a43bebc4922c01cbe2d
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/papers/gpt/query/20261119-polarization-delta-collection/manifest.json
nuclei: ["181Hf", "181Ta"]
tags: ["gamma-gamma-correlation", "linear-polarization", "mixing-ratio", "hyperfine-attenuation"]
---

# Davies 与 Hamilton 1967：¹⁸¹Ta 482 keV 混合比

## Bibliographic Record

K. E. Davies、W. D. Hamilton，*Nuclear Physics A* **96**, 65–80（1967）。PDF 1–16，印刷页 = PDF 页 + 64。Ref. 16 是当时在投的极化仪方法，正式出版见 [[davies-hamilton-1968-gamma-gamma-polarimeter-calibration]]。

## Scope and Reading Depth

覆盖论文 16 页。回核图 1、4–6，表 1–3、计数比、按阶消参及摘要与修正结果。

## Summary

两种 ¹⁸¹Hf 衰变源介质给出不同的 γ–γ 角关联和线偏振调制。对每一介质分别联用两类观测，共同的退取向及先行跃迁因子通过按阶比值约去。摘要给出 482 keV 的 E2/M1 混合比 \(+7.2^{+1.8}_{-1.5}\)，正文补做 476 keV 串扰检查后为 \(+7.3^{+1.7}_{-1.5}\)。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| DH67-BACKGROUND | ¹⁸¹Hf β 衰变的 \((133+137)\)–482 keV 级联。先前用内转换来推断 482 keV 混合比受穿透效应限制。作者引用的 137 keV 方案含 \(\delta=2.3\pm0.9\) 与 \(\lvert\delta\rvert<0.22\) 两个冲突的结论，伴随不同 \(J^\pi\) 解释，保留为不同来源。 | earlier-experiments-and-disagreement | direct-original-pages-for-author-representation | PDF 1–6，图 1、表 1、§§1–4 |
| DH67-DIR | 方向关联在 \(60^\circ,90^\circ,120^\circ,150^\circ,180^\circ\) 取数，按 \(1:2:2:2:1\) 加权。有限探测器和源轴向延展进入拟合，表 2 给实测 \(A_{22},A_{44}\)。没有用固定 \(\sigma/I\) 来生成这两个系数。 | direct-directional-correlation | direct-original-pages | PDF 6–7，§5、图 3、表 2 |
| DH67-POL | 以固定级联角 \(\theta=90^\circ\) 扫方位。两 NaI 晶体做求和极化仪。分析晶体接受 220–344 keV 的散射光子，对主线对应 \(55^\circ\)–\(105^\circ\)。校正后 \(k=N_0/N_{90}\)，用 \(C=(k-1)/(k+1)\) 表示方位调制；482 keV 的共同标定量为 \(Q=0.46\pm0.04\)。 | direct-polarimetry-and-calibration | direct-original-pages | PDF 7–10，§6、图 4–5 |
| DH67-CANCEL | 在同一介质和同一有效级联下写 \(A_{kk}=G_kA_k(1)A_k(2)\)。极化分子同阶为 \(G_kA_k(1)A'_k(2)P_k^2(\cos\theta)\)。代入后，\(-C/Q=\big[\sum_{k=2,4} A_{kk}\{A'_k(2)/A_k(2)\}P_k^2(\cos\theta)\big]/[1+\sum_{k=2,4}A_{kk}P_k(\cos\theta)]\)。\(P_k^2\) 是缔合勒让德函数，\(G_k\) 是源介质扰动的衰减。作者按秩作图并用 M1/E2 的四阶比值恒定来投影二阶解。 | conditional-cancellation-and-inference | direct-original-pages | PDF 10–13，§7、图 6 |
| DH67-RESULT | HCl/HF 合并后未经 476 keV 修正的 E2 比例为 \(98.1^{+0.6}_{-1.2}\%\)，对应 \(\delta=+7.2^{+1.8}_{-1.5}\)。作者估计 476 keV 相对主线为 4%，两线分不开，按纯 M2 算 \(C\) 修正因子 1.05，角关联和极化修正部分抵消，正文末给 \(\delta=+7.3^{+1.7}_{-1.5}\)。 | reported-mixing-ratios | direct-original-pages | PDF 12–14，§§7–9、表 3 |

### 校正 476 keV 串扰前的输入

| ¹⁸¹Hf 源介质 | \(A_{22}\) | \(A_{44}\) | \(k=N_0/N_{90}\) |
| --- | --- | --- | --- |
| HCl | \(-0.091\pm0.004\) | \(-0.011\pm0.006\) | \(1.061\pm0.028\) |
| HF | \(-0.236\pm0.006\) | \(-0.037\pm0.010\) | \(1.129\pm0.029\) |

## Competing Interpretations and Limitations

- 同阶约分要求方向与极化两次测量中 \(G_kA_k(1)\) 相同。先行门内两条线若共享 482 keV 末跃迁，它们的贡献可以共同进入有效的 \(A_k(1)\)。另一条末跃迁 476 keV 的 \(A_k(2),A'_k(2)\) 不同，必须另处理。前向计算遇 \(A_k(2)=0\) 时保留原乘积或取有定义的极限。
- 表 3 图注写 4% 的 137–482 keV 成分，§8 正文在计算 133–476 keV 串扰。表 3 的 HCl、HF 分别为 \((-0.096(4),-0.011(6))\) 和 \((-0.249(6),-0.039(6))\)。两处说明按原文留存。极化方位列表在本文 PDF 8 印出 \(125^\circ\)，1968 年方法标定 PDF 17 的对应方位为 \(135^\circ\)，无定位日志可消除此差异。
- 图 6 的误差条是 probable errors，正文给出的限值用标准差。两介质共享极化仪的 \(Q\) 标定与方法，最终 \(+7.2\) 和 \(+7.3\) 是同一测量的不同校正版本。PDF 15 的圆偏振用于讨论理论后果，原文的 \(\delta\) 提取用线偏振。
- 这是衰变级联方向–方向加方向–线偏振的联合求解。\(A_{22},A_{44}\) 是角关联系数。本文未拟合在束磁子态布居，也未报道在束 \(\sigma/I\) 数值。

## Extracted Pages

- PDF 1–6：混合比的物理动机、衰减和 137 keV 竞争解释、两种源及方向计数。
- PDF 7–11：角关联与极化直接量、标定条件和按秩约分。
- PDF 12–16：图解、两组混合比、末跃迁串扰与受其影响的转换和理论讨论。
