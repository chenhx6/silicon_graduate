---
type: source
title: "Nambudripad 1980 - Ho and Er nuclear orientation"
title_original: "Some Applications of Nuclear Orientation"
aliases: []
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: doctoral-thesis
reading_depth: read
authors: ["Narayanan Nambudripad"]
year: 1980
institution: "University of Oxford"
doi: "10.5287/ora-1avz18ke5"
canonical_source: "University of Oxford doctoral thesis, October 1980"
raw_file: raw/theses/gpt/query/20261119-international-nuclear-structure/W607040476.pdf
raw_sha256: 7829dad806acf37fa858c6b97872e30b62a3796cc6a5eeb7733725fde58ba66a
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/theses/gpt/query/20261119-international-nuclear-structure/manifest-acquisition-batch1.json
comparison_manifest_file: raw/papers/gpt/query/20261120-nambudripad-orientation-crosswalk/manifest.json
comparison_manifest_sha256: cb5678cb1aba7cc61c8bacc014f8d5475ec8cde3dcef5407a3e716cdb2d8381b
nuclei: ["166Ho", "166Er"]
tags: ["nuclear-orientation", "mixing-ratio", "band-mixing", "thesis"]
---

# Nambudripad 1980：¹⁶⁶ᵐHo 核取向与 ¹⁶⁶Er 混合比

## Bibliographic Record

Narayanan Nambudripad，University of Oxford 博士论文，1980 年 10 月，272 页。Oxford Research Archive 标识 `10.5287/ora-1avz18ke5`。下列定位为本地 PDF 页，因插图另页等原因与印刷页的差值不恒定。与 Allsop 等 `10.1098/rspa.1980.0100` 核对 HoVO₄ 摘要，核对表 7.1 所引 West 及 Krane 的书目身份。

## Scope and Reading Depth

核读 268/272 页的科研与书证范围，涵盖八章及书目。排除致谢 PDF 4–5、书目分隔页 PDF 262 和空白 PDF 272。PDF 234 虽无可提取文字，图版仍纳入覆盖。

## Summary

