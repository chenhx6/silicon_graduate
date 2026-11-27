---
type: source
title: "Watanabe et al. 2021 - Beta Decay of the Axially Asymmetric Ground State of 192Re"
aliases: ["Watanabe 2021 192Re", "Watanabe 2021 PLB", "192Re beta decay KISS"]
created: 2026-11-07
updated: 2026-11-27
status: active
archive_required: true
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Beta decay of the axially asymmetric ground state of 192Re"
year: 2021
canonical_source: "https://doi.org/10.1016/j.physletb.2021.136088"
citation_key: ""
raw_file: "raw/papers/gpt/query/20261107-campaign-G08/watanabe-2021-192re-beta-decay.pdf"
raw_sha256: "58142e4d2335a126f270a3a076d7cc19d1d06c8ca9ed19c0a60adc207d7f9780"
tags: ["experiment-ingest", "beta-decay", "192re", "192os", "gamma-soft", "kiss", "hfodd", "a190"]
authors: ["H. Watanabe", "Y. X. Watanabe", "Y. Hirayama", "A. N. Andreyev", "T. Hashimoto", "F. G. Kondev", "G. J. Lane", "Yu. A. Litvinov", "J. J. Liu", "H. Miyatake", "J. Y. Moon", "A. I. Morales", "M. Mukai", "S. Nishimura", "T. Niwase", "M. Rosenbusch", "P. Schury", "Y. Shi", "M. Wada", "P. M. Walker"]
journal: "Physics Letters B"
volume: 814
pages: "136088"
doi: "10.1016/j.physletb.2021.136088"
nuclei: ["192re", "192os", "191re"]
---

# Watanabe2021：192Re低自旋β布居与结构解释

## Bibliographic Record

H. Watanabe et al., PLB814,136088(2021)，DOI10.1016/j.physletb.2021.136088。
White Rose出版版副本共7物理页，PDF1为库方封面，PDF2–7为六页论文。

## Scope and Reading Depth

### Covered scope

正文、Table1和Fig2的β布居/半衰期及HF解释；总控回查实际PDF2–6。

### Not covered

未取得原始β计数、分支完整Cov和HFODD生产代码。
本文是A192链，不是对A194预测高自旋态的直接搜索。

## Key Results

| ID | 实际内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WA21-1 | KISS测192Re的T1/2=15.1(6)s；由β布居/logft暂定基态Jπ=(0−) | experimental-fact + author-interpretation | direct | PDF4 Fig2/讨论 | false |
| WA21-2 | 作者由总β与已观测馈送差估基态β分支89(2)%；低自旋0+/2+布居与logft支持上述指认 | experimental-fact, intensity-balance-derived | direct | PDF4 Table1/Fig2 | false |
| WA21-3 | 低J母态与给定Qβ/选择定则使高J态布居不利；不等于所有高阶禁戒宽度严格为零 | experimental-criterion | direct-framework + our-inference | PDF4/6；本任务边界 | false |
| WA21-4 | HF+SVI以单核子组态与轴不对称形变解释基态/同位素演化 | model-result | direct | PDF5–6 Tables2–3 | false |

## Experiment and Interpretation Boundary

PDF3实际写136Xe与natural Pt多核子转移，靶厚10.7mg/cm²；
不是worker草案的富集198Pt12.5mg/cm²。装置安装与各探针数据使用仍按原文分开。
(0−)是基于强度/logft的暂定指认，不是本次独立直接自旋测量。
0−→0+按作者讨论为first-forbidden non-unique，不能写“一阶非禁戒”。

## Competing Interpretations and Limitations

基态分支由强度平衡而非逐个直接看见β到基态，依赖未见弱feeding的处理。
低自旋β布居限制说明“不观察高自旋γ”可能有选择性原因，
但本论文不能证明194Os某个预测态不存在、已发现或当前搜索已穷尽。
不得将192Re→192Os与194Os跨质量数混作一份直接负结果。

## Summary

为A192增加一个低自旋布居和暂定Jπ的原实验基准。
其HF形变与更高自旋Os/Ir的PES要逐态比较，不能由一个基态推广整个同位素链。

## Knowledge Impact and Learning Decision

`supports + bounded comparison`，关联[[campaign-g08-a190-shape-isomer-20261107]]。
不由本篇单独提取普适gA或高自旋异能态搜寻概率。

## Agent Self-audit Triage

P0: none identified in PDF identity/hash。P1：总控纠正封面/正文页数、靶信息、
暂定自旋、强度平衡属性和A192/A194区分；撤回“完全不能馈送J≥4”的绝对断言。

