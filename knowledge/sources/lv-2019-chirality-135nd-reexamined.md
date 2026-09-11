---
type: source
title: "Lv 等 2019：135Nd 手征重分析与多重手征双重带"
aliases: [Lv 2019 135Nd reexamined, 135Nd positive-parity chiral doublet]
created: 2026-09-12
updated: 2026-09-12
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Chirality of 135Nd reexamined: Evidence for multiple chiral doublet bands"
authors: [B. F. Lv, C. M. Petrache, Q. B. Chen, J. Meng, A. Astier, E. Dupont, P. Greenlees, H. Badran, T. Calverley, D. M. Cox, T. Grahn, J. Hilton, R. Julin, S. Juutinen, J. Konki, J. Pakarinen, P. Papadakis, J. Partanen, P. Rahkila, P. Ruotsalainen, M. Sandzelius, J. Saren, C. Scholey, J. Sorri, S. Stolze, J. Uusitalo, B. Cederwall, A. Ertoprak, H. Liu, S. Guo, M. L. Liu, J. G. Wang, X. H. Zhou, I. Kuti, J. Timár, A. Tucholski, J. Srebrny, C. Andreoiu]
journal: Physical Review C
year: 2019
volume: 100
pages: 024314
doi: 10.1103/PhysRevC.100.024314
arxiv: 1907.12809
language: en
canonical_source: "https://doi.org/10.1103/PhysRevC.100.024314"
zotero_item_key:
citation_key:
zotero_uri:
library_file: "raw/papers/gpt/_incoming/20260912-135nd-crosswalk/lv-2019-135nd-reexamined-arxiv.pdf"
raw_file: "raw/papers/gpt/_incoming/20260912-135nd-crosswalk/lv-2019-135nd-reexamined-arxiv.pdf"
raw_sha256: "97182e90125ce57ac2faa0feeef42b6bc12952b3287f82f277a04f8d32cf0303"
nuclei: [135nd]
reactions: ["100Mo(40Ar,5n)135Nd"]
experiments: [jurogam2-135nd-ar40-152mev]
models: [constrained-covariant-density-functional-theory, particle-rotor-model]
observables: [IPDCO, dco-ratio, two-point-angular-correlation-ratio, bm1-be2-ratio, alignment, energy-levels]
methods: [in-beam-gamma-spectroscopy, gamma-gamma-coincidence, linear-polarization-asymmetry, dco-ratio, two-point-angular-correlation-ratio]
tags: [a130, 135nd, nuclear-chirality, multiple-chiral-doublet-bands, positive-parity, jurogam]
---

# Lv 等（2019）：`135Nd` 手征重分析与多重手征双重带

## Bibliographic Record

B. F. Lv 等，*Chirality of `135Nd` reexamined: Evidence for multiple chiral doublet bands*，*Physical Review C* **100**, 024314 (2019)，DOI `10.1103/PhysRevC.100.024314`，arXiv `1907.12809`。ArXiv API 给出的 journal reference、题名、作者首位和 DOI 与 Crossref 元数据一致；本地 PDF 为 arXiv 版本，SHA-256 为 `97182e90125ce57ac2faa0feeef42b6bc12952b3287f82f277a04f8d32cf0303`。

## Scope and Reading Depth

- `deep-read`：全文 10 个 PDF 页面均完成文本主线阅读。
- 视觉核对：PDF pp.1–3 的题名、摘要、实验结果、部分能级图和门谱；pp.6 的总结；pp.7–10 的 Table I（含 D3、D4、D5、D6 行）。
- 关键核对对象：D3/D4 的 parity revision、四条 IPDCO 数值、D3/D4 连接跃迁、D5/D6 的负宇称谱系、Table I 的逐线 `J^π`。
- 未覆盖：原始事件矩阵、实验标定输入和作者未公开的逐事件分析；这不影响本文表格/正文层级的 parity crosswalk。
- 版本边界：本地文件是公开 arXiv 版本；DOI 期刊身份已由 Crossref/API 核验，但未另行保存出版商 PDF。

## Summary

2019 PRC 重新分析 `135Nd` 的高自旋谱学，明确将 D3/D4 作为正宇称 chiral-doublet pair，并将此前的负宇称 D5/D6 作为另一组 pair。正文、IPDCO、D4↔D3 的 E2、D4→D1 的 E1 以及 D4 表格行形成一致的总体宇称证据；但 D3 的 `334.4 keV` Table I 行仍有局部 `J^π` 异常，绝对 partner strengths/lifetimes 和更强的静态手征措辞仍需保留边界。

