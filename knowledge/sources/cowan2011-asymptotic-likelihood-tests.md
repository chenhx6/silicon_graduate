---
type: source
title: "Cowan 等 2011：非负信号的渐近似然检验与边界"
aliases: [Cowan2011, CCGV asymptotic likelihood tests]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [profile-likelihood, hypothesis-testing, boundary, local-significance]
source_type: statistical-method-paper-author-preprint
reading_depth: skimmed
title_original: "Asymptotic formulae for likelihood-based tests of new physics"
authors: [Glen Cowan, Kyle Cranmer, Eilam Gross, Ofer Vitells]
journal: European Physical Journal C
year: 2011
volume: 71
article_number: "1554"
doi: "10.1140/epjc/s10052-011-1554-0"
arxiv: "1007.1727"
data_version: "arXiv:1007.1727v3, 2013-06-24, 32-page PDF"
canonical_source: "https://arxiv.org/abs/1007.1727v3"
citation_key:
raw_file: "raw/papers/gpt/learning-daily/20261102-poisson-audit/manifest.json"
raw_sha256: "aa5e26a4df8fb55c45e5db53000529eadd9d2647b2b7b9124d8f0044de492f2f"
raw_storage_status: archived-local
archive_required: true
---

# Cowan 等：非负信号的渐近似然检验

## Bibliographic Record

作者 arXiv 元数据页绑定上述题名、四位作者、DOI 与期刊记录 `Eur.Phys.J.C71:1554,2011`。首版为 2010 年预印本，所读修订版为 **2013-06-24 v3**，不能把修订日期写成期刊发表年。32 页 PDF、HTML 与元数据快照均登记在 `raw_file` 指向的 SHA-256 manifest；逐文件名为 `cowan-et-al-1007.1727v3.pdf`、`cowan-et-al-1007.1727v3.html` 和 `cowan-et-al-1007.1727v3-metadata.html`。

本轮调用 `web.run` 检索和打开作者 arXiv 页面；该工具未返回可读正文，随后通过终端从 arXiv 原站取得并核验 PDF/快照。证据取自实际留档原件，未以搜索摘要补写正文。

**下面全部式号采用归档 PDF**。HTML 转换件的式号有偏移，例如 PDF 的 Eq.(49) 对应 HTML Eq.(51)，PDF Eq.(53) 对应 HTML Eq.(55)；不能混用。

## Scope and Reading Depth

- Covered scope：PDF pp.3–7 的定义和条件；pp.14–15 的 $q_0$ 分布；p.23 on/off 似然；pp.26–27 已知本底和固定/扫描峰位的适用范围。局部定向精读，整体保持 `skimmed`。
- Not covered：全文证明链、RooStats 实现、所有模拟图及后续勘误的逐项复算。本文是统计方法来源，没有新核能级、gamma 跃迁或实测核谱。

## Summary

非负信号的单侧似然检验需要边界分布；其渐近 local 校准依赖模型与信息量，不能直接认证核结构发现。

## Key Results

| ID | 方法结论与限定 | claim_kind | evidence_level | source_independence | locator | needs_review |
| --- | --- | --- | --- | --- | --- | --- |
| CW11-1 | bin 期望为信号与本底之和，模板用 bin 积分，控制观测进入联合似然；profile 在固定兴趣参数时重拟合 nuisance。 | model-result | direct | single | PDF p.4 Eqs.(2–7)，p.5 首段 | false |
| CW11-2 | 单侧正信号检验 $q_0$ 对向下涨落取零，不能用来把本底亏损当作正信号。 | model-result | direct | single | PDF p.7 Eqs.(12–13) | false |
| CW11-3 | Wald 渐近近似下，零信号的 $q_0$ 为 $\tfrac12\delta_0+\tfrac12\chi^2_1$，正 $q_0$ 对应 $Z_0\simeq\sqrt{q_0}$。 | model-result | direct | single | PDF pp.14–15 Eqs.(47–53) | false |
| CW11-4 | 原计数与控制计数的 on/off 例子用两项 Poisson 联合似然，本底为 nuisance。 | model-result | direct | single | PDF p.23 Eq.(90) | false |
| CW11-5 | 峰位扫描须计入 elsewhere fluctuation；统计拒绝只构成新现象发现的一部分。 | author-interpretation | direct | single | PDF p.3 第三正文段；pp.26–27 §5.2 | false |

## Competing Interpretations and Limitations

[[poisson-maximum-likelihood-and-gamma-peak-fitting-bias]] 使用这些方法约束固定峰形、已知本底的演示。稀疏计数、零本底、不可识别峰位与系统误差不能由此自动取得精确 $p$ 值、覆盖率或核结构指认。$q_0=0$ 的包含原子尾概率约定、JSON 奇异状态和非负面积求根是本任务实现选择，不冒充作者的软件接口或实验结果。

此处只作 Codex source self-audit；预印本和期刊记录是同一方法工作的不同载体，不是独立实验重复。

## Extracted Pages

直接回读归档 PDF pp.3–7、14–15、23、26–27；式号与页码以 PDF 为准。HTML 和元数据页用于版本身份与转换件对照，未以其错位式号替代 PDF locator。
