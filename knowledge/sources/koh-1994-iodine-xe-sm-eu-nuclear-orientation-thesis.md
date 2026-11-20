---
type: source
title: "Koh 1994 - Iodine decay orientation and Sm/Eu particle rotor"
title_original: "Nuclear Structure Studies involving polarised Iodine, Samarium and Europium: Experimental Techniques and Theoretical Models"
aliases: []
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: doctoral-thesis
reading_depth: read
authors: ["Young Koh"]
year: 1994
institution: "University of Oxford"
doi: "10.5287/ora-6gozne9zz"
canonical_source: "University of Oxford DPhil thesis, Michaelmas Term 1994"
raw_file: raw/theses/gpt/query/20261119-international-nuclear-structure/W7116884503.pdf
raw_sha256: 48d4afd57af0a979c008e9c64575cc4342b8587b7375c0b8db3793374f2d1a50
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/theses/gpt/query/20261119-international-nuclear-structure/manifest-acquisition-batch1.json
comparison_manifest_file: raw/papers/gpt/query/20261120-koh-iodine-orientation-crosswalk/manifest.json
comparison_manifest_sha256: 03850b8f2bb8f5006b460321e1594298a41e71e16545b128a04811eebaa3cf48
nuclei: ["133I", "135I", "133Xe", "135Xe", "138Eu", "139Sm", "141Sm", "143Sm"]
tags: ["nuclear-orientation", "NMR-ON", "mixing-ratio", "triaxial-particle-rotor"]
---

# Koh 1994：碘衰变取向谱与 Sm/Eu 粒子转子计算

## Bibliographic Record

Young Koh，Oxford DPhil，Michaelmas Term 1994，189 页。后续 ¹³⁵I 的 White 等 NMR/ON 论文为 *Nucl. Phys. A* **644**, 277–288（1998），`10.1016/S0375-9474(98)00597-1`。此次将该论文核至书目，其磁矩数值回链至 2008 年 ENSDF 评价的原始归因。

## Scope and Reading Depth

覆盖 185/189 页科研及书证范围。PDF 2、4–5、189 为献辞、致谢或空白。正文印刷页 = PDF 页减 8。目视核对关键原表与 NMR 页，表录保留原本分支和数值差异。

## Summary