## Paper Question and Experimental Design

论文重新检查 `135Nd` 中已知的负宇称 chiral pair，并在同一类 `100Mo(40Ar,5n)` 高自旋谱学中寻找额外的伙伴带。实验使用 152 MeV `40Ar` 束、0.5 mg/cm² 自支撑富集 `100Mo` 靶和 JUROGAM II 的 39 个 Compton-suppressed Ge 探测器（PDF p.2）。能级、自旋和宇称由符合关系、`R_DCO`、`R_ac` 与线偏振联合约束；作者再用 constrained CDFT 和 PRM 比较能谱、alignment 与 `B(M1)/B(E2)`。

## Evidence Chain

1. `D3` 在已知 334-keV 终止位置基础上扩展至约 `33/2+`，并新增多条连向 D2-3qp 的跃迁；正文明确写其 parity based on `R_DCO`/`R_ac` 改为 positive（PDF p.2）。
2. `D4` 的已知结构被延伸并将 spin 下调一单位；`589、649、780 keV` 的 D4↔D3 连接被判为 E2，`1184 keV` 至负宇称 D1 的连接被判为 E1，正文据此说明 D4 与 D3 同为正宇称（PDF p.2）。
3. 为确认 D2–D4 的宇称，作者给出 `830、1015、1161、1184 keV` 四条连接的 IPDCO：`0.043(8)、0.089(28)、0.008(2)、0.018(5)`；正文称这些值显示 electric character，并据此 fix D2、D3、D4 的 positive parity（PDF p.2）。
4. Table I 的 D4 行从 `21/2+→19/2+` 至 `29/2+→27/2+`，以及其续表中的 `23/2+→19/2+`、`25/2+→21/2+`、`27/2+→23/2+`、`21/2+→19/2−` 等，均与正文的正宇称 D4 叙述一致（PDF pp.8–9）。
5. Table I 的 D3 行大部分列为正宇称，但 `334.4 keV` 一行仍写作 `27/2−→25/2+`（PDF p.8）。它与同一表 D3 的其它行、PDF p.2 的 D3 positive-parity 说明和 Fig.1 的整体标注不一致，当前只能标为残余 table-level anomaly；不能把这一孤立行当作对整条 D3 宇称的反向裁决。
6. 2019 论文说此前报告的 D5、D6 levels 在 Ref. [10] 和 [36] 中得到确认，并在 Table I 中将两带逐线列为负宇称；作者把 D5/D6 与新增正宇称 D3/D4 分开作为两组 pair（PDF pp.1–2、6、9–10）。

## 2019 Parity Crosswalk

| 证据层 | 2019 PRC 的直接记录 | 与 thesis/历史论文的关系 |
|---|---|---|
| D3 | 正文由 `R_DCO`/`R_ac` 多条连接将 D3 改为正宇称；IPDCO 段再次把 D3 列入正宇称 D2–D4 | 吕冰峰 2019 thesis 的实验结果同段先写 changed to positive；该 thesis 的孤立负宇称句子不是后发 PRC 的结论 |
| D4 | 正文以 D4↔D3 E2 和 D4→D1 E1 说明 D4 与 D3 同为正宇称；Table I 的 D4 行一致 | thesis physical p.127 的正/负句子冲突由此得到外部期刊版本支持；D4 不再因该文字冲突停在 `stopped` |
| D3 334.4-keV row | 表格仍保留 `27/2−→25/2+` | 作为 2019 版本内部残余 typo/表格异常保存，不扩展为整条带的负宇称结论 |
| D5/D6 | 负宇称、既有 pair；2019 PRC 明确以此前 refs [10,36] 为谱系 | 2003 PRL 的 Band A/B 与 2007 PRL 的 electromagnetic/lifetime paper 是前史；同一物理谱系不重复计为独立实验 |

## Historical Lineage

