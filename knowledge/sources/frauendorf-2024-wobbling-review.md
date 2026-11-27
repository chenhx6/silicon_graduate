---
type: source
title: "Wobbling motion in triaxial nuclei"
aliases: []
created: 2026-07-01
updated: 2026-07-02
status: active
review_status: human-reviewed
source_type: review-preprint
reading_depth: deep-read
title_original: "Wobbling motion in triaxial nuclei"
authors: [S. Frauendorf]
journal: arXiv
year: 2024
volume:
pages: 26
doi: 10.48550/arXiv.2405.02747
arxiv: 2405.02747
language: en
canonical_source: arxiv:2405.02747
zotero_item_key: 3YFN5G2A
citation_key: frauendorf_2024_Wobblingmotion
zotero_uri: zotero://select/library/items/3YFN5G2A
library_file: "E:/zetore reference/高自旋/review/2024_Frauendorf_Wobbling motion in triaxial nuclei.pdf"
raw_file: "raw/papers/2024_Frauendorf_Wobbling motion in triaxial nuclei.pdf"
raw_sha256: C2B08136AF03B4544DE7FBFE5EA3D6677D1704E8C6E13772CB2F934DA554A6EA
nuclei: [163lu, 135pr, 133la, 131cs, 136nd, 151eu]
reactions: []
experiments: []
models: [triaxial-rotor-model, particle-rotor-model, random-phase-approximation, triaxial-projected-shell-model]
observables: [wobbling-energy, interband-e2-strengths, signature-splitting]
methods: [spin-coherent-state-map, spin-squeezed-state-map]
tags: [review, wobbling, transverse-wobbling, longitudinal-wobbling, gamma-softness]
---

# Frauendorf（2024）：三轴核 wobbling 综述

## Bibliographic Record

馆藏底本为 arXiv:2405.02747v1，共 26 个 PDF 页。首页 arXiv 边注为 2024-05-04，作者题头印 2024-05-07。分别保留两个日期及其位置。

同一作品收入 [[book-petrache-chirality-and-wobbling]] 第 2 章，DOI `10.1201/9781032691633-2`，书页 24–61（馆藏书 PDF 43–80）。引用章节时使用刊版页码与编号。已交叉核实 arXiv p. 8 Eqs. (18)–(19) 对应书 p. 34 Eqs. (2.18)–(2.19)，arXiv p. 20 的准粒子表述对应书 p. 52，arXiv Figs. 36–40 对应书 Figs. 2.36–2.40。下列原文异文在这三处刊版定位中仍存在。

## Scope and Reading Depth

原先对 arXiv 全文检索，精读导论、模型分类、正常形变核争议、软芯与结论，并视觉核对 Fig. 46。本轮补齐书籍版第 2 章书页 24–61，覆盖三轴转子、粒子耦合、近似方案、RPA、TPSM、软芯与参考文献。刊版结论按作者综述观点归属。回引的模型程序和原始实验依其各自来源核验。

## Summary

综述以三轴转子（TR）、粒子/准粒子-三轴转子（PTR/QTR）、RPA 和 TPSM 为主线，讨论强形变与正常形变核中的 wobbling，并用角动量进动锥拓扑区分 transverse wobbling（TW）、longitudinal wobbling（LW）和 flip mode（FM）。作者把相邻 wobbling-phonon 带之间集体增强的 E2 跃迁视为核心实验判据，同时系统讨论了 `135Pr` 等正常形变案例的 mixing ratio 争议。综述强调高 j 准粒子可稳定/改变三轴芯行为，TPSM 能在保留 γ-soft 邻核性质的同时再现 wobbling 特征。

## TPSM 图表的输入与文献谱系

