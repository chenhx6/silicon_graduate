---
type: source
title: "Reddingius, Potters and Postma 1968 - Nd neutron-capture anisotropy and polarization"
title_original: "A study of gamma-ray spectra of thermal neutron capture in 143Nd and 145Nd; Including directional anisotropy and linear polarization measurements of such gamma rays from aligned 143Nd nuclei"
aliases: []
created: 2026-11-21
updated: 2026-11-21
status: ai-draft
review_status: unreviewed
source_type: journal-article
reading_depth: read
authors: ["E. R. Reddingius", "J. F. M. Potters", "H. Postma"]
year: 1968
doi: "10.1016/0031-8914(68)90061-X"
canonical_source: "Physica 38 (1968), 48-66, published edition"
raw_file: raw/papers/gpt/query/20261119-polarization-delta-collection/10.1016_0031-8914_68_90061-X.pdf
raw_sha256: 133b9593691d9ab9cd785bd9c3f7a875b68e8cacecf36475a4045a570cf5830c
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/papers/gpt/query/20261119-polarization-delta-collection/manifest.json
nuclei: ["143Nd", "144Nd", "145Nd", "146Nd"]
tags: ["neutron-capture", "linear-polarization", "mixing-ratio", "nuclear-alignment"]
---

# Reddingius、Potters 与 Postma 1968：Nd 俘获后的各向异性与线偏振

## Bibliographic Record

E. R. Reddingius、J. F. M. Potters、H. Postma，*Physica* **38**, 48–66（1968）。PDF 1–19 对应印刷页 48–66。Ref. 2 为同研究团队的早期配对谱仪测量。本文明确用 Ge(Li) 重做方向分布，保留早期方法和所借用的退取向计算。

## Scope and Reading Depth

覆盖 19 页，包括富集样品、俘获峰、各向异性、极化标定、分支比较和文献汇编。目视核对式 1、表 3–6、图 6–7。

## Summary

比较富集 \(^{143,145}\mathrm{Nd}\) 样品以区分俘获得到的 \(^{144,146}\mathrm{Nd}\)。在冷却取向 \(^{143}\mathrm{Nd}\) 的俘获谱中，以两条纯 E2 线标定 Compton 极化仪，再把 \(^{144}\mathrm{Nd}\) 的 864 keV 线偏振与方向各向异性合用，得到 \(2^+_2\to2^+_1\) 的混合比。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| RPP68-ISOTOPE | 6520 keV 和 6505 keV 分别归 \(^{146}\mathrm{Nd}\) 与 \(^{144}\mathrm{Nd}\)。7110(5) keV 线仅见于富 \(^{145}\mathrm{Nd}\) 俘获谱，归 \(^{146}\mathrm{Nd}\)，在 \(^{144}\mathrm{Nd}\) 同能区报告上限 0.008 γ/100 次俘获。初级线与二次跃迁使用不同的强度归一。 | spectral-identification-and-limit | direct-original-pages | PDF 4–10，图 2–5、表 1–3、§4 |
| RPP68-ALIGN | Nd 乙基硫酸盐单晶从 1 K、12.9 kOe 绝热退磁到 0.014 K，按有效自旋哈密顿量计算 \(f_2=0.348,f_4=0.033\)。对 \(^{143}\mathrm{Nd}\) 的 \(s\) 波俘获 \(J=3^-\) 共振采用 \(G_2=35/36,G_4=343/432\)。对低能次级线进一步按平均先行 γ 数 \(\nu\) 估计退取向，纯 E2 的 616、696 keV 各向异性支持 \(\nu=3\) 的参照。 | modeled-alignment-and-control | direct-original-pages | PDF 2–3、10–12，式 3–4、表 5 |
| RPP68-POL | 符合求和极化仪散射体和两个侧探测器均为 NaI(Tl)。616、696 keV 纯 E2 对应 \(\bar Q=0.41(5),0.40(5)\)；能量外推对 814、864 keV 给 \(0.36(4),0.34(4)\)。正文用各向异性与 \(P\) 支持 814 keV 为 1510→696 keV 的 \(3^-\to2^+\) E1，并保留 2377→1560 keV 的既有归属。 | measured-polarization-and-interpretation | direct-original-pages | PDF 2–4、8–9、12–14，式 1–2、图 1、表 4、图 7 |
| RPP68-MIX | 864 keV 连接 1560 与 696 keV 的 \(2^+\) 态。联合 \(W(0^\circ)-1=0.077(13)\) 与 \(P=-0.23(7)\)，在图 6 的 \(\nu=2,3,4\) 曲线比较中选原文 \(\delta>0\) 支，正文给 E2 百分比 18–38，表 6 列 \(\lvert\delta\rvert=0.63\pm0.15\)。前一区间按 \(\delta^2/(1+\delta^2)\) 换算为 \(\lvert\delta\rvert\simeq0.469\)–0.783。 | measured-inputs-and-conditional-mixing | direct-original-pages-and-arithmetic | PDF 9、12–14、17，表 4、图 6–7、表 6 |

### 表 4 与正文的低能线

| \(E_\gamma\) (keV) | \(N_\perp/N_\parallel\) | \(W(0^\circ)-1\) | \(\bar Q\) | 原文 \(P\) |
| --- | --- | --- | --- | --- |
| 616 | \(0.75\pm0.03\) | \(-0.267\pm0.010\) | \(0.41\pm0.05\) | 用式 2 作为标定输入 |
| 696 | \(0.80\pm0.02\) | \(-0.215\pm0.010\) | \(0.40\pm0.05\) | 用式 2 作为标定输入 |
| 814 | \(0.78\pm0.03\) | \(+0.158\pm0.025\) | \(0.36\pm0.04\) | \(-0.35\pm0.06\) |
| 864 | \(0.85\pm0.04\) | \(+0.077\pm0.013\) | \(0.34\pm0.04\) | \(-0.23\pm0.07\) |

## Competing Interpretations and Limitations

- 式 1 定义 \(N_\parallel/N_\perp=(1-\bar QP)/(1+\bar QP)\)，表 4 列倒数 \(r=N_\perp/N_\parallel\)。按 \(P=(r-1)/[\bar Q(r+1)]\) 复算 814 和 864 keV 分别约 −0.343 和 −0.238。两线共用 E2 标定方案，原文未给跨线协方差。PDF 4 把一条标定线印作 816 keV，图表和具体计算给 616 keV。
- 作者对次级线取向的认识来自给定的温度和哈密顿量、俘获后的退取向以及 \(\nu\) 依赖的馈入近似。该模型不是在束高自旋高斯布居，本文范围内没有在束 \(\sigma/I\) 数值。图 6 的条带比较不添加联合置信水平。
- 文中说明 Ref. 16 的混合比约定与本文章同时倒数和反号。表 3 的 4680 keV 四极比例按千分数打印，并有未分辨弱线的替代解释；其 \(\delta<0\) 标签不能转给 864 keV。
- 理论讨论将 1313/1560 keV 态与两声子候选比较。较大的间距、缺少相应低 \(0^+\) 态以及 864 keV 主 M1 是单纯振子图像的限制。表 6 的其余核素主要取自文献重算、加权或来源选择。它们的原始实验手段须回到各篇原文核对。

## Extracted Pages

- PDF 1–5：实验问题、温度、同位素样品、极化方位与装置。
- PDF 6–9：按同位素的强度、能窗和各向异性，四条低能极化线。
- PDF 10–14：束缚能、取向传播、混合分支和能级图。
- PDF 15–19：集体模型与壳效应、偶偶系统学和溯源文献。
