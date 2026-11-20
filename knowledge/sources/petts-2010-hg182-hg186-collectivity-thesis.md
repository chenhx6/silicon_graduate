---
type: source
title: "Petts 2010 - RDDS and Coulomb excitation in 182,186Hg"
title_original: "Shape Coexistence and Collectivity in Neutron-Deficient Mercury Isotopes"
aliases: []
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: doctoral-thesis
reading_depth: read
authors: ["Andrew Petts"]
year: 2010
institution: "University of Liverpool"
doi: "10.17638/00003073"
canonical_source: "University of Liverpool doctoral thesis, September 2010, repository record 3073"
raw_file: raw/theses/gpt/query/20261119-international-nuclear-structure/W574609453.pdf
raw_sha256: bb5b795cccd266d34412fde62bf2969fb2af0b8a16df1af97cf55060c9b34e45
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/theses/gpt/query/20261119-international-nuclear-structure/manifest-acquisition-batch1.json
nuclei: ["182Hg", "186Hg"]
tags: ["RDDS", "Coulomb-excitation", "E2", "shape-coexistence", "thesis"]
---

# Petts 2010：¹⁸²Hg 寿命与 ¹⁸²,¹⁸⁶Hg 库仑激发

## Bibliographic Record

Andrew Petts，利物浦大学博士论文，2010 年 9 月。原件 191 页，正文印刷页为 PDF 页减 20。

## Scope and Reading Depth

已核 178/191 页科研、书证和附录。另对照同实验的 Grahn 2009 寿命表、Bree 2014 结果及 Wrzosek-Lipska 等 2019 年完整库仑激发分析。实验事件和 GOSIA 输入卡另属复现范围。

## Summary

学位论文包含 JYFL 的反冲门控 \(\gamma\gamma\) RDDS 和 REX–ISOLDE 的库仑激发两类采集。前者约束跃迁强度，后者用多步产额和角度分组约束 E2 矩阵元。库仑激发拟合使用部分既有寿命资料，比较时须保留输入依赖。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| PET-TAU | ¹⁸²Hg 的 \(2_1^+,4_1^+,6_1^+,8_1^+,10_1^+\) 分别给平均寿命 41(3)、35.7(15)、8.2(5)、2.9(3)、1.2(3) ps。前两条下行 \(B(E2)\) 分别为 57(4)、264(11) W.u.。Grahn 等 PRC Table I 复用同一次 310 MeV ⁸⁸Sr + ⁹⁶Mo 反冲符合采集。 | measured-lifetimes-and-data-lineage | direct-original-pages | 学位 PDF 101、117，表 4.3；PRC 80, 014324 PDF 2、4，表 I |
| PET-RDDS | 反冲门下在直接馈入线的快慢峰全峰形开门，并分别处理 158° 与 134° 的衰变曲线。正文列 \(2^+\) 谱形，附录另列两个环下五条跃迁的谱形及面积。\(12^+\) 的谱峰附于资料，只有至 \(10^+\) 的寿命进入汇总。 | experimental-selection-and-sensitivity | direct-original-pages | 学位 PDF 101–117、171–191，图 4.3–4.11、表 4.1–4.3、A.1–A.10 |
| PET-COUL | 2008 年秋 REX–ISOLDE 以 2.85 MeV/u 的 Hg 束和 2 mg/cm² 的 ¹¹²Cd、¹¹⁴Cd 靶分别研究 ¹⁸²Hg、¹⁸⁶Hg。学位表 5.16 的 ¹⁸²Hg \(2_1^+\) 对角项为 \(-0.6(5)\) eb，[[doctoral-r1-g31-bree-2014-prl112-coulex-182-188hg]] 给 \(-0.04^{+1.30}_{-1.40}\) eb。2019 年表 1 将这两组镉靶运行列入 2008 年采集，另列 2007 年 Sn、Ag 靶运行。按重合的采集系列处理，束流强度及最终筛选口径分别保留。 | geometry-and-versioned-matrix-elements | direct-original-pages | 学位 PDF 119–120、142，表 5.1、5.16；Bree PRL p. 162701-3 表 I；EPJA PDF 2–4，表 1 |
| PET-FIT | MINIBALL 源定标后按粒子角度分组，采用同靶 Cd 产额归一并在 GOSIA 中积分有限靶厚、角度和效率。学位 ¹⁸²Hg 拟合纳入 \(2_1^+,4_1^+,6_1^+\) 寿命。图解交叉检查省去寿命项，但将其它显著耦合留在原拟合值，因此是条件对照。 | calibration-and-fit-dependency | direct-original-pages | 学位 PDF 59–63、120–127、138–145，表 5.3–5.4、5.13–5.17 |
| PET-186 | 学位表 5.21 的 ¹⁸⁶Hg \(2_1^+\) 对角项为 \(+2.1(8)\) eb、\(Q_s=+1.7(5)\) eb，表 5.22 给 \(\beta_2=-0.13(2)\)。跨页正文称 prolate，与该 \(\beta_2\) 符号及摘要、结论的 oblate 相冲突。2014 和 2019 两份期刊均未列 ¹⁸⁶Hg 的该对角项。 | reported-matrix-element-and-version-boundary | direct-original-pages | 学位 PDF 7、149–151、160，表 5.21–5.22；Bree PRL p. 162701-3 表 I；EPJA PDF 12，表 7 |
| PET-REANALYSIS | 2019 年从原实验输出重分析 ¹⁸²,¹⁸⁴Hg，更新 \(2_2^+\to2_1^+\) 总内转换系数和 γ 分支，并计入参数相关性。表 7 保留跃迁矩阵元与若干相位不变的干涉约束；作者因 E0 约束及符号敏感性，除 ¹⁸⁸Hg 外省列这些 \(2^+\) 对角项，亦未据此给出 \(0^+\) 的三次四极不变量。 | published-analysis-update | direct-original-pages | EPJA PDF 2、11–13，表 6–7、图 14 |