- Zhu 等 2003 PRL（arXiv `nucl-ex/0302029`，DOI `10.1103/PhysRevLett.91.132501`）报告 `110Pd(30Si,5n)`、133 MeV 下的 `135Nd` Band A/B：两条近简并、同宇称的 `ΔI=1` 带，由 `ΔI=1` 和 `ΔI=2` links 连接，并以三维 TAC 讨论三准粒子手征结构。该论文的带名是 Band A/B，不应倒写成其当时已经使用 D5/D6。
- Mukhopadhyay 等 2007 PRL（arXiv `0708.1493`，DOI `10.1103/PhysRevLett.99.172501`）在 `100Mo(40Ar,5n)`、175 MeV 的 Gammasphere 数据中对先前 Band A/B 测得寿命、`B(M1)` 和 `B(E2)`，并讨论从 chiral vibration 到 static chirality。2019 PRC 的 D5/D6 负宇称 pair 与该历史负宇称谱系相连，但实验 campaign 不同。
- Qi 等 2009 的 PRM 理论论文（arXiv `0812.4597`，DOI `10.1016/j.physletb.2009.02.061`）和 Lawrie 等 2020 的 CDFT 理论论文（arXiv `2009.08075`，DOI `10.1016/j.physletb.2020.135795`）是模型/后续理论支持，不替代 2019 PRC 的实验 parity 记录。
- Lv 2019 博士论文是同一作者/实验谱系的学位论文层记录；期刊文章与 thesis 不能作为两个独立 JUROGAM II 实验计数。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | source_independence | locator | research_status | needs_review |
|---|---|---|---|---|---|---|---|
| LV19-1 | 152 MeV `100Mo(40Ar,5n)135Nd`、0.5 mg/cm² 富集靶和 39 个 JUROGAM II Compton-suppressed Ge 探测器用于本实验。 | experimental-fact | direct | single | PDF p.2, Sec.II | completed | false |
| LV19-2 | `R_DCO`、`R_ac`、γγ coincidence 和线偏振共同参与自旋、宇称与多极性赋值。 | experimental-criterion | direct | single | PDF p.2, Sec.II | completed | false |
| LV19-3 | 四条连接的 IPDCO 为 `0.043(8)、0.089(28)、0.008(2)、0.018(5)`，作者以其 electric character 固定 D2、D3、D4 的正宇称。 | experimental-criterion | direct | single | PDF p.2, Sec.II | completed | false |
| LV19-4 | 2019 PRC 的正文、Fig.1/表格和总结共同支持 D3/D4 为正宇称 pair；D4 的正宇称由 D4↔D3 E2 与 D4→D1 E1 连接进一步说明。 | experimental-fact + author-interpretation | direct | multiple-dependent | PDF pp.2–3、6、8–9 | completed | false |
| LV19-5 | D3 Table I 的 `334.4 keV` 行仍写成 `27/2−→25/2+`，与该文其余 D3 正宇称记录不一致；它是保留的表格级异常，而非整条带的独立 parity 裁决。 | experimental-fact | direct | single | PDF p.8, Table I | completed | false |
| LV19-6 | 2019 PRC 将已知负宇称 D5/D6 与新增正宇称 D3/D4 分为两组 chiral doublets；D5/D6 的先前谱系回到 2003 Band A/B 和 2007 lifetime/transition-probability papers。 | synthesis | indirect | multiple-dependent | PDF pp.1–2、6、9–10；crosswalk artifacts | completed | false |
| LV19-7 | PRM 使用 D3/D4 的 `π[(1h11/2)^1(1g7/2)^−1]⊗ν(1h11/2)^−1` 配置；D5/D6 使用 `π(1h11/2)^2⊗ν(1h11/2)^−1`，计算再现能谱和部分 `B(M1)/B(E2)` 趋势。 | model-result | indirect | single | PDF pp.5–6, Fig.3/5/6 | completed | false |
| LV19-8 | 2019 PRC 没有提供所有 partner-resolved absolute strengths/lifetimes，也没有消除弱 link、configuration mixing 或表格孤立行对更强 MχD 措辞的限制。 | our-inference | direct | single | PDF pp.2、5–6、8–10 | completed | false |

## Nuclear Structure and Interpretation

- `D3/D4`：2019 PRC 的实验版本为正宇称 pair，建议组态为 `π[(1h11/2)^1(1g7/2)^−1]⊗ν(1h11/2)^−1`；D3 仅有很少可提取的 `B(M1)/B(E2)` information，不能将 PRM agreement 写成独立几何测量。
- `D5/D6`：负宇称 pair，建议组态为 `π(1h11/2)^2⊗ν(1h11/2)^−1`；2007 PRL 的 lifetime/transition-probability evidence 属于前一负宇称谱系，不是 D3/D4 的寿命证据。
- 2019 PRC 的作者解释是两组 MχD；实验事实是能级、连接、多极性/偏振指标和表格赋值。模型计算再现不等于已排除 γ-soft、configuration mixing、band crossing 或其它集体解释。

