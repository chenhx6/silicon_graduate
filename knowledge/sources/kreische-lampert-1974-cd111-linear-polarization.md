---
type: source
title: "Kreische and Lampert 1974 - Linear polarization in 111Cd"
title_original: "Messung der Linearpolarisation der 245 keV-γ-Strahlung in 111Cd"
aliases: []
created: 2026-11-21
updated: 2026-11-21
status: ai-draft
review_status: unreviewed
source_type: journal-article
reading_depth: read
authors: ["W. Kreische", "W. Lampert"]
year: 1974
doi: "10.1007/BF01668664"
canonical_source: "Zeitschrift für Physik 266 (1974), 51-53, published edition"
raw_file: raw/papers/gpt/query/20261119-polarization-delta-collection/10.1007_BF01668664.pdf
raw_sha256: 10637b7ebf09baa4abad25a8609d2eaec64cd6b58d6e254dfd3cb9b85a0a4481
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/papers/gpt/query/20261119-polarization-delta-collection/manifest.json
nuclei: ["111In", "111Cd"]
tags: ["linear-polarization", "gamma-gamma-correlation", "mixing-ratio", "polarimeter"]
---

# Kreische 与 Lampert 1974：¹¹¹Cd 的 245 keV 极化和 171 keV 混合比符号

## Bibliographic Record

W. Kreische、W. Lampert，*Zeitschrift für Physik* **266**, 51–53（1974）。PDF 1–3 对应印刷页 51–53。Ref. 1 是 1971 年的 Nuclear Data Sheets 既有绝对混合比来源。

## Scope and Reading Depth

三页完整核读，目视核对计数式、图 2–3、\(R\) 拟合和探测器品质的定义。

## Summary

用两片薄 NaI 同时记录 ¹¹¹In 衰变产生的 ¹¹¹Cd 171–245 keV 级联。分析的是第二条 245 keV 线的极化。该结果判定其为纯 E2，并在采用既有 \(\lvert\delta_{171}\rvert=0.145\) 的条件下选择 171 keV 混合的正号。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| KL74-GEOM | 245 keV 在两个直径 3.8 cm、厚 1 mm 的薄 NaI 晶体同时记录，靠散射光子随方位逃逸的差别分析全能峰。171 keV 用可转动的 NaI 选门，每个角度共积累 320 min。与三重符合康普顿装置相比，此布局只要求两条级联 γ 符合。 | measured-apparatus | direct-original-pages | PDF 1–3，§§2–4、图 1–3 |
| KL74-RATIO | 原文 \(p(\Theta)=W(\Theta,0)/W(\Theta,90^\circ)\)；\(N_\parallel/N_\perp=(1+Rp)/(R+p)\)。\(R\) 是极化灵敏度的比值参数，拟合给 1.7。图 2 的级联角依赖在纯 E2 与 M2 预测间选 E2。 | calibration-and-electric-character | direct-original-pages | PDF 2，§§3–4、图 2 |
| KL74-SIGN | 作者明确放弃对 171 keV 的 \(\lvert\delta\rvert\) 重新做 \(\chi^2\) 拟合，计算 \(\delta=\pm0.145\) 两个分支。负号的理想极化变化 \([p(180^\circ)-p(90^\circ)]/p(180^\circ)=0.07\)，低于实验约 0.12，由此选正号。\(N_\parallel+N_\perp\) 随 \(\Theta\) 的变化与普通角关联作控制。 | sign-confirmation-with-fixed-magnitude | direct-original-pages | PDF 2–3，§4、图 2–3 |

## Competing Interpretations and Limitations

- 原生 \(p\) 是强度比。在同一方位定义下 \(P=(p-1)/(p+1)\)。由本篇的响应式推得 \(r=(1+Q_{\rm eff}P)/(1-Q_{\rm eff}P)\)，其中 \(r=N_\parallel/N_\perp\)、\(Q_{\rm eff}=(R-1)/(R+1)\simeq0.259\)。符号与散射几何有关，不能跨设备仅凭计数标号照搬。
- 本篇用 \(A=2(N_\parallel-N_\perp)/(N_\parallel+N_\perp)\) 表示 \(\Theta=90^\circ\) 的不对称，报告 12.8%。\(A^2\varepsilon\) 的品质讨论须与这个系数 2 及探测效率同用。文中比较的 3 mm 晶体计数效率约高三倍，\(A\) 则较小。
- 图 2 的极化证实 245 keV 电性，171 keV 的既有绝对值和本次符号选择是不同证据。全文未给在束 \(\sigma/I\)，也未提供 171 keV 本次独立拟合区间。

## Extracted Pages

- PDF 1：级联动机和薄晶体的方位逃逸原理。
- PDF 2：原生观测量、角扫描、标定及符号检验。
- PDF 3：双符合、效率与不对称、来源。
