---
type: source
title: "Chen & Singh 2020：A=98核数据评价（NDS 164, 1 评价正文精读与能级寿命核查）"
aliases: ["Chen 2020 NDS A=98", "NDS 164 1", "10.1016/j.nds.2020.01.001"]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Nuclear Data Sheets for A=98"
authors: ["Jun Chen", "Balraj Singh"]
journal: Nuclear Data Sheets
year: 2020
volume: 164
pages: 1-364
doi: 10.1016/j.nds.2020.01.001
canonical_source: "https://doi.org/10.1016/j.nds.2020.01.001"
citation_key: ""
raw_file: "raw/papers/gpt/query/20261107-continuation-G17/nds-2020-chen-singh-98mo-adopted.pdf"
raw_sha256: "f98dc0ebd7a111083492fd25710268093d37c40bc45b33b1507704428d8c9bf6"
archive_required: true
nuclei: ["98mo", "98nb", "98zr"]
tags: ["nuclear-data-evaluation", "ensdf", "adopted-levels", "lifetimes", "98mo"]
---

# Chen & Singh 2020：98Mo 评价能级寿命与跃迁几率全量核查

## Bibliographic Record

Jun Chen, Balraj Singh, *Nuclear Data Sheets for A=98*, Nuclear Data Sheets **164** (2020) 1–364. DOI: 10.1016/j.nds.2020.01.001.
文献截止日期为 2020-02-15，含 2021-05-06 修改批注（主要涉及 787.4 keV $2^+ \to 734.8\text{ keV } 0^+$ 的 $B(E2)$ 修正及 2002Zi06 库仑激发分析）。
底本为直接从 NNDC ENSDF 服务器下载的官方 Adopted Levels and Gammas 出版 PDF（51 物理页，661,175 字节，SHA-256: `f98dc0ebd7a111083492fd25710268093d37c40bc45b33b1507704428d8c9bf6`），归档于 `raw/papers/gpt/query/20261107-continuation-G17/`。

## Scope and Reading Depth

