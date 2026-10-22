---
type: source
title: "Ciemała 2020：16C/20O 的寿命—能量联合线形分析"
aliases: [Ciemała 20O 150 fs, 16C conditional lifetime estimate]
created: 2026-10-14
updated: 2026-10-14
status: ai-draft
review_status: unreviewed
source_type: experimental-paper-with-theory-comparison
reading_depth: deep-read
title_original: "Testing ab initio nuclear structure in neutron-rich nuclei: Lifetime measurements of second 2+ state in 16C and 20O"
authors: [M. Ciemała, S. Ziliani, F. C. L. Crespi, S. Leoni, B. Fornal, A. Maj]
author_list_scope: first-six-of-public-copy
journal: Physical Review C
year: 2020
volume: 101
pages: 021303
doi: 10.1103/PhysRevC.101.021303
data_version: arXiv-2002.04814v1-main-seven-pages
canonical_source: "https://doi.org/10.1103/PhysRevC.101.021303"
citation_key:
raw_file: "raw/papers/gpt/day13/ciemala-2020-c16-o20-lifetimes.pdf"
raw_sha256: "b3d93fffb158ac68f7b99d627fe81fe9588dbf316d9f6eea92eb5cfcc1af2962"
raw_storage_status: reserved-unpopulated-public-preprint-only
external_pdf_url: "https://arxiv.org/pdf/2002.04814v1"
nuclei: [16c, 18o, 19o, 20o]
methods: [doppler-correction, dsam, gamma-ray-tracking, velocity-reconstruction]
tags: [agata, vamos, paris, femtosecond-lifetime, energy-lifetime-covariance, shared-data]
---

# 初始速度重建与联合线形拟合

## Bibliographic Record

M. Ciemała 等，Physical Review C **101**, 021303 (2020)，DOI 如上。Crossref 核验题名、首作者、卷与发表日期 2020-02-27；读取 arXiv:2002.04814v1，正文标日期 2020-02-19。出版记录与所读版本分别保留，不假定两份字节一致。

`raw_file` 是未填充的保留位置。公开副本实际位于 `tmp/day13/reopened/ciemala-2020-c16-o20-lifetimes.pdf`，七页，SHA-256 如上；未修改 raw。与 [[ciemala-2019-20o-dsam-analysis-status]]、[[ziliani-2019-agata-calibration-controls]] 的 July 2017 数据是同一实验谱系。

## Scope and Reading Depth

- Covered scope：七页正文主线、实验/重建/联合拟合、参考态、16C 条件结果及模型比较；Fig.3 的二维 χ² 与图注已视觉核验。
- Not covered：生产事件、代码/模板、完整协方差、χ² 数值网格、后续方法篇全文与参考文献全文。source 的最终测量报告不意味着本任务做了实验重拟合。

## Paper Question and Scientific Motivation

在直接转移和深非弹性过程共同产生宽反冲速度分布时，能否利用精确 γ 位置与离子末速度信息测到 tens-to-hundreds fs 寿命，并比较电磁跃迁而不只比较核能量。

## Method and Design Logic

从每一目标态对应的 VAMOS 速度—角度分布出发，包含谱仪响应、选定态反应运动学、靶深度随机发生、停止与 straggling，迭代重建靶内初始速度分布。随后模拟发射时速度和 γ 方向；最后同时拟合寿命与静止 γ 能量，并同时利用三角区的线形。

## Key Evidence and Reasoning Chain

末速度能约束靶后反冲，但短寿命 γ 可在靶内较快时发射。因此用末速度校正后的尾部并非必然校准失效；其寿命解释依赖初速度、能损/深度与响应。已知短态出现局部 χ² minimum，长态产生延伸 valley，二者验证不同的敏感区。

## Summary

本文报告 20O 的 2+2 总寿命 `150(+80/−30) fs` 与共同最优能量 `2394.6±1.0 keV`。16C 结果是能量条件下的寿命估计；不升级为无条件寿命测量。本文及 2019 准备报告不能多计独立实验；[[zanon-2023-o20-high-precision]] 才是另一反应/靶/入口测量的比较。

## Experimental or Theoretical Setup