铁中取向的 ¹³³I、¹³⁵I β 衰变布居 Xe 激发态，轴向与赤道探测给 \(\gamma\) 各向异性。拟合区分晶格位点分数、超精细相互作用、级联退取向和 \(\gamma\) 混合比。Sm/Eu 章另将外来磁矩、电四极矩和能级与粒子三轴转子模型比较。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| KOH-SET | 铁箔中测轴向及三组赤道 Ge(Li) 单谱，取向场 0.7 T，最低约 20 mK。暖谱用于计数归一，另作死时间和半衰期修正。\(Q_2=0.97(1),Q_4=0.89(1)\) 是有限立体角因子。\(U_kA_k\) 的反演依赖晶格好位点分数 \(f\)、核取向和探测几何。 | measurement-and-calibration | direct-original-pages | 学位 PDF 66–73，式 3.2–3.15、§4.2 |
| KOH-XE133 | 529.9 keV 的 \((U_2A_2,U_4A_4)=(-0.76(3),0.27(2))\)，取主要 Gamow–Teller 馈入的 \(U_2=0.874,U_4=0.580\)，给 \(\delta(E2/M1)=2.4(2)\)。作者用四阶项排除另根。1298.2 keV 的二阶反演候选为 4.1(3) 与 0.59(2)，四阶项支持后者。706.6 keV 小根正文给 0.46(2)，表 4.1 给 0.46(3)，两处误差分开保留。 | selected-roots-and-source-discrepancy | direct-original-pages | 学位 PDF 74–76、85，§4.3.2、表 4.1 |
| KOH-HF | ¹³³I 的静态拟合给 \(f\approx79(3)\%\)、\(\lvert B_{\rm hf}\rvert=109.2(1.4)\) T。NMR/ON 以 529 keV 为标记，峰心 712.25(25) MHz，FWHM 2.25 MHz。采用 \(\mu=2.856(5)\,\mu_N\) 和零 Knight shift 得 \(114.51(24)\) T。约 4% 峰处破坏、34(6)% 积分破坏和静态 \(f\) 是不同口径。 | two-method-field-comparison | direct-original-pages | 学位 PDF 74、77–78、86、104–105，式 4.1–4.2、图 4.4 |
| KOH-I135 | 两份 ¹³⁵I 植入样给 \(f_1\approx74(3)\%\)、\(f_2\approx86(3)\%\)，联合拟合给 \(\lvert\mu B_{\rm hf}\rvert=290.6(23)\,\mu_N\,\mathrm T\)。取场 114.4(2) 或 109.2(1.4) T，论文分别给 \(\mu=2.54(2)\) 或 \(2.66(6)\,\mu_N\)。后来的 ENSDF 采用 \(\mu=(+)2.940(2)\,\mu_N\)，归于 1998Wh04 NMR/ON，正号来自同位素系统学。 | conditional-moment-and-evaluation | direct-original-pages-and-evaluation | 学位 PDF 79、90–92，图 4.6–4.8；ENSDF ¹³⁵I PDF 1 |
| KOH-XE135 | 表 4.2 给 1260.4 keV 的 \(\delta=0.72(2)\)。1457.6 keV 保留 \(-0.25(2),-1.7(1)\)，546.6 keV 保留 \(-0.2(1),+0.14(9)\)。1124.0 keV 的 \(A_4\) 与假定纯 GT 馈入下的物理范围不相容，只保留「大正值」和馈入假设冲突。 | retained-roots-and-response-failure | direct-original-pages | 学位 PDF 87–88、100–104、108，§4.5、表 4.2 |
| KOH-ROTOR | 奇 A 计算以刚性三轴核芯并分别处理正负宇称，变动 \(\epsilon_2,\gamma\) 和 Coriolis 衰减。¹⁴³Sm 的磁矩对负 \(\epsilon_2\) 时的 \(\gamma\) 变化不敏感，四极矩误差也限制识别。¹³⁸Eu 对残余 p–n 力有敏感性，约 \(\epsilon_2=0.27,\gamma=25^\circ\) 时的 \(7^+\) 是相对 \(6^-\) 的候选解释。 | model-conditioned-interpretation | direct-original-pages | 学位 PDF 149–154、167–174，表 6.1、6.5–6.6，图 6.12–6.15 |

## Competing Interpretations and Limitations

- \(A_4\) 可额外限制由 \(A_2\) 得到的混合比解，仍继承 \(U_4\) 的馈入假设。该处的 \(Q_k\) 为立体角修正，实验用对光子偏振不敏感的探测计数，不能将 \(Q_k\) 或 \(W(0)/W(90^\circ)\) 作为线偏振 \(P\) 或 DCO 输入。
- NMR 与静态拟合约束的是不同观测量。取向温度、不同晶格占位和退取向假设会改变静态 \(\mu B_{\rm hf}\)；共振分析保留所用参考磁矩和 Knight shift。White 1998 的实验全文和逐项系统误差尚待查证。
- 表 6.6 给组态相关的核芯参数。原文以 \(\epsilon_2\) 正负区别长扁分支，在比较展宽或其他 \(\gamma\) 约定前须保存这一符号。以刚性核芯分别拟合不同奇粒子组态所得参数可诊断形变敏感性，不能据此直接测出核芯的形变动力学。

## Extracted Pages

- PDF 1、3、6–41：身份、目录、统计张量、衰变退取向与超精细相互作用。
- PDF 42–113：稀释制冷、温标、谱分析、两个碘同位素及引文。目视核对 PDF 78–79、85、108。
- PDF 114–188：集体和单粒子模型、Sm/Eu 的组态计算、参考文献与四则附录。表 6.6 已目视。