### Covered Scope
- 51 物理页全部 Adopted Levels, Gammas 正文，以及库仑激发、$(\alpha, 2n\gamma)$、$(n, n'\gamma)$、$(^{30}\text{Si}, X\gamma)$ 与 $^{98}\text{Nb}$ $\beta^-$ 衰变等关联反应数据集。
- 逐级排查 98Mo 所有已知负宇称激发态（尤其是 $3^-$, $5^-$, $7^-$, $9^-$）的半衰期 $T_{1/2}$、跃迁多极性、分支比与绝对跃迁强度 $B(E\lambda)$。
- 重点核验能级：2017.53(3) keV $3^-_1$、2620.78(5) keV $5^-_1$、3096.26(16) keV $(7^-_1)$、3656.7(3) keV $(9^-_1)$ 与 3768.7(6) keV $(9^-_2)$。

### Not Covered
- 2021 年 5 月之后的最新在束实验（如 Karmakar 2026）；ENSDF 尚未收录 2026 年新放置的两条 $E3$ 跃迁（1833.3 keV 与 1585.8 keV）。

## Key Results

| ID | 评价核验事实 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CS20-F1 | 2017.53(3) keV $3^-_1$ 态是全核唯一具有推荐绝对寿命的负宇称态，Adopted $T_{1/2} = 65(7)\text{ ps}$（对应平均寿命 $\tau = 93.8(101)\text{ ps}$）；其基态退激跃迁 2017.46(10) keV 的向下跃迁几率在 Adopted Gammas 中评价为 $B(E3\downarrow) = 30^{+7}_{-5}\text{ W.u.}$（向上基态激发 $B(E3\uparrow; 0^+_1 \to 3^-_1)$ 乘自旋因子 $2J+1=7$，量纲值为 $7 \times B(E3\downarrow)$）。原 note 中提及的“库仑激发数据集 37(6) W.u.”及所谓 coulex.pdf 未在本次底本中见及，予以删除修正。该寿命属于 $3^-_1$ 本征态，绝对不可转移至更高自旋负宇称态。 | evaluated-fact | direct | p.3, p.15 | false |
| CS20-F2 | 2620.78(5) keV $5^-_1$ 态：Adopted Levels 中半衰期 $T_{1/2}$ 明确为空白（未给出任何实验寿命数值、上限或下限）。退激 $\gamma$ 仅包含 603.28(12) keV（相对光子分支 63.3(12)，(E2)）与 1110.77(7) keV（分支 100.0(23)，(E1)）。 | evaluated-fact | direct | p.4, p.20 | false |
| CS20-F3 | 3096.26(16) keV $(7^-_1)$ 态：Adopted Levels 中半衰期 $T_{1/2}$ 明确为空白。退激 $\gamma$ 仅包含 241.7(5) keV（$I_\gamma=11(5)$）、475.6(4) keV（分支 100(12)，(E2)）与 752.77(23) keV（分支 80.9(16)，(E1)）。 | evaluated-fact | direct | p.5, pp.24-25 | false |
| CS20-F4 | 3656.7(3) keV $(9^-_1)$ 态（Band 2）：Adopted Levels 中半衰期 $T_{1/2}$ 明确为空白。退激 $\gamma$ 仅包含 385.1(5) keV（$I_\gamma=69(14)$）、560.5(5) keV（分支 100(12)）与 802.6(5) keV（分支 30(5)）。 | evaluated-fact | direct | p.7, p.28 | false |
| CS20-F5 | 3768.7(6) keV $(9^-_2)$ 态（Band 3）：半衰期 $T_{1/2}$ 明确为空白，退激仅观测到 672.4(5) keV（分支 100）。必须与 Band 2 的 3656.7 keV $9^-_1$ 严格区分，两者属于不同带结构。 | evaluated-fact | direct | p.8, p.28 | false |
| CS20-F6 | 98Mo 在 2 MeV 以上具有皮秒级寿命或上限测量的能级全部为偶宇称态（如 2206.61 keV $2^+$、2333.18 keV $2^+$、2343.62 keV $6^+$、2525.8 keV $2^+$、2700.68 keV $2^+$、2871.1 keV $2,3$、2905.2 keV $4^+$、2915.8 keV $2^+$、2976.89 keV $4^+$、3050.92 keV $4^+$、3229.17 keV $(4^+)$、3557.0 keV $(4^+)$）；负宇称带内无任何测量记录。 | evaluated-fact | direct | pp.3-7 | false |

## Competing Interpretations and Scientific Impact

在当前 NDS 2020 评价底本收录范围内，98Mo 的 $5^-_1, 7^-_1, 9^-_1$ 负宇称能级在 Adopted Levels 中未给出实验半衰期或绝对跃迁几率数据：
1. 现有关于 98Mo 负宇称带衰变的定量实验数据主要为相对光子分支比与部分多极混合比；
2. 在缺乏同一能级的绝对衰变总宽度 $\Gamma_{\text{tot}} = \hbar/\tau$ 时，无法独立标定绝对 $B(E2)$、$B(E1)$ 与 $B(E3)$ 的绝对尺度；不过同母态 $E1/E3$ 强度之商可在消去 $B(E2)$ 分母的前提下提供独立于寿命的相对约束（参见 [[mo98-ru100-same-parent-e1-e3-constraints-20261107]]）。


## Summary

本页记录该原件实际提供的实验/模型信息与读取边界；核心数据/公式沿用上文原表locator，不作为新实验或作者代码复现。


## Competing Interpretations and Limitations

模型参数和解释不等于实验直接测量；原文未报告不等于严格为零或全球不存在。局部比较不能排除全部模型族，适用条件与缺失响应沿用本页记录。


## Extracted Pages

实际读取的PDF/出版页、XML原文段及表号见Scope和逐项locator；全文文件可用不代表全部图点/转引原件或生产实现已核。