## Competing Interpretations and Limitations

- “D3/D4 positive parity”在 2019 PRC 的正文、IPDCO 段、能级图和 D4 表格行之间有多重直接支持；但 Table I 的 D3 `334.4 keV` 行必须逐字保留为未调和的局部异常。
- 同宇称、近简并、E2/M1 连接和 PRM/CDFT agreement 支持 chiral-doublet interpretation，但不能单独证明静态手征；absolute partner-resolved electromagnetic strengths、寿命和独立模型比较仍是限制。
- 2003、2007、2019 的 publication lineage 横跨不同实验设置或同一数据谱系的后续分析。论文数不能替代独立实验数，2007/2019 也不能把 2003 的 Band A/B 当作当时已有 D5/D6 标签。
- 本页不把 2019 PRC 对 D3/D4 的修订倒灌为 Zhu 2003 或 Mukhopadhyay 2007 的原文表述；每个来源的作者解释按发表时间和带号分开保存。

## Codex Self-audit

| 审计项 | 判断 | 证据 |
|---|---|---|
| Identity/locator | DOI、arXiv、题名、作者首位、卷页和本地 PDF SHA 已交叉核对；关键 parity、IPDCO、Table I 页码已视觉核对。 | Crossref/arXiv metadata；PDF pp.1–10；`outputs/literature-acquisition/20260912-135nd-crosswalk.json` |
| Claim separation | 观测/判据、作者解释、PRM/CDFT 模型结果和跨来源谱系推断已分栏；不把 model agreement 直接写成实验事实。 | LV19-1–8；Historical Lineage |
| Conflict handling | thesis 的 D4 正/负句子冲突被 2019 PRC 的正文和表格层支持为正宇称；D3 334.4-keV 表格行仍保留 anomaly。 | PDF p.2、p.8；LV19-4/5 |
| Independence | Lv thesis、2019 PRC、2003 PRL、2007 PRL 和 2009/2020 theory 按 dependent publication/theory lineage 分层，不重复计数。 | Historical Lineage；manifest |
| Paper-use boundary | 页面仍为 `unreviewed`；本轮 `needs_review: false` 表示 Codex 已完成 claim-level 直接证据自审，不表示用户已审核或论文措辞已获准。 | frontmatter；LV19-1–8 |

## Knowledge Impact and Learning Decision

- **纠正知识**：`DD-20260910-136ND-03` 不再因“缺少外部原始论文”而 stopped。2019 PRC 后发期刊版本明确支持 D3/D4 正宇称；原 thesis 的 D4 负宇称句子记录为 source-text error/遗留文字错误。
- **保留边界**：2019 Table I 的 D3 `334.4 keV` 行仍异常；D3/D4 的 MχD 仍是作者解释/候选层级，未凭本 crosswalk 提升为无条件“已证实”。
- **独立性**：本 source 与 Lv thesis、2003 PRL、2007 PRL 共享或延续物理谱系；manifest 中的五个 PDF 是交叉核验材料，不是五个独立实验。
- **Persistence**：建立本 source；更新 `135Nd` 汇总、index、批次报告/closure/self-audit。暂不创建重复的 D3/D4 band pages，避免在表格局部异常尚存时扩张实体。

## Extracted Pages

- [[135nd]]
- [[lv-bingfeng-2019-chirality-136nd-135nd-thesis]]
- [[lv-2021-tilted-precession-135nd]]
- [[petrache-2018-chiral-bands-even-even-136nd]]
- [[multiple-chiral-doublet-bands]]
- [[nuclear-chirality-and-multiple-chiral-doublet-bands]]
- [[jurogam2-135nd-ar40-152mev]]

## Related Knowledge

本页与 `135Nd` 的 D1/TiP、D5/D6 历史谱系、`136Nd` MχD 和 A≈130 手征方法页相连；新建外部 source 不创建重复的 D3/D4 band page。

## Later Paper / Q&A Gate

本页已完成 Codex self-audit；未发生用户页面级审核。若后续问答或论文写作要引用具体 `J^π`、IPDCO 或“D3/D4 正宇称 MχD”措辞，仍应回到 2019 PRC 的原文页码和 Table I，并明确 D3 `334.4 keV` 局部异常及 MχD 的作者解释属性。