- PDF 21–22 的 \(^{163}\mathrm{Lu}\) 算例采用 \(\epsilon=0.40\)、\(\gamma=15^\circ\)，配对隙 \(\Delta_n=0.7527\) MeV、\(\Delta_p=0.9637\) MeV。文中说明 \(\gamma\) 以实验 \(E_{\mathrm w}(21/2)\) 调整。该点属于模型输入约束。Figs. 36–39 的图注将结果连到书稿第 12 章，并鸣谢 G. Bhat 私人交流。刊版 Table 12.1 的 \(^{163}\mathrm{Lu}\) 列为 \((\epsilon,\epsilon',\gamma)=(0.400,0.100,14^\circ)\)，两处参数分别使用。实验点按原测量追溯。
- PDF 22 正文把 Fig. 40 的三核写作 \(N=74\)、\(Z=57,59,41\)，而 PDF 23 图注与图例列 \(^{131}\mathrm{Cs}\)、\(^{133}\mathrm{La}\)、\(^{135}\mathrm{Pr}\)，三者均为 \(N=76\)，对应 \(Z=55,57,59\)。可按图例识别三条曲线。[[sheikh-jehangir-bhat-2024-tpsm-wobbling]] 的刊版 Table 12.1（书 p. 243）按核素列出 \((\epsilon,\epsilon',\gamma)\) 为 \((0.140,0.100,36^\circ)\)、\((0.150,0.110,36^\circ)\)、\((0.160,0.100,32^\circ)\)。这是第 12 章的逐核参数，和综述所述共同 \(\epsilon'=0.10\) 有差别。Fig. 40 实际计算所用的逐核参数还需图源确认。

## 冻结顺排的轴编号与 RPA 组态

PDF 8 Eq. (18) 字面将 \(A_1\) 与被冻结分量 \(\hat J_3-j\) 配对，随后 Eq. (19) 和右栏按短轴 1 写 \(\bar A_1\)，并以 \(\hat J_2,\hat J_3\) 为横向分量。用 [[frauendorf-2014-transverse-wobbling]] PDF 6 Eqs. (11)–(15) 或明确写出物理短、中、长轴的形式复算。该综述的右栏同时声明，作者将 TW/LW 几何分类用于完整 PTR 结果，也用于能够作小振幅展开的部分自旋区间。

PDF 20 右栏将 Matsuzaki 等对 \(^{163,167}\mathrm{Lu}\) 的 \(i_{13/2}\) yrast 组态写作 one-quasineutron。Ref. [65] 原文 [[matsuzaki-2002-positive-gamma-wobbling-163lu]] 的指定组态和 Ref. [66] [[matsuzaki-2004-nuclear-inertia-and-wobbling]] PDF 17 Sec. III C.2 的 \((\pi i_{13/2})^1\) 均给单准质子。对照 Fig. 31 的顺排贡献时按质子组态追溯。

## 刊版的几何分类与惯量标度

书 p. 41 的分类表分别列出 \(\mathbf J\) 与 \(\mathbf j\) 的进动轴。LW 列按 \(\mathbf J\) 绕中轴分类，\(\mathbf j\) 的轴可为短轴、长轴或倾斜轴。TW 栏脚注明低自旋可以先升。表中的带间 E2 量级为作者的比较指示，须结合对应的波函数和实验线。书 p. 47 Eq. (2.29) 引述 Tanabe 模型采用的总体惯量标度 \(\mathcal J_0(I)=\mathcal J_0(I-0.60)/(I+23.5)\)。对固定惯量比，该标度可以改变频率斜率而保留轴排序，比较见 [[wobbling-geometry-phonon-observable-contract]]。

书 p. 39 的 \(^{133}\mathrm{Ba}\) 长轴空穴例子来自 [[rojeeta-devi-2021-multiphonon-transverse-wobbling-133ba]]，作者引用了该文的 HFA 分析。同章 Fig. 2.18（书 p. 40）展示 \(^{130}\mathrm{Ba}\) 的 SCS 图。\(^{133}\mathrm{Ba}\) 的谱学证据回到 Ref. [39] 核查。

## Experimental or Theoretical Setup

这是综合性理论与实验评述，不产生新实验数据。作者比较：

- triaxial rotor；
- particle/quasiparticle triaxial rotor；
- spin coherent/squeezed state 表示；
- microscopic RPA；
- TPSM；
- 多个已发表实验案例。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| F24-1 | 三轴转子的 wobbling 态可按相对 separatrix 的进动轨道拓扑分类，另有 flip-mode 区域。 | author-interpretation | direct | PDF pp.1-4, Figs.3-5 | false |
| F24-2 | 在冻结顺排例子中，TW 的粒子角动量与进动锥轴沿短轴或长轴，垂直于最大转动惯量的中轴。LW 的进动锥围绕最大惯量轴。作者以进动锥轴推广到粒子不牢固顺排的情形。 | model-result | direct | PDF p. 8, right column following discussion of Eq. (19); p. 25, Conclusions | false |
| F24-3 | wobbling 的核心实验信号是相邻 n+1 与 n wobbling bands 之间集体增强的 E2。 | author-interpretation | direct | PDF p.25, Conclusions | false |
| F24-4 | 高 j 准粒子存在时证据较清楚；TW 案例多于 LW，预期的 mid-shell high-j LW 尚未得到演示。 | author-interpretation | contextual | PDF p.25, Conclusions | false |
| F24-5 | TW 可在临界角动量处失稳，并通过 FM 转为 LW。 | model-result | direct | PDF pp.12-15, Fig.21; p.25 | false |
| F24-6 | RPA 是小振幅近似，适用于远离 TW instability 的区域；作者指出它尚未用于正常形变核。 | author-interpretation | direct | PDF p.26 | false |
| F24-7 | TPSM 能同时描述 wobbling、signature-partner 能量和带间跃迁，并缓解简单 PTR 对转动惯量选择的歧义，但从截断壳模型结果提取物理图像的工具仍需发展。 | author-interpretation | direct | PDF pp.22-26 | false |

## Nuclear Structure Information

该综述覆盖多个质量区和核素。对本 Wiki 当前最重要的是：

- 正常形变 A≈130 核的 TW/LW 与 signature-partner 争议；
- γ-soft 偶偶芯与奇 A wobbling 可以在 TPSM 中并存；
- `135Pr`、`133La`、`131Cs`、`136Nd` 等作为模型与判据案例。

## Authors' Interpretation

作者主张用进动锥拓扑而非仅凭 wobbling energy 的升降分类 TW/LW/FM；collective interband E2 是实验识别的关键。

## Model Results

- PTR 直观但依赖转动惯量选择；
- RPA 提供微观小振幅描述；
- TPSM 统一处理芯与价粒子，在多个案例中改善 PTR 对 signature-partner 与跃迁强度的描述。

## Competing Interpretations and Limitations

- 这是单一作者视角的综述，不是多个实验的独立证据；
- 正常形变核 mixing ratio 的实验提取仍存在争议；
- even-even γ-soft 核中的模式与简单刚性 TR wobbling 的关系仍未完全澄清；
- 综述中的“well established”应回溯到具体实验论文后再用于单核素结论。

## Extracted Pages

- Concepts: [[wobbling-motion]], [[transverse-wobbling]], [[longitudinal-wobbling]], [[flip-mode]], [[gamma-soft-deformation]], [[signature-partner-bands]]
- Models: [[triaxial-rotor-model]], [[particle-rotor-model]], [[random-phase-approximation]], [[triaxial-projected-shell-model]]
- Observables: [[wobbling-energy]], [[interband-e2-strengths]], [[signature-splitting]]
- Methods: [[spin-coherent-state-map]], [[spin-squeezed-state-map]]
- Synthesis: [[wobbling-vs-signature-partner]]

## Personal Notes

此文适合作为索引和术语地图；任何具体核素结论都应继续回到原始实验论文。

## Day22 checkpoint093：定义、有效域与表示的定向原件比较

本轮只定向查26页review的Fig.35/39引用背景、PDF p.14 Eqs.(26)–(27)与p.26结论；视觉核p.14的SSS公式。不将review的再引用算新实验，未读取其全部参考。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| F24-D22-R093-1 | 本文SSS表示按P(φ)=ΣKK′exp[−i(K−K′)φ]ρKK′/(2π)定义，由均匀K振幅的局域态(2I+1)^−1/2ΣK|IIK⟩绕3轴旋转生成。它是有限密度矩阵的一维角表示，不是以某个Bogoliubov r替代定义的惯量压缩本征态。较窄基底宽度不能直接当成测得的核γ刚度。 | method-definition-and-inference-boundary | direct-original-and-bounded-comparison | PDF p.14, Eqs.(26)–(27), Fig.24 and adjacent text | true |
| F24-D22-R093-2 | 结论将TPSM中高j准粒子情况下的wobbling与无该准粒子的γ-soft偶偶邻核性质并存视为可解释现象。这是模型/review判断，但已足以要求保留“邻核低spin γ-soft不自动排除奇A某spin模式”的迁移边界，不能由单个S(4)符号推出零恢复力。 | review-interpretation-and-transfer-boundary | direct-original-and-bounded-comparison | PDF p.26, first two paragraphs | true |

## Day22 checkpoint105：QRPA/scissors的量身份与公开伴随核验

本轮定向核现有raw PDF20–22，视觉核p21Figs34/35；另在公开CHORUS accepted manuscript中只读核Ref67（DOI10.1103/PhysRevC.92.064306），身份/版本/范围见outputs/literature-acquisition/20261025-day22-qrpa2015-public-readonly-audit.json。该新文件仅public staging，未正式建立新source摄入或写raw；不得称已归档VoR。现有本review原reading/review不升级。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| F24-D22-R105-1 | Fig35的纵轴标B(M1)out、单位μN²，而图注/邻文写B(M1)out/B(E2)in比值，量身份有不一致；不能直接把该图点当μN²/(e²b²)比值。公开Ref67acceptedPDF12Fig13图注也标绝对B(M1)out，支持先按原图量读取；本文不据此推全书绘图错误或重算原实验。 | plotted-observable-identity | direct-review-and-public-readonly-crosscheck | reviewPDF21Fig35ordinate/caption;Ref67acceptedPDF12Fig13 | true |
| F24-D22-R105-2 | Review讨论在QRPA加LL current-current interaction将wobbling与isovector scissors耦合：质子/中子系统反相进动，wobbling能量上移、M1低能出口受抑，E2比变化较小。这是作者引用的模型结果，不是新实验发现、所有核通用g淬火或弱M1即可确证wobbling。scissors集体相对振动与磁转动shears高j叶片随spin闭合不是相同物理对象。 | model-mechanism-and-transfer-boundary | direct-review | reviewPDF21Figs34/35andLLparagraph;PDF22scissorsdiscussion | true |
| F24-D22-R105-3 | Review的LL段把邻核写164Yb；Ref67公开acceptedPDF11/13却写162Yb，并说明无该核1+谱直接数据、以总M1系统学比较。此为转述对象/独立性需保留的差异，不把review叙述改报成已测该邻核scissors验证。原论文目前仅公开只读伴随，raw归档/正式新source摄入deferred；模型参数/原QRPA代码未重跑。 | citation-lineage-and-independence-audit | direct-review-and-provisional-public-crosscheck | reviewPDF21LLparagraph;Ref67acceptedPDF11neighborparagraph/PDF13conclusion | true |

## Day22 checkpoint107：TPSM图的“suppressed”须指定比较量

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| F24-D22-R107-1 | Fig37绿线标TSD3→TSD2、蓝线标TSD3→TSD1；前者非零且与TSD2→TSD1相对比可比，后者较弱。邻文的“n=2→1 suppressed”不能误读成该通道为零/严格禁戒；它可能是相对谐标度的语句，需先指定分母/比较量。Chapter12原稿Fig8/9与正文强调绝对TSD3→TSD2增强，不据一句话宣布TPSM已排除多声子。两图复用同一模型/资料谱系不增加独立实验，原spin轴/逐点输入未重建。 | figure-text-and-normalizer-boundary | direct-two-existing-originals | ReviewPDF22Fig37/text;SHJ24PDF15Figs8/9andPDF16–17discussion | true |

## Day22 checkpoint108：γ-soft与TPSM比较的真实层级

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| F24-D22-R108-1 | Review以TPSM同一输入再现134Ce的even-I-down交错和135Pr的wobbling趋势，主张配置混合可包含γ涨落；并比较phenomenologicalsoftcore/IBFM所得Ewob上升而与所采实验下降不同。后者精确IBFM能量由Nomura私人通信提供，非本任务公开producer重算。此为作者的模型比较/解释，不能将固定basisγ当绝对刚性或把γ-soft芯普适排除wobbling；也不是独立实验已裁决冲突δ。关于core–particle Pauli“not ensured”的批评须与NOM22实际exchange处理一起读，不改报所有模型完全无Pauli。 | competing-model-and-softness-boundary | direct-review-and-cross-sourcecomparison | ReviewPDF24–25Figs44/45andTPSMparagraph;NOM22PDF3–4Eq5/exchangeparagraph | true |

## 2026-11-27 — 源码包与刊版图件对照

arXiv:2405.02747 源包的 ¹³⁰Ba `130BaEwob.pdf` 和 `130BaSCS.pdf` 对应 Fig. 17/18（书 Fig. 2.17/2.18），共用 Ref. [40]，区分能量与角动量指向概率。¹³³La 的 Fig. 41（书 Fig. 2.41）用归一化 E2 比值图，未激活的 `133la_BE2_Intraband.pdf` 实为绝对强度图。Fig. 40（书 Fig. 2.40）的 ¹³¹Cs／¹³³La／¹³⁵Pr 对比取原 EPS，另有同图 PDF 转换件。具体文件哈希和 locator 见正式队列的 LIT-000193–000208。