18O 126 MeV 入射 181Ta 6.64 mg/cm²，靶中心约 116 MeV；AGATA 31 HPGe、PARIS/LaBr3 与 VAMOS++。VAMOS 轴相对束流45°、接受±6°；AGATA 相对 VAMOS 轴覆盖115°–175°，拟合角区按 γ 与反冲方向120°–140°、140°–160°、160°–180°，不要混用束流轴与离子轴。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CI20-1 | 18O126MeV+Ta6.64mg/cm²，靶中心约116MeV，VAMOS/AGATA/PARIS，直接与耗散过程共同布居；对应2017实验谱系。 | experimental-fact | direct | PDF p.3, setup; Figs.1–2; Ref.49 and 2019 reports | true |
| CI20-2 | Fig.1黑线为state-conditioned末速度，红线为模拟末速度、插图蓝虚线为重建初速度；16C耗散分量约32%。重建初速度不等同单事件直接测量。 | experimental-criterion | direct | PDF p.3, Fig.1/caption and paragraphs | true |
| CI20-3 | 三步MC含末速度角分布、谱仪响应、选态运动学、随机reactiondepth、stopping/straggling；τ与Eγ在三角区共同χ²拟合。 | experimental-criterion | direct | PDF pp.3–4, three-step procedure | true |
| CI20-4 | 長τ>1ps的1375/2371keV19O、1674keV20O与1762keV16C线相对窄；短τ线有尾/宽化，作者归因靶内停止过程中的发射。 | experimental-fact | direct | PDF p.3, Fig.2 discussion | true |
| CI20-5 | 19O2779线最佳τ140(+50/−40)fs、E2779.0(+1.0/−.8)keV，与引用92(19)fs比较；2371线为E2370.6(+.5/−.3)keV的延伸valley，没有局部τminimum。 | experimental-fact | direct | PDF p.4; p.5 Fig.3(a–f)/caption | true |
| CI20-6 | 20O2+2总寿命150(+80/−30)fs、联合最优E2394.6±1.0keV；本实验branch79(5)%给2+2→2+1 partial寿命190(+102/−40)fs。 | experimental-fact | direct | PDF p.4, 20O paragraph; p.5 Fig.3(g–i) | true |
| CI20-7 | 图中solid白轮廓为作者1σ区域；仅用frontsegment约20mm位置时轮廓变宽，原tracking precision<4mm。不能从此图恢复实际χ²grid/Σ。 | experimental-criterion | direct | PDF p.4, position discussion; p.5 Fig.3/caption | true |
| CI20-8 | 16C统计限制使角度合并，Eγ<2216keV时灵敏度很有限；Eγ>2216keV时提示τ<180fs；引用E2217(2)keV后该scenario概率78%。 | experimental-fact | direct | PDF p.4, 16C paragraph; p.5 Fig.3(j–k) | true |
| CI20-9 | MBPT含NN+3N时20O partialτ275fs；VS-IMSRG EM1.8/2.0给249fs，B(M1).0166μN²/B(E2).0684e²fm⁴；不是新的实测B。 | model-result | direct | PDF pp.4–5, model discussion; p.6 Fig.4 | true |
| CI20-10 | 作者认为与NN+3N预测吻合、寿命对结构敏感；IMSRG(2)、有效算符与未包含mesonexchange currents等限制保留。 | author-interpretation | direct | PDF pp.5–6, discussion/conclusion | true |

## Nuclear Structure Information

2+2→2+1 的总寿命、部分寿命和 branching 分开。16C 的 energy-conditioned limit 不能当20O测量的独立复现，也不能以不存在局部minimum的long19O线给一个精确寿命。

## Authors' Interpretation

参考态结果验证其MC方法，20O与16C结果支持比较含三体力的计算。该解释按本文处理保存；2023独立测量带来新的数值张力，不能反写本文为已经解决该差异。

## Model Results

MBPT、VS-IMSRG与NCSM使用不同many-body/算符截断。模型partialτ与实验totalτ须先匹配branch和γ能量再比较；同一个模型的能量、B与寿命也不构成独立三份证据。

## Competing Interpretations and Limitations

- 能量—寿命二维轮廓直接反驳以独立一维误差简单拼接全部约束；16C尤其显示能量条件决定结论。
- 初速度重建、未观测feeding、stopping/depth与响应可能改变线形；本文的两个19O controls不自动证明每个20O nuisance已消除。
- 未取得本文实际χ² definition/grid、完整systematic packet与逐gatecode，不给差异的精确Gaussian显著性，不做 pooledτ。
- 2019/2020同谱系重复引用不增加独立experiment；2023独立采集仍可能共享仪器方法与外部stopping参考，具体数值covariance须按packet核验。

