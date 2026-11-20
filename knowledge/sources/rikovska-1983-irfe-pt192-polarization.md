---
type: source
title: "Rikovska et al. 1983 - Linear polarization from oriented Ir in Fe"
title_original: "Gamma-ray linear polarization and nuclear orientation experiments on oriented 192,194IrFe"
aliases: []
created: 2026-11-21
updated: 2026-11-21
status: ai-draft
review_status: unreviewed
source_type: journal-article
reading_depth: read
authors: ["J. Rikovska", "D. Novakova", "J. Ferencei"]
year: 1983
doi: "10.1007/BF02159712"
canonical_source: "Hyperfine Interactions 15/16 (1983), 41-42, published edition"
raw_file: raw/papers/gpt/query/20261119-polarization-delta-collection/10.1007_BF02159712.pdf
raw_sha256: b8ee389f192877efdc6a8a179b7f6f6967edfd7f45491c30994109ea8f6a97e0
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/papers/gpt/query/20261119-polarization-delta-collection/manifest.json
nuclei: ["192Ir", "192Pt", "194Ir", "194Pt"]
tags: ["linear-polarization", "nuclear-orientation", "mixing-ratio"]
---

# Rikovska 等 1983：Ir/Fe 低温取向和 ¹⁹²Pt 线偏振

## Bibliographic Record

J. Rikovska、D. Novakova、J. Ferencei，*Hyperfine Interactions* **15/16**, 41–42（1983）。PDF 1–2 对应印刷页 41–42。对照引用 Ref. 5 为 [[hamilton-1968-angular-correlations-192pt]]。Ref. 1 在本文用于方法。

## Scope and Reading Depth

两页完整核读。目视核对式 1–5、表 1、β 馈入、¹⁹⁴Ir 的例外与书目。

## Summary

将 Ir/Fe 冷源的轴向角分布与 \(90^\circ\) 线偏振结合，报告 ¹⁹²Pt 的三条有符号混合比。¹⁹⁴Pt 的数值来自另一套温度依赖的角分布拟合。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| R83-SETUP | 约 1 at% Ir/Fe，外场 0.8 T，最低温 \(15\pm1\) mK，方向分布在 \(0^\circ\) 与 \(90^\circ\) 测量。两分片平板 Ge(Li) 极化仪在 \(\theta=90^\circ\) 取两方位，报告 150–1500 keV 的极化检测效率范围约 60%–30%。 | experimental-geometry | direct-original-pages | PDF 1，方法段 |
| R83-RESPONSE | \(A_{\lambda\lambda}=B_\lambda U_\lambda A_\lambda\)。模型在 \(P(\pi/2)\) 中用 \(H_2(\delta)\) 关联极化与已测 \(A_{22},A_{44}\)。方位不对称 \(\Delta=(N_\perp-N_\parallel)/(N_\perp+N_\parallel)\)，\(P_{\rm exp}=\Delta/Q\)。文中利用温度依赖获得 \(B_\lambda\)，另用已知馈入估计 \(U_\lambda\) 和 β 矩阵元强度比。 | response-and-analysis | direct-original-pages | PDF 1–2，式 1–5 |
| R83-PT192 | ¹⁹²Pt 表 1 的 296、308、604 keV 混合比为 \(+15(4),+7.6(1),-1.4(1)\)，以原文符号记录。四条其他线在表内有极化与分布，但未列混合比。 | direct-experimental-table | direct-original-pages | PDF 2，表 1 |
| R83-PT194 | ¹⁹⁴Ir 衰变的 γ 线太弱而且源衰变过快，未得到有效的线偏振测量。889、1184、1294 keV 的 \(1.51(40),1.32(9),1.79(3)\) 由温度依赖 \(W(0^\circ)\) 和已知超精细参数推出。 | angular-distribution-only | direct-original-pages | PDF 2，表后末段 |

### ¹⁹²Pt 表 1 的混合跃迁

| \(E_\gamma\) (keV) | \(J_i^\pi\to J_f^\pi\) | \(A_{22}\) | \(A_{44}\) | \(P_{\rm exp}\) | \(\delta_{\rm exp}\) |
| --- | --- | --- | --- | --- | --- |
| 296 | \(2^+\to2^+\) | \(0.009(5)\) | \(0.033(5)\) | \(0.05(4)\) | \(+15(4)\) |
| 308 | \(3^+\to2^+\) | \(-0.364(6)\) | \(0.155(6)\) | \(0.03(1)\) | \(+7.6(1)\) |
| 604 | \(3^+\to2^+\) | \(0.939(12)\) | \(0.165(14)\) | \(-0.27(4)\) | \(-1.4(1)\) |

## Competing Interpretations and Limitations

- 原文把既有方向关联与理论作对照。比较 [[hamilton-1968-angular-correlations-192pt]] 的带符号值时须复核相位与时序，先各自保留符号。1983 年实验使用 Ir/Fe 的母核低温取向，1968 年实验用 γ–γ 条件关联。
- 原文线偏振用已测 \(A_{22},A_{44}\) 和 \(Q\)。母核热取向和 β 馈入的退取向另作分析。这里的 \(B_\lambda\) 属于低温超精细取向，全文未报告在束 \(\sigma/I\)。
- PDF 1 的温度范围段排作 Pt 衰变，本文的实验身份和末段是 Ir 母核衰变到 Pt。β 的 \(\Lambda^2\) 比和 ¹⁹⁴Pt 仅角分布的 \(\delta\) 各有定义。

## Extracted Pages

- PDF 1：冷源、几何、实验灵敏度和角分布–极化模型。
- PDF 2：计数比、表 1、β 馈入、¹⁹⁴Pt 适用性和书目。
