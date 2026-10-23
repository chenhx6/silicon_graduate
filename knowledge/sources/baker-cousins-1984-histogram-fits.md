---
type: source
title: "Baker–Cousins 1984：计数谱拟合的统计量与区间"
aliases: [Poisson likelihood chi square, Baker Cousins histogram statistic]
created: 2026-10-14
updated: 2026-10-14
status: ai-draft
review_status: unreviewed
source_type: statistical-method-paper-public-report-version
reading_depth: deep-read
title_original: "Clarification of the use of CHI-square and likelihood functions in fits to histograms"
authors: [Steve Baker, Robert D. Cousins]
journal: Nuclear Instruments and Methods in Physics Research
year: 1984
volume: 221
issue: 2
pages: 437-442
doi: "10.1016/0167-5087(84)90016-4"
data_version: UCLA-HEP-83-3-July1983-acceptedOctober1983-KEKSCAN83-11-266
canonical_source: "https://doi.org/10.1016/0167-5087(84)90016-4"
citation_key:
raw_file: "raw/papers/gpt/day13/baker-cousins-1984-histogram-fits-kekscan.pdf"
raw_sha256: "e687601ebec8241a46db58aeeccffa2b4b252fe62c79db5b44ec51092e7c245a"
raw_storage_status: reserved-unpopulated-public-author-report-scan-only
raw_archive_verified_at: 2026-10-23
external_pdf_url: "https://lib-extopc.kek.jp/preprints/PDF/1983/8311/8311266.pdf"
nuclei: []
methods: [histogram-fitting, poisson-likelihood, chi-square, confidence-region]
tags: [counting-statistics, neyman, pearson, normalization, likelihood, finite-sample]
---

# 线形拟合所用的χ²需要完整定义

## Bibliographic Record

Steve Baker、Robert D. Cousins，NIM **221**(2),437–442(1984)，DOI如上；Crossref核验作者/题名/年/卷/页。实际所读是22页UCLA-HEP-83-3报告，封面July1983并写acceptedOctober1983。INSPIRE193548将相同DOI、UCLA报告和KEKSCAN83-11-266绑定；公开KEK副本封面/title/authors/reportID视觉核验，不把22页报告当期刊六页PDF。

原raw未改变，保留slot未填充；临时副本`tmp/day13/reopened/baker-cousins-kekscan-83-11-266.pdf`，SHA如上。OpenAlex无OA位置、猜测的FNAL候选403并未验证身份，之后沿正式INSPIRE/KEK locator取得原报告；不能把失败候选写为本文的实际source。

## Scope and Reading Depth

- Covered scope：22页报告主线及Appendix，Poisson/multinomial、Pearson/Neyman、likelihoodχ²、area条件、point/interval/GOF与finiteN；封面及pp.8/12核心式视觉核验。
- Not covered：1984出版社排印版、所有统计学参考文献、任何20O事件/χ²模板。报告的方法论不是独立核寿命实验。

## Paper Question and Scientific Motivation

直方图的最佳参数、参数区间和拟合优度是不同问题。需要明确计数分布和统计量，避免将任意weightedleast-squares一概当有已知χ²分布，并阐明Poisson与multinomial拟合何时产生相同pointestimate。

## Method and Design Logic

从bin事件n_i、模型积分y_i与N/预测N0出发，定义计数likelihood；与bin-by-bin饱和模型作likelihoodratio生成deviance。再对自由overallscale的score作推导，分析area保持条件与finiteN的适用限制。

## Key Evidence and Reasoning Chain

bin数据的生成机制→likelihood/统计量定义→参数/normalization自由度→pointestimate与interval/GOF各自条件→finiteN模拟验证。只知道“leastχ²”或minimum/reducedχ²的数值不足以完成整条链。

## Summary

Pearson用y_i作分母，Neyman用n_i，两者不等Poissondeviance。自由overallscale时PoissonMLE保持总计数，Poisson与multinomial可有相同pointestimate；区间仍不能一律互换。有限样本的bias与coverage需按具体模型检查，MLE也不是普遍无偏保证。

## Experimental or Theoretical Setup

