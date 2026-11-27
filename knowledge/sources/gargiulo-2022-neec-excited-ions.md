---
type: source
title: "Nuclear Excitation by Electron Capture in Excited Ions"
aliases: [Gargiulo 2022 NEEC in excited ions, Gargiulo 2022 NEEC-EXI]
created: 2026-11-07
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
source_type: theory-article
reading_depth: deep-read
title_original: "Nuclear Excitation by Electron Capture in Excited Ions"
authors: [Simone Gargiulo, Ivan Madan, Fabrizio Carbone]
journal: Physical Review Letters
year: 2022
volume: 128
pages: 212502
doi: 10.1103/PhysRevLett.128.212502
language: en
canonical_source: doi:10.1103/PhysRevLett.128.212502
raw_file: "raw/papers/isomer/isomer_application/nuclear battery/2022_Gargiulo et al_Nuclear Excitation by Electron Capture in Excited Ions.pdf"
raw_sha256: dc0f0fe54e8637a088ba4e9f3b11e3b6d98c07de833a9bc6cb615dc6b29c183f
archive_required: true
nuclei: [73ge, 93mo, 98tc, 125te]
reactions: []
observables: [resonance-strength-boost, k-shell-capture-channels, recoupling-coefficient-lambda]
methods: [flexible-atomic-code-fac, feshbach-projection-operator, recoupling-angular-momentum-algebra, xatom-code]
tags: [neec-exi, excited-ions, ground-state-assumption-violation, k-shell-screening, 73ge, 93mo]
---

# Gargiulo et al. (2022): Nuclear Excitation by Electron Capture in Excited Ions

## Bibliographic Record

Simone Gargiulo, Ivan Madan, and Fabrizio Carbone, "Nuclear Excitation by Electron Capture in Excited Ions," *Physical Review Letters* **128**, 212502 (2022), DOI: `10.1103/PhysRevLett.128.212502`. The archived 17-page PDF is the author-extended preprint version (arXiv:2102.05718v2) containing the complete 5-page Letter text plus 12 pages of Supplemental Material. SHA-256: `dc0f0fe54e8637a088ba4e9f3b11e3b6d98c07de833a9bc6cb615dc6b29c183f`.

## Scope and Reading Depth

Deep reading of the Letter and Supplemental Material. Locators examined: GSA violation and NEEC-EXI concept (PDF p. 1--2 / printed p. 212502-1--2, Fig. 1), recoupling coefficient \(\Lambda\) (PDF p. 2 / printed p. 212502-2, Eq. 2), opening of 100 K-shell channels in \(^{73}\)Ge at \(q=29+\) in Fig. 2 and Table I (PDF p. 2--3 / printed p. 212502-2--3), and discussion of \(^{93}\)Mo stopping (PDF p. 4 / lines 499--515 and 580--583).

## Summary

The authors demonstrate that lifting the Ground State Assumption (GSA) allows NEEC to occur in out-of-equilibrium excited electronic configurations (NEEC-EXI). In \(^{73}\)Ge (13.28 keV transition), outer-electron screening in excited configurations lowers K-shell binding energies below the nuclear excitation energy, opening 100 new resonant K-capture channels at \(q=29+\) and boosting resonance strength by over three orders of magnitude. For \(^{93}\)Mo, excited configurations allow L-shell vacancies at lower charge states (\(q \approx 30\text{--}32\)), providing a \(10^2\text{--}10^3\) gain, though still leaving a multi-order gap to 1%.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GA22-1 | Lifts Ground State Assumption, formulating NEEC in excited electronic configurations (NEEC-EXI) with angular momentum recoupling coefficient Lambda. | theoretical-proposal | theoretical derivation | printed p.212502-1--2, Fig. 1, Eq. (2) | true |
| GA22-2 | Outer-electron screening in excited configurations opens 100 new resonant K-shell capture channels in 73Ge at q=29+. | model-calculation | derived value | printed p.212502-2--3, Fig. 2 | true |
| GA22-3 | Resonance strength in 73Ge increases by >3 orders of magnitude (from 1.25e-4 b*eV under GSA to 0.518 b*eV under NEEC-EXI). | model-calculation | derived value | printed p.212502-3, Table I | true |
| GA22-4 | Evaluates 93Mo stopping: excited configurations allow L-shell vacancies at q=30-32, boosting rates by 2-3 orders of magnitude. | theoretical-extrapolation | model extrapolation | printed p.212502-4, lines 500--515 | true |

## Competing Interpretations and Limitations

NEEC-EXI establishes that out-of-equilibrium atomic states significantly enhance resonance strengths, but the magnitude of the macroscopic enhancement in a beam-foil experiment depends on the transient population of excited atomic states during ion stopping.

## Extracted Pages

- neec-exi
- 73ge
- mo93m

