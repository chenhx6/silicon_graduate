---
type: source
title: "Lizarazo Sabogal 2018 - Gamma-ray spectroscopy of 92,94Se isomeric decay"
title_original: "Gamma-ray spectroscopy of 92,94Se isomeric decay"
aliases: []
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: doctoral-thesis
reading_depth: read
authors: ["Cesar Yesid Lizarazo Sabogal"]
year: 2018
institution: "Technische Universität Darmstadt"
doi: 10.26083/tuprints-00007266
canonical_source: "Approved doctoral dissertation, Technische Universität Darmstadt, PDF 1–3"
raw_file: raw/theses/gpt/query/20261119-international-nuclear-structure/lizarazo_phd_thesis.pdf
raw_sha256: e7d28d9cd104d4dcaad212828d4b4e12006082a98a4b5d0b3c24cbc86d75f5c3
raw_storage_status: archived-local
archive_required: true
nuclei: ["92Se", "94Se"]
tags: [isomers, gamma-spectroscopy, internal-conversion, half-life, shape-evolution]
---

# Lizarazo Sabogal 2018：硒-92、硒-94 的异能态衰变与形状解释

## Bibliographic Record

Cesar Yesid Lizarazo Sabogal，博士学位论文，Technische Universität Darmstadt。
PDF 2 记载提交于 2018 年 1 月 17 日，答辩于 2018 年 2 月 5 日，并给出 tuprints
标识 URN `urn:nbn:de:tuda-tuprints-72660`。

## Scope and Reading Depth

主读和验收范围为 PDF 1–153，含正文章节、两项附录、书目及成果目录。
PDF 154 是个人资料页，保持在本地原件。PDF 18–138 的正文印刷页为 PDF 页 − 17。
Codex 回核关键能级、原图及算术。引文原件及事件级分析各有独立核读范围。

## Summary

用 RIKEN 植入标识和 EURICA 延迟 γ 谱获得 $^{92,94}$Se 的半衰期与候选纲图。
作者将强度平衡、符合关系、可检测性能窗和在束谱结合起来提出自旋宇称，
再与组态和集体模型比较。两处寿命或阻碍计算的原式数字不能直接得到所印结果。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| LS-1 | 利用离子鉴别与植入关联选择延迟 γ，能量校正、time walk、addback、光峰效率和随机符合扣除按各自步骤处理。后续衰变谱与附录的 DALI2 在束谱使用不同探测条件。 | experimental-method | direct-original-pages | PDF 67–98, 99, 142 |
| LS-2 | $^{92}$Se 共用延迟馈入的合计时间谱给出 $T_{1/2}=15.7(7)$ μs。假定没有遗漏强分支，以 503 keV 与 67 keV 的效率修正光子强度推得 $\alpha_{\mathrm{exp}}=2.95(68)$。同全壳 BrIcc 值比较后，作者倾向 67 keV E2，候选纲图把它置于 3072 至 3005 keV。 | measurement-and-conditional-assignment | direct-original-pages | PDF 106 Fig. 7.7, 111–115 Eqs. (113)–(118), Table 11, Fig. 7.13 |
| LS-3 | Eq. (118) 印为 8.9 μs。代入紧邻式中的 $\tau_\gamma=2.44\times10^{-5}$ s 与 $\alpha=2.95$，$T_{1/2}=\tau_\gamma\ln 2/(1+\alpha)\approx4.28$ μs。两者保留，算术复核未改动实验半衰期。 | dimensional-and-arithmetic-check | reproduced-from-printed-operands | PDF 114 Eq. (118) |
| LS-4 | $^{94}$Se 合计延迟谱给出 $T_{1/2}=0.68(5)$ μs。752、1180 keV 弱峰具有相近时间行为，能量和也与另一衰变路径相容。符合统计不足，作者未纳入最终图。2429 keV 的 $7^-$ 为建议归属。 | measurement-and-conditional-assignment | direct-original-pages | PDF 121–127 Figs. 7.17–7.22, Table 13 |
| LS-5 | $^{94}$Se Fig. 7.22 把 495 keV 置于 2429→1934 keV，470 keV 置于低位 $2^+\to0^+$；§8.1 有一处把上端支路写作 470 keV。保留两处原文，以图和能量闭合标记这是疑似笔误。 | text-figure-conflict | direct-original-pages | PDF 126 Fig. 7.22, 130, 136 |
| LS-6 | Eqs. (123)–(124) 印出 $F_W\approx2.52(18)\times10^8$、$f_\nu\approx25.1(3)$。若按前句 269.5 fs 并用同类寿命量比较，$0.68$ μs / $269.5$ fs 约为 $2.52\times10^6$，$\nu=6$ 时六次根约为 11.7。印出的代入分母 $2.695\times10^{-15}$ s 则对应 2.695 fs。归一基准需独立核定后才能引用阻碍数值。 | arithmetic-and-normalization-check | reproduced-from-printed-operands | PDF 130–131 Eqs. (123)–(124), Fig. 8.2 |
| LS-7 | N=60 的偏扁形状解释综合衰变路径、未见分支、邻核和 SCCM/5DCH 等计算。低能跃迁可受内转换和探测阈值压低，较高能段效率缺少直接标定。作者也讨论竞争带可能抬高的解释。 | author-interpretation-and-boundary | direct-original-pages | PDF 128–138 §§8.1–8.3 |

## Competing Interpretations and Limitations

- $^{92}$Se 的转换系数由强度平衡推得，继承效率和未见分支的假设。是否符合 E2 要与误差和可替代多极性一起读，不能由最接近的 BrIcc 中心值固定全部级联性质。
- $^{94}$Se 的 $K$ 阻碍解释还依赖 $K$ 指认、寿命归一及 E1 参照强度。PDF 131 的算术歧义影响同类阻碍系统学比较。
- 附录 B 的在束谱注明摘自 S. Chen 等 Ref. [24]（DOI `10.1103/PhysRevC.95.041302`，书目 PDF 144）。该谱是比较数据，不能把重排进学位论文的图再计为新实验。
- 附录 A 的相对强度都使用同一参照峰（539 或 470 keV）。边际误差传播式未给出跨行协方差，不能按全部强度独立构建联合拟合。

## Extracted Pages

- PDF 1–17：学位、摘要、目录及卷首页。
- PDF 18–66：动机、核模型、SCCM 与 5DCH，γ 谱学和异能态。
- PDF 67–98：RIKEN 实验链、离子鉴别及 EURICA 校准、效率和符合。
- PDF 99–127：两核延迟谱、强度、半衰期、候选纲图。
- PDF 128–142：组态与形状讨论、结论、误差传播和在束对照。
- PDF 143–153：书目和研究成果目录。
