---
type: source
title: "Thomas et al. 2016：96,98Mo核结构、形状共存与混合对称态（Nucl. Phys. A 出版全文精读）"
aliases: ["Thomas 2016 NPA 96,98Mo", "NPA 947 203", "10.1016/j.nuclphysa.2015.12.010"]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Nuclear structure of 96,98Mo: Shape coexistence and mixed-symmetry states"
authors: ["T. Thomas", "V. Werner", "J. Jolie", "K. Nomura", "T. Ahn", "N. Cooper", "H. Duckwitz", "A. Fitzler", "C. Fransen", "A. Gade", "M. Hinton", "G. Ilie", "K. A. Jessen", "A. Linnemann", "P. Petkov", "N. Pietralla", "D. Radeck"]
journal: Nuclear Physics A
year: 2016
volume: 947
pages: 203-233
doi: 10.1016/j.nuclphysa.2015.12.010
canonical_source: "https://doi.org/10.1016/j.nuclphysa.2015.12.010"
citation_key: ""
raw_file: "raw/papers/gpt/query/20261107-continuation-G17/thomas-2016-96-98mo-coexistence.xml"
raw_sha256: "f948e4ffd6292f3b4c807d2ae90ab410c0b4502dab73e35027cc55335a144a0d"
archive_required: true
nuclei: ["98mo", "96mo"]
tags: ["dsam", "level-lifetimes", "shape-coexistence", "mixed-symmetry", "98mo"]
---

# Thomas et al. 2016：98Mo 能级寿命、DSAM 分析与负宇称态核查

## Bibliographic Record

T. Thomas et al., *Nuclear structure of 96,98Mo: Shape coexistence and mixed-symmetry states*, Nuclear Physics A **947** (2016) 203–233. DOI: 10.1016/j.nuclphysa.2015.12.010.
底本为通过 Elsevier ScienceDirect API 获取的出版全文 XML（1,236,957 字节，SHA-256: `f948e4ffd6292f3b4c807d2ae90ab410c0b4502dab73e35027cc55335a144a0d`）及出版底本 PDF（5,107,501 字节，SHA-256: `d226d134cd5978436b64cc7fe362dd4ea7e3f66a8d7055a5dca7dc8e12a2c6c4`），归档于 `raw/papers/gpt/query/20261107-continuation-G17/`。

## Scope and Reading Depth

### Covered Scope
- 针对 98Mo 激发态寿命、DSAM 多普勒线形分析及能级衰变支路开展全文精读。
- 实验装置：耶鲁大学 WNSL 加速器，16 MeV $\alpha + {}^{96}\text{Zr}$（厚度 $1.25\text{ mg/cm}^2$ 富集靶），YRAST Ball 阵列（10 台康普顿抑制 HPGe Clover 探测器）。
- 重点核验 Table 2（98Mo 能级能量、初态自旋宇称、寿命 $\tau$、跃迁能量、相对光子分支比、混合比 $\delta$ 与末态能量）。
- 重点核验 Table 6（98Mo 混合对称态与更高 $2^+$ 态的理论与实验 $B(M1)$ 与 $B(E2)$ 强度）。
- 重点核验第 2.2 节对 2620.56(17) keV $5^-$ 与 3095.74(19) keV $7^-$ 态的观测与讨论。

### Not Covered
- 本实验入射能量为 16 MeV，角动量输入有限，未观测到高自旋 $9^-$ 态（3655.7 keV 或 3767.5 keV）。
- 实验未对负宇称态提取出可用多普勒线形，未报告 $5^-$ 或 $7^-$ 态的绝对寿命或有效寿命上限。

## Key Results

| ID | 全文核验事实 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| TH16-F1 | 2620.56(17) keV 态指认为 $5^-$，观测到 603.25(17) keV（$I_\gamma=63.3(12)$，$\delta=-0.08(11)$，退激至 2017.36 keV $3^-$）与 1110.75(16) keV（$I_\gamma=100$，$\delta=-0.05(10)$，退激至 1509.74 keV $4^+$）；其寿命列 $\tau$ 明确为空白（未给出任何测量值或上下界）。 | experimental-fact | direct | Table 2, p.211 | false |
| TH16-F2 | 3095.74(19) keV 态指认为 $7^-$，观测到 475.23(17) keV（$I_\gamma=100$，$\delta=+0.01(3)$，退激至 2620.56 keV $5^-$）与 752.41(16) keV（$I_\gamma=81.2(16)$，$\delta=-0.01(4)$，退激至 2343.26 keV $6^+$）；其寿命列 $\tau$ 明确为空白。正文第 2.2 节讨论了该态 752 keV 分支与 $\beta$ 衰变文献的差异，但明确未提取寿命。 | experimental-fact | direct | Table 2, p.211; Sec. 2.2 | false |
| TH16-F3 | 2017.36(16) keV $3^-$ 态的寿命列标注为 $\tau = 93.8(101)\text{ ps}$（带文献引用星号 **，对应文献半衰期 $T_{1/2} = 65(7)\text{ ps}$），来自历史库仑激发/衰变文献，非本次新测。 | evaluated-fact | direct | Table 2, p.211 | false |
| TH16-F4 | 本次 DSAM 多普勒线形分析测出有效寿命上限（$\tau_{\text{eff}} < 0.1\sim 0.6\text{ ps}$）的能级全部为正宇称态（包括 2206 keV $2^+_4$、2333 keV $2^+_5$、2525 keV $2^+$、2700 keV $2^+$、2871 keV $2^+,3$、2905 keV $4^+$、2916 keV $2^+$、2976 keV $4^+$、3050 keV $4^+$、3228 keV $5^+,6$ 等），无任何一条负宇称带内寿命。 | experimental-fact | direct | Table 2, Table 6 | false |

## Competing Interpretations and Scientific Impact

本实验是 98Mo 领域极少数采用现代 Clover 探测器阵列与 DSAM 线形拟合的高精度在束 $\gamma$ 谱学工作。实验核验确证：
1. 即便在灵敏度达到亚皮秒量级（$\tau_{\text{eff}} < 0.2\text{ ps}$）的专用 DSAM 实验中，依然未能对 2620 keV $5^-$ 与 3095 keV $7^-$ 提取寿命；
2. 这反映出 98Mo 负宇称态的能级寿命可能长于薄靶 DSAM 的有效阻止时间窗口（即处于皮秒或更长区间），或者受限于级联馈送和统计量无法解出线形；但在本实验未报告寿命的前提下，不应断言历史上完全不存在其它测量；
3. 在缺乏绝对寿命前提下，无法将 98Mo $5^-$ 或 $7^-$ 的相对比值单独归因于八极跃迁矩阵元的绝对增强；不过同母态 $E1/E3$ 强度之商可在消去 $B(E2)$ 分母的前提下提供独立于寿命的相对结构约束（参见 [[mo98-ru100-same-parent-e1-e3-constraints-20261107]]）。


## Summary

本页记录该原件实际提供的实验/模型信息与读取边界；核心数据/公式沿用上文原表locator，不作为新实验或作者代码复现。


## Competing Interpretations and Limitations

模型参数和解释不等于实验直接测量；原文未报告不等于严格为零或全球不存在。局部比较不能排除全部模型族，适用条件与缺失响应沿用本页记录。


## Extracted Pages

实际读取的PDF/出版页、XML原文段及表号见Scope和逐项locator；全文文件可用不代表全部图点/转引原件或生产实现已核。