¹⁶⁶ᵐHo 的低温取向依赖已量温度和超精细场。衰变填充的 ¹⁶⁶Er 能级通过随取向变化的 γ 各向异性约束多极混合。受污染谱线、相近的拟合解和借用的参照系数应在摘录中保留。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| NAM-HO | 以已知多极性参照线拟合 ¹⁶⁶ᵐHo 的核磁偶极矩，论文给 \(3.60(6)\,\mu_N\)。核自旋温度可与冷指或晶格温度不同，分析使用样品条件及由 \(B_{\rm corr}\) 推得的超精细场。 | reported-calibration | direct-original-pages | 学位 PDF 164–184，印刷 §§6.3–6.7、表 6.1–6.3 |
| NAM-MAG | RF 磁化率给 \(T_N=4.0(2)\) mK，增强核磁矩的偶极–偶极模型给 4.8 mK。RF 数据在约 \(1.5\times10^{-2}\) T 出现 spin flop，各向异性分析的相应场约 \(1.2\times10^{-2}\) T。作者把低场多畴分布与晶体钉扎联系起来，场量的具体来源仍有不确定性。 | measured-and-interpreted-magnetic-order | direct-original-pages | 学位 PDF 107–112、121–125、154–161，印刷 §§4.3–4.5、5.10–5.12 |
| NAM-THERM | 单晶磁化率热弛豫受晶体与冷端边界热阻支配，难以直接给自旋–晶格弛豫时间。核制冷章的 HoVO₄–Cu 压片约达晶格温度 \(3.9(3)\) mK，约 \(30\,\mathrm{cm}^2\) 是由非理想热接触推得的有效面积。 | thermal-response-and-inference | direct-original-pages | 学位 PDF 99–102、122、245–246、254–260，印刷 §§4.3.2、8.4–8.7 |
| NAM-MIX | ¹⁶⁶Er 的 \(K=2\) γ 振动带到 \(K=0\) 基带分析继承上一章测定的取向参数。作者按式 3.5、3.8 用 \(\delta\) 作唯一自由参数拟合各向异性，注明相位用 Krane–Steffen。误差规则写为约化 \(\chi^2\) 增加 1。 | inferred-ratio-and-confidence-convention | direct-original-pages | 学位 PDF 191–201，印刷 §§7.2–7.3，式 3.4–3.8、表 7.1 |
| NAM-TAB | 表 7.1 报的是 \(\delta/E_\gamma\)，单位 \(\mathrm{MeV}^{-1}\)。810.3、529.8、830.6 keV 的本工作值依次为 \(-28(4)\)、\(-77^{+19}_{-34}\)、\(-25(4)\)，转换为无量纲 \(\delta\) 约 \(-22.7(3.2)\)、\(-40.8^{+10.1}_{-18.0}\)、\(-20.8(3.3)\)。 | reported-and-converted-ratios | direct-original-pages-and-arithmetic | 学位 PDF 201，印刷 124 页，表 7.1 |
| NAM-ROOT | 464.8 keV 表列大负值 \(-41^{+24}_{-\infty}\) 与小正值 \(+0.09(6)\,\mathrm{MeV}^{-1}\)。正文说明排除小正根采用带间线应主要为 E2 的结构预期。778.8 keV 被污染而未自行提取，691.2 keV 的污染约占 30%。 | multiple-solutions-and-contamination | direct-original-pages | 学位 PDF 200–201，印刷 123–124 页，表 7.1 |
| NAM-BANDS | 跨带 \(B(E2)\) 的 Mikhailov 分析读取已知支路、估计缺失的 \(3_\gamma^+\) 带内线，再比较拟合系数。\(B(M1)\) 的 Mikhailov 型比较中 \(\Delta K=1\) 曲线较符合数据，\(\Delta K=2\) 仍有依赖 \(g_K-g_R\) 符号的两条模型曲线。 | structure-interpretation-with-assumptions | direct-original-pages | 学位 PDF 202–214，印刷 §§7.4–7.6，表 7.2–7.4、图 7.9–7.11 |

## Competing Interpretations and Limitations

- 这里的 \(U_kF_k\) 是核取向角分布分析量。表的输入需要自旋温度、场与退取向系数。未找到这些 ¹⁶⁶Er 支路的同一测量 \(P\) 输入，暂作为核取向方法与多解的比较样本。
- 学位磁矩 \(3.60(6)\,\mu_N\) 与 Allsop 等期刊摘要 \(3.60(5)\,\mu_N\) 条件相符，误差按各版本保留。期刊对于 spin flop 仅在已获得摘要内核验；未把论文按独立重测计数。表 7.1 的 Ref. 2 是 West 1976（`10.1016/0375-9474(76)90449-8`），Ref. 8 是 Krane 1973（`10.1103/PhysRevC.8.1494`）。West 和学位对 465/530 keV 的混合比有差异，作者指出其取向系数相容并讨论拟合差别。对照文献未用摘要补填原表。
- 早期方法报告的约化 \(\chi^2\) 规则需按原文保存，区别于按总 \(\Delta\chi^2=1\) 给出区间。论文也区分平衡核自旋温度与晶格温度，关联 \(B_{\rm hyp}/T\) 指定的取向分布与在束高斯 \(\sigma/I\) 各自的物理条件。

## Extracted Pages

- PDF 1–3、6–85：身份、装置、温标、增强超精细哈密顿量、张量旋转和级联衰减。
- PDF 86–188：射频磁化率、核畴比较、磁矩及热接触。PDF 189–224：¹⁶⁶Er 各向异性与带混合，表 7.1 已目视。
- PDF 225–261、263–271：制冷、热接触、参考文献；PDF 234 装置图版已目视。出版关系限于书目与摘要。
