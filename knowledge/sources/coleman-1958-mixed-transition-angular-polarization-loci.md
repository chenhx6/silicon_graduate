---
type: source
title: "Coleman 1958 - Angular and direction-polarization loci of mixed transitions"
title_original: "The Analysis of Angular and Direction-Polarization Correlation Measurements on Mixed Transitions"
aliases: []
created: 2026-11-21
updated: 2026-11-21
status: ai-draft
review_status: unreviewed
source_type: journal-article
reading_depth: read
authors: ["C. F. Coleman"]
year: 1958
doi: "10.1016/0029-5582(58)90051-8"
canonical_source: "Nuclear Physics 5 (1958), 495-503, published edition"
raw_file: raw/papers/gpt/query/20261119-polarization-delta-collection/10.1016_0029-5582_58_90051-8.pdf
raw_sha256: 5bd458a84f6bd083c8a759d85dd5b49d5d05515ee5fee78d80f41e804674aa8c
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/papers/gpt/query/20261119-polarization-delta-collection/manifest.json
nuclei: ["122Te", "114Cd", "140Ce"]
tags: ["gamma-gamma-correlation", "linear-polarization", "mixing-ratio", "covariance"]
---

# Coleman 1958：混合跃迁的角关联与线偏振参数曲线

## Bibliographic Record

C. F. Coleman，*Nuclear Physics* **5**, 495–503（1958）。PDF 1–9 对应印刷页 495–503。同 DOI 的一页摘录仅覆盖 PDF 1。图 2–3 的其他实验点各有独立引文，¹²²Te 的方向–极化测量由本文报告。

## Scope and Reading Depth

覆盖 9 页的理论、实验样例、附录与参考文献。核对图 3–6、¹²²Te 的参数读数及 \(A_2,A_4\) 误差处理。

## Summary

将两项观测同时画在一张参数图上，用一条曲线表示具有单个混合比的候选级联。若只测方向关联，可能有几条自旋序列或几个 \(\delta\) 分支均可行。本文展示选择混合线来测极化如何提高分支分辨力。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| COL58-LOCUS | 对已定级联中的单个偶极–四极混合跃迁，\(A_2=(a_2+b_2\delta+c_2\delta^2)/(1+\delta^2)\)，\(A_4=c_4\delta^2/(1+\delta^2)\)。图以 \(\delta'=\delta/(1+\lvert\delta\rvert)\) 标注曲线，两端纯多极点是正负支接合处。两条跃迁都混合时，可绘制一族曲线，观测点可能对应不止一组 \((\delta_1,\delta_2)\)。 | parametric-constraint | direct-original-pages | PDF 2–4、8，图 2–3、附录 |
| COL58-POL | 小 \(\lvert\delta\rvert\) 时四阶方向系数从二次项起，混合线的偏振一般保留一阶干涉灵敏度。相同的各向异性可能对应两个 \(\delta\)；若分析纯线，两解的极化可能相近。图 4 的两个宇称标尺相对于 \(P'=0\) 镜像，宇称指被分析跃迁的两端态。 | branch-and-parity-dependence | direct-original-pages | PDF 4–5、8，§3、图 4 |
| COL58-TE | 以 ¹¹⁴Cd 720–560 keV 纯 E2 级联校准，720 keV 的 polarimeter ratio 为 \(1.95\pm0.30\)。¹²²Te 的 690–560 keV 级联在级联夹角 \(105^\circ\) 分析 690 keV 线，支持它是混合跃迁且很可能不变宇称。图 4 与正文选择 \(\delta'\simeq+0.8\) 而非 \(-0.05\)，与既有 \(A_4\) 对应分支一致。按作者坐标换算大支 \(\delta\) 约 \(+4\)，该换算精度受曲线读数限制。 | experiment-and-branch-selection | direct-original-pages-and-arithmetic | PDF 5–7，图 4–6、§3 |
| COL58-COV | 同一角度拟合的 \(A_2,A_4\) 共享输入，两个单独误差不能确定等概率椭圆。附录用独立角度计数传播到两系数并求主方向。各阶有限角度校正不同，变换后的椭圆也要按各阶缩放。 | uncertainty-propagation | direct-original-pages | PDF 8–9，附录 |

## Competing Interpretations and Limitations

- 令 \(u=A_4/c_4\) 且 \(c_4\ne0\)。由原式消元得到 \([A_2-a_2-(c_2-a_2)u]^2=b_2^2u(1-u)\)，其中 \(0\le u\le1\)。\(b_2,c_4\) 均非零时给非退化椭圆。干涉或四阶灵敏度消失时可退化。这是由附录公式直接推出的条件。
- ¹⁴⁰Ce 的方向数据可同时与 \(2,2,0\) 及 \(3,2,0\) 相容。对仪器未分开的两条线，混合与纯线的偏振响应按探测效率和能量响应进入同一观测，不能直接读单线轨迹。这里的 ¹²²Te 例为衰变级联，也未采用在束 \(\sigma/I\) 输入。
- 原刊采用 \(P'=(J_\parallel-J_\perp)/(J_\parallel+J_\perp)\)。PDF 8 的印刷式在同页角分布先写出 \(1+\delta^2\) 归一，而后续 \(P'\) 分母的常数项印成 1。若从给定 \(W=1+A_2P_2+A_4P_4\) 通分，则常数部分为 \(1+\delta^2\)。复用公式从归一的 \(A_k\) 重建，避免沿用版面歧义。

## Extracted Pages

- PDF 1–4：角关联两系数、椭圆及自旋歧义、两条跃迁都混合的曲线族。
- PDF 5–7：偏振选支、宇称标尺、谱仪和 ¹²²Te 标定应用。
- PDF 8–9：参数曲线推导、偏振式、系数协方差和参考文献。