## Competing Interpretations and Limitations

- JYFL 与 REX–ISOLDE 属不同采集。GOSIA 纳入寿命后，所得 \(B(E2)\) 与寿命表的相合仍带该输入依赖。2019 年的运行表与学位论文的镉靶条件一致，所列束流强度不同，例如 ¹⁸²Hg 为 \(3.5\times10^3\) 与 \(4.9\times10^3\) pps。原始事件重合比例未核。学位 PDF 119–120、141；EPJA PDF 4、11。
- \(2_1^+\to0_1^+\) 的 57(4) W.u. 显著小于 \(4_1^+\to2_1^+\) 的 264(11) W.u.。摘要中把较强集体性的范围印为 \(I^\pi\leq4^+\)，按表 4.3 及讨论理解其随自旋的增幅。从 \(B(E2)\) 得到的 \(|Q_t|\) 是幅值，形状解释还需要重取向对角项、混合模型及其不确定度。学位 PDF 7、117、153–156。
- 学位表 6.2 按假设的 \(\delta^2\) 分解 ¹⁸²Hg \(2_2^+\to2_1^+\) 的 E0/M1/E2 成分。2019 年采用来自 ²⁰²Pb 的示例值 \(\delta(E2/M1)=1.85\)，对 0.5–5 作 GOSIA 敏感性扫描；\(\delta<1\) 时与 \(2_2^+\) 相关的矩阵元变化较明显。两项分析所用的内转换/产额输入及 \(\delta\) 条件应按各自版本保存。学位 PDF 157–160，表 6.2；EPJA PDF 13，图 14。
- 学位式 2.66、2.69 将速度与按 \(t\) 写出的导数相乘。由 \(d=vt\)，DDCM 应使用时间斜率 \(dQ/dt\) 或速度乘距离斜率 \(v\,dQ/dd\)。这里记录印刷量纲问题；NAPATAU 的实际实现未复现。学位 PDF 66–68、110–111。参见 [[watkins-2011-au175-pt174-pt175-rdds-thesis]]。

## Extracted Pages

- 学位 PDF 1、7、11–13、15–41：身份、摘要、导航及 Hg 形状共存背景。
- 学位 PDF 43–117、119–151、153–161：库仑激发和 RDDS 理论、设施和触发、谱形与产额、GOSIA 条件和形状讨论。
- 学位 PDF 163–191：参考文献及 RDDS 谱形/峰面积附录。献词、题词、致谢和分隔页 PDF 2–6、8–10、14、42、118、152、162 留档。
- ¹⁸⁰,¹⁸²Hg 的 Grahn 等 PRC 80, 014324（2009）出版原件见 `raw/papers/gpt/query/20261120-petts-hg182-rdds-crosswalk/manifest.json`。Bree 2014 原件随 [[doctoral-r1-g31-bree-2014-prl112-coulex-182-188hg]]。Wrzosek-Lipska 等 EPJA 55, 130（2019），`10.1140/epja/i2019-12815-2`，见 `raw/papers/gpt/query/20261120-petts-coulex-updated-crosswalk/manifest.json`，重点复核 PDF 2–4、11–13。