## Analytical Reconstruction

| ID | 审核项 | Agent判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| CI20-AR1 | stage身份 | 末速度是测量，初速度是state-conditioned重建，发射速度是transport内量。三者不能只因都名为velocity合并。 | CI20-2/3/4 | unreviewed |
| CI20-AR2 | precision与validation | tracking使轮廓更小；同数据重处理不是独立寿命实验。 | CI20-5/7 | unreviewed |
| CI20-AR3 | 数值比较 | 后续70fs应与150fs总寿命比较，不与190fs partial直接比较；原因仍待reanalysis。 | CI20-6; ZA23-3/7 | unreviewed |

## Knowledge Impact and Learning Decision

写回 [[doppler-correction]]、[[doppler-velocity-validation-contract]] 的速度stage/联合拟合/independence契约。可推进L3竞争机制矩阵；实际事件重拟合L4仍not-ready。

## Related Knowledge and Project Relations

后续方法 [[ciemala-2021-deep-inelastic-lifetime-method]] CM21-14/15/17/18给正式version的靶后reference、80%totalerror区域及cumulative/feeding说明；本页2020原图1σ/数值保留，不将方法篇后续confidence自动反写到所有2020结果。


| Relation type | Target | Specific relation |
|---|---|---|
| same-lineage | [[ciemala-2019-20o-dsam-analysis-status]] | 2019预备/2020结果分时版本。 |
| same-lineage | [[ziliani-2019-agata-calibration-controls]] | 同实验time/energy/historycontrols。 |
| independent-comparison | [[zanon-2023-o20-high-precision]] | 独立(d,p)、反应点速度与Ex gates，70fs张力。 |
| methodological-bridge | [[doppler-correction]] | velocity-stage与τ–Eγ联合线形。 |
| methodological-bridge | [[doppler-velocity-validation-contract]] | 数据packet与独立性边界。 |

## Human Review Triage

P0：原始归档未填充边界已隔离。P1：CI20-3/5/6/7/8及ZA23差异、confidence definition和feeding/stoppingpacket；不升级human-reviewed。

## Extracted Pages

七页主线；pp.3–5重建/结果/Fig.3，pp.5–6模型。Fig.3视觉审核，不数字化χ²颜色当原始拟合数据。

## Day19量化审计：20O第二2+态飞秒寿命张力、馈入延迟与反应机制解耦

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_o20_ciemala_zanon_reconciliation_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/o20-ciemala-zanon-reconciliation-result-056.json`，核准了 $^{20}\text{O}(2_2^+)$ 态飞秒寿命测量张力与反应机制边界：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| CI20-D19-1 | 对 $^{20}\text{O}(2_2^+)$ 态飞秒寿命在 Ciemała 2020（$\tau_{\text{tot}} = 150^{+80}_{-30}\text{ fs}$，深非弹性反应）与 Zanon 2023（$\tau_{\text{tot}} = 70 \pm 10\text{ fs}$，直接转移反应）间的 $2.143\times$ 张力（$z = 2.53\sigma$）进行系统学对账：(1) 机制解耦：深非弹性反应伴随宽连续态布居，其未分辨连续级联时延系统性后移了多普勒线形并高估了提取寿命；(2) 关键馈入态：Zanon 2023 发现并隔离了来自 $3_1^+$ 态（$5228\text{ keV}, \tau = 54(9)\text{ fs}$）的 $1156\text{ keV}$ 跨带馈入（分支比 $28(1)\%$），若未予扣除将引入约 $15.12\text{ fs}$ 的表观时延；(3) 反应选择律：直接二体转移反应配合轻带电粒子角与能量测量能够构建严格的激发能 $E_x$ 门，彻底切除门控以上连续态馈入，确立了亚 100 fs 超快时间响应测量的首选反应路线。 | task-lifetime-tension-and-reaction-audit | derived-and-boundary | PDF pp.3-5; zanon-2023-o20-high-precision.md; o20-ciemala-zanon-reconciliation-result-056.json | true |