## Extracted Pages

PDF2–7；题录/方法与布居/模型的定位已分别列出。

## 2026-11-27 — 馆藏原件与覆盖核对

- 物理 PDF 1：库方封面和版次。
- 物理 PDF 2–3：出版首页、引言、KISS 产束及衰变谱学设置、图 1 图题。
- 物理 PDF 4：表 1、图 2–3 图题、β 强度平衡、半衰期与自旋宇称推断。
- 物理 PDF 5–6：图 4–5 图题、表 2–3、奇质量数 Re 基准比较及 ¹⁹²Re 的 HF+SVI 计算。
- 物理 PDF 7：结论续段、利益声明、致谢和参考文献 [1]–[45]。
- 本次获取的具体覆盖：通读物理 PDF 1–7 的给定文本，包括库方封面及连续六页出版正文、表 1–3 的可提取文字、图 1–5 的图题、结论和参考文献。未目视核验图、表排版或公式字形。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A19-1 | KISS 实验通过 ¹⁹²Re 束流开关后的 β 计数增长与衰减拟合得到基态半衰期 15.1(6) s。β–γ 符合谱和 γ 跃迁支持对 ¹⁹²Os 若干已知低激发态的布居识别。 | 实验结果 | source-reported | 物理 PDF 3 图 1 图题及谱学正文，物理 PDF 4 表 1、图 3 图题及半衰期正文。图 3 的曲线和拟合标注待核。 | true |
| A19-2 | 作者以拟合得到的总 β 计数扣除 206 和 489 keV 两条跃迁的总强度，估得通往 ¹⁹²Os 基态的 β 分支为 89(2)%。总跃迁强度包含内转换修正，分析省略未观测的 E0。未见的高位馈送会使图 2 所列相应表观馈送成为上限、相应 log ft 成为下限。 | 强度平衡推导 | source-reported | 物理 PDF 4 表 1、图 2 和图 3 附近正文，未编号强度表达式 (1 + αT)Iγ。图 2 的逐级数值、不等号及标记待核。 | true |
| A19-3 | 作者依据 ¹⁹²Os 的 0⁺、2⁺ 布居格局和 log ft，将 ¹⁹²Re 基态暂定为 Jπ = (0⁻)。通往 ¹⁹²Os 基态的 0⁻→0⁺ 分支按一级禁戒非唯一跃迁讨论。 | 作者解释 | source-reported | 物理 PDF 4 图 2 图题及自旋宇称讨论。图中上标 1u 的具体位置待核。 | true |
| A19-4 | HF+SVI 用单粒子轨道随 γ 的变化解释 Re 链的形变趋势。作者将表 3 中负宇称、计算自旋约 0.09 ℏ、γ = 37.3°、相对能量 293 keV 的组态视为暂定 (0⁻) 基态的最可能对应组态。表内最低计算能量属于正宇称组态。 | 模型结果 | source-reported | 物理 PDF 5 图 4、表 2 及正文，物理 PDF 6 图 5、表 3 及正文。图 5 中央面板的四极矩标记待核。 | true |

¹⁹²Os 的既有能级自旋宇称取自 [11]，Qβ = 4290(70) keV 取自 [29]，内转换系数依据 [30]。奇质量数 Re 的实验参照取自 [34]，HFODD 见 [37]–[38]。建议接受旧条目同版物理 PDF 2–6 的正文覆盖，并修正关键定位。旧条目只明确记录了总控回查 PDF 2–6，本回执补记 PDF 7 的文本覆盖。依赖图内标注的证据待管理人核对。

- WA21-1 将半衰期定位到物理 PDF 4 图 3 和拟合正文，暂定自旋定位到同页图 2 和自旋宇称讨论。WA21-2 将 89(2)% 的直接出处定位到同页强度平衡正文，表 1 保留为相对 γ 强度输入。
- 保留比较笔记已作的草案修正：靶为天然 Pt、10.7 mg/cm²，0⁻→0⁺ 为一级禁戒非唯一，低自旋选择性只作布居限制。将 WA21-4 的组态说明补上表 3 的相对能量与宇称排序。
- 物理 PDF 3 的既有异能态半衰期不对称误差在抽取中跨行散开，引用前核对正文原排。物理 PDF 5 表 2 的 Nilsson 表头有损坏字符，核对原表后再转写。物理 PDF 6 图 5 中央面板的固定四极矩下标以原图核定。
