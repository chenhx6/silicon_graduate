---
type: source
title: "Tonev2007：134Pr详细实验表、动态手征解释与交叉失败"
aliases: [Tonev 2007 134Pr dynamic chirality, 134Pr PRC 76 044313]
created: 2026-10-27
updated: 2026-10-27
status: ai-draft
review_status: unreviewed
source_type: experimental-and-theoretical-paper
reading_depth: read
title_original: "Question of dynamic chirality in nuclei: The case of 134Pr"
authors: [D. Tonev, G. de Angelis, S. Brant, S. Frauendorf, P. Petkov, A. Dewald, F. Dönau, D. L. Balabanski, Q. Zhong, P. Pejovic, D. Bazzacco, P. Bednarczyk, F. Camera, D. Curien, F. Della Vedova, A. Fitzler, A. Gadea, G. Lo Bianco, S. Lenzi, S. Lunardi, N. Marginean, O. Möller, D. R. Napoli, R. Orlandi, E. Sahin, A. Saltarelli, J. Valiente Dobon, K. O. Zell, Jing-ye Zhang, Y. H. Zhang]
year: 2007
journal: Physical Review C
volume: 76
issue: 4
pages: "044313"
doi: 10.1103/PhysRevC.76.044313
canonical_source: https://doi.org/10.1103/PhysRevC.76.044313
citation_key: ""
raw_file: raw/papers/2007_Tonev_134Pr_Dynamic_Chirality.pdf
raw_sha256: 822780157dadbeac4adfa3cd34b919b855a3911c497c229b2216fb7697f1b8aa
raw_storage_status: public-staging-not-archived
actual_body_file: tmp/day24-tonev2007-134pr-long-095/10.1103_PhysRevC.76.044313.pdf
nuclei: [134Pr]
reactions: [119Sn-19F-4n-134Pr]
experiments: [euroball-iv-rdds-dsam-134Pr-2007]
models: [tqptr, ibffm, dynamic-chirality, shape-fluctuations]
methods: [recoil-distance, dsam, differential-decay-curve, compton-polarimetry, wave-function-analysis]
observables: [mean-lifetime, B(E2), B(M1), branching-ratio, linear-polarization, level-scheme]
tags: [134Pr-chirality, dynamic-chirality, shape-fluctuations, companion-matrix]
---


# 134Pr详细实验表与模型比较：形状涨落支持及未解交叉问题

## Bibliographic Record