本文是统计方法推导，无新核谱学采集。一般直方图可为多维；固定总N与Poisson采集不同。应用到Dopplerτ/E必须另加response、selection、feeding、background与template/covariance，本文不提供这些核实验输入。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BC84-1 | 点估计、区间估计与goodness-of-fit需区分；可以采用不同统计量，不能因都叫χ²而混淆任务。 | experimental-criterion | direct | KEKscanPDF pp.2–3, Introduction | true |
| BC84-2 | y_i严格为bin内模型积分，bincenter×width是近似；N设计固定对应multinomial，采集N的计数实验对应independentPoisson。 | experimental-criterion | direct | KEKscanPDF pp.4–5, Eq.(1)/definitions | true |
| BC84-3 | Pearsonχ²=Σ(n−y)²/y，Neymanχ²=Σ(n−y)²/n；multinomial还需Σy=Σn约束，任意权重S不必满足χ²分布。 | experimental-criterion | direct | KEKscanPDF pp.5–6, definitions | true |
| BC84-4 | Poisson likelihood可分解成总计数Poisson概率P(N;N0)×给定N的multinomial；删除P(N)是否允许取决模型/问题。 | experimental-criterion | direct | KEKscanPDF p.7, Eqs.(2–3)/following identity | true |
| BC84-5 | Saturated-bin likelihoodratio给Poissondeviance2Σ[y−n+nln(n/y)]及约束下multinomial2Σnln(n/y)；deviance最小化与其MLE点估计相同，χ²分布为渐近说法。 | experimental-criterion | direct | KEKscanPDF p.8; p.19 Appendix | true |
| BC84-6 | 若可将y_i重参为a′1g_i(其它参数)、Jacobian非零，overallscale完全自由，PoissonMLE保证Σy=Σn。 | experimental-criterion | direct | KEKscanPDF pp.11–13, Eqs.(5–9), especially Eq.(7) | true |
| BC84-7 | 在该scale条件下Poisson/multinomial pointestimates可相同，但intervalestimates不必相同；finiteN需具体检查。 | experimental-criterion | direct | KEKscanPDF pp.13–14, Secs.5–6 | true |
| BC84-8 | 同一likelihooddeviance可服务MLE/interval/GOF；若用MLE估计却改用另χ²做GOF，应明确它们的不同统计意义。 | experimental-criterion | direct | KEKscanPDF pp.14–15, Sec.7 | true |
| BC84-9 | 作者强调WLS与MLE在finiteN可能有bias；minimum统计量未必精确遵循渐近χ²，建议具体MC检验，bias/MSE tradeoff亦存在。 | author-interpretation | direct | KEKscanPDF pp.15–18, Sec.8/Conclusions | true |
| BC84-10 | 报告说线性拟合、weights不依赖parameters时WLS无偏；本页将该原文简述与任务对data-dependentweights的条件审核分开。 | author-interpretation | direct | KEKscanPDF p.16, Sec.8 | true |

## Nuclear Structure Information

无新能级/寿命/B。用于 [[zanon-2023-o20-high-precision]] ZA23-10的Neyman/rebin/jointregion和 [[ciemala-2021-deep-inelastic-lifetime-method]] CM21-17的统计契约，不对两次20Oτ差异给新物理解释。

## Authors' Interpretation

likelihood提供统一构造，但不是在所有问题中保证最佳或无偏；有限样本应研究具体teststatistic。保持area的充分条件明确，不由最后histogram计数相等就证明模型、背景或全部nuisance正确。

## Model Results

本文公式为统计推导。任务独立的uniformPoissonrate/Gaussianregion练习在 [[doppler-correction]]；其bias与coverage数值不是本文发表的MC结果，也不是真实τ拟合偏差。

## Competing Interpretations and Limitations

- fixedN/multinomial与Poisson采集不能只凭已经画了归一化谱任意切换；自由scale、prior、效率与外部yield约束要保留。
- 线形template应对bin积分；数据依赖rebin、response/tails和有限MC会改变统计问题，不能以“每bin≥10”替完整验证。
- Background-subtracted内容可为非整数/负数，并有sharedsideband covariance；它不是无条件Poisson计数。实际signal/background应回到各自观测与forwardmodel。
- p.16 WLS简述需常规固定/适当独立weights假设。Neyman1/n虽然不显式依赖fitparameter，却与dataerrors相关；任务harmonicmean反例只限定过强套用，不宣称本文整体结论错误。
- 低count、边界、未识别nuisance等情况下，不能用本文渐近χ²语句保证真实τ/E区间覆盖；PoissonMLE的非线性参数也可能finiteNbiased。
- Report22pages与publisher6pages的版本/locator分开，排印版尚未取得；同方法引用不新增实验独立性。

## Analytical Reconstruction

| ID | 审核项 | Agent判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| BC84-AR1 | area/point估计 | y=a g有自由scale时能证明N0=N；固定background/prior或物理rate约束可能破坏这个充分条件。 | BC84-4/6/7 | unreviewed |
| BC84-AR2 | source versus exercise | Uniformrate的Poissonmean无偏不等任意τ/E无偏；Gaussian jointregion不用于重标sourceinterval。 | BC84-9/10; ZA23-10; CM21-17 | unreviewed |
| BC84-AR3 | parentdata | on/off背景与rawhist/template缺口未被方法文献或toy替代。 | BC84-2/3/5/9 | unreviewed |

## Knowledge Impact and Learning Decision

写回 [[doppler-correction]] 的计数/区域定义与 [[doppler-velocity-validation-contract]] 数据包。方法L2/L3可推进，actualexperimentalrefitL4未ready。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| cited-method | [[zanon-2023-o20-high-precision]] | SIRef6的统计方法入口；不证明具体生产Neyman实现/coverage。 |
| methodological-bridge | [[ciemala-2021-deep-inelastic-lifetime-method]] | jointconfidence与totalerrors的定义。 |
| methodological-bridge | [[doppler-correction]] | bin/normalization/likelihood/τ–E区域的适用条件。 |
| methodological-bridge | [[doppler-velocity-validation-contract]] | 原计数、背景、template/Σ与closure契约。 |

## Human Review Triage

P0：report身份与publiccopy/raw边界已隔离。P1：BC84-2/3/5/6/7/9/10的条件和与20Ostatisticpacket关系。无human-reviewed升级。

## Extracted Pages

22页报告主线；pp.4–8统计量、11–14scale/interval、15–18bias/GOF、19Appendix为核心；参考20–22仅作引用语境。封面/8/12视觉核验。
