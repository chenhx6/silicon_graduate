---
type: source
title: "Postma 1959 - 166mHo orientation and 166Er linear polarization"
title_original: "Angular distribution and linear polarization of gamma rays from aligned 166mHo nuclei"
aliases: []
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: journal-article
reading_depth: read
authors: ["H. Postma", "A. R. Miedema", "M. C. Eversdijk Smulders"]
year: 1959
doi: "10.1016/S0031-8914(59)97064-8"
canonical_source: "Physica 25 (1959), 671-687, published edition"
raw_file: raw/papers/gpt/query/20261119-polarization-delta-collection/10.1016_s0031-8914_59_97064-8.pdf
raw_sha256: 5e24c549c57160fc03fa90f088aae7705a8be8be8b13548c9df7a2a130351c40
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/papers/gpt/query/20261119-polarization-delta-collection/manifest.json
nuclei: ["166Ho", "166Er"]
tags: ["linear-polarization", "nuclear-orientation", "angular-distribution", "mixing-ratio", "overlapping-peaks"]
---

# Postma 等 1959：¹⁶⁶ᵐHo 取向衰变与 ¹⁶⁶Er 的线偏振

## Bibliographic Record

H. Postma、A. R. Miedema、M. C. Eversdijk Smulders，*Physica* **25**, 671–687（1959）。本地 17 页为完整排印版。另有 `raw/papers/gpt/query/20261119-pdm-delta-broad/10.1016_s0031-8914_59_97064-8.pdf`，其一页文字与排印版第 1 页相同。[[nambudripad-1980-ho-er-nuclear-orientation-thesis]] 第 6 章把本研究作为早期对照，并使用不同基质和仪器。

## Scope and Reading Depth

已核 17/17 页的研究范围及书目。原刊印刷页 = PDF 页 + 670。目视重点为第 675、681、683–684 页。

## Summary

作者用低温超精细排列产生 ¹⁶⁶ᵐHo 取向，由 ¹⁶⁶Er 的 γ 单谱角分布识别多极阶数及混合比，再用康普顿极化对两条主要跃迁的电磁性质及宇称提供约束。两条线在极化符合谱中需要串扰处理。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| POS-ALIGN | 将 ¹⁶⁶ᵐHo 置于 Nd ethyl sulphate 单晶，取向轴为晶体 \(c\) 轴。在 \(T\approx0.025(2)\) K 下用超精细布居参数和级联传递系数分析，各向异性用 1 K 归一。极低温近完全排列和上游 β 馈入去取向是模型输入。 | acquisition-and-orientation | direct-original-pages | 印刷 674–678、680–683 页，式 2–4，表 II |
| POS-ANG | 当 \(1/T^*\approx40\,\mathrm{K}^{-1}\) 时，表 I 的 706 keV 单 γ 分量为 \(W(0)=1.31(2)\)、\(W(90^\circ)=0.84(2)\)，817 keV 为 \(1.65(2)\)、\(1.14(2)\)。角分布插值给 817 keV 的 \(\delta\) 约 30–100，706 keV 的高阶成分 \(\lvert\delta\rvert<0.02\)。两线分别在 \(1790\to973\to267\) keV 级联的一上、一下两个位置。 | angular-data-and-conditional-mixing | direct-original-pages | 印刷 673、675、678–681 页，表 I、图 1、3–4 |
| POS-P | 706 和 817 keV 的 NaI(Tl) 康普顿符合峰互相重叠。90° 发射条件下，混合峰的 \(N_\perp/N_\parallel=0.88(3)\)，低能边 0.65(9)，高能边 1.32(9)。作者用 \(\bar Q=0.50\) 以及低能边约 15% 的 817 keV 和高能边约 10% 的 706 keV 串扰，报告 \(P_{706}=-(0.62^{+0.20}_{-0.18})\)、\(P_{817}=+0.36^{+0.10}_{-0.13}\)。 | jointly-inferred-polarizations | direct-original-pages | 印刷 676–677、683–684 页，式 5 |
| POS-ID | 706 keV 被指认为近纯 E1，817 keV 为 E2 主导并可能有少量 M1。表 I 的 283 keV 信号又是两线重叠。作者假定等强度扣除基带支路后，对剩余 II 分量给 \(\delta=-1.5^{+0.5}_{-0.3}\)，并讨论 1256 keV 的 \(5^-\) 指认。283 keV 未有分线偏振。 | assignment-and-doublet-boundary | direct-original-pages | 印刷 681–686 页，§§5–7 |

## Competing Interpretations and Limitations

- 式 5 对各线用 \(C_iW_i(90^\circ)\) 加权，不能用未加权的 \(P\) 平均。利用表 I 的中心值、\(C_{706}/C_{817}=0.55/0.45\) 与纯多极估计，四种电磁符号给 \(R\) 约 0.602、1.661、0.967、1.034。印刷值为 0.60、1.66、0.96、1.04。混合峰实测 0.88(3) 与所选情形的中心值仍有差距，作者讨论串扰权重及 817 keV 的小偶极成分。高低两侧的纯度估计要与 \(P\) 一并引用。
- 这是低温取向的单 γ 角分布与线偏振比较，\(W\) 相对于晶体轴，不能把表 I 当作现代符合定义的 \(R_{\rm DCO}\) 或直接套用在束取向率。文中另引 Grace 等 \(\gamma\gamma\) 角关联，那些系数属于另一数据链。
- 早期 ¹⁶⁶ᵐHo 磁矩随假定母核自旋 \(I_0=6,7,8\) 而变。\(I_0=7\) 时给 \(3.3(5)\,\mu_N\)，与后来的 HoVO₄ 结果分实验记录。

## Extracted Pages

- PDF 1–7：发表记录、稀土基质、历史能级与探测/偏振装置。
- PDF 8–14：张量传递、反演分支、谱线重叠及混合偏振。
- PDF 15–17：早期符合数据与组态解释、拟合的限度、书目。