D. Tonev等，Physical Review C 76, 044313 (2007)，DOI [10.1103/PhysRevC.76.044313](https://doi.org/10.1103/PhysRevC.76.044313)，received 2007-04-25，published 2007-10-17。现存VoR实测26页、1,527,111 bytes，SHA与frontmatter一致；印刷044313-1至26。原095下载命令/HTTP回执未找到，不以实物身份反推“APS直接下载”。098 APS入口返回403验证页，SI当前未核，不宣称无SI。raw_file为未归档预留路径，实际文件是actual_body_file，raw未修改。

## Scope and Reading Depth

098 worker逐页抽取全文，核主线及Table I/II、几何定义/模型比较/结论，并视觉复核表；root直接核PDF1/2/8/12/13/25及Table II图像。此为来源自审，不是human review、逐式重推或actual producer复现。历史095–097的过强摘要副本保于本run pre-correction-098，以下同ID为当前修订。

## Summary

本篇详细报告Tonev2006的同一组RDDS/DSAM实验，补列γ强度/偏振与EM表。所测134Pr这对带的EM不支持理想静态极限，作者比较TQPTR与含形状自由度的IBFFM：前者能谱/交叉好而EM失配，后者主要EM趋势较好但带间能隙过大且不能重现I=15交叉。作者提出弱涨落主导手征与尚待揭示的内禀对称性共同作用，属于受数据检验的解释，未唯一证明全部机制。

## Key Results

所有本轮claims保持needs_review:true。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| TO07-D24-001 | Table I给初末态/Eγ、实验和两模型强度、Pol与多极性；含空实验格、Seen、上限和仅理论行，不是所有线均有完整实测。39.3 keV由Ref38提供且本实验未见。 | measured-and-model-ledger-boundary | direct-original | physicalPDF9 TableI | true |
| TO07-D24-002 | Table II跨PDF12–14给τ、实验/IBFFM/TQPTR的B(E2)/B(M1)，实验τ覆盖B1 I10–18与B2 I13–17；空白非零，跨带ΔI1缺混合比分离。带内E2逐点见下表，旧固定数值范围撤回。 | experimental-EM-ledger-and-coverage | direct-original | physicalPDF12 TableII | true |
| TO07-D24-003 | Sec III C线偏振定性支持带内ΔI1以M1为主、带内/间ΔI2为E2，带间ΔI1为mixedM1+E2但统计不足定δ。原件没有交付逐线DCO数表，不能据其恢复实测E2混合份额。 | multipolarity-and-missing-delta | direct-original | physicalPDF8 SecIII-C | true |
| TO07-D24-004 | 几何算符/投影分布是模型波函数分析；TQPTR虽EM失配但能谱/交叉有支持。特殊γ30°/轴对称几何演示与微观惯量谱计算需分开，非实验直接角度分布。 | model-geometry-and-scope | model-result | physicalPDF17 SecV-C | true |
| TO07-D24-005 | IBFFM描述主要E2不对称/M1趋势，但低spin大E2、能隙/I15交叉和部分跨带率失败；p11依据本次数据调参，不能算无参holdout成功。 | support-and-model-failure | model-result | physicalPDF25 SecV-F | true |
| TO07-D24-006 | SecVI总结study suggests弱涨落主导手征，并保留intrinsic symmetry yet to be revealed；不等于唯一实验认证或全部静态模型被排尽。 | author-interpretation-and-open-mechanism | direct-original | physicalPDF25 SecVI | true |
| TO07-D24-007 | p2明确为Ref20即Tonev2006实验的详细报告。PE06的branch引用另源不证明事件/标定/Cov独立，也不构成两套独立τ或绝对B验证。 | shared-experiment-and-independence-boundary | direct-original-plus-cross-source | physicalPDF2 Introduction | true |
| TO07-D24-008 | 同spin带内E2的I14/15/16/17两带中央比为3.9231/1.6629/2.3000/2.2979；仅原Table II中央算术，无共同Cov、不作显著性/CI。 | task-table-arithmetic | declared-derived-not-new-measurement | physicalPDF13 TableII | true |

## 模型输入、带归属与高spin有效域

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| TO07-D24-009 | 谱学比较的TQPTR微观惯量比Js:Ji:Jl=1.52:3.55:1，总尺度按邻偶偶核2+能量定标；Figs8/9几何演示另用γ30°/轴对称、1:4:1与β约.2。IBFFM则依据当前数据调整H及EM参数，evib=1.2、boson gR=.15属所选模型输入，非Ce磁矩实测。 | distinct-model-input-and-calibration | direct-original-model-specification | physicalPDF11 SecV-A/B | true |
| TO07-D24-010 | 作者把Band1实验能量曲率变化解释为两额外准粒子对齐，指出I>16不再有两模型假定的2qp特征；这是作者配置解释，不能写成已直接数出准粒子。Fig15脚注还说明I15模型带归属按EM系统学交换、I14模型近简并混合使赋名有歧义；该选择后EM吻合不是独立holdout。 | author-configuration-and-calibration-boundary | direct-original-author-interpretation | physicalPDF23 SecV-F | true |

微观惯量谱计算、特殊几何演示、数据参与调参、作者提出的空间失效是四层不同合同。不能拿演示图的γ/惯量给谱学曲线补输入，也不能把超过所选空间的失配全部归因于形状/手征或以EM赋名后再独立计分。原程序/完整态和Cov仍未恢复。

## Table II：逐伙伴带内E2账本

以下B(E2)单位e²b²，均I→I−2；仅列所选实测格，不补理论列或空格。

|I|Band1 B(E2)|Band2 B(E2)|中央B1/B2|
|---|---|---|---|
|11|.268(33)|未给|—|
|12|.198(29)|未给|—|
|13|.151(27)|未给|—|
|14|.153(21)|.039(19)|3.9231|
|15|.148(21)|.089(20)|1.6629|
|16|.115(19)|.050(18)|2.3000|
|17|.108(22)|.047(17)|2.2979|
|18|.147(27)|未给|—|

Band1在PDF12、Band2的I14/15在PDF13、I16/17在PDF14。13₂→11₁的.0030(5)是跨带E2；13₂→11₂没有实验格，不能错当该带内值。“约2”或“2–3倍”是作者趋势概括，旧.15–.25/.05–.10不是精确包络。τ共享与branch/归一依赖存在，未按独立高斯传播误差制造CI。

## Competing Interpretations and Limitations

SecV-C的Eqs6–13及V-D/E、Figs8–13处理角动量几何/形状的模型分布；它们不是实验直接β/γ概率。IBFFM的γeff与β尺度依模型/EM拟合，不能反演为实测刚性或核形状涨落宽度。Figs15–17/Table II提供EM检验：TQPTR能谱/尖锐交叉可成功而EM失败；IBFFM的EM成功和交叉失败要一起保留。小相互作用不必然说明不同shape，原文p23对PE06推断也作限制。

p25明确保留17₂→15₁ E2和16₂→15₁ M1的失配，并指出能隙过大和I15交叉未重现。结论的weak fluctuation dominated chirality combined with an intrinsic symmetry yet to be revealed必须保留suggests量词和未知内禀对称性。对这对带静态极限的实质反证，不扩大为所有核/所有静态手征或刚性共存的无模型排除。

源自身文字冲突亦保留：p8 τ(15₂)印.897(47)，Table II为.887(47)；Fig15图面middle=IBFFM/bottom=TQPTR而caption次序相反，按图面/原表比对，不静默改原文。该图I15模型带身份相对2006有调整，不将两文当未变输入的独立复现。

## Knowledge Impact and Learning Decision

`supports`有界的EM反证和形状自由度解释，`revises`095–097“全面闭环/唯一物理实质/两独立数据”等强认证。新增逐点E2账本及真实失败项供[[chirality-shape-coexistence-companion-matrix]]复用，不为134Pr或133Ce补缺失δ、绝对跨带EM、signed核或Cov。

## Extracted Pages

- [[chirality-shape-coexistence-companion-matrix]]：逐核/逐pair竞争解释与缺项降级。
- [[tonev-2006-134pr-lifetime-chiral]]：同一实验短报，非第二次独立采集。
- [[petrache-2006-near-degenerate-chiral-misinterpretation]]：不同branch引用和两带混合假设，独立性不按书目计票。