## 2026-11-27 — 馆藏原件与覆盖核对

- 物理第1–2页，正文的基态假设、激发态离子 NEEC、图1和式(1)–(2)。
- 物理第3–6页，⁷³Ge 计算结果、图2（第3页）、正文表 I（第4页）、⁹³Mo 讨论、结论及正文参考文献 [1]–[64]（第5–6页）。
- 物理第7–12页，补充材料内页1–6，共振强度推导、内转换系数缩放、波函数法、K 通道原子宽度及角动量重耦合，式(S1)–(S21)和图 S1（第11页）。
- 物理第13–15页，补充材料内页7–9，⁷³Ge 基态计算的补充表 I 和图 S2（第13页）、FAC 与 NIST 能级比较的图 S3（第14页）、激发态结果的图 S4（第15页）。
- 物理第16–17页，补充材料内页10–11，激光等离子体模型、补充表 II 和图 S5（第16页）、式(S22)–(S24)及补充参考文献 [1]–[26]（第17页）。
- 本次获取的具体覆盖：逐页审读物理第1–17页的提供文本，覆盖正文、补充材料及两套书目。图表审读限于抽取出的图注、表注与表格文字，原图和原公式排版未经目视核对。建议接受旧条目的同版归档匹配，整版深读覆盖待勘误并完成关键图表核对后再验收。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A22-1 | 激发态离子模型将初始电子组态纳入微观 NEEC 率。若俘获打破原有角动量耦合，共振强度还乘以重耦合概率 Λ。 | theoretical-derivation | source-reported | 正文物理第1页图1(c)图注、第2页式(1)–(2)及其说明。补充材料物理第10页式(S14)给出三个电子情形的重耦合概率。 | true |
| A22-2 | 对 ⁷³Ge 的 13.2845 keV 跃迁，模型在 q=29+ 至 32+ 内得到基态假设下的47条 L、M 通道。放宽该假设后得32,723条 L、M 通道及100条 K 通道。K 通道均出现在 q=29+，初态的 1s 仅占一个电子，屏蔽可使 K 俘获放能低于核跃迁能。正文所选通道的波函数法对照显示，共振强度峰值提高逾三个数量级。 | model-calculation | source-reported | 通道计数见物理第2页正文，补充总数见第15页图 S4 及其前文。物理第3页图2(a–b)及第4页正文表 I 的图示与数值列归属待目视核对。 | true |
| A22-3 | 论文引述文献 [11] 在2018年束流实验中报告的 ⁹³Mo 同核异能态退激信号，并指出该信号的 NEEC 解释及其与理论的差距仍有争议。实验数据的出处为被引文献。 | reported-observation | source-reported | 物理第1页引言、第4–5页讨论及第5页参考文献 [11]、[13]–[16]。 | true |
| A22-4 | 作者推测，若电子激发能在 ⁹³Mo 离子于碳靶减速时使 L 层空穴在 q<33+ 仍然存续，较低束流能量下可能出现额外的 L 层俘获通道。原文将差距缩小表述为可能性。 | theoretical-extrapolation | source-reported | 物理第4页表 I 后的 ⁹³Mo 停止讨论及第5页结论。 | true |

⁷³Ge 结果依赖 K 至 M 壳层的组态枚举、至多四个电子的重耦合方案、FAC 能级和波函数，以及内转换系数缩放或波函数法。近阈值 K 通道使用 XATOM 原子宽度，并在能量积分中保留微观率的变化。宏观激发率还取决于电子通量及各荷态和初始组态的占据与存续。相关方法见物理第2页及第7–12页，组态加权见第17页式(S24)。

- 将旧条目的5页正文加12页补充材料改为物理第1–6页正文及书目、第7–17页补充材料。将 212502-x 页码和旧行号改为归档物理页。GA22-2 定位到第2页正文、第3页图2和第15页图 S4。
- GA22-3 引物理第4页正文表 I。q=32+ 的 2p₃⁄₂ 基态允许通道中，1.25×10⁻⁴ b·eV 位于 WF 列，旧条目所称 GSA 的 ICC 缩放列对应 3.26×10⁻⁴ b·eV。q=29+、Eᵣ=0.18 eV 的 K 通道给出 WF 值 0.518 b·eV。按同一 WF 方法比较约为4.14×10³倍，列归属待核对该页原表。
- 将摘要及 GA22-4 的 q=30–32、10²–10³ 增益和距 1% 的说法替换为物理第4–5页讨论的 q<33+ 空穴存续假设。第4页所说的多个数量级增幅来自文献 [16] 对 L 通道部分概率的计算。该页称纳入荷态分布和空穴条件后，总概率仅小幅提高。
- 物理第6页参考文献 [38] 的补充材料网址仍为占位文字。Wiki 可用同一归档件的物理第7–17页定位内嵌补充材料。
